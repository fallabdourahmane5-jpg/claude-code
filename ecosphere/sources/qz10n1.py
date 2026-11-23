# -*- coding: utf-8 -*-
"""Chapitre 10 — questions nouvelles, sous-parties c10-01 à c10-05."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c10-01
f(id='q10-n01', sp='c10-01', niv='comprendre', type='qcmm', b=1,
  q="Pour la sociologie, que peut être l’entreprise au-delà d’un lieu de "
    "production ? (plusieurs réponses)",
  opts=["Une organisation",
        "Un lieu de coopération et un lieu de conflits",
        "Un espace où s’exercent des rapports de pouvoir",
        "Un espace où les comportements individuels sont influencés par des "
        "règles collectives",
        "Un marché où se forment les prix des facteurs"],
  ans=[0, 1, 2, 3],
  why=["Exacte : « entreprise = organisation » est le mot-clé de "
       "l’introduction.",
       "Exacte : coopération et conflit sont indissociables, et c’est l’une "
       "des grandes questions du chapitre.",
       "Exacte : c’est précisément l’objet de l’analyse de Crozier.",
       "Exacte : c’est la définition durkheimienne du poids du social sur "
       "l’individu.",
       "La formation des prix est un objet d’analyse économique, non le "
       "regard sociologique annoncé ici."],
  exp="Le chapitre part de l’idée que faire de la sociologie consiste à faire "
      "la science des phénomènes sociaux : observer des situations "
      "particulières, étudier des comportements individuels, puis repérer "
      "derrière ces cas singuliers des régularités et des tendances "
      "générales. Appliquée à l’entreprise, cette démarche révèle une "
      "organisation traversée par la coopération, le conflit, le pouvoir et "
      "les règles collectives.",
  diss="Le cours souligne que les frontières entre économie et sociologie sont "
       "aujourd’hui moins nettes : certains sociologues étudient les "
       "phénomènes économiques, certains économistes les relations sociales."),

f(id='q10-n02', sp='c10-01', niv='comprendre', type='qcm', b=40,
  q="Comment le cours définit-il le fait d’être rationnel, et quelle "
    "difficulté la sociologie apporte-t-elle à cette définition ?",
  opts=["Être rationnel, c’est maximiser son profit ; la sociologie montre "
        "que les individus y parviennent rarement",
        "Être rationnel, c’est utiliser sa raison pour poursuivre un "
        "objectif ; la sociologie montre que plusieurs formes de rationalité "
        "existent et que toutes les actions ne relèvent pas du calcul "
        "coûts-avantages",
        "Être rationnel, c’est respecter les règles de l’organisation ; la "
        "sociologie montre que ces règles sont arbitraires",
        "Être rationnel, c’est agir sans émotion ; la sociologie montre que "
        "les émotions sont toujours mauvaises conseillères"],
  ans=1,
  why=["Le profit n’est qu’un objectif possible : la définition est plus "
       "large.",
       "La rationalité ne se confond pas avec l’obéissance aux règles, même "
       "si la domination légale-rationnelle les lie.",
       "Le cours ne condamne pas les émotions : il en fait un déterminant de "
       "l’action chez Weber."],
  exp="En économie, la rationalité est souvent présentée sous la forme d’un "
      "calcul coûts-avantages : l’individu cherche les moyens les plus "
      "efficaces d’atteindre son objectif. La sociologie montre que toutes "
      "les actions humaines ne répondent pas à cette logique, que plusieurs "
      "formes de rationalité peuvent exister, et que même une organisation "
      "très rationnelle peut produire des effets négatifs.",
  diss="Ces trois idées annoncent exactement le plan du chapitre : Weber pour "
       "les formes de rationalité, Bronner et Morel pour ses limites, Crozier "
       "pour les effets pervers de l’organisation rationnelle."),

f(id='q10-n03', sp='c10-01', niv='raisonner', type='qcm', b=29,
  q="Parmi les grandes questions annoncées en introduction, laquelle structure "
    "l’ensemble du chapitre ?",
  opts=["Comment mesurer la productivité d’une organisation ?",
        "Jusqu’où les organisations peuvent-elles être réellement "
        "rationnelles ?",
        "Comment fixer le niveau optimal des salaires ?",
        "Quelle est la taille optimale d’une entreprise ?"],
  ans=1,
  why=["La productivité intervient dans l’enquête de Mayo, mais comme "
       "symptôme et non comme problème central.",
       "Le niveau des salaires n’est pas la question directrice de ce "
       "chapitre de sociologie.",
       "La taille optimale de la firme est une question d’économie, traitée "
       "dans le chapitre sur la concentration."],
  exp="L’introduction pose quatre questions : la rationalité étudiée par les "
      "économistes est-elle la même que celle étudiée par les sociologues ? "
      "jusqu’où les organisations peuvent-elles être réellement rationnelles ? "
      "comment expliquer à la fois la coopération et les conflits au sein de "
      "l’entreprise ? quelle relation existe entre l’individu et le collectif ? "
      "C’est la deuxième qui commande l’enchaînement Weber – Mayo – Bronner – "
      "Morel – Crozier.",
  diss="Réponse d’ensemble du chapitre : l’entreprise est bien un lieu de "
       "rationalité, mais une rationalité limitée par les biais cognitifs, "
       "les dynamiques collectives et les rapports de pouvoir."),

f(id='q10-n04', sp='c10-01', niv='comprendre', type='vf', b=9,
  q="Faire de la sociologie consiste à décrire des cas particuliers sans "
    "chercher à en tirer de généralités.",
  ans=False,
  exp="Le cours dit l’inverse : faire de la sociologie consiste à faire la "
      "science des phénomènes sociaux. Le sociologue observe des situations "
      "particulières et étudie des comportements individuels, mais c’est pour "
      "repérer derrière ces cas singuliers des régularités et des tendances "
      "générales. La démarche part donc du cas concret pour aller vers le "
      "général.",
  diss="Même exigence que celle rappelée en économie : partir de faits "
       "empiriques pour dégager des régularités."),

# ------------------------------------------------------------- c10-02
f(id='q10-n05', sp='c10-02', niv='connaitre', type='qcm', b=62,
  q="Comment Durkheim définit-il le fait social ?",
  opts=["Un comportement observé chez la majorité des individus d’une société",
        "Des « manières d’agir, de penser et de sentir, extérieures à "
        "l’individu et qui sont douées d’un pouvoir de coercition en vertu "
        "duquel elles s’imposent à lui »",
        "Le sens subjectif qu’un individu donne à son action",
        "Une régularité statistique sans portée explicative"],
  ans=1,
  why=["La fréquence ne suffit pas : ce qui définit le fait social est son "
       "extériorité et sa contrainte.",
       "Le sens subjectif de l’action est l’objet de la sociologie "
       "wébérienne.",
       "Durkheim utilise les statistiques comme outil, mais le fait social "
       "n’est pas réduit à une régularité : il explique."],
  exp="Cette définition contient deux éléments décisifs : l’extériorité — la "
      "société existe avant l’individu — et la coercition — elle lui impose "
      "des normes, des règles et des comportements. L’individu est donc "
      "fortement influencé par son environnement social : les manières de se "
      "comporter et de respecter certaines règles ne sont pas inventées "
      "individuellement, elles sont transmises par la société.",
  diss="Définition à citer mot pour mot : c’est la pierre de touche du "
       "holisme méthodologique."),

f(id='q10-n06', sp='c10-02', niv='raisonner', type='assoc', b=157,
  q="Associez chaque approche à la limite que le cours lui reconnaît.",
  ans=[["Le holisme méthodologique de Durkheim", "Un risque de déterminisme ou de sociologisme : quelle liberté reste-t-il aux individus ?"],
       ["Expliquer les comportements par les seules structures sociales", "Un risque de déterminisme : comment expliquer les comportements atypiques et le changement social ?"],
       ["L’individualisme méthodologique compréhensif de Weber", "Un risque de relativisme : comment dégager des régularités générales ?"],
       ["Partir du sens subjectif que les individus donnent à leurs actions", "Un risque de relativisme : la subjectivité rend la généralisation plus difficile"]],
  exp="Le cours ne tranche pas entre les deux méthodes : il en montre les "
      "coûts symétriques. Si la société détermine presque entièrement les "
      "individus, on ne comprend plus ni leur liberté, ni les comportements "
      "atypiques, ni le changement social. Si chaque comportement dépend de "
      "la subjectivité, la sociologie peine à établir des régularités.",
  diss="Position équilibrée à adopter en dissertation : les deux démarches "
       "sont complémentaires, et le chapitre les utilise tour à tour."),

f(id='q10-n07', sp='c10-02', niv='appliquer', type='assoc', b=176,
  q="Associez chaque situation au déterminant de l’action correspondant chez "
    "Weber.",
  ans=[["Un ingénieur choisit les matériaux et les techniques permettant de construire efficacement un pont", "L’action rationnelle en finalité"],
       ["Un capitaine reste sur son navire en train de couler parce qu’il considère qu’il s’agit de son devoir", "L’action rationnelle en valeur"],
       ["Une personne accomplit les gestes routiniers de sa journée sans y réfléchir", "Le comportement traditionnel"],
       ["Une personne réagit immédiatement sous le coup de l’émotion", "Le comportement affectuel"]],
  exp="La typologie wébérienne sert un argument précis : l’être humain n’agit "
      "pas toujours comme un homo œconomicus. Seule la première forme "
      "ressemble au calcul coûts-avantages. Weber ajoute cependant que les "
      "sociétés modernes accordent une place croissante à la rationalité en "
      "finalité : c’est le processus de rationalisation.",
  diss="Exemple du cours à retenir pour montrer que l’observation ne suffit "
       "pas : trois salariés travaillent tard pour trois raisons différentes."),

# ------------------------------------------------------------- c10-03
f(id='q10-n08', sp='c10-03', niv='connaitre', type='qcm', b=238,
  q="Comment le cours définit-il la rationalisation chez Weber ?",
  opts=["La transformation des entreprises en bureaucraties publiques",
        "Le processus historique par lequel les activités humaines sont de "
        "plus en plus organisées selon des principes de calcul, de méthode et "
        "d’efficacité",
        "La diminution progressive des inégalités sociales",
        "La mécanisation de la production industrielle"],
  ans=1,
  why=["La bureaucratie est un résultat de la rationalisation, pas sa "
       "définition, et elle n’est pas nécessairement publique.",
       "Les inégalités ne sont pas l’objet de ce concept.",
       "La mécanisation est un phénomène technique : la rationalisation est "
       "bien plus large et touche de nombreuses sphères."],
  exp="La rationalisation est pour Weber le processus caractéristique de la "
      "modernité par lequel la rationalité en finalité, fondée sur le calcul, "
      "la méthode et l’efficacité, occupe une place croissante dans les "
      "activités humaines. Les sociétés modernes cherchent de plus en plus à "
      "prévoir les conséquences et à rendre les comportements prévisibles.",
  diss="Elle ne concerne pas seulement l’économie : elle touche de nombreuses "
       "sphères, ce qui peut provoquer des conflits de valeurs — économie "
       "contre religion, science contre religion."),

f(id='q10-n09', sp='c10-03', niv='raisonner', type='qcm', b=294,
  q="Quelle limite Weber reconnaît-il au désenchantement du monde ?",
  opts=["La science finit toujours par être réfutée",
        "La science explique comment un phénomène se produit, mais ne répond "
        "pas toujours à la question du sens, ce qui peut entraîner une perte "
        "de sens",
        "Les explications magiques restent plus efficaces",
        "La rationalisation ne concerne que les sociétés occidentales"],
  ans=1,
  why=["Weber ne met pas en doute la validité du savoir scientifique.",
       "Le cours ne soutient nulle part l’efficacité supérieure des "
       "explications magiques.",
       "La limite évoquée n’est pas géographique mais porte sur ce que la "
       "science peut dire."],
  exp="La foudre n’est plus expliquée comme la manifestation d’une puissance "
      "divine mais par des phénomènes physiques et électriques : le monde "
      "devient rationnellement explicable. Mais la science répond surtout à "
      "la question « comment », et pas toujours à « quel sens donner à la "
      "souffrance ? » ou « quel sens donner à la mort ? ». La rationalisation "
      "peut donc entraîner une perte de sens.",
  diss="Cette limite éclaire l’ambivalence générale de Weber : la "
       "rationalisation est un progrès d’efficacité qui a un coût existentiel, "
       "comme la bureaucratie est une efficacité qui a un coût de liberté."),

f(id='q10-n10', sp='c10-03', niv='comprendre', type='qcm', b=307,
  q="Sur quoi repose le capitalisme moderne selon Weber ?",
  opts=["Sur le simple désir de gagner de l’argent",
        "Sur la recherche rationnelle du profit, qui suppose d’organiser "
        "méthodiquement l’activité pour rendre le profit calculable et "
        "prévisible",
        "Sur la propriété héréditaire des entreprises",
        "Sur la domination charismatique des grands entrepreneurs"],
  ans=1,
  why=["Le cours précise explicitement qu’il ne suffit pas de vouloir gagner "
       "de l’argent : le désir du gain existe dans toutes les sociétés.",
       "Les fonctions héréditaires caractérisent au contraire les "
       "organisations traditionnelles que Weber oppose à l’entreprise "
       "rationalisée.",
       "Le charisme est l’une des trois dominations, mais ce n’est pas le "
       "fondement du capitalisme moderne."],
  exp="Pour Weber, le capitalisme moderne repose sur la recherche "
      "rationnelle du profit : il faut organiser méthodiquement l’activité "
      "afin de rendre le profit calculable et prévisible. L’organisation "
      "passe donc des fonctions héréditaires et des structures peu organisées "
      "à des qualifications et diplômes, des procédures et des fonctions "
      "clairement définies — règles, qualifications, procédures, hiérarchie.",
  diss="C’est ce passage qui fait le lien avec L’Éthique protestante et "
       "l’esprit du capitalisme (1905) et avec l’analyse de la bureaucratie."),

f(id='q10-n11', sp='c10-03', niv='appliquer', type='assoc', b=335,
  q="Associez chaque situation au type de domination correspondant.",
  ans=[["On obéit parce que « cela a toujours fonctionné ainsi »", "La domination traditionnelle"],
       ["On obéit à un chef religieux en raison de ses qualités personnelles exceptionnelles", "La domination charismatique"],
       ["On obéit au médecin du fait de sa qualification et au juge en raison de sa fonction", "La domination légale-rationnelle"],
       ["On obéit au supérieur hiérarchique en raison du poste qu’il occupe", "La domination légale-rationnelle"]],
  exp="La domination est définie comme la capacité à obtenir l’obéissance ; "
      "ce qui change d’un type à l’autre, c’est la raison pour laquelle "
      "l’obéissance est jugée légitime : la tradition, les qualités "
      "personnelles, ou les règles et la compétence qu’elles reconnaissent. "
      "Dans la domination légale-rationnelle, on obéit moins à la personne "
      "qu’à la fonction.",
  diss="Le cours prévient : dans la réalité les trois formes se combinent, et "
       "le sociologue doit observer quelles légitimités sont réellement "
       "mobilisées."),

# ------------------------------------------------------------- c10-04
f(id='q10-n12', sp='c10-04', niv='comprendre', type='qcmm', b=443,
  q="Quelles caractéristiques Weber attribue-t-il à la bureaucratie ? "
    "(plusieurs réponses)",
  opts=["Une division du travail attribuant à chacun une fonction clairement "
        "définie",
        "Un recrutement fondé sur les diplômes et les compétences "
        "professionnelles",
        "Une hiérarchie clairement définie, représentée par un organigramme",
        "Des décisions fondées sur des règles impersonnelles, et un statut "
        "attaché au poste et non à la personne",
        "La transmission du poste aux enfants du titulaire lors de son départ"],
  ans=[0, 1, 2, 3],
  why=["Exacte : chacun exerce une fonction déterminée au sein de la "
       "coopération.",
       "Exacte : on passe d’une logique de naissance à une logique de "
       "compétence.",
       "Exacte : elle permet d’attribuer clairement les responsabilités.",
       "Exacte : les règles impersonnelles réduisent l’arbitraire, et le "
       "statut protège le salarié des décisions arbitraires.",
       "C’est précisément ce que la bureaucratie exclut : l’individu n’est pas "
       "propriétaire de son poste, une nouvelle personne est sélectionnée "
       "selon les règles."],
  exp="Six caractéristiques sont énumérées par le cours : division du "
      "travail, recrutement selon les compétences, hiérarchie définie, "
      "décisions fondées sur des règles impersonnelles, statut associé au "
      "poste, séparation entre la personne et sa fonction. Leur point commun "
      "est de réduire l’arbitraire : la décision ne dépend plus des "
      "préférences personnelles du supérieur."),

f(id='q10-n13', sp='c10-04', niv='comprendre', type='qcm', b=427,
  q="Pourquoi faut-il faire attention au sens du mot « bureaucratie » chez "
    "Weber ?",
  opts=["Parce que Weber réserve le terme aux administrations publiques",
        "Parce que le terme a aujourd’hui une connotation négative — lourdeur, "
        "lenteur, paperasse — alors que Weber en fait l’organisation "
        "rationnelle de la coopération entre un grand nombre d’individus",
        "Parce que Weber l’emploie comme un synonyme de hiérarchie",
        "Parce que le mot désigne chez lui un groupe social précis, les "
        "fonctionnaires"],
  ans=1,
  why=["Weber décrit un idéal-type d’organisation, qui vaut aussi pour "
       "l’entreprise moderne.",
       "La hiérarchie n’est qu’une des six caractéristiques de la "
       "bureaucratie.",
       "Weber mentionne bien le risque d’un groupe bureaucratique défendant "
       "ses intérêts, mais ce n’est pas la définition du mot."],
  exp="Pour Weber, la bureaucratie est une organisation rationnelle de la "
      "coopération entre un grand nombre d’individus dont chacun exerce une "
      "fonction déterminée. C’est l’idéal-type de l’organisation rationnelle "
      "moderne, et donc un concept d’analyse et non un jugement. Le sens "
      "péjoratif courant est au contraire ce que décriront Crozier, avec le "
      "cercle vicieux bureaucratique, et Morel, avec les décisions absurdes.",
  diss="Piège de vocabulaire fréquent : ne pas prêter à Weber la critique de "
       "la bureaucratie, qui vient après lui."),

f(id='q10-n14', sp='c10-04', niv='comprendre', type='qcm', b=512,
  q="Sur quels trois éléments repose l’entreprise moderne rationalisée selon "
    "Weber ?",
  opts=["La propriété, le capital et le profit",
        "La division du travail, une organisation formalisée et la domination "
        "légale-rationnelle",
        "Le charisme du dirigeant, la tradition et la loi",
        "L’innovation, la concurrence et la publicité"],
  ans=1,
  why=["Ces notions décrivent l’entreprise capitaliste, non son mode "
       "d’organisation rationnelle.",
       "Le charisme et la tradition sont les deux autres types de "
       "domination : ce ne sont pas les fondements de l’entreprise "
       "rationalisée.",
       "Ces éléments relèvent de l’analyse économique des stratégies, non de "
       "l’analyse wébérienne de l’organisation."],
  exp="Chaque individu exerce une fonction particulière : c’est la division "
      "du travail. Les positions et les relations hiérarchiques apparaissent "
      "dans des documents écrits : c’est l’organisation formalisée. Les "
      "individus acceptent l’autorité parce que les fonctions sont légalement "
      "établies, que les titulaires sont supposés compétents et que des règles "
      "définissent les responsabilités : c’est la domination "
      "légale-rationnelle."),

f(id='q10-n15', sp='c10-04', niv='raisonner', type='ordre', b=534,
  q="Remettez dans l’ordre le paradoxe de la rationalisation qui conduit à la "
    "« cage d’acier ».",
  ans=["La rationalisation doit permettre aux individus de mieux maîtriser le "
       "monde et d’organiser efficacement leurs activités",
       "L’organisation se dote de règles, de procédures et de routines de "
       "plus en plus nombreuses",
       "L’efficacité progresse : les décisions deviennent prévisibles et "
       "l’arbitraire reculera",
       "Mais les procédures se multiplient et les individus perdent de leur "
       "autonomie",
       "La rationalisation enferme finalement les individus dans une « cage "
       "d’acier » de règles et de routines"],
  exp="Le paradoxe tient en une phrase du cours : plus une organisation "
      "devient rationnelle, plus elle peut devenir efficace, mais plus elle "
      "risque aussi de réduire la liberté et l’autonomie individuelles. Weber "
      "ajoute le risque qu’un groupe bureaucratique finisse par défendre ses "
      "propres intérêts.",
  diss="Enchaînement à réutiliser pour toute dissertation sur les effets "
       "pervers de la rationalisation, de Weber à Crozier."),

# ------------------------------------------------------------- c10-05
f(id='q10-n16', sp='c10-05', niv='appliquer', type='qcm', b=610,
  q="Entre 1924 et 1927, l’expérience sur l’éclairage à la Western Electric "
    "donne les résultats suivants : la productivité augmente quand "
    "l’éclairage augmente, quand il diminue, et aussi dans le groupe de "
    "contrôle où rien ne change. Qu’en conclut-on ?",
  opts=["Que l’éclairage n’a aucun effet sur le travail humain",
        "Que la hausse de productivité ne peut pas s’expliquer uniquement par "
        "les conditions matérielles de travail : d’autres facteurs doivent "
        "intervenir",
        "Que l’expérience a été mal conduite et doit être abandonnée",
        "Que les ouvrières ont été mieux rémunérées"],
  ans=1,
  why=["La conclusion n’est pas que l’éclairage est indifférent, mais qu’il "
       "n’explique pas à lui seul les résultats.",
       "L’expérience n’est pas invalidée : son résultat paradoxal est "
       "précisément ce qui ouvre la recherche.",
       "La rémunération n’a pas changé dans cette première expérience : elle "
       "sera l’une des variables modifiées dans la Test Room."],
  exp="Le résultat est paradoxal : dans les trois configurations, la "
      "productivité augmente. Il devient donc difficile d’expliquer cette "
      "hausse par les seules conditions matérielles. C’est ce paradoxe qui "
      "conduit Mayo et son équipe à observer de beaucoup plus près un petit "
      "groupe d’ouvrières, dans l’expérience de la Test Room.",
  diss="Bel exemple de raisonnement scientifique : c’est un résultat "
       "inattendu, et non une hypothèse de départ, qui fait naître l’École "
       "des relations humaines."),

f(id='q10-n17', sp='c10-05', niv='connaitre', type='qcm', b=629,
  q="En quoi consiste l’expérience de la « Test Room » menée entre 1927 et "
    "1929 ?",
  opts=["Un questionnaire adressé à l’ensemble des 29 000 salariés de "
        "l’usine",
        "Un petit groupe d’ouvrières volontaires est isolé dans un atelier "
        "pour assembler des relais téléphoniques, les contremaîtres étant "
        "remplacés par des chercheurs qui les observent",
        "Une comparaison entre deux usines situées dans des villes "
        "différentes",
        "Une expérience sur l’éclairage des ateliers"],
  ans=1,
  why=["L’enquête par entretiens vient ensuite, et porte sur environ 20 000 "
       "entretiens.",
       "Aucune comparaison entre deux usines n’est menée.",
       "L’expérience sur l’éclairage est la première, menée entre 1924 et "
       "1927."],
  exp="Plusieurs éléments sont successivement modifiés — système de "
      "rémunération, pauses, horaires — et la productivité est mesurée après "
      "chaque modification. Elle augmente d’environ 20 %, et continue parfois "
      "d’augmenter même lorsque les chercheurs détériorent volontairement "
      "certaines conditions de travail. Le remplacement des contremaîtres par "
      "des chercheurs observateurs est un élément décisif de l’explication.",
  diss="Détail à retenir pour la critique : les ouvrières sont volontaires et "
       "savent qu’elles participent à une expérience — d’où l’effet "
       "Hawthorne."),

f(id='q10-n18', sp='c10-05', niv='comprendre', type='qcm', b=665,
  q="Qu’apporte la vaste enquête par entretiens menée par Mayo et son équipe ?",
  opts=["Elle montre que les salaires sont la seule motivation réelle des "
        "salariés",
        "Elle met en évidence l’importance de l’écoute — le bon agent de "
        "maîtrise doit être un interlocuteur plutôt qu’un simple chef "
        "autoritaire — et l’importance du sens donné au travail",
        "Elle prouve que la productivité dépend uniquement de "
        "l’organisation technique",
        "Elle démontre que les ouvrières de la Test Room avaient été mal "
        "sélectionnées"],
  ans=1,
  why=["Le cours montre au contraire que le travail n’est pas seulement "
       "motivé par la rémunération.",
       "L’organisation technique est précisément ce que ces résultats "
       "relativisent.",
       "La critique des échantillons vient d’autres auteurs, pas de cette "
       "enquête."],
  exp="Environ 20 000 entretiens sont réalisés. Ils confirment que les "
      "travailleurs recherchent non seulement une rémunération, mais aussi de "
      "l’écoute, de la reconnaissance et du sens dans leur activité. Le "
      "manager doit donc être davantage un interlocuteur capable d’écouter "
      "qu’un chef autoritaire.",
  diss="Ces deux résultats — écoute et sens — sont ceux qui font le lien avec "
       "la « recherche d’un travail qui a du sens » étudiée en fin de "
       "chapitre."),

f(id='q10-n19', sp='c10-05', niv='comprendre', type='qcm', b=705,
  q="Qu’est-ce qu’une norme informelle de production, et quel est son effet ?",
  opts=["Une norme de qualité imposée par la direction",
        "Un niveau de production fixé par le groupe de travail lui-même : "
        "celui qui travaille trop vite comme celui qui travaille trop "
        "lentement peut être rappelé à l’ordre",
        "Un objectif chiffré inscrit dans le contrat de travail",
        "Une règle syndicale de limitation du temps de travail"],
  ans=1,
  why=["La direction fixe l’organisation officielle : la norme informelle "
       "échappe précisément à celle-ci.",
       "Rien de contractuel ici : la norme est informelle, c’est-à-dire non "
       "écrite.",
       "Les syndicats ne sont pas à l’origine de ce mécanisme, même s’ils ont "
       "critiqué les interprétations de l’enquête."],
  exp="Mayo montre que les individus appartiennent à des groupes, et que ces "
      "groupes produisent leurs propres normes. Les ouvriers adaptent leur "
      "productivité à celle du groupe, qui exerce une pression dans les deux "
      "sens. La productivité n’est donc pas uniquement déterminée par "
      "l’organisation officielle de l’entreprise : elle dépend aussi de "
      "l’organisation informelle du groupe.",
  diss="Notion charnière : elle annonce la distinction du monde formel et du "
       "monde informel chez Crozier."),

]
