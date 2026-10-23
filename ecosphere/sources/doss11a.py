# -*- coding: utf-8 -*-
"""Ensemble 11 — La monnaie, les banques et le crédit (1/4)."""

from doss_base import d

d('n11-fonctions-monnaie', 11, "Fonctions de la monnaie",
  "Compter, échanger, conserver : trois fonctions et un actif liquide",
  "La monnaie est un actif liquide qui sert à l’évaluation et au règlement des "
  "échanges. Le cours lui attribue trois fonctions, rattachées à Aristote : "
  "unité de compte, intermédiaire des échanges et réserve de valeur. Actif "
  "liquide signifie qu’elle peut être utilisée immédiatement pour acheter des "
  "biens ou des services, sans délai ni perte de valeur.",
  "Le cours construit la monnaie par ses fonctions plutôt que par sa forme, et "
  "c’est ce choix qui permet ensuite de trancher des débats contemporains. Les "
  "trois fonctions d’abord, dont l’origine est rattachée à Aristote, vers 350 "
  "avant notre ère : l’unité de compte sert à mesurer la valeur des biens et "
  "des services ; l’intermédiaire des échanges permet de payer et donc de "
  "régler les échanges entre agents ; la réserve de valeur permet de conserver "
  "du pouvoir d’achat dans le temps. Le cours insiste sur une conséquence "
  "juridique : le billet a un pouvoir libérateur absolu, c’est-à-dire qu’avec "
  "la monnaie on peut tout acheter. Il ajoute une caractérisation "
  "économique originale : la monnaie est à la fois un bien public et un bien "
  "privé, reposant sur la confiance. Bien public, parce qu’elle profite à "
  "toute la société, facilite les échanges entre tous les agents et engendre "
  "des externalités positives, en permettant le commerce elle stimule la "
  "production, la consommation et la croissance. Bien privé, parce que chacun "
  "en possède et l’utilise pour son intérêt personnel, consommer, investir, "
  "épargner. Le cours prolonge l’analyse à l’échelle internationale avec Paul "
  "Krugman, qui définit une monnaie internationale comme une monnaie utilisée "
  "au-delà des frontières nationales par le secteur privé et par les banques "
  "centrales, et distingue six fonctions : monnaie de libellé, véhiculaire et "
  "d’investissement du point de vue privé, monnaie d’ancrage, d’intervention "
  "et de réserve du point de vue des banques centrales. Il s’en sert enfin "
  "comme critère de tri : le Bitcoin ne remplit pas les trois fonctions d’une "
  "monnaie, il n’est ni unité de compte ni réellement moyen d’échange, ce qui "
  "en fait un crypto-actif plutôt qu’une monnaie.",
  [("La mesure des valeurs",
    "Comme unité de compte, la monnaie permet d’exprimer tous les prix dans un "
    "même étalon : elle rend les valeurs comparables, ce qui est la condition "
    "d’un calcul économique et d’une comptabilité."),
   ("Le règlement des échanges",
    "Comme intermédiaire des échanges, la monnaie évite d’avoir à trouver une "
    "contrepartie désirant exactement ce que l’on possède : elle dissocie "
    "l’achat de la vente et élargit donc considérablement le champ des "
    "échanges possibles."),
   ("La conservation du pouvoir d’achat",
    "Comme réserve de valeur, la monnaie permet de reporter une dépense dans "
    "le temps : cette fonction suppose que sa valeur se maintienne, ce qui "
    "explique que l’inflation l’affaiblisse directement."),
   ("Le pouvoir libérateur",
    "Le billet a un pouvoir libérateur absolu : il éteint toute dette et "
    "permet d’acheter n’importe quel bien, ce qui distingue la monnaie des "
    "autres actifs, négociables mais non universellement acceptés."),
   ("L’externalité positive de l’usage collectif",
    "La monnaie est d’autant plus utile que tous l’acceptent : son usage "
    "produit des externalités positives, ce qui en fait un bien public en même "
    "temps qu’un bien privé que chacun détient pour son propre compte.")],
  [{'a': "Définir la monnaie par ses fonctions plutôt que par sa forme permet "
         "de suivre sa dématérialisation historique sans changer de concept.",
    'cond': "L’approche suppose que les trois fonctions soient effectivement "
            "remplies par le support considéré, quel qu’il soit.",
    'lim': "Elle ne dit pas quel degré de liquidité est requis : les agrégats "
           "monétaires sont précisément construits pour classer des actifs "
           "plus ou moins liquides."},
   {'a': "Le critère fonctionnel permet de trancher un débat contemporain : "
         "le Bitcoin n’est pas une monnaie mais un crypto-actif.",
    'cond': "Le verdict suppose de constater que les prix ne sont pas fixés "
            "en Bitcoin et que très peu d’acteurs l’acceptent en paiement.",
    'lim': "Le cours relève tout de même qu’il remplit partiellement une "
           "fonction de réserve de valeur pour ceux qui le thésaurisent, bien "
           "que sa volatilité la fragilise."},
   {'a': "La qualification de bien public explique pourquoi la monnaie ne peut "
         "pas être entièrement laissée au marché.",
    'cond': "Elle suppose que l’usage de la monnaie par un agent n’empêche "
            "pas celui des autres et accroisse au contraire son utilité pour "
            "tous.",
    'lim': "Le cours souligne qu’elle est aussi un bien privé, détenu et "
           "utilisé pour un intérêt personnel, ce qui interdit de la traiter "
           "comme un pur bien collectif."},
   {'a': "L’extension des fonctions à l’échelle internationale par Krugman "
         "explique la domination d’une devise sans recourir à la contrainte "
         "politique.",
    'cond': "Elle exige que la monnaie considérée soit effectivement stable et "
            "liquide, conditions que le cours attribue au dollar.",
    'lim': "Cette lecture fonctionnelle n’explique pas comment une monnaie "
           "acquiert ce statut : le cours doit recourir à l’histoire, le "
           "dollar remplaçant la livre après les deux guerres mondiales."}],
  [{'t': "La monnaie se définit par trois fonctions : unité de compte, "
         "intermédiaire des échanges et réserve de valeur.",
    'qui': "Le cours rattache cette tripartition à Aristote, vers 350 avant "
           "notre ère.",
    'rep': "Le cours relève qu’avant le vingtième siècle les économistes "
           "n’en retenaient que deux, unité de compte et moyen d’échange, "
           "considérant que la monnaie n’affectait que le niveau général des "
           "prix."},
   {'t': "Une monnaie internationale remplit six fonctions, trois du point de "
         "vue privé et trois du point de vue des banques centrales.",
    'qui': "Paul Krugman, dans sa définition de la monnaie internationale.",
    'rep': "La grille décrit bien le statut du dollar, mais le cours montre "
           "qu’elle laisse ouverte la question de l’euro, deuxième monnaie "
           "internationale sans jouer tous ces rôles, et donc plutôt monnaie "
           "régionale."},
   {'t': "Le Bitcoin est une monnaie puisqu’il permet des transactions "
         "décentralisées sans passer par les banques ni par les États.",
    'qui': "L’argument des promoteurs du Bitcoin, créé en 2008 sous le "
           "pseudonyme de Satoshi Nakamoto.",
    'rep': "Le cours objecte qu’il ne remplit pas les trois fonctions : les "
           "prix ne sont pas fixés en Bitcoin, très peu d’acteurs l’acceptent "
           "en paiement, et il ne repose sur aucune valeur réelle ni "
           "garantie, ce qui en fait un actif spéculatif."}],
  [{'n': "Paul Krugman",
    'i': "Une monnaie internationale est utilisée au-delà des frontières "
         "nationales par le secteur privé et par les banques centrales.",
    'p': "Le cours détaille ses six fonctions : du point de vue privé, "
         "monnaie de libellé, véhiculaire et d’investissement ; du point de "
         "vue des banques centrales, monnaie d’ancrage, d’intervention et de "
         "réserve. Le dollar joue ces six rôles, ce qui explique sa "
         "domination."},
   {'n': "Satoshi Nakamoto",
    'i': "Le Bitcoin a été conçu pour permettre des transactions sans banques "
         "ni États, par une technologie décentralisée.",
    'p': "Le cours rappelle que le Bitcoin est créé en 2008 sous ce "
         "pseudonyme, après la crise financière, et repose sur la blockchain, "
         "registre numérique décentralisé où les transactions sont "
         "enregistrées et vérifiées par les utilisateurs eux-mêmes."},
   {'n': "Christine Lagarde",
    'i': "Les économies contemporaines connaissent une situation de "
         "permacrises, succession constante de crises inédites majeures.",
    'p': "Le cours ouvre le chapitre sur le financement de l’économie par ce "
         "diagnostic, ce qui situe la question monétaire dans un contexte "
         "d’instabilité où la confiance dans la monnaie et dans les "
         "institutions devient un enjeu central."}],
  [{'f': "Dans la zone euro, quatre-vingt-onze pour cent de la monnaie est de "
         "la monnaie scripturale, l’essentiel des transactions bancaires étant "
         "des virements et des prélèvements.",
    'p': "Le chiffre montre que les fonctions de la monnaie sont aujourd’hui "
         "assurées par des écritures comptables, ce qui confirme que la "
         "définition fonctionnelle est indépendante du support."},
   {'f': "En France, un individu peut payer jusqu’à mille euros en liquide, et "
         "le commerçant a le droit de refuser un chèque.",
    'p': "Ces règles montrent que le pouvoir libérateur n’est pas identique "
         "pour tous les supports : seule la monnaie fiduciaire a cours légal "
         "sans restriction d’usage, dans les limites fixées par la loi."},
   {'f': "Le nombre total de bitcoins est limité à vingt-et-un millions, dont "
         "dix-neuf virgule huit millions déjà produits, et son cours dépend "
         "uniquement de l’offre et de la demande.",
    'p': "Cette masse fixe et cette volatilité expliquent l’échec de la "
         "fonction de réserve de valeur : un actif dont le prix varie "
         "fortement ne conserve pas le pouvoir d’achat."}],
  [{'q': "Pourquoi accepte-t-on la monnaie ?",
    'f': "Parce qu’elle remplit trois fonctions qu’aucun autre actif ne "
         "cumule : elle mesure les valeurs, elle règle les échanges et elle "
         "conserve du pouvoir d’achat. Le cours ajoute une raison plus "
         "profonde : le billet a un pouvoir libérateur absolu, ce qui "
         "signifie que son acceptation par chacun repose sur la certitude "
         "qu’elle sera acceptée par tous.",
    'r': "Le raisonnement part des fonctions pour arriver à une propriété "
         "collective : l’utilité de la monnaie dépend de son acceptation "
         "générale, ce qui en fait un bien public autant qu’un bien privé.",
    'ex': "Le cours souligne que la monnaie engendre des externalités "
          "positives en permettant le commerce."},
   {'q': "Les cryptomonnaies sont-elles des monnaies comme les autres ?",
    'f': "Le cours applique le critère fonctionnel et conclut que non : le "
         "Bitcoin n’est pas unité de compte, puisque les prix ne sont pas "
         "fixés en Bitcoin, et n’est guère moyen d’échange, puisque très peu "
         "d’entreprises ou de pays l’acceptent. Il ne repose sur aucune "
         "valeur réelle, ni État, ni garantie, ni revenu, ce qui en fait un "
         "actif financier hautement spéculatif.",
    'r': "Le raisonnement applique une définition établie à un cas nouveau, "
         "ce qui permet de trancher sans jugement de valeur sur la "
         "technologie elle-même.",
    'ex': "Le cours qualifie le Bitcoin de crypto-actif plutôt que de "
          "monnaie."},
   {'q': "Qu’est-ce qui fait d’une monnaie une monnaie internationale ?",
    'f': "Krugman répond par l’usage : une monnaie est internationale "
         "lorsqu’elle est utilisée au-delà des frontières par le secteur "
         "privé comme par les banques centrales, à travers six fonctions. Le "
         "dollar les remplit toutes, ce qui explique que le pétrole soit "
         "libellé en dollars même pour une vente entre un pays européen et un "
         "pays asiatique.",
    'r': "On montre que le statut international n’est pas décrété mais "
         "résulte d’usages cumulés, chacun renforçant les autres par un effet "
         "d’entraînement.",
    'ex': "Le cours rappelle que la livre a joué ce rôle jusqu’en 1914, avant "
          "d’être remplacée par le dollar après 1945."}],
  voisins=['n11-confiance', 'n11-monnaie-bancaire', 'n11-liquidite',
           'n11-neutralite-monnaie'])


