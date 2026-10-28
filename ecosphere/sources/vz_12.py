# -*- coding: utf-8 -*-
"""Visualisation 12 — Monnaie, banques et financement (type strates)."""

from vz_base import v, nd, ln

v('vz-financement', 'Monnaie, banques et financement de l’économie',
  'Chapitre 2 · quatre étages, de l’écriture comptable au risque systémique',
  'strates',
  "Tout part d’une écriture comptable : une banque crée la monnaie en "
  "inscrivant une somme au compte de son client. Cette visualisation monte "
  "les quatre étages qui en découlent — ce qu’est la monnaie, qui l’émet et "
  "la contrôle, comment l’économie se finance, et pourquoi ce système est "
  "structurellement fragile.",
  [("La formule à retenir",
    "Les crédits font les dépôts : la banque n’a pas besoin de dépôts "
    "préalables pour accorder un crédit. Tout le chapitre découle de cette "
    "inversion, y compris la question de savoir qui contrôle réellement la "
    "quantité de monnaie."),
   ("Ne pas confondre les deux oppositions",
    "Financement direct / indirect porte sur le canal — marché ou banque. "
    "Monnaie exogène / endogène porte sur l’origine de la création — décision "
    "de la banque centrale ou demande de crédit. Les deux débats sont "
    "indépendants."),
   ("La désintermédiation n’est pas une disparition",
    "Le cours propose de parler d’intermédiation de marché plutôt que de "
    "désintermédiation pure : les marchés prennent de l’importance mais les "
    "banques restent centrales, ce qui complique l’analyse des risques.")],
  [
   # -------------------------------------------------- 1. ce qu’est la monnaie
   nd('monnaie', 'Les trois fonctions de la monnaie', 'coeur',
      "Unité de compte, intermédiaire des échanges, réserve de valeur. Un "
      "actif liquide : utilisable immédiatement, sans délai ni perte de "
      "valeur.",
      grp=1,
      defi="La monnaie est un actif liquide qui sert à l’évaluation et au "
           "règlement des échanges. Le cours lui attribue trois fonctions : "
           "unité de compte, intermédiaire des échanges et réserve de valeur. "
           "Actif liquide signifie qu’elle peut être utilisée immédiatement "
           "pour acheter des biens ou des services, sans délai ni perte de "
           "valeur. La définition est fonctionnelle : elle est indépendante "
           "du support.",
      mec=[("L’unité de compte",
            "La monnaie fournit l’étalon qui rend les biens comparables : "
            "sans elle, il faudrait connaître autant de rapports d’échange "
            "qu’il existe de couples de biens."),
           ("L’intermédiaire des échanges",
            "Elle supprime la nécessité d’une double coïncidence des besoins "
            "qu’impose le troc : chacun peut vendre à l’un et acheter à "
            "l’autre."),
           ("La réserve de valeur",
            "Elle permet de différer un achat en conservant un pouvoir "
            "d’achat. C’est la fonction la plus fragile : elle suppose une "
            "valeur stable, donc la confiance.")],
      faits=[{'f': "Dans la zone euro, quatre-vingt-onze pour cent de la "
                   "monnaie est de la monnaie scripturale, l’essentiel des "
                   "transactions étant des virements et des prélèvements.",
              'p': "Le chiffre montre que les fonctions de la monnaie sont "
                   "aujourd’hui assurées par des écritures comptables, ce qui "
                   "confirme que la définition fonctionnelle est indépendante "
                   "du support."},
             {'f': "Le nombre total de bitcoins est limité à vingt-et-un "
                   "millions, dont dix-neuf virgule huit millions déjà "
                   "produits, et son cours dépend uniquement de l’offre et de "
                   "la demande.",
              'p': "Cette masse fixe et cette volatilité expliquent l’échec "
                   "de la fonction de réserve de valeur : un actif dont le "
                   "prix varie fortement ne conserve pas le pouvoir d’achat."}],
      aut=[{'n': "Satoshi Nakamoto",
            'i': "Le Bitcoin a été conçu pour permettre des transactions sans "
                 "banques ni États, par une technologie décentralisée."}],
      termes=['fonctions de la monnaie', 'monnaie scripturale', 'liquidite'],
      dos=['n11-fonctions-monnaie', 'n11-confiance']),

   nd('creation', 'Les crédits font les dépôts', 'pilier',
      "La banque n’a pas besoin de dépôts préalables : elle monétise une "
      "créance en inscrivant la somme au compte du client.",
      grp=1,
      defi="La création monétaire est la transformation de créances sur les "
           "agents non bancaires en moyens de paiement immédiatement "
           "utilisables : le cours parle de monétisation d’une créance. Sa "
           "formule centrale est que les crédits font les dépôts, "
           "c’est-à-dire que la banque n’a pas besoin de dépôts préalables "
           "pour accorder un crédit.",
      mec=[("La monétisation par simple écriture",
            "Une banque prêtant cinquante mille euros crée la monnaie au "
            "moment du prêt, en inscrivant la somme sur le compte du client : "
            "la monnaie apparaît avec la créance."),
           ("Les trois contreparties de la masse monétaire",
            "Créances sur l’économie, créances sur l’étranger, créances sur "
            "le Trésor public : chaque euro en circulation peut être "
            "rattaché à l’opération qui l’a créé."),
           ("La destruction symétrique",
            "Le remboursement du crédit détruit la monnaie créée : la masse "
            "monétaire est un solde entre créations et remboursements, non un "
            "stock administré.")],
      opp=[{'t': "L’offre de monnaie dépend des autorités monétaires : la "
                 "monnaie est exogène.",
            'qui': "Milton Friedman",
            'rep': "Keynes soutient à l’inverse que la quantité de monnaie "
                   "dépend de la demande de crédit dans l’économie et non "
                   "d’une décision de la banque centrale : c’est l’opposition "
                   "entre monnaie exogène et monnaie endogène."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "La quantité de monnaie dépend de la demande de crédit dans "
                 "l’économie et non d’une décision de la banque centrale."},
           {'n': "John Law",
            'i': "Son système repose sur un circuit où l’émission de billets "
                 "alimente l’achat d’actions qui ramène l’argent à la banque."}],
      termes=['creation monetaire', 'credits font les depots',
              'masse monetaire'],
      dos=['n11-creation-monetaire', 'n11-monnaie-bancaire']),

   # ------------------------------------------ 2. qui émet et qui contrôle
   nd('banques', 'Les banques commerciales', 'pilier',
      "Elles créent la monnaie, mais doivent se refinancer : c’est cette "
      "contrainte qui donne prise à la banque centrale.",
      grp=2,
      defi="Les banques commerciales sont les émetteurs effectifs de la "
           "monnaie scripturale. Leur pouvoir de création n’est pourtant pas "
           "illimité : elles doivent disposer de monnaie centrale pour "
           "assurer les retraits de leurs clients et régler leurs soldes avec "
           "les autres banques. C’est ce besoin de refinancement qui donne "
           "prise à la politique monétaire.",
      mec=[("Les fuites qui obligent à se refinancer",
            "Retraits en billets, règlements interbancaires et réserves "
            "obligatoires imposent à la banque de détenir de la monnaie "
            "centrale : elle doit l’emprunter à la banque centrale ou aux "
            "autres banques."),
           ("Le coût du refinancement comme frein",
            "Plus le taux auquel la banque se refinance est élevé, plus le "
            "crédit qu’elle accorde doit être cher : c’est le canal par "
            "lequel le taux directeur se transmet à l’économie."),
           ("Le multiplicateur ou le diviseur",
            "Lire la relation dans un sens donne un multiplicateur — la "
            "monnaie centrale commande le crédit ; dans l’autre, un "
            "diviseur — le crédit accordé détermine le refinancement "
            "nécessaire. Le choix recouvre l’opposition exogène / endogène.")],
      args=[{'a': "La contrainte de refinancement explique que la banque "
                  "centrale puisse agir sur le volume du crédit sans "
                  "l’administrer directement.",
             'lim': "Lorsque les banques disposent de liquidités abondantes, "
                    "la contrainte cesse d’être mordante et le canal du taux "
                    "s’affaiblit, ce qui a justifié le recours à des "
                    "instruments non conventionnels."}],
      termes=['banques commerciales', 'refinancement',
              'multiplicateur de credit'],
      dos=['n11-banques-commerciales', 'n11-multiplicateur-diviseur']),

   nd('bc', 'La banque centrale', 'pilier',
      "Trois missions : stabilité des prix avec une cible de 2 %, liquidité "
      "du système bancaire, prêteur en dernier ressort.",
      grp=2,
      defi="La banque centrale est l’institution qui émet la monnaie centrale "
           "et conduit la politique monétaire. Le cours résume le rôle de la "
           "Banque centrale européenne en trois missions : assurer la "
           "stabilité des prix, objectif principal, avec une cible "
           "d’inflation de deux pour cent ; assurer la liquidité du système "
           "bancaire ; agir comme prêteur en dernier ressort en cas de crise "
           "des banques.",
      mec=[("Le corridor des taux directeurs",
            "Facilité de dépôt comme taux plancher, facilité de prêt comme "
            "taux plafond, taux de refinancement à une semaine comme "
            "principal signal : la banque centrale ne fixe pas directement "
            "les taux du marché, elle en borne l’intervalle."),
           ("Les instruments non conventionnels",
            "Après 2008 : quantitative easing par achats massifs "
            "d’obligations publiques et privées, qualitative easing modifiant "
            "la composition du bilan, taux négatifs sur la facilité de dépôt. "
            "La banque centrale agit désormais sur les bilans et les "
            "anticipations, et non plus seulement sur le prix de la monnaie."),
           ("Le prêteur en dernier ressort",
            "Elle doit éviter crises bancaires, paniques de liquidité, "
            "blocage du crédit, faillites systémiques et emballements "
            "spéculatifs : cinq risques identifiés, dont chacun appelle un "
            "instrument propre.")],
      aut=[{'n': "Éric Monnet",
            'i': "La banque centrale contemporaine tend à devenir un acteur "
                 "plus large de la gouvernance économique."},
           {'n': "Milton Friedman",
            'i': "La banque centrale doit se contenter de contrôler la "
                 "croissance de la masse monétaire selon une règle simple."},
           {'n': "Stephanie Kelton",
            'i': "Un État souverain monétairement n’est pas soumis à une "
                 "contrainte financière pour sa dépense publique."}],
      termes=['banque centrale', 'taux directeurs', 'politique monetaire',
              'quantitative easing'],
      dos=['n11-banque-centrale', 'n11-preteur-dernier-ressort',
           'n11-independance-bc']),

   # ------------------------------------------- 3. comment on se finance
   nd('besoin', 'Besoins et capacités de financement', 'detail',
      "Certains agents dépensent plus qu’ils ne gagnent, d’autres moins : le "
      "système financier met les seconds en relation avec les premiers.",
      grp=3,
      defi="Un agent est en besoin de financement lorsque ses dépenses "
           "excèdent ses ressources, en capacité de financement dans le cas "
           "inverse. Le financement de l’économie consiste à mettre les "
           "seconds en relation avec les premiers. Lorsqu’une entreprise "
           "finance son investissement sur ses propres ressources, on parle "
           "d’autofinancement : le partage de la valeur ajoutée commande "
           "alors directement sa capacité à investir sans s’endetter.",
      mec=[("L’autofinancement comme première ressource",
            "Lorsque l’excédent brut d’exploitation est suffisant, "
            "l’entreprise peut financer son investissement elle-même ; sinon "
            "elle recourt à l’endettement ou au marché."),
           ("Le recours au financement externe",
            "L’agent en besoin de financement peut emprunter auprès d’une "
            "banque ou émettre des titres : c’est le choix entre financement "
            "indirect et financement direct.")],
      args=[{'a': "Raisonner en besoins et capacités permet de relier le "
                  "partage de la valeur ajoutée, l’épargne des ménages et le "
                  "déficit public dans un même cadre comptable.",
             'lim': "Le cadre est comptable : il décrit qui finance qui, non "
                    "si le financement se dirige vers les emplois les plus "
                    "productifs."}],
      termes=['besoin de financement', 'capacite de financement',
              'autofinancement'],
      dos=['n12-besoin-capacite', 'n12-autofinancement']),

   nd('canaux', 'Financement direct ou indirect', 'pilier',
      "La banque s’interpose, ou le marché met en relation. D’une économie "
      "d’endettement à une économie de marchés financiers.",
      grp=3,
      defi="Le financement indirect, ou intermédié, est assuré principalement "
           "par les banques, qui s’interposent entre prêteurs et emprunteurs. "
           "Le financement direct est assuré par les marchés financiers, via "
           "l’émission et l’échange de titres. Le cours oppose classiquement, "
           "à la suite de John Hicks, une économie d’endettement dominée par "
           "le crédit bancaire et une économie de marchés financiers.",
      mec=[("Ce que fait l’intermédiaire",
            "La banque transforme des ressources courtes en emplois longs, "
            "mutualise le risque et produit l’information sur l’emprunteur : "
            "trois fonctions que le marché n’assure pas de la même manière."),
           ("Les conditions d’accès au marché",
            "Pour être cotée, une entreprise doit généralement être une "
            "société anonyme, fournir une information financière "
            "transparente, respecter des obligations de publication et "
            "accepter une surveillance : le financement direct n’est pas "
            "accessible à toutes."),
           ("L’intermédiation de marché",
            "Le cours propose de parler d’intermédiation de marché plutôt que "
            "de désintermédiation pure : les banques prêtent, achètent des "
            "titres, interviennent sur les marchés, titrisent et gèrent des "
            "portefeuilles.")],
      aut=[{'n': "John Hicks",
            'i': "L’économie passe d’un financement dominé par les banques à "
                 "un financement par émission de titres."},
           {'n': "John Maynard Keynes",
            'i': "La rencontre entre épargne et investissement n’est pas "
                 "automatique, les agents pouvant préférer la liquidité."}],
      faits=[{'f': "Le cours énumère ce que les banques continuent de faire "
                   "dans une économie de marchés financiers : prêter, acheter "
                   "des titres, intervenir sur les marchés, titriser, gérer "
                   "des portefeuilles.",
              'p': "L’énumération démontre que la désintermédiation n’est pas "
                   "une disparition des banques mais une transformation de "
                   "leur activité."}],
      termes=['financement direct', 'financement indirect',
              'intermediation', 'desintermediation'],
      dos=['n12-financement-direct-indirect', 'n12-intermediation',
           'n12-desintermediation']),

   nd('efficience', 'L’efficience des marchés, une hypothèse', 'detail',
      "Si le marché était efficace, le capital irait aux projets les plus "
      "productifs. Le cours l’énonce comme une hypothèse à tester.",
      grp=3, par='canaux',
      defi="L’efficience d’un marché financier désigne sa capacité à produire "
           "des prix qui reflètent correctement la valeur des actifs et à "
           "diriger les capitaux vers les emplois les plus productifs. Le "
           "cours l’énonce explicitement comme une hypothèse à tester : si le "
           "marché était parfaitement efficace, le capital irait "
           "naturellement vers les projets les plus productifs.",
      mec=[("L’efficience informationnelle",
            "Le prix est censé incorporer toute l’information disponible : "
            "c’est la condition pour qu’il serve de signal fiable aux "
            "décisions d’investissement."),
           ("L’opacité produite par l’innovation financière",
            "Les produits structurés sont construits à partir d’un panier "
            "mêlant des créances peu risquées et des créances très risquées, "
            "de sorte que l’investisseur ne voit plus la qualité réelle de ce "
            "qu’il achète."),
           ("La part non observable du système",
            "Le système bancaire parallèle est une finance de l’ombre, moins "
            "visible et parfois moins régulée : une part de la finance "
            "échappe par construction à la production d’information "
            "publique.")],
      opp=[{'t': "Si les marchés sont efficaces, l’allocation du capital est "
                 "optimale et l’intervention est superflue.",
            'qui': "hypothèse d’efficience allocative",
            'rep': "Le cours relève que dans de nombreux pays le capital est "
                   "mal distribué, l’innovation est freinée, les élites "
                   "captent les rentes et les droits de propriété sont "
                   "fragiles : le constat oblige à chercher l’explication "
                   "dans les institutions."}],
      aut=[{'n': "Douglass North",
            'i': "Les institutions sont les règles formelles et informelles "
                 "qui structurent les interactions humaines et réduisent "
                 "l’incertitude."}],
      termes=['efficience des marches', 'allocation de l epargne',
              'produits structures'],
      dos=['n12-efficience', 'n12-allocation-epargne']),

   # ----------------------------------------------- 4. pourquoi c’est fragile
   nd('financiarisation', 'La financiarisation', 'limite',
      "Désintermédiation, décloisonnement, déréglementation : une finance "
      "plus complexe, plus globale et plus risquée.",
      grp=4,
      defi="La financiarisation désigne la place croissante prise par la "
           "finance dans le fonctionnement des économies. Le cours l’inscrit "
           "dans la globalisation financière, marquée par l’ouverture "
           "internationale des capitaux, la déréglementation, l’innovation "
           "financière, la montée de nouveaux acteurs et une instabilité "
           "accrue, et la résume par la règle des trois D : "
           "désintermédiation, décloisonnement, déréglementation.",
      mec=[("Le changement de nature, non de volume",
            "Le cours caractérise la finance depuis les années 2000 comme "
            "plus complexe, plus globale et plus risquée : la "
            "financiarisation n’est pas un simple accroissement quantitatif."),
           ("Le déplacement hors du périmètre régulé",
            "Le système bancaire parallèle réunit fonds monétaires, véhicules "
            "de titrisation, structures non bancaires et intermédiaires peu "
            "ou moins régulés : une part des fonctions bancaires s’est "
            "déplacée hors du champ de la surveillance.")],
      aut=[{'n': "Henri Bourguinat",
            'i': "La transformation financière des années 1980 repose sur la "
                 "désintermédiation, le décloisonnement et la "
                 "déréglementation."},
           {'n': "Milton Friedman",
            'i': "La seule responsabilité de l’entreprise est de maximiser le "
                 "profit pour ses actionnaires."}],
      faits=[{'f': "Le cours relève que les institutions trop grandes pour "
                   "faire faillite sont souvent perçues comme implicitement "
                   "protégées, les profits restant privés tandis que les "
                   "pertes peuvent être supportées par les banques centrales "
                   "et les États.",
              'p': "La concentration financière ajoute à la complexité un "
                   "problème de répartition : la financiarisation socialise "
                   "les pertes tout en privatisant les gains."}],
      termes=['financiarisation', 'globalisation financiere',
              'shadow banking'],
      dos=['n12-financiarisation', 'n12-marches-financiers']),

   nd('instabilite', 'Bulles, spéculation et contagion', 'limite',
      "Le prix cesse de refléter la valeur, la défiance se propage d’un "
      "établissement à l’autre, et le risque devient systémique.",
      grp=4,
      defi="L’instabilité financière désigne la tendance du système à "
           "produire des écarts cumulatifs entre les prix des actifs et leur "
           "valeur fondamentale, puis des retournements brutaux. Une bulle se "
           "forme lorsque l’achat est motivé par l’anticipation d’une hausse "
           "plutôt que par le rendement attendu de l’actif ; le retournement "
           "transforme un problème de prix en problème de solvabilité, qui se "
           "propage par les engagements croisés entre établissements.",
      mec=[("La dynamique auto-entretenue de la bulle",
            "Chacun achète parce que le prix monte, et le prix monte parce "
            "que chacun achète : l’anticipation se valide elle-même tant que "
            "de nouveaux acheteurs entrent."),
           ("Le passage de la liquidité à la solvabilité",
            "Au retournement, les actifs ne trouvent plus preneur à leur prix "
            "affiché : un établissement qui devait vendre pour se refinancer "
            "devient insolvable, sans qu’aucune perte réelle n’ait encore été "
            "constatée."),
           ("La contagion par les engagements croisés",
            "Les établissements se prêtent entre eux : la défaillance de l’un "
            "ampute l’actif des autres, et le doute suffit à tarir le marché "
            "interbancaire. C’est ce qui fait le caractère systémique du "
            "risque.")],
      aut=[{'n': "John Law",
            'i': "Un système fondé sur l’émission de billets et la "
                 "spéculation peut s’effondrer d’un seul coup."},
           {'n': "Henri Bourguinat",
            'i': "Le décloisonnement est l’un des trois D qui transforment "
                 "les marchés financiers depuis les années 1980."}],
      faits=[{'f': "Les actions de la Compagnie du Mississippi passent de "
                   "cent cinquante à quatre mille cent livres avant "
                   "l’éclatement de 1720.",
              'p': "Le chiffre donne l’ordre de grandeur d’une bulle : une "
                   "multiplication par plus de vingt-cinq sans transformation "
                   "équivalente de la valeur productive sous-jacente."},
             {'f': "La crise de 2008 débute par l’effondrement du marché des "
                   "subprimes et se transforme en crise bancaire, crise "
                   "boursière et récession mondiale.",
              'p': "L’enchaînement démontre la transmission de la sphère "
                   "financière à l’économie réelle, et la permanence du "
                   "mécanisme de 1720 sous des formes techniques entièrement "
                   "différentes."}],
      termes=['bulle financiere', 'speculation', 'risque systemique',
              'contagion'],
      dos=['n12-bulles', 'n13-risque-systemique',
           'n13-contagion-financiere']),

   nd('regulation', 'Réguler sans garantir', 'sortie',
      "Le sauvetage évite l’effondrement mais crée un aléa moral : protéger "
      "aujourd’hui encourage la prise de risque de demain.",
      grp=4,
      defi="La régulation financière cherche à contenir l’instabilité sans "
           "supprimer la fonction de financement. Elle se heurte à une "
           "tension propre : l’intervention du prêteur en dernier ressort "
           "est nécessaire pour éviter qu’une panique ne détruise des "
           "établissements solvables, mais elle crée un aléa moral en "
           "garantissant implicitement ceux que l’on juge trop grands pour "
           "faire faillite.",
      mec=[("L’intervention indispensable",
            "Sans prêteur en dernier ressort, une panique de liquidité "
            "détruit des banques solvables : la défaillance devient "
            "auto-réalisatrice, ce que la banque centrale a précisément pour "
            "mission d’empêcher."),
           ("L’aléa moral créé par le sauvetage",
            "Une institution qui anticipe d’être secourue prend davantage de "
            "risques : les profits restent privés tandis que les pertes "
            "peuvent être supportées par les banques centrales et les États."),
           ("La réponse par les exigences préalables",
            "Fonds propres, surveillance et encadrement des pratiques "
            "réduisent la probabilité d’un sauvetage plutôt qu’ils "
            "n’interdisent de l’accorder : on agit en amont faute de pouvoir "
            "renoncer en aval.")],
      args=[{'a': "Réguler en amont permet de conserver le filet de sécurité "
                  "sans en subir entièrement l’effet incitatif : c’est la "
                  "logique des exigences de fonds propres.",
             'lim': "Une part croissante de l’activité s’exerce hors du "
                    "périmètre régulé, dans le système bancaire parallèle : "
                    "la règle se déplace plus lentement que les activités "
                    "qu’elle vise."}],
      aut=[{'n': "Christine Lagarde",
            'i': "Les économies contemporaines connaissent une situation de "
                 "permacrises, succession constante de crises inédites "
                 "majeures."}],
      termes=['regulation financiere', 'alea moral', 'fonds propres',
              'prudentiel'],
      dos=['n12-regulation-financiere', 'n13-alea-moral-sauvetages']),
  ],
  [
   ln('monnaie', 'creation', 'est émise par',
      "Si la monnaie est définie par ses fonctions et non par son support, la "
      "question devient : qui l’émet ? La réponse du cours est directe — la "
      "banque, par monétisation d’une créance, et non par redistribution "
      "d’une épargne préexistante.", 'cause'),
   ln('creation', 'banques', 'est limitée par le refinancement de',
      "La banque crée la monnaie mais subit des fuites : retraits en billets, "
      "règlements interbancaires, réserves obligatoires. Elle doit détenir de "
      "la monnaie centrale, et c’est cette contrainte qui borne son pouvoir "
      "de création.", 'limite'),
   ln('banques', 'bc', 'dépend de',
      "Le besoin de refinancement donne prise à la politique monétaire : en "
      "fixant le taux auquel les banques se procurent la monnaie centrale, la "
      "banque centrale agit sur le coût du crédit sans l’administrer.",
      'conditionne'),
   ln('bc', 'creation', 'tente de piloter',
      "Tout le débat entre monnaie exogène et monnaie endogène se loge ici : "
      "la banque centrale commande-t-elle la quantité de monnaie, ou se "
      "borne-t-elle à en fixer le prix, la quantité résultant de la demande "
      "de crédit ?", 'oppose'),
   ln('creation', 'besoin', 'finance',
      "La monnaie créée par le crédit finance les agents en besoin de "
      "financement : c’est le point où l’analyse monétaire rejoint l’analyse "
      "du financement de l’économie réelle.", 'cause'),
   ln('besoin', 'canaux', 'se satisfait par',
      "L’agent en besoin de financement choisit entre emprunter auprès d’une "
      "banque et émettre des titres. Ce choix n’est pas libre : l’accès au "
      "marché suppose une taille, une forme juridique et une transparence "
      "que toutes les entreprises n’ont pas.", 'cause'),
   ln('canaux', 'efficience', 'suppose, côté marché,',
      "Le financement direct n’est préférable que si le prix des titres "
      "reflète correctement la valeur des actifs. L’efficience n’est donc pas "
      "une propriété constatée mais la condition sous laquelle le marché "
      "alloue mieux que la banque.", 'conditionne'),
   ln('banques', 'canaux', 'reste centrale dans',
      "La désintermédiation n’est pas une disparition : les banques prêtent, "
      "achètent des titres, titrisent et gèrent des portefeuilles. Le cours "
      "préfère parler d’intermédiation de marché.", 'renforce'),
   ln('canaux', 'financiarisation', 'se transforme en',
      "Les trois D — désintermédiation, décloisonnement, déréglementation — "
      "décrivent précisément le passage d’une économie d’endettement à une "
      "finance plus complexe, plus globale et plus risquée.", 'cause'),
   ln('efficience', 'instabilite', 'est démentie par',
      "L’opacité des produits structurés détruit l’information que les "
      "marchés sont censés produire : le prix cesse d’être un signal fiable, "
      "ce qui ouvre la voie aux écarts cumulatifs entre prix et valeur "
      "fondamentale.", 'limite'),
   ln('financiarisation', 'instabilite', 'amplifie',
      "Décloisonnement et innovation multiplient les engagements croisés "
      "entre établissements et entre places : un choc local se transmet plus "
      "vite et plus loin qu’auparavant.", 'cause'),
   ln('instabilite', 'bc', 'oblige à intervenir',
      "Une panique de liquidité détruit des banques solvables : c’est "
      "précisément pour l’empêcher que la banque centrale agit comme prêteur "
      "en dernier ressort, mission que le cours place au même rang que la "
      "stabilité des prix.", 'cause'),
   ln('instabilite', 'regulation', 'appelle',
      "La propagation par les engagements croisés rend la défaillance d’un "
      "établissement coûteuse pour tous : c’est le fondement de la régulation "
      "prudentielle, qui agit avant la crise plutôt qu’après.", 'cause'),
   ln('regulation', 'financiarisation', 'court après',
      "Une part croissante de l’activité s’exerce hors du périmètre régulé, "
      "dans le système bancaire parallèle : la règle se déplace plus "
      "lentement que les activités qu’elle vise.", 'limite'),
   ln('regulation', 'creation', 'encadre sans supprimer',
      "Le but n’est pas d’empêcher la création monétaire, qui finance "
      "l’économie, mais d’en limiter les excès : la régulation cherche le "
      "point où le crédit cesse d’être productif pour devenir "
      "déstabilisant.", 'conditionne'),
  ],
  bandes=[(1, 'Ce qu’est la monnaie'), (2, 'Qui l’émet, qui la contrôle'),
          (3, 'Comment l’économie se finance'),
          (4, 'Pourquoi le système est fragile')],
  fam='Monnaie, finance et crises')
