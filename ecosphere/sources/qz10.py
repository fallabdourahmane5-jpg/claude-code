# -*- coding: utf-8 -*-
"""Chapitre 10 — Sociologie des organisations, rationalité et travail."""

SP = {
 'c10-01': 'Introduction : sociologie des organisations et formes de rationalité',
 'c10-02': 'Durkheim et Weber : deux méthodes ; les quatre déterminants de l’action',
 'c10-03': 'Rationalisation, désenchantement du monde et les trois types de domination',
 'c10-04': 'Idéal-type, neutralité axiologique, bureaucratie et « cage d’acier »',
 'c10-05': 'Elton Mayo, la Western Electric, l’École des relations humaines, effet Hawthorne',
 'c10-06': 'Bronner : marché cognitif, invariants mentaux, médias et algorithmes',
 'c10-07': 'Fausses informations, chambres d’écho, loi de Brandolini, démocratie des crédules',
 'c10-08': 'Morel : Challenger, hiérarchie, conformisme d’Asch, pensée de groupe',
 'c10-09': 'Morel : le lien avec Weber et les métarègles',
 'c10-10': 'Crozier : cercle vicieux bureaucratique, monde formel et monde informel, la SEITA',
 'c10-11': 'Crozier : le pouvoir comme relation, zones d’incertitude, quatre sources de pouvoir',
 'c10-12': 'Crozier : analyse stratégique, coopération conflictuelle, résistance au changement',
 'c10-13': 'Durkheim : intégration, régulation, anomie, égoïsme, groupe professionnel',
 'c10-14': 'Durkheim : solidarité mécanique, solidarité organique, division du travail',
 'c10-15': 'Tertiarisation, salarisation, protections, flexibilité, précarité, Castel',
 'c10-16': 'Désaffiliation, question sociale, transformations du monde ouvrier',
 'c10-17': 'Inégalités de statut, de temps de travail, de salaire ; mesure du chômage',
 'c10-18': 'Les syndicats : organisations, syndicalisation, institutionnalisation, crise',
}

# Questions écartées : chacune reprend, sous forme de vrai/faux inversé ou de
# QCM redondant, une question déjà posée ailleurs dans le chapitre.
DROP = [
 'ch10-vf-1',    # ≡ ch10-qcm-1 (traiter les faits sociaux comme des choses)
 'ch10-vf-2',    # ≡ ch10-qcm-3 (l’individualisme méthodologique est wébérien)
 'ch10-vf-4',    # ≡ ch10-qcm-10 (l’idéal-type n’est pas une description du réel)
 'ch10-vf-6',    # ≡ ch10-open-5 (l’effet Hawthorne fragilise l’interprétation)
 'ch10-vf-9',    # ≡ ch10-aut195-1 (l’asymétrie de la loi de Brandolini)
 'ch10-qcm-24',  # ≡ ch10-aut195-1 (même énoncé, options moins informatives)
 'ch10-vf-14',   # ≡ ch10-qcm-35 (la zone d’incertitude, source de pouvoir)
 'ch10-vf-15',   # ≡ ch10-qcm-37 (le pouvoir n’est pas qu’au sommet)
]


def f(**kw):
    return kw


