# -*- coding: utf-8 -*-
"""Ensemble 20 — Les changes et les déséquilibres internationaux (2/4)."""

from doss_base import d

d('n20-epargne-investissement-ouverte', 20,
  "Épargne et investissement en économie ouverte",
  "X − M = (S − I) + (T − G) : l’identité à connaître absolument",
  "En économie ouverte, le solde extérieur correspond à la somme du solde "
  "épargne-investissement privé et du solde budgétaire public. Le cours "
  "l’établit par l’identité X − M = (S − I) + (T − G), obtenue en combinant "
  "l’équilibre emplois-ressources et l’optique du revenu, et il en fait "
  "l’équation à connaître absolument pour analyser un déséquilibre "
  "extérieur.",
  "Le cours démontre cette identité en deux étapes qu’il faut savoir "
  "refaire. Première étape, l’équilibre emplois-ressources en économie "
  "ouverte : les ressources sont la production nationale et les "
  "importations, les emplois la consommation, l’investissement, les dépenses "
  "publiques et les exportations, d’où Y + M = C + I + G + X, que l’on "
  "réorganise en Y = C + I + G + X − M. Deuxième étape, l’optique du "
  "revenu : le revenu sert à consommer, à épargner et à payer les impôts, "
  "d’où Y = C + S + T. En égalisant les deux écritures et en simplifiant la "
  "consommation, on obtient X − M = (S − I) + (T − G), où X − M désigne le "
  "solde extérieur, S − I le solde épargne-investissement privé et T − G le "
  "solde budgétaire public. Le cours en tire immédiatement l’interprétation "
  "des déséquilibres. Si l’investissement dépasse l’épargne, l’épargne "
  "nationale ne suffit pas et le pays doit obtenir de l’épargne étrangère, "
  "d’où une entrée de capitaux ; si les dépenses publiques dépassent les "
  "recettes, il y a déficit public. Un déficit extérieur peut donc provenir "
  "soit d’un investissement supérieur à l’épargne privée, soit d’un déficit "
  "public, ces deux composantes déterminant ensemble le besoin de "
  "financement de la nation. Lorsque déficit public et déficit extérieur "
  "apparaissent simultanément, on parle de déficits jumeaux, le cours en "
  "donnant la relation causale : déficit public en hausse, demande "
  "intérieure en hausse, importations en hausse, déficit courant en hausse. "
  "Il en fournit trois épisodes américains : Reagan dans les années 1980, "
  "avec baisse des prélèvements et hausse des dépenses notamment de défense "
  "et de recherche, pour un déficit public de 5 % du produit intérieur brut "
  "en 1985 ; George W. Bush au début des années 2000, avec baisses d’impôts, "
  "dépenses militaires, guerre en Irak et éclatement de la bulle internet ; "
  "les mandats de Trump, avec une baisse des impôts dès 2017 et un déficit "
  "public de l’ordre de 6 % du produit intérieur brut depuis 2022. Mais le "
  "cours montre aussi que l’identité permet de lire un déficit "
  "positivement : si le budget public est équilibré et que X − M est "
  "négatif, alors S − I est négatif, donc l’investissement dépasse "
  "l’épargne, ce qui peut être une très bonne nouvelle si ce surcroît "
  "finance des infrastructures, des usines, l’éducation, "
  "l’industrialisation et la croissance future.",
  [("L’équilibre emplois-ressources en économie ouverte",
    "Les ressources sont la production nationale et les importations, les "
    "emplois la consommation, l’investissement, les dépenses publiques et "
    "les exportations : Y + M = C + I + G + X, soit Y = C + I + G + X − M."),
   ("L’optique du revenu",
    "Le revenu sert à consommer, à épargner et à payer les impôts : Y = C + "
    "S + T, où S désigne l’épargne et T les prélèvements nets. C’est la "
    "seconde écriture du même agrégat."),
   ("L’égalisation et la simplification",
    "En égalisant C + I + G + X − M et C + S + T, puis en simplifiant la "
    "consommation, on obtient X − M = (S − I) + (T − G) : le solde extérieur "
    "égale la somme du solde privé et du solde public."),
   ("La lecture du cas investissement supérieur à l’épargne",
    "Si l’investissement dépasse l’épargne, l’épargne nationale ne suffit "
    "pas et le pays doit obtenir de l’épargne étrangère : il en résulte une "
    "entrée de capitaux et un déficit extérieur."),
   ("La lecture du cas déficit public",
    "Si les dépenses publiques dépassent les recettes, le solde T − G est "
    "négatif, ce qui contribue directement au déficit extérieur sans "
    "qu’aucune insuffisance d’épargne privée ne soit nécessaire."),
   ("Le mécanisme des déficits jumeaux",
    "Le cours en donne la chaîne causale : déficit public en hausse, demande "
    "intérieure en hausse, importations en hausse, déficit courant en "
    "hausse. La relance publique fuit partiellement vers l’étranger."),
   ("La lecture positive du déficit",
    "Si le budget public est équilibré et que le solde extérieur est "
    "négatif, alors l’investissement dépasse l’épargne : le déficit finance "
    "des infrastructures, des usines, l’éducation et la croissance future.")],
  [{'a': "L’identité fournit un cadre rigoureux qui relie le solde extérieur "
         "au comportement d’épargne et au budget public.",
    'cond': "La rigueur suppose la démonstration du cours, par "
            "l’égalisation de l’équilibre emplois-ressources et de l’optique "
            "du revenu.",
    'lim': "L’identité est comptable : elle n’établit aucune causalité entre "
           "ses termes, seulement une égalité qui doit être vérifiée à chaque "
           "instant."},
   {'a': "Elle permet de distinguer deux origines très différentes d’un même déficit extérieur, privée et publique.",
    'cond': "La distinction suppose les deux cas du cours : investissement "
            "supérieur à l’épargne privée, ou dépenses publiques supérieures "
            "aux recettes.",
    'lim': "Les deux termes interagissent : le cours montre par les déficits "
           "jumeaux qu’un déficit public peut lui-même creuser le déficit "
           "extérieur par la demande intérieure."},
   {'a': "Elle permet une lecture positive du déficit extérieur lorsqu’il "
         "accompagne un fort investissement.",
    'cond': "La lecture suppose un budget public équilibré, de sorte que le "
            "déficit extérieur traduise exclusivement un excès "
            "d’investissement sur l’épargne.",
    'lim': "Cette lecture dépend de l’usage des fonds : le cours rappelle "
           "ailleurs que la dette peut aussi financer des dépenses "
           "improductives."},
   {'a': "Elle éclaire les excédents aussi bien que les déficits, en "
         "pointant un éventuel sous-investissement.",
    'cond': "L’argument suppose le cas allemand : un excédent courant qui "
            "reflète en partie une épargne élevée associée à un "
            "investissement public et privé insuffisant.",
    'lim': "Le cours ne mesure pas l’investissement optimal : qualifier un "
           "investissement d’insuffisant suppose une norme que l’identité ne "
           "fournit pas."},
   {'a': "Elle relie la politique budgétaire à la contrainte extérieure, ce "
         "qui en fait un outil d’analyse des politiques économiques.",
    'cond': "L’argument suppose le mécanisme des déficits jumeaux : une "
            "relance budgétaire stimule les revenus et la consommation, dont "
            "une partie se porte sur les importations.",
    'lim': "Le cours présente les déficits jumeaux comme une « hypothèse » : "
           "la relation n’est pas systématique et dépend de la propension à "
           "importer."}],
  [{'t': "L’identité X − M = (S − I) + (T − G) démontre que le déficit "
         "public cause le déficit extérieur.",
    'qui': "La lecture causale que le statut comptable de l’identité "
           "interdit.",
    'rep': "Le cours présente l’égalité comme une identité macroéconomique : "
           "elle montre que le solde extérieur correspond à la somme des "
           "deux soldes, et c’est séparément, par le mécanisme de la demande "
           "intérieure, qu’il établit l’hypothèse des déficits jumeaux."},
   {'t': "Un déficit extérieur est toujours le signe d’un problème "
         "d’épargne ou de gestion publique.",
    'qui': "La lecture que le cours corrige en montrant la lecture positive "
           "du déficit.",
    'rep': "Le cours objecte qu’un déficit peut révéler un fort dynamisme "
           "d’investissement : si le budget est équilibré et que le solde "
           "extérieur est négatif, l’investissement dépasse l’épargne et "
           "finance infrastructures, usines, éducation, industrialisation et "
           "croissance future."},
   {'t': "Un pays doit d’abord épargner avant d’investir : le recours à "
         "l’épargne étrangère est un pis-aller.",
    'qui': "La lecture que Nurkse et Rostow conduisent à nuancer.",
    'rep': "Le cours rappelle le cercle vicieux de la pauvreté selon "
           "Nurkse, « un pays est pauvre parce qu’il est pauvre », et le "
           "take-off de Rostow, qui suppose un taux d’investissement élevé, "
           "autour de 15 % du produit intérieur brut : lorsque l’épargne "
           "domestique est insuffisante, le financement extérieur peut être "
           "décisif."},
   {'t': "Un excédent courant traduit nécessairement un excès de compétitivité de l’économie concernée.",
    'qui': "La lecture que l’identité permet de renverser.",
    'rep': "Le cours montre qu’un excédent peut traduire S > I, donc un "
           "investissement insuffisant au regard de l’épargne : l’excédent "
           "courant allemand reflète en partie une épargne élevée associée à "
           "un investissement public et privé insuffisant, que l’Allemagne "
           "cherche à corriger."}],
  [{'n': "Ragnar Nurkse",
    'i': "« Un pays est pauvre parce qu’il est pauvre » : la faiblesse des "
         "revenus bloque l’épargne et donc l’investissement.",
    'p': "Le cours en détaille le cercle vicieux de la pauvreté : la "
         "faiblesse des revenus réduit l’épargne disponible, ce qui limite "
         "l’investissement et empêche les gains de productivité nécessaires "
         "au développement, d’où la nécessité de trouver une source de "
         "financement extérieure."},
   {'n': "Walt Rostow",
    'i': "Le take-off, c’est-à-dire le décollage économique, suppose un fort "
         "taux d’investissement.",
    'p': "Le cours retient un ordre de grandeur d’environ 15 % du produit "
         "intérieur brut, et en tire la conséquence pour l’économie "
         "ouverte : si l’épargne nationale est trop faible, "
         "l’investissement est impossible sans attirer l’épargne étrangère, "
         "ce que permet la globalisation financière."},
   {'n': "John Maynard Keynes",
    'i': "En économie ouverte, une partie du revenu créé par une relance "
         "fuit vers les importations.",
    'p': "Le cours en donne le mécanisme : dépense publique en hausse, "
         "revenus en hausse, consommation en hausse, mais une partie porte "
         "sur des importations, ce qui constitue une fuite hors du circuit "
         "national et réduit le multiplicateur tout en dégradant le solde "
         "extérieur."},
   {'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en tire la lecture des écarts épargne-investissement : "
         "aux États-Unis une croissance fondée sur une forte demande "
         "intérieure, un déficit public élevé et un investissement supérieur "
         "à l’épargne nationale ; en Chine une surépargne associée à un "
         "surinvestissement productif."}],
  [{'f': "L’identité s’obtient en combinant Y + M = C + I + G + X et Y = C + "
         "S + T, ce qui donne X − M = (S − I) + (T − G).",
    'p': "La démonstration établit que le solde extérieur est la somme du "
         "solde épargne-investissement privé et du solde budgétaire public, "
         "ce qui en fixe les deux origines possibles."},
   {'f': "Sous Reagan, la baisse des prélèvements et la hausse des dépenses, "
         "notamment de défense et de recherche, portent le déficit public à "
         "5 % du produit intérieur brut en 1985, tandis que le déficit "
         "extérieur se creuse dans un contexte de dollar fort et de "
         "concurrence japonaise.",
    'p': "Le fait fournit le premier grand épisode de déficits jumeaux et "
         "montre la concomitance des deux soldes."},
   {'f': "Dès 2017 puis dans les années 2020, les politiques budgétaires "
         "américaines portent le déficit public à environ 6 % du produit "
         "intérieur brut depuis 2022, avec en 2025 un déficit extérieur de "
         "plus de 1 200 milliards de dollars, soit environ 4 % du produit "
         "intérieur brut.",
    'p': "Les chiffres illustrent la persistance contemporaine des déficits "
         "jumeaux américains et l’ampleur du besoin de financement "
         "extérieur."},
   {'f': "Le taux d’épargne des ménages chinois dépasse 40 % du revenu "
         "disponible, pour trois raisons avancées : épargne de précaution "
         "face à une protection sociale moins développée, déséquilibres "
         "démographiques issus de la politique de l’enfant unique, et effet "
         "richesse négatif de la crise immobilière depuis 2020.",
    'p': "Le fait explique le terme S de l’identité dans le cas chinois et "
         "montre que l’épargne dépend d’institutions autant que de "
         "préférences."},
   {'f': "L’excédent courant allemand reflète en partie une épargne élevée "
         "associée à un investissement public et privé insuffisant, "
         "l’Allemagne évoquant un plan d’investissement de l’ordre de 500 "
         "milliards d’euros pour réduire l’écart entre épargne et "
         "investissement.",
    'p': "Le fait montre que l’identité permet de diagnostiquer un excédent "
         "comme un défaut d’investissement et non comme une performance."},
   {'f': "Rostow retient un taux d’investissement d’environ 15 % du produit "
         "intérieur brut comme condition du take-off, et Nurkse résume le "
         "blocage par la formule « un pays est pauvre parce qu’il est "
         "pauvre ».",
    'p': "Les deux références montrent pourquoi un déficit extérieur peut "
         "être normal au début du rattrapage, l’épargne domestique étant "
         "structurellement insuffisante."}],
  [{'q': "Sujet sur l’origine d’un déficit extérieur",
    'f': "Le cours impose de passer par l’identité macroéconomique. De "
         "l’équilibre emplois-ressources Y + M = C + I + G + X et de "
         "l’optique du revenu Y = C + S + T, on tire X − M = (S − I) + (T − "
         "G). Un déficit extérieur peut donc provenir soit d’un "
         "investissement supérieur à l’épargne privée, soit d’un déficit "
         "public, ces deux composantes déterminant ensemble le besoin de "
         "financement de la nation.",
    'r': "On montre que le déficit extérieur n’est pas d’abord un problème "
         "de compétitivité mais un écart entre épargne et emploi de cette "
         "épargne, ce qui déplace l’analyse vers le comportement des agents.",
    'ex': "Le cas où l’investissement dépasse l’épargne : le pays doit "
          "obtenir de l’épargne étrangère."},
   {'q': "Sujet sur les déficits jumeaux",
    'f': "Le cours en donne la définition et le mécanisme. Les déficits "
         "jumeaux correspondent à la coexistence d’un déficit budgétaire et "
         "d’un déficit courant, selon la relation déficit public en hausse, "
         "demande intérieure en hausse, importations en hausse, déficit "
         "courant en hausse. Les États-Unis en fournissent trois épisodes : "
         "Reagan dans les années 1980 avec 5 % du produit intérieur brut de "
         "déficit public en 1985, George W. Bush au début des années 2000, "
         "et les mandats de Trump avec environ 6 % depuis 2022.",
    'r': "On montre que le lien passe par la demande intérieure et la "
         "propension à importer, ce qui en fait une hypothèse conditionnelle "
         "et non une loi.",
    'ex': "Le déficit courant américain de plus de 1 200 milliards de "
          "dollars en 2025, soit environ 4 % du produit intérieur brut."},
   {'q': "Sujet demandant si un déficit extérieur est nécessairement "
         "préoccupant",
    'f': "Le cours répond par la négative dans deux cas. Le déficit peut "
         "d’abord être temporaire, provoqué par une hausse du prix du "
         "pétrole, un choc géopolitique ou une crise énergétique, et se "
         "résorber lorsque le choc disparaît. Il peut ensuite révéler un "
         "investissement élevé : si le budget public est équilibré et que X "
         "− M est négatif, alors I dépasse S, ce qui peut être une très "
         "bonne nouvelle puisque le pays finance infrastructures, usines, "
         "éducation, industrialisation et croissance future.",
    'r': "On montre que la nature du déficit importe plus que son montant, "
         "ce qui impose d’examiner l’usage des capitaux empruntés.",
    'ex': "Le take-off de Rostow, qui suppose un taux d’investissement "
          "d’environ 15 % du produit intérieur brut."},
   {'q': "Sujet sur le financement extérieur du développement",
    'f': "Le cours relie l’identité au développement. Nurkse décrit le "
         "cercle vicieux de la pauvreté : la faiblesse des revenus réduit "
         "l’épargne disponible, ce qui limite l’investissement et empêche "
         "les gains de productivité. Rostow montre que le take-off suppose "
         "un taux d’investissement élevé, autour de 15 % du produit "
         "intérieur brut. La globalisation financière peut casser ce cercle "
         "en permettant à un pays à faible épargne de recevoir l’épargne du "
         "reste du monde.",
    'r': "On montre que la mobilité des capitaux peut lever la contrainte "
         "d’épargne domestique, mais au prix d’une dépendance aux conditions "
         "financières internationales.",
    'ex': "Le recyclage des pétrodollars des années 1970, puis le "
          "retournement provoqué par le choc Volcker."}],
  voisins=['n20-capacite-besoin-financement', 'n20-solde-courant',
           'n20-desequilibres-mondiaux', 'n20-crise-change'])

