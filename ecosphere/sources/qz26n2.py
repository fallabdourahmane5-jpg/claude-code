# -*- coding: utf-8 -*-
"""Chapitre 26 — questions nouvelles, politiques de change et dollar (c26-08 à c26-16)."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c26-08
f(id='q26-n17', sp='c26-08', niv='appliquer', type='ordre', b=1554,
  q="Remettez dans l’ordre l’enchaînement qui conduit des chocs pétroliers à "
    "la crise de la dette.",
  ans=["Les chocs pétroliers des années 1970 engendrent d’importants "
       "excédents courants dans les pays de l’OPEP, environ 450 milliards de "
       "dollars cumulés entre 1974 et 1981",
       "Ces recettes sont déposées dans les banques occidentales, qui les "
       "réorientent vers les pays en développement",
       "L’endettement extérieur progresse fortement : la dette "
       "latino-américaine passe de 75 milliards de dollars en 1975 à 315 "
       "milliards en 1983",
       "À partir de 1979, le choc Volcker relève les taux américains et fait "
       "s’apprécier le dollar",
       "Le service de la dette explose, passant d’environ 12 à 66 milliards "
       "de dollars",
       "La crise mexicaine de 1982 déclenche la crise internationale de la "
       "dette"],
  exp="Le double mécanisme de retournement est essentiel : la hausse des taux "
      "renchérit le coût d’emprunts souvent conclus à taux variable, tandis "
      "que l’appréciation du dollar alourdit le principal des dettes "
      "libellées en monnaie américaine. La dégradation simultanée des "
      "recettes d’exportation, liée au ralentissement mondial, aggrave encore "
      "la situation.",
  diss="Leçon générale : s’endetter dans une devise que l’on ne contrôle pas "
       "expose aux décisions d’une banque centrale étrangère."),

f(id='q26-n18', sp='c26-08', niv='raisonner', type='qcm', b=1671,
  q="Pourquoi l’endettement en devises rend-il toute dépréciation "
    "dangereuse ?",
  opts=["Parce qu’il réduit les exportations",
        "Par effet de bilan : les dettes libellées en devises s’alourdissent "
        "alors que les revenus restent en monnaie nationale",
        "Parce qu’il augmente les réserves de change",
        "Parce qu’il interdit les interventions de la banque centrale"],
  ans=1,
  why=["Une dépréciation stimule au contraire les exportations : c’est le "
       "mécanisme attendu.",
       "Les réserves de change ne sont pas augmentées par l’endettement.",
       "Rien n’interdit à la banque centrale d’intervenir : c’est sa capacité "
       "qui est limitée par ses réserves."],
  exp="C’est l’une des deux raisons de la peur du flottement mise en évidence "
      "par Calvo et Reinhart (2002), l’autre étant le risque d’inflation "
      "importée, qui peut contraindre la banque centrale à relever ses taux "
      "et freiner l’activité. Dans les deux cas, le pays officiellement "
      "flottant intervient en réalité pour limiter les variations de sa "
      "monnaie : la volatilité de ses réserves et de ses taux le révèle "
      "mieux que ses déclarations.",
  diss="Articulation forte avec la crise de la dette : l’effet de bilan "
       "explique à la fois la crise de 1982 et la prudence des émergents "
       "depuis."),

f(id='q26-n19', sp='c26-08', niv='comprendre', type='qcmm', b=1618,
  q="Quels avantages le cours attribue-t-il aux régimes de changes fixes ? "
    "(plusieurs réponses)",
  opts=["Réduire l’incertitude pour les agents engagés dans les échanges "
        "internationaux",
        "Réduire les coûts de transaction",
        "Discipliner la politique monétaire et ancrer les anticipations "
        "d’inflation",
        "Restaurer la crédibilité des autorités monétaires",
        "Supprimer la contrainte extérieure"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la stabilité du change sécurise les décisions "
       "d’exportation et d’investissement.",
       "Exacte : moins de couverture nécessaire, donc moins de frais.",
       "Exacte : l’engagement de parité contraint la banque centrale.",
       "Exacte : c’est l’argument décisif après une période d’inflation "
       "élevée.",
       "Inexacte : les changes fixes renforcent au contraire la contrainte "
       "extérieure, puisqu’il faut défendre la parité."],
  exp="Ces avantages se regroupent en deux familles : réduire l’incertitude "
      "et les coûts de transaction d’une part, lutter contre l’inflation et "
      "restaurer la crédibilité d’autre part. Le coût correspondant est "
      "l’abandon de l’autonomie monétaire dès lors que les capitaux "
      "circulent — c’est le triangle de Mundell.",
  diss="Lecture croisée à proposer : les avantages des changes fixes sont les "
       "limites des changes flottants, et réciproquement."),

# ------------------------------------------------------------- c26-09
f(id='q26-n20', sp='c26-09', niv='appliquer', type='assoc', b=1746,
  q="Associez chaque système monétaire international au sommet du triangle de "
    "Mundell qu’il sacrifie.",
  ans=[["Bretton Woods, de 1944 à 1971",
        "La libre circulation des capitaux"],
       ["Le flottement généralisé, à partir de 1973",
        "La stabilité des taux de change"],
       ["La zone euro, depuis 1999",
        "L'autonomie des politiques monétaires nationales"]],
  exp="Les trois configurations possibles du triangle ont donc été réellement "
      "expérimentées, ce qui fonde la formule de Jean-Marc Daniel : « Le "
      "monde a accompli une sorte de parcours complet en essayant toutes les "
      "éventualités offertes par le triangle des incompatibilités de Robert "
      "Mundell. » Cette lecture interdit toute interprétation téléologique : "
      "aucun système n’était plus moderne qu’un autre.",
  diss="Usage très efficace : utiliser le triangle comme grille de lecture de "
       "l’histoire monétaire, plutôt que comme simple théorème."),

f(id='q26-n21', sp='c26-09', niv='raisonner', type='qcm', b=1810,
  q="Que révèlent les crises du SME de 1992-1993 au regard du triangle de "
    "Mundell ?",
  opts=["Que les changes flottants sont instables",
        "Que la combinaison de changes fixes européens et d’une mobilité "
        "croissante des capitaux devenait intenable",
        "Que les banques centrales ne peuvent pas coopérer",
        "Que l’euro était inutile"],
  ans=1,
  why=["Le SME était précisément un régime de changes fixes, non flottants.",
       "Les banques centrales ont au contraire coopéré, mais leurs moyens "
       "étaient insuffisants face aux capitaux.",
       "Ces crises sont au contraire l’un des arguments en faveur de la "
       "monnaie unique."],
  exp="C’est pourquoi les marges de fluctuation sont élargies à ± 15 % en août "
      "1993, contre ± 2 % auparavant : à défaut de pouvoir restaurer "
      "l’autonomie monétaire ou de fermer les mouvements de capitaux, on "
      "assouplit la contrainte de change. La monnaie unique de 1999 constitue "
      "la réponse inverse : elle supprime la contrainte de change en "
      "supprimant les changes eux-mêmes, au prix de l’autonomie monétaire "
      "nationale.",
  diss="Enchaînement très démonstratif : crise du régime intermédiaire, puis "
       "choix d’un des sommets — ici l’abandon de l’autonomie."),

# ------------------------------------------------------------- c26-10
f(id='q26-n22', sp='c26-10', niv='appliquer', type='assoc', b=1984,
  q="Associez chaque instrument de la politique de change au mécanisme par "
    "lequel il agit.",
  ans=[["La banque centrale achète ou vend sa monnaie contre des devises sur "
        "le marché", "Intervention directe"],
       ["La banque centrale modifie l’attractivité des placements libellés "
        "dans sa monnaie", "Action par le taux d'intérêt"],
       ["Les autorités restreignent certaines opérations en devises",
        "Contrôle des changes"]],
  exp="Chacun comporte des limites. L’intervention directe est asymétrique : "
      "freiner une appréciation est relativement facile, puisque la banque "
      "centrale peut créer sa propre monnaie, alors que la défense contre une "
      "dépréciation est limitée par des réserves nécessairement finies — "
      "c’est ce qui rend les attaques spéculatives possibles. L’action par "
      "les taux entre en conflit avec les objectifs internes. Le contrôle des "
      "changes se heurte à l’intégration financière.",
  diss="Hiérarchie à proposer : plus un instrument est efficace sur le change, "
       "plus il contraint les autres objectifs de politique économique."),

f(id='q26-n23', sp='c26-10', niv='raisonner', type='courte', b=1899,
  q="Pourquoi une guerre des monnaies ne peut-elle pas bénéficier à tous ses "
    "participants ?",
  ans={'modele': "Pour une raison d’abord logique : les taux de change sont "
       "relatifs. Une dépréciation chez l’un est nécessairement une "
       "appréciation chez l’autre, de sorte que tous les pays ne peuvent pas "
       "déprécier simultanément leur monnaie les uns par rapport aux autres. "
       "Le cours présente cette relativité comme la limite fondamentale de "
       "toute guerre des monnaies : ce n’est pas seulement un coût, c’est une "
       "impossibilité. S’y ajoutent des coûts réels. L’inflation importée "
       "renchérit les produits et les intrants, ce qui érode le gain de "
       "compétitivité par les effets de second tour sur les salaires et les "
       "coûts : c’est le cercle vicieux de la monnaie faible. Les effets "
       "attendus dépendent en outre de la condition de Marshall-Lerner et "
       "prennent du temps, selon la courbe en J. Enfin, l’accusation de "
       "manipulation monétaire est difficile à établir : le cours souligne, à "
       "propos de la Chine, qu’une accusation de sous-évaluation ne démontre "
       "pas à elle seule une manipulation, l’évaluation du niveau d’équilibre "
       "d’une monnaie étant complexe.",
       'cites': [],
       'cles': [{'f': ['relatif', 'relativite', 'simultanement',
                       'appreciation chez l autre'],
                 'l': "les taux de change sont relatifs : impossibilité logique"},
                {'f': ['fondamentale', 'pas seulement un cout',
                       'impossibilite'],
                 'l': "c'est la limite fondamentale, non un simple coût"},
                {'f': ['inflation importee', 'second tour', 'erode', 'cout'],
                 'l': "l'inflation importée érode le gain de compétitivité"},
                {'f': ['marshall-lerner', 'elasticite', 'courbe en j',
                       'delai'],
                 'l': "les conditions d'efficacité : Marshall-Lerner et délais"},
                {'f': ['manipulation', 'sous-evaluation', 'chine',
                       'difficile'],
                 'l': "la difficulté d'établir une manipulation monétaire"}]},
  exp="La limite fondamentale est que les taux de change étant relatifs, tous "
      "les pays ne peuvent pas déprécier simultanément les uns par rapport "
      "aux autres : c’est une impossibilité logique, et non seulement un "
      "coût.",
  diss="Argument à rapprocher du dilemme du prisonnier : chacun a intérêt à "
       "déprécier, mais le résultat collectif est nul ou négatif."),

# ------------------------------------------------------------- c26-11
f(id='q26-n24', sp='c26-11', niv='appliquer', type='qcm', b=2131,
  q="Avec des élasticités-prix de 0,5 pour les exportations et de 0,4 pour "
    "les importations, la condition de Marshall-Lerner est-elle vérifiée ?",
  opts=["Oui, car la somme vaut 0,9",
        "Non, car la somme vaut 0,9, donc moins de 1 : le solde commercial se "
        "détériorerait",
        "Oui, car chaque élasticité est positive",
        "La condition ne s’applique pas à ces valeurs"],
  ans=1,
  why=["0,9 est précisément inférieur à 1 : la condition n’est pas "
       "vérifiée.",
       "Le signe des élasticités n’est pas le critère : c’est la somme de "
       "leurs valeurs absolues.",
       "La condition s’applique à toutes les valeurs d’élasticité."],
  exp="La règle est |εX| + |εM| > 1. Au-dessus de 1, les effets-volume "
      "l’emportent sur les effets-prix et le solde s’améliore ; égale à 1, "
      "l’effet global est nul dans le cadre simplifié ; en dessous, le solde "
      "se détériore. L’illustration du cours le vérifie : avec 0,8 et 0,6, "
      "une dévaluation de 10 % porte le solde à + 4,6, alors qu’avec 0,3 et "
      "0,2 il tombe à − 4,8.",
  diss="Leçon à formuler : ce n’est pas la baisse du taux de change qui "
       "garantit l’amélioration du solde, mais la réaction des volumes "
       "échangés."),

f(id='q26-n25', sp='c26-11', niv='raisonner', type='qcmm', b=2167,
  q="Quels facteurs affaiblissent l’efficacité d’une dévaluation ? (plusieurs "
    "réponses)",
  opts=["Des élasticités-prix faibles, ne vérifiant pas la condition de "
        "Marshall-Lerner",
        "Une spécialisation reposant sur la compétitivité hors prix",
        "Un comportement de marge des exportateurs, qui ne répercutent pas "
        "la dévaluation sur leurs prix",
        "Une désindustrialisation privant l’économie de substituts nationaux "
        "aux importations",
        "Un contenu importé élevé des exportations",
        "Une forte sensibilité des volumes exportés aux prix"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : les effets-prix l’emportent alors sur les effets-volume.",
       "Exacte : les acheteurs y privilégient la qualité, l’innovation et la "
       "marque.",
       "Exacte : les entreprises reconstituent leurs marges au lieu de gagner "
       "des volumes.",
       "Exacte : sans substitut national, la facture augmente sans que les "
       "volumes diminuent.",
       "Exacte : la dévaluation renchérit alors les intrants des "
       "exportateurs eux-mêmes.",
       "Inexacte : une forte sensibilité des volumes aux prix renforce au "
       "contraire l’efficacité de la dévaluation."],
  exp="À ces facteurs s’ajoutent les délais, décrits par la courbe en J, et "
      "l’inflation importée, qui érode le gain par les effets de second tour "
      "sur les salaires et les coûts. Le cours ajoute une nuance importante : "
      "une faible sensibilité aux prix peut traduire un fort pouvoir de "
      "marché plutôt qu’un manque de compétitivité.",
  diss="Grille complète d’évaluation d’une dévaluation : élasticités, délais, "
       "comportement de marge, substituts nationaux, contenu importé, "
       "inflation importée."),

# ------------------------------------------------------------- c26-13
f(id='q26-n26', sp='c26-13', niv='raisonner', type='qcm', b=2498,
  q="Quelle est la logique économique de la désinflation compétitive ?",
  opts=["Dévaluer régulièrement pour gagner des parts de marché",
        "Obtenir une inflation inférieure à celle des partenaires, ce qui "
        "améliore progressivement le taux de change réel à parité inchangée",
        "Augmenter les droits de douane",
        "Laisser flotter la monnaie"],
  ans=1,
  why=["La dévaluation régulière est exactement la stratégie à laquelle on "
       "renonce en mars 1983.",
       "Les droits de douane relèvent de la politique commerciale.",
       "Le flottement contredirait l’engagement de maintenir la parité dans "
       "le SME."],
  exp="La compétitivité-prix dépend du taux de change réel, qui combine le "
      "taux nominal et les niveaux de prix relatifs. Si le taux nominal est "
      "maintenu, une inflation plus faible que celle des partenaires améliore "
      "donc mécaniquement la compétitivité : c’est une dévaluation réelle "
      "obtenue sans dévaluation nominale. Trois familles d’instruments y "
      "concourent : une politique monétaire restrictive, des politiques "
      "structurelles et une politique budgétaire de maîtrise de la demande.",
  diss="Reformulation éclairante : la désinflation compétitive est une "
       "dévaluation réelle lente, substituée à une dévaluation nominale "
       "rapide."),

f(id='q26-n27', sp='c26-13', niv='appliquer', type='qcm', b=2519,
  q="Une entreprise dégage un excédent brut d’exploitation de 48 pour une "
    "valeur ajoutée de 150. Quel est son taux de marge ?",
  opts=["32 %",
        "48 %",
        "3,1 %",
        "312 %"],
  ans=0,
  why=["48 % confondrait le taux de marge avec le montant de l’EBE.",
       "3,1 % correspondrait au rapport inverse exprimé en pourcentage mal "
       "placé.",
       "312 % est le rapport VA / EBE, c’est-à-dire l’inverse du taux de "
       "marge."],
  exp="Le taux de marge se calcule comme EBE / VA × 100, soit ici "
      "48/150 × 100 = 32 %. Il mesure la part de la richesse créée qui reste "
      "à l’entreprise après rémunération du travail et impôts sur la "
      "production. Ce niveau de 32 % est précisément celui atteint par les "
      "entreprises françaises en 1989, contre 25 % en 1985 : environ 7 points "
      "de redressement, l’un des trois succès de la politique du franc fort.",
  diss="Enjeu du calcul : c’est la condition initiale du théorème de Schmidt, "
       "dont le cours montre que la suite ne s’est pas réalisée."),

# ------------------------------------------------------------- c26-14
f(id='q26-n28', sp='c26-14', niv='appliquer', type='assoc', b=2586,
  q="Classez chaque situation selon qu’elle produit un effet de levier ou un "
    "effet de massue.",
  ans=[["Rentabilité économique de 10 % et coût réel de l’endettement de 4 %",
        "Effet de levier : l'endettement améliore la rentabilité financière"],
       ["Taux nominal de 10 % et inflation de 14 %, soit un taux réel de − 4 %",
        "Effet de levier : l'endettement améliore la rentabilité financière"],
       ["Rentabilité économique de 5 % et coût réel de l’endettement de 8 %",
        "Effet de massue : l'endettement dégrade la rentabilité financière"],
       ["Taux nominal de 10 % et inflation ramenée à 2 %, soit un taux réel "
        "de + 8 %",
        "Effet de massue : l'endettement dégrade la rentabilité financière"]],
  exp="Le critère est unique : comparer la rentabilité économique au coût "
      "réel de l’endettement. C’est ce qui explique l’effet pervers de la "
      "désinflation sur l’investissement : en faisant passer le taux réel de "
      "− 4 % à + 8 % pour un même taux nominal de 10 %, elle fait basculer "
      "les entreprises du levier à la massue, et les incite à se désendetter "
      "plutôt qu’à investir.",
  diss="Articulation décisive : c’est la première des trois limites du "
       "théorème de Schmidt, avec la globalisation financière et la faiblesse "
       "des débouchés anticipés."),

f(id='q26-n29', sp='c26-14', niv='raisonner', type='courte', b=2723,
  q="Pourquoi le bilan de la politique du franc fort est-il qualifié de "
    "contrasté ?",
  ans={'modele': "Parce que ses succès et ses coûts sont également réels et "
       "mesurables. Trois succès d’abord : la désinflation, l’inflation "
       "française passant d’environ 14 % au début des années 1980 à environ "
       "2 % au début des années 1990 ; le redressement de la balance des "
       "transactions courantes ; et la restauration des marges des "
       "entreprises, le taux de marge passant de 25 % en 1985 à 32 % en 1989. "
       "Mais trois coûts ensuite : une croissance plus faible, de l’ordre de "
       "2 % par an contre 3 % dans l’OCDE selon les repères comparatifs du "
       "cours ; un chômage élevé, passant d’environ 8 % en 1982 à environ "
       "12 % en 1998 alors qu’il est de l’ordre de 7 % dans les autres pays "
       "de l’OCDE ; et des effets d’hystérèse, les chocs initialement "
       "conjoncturels laissant des conséquences persistantes sur le niveau du "
       "chômage. La transmission attendue des marges vers l’investissement et "
       "l’emploi ne s’est donc pas réalisée. Le cours ajoute une nuance "
       "essentielle : il serait excessif d’attribuer l’ensemble des "
       "difficultés françaises ultérieures à cette seule politique, la "
       "désindustrialisation, les transformations technologiques, la "
       "mondialisation et d’autres choix y contribuant également.",
       'cles': [{'f': ['desinflation', '14', '2'],
                 'l': "succès : la désinflation"},
                {'f': ['balance', 'courante', 'exterieur', 'redress'],
                 'l': "succès : le redressement extérieur"},
                {'f': ['marge', '25', '32'],
                 'l': "succès : la restauration des marges"},
                {'f': ['croissance', '2', '3', 'ocde'],
                 'l': "coût : une croissance plus faible"},
                {'f': ['chomage', '8', '12', '7'],
                 'l': "coût : un chômage élevé"},
                {'f': ['hysterese', 'persistant', 'durable'],
                 'l': "coût : les effets d'hystérèse"},
                {'f': ['nuance', 'excessif', 'autres facteur',
                       'desindustrialisation'],
                 'l': "nuance : d'autres facteurs expliquent les difficultés ultérieures"}]},
  exp="Si la politique du franc fort a permis à la France de restaurer sa "
      "stabilité monétaire et ses équilibres extérieurs, son maintien "
      "prolongé a contribué à freiner la demande et l’investissement, "
      "révélant les coûts potentiellement durables d’une désinflation "
      "compétitive sur la croissance et l’emploi.",
  diss="Conclusion générale du chapitre à reprendre : une monnaie forte n’est "
       "pas nécessairement une bonne monnaie pour tous les agents et dans "
       "toutes les situations."),

# ------------------------------------------------------------- c26-15
f(id='q26-n30', sp='c26-15', niv='raisonner', type='qcm', b=2872,
  q="En quoi le protectionnisme américain contrarie-t-il l’objectif de "
    "dépréciation du dollar ?",
  opts=["Parce qu’il réduit les exportations américaines",
        "Parce que les droits de douane renchérissent les importations et "
        "peuvent alimenter l’inflation, ce qui pousse à des taux plus élevés "
        "et soutient donc le dollar",
        "Parce qu’il augmente les réserves de change",
        "Parce qu’il interdit les interventions de change"],
  ans=1,
  why=["La baisse des exportations est un effet des représailles, non le "
       "canal de la contradiction monétaire.",
       "Les réserves de change ne sont pas augmentées par les droits de "
       "douane.",
       "Aucune interdiction d’intervenir n’est en cause."],
  exp="Le protectionnisme et la volonté de déprécier le dollar poursuivent "
      "donc des logiques potentiellement incompatibles : l’un alimente "
      "l’inflation, donc les taux, donc l’attractivité des placements en "
      "dollars, tandis que l’autre suppose au contraire une baisse de cette "
      "attractivité. Le cours relève cette contradiction interne de la "
      "politique économique américaine contemporaine.",
  diss="À articuler avec le paradoxe du dollar : déprécier la monnaie de "
       "réserve mondiale risque en outre de fragiliser la confiance dans les "
       "actifs américains."),

f(id='q26-n31', sp='c26-15', niv='raisonner', type='vf', b=2871,
  q="Selon le cours, la doctrine Miran fournit une explication établie de la "
    "surévaluation du dollar.",
  ans=False,
  exp="Le cours précise explicitement que cette explication est à nuancer. La "
      "doctrine Miran, exposée dans un rapport de novembre 2024, soutient que "
      "la demande internationale d’actifs sûrs libellés en dollars "
      "entretiendrait une surévaluation de la monnaie américaine, laquelle "
      "pénaliserait les exportateurs et l’industrie manufacturière. Mais "
      "l’évaluation du niveau d’équilibre d’une monnaie est complexe, et le "
      "cours invite à la prudence — comme il le fait pour l’accusation de "
      "sous-évaluation adressée à la Chine.",
  diss="Exigence méthodologique constante du chapitre : distinguer le "
       "mécanisme invoqué, souvent clair, de sa démonstration empirique, "
       "souvent incertaine."),

f(id='q26-n32', sp='c26-15', niv='raisonner', type='qcm', b=2931,
  q="Quel obstacle principal le projet d’accords de Mar-a-Lago rencontre-t-il ?",
  opts=["L’interdiction par le FMI de toute coordination monétaire",
        "Les intérêts divergents des grandes puissances, dont les modèles "
        "économiques ne bénéficieraient pas également d’une dépréciation du "
        "dollar",
        "L’absence de précédent historique",
        "Le refus de la Réserve fédérale"],
  ans=1,
  why=["Le FMI n’interdit pas la coordination : les accords du Plaza et du "
       "Louvre en sont des précédents.",
       "Le précédent existe précisément : le projet s’y réfère "
       "explicitement.",
       "La position de la Fed n’est pas l’obstacle identifié par le cours."],
  exp="Le projet viserait à organiser une dépréciation concertée du dollar à "
      "l’image des accords du Plaza de 1985. Mais la configuration a changé : "
      "en 1985, les cinq puissances partageaient le diagnostic d’un dollar "
      "trop fort. Aujourd’hui, une dépréciation du dollar pénaliserait les "
      "économies exportatrices, dont la compétitivité repose sur l’accès au "
      "marché américain, et dévaloriserait les réserves en dollars des "
      "banques centrales.",
  diss="Comparaison instructive : la coordination monétaire exige un "
       "diagnostic partagé, que la fragmentation géoéconomique rend plus "
       "difficile."),

# ------------------------------------------------------------- c26-16
f(id='q26-n33', sp='c26-16', niv='raisonner', type='ordre', b=3038,
  q="Remettez dans l’ordre le mécanisme par lequel les stablecoins peuvent "
    "soutenir la demande de dollars.",
  ans=["La demande de stablecoins indexés sur le dollar augmente",
       "Leurs émetteurs doivent détenir des actifs de réserve adaptés, "
       "notamment des bons du Trésor américain",
       "La demande privée de dollars et de titres publics américains "
       "s’accroît",
       "Le financement du Trésor américain est facilité et la demande "
       "internationale d’actifs en dollars soutenue",
       "La domination monétaire américaine peut ainsi être prolongée"],
  exp="Le GENIUS Act, cadre fédéral encadrant les stablecoins de paiement "
      "adopté en juillet 2025, peut favoriser le développement de ce marché, "
      "ce qui présente un intérêt stratégique pour la demande internationale "
      "d’actifs américains. Il faut toutefois distinguer trois catégories : "
      "les stablecoins privés adossés à un actif de référence, les monnaies "
      "numériques de banque centrale et les cryptoactifs non adossés à une "
      "monnaie officielle.",
  diss="Paradoxe final du chapitre : l’innovation financière privée peut "
       "prolonger le privilège monétaire que la politique commerciale "
       "menace."),

f(id='q26-n34', sp='c26-16', niv='raisonner', type='courte', b=2979,
  q="En quoi la volonté de déprécier le dollar se heurte-t-elle à son rôle "
    "international d’assurance ?",
  ans={'modele': "Le dollar bénéficie d’une demande internationale "
       "structurelle, liée à ses trois fonctions : monnaie véhiculaire, unité "
       "de compte et réserve de valeur internationale. Il joue à ce titre un "
       "rôle d’assurance : en période de tension, les investisseurs se "
       "réfugient dans les actifs libellés en dollars, considérés comme sûrs. "
       "Or déprécier la monnaie de réserve mondiale réduit la valeur externe "
       "de tous les placements en dollars — dans l’exemple du cours, un "
       "patrimoine perd 20 % de sa valeur externe — et fait donc courir un "
       "risque de perte de confiance. Le paradoxe est que cette demande "
       "internationale est précisément ce que la doctrine Miran incrimine, en "
       "y voyant la cause d’une surévaluation pénalisant l’industrie "
       "manufacturière américaine : les États-Unis tireraient donc avantage "
       "d’une position qu’ils voudraient affaiblir. Une dépréciation réussie "
       "risquerait ainsi de fragiliser le système monétaire international et "
       "le privilège même dont elle cherche à corriger les effets.",
       'cles': [{'f': ['demande internationale', 'structurelle', 'reserve',
                       'vehiculaire'],
                 'l': "une demande internationale structurelle"},
                {'f': ['assurance', 'refuge', 'sur', 'tension'],
                 'l': "le rôle d'assurance en période de tension"},
                {'f': ['20', 'valeur externe', 'patrimoine', 'perd'],
                 'l': "une dépréciation réduit la valeur externe des placements"},
                {'f': ['confiance', 'perte de confiance', 'fragilis'],
                 'l': "un risque de perte de confiance"},
                {'f': ['miran', 'surevaluation', 'manufacturiere',
                       'incrimine'],
                 'l': "or c'est cette demande que la doctrine Miran incrimine"},
                {'f': ['privilege', 'paradoxe', 'systeme monetaire',
                       'affaiblir'],
                 'l': "le paradoxe : affaiblir son propre privilège"}]},
  exp="Le dollar bénéficie d’une demande internationale structurelle et joue "
      "un rôle d’assurance ; une dépréciation réduit la valeur externe des "
      "placements en dollars et fait courir un risque de perte de confiance.",
  diss="Conclusion possible du chapitre : le privilège monétaire américain "
       "est aussi une contrainte, et sa remise en cause est d’abord "
       "américaine."),

f(id='q26-n35', sp='c26-16', niv='comprendre', type='qcm', b=2994,
  q="Qu’est-ce qui distingue une monnaie numérique de banque centrale d’un "
    "stablecoin ?",
  opts=["La monnaie numérique de banque centrale est adossée à l’or",
        "La monnaie numérique de banque centrale est une forme numérique de "
        "monnaie de banque centrale, alors qu’un stablecoin est émis par un "
        "acteur privé qui cherche à maintenir une parité",
        "Le stablecoin ne peut pas servir aux paiements",
        "La monnaie numérique de banque centrale n’est pas convertible"],
  ans=1,
  why=["Aucune des deux n’est adossée à l’or.",
       "Les stablecoins servent précisément de moyen de paiement : c’est "
       "l’objet du GENIUS Act.",
       "La convertibilité n’est pas le critère de distinction."],
  exp="La différence est donc celle de l’émetteur et de la nature de "
      "l’engagement : une monnaie numérique de banque centrale est une "
      "créance sur la banque centrale, tandis qu’un stablecoin repose sur "
      "l’engagement d’un émetteur privé et sur les actifs de réserve qu’il "
      "détient. C’est pourquoi un stablecoin peut perdre sa parité, "
      "temporairement ou durablement — risque qui n’existe pas pour la "
      "monnaie de banque centrale.",
  diss="Trois catégories à distinguer systématiquement : MNBC, stablecoins "
       "privés adossés, cryptoactifs non adossés à une monnaie officielle."),

]