FIX = {

# =============================================================== c10-02
'ch10-qcm-1': f(niv='connaitre', sp='c10-02', b=79,
 exp="« Il faut traiter les faits sociaux comme des choses » est la règle "
     "méthodologique célèbre de Durkheim. Elle signifie que le sociologue "
     "doit écarter ses opinions personnelles, utiliser notamment des méthodes "
     "statistiques et rechercher des relations objectives entre les "
     "phénomènes, comme le ferait un naturaliste avec son objet d’étude.",
 why=["Traiter les faits sociaux comme des opinions reviendrait précisément à "
      "ce que Durkheim veut éviter : la subjectivité du chercheur.",
      "Partir des intentions des acteurs est la démarche de Weber, la "
      "sociologie compréhensive.",
      "Durkheim cherche des régularités, donc l’inverse de l’exception."],
 diss="Formule la plus citable de la méthode durkheimienne : elle fonde "
      "l’objectivité du regard sociologique."),
'ch10-qcm-2': f(niv='comprendre', sp='c10-02', b=121,
 exp="Dans le holisme méthodologique, la société constitue une réalité "
     "distincte de la simple somme des individus et capable d’exercer une "
     "contrainte sur eux. Le rôle du sociologue est donc d’identifier les "
     "structures sociales qui influencent les individus : on explique le "
     "comportement individuel par le social qui le précède.",
 why=["Le sens subjectif des acteurs est le point de départ de "
      "l’individualisme méthodologique de Weber.",
      "Les préférences économiques renvoient à l’homo œconomicus, que le "
      "chapitre présente d’ailleurs comme un idéal-type.",
      "Le hasard n’explique rien en sociologie : le fait social est "
      "précisément ce qui se répète."],
 diss="Opposition à poser d’emblée : Durkheim explique, Weber comprend."),
'ch10-qcm-3': f(niv='connaitre', sp='c10-02', b=134,
 exp="L’individualisme méthodologique est la démarche de Weber : il part des "
     "individus et de leurs actions pour comprendre la société, dans une "
     "approche microsociologique et compréhensive. Le holisme méthodologique "
     "est au contraire la position de Durkheim.",
 why=["Durkheim défend le holisme méthodologique, c’est-à-dire la démarche "
      "inverse.",
      "Mayo est l’auteur des expériences de la Western Electric et de "
      "l’École des relations humaines.",
      "Crozier développe l’analyse stratégique des organisations, bien "
      "postérieure à ce débat de méthode."]),
'ch10-qcm-4': f(niv='connaitre', sp='c10-02', b=97,
 exp="Pour Weber, la sociologie étudie l’activité sociale, définie comme une "
     "« action significative orientée vers autrui ». Il ne suffit donc pas "
     "d’observer ce que fait un individu : il faut comprendre quel sens il "
     "donne à son comportement et quelles motivations l’orientent. C’est la "
     "sociologie compréhensive.",
 why=["Une action isolée et sans but n’est pas une activité sociale : il "
      "manque l’orientation vers autrui.",
      "Weber ne réduit pas l’action sociale à l’économie : il distingue au "
      "contraire quatre déterminants de l’action.",
      "Une action imposée par la loi relèverait de la contrainte, non du sens "
      "subjectif."],
 diss="Exemple du cours à réutiliser : trois salariés travaillent tard, l’un "
      "pour une promotion, l’autre par devoir moral, le troisième par "
      "habitude — même comportement, trois sens sociologiques."),
'ch10-qcm-5': f(niv='connaitre', sp='c10-02', b=178,
 exp="L’action rationnelle en finalité consiste à adapter les moyens employés "
     "aux objectifs poursuivis, en tenant compte des conséquences prévisibles "
     "de l’action : l’individu compare les moyens disponibles, choisit le plus "
     "efficace et anticipe les effets. C’est la forme de rationalité la plus "
     "proche de celle de l’homo œconomicus.",
 why=["La coutume caractérise le comportement traditionnel.",
      "Les émotions caractérisent le comportement affectuel.",
      "Une croyance religieuse relèverait plutôt de l’action rationnelle en "
      "valeur."],
 diss="Exemple du cours : l’ingénieur qui choisit matériaux et techniques "
      "pour construire efficacement un pont."),
'ch10-qcm-6': f(niv='comprendre', sp='c10-02', b=193,
 exp="L’action rationnelle en valeur est guidée par des convictions "
     "auxquelles l’individu accorde une valeur propre, indépendamment des "
     "conséquences. Elle reste rationnelle, mais par rapport à des valeurs et "
     "non à un résultat : le capitaine qui reste sur son navire en train de "
     "couler agit de manière absurde en coûts-avantages, mais cohérente par "
     "rapport à son devoir.",
 why=["La maximisation du profit renvoie à l’action rationnelle en finalité.",
      "L’habitude définit le comportement traditionnel.",
      "La contrainte extérieure n’est pas un déterminant de l’action dans la "
      "typologie wébérienne."],
 diss="Démonstration importante : une action peut être rationnelle sans être "
      "intéressée. L’économie ne détient pas le monopole de la rationalité."),
'ch10-qcm-7': f(niv='connaitre', sp='c10-02', b=207,
 exp="Le comportement traditionnel est dicté par l’habitude ou la coutume : "
     "l’individu agit ainsi parce qu’on a toujours fait ainsi, en reproduisant "
     "un comportement transmis. Le cours souligne qu’une grande partie des "
     "gestes routiniers de la vie quotidienne relève de cette catégorie.",
 why=["Le calcul caractérise l’action rationnelle en finalité.",
      "L’émotion caractérise le comportement affectuel.",
      "La hiérarchie relève de la domination, question distincte de celle des "
      "déterminants de l’action."]),
'ch10-qcm-8': f(niv='connaitre', sp='c10-02', b=216,
 exp="Le comportement affectuel est déterminé par les émotions et les "
     "sentiments immédiats : la personne réagit sur le moment, sans calcul ni "
     "référence à une valeur ou à une tradition. C’est la quatrième des "
     "formes d’action distinguées par Weber.",
 why=["Les règles renvoient à la domination légale-rationnelle, non à "
      "l’affect.",
      "La religion relève plutôt de l’action rationnelle en valeur ou du "
      "comportement traditionnel.",
      "Le contrat est une forme juridique, pas un déterminant affectif de "
      "l’action."],
 diss="Les quatre déterminants servent un seul argument : l’être humain "
      "n’agit pas toujours comme un homo œconomicus."),
'ch10-open-1': f(niv='raisonner', sp='c10-02', b=156,
 exp="Durkheim adopte une approche holiste et macrosociologique : la société "
     "est une réalité distincte de la somme des individus, capable d’exercer "
     "une contrainte sur eux ; le sociologue explique donc les comportements "
     "individuels par les structures sociales et doit traiter les faits "
     "sociaux comme des choses, en écartant ses opinions et en recourant aux "
     "statistiques. Weber adopte une approche individualiste, "
     "microsociologique et compréhensive : il part du sens subjectif que les "
     "individus donnent à leurs actions, l’activité sociale étant une action "
     "significative orientée vers autrui. Chaque démarche a sa limite : le "
     "holisme risque un déterminisme excessif qui réduit la marge de manœuvre "
     "des individus et rend difficile l’explication des comportements "
     "atypiques et du changement social ; l’approche compréhensive risque le "
     "relativisme, car l’insistance sur la subjectivité rend plus difficile le "
     "dégagement de régularités.",
 diss="Les deux approches ne sont pas exclusives : tout le chapitre les fait "
      "travailler ensemble, Durkheim pour l’intégration par le travail, Weber "
      "pour la rationalité des organisations."),
'ch10-open-2': f(niv='connaitre', sp='c10-02', b=176,
 exp="Weber distingue quatre déterminants de l’action. L’action rationnelle "
     "en finalité adapte les moyens au but poursuivi en anticipant les "
     "conséquences : c’est la forme la plus proche de l’homo œconomicus, "
     "illustrée par l’ingénieur qui choisit les techniques les plus efficaces. "
     "L’action rationnelle en valeur est accomplie au nom d’une conviction, "
     "indépendamment de ses conséquences : le capitaine qui reste sur son "
     "navire. Le comportement traditionnel est dicté par l’habitude ou la "
     "coutume, et couvre une grande partie des gestes routiniers. Le "
     "comportement affectuel est déterminé par les émotions et les sentiments "
     "immédiats. Cette typologie montre que l’être humain n’agit pas toujours "
     "comme un homo œconomicus ; Weber ajoute toutefois que les sociétés "
     "modernes accordent une place croissante à la rationalité en finalité, "
     "ce qu’il appelle la rationalisation."),

# =============================================================== c10-03
'ch10-qcm-9': f(niv='comprendre', sp='c10-03', b=281,
 exp="Le désenchantement du monde désigne le recul des explications magiques "
     "et religieuses au profit d’une compréhension rationnelle et "
     "scientifique du monde. L’exemple du cours est la foudre, qui n’est plus "
     "expliquée comme la manifestation d’une puissance divine mais par des "
     "phénomènes physiques et électriques. Weber signale une limite : la "
     "science explique comment, pas toujours pourquoi, d’où un risque de perte "
     "de sens.",
 why=["Weber n’annonce aucune fin du capitalisme : il en analyse au contraire "
      "le fondement rationnel.",
      "La productivité n’est pas en cause : il s’agit d’un phénomène "
      "culturel et cognitif.",
      "Le syndicalisme est traité dans une autre partie du chapitre, sans lien "
      "avec ce concept."],
 diss="Point de bascule du chapitre : c’est ce concept que Bronner viendra "
      "discuter, en montrant que plus d’informations ne produit pas "
      "mécaniquement plus de rationalité."),
'ch10-qcm-10': f(niv='connaitre', sp='c10-03', b=384,
 exp="L’idéal-type est une construction intellectuelle abstraite servant à "
     "analyser la réalité. Le sociologue sélectionne certains traits d’un "
     "phénomène, les organise de façon cohérente et accentue volontairement "
     "certains d’entre eux pour faire apparaître la logique du phénomène. Le "
     "mot « idéal » ne signifie donc nullement « souhaitable ».",
 why=["Ce n’est pas une moyenne statistique : l’idéal-type accentue des "
      "traits au lieu de les lisser.",
      "Ce n’est pas un modèle à imiter : la confusion vient du mot « idéal ».",
      "Ce n’est pas une norme juridique : l’idéal-type est un outil de "
      "connaissance, pas une prescription."],
 diss="Exemple donné par le cours : l’homo œconomicus est lui-même un "
      "idéal-type, puisqu’aucun individu réel ne se comporte exactement ainsi."),
'ch10-qcm-12': f(niv='connaitre', sp='c10-03', b=335,
 exp="Weber construit trois types idéaux de domination — la domination étant "
     "définie comme la capacité à obtenir l’obéissance. La domination "
     "traditionnelle repose sur la croyance dans le caractère légitime ou "
     "sacré des traditions, la domination charismatique sur les qualités "
     "personnelles exceptionnelles attribuées à un individu, la domination "
     "légale-rationnelle sur les règles et les compétences.",
 why=["Deux types seraient insuffisants : il manquerait le charisme ou la "
      "tradition.",
      "Quatre correspond au nombre de déterminants de l’action, non au "
      "nombre de dominations.",
      "Weber n’en distingue pas cinq : attention à ne pas confondre les deux "
      "typologies du chapitre."],
 diss="Le cours précise que dans la réalité les trois formes se combinent : un "
      "dirigeant tire son autorité de son poste, de son expérience et de sa "
      "personnalité."),
'ch10-qcm-13': f(niv='comprendre', sp='c10-03', b=360,
 exp="La domination légale-rationnelle repose sur la croyance dans la "
     "légitimité des règles et dans la compétence de ceux auxquels ces règles "
     "donnent une autorité : on obéit moins à la personne qu’à la fonction "
     "qu’elle occupe. Le cours cite le médecin du fait de sa qualification, le "
     "juge en raison de sa fonction, le supérieur en raison de son poste.",
 why=["Le charisme d’un chef définit la domination charismatique.",
      "La tradition définit la domination traditionnelle.",
      "La force physique n’est pas une forme de légitimité : la domination, "
      "chez Weber, suppose une obéissance jugée légitime."],
 diss="C’est cette forme de domination qui prend sa forme la plus aboutie "
      "dans la bureaucratie."),
'ch10-qcm-14': f(niv='comprendre', sp='c10-03', b=349,
 exp="La domination charismatique repose sur les qualités personnelles "
     "exceptionnelles attribuées à un individu : on lui obéit parce qu’on le "
     "considère comme exceptionnel. Le cours cite le chef religieux "
     "charismatique et certains dirigeants politiques.",
 why=["La coutume définit la domination traditionnelle.",
      "Le règlement intérieur relève de la domination légale-rationnelle.",
      "L’ancienneté renvoie plutôt à la tradition ou au statut, non au "
      "charisme."]),

# =============================================================== c10-04
'ch10-qcm-11': f(niv='comprendre', sp='c10-04', b=409,
 exp="La neutralité axiologique exige que le sociologue distingue l’analyse "
     "scientifique de ses propres jugements de valeur : il ne doit pas "
     "transformer son analyse en jugement moral ni présenter ses préférences "
     "personnelles comme des vérités scientifiques. S’il exprime un jugement "
     "personnel, il doit l’expliciter comme tel.",
 why=["Elle n’interdit pas l’analyse : elle en précise les conditions.",
      "Défendre ses opinions comme des résultats scientifiques est exactement "
      "ce qu’elle proscrit.",
      "Elle ne dit rien contre l’enquête : Weber est lui-même un auteur "
      "d’enquêtes comparatives."]),
'ch10-qcm-15': f(niv='connaitre', sp='c10-04', b=511,
 exp="Pour Weber, la bureaucratie est l’idéal-type de l’organisation "
     "rationnelle moderne : une organisation rationnelle de la coopération "
     "entre un grand nombre d’individus dont chacun exerce une fonction "
     "déterminée. La division du travail, la hiérarchie, les qualifications et "
     "les règles impersonnelles permettent d’accroître l’efficacité et de "
     "limiter l’arbitraire.",
 why=["Le désordre organisationnel est le sens péjoratif courant du mot, non "
      "le sens wébérien.",
      "La petite entreprise n’est pas l’objet de ce concept, qui vise les "
      "grandes organisations.",
      "Le syndicalisme est une organisation collective de travailleurs, "
      "analysée ailleurs dans le chapitre."],
 diss="Attention au sens du mot : aujourd’hui « bureaucratie » a une "
      "connotation négative, alors que Weber en fait le modèle de la "
      "rationalité organisationnelle."),
'ch10-qcm-16': f(niv='comprendre', sp='c10-04', b=534,
 exp="La « cage d’acier » désigne l’enfermement des individus dans les "
     "règles, les routines et les procédures. La rationalisation devait "
     "permettre de maîtriser le monde et d’organiser efficacement les "
     "activités ; paradoxalement, son développement peut réduire la liberté et "
     "l’autonomie individuelles. Plus une organisation devient rationnelle, "
     "plus elle est efficace, mais plus elle risque d’enfermer.",
 why=["Il s’agit d’une image, non d’une prison réelle.",
      "La cage d’acier n’est pas un outil de production mais une métaphore de "
      "la contrainte bureaucratique.",
      "Ce n’est pas un type de contrat : aucune dimension juridique n’est en "
      "jeu."],
 diss="Formule à citer dans toute dissertation sur les limites de la "
      "rationalisation ; elle annonce Crozier et Morel."),
'ch10-vf-3': f(niv='comprendre', sp='c10-04', b=552,
 exp="La bureaucratie est ambivalente chez Weber, non négative. Elle accroît "
     "l’efficacité et réduit l’arbitraire grâce à la division du travail, aux "
     "qualifications, à la hiérarchie et aux règles impersonnelles. Mais une "
     "rationalisation excessive peut multiplier les procédures, faire perdre "
     "leur autonomie aux individus, voire former un groupe bureaucratique "
     "défendant ses propres intérêts, et enfermer dans une « cage d’acier ».",
 diss="Erreur classique à éviter : prêter à Weber la critique de la "
      "bureaucratie qui est celle de Crozier."),
'ch10-vf-5': f(niv='comprendre', sp='c10-04', b=417,
 exp="La neutralité axiologique ne demande pas au sociologue de n’avoir "
     "aucune valeur personnelle : elle lui demande de ne pas transformer son "
     "analyse scientifique en jugement moral. S’il exprime une préférence "
     "personnelle, il doit l’expliciter et distinguer clairement le jugement "
     "scientifique du jugement de valeur.",
 diss="Point de méthode très utile : l’objectivité sociologique ne consiste "
      "pas à ne rien penser, mais à dire d’où l’on parle."),
'ch10-open-3': f(niv='connaitre', sp='c10-04', b=381,
 exp="L’idéal-type est une construction intellectuelle abstraite qui accentue "
     "volontairement certains traits d’un phénomène afin d’en faire un "
     "instrument de comparaison. Le sociologue sélectionne certains traits, "
     "les organise de façon cohérente et les accentue pour faire apparaître "
     "clairement la logique du phénomène. L’idéal-type ne correspond donc pas "
     "nécessairement à une situation existant parfaitement dans la réalité, et "
     "le mot « idéal » ne signifie pas « souhaitable ». Sa fonction est de "
     "permettre de comparer et d’interpréter le réel, en mesurant l’écart "
     "entre le modèle pur et les situations concrètes : les trois types de "
     "domination et la bureaucratie sont des idéaux-types, et l’homo "
     "œconomicus en est un autre exemple."),
'ch10-open-4': f(niv='raisonner', sp='c10-04', b=524,
 exp="La bureaucratie accroît l’efficacité et réduit l’arbitraire : la "
     "division du travail attribue à chacun une fonction clairement définie, "
     "le recrutement repose sur les diplômes et les compétences et non sur la "
     "naissance, la hiérarchie est formalisée par un organigramme, les "
     "décisions reposent sur des règles impersonnelles plutôt que sur les "
     "préférences du supérieur, le statut est attaché au poste et protège le "
     "salarié, et la personne n’est pas propriétaire de sa fonction. Mais "
     "Weber en voit aussi les dangers : une rationalisation excessive "
     "multiplie les procédures, fait perdre leur autonomie aux individus et "
     "peut faire émerger un groupe bureaucratique défendant ses propres "
     "intérêts. C’est l’image de la « cage d’acier » : la rationalisation "
     "censée permettre de mieux maîtriser le monde finit par enfermer ceux qui "
     "y vivent. Le paradoxe est que plus une organisation devient rationnelle, "
     "plus elle est efficace et plus elle risque de réduire la liberté "
     "individuelle.",
 diss="Cette ambivalence est le fil conducteur du chapitre : Morel et Crozier "
      "montreront que les mêmes mécanismes produisent des effets pervers."),

# =============================================================== c10-05
'ch10-qcm-17': f(niv='connaitre', sp='c10-05', b=595,
 exp="Les expériences ont été menées à la Western Electric Company, qui "
     "possède dans les années 1920 des usines de matériel téléphonique dans "
     "la banlieue de Chicago, où travaillent environ 29 000 personnes. Les "
     "conditions y sont plutôt avantageuses pour l’époque — salaires "
     "supérieurs à la moyenne, bonnes conditions matérielles — et pourtant "
     "l’entreprise connaît des difficultés sociales.",
 why=["Ford est associé au fordisme et à la chaîne de montage, dans un autre "
      "chapitre.",
      "Toyota renvoie au toyotisme, également traité ailleurs.",
      "La SEITA est l’entreprise du « monopole industriel » étudiée par "
      "Crozier."]),
'ch10-qcm-18': f(niv='connaitre', sp='c10-05', b=765,
 exp="L’effet Hawthorne, aussi appelé effet d’observation, désigne la "
     "modification du comportement d’un individu provoquée par le simple fait "
     "qu’il se sait observé. Les ouvrières de la Test Room savaient qu’elles "
     "participaient à une expérience et bénéficiaient de l’attention des "
     "chercheurs : leur productivité a pu augmenter pour cette seule raison.",
 why=["Aucune hausse de salaire n’est en cause : la rémunération n’est qu’une "
      "des variables modifiées.",
      "Une panne de machine renvoie à l’enquête de Crozier à la SEITA.",
      "Un biais de sélection concerne la composition de l’échantillon : c’est "
      "une autre critique adressée à Mayo."],
 diss="Effet à double tranchant : il est une découverte sur le facteur humain "
      "et une objection méthodologique aux conclusions de Mayo."),
'ch10-qcm-19': f(niv='comprendre', sp='c10-05', b=647,
 exp="En observant les ouvrières de la Test Room, Mayo constate l’importance "
     "des relations sociales : elles forment un véritable groupe, développent "
     "de bonnes relations entre elles, se sentent observées et écoutées, et "
     "entretiennent avec les chercheurs une relation différente de celle "
     "qu’elles avaient avec les contremaîtres. Le regard bienveillant de "
     "l’encadrement joue donc un rôle important.",
 why=["Les primes financières relèvent de l’explication taylorienne que Mayo "
      "conteste.",
      "La discipline stricte est à l’opposé : le remplacement des "
      "contremaîtres par des chercheurs a plutôt desserré le contrôle.",
      "La mécanisation est une condition technique, précisément insuffisante "
      "à expliquer les résultats."]),
'ch10-qcm-20': f(niv='connaitre', sp='c10-05', b=723,
 exp="L’École des relations humaines, née des travaux de Mayo, considère "
     "l’entreprise comme un système social : elle n’est pas seulement une "
     "organisation technique mais aussi une collectivité humaine, dans "
     "laquelle les salariés développent des relations privilégiées et forment "
     "des groupes. La performance suppose donc de concilier facteurs "
     "techniques et facteurs humains.",
 why=["La machine est l’image mécaniste du travail que Mayo critique chez "
      "Taylor.",
      "L’entreprise comme marché est la thèse de l’approche contractuelle de "
      "la firme, en économie.",
      "La bureaucratie parfaite est l’idéal-type wébérien, que ce courant ne "
      "reprend pas."]),
'ch10-qcm-21': f(niv='connaitre', sp='c10-05', b=693,
 exp="Mayo s’oppose principalement à Taylor. Dans la conception taylorienne, "
     "la productivité repose sur l’organisation scientifique du travail, les "
     "incitations économiques et l’amélioration des conditions techniques, et "
     "le travailleur est vu comme un individu réagissant aux incitations "
     "matérielles. Mayo montre que les comportements sont plus complexes : les "
     "individus appartiennent à des groupes dotés de normes informelles de "
     "production.",
 why=["Weber n’est pas la cible de Mayo : il s’intéresse à la rationalité des "
      "organisations, non à la motivation des ouvriers.",
      "Durkheim intervient dans ce chapitre sur l’intégration par le travail.",
      "Castel analyse la condition salariale et la désaffiliation, bien plus "
      "tard."],
 diss="Notion décisive à retenir : la norme informelle de production — le "
      "groupe rappelle à l’ordre celui qui travaille trop vite comme celui "
      "qui travaille trop lentement."),
'ch10-vf-7': f(niv='comprendre', sp='c10-05', b=590,
 exp="Mayo montre exactement l’inverse : la productivité ne dépend pas "
     "uniquement des conditions matérielles et économiques du travail. Les "
     "relations humaines, l’intégration au groupe, le sentiment d’être écouté "
     "et le sens donné au travail jouent également un rôle essentiel. "
     "L’expérience sur l’éclairage le prouve : la productivité augmente même "
     "lorsque l’éclairage est diminué, et même dans le groupe de contrôle."),
'ch10-open-5': f(niv='comprendre', sp='c10-05', b=756,
 exp="L’effet Hawthorne désigne la modification du comportement d’un "
     "individu provoquée par le simple fait qu’il se sait observé. Les "
     "ouvrières de la Test Room savaient qu’elles participaient à une "
     "expérience, bénéficiaient de l’attention des chercheurs, d’un "
     "encadrement particulier et du sentiment d’être considérées. Sa portée "
     "est double. C’est d’abord une découverte majeure sur le rôle du facteur "
     "humain : l’attention portée aux salariés influence leur travail. Mais "
     "c’est aussi une objection méthodologique aux conclusions de Mayo, "
     "puisque la hausse de productivité observée peut tenir au dispositif "
     "expérimental lui-même et non aux conditions de travail testées. "
     "L’interprétation initiale de l’expérience s’en trouve donc fragilisée."),
'ch10-open-6': f(niv='raisonner', sp='c10-05', b=775,
 exp="Quatre critiques sont formulées par le cours. L’effet Hawthorne "
     "d’abord : l’observation elle-même peut avoir modifié le comportement "
     "des ouvrières, de sorte que les résultats ne proviennent pas "
     "nécessairement des changements de conditions de travail. La faiblesse "
     "des échantillons ensuite : l’expérience de la Test Room ne porte que sur "
     "un petit groupe d’ouvrières, ce qui interdit de généraliser "
     "automatiquement. Le caractère très particulier de la situation "
     "également : des ouvrières volontaires, placées dans un dispositif "
     "expérimental spécifique, ne sont pas représentatives de tous les "
     "salariés. Enfin, l’environnement social est insuffisamment pris en "
     "compte : on reproche à Mayo de négliger le contexte extérieur à "
     "l’atelier, et les syndicats ont critiqué certaines interprétations de "
     "l’enquête."),

# =============================================================== c10-06
'ch10-qcm-22': f(niv='connaitre', sp='c10-06', b=831,
 exp="Le marché cognitif désigne l’espace, pensé comme un lieu fictif, où se "
     "rencontrent une offre et une demande d’informations. Comme sur un marché "
     "classique, certains contenus attirent davantage l’attention que "
     "d’autres. Sa particularité est d’être dérégulé : vraies informations, "
     "fausses informations et croyances y circulent simultanément.",
 why=["Le marché du travail qualifié est un marché au sens strict, étranger à "
      "ce concept.",
      "Le marché boursier échange des titres, non des informations.",
      "Le marché de la formation concerne l’offre de diplômes, pas la "
      "circulation des croyances."]),
'ch10-qcm-23': f(niv='connaitre', sp='c10-06', b=908,
 exp="L’avarice cognitive désigne la tendance des individus à économiser "
     "leurs efforts intellectuels : ils n’aiment pas consacrer beaucoup "
     "d’énergie à comprendre des problèmes complexes et privilégient donc des "
     "raisonnements rapides et intuitifs. Cela augmente leur vulnérabilité aux "
     "biais cognitifs.",
 why=["Ce n’est pas un refus d’apprendre mais une économie d’effort, souvent "
      "inconsciente.",
      "Il ne s’agit pas d’épargne au sens économique : le terme est une "
      "métaphore.",
      "Ce n’est pas un biais de mémoire : la mémoire intervient plutôt dans "
      "l’effet de réitération."],
 diss="À relier à Kahneman, cité plus loin dans le chapitre : les individus "
      "mobilisent souvent des raisonnements rapides et intuitifs."),
'ch10-vf-8': f(niv='comprendre', sp='c10-06', b=828,
 exp="Pour Bronner, Internet ne produit pas automatiquement davantage de "
     "rationalité. L’accès massif à l’information ne garantit pas sa "
     "progression : dans un marché cognitif dérégulé, nos biais cognitifs et "
     "les logiques d’audience peuvent favoriser la diffusion de contenus "
     "trompeurs ou simplificateurs. C’est précisément ce qui distingue son "
     "analyse de l’attente que l’on pourrait former à partir du "
     "désenchantement du monde de Weber."),
'ch10-open-7': f(niv='connaitre', sp='c10-06', b=847,
 exp="Le marché cognitif est l’espace dans lequel se rencontrent une offre et "
     "une demande d’informations : un lieu fictif où circulent informations, "
     "croyances et opinions, et où certains contenus attirent davantage "
     "l’attention que d’autres. Sa caractéristique essentielle est sa "
     "dérégulation : les savoirs vérifiés comme les fausses informations y "
     "circulent simultanément. Pour Bronner, l’accès massif à l’information "
     "permis par Internet ne garantit donc pas la progression de la "
     "rationalité : les invariants mentaux — attirance pour le conflit, la "
     "peur et le spectaculaire, goût de la visibilité sociale, avarice "
     "cognitive, préférence pour les plaisirs à court terme — et les logiques "
     "d’audience des médias favorisent les contenus les plus attractifs "
     "plutôt que les plus fiables."),

# =============================================================== c10-07
'ch10-qcm-25': f(niv='comprendre', sp='c10-07', b=991,
 exp="L’insularité cognitive désigne la situation d’un individu évoluant dans "
     "un environnement informationnel où il rencontre surtout des opinions "
     "proches des siennes et des contenus confortant sa vision du monde. On "
     "parle alors de chambre d’écho : les mêmes idées circulent entre "
     "personnes partageant les mêmes opinions et paraissent de plus en plus "
     "évidentes.",
 why=["Les syndicats sont des organisations collectives, étudiées dans une "
      "autre partie du chapitre.",
      "Les bureaucraties sont des formes d’organisation, pas des "
      "environnements informationnels.",
      "Le groupe professionnel est la notion durkheimienne d’intégration par "
      "le travail."],
 diss="Le phénomène est renforcé par les algorithmes, qui proposent davantage "
      "de contenus similaires à ceux auxquels l’internaute a déjà réagi."),
'ch10-qcm-26': f(niv='connaitre', sp='c10-07', b=1006,
 exp="Le biais de confirmation correspond à la tendance à rechercher, "
     "retenir et privilégier les informations qui confirment ce que l’on pense "
     "déjà, et inversement à négliger les informations contradictoires. Il "
     "renforce l’insularité cognitive et les chambres d’écho.",
 why=["Chercher la contradiction est précisément la solution recommandée par "
      "Bronner contre ce biais.",
      "Le doute systématique n’est pas un biais mais une posture critique.",
      "Changer d’avis souvent est l’inverse du mécanisme décrit."],
 diss="Ce biais réapparaît chez Morel dans l’analyse de la dynamique de "
      "groupe : le lien entre les deux auteurs se fait là."),
'ch10-qcm-27': f(niv='connaitre', sp='c10-08', b=1204,
 exp="Christian Morel étudie les décisions absurdes : il cherche à comprendre "
     "pourquoi des organisations rationnelles produisent parfois des erreurs, "
     "pourquoi plusieurs individus compétents peuvent collectivement prendre "
     "une mauvaise décision, et comment éviter ces dysfonctionnements. Son "
     "analyse porte donc sur la dimension collective de la décision, à partir "
     "d’accidents de sous-marins nucléaires, d’erreurs en bloc opératoire ou "
     "de catastrophes industrielles.",
 why=["Les cycles économiques relèvent de l’analyse macroéconomique.",
      "La solidarité organique est un concept de Durkheim.",
      "Les zones monétaires appartiennent à l’économie internationale."]),
'ch10-qcm-29': f(niv='connaitre', sp='c10-08', b=1340,
 exp="L’expérience de Solomon Asch, en 1951, porte sur le conformisme au sein "
     "d’un groupe : un individu peut se ranger à l’avis du groupe même "
     "lorsque cet avis est manifestement faux. Lorsque plusieurs personnes "
     "donnent la même réponse, l’individu peut douter de son propre jugement "
     "et préférer suivre l’opinion majoritaire.",
 why=["La productivité est l’objet des expériences de Mayo à la Western "
      "Electric.",
      "La mémoire n’est pas en jeu : l’individu voit correctement, mais "
      "répond autrement.",
      "L’apprentissage n’est pas l’objet du paradigme d’Asch."],
 diss="Mécanisme central pour comprendre Challenger : des individus informés "
      "peuvent taire ce qu’ils savent sous la pression du groupe."),
'ch10-qcm-31': f(niv='comprendre', sp='c10-09', b=1434,
 exp="Les métarègles sont des règles sur la manière de décider : elles "
     "visent à prévenir les décisions absurdes. Les organisations ne doivent "
     "pas simplement multiplier les procédures ; elles doivent créer des règles "
     "permettant de faire remonter les objections, de confronter les points de "
     "vue et de tirer des leçons des erreurs.",
 why=["L’augmentation de la production n’est pas l’objectif : il s’agit de la "
      "qualité de la décision.",
      "Les métarègles ne portent pas sur les rémunérations.",
      "Morel ne propose pas de supprimer la hiérarchie mais d’en réduire "
      "temporairement le poids dans certaines décisions."]),
'ch10-vf-11': f(niv='comprendre', sp='c10-08', b=1287,
 exp="Pour Morel, les décisions absurdes ne sont généralement pas dues à une "
     "seule erreur individuelle ni à l’incompétence d’une personne : elles "
     "résultent de l’accumulation de biais cognitifs, de pressions "
     "collectives et de dysfonctionnements organisationnels. Trois grands "
     "facteurs se renforcent mutuellement : le poids de la hiérarchie, la "
     "dynamique de groupe et le fonctionnement bureaucratique.",
 diss="Formule à retenir : la décision absurde est une œuvre collective."),
'ch10-open-8': f(niv='comprendre', sp='c10-07', b=1016,
 exp="Plusieurs mécanismes se combinent. D’abord la persistance des premières "
     "informations : une information reçue en premier continue d’influencer "
     "l’individu même après un démenti, qui n’efface pas complètement la trace "
     "initiale. Ensuite la vitesse de circulation : selon les éléments retenus "
     "par Bronner, les fausses informations circulent environ six fois plus "
     "vite que les vraies, car leur caractère spectaculaire ou émotionnel "
     "correspond particulièrement bien aux mécanismes de captation de "
     "l’attention. Puis l’effet de réitération : plus une information est "
     "répétée, plus elle paraît crédible, la familiarité étant confondue avec "
     "la vérité. Enfin la loi de Brandolini, énoncée en 2013 : l’énergie "
     "nécessaire pour réfuter une fausse information est bien supérieure à "
     "celle nécessaire pour la produire, car il faut rassembler des sources, "
     "vérifier plusieurs éléments et développer un raisonnement complexe."),
'ch10-open-9': f(niv='comprendre', sp='c10-08', b=1280,
 exp="Une décision absurde est une décision collective qui va durablement à "
     "l’encontre du but recherché, prise par une organisation pourtant "
     "rationnelle, dotée de règles, d’experts et de procédures. Morel "
     "l’explique par trois familles de causes. Le poids de la hiérarchie "
     "produit la crainte de contester l’autorité, la crainte d’insister après "
     "une première objection non retenue, et l’autocensure liée au sentiment "
     "d’incompétence, la division du travail fragmentant les domaines de "
     "compétence. La dynamique de groupe ajoute le conformisme mis en évidence "
     "par Asch en 1951 et la pensée de groupe théorisée par Irving Janis en "
     "1982, avec l’illusion d’unanimité. Des mécanismes cognitifs enfin, comme "
     "le biais de confirmation. La décision absurde est donc une œuvre "
     "collective et non une faute individuelle : l’accident de Challenger le "
     "montre, puisque plusieurs personnes disposaient des informations "
     "permettant d’identifier le danger."),
'ch10-aut195-1': f(niv='connaitre', sp='c10-07', b=1048,
 exp="Énoncée en 2013, la loi de Brandolini souligne que l’énergie nécessaire "
     "pour réfuter une fausse information est bien supérieure à celle "
     "nécessaire pour la produire : une affirmation fausse peut être lancée en "
     "une phrase, alors que sa réfutation exige de rassembler des sources, de "
     "vérifier plusieurs éléments et de développer un raisonnement complexe. "
     "Cette asymétrie de coûts explique, avec l’effet de réitération, pourquoi "
     "l’abondance d’informations ne produit pas mécaniquement une société plus "
     "rationnelle — ce que Bronner nomme la « démocratie des crédules ».",
 why=["C’est l’effet de réitération, autre mécanisme du chapitre.",
      "C’est le biais de confirmation, également distinct.",
      "C’est précisément la thèse que Bronner réfute."]),

# =============================================================== c10-08 / 09
'ch10-qcm-30': f(niv='connaitre', sp='c10-08', b=1361,
 exp="Le « Groupthink », ou pensée de groupe, est théorisé par Irving Janis "
     "en 1982 : dans un groupe, les individus cherchent l’harmonie et évitent "
     "d’exprimer leurs désaccords ou de contester la position majoritaire. "
     "Comme personne n’exprime ses doutes, chacun croit que les autres sont "
     "tous d’accord : c’est l’illusion de l’unanimité.",
 why=["Asch est l’auteur de l’expérience sur le conformisme, en 1951.",
      "Mayo a mené les expériences de la Western Electric.",
      "Crozier développe l’analyse stratégique des organisations."]),
'ch10-vf-10': f(niv='comprendre', sp='c10-08', b=1350,
 exp="C’est le résultat du paradigme d’Asch : sous l’effet de la pression "
     "conformiste exercée par le groupe, un individu peut adopter une réponse "
     "qu’il sait pourtant erronée. Lorsque plusieurs personnes donnent toutes "
     "la même réponse, il peut douter de son propre jugement et préférer "
     "suivre l’opinion majoritaire plutôt que s’isoler.",
 diss="Résultat essentiel pour le chapitre : réunir plusieurs individus ne "
      "garantit pas une décision plus rationnelle."),
'ch10-qcm-28': f(niv='appliquer', sp='c10-08', b=1232,
 exp="En 1986, la navette Challenger explose peu après son décollage, alors "
     "que les vingt-quatre lancements précédents s’étaient bien déroulés. Le "
     "problème vient de joints flexibles situés sur les boosters, qui "
     "fonctionnent mal par températures exceptionnellement basses et laissent "
     "échapper des gaz brûlants. Mais ce qui intéresse Morel est la décision "
     "collective prise juste avant : certains ingénieurs de Thiokol jugeaient "
     "le lancement dangereux, sans qu’aucune objection soit suffisamment forte "
     "pour l’empêcher.",
 why=["Il s’agit au contraire de l’échec organisationnel le plus analysé du "
      "chapitre.",
      "Aucun conflit syndical n’est en cause dans cet accident.",
      "L’effet Hawthorne concerne les expériences de Mayo et le fait de se "
      "savoir observé."],
 diss="Détail organisationnel décisif à citer : les joints n’étaient plus "
      "considérés comme une pièce déterminante du lancement, ce qui a privé "
      "l’alerte de tout poids."),
'ch10-qcm-32': f(niv='comprendre', sp='c10-09', b=1442,
 q="En quoi consiste la « hiérarchie restreinte impliquée » proposée par "
   "Morel ?",
 opts=["À multiplier les échelons hiérarchiques pour mieux contrôler les "
       "décisions",
       "À réduire temporairement le poids de la hiérarchie en confiant "
       "davantage le pouvoir de décision aux personnes réellement compétentes "
       "et directement confrontées à la situation",
       "À supprimer définitivement toute hiérarchie dans l’organisation",
       "À externaliser les décisions difficiles auprès de consultants"],
 ans=1,
 exp="La hiérarchie restreinte impliquée consiste à donner davantage de poids "
     "décisionnel aux acteurs disposant de l’expertise et de l’expérience "
     "directe de la situation, même lorsqu’ils occupent une position "
     "hiérarchique inférieure. Dans une situation technique complexe, l’avis "
     "de l’ingénieur spécialiste doit pouvoir peser davantage que celui d’un "
     "supérieur qui maîtrise moins le problème. Il s’agit donc d’un transfert "
     "du pouvoir de décision, non d’une suppression de la hiérarchie.",
 why=["Multiplier les échelons aggraverait exactement le problème que Morel "
      "cherche à corriger.",
      "Morel ne supprime pas la hiérarchie : il en réduit temporairement le "
      "poids sur certaines décisions.",
      "L’externalisation éloignerait la décision de ceux qui connaissent la "
      "situation : c’est le contraire de l’implication."],
 diss="Cette métarègle est la réponse directe au cas Challenger : les "
      "ingénieurs savaient, mais leur avis ne pesait pas."),
'ch10-vf-12': f(niv='connaitre', sp='c10-09', b=1512,
 exp="Les check-lists font bien partie des métarègles de Morel. Elles "
     "permettent de sécuriser les procédures complexes en vérifiant "
     "systématiquement que toutes les opérations nécessaires ont été réalisées "
     "et qu’aucune étape n’a été oubliée, même lorsque les acteurs sont "
     "expérimentés. Utilisées depuis longtemps dans l’aéronautique, elles ont "
     "permis de réduire de 50 % la mortalité dans certains blocs opératoires.",
 diss="Argument puissant pour une dissertation : une amélioration "
      "organisationnelle très simple peut produire un gain considérable."),
'ch10-open-10': f(niv='comprendre', sp='c10-09', b=1434,
 exp="Morel propose cinq métarègles. La hiérarchie restreinte impliquée "
     "réduit temporairement le poids de la hiérarchie classique en confiant "
     "davantage le pouvoir de décision aux personnes réellement compétentes et "
     "directement confrontées à la situation, même sans position hiérarchique "
     "élevée. Le débat contradictoire organisé oblige le groupe à confronter "
     "sa décision à des objections, notamment en attribuant explicitement à "
     "quelqu’un le rôle d’avocat du diable, chargé de chercher les faiblesses "
     "de la décision même si tout le monde semble d’accord. La décision par "
     "consensus cherche ensuite une solution que le groupe peut accepter, "
     "plutôt que d’imposer mécaniquement la position de l’autorité. La "
     "non-punition systématique des erreurs permet le retour d’expérience : si "
     "les erreurs sont punies, les individus les cachent et l’organisation "
     "perd une information précieuse. Les check-lists, enfin, sécurisent les "
     "procédures complexes en évitant les oublis d’étapes.",
 diss="Logique d’ensemble : organiser la contradiction, l’apprentissage et la "
      "remontée de l’expertise plutôt que multiplier les procédures."),

# =============================================================== c10-10
'ch10-qcm-33': f(niv='connaitre', sp='c10-10', b=1650,
 exp="L’Acteur et le système, publié en 1977, est écrit par Michel Crozier "
     "avec Erhard Friedberg. Crozier est aussi l’auteur du Phénomène "
     "bureaucratique (1963) et le fondateur du Centre de sociologie des "
     "organisations ; sa méthode repose sur des enquêtes de terrain.",
 why=["Weber a participé en 1903, avec Werner Sombart, à la création d’une "
      "revue allemande de sciences sociales, mais pas à cet ouvrage.",
      "Mayo et Taylor sont opposés dans ce chapitre, ils n’ont rien écrit "
      "ensemble.",
      "Durkheim fonde en 1896 la revue L’Année sociologique ; cet appariement "
      "ne correspond à rien dans le cours."]),
'ch10-qcm-34': f(niv='comprendre', sp='c10-10', b=1675,
 exp="Le cercle vicieux bureaucratique décrit l’enchaînement suivant : les "
     "règles impersonnelles et la centralisation produisent de la rigidité et "
     "isolent les niveaux hiérarchiques ; la communication entre groupes "
     "devient plus difficile ; pour résoudre les problèmes nés de cette "
     "rigidité, l’organisation crée de nouvelles règles, qui la rendent à leur "
     "tour plus rigide encore.",
 why=["Les profits ne sont pas en jeu : il s’agit du fonctionnement interne de "
      "l’organisation.",
      "Les effectifs ne sont pas concernés par ce mécanisme.",
      "Le conflit ouvert n’est pas le résultat décrit : le cercle vicieux "
      "produit de la rigidité, non un affrontement déclaré."],
 diss="Réponse directe à Weber : les règles censées rationaliser peuvent "
      "produire l’effet inverse."),
'ch10-vf-13': f(niv='raisonner', sp='c10-10', b=1663,
 exp="Crozier ne nie pas que les règles cherchent à rationaliser "
     "l’organisation, mais il montre qu’elles peuvent produire l’effet "
     "inverse. Le cercle vicieux bureaucratique engendre de la rigidité, et à "
     "côté du monde formel décrit par l’organigramme existe un monde informel "
     "fait de relations réelles, d’affects et de rapports de pouvoir qui "
     "échappe aux règles. La bureaucratie n’est donc pas l’organisation "
     "parfaitement rationnelle de l’idéal-type wébérien.",
 diss="Articulation à soigner : Crozier ne réfute pas Weber, il confronte "
      "l’idéal-type à l’enquête de terrain."),
'ch10-open-11': f(niv='comprendre', sp='c10-10', b=1676,
 exp="Les grandes organisations mettent en place des règles impersonnelles et "
     "une forte centralisation des décisions. Ces règles produisent de la "
     "rigidité et isolent les différents niveaux hiérarchiques, ce qui rend la "
     "communication entre groupes plus difficile. Pour résoudre les problèmes "
     "provoqués par cette rigidité, l’organisation crée de nouvelles règles — "
     "qui la rendent à leur tour plus rigide : le cercle se referme. La "
     "bureaucratie n’est donc pas l’organisation parfaitement rationnelle "
     "décrite par Weber : elle sécrète ses propres blocages. Cette analyse "
     "conduit Crozier à distinguer le monde formel, celui de l’organigramme "
     "établi par la direction, et le monde informel, celui des relations "
     "réelles, des affects et des rapports de pouvoir, que le sociologue peut "
     "représenter par un sociogramme."),

# =============================================================== c10-11
'ch10-qcm-35': f(niv='comprendre', sp='c10-11', b=1863,
 exp="Une zone d’incertitude est une situation que les règles ne couvrent "
     "pas : règles imprécises ou incomplètes, situations imprévisibles. Toutes "
     "les organisations en possèdent, car aucune règle ne peut prévoir toutes "
     "les situations. Ce qui est un problème pour l’organisation devient une "
     "ressource pour l’acteur qui parvient à la maîtriser mieux que les "
     "autres : les autres deviennent dépendants de lui.",
 why=["Il ne s’agit pas d’un espace géographique mais d’un espace de "
      "pouvoir.",
      "Ce n’est pas un service de l’organisation : la zone d’incertitude "
      "traverse les services.",
      "Ce n’est pas un type de contrat ; au contraire, elle naît de ce que les "
      "règles ne prévoient pas."]),
'ch10-qcm-36': f(niv='appliquer', sp='c10-11', b=1776,
 exp="Les ouvrières de production dépendent du fonctionnement de leurs "
     "machines : en cas de panne, elles ne peuvent plus produire normalement "
     "et peuvent perdre une partie de leurs primes. Or seuls les ouvriers "
     "d’entretien savent réparer les machines. Leur savoir-faire leur donne "
     "une ressource rare et le contrôle d’une situation incertaine : les "
     "ouvrières ne savent ni quand ni comment la machine sera réparée.",
 why=["L’ancienneté n’est pas la source de pouvoir identifiée par "
      "l’enquête.",
      "Le diplôme n’intervient pas : c’est le savoir-faire pratique qui "
      "compte.",
      "Le syndicat n’est pas en cause dans ce mécanisme."],
 diss="Conséquence sociale observée par Crozier : les ouvrières hésitent à "
      "critiquer les ouvriers d’entretien, de peur qu’ils réparent avec moins "
      "de bonne volonté."),
'ch10-qcm-37': f(niv='comprendre', sp='c10-11', b=1810,
 exp="Pour Crozier, le pouvoir est la capacité d’un acteur à influencer "
     "d’autres acteurs en utilisant à son avantage les ressources dont il "
     "dispose et qui lui permettent de maîtriser des zones d’incertitude. Le "
     "pouvoir n’est donc pas un attribut attaché à un titre : il existe dans "
     "une relation. Il est de ce fait diffus, et un acteur subalterne peut en "
     "disposer s’il contrôle une ressource essentielle pour les autres.",
 why=["La concentration au sommet est la conception classique que Crozier "
      "réfute avec l’enquête de la SEITA.",
      "Le pouvoir n’est pas purement juridique : l’organigramme ne dit pas "
      "qui influence réellement qui.",
      "Le pouvoir est au contraire omniprésent dans l’organisation."],
 diss="Comparaison du cours : alors que Marx situe le pouvoir dans la "
      "propriété du capital, donc au sommet, Crozier le montre distribué "
      "entre tous les acteurs qui contrôlent des ressources stratégiques."),
'ch10-open-12': f(niv='comprendre', sp='c10-11', b=1864,
 exp="Une zone d’incertitude est une situation que les règles de "
     "l’organisation ne parviennent pas à couvrir : règles imprécises ou "
     "incomplètes, événements imprévisibles. Toutes les organisations en "
     "possèdent, puisque aucune règle ne peut tout prévoir. Pour "
     "l’organisation, c’est une contrainte : les comportements deviennent "
     "moins prévisibles et le fonctionnement moins contrôlable, d’où la "
     "tendance à vouloir réduire ces zones. Mais pour un acteur, c’est une "
     "ressource : s’il la maîtrise mieux que les autres, il rend son propre "
     "comportement moins prévisible tout en influençant celui de ses "
     "partenaires, qui deviennent dépendants de lui. À la SEITA, les ouvriers "
     "d’entretien tirent ainsi leur pouvoir de la réparation des machines, "
     "compétence indispensable et difficilement contrôlable dont dépend la "
     "productivité des ouvrières — alors qu’ils ne sont pas leurs supérieurs "
     "hiérarchiques."),

# =============================================================== c10-13
'ch10-qcm-38': f(niv='connaitre', sp='c10-13', b=2200,
 exp="L’anomie désigne chez Durkheim une situation dans laquelle les normes "
     "collectives sont affaiblies, floues ou absentes : l’individu ne sait "
     "plus clairement quelles règles suivre ni ce qu’il peut légitimement "
     "attendre. Les désirs devenant illimités, Durkheim parle d’une « passion "
     "de l’infini » : on veut toujours davantage sans disposer de normes "
     "indiquant jusqu’où aller.",
 why=["Un excès de normes serait l’inverse : l’anomie est un défaut de "
      "régulation.",
      "L’anomie n’est pas une forme de solidarité, mais un dysfonctionnement "
      "de la régulation sociale.",
      "Ce n’est pas un type d’organisation : le concept porte sur les normes, "
      "non sur les structures."],
 diss="Couple à ne jamais séparer : l’anomie est un défaut de régulation, "
      "l’égoïsme un défaut d’intégration."),
'ch10-vf-17': f(niv='comprendre', sp='c10-13', b=2296,
 exp="Le groupe professionnel remplit bien les deux fonctions. Contre "
     "l’égoïsme, défaut d’intégration : le travailleur appartient à un "
     "collectif, entretient des relations régulières et n’est donc pas isolé. "
     "Contre l’anomie, défaut de régulation : le groupe professionnel partage "
     "des règles communes et une morale professionnelle qui encadrent les "
     "comportements. C’est la solution avancée par Durkheim face à la "
     "fragilisation de la famille, de la religion et des communautés locales.",
 diss="Argument central de Durkheim sur le travail : le groupe professionnel "
      "peut devenir le nouveau support de la cohésion sociale moderne."),

# =============================================================== c10-14
'ch10-qcm-39': f(niv='connaitre', sp='c10-14', b=2343,
 exp="La solidarité mécanique est caractéristique des sociétés "
     "traditionnelles ou simples : elle repose sur la ressemblance entre des "
     "individus exerçant des activités proches et partageant largement les "
     "mêmes croyances et valeurs. Durkheim file l’analogie des pièces d’une "
     "machine, interchangeables. La conscience collective y est très forte, ce "
     "qui laisse peu d’autonomie à la conscience individuelle.",
 why=["La complémentarité fonde la solidarité organique.",
      "La hiérarchie n’est pas le principe de cette solidarité.",
      "Le contrat suppose au contraire des individus différenciés et "
      "spécialisés."]),
'ch10-qcm-40': f(niv='connaitre', sp='c10-14', b=2381,
 exp="La solidarité organique caractérise les sociétés modernes, "
     "différenciées et industrielles, marquées par une forte division du "
     "travail : elle repose sur la complémentarité d’individus spécialisés. "
     "Durkheim file ici l’analogie des organes du corps humain, dont chacun "
     "exerce une fonction particulière mais a besoin des autres pour "
     "fonctionner.",
 why=["La ressemblance fonde la solidarité mécanique.",
      "La tradition caractérise les sociétés à solidarité mécanique.",
      "La contrainte n’est pas le ressort de cette solidarité, mais "
      "l’interdépendance."],
 diss="Mécanisme à retenir : division du travail → spécialisation → "
      "différenciation → complémentarité → interdépendance."),
'ch10-vf-16': f(niv='comprendre', sp='c10-14', b=2329,
 exp="Pour Durkheim, la solidarité ne disparaît pas avec la modernité : elle "
     "change de forme. La division du travail fait passer d’une solidarité "
     "mécanique, fondée sur la ressemblance, à une solidarité organique, "
     "fondée sur la différence et la complémentarité. Les deux formes se sont "
     "historiquement succédé mais peuvent coexister dans une même société.",
 diss="Réponse de Durkheim au pessimisme sur la modernité : plus les "
      "individus se différencient, plus ils dépendent les uns des autres."),
'ch10-open-13': f(niv='comprendre', sp='c10-14', b=2342,
 exp="La solidarité mécanique caractérise les sociétés traditionnelles ou "
     "simples : elle repose sur la ressemblance entre individus partageant "
     "largement les mêmes activités, valeurs et croyances, à la manière des "
     "pièces interchangeables d’une machine. La conscience collective — "
     "l’ensemble des croyances et des sentiments communs à la moyenne des "
     "membres d’une même société — y est très forte, et l’individu dispose de "
     "peu d’autonomie. La solidarité organique caractérise les sociétés "
     "modernes, différenciées et industrielles : la forte division du travail "
     "rend les individus spécialisés, donc différents, mais complémentaires et "
     "interdépendants, comme les organes d’un corps. La conscience "
     "individuelle y devient plus autonome, sans que la conscience collective "
     "disparaisse : l’individu est à la fois plus libre et plus dépendant des "
     "autres. Les deux solidarités se sont historiquement succédé mais peuvent "
     "coexister."),
'ch10-open-14': f(niv='raisonner', sp='c10-14', b=2450,
 exp="Le travail est intégrateur pour cinq raisons chez Durkheim. Il crée des "
     "relations, en mettant l’individu en contact avec d’autres personnes. Il "
     "rattache à un groupe, le collectif professionnel. Il produit de la "
     "complémentarité, puisque la division du travail rend les individus "
     "spécialisés mais complémentaires. Il produit de l’interdépendance : plus "
     "les individus sont spécialisés, moins ils peuvent satisfaire seuls leurs "
     "besoins. Il peut enfin fournir des normes, le groupe professionnel "
     "transmettant une morale et des règles communes. Le travail assure donc "
     "simultanément les deux fonctions que la société doit remplir : "
     "l’intégration, dont le défaut produit l’égoïsme, et la régulation, dont "
     "le défaut produit l’anomie."),
'ch10-open-15': f(niv='raisonner', sp='c10-15', b=2510,
 exp="Le travail continue d’intégrer : il procure un revenu, un statut, des "
     "relations sociales, une appartenance collective et une identité, et il "
     "relie les individus par des mécanismes de solidarité comme la retraite "
     "par répartition, où les actifs financent les pensions des retraités. "
     "Mais son pouvoir intégrateur est devenu moins automatique. Le chômage de "
     "masse, la précarisation, la flexibilité, la multiplication des formes "
     "d’emploi instables et la pauvreté laborieuse font que l’emploi ne "
     "garantit plus durablement revenu, statut et relations. Pour Castel, la "
     "perte d’emploi peut enclencher un processus de désaffiliation : "
     "l’individu perd simultanément des protections, des relations sociales et "
     "une partie de son identité. L’intégration par le travail demeure donc "
     "puissante, mais fragilisée.",
 diss="Formulation équilibrée attendue : le travail reste intégrateur, mais "
      "cette intégration n’est plus garantie par le simple fait d’avoir un "
      "emploi."),

# =============================================================== c10-16
'ch10-qcm-41': f(niv='connaitre', sp='c10-16', b=2709,
 exp="La désaffiliation désigne chez Robert Castel un processus dans lequel "
     "l’individu perd progressivement ses protections, ses relations sociales "
     "et une partie de son identité sociale. Le chômage de masse des années "
     "1970-1980 ne produit donc pas seulement une perte de revenu mais une "
     "perte de liens : perdre un métier peut signifier perdre une partie de "
     "son inscription dans la société.",
 why=["Une démission volontaire est un acte individuel, pas un processus de "
      "rupture sociale.",
      "Changer de syndicat n’a aucun rapport avec ce concept.",
      "Une reconversion est un changement de métier, non une perte "
      "d’inscription sociale."],
 diss="À citer avec Les Métamorphoses de la question sociale (1995) : la "
      "question sociale ne disparaît pas, elle se transforme."),
'ch10-vf-18': f(niv='comprendre', sp='c10-16', b=2683,
 exp="Pour Castel, la société salariale a transformé l’emploi en support "
     "d’intégration : au cours du XXe siècle, le salariat ne donne plus "
     "seulement un salaire mais un statut, des droits sociaux et une "
     "appartenance à la collectivité. C’est précisément ce qui rend la montée "
     "du chômage et de la précarité si déstabilisante : elle fragilise "
     "beaucoup plus qu’un revenu.",
 diss="Enchaînement à retenir : société salariale → effritement de la "
      "condition salariale → désaffiliation."),

# =============================================================== c10-17
'ch10-qcm-42': f(niv='connaitre', sp='c10-17', b=2990,
 exp="Le halo du chômage regroupe des personnes situées à la frontière entre "
     "emploi, chômage et inactivité : elles souhaitent travailler mais ne "
     "remplissent pas l’ensemble des critères officiels du chômage — elles ne "
     "recherchent pas activement dans l’immédiat, ne sont pas disponibles dans "
     "les délais requis, ou disposent seulement d’une activité très réduite.",
 why=["Les chômeurs de longue durée sont des chômeurs au sens strict, donc "
      "hors du halo.",
      "Les retraités sont des inactifs qui ne souhaitent pas, en principe, "
      "travailler.",
      "Les étudiants sans emploi et sans recherche active sont classés "
      "inactifs."],
 diss="Notion clé pour montrer que le chômage est aussi une construction "
      "statistique : 2,6 millions au sens du BIT, 3,2 millions en catégorie A "
      "de France Travail, plus de 7 millions avec les catégories larges."),
'ch10-vf-19': f(niv='connaitre', sp='c10-17', b=2934,
 exp="La définition du chômage du BIT, utilisée pour les comparaisons "
     "internationales, suppose au contraire trois critères cumulatifs : ne pas "
     "avoir travaillé, même une heure, pendant la semaine de référence ; "
     "rechercher activement un emploi ; être disponible pour travailler "
     "rapidement. C’est cette exigence de recherche active qui distingue le "
     "chômeur de l’inactif.",
 diss="Rappel utile : un chômeur appartient à la population active, alors "
      "qu’une personne sans emploi n’est pas automatiquement chômeuse."),

# =============================================================== c10-18
'ch10-vf-20': f(niv='comprendre', sp='c10-18', b=3106,
 exp="Le taux de syndicalisation est passé d’environ 30 % en 1949 à environ "
     "20 % en 1969, 16,6 % en 1980 et 10,3 % en 2019. Le cours attribue ce "
     "recul à trois causes : la désindustrialisation, qui réduit la base "
     "ouvrière historique du syndicalisme ; la montée de l’individualisme, "
     "rapprochée du paradoxe de l’action collective de Mancur Olson ; et la "
     "mondialisation, qui disperse les lieux de production.",
 diss="Nuance essentielle : la baisse de l’adhésion syndicale ne signifie pas "
      "la disparition des conflits, qui se sont en partie "
      "institutionnalisés."),

}