d('n11-confiance', 11, "Confiance monétaire",
  "Fiducia : une monnaie ne vaut que ce que l’on croit qu’elle vaut",
  "La confiance est le fondement de la valeur de la monnaie : le cours "
  "rappelle que la monnaie repose sur la confiance et que le mot fiduciaire "
  "vient du latin fiducia, qui signifie précisément confiance. C’est cette "
  "confiance qui donne au billet son pouvoir libérateur absolu, alors qu’il "
  "n’a par lui-même aucune valeur intrinsèque.",
  "Le cours traite la confiance monétaire par son histoire, ce qui en fait un "
  "objet démontrable et non une pétition de principe. Point de départ : la "
  "monnaie est à la fois un bien public et un bien privé se fondant sur la "
  "confiance, et la monnaie fiduciaire tire son nom du latin fiducia. La "
  "dématérialisation en est la démonstration historique : au début la valeur "
  "de la monnaie reposait sur les métaux, puis elle est devenue fiduciaire, "
  "puis scripturale, et le cours note que la tendance de l’histoire est de "
  "toujours changer de forme de monnaie. À chaque étape, la part de la valeur "
  "intrinsèque diminue et la part de la confiance augmente. L’épisode décisif "
  "est le système de John Law. En 1716, la France est ruinée après les guerres "
  "de Louis quatorze et manque de monnaie métallique ; Law crée la Banque "
  "Générale, banque privée émettant des billets convertibles en or, ce qui "
  "inspire confiance, puis la Banque Royale en 1718, l’État garantissant "
  "désormais les billets. Les gens achètent avec ces billets des actions de la "
  "Compagnie du Mississippi, dont le cours passe de cent cinquante à quatre "
  "mille cent livres. Le mécanisme devient circulaire : la banque émet des "
  "billets, l’État rembourse ses dettes, les individus achètent des actions, "
  "l’argent revient à la Banque, de nouveaux billets sont fabriqués, d’où une "
  "création monétaire sans limite. En 1720 le système éclate : les gens "
  "veulent échanger leurs billets contre de l’or, la Banque n’a plus de "
  "réserves, c’est la panique et l’effondrement. Les conséquences sont une "
  "crise financière, la ruine des épargnants, mais surtout une hostilité "
  "durable des Français envers les banques et la monnaie papier, et un retour "
  "à la monnaie métallique pendant longtemps. La confiance détruite ne se "
  "reconstitue pas vite.",
  [("L’absence de valeur intrinsèque",
    "Un billet ne vaut rien par lui-même : sa valeur procède entièrement de "
    "la croyance qu’il sera accepté, ce que signale l’étymologie du mot "
    "fiduciaire, du latin fiducia."),
   ("Le caractère auto-réalisateur de l’acceptation",
    "Chacun accepte la monnaie parce qu’il anticipe que les autres "
    "l’accepteront : la confiance se valide elle-même tant qu’elle est "
    "partagée, ce qui explique à la fois sa solidité ordinaire et sa fragilité "
    "soudaine."),
   ("La garantie institutionnelle",
    "La convertibilité, puis la garantie de l’État, puis celle de la banque "
    "centrale fournissent un support à la confiance : la monnaie fiduciaire "
    "est d’abord devenue monnaie officielle parce que l’État garantissait les "
    "billets."),
   ("Le déséquilibre entre engagements et réserves",
    "Quand les billets émis dépassent largement les réserves qui les "
    "couvrent, une demande simultanée de conversion devient impossible à "
    "honorer : la confiance se retourne en panique sans que la valeur "
    "économique sous-jacente ait changé."),
   ("La persistance de la méfiance",
    "Une crise de confiance laisse des traces bien au-delà de ses pertes "
    "comptables : l’hostilité durable des Français envers les banques et la "
    "monnaie papier après 1720 montre que la confiance se détruit vite et se "
    "reconstruit lentement.")],
  [{'a': "Faire de la confiance le fondement de la monnaie explique sa "
         "dématérialisation progressive sans changer de concept.",
    'cond': "L’argument suppose une institution crédible pour garantir la "
            "monnaie, État ou banque centrale.",
    'lim': "Il rend la valeur de la monnaie dépendante d’une croyance, donc "
           "vulnérable à des retournements rapides que les fondamentaux "
           "économiques n’expliquent pas."},
   {'a': "L’épisode de John Law fournit une démonstration historique : une "
         "monnaie dont les contreparties disparaissent s’effondre.",
    'cond': "La leçon vaut pour un système promettant la convertibilité en un "
            "actif que l’émetteur ne détient pas en quantité suffisante.",
    'lim': "Les monnaies contemporaines ne sont plus convertibles en or, de "
           "sorte que le mécanisme précis de 1720 ne peut pas se reproduire "
           "à l’identique."},
   {'a': "La confiance explique l’attractivité internationale d’une monnaie "
         "mieux que la seule taille de l’économie émettrice.",
    'cond': "Elle suppose que la monnaie conserve effectivement sa valeur "
            "dans le temps, ce que le cours attribue au dollar.",
    'lim': "Cette confiance peut devenir un privilège auto-entretenu : la "
           "demande mondiale de dollars soutient sa valeur, ce qui renforce "
           "la confiance indépendamment des performances économiques."},
   {'a': "L’absence de garantie institutionnelle explique la fragilité des "
         "crypto-actifs, qu’aucun État ne soutient.",
    'cond': "Le raisonnement exige de constater que ces actifs ne reposent "
            "sur aucun État, ne sont pas soutenus par les banques centrales "
            "et n’offrent aucune garantie.",
    'lim': "Leurs promoteurs répondent que la confiance peut venir du "
           "protocole lui-même, la blockchain permettant la vérification sans "
           "autorité centrale."}],
  [{'t': "La monnaie repose sur la confiance et non sur une valeur "
         "intrinsèque, ce qui explique qu’elle ait pu se dématérialiser.",
    'qui': "L’analyse du cours, qui rattache le mot fiduciaire au latin "
           "fiducia.",
    'rep': "Le cours montre la contrepartie de cette dépendance : l’épisode "
           "de John Law en 1720 prouve qu’une perte de confiance suffit à "
           "détruire une monnaie, provoquant panique, effondrement et "
           "hostilité durable envers le papier-monnaie."},
   {'t': "Un système de papier-monnaie garanti par l’État permet de relancer "
         "l’économie par le crédit et par une plus grande circulation "
         "monétaire.",
    'qui': "John Law, dans le système qu’il met en place entre 1716 et 1720.",
    'rep': "Le cours relève que le mécanisme devient circulaire et conduit à "
           "une création monétaire sans limite, puis à l’effondrement de "
           "1720 ; Schumpeter lui rend néanmoins hommage comme monétariste et "
           "pré-keynésien."},
   {'t': "La suppression des billets serait sans inconvénient, puisque la "
         "monnaie scripturale remplit les mêmes fonctions à moindre coût.",
    'qui': "L’argument des banques, que le cours rapporte avec ses raisons de "
           "coût et de traçabilité.",
    'rep': "Le cours cite les objections : fraude électronique, obligation "
           "légale de pouvoir payer partout en espèces dans la zone euro, et "
           "disparition du seul moyen de paiement anonyme."}],
  [{'n': "John Law",
    'i': "Il veut remplacer la monnaie métallique par des billets de banque "
         "pour relancer l’économie par le crédit.",
    'p': "Le cours décrit son dispositif : la Banque Générale en 1716, banque "
         "privée émettant des billets convertibles en or ce qui inspire "
         "confiance, devenue Banque Royale en 1718 avec la garantie de "
         "l’État, puis la Compagnie du Mississippi dont les actions passent "
         "de cent cinquante à quatre mille cent livres."},
   {'n': "Joseph Schumpeter",
    'i': "Il rend hommage à John Law en le qualifiant de monétariste et de "
         "pré-keynésien.",
    'p': "Le cours mentionne ce jugement pour nuancer la condamnation de "
         "l’épisode : Law a compris avant d’autres le rôle actif de la "
         "monnaie et du crédit dans l’activité, même si son système a produit "
         "la première grande bulle financière."},
   {'n': "Jean Bodin",
    'i': "Un excès de monnaie provoque de l’inflation, c’est-à-dire une "
         "hausse des prix.",
    'p': "Le cours le range parmi les auteurs classiques pour qui la monnaie "
         "n’est qu’un voile : il reconnaît que le commerce passe par la "
         "monnaie, mais observe que trop de monnaie fait monter les prix sans "
         "accroître la production, ce qui mine la confiance dans sa valeur."}],
  [{'f': "En 1716 la France est ruinée après les guerres de Louis quatorze et "
         "manque de monnaie métallique, ce qui conduit John Law à proposer "
         "des billets de banque.",
    'p': "Le contexte montre que la monnaie de confiance naît d’une pénurie "
         "de monnaie de valeur intrinsèque, et non d’un choix doctrinal."},
   {'f': "En 1720, les détenteurs veulent échanger leurs billets contre de "
         "l’or, la Banque n’a plus de réserves, et le système s’effondre dans "
         "la panique.",
    'p': "Le mécanisme démontre qu’un système fondé sur la confiance résiste "
         "tant que les demandes de conversion restent dispersées et cède dès "
         "qu’elles se concentrent."},
   {'f': "La crise de 1720 provoque la ruine des épargnants mais aussi une "
         "hostilité durable des Français envers les banques et la monnaie "
         "papier, avec un retour à la monnaie métallique pendant longtemps.",
    'p': "La durée de cette défiance montre que la confiance monétaire est un "
         "actif collectif coûteux à reconstituer, ce qui justifie les "
         "institutions chargées de la préserver."}],
  [{'q': "Pourquoi accepte-t-on la monnaie ?",
    'f': "Parce qu’on fait confiance à ceux qui l’émettent et à ceux qui "
         "l’accepteront. Le cours le dit d’emblée : la monnaie est à la fois "
         "un bien public et un bien privé se fondant sur la confiance, et le "
         "mot fiduciaire vient du latin fiducia. Un billet n’a aucune valeur "
         "intrinsèque : il ne vaut que par la certitude partagée qu’il sera "
         "reçu en paiement.",
    'r': "Le raisonnement remonte de l’acceptation observée à sa condition, "
         "une croyance collective, puis montre que cette croyance a besoin "
         "d’un garant institutionnel.",
    'ex': "La dématérialisation, du métal au billet puis à l’écriture "
          "comptable, mesure la part croissante de la confiance."},
   {'q': "Une monnaie peut-elle perdre sa valeur sans que l’économie "
         "change ?",
    'f': "L’épisode de John Law le démontre : en 1720, aucune ressource "
         "productive ne disparaît, mais les détenteurs veulent convertir leurs "
         "billets en or, la Banque n’a plus de réserves, et la panique "
         "détruit la monnaie. La valeur reposait sur une promesse que le "
         "nombre de billets émis rendait impossible à tenir.",
    'r': "On isole la variable monétaire des variables réelles pour montrer "
         "qu’un effondrement monétaire peut être purement institutionnel et "
         "non productif.",
    'ex': "Les actions de la Compagnie du Mississippi passent de cent "
          "cinquante à quatre mille cent livres avant l’effondrement."},
   {'q': "La confiance se décrète-t-elle ?",
    'f': "Non, et les conséquences de 1720 le montrent : au-delà de la crise "
         "financière et de la ruine des épargnants, le cours relève une "
         "hostilité durable des Français envers les banques et la monnaie "
         "papier, avec un retour prolongé à la monnaie métallique. La "
         "garantie de l’État avait pourtant été accordée en 1718.",
    'r': "Le raisonnement oppose la garantie formelle, décrétée, à la "
         "confiance effective, qui dépend de l’expérience accumulée, et en "
         "tire la lenteur de sa reconstitution.",
    'ex': "La Banque Générale de 1716 inspirait confiance précisément parce "
          "que ses billets étaient convertibles en or."}],
  voisins=['n11-fonctions-monnaie', 'n11-creation-monetaire',
           'n13-panique-bancaire', 'n11-banque-centrale'])


