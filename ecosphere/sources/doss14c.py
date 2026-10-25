# -*- coding: utf-8 -*-
"""Ensemble 14 — L’inflation et la stabilité des prix (3/4)."""

from doss_base import d

d('n14-anticipations-inflation', 14, "Anticipations d’inflation",
  "Ce que les agents croient des prix futurs devient une donnée économique",
  "Les anticipations d’inflation sont les prévisions que les agents forment "
  "sur l’évolution future des prix et qui commandent leurs décisions de "
  "salaire, de prix et de placement. Le cours en distingue deux formes : les "
  "anticipations adaptatives de Friedman, où les agents apprennent de "
  "l’inflation passée, et les anticipations rationnelles de la nouvelle "
  "économie classique, où ils intègrent la règle suivie par les autorités.",
  "Le cours fait des anticipations la variable qui décide de l’efficacité "
  "des politiques, et c’est cette fonction qui en commande toute "
  "l’importance. Le point de départ est l’illusion monétaire. À court terme, "
  "selon Friedman, la courbe de Phillips peut exister parce que les salariés "
  "en sont victimes : les prix montent, mais ils ne voient pas tout de suite "
  "que leur salaire réel baisse, donc les entreprises peuvent embaucher et "
  "le chômage baisse. L’anticipation est ici défaillante, et c’est cette "
  "défaillance qui laisse une prise à la politique monétaire. La première "
  "forme d’anticipation est adaptative : les agents apprennent de l’inflation "
  "passée et adaptent leurs comportements, les salariés demandant des hausses "
  "de salaires et les entreprises augmentant leurs prix. Le cours en tire la "
  "conséquence décisive : la politique monétaire marche au début, mais "
  "ensuite les gens s’adaptent, l’effet sur la production disparaît et "
  "l’inflation continue. Au début, les agents pensent que la hausse de la "
  "demande est réelle, donc ils produisent plus ; mais rapidement ils voient "
  "que les prix montent, comprennent qu’il s’agit d’inflation, réclament des "
  "hausses de salaires, et la production retourne à son niveau initial. "
  "L’effet réel est donc ni durable ni prévisible, et c’est pourquoi "
  "Friedman le qualifie d’instable. La seconde forme est rationnelle, et le "
  "cours la rattache à la nouvelle économie classique : les agents "
  "connaissent la règle suivie par les autorités et en intègrent les effets "
  "avant qu’ils ne se produisent, de sorte qu’une politique annoncée n’agit "
  "que sur les variables nominales. Les politiques discrétionnaires créent "
  "alors de l’incertitude, perturbent les anticipations et accentuent "
  "l’instabilité économique, d’où la conclusion que la meilleure politique "
  "économique est l’absence de politique économique, seules étant acceptées "
  "des règles simples, crédibles et stables dans le temps. Le cours montre "
  "enfin le retournement contemporain : loin de subir les anticipations, la "
  "banque centrale s’en sert. Par le canal des anticipations, qu’il nomme "
  "aussi forward guidance, elle annonce l’orientation future probable des "
  "taux, sa stratégie et sa volonté de soutenir l’activité ou de combattre "
  "l’inflation, afin de rassurer les marchés, réduire l’incertitude, "
  "encourager l’investissement et ancrer les anticipations d’inflation. Le "
  "cours conclut que les anticipations deviennent un outil monétaire à part "
  "entière.",
  [("L’illusion monétaire comme point de départ",
    "Les salariés voient monter les prix sans percevoir aussitôt la baisse "
    "de leur salaire réel : cette erreur temporaire laisse une prise à la "
    "politique monétaire, que les entreprises exploitent en embauchant."),
   ("L’apprentissage adaptatif",
    "Les agents apprennent de l’inflation passée et adaptent leurs "
    "comportements : le cours donne l’exemple des salariés qui demandent des "
    "hausses de salaires et des entreprises qui augmentent leurs prix."),
   ("La disparition de l’effet réel",
    "La production retourne à son niveau initial et seule l’inflation "
    "reste : l’anticipation révisée a neutralisé l’impulsion, ce qui rend "
    "l’effet réel instable, ni durable ni prévisible."),
   ("L’anticipation de la règle",
    "Dans la version rationnelle, les agents connaissent la règle suivie par "
    "les autorités et en intègrent les effets avant qu’ils ne se produisent : "
    "la politique n’a plus même d’effet transitoire."),
   ("Le coût de la discrétion",
    "Les politiques discrétionnaires créent de l’incertitude, perturbent les "
    "anticipations et accentuent l’instabilité économique, d’où la "
    "préférence pour des règles simples, crédibles et stables."),
   ("Le retournement : l’anticipation comme instrument",
    "La banque centrale annonce l’orientation future probable des taux pour "
    "modifier les anticipations des agents : le cours conclut qu’elles "
    "deviennent un outil monétaire à part entière.")],
  [{'a': "Faire des anticipations une variable explicative permet de rendre "
         "compte de l’échec des politiques sans invoquer d’erreur technique.",
    'cond': "L’argument suppose que les agents révisent effectivement leurs "
            "prévisions, par apprentissage ou par connaissance de la règle.",
    'lim': "Le cours montre que la vitesse de révision est inconnue : "
           "Friedman parle d’un effet instable, ni durable ni prévisible, ce "
           "qui rend la prévision malaisée."},
   {'a': "La distinction entre anticipations adaptatives et rationnelles "
         "hiérarchise les conclusions de politique économique.",
    'cond': "La distinction suppose que l’on puisse observer si les agents "
            "extrapolent le passé ou anticipent la règle, ce que le cours ne "
            "résout pas empiriquement.",
    'lim': "Les deux hypothèses conduisent à la même conclusion de long "
           "terme, l’inefficacité de la politique monétaire : elles ne "
           "diffèrent que par le délai."},
   {'a': "La notion fonde le canal des anticipations, qui donne à la banque "
         "centrale un instrument sans coût budgétaire.",
    'cond': "L’efficacité suppose que les annonces soient crues, donc une "
            "crédibilité préalablement acquise.",
    'lim': "Le cours rappelle le risque symétrique : une annonce non suivie "
           "d’effet détruit la crédibilité qu’elle supposait, et les "
           "politiques discrétionnaires perturbent les anticipations."},
   {'a': "Elle explique l’intérêt d’une cible d’inflation publique et "
         "chiffrée plutôt que d’un objectif implicite.",
    'cond': "La cible suppose une communication régulière, ce que le cours "
            "décrit comme l’annonce de l’orientation future des taux et de la "
            "stratégie.",
    'lim': "Une cible devient contraignante : s’en écarter durablement "
           "désancre les anticipations, ce que le cours redoute en faisant de "
           "leur ancrage un objectif explicite."},
   {'a': "Elle éclaire la différence entre variables nominales et réelles, "
         "donc le véritable enjeu des politiques conjoncturelles.",
    'cond': "La distinction exige que les agents raisonnent en termes réels "
            "dès qu’ils cessent d’être victimes de l’illusion monétaire.",
    'lim': "Le cours observe pourtant que l’illusion existe à court terme : "
           "les agents ne raisonnent donc pas toujours en termes réels, ce "
           "qui ouvre une marge d’action temporaire."}],
  [{'t': "Les anticipations s’adaptent en apprenant de l’inflation passée : "
         "la politique monétaire garde donc un effet réel transitoire.",
    'qui': "Milton Friedman, dans l’analyse des anticipations adaptatives "
           "que le cours expose.",
    'rep': "La nouvelle économie classique objecte que les agents anticipent "
           "la règle elle-même : le cours rapporte d’ailleurs chez Friedman "
           "une version forte où les entreprises anticipent immédiatement la "
           "hausse future des salaires nominaux."},
   {'t': "Les agents sont parfaitement rationnels : la meilleure politique "
         "économique est donc l’absence de politique économique.",
    'qui': "La nouvelle économie classique, telle que le cours la présente.",
    'rep': "Le cours oppose la nouvelle économie keynésienne : rigidités de "
           "prix et de salaires, asymétries d’information et concurrence "
           "imparfaite font que la demande globale peut rester insuffisante "
           "sans ajustement automatique."},
   {'t': "Les anticipations sont subies par la politique monétaire : elles "
         "ne peuvent pas être un instrument.",
    'qui': "La lecture classique de l’inefficacité des politiques "
           "conjoncturelles.",
    'rep': "Le cours décrit précisément le contraire avec le canal des "
           "anticipations : la banque centrale annonce l’orientation future "
           "des taux pour rassurer les marchés et ancrer les anticipations "
           "d’inflation, qui deviennent un outil à part entière."},
   {'t': "Les anticipations ne sont pas rationnelles mais mimétiques et "
         "autoréalisatrices : elles produisent la réalité qu’elles décrivent.",
    'qui': "Robert Merton, dont le cours fait de la prophétie "
           "autoréalisatrice un concept clé en économie.",
    'rep': "Le cours réunit les deux lectures dans la politique monétaire : "
           "c’est justement parce que les croyances font la réalité que "
           "l’ancrage des anticipations devient un objectif, et non une "
           "simple hypothèse de modèle."}],
  [{'n': "Milton Friedman",
    'i': "Les agents forment des anticipations adaptatives : ils apprennent "
         "de l’inflation passée et adaptent leurs comportements.",
    'p': "Le cours en tire la séquence complète : la politique monétaire "
         "marche au début, mais ensuite les gens s’adaptent, l’effet sur la "
         "production disparaît et l’inflation continue ; l’effet réel est "
         "donc ni durable ni prévisible, autrement dit instable."},
   {'n': "Milton Friedman",
    'i': "L’illusion monétaire explique l’effet de court terme de la "
         "politique monétaire.",
    'p': "Le cours précise le mécanisme : à court terme les salariés voient "
         "les prix monter mais ne voient pas tout de suite que leur salaire "
         "réel baisse, donc les entreprises embauchent et le chômage baisse ; "
         "à long terme l’illusion disparaît et le chômage revient à son "
         "niveau naturel."},
   {'n': "Thomas Sargent",
    'i': "Les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent.",
    'p': "Le cours en tire qu’une politique annoncée n’agit que sur les "
         "variables nominales, d’où la préférence pour des règles plutôt que "
         "pour la discrétion : les anticipations rationnelles suppriment "
         "jusqu’à l’effet transitoire que Friedman concédait."},
   {'n': "Robert Merton",
    'i': "Une croyance collective peut provoquer les comportements qui la "
         "rendent vraie.",
    'p': "Le cours en fait un concept clé en économie, avec pour exemples la "
         "panique bancaire et la bulle spéculative : appliquée aux prix, la "
         "prophétie autoréalisatrice explique pourquoi une anticipation "
         "d’inflation partagée peut suffire à la produire."}],
  [{'f': "Le cours rapporte que la politique monétaire marche au début, mais "
         "qu’ensuite les gens s’adaptent et que l’effet sur la production "
         "disparaît.",
    'p': "Le fait montre que l’anticipation est le mécanisme par lequel une "
         "politique perd son effet réel : le temps de réaction des agents "
         "mesure la marge d’action des autorités."},
   {'f': "Le cours range parmi les effets recherchés du canal des "
         "anticipations le fait d’ancrer les anticipations d’inflation.",
    'p': "Le fait démontre le retournement de statut : d’obstacle à la "
         "politique monétaire, les anticipations sont devenues l’un de ses "
         "objectifs explicites."},
   {'f': "Le cours conclut que les anticipations deviennent un outil "
         "monétaire à part entière.",
    'p': "La formule montre que la communication est désormais rangée au "
         "même niveau que les taux directeurs parmi les instruments de la "
         "banque centrale."},
   {'f': "Pour la nouvelle économie classique, seules sont acceptées des "
         "règles simples, crédibles et stables dans le temps.",
    'p': "Le fait montre la conséquence institutionnelle de l’hypothèse "
         "d’anticipations rationnelles : si les agents anticipent la règle, "
         "mieux vaut une règle qu’une décision."}],
  [{'q': "Sujet sur l’efficacité des politiques conjoncturelles",
    'f': "Les anticipations décident de l’efficacité d’une politique bien "
         "plus que son contenu. Le cours en donne la démonstration avec "
         "Friedman : les agents forment des anticipations adaptatives, ils "
         "apprennent de l’inflation passée et adaptent leurs comportements, "
         "de sorte que la politique monétaire marche au début, puis les gens "
         "s’adaptent, l’effet sur la production disparaît et l’inflation "
         "continue.",
    'r': "On montre que l’effet d’une politique dépend du délai de révision "
         "des anticipations, ce qui déplace le débat du choix des "
         "instruments vers la vitesse d’ajustement des agents.",
    'ex': "La formule du cours sur l’effet réel : ni durable, ni prévisible, "
          "autrement dit instable."},
   {'q': "Sujet sur règles et discrétion en politique économique",
    'f': "Le statut des anticipations commande le choix entre règle et "
         "discrétion. Si les agents connaissent la règle suivie par les "
         "autorités et en intègrent les effets avant qu’ils ne se produisent, "
         "comme le soutient Sargent, une politique annoncée n’agit que sur "
         "les variables nominales et les politiques discrétionnaires ne font "
         "qu’accentuer l’instabilité économique. D’où la préférence pour des "
         "règles simples, crédibles et stables dans le temps.",
    'r': "On montre que l’argument en faveur des règles ne porte pas sur "
         "leur contenu mais sur leur prévisibilité, ce qui explique sa force "
         "indépendamment de la politique choisie.",
    'ex': "La règle de contrôle de la croissance de la masse monétaire que "
          "Friedman propose, à pourcentage constant."},
   {'q': "Sujet sur la communication des banques centrales",
    'f': "La parole de la banque centrale est devenue un instrument. Le "
         "cours décrit le canal des anticipations, aussi nommé forward "
         "guidance : la banque centrale annonce l’orientation future probable "
         "des taux, sa stratégie, sa volonté de soutenir l’activité ou de "
         "combattre l’inflation, afin de rassurer les marchés, réduire "
         "l’incertitude, encourager l’investissement et ancrer les "
         "anticipations d’inflation.",
    'r': "On montre que ce canal agit sans mouvement de taux, ce qui en fait "
         "un instrument précieux lorsque les taux sont déjà au plus bas.",
    'ex': "La conclusion du cours : les anticipations deviennent un outil "
          "monétaire à part entière."},
   {'q': "Sujet sur l’illusion monétaire",
    'f': "L’illusion monétaire est la condition de possibilité d’une "
         "politique monétaire efficace, ce qui en dit long sur la fragilité "
         "de celle-ci. Le cours l’énonce clairement : à court terme la courbe "
         "de Phillips peut exister parce que les salariés sont victimes de "
         "l’illusion monétaire, les prix montant sans qu’ils voient tout de "
         "suite que leur salaire réel baisse ; à long terme, il n’y a plus "
         "d’illusion et le chômage revient à son niveau naturel.",
    'r': "On montre que l’efficacité repose sur une erreur de perception, ce "
         "qui explique pourquoi elle est nécessairement transitoire et "
         "pourquoi sa répétition la détruit.",
    'ex': "Le constat du cours sur les années soixante-dix : les gens ne "
          "sont plus victimes de l’illusion monétaire, ils anticipent, donc "
          "la politique monétaire ne marche plus."}],
  voisins=['n14-courbe-phillips', 'n14-ancrage-anticipations',
           'n14-boucle-prix-salaires', 'n14-credibilite-monetaire'])