# Les quinze questions ouvertes héritées n'avaient aucune grille de
# correction : le corrigé rédigé sert de réponse modèle et l'on explicite les
# éléments que la réponse doit contenir.
CLES = {
 'ch10-open-1': [
   {'f': ['structure', 'holisme', 'chose', 'macro'],
    'l': 'Durkheim : expliquer par les structures sociales'},
   {'f': ['sens', 'comprehensive', 'individualisme', 'subjectif'],
    'l': 'Weber : comprendre le sens donné par les individus'},
   {'f': ['determinisme', 'sociologisme'],
    'l': 'la limite du holisme : le déterminisme'},
   {'f': ['relativisme', 'regularite'],
    'l': 'la limite de l’approche compréhensive : le relativisme'}],
 'ch10-open-2': [
   {'f': ['finalite', 'moyen', 'but'], 'l': 'l’action rationnelle en finalité'},
   {'f': ['valeur', 'conviction', 'devoir'], 'l': 'l’action rationnelle en valeur'},
   {'f': ['traditionnel', 'habitude', 'coutume'], 'l': 'le comportement traditionnel'},
   {'f': ['affectuel', 'emotion', 'sentiment'], 'l': 'le comportement affectuel'}],
 'ch10-open-3': [
   {'f': ['construction', 'abstrait', 'accentue'],
    'l': 'une construction qui accentue certains traits'},
   {'f': ['pas une description', 'ne correspond pas', 'pas la realite', 'pur'],
    'l': 'ce n’est pas une description fidèle du réel'},
   {'f': ['comparer', 'comparaison', 'interpreter', 'ecart'],
    'l': 'sa fonction : comparer et interpréter la réalité'}],
 'ch10-open-4': [
   {'f': ['efficacite', 'arbitraire', 'regle impersonnelle', 'qualification'],
    'l': 'elle accroît l’efficacité et réduit l’arbitraire'},
   {'f': ['procedure', 'autonomie', 'routine'],
    'l': 'mais elle multiplie les procédures et réduit l’autonomie'},
   {'f': ['cage d acier', 'cage'], 'l': 'l’image de la « cage d’acier »'}],
 'ch10-open-5': [
   {'f': ['observe', 'observation', 'sait observ'],
    'l': 'la modification du comportement par le fait de se savoir observé'},
   {'f': ['facteur humain', 'attention', 'consider'],
    'l': 'une découverte sur le rôle du facteur humain'},
   {'f': ['fragilise', 'critique', 'interpretation', 'dispositif'],
    'l': 'une objection à l’interprétation initiale de Mayo'}],
 'ch10-open-6': [
   {'f': ['hawthorne', 'observation'], 'l': 'l’effet Hawthorne lui-même'},
   {'f': ['echantillon', 'petit groupe', 'generalis'],
    'l': 'la faiblesse des échantillons'},
   {'f': ['volontaire', 'particulier', 'representatif', 'experimental'],
    'l': 'le caractère très particulier de la situation'},
   {'f': ['environnement social', 'syndicat', 'exterieur'],
    'l': 'la prise en compte insuffisante de l’environnement social'}],
 'ch10-open-7': [
   {'f': ['offre', 'demande', 'information'],
    'l': 'la rencontre d’une offre et d’une demande d’informations'},
   {'f': ['deregule', 'fausse', 'croyance'],
    'l': 'un marché dérégulé où circulent aussi les fausses informations'},
   {'f': ['invariant', 'biais', 'audience', 'attention'],
    'l': 'les invariants mentaux et les logiques d’audience'}],
 'ch10-open-8': [
   {'f': ['premiere information', 'persist', 'dementi'],
    'l': 'la persistance des premières informations'},
   {'f': ['six fois', 'vite', 'viralite', 'spectaculaire'],
    'l': 'la circulation plus rapide des fausses informations'},
   {'f': ['reiteration', 'repet'], 'l': 'l’effet de réitération'},
   {'f': ['brandolini', 'refuter', 'energie'], 'l': 'la loi de Brandolini'}],
 'ch10-open-9': [
   {'f': ['hierarchie', 'contester', 'autocensure', 'insister'],
    'l': 'le poids de la hiérarchie'},
   {'f': ['asch', 'conformisme', 'janis', 'groupthink', 'unanimite'],
    'l': 'la dynamique de groupe : conformisme et pensée de groupe'},
   {'f': ['biais de confirmation', 'cognitif'],
    'l': 'les mécanismes cognitifs'},
   {'f': ['collective', 'oeuvre collective', 'pas individuelle'],
    'l': 'une œuvre collective, non une faute individuelle'}],
 'ch10-open-10': [
   {'f': ['hierarchie restreinte', 'competent', 'implique'],
    'l': 'la hiérarchie restreinte impliquée'},
   {'f': ['contradictoire', 'avocat du diable', 'objection'],
    'l': 'le débat contradictoire et l’avocat du diable'},
   {'f': ['consensus'], 'l': 'la décision par consensus'},
   {'f': ['punir', 'erreur', 'retour d experience'],
    'l': 'ne pas punir systématiquement les erreurs'},
   {'f': ['check list', 'checklist', 'liste'], 'l': 'les check-lists'}],
 'ch10-open-11': [
   {'f': ['regle impersonnelle', 'centralisation', 'rigidite'],
    'l': 'les règles produisent de la rigidité'},
   {'f': ['nouvelle regle', 'encore plus', 'cercle'],
    'l': 'l’organisation y répond par de nouvelles règles'},
   {'f': ['pas parfaitement rationnelle', 'weber', 'blocage', 'informel'],
    'l': 'la bureaucratie n’est donc pas parfaitement rationnelle'}],
 'ch10-open-12': [
   {'f': ['regle', 'imprecise', 'incomplete', 'pas prevu', 'controle'],
    'l': 'une situation que les règles ne couvrent pas'},
   {'f': ['dependant', 'depend', 'pouvoir', 'ressource'],
    'l': 'celui qui la maîtrise rend les autres dépendants'},
   {'f': ['seita', 'entretien', 'machine', 'reparation'],
    'l': 'l’exemple des ouvriers d’entretien de la SEITA'}],
 'ch10-open-13': [
   {'f': ['ressemblance', 'mecanique', 'meme', 'traditionnelle'],
    'l': 'la solidarité mécanique repose sur la ressemblance'},
   {'f': ['conscience collective'],
    'l': 'la conscience collective y est très forte'},
   {'f': ['organique', 'complementarite', 'specialis', 'interdependan'],
    'l': 'la solidarité organique repose sur la complémentarité'},
   {'f': ['conscience individuelle', 'autonomie', 'autonome'],
    'l': 'la conscience individuelle y devient plus autonome'}],
 'ch10-open-14': [
   {'f': ['relation', 'contact'], 'l': 'il crée des relations'},
   {'f': ['groupe professionnel', 'collectif'], 'l': 'il rattache à un groupe'},
   {'f': ['complementarite', 'interdependance', 'division du travail'],
    'l': 'il produit complémentarité et interdépendance'},
   {'f': ['norme', 'regle', 'morale'], 'l': 'il peut fournir des normes'},
   {'f': ['egoisme', 'anomie'],
    'l': 'il lutte contre l’égoïsme et contre l’anomie'}],
 'ch10-open-15': [
   {'f': ['revenu', 'statut', 'identite', 'relation'],
    'l': 'le travail procure revenu, statut, relations et identité'},
   {'f': ['precarit', 'flexibilite', 'chomage', 'pauvrete laborieuse'],
    'l': 'mais précarité, flexibilité et chômage le fragilisent'},
   {'f': ['desaffiliation', 'castel'],
    'l': 'le processus de désaffiliation décrit par Castel'}],
}

for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'modele': FIX[_id]['exp'], 'cles': _c}


from qz10n1 import L as _N1
from qz10n2 import L as _N2
from qz10n3 import L as _N3
from qz10n4 import L as _N4

NEW = _N1 + _N2 + _N3 + _N4
