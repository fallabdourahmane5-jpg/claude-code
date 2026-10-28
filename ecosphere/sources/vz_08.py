# -*- coding: utf-8 -*-
"""Visualisation 8 — Libre-échange et protectionnisme (type duel)."""

from vz_base import v, nd, ln

v('vz-libre-echange', 'Libre-échange et protectionnisme',
  '2ᵉ année, chapitres 3 et 4 · un arbitrage, pas une doctrine',
  'duel',
  "Les deux camps ne se contredisent pas autant qu’il y paraît : les "
  "arguments du libre-échange reposent sur des conditions explicites, et le "
  "protectionnisme se justifie précisément là où ces conditions ne sont pas "
  "réunies. Cette visualisation place les gains de l’ouverture à gauche, les "
  "raisons de protéger à droite, et en bas ce qui permet de trancher : les "
  "conditions de validité et le coût des représailles.",
  [("Ne pas opposer deux doctrines mais deux diagnostics",
    "Chaque argument favorable à l’ouverture suppose une condition : "
    "mobilité des facteurs, échelle atteignable, concurrence effective en "
    "aval, capacité d’absorption, qualité de la spécialisation. Le "
    "protectionnisme argumenté se loge exactement dans ces failles."),
   ("Distinguer les protections",
    "Protection éducatrice, politique commerciale stratégique, sécurité "
    "économique : trois logiques distinctes, trois critères d’évaluation "
    "différents. Les confondre est l’erreur la plus fréquente dans les "
    "copies."),
   ("Comparer au bon contrefactuel",
    "Le coût de l’ouverture doit être comparé au coût de la protection, et "
    "non à un état idéal sans ajustement. Les chiffrages du FMI en bas de "
    "figure donnent cet ordre de grandeur.")],
  [
   nd('question', 'Ouvrir ou protéger ?', 'coeur',
      "La question n’est ni « le libre-échange est-il bon ? » ni « le "
      "protectionnisme est-il légitime ? », mais : quelles conditions "
      "l’ouverture suppose-t-elle, et sont-elles réunies ici ?",
      grp=0,
      defi="Le débat sur la politique commerciale n’oppose pas deux systèmes "
           "de valeurs mais deux diagnostics sur une même économie. Les "
           "arguments favorables au libre-échange se rangent en quatre "
           "familles — allocatif, échelle, concurrentiel, dynamique — et "
           "chacun repose sur des hypothèses explicites. La discussion de ces "
           "hypothèses, bien plus que l’énoncé des arguments, fait la valeur "
           "d’une analyse. Symétriquement, les protections les mieux "
           "argumentées ne nient pas les gains de l’échange : elles "
           "soutiennent que les conditions de leur réalisation ne sont pas "
           "présentes.",
      mec=[("Partir des conditions, non des conclusions",
            "Un gain allocatif suppose la mobilité des facteurs, un gain "
            "d’échelle suppose un seuil de production atteignable, un gain "
            "concurrentiel suppose une distribution elle-même "
            "concurrentielle. Chaque condition manquante déplace le "
            "diagnostic."),
           ("Distinguer le statique et le dynamique",
            "Le gain statique de l’échange est compatible avec une "
            "spécialisation défavorable à long terme : un pays peut gagner à "
            "court terme en se spécialisant dans des productions à faible "
            "contenu technologique et perdre en trajectoire de croissance."),
           ("Comparer deux situations réelles",
            "Le coût de l’ouverture se compare au coût de la protection, et "
            "non à un état idéal sans ajustement : les deux options ont des "
            "coûts, et c’est leur écart qui décide.")],
      faits=[{'f': "Les rounds du GATT font passer les droits de douane sur "
                   "les produits manufacturés d’environ 40 % à environ 4 %, "
                   "les concessions négociées étant généralisées par la "
                   "clause de la nation la plus favorisée.",
              'p': "La libéralisation a été obtenue par un marchandage "
                   "réciproque et non par l’adhésion des gouvernements à la "
                   "théorie : les arguments favorables au libre-échange "
                   "n’ont pas été la cause de son adoption."}],
      termes=['libre echange', 'protectionnisme', 'politique commerciale'],
      dos=['le28-libre-echange', 'le28-protectionnisme']),

   # ---------------------------------------- colonne 1 : les gains de l’échange
   nd('allocatif', 'L’argument allocatif', 'pilier',
      "La spécialisation selon les coûts comparés accroît la production "
      "disponible pour tous les partenaires, même lorsqu’un pays est moins "
      "productif partout.",
      grp=1,
      defi="L’argument allocatif est le plus ancien et le plus fort : en se "
           "spécialisant selon ses coûts comparés, chaque pays libère des "
           "ressources des productions où il est relativement le moins "
           "efficace pour les concentrer là où il l’est le plus. La "
           "production mondiale s’en trouve accrue, et l’échange permet à "
           "chacun de consommer au-delà de ses possibilités de production. Le "
           "modèle HOS reformule ensuite l’argument à partir des dotations "
           "factorielles, en en tirant une conséquence distributive.",
      mec=[("L’avantage comparatif plutôt qu’absolu",
            "L’échange reste avantageux même lorsqu’un pays est moins "
            "productif dans toutes les activités : ce qui compte est le coût "
            "d’opportunité, c’est-à-dire ce à quoi il faut renoncer pour "
            "produire un bien plutôt qu’un autre."),
           ("La condition de mobilité des facteurs",
            "Le gain exige que le travail et le capital quittent les branches "
            "en recul pour rejoindre les branches en expansion. Cette "
            "mobilité est coûteuse, lente et géographiquement inégale ; "
            "lorsqu’elle fait défaut, la spécialisation produit un gain de "
            "prix et une perte d’emploi simultanés."),
           ("La conséquence distributive du modèle HOS",
            "Si l’échange s’explique par les dotations factorielles, il "
            "profite au facteur abondant et dessert le facteur rare dans "
            "chaque pays : le gain national recouvre des effets opposés selon "
            "les catégories.")],
      aut=[{'n': "David Ricardo",
            'i': "La spécialisation selon les coûts comparés augmente la "
                 "production disponible pour tous les partenaires."},
           {'n': "Eli Heckscher",
            'i': "Le commerce s’explique par les différences de dotations "
                 "factorielles entre pays."},
           {'n': "Bertil Ohlin",
            'i': "Chaque pays exporte le bien intensif dans le facteur dont "
                 "il est relativement le mieux doté."}],
      termes=['avantage comparatif', 'dotations factorielles',
              'specialisation internationale'],
      dos=['n16-avantages-comparatifs', 'n16-dotations-factorielles']),

   nd('echelle', 'Échelle, variété, concurrence', 'pilier',
      "Les rendements croissants fondent trois gains distincts : coût moyen "
      "plus bas, variété plus large, rentes comprimées par la pression "
      "concurrentielle.",
      grp=1,
      defi="L’argument d’échelle et l’argument concurrentiel ne reposent pas "
           "sur des différences entre pays mais sur la taille du marché. "
           "L’élargissement du marché abaisse les coûts moyens, permet la "
           "différenciation des produits et expose les producteurs installés "
           "à une concurrence qui réduit leurs rentes et leurs prix. C’est ce "
           "qui explique le commerce intrabranche entre économies "
           "comparables, que les avantages comparatifs ne prédisent pas.",
      mec=[("L’abaissement du coût moyen",
            "Avec des rendements croissants, produire davantage fait baisser "
            "le coût unitaire : l’accès à un marché plus vaste permet de "
            "franchir des seuils de production inatteignables dans un cadre "
            "national."),
           ("La variété offerte au consommateur",
            "La différenciation des produits fait que l’échange ne consiste "
            "pas à remplacer une production par une autre mais à élargir la "
            "gamme disponible : le gain porte sur le choix autant que sur le "
            "prix."),
           ("La condition de concurrence effective en aval",
            "La baisse des prix à l’importation n’atteint le consommateur que "
            "si la distribution et les marchés intérieurs sont eux-mêmes "
            "concurrentiels. Sinon, la baisse est captée en marges et le gain "
            "de pouvoir d’achat ne se matérialise pas.")],
      aut=[{'n': "Paul Krugman",
            'i': "Les rendements croissants fondent trois gains distincts : "
                 "coût moyen, variété, pression concurrentielle."}],
      termes=['economies d echelle', 'commerce intrabranche',
              'differenciation des produits'],
      dos=['n16-economies-echelle',
           'n16-commerce-interbranche-intrabranche']),

   nd('dynamique', 'L’argument dynamique', 'detail',
      "L’exposition internationale accélère l’apprentissage et la montée en "
      "gamme — à condition de pouvoir absorber les techniques étrangères.",
      grp=1, par='echelle',
      defi="L’argument dynamique porte sur la trajectoire plutôt que sur le "
           "niveau : l’exposition à la concurrence internationale contraint "
           "les producteurs à améliorer leurs procédés, et l’accès aux biens "
           "d’équipement et aux techniques étrangères accélère "
           "l’apprentissage. Il est le plus favorable au développement, mais "
           "aussi le plus conditionnel : il suppose une capacité "
           "d’absorption.",
      mec=[("La discipline par la concurrence",
            "Un producteur exposé ne peut pas répercuter durablement son "
            "inefficacité dans ses prix : l’ouverture agit comme un "
            "aiguillon permanent sur la productivité."),
           ("La condition de capacité d’absorption",
            "Le transfert technologique suppose un niveau de qualification, "
            "des infrastructures et des institutions permettant d’assimiler "
            "les techniques étrangères. Sans cela, l’ouverture donne accès à "
            "des produits importés sans produire de montée en gamme.")],
      args=[{'a': "L’argument dynamique explique que l’ouverture ait été "
                  "développante pour les économies dotées d’une base "
                  "éducative et institutionnelle, et décevante pour les "
                  "autres.",
             'lim': "Il rend la recommandation conditionnelle : ouvrir sans "
                    "capacité d’absorption revient à importer des produits "
                    "plutôt qu’à acquérir des capacités."}],
      faits=[{'f': "Les simulations de l’OMC de 2026 associent à une "
                   "coopération multilatérale renforcée un gain d’environ "
                   "+2,9 % de PIB mondial à l’horizon 2050, et d’environ "
                   "+7,7 % de PIB pour les pays les moins avancés.",
              'p': "L’ordre de grandeur donne une mesure contemporaine du "
                   "gain attendu de l’ouverture coordonnée, et indique que ce "
                   "gain est plus élevé pour les économies les plus pauvres."}],
      termes=['gains a l echange', 'montee en gamme', 'transfert de technologie'],
      dos=['le28-arguments-le', 'n16-gains-echange']),

   nd('reciprocite', 'La réciprocité et le cadre multilatéral', 'detail',
      "L’ouverture s’est faite par marchandage négocié : concessions "
      "réciproques, puis généralisation par la clause de la nation la plus "
      "favorisée.",
      grp=1, par='allocatif',
      defi="La réciprocité commerciale est le principe selon lequel une "
           "concession n’est accordée qu’en échange d’une concession "
           "équivalente. Elle explique la mécanique historique de "
           "l’ouverture : les rounds du GATT ont fait passer les droits de "
           "douane sur les produits manufacturés d’environ 40 % à environ "
           "4 %, chaque concession négociée étant ensuite généralisée par la "
           "clause de la nation la plus favorisée.",
      mec=[("Le marchandage comme moteur",
            "Chaque gouvernement obtient de ses exportateurs le soutien "
            "nécessaire pour accepter l’ouverture de son propre marché : la "
            "réciprocité rend l’ouverture politiquement finançable."),
           ("La généralisation multilatérale",
            "La clause de la nation la plus favorisée étend à tous les "
            "membres la concession accordée à l’un : le bilatéral devient "
            "multilatéral sans négociation supplémentaire."),
           ("La fragilité du dispositif",
            "La réciprocité canalisait les logiques mercantilistes en les "
            "rendant coopératives. Sa disparition libère les ripostes et "
            "transforme la négociation en rapport de force.")],
      faits=[{'f': "Le droit de douane moyen atteint 15,9 % du prix dans "
                   "l’agriculture contre environ 3 % dans l’industrie en 2019.",
              'p': "L’écart montre que les arguments favorables à l’ouverture "
                   "n’ont pas été appliqués uniformément : le secteur où les "
                   "pays en développement disposent d’avantages comparatifs "
                   "est précisément le plus protégé."}],
      aut=[{'n': "Paul Krugman",
            'i': "La réciprocité canalisait le mercantilisme ; sa disparition "
                 "libère les ripostes."}],
      termes=['reciprocite', 'nation la plus favorisee', 'gatt'],
      dos=['le28-reciprocite', 'n17-integration-economique']),

   # ------------------------------------- colonne 2 : les raisons de protéger
   nd('educateur', 'Le protectionnisme éducateur', 'pilier',
      "Protéger une industrie naissante le temps qu’elle franchisse le seuil "
      "d’échelle — et organiser ensuite sa propre disparition.",
      grp=2,
      defi="Le protectionnisme éducateur désigne la protection temporaire "
           "d’une industrie naissante, c’est-à-dire d’une branche qui n’est "
           "pas aujourd’hui compétitive mais qui peut le devenir une fois "
           "accumulés l’expérience et les volumes nécessaires. Trois traits "
           "le distinguent de toute autre protection : il vise une industrie "
           "en formation, il est justifié par un gain futur et non par la "
           "préservation d’un acquis, et il doit organiser sa propre "
           "disparition.",
      mec=[("Le seuil critique de production",
            "Il existe un volume au-delà duquel le coût moyen national "
            "descend sous le prix mondial. Tant que la production reste "
            "inférieure à ce seuil, le producteur est non compétitif ; "
            "au-delà, il l’est durablement. Le problème est de franchir le "
            "seuil, non de rattraper un retard d’efficacité."),
           ("Le report de la demande domestique",
            "Droits de douane ou restriction des importations réorientent la "
            "demande nationale vers les producteurs domestiques. La "
            "production augmente, ce qui déclenche les économies d’échelle et "
            "fait baisser le coût moyen."),
           ("L’apprentissage proprement éducateur",
            "Au-delà des économies d’échelle statiques, la production répétée "
            "améliore les procédés, forme la main-d’œuvre et consolide les "
            "réseaux de fournisseurs."),
           ("L’extinction de la protection",
            "Une fois le seuil franchi, la protection devient inutile et doit "
            "être supprimée. Maintenue, elle produit rente, lobbying, absence "
            "d’innovation et gaspillage des ressources.")],
      aut=[{'n': "Friedrich List",
            'i': "Le libre-échange peut figer les écarts de développement "
                 "lorsqu’une industrie naissante affronte immédiatement des "
                 "producteurs déjà compétitifs."},
           {'n': "Alexander Hamilton",
            'i': "La protection des industries naissantes est une condition "
                 "du développement industriel."},
           {'n': "Paul Krugman",
            'i': "Une industrie potentiellement compétitive peut ne jamais "
                 "émerger faute d’atteindre le seuil d’échelle."}],
      faits=[{'f': "L’Union européenne présente un retard dans certaines "
                   "technologies — numérique, semi-conducteurs, technologies "
                   "de la transition, certaines technologies vertes.",
              'p': "Un pays avancé peut être « en développement » relativement "
                   "à une frontière technologique sectorielle : l’argument "
                   "des industries naissantes se transpose alors à une "
                   "filière plutôt qu’à un pays."}],
      termes=['protectionnisme educateur', 'industrie naissante',
              'friedrich list'],
      dos=['le28-educateur', 'le28-temporaire-permanent']),

   nd('strategique', 'La politique commerciale stratégique', 'pilier',
      "Faire en sorte que le profit d’un secteur oligopolistique revienne à "
      "la firme nationale plutôt qu’à sa rivale : l’instrument est la "
      "subvention, pas la douane.",
      grp=2,
      defi="La politique commerciale stratégique désigne l’utilisation de "
           "l’intervention publique pour modifier l’issue de la concurrence "
           "entre quelques grandes firmes internationales. Développée par "
           "James Brander et Barbara Spencer en 1983, elle ne vise pas à "
           "protéger une industrie existante mais à faire en sorte que le "
           "profit disponible dans un secteur oligopolistique revienne à la "
           "firme nationale plutôt qu’à sa rivale étrangère.",
      mec=[("L’identification d’un marché oligopolistique",
            "Le secteur doit comporter des coûts fixes tels que seul un petit "
            "nombre de producteurs puisse être rentable à l’échelle "
            "mondiale : c’est cette rareté des places qui crée le profit à "
            "capter."),
           ("L’engagement public crédible",
            "L’État annonce un soutien — subvention, financement de la "
            "recherche, commande publique — assez ferme pour que le "
            "concurrent étranger le tienne pour acquis dans son propre "
            "calcul."),
           ("Le renoncement du rival",
            "Anticipant un concurrent soutenu, la firme étrangère conclut que "
            "son investissement ne serait pas rentable et renonce. Aucune "
            "barrière n’a été érigée : c’est l’anticipation qui a produit "
            "l’effet."),
           ("La riposte symétrique",
            "Si l’État étranger raisonne de même, les deux firmes "
            "investissent, le marché ne rentabilise pas les deux, et les deux "
            "pays supportent le coût de leur soutien sans capter le profit "
            "espéré.")],
      aut=[{'n': "James Brander",
            'i': "L’intervention publique modifie stratégiquement la "
                 "concurrence entre quelques grandes firmes internationales."},
           {'n': "Barbara Spencer",
            'i': "L’instrument pertinent relève largement de la subvention, "
                 "notamment à la recherche, plutôt que du droit de douane."}],
      faits=[{'f': "Le projet européen d’Industrial Accelerator Act prévoit "
                   "préférence européenne dans les marchés publics, "
                   "conditionnement des investissements étrangers et "
                   "exigences de transfert technologique.",
              'p': "Les instruments correspondent précisément à la boîte à "
                   "outils de la politique commerciale stratégique, appliquée "
                   "à l’échelle d’une union régionale plutôt que d’un État."}],
      termes=['politique commerciale strategique', 'brander spencer',
              'subventions'],
      dos=['le28-politique-strategique', 'le28-subventions']),

   nd('couts', 'Les coûts de l’ouverture', 'limite',
      "Destructions d’emplois concentrées, qualifications dépréciées, "
      "territoires dévitalisés : l’ajustement n’est ni instantané, ni "
      "gratuit, ni nécessairement complet.",
      grp=2,
      defi="Les coûts de l’ouverture désignent les pertes supportées pendant "
           "et après la réallocation des facteurs provoquée par la "
           "concurrence internationale : destructions d’emplois dans les "
           "branches exposées, dépréciation de qualifications devenues "
           "inutiles, dévitalisation de territoires spécialisés, coûts "
           "budgétaires de l’accompagnement. L’ajustement désigne le "
           "processus par lequel l’économie se réorganise ; il n’est ni "
           "instantané, ni gratuit, ni nécessairement complet.",
      mec=[("La dépréciation du capital humain spécifique",
            "Les qualifications acquises dans une branche ne sont pas "
            "intégralement transférables. Un salarié expérimenté peut se "
            "retrouver en concurrence avec des débutants dans un autre "
            "secteur, ce qui transforme une perte d’emploi en perte durable "
            "de revenu."),
           ("La concentration territoriale des pertes",
            "Les branches exposées sont souvent géographiquement "
            "concentrées : la fermeture d’un établissement réduit les revenus "
            "locaux, puis la demande adressée aux commerces et aux services, "
            "ce qui dévitalise un bassin d’emploi entier."),
           ("L’hystérèse de l’ajustement",
            "Plus l’épisode de chômage se prolonge, plus la réinsertion "
            "devient difficile : les compétences se dégradent et le signal "
            "envoyé aux employeurs se détériore. Un choc transitoire peut "
            "ainsi produire des effets durables."),
           ("Le décalage temporel entre gains et pertes",
            "La baisse des prix à l’importation est immédiate et diffuse ; "
            "les pertes d’emploi se matérialisent progressivement et sont "
            "concentrées. Le bilan social perçu est donc plus défavorable que "
            "le bilan comptable.")],
      aut=[{'n': "Dani Rodrik",
            'i': "La réponse au déclassement ne peut pas se limiter à la "
                 "réindustrialisation : il faut élever la qualité des emplois "
                 "de services, où se concentre l’emploi."},
           {'n': "Lionel Fontagné",
            'i': "Les effets de l’ouverture sont ambivalents et doivent être "
                 "évalués canal par canal."}],
      faits=[{'f': "L’ouverture s’est accompagnée, dans les économies "
                   "avancées, d’une désindustrialisation dont le cours "
                   "analyse les causes multiples — gains de productivité, "
                   "évolution de la demande, concurrence internationale.",
              'p': "Attribuer l’intégralité des pertes d’emploi industriel à "
                   "l’ouverture serait inexact : la part imputable au "
                   "commerce doit être distinguée de celle qui relève de la "
                   "productivité et de la tertiarisation."}],
      termes=['couts de l ouverture', 'desindustrialisation', 'ajustement'],
      dos=['le28-couts-ouverture', 'n10-polarisation']),

   nd('securite', 'La sécurité économique', 'detail',
      "Le critère n’est plus l’efficience mais la résilience : on accepte un "
      "surcoût en échange d’une réduction de vulnérabilité.",
      grp=2, par='strategique',
      defi="La protection au nom de la sécurité économique désigne les "
           "mesures destinées à réduire une dépendance jugée dangereuse, à "
           "préserver une capacité productive critique ou à sécuriser un "
           "approvisionnement stratégique. Son critère d’évaluation n’est pas "
           "l’efficience mais la résilience : elle accepte explicitement un "
           "surcoût en échange d’une réduction de vulnérabilité.",
      mec=[("L’identification de la dépendance critique",
            "Toutes les dépendances ne se valent pas : seule compte celle "
            "dont l’interruption produirait un dommage majeur et qui ne peut "
            "être compensée rapidement par un fournisseur alternatif."),
           ("L’asymétrie comme source de pouvoir",
            "Une dépendance réciproque constitue un verrou mutuel ; une "
            "dépendance unilatérale constitue une prise. C’est l’asymétrie, "
            "et non l’échange, qui crée la vulnérabilité."),
           ("Le coût de la rupture",
            "Raccourcir les chaînes de valeur augmente les coûts de "
            "production et peut élever les prix. Plus la rupture est brutale, "
            "plus le coût est élevé, car les entreprises doivent reconstruire "
            "très vite leurs approvisionnements.")],
      args=[{'a': "Le critère de résilience justifie des protections ciblées "
                  "sur un petit nombre de filières réellement critiques, "
                  "distinctes d’un protectionnisme généralisé.",
             'lim': "Le périmètre du stratégique est extensible : invoqué "
                    "sans critère, l’argument de sécurité peut couvrir "
                    "n’importe quelle demande de protection sectorielle."}],
      aut=[{'n': "Janet Yellen",
            'i': "La sécurité des approvisionnements est devenue un objectif "
                 "des politiques économiques."}],
      termes=['securite economique', 'souverainete', 'relocalisation'],
      dos=['le28-securite-souverainete', 'n17-dependances-strategiques']),

   # ------------------------------------------------- bas : ce qui tranche
   nd('conditions', 'Les cinq conditions de validité', 'sortie',
      "Mobilité des facteurs, échelle atteignable, concurrence en aval, "
      "capacité d’absorption, qualité de la spécialisation : c’est ici que se "
      "décide le diagnostic.",
      grp=3,
      defi="Les arguments favorables au libre-échange ne sont pas faux : ils "
           "sont conditionnels. Le cours énumère cinq conditions dont "
           "dépendent leurs conclusions, et c’est leur examen, pays par pays "
           "et secteur par secteur, qui tranche entre ouverture et "
           "protection. Un argument protectionniste solide identifie "
           "précisément laquelle de ces conditions fait défaut ; un argument "
           "protectionniste faible se contente d’invoquer la perte d’emplois.",
      mec=[("Mobilité des facteurs",
            "Sans réallocation effective du travail et du capital, le gain "
            "allocatif ne se réalise pas : il reste un gain de prix "
            "accompagné d’une perte d’emploi."),
           ("Échelle atteignable et concurrence en aval",
            "Si le seuil d’échelle n’est pas franchissable, l’ouverture "
            "consolide l’opérateur installé ; si la distribution n’est pas "
            "concurrentielle, la baisse des prix est captée en marges."),
           ("Absorption et qualité de la spécialisation",
            "Sans capacité d’absorption, l’ouverture importe des produits "
            "sans transférer de capacités ; et le gain statique reste "
            "compatible avec une spécialisation défavorable à long terme.")],
      args=[{'a': "Raisonner par conditions transforme un débat doctrinal en "
                  "diagnostic : on cesse d’être pour ou contre l’ouverture "
                  "pour déterminer dans quels secteurs et à quel rythme elle "
                  "est avantageuse.",
             'lim': "Le diagnostic reste contestable : les conditions sont "
                    "difficiles à mesurer, ce qui laisse une marge "
                    "d’appréciation que les intérêts organisés savent "
                    "exploiter."}],
      termes=['conditions de validite', 'mobilite des facteurs',
              'gains a l echange'],
      dos=['le28-arguments-le', 'le28-ouverture-progressive']),

   nd('representailles', 'Représailles et guerres commerciales', 'limite',
      "Chaque mesure en appelle une autre, les exportateurs les plus "
      "productifs perdent des débouchés, et les chaînes se réorganisent "
      "durablement.",
      grp=3,
      defi="Les représailles désignent les mesures qu’un pays adopte en "
           "réponse à une restriction commerciale décidée par un partenaire : "
           "relèvement de droits sur ses exportations, restrictions ciblées, "
           "suspension de concessions. Leur enchaînement produit une guerre "
           "commerciale, c’est-à-dire une escalade dans laquelle chaque "
           "mesure en appelle une autre.",
      mec=[("Le choix politique de la riposte",
            "Le partenaire choisit des produits dont la restriction maximise "
            "la pression politique : secteurs exportateurs concentrés, "
            "régions politiquement sensibles. La riposte vise le décideur "
            "autant que l’économie."),
           ("La perte sur les exportations",
            "Les producteurs exportateurs du pays initiateur, souvent plus "
            "productifs que le secteur protégé, perdent des débouchés : le "
            "bilan national peut devenir négatif alors même que la mesure a "
            "atteint son objectif sectoriel."),
           ("L’escalade et son irréversibilité partielle",
            "Chaque riposte appelle une contre-riposte, et reculer devient "
            "politiquement coûteux. Au-delà des flux visés, l’incertitude "
            "conduit les entreprises à réorganiser durablement leurs "
            "approvisionnements.")],
      aut=[{'n': "John Nash",
            'i': "La protection généralisée est un équilibre non coopératif "
                 "sous-optimal."},
           {'n': "Edward Luttwak",
            'i': "Après 1989, la rivalité de puissance change d’instruments : "
                 "la logique reste celle du conflit, la grammaire devient "
                 "celle du commerce."}],
      faits=[{'f': "Les estimations du FMI de 2023 chiffrent à environ "
                   "−0,3 % du PIB mondial un découplage stratégique limité, "
                   "et à environ −2,3 % une fragmentation en deux blocs, "
                   "jusqu’à −7 % en cas de transition brutale.",
              'p': "Ces ordres de grandeur donnent le coût agrégé d’une "
                   "escalade menée jusqu’à son terme, et montrent que la "
                   "rapidité de la rupture pèse autant que son ampleur."},
             {'f': "Entre 2010 et 2024, les importations des pays alliés des "
                   "États-Unis progressent de 40 % en provenance d’autres "
                   "alliés et reculent de 80 % avec les alliés de la Russie, "
                   "en évolution relative.",
              'p': "La réorientation montre que les tensions commerciales ne "
                   "se traduisent pas seulement par des droits de douane mais "
                   "par une recomposition durable de la géographie des "
                   "échanges."}],
      termes=['representailles', 'guerre commerciale',
              'fragmentation geoeconomique'],
      dos=['le28-representailles', 'le28-couts-protectionnisme']),
  ],
  [
   ln('question', 'allocatif', 'examinée d’abord par',
      "Le point de départ reste l’argument le plus robuste : la "
      "spécialisation selon les coûts comparés accroît la production "
      "disponible. Toute discussion sur la protection doit commencer par "
      "admettre ce gain avant d’en discuter les conditions.", 'conditionne'),
   ln('question', 'educateur', 'contestée d’abord par',
      "La première objection n’est pas que l’échange appauvrit, mais qu’il "
      "fige : une industrie potentiellement compétitive peut ne jamais "
      "émerger si elle affronte trop tôt des producteurs déjà installés.",
      'oppose'),
   ln('allocatif', 'echelle', 'complété par',
      "Les avantages comparatifs n’expliquent pas le commerce entre économies "
      "comparables. Les rendements croissants et la différenciation des "
      "produits rendent compte du commerce intrabranche, qui est la plus "
      "grande part des échanges entre pays développés.", 'renforce'),
   ln('echelle', 'dynamique', 'prolongé dans le temps par',
      "Au gain statique d’échelle s’ajoute un effet de trajectoire : "
      "l’exposition à la concurrence contraint à améliorer les procédés, et "
      "l’accès aux techniques étrangères accélère l’apprentissage — si la "
      "capacité d’absorption existe.", 'cause'),
   ln('allocatif', 'reciprocite', 'mis en œuvre par',
      "L’ouverture ne s’est pas faite par conviction théorique mais par "
      "marchandage : chaque concession a été échangée, puis généralisée par "
      "la clause de la nation la plus favorisée. Les droits manufacturiers "
      "sont passés d’environ 40 % à environ 4 %.", 'cause'),
   ln('echelle', 'educateur', 'fonde aussi',
      "Krugman réhabilite l’argument de List à partir des économies d’échelle "
      "plutôt que du retard national : le même mécanisme de rendements "
      "croissants qui fonde le gain à l’ouverture fonde aussi, avant le seuil "
      "critique, la protection temporaire.", 'oppose'),
   ln('educateur', 'strategique', 'se prolonge en',
      "Le protectionnisme éducateur vise une industrie en formation, la "
      "politique commerciale stratégique un profit oligopolistique à capter. "
      "Les deux reposent sur les rendements croissants, mais le second ne "
      "suppose aucun retard à rattraper.", 'cause'),
   ln('strategique', 'securite', 'rejoint',
      "Subventions, contenu local, commande publique et conditionnement des "
      "investissements étrangers servent indifféremment la captation d’un "
      "profit et la sécurisation d’un approvisionnement : les instruments "
      "sont les mêmes, les critères d’évaluation diffèrent.", 'renforce'),
   ln('couts', 'question', 'pèse sur',
      "Le bilan social perçu est plus défavorable que le bilan comptable, "
      "parce que les gains sont diffus et immédiats tandis que les pertes "
      "sont concentrées et différées. C’est cette asymétrie, et non le solde "
      "agrégé, qui décide politiquement.", 'limite'),
   ln('allocatif', 'couts', 'suppose une mobilité coûteuse',
      "Le gain allocatif exige que travail et capital quittent les branches "
      "en recul. Cette mobilité est coûteuse, lente et géographiquement "
      "inégale : lorsqu’elle fait défaut, il reste un gain de prix et une "
      "perte d’emploi simultanés.", 'limite'),
   ln('conditions', 'allocatif', 'borne',
      "Chacun des quatre arguments favorables à l’ouverture repose sur une "
      "condition explicite. Les énoncer sans les discuter revient à conclure "
      "avant d’avoir examiné : c’est la discussion des conditions qui fait la "
      "valeur de l’analyse.", 'limite'),
   ln('conditions', 'educateur', 'légitime ou disqualifie',
      "Un argument protectionniste solide identifie précisément laquelle des "
      "conditions fait défaut — ici, l’échelle atteignable. Un argument "
      "faible se contente d’invoquer la perte d’emplois, qui ne désigne "
      "aucune condition manquante.", 'conditionne'),
   ln('educateur', 'representailles', 'dégénère s’il se prolonge',
      "Maintenue au-delà du seuil, la protection produit rente, lobbying et "
      "absence d’innovation ; et comme toute restriction, elle appelle des "
      "représailles. La clause d’extinction n’est pas un détail : elle est la "
      "condition de légitimité du dispositif.", 'limite'),
   ln('representailles', 'conditions', 'change le contrefactuel',
      "Le coût de l’ouverture doit être comparé au coût de la protection, non "
      "à un état idéal sans ajustement. Les chiffrages du FMI — −0,3 % pour "
      "un découplage limité, −2,3 % pour une fragmentation en deux blocs — "
      "donnent cet ordre de grandeur.", 'mesure'),
   ln('securite', 'representailles', 'risque de servir de prétexte',
      "Le périmètre du stratégique est extensible. Invoqué sans critère, "
      "l’argument de sécurité couvre n’importe quelle demande sectorielle et "
      "alimente l’escalade qu’il prétendait prévenir.", 'limite'),
  ],
  bandes=[(1, 'Les gains de l’ouverture'),
          (2, 'Les raisons de protéger'),
          (3, 'Ce qui permet de trancher')],
  fam='Mondialisation et échanges')
