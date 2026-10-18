# -*- coding: utf-8 -*-
"""Ensemble 28 — deuxième série : le protectionnisme et ses formes.

Matière tirée du chapitre 3 de deuxième année (arguments en faveur du
protectionnisme, List, Kaldor, Brander et Spencer, conditions d'efficacité) et
du chapitre 4 (exceptions, sauvegardes, fragmentation).
"""

from doss_base import d

# ---------------------------------------------------------------- 28.05
d('le28-ouverture-progressive', 28,
  "Ouverture commerciale progressive et maîtrisée",
  "Ouvrir n’est pas une décision binaire mais un calendrier",
  "L’ouverture progressive désigne une libéralisation échelonnée dans le temps "
  "et ordonnée par secteurs, calée sur le stade de développement de l’économie "
  "et sur la capacité des branches à soutenir la concurrence. Elle s’oppose à la "
  "fois à l’autarcie et à l’ouverture immédiate et généralisée : l’enjeu n’y est "
  "pas de savoir s’il faut s’ouvrir, mais quand, dans quel ordre et à quel "
  "rythme.",
  "Présenter le choix de politique commerciale comme une alternative entre "
  "ouvrir et fermer fait disparaître la variable la plus importante : le "
  "calendrier. Le cours en fournit la formulation la plus nette à travers les "
  "phases de List — ouverture initiale d’une économie encore agricole, "
  "protection pendant le démarrage industriel, retour au libre-échange à "
  "maturité. La logique est séquentielle : ce qui est bénéfique à un stade peut "
  "être destructeur à un autre, parce que la capacité des producteurs nationaux "
  "à répondre à la concurrence change avec le niveau de développement. Deux "
  "raisons rendent la progressivité préférable à l’ouverture brutale. La "
  "première est microéconomique : l’adaptation d’une entreprise — "
  "investissement, montée en gamme, réorganisation — prend du temps, et un choc "
  "instantané élimine des producteurs qui auraient pu s’ajuster. La seconde est "
  "sociale : l’étalement permet aux politiques de formation et de reconversion "
  "d’agir avant que les pertes ne deviennent irréversibles. Mais la "
  "progressivité comporte son risque propre, et il est symétrique : un "
  "calendrier sans date de sortie crédible se transforme en protection "
  "permanente, parce que les bénéficiaires s’organisent pour obtenir son "
  "prolongement. La progressivité n’est donc une politique sérieuse que si elle "
  "est annoncée, datée et engageante.",
  [("Le séquencement par stade de développement",
    "L’économie encore agricole gagne à l’ouverture, qui diversifie ses "
    "approvisionnements ; l’économie en démarrage industriel a besoin de "
    "protéger ses nouvelles branches ; l’économie mature gagne de nouveau à "
    "l’ouverture, ses entreprises pouvant affronter la concurrence."),
   ("Le séquencement par secteur",
    "Tous les secteurs n’ont pas la même maturité. Ouvrir d’abord les branches "
    "déjà compétitives, puis celles en rattrapage, permet d’obtenir les gains de "
    "l’ouverture sans détruire les capacités en formation."),
   ("L’annonce crédible du calendrier",
    "Un calendrier public et daté modifie les anticipations : les entreprises "
    "protégées savent que la protection cessera et investissent pour s’y "
    "préparer. Sans cette crédibilité, elles investissent au contraire dans le "
    "lobbying."),
   ("La conditionnalité des mesures",
    "Subordonner le maintien de la protection à des résultats vérifiables — "
    "investissement, productivité, exportations — transforme l’abri en "
    "contrepartie et réduit le risque de rente."),
   ("L’articulation avec l’accompagnement social",
    "L’étalement n’a de valeur que s’il est utilisé : il doit être employé à "
    "former, reconvertir et redéployer, faute de quoi il ne fait que repousser "
    "le choc sans en réduire l’ampleur.")],
  [{'a': "La progressivité réduit le coût d’ajustement en laissant aux facteurs "
         "le temps de se redéployer et aux entreprises celui d’investir.",
    'cond': "Le temps gagné doit être effectivement employé à la transformation : "
            "cela suppose des engagements vérifiables et un suivi.",
    'lim': "Si le temps n’est pas utilisé, l’étalement ne réduit pas le coût, il "
           "le diffère — et le choc final survient dans une économie qui s’y est "
           "moins préparée encore."},
   {'a': "La progressivité rend l’ouverture politiquement soutenable, donc "
         "durable, alors qu’une ouverture brutale peut être annulée par "
         "l’alternance politique.",
    'cond': "Il faut que le calendrier soit perçu comme équitable et que les "
            "secteurs protégés le plus longtemps soient ceux dont le rattrapage "
            "est plausible, non les mieux organisés politiquement.",
    'lim': "Le choix des secteurs protégés est précisément l’objet du lobbying : "
           "la progressivité offre une surface d’influence que l’ouverture "
           "immédiate ne donne pas."},
   {'a': "La progressivité permet de construire des avantages comparatifs au "
         "lieu de les subir, en donnant aux branches naissantes le temps "
         "d’atteindre leur échelle.",
    'cond': "Le marché intérieur doit être assez vaste pour permettre d’atteindre "
            "cette échelle, et la concurrence interne doit être maintenue.",
    'lim': "Si le marché national est insuffisant ou si la concurrence intérieure "
           "disparaît, la protection produit des producteurs installés mais non "
           "compétitifs."}],
  [{'t': "Un calendrier progressif n’est jamais respecté : les protections "
         "transitoires deviennent permanentes.",
    'qui': "Argument de recherche de rente exposé dans le cours : la protection "
           "prolongée engendre rente, lobbying, absence d’innovation et "
           "gaspillage de ressources.",
    'rep': "L’objection est empiriquement sérieuse. Elle n’invalide pas la "
           "progressivité mais impose des dispositifs d’engagement : dégressivité "
           "automatique, clause d’extinction, évaluation indépendante."},
   {'t': "L’ouverture brutale est préférable parce qu’elle rend l’adaptation "
         "inévitable et empêche les stratégies d’attente.",
    'qui': "Position implicite des programmes d’ajustement rapide, discutée dans "
           "le cours à propos de l’ouverture et du développement.",
    'rep': "Elle suppose que les producteurs puissent s’adapter immédiatement, ce "
           "que contredit l’existence de seuils d’échelle et de capital humain "
           "spécifique : l’adaptation impossible n’est pas accélérée par "
           "l’urgence, elle est remplacée par la disparition."}],
  [{'n': "Friedrich List",
    'i': "La politique commerciale doit suivre le stade de développement : la "
         "protection ne se justifie que pendant la phase de démarrage "
         "industriel, entre une ouverture initiale et un retour au libre-échange.",
    'p': "La séquence complète — ouverture, protection pendant le démarrage, "
         "maturation, retour au libre-échange — montre que List n’est pas un "
         "théoricien de la fermeture mais du calendrier : c’est le stade de "
         "développement qui commande la politique commerciale."},
   {'n': "Friedrich List",
    'i': "Dans la phase où l’économie est encore essentiellement agricole, c’est "
         "l’ouverture, et non la protection, que List recommande.",
    'p': "Les importations permettent notamment de diversifier les "
         "approvisionnements, tandis que les gains de productivité agricoles "
         "libèrent main-d’œuvre et capital pour l’industrialisation à venir. La "
         "protection n’a donc pas de sens avant qu’il y ait quelque chose à "
         "protéger."},
   {'n': "Paul Krugman",
    'i': "Le seuil d’échelle détermine le moment où l’ouverture devient "
         "bénéfique.",
    'p': "Tant que la production nationale reste sous le seuil Q0, le coût moyen "
         "demeure supérieur au prix mondial et l’ouverture élimine le producteur ; "
         "au-delà, elle le discipline utilement. Le modèle fournit ainsi un "
         "critère objectif de calendrier."}],
  [{'f': "Pour List, la logique complète est : ouverture initiale, protection "
         "pendant le démarrage industriel, maturation, retour au libre-échange.",
    'p': "La séquence donne un contenu opérationnel à l’idée d’ouverture "
         "maîtrisée et interdit de présenter List comme un protectionniste "
         "inconditionnel."},
   {'f': "Le système commercial international admet certaines différences de "
         "traitement au bénéfice des pays en développement, selon la logique "
         "retard de développement, protection temporaire, montée en gamme, "
         "ouverture future.",
    'p': "La progressivité n’est donc pas seulement une recommandation "
         "théorique : elle est partiellement inscrite dans les règles "
         "multilatérales elles-mêmes."},
   {'f': "L’Allemagne entre tardivement dans l’industrialisation et organise son "
         "marché intérieur autour du Zollverein.",
    'p': "L’unification douanière interne précède l’ouverture externe : la "
         "séquence illustre qu’un grand marché intérieur peut être la condition "
         "préalable d’une ouverture réussie."}],
  [{'q': "Sujet du type « Faut-il s’ouvrir pour se développer ? »",
    'f': "La question n’appelle pas une réponse en oui ou non mais en "
         "calendrier : l’ouverture est favorable lorsque l’appareil productif "
         "peut en tirer parti, destructrice lorsqu’elle précède la constitution "
         "de cet appareil. Le critère n’est pas le degré d’ouverture mais sa "
         "chronologie par rapport au stade de développement.",
    'r': "On substitue à l’opposition ouverture/fermeture une analyse par phases, "
         "ce qui permet d’intégrer dans un même raisonnement les succès et les "
         "échecs des stratégies d’ouverture.",
    'ex': "La séquence de List — ouverture, protection, maturation, ouverture — "
          "et le Zollverein allemand."},
   {'q': "Sujet du type « Comment empêcher une protection temporaire de devenir "
         "permanente ? »",
    'f': "Le problème n’est pas de décider la sortie mais de la rendre crédible "
         "à l’avance : une protection sans date, sans dégressivité et sans "
         "contrepartie vérifiable crée immédiatement les intérêts qui "
         "s’opposeront à sa suppression.",
    'r': "On traite la question comme un problème d’engagement : ce sont les "
         "dispositifs institutionnels — dégressivité automatique, clause "
         "d’extinction, évaluation indépendante —, et non la bonne volonté des "
         "gouvernements successifs, qui déterminent l’issue.",
    'ex': "Le cours décrit l’enchaînement protection permanente, rente, "
          "lobbying, absence d’innovation, gaspillage des ressources."}],
  voisins=['le28-educateur', 'le28-temporaire-permanent', 'le28-couts-ouverture',
           'le28-protectionnisme'])

