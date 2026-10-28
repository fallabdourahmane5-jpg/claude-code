# -*- coding: utf-8 -*-
"""Visualisation 16 — Organiser le travail, exercer le pouvoir (hub)."""

from vz_base import v, nd, ln

v('vz-organisations', 'Organiser le travail, exercer le pouvoir',
  'Chapitre 10 · noyau et branches',
  'hub',
  "Une organisation n’est jamais ce que son organigramme en dit. Le cœur "
  "pose la question : comment obtenir d’un collectif un travail coordonné ? "
  "Les branches déploient les quatre réponses successives — rationaliser, "
  "motiver, réguler par la règle, rendre flexible — et la cinquième lecture, "
  "celle du pouvoir, qui traverse toutes les autres.",
  [("Quatre modèles, une même question",
    "Taylorisme, relations humaines, bureaucratie, toyotisme : chacun répond "
    "à l’échec du précédent. Restituer l’enchaînement vaut mieux que "
    "juxtaposer des fiches."),
   ("La lecture transversale",
    "L’analyse stratégique de Crozier ne s’ajoute pas aux quatre modèles : "
    "elle les relit tous. Partout où une règle est incomplète, quelqu’un "
    "contrôle une zone d’incertitude, donc détient du pouvoir."),
   ("Ce que chaque modèle transfère",
    "Le taylorisme transfère le savoir de l’atelier au bureau des méthodes ; "
    "le toyotisme le rend aux opérateurs. Suivre ce déplacement du contrôle "
    "donne le fil conducteur le plus solide pour une dissertation.")],
  [
   nd('coeur', 'Comment coordonner un collectif ?', 'coeur',
      "Produire à plusieurs suppose de prescrire, de contrôler et de motiver. "
      "Chaque modèle d’organisation est une réponse différente à ces trois "
      "exigences.",
      grp=0,
      defi="Organiser le travail consiste à obtenir d’un ensemble d’individus "
           "un résultat coordonné qu’aucun d’eux ne produirait seul. "
           "L’exercice suppose trois opérations distinctes : prescrire ce "
           "qu’il faut faire, vérifier que cela a été fait, et donner aux "
           "personnes une raison de le faire. Les grands modèles "
           "d’organisation se distinguent par la place qu’ils accordent à "
           "chacune, et par ce qu’ils supposent du travailleur.",
      mec=[("La division du travail comme point de départ",
            "Spécialiser les tâches élève la productivité mais crée un besoin "
            "de coordination : plus la division est poussée, plus le coût "
            "d’articulation des postes augmente."),
           ("Le travail prescrit et le travail réel",
            "Ce que l’organisation demande ne recouvre jamais exactement ce "
            "que la situation exige. Cet écart est irréductible : aucune "
            "règle ne peut prévoir toutes les situations possibles."),
           ("La question du contrôle",
            "Dans l’organisation traditionnelle, le travail échappe en partie "
            "au contrôle de l’entreprise : les ouvriers qualifiés maîtrisent "
            "le processus et leur rythme. Tout le XXᵉ siècle industriel "
            "s’organise autour de ce déplacement du contrôle.")],
      aut=[{'n': "Herbert Simon",
            'i': "Les individus sont rationnels mais ne disposent ni de "
                 "toutes les informations ni de la capacité d’anticiper "
                 "toutes les conséquences."}],
      termes=['division du travail', 'organisation du travail',
              'coordination'],
      dos=['n9-division-travail', 'n9-controle-travail']),

   nd('taylor', 'Rationaliser : le taylorisme', 'pilier',
      "Observer les gestes, découper les tâches, chronométrer. Le savoir "
      "passe de l’atelier au bureau des méthodes.",
      grp=1,
      defi="Le taylorisme est l’organisation du travail fondée sur "
           "l’organisation scientifique du travail de Frederick Taylor : "
           "observation des gestes, découpage des tâches, chronométrage, afin "
           "d’identifier la manière la plus efficace de produire. Le cours "
           "insiste sur sa raison d’être : dans l’organisation "
           "traditionnelle, le travail échappe en partie au contrôle de "
           "l’entreprise.",
      mec=[("Le transfert du savoir productif",
            "Dans l’atelier traditionnel, les ouvriers sont qualifiés, "
            "maîtrisent l’ensemble du processus et contrôlent leur rythme. Le "
            "taylorisme vise d’abord un transfert de contrôle, et non une "
            "simple intensification de l’effort."),
           ("La double division du travail",
            "Division horizontale par la parcellisation des tâches, division "
            "verticale par la séparation entre ceux qui conçoivent et ceux "
            "qui exécutent : la seconde est la plus structurante."),
           ("La rémunération comme instrument disciplinaire",
            "Le salaire différentiel aux pièces attribue un salaire plus "
            "élevé en cas de respect de la norme et plus faible en cas de "
            "non-respect : la paie devient un outil de contrôle.")],
      opp=[{'t': "La parcellisation produit un travail en miettes, vidé de "
                 "son sens pour celui qui l’exécute.",
            'qui': "Georges Friedmann",
            'rep': "L’objection est confirmée par les coûts que le cours "
                   "énumère : turn-over élevé, absentéisme, malfaçons, et les "
                   "dépenses de recrutement, formation, remplacement et "
                   "retouches qui en découlent."}],
      aut=[{'n': "Frederick Taylor",
            'i': "Le travail doit devenir un objet mesurable et rationnel, "
                 "afin d’identifier la manière la plus efficace de produire."},
           {'n': "Georges Friedmann",
            'i': "La parcellisation taylorienne produit un travail en "
                 "miettes."}],
      termes=['taylorisme', 'organisation scientifique du travail',
              'parcellisation'],
      dos=['n9-taylorisme', 'n9-ost']),

   nd('ford', 'Produire et faire consommer : le fordisme', 'pilier',
      "La chaîne de montage pour la production de masse, la hausse des "
      "salaires pour la consommation de masse. Un système cohérent.",
      grp=1,
      defi="Le fordisme est le modèle d’organisation qui prolonge le "
           "taylorisme en y ajoutant deux éléments : la chaîne de montage, "
           "qui permet la production de masse, et l’augmentation des "
           "salaires, qui permet la consommation de masse. Le cours en fait "
           "un système cohérent articulant production et consommation, et le "
           "modèle dominant des Trente Glorieuses.",
      mec=[("La chaîne impose le rythme",
            "Le convoyeur retire à l’opérateur la maîtrise de sa cadence : le "
            "contrôle du rythme, que le taylorisme visait par la "
            "prescription, est obtenu par le dispositif technique lui-même."),
           ("La standardisation et l’échelle",
            "La standardisation d’un modèle unique permet la production en "
            "série et l’effondrement du coût unitaire, donc la conquête d’un "
            "marché de masse."),
           ("Le salaire comme investissement",
            "Doubler le salaire journalier fidélise la main-d’œuvre : le coût "
            "d’opportunité du départ devient supérieur à l’inconfort du "
            "poste, ce qui coûte moins cher que le turn-over évité.")],
      faits=[{'f': "Le prix d’une Ford passe de six cent quatre-vingt-dix "
                   "dollars en 1913 à deux cent quatre-vingt-dix dollars en "
                   "1929, et en 1914 soixante pour cent des voitures "
                   "produites aux États-Unis sont des Ford.",
              'p': "La baisse du prix de plus de moitié et la part de marché "
                   "obtenue valident ensemble le lien entre baisse des coûts "
                   "et élargissement de la demande."},
             {'f': "Ford fait passer le salaire journalier de deux dollars "
                   "cinquante, moyenne de l’époque, à cinq dollars.",
              'p': "Le doublement montre que la fidélisation par le coût "
                   "d’opportunité du départ était jugée moins coûteuse que le "
                   "turn-over qu’elle évitait."}],
      aut=[{'n': "Henry Ford",
            'i': "Il prolonge le taylorisme par la chaîne de montage et par "
                 "l’augmentation des salaires."}],
      termes=['fordisme', 'production de masse', 'chaine de montage'],
      dos=['n9-fordisme', 'n9-taylorisme']),

   nd('mayo', 'Motiver : l’école des relations humaines', 'pilier',
      "Vingt mille entretiens à la Western Electric : la productivité dépend "
      "aussi des relations, de l’esprit de groupe et de la reconnaissance.",
      grp=1,
      defi="L’École des relations humaines naît des travaux d’Elton Mayo à la "
           "Western Electric Company, publiés dans The Human Problems of an "
           "Industrial Civilization en 1933. Son idée centrale est que "
           "l’entreprise doit être considérée comme un système social, et non "
           "seulement comme un système technique : la productivité dépend "
           "aussi des relations entre salariés, de l’esprit de groupe et de "
           "la reconnaissance.",
      mec=[("Le paradoxe initial",
            "En 1924, la Western Electric emploie environ vingt-neuf mille "
            "personnes dans des usines aux conditions avantageuses pour "
            "l’époque, et connaît pourtant de l’absentéisme et du freinage : "
            "des conditions matérielles favorables ne garantissent pas la "
            "productivité."),
           ("L’expérience qui disqualifie l’explication matérielle",
            "Dans la Test Room, entre 1927 et 1929, la productivité d’un "
            "petit groupe d’ouvrières augmente d’environ vingt pour cent sur "
            "une année, parfois même lorsque les chercheurs détériorent "
            "volontairement certaines conditions de travail."),
           ("La norme informelle du groupe",
            "Il peut exister une norme de production fixée par le groupe et "
            "non par la direction : le collectif régule l’effort "
            "indépendamment des incitations officielles.")],
      aut=[{'n': "Elton Mayo",
            'i': "Les salariés ne réagissent pas uniquement aux incitations "
                 "économiques, mais aussi aux normes informelles de leur "
                 "groupe."}],
      faits=[{'f': "Entre 1928 et 1931, environ vingt mille entretiens sont "
                   "réalisés à la Western Electric.",
              'p': "L’ampleur de l’enquête qualitative donne du poids aux "
                   "deux résultats qu’elle dégage : l’importance de l’écoute "
                   "et l’importance du sens donné au travail."}],
      termes=['relations humaines', 'elton mayo', 'motivation au travail'],
      dos=['n9-relations-humaines', 'n9-motivation']),

   nd('weber', 'Régler : la bureaucratie', 'pilier',
      "Règles impersonnelles, hiérarchie, compétences, procédures. Chez "
      "Weber, moins d’arbitraire ; chez Crozier, un cercle vicieux.",
      grp=1,
      defi="La bureaucratie désigne une organisation fondée sur la division "
           "du travail, la hiérarchie, les compétences, les règles "
           "impersonnelles et les procédures. Le cours oppose deux lectures : "
           "chez Weber, elle permet en principe plus d’efficacité et moins "
           "d’arbitraire ; chez Crozier, elle peut produire l’effet inverse, "
           "par un cercle vicieux où les règles destinées à corriger les "
           "dysfonctionnements engendrent davantage de rigidité.",
      mec=[("La promesse wébérienne",
            "La règle impersonnelle soustrait la décision à l’arbitraire du "
            "supérieur : chacun sait ce qui s’applique, et la compétence "
            "plutôt que la faveur détermine la position."),
           ("Le cercle vicieux en cinq étapes",
            "Règles impersonnelles, rigidité, problèmes de communication et "
            "de fonctionnement, création de nouvelles règles, encore plus de "
            "rigidité. Le dysfonctionnement découle de la logique même des "
            "règles, non de leur mauvaise application."),
           ("Pourquoi la réforme échoue",
            "Ajouter des procédures pour corriger les effets des procédures "
            "relance exactement le mécanisme : c’est ce qui rend la "
            "bureaucratie résistante aux réformes qui lui ressemblent.")],
      aut=[{'n': "Max Weber",
            'i': "La bureaucratie repose sur la division du travail, la "
                 "hiérarchie, les compétences, les règles impersonnelles et "
                 "les procédures."},
           {'n': "Michel Crozier",
            'i': "La bureaucratie peut fonctionner selon un cercle vicieux : "
                 "les règles destinées à corriger les dysfonctionnements "
                 "produisent davantage de rigidité."},
           {'n': "Christian Morel",
            'i': "Le poids de la hiérarchie peut conduire à des décisions "
                 "absurdes."}],
      termes=['bureaucratie', 'regles impersonnelles',
              'cercle vicieux bureaucratique'],
      dos=['n9-bureaucratie', 'n9-regles']),

   nd('ohno', 'Rendre flexible : le toyotisme', 'pilier',
      "Juste-à-temps, flux tendus, cinq zéros, équipes semi-autonomes : le "
      "contrôle de la qualité redescend au poste de travail.",
      grp=1,
      defi="Le toyotisme est le modèle d’organisation développé par Toyota "
           "après la Seconde Guerre mondiale, qui répond aux limites du "
           "modèle tayloro-fordiste par la flexibilité et la qualité. Il "
           "repose sur le juste-à-temps, les flux tendus, la règle des cinq "
           "zéros et sur une nouvelle place accordée aux travailleurs, "
           "devenus polyvalents et responsables de la qualité.",
      mec=[("La production tirée par l’aval",
            "On ne produit que ce qu’on a vendu : le flux part de la commande "
            "et remonte la chaîne, au lieu d’être poussé par les capacités "
            "disponibles."),
           ("L’inversion de la division verticale",
            "Les opérateurs travaillent en équipes semi-autonomes, "
            "surveillent les machines, qui s’arrêtent automatiquement en cas "
            "de problème, et peuvent arrêter la chaîne : le contrôle de la "
            "qualité est déplacé vers le poste."),
           ("Le savoir ouvrier redevenu ressource",
            "La démarche kaizen sollicite les opérateurs pour proposer des "
            "améliorations de leur poste, alors que le taylorisme avait "
            "transféré ce savoir au bureau des méthodes.")],
      args=[{'a': "Le toyotisme corrige les coûts sociaux du taylorisme — "
                  "turn-over, absentéisme, malfaçons — en rendant au "
                  "travailleur une part de maîtrise sur son poste.",
             'lim': "Les flux tendus rendent la production plus vulnérable "
                    "aux perturbations : la suppression des stocks supprime "
                    "aussi le matelas qui absorbait les aléas."}],
      aut=[{'n': "Taiichi Ohno",
            'i': "La production doit être tirée par l’aval : on ne produit "
                 "que ce qu’on a vendu."}],
      faits=[{'f': "La règle des cinq zéros du système de production de "
                   "Toyota fixe zéro stock, zéro délai, zéro panne, zéro "
                   "défaut et zéro papier.",
              'p': "La formulation chiffrée montre que la lutte contre le "
                   "gaspillage n’est pas un principe vague mais un objectif "
                   "décliné poste par poste."}],
      termes=['toyotisme', 'juste a temps', 'flux tendus', 'kaizen'],
      dos=['n9-toyotisme', 'n9-flexibilite-organisationnelle']),

   nd('crozier', 'Le pouvoir : zones d’incertitude', 'debat',
      "Aucune règle ne prévoit tout. Celui qui maîtrise ce qui reste "
      "imprévisible détient du pouvoir, quelle que soit sa place dans "
      "l’organigramme.",
      grp=2, par='weber',
      defi="Une zone d’incertitude est une situation dans laquelle les règles "
           "sont imprécises ou incomplètes et certaines situations ne sont "
           "pas totalement prévisibles. Le cours précise que toutes les "
           "organisations en possèdent, parce qu’aucune règle ne peut prévoir "
           "toutes les situations possibles, et que ce qui constitue un "
           "problème pour l’organisation devient une ressource pour certains "
           "acteurs.",
      mec=[("Le pouvoir suit la dépendance, non la hiérarchie",
            "L’organigramme est établi par la direction et ne montre pas "
            "nécessairement qui influence réellement qui : des positions "
            "subalternes peuvent détenir une capacité de blocage."),
           ("Les quatre ressources de l’incertitude",
            "La compétence, les relations, l’information et les règles de "
            "l’organisation : l’incertitude n’est pas seulement technique, ce "
            "qui multiplie les détenteurs possibles de pouvoir."),
           ("Le pouvoir par anticipation",
            "À la SEITA, les ouvrières hésitent à critiquer les ouvriers "
            "d’entretien par crainte d’une moindre bonne volonté : il suffit "
            "que la sanction soit possible pour qu’elle modifie les "
            "comportements.")],
      aut=[{'n': "Michel Crozier",
            'i': "La maîtrise d’une zone d’incertitude est une source de "
                 "pouvoir."},
           {'n': "Erhard Friedberg",
            'i': "L’organisation s’analyse comme un système d’action concret, "
                 "où les acteurs disposent de marges de manœuvre."}],
      faits=[{'f': "À la SEITA, les ouvrières ne savent pas quand leur "
                   "machine sera réparée, avec quelle rapidité ni avec quelle "
                   "qualité, alors que leurs primes en dépendent.",
              'p': "Le cas identifie précisément la zone d’incertitude : non "
                   "pas la panne elle-même, mais l’imprévisibilité de sa "
                   "réparation, qui est ce que les ouvriers d’entretien "
                   "contrôlent."}],
      termes=['zone d incertitude', 'acteur strategique',
              'analyse strategique'],
      dos=['n9-zones-incertitude', 'n9-acteur-strategique',
           'n9-autorite-pouvoir']),

   nd('culture', 'La culture et les règles informelles', 'detail',
      "Normes, habitudes et représentations partagées : ce que l’approche "
      "contractuelle de la firme laisse hors champ.",
      grp=2, par='mayo',
      defi="La culture d’entreprise désigne l’ensemble des normes, habitudes "
           "et représentations partagées qui orientent les comportements au "
           "sein d’une organisation, sans être inscrites dans ses règles "
           "officielles. Le cours l’introduit par la négative : c’est l’une "
           "des dimensions que l’approche contractuelle de la firme oublie, "
           "avec les relations humaines, les rapports de pouvoir et les "
           "dimensions sociales et politiques.",
      mec=[("La règle informelle comme complément nécessaire",
            "Puisque aucune prescription ne couvre toutes les situations, les "
            "habitudes partagées comblent l’écart : elles ne contredisent pas "
            "la règle, elles la rendent applicable."),
           ("La norme de groupe comme régulation",
            "Les groupes de travail produisent des normes informelles qui "
            "commandent la production : la direction fixe un objectif, le "
            "collectif fixe un rythme.")],
      args=[{'a': "Prendre au sérieux la culture explique pourquoi deux "
                  "entreprises dotées des mêmes procédures obtiennent des "
                  "résultats très différents.",
             'lim': "La notion est difficile à délimiter : invoquée sans "
                    "enquête, elle sert à expliquer après coup n’importe quel "
                    "écart constaté."}],
      aut=[{'n': "Elton Mayo",
            'i': "L’entreprise doit être considérée comme un système social "
                 "et une collectivité humaine."},
           {'n': "Douglass North",
            'i': "Les institutions reposent à la fois sur des règles "
                 "formelles et sur des règles informelles."}],
      termes=['culture d entreprise', 'regles informelles', 'normes'],
      dos=['n9-culture-entreprise', 'n9-regles']),

   nd('cout', 'Le coût humain de l’organisation', 'limite',
      "Turn-over, absentéisme, malfaçons, souffrance : les dysfonctionnements "
      "sociaux ont un coût chiffrable, et c’est lui qui fait changer de "
      "modèle.",
      grp=2, par='taylor',
      defi="Chaque modèle d’organisation produit ses propres "
           "dysfonctionnements, et c’est leur coût qui déclenche le passage "
           "au suivant. Le cours énumère pour le taylorisme : turn-over "
           "élevé, absentéisme, malfaçons, et les coûts qui en découlent — "
           "recrutement, formation, remplacement, retouches. La souffrance au "
           "travail n’est donc pas seulement une question morale : elle a une "
           "traduction comptable.",
      mec=[("Le coût du désengagement",
            "Un salarié qui n’a aucune marge de décision n’apporte que sa "
            "force de travail : l’organisation perd la connaissance de la "
            "situation que lui seul détient."),
           ("L’écart entre travail prescrit et travail réel",
            "Ce que l’organisation demande ne recouvre jamais exactement ce "
            "que la situation exige : c’est dans cet écart que se logent à la "
            "fois l’initiative et la souffrance."),
           ("Le déclenchement du changement de modèle",
            "C’est lorsque le coût des dysfonctionnements dépasse le gain de "
            "la prescription que l’entreprise cherche une autre organisation "
            "— ce qui explique l’enchaînement historique des modèles.")],
      aut=[{'n': "Georges Friedmann",
            'i': "La parcellisation taylorienne produit un travail en "
                 "miettes."}],
      termes=['souffrance au travail', 'autonomie au travail',
              'absenteisme'],
      dos=['n9-souffrance-sens', 'n9-autonomie']),
  ],
  [
   ln('coeur', 'taylor', 'reçoit une première réponse de',
      "Si le travail échappe en partie au contrôle de l’entreprise parce que "
      "l’ouvrier qualifié maîtrise le processus, alors la première réponse "
      "consiste à mesurer ce processus et à le transférer au bureau des "
      "méthodes.", 'cause'),
   ln('taylor', 'ford', 'est prolongé par',
      "Le fordisme ne remplace pas le taylorisme : il y ajoute la chaîne, qui "
      "impose le rythme par le dispositif technique, et le salaire élevé, qui "
      "fidélise. La rationalisation du travail en reste le socle.", 'cause'),
   ln('taylor', 'cout', 'produit',
      "Turn-over élevé, absentéisme, malfaçons, et les coûts de recrutement, "
      "formation, remplacement et retouches : les dysfonctionnements sociaux "
      "ont une traduction comptable qui finit par peser plus que le gain de "
      "prescription.", 'cause'),
   ln('cout', 'mayo', 'appelle',
      "C’est le paradoxe de conditions matérielles favorables associées à de "
      "l’absentéisme et du freinage qui justifie l’enquête de la Western "
      "Electric : il faut chercher ailleurs que dans le poste de travail.",
      'cause'),
   ln('mayo', 'culture', 'met au jour',
      "Les groupes de travail produisent des normes informelles qui "
      "commandent la production : la direction fixe un objectif, le collectif "
      "fixe un rythme. La culture entre ainsi dans l’analyse de "
      "l’organisation.", 'cause'),
   ln('coeur', 'weber', 'reçoit une autre réponse de',
      "Plutôt que de prescrire le geste, on peut régler la fonction : la "
      "règle impersonnelle soustrait la décision à l’arbitraire et fait de la "
      "compétence, non de la faveur, le critère de la position.", 'cause'),
   ln('weber', 'crozier', 'est retournée par',
      "La règle impersonnelle ne peut pas tout prévoir. Là où elle est "
      "incomplète s’ouvre une zone d’incertitude, et celui qui la maîtrise "
      "détient un pouvoir que l’organigramme ne montre pas.", 'oppose'),
   ln('crozier', 'weber', 'explique l’échec des réformes de',
      "Les organisations changent difficilement parce que les réformes "
      "menacent les zones d’incertitude sur lesquelles les acteurs ont bâti "
      "leurs stratégies : ajouter des procédures relance exactement le cercle "
      "vicieux.", 'renforce'),
   ln('cout', 'ohno', 'conduit à',
      "Le toyotisme répond aux limites du modèle tayloro-fordiste : il rend "
      "au travailleur une part de maîtrise sur son poste, ce qui réduit "
      "précisément les coûts de désengagement que le taylorisme produisait.",
      'cause'),
   ln('ohno', 'taylor', 'inverse la division verticale de',
      "La démarche kaizen sollicite les opérateurs pour améliorer leur poste, "
      "alors que le taylorisme avait transféré ce savoir au bureau des "
      "méthodes : le mouvement est exactement inverse.", 'oppose'),
   ln('mayo', 'ohno', 'prépare',
      "Si la productivité dépend des relations, de l’esprit de groupe et de "
      "la reconnaissance, alors les équipes semi-autonomes et la "
      "responsabilité de la qualité au poste ne sont pas une concession mais "
      "un levier d’efficacité.", 'cause'),
   ln('ohno', 'crozier', 'déplace les zones d’incertitude',
      "Rendre l’opérateur polyvalent et responsable de la qualité lui donne "
      "la maîtrise d’aléas que la prescription contrôlait : le pouvoir se "
      "redistribue en même temps que le travail se réorganise.", 'renforce'),
   ln('culture', 'crozier', 'se complète avec',
      "Normes partagées et stratégies d’acteurs décrivent deux faces du même "
      "écart à la règle officielle : l’une par ce qui est commun, l’autre par "
      "ce qui est disputé.", 'renforce'),
   ln('crozier', 'coeur', 'relit toute la question',
      "Coordonner n’est jamais seulement prescrire : c’est composer avec des "
      "acteurs qui disposent de marges de manœuvre et les utilisent. Le "
      "pouvoir n’est pas un obstacle à l’organisation, il en est une "
      "dimension.", 'renforce'),
   ln('ohno', 'cout', 'déplace sans supprimer',
      "Les flux tendus rendent la production plus vulnérable aux "
      "perturbations : supprimer les stocks supprime aussi le matelas qui "
      "absorbait les aléas, et la pression se reporte sur les personnes.",
      'limite'),
   ln('ford', 'culture', 'lie le salaire à l’appartenance',
      "Doubler le salaire ne joue pas seulement sur le calcul individuel : il "
      "installe une norme d’appartenance à l’entreprise, dont le coût de "
      "sortie devient dissuasif.", 'cause'),
  ],
  fam='Innovation, travail et entreprise')
