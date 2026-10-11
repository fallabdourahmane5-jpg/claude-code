# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 2 — Le financement de l'économie."""

R = {'2': {

 'q': "Comment la monnaie est-elle créée et pilotée, qui en détient réellement le pouvoir, et "
      "que révèle le passage d’un financement bancaire à un financement de marché sur la "
      "stabilité du système ?",

 'ess':
  "Le chapitre suit la monnaie du concept à la crise, et son fil conducteur est une question "
  "de pouvoir. On part des formes : la monnaie est un actif liquide fondé sur la confiance, "
  "de plus en plus dématérialisé — 91 % de scripturale en zone euro — et sa dimension "
  "internationale obéit aux six fonctions de Krugman, que seul le dollar remplit toutes. On "
  "passe ensuite à la création : « les crédits font les dépôts », ce qui ouvre l’affrontement "
  "central du chapitre entre multiplicateur (monnaie exogène, la banque centrale commande) et "
  "diviseur (monnaie endogène, la demande de crédit commande). Ce débat se prolonge dans la "
  "question de la neutralité : la monnaie n’est-elle qu’un voile, comme le soutiennent la "
  "théorie quantitative de Fisher puis Friedman, ou agit-elle sur le réel ? La courbe de "
  "Phillips et son effondrement dans la stagflation tranchent partiellement : la monnaie est "
  "puissante sur les prix, la politique monétaire impuissante sur le chômage durable. La "
  "troisième partie décrit l’arsenal — trois taux directeurs, un corridor, quatre canaux de "
  "transmission — puis sa rupture en 2008, quand la trappe à liquidité impose les politiques "
  "non conventionnelles. Le chapitre se referme sur la transformation du financement "
  "lui-même : de l’économie d’endettement de Hicks à l’économie de marchés financiers, "
  "transformée par les trois D de Bourguinat, et sur le prix payé — titrisation, opacité, "
  "aléa moral, risque systémique.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. Introduction : financer l’économie en régime de permacrises",
   'sp': [
    {'t': "A. Le cadre et les acteurs",
     'd': ["Le chapitre s’ouvre sur les institutions : Christine Lagarde à la tête de la "
           "Banque centrale européenne, François Villeroy de Galhau à la Banque de France, "
           "Jerome Powell à la Réserve fédérale américaine. Lagarde qualifie la période de "
           "permacrises : une succession constante de crises inédites majeures, autrement dit "
           "un régime où la crise n’est plus l’exception.",
           "Trois questions structurent la suite : comment ont évolué les formes de la "
           "monnaie, comment les courants économiques s’opposent sur sa nature, et comment le "
           "financement par le crédit bancaire a été progressivement concurrencé par d’autres "
           "canaux."]},
   ],
   'v': "Pour répondre, il faut commencer par ce qu’est la monnaie et par la manière dont ses "
        "formes se sont transformées."},

  # ----------------------------------------------------------------- II
  {'t': "II. Formes et fonctions de la monnaie",
   'sp': [
    {'t': "A. Ce qu’est la monnaie : un actif liquide fondé sur la confiance",
     'd': ["La monnaie est un actif liquide qui sert à l’évaluation et au règlement des "
           "échanges. Liquide signifie utilisable immédiatement, sans délai ni perte de "
           "valeur. Trois caractéristiques en découlent : c’est un actif, elle sert d’unité de "
           "compte pour mesurer la valeur des biens, et elle permet le règlement des échanges "
           "entre agents.",
           "Le cours insiste sur un double statut. La monnaie est un bien public : elle rend "
           "service à tous, facilite les échanges et génère des externalités positives, "
           "puisqu’en permettant le commerce elle stimule production, consommation et "
           "croissance. Elle est aussi un bien privé : chacun la détient et l’utilise pour son "
           "intérêt propre. Dans les deux cas, elle ne tient que par la confiance."]},
    {'t': "B. La dématérialisation : des métaux à la monnaie scripturale",
     'd': ["L’histoire monétaire est une suite de changements de forme : la valeur reposait "
           "d’abord sur les métaux, puis sur la monnaie fiduciaire — du latin fiducia, "
           "confiance —, et désormais sur la monnaie scripturale. Dans la zone euro, 91 % de "
           "la monnaie est scripturale, et les paiements par téléphone représentent déjà 15 % "
           "des paiements. En France, un particulier ne peut régler plus de 1 000 euros en "
           "liquide, et un commerçant peut refuser un chèque.",
           "Deux distinctions sont à tenir. D’abord entre la monnaie scripturale — la somme "
           "inscrite sur un compte — et ses supports, qui ne sont que des moyens de la "
           "transférer : chèque, carte bancaire, application mobile, virement, prélèvement. "
           "Ensuite entre les types de comptes : sur un compte courant, ou compte à vue, la "
           "somme est récupérable sans délai ni coût ; sur un compte rémunéré ou à terme, il y "
           "a un délai. En France, la gratuité des chèques a pour contrepartie la non-"
           "rémunération des comptes courants.",
           "Le débat sur la disparition des billets est explicitement posé. Pour les banques, "
           "le passage au scriptural réduit les coûts — fabrication des billets, entretien des "
           "distributeurs, déjà en diminution —, met fin à la thésaurisation et permet de "
           "tracer les transactions, l’espèce étant le seul paiement anonyme. Contre la "
           "suppression : la fraude électronique, et une règle de la zone euro selon laquelle "
           "on doit pouvoir payer partout en espèces, notamment pour les touristes ; les "
           "banques répondent par le cash back, qui permet de récupérer des billets chez le "
           "commerçant."]},
    {'t': "C. Ce que révèle la répartition des paiements",
     'd': ["Les données de 2020 en France donnent un résultat contre-intuitif qu’il faut "
           "savoir citer : les cartes de paiement représentent 56,6 % des opérations — 13,9 "
           "milliards sur 24,56 — mais seulement 1,6 % des montants — 578 milliards d’euros "
           "sur 35 592,7. À l’inverse, virements et prélèvements ne comptent que pour 37 % des "
           "opérations mais près de 97 % des montants échangés."],
     'lim': "La leçon de méthode est générale : compter les opérations ou compter les montants "
            "ne décrit pas le même système de paiement — le quotidien passe par la carte, "
            "l’essentiel de la valeur par le virement."},
    {'t': "D. Les agrégats monétaires : mesurer la masse monétaire par degré de liquidité",
     'd': ["La masse monétaire est la quantité totale de monnaie en circulation à un moment "
           "donné. Elle se mesure par des agrégats emboîtés du plus liquide au moins liquide : "
           "M1 regroupe les billets et les dépôts à vue ; M2 ajoute l’épargne de court terme "
           "(livrets, dépôts à terme) ; M3 ajoute les placements monétaires. Quand on dit que "
           "la banque centrale contrôle la masse monétaire, c’est M3 qui est visé.",
           "Les titres de créances négociables sont des actifs de court ou moyen terme "
           "permettant de se financer sur le marché monétaire plutôt que par crédit bancaire ; "
           "leur montant unitaire minimum est de 150 000 euros et les titres courts sont "
           "devenus les NeuCP en 2016. Trois catégories selon l’émetteur : certificats de "
           "dépôt pour les banques (1 jour à 1 an), billets de trésorerie pour les entreprises "
           "(1 jour à 1 an), bons du Trésor pour l’État (13 semaines à 5 ans).",
           "Les organismes de placement collectif en valeurs mobilières mutualisent l’épargne. "
           "Deux formes : le fonds commun de placement, créé en 1979, qui n’a pas de "
           "personnalité morale — l’investisseur est copropriétaire, porteur de parts — et la "
           "SICAV, société à capital variable dont l’investisseur est actionnaire. Les deux "
           "offrent une gestion professionnelle et une diversification du risque."]},
    {'t': "E. Des fonctions nationales aux fonctions internationales",
     'd': ["Les trois fonctions classiques remontent à Aristote (vers 350 avant J.-C.) : unité "
           "de compte, intermédiaire des échanges, réserve de valeur. Le billet a un pouvoir "
           "libératoire absolu : il permet d’éteindre une dette.",
           "Au niveau international, la livre sterling domine jusqu’en 1914, adossée à la "
           "Bourse de Londres. La Première Guerre mondiale endette fortement le Royaume-Uni et "
           "fait des États-Unis la nouvelle puissance : le dollar s’impose, surtout après 1945 "
           "avec Bretton Woods et le plan Marshall.",
           "Krugman définit six fonctions d’une monnaie internationale, réparties en deux "
           "points de vue. Pour le secteur privé : monnaie de libellé (les prix y sont "
           "exprimés — le pétrole est coté en dollars même entre un Européen et un Asiatique), "
           "monnaie véhiculaire (elle sert aux paiements internationaux — une entreprise "
           "française peut payer des produits chinois en dollars), monnaie d’investissement "
           "(on y place ses avoirs — obligations américaines). Pour les banques centrales : "
           "monnaie d’ancrage (le franc CFA est ancré à l’euro, le dollar de Hong Kong au "
           "dollar américain), monnaie d’intervention (pour agir sur le marché des changes), "
           "monnaie de réserve (pour détenir ses réserves officielles)."],
     'lim': "L’euro n’est que la deuxième monnaie internationale : le cours l’analyse comme "
            "une monnaie plutôt régionale, le dollar restant préféré pour sa stabilité, y "
            "compris pour l’endettement extérieur."},
    {'t': "F. L’euro : construction, institutions et objectif",
     'd': ["Avant l’euro existait le Système monétaire européen, dans lequel le cours des "
           "monnaies ne devait pas varier de plus de 2,5 % autour d’une référence, l’ECU. "
           "L’ECU n’était pas une vraie monnaie mais une unité de compte, moyenne pondérée des "
           "monnaies européennes. Le système n’a pas tenu : les banques centrales nationales "
           "ne parvenaient plus à stabiliser les parités.",
           "L’euro entre en vigueur en 1999, avec 15 pays à l’origine, 20 en 2025, 21 en 2026 "
           "avec l’entrée de la Bulgarie. Avant 1999, il existait quinze politiques monétaires "
           "distinctes ; désormais une seule, orchestrée par la BCE, dont les banques "
           "centrales nationales détiennent des parts. L’Eurosystème réunit la BCE et les "
           "banques centrales des pays ayant l’euro — Andorre utilise l’euro sans en faire "
           "partie, n’étant pas dans l’Union ; le Système européen de banques centrales ajoute "
           "les banques centrales des pays de l’Union hors zone euro.",
           "La BCE assure trois choses : la stabilité des prix, objectif principal, avec une "
           "cible d’inflation de 2 % ; la liquidité du système bancaire, qui permet aux "
           "banques commerciales d’accorder des crédits ; et le rôle de prêteur en dernier "
           "ressort en cas de crise bancaire."]},
    {'t': "G. Le change : régimes, risque et triangle de Mundell",
     'd': ["Le cours d’une monnaie est un prix : si 1 euro passe de 1,10 à 1,17 dollar, l’euro "
           "s’apprécie et le dollar se déprécie. Le vocabulaire distingue la dépréciation, "
           "baisse du cours en change flottant décidée par le marché, et la dévaluation, "
           "baisse décidée par l’État en change fixe. En régime fixe, la parité est fixée par "
           "l’État ou la banque centrale, ce qui apporte de la stabilité ; en régime flottant, "
           "elle varie selon l’offre et la demande, ce qui laisse à la banque centrale une "
           "politique monétaire indépendante mais crée de l’incertitude.",
           "Avant 1999, chaque pays avait sa monnaie, d’où un risque de change : si la monnaie "
           "se dépréciait les importations renchérissaient, si elle se réévaluait les "
           "exportations perdaient en compétitivité ; un agent détenant une devise dévaluée "
           "perdait de l’argent, ce qui dissuadait les échanges. Une appréciation de l’euro "
           "sert les importateurs européens et les exportateurs américains, et dessert les "
           "exportateurs européens et les importateurs américains : les intérêts des agents "
           "sont contradictoires. Le cours nuance toutefois : un produit sans substitut reste "
           "acheté malgré la hausse de son prix.",
           "Deux notions en découlent. La dépréciation compétitive, ou dumping monétaire, "
           "consiste à baisser volontairement la valeur de sa monnaie pour doper les "
           "exportations : c’est impossible à l’intérieur de la zone euro, puisque la monnaie "
           "est commune. Le choc asymétrique désigne un événement qui n’affecte pas également "
           "tous les pays d’une union monétaire — une récession en Espagne mais pas en "
           "Allemagne — alors qu’une seule politique monétaire s’applique à tous.",
           "Le triangle de Mundell (années 1960) formalise l’impossibilité : on ne peut cumuler "
           "libre circulation des capitaux, autonomie de la politique monétaire et stabilité "
           "du taux de change ; il faut en choisir deux. Autonomie plus liberté des capitaux "
           "donne un change flottant — le cas américain. Stabilité plus liberté des capitaux "
           "oblige à aligner ses taux sur le pays de référence, donc à renoncer à l’autonomie. "
           "Stabilité plus autonomie exige de contrôler les mouvements de capitaux — le cas "
           "chinois pendant longtemps."],
     'lim': "L’euro a supprimé le risque de change entre ses membres et rendu les prix "
            "transparents, mais ce risque s’est déplacé vers l’extérieur de la zone ; et une "
            "sortie de l’euro impliquerait une monnaie plus faible, des importations plus "
            "chères, une dette en devises plus lourde et une défiance des marchés."},
    {'t': "H. Les cryptomonnaies sont-elles des monnaies ?",
     'd': ["Le bitcoin naît en 2008, sous le pseudonyme de Satoshi Nakamoto, dans le "
           "prolongement direct de la crise financière : l’objectif est de se passer des "
           "banques et des États. Il repose sur la blockchain, registre numérique décentralisé "
           "où les transactions sont enregistrées et vérifiées par les utilisateurs, sans "
           "autorité centrale. Son émission est plafonnée à 21 millions d’unités, atteintes "
           "vers 2140, dont 19,8 millions déjà produites : sa masse est donc fixe, à l’inverse "
           "d’une monnaie classique. Son cours dépend uniquement de l’offre et de la demande, "
           "d’où une forte volatilité, et les transactions sont pseudonymes.",
           "Le test décisif est fonctionnel : le bitcoin ne remplit pas les trois fonctions de "
           "la monnaie. Il n’est pas unité de compte — les prix ne sont pas fixés en bitcoin — "
           "ni réellement moyen d’échange — très peu d’acteurs l’acceptent. Il ne repose sur "
           "aucune valeur sous-jacente : ni État, ni banque centrale, ni garantie, ni revenu. "
           "C’est donc un crypto-actif, un actif financier spéculatif, qu’on achète surtout "
           "dans l’espoir de le revendre plus cher."],
     'lim': "Sur le risque systémique, la réponse du cours est datée et conditionnelle : "
            "aujourd’hui non, car le bitcoin pèse peu dans le système financier, est surtout "
            "thésaurisé et les banques y sont peu exposées ; mais une adoption massive par les "
            "banques, les États ou les grandes entreprises rendrait un effondrement "
            "déstabilisant."},
   ],
   'v': "Les formes et les fonctions étant posées, reste la question décisive : d’où vient la "
        "monnaie ? Elle n’est pas donnée, elle est créée — et savoir par qui, c’est savoir qui "
        "détient le pouvoir monétaire."},

  # ---------------------------------------------------------------- III
  {'t': "III. La création monétaire : qui détient le pouvoir ?",
   'sp': [
    {'t': "A. Le précédent de John Law (1716-1720)",
     'd': ["La France est ruinée après les guerres de Louis XIV et manque de monnaie "
           "métallique. John Law propose de remplacer l’or par des billets pour relancer "
           "l’économie par la circulation et le crédit. Il crée en 1716 la Banque Générale, "
           "banque privée émettant des billets convertibles en or, qui devient Banque Royale "
           "en 1718 : l’État garantit alors les billets, qui deviennent monnaie officielle. "
           "En parallèle, la Compagnie du Mississippi exploite la Louisiane ; le public achète "
           "ses actions avec les billets de la Banque Royale, et le cours passe de 150 à "
           "4 100 livres.",
           "Le mécanisme est circulaire : la banque émet des billets, l’État rembourse ses "
           "dettes, les particuliers achètent des actions, l’argent revient à la banque qui "
           "émet de nouveaux billets — soit une création monétaire sans limite. En 1720, le "
           "système éclate : les porteurs veulent convertir leurs billets en or, la banque n’a "
           "plus de réserves, c’est la panique.",
           "Les conséquences dépassent la crise : ruine des épargnants, et hostilité durable "
           "des Français envers les banques et le papier-monnaie, d’où un retour prolongé à la "
           "monnaie métallique. Schumpeter rend pourtant hommage à Law, qu’il qualifie à la "
           "fois de monétariste et de pré-keynésien."],
     'lim': "La leçon est structurelle, pas anecdotique : la monnaie-papier ne tient que par "
            "la confiance, et la convertibilité promise devient intenable dès que tous "
            "l’exercent en même temps."},
    {'t': "B. Qui crée la monnaie : banques spécialisées et banques universelles",
     'd': ["La loi bancaire de 1945 impose aux banques de dépôt de travailler sur des "
           "échéances inférieures à deux ans : elles prêtent et empruntent à court terme et "
           "assurent la liquidité du système, les clients pouvant retirer à tout moment ; "
           "elles ne financent donc pas les projets longs. Les banques d’affaires prennent en "
           "charge placements et fusions-acquisitions.",
           "Les banques universelles — BNP Paribas, Société générale, Bank of America — "
           "exercent toutes les activités : dépôt, crédit, investissement. Le modèle apparaît "
           "en Allemagne au XIXᵉ siècle et se généralise en France dans les années 1980. "
           "Avantage : souplesse et rentabilité."],
     'lim': "Le risque est de liquidité et il est précis : la banque universelle finance des "
            "emplois longs avec des ressources courtes, de sorte qu’un retrait massif des "
            "déposants peut la mettre en difficulté — d’où la préférence de certains "
            "économistes pour une séparation des activités, argument réactivé après 2008."},
    {'t': "C. « Les crédits font les dépôts » : le mécanisme de base",
     'd': ["La monnaie est créée dans trois situations : quand une banque de second rang "
           "accorde un crédit à un ménage ou une entreprise ; quand un exportateur demande la "
           "conversion de ses devises en monnaie nationale ; quand une banque achète des "
           "obligations d’État — elle inscrit alors +10 millions à l’actif (les titres) et "
           "+10 millions au passif (le compte du Trésor crédité), sans avoir « sorti » un "
           "argent préexistant.",
           "D’où la formule centrale : les crédits font les dépôts. La banque n’a pas besoin "
           "de dépôts préalables pour prêter ; elle crée simultanément la monnaie et sa "
           "contrepartie. La création monétaire se définit alors comme la transformation de "
           "créances sur les agents non bancaires en moyens de paiement immédiatement "
           "utilisables — on parle de monétisation d’une créance. Autrement dit, la banque "
           "transforme une promesse de remboursement en argent disponible sur un compte.",
           "À chaque création correspond une contrepartie, c’est-à-dire l’actif détenu en face "
           "de la monnaie créée. Les contreparties de la masse monétaire sont au nombre de "
           "trois : créances sur l’économie (entreprises et ménages), créances sur l’étranger, "
           "créances sur le Trésor public."],
     'mec': "Crédit accordé → inscription simultanée au passif (dépôt) et à l’actif (créance) "
            "→ monnaie créée ; remboursement → destruction de monnaie."},
    {'t': "D. Première lecture : le multiplicateur de crédit et la monnaie exogène",
     'd': ["Le multiplicateur explique comment une base monétaire limitée engendre beaucoup "
           "plus de monnaie scripturale. L’idée : les banques prêtent ce qui leur reste après "
           "les retraits en billets. Avec un taux de fuite r = 20 %, un crédit initial de 100 "
           "laisse 80 dans la banque, qui peuvent être reprêtés ; la deuxième vague laisse 64, "
           "puis 51,2, et ainsi de suite. La suite géométrique converge : 100 de base "
           "monétaire produisent 500 de monnaie.",
           "Dans cette optique, la banque centrale contrôle la base monétaire — billets et "
           "réserves, soit M0 — et les banques de second rang sont contraintes par les "
           "retraits et les réserves obligatoires. La causalité va de la monnaie centrale vers "
           "la masse monétaire : MC → M. La monnaie est dite exogène, parce que sa quantité "
           "est décidée de l’extérieur de l’économie, par la banque centrale, et non par la "
           "demande de crédit."],
     'mec': "Base monétaire 100, fuite r = 20 % → 100 → 80 → 64 → 51,2 … → total 500 : "
            "multiplicateur = 1/r."},
    {'t': "E. Seconde lecture : le diviseur de crédit et la monnaie endogène",
     'd': ["La lecture keynésienne inverse la causalité : M → MC. Ce ne sont pas les banques "
           "centrales qui décident de la quantité de monnaie, mais la demande de crédit. Les "
           "banques commerciales prêtent d’abord et se refinancent ensuite.",
           "Le déroulé est en quatre temps. Un agent demande un crédit de 100 000 euros. La "
           "banque crédite immédiatement le compte — création monétaire — sans vérifier "
           "d’abord ses réserves. Elle regarde ensuite combien les clients retireront en "
           "billets et combien elle doit déposer en réserves obligatoires. Si elle manque de "
           "monnaie centrale, elle se la procure sur le marché interbancaire ou auprès de la "
           "banque centrale, qui la lui fournit presque toujours, parce qu’elle doit garantir "
           "la stabilité du système et le financement de l’économie.",
           "L’idée clé est que l’offre de monnaie s’adapte à la demande de crédit : la banque "
           "ne prête pas ce qu’elle a, elle prête ce que les agents veulent emprunter. Le "
           "ratio de réserves d est l’inverse du multiplicateur k.",
           "Cette divergence n’est pas née au XXᵉ siècle : dès le XIXᵉ, la Banking School et "
           "la Currency School s’opposaient sur le point de savoir si les billets émis "
           "devaient être intégralement couverts par les stocks d’or. On rattache la Banking "
           "School à Keynes — la monnaie doit s’adapter aux besoins de l’économie — et la "
           "Currency School aux monétaristes — sa quantité doit être strictement contrôlée par "
           "une autorité extérieure."],
     'lim': "La question que pose explicitement le cours est celle du pouvoir : la banque "
            "centrale contrôle la monnaie centrale, les banques commerciales créent la monnaie "
            "scripturale, et la masse monétaire dépend de la demande de crédit — ce qui "
            "relativise l’idée d’un contrôle direct de la quantité de monnaie."},
    {'t': "F. La monnaie n’est-elle qu’un voile ? Des classiques à Friedman",
     'd': ["Dire que la monnaie est un voile, c’est affirmer qu’elle n’a pas d’effet réel : "
           "elle facilite les échanges mais ne crée pas de richesse et n’influence pas la "
           "production. Trois auteurs fondent cette vision. Jean Bodin, au XVIᵉ siècle, "
           "observe que trop de monnaie produit de l’inflation : elle agit sur les prix, pas "
           "sur la production. Jean-Baptiste Say, avec la loi des débouchés, soutient que ce "
           "sont les biens qui paient les biens, la monnaie ne jouant aucun rôle actif. David "
           "Ricardo défend une vision strictement quantitative : plus de monnaie, seulement "
           "plus de prix. Avant le XXᵉ siècle, on ne reconnaissait d’ailleurs à la monnaie que "
           "deux fonctions, unité de compte et moyen d’échange, l’abondance produisant "
           "l’inflation et la pénurie la déflation.",
           "Irving Fisher formalise avec l’équation des échanges MV = PT : M la quantité de "
           "monnaie, V sa vitesse de circulation, P le niveau général des prix, T le volume "
           "des transactions. Sous l’hypothèse que V et T sont stables, toute hausse de M se "
           "traduit proportionnellement par une hausse de P. L’inflation est donc un phénomène "
           "monétaire.",
           "Friedman, dans La théorie quantitative de la monnaie, un nouvel énoncé (1956), "
           "modernise la thèse : la monnaie est exogène, l’inflation est toujours et partout "
           "un phénomène monétaire, et à long terme la monnaie est neutre — elle n’influence "
           "ni la production ni l’emploi. Il observe une relation stable entre agrégats "
           "monétaires et niveau des prix sur longue période, et suppose des anticipations "
           "adaptatives : les agents apprennent de l’inflation passée et ajustent leurs "
           "comportements — les salariés réclament des hausses, les entreprises relèvent leurs "
           "prix.",
           "Friedman concède pourtant un effet réel de court terme : une politique "
           "expansionniste fait baisser les taux, facilite le crédit, stimule investissement "
           "et consommation, donc la production, et fait reculer le chômage. Mais cette "
           "relation est instable, parce que les agents finissent par comprendre qu’il s’agit "
           "d’inflation : la production revient à son niveau initial, seule l’inflation "
           "subsiste. Il existe en outre un taux de chômage naturel, irréductible."],
     'mec': "MV = PT avec V et T stables → M ↑ entraîne P ↑ proportionnellement. Court terme : "
            "M ↑ → taux ↓ → crédit ↑ → production ↑ ; mais anticipations adaptatives → salaires "
            "et prix ↑ → retour au niveau initial.",
     'lim': "La formule à retenir est donc paradoxale : chez Friedman la monnaie est "
            "puissante, puisqu’elle détermine l’inflation, mais la politique monétaire est "
            "impuissante, puisque les agents anticipent — d’où sa règle de croissance "
            "monétaire à k %."},
    {'t': "G. La courbe de Phillips, la stagflation et la fin d’une illusion",
     'd': ["Le point de départ est keynésien : quand le chômage est faible, les salariés "
           "obtiennent des hausses de salaires, les coûts montent, les prix suivent — d’où une "
           "relation inverse entre chômage et inflation. En 1958, Alban W. Phillips observe "
           "cette relation entre taux de croissance des salaires nominaux et chômage au "
           "Royaume-Uni entre 1861 et 1957 ; la relation n’est ni linéaire ni stable, et la "
           "courbe coupe l’axe des abscisses en un point qui définit le NAWRU, taux de chômage "
           "pour lequel la croissance des salaires nominaux est nulle. Samuelson et Solow "
           "confirment la relation aux États-Unis. Les gouvernements des années 1960-1970 en "
           "tirent une politique : accepter un peu d’inflation pour réduire le chômage.",
           "Friedman conteste. À court terme, la courbe peut exister à cause de l’illusion "
           "monétaire : les salariés voient leur salaire nominal mais pas tout de suite la "
           "baisse de leur salaire réel, donc les entreprises embauchent. À long terme, "
           "l’illusion se dissipe : les salariés exigent des hausses nominales, les entreprises "
           "relèvent leurs prix, et le chômage revient à son niveau naturel. La courbe de "
           "Phillips devient verticale.",
           "Les années 1970 tranchent empiriquement. Lors du choc pétrolier, les coûts des "
           "firmes explosent, elles licencient : on obtient simultanément inflation et "
           "chômage. C’est la stagflation, qui détruit la relation de Phillips, puisque "
           "l’inflation n’a pas fait baisser le chômage. Les monétaristes y voient la "
           "confirmation de leur thèse : les agents ne sont plus victimes d’illusion "
           "monétaire, donc la politique monétaire ne fonctionne plus."],
     'lim': "La solution de Friedman est cohérente avec son diagnostic : laisser le chômage "
            "revenir à son niveau naturel et se contenter de contrôler la croissance de la "
            "masse monétaire."},
    {'t': "H. L’hélicoptère monétaire : une issue, et pourquoi elle est contestée",
     'd': ["Face à l’inefficacité des instruments traditionnels, Friedman évoque une solution "
           "radicale : créer de la monnaie et la distribuer directement aux agents non "
           "financiers, ménages ou État, sans passer par les banques commerciales. "
           "Contrairement au quantitative easing, la monnaie n’est pas injectée dans le système "
           "bancaire mais versée aux ménages ou affectée à une dépense publique, pour stimuler "
           "immédiatement la demande.",
           "L’intérêt est de contourner la trappe à liquidité : même avec des taux très bas, "
           "les banques n’accordent pas de crédits et les agents n’investissent pas, de sorte "
           "que la politique monétaire devient inefficace.",
           "Mais la mesure brouille la frontière entre politique monétaire et politique "
           "budgétaire. Donner de l’argent aux ménages revient à verser une allocation ou une "
           "prime : décider qui reçoit combien est une décision politique, pas monétaire. "
           "Donner de l’argent à l’État revient à monétiser la dette, ce que le droit "
           "européen interdit précisément pour éviter les dérives inflationnistes."],
     'lim': "Trois limites sont explicitement listées : la perte d’indépendance de la banque "
            "centrale, qui n’est plus crédible pour lutter contre l’inflation ; un aléa moral "
            "public, l’État n’ayant plus d’incitation à maîtriser son déficit ; et un risque "
            "inflationniste, la dépense n’ayant pas de contrepartie productive immédiate. "
            "L’hélicoptère monétaire reste donc une solution surtout théorique."},
   ],
   'v': "Si la création monétaire dépend largement du crédit bancaire, alors toute action sur "
        "les conditions de refinancement influence indirectement la monnaie, l’activité et les "
        "prix : c’est l’objet de la politique monétaire."},

  # ----------------------------------------------------------------- IV
  {'t': "IV. La politique monétaire : objectifs, instruments et rupture de 2008",
   'sp': [
    {'t': "A. La chaîne fondamentale et les trois objectifs",
     'd': ["La politique monétaire ne consiste pas seulement à fixer un taux : elle encadre "
           "les conditions générales de circulation de la monnaie. Sa chaîne de causalité est "
           "explicite : taux directeurs → conditions du crédit → création monétaire → demande "
           "globale → inflation et activité.",
           "Trois objectifs se superposent. La stabilité des prix d’abord : si le crédit "
           "progresse trop vite par rapport à la production, la masse monétaire augmente, la "
           "demande s’élève et des tensions inflationnistes apparaissent ; la BCE vise 2 % à "
           "moyen terme. Le soutien à la croissance ensuite : une baisse des taux rend le "
           "crédit moins cher, soutient investissement et consommation, donc la demande "
           "globale — mais cet objectif entre en tension avec le premier, d’où le dilemme "
           "classique entre relancer l’activité et maîtriser l’inflation. La stabilité "
           "financière enfin, devenue essentielle depuis 2008 : éviter les crises bancaires, "
           "les paniques de liquidité, le blocage du crédit, les faillites systémiques et les "
           "emballements spéculatifs, ce qui suppose d’être prêteur en dernier ressort.",
           "Depuis les années 2020, Éric Monnet (La Banque providence, 2021) soutient que les "
           "missions s’élargissent encore : accompagner la transition écologique, créer une "
           "monnaie numérique de banque centrale, prendre en charge la dette publique. La "
           "banque centrale devient un acteur plus large de la gouvernance économique, qu’il "
           "propose de démocratiser. Dans le même mouvement, la théorie monétaire moderne — "
           "héritée d’Abba Lerner (1943), popularisée par Stephanie Kelton (Le mythe du "
           "déficit, 2021) — affirme qu’un État souverain monétairement n’a pas de contrainte "
           "financière, le seul blocage possible étant réel : le pays doit disposer des "
           "ressources en main-d’œuvre, en capacités de production et en matières premières "
           "pour que la création monétaire ne se traduise pas en inflation."],
     'lim': "Être prêteur en dernier ressort crée un aléa moral : si les acteurs savent qu’ils "
            "seront secourus, ils peuvent adopter des comportements imprudents."},
    {'t': "B. Les instruments conventionnels : trois taux et un corridor",
     'd': ["Avant 2008, dans un contexte de faible inflation, la politique monétaire repose "
           "sur la variation des taux directeurs, qui influence le marché interbancaire, les "
           "taux bancaires, le coût du crédit, la création monétaire, la demande globale et "
           "l’inflation. Elle agit principalement par le canal du crédit bancaire.",
           "Trois taux structurent le système. Le taux de facilité de dépôt rémunère les "
           "liquidités que les banques placent auprès de la banque centrale : c’est le taux "
           "plancher, car s’il est élevé les banques préfèrent placer plutôt que prêter. Le "
           "taux de facilité de prêt est celui auquel elles empruntent à très court terme : "
           "c’est le taux plafond, qui borne le coût maximal du refinancement. Entre les deux, "
           "le taux de refinancement, sur une semaine, constitue le principal signal monétaire.",
           "Les deux facilités forment le corridor des taux directeurs, à l’intérieur duquel "
           "évoluent les taux du marché interbancaire — l’EONIA, remplacé par l’€STR. Ce "
           "corridor oriente les échanges de liquidités entre banques, stabilise le marché "
           "interbancaire et transmet efficacement la politique monétaire. S’y ajoutent les "
           "réserves obligatoires, fraction des dépôts à conserver à la banque centrale, et "
           "les opérations d’open market, achats ou ventes de titres."],
     'mec': "Baisse des taux directeurs → baisse de l’€STR → baisse du coût de refinancement "
            "des banques → baisse des taux débiteurs → hausse de la demande de crédit → hausse "
            "de la création monétaire."},
    {'t': "C. Les quatre canaux de transmission",
     'd': ["Le canal des taux d’intérêt est le plus classique : taux ↓ → crédit ↑ → monnaie ↑ "
           "→ demande ↑ → inflation potentielle ↑. Le canal du prix des actifs passe par la "
           "valorisation : quand les taux baissent, les obligations déjà émises deviennent "
           "plus attractives, leur prix monte, et les détenteurs d’actifs se sentent plus "
           "riches — c’est un effet de richesse, proche de l’effet Pigou dans sa logique "
           "patrimoniale, qui soutient consommation et investissement.",
           "Le canal des anticipations, ou forward guidance, fait de la communication un "
           "instrument : en annonçant l’orientation future des taux, la banque centrale "
           "rassure les marchés, réduit l’incertitude, encourage l’investissement et ancre les "
           "anticipations d’inflation. Le canal du taux de change joue en économie ouverte : "
           "des taux plus élevés attirent les capitaux étrangers, la monnaie s’apprécie et les "
           "exportations perdent en compétitivité ; des taux plus bas la font se déprécier et "
           "améliorent la compétitivité extérieure."],
     'lim': "Raisonner sur un seul canal est la faute la plus fréquente : une hausse des taux "
            "agit simultanément sur le crédit, le patrimoine, les anticipations et le change, "
            "et ces effets peuvent se contrarier."},
    {'t': "D. 2008 : la trappe à liquidité et les politiques non conventionnelles",
     'd': ["La crise de 2008 est immobilière, bancaire, financière puis économique. Elle "
           "provoque une chute de la confiance, un blocage du crédit, l’effondrement de "
           "certains actifs, une récession et une montée du chômage.",
           "Après avoir fortement baissé leurs taux, les banques centrales se heurtent à la "
           "trappe à liquidité : les taux sont déjà très bas, les agents préfèrent conserver "
           "des liquidités, les banques restent prudentes, l’investissement ne repart pas. "
           "Baisser encore les taux ne suffit plus.",
           "D’où les politiques monétaires non conventionnelles, dont les objectifs sont de "
           "rétablir la liquidité, débloquer le crédit, éviter la déflation, stabiliser les "
           "marchés et soutenir l’activité. Le quantitative easing consiste en achats massifs "
           "de titres, publics et privés : il injecte de la liquidité, fait monter le prix des "
           "titres, baisser les taux à moyen et long terme, soutient le crédit et "
           "l’investissement et lutte contre la déflation — la banque centrale augmente la "
           "taille de son bilan. Le qualitative easing en modifie la composition plutôt que la "
           "taille : achat d’actifs plus risqués contre des titres moins risqués revendus, "
           "élargissement des garanties acceptées, réallocation de portefeuille. Les taux "
           "négatifs, appliqués surtout à la facilité de dépôt, visent à dissuader les banques "
           "de thésauriser leurs liquidités et à les pousser à prêter ; ils ciblent les "
           "banques, non directement les ménages. S’y ajoutent les prêts de long terme aux "
           "banques, LTRO et TLTRO, parfois ciblés."],
     'lim': "La limite centrale de ces politiques est l’aléa moral : en garantissant la "
            "liquidité et en soutenant les prix d’actifs, la banque centrale peut encourager "
            "des comportements imprudents."},
   ],
   'v': "La banque centrale a pris tant de place parce que le mode de financement de "
        "l’économie s’était lui-même transformé : il faut donc examiner le passage du crédit "
        "bancaire aux marchés de capitaux."},

  # ------------------------------------------------------------------ V
  {'t': "V. D’une économie d’endettement à une économie de marchés financiers",
   'sp': [
    {'t': "A. Financement intermédié et financement direct",
     'd': ["Le financement peut être intermédié, assuré principalement par les banques qui "
           "s’interposent entre prêteurs et emprunteurs, ou direct, assuré par les marchés "
           "financiers via l’émission et l’échange de titres. L’analyse a longtemps opposé une "
           "économie d’endettement, dominée par le crédit bancaire, à une économie de marchés "
           "financiers, où les agents se financent sur les marchés de capitaux.",
           "Le marché monétaire finance le court terme, le marché financier le moyen et long "
           "terme ; le marché primaire est celui de l’émission — le « marché du neuf » —, le "
           "marché secondaire celui des titres déjà émis, et c’est lui qui assure la liquidité."]},
    {'t': "B. Pourquoi détenir des titres : revenu, plus-value, spéculation",
     'd': ["Trois motifs. Le revenu d’abord : une obligation est un titre de créance qui "
           "procure des revenus fixes, les coupons ; une action est un titre de propriété qui "
           "procure des revenus variables, les dividendes, et donne un droit de vote en "
           "assemblée générale. La plus-value ensuite : on achète pour revendre plus cher. La "
           "spéculation enfin, qui peut jouer à la hausse — acheter aujourd’hui pour revendre "
           "demain — ou à la baisse, en pariant sur la chute d’un actif par la vente à "
           "découvert, les marchés à terme ou les produits dérivés.",
           "Le marché ne sert donc pas seulement à financer : il sert aussi à arbitrer, à "
           "couvrir des risques et à spéculer."]},
    {'t': "C. Les types de marchés et la Bourse",
     'd': ["Le marché au comptant correspond à une transaction immédiate, paiement et "
           "livraison étant proches dans le temps. Le marché à terme conclut aujourd’hui une "
           "opération exécutée plus tard, à un prix fixé à l’avance : il sert à se couvrir "
           "contre le risque, à anticiper l’évolution des prix et à spéculer. Le marché de gré "
           "à gré, ou OTC, n’est pas centralisé : négociation bilatérale, pas nécessairement "
           "de place boursière organisée, moins de transparence, plus de souplesse, et "
           "souvent plus de risque systémique. Le service de règlement différé permet de "
           "différer le règlement d’une opération, ce qui crée un effet de levier et facilite "
           "la prise de position sans paiement immédiat intégral.",
           "La Bourse est l’institution centrale : elle permet l’émission de titres, organise "
           "leur cotation, assure la liquidité des actifs, fait se rencontrer offreurs et "
           "demandeurs de capitaux et produit une information de prix. Repères historiques : "
           "la Bourse de Paris est créée en 1724 ; en 2000 elle fusionne avec Amsterdam et "
           "Bruxelles pour former Euronext, rejoint en 2002 par Lisbonne, le LIFFE londonien "
           "des produits dérivés et Athènes — soit une concentration et une "
           "internationalisation des marchés. Pour être cotée, une entreprise doit "
           "généralement être une société anonyme, fournir une information financière "
           "transparente, respecter des obligations de publication et accepter la surveillance "
           "des marchés."]},
    {'t': "D. La thèse de Hicks et sa nuance contemporaine",
     'd': ["John Hicks théorise le basculement d’une économie d’endettement — financement "
           "dominé par les banques, rôle central du crédit, forte intermédiation — vers une "
           "économie de marchés financiers — financement croissant par émission de titres, "
           "rôle accru des marchés de capitaux et des investisseurs.",
           "Le cours nuance explicitement : les banques n’ont pas disparu. Elles prêtent "
           "toujours, mais achètent aussi des titres, interviennent sur les marchés, "
           "titrisent, gèrent des portefeuilles. On parle donc plutôt d’intermédiation de "
           "marché : les marchés prennent de l’importance, mais les banques restent centrales "
           "et interviennent elles-mêmes de plus en plus par les marchés."],
     'lim': "Le passage à l’économie de marchés financiers n’est pas la disparition du système "
            "bancaire, mais une transformation des modalités de financement — formulation à "
            "reprendre telle quelle pour éviter le contresens."},
    {'t': "E. Les trois D de Bourguinat et la finance d’après 2000",
     'd': ["Henri Bourguinat, dans Les vertiges de la finance internationale (1987), résume la "
           "transformation des marchés depuis les années 1980 par trois D : déréglementation, "
           "décloisonnement, désintermédiation. Elle s’inscrit dans la globalisation "
           "financière — ouverture internationale des capitaux, innovation financière, montée "
           "de nouveaux acteurs, instabilité accrue.",
           "Depuis les années 2000, la finance devient plus complexe, plus globale et plus "
           "risquée. Les marchés de gré à gré se développent pour leur souplesse, leurs "
           "produits sur mesure, leur rapidité et le contournement partiel des contraintes des "
           "marchés organisés — mais ils sont plus difficiles à surveiller. Le shadow banking "
           "désigne les activités de financement réalisées hors du système bancaire "
           "traditionnel ou à sa périphérie — fonds monétaires, véhicules de titrisation, "
           "intermédiaires peu régulés — qui créent de la liquidité, transforment les "
           "maturités et prennent des risques proches de ceux des banques sans être soumis aux "
           "mêmes règles prudentielles."]},
    {'t': "F. Titrisation, CDO, CDS : la dispersion du risque",
     'd': ["La titrisation transforme des créances, souvent bancaires, en titres négociables : "
           "la banque regroupe ses prêts immobiliers, les cède à un véhicule financier qui "
           "émet des titres vendus à des investisseurs. Elle permet de sortir des créances du "
           "bilan, de récupérer des liquidités, de transférer le risque et de financer de "
           "nouveaux crédits. Avantage : plus de liquidité et de capacité de financement. "
           "Risque : dilution de la responsabilité, lisibilité moindre du risque, formation de "
           "bulles — ce qui s’est produit en 2007-2008.",
           "Les CDO sont construits à partir d’un panier de dettes — crédits immobiliers, "
           "prêts bancaires, autres créances — transformées en titres négociables. Leur danger "
           "tient à deux effets : l’opacité, car le panier mélange des créances peu risquées "
           "et très risquées, si bien que l’investisseur ne voit plus la qualité réelle de ce "
           "qu’il achète ; et la diffusion mondiale du risque, puisqu’ils sont vendus partout, "
           "de sorte qu’une hausse des défauts propage la crise très vite.",
           "Les CDS sont des produits dérivés jouant le rôle d’assurance : le détenteur d’une "
           "créance paie une prime et se fait indemniser en cas de défaut. Le problème est "
           "qu’on peut acheter un CDS sans détenir l’obligation, donc parier sur la faillite "
           "d’une entreprise ou d’un État. Trois risques en découlent : la spéculation sur la "
           "faillite, l’effet de contagion si de nombreux acteurs sont liés entre eux, et le "
           "risque systémique si le vendeur du CDS ne peut lui-même indemniser — exactement ce "
           "qui a fragilisé certains acteurs en 2008."],
     'mec': "Créances bancaires → regroupées et cédées à un véhicule → titres vendus "
            "mondialement → le risque sort du bilan mais se disperse et devient illisible → "
            "un choc de défauts se propage à tout le système."},
    {'t': "G. Too Big To Fail : concentration, aléa moral et socialisation des pertes",
     'd': ["Certaines institutions financières sont si grandes et si centrales que leur "
           "faillite menacerait le système bancaire, les paiements, le crédit et l’économie "
           "réelle : elles sont perçues comme implicitement protégées.",
           "Trois problèmes en résultent. Le risque systémique : la chute d’un grand acteur "
           "contamine tout le système. L’aléa moral : si les acteurs pensent qu’ils seront "
           "sauvés, ils prennent davantage de risques et fragilisent l’ensemble. La "
           "socialisation des pertes : les profits restent privés, mais les pertes sont en "
           "partie supportées par les banques centrales et les États, donc par la "
           "collectivité."]},
   ],
   'v': "La boucle se referme sur la notion qui fondait la monnaie au début du chapitre : la "
        "confiance — c’est elle que la crise détruit, et c’est pour la restaurer que la banque "
        "centrale a dû élargir ses missions."},
 ],

 'ae': [
  {'n': "Aristote", 'k': 'a',
   'i': "Les trois fonctions de la monnaie — unité de compte, intermédiaire des échanges, "
        "réserve de valeur — qui servent de test pour juger le bitcoin."},
  {'n': "Paul Krugman", 'k': 'a',
   'i': "Les six fonctions de la monnaie internationale : libellé, véhiculaire, investissement "
        "pour le privé ; ancrage, intervention, réserve pour les banques centrales."},
  {'n': "Robert Mundell", 'k': 'a',
   'i': "Le triangle d’incompatibilité : liberté des capitaux, autonomie monétaire et change "
        "stable ne peuvent coexister — on en choisit deux."},
  {'n': "John Law (1716-1720)", 'k': 'a',
   'i': "Première tentative de monnaie-papier en France : la confiance crée la monnaie, et sa "
        "perte la détruit. Schumpeter le dit monétariste et pré-keynésien."},
  {'n': "Banking School contre Currency School (XIXᵉ siècle)", 'k': 'a',
   'i': "L’ancêtre du débat exogène/endogène : les billets doivent-ils être couverts par l’or, "
        "ou s’adapter aux besoins de l’économie ?"},
  {'n': "Jean Bodin, Jean-Baptiste Say, David Ricardo", 'k': 'a',
   'i': "La monnaie n’est qu’un voile : elle agit sur les prix, jamais sur la production."},
  {'n': "Irving Fisher", 'k': 'a',
   'i': "MV = PT : identité comptable qui devient théorie quantitative sous l’hypothèse de "
        "stabilité de V et T."},
  {'n': "Milton Friedman (1956)", 'k': 'a',
   'i': "Monnaie exogène, neutre à long terme, anticipations adaptatives : la monnaie est "
        "puissante, la politique monétaire impuissante."},
  {'n': "Alban W. Phillips (1958), puis Samuelson et Solow", 'k': 'a',
   'i': "La relation inverse entre chômage et croissance des salaires nominaux, observée au "
        "Royaume-Uni de 1861 à 1957, et le NAWRU."},
  {'n': "John Hicks", 'k': 'a',
   'i': "Le passage de l’économie d’endettement à l’économie de marchés financiers — thèse à "
        "nuancer par l’intermédiation de marché."},
  {'n': "Henri Bourguinat, Les vertiges de la finance internationale (1987)", 'k': 'a',
   'i': "Les trois D — déréglementation, décloisonnement, désintermédiation — qui expliquent "
        "la globalisation financière depuis les années 1980."},
  {'n': "Éric Monnet, La Banque providence (2021)", 'k': 'a',
   'i': "Les banques centrales deviennent des acteurs de la gouvernance économique : "
        "transition écologique, monnaie numérique, dette publique — d’où un enjeu "
        "démocratique."},
  {'n': "Abba Lerner (1943) et Stephanie Kelton (2021)", 'k': 'a',
   'i': "Théorie monétaire moderne : un État souverain monétairement n’a pas de contrainte "
        "financière, seulement une contrainte réelle et inflationniste."},
  {'n': "Christine Lagarde", 'k': 'a',
   'i': "Les permacrises : la crise n’est plus un accident ponctuel mais le régime ordinaire "
        "dans lequel la politique monétaire doit opérer."},
  {'n': "La bulle du Mississippi (1720)", 'k': 'e',
   'i': "Des actions de 150 à 4 100 livres, puis l’effondrement quand chacun veut son or : la "
        "première grande bulle financière française."},
  {'n': "Le SME et l’ECU (± 2,5 %)", 'k': 'e',
   'i': "Une unité de compte et des marges étroites, jusqu’à l’échec : l’euro naît de cette "
        "impossibilité à stabiliser des monnaies séparées."},
  {'n': "Les paiements en France en 2020", 'k': 'e',
   'i': "Cartes : 56,6 % des opérations mais 1,6 % des montants ; virements et prélèvements : "
        "37 % des opérations et ≈ 97 % des montants."},
  {'n': "La crise de 2008", 'k': 'e',
   'i': "Titrisation, CDO et CDS transforment des défauts immobiliers américains en crise "
        "systémique mondiale, et imposent les politiques non conventionnelles."},
  {'n': "Le bitcoin (2008, Satoshi Nakamoto)", 'k': 'e',
   'i': "21 millions d’unités au maximum, 19,8 millions émises, forte volatilité : un "
        "crypto-actif qui ne remplit pas les trois fonctions de la monnaie."},
  {'n': "La stagflation des années 1970", 'k': 'e',
   'i': "Inflation et chômage simultanés après le choc pétrolier : la réfutation empirique de "
        "la courbe de Phillips."},
 ],

 'arg': [
  "Monnaie endogène ou exogène n’est pas une querelle d’école : c’est la question de savoir "
  "qui commande. Multiplicateur (MC → M) : la banque centrale contrôle la quantité. Diviseur "
  "(M → MC) : elle ne contrôle que le prix, l’offre de monnaie s’adaptant à la demande de "
  "crédit.",
  "« Les crédits font les dépôts » renverse l’intuition : une banque n’a pas besoin d’épargne "
  "préalable pour prêter, ce qui invalide l’idée d’une épargne qui financerait "
  "l’investissement.",
  "Une variation des taux agit par quatre canaux simultanés — crédit, prix des actifs, "
  "anticipations, change : mobiliser les quatre vaut mieux que développer le seul canal du "
  "crédit.",
  "Les politiques non conventionnelles ont restauré la liquidité mais gonflé le prix des "
  "actifs : argument central pour relier politique monétaire et inégalités de patrimoine.",
  "La désintermédiation n’a pas supprimé le risque, elle l’a dispersé : titrisation, CDO et "
  "CDS rendent la contagion plus rapide et la régulation plus difficile.",
  "La formule de Friedman doit être citée entière : la monnaie est puissante (elle détermine "
  "l’inflation), la politique monétaire est impuissante (les agents anticipent).",
 ],

 'deb': [
  "La monnaie est-elle neutre ? Voile des classiques et théorie quantitative contre monnaie "
  "active des keynésiens — le cours tranche partiellement : neutre à long terme, active mais "
  "instable à court terme.",
  "Qui contrôle la masse monétaire : la banque centrale par la base monétaire, ou la demande "
  "de crédit des agents ?",
  "Faut-il élargir le mandat de la BCE au climat, à la monnaie numérique et à la dette "
  "publique, comme le propose Monnet, ou s’en tenir à la stabilité des prix ?",
  "La théorie monétaire moderne libère-t-elle d’une contrainte artificielle, ou nie-t-elle la "
  "contrainte réelle d’inflation ?",
  "Faut-il séparer banques de dépôt et banques d’affaires, ou la banque universelle est-elle "
  "plus efficace malgré son risque de liquidité ?",
  "Les crypto-actifs peuvent-ils devenir des monnaies, ou leur volatilité et l’absence de "
  "valeur sous-jacente les en empêchent-elles structurellement ?",
 ],

 'lien': [
  {'c': 1, 'p': "Le financement du déficit par émission d’obligations, la charge de la dette, "
                "le quantitative easing comme solution à l’endettement et le policy mix "
                "prolongent directement ce chapitre."},
  {'c': 6, 'p': "Le coût du capital, les conditions de financement de l’investissement et la "
                "stagnation séculaire relient politique monétaire et croissance potentielle."},
  {'c': 7, 'p': "La hiérarchie monétaire internationale et la dette en devises des pays en "
                "développement se comprennent à partir des six fonctions de Krugman."},
  {'c': 21, 'p': "Le dollar comme monnaie de réserve et d’intervention est la clé du privilège "
                 "exorbitant américain et des déséquilibres mondiaux."},
  {'c': 8, 'p': "La financiarisation et la montée des marchés de capitaux nourrissent le "
                "capitalisme actionnarial et la gouvernance d’entreprise."},
  {'c': 9, 'p': "La concentration bancaire et les institutions « too big to fail » posent à la "
                "finance la question de la taille et du pouvoir de marché."},
 ],

 'min': [
  "Trois fonctions (Aristote), une confiance ; 91 % de monnaie scripturale en zone euro ; "
  "cartes = 56,6 % des opérations mais 1,6 % des montants.",
  "M1 ⊂ M2 ⊂ M3 ; la banque centrale contrôle M3 ; TCN ≥ 150 000 € ; OPCVM = FCP (parts) ou "
  "SICAV (actions).",
  "Krugman : six fonctions internationales ; triangle de Mundell : deux objectifs sur trois.",
  "« Les crédits font les dépôts » : multiplicateur (exogène, MC → M, 100 → 500 avec r = "
  "20 %) contre diviseur (endogène, M → MC).",
  "MV = PT (Fisher) ; Friedman : neutralité à long terme, anticipations adaptatives, chômage "
  "naturel — monnaie puissante, politique monétaire impuissante.",
  "Phillips (1958, RU 1861-1957) et le NAWRU ; stagflation des années 1970 : la courbe devient "
  "verticale.",
  "Trois taux directeurs : facilité de dépôt (plancher), facilité de prêt (plafond), "
  "refinancement à une semaine (signal) ; corridor, €STR ex-EONIA ; cible de 2 %.",
  "Quatre canaux : taux d’intérêt, prix des actifs (effet richesse), anticipations (forward "
  "guidance), taux de change.",
  "2008 : trappe à liquidité → QE (taille du bilan), qualitative easing (composition), taux "
  "négatifs, LTRO/TLTRO — et aléa moral.",
  "Hicks : économie d’endettement → marchés financiers, nuancée en intermédiation de marché ; "
  "trois D de Bourguinat (1987) ; titrisation, CDO, CDS, shadow banking, too big to fail.",
 ],
}}