d('n11-creation-monetaire', 11, "Création monétaire",
  "Les crédits font les dépôts : monétiser une créance",
  "La création monétaire est la transformation de créances sur les agents non "
  "bancaires en moyens de paiement immédiatement utilisables pour effectuer "
  "des règlements : le cours parle de monétisation d’une créance. Sa formule "
  "centrale est que les crédits font les dépôts, c’est-à-dire que la banque "
  "n’a pas besoin de dépôts préalables pour accorder un crédit.",
  "Le cours construit la création monétaire par un renversement de l’intuition "
  "commune, puis en précise les occasions, les contreparties et les limites. "
  "Le renversement d’abord : quand un ménage ou une entreprise demande un "
  "crédit, la banque crée en même temps la monnaie et sa contrepartie, d’où la "
  "formule les crédits font les dépôts ; la banque n’a pas besoin de dépôts "
  "préalables pour faire un crédit. L’exemple est explicite : une banque prête "
  "cinquante mille euros à un ménage ou à une entreprise et crée la monnaie au "
  "moment du prêt, en inscrivant cette somme sur le compte du client. La "
  "définition générale suit : la création monétaire est la transformation de "
  "créances sur les agents non bancaires en moyens de paiement immédiatement "
  "utilisables, c’est-à-dire la monétisation d’une créance ; la banque "
  "transforme une promesse de remboursement en argent disponible sur un "
  "compte. Les occasions sont au nombre de trois : lorsqu’une banque accorde "
  "un crédit à un ménage ou à une entreprise ; lorsqu’un exportateur demande "
  "la conversion de ses devises en monnaie nationale ; lorsqu’une banque "
  "achète des obligations d’État, auquel cas elle n’a pas sorti d’argent "
  "qu’elle possédait mais a créé la monnaie en même temps qu’elle acquérait le "
  "titre. Les contreparties sont les actifs que la banque détient en face de "
  "la monnaie créée : créances sur l’économie, créances sur l’étranger, "
  "créances sur le Trésor public. Les limites enfin : la création monétaire "
  "n’est pas sans limite, la banque devant disposer de monnaie centrale pour "
  "les retraits en billets et pour les réserves obligatoires, qu’elle obtient "
  "sur le marché interbancaire ou par refinancement auprès de la banque "
  "centrale. Le système de John Law illustre a contrario ce qu’est une "
  "création monétaire sans limite.",
  [("La monétisation d’une créance",
    "La banque inscrit sur le compte du client une somme qu’elle ne détenait "
    "pas, en échange d’une promesse de remboursement : une dette privée "
    "devient un moyen de paiement immédiatement utilisable."),
   ("L’inversion de la chronologie",
    "Le crédit précède le dépôt et non l’inverse : la banque ne prête pas une "
    "épargne préalablement collectée, elle crée simultanément la monnaie et sa "
    "contrepartie dans son bilan."),
   ("La création par acquisition d’actifs",
    "Lorsqu’une banque achète des obligations d’État ou convertit des devises, "
    "elle crée aussi de la monnaie : l’actif entre à son bilan et le compte du "
    "vendeur est crédité, sans qu’aucune somme préexistante soit déplacée."),
   ("Les contreparties de la masse monétaire",
    "À toute monnaie créée correspond un actif détenu par la banque : "
    "créances sur l’économie, sur l’étranger ou sur le Trésor public, ce qui "
    "permet de lire l’origine de la monnaie en circulation."),
   ("La destruction monétaire par remboursement",
    "Le mécanisme est réversible : lorsque le crédit est remboursé, la "
    "créance s’éteint et la monnaie correspondante disparaît, de sorte que la "
    "masse monétaire résulte du solde entre crédits accordés et crédits "
    "remboursés."),
   ("La contrainte de monnaie centrale",
    "La banque doit se procurer de la monnaie centrale pour faire face aux "
    "retraits en billets et aux réserves obligatoires : elle l’obtient sur le "
    "marché interbancaire ou par refinancement, ce qui borne sa capacité de "
    "création.")],
  [{'a': "La formule les crédits font les dépôts explique correctement le "
         "fonctionnement bancaire observé, là où l’intuition d’une "
         "intermédiation pure échoue.",
    'cond': "L’argument suppose que la banque puisse se refinancer "
            "ultérieurement en monnaie centrale, faute de quoi elle ne "
            "pourrait pas honorer les retraits.",
    'lim': "Il ne signifie pas que la création soit illimitée : réserves "
           "obligatoires, retraits en billets et coût du refinancement la "
           "contraignent effectivement."},
   {'a': "Identifier les contreparties de la masse monétaire permet de "
         "comprendre d’où vient la monnaie en circulation.",
    'cond': "La lecture suppose que l’on dispose du bilan consolidé des "
            "banques, distinguant créances sur l’économie, sur l’étranger et "
            "sur le Trésor.",
    'lim': "Elle ne dit rien de la qualité de ces créances : une monnaie "
           "créée face à des créances douteuses pose un problème que "
           "l’agrégat ne révèle pas."},
   {'a': "Le caractère réversible de la création monétaire explique qu’une "
         "contraction du crédit réduise la masse monétaire sans décision "
         "publique.",
    'cond': "Le mécanisme suppose que les remboursements excèdent les "
            "nouveaux crédits accordés, situation caractéristique des phases "
            "de crise.",
    'lim': "Cette contraction peut devenir déflationniste, ce qui explique "
           "que les banques centrales aient cherché après 2008 à soutenir le "
           "crédit par des moyens non conventionnels."},
   {'a': "L’épisode de John Law montre ce qu’une création monétaire sans "
         "contrepartie solide produit.",
    'cond': "La comparaison vaut pour un système promettant une "
            "convertibilité que les réserves ne permettent pas d’assurer.",
    'lim': "Les systèmes contemporains ne reposent plus sur la "
           "convertibilité métallique : la limite y est prudentielle et "
           "monétaire, non la disponibilité d’un stock d’or."}],
  [{'t': "Les crédits font les dépôts : la banque n’a pas besoin de dépôts "
         "préalables pour accorder un crédit.",
    'qui': "L’analyse du cours sur la création monétaire par les banques "
           "commerciales.",
    'rep': "Le cours précise aussitôt la contrainte : la banque doit ensuite "
           "obtenir de la monnaie centrale pour les retraits et les réserves "
           "obligatoires, ce qu’elle trouve sur le marché interbancaire ou "
           "auprès de la banque centrale."},
   {'t': "C’est la banque centrale qui détermine la quantité de monnaie, les "
         "banques commerciales n’en étant que les relais.",
    'qui': "Le courant monétaire, avec le multiplicateur de crédit et la "
           "monnaie exogène.",
    'rep': "Le courant keynésien répond par le diviseur de crédit : les "
           "banques prêtent d’abord et se refinancent ensuite, de sorte que "
           "l’offre de monnaie s’adapte à la demande de crédit et que la "
           "monnaie est endogène."},
   {'t': "Une création monétaire abondante permet de relancer l’économie sans "
         "qu’aucune limite réelle ne vienne l’arrêter.",
    'qui': "Le système de John Law, que le cours présente comme une création "
           "monétaire sans limite.",
    'rep': "Le cours montre l’issue : en 1720 les détenteurs veulent "
           "convertir leurs billets, la Banque n’a plus de réserves, et le "
           "système s’effondre dans la panique, provoquant une crise "
           "financière et la ruine des épargnants."}],
  [{'n': "John Law",
    'i': "Son système repose sur un circuit où l’émission de billets alimente "
         "l’achat d’actions qui ramène l’argent à la banque.",
    'p': "Le cours décrit ce circuit : la banque émet des billets, l’État "
         "rembourse ses dettes, les individus achètent des actions, l’argent "
         "revient à la Banque, de nouveaux billets sont fabriqués, ce qui "
         "constitue une création monétaire sans limite."},
   {'n': "John Maynard Keynes",
    'i': "La quantité de monnaie dépend de la demande de crédit dans "
         "l’économie et non d’une décision de la banque centrale.",
    'p': "Le cours rattache au courant keynésien le principe du diviseur de "
         "crédit : les banques commerciales prêtent d’abord, puis se "
         "refinancent auprès de la banque centrale, de sorte que la création "
         "monétaire est endogène à l’économie réelle."},
   {'n': "Milton Friedman",
    'i': "L’offre de monnaie dépend des autorités monétaires, donc la monnaie "
         "est exogène.",
    'p': "Le cours rattache à cette position le mécanisme du multiplicateur "
         "de crédit : la banque centrale contrôle la base monétaire, les "
         "banques commerciales transforment cette monnaie centrale en masse "
         "monétaire, et la quantité est décidée de l’extérieur de "
         "l’économie."}],
  [{'f': "Le cours prend l’exemple d’une banque prêtant cinquante mille euros "
         "à un ménage ou à une entreprise : elle crée la monnaie au moment du "
         "prêt en inscrivant la somme sur le compte du client.",
    'p': "L’exemple montre que la création est une simple écriture "
         "comptable : la monnaie apparaît avec la créance, ce qui est "
         "exactement le sens de la monétisation."},
   {'f': "Lorsqu’une banque commerciale achète pour dix millions d’euros "
         "d’obligations d’État, son actif augmente du montant des titres et "
         "son passif du montant porté au compte du Trésor.",
    'p': "L’écriture démontre qu’elle n’a pas sorti d’argent qu’elle "
         "possédait : elle a créé la monnaie en même temps qu’elle acquérait "
         "l’actif."},
   {'f': "Le cours énumère trois contreparties à la masse monétaire : "
         "créances sur l’économie, créances sur l’étranger, créances sur le "
         "Trésor public.",
    'p': "Cette typologie permet d’attribuer chaque euro en circulation à "
         "l’opération qui l’a créé, et donc de distinguer monnaie créée pour "
         "l’économie privée et monnaie créée pour l’État."}],
  [{'q': "Qui crée la monnaie ?",
    'f': "Les banques commerciales, lorsqu’elles accordent un crédit, "
         "convertissent des devises ou achètent des titres publics. La "
         "formule du cours est sans ambiguïté : les crédits font les dépôts, "
         "la banque n’a pas besoin de dépôts préalables. La banque centrale, "
         "elle, crée la monnaie centrale et encadre cette création.",
    'r': "Le raisonnement distingue deux étages, monnaie scripturale créée "
         "par les banques de second rang et monnaie centrale créée par la "
         "banque centrale, ce qui permet de répondre sans confondre les deux "
         "niveaux.",
    'ex': "Une banque prêtant cinquante mille euros inscrit la somme au "
          "compte du client au moment même du prêt."},
   {'q': "Les banques prêtent-elles seulement l’épargne qu’elles "
         "collectent ?",
    'f': "Non, et c’est le point que le cours souligne le plus fermement : "
         "quand un ménage ou une entreprise demande un crédit, la banque crée "
         "en même temps la monnaie et sa contrepartie. L’épargne préalable "
         "n’est pas la condition du crédit ; la condition est la capacité de "
         "la banque à se procurer ensuite la monnaie centrale nécessaire.",
    'r': "On remplace une représentation de la banque comme simple "
         "intermédiaire par une analyse de bilan, ce qui montre que le "
         "dépôt est le résultat du crédit et non sa source.",
    'ex': "Le cours formule explicitement que les crédits font les dépôts."},
   {'q': "La création monétaire est-elle sans limite ?",
    'f': "Le cours pose la question et y répond par la contrainte de monnaie "
         "centrale : la banque doit faire face aux retraits en billets et aux "
         "réserves obligatoires, et doit donc se refinancer sur le marché "
         "interbancaire ou auprès de la banque centrale. L’histoire fournit "
         "le contre-exemple, le système de John Law ayant précisément "
         "fonctionné sans cette limite jusqu’à son effondrement en 1720.",
    'r': "Le raisonnement identifie la contrainte effective, non comptable "
         "mais institutionnelle, puis l’illustre par le cas où elle a été "
         "absente.",
    'ex': "La Banque Royale n’a plus de réserves en 1720 lorsque les "
          "détenteurs demandent la conversion de leurs billets."}],
  voisins=['n11-monnaie-bancaire', 'n11-multiplicateur-diviseur',
           'n11-credit', 'n11-banque-centrale'])


