# -*- coding: utf-8 -*-
"""Chapitre 4 — complément de questions « Appliquer » et « Raisonner ».

Le chapitre de microéconomie se prête particulièrement au calcul et au
raisonnement : élasticités et typologie des biens, effet de substitution et
effet de revenu, rendements factoriels et rendements d'échelle, lien entre
productivité et coûts, conditions de rentabilité, portée réelle du théorème
d'Arrow-Debreu et de la critique Sonnenschein-Mantel-Debreu, rationalité
limitée et biais. Chaque renvoi a été vérifié dans le texte du cours.
"""


def f(**kw):
    return kw


L = [

# ----------------------------- c4-01 · préférences et arbitrage
f(id='q4-m01', sp='c4-01', niv='appliquer', type='qcm', b=128,
  q="Un consommateur maximise son utilité sous contrainte de budget. Que "
    "vaut alors son taux marginal de substitution entre deux biens ?",
  opts=["Le rapport des prix des deux biens",
        "Le rapport des quantités consommées",
        "Zéro, puisque l’utilité est maximale",
        "Le rapport des utilités totales"],
  ans=0,
  why=["Le rapport des quantités décrit le panier choisi, pas la condition "
       "d’optimalité.",
       "Un TMS nul signifierait que le consommateur ne consent plus aucune "
       "substitution : ce n’est pas la condition d’équilibre.",
       "L’arbitrage se fait à la marge : ce sont les utilités marginales, et "
       "non les utilités totales, qui interviennent."],
  exp="À l’optimum, le taux auquel le consommateur accepte d’échanger un "
      "bien contre l’autre sans changer de satisfaction — le TMS, pente de "
      "la courbe d’indifférence — égale le taux auquel le marché lui permet "
      "de le faire, c’est-à-dire le rapport des prix, pente de la droite de "
      "budget. Tant que les deux diffèrent, l’agent peut gagner en utilité "
      "en modifiant son panier : la tangence est la condition d’arrêt.",
  diss="Cette égalité est le prototype du raisonnement marginaliste : "
       "l’optimum se situe là où le taux d’échange subjectif rejoint le taux "
       "d’échange objectif."),

f(id='q4-m02', sp='c4-01', niv='raisonner', type='qcm', b=131,
  q="Le prix du burger baisse, celui de la glace ne change pas. Pourquoi le "
    "cours décompose-t-il la réaction du consommateur en deux effets ?",
  opts=["Parce qu’une baisse de prix modifie à la fois le prix relatif — "
        "effet de substitution — et le pouvoir d’achat réel — effet de revenu",
        "Parce que le consommateur ne sait pas quoi choisir",
        "Parce que l’utilité marginale est décroissante",
        "Parce que les deux biens sont complémentaires"],
  ans=0,
  why=["L’indécision n’a rien à voir : la décomposition est analytique, pas "
       "psychologique.",
       "La décroissance de l’utilité marginale explique la forme des courbes, "
       "non la décomposition de l’effet prix.",
       "La complémentarité ou la substituabilité se mesure par l’élasticité "
       "croisée : c’est une autre question."],
  exp="Une variation de prix agit par deux canaux distincts. L’effet de "
      "substitution : le burger devenant relativement moins cher, on en "
      "consomme plus et on consomme moins de glace. L’effet de revenu : à "
      "revenu nominal inchangé, la baisse d’un prix élève le revenu réel — "
      "les néoclassiques raisonnent en termes réels — ce qui permet de "
      "consommer davantage des deux biens. L’effet total observé est la "
      "somme des deux, et leur sens peut diverger.",
  diss="La décomposition explique les cas limites : c’est lorsque l’effet de "
       "revenu l’emporte et joue en sens contraire qu’apparaît un bien de "
       "Giffen."),

# ----------------------------------------- c4-02 · les élasticités
f(id='q4-m03', sp='c4-02', niv='appliquer', type='assoc', b=177,
  q="Associez chaque mesure d’élasticité à ce qu’elle permet d’établir.",
  ans=[["Élasticité-prix de la demande",
        "Si le bien est élastique ou inélastique au prix"],
       ["Élasticité-revenu de la demande",
        "Si le bien est normal, supérieur ou inférieur"],
       ["Élasticité-prix croisée",
        "Si deux biens sont complémentaires, substituables ou indépendants"]],
  exp="Une élasticité n’est rien d’autre qu’un rapport entre deux variations : "
      "ce qui change d’une élasticité à l’autre, c’est la variable mise au "
      "dénominateur. Le cours insiste sur l’usage : ces trois mesures "
      "servent à classer les biens, au point que « dire le nom du bien, "
      "c’est déjà dire comment sa demande réagit ». Il rattache d’ailleurs "
      "la loi d’Engel à l’élasticité-revenu, nommée après coup.",
  diss="Savoir quelle élasticité répond à quelle question évite la confusion "
       "la plus coûteuse en microéconomie : un bien inférieur n’est pas un "
       "bien inélastique."),

f(id='q4-m04', sp='c4-02', niv='appliquer', type='qcm', b=232,
  q="Le prix des places de cinéma augmente et la demande de vidéo à la "
    "demande progresse. Que vaut l’élasticité-prix croisée, et comment "
    "qualifier les deux biens ?",
  opts=["Elle est positive : les biens sont substituables",
        "Elle est négative : les biens sont complémentaires",
        "Elle est nulle : les biens sont indépendants",
        "Elle est positive : les biens sont complémentaires"],
  ans=0,
  why=["Une élasticité croisée négative signale au contraire des biens "
       "complémentaires : la hausse du prix de l’un réduit la demande de "
       "l’autre.",
       "Une élasticité nulle correspond au cas neutre, où la demande de l’un "
       "ne réagit pas au prix de l’autre.",
       "Le signe est bon mais la conclusion ne l’est pas : une élasticité "
       "croisée positive caractérise des substituts."],
  exp="Le signe fait la typologie. Croisée positive : le prix de B monte, la "
      "demande de A monte aussi — le consommateur remplace B par A, les "
      "biens sont substituables ; c’est exactement l’exemple du cinéma et de "
      "la vidéo à la demande. Croisée négative : le prix de B monte, la "
      "demande de A baisse — on les consomme ensemble, ils sont "
      "complémentaires. Croisée nulle : les biens sont indépendants.",
  diss="L’élasticité croisée est l’outil qui permet de définir un marché "
       "pertinent en droit de la concurrence : deux biens très substituables "
       "appartiennent au même marché."),

f(id='q4-m05', sp='c4-02', niv='raisonner', type='qcm', b=167,
  q="Un médicament vital n’a aucun substitut. Que peut en déduire le "
    "producteur, et qu’en subit le consommateur ?",
  opts=["La demande est inélastique : le producteur peut relever son prix "
        "sans grande perte de volume, et les dépenses du consommateur "
        "augmentent mécaniquement",
        "La demande est élastique : toute hausse de prix effondrerait les "
        "ventes",
        "La demande est inélastique : baisser le prix ferait fortement "
        "augmenter les ventes",
        "L’élasticité ne se définit pas pour les biens de santé"],
  ans=0,
  why=["L’absence de substitut rend justement la demande peu sensible au "
       "prix.",
       "C’est le contraire : si la demande ne réagit pas au prix, une baisse "
       "ne la stimule guère — le cours note que « baisser les prix ne sert à "
       "rien ».",
       "L’élasticité se mesure pour tout bien ; la santé en fournit "
       "précisément le cas extrême."],
  exp="Le cours relie explicitement l’inélasticité à l’absence de "
      "substitution : le consommateur « ne peut pas substituer, il est "
      "contraint de payer plus, ses dépenses augmentent mécaniquement ». "
      "Pour le producteur, c’est « une assurance » : il peut augmenter ses "
      "prix sans trop de risque. L’élasticité n’est donc pas une "
      "caractéristique neutre : elle mesure un rapport de force, et c’est "
      "pourquoi l’État régule les prix de certains de ces biens.",
  diss="Faire de l’élasticité un indicateur de pouvoir de marché, et non un "
       "simple coefficient, transforme une question technique en argument de "
       "politique économique."),

f(id='q4-m06', sp='c4-02', niv='raisonner', type='vf', b=249,
  q="Vrai ou faux : l’élasticité-prix d’un bien est une caractéristique fixe "
    "de ce bien. Justifiez.",
  ans=False,
  exp="Le cours est net : « l’élasticité n’est pas une constante ». Elle "
      "dépend du temps — à court terme le consommateur n’a pas encore "
      "d’alternative, à long terme il en trouve, de sorte que la demande "
      "devient plus élastique —, de l’existence de substituts, et du "
      "comportement des consommateurs. Un même bien peut donc être "
      "inélastique dans l’immédiat et élastique à horizon de quelques "
      "années : c’est ce qui explique qu’une taxe produise peu d’effet la "
      "première année et davantage ensuite.",
  diss="La dimension temporelle de l’élasticité est l’argument décisif en "
       "faveur des signaux-prix durables : une fiscalité écologique ne "
       "produit ses effets qu’à mesure que les substituts apparaissent."),

# ------------------------------------- c4-03 · théorie du producteur
f(id='q4-m07', sp='c4-03', niv='appliquer', type='qcm', b=334,
  q="Une entreprise double simultanément son capital et son travail, et sa "
    "production est multipliée par 2,4. De quels rendements s’agit-il, et à "
    "quel horizon raisonne-t-on ?",
  opts=["Rendements d’échelle croissants, à long terme puisque tous les "
        "facteurs varient",
        "Rendements factoriels décroissants, à court terme",
        "Rendements d’échelle constants, à long terme",
        "Rendements d’échelle décroissants, à court terme"],
  ans=0,
  why=["Les rendements factoriels supposent qu’un seul facteur varie, les "
       "autres étant fixes : ce n’est pas le cas ici.",
       "Des rendements constants auraient multiplié la production par 2 "
       "exactement.",
       "Des rendements décroissants donneraient un facteur inférieur à 2, et "
       "les rendements d’échelle ne se définissent qu’à long terme."],
  exp="Tout tient à la distinction d’horizon. À court terme, un seul facteur "
      "varie : on parle de rendements factoriels et la productivité "
      "marginale finit par décroître, le capital étant fixe. À long terme, "
      "tous les facteurs varient dans les mêmes proportions : on parle de "
      "rendements d’échelle, croissants si la production augmente plus que "
      "proportionnellement, constants si elle suit, décroissants sinon. Le "
      "cours rappelle que le court et le long terme sont des notions "
      "logiques, non des durées en années.",
  diss="Associer rendements croissants, économies d’échelle et division du "
       "travail chez Smith permet de relier microéconomie et analyse de la "
       "concentration industrielle."),

f(id='q4-m08', sp='c4-03', niv='raisonner', type='qcm', b=502,
  q="La productivité marginale du travail diminue. Que devient le coût "
    "marginal, et pourquoi ?",
  opts=["Il augmente : coût marginal et productivité marginale varient en "
        "sens inverse, puisqu’il faut plus de travail pour une unité "
        "supplémentaire",
        "Il diminue, car l’entreprise produit davantage",
        "Il reste constant, les salaires étant fixés par le marché",
        "Il augmente seulement si le prix de vente baisse"],
  ans=0,
  why=["Produire davantage ne fait pas baisser le coût marginal lorsque la "
       "productivité recule : c’est l’inverse.",
       "Le salaire unitaire peut être constant ; c’est la quantité de "
       "travail nécessaire par unité produite qui augmente.",
       "Le prix de vente n’intervient pas dans le calcul du coût : il "
       "intervient ensuite, pour juger de la rentabilité."],
  exp="Le lien est mécanique : si une unité supplémentaire de travail produit "
      "moins, alors il faut davantage de travail — donc de dépense — pour "
      "obtenir une unité de plus de production. Le cours énonce la règle sous "
      "forme symétrique : le coût marginal varie en sens inverse de la "
      "productivité marginale, le coût moyen en sens inverse de la "
      "productivité moyenne. C’est ce qui donne aux courbes de coût leur "
      "forme en U.",
  diss="Ce lien productivité-coût est le chaînon qui relie l’analyse "
       "technique de la production à l’analyse économique des prix."),

f(id='q4-m09', sp='c4-03', niv='appliquer', type='qcm', b=510,
  q="Une entreprise vend à un prix supérieur à son coût variable moyen mais "
    "inférieur à son coût moyen total. Que conclut l’analyse du cours ?",
  opts=["Elle n’est pas rentable à terme, mais elle a intérêt à poursuivre à "
        "court terme puisqu’elle couvre ses coûts variables",
        "Elle est rentable, puisqu’elle couvre ses coûts variables",
        "Elle doit cesser immédiatement toute production",
        "Elle est rentable à terme mais pas à court terme"],
  ans=0,
  why=["Couvrir les seuls coûts variables ne suffit pas à la rentabilité : "
       "les coûts fixes restent à financer.",
       "Cesser toute production obligerait à supporter les coûts fixes sans "
       "aucune recette : la perte serait plus grande.",
       "L’énoncé inverse les horizons : c’est à court terme que la poursuite "
       "se justifie."],
  exp="Deux seuils, deux horizons. Le seuil de fermeture est le coût variable "
      "moyen : en deçà, chaque unité produite aggrave la perte. Le seuil de "
      "rentabilité est le coût moyen total : « une entreprise est rentable "
      "que si elle couvre son coût moyen », dans le cadre de la concurrence "
      "pure et parfaite où elle est preneuse de prix. Entre les deux, "
      "l’entreprise perd de l’argent mais limite sa perte en produisant : "
      "le cours note qu’en début d’activité, couvrir les coûts variables "
      "peut suffire à rester viable.",
  diss="La distinction des deux seuils permet d’expliquer pourquoi des "
       "entreprises déficitaires continuent de produire, sans y voir une "
       "irrationalité."),

f(id='q4-m10', sp='c4-03', niv='raisonner', type='ordre', b=368,
  q="Remettez dans l’ordre l’enchaînement qui conduit une entreprise des "
    "économies aux déséconomies d’échelle.",
  ans=["L’entreprise augmente tous ses facteurs de production",
       "La spécialisation du travail et une meilleure organisation font "
       "progresser la production plus que proportionnellement",
       "La taille atteint un seuil au-delà duquel la coordination devient "
       "difficile",
       "La gestion se complexifie et l’entreprise devient trop grande",
       "Les coûts augmentent plus vite que la production : c’est la "
       "déséconomie d’échelle"],
  exp="Les rendements d’échelle ne sont pas constants sur toute la plage de "
      "production : le cours décrit d’abord des gains liés à la "
      "spécialisation — explicitement rattachés à Smith — puis des pertes "
      "liées à la coordination, à la complexité de gestion et à la taille. "
      "C’est ce retournement qui donne à la courbe de coût moyen de long "
      "terme sa forme en U et qui fixe une taille optimale.",
  diss="L’existence d’une taille optimale est l’argument qui empêche de "
       "conclure que la concentration est toujours efficace."),

# -------------------------- c4-04 et c4-05 · équilibre et ses limites
f(id='q4-m11', sp='c4-04', niv='raisonner', type='qcm', b=526,
  q="Quelle est la principale critique adressée au raisonnement en équilibre "
    "partiel ?",
  opts=["L’hypothèse « toutes choses égales par ailleurs » ne tient pas, car "
        "les marchés sont interdépendants",
        "Il ne permet pas de calculer les élasticités",
        "Il suppose que les entreprises fixent leurs prix",
        "Il ignore le comportement des consommateurs"],
  ans=0,
  why=["Les élasticités se calculent précisément dans ce cadre.",
       "En concurrence pure et parfaite, le producteur est au contraire "
       "preneur de prix.",
       "L’équilibre partiel confronte bien offre et demande : il ne néglige "
       "pas le consommateur."],
  exp="Marshall raisonne ceteris paribus : on met un marché « au "
      "microscope » en supposant le reste inchangé. La démarche est "
      "légitime comme simplification, mais le cours en pointe la limite : "
      "les marchés sont interdépendants, de sorte que l’hypothèse ne tient "
      "pas. C’est cette interdépendance que Sonnenschein invoque pour "
      "montrer que la forme même de la courbe de demande agrégée est "
      "incertaine.",
  diss="Opposer équilibre partiel et équilibre général permet de poser "
       "proprement la question des effets de bouclage, centrale dès qu’on "
       "évalue une politique économique."),

f(id='q4-m12', sp='c4-05', niv='raisonner', type='courte', b=736,
  q="Le théorème d’Arrow-Debreu prouve-t-il que le marché conduit à "
    "l’équilibre ? Répondez précisément.",
  ans={'modele':
       "Non : il prouve seulement qu’un équilibre général peut exister, et "
       "encore sous des hypothèses extrêmement restrictives — rationalité, "
       "concurrence parfaite, information complète. Or l’existence n’est pas "
       "la stabilité. La question de savoir si le système converge vers cet "
       "équilibre reçoit une réponse négative : il n’existe pas de mécanisme "
       "automatique assurant le retour à l’équilibre. L’équilibre général "
       "peut donc exister tout en étant totalement instable, ce qui prive la "
       "démonstration de sa portée pratique.",
       'cles': [{'f': ['existe', 'existence'],
                 'l': 'le théorème porte sur l’existence'},
                {'f': ['hypothese', 'restrictive', 'stricte'],
                 'l': 'sous des hypothèses très restrictives'},
                {'f': ['stabilit', 'instable', 'converge', 'retour'],
                 'l': 'il ne dit rien de la stabilité'},
                {'f': ['pas de mecanisme', 'aucun mecanisme', 'automatique'],
                 'l': 'aucun mécanisme automatique de retour à l’équilibre'}]},
  exp="Le cours sépare soigneusement deux questions : « est-ce que "
      "l’équilibre existe ? » et « est-ce que le système y converge ? ». "
      "Arrow et Debreu répondent à la première, sous conditions très "
      "strictes. La seconde reçoit une réponse « beaucoup plus inquiétante "
      "pour la théorie néoclassique » : rien ne garantit la convergence. "
      "C’est le point que la critique Sonnenschein-Mantel-Debreu prolonge en "
      "montrant que la demande agrégée peut prendre n’importe quelle forme.",
  diss="Distinguer existence et stabilité est la façon la plus rigoureuse de "
       "critiquer l’autorégulation : on ne conteste pas le théorème, on "
       "montre ce qu’il ne dit pas."),

f(id='q4-m13', sp='c4-05', niv='raisonner', type='qcm', b=743,
  q="Que montrent Sonnenschein, Mantel et Debreu à propos de la demande "
    "agrégée ?",
  opts=["Qu’elle peut prendre n’importe quelle forme — croissante, "
        "chaotique — même si les demandes individuelles sont régulières : "
        "une microéconomie « propre » ne garantit pas une macroéconomie "
        "« propre »",
        "Qu’elle est toujours décroissante, comme la demande individuelle",
        "Que les consommateurs ne sont pas rationnels",
        "Que l’équilibre général n’existe pas"],
  ans=0,
  why=["C’est précisément ce que leur résultat interdit de conclure : "
       "l’agrégation ne transmet pas les propriétés individuelles.",
       "Le résultat ne porte pas sur la rationalité individuelle, qui est "
       "maintenue par hypothèse.",
       "L’existence est acquise par Arrow-Debreu : c’est la forme et la "
       "stabilité qui sont en cause."],
  exp="Le résultat est un théorème d’impossibilité sur l’agrégation : même en "
      "partant d’agents parfaitement rationnels, la fonction de demande "
      "agrégée ne conserve pas les propriétés des demandes individuelles. "
      "Le cours ajoute que Steve Keen reprend cette critique pour contester "
      "la forme habituellement donnée aux courbes, et note qu’on continue "
      "malgré tout de les tracer décroissantes faute de mieux.",
  diss="Cet argument est le plus solide contre l’usage macroéconomique des "
       "courbes d’offre et de demande : il vient de l’intérieur de la "
       "théorie, pas d’une critique hétérodoxe externe."),

f(id='q4-m14', sp='c4-04', niv='appliquer', type='vf', b=753,
  q="Vrai ou faux : une situation Pareto-optimale est nécessairement une "
    "situation juste. Justifiez.",
  ans=False,
  exp="L’optimum de Pareto est un critère d’efficacité, non d’équité : une "
      "situation est Pareto-optimale si l’on ne peut améliorer le sort de "
      "quelqu’un sans détériorer celui d’un autre. Une répartition "
      "extrêmement inégale peut satisfaire ce critère, dès lors que tout "
      "transfert ferait un perdant. Le critère dit seulement qu’il n’existe "
      "plus de gain mutuel disponible ; il ne dit rien du point de départ ni "
      "de la distribution atteinte.",
  diss="Rappeler que Pareto mesure l’efficacité et non la justice est "
       "indispensable dès qu’un sujet porte sur les inégalités : cela ouvre "
       "la distinction entre efficacité et équité."),

# ------------------- c4-06 · rationalité limitée et comportements
f(id='q4-m15', sp='c4-06', niv='appliquer', type='qcm', b=811,
  q="Un acheteur renonce à comparer toutes les offres et retient la première "
    "qui lui paraît satisfaisante. Quel concept cette conduite "
    "illustre-t-elle ?",
  opts=["La rationalité limitée de Herbert Simon",
        "Le biais d’ancrage",
        "L’asymétrie d’information d’Akerlof",
        "L’optimum de Pareto"],
  ans=0,
  why=["Le biais d’ancrage désigne l’influence d’un chiffre initial, même "
       "arbitraire, sur les décisions suivantes.",
       "L’asymétrie d’information suppose qu’une partie en sait plus que "
       "l’autre : ici, l’acheteur choisit de ne pas chercher davantage.",
       "L’optimum de Pareto est un critère d’efficacité collective, sans "
       "rapport avec la décision individuelle."],
  exp="Simon ne dit pas que les agents sont irrationnels : il montre qu’ils "
      "disposent d’une information limitée, de capacités cognitives bornées "
      "et d’un temps contraint. Ils ne maximisent donc pas, ils se "
      "satisfont d’une solution suffisante. C’est la rationalité limitée, "
      "qui vise directement l’hypothèse de rationalité parfaite de la "
      "microéconomie néoclassique.",
  diss="Simon ouvre la voie à toute l’économie comportementale : il déplace "
       "la critique de la conclusion — l’équilibre — vers l’hypothèse — la "
       "rationalité."),

f(id='q4-m16', sp='c4-06', niv='raisonner', type='assoc', b=917,
  q="Associez chaque auteur à l’hypothèse de la concurrence pure et parfaite "
    "qu’il met en défaut, selon le cours.",
  ans=[["Herbert Simon", "La rationalité parfaite : l’information et les "
                         "capacités cognitives sont limitées"],
       ["Daniel Kahneman", "La rationalité parfaite encore : le système 1, "
                           "rapide et intuitif, produit des biais"],
       ["George Akerlof", "La transparence de l’information : certains "
                          "agents en savent plus que d’autres"]],
  exp="Les trois critiques se complètent. Simon montre que l’agent ne peut "
      "pas tout calculer ; Kahneman, dans Système 1 / Système 2 (2011), "
      "montre qu’il ne le veut pas toujours, la pensée rapide et "
      "émotionnelle l’emportant dans la plupart des décisions quotidiennes ; "
      "Akerlof montre que l’information elle-même est inégalement répartie. "
      "Le cours en tire une conclusion commune : si les comportements sont "
      "biaisés et les informations asymétriques, le marché ne garantit plus "
      "automatiquement une allocation efficace.",
  diss="Organiser les critiques par hypothèse attaquée — plutôt que par "
       "auteur — donne une architecture immédiate à une partie de "
       "dissertation sur les limites du modèle concurrentiel."),

f(id='q4-m17', sp='c4-06', niv='appliquer', type='qcm', b=946,
  q="Un vendeur affiche d’abord un prix barré très élevé, puis le prix réel. "
    "Quel biais exploite-t-il ?",
  opts=["Le biais d’ancrage : un chiffre initial, même arbitraire, oriente "
        "les jugements ultérieurs",
        "L’aversion à la perte",
        "La rationalité limitée",
        "L’effet de démonstration"],
  ans=0,
  why=["L’aversion à la perte porte sur l’asymétrie entre gains et pertes "
       "ressentis, non sur l’effet d’un point de référence affiché.",
       "La rationalité limitée est le cadre général ; l’ancrage en est une "
       "manifestation précise.",
       "L’effet de démonstration relève de l’analyse de la consommation chez "
       "Duesenberry, au chapitre 1."],
  exp="L’ancrage est un biais systématique : le premier chiffre rencontré "
      "sert de point de référence, même lorsqu’il est arbitraire ou sans "
      "rapport avec la valeur du bien. Le prix barré fabrique cette "
      "référence, et le prix réel paraît ensuite avantageux par comparaison. "
      "Le cours rattache ce type d’erreur au système 1 de Kahneman : rapide, "
      "intuitif, mobilisé dans la plupart des décisions quotidiennes.",
  diss="Les biais cognitifs ne sont pas des curiosités : ils sont "
       "délibérément exploités par les stratégies commerciales, ce qui "
       "justifie une régulation de l’information du consommateur."),

f(id='q4-m18', sp='c4-06', niv='raisonner', type='courte', b=1022,
  q="Quelle conséquence le cours tire-t-il, pour l’efficacité du marché, des "
    "travaux sur la rationalité et l’information ?",
  ans={'modele':
       "Si les comportements sont biaisés, stratégiques et influencés par les "
       "croyances, et si l’information est inégalement répartie, alors le "
       "marché ne garantit plus automatiquement une allocation efficace des "
       "ressources. L’économie expérimentale et la théorie des jeux ajoutent "
       "que la rationalité individuelle ne conduit pas toujours à "
       "l’efficacité collective : les individus sont influencés par "
       "l’équité et par leurs croyances sur le comportement d’autrui. La "
       "conclusion n’est pas que le marché est inutile, mais que son "
       "efficacité est conditionnelle, et qu’elle dépend d’hypothèses que "
       "la réalité ne vérifie pas toujours.",
       'cles': [{'f': ['biais', 'strategique', 'croyance'],
                 'l': 'des comportements biaisés et stratégiques'},
                {'f': ['allocation', 'efficac'],
                 'l': 'l’allocation efficace n’est plus garantie'},
                {'f': ['jeux', 'experimental'],
                 'l': 'l’apport de la théorie des jeux et de l’expérimentation'},
                {'f': ['collectiv', 'equite'],
                 'l': 'rationalité individuelle ≠ efficacité collective'}]},
  exp="Le cours construit sa conclusion en trois temps : les agents ne sont "
      "ni parfaitement rationnels — Simon, Kahneman — ni parfaitement "
      "informés — Akerlof ; les comportements sont stratégiques et dépendent "
      "des croyances ; donc l’allocation efficace n’est plus automatique. "
      "La formulation importe : il s’agit d’une efficacité conditionnelle, "
      "non d’une réfutation du marché.",
  diss="Cette conclusion mesurée est exactement le ton attendu : elle permet "
       "de justifier une intervention ciblée — information, régulation — sans "
       "verser dans le rejet du mécanisme marchand."),
]
