# -*- coding: utf-8 -*-
"""Ensemble 28 — cinquième série : instruments non tarifaires et politiques
sectorielles."""

from doss_base import d

# ---------------------------------------------------------------- 28.14
d('le28-non-tarifaire', 28,
  "Protectionnisme non tarifaire : quotas, licences, normes et procédures",
  "Une protection moins visible, moins mesurable et plus difficile à négocier",
  "Le protectionnisme non tarifaire regroupe toutes les entraves aux échanges "
  "qui ne passent pas par un droit de douane : quotas limitant les volumes "
  "importés, licences d’importation, normes techniques, sanitaires ou "
  "environnementales, exigences de contenu local, procédures administratives "
  "et délais douaniers. Ces mesures modifient elles aussi les prix relatifs et "
  "redistribuent les surplus, mais leur effet protecteur est beaucoup plus "
  "difficile à chiffrer.",
  "La montée des barrières non tarifaires est la conséquence directe du succès "
  "des négociations tarifaires : à mesure que les droits de douane sur les "
  "produits manufacturés tombaient vers 4 %, les obstacles restants sont devenus "
  "essentiellement réglementaires. Lawrence en tire la conséquence théorique en "
  "distinguant l’intégration superficielle, qui supprime les barrières situées "
  "aux frontières, de l’intégration profonde, qui rapproche les règles internes. "
  "Trois propriétés distinguent économiquement ces instruments du tarif. "
  "Premièrement, le quota crée une rente privée plutôt qu’une recette publique : "
  "la différence entre le prix intérieur et le prix mondial revient à celui qui "
  "détient la licence d’importation, et non à l’État. Deuxièmement, le quota "
  "fixe les volumes et laisse les prix s’ajuster, ce qui le rend plus rigide "
  "qu’un tarif : si la demande augmente, le prix intérieur monte sans limite, "
  "alors qu’un droit de douane laisse les importations croître. Troisièmement, "
  "la norme est ambiguë par construction : elle peut poursuivre un objectif "
  "légitime de santé, de sécurité ou d’environnement tout en produisant un effet "
  "protecteur, et il est souvent impossible de démêler les deux. C’est cette "
  "ambiguïté qui en fait l’instrument privilégié du protectionnisme "
  "contemporain : une norme n’apparaît pas dans les statistiques de protection "
  "et se défend toujours par son objectif affiché.",
  [("Le contingentement des volumes",
    "Le quota fixe une quantité maximale importable. L’offre totale étant "
    "limitée, le prix intérieur s’élève jusqu’à équilibrer la demande, ce qui "
    "protège les producteurs nationaux sans qu’aucun impôt ne soit perçu."),
   ("La création d’une rente de licence",
    "L’écart entre le prix intérieur et le prix mondial revient au détenteur de "
    "l’autorisation d’importer. Cette rente privée explique que l’attribution "
    "des licences devienne elle-même un enjeu, et une source de corruption "
    "potentielle."),
   ("L’effet protecteur des normes",
    "Une exigence technique, sanitaire ou environnementale impose un coût "
    "d’adaptation aux producteurs étrangers, parfois supérieur à celui que "
    "supportent les producteurs nationaux déjà conformes. L’accès au marché est "
    "restreint sans qu’aucune barrière commerciale ne soit affichée."),
   ("Le coût des procédures",
    "Délais douaniers, formalités, certifications multiples renchérissent "
    "l’importation et pénalisent particulièrement les petites entreprises et les "
    "pays dont l’administration est peu outillée."),
   ("La difficulté de la négociation",
    "Un tarif se chiffre et s’échange ; une norme se discute. La libéralisation "
    "non tarifaire suppose une harmonisation ou une reconnaissance mutuelle des "
    "règles internes, donc une négociation sur la souveraineté réglementaire.")],
  [{'a': "Les normes peuvent poursuivre des objectifs légitimes de santé, de "
         "sécurité ou d’environnement que le libre jeu du marché ne garantirait "
         "pas.",
    'cond': "La norme doit être fondée scientifiquement, appliquée "
            "indifféremment aux producteurs nationaux et étrangers, et "
            "proportionnée au risque qu’elle traite.",
    'lim': "Ces trois critères sont difficiles à vérifier, ce qui laisse une "
           "marge considérable pour un protectionnisme déguisé et nourrit les "
           "contentieux commerciaux."},
   {'a': "Le quota offre un contrôle précis du volume importé, utile lorsqu’un "
         "afflux brutal menace une branche.",
    'cond': "L’usage doit être temporaire, justifié par un afflux établi et "
            "encadré juridiquement, comme dans le cadre d’une clause de "
            "sauvegarde assortie d’une échéance.",
    'lim': "Contrairement au tarif, il ne laisse pas les importations s’ajuster "
           "à la demande : en cas de choc, le prix intérieur s’envole et le coût "
           "pour les consommateurs devient incontrôlé."},
   {'a': "L’exigence de normes communes peut faciliter les échanges lorsqu’elle "
         "remplace une multiplicité de règles nationales divergentes.",
    'cond': "Il faut une harmonisation ou une reconnaissance mutuelle "
            "effectives, ce que seule une intégration régionale profonde permet "
            "généralement d’obtenir.",
    'lim': "L’harmonisation se fait rarement à égalité : la puissance "
           "réglementaire la plus importante impose souvent ses standards aux "
           "autres."}],
  [{'t': "Les barrières non tarifaires sont moins visibles donc moins "
         "contestables, ce qui en fait l’instrument privilégié du "
         "protectionnisme contemporain.",
    'qui': "Constat découlant de la distinction de Lawrence entre intégration "
           "superficielle et intégration profonde.",
    'rep': "L’opacité est réelle, mais elle ne suffit pas à disqualifier des "
           "mesures dont certaines répondent à des préférences collectives "
           "légitimes : le problème est celui du contrôle, non de l’existence."},
   {'t': "Le quota est économiquement inférieur au tarif, puisqu’il transfère la "
         "rente à des opérateurs privés au lieu de l’État.",
    'qui': "Résultat classique de l’analyse en surplus.",
    'rep': "L’argument est exact, et il explique pourquoi la conversion des "
           "quotas en droits de douane a constitué un objectif des négociations "
           "multilatérales."},
   {'t': "Les normes protègent les producteurs nationaux plus que les "
         "consommateurs qu’elles invoquent.",
    'qui': "Soupçon récurrent dans les contentieux commerciaux, lié à "
           "l’ambiguïté intrinsèque de l’instrument.",
    'rep': "Le critère de départage est opérationnel : une norme réellement "
           "protectrice des consommateurs s’applique de la même façon aux "
           "produits nationaux ; si elle ne vise que l’importation, l’objectif "
           "affiché est douteux."}],
  [{'n': "Robert Lawrence",
    'i': "L’intégration profonde porte sur les règles internes, non sur les "
         "barrières frontalières.",
    'p': "Regionalism, Multilateralism and Deeper Integration (1996) : à mesure "
         "que les droits de douane baissent, les obstacles pertinents deviennent "
         "les normes sociales, environnementales, sanitaires, les règles de "
         "concurrence et de marchés publics."},
   {'n': "Robert Lawrence",
    'i': "La profondeur réglementaire est plus facile à atteindre entre un petit "
         "nombre de partenaires proches.",
    'p': "Cela explique mécaniquement pourquoi l’intégration profonde progresse "
         "au niveau régional pendant que le multilatéralisme s’enlise : harmoniser "
         "des règles internes suppose une homogénéité de préférences que 166 "
         "membres n’ont pas."},
   {'n': "Jagdish Bhagwati",
    'i': "La multiplication des règles d’origine et des normes propres à chaque "
         "accord engendre un « bol de spaghettis ».",
    'p': "Le coût n’est plus tarifaire mais administratif : une même entreprise "
         "doit établir la conformité de son produit à des règles différentes "
         "selon le marché visé, ce qui pèse surtout sur les petites structures."}],
  [{'f': "Le régime de quotas textiles de l’accord multifibres, entré en vigueur "
         "en 1974, a pris fin le 1ᵉʳ janvier 2005 au terme d’un démantèlement de "
         "dix ans décidé à l’Uruguay Round.",
    'p': "L’exemple montre la longévité d’un instrument non tarifaire et la "
         "lenteur de sa suppression, alors même que les tarifs avaient été "
         "négociés beaucoup plus vite."},
   {'f': "Le cours cite parmi les instruments protectionnistes contemporains les "
         "quotas, les normes, le contenu local et les subventions.",
    'p': "L’énumération montre que la protection s’est déplacée du tarif vers "
         "des instruments moins mesurables, ce qui complique l’évaluation du "
         "degré réel d’ouverture d’une économie."}],
  [{'q': "Sujet du type « Les normes protègent-elles les consommateurs ou les "
         "producteurs nationaux ? »",
    'f': "La norme est ambiguë par construction : elle peut servir un objectif "
         "collectif légitime tout en produisant un effet protecteur, et rien "
         "dans sa forme ne permet de trancher. Le critère de départage est "
         "l’application indifférenciée : une norme qui s’impose aussi aux "
         "producteurs nationaux poursuit vraisemblablement son objectif affiché ; "
         "une exigence qui ne vise en pratique que l’importation ne le fait pas.",
    'r': "On substitue à un débat d’intention un critère observable, ce qui "
         "permet de traiter des cas concrets au lieu de rester dans la "
         "suspicion générale.",
    'ex': "Le mécanisme d’ajustement carbone aux frontières tient compte du prix "
          "du carbone déjà payé à l’étranger, précisément pour rester une "
          "mesure d’égalisation et non une barrière."},
   {'q': "Sujet du type « Le protectionnisme a-t-il reculé ? »",
    'f': "Mesurer le protectionnisme par le seul droit de douane conduit à "
         "surestimer l’ouverture : la baisse des tarifs de 40 % à 4 % sur les "
         "manufactures s’est accompagnée d’un déplacement de la protection vers "
         "des instruments réglementaires qui n’apparaissent dans aucune "
         "statistique tarifaire.",
    'r': "Le raisonnement porte sur l’instrument de mesure lui-même, ce qui "
         "permet de montrer qu’une même statistique peut décrire une ouverture "
         "apparente et une protection déplacée.",
    'ex': "La distinction de Lawrence entre intégration superficielle et "
          "intégration profonde."}],
  voisins=['le28-droits-douane', 'le28-contenu-local', 'le28-environnemental',
           'le28-social', 'le28-marches-publics', 'le28-protectionnisme'])

