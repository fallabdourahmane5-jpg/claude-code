# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 5 — Défaillances du marché et régulation."""

R = {'5': {

 'q': "Quand le marché concurrentiel échoue-t-il à allouer efficacement les ressources, et "
      "qui — l’État, le marché lui-même ou la communauté — est le mieux placé pour y "
      "remédier ?",

 'ess':
  "Le chapitre part d’un critère unique : en microéconomie standard, l’allocation est "
  "efficace quand le prix égale le coût marginal. Toute structure qui empêche P = Cm produit "
  "une allocation sous-optimale. À partir de là, le cours examine quatre défaillances, "
  "chacune correspondant à la violation d’une condition de la concurrence pure et parfaite. "
  "Le monopole d’abord — en distinguant soigneusement le monopole naturel, seule véritable "
  "défaillance structurelle, des monopoles d’innovation, d’institution et de réseau. Les "
  "biens collectifs et les biens communs ensuite, qui échappent au système de prix par "
  "non-excluabilité : les premiers par sous-production, du fait du passager clandestin "
  "d’Olson, les seconds par surexploitation, du fait de la tragédie des communs de Hardin. "
  "Les externalités, qui dissocient coût privé et coût social et produisent soit une "
  "surproduction, soit une sous-production. Les asymétries d’information enfin, qui "
  "suffisent à elles seules à faire échouer un marché — sélection adverse avant le contrat, "
  "aléa moral après. La seconde moitié du chapitre est consacrée aux remèdes, classés en "
  "trois familles : agir par les règles, par les prix (Pigou), par les quantités (Coase). "
  "Et le cours retourne finalement l’analyse contre l’État lui-même, avec l’école des choix "
  "publics, avant de présenter la troisième voie d’Ostrom : la gestion collective.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. Introduction : ce qu’est une défaillance de marché",
   'sp': [
    {'t': "A. Définition et champ du chapitre",
     'd': ["Une défaillance de marché est une situation dans laquelle le marché concurrentiel "
           "n’arrive pas à allouer les ressources de façon optimale : on produit trop ou pas "
           "assez, trop cher ou pas assez cher. Le cours en retient quatre : le monopole "
           "naturel, les biens collectifs et communs, les externalités, les asymétries "
           "d’information.",
           "Arthur Pigou, successeur de Marshall et rival de Keynes, en est l’auteur de "
           "référence. Sa position est précise et doit être citée comme telle : il est libéral, "
           "mais estime que dans certaines situations le marché est défaillant et que l’État "
           "est alors légitime à intervenir. C’est le projet de l’économie du bien-être, qui "
           "cherche à maximiser l’utilité collective.",
           "Le cours distingue enfin deux problèmes distincts : les défaillances de marché "
           "d’une part, la concurrence imparfaite d’autre part. Traiter de la concurrence pure "
           "et parfaite, c’est traiter de tout ce qui la contrarie."]},
   ],
   'v': "Pour juger qu’un marché échoue, encore faut-il un critère d’efficacité : c’est "
        "l’égalité entre le prix et le coût marginal."},

  # ----------------------------------------------------------------- II
  {'t': "II. Le monopole : quand la structure du marché empêche P = Cm",
   'sp': [
    {'t': "A. Le critère d’efficacité et le comportement du monopoleur",
     'd': ["La condition fondamentale d’efficacité est P = Cm. Lorsqu’elle est respectée, la "
           "quantité produite est optimale, le surplus total — consommateurs plus producteurs "
           "— est maximal, il n’y a ni pénurie ni gaspillage, et le bien-être collectif est "
           "maximisé. Cette situation correspond à la concurrence pure et parfaite, qui sert "
           "de référence théorique.",
           "Un monopole est une situation où une seule entreprise produit un bien sans "
           "substitut proche, et où elle est faiseuse de prix. Sa règle de maximisation du "
           "profit n’est pas P = Cm mais Rm = Cm : recette marginale égale coût marginal. Il "
           "en résulte P > Cm, une quantité produite plus faible que la quantité socialement "
           "optimale et des prix plus élevés.",
           "Le mécanisme est le suivant : le monopoleur observe la demande, connaît le prix "
           "maximum que les consommateurs acceptent de payer, et fixe son prix sur cette "
           "disposition à payer, non sur son coût marginal. La différence avec la concurrence "
           "pure et parfaite tient à l’élasticité de la demande adressée à la firme : "
           "parfaitement élastique en CPP, ce qui garantit P = Rm = Cm ; décroissante en "
           "monopole, ce qui autorise l’écart.",
           "Les conséquences sont une réduction du surplus du consommateur, l’apparition d’une "
           "rente de monopole, et une perte sèche — le triangle d’Harberger — c’est-à-dire une "
           "richesse collective qui disparaît sans profiter à personne."],
     'mec': "CPP : demande parfaitement élastique → P = Rm = Cm → optimum. Monopole : demande "
            "décroissante → Rm = Cm mais P > Cm → quantité trop faible, prix trop élevé, perte "
            "sèche."},
    {'t': "B. Le monopole est-il toujours une défaillance ? Non — une typologie",
     'd': ["Le cours répond explicitement non : le monopole en général n’est pas "
           "automatiquement une défaillance de marché. Il distingue quatre types de monopoles, "
           "qui n’ont ni les mêmes causes ni les mêmes effets.",
           "Le monopole naturel est la véritable défaillance. Il apparaît quand les coûts "
           "fixes sont très élevés, les coûts marginaux très faibles et les rendements "
           "croissants : une seule entreprise produit alors à moindre coût que plusieurs "
           "concurrentes — eau, électricité, gaz, chemins de fer, télécommunications, réseaux. "
           "Le blocage est structurel : à P = Cm l’entreprise ne couvre pas ses coûts fixes et "
           "fait des pertes, puisque Cm est inférieur à CM ; à P > Cm elle survit, mais le prix "
           "est trop élevé et la quantité trop faible. Le marché ne peut pas résoudre seul ce "
           "problème. D’où des solutions publiques : nationalisation, régulation par prix "
           "plafond, tarification au coût moyen, ou subvention permettant d’atteindre P = Cm.",
           "Le monopole d’innovation est temporaire : le brevet confère une exclusivité "
           "d’exploitation pour vingt ans au maximum sur un territoire donné. Schumpeter le "
           "justifie : la concurrence doit être la règle, mais l’innovation doit être "
           "protégée, car le monopole temporaire incite à innover, finance la recherche et "
           "favorise le progrès technique. Les effets négatifs sont symétriques : prix élevés, "
           "accès limité aux innovations — le cas des médicaments —, ralentissement possible "
           "de la diffusion et stratégies de verrouillage par brevets abusifs.",
           "Le monopole d’institution est créé par la loi, pour garantir un service public, "
           "contrôler des secteurs sensibles ou protéger l’intérêt général — jeux d’argent, "
           "transport ferroviaire, anciens monopoles énergétiques. Avantages : continuité du "
           "service et logique d’intérêt général. Limites : manque d’efficacité, absence de "
           "concurrence donc d’incitation à innover, bureaucratie, et défaillance de l’État au "
           "sens du Public Choice.",
           "Le monopole de réseau émerge enfin quand l’utilité du service augmente avec le "
           "nombre d’utilisateurs — réseaux sociaux, moteurs de recherche, plateformes. Il "
           "apporte efficacité, standardisation et innovation rapide, mais fait courir un "
           "risque de domination durable, de verrouillage du marché, d’abus de position "
           "dominante et d’exploitation des données."],
     'lim': "La conclusion du cours est nuancée : certains monopoles se justifient par "
            "l’innovation, les rendements croissants ou l’intérêt général, mais tous empêchent "
            "l’égalité P = Cm, ce qui justifie une régulation adaptée à chaque cas — et non un "
            "rejet global du monopole."},
   ],
   'v': "Le monopole naturel montre qu’une défaillance peut venir de la structure du marché. "
        "D’autres viennent de la nature même des biens échangés."},

  # ---------------------------------------------------------------- III
  {'t': "III. Biens collectifs et biens communs : quand le prix ne peut plus jouer",
   'sp': [
    {'t': "A. Rivalité et excluabilité : deux critères à ne pas confondre",
     'd': ["La rivalité répond à la question : le fait que je consomme empêche-t-il un autre "
           "de consommer la même chose ? Un pain au chocolat est rival, l’éclairage public ne "
           "l’est pas. L’excluabilité répond à une autre question : peut-on empêcher quelqu’un "
           "de consommer s’il ne paie pas ? Le cinéma et un abonnement sont excluables, l’air "
           "et l’éclairage public ne le sont pas.",
           "Le cours insiste : la rivalité concerne la quantité disponible, l’excluabilité "
           "concerne le paiement et le filtrage de l’accès. Les deux notions sont totalement "
           "distinctes, et c’est leur croisement qui structure toute l’analyse."]},
    {'t': "B. La typologie en quatre types de biens",
     'd': ["Les biens privés sont rivaux et excluables : il faut payer pour consommer, et la "
           "consommation de l’un empêche celle des autres. Ce sont les biens « normaux » de "
           "l’économie, parfaitement adaptés au marché — une voiture, des pommes, un service "
           "de coiffure.",
           "Les biens de club sont non rivaux mais excluables : on peut faire payer l’accès "
           "alors que plusieurs personnes consomment simultanément, au moins jusqu’à un "
           "certain seuil. L’autoroute à péage en est le modèle : la barrière rend le bien "
           "excluable, et plusieurs voitures circulent sans se gêner. Le marché fonctionne "
           "bien ici, et le problème n’apparaît qu’en cas de saturation, lorsque le bien "
           "devient rival.",
           "Les biens communs sont rivaux mais non excluables : ce que je prends manque aux "
           "autres, mais on ne peut pas empêcher l’accès — les poissons en mer, les forêts. La "
           "conséquence est la surexploitation, chacun ayant intérêt à consommer avant les "
           "autres.",
           "Les biens collectifs purs sont non rivaux et non excluables — défense nationale, "
           "éclairage public, sécurité, air pur. Personne ne peut en être exclu et la "
           "consommation de l’un ne gêne pas celle des autres."],
     'lim': "Le cours signale un piège de vocabulaire : en anglais public signifie collectif, "
            "alors qu’en français public renvoie à l’État. Un public good n’est donc pas "
            "nécessairement fourni par l’État — même si, en pratique, c’est souvent le cas."},
    {'t': "C. Le phare et le passager clandestin",
     'd': ["Le phare est l’exemple canonique du bien collectif pur. Il est non rival : qu’un, "
           "dix ou cent bateaux utilisent sa lumière ne la diminue pas. Il est non excluable : "
           "on ne peut ni poser une barrière, ni vendre un ticket, ni faire payer un bateau en "
           "particulier — contrairement à l’autoroute à péage, aucun moyen technique ne permet "
           "de contrôler qui paie.",
           "D’où le problème du passager clandestin, théorisé par Mancur Olson : chaque bateau "
           "veut bénéficier de la lumière, mais aucun n’a intérêt à payer, puisqu’il en "
           "profitera de toute façon. Chacun raisonne ainsi, personne ne finance, et le bien "
           "n’existe pas.",
           "La conséquence est l’impossibilité d’une production privée : une entreprise ne "
           "peut ni faire payer, ni contrôler l’accès, donc ne peut pas être rentable. Le "
           "marché échoue complètement, et une seule solution demeure : le financement par "
           "l’impôt, l’État collectant puis fournissant le bien à tous."]},
    {'t': "D. Le statut d’un bien n’est pas figé",
     'd': ["Un point important du cours : un bien n’est pas naturellement privé ou commun pour "
           "toujours. Son statut peut changer sous l’effet de la technologie, des règles "
           "institutionnelles ou de décisions politiques.",
           "La technologie d’abord, avec l’exemple de l’eau. Au départ, elle est un bien "
           "commun : non excluable — chacun va au puits ou à la fontaine — et rivale. Puis "
           "vient la distribution par immeuble, puis l’individualisation des compteurs : "
           "chacun paie ce qu’il consomme et peut être exclu en cas de non-paiement. L’eau "
           "devient un bien privé.",
           "Les règles ensuite : même quand on sait techniquement capter l’eau, on ne peut pas "
           "détourner librement un cours d’eau ni s’approprier tout le débit d’une rivière, "
           "parce que l’État impose des règles, des quotas et le maintien d’un débit minimal. "
           "La réglementation empêche donc la privatisation totale de certaines ressources "
           "communes.",
           "La politique enfin : les vaccins sont produits par des firmes privées et protégés "
           "par des brevets, donc techniquement des biens privés ; mais quand la santé "
           "publique devient un objectif collectif, se pose la question de leur transformation "
           "en bien commun. L’exemple inverse est celui des enclosures anglaises, qui rendent "
           "l’exclusion possible et transforment un bien collectif en bien privé."]},
    {'t': "E. Pourquoi ce sont des défaillances : sous-production et surexploitation",
     'd': ["Le principe général est qu’un marché ne fonctionne que si les agents ont des "
           "incitations à produire, si les prix permettent de faire payer et si la production "
           "est rentable. Quand on ne peut pas faire payer, ou quand l’usage individuel nuit à "
           "l’intérêt collectif, l’allocation devient inefficace.",
           "Pour les biens collectifs purs, la non-excluabilité empêche de faire payer : "
           "chacun se comporte en passager clandestin, aucun producteur privé ne peut "
           "rentabiliser, et le résultat est une sous-production voire une absence totale de "
           "production, alors même que le bien est socialement utile. Le prix ne joue plus son "
           "rôle d’allocation. Solution : financement par l’impôt, production ou commande "
           "publique.",
           "Pour les biens communs, chacun raisonne autrement : « si je ne consomme pas "
           "maintenant, quelqu’un d’autre le fera ». Il n’existe ni prix dissuasif, ni règle "
           "collective spontanée, et le marché n’intègre pas le coût collectif futur. Le "
           "résultat est la surexploitation, jusqu’à l’épuisement ou la dégradation "
           "irréversible. Solutions possibles : réglementation par quotas, privatisation par "
           "attribution de droits de propriété, ou gestion collective."],
     'mec': "Non-excluabilité → le prix ne peut plus jouer → soit passager clandestin et "
            "sous-production (biens collectifs), soit course à la ressource et surexploitation "
            "(biens communs)."},
    {'t': "F. Hardin et Olson : deux façons dont l’intérêt individuel détruit l’intérêt "
          "collectif",
     'd': ["Garrett Hardin, dans The Tragedy of the Commons (1968), montre que les communs ne "
           "conduisent pas naturellement au bien-être collectif : lorsque l’usage est "
           "collectif et l’accès libre, les individus gaspillent, surexploitent et épuisent la "
           "ressource. Le mécanisme est asymétrique : le gain d’un usage supplémentaire est "
           "individuel, tandis que le coût de la dégradation est partagé par tous. Chacun "
           "surexploite donc, la ressource s’épuise, et l’intérêt général n’est pas satisfait.",
           "C’est une remise en cause directe de l’idée libérale classique selon laquelle la "
           "somme des intérêts individuels produit l’intérêt collectif : ici, c’est l’inverse. "
           "Le mécanisme s’éclaire par le dilemme du prisonnier : chaque agriculteur a intérêt "
           "à faire paître le maximum de bêtes, parce qu’il ignore ce que feront les autres et "
           "anticipe qu’ils surexploiteront ; il surexploite donc pour se protéger, et si tous "
           "font de même, la terre est détruite et tout le monde perd.",
           "Mancur Olson, dans The Logic of Collective Action (1965), met en évidence un "
           "problème voisin mais distinct : même quand tout le monde a intérêt à ce qu’un bien "
           "collectif existe, il est individuellement rationnel de ne pas contribuer, puisque "
           "le bénéfice est collectif et le coût individuel. C’est le paradoxe de l’action "
           "collective : ce qui est souhaitable collectivement est contredit par la "
           "rationalité individuelle.",
           "Deux exemples le rendent concret. Les transports publics : ne pas payer son billet "
           "est moralement condamnable et collectivement destructeur, mais individuellement "
           "rationnel si la probabilité de contrôle est faible et le gain immédiat certain. La "
           "grève : faire grève coûte une journée de salaire, alors que laisser les autres la "
           "faire permet d’obtenir les bénéfices sans en payer le coût — mais sans grévistes, "
           "rien ne change."],
     'lim': "Ensemble, Hardin et Olson établissent la même conclusion par deux voies : sans "
            "règles, sans institutions et sans contrainte collective, ni les biens communs ni "
            "les biens collectifs ne peuvent être durablement préservés ou produits."},
   ],
   'v': "Reste une défaillance qui ne tient ni à la structure du marché ni à la nature du "
        "bien, mais au fait qu’une partie des effets d’une activité échappe entièrement au "
        "marché."},

  # ----------------------------------------------------------------- IV
  {'t': "IV. Les externalités : des coûts et des bénéfices qui ne passent pas par le marché",
   'sp': [
    {'t': "A. Définition et principe",
     'd': ["Toutes les activités économiques ne passent pas par le marché : certaines "
           "produisent des effets sur d’autres agents sans échange marchand. Une externalité "
           "est la répercussion, positive ou négative, de l’activité d’un agent sur un autre, "
           "sans que cette répercussion passe par le marché, donc sans contrepartie monétaire. "
           "Le point essentiel est qu’il n’y a ni paiement ni compensation.",
           "Le marché ne prend en compte que ce qui est payé ; or une externalité est "
           "précisément ce qui n’est pas payé. Le prix de marché ne reflète donc pas le coût "
           "ou le bénéfice réel pour la société."]},
    {'t': "B. L’externalité négative : un coût qui reste gratuit",
     'd': ["Une externalité négative existe lorsqu’une activité impose un coût à d’autres sans "
           "compensation : une usine qui pollue l’air d’un village ou une rivière, un "
           "agriculteur utilisant des pesticides près des habitations, une boîte de nuit "
           "voisine d’un EHPAD. Les riverains subissent un dommage, l’entreprise ne paie rien "
           "pour ce dommage : c’est un coût externe.",
           "Le mécanisme est précis. L’offre repose sur le coût marginal privé, celui que "
           "supporte l’entreprise seule, qui ne comprend ni la pollution ni les nuisances. Le "
           "prix d’équilibre observé ne couvre donc que ce coût privé et ignore le coût "
           "externe : il est artificiellement trop bas, ce que le cours appelle un « mensonge "
           "économique », une partie du coût étant cachée. Le véritable coût est le coût "
           "marginal social : CmS = CmP + coût externe, de sorte que la courbe de coût social "
           "se situe au-dessus de la courbe de coût privé.",
           "La conséquence est une surproduction : sans prise en compte de l’externalité, le "
           "prix est trop bas et la quantité trop élevée ; avec prise en compte, le prix "
           "optimal est plus élevé et la quantité plus faible. Le marché produit donc trop "
           "d’un bien socialement coûteux. Le film Erin Brockovich en donne l’illustration : "
           "une entreprise pollue l’eau, les habitants développent maladies, cancers et "
           "malformations, et l’entreprise ne paie pas pour ces dommages."],
     'mec': "CmP < CmS → prix trop bas, quantité trop élevée → surproduction et perte de "
            "bien-être collectif."},
    {'t': "C. L’externalité positive : un bénéfice qui n’est pas rémunéré",
     'd': ["Symétriquement, une externalité est positive lorsqu’une activité procure un "
           "avantage sans paiement : l’apiculteur qui bénéficie d’un champ de fleurs voisin, "
           "un commerce installé près d’un lycée ou d’une université qui profite d’une "
           "clientèle sans rien verser à l’établissement, un fleuriste à proximité d’un hôpital "
           "ou d’un cimetière.",
           "Le marché raisonne toujours à partir du coût marginal privé et ignore le bénéfice "
           "externe. Or, pour la société, le coût réel est plus faible que celui supporté par "
           "l’entreprise seule, puisque l’activité crée un avantage collectif : CmS = CmP − "
           "bénéfice externe, et la courbe de coût social passe en dessous de la courbe de coût "
           "privé.",
           "La conséquence est une sous-production : le prix observé est trop élevé et la "
           "quantité trop faible par rapport à l’optimum. Le marché empêche donc une activité "
           "socialement bénéfique de se développer suffisamment."],
     'mec': "CmP > CmS → prix trop élevé, quantité trop faible → sous-production.",
     'lim': "La formule de synthèse à retenir est symétrique : externalité négative → coût "
            "privé inférieur au coût social → surproduction et prix trop faible ; externalité "
            "positive → coût privé supérieur au coût social → sous-production et prix trop "
            "élevé. Dans les deux cas, l’allocation est sous-optimale."},
   ],
   'v': "Les trois premières défaillances touchent les prix, les quantités ou la nature des "
        "biens. La quatrième touche l’information elle-même."},

  # ------------------------------------------------------------------ V
  {'t': "V. Les asymétries d’information",
   'sp': [
    {'t': "A. Sélection adverse : l’asymétrie avant le contrat",
     'd': ["Il y a asymétrie d’information lorsque, dans un échange ou un contrat, un agent "
           "possède plus d’informations que l’autre : l’échange est biaisé et le marché ne "
           "fonctionne plus correctement. Cette défaillance a été identifiée dans les années "
           "1970, principalement par George Akerlof dans The Market for Lemons (1970). Elle se "
           "décline en deux moments : avant la signature du contrat, c’est la sélection "
           "adverse ; après, c’est l’aléa moral.",
           "La sélection adverse apparaît quand, du fait d’une asymétrie avant l’échange, les "
           "produits de mauvaise qualité restent sur le marché tandis que les bons en sortent. "
           "Sur le marché des voitures d’occasion, le vendeur connaît la qualité de son "
           "véhicule, pas l’acheteur ; ce dernier devient méfiant et baisse son consentement à "
           "payer ; le prix moyen baisse ; les vendeurs de bonnes voitures renoncent à vendre ; "
           "il ne reste que les mauvaises. Les mauvaises voitures chassent les bonnes — c’est "
           "l’application de la loi de Gresham, selon laquelle la mauvaise monnaie chasse la "
           "bonne.",
           "Le même mécanisme joue sur le crédit bancaire : la banque ignore si l’emprunteur "
           "est prudent ou risqué, elle relève ses taux pour se protéger, les emprunteurs "
           "prudents renoncent, les risqués acceptent — et la banque attire précisément les "
           "mauvais profils."],
     'mec': "Qualité invisible → prix unique moyen → les bons produits sortent → qualité "
            "moyenne ↓ → confiance ↓ → le marché peut disparaître."},
    {'t': "B. Aléa moral : l’asymétrie après le contrat",
     'd': ["L’aléa moral apparaît lorsqu’un agent, une fois protégé, adopte un comportement "
           "plus risqué qu’avant. Trois exemples structurent le cours. La banque centrale "
           "prêteur en dernier ressort protège le système bancaire, mais les banques savent "
           "qu’elles seront sauvées et prennent davantage de risques — c’est le « too big to "
           "fail ». L’assurance protège contre les accidents, mais peut encourager "
           "l’imprudence : conduite plus risquée, moindre vigilance. L’annulation des dettes, "
           "si elle est anticipée, incite à s’endetter davantage.",
           "D’où une ambiguïté que le cours formule nettement : les dispositifs de protection "
           "sont nécessaires pour stabiliser l’économie, mais ils créent eux-mêmes de l’aléa "
           "moral. La solution est en même temps une partie du problème."],
     'lim': "L’intérêt théorique de cette défaillance est qu’elle est pure : même avec des "
            "agents rationnels, sans monopole ni externalité, le marché n’alloue pas "
            "efficacement les ressources — le problème vient uniquement de l’information "
            "imparfaite."},
   ],
   'v': "Les quatre défaillances étant établies, la question devient pratique : comment les "
        "corriger, et par quels instruments ?"},

  # ----------------------------------------------------------------- VI
  {'t': "VI. Corriger les défaillances : règles, prix, quantités",
   'sp': [
    {'t': "A. Agir par les règles : la réglementation",
     'd': ["L’État impose directement des normes et des interdictions. Contre les monopoles : "
           "lois antitrust — le Sherman Act de 1890 —, interdiction de certaines fusions, "
           "contrôle de la concurrence. Pour les biens communs : quotas de pêche, limitation "
           "de l’accès aux ressources, protection contre la surexploitation. Contre les "
           "externalités négatives : normes environnementales d’émission, de production, de "
           "procédés ou de qualité — interdiction des sacs plastiques, normes automobiles. "
           "Contre les asymétries d’information : garanties légales, étiquetage, obligation "
           "d’information — la garantie légale de conformité a ainsi été portée à douze mois."],
     'lim': "Cinq limites sont listées : la réglementation est peu incitative — on respecte la "
            "norme sans chercher à faire mieux —, sensible au lobbying, peu flexible, exposée "
            "au contournement, et pas toujours efficace économiquement."},
    {'t': "B. Agir par les prix : la solution de Pigou",
     'd': ["Le principe est de corriger les prix pour qu’ils reflètent le vrai coût ou le vrai "
           "bénéfice social. Face à une externalité négative, la taxe pigouvienne applique le "
           "principe pollueur-payeur : elle fait payer à l’entreprise le coût qu’elle impose à "
           "la société, ce qui augmente son coût marginal privé jusqu’au coût social, fait "
           "monter le prix et baisser la quantité, donc ramène à l’optimum collectif. Face à "
           "une externalité positive, la subvention rémunère le bénéfice collectif : elle "
           "abaisse le coût, fait baisser le prix et augmenter la quantité.",
           "L’exemple empirique du cours est la taxe carbone britannique instaurée en 2013 : "
           "la part du charbon dans la production électrique passe de 40 % en 2012 à 4 % en "
           "2019. Le mécanisme d’ajustement carbone aux frontières européen prolonge la "
           "logique à l’échelle du commerce extérieur.",
           "Le cours ajoute deux questions pratiques. Qui taxer, du producteur ou du "
           "consommateur ? Si c’est le producteur, il examinera l’élasticité de la demande "
           "avant de décider s’il répercute la taxe dans ses prix. Et parfois l’État choisit "
           "de produire plutôt que de taxer ou subventionner : les Musgrave parlent alors de "
           "biens tutélaires, mis à disposition de la population quasi gratuitement et "
           "financés par l’impôt."],
     'lim': "Avantages : la taxation est incitative, flexible et économiquement efficace. "
            "Limites : il est difficile de mesurer précisément le coût externe, "
            "l’acceptabilité politique est faible, et l’effet inflationniste est possible. Le "
            "débat sur le MACF illustre les effets pervers : en fuyant l’Europe, on résout le "
            "problème à l’échelle européenne mais on le déplace à l’échelle mondiale ; "
            "certains contestent même qu’il s’agisse d’une taxe, puisque son niveau varie avec "
            "le prix du marché des quotas."},
    {'t': "C. Agir par les quantités : quotas échangeables et effet Jevons",
     'd': ["Plutôt que de fixer le prix, on fixe la quantité et on laisse le marché déterminer "
           "le prix. L’État fixe un plafond global d’émissions, attribue des quotas, et les "
           "entreprises les échangent : celles qui polluent peu vendent, celles qui polluent "
           "beaucoup achètent. Le marché européen des quotas d’émission en est l’application. "
           "L’effet recherché est que la pollution soit réduite au moindre coût collectif.",
           "Avantages : très efficace économiquement, et incitation permanente à innover. "
           "Limites : prix volatil, complexité, risque de spéculation, et problème de la "
           "répartition initiale des quotas.",
           "Le cours signale un effet pervers transversal, l’effet Jevons : quand le progrès "
           "technique rend un bien moins coûteux, on en consomme davantage, ce qui peut "
           "annuler l’économie recherchée — Jevons l’avait constaté avec le charbon, et "
           "l’argument vaut pour les politiques d’efficacité énergétique."]},
    {'t': "D. Prix plancher et prix plafond : quand l’intervention crée elle-même une "
          "inefficacité",
     'd': ["Puisque l’État est en charge de l’allocation des ressources quand le marché "
           "défaille, il peut aussi fixer un prix minimum ou maximum. Le prix plancher est un "
           "prix minimum sous lequel il est interdit de vendre : le SMIC sur le marché du "
           "travail, les prix garantis agricoles. S’il est inférieur au prix d’équilibre il ne "
           "change rien ; s’il lui est supérieur, l’offre excède la demande.",
           "Les effets sont alors en chaîne : surproduction — sur le marché du travail, un "
           "excès d’offre de travail, c’est-à-dire du chômage ; gaspillage, avec des stocks "
           "détruits ou des travailleurs sans emploi ; allocation sous-optimale, puisqu’on "
           "produit une quantité qui n’est ni la bonne ni au bon prix ; perte sèche, une part "
           "de la richesse collective disparaissant sans profiter à personne ; distorsion des "
           "surplus, le producteur captant une partie du surplus du consommateur ; et "
           "incitation à l’illégalité, par le travail au noir ou le paiement sous le minimum.",
           "Le prix plafond est le symétrique : un prix maximum au-dessus duquel il est "
           "interdit de vendre — encadrement des loyers, prix alimentaires en période de "
           "crise. S’il est inférieur au prix d’équilibre, la demande excède l’offre : "
           "pénurie — beaucoup de locataires et pas assez de logements —, échanges "
           "bénéfiques qui n’ont pas lieu, perte sèche, distorsion des surplus au profit du "
           "consommateur, développement de l’économie illégale avec loyers au noir et "
           "dessous-de-table, et dégradation de la qualité faute d’entretien et de rénovation."],
     'lim': "Le cours apporte une nuance décisive : l’Institut des politiques publiques "
            "(Avignon et Guigue), en analysant la PAC, montre qu’un prix plancher sur les "
            "produits finaux peut avoir des effets pervers, mais devient efficace en situation "
            "de monopsone — c’est-à-dire quand c’est l’acheteur, et non le vendeur, qui est "
            "faiseur de prix."},
   ],
   'v': "Toutes ces solutions supposent un État capable et désintéressé. C’est précisément "
        "cette hypothèse que l’école des choix publics conteste."},

  # ---------------------------------------------------------------- VII
  {'t': "VII. Qui corrige ? L’État, le marché ou la communauté",
   'sp': [
    {'t': "A. Le contrepied à Pigou : les défaillances de l’État",
     'd': ["Pigou affirme que l’intervention est justifiée quand le marché échoue. Dans les "
           "années 1970-1980, l’école des choix publics — Buchanan (Nobel 1986), Tullock, "
           "Stigler (Nobel 1982) — répond qu’il existe aussi des défaillances de l’État. Le "
           "contexte est celui du retour du libéralisme : Thatcher, Reagan, le succès de "
           "Friedman, la redécouverte de Hayek.",
           "L’hypothèse centrale est que l’État n’est pas un être neutre au-dessus de la "
           "société : il est composé d’hommes politiques, de hauts fonctionnaires, "
           "d’administrations et de groupes organisés, tous rationnels. On applique donc à "
           "l’État la logique qu’on applique au marché : chacun maximise son utilité, et pour "
           "un politicien l’utilité, c’est la réélection. C’est l’individualisme "
           "méthodologique appliqué à la politique : la politique devient un marché politique "
           "où les électeurs sont demandeurs, les politiciens offreurs, et les promesses des "
           "biens politiques.",
           "La conséquence est que, même lorsqu’il veut corriger une défaillance, l’État peut "
           "agir pour des raisons électoralistes, favoriser des groupes organisés, produire "
           "des politiques inefficaces ou des effets pervers — une politique environnementale "
           "soutenue puis abandonnée parce qu’elle coûte des voix. Stigler y ajoute la capture "
           "réglementaire, Tullock la recherche de rente, c’est-à-dire des dépenses visant à "
           "obtenir un avantage distribué par la décision publique plutôt qu’à produire de la "
           "richesse.",
           "Le cours applique cette critique au monopole naturel confié au privé : apparition "
           "d’une rente de monopole, qui n’est ni une récompense de l’innovation ni de la "
           "productivité mais du pouvoir de marché ; absence d’incitation à réduire les coûts, "
           "faute de concurrence ; et perte de contrôle de l’État sur les prix, les coûts et "
           "la stratégie industrielle. Mais le monopole public n’est pas exempt de reproches : "
           "il peut être inefficace, bureaucratique et servir des intérêts politiques."],
     'lim': "La formule de synthèse : Pigou dit que le marché est imparfait et que l’État peut "
            "l’améliorer ; le Public Choice dit que l’État est imparfait et peut aggraver le "
            "marché. Il n’existe pas de solution parfaite, seulement des arbitrages."},
    {'t': "B. Coase : résoudre l’externalité par les droits de propriété",
     'd': ["Coase part d’un constat différent : les externalités ne viennent pas seulement "
           "d’un problème de comportement, mais d’un problème d’organisation et de droits de "
           "propriété. Il ne rejette pas l’État, mais conteste que la taxe soit toujours la "
           "meilleure solution, et pose une question simple : pourquoi faire intervenir l’État "
           "si les agents peuvent s’entendre entre eux ?",
           "Le principe est que si l’on attribue clairement des droits de propriété, les "
           "agents peuvent négocier et résoudre l’externalité par le marché : on transforme un "
           "problème social en échange marchand. L’exemple du cours est celui des éléphants : "
           "ressource commune n’appartenant à personne, ils sont chassés par des braconniers "
           "malgré des lois contournées ; si chaque troupeau a un propriétaire identifié — ONG, "
           "association, État, entreprise —, celui-ci a intérêt à les protéger, peut financer "
           "la protection, négocier des compensations et organiser une gestion durable. "
           "L’externalité est internalisée.",
           "Internaliser une externalité, c’est intégrer les coûts ou bénéfices externes dans "
           "le calcul économique des agents : chez Pigou par la taxe, chez Coase par la "
           "négociation et le marché. Deux conditions sont requises : des droits de propriété "
           "clairement définis — qui possède quoi, sur quelle ressource, pour combien de temps "
           "— et des droits échangeables, ce qui permet la création d’un marché, comme pour "
           "les quotas de CO₂.",
           "Coase insiste sur un point crucial : le marché n’est pas gratuit. Les coûts de "
           "transaction regroupent la recherche d’information, la négociation, la rédaction "
           "des contrats et le contrôle. La solution de marché ne fonctionne donc que si ces "
           "coûts sont faibles, si les acteurs ne sont pas trop nombreux et si les droits sont "
           "faciles à définir — terres agricoles, quotas, concessions, ressources localisées."],
     'lim': "Coase n’est pas anti-État : celui-ci reste indispensable pour définir les droits "
            "de propriété, garantir leur respect et faire appliquer les contrats — d’où son "
            "classement parmi les néo-institutionnalistes. Mais quand les biens sont difficiles "
            "à délimiter (l’air, les océans, le climat, les espèces très mobiles), que les "
            "acteurs sont trop nombreux et les coûts de transaction élevés, la négociation "
            "devient trop coûteuse et l’intervention publique ou collective redevient "
            "nécessaire."},
    {'t': "C. Les limites de Coase : marchandisation et tragédie des anti-communs",
     'd': ["Première limite : tous les biens ne se prêtent pas à la propriété. Certains sont "
           "immatériels, diffus, transfrontaliers ou symboliquement communs — l’air, le "
           "climat, les océans, la forêt amazonienne. L’Amazonie traverse plusieurs États et "
           "constitue, pour certaines communautés locales, un bien commun au sens fort, "
           "culturel et vital : dire à qui elle appartient est complexe et politiquement "
           "contestable.",
           "D’où une critique philosophique : faut-il marchandiser la nature pour la protéger ? "
           "Avec la logique de Coase, le climat, l’air pur et la biodiversité deviennent des "
           "marchés, ce qui étend l’esprit capitaliste à des domaines qui lui échappaient. Le "
           "risque identifié est net : ce qui n’a pas de prix n’existe pas économiquement, "
           "mais en donnant une valeur marchande à la nature on perd peut-être sa valeur "
           "symbolique, sociale et culturelle.",
           "Seconde limite, apportée par Michael Heller (1998) : la tragédie des anti-communs. "
           "À l’inverse de la tragédie des communs, qui vient d’un défaut de propriété, "
           "celle-ci vient d’un excès : trop de droits de propriété empêchent l’usage efficace "
           "d’une ressource. L’exemple central est l’industrie pharmaceutique — à force de "
           "multiplier les brevets sur les molécules, les principes actifs et les procédés, "
           "chaque innovation suppose de payer des royalties et d’obtenir des autorisations "
           "multiples, si bien que la recherche devient plus lente, plus coûteuse, parfois "
           "bloquée. Par analogie avec les enclosures agricoles, on parle d’enclosures de la "
           "connaissance : un savoir autrefois partagé et cumulatif devient fragmenté et "
           "verrouillé."],
     'lim': "Le paradoxe est explicite : le droit de propriété, censé encourager l’innovation, "
            "peut finir par la freiner — ce qui vaut aussi pour les brevets défensifs, déposés "
            "non pour exploiter une innovation mais pour bloquer les concurrents."},
    {'t': "D. Ostrom : la troisième voie de la gestion collective",
     'd': ["Elinor Ostrom (1933-2012), première femme à recevoir le prix Nobel d’économie en "
           "2009, s’inscrit dans la nouvelle économie institutionnelle. Elle part d’un constat "
           "critique : les économistes présentent une alternative trop simple — soit le "
           "marché, soit l’État. Hardin lui-même ne voyait que deux issues, privatiser ou "
           "nationaliser.",
           "Ostrom conteste cette vision et montre empiriquement que de nombreuses communautés "
           "gèrent durablement des biens communs sans passer ni par l’État ni par le marché : "
           "gestion de l’eau en Espagne, pâturages collectifs en Suisse, forêts au Japon, "
           "systèmes d’irrigation en Asie, communautés rurales en Afrique et en Amérique "
           "latine. La tragédie des communs n’est donc pas une fatalité.",
           "Dans ces communautés, les individus se connaissent, établissent ensemble des "
           "règles, contrôlent l’usage de la ressource et sanctionnent les abus : c’est une "
           "gouvernance collective, qui relève d’une logique de coopération et non d’une "
           "logique de prix ou d’impôt. Ostrom nomme ces règles des arrangements "
           "institutionnels : formels ou informels, construits par les utilisateurs eux-mêmes, "
           "adaptés au contexte local, flexibles et évolutifs — quotas décidés collectivement, "
           "tours de rôle, surveillance mutuelle, sanctions graduées, négociation permanente.",
           "Le champ d’application s’est élargi : communs naturels (eau, forêts, pâturages, "
           "pêche), communs culturels (œuvres, savoirs, patrimoine), communs numériques "
           "(logiciels libres, encyclopédies collaboratives, données ouvertes) et communs de "
           "la connaissance (recherche scientifique, vaccins, brevets)."],
     'lim': "Le cours est explicite sur la portée du modèle : il fonctionne surtout quand la "
            "communauté est petite — souvent moins de cent personnes —, que les acteurs se "
            "connaissent, que la confiance existe, que la communication et la surveillance "
            "sont possibles et que les règles sont acceptées par tous. Ce modèle n’est donc "
            "pas universel mais local."},
   ],
   'v': "La conclusion du chapitre est une règle de méthode : entre l’État de Pigou, le marché "
        "de Coase et la communauté d’Ostrom, il n’existe pas de solution unique — seulement des "
        "arbitrages entre efficacité économique et faisabilité politique."},
 ],

 'ae': [
  {'n': "Arthur Pigou, l’économie du bien-être", 'k': 'a',
   'i': "Libéral, mais partisan de l’intervention quand le marché défaille : internaliser "
        "l’externalité par la taxe ou la subvention."},
  {'n': "Joseph Schumpeter", 'k': 'a',
   'i': "Justifie le monopole d’innovation : la concurrence doit être la règle, mais "
        "l’innovation doit être temporairement protégée pour être financée."},
  {'n': "Garrett Hardin, The Tragedy of the Commons (1968)", 'k': 'a',
   'i': "Le gain est individuel, le coût de la dégradation collectif : l’intérêt individuel "
        "détruit la ressource commune."},
  {'n': "Mancur Olson, The Logic of Collective Action (1965)", 'k': 'a',
   'i': "Le paradoxe de l’action collective : bénéfice collectif, coût individuel, donc "
        "personne ne contribue — transports publics, grèves."},
  {'n': "George Akerlof, The Market for Lemons (1970)", 'k': 'a',
   'i': "La sélection adverse : quand la qualité est invisible, les mauvais produits chassent "
        "les bons et le marché peut disparaître."},
  {'n': "Michael Spence", 'k': 'a',
   'i': "Le signalement : un diplôme est crédible parce qu’il est coûteux à imiter — une "
        "réponse privée à l’asymétrie d’information."},
  {'n': "Ronald Coase", 'k': 'a',
   'i': "Droits de propriété définis et échangeables plus coûts de transaction faibles : les "
        "agents internalisent l’externalité sans l’État — qui reste nécessaire pour poser le "
        "cadre."},
  {'n': "Michael Heller (1998)", 'k': 'a',
   'i': "La tragédie des anti-communs : trop de droits de propriété bloquent l’usage, d’où les "
        "enclosures de la connaissance."},
  {'n': "Elinor Ostrom (Nobel 2009)", 'k': 'a',
   'i': "Ni marché ni État : des communautés élaborent des arrangements institutionnels et "
        "gèrent durablement les communs, surtout en deçà d’une centaine de personnes."},
  {'n': "James Buchanan, Gordon Tullock, George Stigler", 'k': 'a',
   'i': "L’école des choix publics : l’État est une somme d’intérêts individuels — capture "
        "réglementaire, recherche de rente, marché politique."},
  {'n': "Richard et Peggy Musgrave", 'k': 'a',
   'i': "Les biens tutélaires : l’État choisit parfois de produire lui-même et de fournir "
        "quasi gratuitement, plutôt que de taxer ou subventionner."},
  {'n': "William Stanley Jevons", 'k': 'a',
   'i': "L’effet Jevons : quand le progrès technique abaisse le coût d’un bien, on en consomme "
        "davantage — ce qui peut annuler l’économie recherchée."},
  {'n': "Le phare", 'k': 'e',
   'i': "Non rival et non excluable : aucun bateau n’a intérêt à payer, donc aucune entreprise "
        "privée ne peut le produire — seul l’impôt le permet."},
  {'n': "L’autoroute à péage", 'k': 'e',
   'i': "Le bien de club : excluable par la barrière, non rival tant qu’il n’y a pas de "
        "congestion — la saturation le rend rival."},
  {'n': "L’eau, de la fontaine au compteur individuel", 'k': 'e',
   'i': "La technologie transforme un bien commun en bien privé en rendant l’exclusion "
        "possible — mais la réglementation empêche la privatisation d’une rivière."},
  {'n': "Erin Brockovich", 'k': 'e',
   'i': "Une entreprise pollue l’eau, les riverains subissent maladies et malformations, et le "
        "coût n’entre pas dans ses décisions : l’externalité négative en situation réelle."},
  {'n': "La taxe carbone britannique (2013)", 'k': 'e',
   'i': "La part du charbon dans l’électricité passe de 40 % en 2012 à 4 % en 2019 : la taxe "
        "pigouvienne fonctionne quand le signal-prix est fort."},
  {'n': "Le marché européen des quotas d’émission et le MACF", 'k': 'e',
   'i': "On fixe la quantité et le marché fixe le prix : efficace, mais volatil, complexe, et "
        "susceptible de déplacer le problème au lieu de l’éradiquer."},
  {'n': "Le SMIC et l’encadrement des loyers", 'k': 'e',
   'i': "Prix plancher et prix plafond contraignants : chômage et stocks invendus d’un côté, "
        "pénurie et dégradation de la qualité de l’autre."},
  {'n': "Les brevets pharmaceutiques", 'k': 'e',
   'i': "Vingt ans d’exclusivité incitent à innover, mais leur multiplication ralentit la "
        "recherche : monopole d’innovation et anti-communs sur le même objet."},
 ],

 'arg': [
  "Chaque défaillance est la violation d’une condition de la concurrence pure et parfaite : "
  "c’est le fil qui relie ce chapitre au précédent et qui structure une dissertation.",
  "Le monopole naturel n’est pas un abus mais une donnée technique (Cm < CM) : le débat porte "
  "sur le mode de régulation — tarification au coût moyen, subvention, nationalisation — et "
  "non sur l’opportunité du monopole.",
  "La non-excluabilité produit deux défaillances opposées : sous-production pour les biens "
  "collectifs (passager clandestin), surexploitation pour les biens communs (tragédie des "
  "communs). Les confondre est l’erreur la plus fréquente.",
  "Externalité négative et positive se raisonnent avec le même outil — l’écart entre coût "
  "marginal privé et coût marginal social — mais avec des conclusions symétriques : "
  "surproduction d’un côté, sous-production de l’autre.",
  "Sélection adverse (avant le contrat) et aléa moral (après) n’appellent pas les mêmes "
  "remèdes : signalement et garantie pour l’une, franchise et bonus-malus pour l’autre.",
  "Pigou, Coase et Ostrom ne s’opposent pas terme à terme : ils supposent des coûts de "
  "transaction, des tailles de communauté et des capacités d’appropriation différents.",
  "Reconnaître les défaillances du marché n’implique pas l’efficacité de l’État : capture "
  "réglementaire, recherche de rente et électoralisme imposent la symétrie de l’analyse.",
 ],

 'deb': [
  "Taxer ou créer un marché de droits ? La taxe fixe le prix et laisse la quantité "
  "incertaine, le marché de quotas fixe la quantité et laisse le prix volatil.",
  "Les communs doivent-ils être privatisés, nationalisés ou gouvernés collectivement ? Hardin "
  "contre Ostrom, avec Coase en position intermédiaire.",
  "Faut-il marchandiser la nature pour la protéger, ou cette marchandisation détruit-elle la "
  "valeur symbolique qu’on prétend défendre (Amazonie, marché du carbone) ?",
  "Le brevet encourage-t-il l’innovation ou la bloque-t-il ? Monopole d’incitation chez "
  "Schumpeter contre enclosures de la connaissance chez Heller.",
  "L’État est-il un correcteur neutre ou un acteur intéressé comme les autres ? Pigou contre "
  "le Public Choice.",
  "Un prix plancher est-il toujours inefficace ? L’analyse de la PAC montre qu’il peut au "
  "contraire être justifié en situation de monopsone.",
 ],

 'lien': [
  {'c': 4, 'p': "Ce chapitre est le négatif du précédent : les cinq conditions de la CPP y "
                "sont levées une à une, et Akerlof comme la perte sèche y sont déjà posés."},
  {'c': 9, 'p': "Pouvoir de marché, barrières à l’entrée, effets de réseau et politique de la "
                "concurrence prolongent l’analyse du monopole à l’échelle des stratégies "
                "d’entreprise."},
  {'c': 1, 'p': "Les trois fonctions de Musgrave et les biens tutélaires donnent la traduction "
                "budgétaire de la correction des défaillances."},
  {'c': 7, 'p': "Climat, haute mer et biens communs mondiaux transposent Hardin et Ostrom à "
                "l’échelle planétaire, avec la tragédie des horizons."},
  {'c': 6, 'p': "Externalités positives de la connaissance, brevets et bien non rival relient "
                "défaillances de marché et théories de la croissance endogène."},
  {'c': 2, 'p': "L’aléa moral du prêteur en dernier ressort et le « too big to fail » sont "
                "développés dans le chapitre monétaire."},
 ],

 'min': [
  "Critère d’efficacité : P = Cm. Quatre défaillances : monopole naturel, biens collectifs et "
  "communs, externalités, asymétries d’information.",
  "Monopole : Rm = Cm donc P > Cm, quantité trop faible, perte sèche (triangle d’Harberger). "
  "Quatre types : naturel, d’innovation, d’institution, de réseau.",
  "Monopole naturel : coûts fixes élevés, Cm < CM — à P = Cm, pertes. Seule vraie défaillance "
  "structurelle.",
  "Rivalité × excluabilité : bien privé, bien de club, bien commun, bien collectif. Le statut "
  "d’un bien n’est pas figé (eau, vaccins, enclosures).",
  "Hardin (1968) : surexploitation ; Olson (1965) : passager clandestin et sous-production.",
  "Externalité négative : CmP < CmS → surproduction, prix trop bas. Positive : CmP > CmS → "
  "sous-production, prix trop élevé.",
  "Akerlof (1970) : sélection adverse avant le contrat (loi de Gresham) ; aléa moral après "
  "(too big to fail, assurance).",
  "Trois familles de remèdes : règles (normes, antitrust, garantie de 12 mois), prix (taxe "
  "pigouvienne, subvention), quantités (quotas échangeables).",
  "Prix plancher → surproduction et chômage ; prix plafond → pénurie et dégradation de la "
  "qualité ; dans les deux cas, perte sèche.",
  "Public Choice (Buchanan, Tullock, Stigler) : l’État défaille aussi. Coase : droits de "
  "propriété et coûts de transaction. Heller : anti-communs. Ostrom : communauté locale.",
 ],
}}
