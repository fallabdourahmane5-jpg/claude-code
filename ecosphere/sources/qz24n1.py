# -*- coding: utf-8 -*-
"""Chapitre 24 — questions nouvelles : bilan des rounds et sous-parties institutionnelles."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c24-08
f(id='q24-n01', sp='c24-08', niv='connaitre', type='qcm', b=1421,
  q="De quel ordre de grandeur les droits de douane sur les produits "
    "manufacturés ont-ils reculé dans les économies avancées depuis le début "
    "des négociations commerciales ?",
  opts=["D’environ 40 % à 3 ou 4 %",
        "D’environ 20 % à 10 %",
        "D’environ 15,9 % à 3 %",
        "D’environ 60 % à 20 %"],
  ans=0,
  why=["Un recul de 20 % à 10 % sous-estime très largement l’ampleur du "
       "mouvement.",
       "15,9 % contre 3 % est la comparaison entre agriculture et industrie "
       "en 2019, et non une évolution dans le temps.",
       "60 % à 20 % ne correspond à aucun des ordres de grandeur du cours."],
  exp="Avant les grandes négociations, les droits de douane étaient "
      "particulièrement élevés dans de nombreuses économies industrielles, "
      "avec un ordre de grandeur d’environ 40 % au début du processus. Après "
      "plusieurs décennies de négociations, les droits moyens sur les "
      "produits manufacturés dans les économies avancées se situent autour "
      "de 3 à 4 %. C’est la principale réussite historique du GATT.",
  diss="Prudence immédiate à afficher : il ne faut pas attribuer toute la "
       "croissance du commerce mondial à cette seule libéralisation."),

f(id='q24-n02', sp='c24-08', niv='appliquer', type='assoc', b=1448,
  q="Associez chaque facteur de croissance du commerce mondial entre les "
    "années 1950 et 1980 à sa contribution, dans la décomposition attribuée à "
    "Findlay et O’Rourke (2002).",
  ans=[["La hausse des revenus", "Environ 67 %"],
       ["La réduction des droits de douane", "Environ 25 %"],
       ["La baisse des coûts de transport", "Environ 8 %"]],
  exp="La croissance économique constitue donc le principal moteur de "
      "l’expansion commerciale : lorsque les économies s’enrichissent, elles "
      "échangent davantage. La libéralisation joue un rôle réel mais non "
      "majoritaire, et les innovations logistiques — au premier rang "
      "desquelles la conteneurisation — comptent pour environ 8 %.",
  diss="Leçon de méthode : le GATT et l’OMC ont accompagné et facilité "
       "l’expansion du commerce mondial sans en être les seuls moteurs."),

f(id='q24-n03', sp='c24-08', niv='raisonner', type='courte', b=1448,
  q="Pourquoi serait-il incorrect d’attribuer la croissance du commerce "
    "mondial depuis 1945 à la seule libéralisation commerciale ?",
  ans={'modele': "Parce que la décomposition attribuée à Findlay et O’Rourke "
       "(2002) montre que la réduction des droits de douane n’explique "
       "qu’environ un quart de la croissance du commerce mondial entre les "
       "années 1950 et 1980. La hausse des revenus en explique environ deux "
       "tiers : plus les économies s’enrichissent, plus elles produisent et "
       "consomment, donc plus elles échangent. La baisse des coûts de "
       "transport, portée notamment par la conteneurisation, compte pour "
       "environ 8 %. La croissance du commerce dépend donc simultanément de "
       "la croissance économique, de la technologie et des règles "
       "commerciales. L’implication est importante pour l’évaluation du "
       "multilatéralisme : le GATT puis l’OMC ont accompagné et facilité "
       "l’expansion des échanges plus qu’ils ne l’ont produite, et "
       "symétriquement, leur affaiblissement ne suffira pas à faire "
       "disparaître le commerce mondial.",
       'cles': [{'f': ['25', 'un quart', 'droit de douane'],
                 'l': "la libéralisation n'explique qu'environ 25 %"},
                {'f': ['revenu', 'deux tiers', '67', 'croissance economique'],
                 'l': "la hausse des revenus explique environ deux tiers"},
                {'f': ['transport', 'conteneur', '8'],
                 'l': "la baisse des coûts de transport, environ 8 %"},
                {'f': ['simultan', 'plusieurs facteur', 'combin'],
                 'l': "la croissance du commerce a plusieurs déterminants"},
                {'f': ['accompagne', 'facilite', 'pas le seul moteur',
                       'nuance'],
                 'l': "le multilatéralisme a accompagné plus qu'il n'a produit l'expansion"}]},
  exp="La décomposition présentée dans le cours montre que la libéralisation "
      "commerciale n’explique qu’une partie de la croissance des échanges : la "
      "hausse des revenus joue un rôle plus important encore.",
  diss="Argument à double tranchant très utile : il relativise le succès du "
       "multilatéralisme, mais aussi la portée de son affaiblissement."),

f(id='q24-n04', sp='c24-08', niv='comprendre', type='qcmm', b=1399,
  q="Quels succès le cours attribue-t-il aux cycles de négociation du GATT "
    "puis de l’OMC ? (plusieurs réponses)",
  opts=["Une forte réduction des droits de douane",
        "Une augmentation du nombre de pays participants",
        "Un élargissement des domaines réglementés",
        "Une institutionnalisation du commerce international",
        "La suppression de toute exception sectorielle"],
  ans=[0, 1, 2, 3],
  why=["Exacte : d’environ 40 % à 3 ou 4 % sur les produits manufacturés dans "
       "les économies avancées.",
       "Exacte : de 23 pays en 1947 à 166 membres de l’OMC en 2026.",
       "Exacte : du seul tarif au dumping, aux subventions, aux services et à "
       "la propriété intellectuelle.",
       "Exacte : l’OMC de 1995 remplace un simple accord par une véritable "
       "organisation.",
       "Inexacte : l’agriculture, le textile et le traitement spécial et "
       "différencié montrent au contraire la persistance des exceptions."],
  exp="Le bilan est donc historiquement positif. Mais la réussite de ces "
      "cycles devient progressivement plus difficile à reproduire : la "
      "coopération commerciale se heurte à des intérêts économiques, "
      "politiques et stratégiques divergents, et le multilatéralisme "
      "rencontre les limites de son propre approfondissement.",
  diss="Formule de transition efficace : le succès du multilatéralisme est "
       "aussi la cause de ses difficultés présentes."),

f(id='q24-n05', sp='c24-08', niv='raisonner', type='ordre', b=1557,
  q="Remettez dans l’ordre l’enchaînement qui conduit du succès du "
    "multilatéralisme à sa fragmentation.",
  ans=["Les premiers cycles réunissent peu de pays, aux intérêts "
       "relativement proches, et portent surtout sur les droits de douane",
       "L’élargissement géographique et thématique accroît fortement le "
       "nombre de participants et de sujets",
       "Les différences de développement et d’intérêts stratégiques rendent "
       "les compromis globaux beaucoup plus difficiles",
       "Le cycle de Doha s’enlise, révélant l’impossibilité d’un grand "
       "compromis unique",
       "Les États se tournent vers des cadres plus restreints : accords "
       "régionaux et plurilatéraux",
       "La multiplication de ces accords particuliers fragmente les règles du "
       "commerce international"],
  exp="L’essoufflement du multilatéralisme ne signifie donc pas la "
      "disparition des négociations commerciales, mais leur déplacement vers "
      "des cadres régionaux et plurilatéraux : la recherche d’accords entre "
      "groupes restreints facilite les compromis tout en accentuant la "
      "fragmentation de la gouvernance commerciale mondiale.",
  diss="Enchaînement central du chapitre, utilisable comme plan de partie "
       "entière."),

f(id='q24-n06', sp='c24-08', niv='comprendre', type='qcm', b=1506,
  q="Pourquoi la multiplication des participants a-t-elle compliqué les "
    "négociations commerciales ?",
  opts=["Parce que les réunions deviennent matériellement impossibles à "
        "organiser",
        "Parce que les écarts de développement s’accroissent : les économies "
        "avancées veulent protéger certains secteurs stratégiques et leur "
        "propriété intellectuelle, les pays en développement demandent "
        "davantage d’accès aux marchés et de flexibilités",
        "Parce que les pays en développement refusent de négocier",
        "Parce que le nombre de thèmes diminue"],
  ans=1,
  why=["L’organisation matérielle n’est pas l’obstacle identifié par le "
       "cours.",
       "Les pays en développement négocient activement : ils portent au "
       "contraire l’agenda de Doha.",
       "Le nombre de thèmes augmente au contraire fortement."],
  exp="Les premiers cycles réunissaient un nombre limité de pays aux intérêts "
      "économiques souvent proches. L’élargissement change la nature du "
      "problème : certains États cherchent aussi à préserver leurs capacités "
      "d’intervention publique. Le cycle de Doha illustre particulièrement "
      "cette difficulté, d’autant qu’il combine un grand nombre de "
      "participants et un programme très large.",
  diss="À articuler avec l’engagement unique : plus il y a de sujets, plus "
       "chacun peut bloquer l’ensemble."),

f(id='q24-n07', sp='c24-08', niv='raisonner', type='qcm', b=1532,
  q="Comment le retour des intérêts nationaux fragilise-t-il le "
    "multilatéralisme, selon le cours ?",
  opts=["Les États quittent massivement l’OMC",
        "Lorsque la croissance ralentit et que les tensions géopolitiques "
        "augmentent, les gouvernements subissent des pressions pour protéger "
        "leurs entreprises et les échanges deviennent des instruments de "
        "puissance",
        "Les entreprises refusent d’exporter",
        "Les droits de douane deviennent juridiquement impossibles"],
  ans=1,
  why=["Aucun retrait massif de l’OMC n’est constaté : le nombre de membres "
       "atteint 166 en 2026.",
       "Les entreprises continuent d’exporter : ce sont les règles qui se "
       "fragmentent.",
       "Les droits de douane restent parfaitement praticables, dans la limite "
       "des tarifs consolidés."],
  exp="Les États cherchent alors à sécuriser leurs approvisionnements, à "
      "réduire certaines dépendances et à soutenir leurs entreprises "
      "stratégiques. Le multilatéralisme devient plus difficile à maintenir, "
      "sans que les États renoncent pour autant à négocier : ils le font "
      "simplement dans des cadres plus restreints, ce qui explique le "
      "développement des accords régionaux et plurilatéraux.",
  diss="Distinction à tenir : ce n’est pas la fin de la négociation "
       "commerciale, c’est le changement de son cadre."),

f(id='q24-n08', sp='c24-08', niv='comprendre', type='vf', b=1472,
  q="L’élargissement du GATT puis de l’OMC a renforcé la portée "
    "internationale des règles commerciales communes.",
  ans=True,
  exp="Initialement limité à 23 pays en 1947, le système s’est étendu à la "
      "quasi-totalité des grandes économies : 123 participants concluent "
      "l’Uruguay Round, et l’OMC compte 166 membres en 2026, la Chine "
      "l’ayant rejointe en 2001. De nombreuses économies en transition y ont "
      "également adhéré. Cet élargissement a permis d’étendre les règles "
      "commerciales à une part croissante de l’économie mondiale — mais il a "
      "aussi rendu les compromis globaux beaucoup plus difficiles.",
  diss="Ambivalence à exploiter : le même élargissement constitue à la fois le "
       "deuxième succès du multilatéralisme et l’une des causes de son "
       "blocage."),

f(id='q24-n09', sp='c24-08', niv='raisonner', type='qcm', b=1555,
  q="Quel problème la multiplication des accords plurilatéraux et régionaux "
    "soulève-t-elle ?",
  opts=["Elle rend les compromis plus difficiles à obtenir",
        "Elle peut fragmenter les règles du commerce international et "
        "affaiblir la cohérence du système multilatéral",
        "Elle supprime les droits de douane entre tous les pays",
        "Elle interdit les négociations futures"],
  ans=1,
  why=["Ces accords facilitent au contraire les compromis entre pays aux "
       "intérêts proches : c’est précisément leur attrait.",
       "Ils ne suppriment les droits qu’entre leurs membres, ce qui crée des "
       "discriminations.",
       "Ils n’interdisent aucune négociation future, multilatérale "
       "comprise."],
  exp="Les compromis sont plus faciles à obtenir entre pays partageant "
      "certains intérêts : c’est l’avantage de ces cadres restreints. Mais "
      "chaque accord ajoute ses propres règles, droits, règles d’origine et "
      "procédures, de sorte que la gouvernance commerciale se fragmente — "
      "c’est exactement le « bol de spaghettis » décrit par Bhagwati.",
  diss="Résultat contre-intuitif à mobiliser : les simulations de l’OMC "
       "montrent qu’un monde d’accords préférentiels serait plus coûteux "
       "qu’un monde fragmenté en blocs."),

f(id='q24-n10', sp='c24-08', niv='comprendre', type='qcm', b=1489,
  q="Comment le cours caractérise-t-il l’élargissement des domaines couverts "
    "par les règles internationales ?",
  opts=["Le multilatéralisme se limite désormais aux droits de douane",
        "Le multilatéralisme ne se limite plus à supprimer des barrières : il "
        "organise les conditions de la concurrence internationale",
        "Les règles internationales ne concernent plus que les services",
        "Les négociations abandonnent les pratiques commerciales déloyales"],
  ans=1,
  why=["C’est l’inverse : les négociations ont dépassé le seul tarif.",
       "Les services sont un domaine ajouté, non le seul domaine couvert.",
       "Les pratiques déloyales sont au contraire progressivement encadrées, "
       "dès le Kennedy Round."],
  exp="Initialement, les négociations portaient principalement sur les droits "
      "de douane appliqués aux marchandises ; elles concernent désormais aussi "
      "les pratiques commerciales et de nouveaux secteurs. Cela permet de "
      "construire un cadre de régulation plus complet, mais plus les règles "
      "deviennent nombreuses et complexes, plus les négociations exigent des "
      "compromis difficiles.",
  diss="Formule à retenir : le multilatéralisme rencontre les limites de son "
       "propre approfondissement."),

# ------------------------------------------------------------- c24-15
f(id='q24-n11', sp='c24-15', niv='raisonner', type='ordre', b=2920,
  q="Remettez dans l’ordre le problème d’action collective posé par le "
    "climat.",
  ans=["La stabilité climatique est non rivale : si un pays en bénéficie, "
       "cela n’empêche pas les autres d’en bénéficier",
       "Elle est difficilement excluable : on ne peut la réserver aux pays "
       "ayant financé les réductions d’émissions",
       "Si un pays réduit ses émissions, le bénéfice est mondial alors que le "
       "coût est national",
       "Chaque État a donc une incitation individuelle à laisser les autres "
       "agir",
       "Le bien public climatique est produit en quantité insuffisante"],
  exp="C’est le problème classique du passager clandestin, appliqué au bien "
      "public mondial le plus évident. La sortie de ce piège suppose qu’un "
      "acteur accepte de jouer un rôle moteur. Le cours suggère que l’Union "
      "européenne pourrait partiellement remplir ce rôle, non par la "
      "puissance militaire ou technologique, mais par la taille de son "
      "marché.",
  diss="Enchaînement identique à celui de la gouvernance commerciale : c’est "
       "ce qui justifie de traiter les deux dans le même chapitre."),

f(id='q24-n12', sp='c24-15', niv='comprendre', type='qcm', b=2940,
  q="Sur quel mécanisme repose la puissance régulatrice de l’Union européenne "
    "par son marché ?",
  opts=["Elle subventionne les entreprises étrangères qui respectent ses "
        "normes",
        "De nombreuses entreprises étrangères ne pouvant renoncer à un marché "
        "de 450 millions de consommateurs au niveau de vie élevé, l’Union peut "
        "conditionner l’accès au respect de ses normes",
        "Elle impose ses normes par des accords militaires",
        "Elle interdit les importations de tous les pays non conformes"],
  ans=1,
  why=["Aucune subvention aux entreprises étrangères n’est en cause.",
       "L’Union ne dispose pas de ce type de levier militaire : c’est "
       "précisément sa faiblesse relative.",
       "Il n’y a pas d’interdiction générale : c’est l’accès conditionné qui "
       "produit l’effet."],
  exp="L’Union impose donc indirectement certaines de ses normes : une "
      "entreprise qui veut vendre en Europe adapte ses produits, et souvent "
      "ses procédés, aux exigences européennes — y compris pour ses autres "
      "marchés, par économie d’échelle. Cette logique devient particulièrement "
      "importante en matière climatique, puisqu’elle peut conduire les "
      "producteurs étrangers à réduire l’intensité carbone de leurs "
      "productions.",
  diss="Mécanisme à nommer précisément : la taille du marché se convertit en "
       "pouvoir normatif, faute de pouvoir se convertir en puissance "
       "géopolitique."),

f(id='q24-n13', sp='c24-15', niv='appliquer', type='ordre', b=2967,
  q="Remettez dans l’ordre le fonctionnement et l’effet attendu du MACF.",
  ans=["Les producteurs européens supportent un coût carbone, via le système "
       "d’échange de quotas",
       "Sans mécanisme aux frontières, la production étrangère moins taxée "
       "bénéficierait d’un avantage de coût",
       "Le MACF aligne progressivement le coût carbone de certaines "
       "importations sur celui supporté dans l’Union",
       "Les fuites de carbone sont évitées, puisque délocaliser ne permet "
       "plus d’échapper au prix du carbone",
       "Les producteurs étrangers ont intérêt à décarboner pour conserver "
       "leur accès au marché européen"],
  exp="Le MACF illustre la capacité de l’Union européenne à transformer la "
      "taille de son marché en puissance normative. Son objet n’est pas de "
      "protéger les producteurs européens en général, mais d’éviter qu’une "
      "politique climatique ambitieuse ne les pénalise face à des "
      "concurrents soumis à un prix du carbone plus faible.",
  diss="Lecture à deux niveaux, indispensable en dissertation : instrument "
       "climatique vu de Bruxelles, barrière commerciale vue de ses "
       "partenaires."),

f(id='q24-n14', sp='c24-15', niv='raisonner', type='qcm', b=2877,
  q="Pourquoi la coopération multilatérale renforcée bénéficierait-elle "
    "surtout aux économies petites et pauvres, d’après les simulations de "
    "l’OMC ?",
  opts=["Parce qu’elles exportent davantage que les grandes économies",
        "Parce qu’elles disposent du plus faible pouvoir de négociation "
        "bilatéral et bénéficient donc le plus de règles universelles et non "
        "discriminatoires",
        "Parce qu’elles reçoivent des transferts financiers de l’OMC",
        "Parce qu’elles sont exemptées de droits de douane"],
  ans=1,
  why=["Leur volume d’exportations est au contraire faible en valeur "
       "absolue.",
       "L’OMC n’effectue pas de transferts financiers : ce n’est pas une "
       "banque de développement.",
       "Aucune exemption générale de droits n’existe, même si le SGP accorde "
       "des préférences."],
  exp="Le gain de PIB pourrait atteindre environ +7,7 % pour les pays les "
      "moins avancés, contre +2,9 % pour le monde. La logique est simple : "
      "dans un système de règles universelles, un petit pays obtient les "
      "mêmes conditions qu’un grand ; dans un monde d’accords bilatéraux, il "
      "négocie en position de faiblesse. La coopération universelle réduit "
      "les discriminations commerciales et permet d’exploiter davantage les "
      "gains de spécialisation.",
  diss="Argument d’équité décisif : le multilatéralisme protège les faibles "
       "mieux que le bilatéralisme."),

f(id='q24-n15', sp='c24-15', niv='raisonner', type='courte', b=2877,
  q="Pourquoi un monde organisé uniquement par des accords de libre-échange "
    "serait-il plus coûteux qu’un monde fragmenté en blocs, selon les "
    "simulations de l’OMC ?",
  ans={'modele': "Parce que ce qui coûte cher n’est pas seulement la "
       "restriction des échanges, c’est aussi la fragmentation des règles. "
       "Dans le scénario des accords préférentiels généralisés, chaque "
       "accord fixe ses propres droits, règles d’origine, normes et "
       "procédures : le « bol de spaghettis » devient encore plus important, "
       "les économies extérieures à chaque accord sont discriminées, et la "
       "complexité administrative pèse sur toutes les entreprises. Les "
       "simulations donnent −6,9 % de PIB mondial et −26,9 % d’exportations "
       "pour ce scénario, contre −5,1 % et −18,6 % pour le scénario "
       "géopolitiquement fragmenté. À l’inverse, une coopération "
       "multilatérale renforcée produirait +2,9 % de PIB mondial et +17,9 % "
       "d’exportations, et jusqu’à +7,7 % de PIB pour les pays les moins "
       "avancés. La conclusion est que l’unité des règles a une valeur propre, "
       "indépendante du degré d’ouverture.",
       'cles': [{'f': ['fragmentation des regle', 'propres regle', 'spaghetti'],
                 'l': "la fragmentation des règles, et non la seule fermeture"},
                {'f': ['discrimin', 'exterieur', 'preferentiel'],
                 'l': "la discrimination des économies extérieures aux accords"},
                {'f': ['6,9', '26,9', 'coute'],
                 'l': "−6,9 % de PIB et −26,9 % d'exportations"},
                {'f': ['5,1', '18,6', 'fragmente', 'bloc'],
                 'l': "contre −5,1 % et −18,6 % pour le scénario en blocs"},
                {'f': ['2,9', '17,9', '7,7', 'cooperation renforcee'],
                 'l': "une coopération renforcée produirait au contraire des gains"},
                {'f': ['unite', 'universel', 'coherence', 'valeur propre'],
                 'l': "l'unité des règles a une valeur propre"}]},
  exp="Les accords préférentiels fragmentent les règles, discriminent les "
      "économies extérieures et amplifient le « bol de spaghettis » : le "
      "scénario correspondant est plus coûteux que celui d’un monde "
      "géopolitiquement fragmenté.",
  diss="Résultat le plus contre-intuitif du chapitre, donc le plus "
       "valorisable : plus d’accords de libre-échange n’équivaut pas à plus "
       "de libre-échange."),

f(id='q24-n16', sp='c24-15', niv='comprendre', type='vf', b=2924,
  q="La sortie du piège du passager clandestin climatique suppose qu’un "
    "acteur accepte de jouer un rôle moteur.",
  ans=True,
  exp="C’est la conclusion que le cours tire de l’analyse en termes de bien "
      "public mondial : puisque chaque État a une incitation individuelle à "
      "laisser les autres agir, l’action collective ne s’organise pas "
      "spontanément. Il faut donc un acteur disposé à supporter une part "
      "disproportionnée du coût initial — exactement la fonction que "
      "Kindleberger attribue au leader hégémonique. L’Union européenne "
      "pourrait partiellement remplir ce rôle dans le domaine climatique, non "
      "par la puissance militaire ou technologique mais par la taille de son "
      "marché.",
  diss="Pont explicite entre les deux moitiés du chapitre : le climat exige "
       "ce que Kindleberger décrivait pour le commerce."),

]