d('n11-monnaie-bancaire', 11, "Monnaie bancaire",
  "Quatre-vingt-onze pour cent de la monnaie n’est qu’une écriture",
  "La monnaie bancaire, ou monnaie scripturale, est la somme inscrite sur un "
  "compte bancaire. Le cours la distingue soigneusement de son support, qui "
  "est le moyen utilisé pour transférer cette somme : chèque, carte bancaire, "
  "application mobile, virement, prélèvement. Dans la zone euro, elle "
  "représente quatre-vingt-onze pour cent de la monnaie.",
  "Le cours traite la monnaie bancaire comme l’aboutissement actuel d’un "
  "mouvement historique, et il en tire trois séries de conséquences. La "
  "distinction conceptuelle d’abord, que le cours juge essentielle : la "
  "monnaie scripturale est la somme inscrite sur un compte bancaire, tandis "
  "que le support de monnaie scripturale est le moyen permettant de "
  "transférer cette somme, chèque, carte bancaire, application mobile, "
  "virement ou prélèvement. Confondre les deux conduit à prendre un instrument "
  "de paiement pour de la monnaie. Le cours affine en distinguant le compte "
  "courant, aussi appelé compte à vue ou dépôt à vue, dont l’individu peut "
  "récupérer la somme sans délai et sans coût, du compte rémunéré et du compte "
  "à terme, qui comportent un délai ; il note d’ailleurs que les chèques étant "
  "gratuits en France, les comptes courants n’y sont pas rémunérés. La "
  "dynamique historique ensuite : au début la valeur de la monnaie reposait "
  "sur les métaux, puis elle est devenue fiduciaire, puis scripturale, la "
  "tendance de l’histoire étant de toujours changer de forme de monnaie. Le "
  "débat contemporain enfin : on annonce la disparition des billets, et le "
  "cours expose les arguments des deux camps. Pour les banques, le passage à "
  "la monnaie scripturale réduit les coûts, produire des billets coûte cher et "
  "les distributeurs diminuent déjà ; il permet aussi de mieux tracer les "
  "transactions, le paiement en espèces étant le seul paiement anonyme, et met "
  "fin à la thésaurisation. Contre la suppression, le cours relève la fraude "
  "électronique, une loi de la zone euro prévoyant qu’on devrait pouvoir payer "
  "partout en espèces, notamment pour les touristes, auxquels les banques "
  "répondent par le cash back.",
  [("La monnaie comme écriture",
    "La monnaie bancaire n’est qu’un solde inscrit sur un compte : sa "
    "circulation ne consiste pas à déplacer un objet mais à modifier "
    "simultanément deux écritures, ce qui en fait une monnaie sans support "
    "matériel."),
   ("La distinction entre monnaie et support",
    "Chèque, carte, virement et prélèvement ne sont pas de la monnaie mais "
    "des moyens de la mobiliser : la même somme inscrite peut être transférée "
    "par plusieurs supports, dont le coût et la traçabilité diffèrent."),
   ("La hiérarchie des liquidités",
    "Le compte courant permet de récupérer la somme sans délai ni coût, alors "
    "que le compte rémunéré et le compte à terme imposent un délai : c’est "
    "cette gradation que les agrégats monétaires traduisent."),
   ("La dématérialisation cumulative",
    "Du métal au billet puis à l’écriture, chaque étape réduit la part de "
    "valeur intrinsèque et accroît celle de la confiance : la forme de la "
    "monnaie change, ses fonctions demeurent."),
   ("La traçabilité comme enjeu",
    "La monnaie scripturale laisse une trace que les espèces n’ont pas : le "
    "passage au scriptural réduit les coûts d’émission et rend les "
    "transactions suivables, ce qui en fait aussi un enjeu de liberté et de "
    "fraude.")],
  [{'a': "La monnaie scripturale réduit les coûts de la circulation "
         "monétaire, puisqu’elle évite la production et la distribution de "
         "billets.",
    'cond': "L’économie suppose une infrastructure de paiement fiable et un "
            "accès généralisé aux comptes bancaires.",
    'lim': "Le cours relève le risque de fraude électronique, qui déplace le "
           "coût de la sécurité plutôt qu’il ne le supprime."},
   {'a': "Distinguer la monnaie de son support évite une confusion fréquente "
         "et permet de comprendre les statistiques de paiement.",
    'cond': "La distinction n’est utile que si l’on dispose de données "
            "séparant le nombre d’opérations et les montants échangés.",
    'lim': "Elle ne tranche pas la question de savoir si certains supports "
           "nouveaux, comme les paiements par téléphone, créent des usages "
           "monétaires inédits ou se contentent de relayer les anciens."},
   {'a': "La domination du scriptural confirme que la monnaie se définit par "
         "ses fonctions et non par sa forme.",
    'cond': "Le raisonnement suppose que les trois fonctions soient "
            "effectivement remplies par une simple inscription comptable.",
    'lim': "Cette dématérialisation rend la monnaie entièrement dépendante du "
           "système bancaire et de sa solidité, ce que la monnaie fiduciaire "
           "ne faisait pas au même degré."},
   {'a': "Le maintien des espèces se justifie par des usages que le "
         "scriptural ne couvre pas, dont l’anonymat et l’accessibilité.",
    'cond': "L’argument suppose qu’une partie de la population ou des "
            "transactions reste effectivement mal servie par les paiements "
            "électroniques.",
    'lim': "Les banques répondent par le cash back, qui permet de payer plus "
           "que le montant facturé par carte afin que le commerçant rende la "
           "différence en billets."}],
  [{'t': "La monnaie scripturale est aujourd’hui la forme dominante de la "
         "monnaie, l’essentiel des transactions étant des virements et des "
         "prélèvements.",
    'qui': "Le constat du cours pour la zone euro, où elle atteint "
           "quatre-vingt-onze pour cent de la monnaie.",
    'rep': "Le cours nuance la portée de ce chiffre en distinguant nombre "
           "d’opérations et montants : les cartes dominent les opérations, les "
           "virements et prélèvements dominent les montants."},
   {'t': "Les billets vont disparaître, car le scriptural réduit les coûts et "
         "permet de tracer les transactions.",
    'qui': "La position des banques, telle que le cours la rapporte.",
    'rep': "Le cours objecte la fraude électronique et rappelle qu’une loi de "
           "la zone euro prévoit qu’on devrait pouvoir payer partout en "
           "espèces, le paiement en espèces étant par ailleurs le seul "
           "paiement anonyme."},
   {'t': "La monnaie se confond avec ses instruments de paiement, carte "
         "bancaire, chèque, virement ou prélèvement.",
    'qui': "La confusion courante que le cours entend dissiper.",
    'rep': "Le cours distingue la monnaie scripturale, somme inscrite sur un "
           "compte, et le support de monnaie scripturale, moyen utilisé pour "
           "transférer cette somme, ce qui montre que l’instrument n’est pas "
           "la monnaie."}],
  [{'n': "Irving Fisher",
    'i': "La quantité de monnaie, multipliée par sa vitesse de circulation, "
         "égale le niveau des prix multiplié par le volume des transactions.",
    'p': "Le cours mobilise son équation pour rappeler que la mesure de la "
         "masse monétaire est indissociable d’une hypothèse sur sa vitesse de "
         "circulation, question que la généralisation de la monnaie "
         "scripturale rend d’autant plus délicate."},
   {'n': "Paul Krugman",
    'i': "Les fonctions de la monnaie se dédoublent à l’échelle "
         "internationale selon qu’on se place du côté privé ou des banques "
         "centrales.",
    'p': "Le cours s’en sert pour rappeler que la forme scripturale n’enlève "
         "rien aux fonctions : le dollar joue ses six rôles internationaux "
         "principalement sous forme d’écritures, et non sous forme de "
         "billets."},
   {'n': "Christine Lagarde",
    'i': "Les économies contemporaines traversent une succession constante de "
         "crises inédites majeures.",
    'p': "Le cours ouvre sur ce diagnostic de permacrises, qui donne son "
         "enjeu à la question du support monétaire : une monnaie entièrement "
         "scripturale fait dépendre les paiements de la continuité du système "
         "bancaire et de ses infrastructures."}],
  [{'f': "Dans la zone euro, quatre-vingt-onze pour cent de la monnaie est "
         "scripturale, et les paiements par téléphone représentent désormais "
         "quinze pour cent des paiements.",
    'p': "Les deux chiffres montrent que la dématérialisation se poursuit à "
         "l’intérieur même du scriptural, par le renouvellement de ses "
         "supports."},
   {'f': "En 2020 en France, les cartes de paiement représentent "
         "cinquante-six virgule six pour cent des opérations mais seulement un "
         "virgule six pour cent des montants, tandis que virements et "
         "prélèvements font environ trente-sept pour cent des opérations et "
         "près de quatre-vingt-dix-sept pour cent des montants.",
    'p': "L’écart démontre qu’il faut distinguer le nombre d’opérations des "
         "montants échangés : les instruments du quotidien ne sont pas ceux "
         "qui portent la masse des règlements."},
   {'f': "En France, un individu peut payer jusqu’à mille euros en liquide et "
         "le commerçant a le droit de refuser un chèque.",
    'p': "Ces règles montrent que les supports n’ont pas le même statut "
         "juridique, alors qu’ils mobilisent la même monnaie inscrite en "
         "compte."}],
  [{'q': "Qu’est-ce que la monnaie bancaire ?",
    'f': "Une écriture, et non un objet. Le cours définit la monnaie "
         "scripturale comme la somme inscrite sur un compte bancaire, et "
         "insiste sur la distinction avec son support, c’est-à-dire le moyen "
         "utilisé pour transférer cette somme. Une carte bancaire n’est donc "
         "pas de la monnaie : elle est l’instrument qui permet d’en disposer.",
    'r': "Le raisonnement sépare l’actif monétaire de l’instrument de "
         "transfert, ce qui permet de lire correctement les statistiques de "
         "paiement et d’éviter une confusion courante.",
    'ex': "Chèque, carte bancaire, application mobile, virement et "
          "prélèvement sont des supports selon le cours."},
   {'q': "Faut-il supprimer les billets ?",
    'f': "Les arguments des banques sont réels : produire des billets coûte "
         "cher, le scriptural réduit les coûts, permet de mieux tracer les "
         "transactions et met fin à la thésaurisation. Mais le cours oppose la "
         "fraude électronique, une loi de la zone euro garantissant la "
         "possibilité de payer partout en espèces, et le fait que le paiement "
         "en espèces est le seul paiement anonyme.",
    'r': "On met en balance une économie de coûts mesurable et des usages "
         "difficilement substituables, ce qui conduit à un arbitrage et non à "
         "une solution évidente.",
    'ex': "Les banques répondent à la baisse du nombre de distributeurs par "
          "le cash back chez les commerçants."},
   {'q': "La monnaie a-t-elle changé de nature en se dématérialisant ?",
    'f': "Non, mais elle a changé de fondement. Le cours rappelle qu’au début "
         "la valeur de la monnaie reposait sur les métaux, puis qu’elle est "
         "devenue fiduciaire, puis scripturale, la tendance de l’histoire "
         "étant de toujours changer de forme. Les trois fonctions demeurent ; "
         "ce qui augmente à chaque étape, c’est la part de la confiance.",
    'r': "Le raisonnement sépare la permanence des fonctions de la "
         "transformation du support, et montre que la dématérialisation "
         "déplace la question vers les institutions qui garantissent la "
         "monnaie.",
    'ex': "Le mot fiduciaire vient du latin fiducia, qui signifie "
          "confiance."}],
  voisins=['n11-creation-monetaire', 'n11-liquidite', 'n11-confiance',
           'n11-banques-commerciales'])