d('n14-courbe-phillips', 14, "Courbe de Phillips",
  "L’arbitrage entre inflation et chômage, et son effondrement",
  "La courbe de Phillips est la relation inverse observée entre le chômage et "
  "la croissance des salaires nominaux, puis l’inflation. Le cours en suit "
  "toute la trajectoire : l’observation de Phillips en 1958, la confirmation "
  "de Samuelson et Solow aux États-Unis, la critique de Friedman qui la rend "
  "verticale à long terme, et sa destruction expérimentale par la stagflation "
  "des années soixante-dix.",
  "Le cours traite la courbe de Phillips comme un récit en quatre moments, "
  "et c’est cette forme qui en fait un objet de dissertation si efficace. "
  "Premier moment, le point de départ keynésien. Keynes, Phillips, Samuelson "
  "et Solow soutiennent que l’inflation peut réduire le chômage, selon la "
  "chaîne suivante : quand le chômage est faible, les salariés demandent des "
  "hausses de salaires ; plus de salaires signifie une hausse des coûts donc "
  "des prix, donc de l’inflation. On obtient une relation inverse entre "
  "chômage et inflation. Deuxième moment, l’observation. En 1958, Alban "
  "William Phillips observe une relation inverse entre le taux de croissance "
  "des salaires nominaux et celui du chômage, à partir d’une étude empirique "
  "portant sur le Royaume-Uni entre 1861 et 1957. Le cours précise "
  "immédiatement les réserves : la relation n’est ni linéaire ni stable, et "
  "la courbe passe par l’axe des abscisses, ce qui signifie qu’il existe un "
  "taux de chômage pour lequel la croissance des salaires nominaux est nulle. "
  "Samuelson et Solow confirment la relation pour les États-Unis : en période "
  "de croissance l’inflation est élevée et le chômage faible, en période de "
  "crise l’inflation est faible et le chômage fort. Les gouvernements des "
  "années soixante et soixante-dix en déduisent qu’en acceptant un peu "
  "d’inflation on peut réduire le chômage, donc que l’État peut provoquer de "
  "l’inflation pour faire baisser le chômage. Troisième moment, la critique "
  "de Friedman. À court terme, la courbe peut exister parce que les salariés "
  "sont victimes de l’illusion monétaire. À long terme, il n’y a plus "
  "d’illusion : les salariés voient que les prix montent, demandent des "
  "hausses de salaires nominaux, les entreprises doivent augmenter leurs prix "
  "encore, et le chômage revient à son niveau naturel. Il n’existe donc plus "
  "de relation inflation-chômage et la courbe devient verticale. Friedman "
  "pousse même plus loin : les entreprises anticipent immédiatement que "
  "l’inflation entraînera une hausse future des salaires nominaux par les "
  "syndicats, donc elles n’embaucheront pas plus. Quatrième moment, la "
  "réfutation empirique. Lors du choc pétrolier, les firmes voient leurs "
  "coûts augmenter, donc elles licencient, d’où inflation et chômage "
  "ensemble : c’est la stagflation, qui détruit expérimentalement la courbe "
  "de Phillips puisque l’inflation n’a pas fait baisser le chômage.",
  [("La tension du marché du travail",
    "Un chômage faible met les salariés en position de demander des hausses "
    "de salaires : c’est le premier maillon de la relation, celui que "
    "Phillips observe statistiquement."),
   ("La transmission des salaires aux prix",
    "Plus de salaires signifie une hausse des coûts, donc une hausse des "
    "prix : la relation initialement établie entre chômage et salaires "
    "nominaux devient une relation entre chômage et inflation."),
   ("L’effet attendu sur l’emploi",
    "Selon la lecture keynésienne, l’inflation fait baisser les salaires "
    "réels, donc les entreprises embauchent plus : c’est l’inversion de "
    "causalité qui transforme l’observation en instrument de politique."),
   ("L’illusion monétaire de court terme",
    "Les salariés voient monter les prix mais ne voient pas tout de suite "
    "que leur salaire réel baisse : c’est cette erreur temporaire qui rend la "
    "courbe exploitable, selon Friedman."),
   ("La révision des anticipations",
    "Les salariés finissent par demander des hausses de salaires nominaux et "
    "les entreprises par augmenter leurs prix encore : le chômage revient à "
    "son niveau naturel et la courbe devient verticale."),
   ("L’anticipation immédiate",
    "Dans la version forte, les entreprises anticipent dès le départ la "
    "hausse future des salaires nominaux via les syndicats, donc "
    "n’embauchent pas plus : il ne reste que l’inflation."),
   ("La réfutation par le choc d’offre",
    "Le choc pétrolier produit simultanément inflation et chômage : la "
    "relation est détruite expérimentalement, puisque l’inflation n’a pas "
    "fait baisser le chômage.")],
  [{'a': "La courbe fournit une relation empirique robuste sur près d’un "
         "siècle, ce qui lui a donné une autorité considérable.",
    'cond': "L’autorité suppose que la période observée soit représentative, "
            "ce que la longueur de l’échantillon de Phillips, de 1861 à "
            "1957, semblait garantir.",
    'lim': "Le cours relève d’emblée que la relation n’est ni linéaire ni "
           "stable : la régularité observée n’était donc pas une loi."},
   {'a': "Elle a été confirmée sur une seconde économie, ce qui écartait "
         "l’hypothèse d’une particularité nationale.",
    'cond': "La confirmation suppose que Samuelson et Solow aient observé le "
            "même phénomène, ce que le cours affirme pour les États-Unis.",
    'lim': "Le cours décrit cette confirmation en termes de conjoncture, "
           "inflation élevée en croissance et faible en crise : c’est une "
           "corrélation cyclique, non une relation causale établie."},
   {'a': "Elle a fourni un cadre opératoire aux gouvernements, qui "
         "disposaient ainsi d’un arbitrage explicite.",
    'cond': "L’usage suppose que la relation soit stable et exploitable, "
            "donc que les agents ne modifient pas leur comportement lorsque "
            "la politique change.",
    'lim': "C’est précisément cette condition que Friedman attaque : dès que "
           "l’illusion monétaire disparaît, l’arbitrage s’évanouit et il ne "
           "reste que l’inflation."},
   {'a': "Sa critique a introduit la notion de taux de chômage naturel, qui "
         "reste un repère de politique économique.",
    'cond': "La notion suppose qu’il existe un niveau de chômage "
            "incompressible lié aux frictions du marché du travail, "
            "information imparfaite et mobilité.",
    'lim': "Le cours présente ce taux comme une limite qu’on ne peut pas "
           "réduire par la relance, sans fournir de méthode pour l’estimer, "
           "ce qui en rend l’usage délicat."},
   {'a': "Son effondrement a eu une portée méthodologique : il a montré "
         "qu’une relation statistique peut dépendre du régime de politique "
         "en vigueur.",
    'cond': "La leçon suppose que le comportement des agents réagisse à la "
            "politique suivie, ce que les anticipations adaptatives puis "
            "rationnelles formalisent.",
    'lim': "Le cours propose deux explications concurrentes du même "
           "effondrement, le choc d’offre et la fin de l’illusion monétaire, "
           "sans les hiérarchiser."}],
  [{'t': "Une inflation modérée peut faire baisser le chômage : l’État peut "
         "donc provoquer de l’inflation pour réduire le chômage.",
    'qui': "Les gouvernements des années soixante et soixante-dix, s’appuyant "
           "sur Keynes, Phillips, Samuelson et Solow.",
    'rep': "Le cours répond par Friedman : à long terme il n’y a plus "
           "d’illusion monétaire, le chômage revient à son niveau naturel et "
           "la courbe de Phillips devient verticale, de sorte qu’il ne reste "
           "que l’inflation."},
   {'t': "À long terme, il n’existe aucune relation entre inflation et "
         "chômage : la politique monétaire est impuissante.",
    'qui': "Milton Friedman et l’école monétariste, dont le cours expose la "
           "critique de la courbe.",
    'rep': "Le cours maintient que Friedman lui-même reconnaît un effet de "
           "court terme : il existe une influence de la monnaie sur les "
           "variables réelles à court terme, même si cette relation est "
           "instable."},
   {'t': "Ce n’est pas la théorie mais les faits qui ont tranché : c’est le "
         "choc pétrolier, non les anticipations, qui a détruit la relation.",
    'qui': "La lecture par le choc d’offre que le cours développe à propos "
           "de la stagflation.",
    'rep': "Le cours rapporte la réponse monétariste : normal, les gens ne "
           "sont plus victimes d’illusion monétaire, ils anticipent, donc la "
           "politique monétaire ne marche plus, ce qui attribue au "
           "comportement et non au choc le rôle décisif."},
   {'t': "Le marché du travail n’obéit pas à ce type de relation : les "
         "rigidités et les asymétries d’information en commandent le "
         "fonctionnement.",
    'qui': "La nouvelle économie keynésienne, telle que le cours la "
           "présente.",
    'rep': "Le cours retient cette analyse comme un complément : rigidités "
           "de prix et de salaires, asymétries d’information et concurrence "
           "imparfaite expliquent le chômage involontaire que ni la courbe ni "
           "sa version verticale ne traitent."}],
  [{'n': "Alban William Phillips",
    'i': "Il existe une relation inverse entre le taux de croissance des "
         "salaires nominaux et celui du chômage.",
    'p': "Le cours date l’observation de 1958 et en donne la base, une étude "
         "empirique sur le Royaume-Uni entre 1861 et 1957, en ajoutant que "
         "la relation n’est ni linéaire ni stable et qu’elle passe par l’axe "
         "des abscisses, ce qui définit un taux de chômage à croissance "
         "salariale nulle."},
   {'n': "Paul Samuelson",
    'i': "La relation entre inflation et chômage se vérifie aussi aux "
         "États-Unis.",
    'p': "Le cours rapporte la confirmation qu’il établit avec Robert "
         "Solow : en période de croissance le niveau d’inflation est élevé et "
         "le chômage faible, en période de crise l’inflation est faible et le "
         "chômage fort."},
   {'n': "Robert Solow",
    'i': "La relation inverse entre inflation et chômage s’observe sur le "
         "cycle américain.",
    'p': "Le cours l’associe à Samuelson dans cette vérification, ce qui "
         "donna à la courbe son autorité internationale : la régularité "
         "n’était plus une particularité britannique mais semblait une "
         "propriété générale des économies de marché."},
   {'n': "Milton Friedman",
    'i': "À long terme la courbe de Phillips devient verticale et le chômage "
         "revient à son niveau naturel.",
    'p': "Le cours en donne les deux temps : à court terme la courbe peut "
         "exister par l’illusion monétaire ; à long terme les salariés voient "
         "les prix monter, demandent des hausses de salaires nominaux, les "
         "entreprises augmentent encore leurs prix, et il n’existe plus de "
         "relation inflation-chômage."}],
  [{'f': "En 1958, Phillips observe une relation inverse entre croissance des "
         "salaires nominaux et chômage, sur le Royaume-Uni entre 1861 et "
         "1957.",
    'p': "La date et la période couverte expliquent l’autorité acquise par "
         "la relation : près d’un siècle de données donnait à la régularité "
         "l’apparence d’une loi."},
   {'f': "Le cours relève que la courbe passe par l’axe des abscisses, ce qui "
         "définit un taux de chômage à croissance des salaires nominaux "
         "nulle.",
    'p': "Le détail technique montre que la relation comporte dès l’origine "
         "un point d’arrêt, préfiguration du taux de chômage naturel que "
         "Friedman formalisera."},
   {'f': "Samuelson et Solow confirment la relation pour les États-Unis, "
         "inflation élevée et chômage faible en croissance, et inversement en "
         "crise.",
    'p': "La confirmation sur une seconde économie explique pourquoi les "
         "gouvernements des années soixante et soixante-dix ont cru pouvoir "
         "en faire un instrument."},
   {'f': "La stagflation des années soixante-dix associe inflation et "
         "chômage élevé, ce qui détruit expérimentalement la courbe.",
    'p': "Le fait démontre la fragilité d’une relation purement empirique : "
         "elle n’a pas été réfutée par un argument mais par un épisode "
         "qu’elle déclarait improbable."}],
  [{'q': "Sujet sur l’arbitrage entre inflation et chômage",
    'f': "L’arbitrage entre inflation et chômage a existé comme fait "
         "statistique avant d’être contesté comme loi. Le cours rapporte "
         "qu’en 1958 Alban William Phillips observe une relation inverse "
         "entre le taux de croissance des salaires nominaux et celui du "
         "chômage sur le Royaume-Uni entre 1861 et 1957, et que Samuelson et "
         "Solow confirment cette relation pour les États-Unis. Les "
         "gouvernements en déduisent qu’en acceptant un peu d’inflation on "
         "peut réduire le chômage.",
    'r': "On distingue la corrélation observée de la relation causale "
         "exploitable, pour montrer que c’est le passage de l’une à l’autre "
         "qui était fautif.",
    'ex': "La réserve que le cours énonce dès la présentation : la relation "
          "n’est ni linéaire ni stable."},
   {'q': "Sujet sur la critique monétariste du keynésianisme",
    'f': "La courbe de Phillips est le terrain où la critique monétariste "
         "porte le plus loin. Friedman accorde qu’à court terme la courbe "
         "peut exister, parce que les salariés sont victimes de l’illusion "
         "monétaire et ne voient pas tout de suite que leur salaire réel "
         "baisse ; mais à long terme ils demandent des hausses de salaires "
         "nominaux, les entreprises augmentent encore leurs prix, le chômage "
         "revient à son niveau naturel et la courbe devient verticale.",
    'r': "On montre que la critique ne nie pas le fait mais en limite la "
         "portée temporelle, ce qui est plus solide qu’une réfutation "
         "frontale.",
    'ex': "La formule du cours : la monnaie est puissante, mais la politique "
          "monétaire est impuissante."},
   {'q': "Sujet sur la réfutation des théories par les faits",
    'f': "La courbe de Phillips offre un cas rare de réfutation par "
         "l’événement. Le cours écrit que lors du choc pétrolier les firmes "
         "voient leurs coûts augmenter, donc elles sont obligées de "
         "licencier, d’où inflation et chômage, c’est-à-dire la stagflation ; "
         "et il conclut que cela détruit expérimentalement la courbe de "
         "Phillips, parce que l’inflation n’a pas fait baisser le chômage et "
         "qu’on a eu les deux, inflation et chômage élevé.",
    'r': "On montre qu’une relation purement empirique est vulnérable à "
         "l’apparition d’une configuration qu’elle déclarait improbable, ce "
         "qui plaide pour des théories dotées d’un mécanisme explicite.",
    'ex': "Les chocs pétroliers de 1973 et 1979, le baril passant de cinq à "
          "trente dollars."},
   {'q': "Sujet sur le chômage et ses déterminants",
    'f': "La critique de la courbe de Phillips débouche sur une notion "
         "durable, le taux de chômage naturel. Le cours rapporte que Friedman "
         "introduit l’idée d’un niveau de chômage incompressible, lié aux "
         "frictions du marché du travail, information imparfaite et mobilité, "
         "et que toute tentative de le réduire par la relance échoue. "
         "L’analyse déplace ainsi la politique de l’emploi des instruments "
         "conjoncturels vers les instruments structurels.",
    'r': "On montre que la verticalité de la courbe à long terme équivaut à "
         "l’existence d’un taux de chômage indépendant de l’inflation, ce qui "
         "change la nature des remèdes envisageables.",
    'ex': "Le point relevé par le cours chez Phillips lui-même, où la courbe "
          "coupe l’axe des abscisses."}],
  voisins=['n14-stagflation', 'n14-anticipations-inflation',
           'n14-boucle-prix-salaires', 'n14-inflation-demande'],
  comp={'titre': "La courbe de Phillips : lecture keynésienne et lecture "
                 "monétariste",
        'a': "Lecture keynésienne",
        'b': "Lecture monétariste",
        'lignes': [
          ("Auteurs mobilisés par le cours", "Keynes, Phillips, Samuelson et "
           "Solow", "Milton Friedman et l’école monétariste"),
          ("Nature de la relation", "Relation inverse stable et exploitable "
           "entre chômage et inflation",
           "Relation valable à court terme seulement, verticale à long "
           "terme"),
          ("Mécanisme central", "L’inflation abaisse les salaires réels, donc "
           "les entreprises embauchent",
           "Les salariés sont momentanément victimes de l’illusion "
           "monétaire"),
          ("Rôle des anticipations", "Absent de l’analyse initiale",
           "Déterminant : anticipations adaptatives, puis fin de l’illusion "
           "monétaire"),
          ("Niveau de chômage de référence", "Le chômage peut être réduit par "
           "la demande", "Il existe un taux de chômage naturel qu’on ne peut "
           "pas réduire"),
          ("Conséquence pour l’État", "L’État peut provoquer de l’inflation "
           "pour baisser le chômage",
           "La politique monétaire est impuissante à réduire le chômage"),
          ("Instrument préconisé", "Politique conjoncturelle "
           "discrétionnaire, budgétaire et monétaire",
           "Règle de contrôle de la croissance de la masse monétaire"),
          ("Vérification invoquée", "L’observation de Phillips en 1958 et sa "
           "confirmation américaine",
           "La stagflation des années soixante-dix, inflation et chômage "
           "élevés"),
          ("Formule du cours", "Si on accepte un peu d’inflation, on peut "
           "réduire le chômage",
           "La monnaie est puissante, mais la politique monétaire est "
           "impuissante")]})


