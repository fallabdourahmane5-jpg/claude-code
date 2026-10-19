# -*- coding: utf-8 -*-
"""Ensemble 6 — Les défaillances du marché et les limites de l’intervention
publique (1/4)."""

from doss_base import d

d('n6-externalites', 6, "Externalités positives et négatives",
  "Des effets sur autrui qui ne passent pas par le prix, dans les deux sens",
  "Une externalité est l’effet positif ou négatif de l’activité d’un agent "
  "économique sur un autre, sans compensation monétaire : une répercussion qui "
  "ne passe pas par le marché et n’est pas prise en compte dans le prix. "
  "L’externalité négative conduit à une surproduction et à un prix trop bas, "
  "l’externalité positive à une sous-production d’un bien pourtant "
  "socialement utile.",
  "Les externalités constituent la première des quatre défaillances de marché "
  "que le cours recense, et elles ont la particularité d’être symétriques : il "
  "faut traiter les deux sens, car la plupart des copies n’en retiennent qu’un. "
  "Le cas négatif d’abord. Une entreprise qui pollue impose des dommages à la "
  "population mais ne paie pas pour eux : il existe donc un coût externe, "
  "supporté par d’autres et ignoré dans ses décisions de production. "
  "Graphiquement, la courbe de coût marginal social se situe au-dessus de la "
  "courbe de coût marginal privé. Sans prise en compte de l’externalité, le "
  "prix d’équilibre est trop bas et la quantité trop élevée ; avec prise en "
  "compte du coût social, le prix est plus élevé et la quantité plus faible. La "
  "conclusion est nette : l’externalité négative conduit à une surproduction et "
  "à une sous-évaluation du prix, et le marché produit trop d’un bien "
  "socialement coûteux. Le cas positif ensuite, exactement symétrique : une "
  "activité crée un avantage pour d’autres sans être payée pour cela, l’exemple "
  "du cours étant la proximité d’une université pour un commerce. Il existe un "
  "gain réel pour la collectivité, mais il est gratuit, et le bien est donc "
  "insuffisamment produit. Les remèdes découlent directement de cette analyse "
  "et se répartissent en trois familles. Avec Pigou, on agit par les prix : "
  "taxe pigouvienne sur l’externalité négative selon le principe "
  "pollueur-payeur, subvention sur l’externalité positive pour rémunérer le "
  "bénéfice collectif créé. Avec Coase, on agit par les quantités et les droits "
  "de propriété échangeables. Avec la réglementation, on agit par les règles. "
  "Le cours ajoute une quatrième voie avec Ostrom, la gestion collective "
  "locale, et conclut qu’il n’existe pas de solution parfaite, seulement des "
  "arbitrages.",
  [("La divergence entre coût privé et coût social",
    "L’agent ne supporte qu’une partie des conséquences de sa décision : "
    "l’écart entre le coût marginal social et le coût marginal privé mesure "
    "exactement l’externalité, et c’est lui que la correction doit annuler."),
   ("La surproduction en cas d’externalité négative",
    "Comme l’entreprise ignore le coût qu’elle impose, elle produit trop et "
    "vend trop bon marché : l’équilibre s’établit à un prix inférieur et une "
    "quantité supérieure à l’optimum, d’où une perte de bien-être."),
   ("La sous-production en cas d’externalité positive",
    "Le producteur ne perçoit pas la valeur du bénéfice qu’il crée pour les "
    "autres : il arrête son activité avant le point socialement optimal, de "
    "sorte que la collectivité est privée d’un gain gratuit."),
   ("La correction par le prix",
    "La taxe relève le coût marginal privé jusqu’au coût social, le prix monte "
    "et la quantité baisse ; la subvention abaisse le coût, le prix baisse et "
    "la quantité augmente jusqu’à la production socialement optimale."),
   ("L’absence de solution parfaite",
    "Chaque remède a son défaut propre : mesure du dommage pour la taxe, coûts "
    "de transaction pour les droits de propriété, effet de seuil et "
    "contournement pour la norme, de sorte qu’on arbitre entre imperfections.")],
  [{'a': "La notion fournit un critère objectif d’intervention publique, "
         "fondé sur un prix faux plutôt que sur un jugement de valeur.",
    'cond': "Le critère suppose que l’écart entre coût privé et coût social "
            "puisse être estimé, ce que le cours identifie comme la "
            "difficulté principale de la taxation.",
    'lim': "Une estimation erronée du coût externe produit une correction mal "
           "calibrée, donc une inefficacité de sens opposé à celle que l’on "
           "voulait supprimer."},
   {'a': "Elle traite symétriquement les effets négatifs et positifs, ce qui "
         "justifie aussi bien la taxe que la subvention.",
    'cond': "La symétrie exige d’identifier un bénéfice collectif réel et non "
            "une simple externalité supposée.",
    'lim': "La subvention peut produire un effet d’aubaine, lorsque l’agent "
           "aurait adopté le même comportement en son absence : l’aide réduit "
           "alors le coût sans changer la décision."},
   {'a': "Elle se prête à plusieurs remèdes, ce qui permet d’adapter "
         "l’instrument aux caractéristiques du problème.",
    'cond': "L’adaptation suppose de connaître la mesurabilité du dommage, le "
            "nombre d’acteurs et le niveau des coûts de transaction.",
    'lim': "Le cours est explicite : il n’existe pas de solution parfaite, "
           "seulement des arbitrages, et il existe aussi des défaillances de "
           "l’État."},
   {'a': "Elle éclaire des enjeux contemporains majeurs, de la pollution "
         "locale jusqu’au réchauffement climatique mondial.",
    'cond': "La transposition au climat suppose de traiter l’atmosphère comme "
            "un bien commun mondial, ce que le cours fait explicitement.",
    'lim': "À cette échelle, le théorème de Coase ne s’applique plus : l’air, "
           "les océans et le climat sont précisément les biens pour lesquels "
           "attribuer des droits de propriété est le plus difficile."}],
  [{'t': "Le marché peut internaliser lui-même les externalités si les droits "
         "de propriété sont clairement définis.",
    'qui': "Ronald Coase, dont le théorème fonde l’action par les quantités.",
    'rep': "La solution ne vaut qu’à trois conditions strictes : coûts de "
           "transaction faibles, acteurs peu nombreux, droits faciles à "
           "définir, ce qui exclut les externalités diffuses."},
   {'t': "L’extension des droits de propriété peut créer de nouvelles "
         "inefficacités plutôt que de les corriger.",
    'qui': "Michael Heller, avec la tragédie des anti-communs.",
    'rep': "L’argument est décisif : à force de multiplier les brevets, chaque "
           "innovation exige royalties et autorisations multiples, de sorte "
           "que la recherche devient plus lente, plus coûteuse, parfois "
           "bloquée."},
   {'t': "L’intervention publique destinée à corriger une externalité peut "
         "être capturée par des intérêts privés.",
    'qui': "L’école des choix publics, dont le cours rapporte qu’elle "
           "dénonce des réglementations capturées par des intérêts privés.",
    'rep': "L’objection est sérieuse mais ne rétablit pas l’efficacité du "
           "marché : elle impose de comparer deux imperfections, celle du "
           "marché et celle de l’État, au lieu d’en supposer une parfaite."},
   {'t': "Ni le marché ni l’État ne sont nécessaires : les usagers peuvent "
         "s’organiser eux-mêmes.",
    'qui': "Elinor Ostrom, avec la gestion collective locale.",
    'rep': "Sa démonstration est empiriquement solide, mais le cours en "
           "signale la limite d’échelle : ses mécanismes s’appliquent "
           "difficilement aux biens communs mondiaux."}],
  [{'n': "Arthur Pigou",
    'i': "Il faut corriger les prix pour qu’ils reflètent le vrai coût ou le "
         "vrai bénéfice pour la société.",
    'p': "Le cours le présente comme successeur de Marshall et rival de "
         "Keynes, libéral mais fondateur de l’économie du bien-être : il "
         "soutient qu’il existe des situations où le marché est défaillant et "
         "où l’État est alors légitime pour intervenir."},
   {'n': "Arthur Pigou",
    'i': "Une externalité positive doit être subventionnée, et pas seulement "
         "une externalité négative taxée.",
    'p': "C’est un second apport, strictement symétrique du premier : la "
         "subvention rémunère le bénéfice collectif créé, ce qui abaisse le "
         "coût, fait baisser le prix et augmenter la quantité jusqu’à la "
         "production socialement optimale."},
   {'n': "Ronald Coase",
    'i': "Les externalités peuvent être résolues par le marché si des droits "
         "de propriété clairement définis sont attribués.",
    'p': "Sa condition est explicite : il faut que les coûts de transaction "
         "soient faibles, que les acteurs ne soient pas trop nombreux et que "
         "les droits soient faciles à définir. La solution fonctionne pour les "
         "ressources localisées, non pour l’air ou le climat."},
   {'n': "Elinor Ostrom",
    'i': "Une troisième voie existe entre le marché et l’État : la gestion "
         "collective par des communautés locales.",
    'p': "Le cours la situe dans un tableau comparatif : Hardin pour la "
         "privatisation ou l’État, Pigou pour l’intervention publique par "
         "taxes et réglementation, Coase pour les droits de propriété et le "
         "marché, Ostrom pour l’auto-organisation."}],
  [{'f': "Le cours définit l’externalité comme une répercussion de l’activité "
         "d’un agent économique sur un autre qui ne passe pas par le marché et "
         "qui n’est pas prise en compte dans le prix.",
    'p': "La définition désigne la cause de la défaillance — l’absence de prix "
         "— et donc le remède, la correction du prix."},
   {'f': "Sans prise en compte de l’externalité négative, le prix est trop bas "
         "et la quantité trop élevée ; avec prise en compte du coût social, le "
         "prix est plus élevé et la quantité plus faible.",
    'p': "Le résultat graphique permet de démontrer la surproduction au lieu "
         "de l’affirmer, ce qui est indispensable dans un sujet de "
         "microéconomie."},
   {'f': "L’exemple d’externalité positive donné par le cours est la proximité "
         "d’une université pour un commerce : il existe un gain réel pour la "
         "collectivité, mais il est gratuit.",
    'p': "L’exemple montre que l’externalité positive est aussi une "
         "défaillance : la gratuité du bénéfice conduit à sous-produire une "
         "activité socialement utile."},
   {'f': "Le cours conclut qu’il n’existe pas de solution parfaite, seulement "
         "des arbitrages, puisqu’il existe aussi des défaillances de l’État, "
         "du lobbying, des effets pervers et des problèmes d’acceptabilité "
         "politique.",
    'p': "La conclusion interdit de présenter l’intervention publique comme la "
         "réponse évidente et fournit la transition vers les défaillances de "
         "l’État."}],
  [{'q': "Sujet du type « Le marché conduit-il à une allocation efficace des "
         "ressources ? »",
    'f': "L’externalité constitue le contre-exemple le plus net, car elle "
         "n’exige aucune hypothèse sur le comportement des agents. Puisqu’elle "
         "est une répercussion qui ne passe pas par le marché et n’est pas "
         "prise en compte dans le prix, l’entreprise ignore le coût social de "
         "la pollution : elle produit trop et vend trop bon marché, et "
         "l’équilibre de marché est inefficace. Le raisonnement symétrique "
         "vaut pour l’externalité positive, bénéfice réel mais gratuit, donc "
         "insuffisamment produit.",
    'r': "Le raisonnement établit l’inefficacité sans invoquer ni pouvoir de "
         "marché ni irrationalité, ce qui le rend valable même dans le cadre "
         "le plus favorable au marché.",
    'ex': "La proximité d’une université pour un commerce, gain collectif réel "
          "mais non rémunéré."},
   {'q': "Sujet du type « Comment corriger une défaillance de marché ? »",
    'f': "Le cours énumère trois familles de solutions dont aucune n’est "
         "universellement supérieure : l’action par les règles, avec normes et "
         "interdictions ; l’action par les prix avec Pigou, taxe sur "
         "l’externalité négative et subvention sur l’externalité positive ; "
         "l’action par les quantités avec Coase, quotas et droits de propriété "
         "échangeables. Il ajoute la gestion collective locale d’Ostrom, et "
         "conclut qu’il n’existe pas de solution parfaite, seulement des "
         "arbitrages.",
    'r': "Le raisonnement remplace la recherche du bon instrument par une "
         "comparaison d’imperfections, ce qui est la seule manière honnête de "
         "conclure sur ce type de sujet.",
    'ex': "Le tableau du cours opposant les solutions de Hardin, Pigou, Coase "
          "et Ostrom."}],
  voisins=['n6-biens-collectifs', 'n6-taxation', 'n6-reglementation',
           'n6-defaillances-etat'])


