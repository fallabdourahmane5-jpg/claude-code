# -*- coding: utf-8 -*-
"""Visualisation 10 — Régionalisation et gouvernance mondiale (strates)."""

from vz_base import v, nd, ln

v('vz-gouvernance', 'Régionalisation et gouvernance mondiale',
  '2ᵉ année, chapitre 4 · quatre étages institutionnels',
  'strates',
  "Les États ne cessent pas de négocier : ils négocient ailleurs. Cette "
  "visualisation descend les quatre étages du chapitre : l’ordre "
  "multilatéral construit après 1945, son enlisement à partir des années "
  "2000, le report des négociations vers le niveau régional, et ce qui reste "
  "à organiser mondialement — les biens publics mondiaux et le système "
  "monétaire.",
  [("Le fil directeur",
    "La régionalisation n’est pas une alternative choisie au "
    "multilatéralisme : c’est une conséquence de son enlisement. Tenir cette "
    "causalité évite de présenter les accords régionaux comme un phénomène "
    "autonome."),
   ("Deux auteurs indispensables",
    "Balassa pour l’échelle d’intégration — zone de libre-échange, union "
    "douanière, marché commun, union économique, union monétaire. Viner pour "
    "l’évaluation — toute préférence régionale crée du trafic et en détourne "
    "simultanément."),
   ("La conclusion du cours",
    "Le véritable enjeu n’est probablement pas mondialisation ou "
    "démondialisation, mais quelle forme de mondialisation et à quel niveau "
    "organiser les règles. La question est institutionnelle avant d’être "
    "quantitative.")],
  [
   # ------------------------------------------------ 1. l’ordre multilatéral
   nd('multilateralisme', 'Le multilatéralisme', 'coeur',
      "Une action collective entre au moins trois États pour établir des "
      "règles communes. Non-discrimination, réciprocité, transparence : les "
      "trois principes du GATT puis de l’OMC.",
      grp=1,
      defi="Le multilatéralisme correspond à l’organisation de relations "
           "internationales autour de règles négociées collectivement et "
           "applicables à un ensemble de pays : une action collective entre "
           "au moins trois États visant à établir des règles communes "
           "organisant les interdépendances internationales, par opposition à "
           "l’unilatéralisme et au bilatéralisme. Le cours en situe "
           "l’origine dans l’ordre d’après 1945.",
      mec=[("Les cinq formes de relations commerciales",
            "Unilatéralisme, bilatéralisme, régionalisme, plurilatéralisme et "
            "multilatéralisme : la typologie permet de classer rigoureusement "
            "les relations commerciales et d’éviter de confondre une "
            "négociation à deux avec une règle collective."),
           ("Les principes constitutifs",
            "Le multilatéralisme repose sur la réciprocité et l’équité ; le "
            "GATT puis l’Organisation mondiale du commerce sur trois "
            "principes fondamentaux : non-discrimination, réciprocité et "
            "transparence."),
           ("La mécanique de la généralisation",
            "La clause de la nation la plus favorisée étend à tous les "
            "membres la concession accordée à l’un : c’est elle qui "
            "transforme une négociation bilatérale en règle collective.")],
      aut=[{'n': "Paul Krugman",
            'i': "Le multilatéralisme du GATT relève d’un « mercantilisme "
                 "éclairé »."},
           {'n': "Charles Kindleberger",
            'i': "Un ordre économique international stable nécessite qu’une "
                 "puissance dominante accepte d’assumer certaines "
                 "responsabilités collectives."}],
      faits=[{'f': "En 1947, vingt-trois pays signent le GATT, après l’échec "
                   "du projet d’Organisation internationale du commerce, les "
                   "États-Unis n’ayant pas ratifié la Charte de La Havane.",
              'p': "Le pilier commercial de l’ordre d’après-guerre est né "
                   "d’un compromis : un accord commercial plutôt qu’une "
                   "véritable organisation internationale."}],
      termes=['multilateralisme', 'gatt', 'organisation mondiale du commerce'],
      dos=['n21-multilateralisme', 'n21-omc']),

   nd('institutions', 'L’architecture d’après 1945', 'pilier',
      "ONU, FMI, Banque mondiale, GATT puis OMC en 1995 — et, après 2008, le "
      "G20 comme principal forum de coordination.",
      grp=1,
      defi="La gouvernance mondiale désigne un mode de régulation "
           "supranationale édictant des règles d’organisation à l’échelle de "
           "la planète, issu le plus souvent de la coopération "
           "internationale. La notion est plus large que la seule production "
           "de règles : elle concerne le pouvoir des acteurs, son "
           "organisation, les mécanismes de coordination et les institutions "
           "qui font respecter les règles communes.",
      mec=[("La construction d’après-guerre",
            "La première grande architecture contemporaine apparaît après la "
            "Seconde Guerre mondiale : Organisation des Nations unies, Fonds "
            "monétaire international, Banque mondiale, puis le système "
            "commercial issu du GATT auquel succède l’Organisation mondiale "
            "du commerce en 1995."),
           ("Le déplacement vers les forums informels",
            "La crise de 2008 consacre le G20 comme principal forum "
            "économique mondial et lieu de coordination : le centre de "
            "gravité se déplace vers des enceintes moins formelles que les "
            "organisations internationales."),
           ("La contestation du contenu des règles",
            "L’Organisation mondiale du commerce est accusée d’avoir porté un "
            "ordre asymétrique : la question de l’accès aux médicaments "
            "révèle les tensions entre propriété intellectuelle et santé "
            "publique.")],
      aut=[{'n': "Arnaud Orain",
            'i': "Nous serions entrés dans un nouvel âge du capitalisme de la "
                 "finitude."}],
      args=[{'a': "L’architecture multilatérale a produit un bien public "
                  "réel : la prévisibilité des règles commerciales et "
                  "financières, qui réduit le coût de l’échange pour tous.",
             'lim': "Sa légitimité est contestée parce que les règles ont été "
                    "écrites par les puissances dominantes de 1945, ce qui "
                    "explique que la contestation vienne aussi des pays "
                    "émergents."}],
      termes=['gouvernance mondiale', 'fmi', 'banque mondiale', 'g20'],
      dos=['n21-gouvernance-mondiale', 'n21-fmi']),

   # --------------------------------------------------- 2. l’enlisement
   nd('enlisement', 'L’enlisement du multilatéralisme', 'limite',
      "Seattle 1999 révèle une crise de légitimité ; le cycle de Doha "
      "s’enlise, notamment du fait du principe de l’engagement unique.",
      grp=2,
      defi="La crise du multilatéralisme commercial est antérieure aux "
           "tensions géopolitiques contemporaines. La conférence de Seattle "
           "de 1999 révèle une crise de légitimité de l’Organisation "
           "mondiale du commerce, et le cycle de Doha ouvert en 2001 "
           "s’enlise, notamment du fait du principe de l’engagement unique, "
           "qui subordonne l’accord sur chaque point à l’accord sur "
           "l’ensemble.",
      mec=[("Le blocage par l’engagement unique",
            "Rien n’est acquis tant que tout n’est pas acquis : la règle "
            "garantit l’équilibre global du paquet mais donne à chaque membre "
            "un pouvoir de blocage sur l’ensemble de la négociation."),
           ("L’élargissement du nombre de parties",
            "Avec l’entrée de nombreux pays aux intérêts hétérogènes, "
            "l’espace d’accord se rétrécit : ce qui fait la légitimité du "
            "multilatéralisme en complique l’exercice."),
           ("Le retour de l’unilatéralisme des grandes puissances",
            "Les deux principales puissances économiques mondiales adoptent "
            "de plus en plus des stratégies unilatérales et s’écartent de "
            "certaines règles : la crise vient des acteurs les plus "
            "puissants, non des plus faibles.")],
      faits=[{'f': "L’Organisation mondiale du commerce évoque dans son "
                   "rapport de juillet 2026 un « tournant décisif pour le "
                   "multilatéralisme ».",
              'p': "La formule, émise par l’institution elle-même, mesure "
                   "l’ampleur de la crise et interdit de la présenter comme "
                   "une difficulté passagère."},
             {'f': "Entre les deux grandes puissances se trouvent les "
                   "puissances intermédiaires, parfois qualifiées de "
                   "« zèbres », qui répondent par la multiplication des "
                   "accords commerciaux.",
              'p': "Le fait explique l’accélération du régionalisme comme "
                   "substitut au multilatéralisme : ce sont les puissances "
                   "moyennes qui en sont les acteurs les plus actifs."}],
      termes=['cycle de doha', 'unilateralisme', 'crise du multilateralisme'],
      dos=['n21-multilateralisme', 'n21-omc']),

   nd('fragmentation', 'La fragmentation géoéconomique', 'limite',
      "Les échanges augmentent davantage entre pays politiquement proches : "
      "la géographie du commerce suit désormais les alignements.",
      grp=2,
      defi="La fragmentation géoéconomique désigne la recomposition des flux "
           "commerciaux selon les alignements politiques plutôt que selon les "
           "seuls avantages comparatifs. Elle ne se traduit pas "
           "nécessairement par une baisse du commerce mondial, mais par un "
           "changement de sa géographie : les échanges augmentent davantage "
           "entre pays politiquement proches, ce qui rend la fragmentation "
           "déjà observable.",
      mec=[("La prime à la proximité politique",
            "Le risque d’interruption d’un approvisionnement dépend de la "
            "relation politique avec le fournisseur : à coût égal, un "
            "partenaire allié devient préférable, ce qui déplace les flux "
            "sans les réduire."),
           ("Le coût de la rupture mesuré",
            "Les estimations disponibles chiffrent le coût d’une "
            "fragmentation en blocs, et montrent que la rapidité de la "
            "rupture pèse autant que son ampleur : une réorganisation "
            "progressive est bien moins coûteuse qu’une rupture brutale.")],
      aut=[{'n': "Sébastien Jean",
            'i': "Trois scénarios sont envisageables pour l’avenir du "
                 "commerce international."},
           {'n': "Branko Milanovic",
            'i': "La grande transformation contemporaine correspond à une "
                 "renationalisation du marché."}],
      faits=[{'f': "Les échanges augmentent davantage entre pays "
                   "politiquement proches, ce qui rend la fragmentation "
                   "géopolitique des échanges déjà observable.",
              'p': "Le fait relie la régionalisation commerciale à la "
                   "recomposition géopolitique et montre que les deux "
                   "processus se renforcent."}],
      termes=['fragmentation geoeconomique', 'blocs', 'demondialisation'],
      dos=['n17-fragmentation-geoeconomique', 'n17-demondialisation']),

   # ------------------------------------------------- 3. le report régional
   nd('regionalisation', 'La régionalisation', 'pilier',
      "642 accords notifiés, 388 en vigueur : plus aucun membre de l’OMC "
      "n’est extérieur aux accords préférentiels.",
      grp=3,
      defi="La régionalisation désigne le déplacement des négociations "
           "commerciales du niveau mondial vers des groupes plus restreints "
           "de pays, qui organisent entre eux des accords commerciaux "
           "régionaux. Le cours la présente comme une conséquence de "
           "l’enlisement du multilatéralisme : les États ne cessent pas de "
           "négocier, ils négocient ailleurs.",
      mec=[("Le report des négociations",
            "Face au blocage multilatéral, les États cherchent des enceintes "
            "où l’accord reste possible : moins de parties, intérêts plus "
            "homogènes, calendrier maîtrisable."),
           ("L’empilement des appartenances",
            "Un pays peut appartenir simultanément à plusieurs réseaux "
            "d’accords : on n’a plus un pays pour un accord mais un pays pour "
            "plusieurs accords, plusieurs partenaires et plusieurs ensembles "
            "de règles — ce que le cours résume par l’image du « bol de "
            "spaghettis »."),
           ("Le changement de nature des accords",
            "Les accords contemporains deviennent des accords commerciaux "
            "profonds, intégrant des normes sociales et environnementales : "
            "ils harmonisent des réglementations internes et pas seulement "
            "des tarifs.")],
      aut=[{'n': "Robert Lawrence",
            'i': "Il faut distinguer intégration superficielle et intégration "
                 "profonde selon les domaines couverts."}],
      faits=[{'f': "Au 1er septembre 2026, 642 accords commerciaux régionaux "
                   "ont été notifiés à l’Organisation mondiale du commerce et "
                   "388 sont en vigueur, après une progression faible "
                   "jusqu’aux années 1980 puis très rapide à partir des "
                   "années 1990.",
              'p': "Les chiffres établissent l’ampleur et la datation du "
                   "phénomène, et montrent qu’il s’accélère au moment où les "
                   "négociations multilatérales se compliquent."},
             {'f': "La carte du cours montre 181 notifications d’accords "
                   "concernant l’Europe, parmi les économies particulièrement "
                   "engagées figurant aussi le Royaume-Uni, le Chili, "
                   "Singapour, la Turquie, le Mexique, la Corée et la Chine.",
              'p': "Les grandes puissances commerciales sont les acteurs les "
                   "plus actifs du régionalisme, et non ses victimes."}],
      termes=['regionalisation', 'accords commerciaux regionaux',
              'accords preferentiels'],
      dos=['n21-regionalisation', 'n21-accords-commerciaux-regionaux']),

   nd('balassa', 'Les cinq étapes de Balassa', 'detail',
      "Zone de libre-échange, union douanière, marché commun, union "
      "économique, union monétaire : un continuum d’intégration croissante.",
      grp=3,
      defi="Bela Balassa décrit l’intégration économique régionale comme un "
           "continuum de cinq étapes successives et croissantes. Chacune "
           "ajoute une contrainte à la précédente : la zone de libre-échange "
           "supprime les droits internes, l’union douanière y ajoute un tarif "
           "extérieur commun, le marché commun la libre circulation des "
           "facteurs, l’union économique la coordination des politiques, "
           "l’union monétaire une monnaie unique.",
      mec=[("De la zone de libre-échange à l’union douanière",
            "Supprimer les droits entre membres ne suffit pas : sans tarif "
            "extérieur commun, les importations entrent par le pays le moins "
            "protégé, ce qui impose des règles d’origine ou le passage à "
            "l’union douanière."),
           ("Du marché commun à l’union économique",
            "Faire circuler les facteurs expose les différences de "
            "réglementation et de fiscalité : l’intégration appelle une "
            "harmonisation, donc un transfert de compétences."),
           ("L’union monétaire et ses exigences",
            "Partager une monnaie supprime l’ajustement par le change : les "
            "chocs asymétriques doivent alors être absorbés par la mobilité, "
            "les transferts budgétaires ou les prix, faute de quoi "
            "l’ajustement se fait par l’emploi.")],
      aut=[{'n': "Bela Balassa",
            'i': "L’intégration économique régionale passe par cinq étapes "
                 "successives et croissantes."},
           {'n': "Robert Mundell",
            'i': "On ne peut pas avoir simultanément libre circulation des "
                 "capitaux, politique monétaire autonome et change stable."}],
      termes=['union douaniere', 'marche commun',
              'union economique et monetaire', 'balassa'],
      dos=['n21-uem', 'n21-union-douaniere', 'n21-zone-libre-echange']),

   nd('viner', 'Création et détournement de trafic', 'detail',
      "Toute préférence régionale fait les deux à la fois. Le bilan dépend de "
      "l’effet dominant : il est empirique, jamais automatique.",
      grp=3,
      defi="Jacob Viner montre, dans The Customs Union Issue de 1950, qu’une "
           "union douanière produit simultanément deux effets contraires : "
           "une création de trafic, lorsqu’une production domestique coûteuse "
           "est remplacée par une importation moins chère venant d’un "
           "partenaire, et un détournement de trafic, lorsqu’une préférence "
           "tarifaire écarte un fournisseur extérieur plus efficace. Le bilan "
           "dépend de l’effet dominant.",
      mec=[("La création de trafic",
            "Avant l’accord, un pays produit lui-même certains biens qu’un "
            "partenaire pourrait produire à moindre coût, les droits de "
            "douane empêchant l’importation. La suppression des droits "
            "corrige cette inefficacité."),
           ("Le détournement de trafic",
            "Le pays importait depuis le fournisseur mondial le moins cher ; "
            "après l’union, le prix du partenaire hors droits peut devenir "
            "inférieur au prix du tiers augmenté du droit de douane : un "
            "fournisseur plus efficace est écarté."),
           ("Le caractère inévitable de la discrimination",
            "Supprimer les droits uniquement entre quelques partenaires crée "
            "nécessairement une discrimination envers les pays extérieurs : "
            "le détournement est inhérent à toute préférence régionale, non "
            "un accident de mise en œuvre.")],
      aut=[{'n': "Jacob Viner",
            'i': "Une union douanière produit simultanément création et "
                 "détournement de trafic, et n’améliore donc pas "
                 "nécessairement le bien-être."}],
      faits=[{'f': "Le cours conclut que si la création de trafic dépasse le "
                   "détournement, l’accord améliore globalement le bien-être, "
                   "et que dans le cas inverse il peut réduire l’efficience.",
              'p': "Le critère montre que le jugement sur un accord est "
                   "nécessairement empirique : aucune position de principe ne "
                   "tient sur le régionalisme."}],
      termes=['creation de trafic', 'detournement de trafic', 'viner',
              'union douaniere'],
      dos=['n21-creation-detournement-commerce', 'le28-detournement']),

   # ------------------------------------------- 4. ce qui reste à organiser
   nd('bpm', 'Les biens publics mondiaux', 'pilier',
      "Climat, biodiversité, stabilité financière, règles équitables : non "
      "rivaux, non excluables. Aucun État ne peut les produire seul.",
      grp=4,
      defi="Un bien public mondial possède deux propriétés : la non-rivalité, "
           "sa consommation par un acteur n’empêchant pas les autres d’en "
           "bénéficier, et la non-exclusion, puisqu’il est difficile "
           "d’empêcher un acteur d’en bénéficier. Le cours en fait la "
           "justification fondamentale de la gouvernance mondiale, puisque "
           "leur production ne peut être efficacement assurée par des États "
           "agissant isolément.",
      mec=[("Le passager clandestin à l’échelle des États",
            "Sans coordination internationale, chaque État a intérêt à "
            "laisser les autres supporter le coût : le comportement de "
            "passager clandestin produit un équilibre de Nash sous-optimal."),
           ("L’étendue de la catégorie",
            "Les biens publics mondiaux concernent la préservation du climat "
            "et de la biodiversité, la stabilité financière, la stabilité du "
            "commerce international et l’existence de règles commerciales "
            "équitables : des objets environnementaux autant "
            "qu’institutionnels."),
           ("La voie de la puissance régulatrice",
            "À défaut de coordination mondiale, un grand marché peut imposer "
            "unilatéralement des règles servant un bien public : le mécanisme "
            "d’ajustement carbone aux frontières transforme la taille du "
            "marché européen en instrument climatique.")],
      aut=[{'n': "John Nash",
            'i': "Un équilibre non coopératif peut être collectivement "
                 "sous-optimal alors que chacun agit rationnellement."},
           {'n': "Charles Kindleberger",
            'i': "La stabilité internationale repose sur la fourniture de "
                 "biens publics internationaux par une puissance dominante."}],
      faits=[{'f': "Le cours relève le paradoxe fondamental de la période : "
                   "les États veulent retrouver leur souveraineté nationale "
                   "alors que certains problèmes exigent une coordination, et "
                   "la montée des tensions géopolitiques fait reculer la "
                   "coopération.",
              'p': "La difficulté est politique : le besoin de biens publics "
                   "mondiaux s’accroît au moment où la capacité de les "
                   "produire diminue."}],
      termes=['biens publics mondiaux', 'cooperation internationale',
              'passager clandestin'],
      dos=['n21-biens-publics-mondiaux', 'n21-cooperation-internationale']),

   nd('dollar', 'L’hégémonie du dollar', 'debat',
      "Les titres du Trésor américain sont l’actif sûr mondial : les "
      "États-Unis empruntent dans leur propre monnaie, à un coût anormalement "
      "bas.",
      grp=4,
      defi="L’hégémonie du dollar désigne la place centrale qu’occupe la "
           "monnaie américaine dans le système monétaire international : les "
           "actifs américains, notamment les titres publics, sont "
           "particulièrement recherchés et constituent l’actif sûr mondial, "
           "de sorte que les États-Unis peuvent attirer beaucoup de capitaux, "
           "emprunter dans leur propre monnaie et bénéficier d’une forte "
           "demande internationale pour leurs actifs. C’est ce que le cours "
           "qualifie de « privilège exorbitant ».",
      mec=[("La mesure exacte du privilège",
            "Les États-Unis attirent massivement les capitaux sans offrir "
            "nécessairement les rendements les plus élevés : l’avantage ne se "
            "mesure pas au volume de capitaux attirés mais à l’écart entre ce "
            "volume et le rendement offert, c’est-à-dire à un coût de "
            "financement anormalement bas."),
           ("La suppression de la contrainte extérieure",
            "Le FMI préconise pour les États-Unis un assainissement "
            "budgétaire, selon la séquence hausse des recettes, réduction du "
            "déficit public, réduction du déficit courant. La solution est "
            "connue ; ce qui manque est la contrainte qui obligerait à "
            "l’appliquer, précisément parce que le privilège la supprime."),
           ("Le caractère réversible du statut",
            "Le dollar a remplacé la livre sterling, dominante jusqu’en 1914, "
            "surtout après 1945 ; il a conservé sa centralité après la "
            "suspension de sa convertibilité en or en 1971. Le statut est "
            "donc réversible, mais sa base n’est pas l’adossement métallique.")],
      aut=[{'n': "Hélène Rey",
            'i': "Les conditions financières mondiales sont déterminées par "
                 "la politique monétaire du centre du système."},
           {'n': "Henri Bourguinat",
            'i': "La finance internationale se caractérise par un "
                 "enchevêtrement de marchés et de monnaies qui amplifie "
                 "l’instabilité."}],
      faits=[{'f': "Le déficit courant américain dépasse 1 200 milliards de "
                   "dollars et approche 4 % du PIB en 2025, avec un déficit "
                   "public d’environ 6 % du PIB depuis 2022, contre 5 % en "
                   "1985.",
              'p': "Les ordres de grandeur montrent la taille du déséquilibre "
                   "que l’hégémonie monétaire rend soutenable, et indiquent "
                   "que la situation actuelle n’est pas sans précédent mais "
                   "en dépasse l’ampleur."}],
      termes=['hegemonie du dollar', 'systeme monetaire international',
              'privilege exorbitant'],
      dos=['n21-hegemonie-dollar', 'n21-systeme-monetaire-international']),

   nd('question', 'Quelle forme, et à quel niveau ?', 'sortie',
      "Le véritable enjeu n’est pas mondialisation ou démondialisation, mais "
      "quelle forme de mondialisation et à quel niveau organiser les règles.",
      grp=4,
      defi="Le cours conclut que le véritable enjeu n’est probablement pas "
           "mondialisation ou démondialisation mais quelle forme de "
           "mondialisation et à quel niveau organiser les règles. La question "
           "est institutionnelle avant d’être quantitative : ce qui se joue "
           "n’est pas le volume des échanges mais le niveau — national, "
           "régional, mondial — auquel sont décidées les règles qui les "
           "encadrent.",
      mec=[("Le choix du niveau pertinent",
            "Certaines règles n’ont de sens qu’au niveau mondial, parce que "
            "leur objet l’est : climat, stabilité financière. D’autres "
            "peuvent être régionales sans perte d’efficacité. Le bon niveau "
            "dépend de l’étendue de l’effet à réguler."),
           ("Le coût de la discordance des niveaux",
            "Lorsque le problème est mondial et la décision nationale, la "
            "sous-production est garantie : c’est exactement le mécanisme du "
            "passager clandestin appliqué aux États."),
           ("La régionalisation comme second rang",
            "À défaut d’accord mondial, l’accord régional produit une partie "
            "des bénéfices attendus tout en créant une discrimination envers "
            "les tiers : c’est une solution de second rang, pas un "
            "équivalent.")],
      args=[{'a': "Reformuler le débat en termes de niveau d’organisation "
                  "évite l’alternative stérile entre ouverture et fermeture, "
                  "et désigne un objet de négociation précis.",
             'lim': "Le choix du niveau est lui-même un enjeu de pouvoir : "
                    "déplacer une règle du national au supranational "
                    "redistribue l’influence entre acteurs, ce qui explique "
                    "la résistance à la coordination."}],
      aut=[{'n': "Dani Rodrik",
            'i': "L’hypermondialisation entre en conflit avec la démocratie "
                 "et la souveraineté nationale."}],
      termes=['gouvernance mondiale', 'coordination des politiques',
              'subsidiarite'],
      dos=['n21-gouvernance-mondiale', 'n21-coordination-politiques']),
  ],
  [
   ln('multilateralisme', 'institutions', 'se dote de',
      "Le principe multilatéral ne vaut que s’il est porté par des "
      "institutions capables d’édicter et de faire respecter les règles : "
      "ONU, FMI, Banque mondiale, GATT puis OMC en 1995.", 'cause'),
   ln('multilateralisme', 'enlisement', 'se bloque par ses propres règles',
      "L’engagement unique garantit l’équilibre global du paquet négocié mais "
      "donne à chaque membre un pouvoir de blocage sur l’ensemble : ce qui "
      "fait la légitimité du multilatéralisme en complique l’exercice.",
      'limite'),
   ln('institutions', 'enlisement', 'perd sa légitimité',
      "Seattle en 1999 révèle une crise de légitimité, et l’Organisation "
      "mondiale du commerce est accusée d’avoir porté un ordre asymétrique. "
      "La contestation porte sur le contenu des règles, pas seulement sur "
      "leur existence.", 'limite'),
   ln('enlisement', 'regionalisation', 'provoque le report vers',
      "Les États ne cessent pas de négocier : ils négocient ailleurs. "
      "L’accélération du régionalisme à partir des années 1990 coïncide "
      "précisément avec la complication des négociations multilatérales.",
      'cause'),
   ln('fragmentation', 'regionalisation', 'oriente les accords',
      "Les échanges augmentent davantage entre pays politiquement proches : "
      "la recomposition géopolitique et la régionalisation commerciale se "
      "renforcent mutuellement, la seconde donnant forme juridique à la "
      "première.", 'renforce'),
   ln('enlisement', 'fragmentation', 'laisse place à',
      "Quand la règle commune ne s’impose plus, les grandes puissances "
      "adoptent des stratégies unilatérales : la géographie des échanges se "
      "recompose alors selon les alignements plutôt que selon les seuls "
      "avantages comparatifs.", 'cause'),
   ln('regionalisation', 'balassa', 'se gradue selon',
      "Tous les accords régionaux ne se valent pas : l’échelle de Balassa "
      "permet de situer précisément le degré d’intégration, de la simple "
      "suppression des droits internes à la monnaie unique.", 'mesure'),
   ln('regionalisation', 'viner', 's’évalue par',
      "Un accord régional n’améliore pas automatiquement le bien-être : il "
      "crée du trafic et en détourne simultanément. Le jugement est "
      "empirique, et dépend de l’effet dominant.", 'mesure'),
   ln('viner', 'multilateralisme', 'plaide pour le niveau mondial',
      "Le détournement est inhérent à toute préférence régionale, puisque "
      "supprimer les droits entre quelques partenaires discrimine "
      "nécessairement les tiers. Seule une règle générale l’évite : c’est "
      "l’argument théorique en faveur du multilatéralisme.", 'oppose'),
   ln('balassa', 'bpm', 'bute sur les chocs asymétriques',
      "Plus l’intégration est profonde, plus les instruments nationaux "
      "d’ajustement disparaissent : l’union monétaire supprime le change, ce "
      "qui exige des mécanismes communs d’absorption des chocs, donc une "
      "production collective de stabilité.", 'conditionne'),
   ln('bpm', 'institutions', 'justifie',
      "C’est la sous-production spontanée des biens non rivaux et non "
      "excluables qui fonde la gouvernance mondiale : sans coordination, "
      "chaque État a intérêt à laisser les autres supporter le coût.",
      'cause'),
   ln('fragmentation', 'bpm', 'en compromet la production',
      "Le paradoxe de la période : les États veulent retrouver leur "
      "souveraineté alors que certains problèmes exigent une coordination. Le "
      "besoin s’accroît au moment où la capacité diminue.", 'limite'),
   ln('dollar', 'bpm', 'illustre l’asymétrie de l’ordre',
      "La fourniture de l’actif sûr mondial est un bien public international, "
      "mais elle confère à son émetteur un privilège : la stabilité produite "
      "et l’avantage capté vont de pair, ce que Kindleberger relie à la "
      "responsabilité de la puissance dominante.", 'renforce'),
   ln('bpm', 'question', 'pose la question du niveau',
      "Un problème mondial traité par des décisions nationales est "
      "structurellement sous-traité. Le choix du niveau d’organisation n’est "
      "donc pas une question de procédure : il détermine si le bien sera "
      "produit ou non.", 'cause'),
   ln('regionalisation', 'question', 'est une solution de second rang',
      "L’accord régional produit une partie des bénéfices attendus tout en "
      "créant une discrimination envers les tiers. Il ne remplace pas la "
      "règle générale : il en est le substitut imparfait.", 'limite'),
   ln('dollar', 'question', 'rappelle qui écrit les règles',
      "Le privilège exorbitant montre que l’ordre international n’est pas "
      "neutre : le niveau auquel les règles sont décidées redistribue "
      "l’influence, ce qui explique la résistance à la coordination autant "
      "que la demande de réforme.", 'renforce'),
  ],
  bandes=[(1, 'L’ordre multilatéral'), (2, 'Son enlisement'),
          (3, 'Le report vers le régional'),
          (4, 'Ce qui reste à organiser')],
  fam='Mondialisation et échanges')