d('n14-stagflation', 14, "Stagflation",
  "Inflation et chômage ensemble, ce que nulle théorie n’attendait",
  "Le cours définit la stagflation d’une parenthèse : stagnation de la "
  "production et inflation. Elle désigne la configuration des années "
  "soixante-dix où l’inflation et le chômage augmentent simultanément. Le "
  "cours lui donne une cause, le choc pétrolier, et une portée théorique "
  "majeure : elle détruit expérimentalement la courbe de Phillips, puisque "
  "l’inflation n’a pas fait baisser le chômage.",
  "Le cours fait de la stagflation un point de rupture et non un simple "
  "épisode, et c’est à ce titre qu’elle mérite un dossier à part entière. Le "
  "mécanisme est bref et complet : lors du choc pétrolier, les firmes voient "
  "leurs coûts augmenter, donc elles sont obligées de licencier, d’où "
  "inflation et chômage. Le cours nomme alors la configuration : c’est la "
  "stagflation, stagnation de la production et inflation. Et il en tire la "
  "conséquence : cela détruit expérimentalement la courbe de Phillips, parce "
  "que l’inflation n’a pas fait baisser le chômage et qu’on a eu les deux, "
  "inflation et chômage élevé. Les données du choc sont précises : en 1973 le "
  "monde connaît un premier choc pétrolier, c’est-à-dire une forte hausse du "
  "prix du baril, puis un second en 1979, le baril passant au total de cinq à "
  "trente dollars, ce qui provoque une forte hausse du chômage en raison d’un "
  "fort taux de licenciement en réponse à la hausse des coûts de production. "
  "La portée de l’épisode dépasse largement la conjoncture, et le cours en "
  "suit les effets dans trois directions. Première direction, la théorie "
  "monétaire : les libéraux et les monétaristes expliquent l’épisode en "
  "disant que les gens ne sont plus victimes de l’illusion monétaire, qu’ils "
  "anticipent, et que la politique monétaire ne marche donc plus. Le cours "
  "rapporte la conclusion des friedmaniens : la monnaie est puissante, mais "
  "la politique monétaire est inefficace, et il faut laisser faire le marché, "
  "laisser le chômage revenir à son niveau naturel et contrôler la croissance "
  "de la masse monétaire. Deuxième direction, l’histoire des idées : le "
  "chapitre sur les grands courants rappelle que ces phénomènes ne sont pas "
  "expliqués par les modèles keynésiens traditionnels, notamment par la "
  "courbe de Phillips qui postulait un arbitrage stable entre inflation et "
  "chômage, de sorte que la crédibilité du keynésianisme est fortement remise "
  "en cause, ouvrant la voie à un renouveau des idées libérales et à "
  "l’installation de l’école monétariste associée à l’École de Chicago. "
  "Troisième direction, l’analyse de l’investissement : le retour des "
  "approches par l’offre et par les profits dans les années quatre-vingt-dix "
  "est présenté comme une conséquence directe du choc, appuyé par le discours "
  "du chancelier allemand Helmut Schmidt.",
  [("Le choc sur le prix d’un intrant",
    "Le prix du pétrole augmente fortement en 1973 puis en 1979, le baril "
    "passant de cinq à trente dollars : une seule ligne de coût se déplace "
    "pour toutes les économies industrielles."),
   ("La hausse des coûts de production",
    "Les firmes voient leurs coûts augmenter sans l’avoir décidé : le cours "
    "parle d’une hausse des coûts de production à laquelle elles doivent "
    "répondre immédiatement."),
   ("La répercussion sur les prix",
    "Les entreprises augmentent leurs prix de vente pour préserver leurs "
    "marges : l’inflation apparaît alors qu’aucune demande excédentaire n’est "
    "en cause."),
   ("Les licenciements",
    "Le cours insiste sur l’effet simultané : les firmes sont obligées de "
    "licencier, ce qui provoque une forte hausse du chômage par un fort taux "
    "de licenciement."),
   ("La configuration inédite",
    "Inflation et chômage augmentent ensemble : c’est la stagflation, "
    "stagnation de la production et inflation, situation que la courbe de "
    "Phillips excluait."),
   ("La réfutation de l’arbitrage",
    "L’inflation n’a pas fait baisser le chômage et on a eu les deux : la "
    "relation tenue pour stable est détruite expérimentalement."),
   ("Le basculement doctrinal",
    "La crédibilité du keynésianisme est fortement remise en cause, ce qui "
    "ouvre la voie au renouveau des idées libérales et à l’installation de "
    "l’école monétariste.")],
  [{'a': "La stagflation prouve qu’une relation empirique peut cesser de "
         "valoir sans avoir été réfutée par un argument théorique.",
    'cond': "La démonstration suppose que l’épisode soit bien celui que la "
            "relation excluait, ce que le cours affirme : on a eu les deux, "
            "inflation et chômage élevé.",
    'lim': "L’épisode n’invalide pas l’existence d’un arbitrage à court "
           "terme, que Friedman lui-même concède en invoquant l’illusion "
           "monétaire."},
   {'a': "Elle établit l’existence d’une inflation d’origine non monétaire, "
         "puisque la cause est un prix d’intrant.",
    'cond': "L’argument suppose que la hausse du prix du pétrole soit bien "
            "la cause dominante, ce que le cours présente comme tel.",
    'lim': "Les monétaristes attribuent l’épisode aux anticipations plutôt "
           "qu’au choc : le cours rapporte les deux explications sans les "
           "hiérarchiser."},
   {'a': "Elle met en évidence les limites des politiques conjoncturelles, "
         "incapables de traiter deux déséquilibres de sens opposé.",
    'cond': "L’impasse suppose un seul instrument disponible, le taux "
            "directeur ou la dépense publique, agissant dans un seul sens sur "
            "la demande.",
    'lim': "Le cours montre que l’on peut sortir de l’impasse par une "
           "politique structurelle ou par un choc de taux assumé, comme celui "
           "que conduit Volcker en 1979."},
   {'a': "Elle explique un basculement doctrinal majeur dans l’histoire de la "
         "pensée économique, du keynésianisme au monétarisme.",
    'cond': "Le lien suppose que la courbe de Phillips ait bien été au cœur "
            "du keynésianisme appliqué, ce que le cours établit en parlant "
            "d’un arbitrage postulé stable.",
    'lim': "Le cours ne présente pas ce basculement comme une victoire "
           "théorique : il parle d’une crédibilité remise en cause, donc d’un "
           "mouvement d’idées autant que d’une démonstration."},
   {'a': "Elle fournit un critère de diagnostic encore utilisable, par la "
         "direction conjointe des prix et de l’emploi.",
    'cond': "Le critère suppose de pouvoir observer les deux variables "
            "simultanément et d’exclure un choc de demande concomitant.",
    'lim': "Un épisode réel peut mêler les deux chocs : le cours décrit "
           "d’ailleurs une hausse du chômage consécutive au choc d’offre, "
           "donc une contraction de la demande qui en découle."}],
  [{'t': "La stagflation vient de la fin de l’illusion monétaire, non du "
         "choc pétrolier : les agents anticipent, donc la politique monétaire "
         "ne marche plus.",
    'qui': "Les libéraux et les monétaristes, dont le cours rapporte "
           "l’explication.",
    'rep': "Le cours maintient les deux causes côte à côte : il décrit le "
           "mécanisme du choc de coût, les firmes licenciant en réponse à la "
           "hausse des coûts, tout en rapportant l’explication par les "
           "anticipations."},
   {'t': "La stagflation justifie l’abandon de toute politique conjoncturelle "
         "au profit de règles simples.",
    'qui': "La conclusion des friedmaniens, telle que le cours la résume.",
    'rep': "Le cours rappelle que les keynésiens conservent un argument de "
           "poids : rigidités de prix et de salaires, asymétries "
           "d’information et concurrence imparfaite font que la demande "
           "globale peut rester durablement insuffisante."},
   {'t': "Un choc de coût ne peut pas produire une inflation durable : seule "
         "la monnaie en est capable.",
    'qui': "L’objection quantitativiste issue de la théorie que le cours "
           "rattache à Fisher et Friedman.",
    'rep': "Le cours répond par la boucle salariale : les salariés réclament "
           "des hausses de salaires nominaux, les entreprises augmentent "
           "encore leurs prix, ce qui transforme un choc ponctuel en "
           "dynamique inflationniste."},
   {'t': "La stagflation n’est qu’un accident : un choc exogène ne remet pas "
         "en cause la validité d’un modèle économique.",
    'qui': "La défense possible du cadre keynésien face à l’épisode.",
    'rep': "Le cours tranche nettement : ces phénomènes ne sont pas "
           "expliqués par les modèles keynésiens traditionnels, et la "
           "crédibilité du keynésianisme est fortement remise en cause."}],
  [{'n': "Milton Friedman",
    'i': "Les gens ne sont plus victimes de l’illusion monétaire, ils "
         "anticipent, donc la politique monétaire ne marche plus.",
    'p': "Le cours fait de cette phrase l’explication monétariste de la "
         "stagflation et en tire la conclusion des friedmaniens : la monnaie "
         "est puissante puisqu’elle détermine l’inflation, mais la politique "
         "monétaire est impuissante puisque les individus anticipent et "
         "neutralisent son effet réel."},
   {'n': "Alban William Phillips",
    'i': "La relation entre chômage et croissance des salaires nominaux "
         "n’est ni linéaire ni stable.",
    'p': "Le cours rapporte cette réserve dès la présentation de son étude "
         "de 1958 sur le Royaume-Uni entre 1861 et 1957 : la stagflation ne "
         "contredit donc pas tant Phillips lui-même que l’usage qui a été "
         "fait de sa courbe par les gouvernements."},
   {'n': "Paul Volcker",
    'i': "Il faut une politique monétaire restrictive pour sortir d’une "
         "inflation élevée, même au prix d’un choc de taux.",
    'p': "Le cours précise qu’il arrive à la tête de la Réserve fédérale en "
         "1979, c’est-à-dire au cœur de l’épisode, et engage une forte hausse "
         "des taux : c’est la réponse qui met fin à l’inflation, mais elle "
         "déclenche la crise de la dette du début des années "
         "quatre-vingt."}],
  [{'f': "Le cours définit la stagflation par une parenthèse : stagnation de "
         "la production et inflation.",
    'p': "La définition montre que le terme réunit deux maux qu’on pensait "
         "alternatifs : c’est cette simultanéité, et non le niveau atteint, "
         "qui fait sa nouveauté théorique."},
   {'f': "En 1973 survient un premier choc pétrolier, puis un second en "
         "1979 ; le baril passe au total de cinq à trente dollars.",
    'p': "Le chiffre mesure l’ampleur du choc de coût et explique pourquoi il "
         "a pu produire simultanément inflation et licenciements dans toutes "
         "les économies industrielles."},
   {'f': "Le cours conclut que la stagflation détruit expérimentalement la "
         "courbe de Phillips, puisque l’inflation n’a pas fait baisser le "
         "chômage.",
    'p': "Le fait montre la portée théorique de l’épisode : il ne corrige "
         "pas une estimation, il invalide une relation sur laquelle reposait "
         "la politique économique des années soixante."},
   {'f': "Le cours relève que la crédibilité du keynésianisme est fortement "
         "remise en cause, ouvrant la voie à un renouveau des idées "
         "libérales.",
    'p': "Le fait situe la conséquence doctrinale : c’est à ce moment que "
         "l’école monétariste associée à l’École de Chicago s’impose "
         "progressivement, avec Friedman pour représentant majeur."}],
  [{'q': "Sujet sur inflation et chômage",
    'f': "La stagflation est l’épisode qui a dissocié deux variables "
         "jusque-là liées. Le cours en donne le mécanisme en une phrase : "
         "lors du choc pétrolier, les firmes voient leurs coûts augmenter, "
         "donc elles sont obligées de licencier, d’où inflation et chômage. "
         "Et il en tire la conséquence : c’est la stagflation, stagnation de "
         "la production et inflation, ce qui détruit expérimentalement la "
         "courbe de Phillips.",
    'r': "On montre que la simultanéité des deux maux suffit à réfuter un "
         "arbitrage, puisqu’un arbitrage suppose précisément qu’on ne puisse "
         "pas avoir les deux ensemble.",
    'ex': "Les chocs pétroliers de 1973 et 1979, avec un baril passant de "
          "cinq à trente dollars."},
   {'q': "Sujet sur les ruptures dans l’histoire de la pensée économique",
    'f': "Un épisode conjoncturel peut déplacer tout un paysage théorique. "
         "Le cours écrit que les phénomènes des années soixante-dix ne sont "
         "pas expliqués par les modèles keynésiens traditionnels, notamment "
         "par la courbe de Phillips qui postulait un arbitrage stable entre "
         "inflation et chômage, de sorte que la crédibilité du keynésianisme "
         "est fortement remise en cause, ouvrant la voie à un renouveau des "
         "idées libérales.",
    'r': "On montre que la défaite d’un courant tient moins à la réfutation "
         "d’une thèse qu’à son incapacité à rendre compte d’une configuration "
         "nouvelle.",
    'ex': "L’installation progressive de l’école monétariste associée à "
          "l’École de Chicago, avec Friedman pour représentant majeur."},
   {'q': "Sujet sur les limites des politiques conjoncturelles",
    'f': "La stagflation place la politique conjoncturelle dans une impasse "
         "qu’un seul instrument ne peut pas lever. Soutenir la demande "
         "nourrit l’inflation sans lever la contrainte de coût ; resserrer la "
         "monnaie aggrave un chômage déjà provoqué par les licenciements. Le "
         "cours constate que la politique monétaire est impuissante à réduire "
         "le chômage, et les monétaristes en concluent qu’il faut laisser le "
         "chômage revenir à son niveau naturel.",
    'r': "On montre que l’impasse vient de ce que deux déséquilibres de sens "
         "opposé coexistent, ce qui exige autant d’instruments que "
         "d’objectifs.",
    'ex': "La solution de Friedman telle que le cours la résume : laisser "
          "faire le marché et contrôler la croissance de la masse monétaire."},
   {'q': "Sujet sur les chocs d’offre",
    'f': "La stagflation est la signature du choc d’offre. Là où un choc de "
         "demande fait varier les prix et l’activité dans le même sens, un "
         "choc d’offre les fait varier en sens contraire : le cours décrit "
         "les firmes voyant leurs coûts augmenter, licenciant en réponse, et "
         "produisant ainsi inflation et chômage ensemble. C’est pourquoi la "
         "direction conjointe des deux variables permet d’identifier "
         "l’origine du choc.",
    'r': "On fait de la configuration observée un instrument de diagnostic, "
         "ce qui permet de choisir l’instrument de politique économique à "
         "partir des faits et non d’une doctrine.",
    'ex': "La forte hausse du chômage que le cours attribue à un fort taux "
          "de licenciement en réponse à la hausse des coûts de production."}],
  voisins=['n14-courbe-phillips', 'n14-inflation-couts',
           'n14-anticipations-inflation', 'n13-chocs-offre-demande'])