d('n6-biens-collectifs', 6, "Biens collectifs",
  "Ni rivaux ni excluables : le marché ne les produit pas du tout",
  "Les biens collectifs purs sont des biens non rivaux et non excluables : on "
  "ne peut empêcher personne de consommer, et la consommation de l’un ne gêne "
  "pas celle des autres. Faute de pouvoir faire payer les utilisateurs, aucun "
  "producteur privé ne peut rentabiliser la production : le résultat est une "
  "sous-production, voire une absence totale de production, alors même que le "
  "bien est socialement utile.",
  "Le bien collectif est la défaillance de marché la plus radicale, car elle ne "
  "produit pas une mauvaise allocation mais l’absence de marché. Son "
  "identification repose sur la typologie construite à partir de deux critères "
  "indépendants. La rivalité répond à la question de savoir si la consommation "
  "par un individu empêche celle des autres ; l’excluabilité à celle de savoir "
  "si l’on peut empêcher quelqu’un de consommer s’il ne paie pas. Le bien "
  "collectif pur cumule les deux réponses négatives, et le cours en donne les "
  "exemples canoniques : défense nationale, éclairage public, sécurité, air "
  "pur. Le mécanisme de la défaillance est celui du passager clandestin, "
  "analysé par Mancur Olson. Chaque individu raisonne ainsi : je peux "
  "bénéficier du bien même si je ne paie pas. Le cours l’illustre par le "
  "phare : chaque bateau veut bénéficier de la lumière, aucun n’a intérêt à "
  "payer volontairement puisqu’il en profitera de toute façon, et "
  "contrairement à l’autoroute à péage il n’existe aucun moyen technique de "
  "contrôler qui paie pour la lumière. Résultat : personne ne finance, "
  "personne ne produit, le bien n’existe pas. Une entreprise privée n’a donc "
  "aucun intérêt à produire un bien collectif pur. La solution est "
  "l’intervention de l’État, par un financement par l’impôt et une production "
  "publique ou une commande publique. Le cours ajoute une notion précieuse, "
  "celle de bien tutélaire chez Musgrave : des biens institutionnellement pris "
  "en charge par l’État, mis à disposition de la population quasi gratuitement "
  "et financés par l’impôt. Deux prolongements complètent le dossier. D’une "
  "part la monnaie, que le cours analyse comme à la fois bien public et bien "
  "privé, génératrice d’externalités positives puisqu’elle profite à toute la "
  "société. D’autre part la question politique que soulève l’école des choix "
  "publics : qui décide qu’un bien doit devenir public ?",
  [("Le cumul de la non-rivalité et de la non-excluabilité",
    "La consommation de l’un n’empêche pas celle des autres et nul ne peut "
    "être écarté : ces deux propriétés ensemble suppriment à la fois la rareté "
    "perçue et la possibilité de faire payer."),
   ("L’impossibilité de faire payer",
    "Faute d’excluabilité, l’entreprise ne peut conditionner l’accès au "
    "paiement : le prix cesse de jouer son rôle d’allocation, et l’activité "
    "devient non rentabilisable pour un producteur privé."),
   ("Le comportement de passager clandestin",
    "Chaque agent raisonne en se disant qu’il bénéficiera du bien même sans "
    "payer : la somme de ces calculs rationnels aboutit à ce que personne ne "
    "finance et donc à ce que le bien n’existe pas."),
   ("La sous-production comme résultat",
    "Le bien est désirable collectivement mais impossible à produire par le "
    "marché : l’allocation est sous-optimale non par excès mais par défaut, "
    "ce qui distingue le bien collectif du bien commun."),
   ("Le financement par l’impôt",
    "L’État résout le problème en rendant la contribution obligatoire : "
    "l’impôt supprime la possibilité du passager clandestin, et la production "
    "peut être publique ou confiée par commande publique.")],
  [{'a': "La notion fournit une justification rigoureuse de l’État "
         "producteur, fondée sur une propriété technique des biens et non sur "
         "une préférence politique.",
    'cond': "La justification suppose que le bien soit effectivement non "
            "excluable, ce qui est une question technique susceptible "
            "d’évoluer.",
    'lim': "Le statut d’un bien n’est pas figé : le progrès technique peut "
           "créer l’excluabilité, comme l’illustre le passage du puits "
           "collectif au compteur individuel pour l’eau."},
   {'a': "Elle explique l’existence historique de services publics que le "
         "marché n’a jamais pris en charge.",
    'cond': "L’explication vaut pour les biens collectifs purs, et doit être "
            "distinguée des monopoles d’institution créés par la loi.",
    'lim': "Beaucoup de services publics réels ne sont pas des biens "
           "collectifs purs : ils sont excluables et leur prise en charge "
           "relève d’un choix politique, non d’une nécessité technique."},
   {'a': "Elle se complète utilement par la notion de bien tutélaire, qui "
         "rend compte des biens mis à disposition quasi gratuitement.",
    'cond': "La notion suppose que la collectivité juge la consommation du "
            "bien souhaitable indépendamment de la demande exprimée.",
    'lim': "Ce jugement est précisément ce que l’école des choix publics "
           "conteste en demandant qui décide qu’un bien doit devenir public."},
   {'a': "Elle éclaire l’analyse de la monnaie, qui produit des externalités "
         "positives en facilitant les échanges de tous les agents.",
    'cond': "L’argument vaut pour la monnaie comme institution, non pour les "
            "encaisses individuelles qui sont, elles, rivales et "
            "appropriables.",
    'lim': "Le cours souligne cette dualité : la monnaie est à la fois un bien "
           "public, car elle profite à toute la société, et un bien privé, car "
           "chacun en possède et l’utilise pour son intérêt personnel."}],
  [{'t': "La décision de rendre un bien public est une décision politique et "
         "non le constat d’une propriété technique.",
    'qui': "L’école des choix publics, qui demande qui décide qu’un bien doit "
           "devenir public et pourquoi l’État plutôt que la population.",
    'rep': "L’objection est forte et le cours l’illustre par le débat sur les "
           "vaccins pendant la crise du Covid : bien privé ou bien public, la "
           "réponse n’est pas donnée par les propriétés du bien."},
   {'t': "La production publique souffre de défauts propres qui peuvent "
         "excéder le gain obtenu.",
    'qui': "La critique des monopoles d’institution que le cours formule.",
    'rep': "Les limites sont réelles — manque d’efficacité, absence de "
           "concurrence donc pas forcément d’innovation, risques de "
           "bureaucratie, défaillance de l’État — mais elles ne rétablissent "
           "pas la possibilité d’une production privée du bien collectif pur."},
   {'t': "Le statut de bien collectif n’est pas une donnée naturelle mais "
         "dépend de la technologie disponible.",
    'qui': "Le constat du cours selon lequel un bien peut changer de catégorie "
           "sous l’effet de la technologie, des règles ou de décisions "
           "politiques.",
    'rep': "L’objection est exacte et féconde : elle montre que l’innovation "
           "peut déplacer la frontière du marché, comme l’illustre "
           "l’individualisation des compteurs d’eau."},
   {'t': "Le problème n’est pas la production mais le financement : il "
         "suffirait d’une contribution volontaire bien organisée.",
    'qui': "Une lecture optimiste de l’action collective.",
    'rep': "Olson montre le contraire : chaque agent raisonne en se demandant "
           "pourquoi il paierait puisque les autres en profiteront aussi, de "
           "sorte que personne ne finance et que le bien n’existe pas."}],
  [{'n': "Mancur Olson",
    'i': "Un passager clandestin est quelqu’un qui consomme un bien sans "
         "vouloir participer à son financement.",
    'p': "Le cours développe sa notion de free rider avec l’exemple du "
         "phare : chaque bateau veut la lumière, aucun n’a intérêt à payer "
         "volontairement, de sorte que personne ne finance, personne ne "
         "produit, et le bien n’existe pas."},
   {'n': "Richard Musgrave",
    'i': "Certains biens sont tutélaires : institutionnellement pris en charge "
         "par l’État.",
    'p': "Le cours précise la définition : des biens que l’État met à "
         "disposition de la population quasi gratuitement, financés par "
         "l’impôt. La notion complète celle de bien collectif, car un bien "
         "tutélaire peut être excluable mais jugé socialement nécessaire."},
   {'n': "Arthur Pigou",
    'i': "L’État est légitime pour intervenir lorsque le marché est "
         "défaillant.",
    'p': "Son économie du bien-être fournit le cadre général : analyser le "
         "bien-être consiste à chercher la situation qui maximise l’utilité "
         "collective, ce qui justifie la production publique des biens que le "
         "marché ne produit pas."},
   {'n': "James Buchanan",
    'i': "L’État n’incarne pas automatiquement l’intérêt général : il est une "
         "somme d’intérêts individuels.",
    'p': "Prix Nobel 1986 et principal auteur de l’école des choix publics, il "
         "fournit l’objection décisive : la décision de rendre un bien public "
         "est prise par des acteurs rationnels poursuivant leurs propres "
         "objectifs, notamment la réélection."}],
  [{'f': "Les exemples de biens collectifs purs donnés par le cours sont la "
         "défense nationale, l’éclairage public, la sécurité et l’air pur.",
    'p': "L’énumération montre que ces biens relèvent souvent des fonctions "
         "régaliennes, ce qui explique leur prise en charge publique "
         "historique."},
   {'f': "Contrairement à l’autoroute à péage, il n’existe aucun moyen "
         "technique de contrôler qui paie pour la lumière d’un phare.",
    'p': "La comparaison isole exactement la variable décisive : ce n’est pas "
         "l’utilité du bien qui change mais la possibilité technique "
         "d’exclure."},
   {'f': "Le cours résume la défaillance en une phrase : les biens collectifs "
         "et les biens communs constituent des défaillances de marché car la "
         "non-excluabilité empêche le système de prix de jouer son rôle.",
    'p': "La formule relie les deux cas à une même cause tout en distinguant "
         "leurs effets, sous-production d’un côté, surexploitation de "
         "l’autre."},
   {'f': "En tant que bien public, la monnaie génère des externalités "
         "positives : en permettant le commerce, elle stimule la production, "
         "la consommation et la croissance.",
    'p': "Le cas montre qu’un bien collectif peut être une institution et non "
         "un objet, et que sa valeur réside dans l’usage qu’en font tous les "
         "agents simultanément."}],
  [{'q': "Sujet du type « Pourquoi l’État produit-il certains biens ? »",
    'f': "La réponse tient à une propriété technique et non à un choix "
         "politique. Les biens collectifs purs sont non rivaux et non "
         "excluables : à cause de la non-excluabilité, il est impossible de "
         "faire payer les utilisateurs, chaque agent raisonnant en se disant "
         "qu’il peut bénéficier du bien même sans payer. Aucun producteur "
         "privé ne peut donc rentabiliser la production, et la solution est "
         "l’intervention de l’État, par un financement par l’impôt et une "
         "production ou une commande publique.",
    'r': "Le raisonnement fonde l’intervention sur une impossibilité "
         "technique, ce qui la rend beaucoup plus difficile à contester qu’un "
         "argument d’équité ou de préférence collective.",
    'ex': "Le phare, dont aucune entreprise privée n’a intérêt à financer la "
          "construction puisqu’elle ne peut faire payer les bateaux."},
   {'q': "Sujet du type « Qui décide de ce qui doit être public ? »",
    'f': "La typologie des biens ne suffit pas à trancher, et c’est là que "
         "l’école des choix publics porte sa critique la plus incisive : qui "
         "décide qu’un bien doit devenir public, et pourquoi l’État plutôt que "
         "la population ? Le cours souligne d’ailleurs que le statut d’un bien "
         "n’est pas figé et qu’il peut changer sous l’effet de la technologie, "
         "des règles institutionnelles ou de décisions politiques.",
    'r': "Le raisonnement montre que la frontière entre public et privé est "
         "construite et révisable, ce qui transforme une question de "
         "classification en question de décision collective.",
    'ex': "Le débat sur le vaccin contre le Covid : bien privé ou bien "
          "commun ?"}],
  voisins=['n6-passager-clandestin', 'n6-externalites', 'n6-choix-publics',
           'n4-communs'])