d('n20-capacite-besoin-financement', 20,
  "Capacité et besoin de financement extérieur",
  "Prêteur ou emprunteur net vis-à-vis du reste du monde",
  "Un pays en déficit courant dépense davantage vis-à-vis du reste du monde "
  "qu’il ne reçoit : il est en besoin de financement, qu’il doit combler par "
  "des capitaux étrangers. Un pays en excédent courant dispose d’une épargne "
  "supérieure à ses besoins domestiques : il dégage une capacité de "
  "financement, qu’il emploie à acheter des actifs étrangers, à prêter au "
  "reste du monde ou à réaliser des investissements directs sortants.",
  "Le cours fait de cette notion le point de jonction entre le haut et le "
  "bas de la balance des paiements. Le mécanisme du besoin de financement "
  "est le suivant : si un pays présente un déficit courant, cela signifie "
  "qu’il dépense davantage vis-à-vis du reste du monde qu’il ne reçoit ; il "
  "est alors en besoin de financement, qu’il comble grâce à des capitaux "
  "étrangers, d’où l’enchaînement déficit courant, besoin de financement, "
  "entrée nette de capitaux. La situation inverse correspond à une capacité "
  "de financement : si le compte courant est positif, le pays dispose d’une "
  "épargne supérieure à ses besoins domestiques et peut acheter des actifs "
  "étrangers, prêter au reste du monde ou réaliser des investissements "
  "directs sortants, d’où l’enchaînement excédent courant, capacité de "
  "financement, sortie nette de capitaux. Le cours insiste sur le fait que "
  "cette relation n’est pas simplement comptable : elle se démontre à partir "
  "de l’équilibre emplois-ressources, qui conduit à l’identité X − M = (S − "
  "I) + (T − G). Un pays dont l’investissement dépasse l’épargne ou dont les "
  "dépenses publiques dépassent les recettes est donc nécessairement en "
  "besoin de financement. La question devient alors de savoir comment "
  "attirer durablement les capitaux nécessaires. Pour attirer les "
  "investissements directs, il faut des infrastructures de qualité, la "
  "stabilité politique, la sécurité juridique, une fiscalité attractive, un "
  "marché intéressant et une main-d’œuvre compétente, selon la logique "
  "attractivité du territoire, donc investissements directs entrants. Pour "
  "attirer les investissements de portefeuille, le pays doit proposer des "
  "actifs sûrs, des rendements intéressants et des taux d’intérêt "
  "suffisamment attractifs, les investisseurs recherchant un bon couple "
  "rendement et risque. Le financement d’un déficit extérieur dépend donc de "
  "l’attractivité du pays, qu’elle repose sur ses perspectives productives "
  "pour les investissements directs ou sur le couple rendement-risque de ses "
  "actifs financiers. Mais cette dépendance peut devenir dangereuse si les "
  "investisseurs changent brutalement de comportement : un sudden stop "
  "correspond à un arrêt brutal des entrées de capitaux étrangers, "
  "éventuellement accompagné de sorties massives, provoqué par une crise "
  "politique, une perte de confiance, une hausse du risque, un meilleur "
  "rendement ailleurs ou une modification des taux d’intérêt "
  "internationaux. Le risque est particulièrement fort quand les acteurs "
  "domestiques se sont endettés en devise étrangère.",
  [("Le constat du déficit courant",
    "Un déficit courant signifie que le pays dépense davantage vis-à-vis du "
    "reste du monde qu’il ne reçoit : il doit donc trouver des ressources "
    "financières extérieures pour couvrir cet écart."),
   ("Le besoin de financement et son financement",
    "Le pays est en besoin de financement, comblé grâce à des capitaux "
    "étrangers : déficit courant, besoin de financement, entrée nette de "
    "capitaux. Le haut et le bas de la balance se répondent."),
   ("La capacité de financement symétrique",
    "Si le compte courant est positif, le pays dispose d’une épargne "
    "supérieure à ses besoins domestiques : il peut acheter des actifs "
    "étrangers, prêter au reste du monde ou réaliser des investissements "
    "directs sortants."),
   ("La démonstration par l’identité macroéconomique",
    "La relation n’est pas simplement comptable : l’identité X − M = (S − I) "
    "+ (T − G) montre qu’un investissement supérieur à l’épargne ou un "
    "déficit public place nécessairement la nation en besoin de financement."),
   ("Les conditions d’attraction des investissements directs",
    "Pour financer son besoin, le pays doit rester attractif : "
    "infrastructures de qualité, stabilité politique, sécurité juridique, "
    "fiscalité attractive, marché intéressant, main-d’œuvre compétente."),
   ("Les conditions d’attraction des capitaux de portefeuille",
    "Les investisseurs de portefeuille recherchent un bon couple rendement "
    "et risque : le pays doit proposer des actifs sûrs, des rendements "
    "intéressants et des taux d’intérêt suffisamment attractifs."),
   ("La fragilité révélée par le sudden stop",
    "Un sudden stop est un arrêt brutal des entrées de capitaux étrangers, "
    "éventuellement accompagné de sorties massives, provoqué par une crise "
    "politique, une perte de confiance, une hausse du risque ou une "
    "modification des taux internationaux.")],
  [{'a': "La notion relie directement le solde courant au compte financier, "
         "ce qui unifie la lecture de la balance des paiements.",
    'cond': "L’unification suppose la correspondance établie par le cours "
            "entre le haut et le bas de la balance.",
    'lim': "La correspondance est comptable : elle garantit que le déficit "
           "est financé, non qu’il l’est à des conditions acceptables."},
   {'a': "Elle se démontre à partir de l’équilibre emplois-ressources, ce "
         "qui lui donne un fondement théorique et non seulement comptable.",
    'cond': "La démonstration suppose l’identité X − M = (S − I) + (T − G), "
            "obtenue en combinant les deux écritures du revenu.",
    'lim': "L’identité ne dit pas quelle composante est à l’origine du "
           "déséquilibre : elle juxtapose les soldes sans les hiérarchiser."},
   {'a': "Elle déplace la question de la compétitivité vers celle de "
         "l’attractivité financière du territoire.",
    'cond': "Le déplacement suppose la liste du cours : infrastructures, "
            "stabilité politique, sécurité juridique, fiscalité, marché, "
            "qualification de la main-d’œuvre.",
    'lim': "Cette attractivité peut entrer en conflit avec d’autres "
           "objectifs : le cours montre ailleurs que la concurrence pour "
           "attirer les capitaux peut conduire au moins-disant fiscal."},
   {'a': "Elle distingue les types de capitaux selon leur stabilité, ce qui "
         "qualifie la fragilité du financement.",
    'cond': "La distinction suppose le constat du cours : les "
            "investissements de portefeuille sont très mobiles, les "
            "investissements directs beaucoup plus durables puisqu’une usine "
            "ne se déplace pas en quelques secondes.",
    'lim': "Même les investissements directs peuvent se retirer à moyen "
           "terme : le cours souligne que la firme déplace les activités dès "
           "que les coûts augmentent."},
   {'a': "Elle fait apparaître un risque identifiable, le sudden stop, ce "
         "qui rend la vulnérabilité analysable.",
    'cond': "Le risque suppose les causes énumérées par le cours : crise "
            "politique, perte de confiance, hausse du risque, meilleur "
            "rendement ailleurs, modification des taux d’intérêt "
            "internationaux.",
    'lim': "Le cours ne fournit pas d’indicateur d’alerte : le sudden stop "
           "est par nature brutal et difficile à anticiper."}],
  [{'t': "Puisque la balance des paiements est équilibrée, un besoin de "
         "financement est automatiquement couvert et ne pose pas problème.",
    'qui': "La lecture que le cours corrige en traitant la soutenabilité.",
    'rep': "Le cours objecte qu’un déficit courant n’est soutenable que si "
           "le pays parvient à attirer durablement les capitaux étrangers "
           "nécessaires à son financement, et qu’un sudden stop, arrêt "
           "brutal des entrées de capitaux, peut provoquer une crise de "
           "financement dans une économie dépendante des capitaux "
           "extérieurs."},
   {'t': "Tous les capitaux étrangers se valent pour financer un besoin de financement extérieur durable.",
    'qui': "La lecture que la distinction des types de capitaux corrige.",
    'rep': "Le cours distingue : les investissements de portefeuille sont "
           "très mobiles et peuvent se retirer lorsque le risque augmente, "
           "tandis que les investissements directs sont beaucoup plus "
           "durables parce qu’une usine ne peut pas être déplacée en "
           "quelques secondes."},
   {'t': "Une capacité de financement est toujours préférable, pour une nation, à un besoin de financement.",
    'qui': "La lecture que la critique de l’excédent allemand relativise.",
    'rep': "Le cours objecte qu’un excédent courant peut refléter une "
           "épargne élevée associée à un investissement public et privé "
           "insuffisant, et qu’un besoin de financement peut au contraire "
           "accompagner un fort dynamisme d’investissement finançant "
           "infrastructures, usines, éducation et croissance future."},
   {'t': "Un pays en besoin de financement n’a qu’à offrir des taux "
         "d’intérêt plus élevés pour attirer les capitaux nécessaires.",
    'qui': "La lecture que les conditions d’attractivité du cours "
           "complètent.",
    'rep': "Le cours montre que l’attractivité repose aussi sur les "
           "infrastructures, la stabilité politique, la sécurité juridique, "
           "la taille du marché et la qualification de la main-d’œuvre, et "
           "qu’un taux élevé accroît par ailleurs la charge de la dette, "
           "donc le risque perçu."}],
  [{'n': "Walt Rostow",
    'i': "Le décollage économique suppose un taux d’investissement élevé.",
    'p': "Le cours retient un ordre de grandeur d’environ 15 % du produit "
         "intérieur brut et en tire la conséquence pour l’économie ouverte : "
         "si l’épargne nationale est trop faible, l’investissement est "
         "impossible sans attirer l’épargne étrangère, c’est-à-dire sans se "
         "placer en besoin de financement."},
   {'n': "Ragnar Nurkse",
    'i': "« Un pays est pauvre parce qu’il est pauvre » : la faiblesse de "
         "l’épargne bloque le développement.",
    'p': "Le cours en détaille le cercle vicieux : la faiblesse des revenus "
         "réduit l’épargne disponible, ce qui limite l’investissement et "
         "empêche les gains de productivité nécessaires au développement, "
         "d’où la nécessité d’une source de financement extérieure."},
   {'n': "Paul Volcker",
    'i': "La forte hausse des taux américains de 1979 redirige les capitaux "
         "mondiaux vers les États-Unis.",
    'p': "Le cours en donne le mécanisme : taux américains en hausse, "
         "placements américains plus attractifs, capitaux quittant les "
         "économies émergentes, de sorte que les pays en développement qui "
         "dépendaient de ces entrées connaissent un sudden stop."},
   {'n': "Charles-Albert Michalet",
    'i': "Les États cherchent à séduire les firmes multinationales pour "
         "attirer leurs investissements.",
    'p': "Le cours relie La Séduction des nations, en 1999, au financement "
         "du besoin extérieur : pour attirer les investissements directs, il "
         "faut des infrastructures de qualité, la stabilité politique, la "
         "sécurité juridique, une fiscalité attractive, un marché "
         "intéressant et une main-d’œuvre compétente."}],
  [{'f': "Le cours formule les deux enchaînements symétriques : déficit "
         "courant, besoin de financement, entrée nette de capitaux ; "
         "excédent courant, capacité de financement, sortie nette de "
         "capitaux.",
    'p': "Les deux schémas établissent la correspondance entre le haut et le "
         "bas de la balance des paiements et fondent toute l’analyse du "
         "financement extérieur."},
   {'f': "Pour attirer les investissements directs, le cours exige des "
         "infrastructures de qualité, la stabilité politique, la sécurité "
         "juridique, une fiscalité attractive, un marché intéressant et une "
         "main-d’œuvre compétente.",
    'p': "L’énumération montre que le financement d’un déficit extérieur "
         "dépend de l’attractivité productive du territoire et non seulement "
         "de son rendement financier."},
   {'f': "Pour attirer les investissements de portefeuille, le pays doit "
         "proposer des actifs sûrs, des rendements intéressants et des taux "
         "d’intérêt suffisamment attractifs, les investisseurs recherchant "
         "un bon couple rendement et risque.",
    'p': "Le fait montre la seconde voie de financement et explique "
         "pourquoi le niveau des taux d’intérêt pèse sur la contrainte "
         "extérieure."},
   {'f': "Un sudden stop correspond à un arrêt brutal des entrées de "
         "capitaux étrangers, pouvant s’accompagner de sorties massives, du "
         "fait d’une crise politique, d’une perte de confiance, d’une hausse "
         "du risque, d’un meilleur rendement ailleurs ou d’une modification "
         "des taux d’intérêt internationaux.",
    'p': "Le fait nomme et explique le risque principal attaché à un besoin de financement durable, dont la plupart des déclencheurs échappent au pays concerné."},
   {'f': "Les investissements de portefeuille sont très mobiles tandis que "
         "les investissements directs sont beaucoup plus durables, parce "
         "qu’une usine ne peut pas être déplacée en quelques secondes.",
    'p': "La distinction démontre que la composition du financement, et pas "
         "seulement son montant, détermine la fragilité d’une économie."},
   {'f': "Le compte financier français de 2025 fait apparaître des sorties "
         "nettes de 31 milliards d’euros au titre des investissements "
         "directs et de 133 milliards au titre des investissements de "
         "portefeuille, contre une entrée nette de 185 milliards au titre "
         "des autres investissements.",
    'p': "La lecture montre comment un besoin de financement se couvre "
         "concrètement, et que les postes du compte financier peuvent jouer "
         "en sens contraires."}],
  [{'q': "Sujet sur le financement du déséquilibre extérieur",
    'f': "Le cours établit la correspondance entre les deux moitiés de la "
         "balance. Un déficit courant signifie que le pays dépense davantage "
         "vis-à-vis du reste du monde qu’il ne reçoit : il est en besoin de "
         "financement, qu’il comble grâce à des capitaux étrangers. Un "
         "excédent courant signifie à l’inverse qu’il dispose d’une épargne "
         "supérieure à ses besoins domestiques et dégage une capacité de "
         "financement, utilisable pour acheter des actifs étrangers, prêter "
         "au reste du monde ou investir directement à l’étranger.",
    'r': "On montre que le solde courant détermine la position de prêteur ou "
         "d’emprunteur net de la nation, ce qui relie le commerce au "
         "financement international.",
    'ex': "Le compte financier français de 2025, presque équilibré à environ "
          "8 milliards d’euros."},
   {'q': "Sujet sur les conditions du financement extérieur",
    'f': "Le cours distingue deux voies. Pour attirer les investissements "
         "directs, il faut des infrastructures de qualité, la stabilité "
         "politique, la sécurité juridique, une fiscalité attractive, un "
         "marché intéressant et une main-d’œuvre compétente. Pour attirer "
         "les investissements de portefeuille, il faut proposer des actifs "
         "sûrs, des rendements intéressants et des taux d’intérêt "
         "suffisamment attractifs. Le financement d’un déficit dépend donc "
         "de l’attractivité du pays, productive ou financière.",
    'r': "On montre que la contrainte extérieure est une contrainte "
         "d’attractivité, ce qui explique que les politiques de "
         "compétitivité et d’attractivité soient liées.",
    'ex': "Le couple rendement-risque recherché par les investisseurs de "
          "portefeuille."},
   {'q': "Sujet sur les risques d’une dépendance au financement étranger",
    'f': "Le cours nomme le risque principal. Un sudden stop correspond à un "
         "arrêt brutal des entrées de capitaux étrangers, pouvant "
         "s’accompagner de sorties massives, provoqué par une crise "
         "politique, une perte de confiance, une hausse du risque, un "
         "meilleur rendement ailleurs ou une modification des taux "
         "internationaux. Ce risque est particulièrement fort quand les "
         "acteurs domestiques se sont endettés dans une devise étrangère, "
         "puisqu’une dépréciation alourdit mécaniquement la dette.",
    'r': "On montre que la vulnérabilité dépend de la composition du "
         "financement et de la devise d’endettement, ce qui distingue des "
         "situations de déficit apparemment comparables.",
    'ex': "Le choc Volcker de 1979, qui fait des États-Unis une « pompe "
          "aspirante » à capitaux."},
   {'q': "Sujet demandant si un besoin de financement est préoccupant",
    'f': "Le cours refuse la réponse univoque. Un déficit peut être "
         "temporaire, provoqué par une hausse du prix du pétrole, un choc "
         "géopolitique ou une crise énergétique. Il peut aussi révéler un "
         "investissement élevé : avec un budget équilibré, X − M négatif "
         "implique I supérieur à S, donc un pays qui finance "
         "infrastructures, usines, éducation, industrialisation et "
         "croissance future. Nurkse et Rostow montrent même qu’au début du "
         "rattrapage, le recours à l’épargne étrangère peut être décisif.",
    'r': "On montre que la soutenabilité dépend de l’usage des capitaux et "
         "de la stabilité de leur source, et non du signe du solde.",
    'ex': "Le take-off de Rostow, supposant un taux d’investissement "
          "d’environ 15 % du produit intérieur brut."}],
  voisins=['n20-solde-courant', 'n20-epargne-investissement-ouverte',
           'n20-crise-change', 'n20-position-exterieure-nette'])