# ---------------------------------------------------------------- 28.15
d('le28-subventions', 28, "Subventions à la production et aux exportations",
  "Faire payer le contribuable plutôt que le consommateur",
  "Une subvention est un transfert public accordé à un producteur national, sous "
  "forme d’aide directe, de crédit d’impôt, de prêt bonifié ou de financement de "
  "la recherche. La subvention à la production abaisse le coût du producteur sur "
  "son marché intérieur ; la subvention à l’exportation abaisse le prix auquel "
  "il peut vendre à l’étranger. Dans les deux cas, l’avantage est financé par le "
  "budget et non par le prix payé par le consommateur.",
  "La subvention est devenue l’instrument central du protectionnisme "
  "contemporain, et il faut comprendre pourquoi. Économiquement d’abord : à "
  "objectif de soutien donné, elle introduit moins de distorsions qu’un droit de "
  "douane, puisqu’elle ne renchérit pas le prix à la consommation et ne pénalise "
  "pas les entreprises utilisatrices du bien. Politiquement ensuite : son coût "
  "est budgétaire, donc diffus et peu visible, là où un droit de douane se "
  "traduit immédiatement en hausse de prix. Juridiquement enfin : elle est plus "
  "difficile à qualifier et à sanctionner qu’une barrière à la frontière. C’est "
  "d’ailleurs l’instrument que mobilisent, en pratique, les politiques "
  "commerciales stratégiques — le cours précise que l’instrument étudié par "
  "Brander et Spencer relève largement de la subvention, notamment à la "
  "recherche. Mais la subvention appelle deux objections sérieuses. La première "
  "est budgétaire : ce qui est versé à un secteur n’est pas disponible "
  "ailleurs, et l’éviction porte aussi sur les facteurs rares — ingénieurs, "
  "capital, foncier industriel. La seconde est stratégique : parce qu’elle est "
  "efficace, elle est imitable, et la généralisation des soutiens produit une "
  "surenchère dont personne ne sort gagnant. C’est exactement ce que décrivent "
  "l’Inflation Reduction Act américain et la réponse européenne.",
  [("L’abaissement du coût privé",
    "L’aide réduit le coût supporté par le producteur, ce qui lui permet de "
    "vendre moins cher, d’investir davantage ou de supporter des pertes "
    "initiales le temps d’atteindre son échelle."),
   ("Le déplacement de la charge vers le contribuable",
    "Contrairement au droit de douane, le coût n’est pas supporté par "
    "l’acheteur du bien mais par le budget public : la distorsion de prix à la "
    "consommation disparaît, la contrainte budgétaire la remplace."),
   ("L’effet sur la concurrence internationale",
    "Un producteur subventionné affronte ses concurrents étrangers avec un coût "
    "artificiellement abaissé. Ceux-ci perdent des parts de marché sans que leur "
    "efficacité ait changé, d’où la qualification de distorsion de concurrence."),
   ("La riposte par les droits compensateurs",
    "Les règles commerciales permettent de relever temporairement les droits de "
    "douane pour neutraliser l’avantage conféré par une subvention étrangère : "
    "ce sont les droits compensateurs."),
   ("La surenchère",
    "Parce que la subvention est efficace et difficile à sanctionner, les "
    "partenaires l’imitent. Chacun dépense pour conserver sa position, et "
    "l’avantage relatif recherché s’annule tandis que les coûts budgétaires "
    "s’accumulent.")],
  [{'a': "À objectif donné, la subvention est moins coûteuse en efficience qu’un "
         "droit de douane, puisqu’elle ne distord pas le prix à la consommation.",
    'cond': "Le financement doit être assuré sans prélèvement lui-même très "
            "distorsif, et l’aide doit viser la production et non la survie.",
    'lim': "L’avantage disparaît si la dépense évince des usages publics plus "
           "productifs ou si elle est financée par un endettement coûteux."},
   {'a': "Elle permet de soutenir une industrie naissante sans pénaliser les "
         "entreprises situées en aval, qui continuent de s’approvisionner au "
         "prix mondial.",
    'cond': "Le soutien doit être temporaire et conditionné à des résultats "
            "vérifiables : production, productivité, exportations.",
    'lim': "La conditionnalité est rarement appliquée avec rigueur, et une aide "
           "reconduite produit les mêmes effets de rente qu’une protection "
           "tarifaire permanente."},
   {'a': "Elle peut corriger une externalité positive, lorsque la recherche "
         "d’une entreprise bénéficie à l’ensemble de l’économie.",
    'cond': "L’externalité doit être réelle et le montant de l’aide proportionné "
            "à l’écart entre rendement privé et rendement social.",
    'lim': "L’argument d’externalité est invoqué bien au-delà des cas où il "
           "s’applique, et sert souvent d’habillage à un soutien sectoriel "
           "ordinaire."}],
  [{'t': "La subvention fausse la concurrence internationale au détriment de "
         "producteurs étrangers plus efficaces.",
    'qui': "Fondement juridique des droits compensateurs, décrits dans le cours.",
    'rep': "L’objection est recevable, mais elle vaut symétriquement : un pays "
           "dont les concurrents sont subventionnés subit lui aussi une "
           "distorsion. D’où la logique de compensation plutôt que "
           "d’interdiction pure."},
   {'t': "Les subventions déclenchent une course aux aides publiques qui épuise "
         "les budgets sans modifier les positions relatives.",
    'qui': "Conséquence du caractère non coopératif de l’instrument, illustrée "
           "par la réponse européenne à l’Inflation Reduction Act.",
    'rep': "C’est un dilemme classique : la mesure est rationnelle "
           "individuellement et destructrice collectivement, ce qui appelle une "
           "coordination internationale plutôt qu’un renoncement unilatéral."},
   {'t': "La subvention est moins visible que le tarif, donc moins contrôlée "
         "démocratiquement : son coût n’apparaît pas dans les prix et se dilue "
         "dans la masse du budget public.",
    'qui': "Conséquence du déplacement de la charge vers le budget.",
    'rep': "L’objection plaide pour une évaluation publique systématique des "
           "aides, pas contre l’instrument : un droit de douane est visible mais "
           "son coût réel pour les consommateurs ne l’est pas davantage."}],
  [{'n': "James Brander",
    'i': "La politique commerciale stratégique passe en pratique par la "
         "subvention plus que par le tarif.",
    'p': "Avec Barbara Spencer (1983), le soutien public à la recherche modifie "
         "le calcul du concurrent étranger dans un oligopole : il s’agit moins "
         "de bloquer une importation que de rendre crédible l’engagement du "
         "producteur national."},
   {'n': "Barbara Spencer",
    'i': "L’engagement public doit être crédible et antérieur à la décision du "
         "rival.",
    'p': "La subvention n’a d’effet dissuasif que si le concurrent la tient pour "
         "acquise au moment où il décide d’investir : c’est la crédibilité de "
         "l’engagement, et non son montant, qui produit le résultat."},
   {'n': "Arthur Pigou",
    'i': "Une subvention peut corriger une externalité positive en rapprochant "
         "le rendement privé du rendement social.",
    'p': "La justification est allocative et non stratégique : elle vaut lorsque "
         "l’activité produit des bénéfices que son auteur ne capte pas, "
         "typiquement la recherche, et non lorsqu’il s’agit de capter un profit "
         "au détriment d’un concurrent."}],
  [{'f': "L’Inflation Reduction Act lie certaines aides et bonifications au "
         "contenu local : plus la chaîne de valeur est localisée aux États-Unis, "
         "plus l’aide est importante.",
    'p': "L’exemple montre la combinaison contemporaine d’un objectif "
         "écologique, d’un objectif industriel et d’un objectif de souveraineté "
         "dans un même instrument budgétaire."},
   {'f': "Le projet européen d’Industrial Accelerator Act du 4 mars 2026 combine "
         "préférence européenne dans les marchés publics et les aides, "
         "conditionnement de certains investissements étrangers et exigences de "
         "transfert technologique, avec un objectif de 20 % du PIB européen pour "
         "l’industrie d’ici 2035.",
    'p': "La réponse européenne illustre la dynamique de surenchère : une "
         "politique de soutien en appelle une autre."},
   {'f': "Les règles commerciales prévoient des droits compensateurs permettant "
         "de relever temporairement les droits de douane face à une subvention "
         "étrangère.",
    'p': "L’existence de cet instrument montre que la subvention est reconnue "
         "comme une distorsion commerciale, et non comme une simple politique "
         "interne."}],
  [{'q': "Sujet du type « Les subventions peuvent-elles être plus efficaces que "
         "les droits de douane ? »",
    'f': "La subvention domine le droit de douane sur trois plans : elle ne "
         "renchérit pas le prix à la consommation, elle ne pénalise pas les "
         "entreprises utilisatrices du bien soutenu, et elle cible directement "
         "l’activité qu’on veut développer. Son coût est cependant budgétaire, "
         "donc contraint, et son efficacité même la rend imitable, ce qui "
         "déclenche une surenchère.",
    'r': "La comparaison se mène instrument par instrument sur l’incidence, le "
         "nombre de distorsions et la réaction attendue des partenaires.",
    'ex': "Brander et Spencer raisonnent sur un instrument relevant largement de "
          "la subvention à la recherche."},
   {'q': "Sujet du type « L’État peut-il choisir les secteurs d’avenir ? »",
    'f': "La subvention rend le choix sectoriel opérationnel, mais elle en "
         "révèle aussi la difficulté : contrairement au droit de douane, qui "
         "répond à une demande de protection, elle suppose une anticipation sur "
         "les technologies qui compteront, et son coût est engagé avant tout "
         "résultat.",
    'r': "On relie l’instrument à la question informationnelle : la subvention "
         "exige davantage de connaissance que la protection, ce qui en fait un "
         "pari plus exigeant.",
    'ex': "L’objectif européen de 20 % du PIB industriel en 2035 suppose "
          "d’identifier aujourd’hui les filières qui l’atteindront."}],
  voisins=['le28-politique-strategique', 'le28-offensif', 'le28-droits-douane',
           'le28-contenu-local', 'le28-agricole', 'le28-dumping'])