d('n6-passager-clandestin', 6, "Passager clandestin",
  "Profiter d’un bien sans contribuer à son financement",
  "Le passager clandestin, ou free rider, est celui qui consomme un bien sans "
  "vouloir participer à son financement. Analysé par Mancur Olson, ce "
  "comportement rationnel conduit à ce que personne ne finance un bien "
  "pourtant utile à tous : il explique la sous-production des biens "
  "collectifs et, à l’échelle internationale, le blocage de la coopération "
  "entre États.",
  "Le passager clandestin est le mécanisme le plus transversal du programme, "
  "puisqu’on le retrouve en microéconomie, en sociologie et en économie "
  "internationale. Sa formulation microéconomique est celle du cours sur les "
  "défaillances : à cause de la non-excluabilité, il est impossible de faire "
  "payer les utilisateurs, et chaque individu raisonne ainsi — je peux "
  "bénéficier du bien même si je ne paie pas. L’exemple du phare est "
  "transparent : chaque bateau veut bénéficier de la lumière, mais aucun n’a "
  "intérêt à payer volontairement, car même sans payer il en profitera. "
  "Résultat : personne ne finance, personne ne produit, le bien n’existe pas. "
  "La conséquence est l’impossibilité de production privée, puisqu’une "
  "entreprise n’a aucun intérêt à produire un bien dont elle ne peut "
  "contrôler l’accès. Sa formulation sociologique est le paradoxe de l’action "
  "collective, que le cours mobilise à propos du syndicalisme : un individu "
  "peut bénéficier des avantages obtenus par une mobilisation collective sans "
  "y participer lui-même, et il peut donc avoir intérêt à laisser les autres "
  "supporter le coût de l’action collective. Le cours en tire une explication "
  "de la baisse de l’engagement syndical, la montée de l’individualisme "
  "fragilisant la mobilisation. Sa formulation internationale enfin, et c’est "
  "celle qui a le plus de portée : les biens publics mondiaux — stabilité "
  "financière, stabilité du commerce international, règles commerciales "
  "équitables — rencontrent un problème classique d’action collective. Sans "
  "coordination internationale, chaque État a intérêt à laisser les autres "
  "supporter le coût, d’où un comportement de passager clandestin et un "
  "équilibre de Nash sous-optimal. La gouvernance mondiale trouve précisément "
  "là sa justification : établir des règles de bonne conduite afin de "
  "coordonner les comportements nationaux. Le climat relève exactement de "
  "cette logique.",
  [("La non-excluabilité comme condition",
    "Le comportement n’est possible que si l’on ne peut pas être écarté du "
    "bénéfice : c’est l’impossibilité technique d’exclure, et non une "
    "disposition morale, qui engendre le passager clandestin."),
   ("Le calcul individuel",
    "Chacun raisonne en se demandant pourquoi il paierait puisque les autres "
    "en profiteront aussi : le raisonnement est parfaitement rationnel, ce qui "
    "explique sa généralité."),
   ("L’agrégation défavorable",
    "Si tous raisonnent ainsi, personne ne finance et le bien n’existe pas : "
    "le résultat collectif est pire que celui qu’aucun agent ne souhaitait, "
    "sans qu’aucun se soit comporté de façon irrationnelle."),
   ("L’impossibilité de production privée",
    "Une entreprise ne peut rentabiliser un bien dont elle ne contrôle pas "
    "l’accès : le marché n’échoue pas à bien allouer, il échoue à exister, ce "
    "qui appelle une contribution obligatoire."),
   ("La transposition aux États",
    "Entre pays, le même mécanisme produit un équilibre de Nash sous-optimal : "
    "chaque État préfère que les autres supportent le coût du bien public "
    "mondial, d’où la nécessité de règles coordonnées.")],
  [{'a': "Le mécanisme explique la sous-production des biens collectifs sans "
         "supposer ni égoïsme particulier ni irrationalité.",
    'cond': "Il suppose que les contributeurs soient suffisamment nombreux "
            "pour que l’abstention de l’un reste imperceptible.",
    'lim': "Dans un petit groupe où chacun est identifiable, la pression "
           "sociale peut suffire à obtenir la contribution, comme le montrent "
           "les travaux d’Ostrom sur les communautés d’usagers."},
   {'a': "Il justifie l’impôt comme mode de financement, puisqu’il rend la "
         "contribution obligatoire.",
    'cond': "L’argument suppose que le bien soit effectivement collectif, "
            "faute de quoi l’impôt finance ce que le marché aurait produit.",
    'lim': "Il ne dit rien du niveau souhaitable de production, que la "
           "décision politique doit fixer, ce que l’école des choix publics "
           "conteste précisément."},
   {'a': "Il s’applique à des domaines très différents, de la production de "
         "biens publics au syndicalisme et à la coopération internationale.",
    'cond': "La transposition suppose que l’avantage soit effectivement "
            "accessible sans contribution, ce qui vaut pour une convention "
            "collective comme pour la stabilité climatique.",
    'lim': "La généralité du mécanisme peut masquer les différences de "
           "contexte : les remèdes applicables à un phare ne valent pas pour "
           "le climat."},
   {'a': "Il fournit la justification économique de la gouvernance mondiale, "
         "qui établit des règles pour coordonner les comportements nationaux.",
    'cond': "La coordination suppose que les États perçoivent un gain commun "
            "supérieur au coût de leur contribution.",
    'lim': "Aucune autorité supranationale ne peut imposer la contribution, de "
           "sorte que la coopération reste fondée sur des engagements que "
           "chacun peut rompre."}],
  [{'t': "Le passager clandestin n’est pas une fatalité : des communautés "
         "parviennent à organiser la contribution.",
    'qui': "Elinor Ostrom, pour qui la coopération est possible et les "
           "individus ne sont pas seulement égoïstes.",
    'rep': "La démonstration est empirique et solide, mais elle repose sur "
           "l’interconnaissance et la surveillance mutuelle, conditions "
           "absentes à grande échelle."},
   {'t': "Le même mécanisme peut produire la surexploitation et non seulement "
         "la sous-production.",
    'qui': "Garrett Hardin, avec la tragédie des communs.",
    'rep': "L’observation est juste et le cours la formule : la "
           "non-excluabilité conduit soit à des comportements de passager "
           "clandestin et à une sous-production, soit à une surexploitation "
           "des ressources, selon que le bien est rival ou non."},
   {'t': "La contribution peut être obtenue par des incitations sélectives "
         "plutôt que par la contrainte.",
    'qui': "La logique de l’action collective qu’Olson applique aux "
           "organisations.",
    'rep': "L’idée est cohérente avec son analyse : si le bien collectif ne "
           "suffit pas à motiver, il faut y adjoindre des avantages réservés "
           "aux contributeurs, ce qui restaure une forme d’excluabilité."},
   {'t': "Le problème se résout par la coordination internationale plutôt que "
         "par la contrainte nationale.",
    'qui': "L’analyse des biens publics mondiaux que le cours développe.",
    'rep': "La coordination est nécessaire mais fragile : elle produit des "
           "règles de bonne conduite sans mécanisme de sanction comparable à "
           "celui de l’impôt."}],
  [{'n': "Mancur Olson",
    'i': "Un free rider est quelqu’un qui consomme un bien sans vouloir "
         "participer à son financement.",
    'p': "Le cours en fait l’auteur central de la notion et l’illustre par le "
         "phare : chaque bateau veut la lumière, aucun n’a intérêt à payer "
         "volontairement, de sorte que personne ne finance et que le bien "
         "n’existe pas, d’où l’impossibilité d’une production privée."},
   {'n': "Mancur Olson",
    'i': "Le paradoxe de l’action collective explique qu’on puisse bénéficier "
         "d’une mobilisation sans y participer.",
    'p': "C’est un second apport, que le cours mobilise pour le syndicalisme : "
         "un individu peut bénéficier des avantages obtenus par une "
         "mobilisation collective sans y participer, et avoir intérêt à "
         "laisser les autres en supporter le coût, ce qui fragilise "
         "l’engagement."},
   {'n': "Garrett Hardin",
    'i': "Sans régulation, un bien commun mondial tend à être surexploité.",
    'p': "Le cours applique son mécanisme au climat : sans coordination "
         "internationale apparaissent des comportements de passager "
         "clandestin, un sous-investissement collectif et une surexploitation "
         "des ressources planétaires."},
   {'n': "Elinor Ostrom",
    'i': "Des communautés locales parviennent à organiser la contribution sans "
         "marché ni État.",
    'p': "Son apport conteste le caractère inéluctable du passager "
         "clandestin : les individus ne sont pas seulement égoïstes, les "
         "institutions locales sont efficaces, et la microéconomie doit "
         "intégrer les normes sociales."}],
  [{'f': "Le cours formule le calcul du passager clandestin ainsi : pourquoi "
         "est-ce que je paierais, puisque les autres vont en profiter aussi ?",
    'p': "La formulation à la première personne rend immédiatement "
         "intelligible le caractère rationnel du comportement, ce qui est "
         "l’essentiel de la démonstration."},
   {'f': "Le cours énumère comme biens publics mondiaux la stabilité "
         "financière, la stabilité du commerce international et l’existence de "
         "règles commerciales équitables.",
    'p': "La liste montre que les biens publics mondiaux ne sont pas seulement "
         "environnementaux et que la gouvernance économique internationale "
         "relève du même problème."},
   {'f': "Sans coordination internationale, chaque État a intérêt à laisser "
         "les autres supporter le coût, ce qui conduit à un équilibre de Nash "
         "sous-optimal.",
    'p': "La référence à l’équilibre de Nash montre que le résultat est "
         "stable : il ne s’agit pas d’un accident mais d’une configuration que "
         "personne n’a intérêt à quitter unilatéralement."},
   {'f': "Le cours relie la montée de l’individualisme au paradoxe de l’action "
         "collective pour expliquer la fragilisation de l’engagement syndical, "
         "notamment chez les jeunes.",
    'p': "L’application sociologique montre la portée du mécanisme hors de la "
         "production de biens, dans l’analyse des organisations collectives."}],
  [{'q': "Sujet du type « L’action collective est-elle possible ? »",
    'f': "Le paradoxe d’Olson en montre la difficulté structurelle : un "
         "individu peut bénéficier des avantages obtenus par une mobilisation "
         "collective sans y participer lui-même, et il peut donc avoir intérêt "
         "à laisser les autres supporter le coût de l’action collective. Le "
         "cours en tire une explication de la fragilisation de l’engagement "
         "syndical, la montée de l’individualisme conduisant les individus à "
         "souhaiter profiter des résultats sans en supporter le coût.",
    'r': "Le raisonnement montre que l’obstacle à l’action collective n’est "
         "pas le désintérêt pour le but poursuivi mais la structure des "
         "incitations, ce qui déplace la question vers les dispositifs de "
         "mobilisation.",
    'ex': "Une convention collective dont bénéficient tous les salariés, "
          "syndiqués ou non."},
   {'q': "Sujet du type « Pourquoi la coopération internationale est-elle si "
         "difficile ? »",
    'f': "Les biens publics mondiaux rencontrent un problème classique "
         "d’action collective : sans coordination internationale, chaque État "
         "a intérêt à laisser les autres supporter le coût, d’où un "
         "comportement de passager clandestin et un équilibre de Nash "
         "sous-optimal. La gouvernance mondiale trouve précisément là sa "
         "justification, puisqu’elle permet d’établir des règles de bonne "
         "conduite afin de coordonner les comportements nationaux.",
    'r': "Le raisonnement montre que l’échec de la coopération est un "
         "équilibre et non un dysfonctionnement, ce qui explique sa "
         "persistance malgré l’accord de tous sur l’objectif.",
    'ex': "Le climat, bien commun mondial que le cours analyse par la logique "
          "du passager clandestin à l’échelle de la planète."}],
  voisins=['n6-biens-collectifs', 'n4-tragedie', 'n6-coordination',
           'n4-communs'])