d('n20-desequilibres-mondiaux', 20, "Déséquilibres mondiaux",
  "Des stratégies de croissance déséquilibrées, pas des anomalies comptables",
  "Les déséquilibres mondiaux désignent la coexistence durable de grands "
  "excédents et de grands déficits courants entre zones économiques. Le "
  "cours en retient la lecture d’Hélène Rey : les déséquilibres excessifs "
  "sont la conséquence de stratégies nationales de croissance elles-mêmes "
  "déséquilibrées, aux États-Unis, en Chine, dans l’Union européenne et chez "
  "les pays exportateurs de pétrole.",
  "Le cours construit les déséquilibres mondiaux comme un problème de "
  "modèles de croissance et non de comptabilité. L’idée essentielle, qu’il "
  "attribue à Hélène Rey, est que les déséquilibres mondiaux excessifs sont "
  "la conséquence de stratégies nationales de croissance elles-mêmes "
  "déséquilibrées : les déséquilibres extérieurs ne sont pas de simples "
  "anomalies comptables, ils reflètent les faiblesses structurelles des "
  "modèles de croissance nationaux. Le cours décline alors ces faiblesses. "
  "Les États-Unis d’abord : un déficit public proche de 6 % du produit "
  "intérieur brut, donc des dépenses publiques supérieures aux recettes, ce "
  "qui contribue directement au déficit extérieur, et un investissement "
  "supérieur à l’épargne nationale, ce qui rend nécessaire l’entrée de "
  "capitaux étrangers ; leur croissance est donc fondée sur une forte "
  "demande intérieure, un déficit public élevé et l’épargne étrangère. La "
  "Chine ensuite, à l’opposé : un taux d’épargne des ménages dépassant 40 % "
  "du revenu disponible, pour trois raisons avancées — une épargne de "
  "précaution liée à une protection sociale relativement moins développée, "
  "les déséquilibres démographiques issus de la politique de l’enfant "
  "unique, et l’effet richesse négatif de la crise immobilière depuis "
  "environ 2020 — mais aussi un investissement productif massif dans "
  "l’industrie, les technologies, les infrastructures et les capacités de "
  "production, alors que la demande interne ne progresse pas aussi vite : "
  "c’est une situation de surcapacité productive. Celle-ci produit deux "
  "conséquences : une pression déflationniste, l’offre excédant la demande, "
  "ce qui renforce encore la compétitivité-prix des exportations chinoises ; "
  "et la nécessité d’exporter les surplus. L’Allemagne enfin : son excédent "
  "courant reflète en partie une épargne élevée associée à un investissement "
  "public et privé insuffisant, ce qu’elle cherche désormais à corriger en "
  "assouplissant ses contraintes budgétaires pour financer infrastructures, "
  "transition énergétique, autonomie stratégique et défense, un vaste plan "
  "d’investissement de l’ordre de 500 milliards d’euros étant évoqué, "
  "l’objectif étant de réduire l’écart entre épargne et investissement et "
  "donc potentiellement l’excédent courant. Le cours conclut que l’obstacle "
  "principal à la résorption des déséquilibres mondiaux est politique : les "
  "solutions économiques sont connues, mais elles supposent une "
  "coordination précisément rendue difficile par la fragmentation "
  "géopolitique actuelle.",
  [("La lecture par les modèles de croissance",
    "Les déséquilibres mondiaux excessifs sont la conséquence de stratégies "
    "nationales de croissance elles-mêmes déséquilibrées : ils reflètent les "
    "faiblesses structurelles de ces modèles et non de simples écarts "
    "comptables."),
   ("Le déficit américain par la demande et le budget",
    "Un déficit public proche de 6 % du produit intérieur brut et un "
    "investissement supérieur à l’épargne nationale rendent nécessaire "
    "l’entrée de capitaux étrangers : la croissance américaine est fondée "
    "sur la demande intérieure et l’épargne du reste du monde."),
   ("La surépargne chinoise",
    "Le taux d’épargne des ménages chinois dépasse 40 % du revenu "
    "disponible, du fait d’une épargne de précaution liée à une protection "
    "sociale moins développée, de déséquilibres démographiques et de l’effet "
    "richesse négatif de la crise immobilière."),
   ("Le surinvestissement et la surcapacité",
    "La Chine investit massivement dans l’industrie, les technologies, les "
    "infrastructures et les capacités de production, alors que la demande "
    "interne ne progresse pas aussi vite : les capacités dépassent la "
    "consommation domestique."),
   ("La pression déflationniste et l’exportation des surplus",
    "Quand l’offre dépasse la demande, les prix subissent une pression à la "
    "baisse, ce qui renforce la compétitivité-prix des produits chinois et "
    "oblige à vendre une partie de la production à l’étranger."),
   ("L’excédent allemand par le sous-investissement",
    "L’excédent courant allemand reflète en partie une épargne élevée "
    "associée à un investissement public et privé insuffisant, d’où la "
    "volonté d’assouplir les contraintes budgétaires pour investir."),
   ("L’obstacle politique à la résorption",
    "Les solutions économiques sont connues, mais elles supposent une "
    "coordination précisément rendue difficile par la fragmentation "
    "géopolitique actuelle : l’obstacle principal est politique.")],
  [{'a': "La notion déplace l’analyse des soldes vers les modèles de "
         "croissance, ce qui en fait un objet économique et non comptable.",
    'cond': "Le déplacement suppose la thèse d’Hélène Rey reprise par le "
            "cours : les déséquilibres reflètent les faiblesses "
            "structurelles des modèles nationaux.",
    'lim': "Qualifier un modèle de déséquilibré suppose une norme "
           "d’équilibre que le cours ne définit pas précisément."},
   {'a': "Elle identifie des mécanismes nationaux précis, ce qui évite les "
         "généralités sur la mondialisation.",
    'cond': "L’argument suppose les trois cas détaillés du cours : "
            "États-Unis, Chine, Allemagne, avec leurs chiffres respectifs.",
    'lim': "Les quatre zones citées — États-Unis, Chine, Union européenne, "
           "pays exportateurs de pétrole — ne sont pas toutes traitées avec "
           "le même détail."},
   {'a': "Elle relie les déséquilibres extérieurs aux institutions "
         "domestiques, notamment à la protection sociale.",
    'cond': "L’argument suppose l’explication chinoise du cours : une "
            "protection sociale relativement moins développée élève "
            "l’incertitude et donc l’épargne de précaution.",
    'lim': "Le cours présente trois raisons dont il ne hiérarchise pas "
           "l’importance, et il avertit que le détail démographique importe "
           "moins que le mécanisme."},
   {'a': "Elle montre que les déséquilibres ont des effets sur les prix "
         "mondiaux et pas seulement sur les soldes.",
    'cond': "L’argument suppose l’enchaînement du cours : surcapacité, "
            "pression à la baisse sur les prix, déflation, compétitivité-prix "
            "chinoise renforcée.",
    'lim': "Le cours ne mesure pas l’ampleur de cette pression "
           "déflationniste sur les prix mondiaux, il en décrit la direction."},
   {'a': "Elle fait apparaître l’obstacle décisif à la résorption, qui est politique et non technique.",
    'cond': "L’argument suppose la conclusion du cours : les solutions "
            "économiques sont connues mais supposent une coordination rendue "
            "difficile par la fragmentation géopolitique.",
    'lim': "Cette conclusion rend l’analyse peu prédictive : elle explique "
           "l’absence de résorption sans indiquer à quelle condition elle "
           "pourrait advenir."}],
  [{'t': "Les déséquilibres mondiaux sont des anomalies comptables qui se "
         "corrigent spontanément par les taux de change.",
    'qui': "La lecture que la thèse d’Hélène Rey reprise par le cours "
           "réfute.",
    'rep': "Le cours objecte que les déséquilibres extérieurs mondiaux ne "
           "sont pas de simples anomalies comptables : ils reflètent les "
           "faiblesses structurelles des modèles de croissance nationaux, aux "
           "États-Unis, en Chine, dans l’Union européenne et chez les pays "
           "exportateurs de pétrole."},
   {'t': "Le déficit américain résulte d’une concurrence déloyale de ses "
         "partenaires commerciaux.",
    'qui': "La lecture que le cours corrige par l’analyse de l’épargne et du "
           "budget américains.",
    'rep': "Le cours impute le déficit américain à un modèle interne : un "
           "déficit public proche de 6 % du produit intérieur brut et un "
           "investissement supérieur à l’épargne nationale, ce qui rend "
           "nécessaire l’entrée de capitaux étrangers et traduit une "
           "croissance fondée sur la demande intérieure."},
   {'t': "L’excédent commercial chinois provient essentiellement de salaires artificiellement bas.",
    'qui': "La lecture que le cours complète par la surépargne et la "
           "surcapacité.",
    'rep': "Le cours impute l’excédent chinois à un taux d’épargne des "
           "ménages dépassant 40 % du revenu disponible et à un "
           "investissement productif massif dépassant les capacités "
           "d’absorption de la demande intérieure : c’est une situation de "
           "surcapacité productive, non un simple avantage salarial."},
   {'t': "L’excédent courant allemand atteste à lui seul la réussite de son modèle exportateur.",
    'qui': "La lecture que le cours nuance en analysant l’investissement "
           "allemand.",
    'rep': "Le cours objecte que l’excédent allemand reflète en partie une "
           "épargne élevée associée à un investissement public et privé "
           "insuffisant, et que l’Allemagne cherche désormais à corriger ce "
           "sous-investissement par un plan de l’ordre de 500 milliards "
           "d’euros, ce qui réduirait son excédent."}],
  [{'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en fait la thèse centrale de la section : les "
         "déséquilibres extérieurs mondiaux ne sont pas de simples anomalies "
         "comptables mais révèlent les faiblesses structurelles des modèles "
         "de croissance nationaux, les principales zones concernées étant les "
         "États-Unis, la Chine, l’Union européenne et les pays exportateurs "
         "de pétrole."},
   {'n': "John Maynard Keynes",
    'i': "La demande intérieure et la propension à importer déterminent le "
         "solde extérieur.",
    'p': "Le cours en donne le mécanisme appliqué aux déséquilibres : une "
         "relance budgétaire stimule les revenus et la consommation, dont "
         "une partie se porte sur les importations, ce qui détériore le "
         "solde extérieur et explique le lien entre déficit public et "
         "déficit courant."},
   {'n': "Branko Milanovic",
    'i': "La courbe de l’éléphant montre des gagnants et des perdants très "
         "inégalement répartis de la mondialisation.",
    'p': "Le cours en tire trois groupes : les classes moyennes émergentes "
         "et le top 1 % mondial comme grands gagnants, les classes "
         "populaires des pays développés comme perdants relatifs, ce qui "
         "explique en partie que la contestation politique accompagne les "
         "déséquilibres."},
   {'n': "Paul Volcker",
    'i': "Une forte hausse des taux américains redirige brutalement les "
         "capitaux mondiaux.",
    'p': "Le cours en donne le mécanisme de 1979 : taux américains en "
         "hausse, placements américains plus attractifs, capitaux quittant "
         "les économies émergentes, de sorte que les États-Unis deviennent "
         "une « pompe aspirante » à capitaux et que les pays dépendants "
         "connaissent un sudden stop."}],
  [{'f': "Le déficit public américain est proche de 6 % du produit intérieur "
         "brut, et le déficit courant dépasse 1 200 milliards de dollars en "
         "2025, soit environ 4 % du produit intérieur brut.",
    'p': "Les chiffres établissent l’ampleur du déséquilibre américain et "
         "montrent la simultanéité du déficit public et du déficit "
         "extérieur."},
   {'f': "Le taux d’épargne des ménages chinois dépasse 40 % du revenu "
         "disponible, un niveau exceptionnellement élevé, pour trois raisons "
         "avancées : épargne de précaution, déséquilibre démographique issu "
         "de la politique de l’enfant unique, effet richesse négatif de la "
         "crise immobilière depuis environ 2020.",
    'p': "Le chiffre explique le terme d’épargne dans l’identité "
         "macroéconomique et montre que l’excédent chinois s’enracine dans "
         "des institutions domestiques."},
   {'f': "La Chine investit massivement dans l’industrie, les technologies, "
         "les infrastructures et les capacités de production, mais la "
         "demande interne ne progresse pas aussi vite : les capacités de "
         "production dépassent la consommation domestique.",
    'p': "Le fait établit la surcapacité productive et explique la "
         "nécessité d’exporter les surplus."},
   {'f': "Quand l’offre dépasse la demande, les prix subissent une pression "
         "à la baisse : la déflation chinoise renforce ainsi la "
         "compétitivité-prix de ses exportations sur les marchés "
         "internationaux.",
    'p': "Le fait montre que le déséquilibre chinois s’exporte par les prix "
         "autant que par les volumes, ce qui alimente les tensions "
         "commerciales."},
   {'f': "L’Allemagne cherche à assouplir ses contraintes budgétaires pour "
         "financer infrastructures, transition énergétique, autonomie "
         "stratégique et défense, un vaste plan d’investissement de l’ordre "
         "de 500 milliards d’euros étant évoqué.",
    'p': "Le fait montre qu’un pays excédentaire peut corriger son "
         "déséquilibre par l’investissement domestique, ce qui réduirait "
         "l’écart entre épargne et investissement."},
   {'f': "L’obstacle principal à la résorption des déséquilibres mondiaux "
         "est politique : les solutions économiques sont connues mais elles "
         "supposent une coordination rendue difficile par la fragmentation "
         "géopolitique actuelle.",
    'p': "Le fait explique la persistance des déséquilibres malgré "
         "l’existence de remèdes identifiés, et relie la question à la "
         "fragmentation géoéconomique."}],
  [{'q': "Sujet sur les causes des déséquilibres mondiaux",
    'f': "Le cours retient la lecture d’Hélène Rey : les déséquilibres "
         "mondiaux excessifs sont la conséquence de stratégies nationales de "
         "croissance elles-mêmes déséquilibrées, et non de simples anomalies "
         "comptables. Les États-Unis ont une croissance fondée sur une forte "
         "demande intérieure, un déficit public proche de 6 % du produit "
         "intérieur brut et un investissement supérieur à l’épargne "
         "nationale. La Chine combine une surépargne des ménages dépassant "
         "40 % du revenu disponible et un surinvestissement productif.",
    'r': "On montre que les soldes extérieurs sont le miroir de choix "
         "domestiques d’épargne, d’investissement et de protection sociale, "
         "ce qui déplace la solution vers les politiques internes.",
    'ex': "La surcapacité productive chinoise, où les capacités dépassent la "
          "consommation domestique."},
   {'q': "Sujet sur la résorption des déséquilibres extérieurs",
    'f': "Le cours identifie un obstacle qui n’est pas économique. "
         "L’obstacle principal à la résorption des déséquilibres mondiaux "
         "est politique : les solutions économiques sont connues, mais elles "
         "supposent une coordination précisément rendue difficile par la "
         "fragmentation géopolitique actuelle. Le cas allemand montre "
         "pourtant qu’une correction est possible, puisque l’assouplissement "
         "budgétaire et un plan d’investissement de l’ordre de 500 milliards "
         "d’euros réduiraient l’écart entre épargne et investissement.",
    'r': "On montre que l’ajustement suppose une action simultanée des "
         "excédentaires et des déficitaires, donc une coordination que la "
         "rivalité géopolitique empêche.",
    'ex': "Le plan allemand finançant infrastructures, transition "
          "énergétique, autonomie stratégique et défense."},
   {'q': "Sujet sur la surcapacité chinoise et ses effets mondiaux",
    'f': "Le cours décrit un mécanisme en deux conséquences. La Chine "
         "investit massivement dans l’industrie, les technologies, les "
         "infrastructures et les capacités de production, mais la demande "
         "interne ne progresse pas aussi vite : les capacités dépassent la "
         "consommation domestique. D’où, premièrement, une pression "
         "déflationniste, puisque l’offre excède la demande, ce qui renforce "
         "encore la compétitivité-prix des produits chinois ; "
         "deuxièmement, la nécessité d’exporter les surplus.",
    'r': "On montre que le déséquilibre interne chinois se transmet aux "
         "autres économies par les prix autant que par les volumes, ce qui "
         "explique l’intensité des tensions commerciales.",
    'ex': "La déflation chinoise rendant les produits encore plus "
          "compétitifs sur les marchés internationaux."},
   {'q': "Sujet sur les conséquences politiques des déséquilibres",
    'f': "Le cours relie les déséquilibres à la contestation. La courbe de "
         "l’éléphant de Branko Milanovic fait apparaître trois groupes : les "
         "classes moyennes émergentes et le top 1 % mondial comme grands "
         "gagnants, les classes populaires des pays développés comme "
         "perdants relatifs. Cette répartition explique en partie pourquoi "
         "une mondialisation favorable à la croissance mondiale peut "
         "néanmoins provoquer mécontentement, contestation politique et "
         "protectionnisme.",
    'r': "On montre que le paradoxe distributif de l’hypermondialisation "
         "crée les conditions politiques du retour du protectionnisme, ce "
         "qui relie les soldes extérieurs aux choix électoraux.",
    'ex': "Les classes populaires des pays développés comme perdants "
          "relatifs de l’hypermondialisation."}],
  voisins=['n20-solde-courant', 'n20-epargne-investissement-ouverte',
           'n20-position-exterieure-nette', 'n17-fragmentation-geoeconomique'])