# ---------------------------------------------------------------- 28.06
d('le28-protectionnisme', 28, "Protectionnisme",
  "Une situation, un ensemble d’instruments, et sept justifications inégales",
  "Le protectionnisme désigne une situation dans laquelle les échanges "
  "internationaux sont entravés par des mesures publiques : droits de douane, "
  "quotas, normes, exigences de contenu local, subventions. Comme le "
  "libre-échange, il est d’abord un état observable avant d’être une doctrine. "
  "Toutes ces mesures ont un point commun : elles modifient les prix relatifs, "
  "redistribuent les surplus entre producteurs, consommateurs et État, et créent "
  "donc nécessairement des perdants.",
  "Le cours construit le protectionnisme en trois couches qu’il faut tenir "
  "séparées. La première est factuelle : le protectionnisme est un ensemble "
  "d’instruments, tarifaires et non tarifaires, dont les effets économiques "
  "diffèrent fortement — un droit de douane procure une recette publique, un "
  "quota crée une rente privée, une norme peut protéger sans être identifiée "
  "comme protectrice. La deuxième est historique : le protectionnisme a été la "
  "norme plutôt que l’exception, Bairoch décrivant le XIXᵉ siècle comme un "
  "« océan de protectionnisme », ce qui interdit de le présenter comme une "
  "déviation récente. La troisième est théorique : le cours recense sept "
  "justifications — recettes fiscales, soutien keynésien de la demande, "
  "réduction de certaines dépendances, lutte contre une concurrence jugée "
  "déloyale, protection des industries naissantes avec List, accompagnement des "
  "industries vieillissantes avec Kaldor, politique commerciale stratégique avec "
  "Brander et Spencer — en précisant que leur solidité est très inégale. Les "
  "arguments théoriques favorables au protectionnisme sont moins nombreux que "
  "ceux favorables au libre-échange, et le plus puissant d’entre eux est celui "
  "du protectionnisme éducateur. L’essentiel, pour une copie, est que chacune de "
  "ces justifications est soumise à des conditions précises : une protection "
  "échoue si elle devient permanente, si elle supprime la concurrence intérieure, "
  "si le marché national est insuffisant, ou si l’industrie protégée ne devient "
  "jamais compétitive.",
  [("La modification des prix relatifs",
    "Toute mesure protectionniste renchérit le produit importé par rapport au "
    "produit national, ce qui réoriente la demande vers les producteurs "
    "domestiques. C’est le mécanisme commun à tous les instruments, quelle que "
    "soit leur forme juridique."),
   ("La redistribution des surplus",
    "Le producteur national gagne en volume et en prix, le consommateur perd en "
    "pouvoir d’achat, l’État gagne une recette dans le cas du droit de douane. "
    "Le solde net est généralement négatif en termes d’efficacité, car une "
    "partie du surplus est détruite plutôt que transférée."),
   ("L’effet sur les entreprises utilisatrices",
    "Lorsque le bien protégé est un intrant, la mesure renchérit la production "
    "des entreprises situées en aval, qui perdent en compétitivité sur leurs "
    "propres marchés. Protéger l’acier pénalise l’industrie qui en consomme."),
   ("Les représailles",
    "Les partenaires affectés peuvent répliquer par des mesures symétriques, ce "
    "qui réduit les exportations du pays initiateur et peut annuler le gain "
    "attendu. L’effet net dépend donc de la réaction des autres, non de la seule "
    "mesure prise."),
   ("Le contournement par les firmes",
    "Les entreprises peuvent réorganiser leurs chaînes de valeur, transiter par "
    "un pays tiers ou investir sur place pour franchir la barrière. La mesure "
    "déplace alors les flux sans produire la relocalisation attendue.")],
  [{'a': "Les droits de douane procurent des recettes fiscales, un argument "
         "particulièrement pertinent lorsque la base fiscale intérieure est "
         "faible.",
    'cond': "L’argument vaut surtout pour des administrations fiscales peu "
            "développées, pour lesquelles la frontière est un point de "
            "prélèvement plus facile à contrôler que le revenu ou la "
            "consommation intérieure.",
    'lim': "La recette diminue à mesure que le droit est élevé, puisqu’il réduit "
           "les volumes importés ; et le prélèvement pèse sur les consommateurs, "
           "souvent de manière régressive."},
   {'a': "Limiter les importations peut réduire les fuites et renforcer l’effet "
         "d’une relance, selon l’argument keynésien.",
    'cond': "Il faut une économie en sous-emploi, une capacité de production "
            "nationale disponible, et l’absence de représailles qui annuleraient "
            "l’effet sur la demande extérieure.",
    'lim': "L’argument est non coopératif : si tous les pays l’appliquent, la "
           "demande mondiale se contracte et chacun perd. Son efficacité suppose "
           "donc que les autres ne fassent pas de même."},
   {'a': "La protection peut réduire certaines dépendances et préserver "
         "l’autonomie nationale dans des secteurs jugés critiques.",
    'cond': "Encore faut-il identifier correctement les dépendances réellement "
            "dangereuses, et disposer d’alternatives productives crédibles à un "
            "coût acceptable.",
    'lim': "La réduction des dépendances a un coût chiffrable en efficience, et "
           "la liste des secteurs « stratégiques » tend à s’allonger sous la "
           "pression des intérêts organisés."},
   {'a': "Des mesures compensatrices peuvent corriger une concurrence faussée par "
         "des subventions ou des pratiques de prix déloyales.",
    'cond': "La distorsion doit être établie selon des critères juridiques "
            "vérifiables, et la mesure doit être proportionnée à l’avantage "
            "indûment obtenu.",
    'lim': "La qualification de « déloyal » est elle-même un enjeu de pouvoir : "
           "l’instrument correctif peut devenir un instrument protectionniste "
           "ordinaire sous couvert de rétablissement de l’équité."}],
  [{'t': "Le protectionnisme coûte aux consommateurs et aux entreprises "
         "utilisatrices plus qu’il ne rapporte aux producteurs protégés.",
    'qui': "Analyse des surplus développée dans le cours à propos du droit de "
           "douane et des barrières non tarifaires.",
    'rep': "Le résultat est robuste en statique, mais il ne traite pas les "
           "effets dynamiques : si la protection permet l’apprentissage et "
           "l’atteinte d’une échelle, la perte statique peut être compensée par "
           "un gain futur. Tout dépend donc de la réalité de ce gain."},
   {'t': "Les mesures protectionnistes provoquent des représailles et peuvent "
         "être contournées par les firmes.",
    'qui': "Constat posé explicitement dans le cours.",
    'rep': "Cette double objection est décisive pour les mesures généralisées et "
           "visibles ; elle l’est moins pour des mesures ciblées, négociées ou "
           "inscrites dans un cadre multilatéral qui limite la riposte."},
   {'t': "Le protectionnisme engendre de la recherche de rente : les entreprises "
         "protégées investissent dans le maintien politique de leur protection "
         "plutôt que dans leur productivité.",
    'qui': "Mécanisme décrit dans le cours : protection permanente, rente, "
           "lobbying, absence d’innovation, gaspillage des ressources.",
    'rep': "L’objection vise la durée plus que le principe : elle rend la clause "
           "d’extinction et la conditionnalité indispensables, sans interdire "
           "une protection bornée dans le temps."}],
  [{'n': "Paul Bairoch",
    'i': "Le XIXᵉ siècle est un « océan de protectionnisme », y compris chez les "
         "puissances industrielles.",
    'p': "Corn Laws renforcées à partir de 1815, interdiction d’exporter "
         "certaines machines jusqu’en 1842, préférence commerciale coloniale, "
         "droits parmi les plus élevés d’Europe autour de 1820 : le Royaume-Uni "
         "ne devient réellement libre-échangiste que dans la seconde moitié du "
         "siècle."},
   {'n': "Alexander Hamilton",
    'i': "La protection temporaire comme instrument du rattrapage industriel.",
    'p': "L’idée apparaît chez lui à la fin du XVIIIᵉ siècle aux États-Unis, "
         "avant d’être systématisée par List : une économie en retard ne peut "
         "développer ses industries si elle les expose immédiatement à des "
         "concurrents déjà installés."},
   {'n': "Friedrich List",
    'i': "Le protectionnisme éducateur : protéger temporairement les industries "
         "naissantes pour permettre le rattrapage.",
    'p': "Système national d’économie politique (1841), écrit dans le contexte du "
         "retard industriel allemand face au Royaume-Uni. La protection n’est "
         "légitime que pendant la phase de démarrage et doit préparer sa propre "
         "disparition."},
   {'n': "Nicholas Kaldor",
    'i': "La protection temporaire transposée aux industries vieillissantes "
         "(1966).",
    'p': "Il s’agit de protéger temporairement une branche menacée par la "
         "concurrence afin de permettre sa reconversion ou sa montée en gamme, "
         "au risque d’entretenir des « canards boiteux »."},
   {'n': "James Brander",
    'i': "La politique commerciale stratégique : l’intervention publique modifie "
         "la concurrence entre quelques grandes firmes internationales.",
    'p': "Avec Barbara Spencer, International R&D Rivalry and Industrial "
         "Strategy (1983). Il ne s’agit plus de protéger une industrie mais de "
         "déplacer un profit oligopolistique vers la firme nationale."},
   {'n': "Barbara Spencer",
    'i': "Le soutien public crédible dissuade la firme rivale d’investir.",
    'p': "Dans un oligopole où le profit n’est accessible qu’à un petit nombre de "
         "firmes, l’engagement public de soutien modifie le calcul du concurrent "
         "étranger : l’instrument mobilisé relève en pratique largement de la "
         "subvention, notamment à la recherche."}],
  [{'f': "Le cours recense sept justifications du protectionnisme : recettes "
         "fiscales, argument keynésien, autonomie nationale, concurrence "
         "déloyale, List, Kaldor, Brander-Spencer.",
    'p': "La liste fournit à elle seule une structure de partie, et rappelle que "
         "les arguments favorables au protectionnisme sont moins nombreux que "
         "ceux favorables au libre-échange."},
   {'f': "Une protection peut échouer si elle devient permanente, si elle "
         "supprime la concurrence intérieure, si le marché national est "
         "insuffisant, ou si l’industrie protégée ne devient jamais compétitive.",
    'p': "Ces quatre causes d’échec constituent la grille d’évaluation la plus "
         "opérationnelle pour juger n’importe quelle mesure protectionniste "
         "concrète."},
   {'f': "Autour de 1820, les droits de douane britanniques figurent parmi les "
         "plus élevés d’Europe.",
    'p': "Le fait sert d’appui à la thèse selon laquelle les puissances "
         "industrielles ont libéralisé après s’être construites, et non avant."}],
  [{'q': "Sujet du type « Le protectionnisme est-il toujours néfaste ? »",
    'f': "Le protectionnisme n’est pas une doctrine unique mais un ensemble "
         "d’instruments servant des justifications de solidité très inégale. "
         "Juger le protectionnisme en bloc revient à confondre une recette "
         "douanière destinée à financer un État, une protection temporaire "
         "destinée à faire naître une industrie, et une protection permanente "
         "qui entretient une rente.",
    'r': "Le plan trie les justifications par solidité décroissante et applique "
         "à chacune la grille des quatre causes d’échec, ce qui produit une "
         "évaluation différenciée au lieu d’un verdict global.",
    'ex': "List et Krugman d’un côté, l’enchaînement protection permanente, "
          "rente, lobbying de l’autre."},
   {'q': "Sujet du type « Le libre-échange est-il toujours préférable au "
         "protectionnisme ? »",
    'f': "L’histoire économique interdit de poser la question comme celle d’une "
         "norme et de son exception : Bairoch décrit un XIXᵉ siècle "
         "protectionniste, et les droits de douane sur les manufactures ne "
         "tombent à environ 4 % qu’au terme d’un demi-siècle de négociations "
         "multilatérales.",
    'r': "Commencer par le fait historique déplace la charge de la preuve et "
         "permet d’examiner les conditions d’efficacité de chaque régime plutôt "
         "que de supposer l’un des deux naturel.",
    'ex': "Corn Laws renforcées à partir de 1815, machines dont l’exportation "
          "reste interdite jusqu’en 1842."},
   {'q': "Sujet du type « Un pays peut-il améliorer sa situation par la "
         "protection sans dégrader celle de ses partenaires ? »",
    'f': "La plupart des arguments protectionnistes sont non coopératifs : "
         "l’argument keynésien de réduction des fuites, comme le déplacement de "
         "profit oligopolistique de Brander et Spencer, supposent que les autres "
         "ne répliquent pas. Généralisés, ils détruisent le gain qu’ils "
         "promettaient individuellement.",
    'r': "Distinguer les arguments coopératifs des arguments non coopératifs "
         "permet de montrer que l’efficacité d’une mesure dépend du comportement "
         "des partenaires, donc du cadre institutionnel.",
    'ex': "Le cours souligne que les mesures protectionnistes provoquent souvent "
          "des représailles."}],
  voisins=['le28-libre-echange', 'le28-educateur', 'le28-defensif', 'le28-offensif',
           'le28-droits-douane', 'le28-non-tarifaire', 'le28-representailles'])