d('n6-asymetries', 6, "Asymétries d’information",
  "Quand un agent sait ce que l’autre ignore, l’échange se dégrade",
  "Il y a asymétrie d’information lorsque, dans un échange ou un contrat, un "
  "agent possède plus d’informations que l’autre. Tous les agents ne disposent "
  "alors pas de la même information, l’échange est biaisé et le marché ne "
  "fonctionne plus correctement. Le cours en fait une défaillance de marché "
  "identifiée dans les années 1970, dont l’auteur principal est George "
  "Akerlof.",
  "L’asymétrie d’information est la défaillance la plus subtile du programme, "
  "car elle ne tient ni à la nature du bien ni à la structure du marché mais à "
  "la distribution de la connaissance. Le cours insiste sur un point décisif : "
  "la théorie néoclassique suppose une information parfaite, gratuite et "
  "symétrique entre tous les agents — c’est la transparence de l’information — "
  "mais dans la réalité c’est l’inverse qui domine, et l’asymétrie n’est pas "
  "une exception mais la situation normale des marchés. L’analyse fondatrice "
  "est celle d’Akerlof dans The Market for Lemons (1970) : sur le marché des "
  "voitures d’occasion, le vendeur sait si sa voiture est bonne ou mauvaise, "
  "l’acheteur ne le sait pas ; l’acheteur propose donc un prix moyen, ce prix "
  "est trop bas pour les bonnes voitures, les vendeurs de bonnes voitures "
  "quittent le marché, il ne reste que des mauvaises, la qualité moyenne "
  "baisse, la confiance disparaît et le marché peut s’effondrer. L’asymétrie "
  "d’information peut donc faire disparaître un marché, et non seulement en "
  "dégrader l’efficacité. Le cours construit ensuite une distinction "
  "temporelle qu’il faut absolument maîtriser : avant la signature du contrat, "
  "l’asymétrie produit une sélection adverse, aussi appelée antisélection ; "
  "après la signature, elle produit un aléa moral, aussi appelé risque moral. "
  "Le remède relève de l’action par les règles : la protection du "
  "consommateur, par les garanties légales, l’étiquetage et les obligations "
  "d’information, le cours citant la garantie légale de conformité portée à "
  "douze mois. Deux prolongements importants. D’une part, la nouvelle économie "
  "keynésienne fait de l’asymétrie l’une des trois imperfections qui "
  "expliquent le chômage involontaire, le marché du travail étant "
  "particulièrement concerné. D’autre part, la défaillance est purement "
  "informationnelle : même avec des agents rationnels, même sans monopole ni "
  "externalité, le marché n’alloue pas efficacement les ressources.",
  [("L’inégale répartition de la connaissance",
    "Un agent détient une information que l’autre n’a pas et qui influence "
    "l’échange : le contrat se conclut donc sur des bases différentes selon la "
    "partie, ce qui en biaise le résultat."),
   ("La réaction défensive de la partie mal informée",
    "Ne pouvant distinguer les bons des mauvais, l’acheteur applique un "
    "traitement moyen : ce prix moyen est trop bas pour la qualité haute et "
    "trop élevé pour la qualité basse."),
   ("L’éviction de la qualité haute",
    "Les détenteurs de biens de bonne qualité refusent un prix moyen qui les "
    "sous-évalue et quittent le marché : la qualité moyenne baisse, ce qui "
    "abaisse encore le prix accepté."),
   ("La spirale de défiance",
    "Chaque tour de ce mécanisme dégrade la qualité moyenne et la confiance : "
    "le marché peut finir par disparaître alors qu’il existait des échanges "
    "mutuellement avantageux à réaliser."),
   ("La distinction temporelle",
    "Avant le contrat, l’asymétrie produit une sélection adverse sur les "
    "caractéristiques cachées ; après le contrat, un aléa moral sur les "
    "comportements non observables : deux problèmes distincts et deux remèdes "
    "différents.")],
  [{'a': "La notion identifie une défaillance purement informationnelle, qui "
         "subsiste même avec des agents rationnels et sans monopole ni "
         "externalité.",
    'cond': "L’argument suppose que l’information en cause soit pertinente "
            "pour la décision d’échange et coûteuse à obtenir.",
    'lim': "Lorsque l’information est facilement vérifiable, l’asymétrie "
           "disparaît : la défaillance dépend donc du coût d’acquisition de la "
           "connaissance."},
   {'a': "Elle montre que le marché peut non seulement mal allouer mais "
         "disparaître, ce qui est une défaillance d’un ordre supérieur.",
    'cond': "La disparition suppose que les vendeurs de bonne qualité aient "
            "une alternative à la vente, faute de quoi ils accepteraient le "
            "prix moyen.",
    'lim': "En pratique, des dispositifs privés — garanties, labels, "
           "réputation — limitent le mécanisme sans intervention publique."},
   {'a': "Elle justifie des remèdes réglementaires précis et peu coûteux : "
         "garanties légales, étiquetage, obligation d’information.",
    'cond': "Ces remèdes supposent que l’information révélée soit vérifiable "
            "et sanctionnable en cas de fausse déclaration.",
    'lim': "Ils relèvent de l’action par les règles, dont le cours rappelle "
           "les défauts : effet de seuil, sensibilité au lobbying, risque de "
           "contournement."},
   {'a': "Elle éclaire le fonctionnement du marché du travail, "
         "particulièrement concerné selon la nouvelle économie keynésienne.",
    'cond': "L’application suppose que la productivité du salarié soit "
            "imparfaitement observable avant et pendant la relation de "
            "travail.",
    'lim': "Elle n’explique pas à elle seule le chômage involontaire, que la "
           "nouvelle économie keynésienne rattache aussi aux rigidités de prix "
           "et à la concurrence imparfaite."}],
  [{'t': "La transparence de l’information est l’exception et l’asymétrie la "
         "règle, ce qui ruine une hypothèse centrale du modèle standard de "
         "concurrence.",
    'qui': "George Akerlof, dont le cours souligne que l’asymétrie est la "
           "situation normale des marchés.",
    'rep': "L’objection est forte parce qu’elle est généralisable : elle ne "
           "porte pas sur un marché particulier mais sur une hypothèse "
           "constitutive de la concurrence pure et parfaite."},
   {'t': "Des dispositifs privés comme la réputation ou la garantie "
         "commerciale suffisent à corriger l’asymétrie.",
    'qui': "La lecture par la réputation et les garanties commerciales.",
    'rep': "Ces dispositifs existent, mais le cours montre que la protection "
           "du consommateur relève aussi de la règle : garanties légales, "
           "étiquetage, obligation d’information, la garantie légale de "
           "conformité étant portée à douze mois."},
   {'t': "L’asymétrie explique le chômage involontaire et durable, et non "
         "seulement l’échec de marchés particuliers.",
    'qui': "La nouvelle économie keynésienne, que le cours expose.",
    'rep': "L’extension est cohérente : l’information est imparfaite, certains "
           "agents savent plus que d’autres, et le marché du travail est "
           "particulièrement concerné, avec l’aléa moral et les salaires "
           "d’efficience."},
   {'t': "La correction de l’asymétrie peut elle-même être captée par les "
         "producteurs, qui façonnent les normes d’information.",
    'qui': "L’école des choix publics, qui dénonce des réglementations "
           "capturées par des intérêts privés.",
    'rep': "L’objection impose de comparer deux imperfections plutôt que de "
           "supposer un régulateur neutre, mais elle ne rétablit pas "
           "l’efficacité d’un marché opaque."}],
  [{'n': "George Akerlof",
    'i': "L’asymétrie d’information peut non seulement dégrader un marché, "
         "mais le faire disparaître entièrement.",
    'p': "Dans The Market for Lemons (1970), il montre que l’acheteur "
         "ignorant la qualité propose un prix moyen, trop bas pour les bonnes "
         "voitures dont les vendeurs quittent alors le marché : la qualité "
         "moyenne baisse, la confiance disparaît et le marché peut "
         "s’effondrer."},
   {'n': "Herbert Simon",
    'i': "Les agents recherchent des solutions satisfaisantes plutôt "
         "qu’optimales.",
    'p': "Le cours présente sa rationalité limitée en continuité avec la "
         "critique de la transparence : traiter une information complète "
         "supposerait des capacités de calcul que les agents n’ont pas, ce qui "
         "rend le modèle standard psychologiquement fragile."},
   {'n': "Oliver Williamson",
    'i': "L’information peut être imparfaite et asymétrique, une partie "
         "disposant de plus d’informations que l’autre.",
    'p': "Le cours le rapproche d’Akerlof sur ce point et oppose les deux à "
         "Crozier : là où Williamson et Akerlof cherchent à réduire les "
         "asymétries, Crozier montre que les acteurs peuvent au contraire "
         "entretenir l’incertitude pour conserver du pouvoir."},
   {'n': "Michel Crozier",
    'i': "Les acteurs d’une organisation utilisent les zones d’incertitude à "
         "leur avantage.",
    'p': "Le cours l’oppose explicitement à Williamson et Akerlof : "
         "l’asymétrie d’information n’est pas seulement un obstacle à "
         "l’échange, elle est aussi une ressource stratégique que les acteurs "
         "ont intérêt à préserver."}],
  [{'f': "Le cours définit l’asymétrie d’information comme la situation où, "
         "dans un échange ou un contrat, un agent possède plus d’informations "
         "que l’autre.",
    'p': "La définition insiste sur le cadre contractuel, ce qui prépare la "
         "distinction entre ce qui se joue avant et après la signature."},
   {'f': "George Akerlof publie son article The Market for Lemons en 1970, "
         "sur le marché des voitures d’occasion.",
    'p': "La date situe l’asymétrie d’information comme une défaillance "
         "identifiée dans les années 1970, postérieure donc aux externalités "
         "et aux biens collectifs."},
   {'f': "Le cours distingue la sélection adverse, avant la signature du "
         "contrat, et l’aléa moral, après la signature.",
    'p': "La distinction temporelle est l’élément le plus utile du dossier : "
         "elle permet de classer immédiatement tout exemple rencontré."},
   {'f': "Le remède relève de la protection du consommateur par garanties "
         "légales, étiquetage et obligation d’information, le cours citant la "
         "garantie légale de conformité portée à douze mois.",
    'p': "L’exemple montre que la réponse publique à l’asymétrie est souvent "
         "peu coûteuse et consiste à rendre l’information disponible plutôt "
         "qu’à interdire l’échange."}],
  [{'q': "Sujet du type « L’information parfaite est-elle une hypothèse "
         "acceptable ? »",
    'f': "Le cours répond clairement non. La théorie néoclassique suppose une "
         "information parfaite, gratuite et symétrique entre tous les agents, "
         "ce qu’elle appelle la transparence de l’information ; mais dans la "
         "réalité c’est l’inverse qui domine, et l’asymétrie n’est pas une "
         "exception mais la situation normale des marchés. Akerlof en tire une "
         "conséquence radicale : l’asymétrie peut faire disparaître un marché.",
    'r': "Le raisonnement ne se contente pas de constater l’imperfection : il "
         "montre qu’elle produit un effet qualitativement différent, la "
         "disparition du marché et non sa simple inefficacité.",
    'ex': "Le marché des voitures d’occasion, où les mauvaises voitures "
          "chassent les bonnes, par application de la loi de Gresham."},
   {'q': "Sujet du type « Comment l’État peut-il améliorer le fonctionnement "
         "des marchés ? »",
    'f': "L’asymétrie d’information appelle une intervention d’un type "
         "particulier, qui ne porte ni sur les prix ni sur les quantités mais "
         "sur l’information elle-même. Le cours range ce remède dans l’action "
         "par les règles : la protection du consommateur passe par les "
         "garanties légales, l’étiquetage et l’obligation d’information, avec "
         "pour exemple la garantie légale de conformité portée à douze mois.",
    'r': "Le raisonnement montre qu’une intervention peut rétablir les "
         "conditions du marché au lieu de s’y substituer, ce qui en fait la "
         "forme la plus consensuelle de régulation.",
    'ex': "L’étiquetage, qui révèle une caractéristique cachée sans modifier "
          "ni le prix ni la quantité échangée."}],
  voisins=['n6-selection-adverse', 'n6-alea-moral', 'n6-reglementation',
           'n5-cpp'])