d('n20-crise-change', 20, "Crise de change",
  "Sudden stop, dette en devises, réserves épuisées : le Mexique 1982",
  "Le cours n’emploie pas l’expression « crise de change » : il décrit le "
  "même phénomène sous les noms de sudden stop et de crise de financement. "
  "Un sudden stop est un arrêt brutal des entrées de capitaux étrangers, "
  "éventuellement accompagné de sorties massives, qui provoque une crise "
  "dans une économie dépendante des capitaux extérieurs, d’autant plus "
  "grave que les acteurs domestiques se sont endettés en devise étrangère.",
  "Le cours construit le scénario complet d’une crise de financement "
  "extérieur, qu’il nomme sudden stop plutôt que crise de change, et il "
  "faut signaler cette différence de vocabulaire. Le point de départ est la "
  "dépendance : un déficit courant n’est soutenable que si le pays parvient "
  "à attirer durablement les capitaux étrangers nécessaires à son "
  "financement. Or cette dépendance devient dangereuse si les investisseurs "
  "changent brutalement de comportement : un sudden stop correspond à un "
  "arrêt brutal des entrées de capitaux étrangers, pouvant s’accompagner de "
  "sorties massives, provoqué par une crise politique, une perte de "
  "confiance, une hausse du risque, un meilleur rendement ailleurs ou une "
  "modification des taux d’intérêt internationaux. Le facteur aggravant est "
  "la dette en devises : si un pays emprunte en dollars alors que ses "
  "revenus sont en monnaie nationale, une dépréciation alourdit "
  "mécaniquement la dette, selon l’enchaînement monnaie nationale en baisse, "
  "valeur de la dette en dollars en hausse, difficultés de remboursement en "
  "hausse. S’y ajoute le cercle vicieux des monnaies faibles : un déficit "
  "commercial important accroît l’offre de monnaie nationale, puisque les "
  "résidents vendent leur monnaie pour acheter des devises afin de payer "
  "leurs importations, ce qui déprécie la monnaie, renchérit les "
  "importations et aggrave le déficit ; cette dépréciation peut transmettre "
  "le déséquilibre à l’économie domestique par l’inflation importée, voire "
  "l’hyperinflation dans les cas extrêmes, le cours citant l’Argentine, le "
  "Liban et la Turquie. Le cas d’école est mexicain. Paul Volcker arrive à "
  "la tête de la Réserve fédérale en 1979 dans un contexte d’inflation "
  "élevée et augmente fortement les taux d’intérêt : les placements "
  "américains deviennent plus attractifs, les capitaux quittent les "
  "économies émergentes et les États-Unis deviennent une « pompe aspirante "
  "» à capitaux. Le Mexique, qui possède un déficit extérieur, s’est endetté "
  "en dollars et dépend des capitaux étrangers, subit donc simultanément la "
  "baisse des entrées, la hausse des taux d’intérêt et l’alourdissement de "
  "sa dette en dollars. Lors de la crise de 1982, il connaît une fuite des "
  "capitaux, la sortie des investissements de portefeuille, la persistance "
  "du déficit courant et l’insuffisance des nouvelles entrées ; il utilise "
  "d’abord ses réserves de devises, mais celles-ci sont limitées, et "
  "lorsqu’elles deviennent insuffisantes surviennent l’incapacité de payer "
  "puis la cessation de paiement, ce qui ouvre la crise de la dette "
  "latino-américaine.",
  [("La dépendance initiale au financement extérieur",
    "Un déficit courant n’est soutenable que si le pays parvient à attirer "
    "durablement les capitaux étrangers nécessaires : cette dépendance est "
    "la condition de la crise."),
   ("Le retournement des conditions internationales",
    "Une modification des taux d’intérêt internationaux rend les placements "
    "ailleurs plus attractifs : les investisseurs se demandent pourquoi "
    "placer dans une économie risquée si une économie avancée offre "
    "désormais un rendement élevé."),
   ("L’arrêt brutal des entrées de capitaux",
    "Le sudden stop correspond à un arrêt brutal des entrées de capitaux "
    "étrangers, pouvant s’accompagner de sorties massives, du fait d’une "
    "crise politique, d’une perte de confiance ou d’une hausse du risque "
    "perçu."),
   ("L’alourdissement de la dette en devises",
    "Si le pays emprunte en dollars alors que ses revenus sont en monnaie "
    "nationale, une dépréciation alourdit mécaniquement la dette : monnaie "
    "nationale en baisse, valeur de la dette en dollars en hausse, "
    "difficultés de remboursement en hausse."),
   ("Le cercle vicieux des monnaies faibles",
    "Un déficit commercial important accroît l’offre de monnaie nationale, "
    "ce qui la déprécie, renchérit les importations et aggrave le déficit, "
    "d’où une nouvelle dépréciation : la spirale s’auto-entretient."),
   ("La transmission par l’inflation importée",
    "Des importations plus chères élèvent les coûts de production puis les "
    "prix domestiques, ce qui peut générer une inflation importée, voire une "
    "hyperinflation dans les cas extrêmes."),
   ("L’épuisement des réserves de devises",
    "Le pays utilise d’abord ses réserves de devises pour amortir le choc, "
    "mais celles-ci sont limitées : quand elles deviennent insuffisantes "
    "surviennent l’incapacité de payer puis la cessation de paiement.")],
  [{'a': "La notion identifie un mécanisme de crise précis, par l’arrêt des "
         "entrées de capitaux plutôt que par la seule dégradation du solde.",
    'cond': "L’argument suppose la définition du cours : un sudden stop "
            "provoque une crise de financement dans une économie dépendante "
            "des capitaux extérieurs.",
    'lim': "Le cours n’emploie pas l’expression « crise de change » : il "
           "décrit une crise de financement extérieur, dont la dimension "
           "monétaire est une conséquence plutôt qu’un point de départ."},
   {'a': "Elle fait apparaître le rôle décisif de la devise dans laquelle la dette extérieure est libellée.",
    'cond': "L’argument suppose le mécanisme du cours : une dépréciation "
            "alourdit mécaniquement une dette libellée en devise étrangère "
            "lorsque les revenus sont en monnaie nationale.",
    'lim': "Le cours ne compare pas les régimes d’endettement : il décrit le "
           "danger de la dette en devises sans examiner les coûts d’un "
           "endettement en monnaie nationale."},
   {'a': "Elle relie la crise financière à une crise des prix, par le canal de l’inflation importée.",
    'cond': "L’articulation suppose l’enchaînement du cours : importations "
            "plus chères, coûts de production en hausse, prix domestiques en "
            "hausse, inflation importée.",
    'lim': "Le cours rappelle que ce cercle vicieux ne s’enclenche pas "
           "nécessairement, puisqu’une monnaie plus faible peut aussi "
           "stimuler les exportations selon la logique de la courbe en J."},
   {'a': "Elle s’appuie sur un cas historique entièrement documenté par le cours, la crise mexicaine de 1982.",
    'cond': "Le cas suppose les trois conditions réunies : déficit "
            "extérieur, endettement en dollars, dépendance aux capitaux "
            "étrangers.",
    'lim': "Un cas unique ne fournit pas une théorie générale : le cours "
           "l’utilise pour illustrer le mécanisme du sudden stop, non pour "
           "prédire les crises."},
   {'a': "Elle montre à la fois la fonction et la limite des réserves de change détenues par un pays.",
    'cond': "L’argument suppose le rôle décrit par le cours : les réserves "
            "servent de dernier amortisseur lorsque les entrées de capitaux "
            "cessent.",
    'lim': "Le cours souligne que ces réserves sont limitées : elles "
           "retardent la crise sans l’empêcher si le déséquilibre "
           "persiste."}],
  [{'t': "Une crise de financement extérieur résulte d’une mauvaise gestion "
         "interne du pays concerné.",
    'qui': "La lecture que le cas mexicain de 1982 nuance.",
    'rep': "Le cours montre que le déclencheur est extérieur : Paul Volcker "
           "augmente fortement les taux américains en 1979, les placements "
           "américains deviennent plus attractifs et les capitaux quittent "
           "les économies émergentes, de sorte que les pays dépendants de "
           "ces entrées connaissent un sudden stop."},
   {'t': "Emprunter en devise étrangère est neutre, puisque la dette reste "
         "la même quantité de monnaie.",
    'qui': "La lecture que le danger de la dette en devises contredit.",
    'rep': "Le cours objecte que si les revenus sont en monnaie nationale et "
           "la dette en dollars, une dépréciation rend la dette beaucoup "
           "plus lourde en monnaie nationale : l’endettement en devises "
           "accroît donc la vulnérabilité extérieure."},
   {'t': "Une dépréciation de la monnaie résout le déséquilibre extérieur en "
         "rendant les exportations plus compétitives.",
    'qui': "La lecture que le cercle vicieux des monnaies faibles "
           "complique.",
    'rep': "Le cours montre que la dépréciation renchérit d’abord les "
           "importations, ce qui aggrave le déficit et provoque une nouvelle "
           "dépréciation, et qu’elle peut générer une inflation importée "
           "voire une hyperinflation, comme en Argentine, au Liban ou en "
           "Turquie."},
   {'t': "Des réserves de change suffisantes mettent un pays à l’abri d’une "
         "crise de financement.",
    'qui': "La lecture que le cas mexicain démentit.",
    'rep': "Le cours montre que le Mexique utilise d’abord ses réserves de "
           "devises, mais que celles-ci sont limitées : quand elles "
           "deviennent insuffisantes surviennent l’incapacité de payer puis "
           "la cessation de paiement, ce qui ouvre la crise de la dette "
           "latino-américaine."}],
  [{'n': "Paul Volcker",
    'i': "La forte hausse des taux américains de 1979 redirige les capitaux "
         "mondiaux vers les États-Unis.",
    'p': "Le cours en donne le mécanisme complet : contexte d’inflation "
         "élevée, hausse forte des taux, placements américains plus "
         "attractifs, capitaux quittant les économies émergentes, États-Unis "
         "devenant une « pompe aspirante » à capitaux et pays dépendants "
         "subissant un sudden stop."},
   {'n': "Ragnar Nurkse",
    'i': "La faiblesse de l’épargne domestique oblige les économies pauvres "
         "à recourir au financement extérieur.",
    'p': "Le cours en détaille le cercle vicieux de la pauvreté et en tire "
         "la condition de la crise : c’est parce que ces économies "
         "dépendent structurellement de l’épargne du reste du monde qu’un "
         "retournement des flux financiers internationaux les expose à une "
         "crise de financement."},
   {'n': "Benjamin Lemoine",
    'i': "Certains acteurs financiers privés peuvent transformer la dette "
         "souveraine en terrain de chasse spéculatif.",
    'p': "Le cours situe Chasseurs d’États en 2024 et évoque les fonds "
         "vautours, fonds d’investissement privés qui rachètent à bas prix "
         "la dette d’États en difficulté : la crise de financement ouvre "
         "ainsi un rapport de force entre souveraineté publique et finance "
         "privée."},
   {'n': "Henri Bourguinat",
    'i': "La globalisation financière repose sur les trois D : "
         "décloisonnement, déréglementation, désintermédiation.",
    'p': "Le cours situe cette analyse en 1987 et en tire la condition de "
         "possibilité des sudden stops : c’est la libre circulation des "
         "capitaux ainsi instituée qui permet des entrées massives, puis des "
         "retraits aussi brutaux, dans les économies dépendantes du "
         "financement extérieur."}],
  [{'f': "Un sudden stop correspond à un arrêt brutal des entrées de "
         "capitaux étrangers, pouvant s’accompagner de sorties massives, du "
         "fait d’une crise politique, d’une perte de confiance, d’une hausse "
         "du risque, d’un meilleur rendement ailleurs ou d’une modification "
         "des taux d’intérêt internationaux.",
    'p': "La définition nomme le phénomène et en énumère les déclencheurs, "
         "dont la plupart sont extérieurs au pays frappé."},
   {'f': "Paul Volcker arrive à la Réserve fédérale en 1979 dans un contexte "
         "d’inflation élevée et augmente fortement les taux d’intérêt, ce "
         "qui ramène massivement les capitaux mondiaux vers les États-Unis.",
    'p': "Le fait établit le déclencheur externe de la crise "
         "latino-américaine et montre la transmission internationale de la "
         "politique monétaire américaine."},
   {'f': "Lors de la crise de 1982, le Mexique connaît une fuite des "
         "capitaux, la sortie des investissements de portefeuille, la "
         "persistance de son déficit courant et l’insuffisance des nouvelles "
         "entrées ; il utilise ses réserves de devises, puis, celles-ci "
         "devenant insuffisantes, se trouve en cessation de paiement.",
    'p': "Le cas démontre la séquence complète d’une crise de financement "
         "extérieur et le rôle des réserves comme dernier amortisseur."},
   {'f': "Si un pays emprunte en dollars alors que ses revenus sont en "
         "monnaie nationale, une dépréciation alourdit mécaniquement la "
         "dette : monnaie nationale en baisse, valeur de la dette en dollars "
         "en hausse, difficultés de remboursement en hausse.",
    'p': "Le fait identifie le facteur aggravant décisif et explique "
         "pourquoi deux pays au même déficit ne sont pas également "
         "vulnérables."},
   {'f': "La dépréciation peut transmettre le déséquilibre extérieur à "
         "l’économie domestique par l’inflation importée, voire "
         "l’hyperinflation dans les cas extrêmes, le cours citant "
         "l’Argentine, le Liban et la Turquie.",
    'p': "Le fait montre que la crise de financement devient une crise des "
         "prix, ce qui en étend les effets à l’ensemble de la population."},
   {'f': "Le resserrement monétaire de Volcker transforme la dépendance "
         "financière des économies latino-américaines en crise de dette : "
         "les capitaux repartent vers les États-Unis tandis que le coût des "
         "dettes libellées en dollars explose.",
    'p': "Le fait établit la conjonction des deux canaux, retrait des "
         "capitaux et renchérissement de la dette, qui rend la crise "
         "inévitable."}],
  [{'q': "Sujet sur les crises de financement des économies émergentes",
    'f': "Le cours décrit la séquence complète. Un pays en déficit courant "
         "dépend des capitaux étrangers ; un sudden stop, arrêt brutal des "
         "entrées, éventuellement accompagné de sorties massives, survient à "
         "la suite d’une crise politique, d’une perte de confiance ou d’une "
         "modification des taux internationaux ; si le pays s’est endetté en "
         "devise étrangère, la dépréciation alourdit mécaniquement sa dette ; "
         "ses réserves de devises, limitées, s’épuisent, et survient la "
         "cessation de paiement.",
    'r': "On montre que la crise résulte de la conjonction d’une dépendance "
         "structurelle et d’un choc extérieur, et non d’une seule mauvaise "
         "gestion interne.",
    'ex': "La crise mexicaine de 1982, point de départ de la crise de la "
          "dette latino-américaine."},
   {'q': "Sujet sur les effets internationaux de la politique monétaire "
         "américaine",
    'f': "Le cours décrit le choc Volcker. Paul Volcker arrive à la Réserve "
         "fédérale en 1979 dans un contexte d’inflation élevée et augmente "
         "fortement les taux d’intérêt : les placements américains "
         "deviennent plus attractifs, les investisseurs se demandent "
         "pourquoi placer dans une économie émergente risquée, et les "
         "capitaux retournent vers les États-Unis, qui deviennent une "
         "« pompe aspirante » à capitaux. Les pays qui dépendaient de ces "
         "entrées connaissent alors un sudden stop.",
    'r': "On montre que la politique monétaire d’une grande économie est une "
         "variable extérieure pour les pays dépendants du financement "
         "international, ce qui limite leur autonomie.",
    'ex': "Le Mexique de 1982, dont le déficit extérieur et la dette en "
          "dollars se conjuguent avec la hausse des taux."},
   {'q': "Sujet sur le cercle vicieux des monnaies faibles",
    'f': "Le cours décrit une spirale. Toutes choses égales par ailleurs, un "
         "déficit commercial important accroît l’offre de monnaie nationale, "
         "puisque les résidents vendent leur monnaie pour acheter des "
         "devises afin de payer leurs importations, ce qui la déprécie ; la "
         "dépréciation renchérit les importations libellées en dollars, "
         "pétrole et matières premières notamment, ce qui aggrave le déficit "
         "et déprécie encore la monnaie. La spirale peut devenir "
         "inflationniste.",
    'r': "On montre que le taux de change et le solde extérieur peuvent se "
         "renforcer mutuellement au lieu de se corriger, ce qui invalide la "
         "confiance dans un rééquilibrage automatique.",
    'ex': "L’inflation importée, voire l’hyperinflation, en Argentine, au "
          "Liban ou en Turquie."},
   {'q': "Sujet sur la vulnérabilité liée à l’endettement en devises",
    'f': "Le cours isole ce facteur aggravant. Supposons qu’un pays emprunte "
         "en dollars alors que ses revenus sont en monnaie nationale : si sa "
         "monnaie se déprécie, la dette en dollars devient beaucoup plus "
         "lourde en monnaie nationale, selon l’enchaînement monnaie "
         "nationale en baisse, valeur de la dette en dollars en hausse, "
         "difficultés de remboursement en hausse. L’endettement en devises "
         "accroît donc la vulnérabilité extérieure.",
    'r': "On montre que la composition de la dette conditionne la gravité "
         "d’une crise, ce qui explique que deux pays au même déficit ne "
         "soient pas également exposés.",
    'ex': "Le Mexique de 1982, endetté en dollars avec des revenus en "
          "monnaie nationale."}],
  voisins=['n20-capacite-besoin-financement', 'n20-appreciation-depreciation',
           'n20-position-exterieure-nette', 'n20-changes-fixes-flottants'])