# ---------------------------------------------------------------- 28.07
d('le28-educateur', 28, "Protectionnisme éducateur et industries naissantes",
  "Protéger une industrie qui n’est pas encore compétitive mais peut le devenir",
  "Le protectionnisme éducateur désigne la protection temporaire d’une industrie "
  "naissante, c’est-à-dire d’une branche qui n’est pas aujourd’hui compétitive "
  "mais qui peut le devenir une fois qu’elle aura accumulé l’expérience et les "
  "volumes nécessaires. Il se distingue de toute autre protection par trois "
  "traits : il vise une industrie en formation, il est justifié par un gain "
  "futur et non par la préservation d’un acquis, et il doit organiser sa propre "
  "disparition.",
  "Le problème auquel cette politique répond est précis, et c’est lui qu’il faut "
  "exposer avant toute chose. Une entreprise étrangère déjà installée dispose "
  "d’une grande expérience, d’économies d’échelle, d’un marché important et de "
  "coûts unitaires plus faibles. Si un pays en retard s’ouvre immédiatement, "
  "l’enchaînement est mécanique : l’industrie naissante affronte des entreprises "
  "déjà compétitives, disparaît, et le rattrapage devient impossible. Le "
  "libre-échange peut donc figer les écarts de développement — ce n’est pas une "
  "objection morale, c’est une conséquence du modèle. La solution consiste à "
  "protéger temporairement l’industrie nationale : la demande domestique se "
  "reporte vers les producteurs nationaux, la production augmente, les économies "
  "d’échelle se réalisent, le coût moyen baisse, et la compétitivité finit par "
  "s’établir sans protection. Krugman formalise exactement ce mécanisme : si "
  "les coûts moyens thaïlandais peuvent à long terme devenir inférieurs aux "
  "coûts suisses, mais que les quantités produites au démarrage sont trop "
  "faibles pour y parvenir, le producteur potentiellement le plus efficace "
  "n’entre jamais sur le marché. La protection permet de franchir le seuil Q0 "
  "au-delà duquel les économies d’échelle rendent le producteur viable. Le point "
  "capital, trop souvent omis, est que List ne défend pas une fermeture "
  "permanente : la protection dépend du stade de développement, et doit "
  "disparaître à maturité. Une protection éducatrice qui ne s’éteint pas cesse "
  "d’être éducatrice et devient une rente.",
  [("Le désavantage initial du nouvel entrant",
    "Le producteur étranger installé cumule expérience, échelle, marché et coûts "
    "unitaires faibles. Le nouvel entrant produit peu, donc cher : son coût "
    "moyen dépasse le prix mondial, indépendamment de son efficacité "
    "potentielle."),
   ("Le seuil critique de production",
    "Il existe un volume Q0 au-delà duquel le coût moyen national descend sous "
    "le prix mondial. Tant que la production reste inférieure à Q0, le "
    "producteur est non compétitif ; au-delà, il l’est durablement. Le problème "
    "est donc de franchir ce seuil, non de rattraper un retard d’efficacité."),
   ("Le report de la demande domestique",
    "Droits de douane ou restriction des importations réorientent la demande "
    "nationale vers les producteurs domestiques. La production nationale "
    "augmente, ce qui déclenche les économies d’échelle et fait baisser le coût "
    "moyen."),
   ("L’apprentissage et l’accumulation d’expérience",
    "Au-delà des seules économies d’échelle statiques, la production répétée "
    "améliore les procédés, forme la main-d’œuvre et consolide les réseaux de "
    "fournisseurs. C’est le contenu proprement « éducateur » de la protection."),
   ("L’extinction de la protection",
    "Une fois le seuil franchi et la compétitivité acquise, la protection "
    "devient inutile et doit être supprimée. Maintenue, elle produit rente, "
    "lobbying, absence d’innovation et gaspillage des ressources.")],
  [{'a': "Une industrie potentiellement efficace peut ne jamais émerger sans "
         "protection : l’ouverture immédiate élimine le producteur avant qu’il "
         "n’atteigne son échelle.",
    'cond': "Il faut que l’industrie soit effectivement viable à terme, c’est-à- "
            "dire que son coût moyen de long terme puisse descendre sous le prix "
            "mondial — ce qui doit être établi et non supposé.",
    'lim': "L’identification de ces industries est difficile et politiquement "
           "manipulable : chaque branche a intérêt à se présenter comme "
           "potentiellement compétitive."},
   {'a': "La protection permet de construire un avantage comparatif plutôt que "
         "de le subir, puisque l’avantage de coût résulte ici de l’histoire et "
         "non des dotations.",
    'cond': "Le marché national doit être suffisamment vaste pour permettre "
            "d’atteindre le seuil d’échelle : la principale condition posée par "
            "le cours est l’existence d’une demande domestique assez importante.",
    'lim': "Pour une petite économie, le marché intérieur ne permet pas "
           "d’atteindre l’échelle : la stratégie suppose alors un accès à des "
           "marchés extérieurs, donc une intégration régionale ou une politique "
           "d’exportation."},
   {'a': "La protection temporaire a une justification historique : plusieurs "
         "économies aujourd’hui développées n’ont adopté le libre-échange "
         "qu’après avoir consolidé leur appareil productif.",
    'cond': "L’argument historique n’établit une causalité que si l’on montre que "
            "la protection a effectivement permis le rattrapage, et non "
            "simplement qu’elle l’a accompagné.",
    'lim': "Les contextes diffèrent : la taille des marchés, l’intensité "
           "technologique et les règles commerciales d’aujourd’hui ne sont pas "
           "celles du XIXᵉ siècle."}],
  [{'t': "La protection supprime l’aiguillon concurrentiel : abritée, "
         "l’entreprise n’a plus de raison de réduire ses coûts.",
    'qui': "Deuxième condition posée par le cours : la protection ne doit pas "
           "supprimer la concurrence intérieure.",
    'rep': "L’objection est décisive et conduit à une règle pratique : protéger "
           "contre l’extérieur tout en maintenant plusieurs producteurs en "
           "concurrence à l’intérieur. Une protection accordée à un monopole "
           "national cumule les inconvénients des deux régimes."},
   {'t': "La protection temporaire devient permanente : les entreprises "
         "protégées cherchent à maintenir politiquement leur protection même "
         "lorsqu’elle n’est plus justifiée.",
    'qui': "Troisième condition, présentée dans le cours comme la condition "
           "essentielle chez List.",
    'rep': "C’est la critique la plus solide. Elle impose des dispositifs "
           "d’extinction automatique et d’évaluation indépendante : sans eux, "
           "l’argument éducateur sert d’habillage à une rente."},
   {'t': "L’État ne dispose pas de l’information nécessaire pour identifier à "
         "l’avance les industries qui deviendront compétitives, et choisit donc "
         "en fonction du poids politique des branches plutôt que de leur "
         "potentiel réel.",
    'qui': "Objection d’information, implicite dans la quatrième cause d’échec "
           "recensée : l’industrie protégée peut ne jamais devenir compétitive.",
    'rep': "Elle plaide pour des critères objectivables — existence d’économies "
           "d’échelle, taille du marché accessible, trajectoire de coûts — "
           "plutôt que pour un renoncement, d’autant que le coût d’une erreur "
           "est borné si la protection est datée."}],
  [{'n': "Alexander Hamilton",
    'i': "La protection des industries naissantes comme condition du "
         "développement industriel américain.",
    'p': "L’idée apparaît chez lui à la fin du XVIIIᵉ siècle : un pays neuf ne "
         "peut pas développer ses manufactures s’il les expose sans délai à la "
         "concurrence des producteurs britanniques déjà établis."},
   {'n': "Friedrich List",
    'i': "Le libre-échange peut figer les écarts de développement lorsqu’une "
         "industrie naissante affronte immédiatement des producteurs déjà "
         "compétitifs.",
    'p': "Système national d’économie politique (1841). List raisonne dans le "
         "contexte du retard industriel allemand par rapport au Royaume-Uni : la "
         "protection donne à l’industrie le temps d’accumuler expérience et "
         "économies d’échelle."},
   {'n': "Friedrich List",
    'i': "La protection n’est légitime que durant le démarrage industriel.",
    'p': "Trois phases : une économie encore agricole gagne à l’ouverture ; le "
         "démarrage industriel justifie la protection ; la maturité la rend "
         "inutile. La protection doit préparer sa propre disparition."},
   {'n': "Paul Krugman",
    'i': "Formalisation du mécanisme : une industrie potentiellement compétitive "
         "peut ne jamais émerger faute d’atteindre le seuil d’échelle.",
    'p': "L’exemple du cours oppose la Suisse et la Thaïlande dans la production "
         "de montres : les coûts moyens thaïlandais peuvent devenir inférieurs "
         "à long terme, mais les faibles quantités initiales maintiennent le coût "
         "au-dessus du prix mondial."},
   {'n': "Paul Krugman",
    'i': "Réhabilitation du protectionnisme éducateur de List à partir des "
         "économies d’échelle plutôt que de l’argument du retard national.",
    'p': "Le raisonnement est appliqué au cas vietnamien : tant que la production "
         "reste inférieure à Q0, le prix vietnamien dépasse le prix mondial "
         "chinois ; une protection temporaire réoriente la demande, fait croître "
         "la production, abaisse le coût moyen, puis peut être supprimée."}],
  [{'f': "L’Allemagne entre tardivement dans l’industrialisation et organise son "
         "marché intérieur autour du Zollverein.",
    'p': "L’exemple montre que la condition de taille du marché peut être "
         "satisfaite par l’unification douanière interne avant même l’ouverture "
         "extérieure."},
   {'f': "Le cours relève que plusieurs économies aujourd’hui développées n’ont "
         "adopté pleinement le libre-échange qu’après avoir consolidé leur "
         "appareil productif.",
    'p': "Le fait renforce l’argument selon lequel l’ouverture est plus "
         "avantageuse une fois le rattrapage accompli, donc que l’ordre des "
         "politiques compte autant que leur contenu."},
   {'f': "L’Union européenne présente un retard dans certaines technologies — "
         "numérique, semi-conducteurs, technologies de la transition, certaines "
         "technologies vertes.",
    'p': "Le cours en déduit qu’un pays avancé peut être « en développement » "
         "relativement à une frontière technologique sectorielle : l’argument "
         "des industries naissantes se transpose alors à une filière plutôt qu’à "
         "un pays."},
   {'f': "Des droits compensateurs peuvent être défendus comme une protection "
         "temporaire permettant aux producteurs européens de se réindustrialiser "
         "et de monter en gamme face à des producteurs étrangers subventionnés.",
    'p': "L’enchaînement — subventions étrangères, désavantage européen, "
         "protection temporaire, investissements, rattrapage — montre la "
         "réactivation contemporaine de l’argument de List dans une économie "
         "avancée."}],
  [{'q': "Sujet du type « Faut-il protéger une industrie avant de l’exposer à la "
         "concurrence internationale ? »",
    'f': "La réponse dépend entièrement de la raison pour laquelle l’industrie "
         "n’est pas compétitive. Si elle ne l’est pas parce qu’elle produit trop "
         "peu pour réaliser ses économies d’échelle, une protection temporaire "
         "peut lui permettre de franchir le seuil et de devenir durablement "
         "viable ; si elle ne l’est pas parce que ses coûts de long terme "
         "resteront supérieurs au prix mondial, la protection ne fera que "
         "différer sa disparition en la faisant payer aux consommateurs.",
    'r': "Le critère discriminant est la trajectoire du coût moyen de long terme, "
         "que le modèle de Krugman permet d’expliciter : c’est lui qui sépare le "
         "protectionnisme éducateur du soutien à une activité non viable.",
    'ex': "Suisse et Thaïlande dans l’horlogerie : le coût thaïlandais peut "
          "devenir inférieur, mais seulement au-delà d’un certain volume."},
   {'q': "Sujet du type « Le protectionnisme est-il toujours éducateur ? »",
    'f': "Le protectionnisme n’est éducateur que s’il réunit trois conditions : "
         "une industrie dont la viabilité future est établie, un marché intérieur "
         "assez vaste pour atteindre l’échelle critique, et une concurrence "
         "maintenue à l’intérieur du marché protégé. Il faut y ajouter une "
         "quatrième condition, décisive chez List : la protection doit être "
         "strictement temporaire.",
    'r': "Formuler la réponse comme une liste de conditions vérifiables permet de "
         "traiter successivement les cas où le protectionnisme éduque et ceux où "
         "il entretient une rente, sans trancher par avance.",
    'ex': "L’enchaînement décrit par le cours : protection permanente, rente, "
          "lobbying, absence d’innovation, gaspillage des ressources."},
   {'q': "Sujet du type « Les avantages comparatifs sont-ils donnés ou "
         "construits ? »",
    'f': "Le protectionnisme éducateur est la démonstration que l’avantage "
         "comparatif peut être construit : s’il existe un seuil de production "
         "au-delà duquel un pays devient le producteur le moins coûteux, alors "
         "c’est l’histoire, et non la dotation, qui détermine qui occupe cette "
         "position — et une politique peut en changer l’issue.",
    'r': "On oppose la conception statique de l’avantage, héritée de Ricardo et "
         "du modèle HOS, à la conception dynamique issue des rendements "
         "croissants, ce qui donne au sujet une véritable progression théorique.",
    'ex': "Krugman montre que le producteur potentiellement le plus efficace peut "
          "ne jamais entrer sur le marché."}],
  voisins=['le28-protectionnisme', 'le28-offensif', 'le28-temporaire-permanent',
           'le28-ouverture-progressive', 'le28-vieillissantes',
           'le28-politique-strategique'])