# ---------------------------------------------------------------- 28.16
d('le28-politique-strategique', 28, "Politique commerciale stratégique",
  "Déplacer un profit oligopolistique vers la firme nationale",
  "La politique commerciale stratégique désigne l’utilisation de l’intervention "
  "publique pour modifier l’issue de la concurrence entre quelques grandes "
  "firmes internationales. Développée par James Brander et Barbara Spencer dans "
  "International R&D Rivalry and Industrial Strategy (1983), elle ne vise pas à "
  "protéger une industrie existante mais à faire en sorte que le profit "
  "disponible dans un secteur oligopolistique revienne à la firme nationale "
  "plutôt qu’à sa rivale étrangère.",
  "Le raisonnement suppose une structure de marché très particulière, et c’est "
  "la première chose à poser : un secteur où les coûts fixes sont si élevés — "
  "recherche, développement, capacités de production — que le marché mondial ne "
  "peut rentabiliser qu’un petit nombre de producteurs. Dans cette "
  "configuration, l’entrée de la seconde firme rend les deux déficitaires : "
  "celle qui investit la première, ou celle dont l’engagement est le plus "
  "crédible, prend tout. L’intervention publique agit alors sur les "
  "anticipations plutôt que sur les coûts observés : en s’engageant de façon "
  "crédible à soutenir sa firme, l’État rend l’entrée non rentable pour le "
  "rival étranger, qui renonce. Le profit oligopolistique revient à la firme "
  "nationale, et le gain pour le pays peut excéder le coût de la subvention. Le "
  "point essentiel pour une copie est la nature de ce gain : il ne s’agit pas "
  "d’une création de valeur mais d’un transfert international. Le pays gagne ce "
  "que l’autre perd, ce qui explique trois propriétés du modèle. Il est "
  "non coopératif, donc générateur de représailles. Il n’est applicable que dans "
  "des oligopoles identifiés, non dans des secteurs concurrentiels. Et il "
  "suppose une information dont l’État dispose rarement : connaître les coûts et "
  "les intentions du rival. Le cours souligne enfin que l’instrument mobilisé "
  "relève en pratique largement de la subvention, notamment à la recherche.",
  [("L’identification d’un marché oligopolistique",
    "Le secteur doit comporter des coûts fixes tels que seul un petit nombre de "
    "producteurs puisse être rentable à l’échelle mondiale. C’est cette rareté "
    "des places qui crée le profit à capter."),
   ("L’engagement public crédible",
    "L’État annonce un soutien — subvention, financement de la recherche, "
    "commande publique — de manière suffisamment ferme pour que le concurrent "
    "étranger le tienne pour acquis dans son propre calcul."),
   ("Le renoncement du rival",
    "Anticipant un concurrent soutenu, la firme étrangère conclut que son "
    "investissement ne serait pas rentable et renonce. Aucune barrière n’a été "
    "érigée : c’est l’anticipation qui a produit l’effet."),
   ("La captation du profit",
    "La firme nationale occupe seule la position rentable. Le profit réalisé "
    "peut excéder le montant de la subvention, auquel cas l’opération est "
    "gagnante pour le pays pris globalement."),
   ("La riposte symétrique",
    "Si l’État étranger raisonne de même et s’engage lui aussi, les deux firmes "
    "investissent, le marché ne rentabilise pas les deux, et les deux pays "
    "supportent le coût de leur soutien sans capter le profit espéré.")],
  [{'a': "Dans un oligopole, un engagement public crédible peut transférer un "
         "profit important vers la firme nationale à un coût budgétaire "
         "inférieur.",
    'cond': "Le marché doit réellement être oligopolistique, l’engagement doit "
            "précéder la décision du rival et être perçu comme irréversible.",
    'lim': "Le gain est un transfert et non une création : il suppose que le "
           "partenaire subisse une perte équivalente, ce qui rend la mesure "
           "instable."},
   {'a': "Le soutien à la recherche produit en outre des externalités "
         "technologiques qui bénéficient à l’ensemble de l’économie.",
    'cond': "Il faut que les connaissances produites diffusent effectivement "
            "au-delà de la firme soutenue, par la mobilité des chercheurs, les "
            "publications ou les fournisseurs.",
    'lim': "Cette justification est allocative et non stratégique : elle "
           "légitime le soutien à la recherche en général, pas le ciblage d’un "
           "champion national."},
   {'a': "L’instrument est compatible avec le maintien de l’ouverture, puisqu’il "
         "n’érige aucune barrière à la frontière.",
    'cond': "Encore faut-il que les partenaires ne le qualifient pas de "
            "subvention prohibée et ne ripostent pas par des droits "
            "compensateurs.",
    'lim': "L’absence de barrière visible ne supprime pas le conflit : elle le "
           "déplace du terrain douanier vers le terrain des aides d’État."}],
  [{'t': "Le modèle exige une information que l’État ne possède pas : coûts, "
         "intentions et calendrier du rival étranger.",
    'qui': "Objection informationnelle classique adressée au modèle.",
    'rep': "Elle est sérieuse et restreint fortement le champ d’application. "
           "Elle n’annule pas le raisonnement dans les cas où la structure de "
           "l’industrie est bien connue, typiquement l’aéronautique ou les "
           "semi-conducteurs."},
   {'t': "Généralisée, la politique commerciale stratégique conduit à une "
         "surenchère de soutiens où chacun dépense sans capter de profit.",
    'qui': "Conséquence directe du caractère non coopératif du modèle.",
    'rep': "C’est une situation de dilemme : chaque État a intérêt à intervenir, "
           "le résultat collectif est inférieur. Seule une coordination — ou une "
           "discipline multilatérale sur les subventions — permet d’en sortir."},
   {'t': "Le gain national peut être capté par les actionnaires de la firme "
         "soutenue plutôt que par la collectivité qui a financé le soutien.",
    'qui': "Objection distributive, liée à l’absence de contrepartie dans de "
           "nombreux dispositifs d’aide.",
    'rep': "Elle plaide pour conditionner les aides — localisation de la "
           "production, emploi, partage de la propriété intellectuelle — comme "
           "le prévoit le projet européen d’Industrial Accelerator Act."}],
  [{'n': "James Brander",
    'i': "L’intervention publique modifie stratégiquement la concurrence entre "
         "quelques grandes firmes internationales.",
    'p': "International R&D Rivalry and Industrial Strategy (1983), avec Barbara "
         "Spencer. Le déplacement du raisonnement est décisif : on ne protège "
         "plus une industrie, on change l’issue d’un jeu entre firmes."},
   {'n': "Barbara Spencer",
    'i': "L’instrument pertinent relève largement de la subvention, notamment à "
         "la recherche, plutôt que du droit de douane.",
    'p': "Ce point est explicitement souligné dans le cours : la politique "
         "commerciale stratégique est une politique industrielle avant d’être "
         "une politique douanière, ce qui explique sa forme contemporaine."},
   {'n': "Paul Krugman",
    'i': "Les rendements croissants rendent possible qu’un soutien initial "
         "détermine durablement la localisation d’une industrie.",
    'p': "Lorsque le coût moyen décroît avec la production cumulée, la firme "
         "qui démarre la première conserve l’avantage : la politique publique "
         "peut alors fixer une position que le marché aurait attribuée au "
         "hasard de l’histoire."}],
  [{'f': "Le cours précise que l’instrument étudié par Brander et Spencer relève "
         "en pratique largement de la subvention.",
    'p': "La précision est importante : elle relie directement un modèle de 1983 "
         "aux politiques industrielles contemporaines, qui passent par le budget "
         "et non par la douane."},
   {'f': "Le projet européen d’Industrial Accelerator Act prévoit préférence "
         "européenne dans les marchés publics, conditionnement des "
         "investissements étrangers et exigences de transfert technologique.",
    'p': "Les instruments décrits correspondent précisément à la boîte à outils "
         "de la politique commerciale stratégique, appliquée à l’échelle d’une "
         "union régionale plutôt que d’un État."}],
  [{'q': "Sujet du type « L’État peut-il choisir les secteurs d’avenir ? »",
    'f': "La politique commerciale stratégique fournit la version la plus "
         "rigoureuse de l’argument interventionniste : dans un oligopole où le "
         "profit n’est accessible qu’à un petit nombre de firmes, l’engagement "
         "public crédible peut en déterminer le bénéficiaire. Mais elle en "
         "montre aussi les limites, puisqu’elle exige de connaître la structure "
         "du marché, les coûts du rival et sa réaction.",
    'r': "On passe d’un débat doctrinal sur le rôle de l’État à l’examen des "
         "conditions informationnelles et structurelles de l’intervention.",
    'ex': "Brander et Spencer (1983), appliqué aux secteurs à très forts coûts "
          "fixes de recherche."},
   {'q': "Sujet du type « Un pays peut-il améliorer sa situation par la "
         "protection sans dégrader celle de ses partenaires ? »",
    'f': "La politique commerciale stratégique répond négativement de la façon "
         "la plus nette : le gain national y est exactement la perte du "
         "partenaire, puisqu’il s’agit de capter un profit que le rival aurait "
         "réalisé. C’est l’exemple type d’une mesure rationnelle "
         "individuellement et destructrice collectivement.",
    'r': "On utilise le caractère non coopératif du modèle pour montrer que "
         "certaines politiques commerciales ne sont pas généralisables sans "
         "s’annuler.",
    'ex': "La surenchère de subventions entre l’Inflation Reduction Act et la "
          "réponse industrielle européenne."}],
  voisins=['le28-offensif', 'le28-subventions', 'le28-educateur',
           'le28-representailles', 'le28-marches-publics'])
