# -*- coding: utf-8 -*-
"""Ensemble 16 — Le commerce international et la spécialisation (3/5)."""

from doss_base import d

d('n16-egalisation-remunerations', 16,
  "Égalisation des rémunérations factorielles",
  "Le commerce des biens rapproche le prix des facteurs",
  "Le théorème Stolper-Samuelson établit que le libre-échange tend à "
  "rapprocher les prix des facteurs entre pays, sous les hypothèses du modèle "
  "et notamment en situation de spécialisation incomplète. Le cours en donne "
  "la raison : le commerce peut partiellement substituer la mobilité des "
  "biens à celle des facteurs, puisque l’échange transporte indirectement les "
  "services des facteurs incorporés dans les produits.",
  "Le cours construit ce résultat en deux temps, interne puis international, "
  "et c’est cet enchaînement qu’il faut restituer. Le point de départ est "
  "l’article de Wolfgang Stolper et Paul Samuelson publié en 1941 sous le "
  "titre Protection and Real Wages, et l’idée fondatrice est que le commerce "
  "international peut être interprété comme un échange indirect de facteurs "
  "de production. Le cours en donne l’exemple : un ordinateur contre un "
  "pyjama. L’ordinateur est relativement intensif en capital et en travail "
  "qualifié, le pyjama en travail peu qualifié ; lorsque les États-Unis "
  "exportent un ordinateur, ils exportent indirectement les services du "
  "capital et du travail qualifié incorporés dans ce produit, et lorsqu’ils "
  "importent un vêtement, ils importent indirectement les services du travail "
  "peu qualifié. Le commerce des biens peut donc être lu comme un commerce "
  "indirect des facteurs. Le premier temps est distributif à l’intérieur des "
  "pays. Dans un pays avancé relativement abondant en travail qualifié, la "
  "spécialisation se fait dans des productions exigeant beaucoup de "
  "qualifications, donc la demande de travail qualifié augmente et le salaire "
  "des travailleurs qualifiés monte ; parallèlement le pays importe des "
  "produits intensifs en travail peu qualifié, ce qui équivaut à une "
  "augmentation indirecte de l’offre de travail peu qualifié, et les secteurs "
  "intensifs en travail non qualifié domestique reculent, d’où une pression à "
  "la baisse sur la rémunération relative des travailleurs peu qualifiés. "
  "Dans un pays en développement, le mécanisme théorique est inversé : le "
  "facteur relativement abondant étant souvent le travail peu qualifié, la "
  "spécialisation accroît la demande de ce facteur et peut donc augmenter le "
  "salaire réel des travailleurs peu qualifiés, réduisant certaines "
  "inégalités internes. Le second temps est international. En augmentant la "
  "rémunération des facteurs initialement abondants et peu chers, le commerce "
  "tend à rapprocher le prix des facteurs entre pays : dans le pays abondant "
  "en capital la demande de capital augmente donc sa rémunération monte, dans "
  "le pays abondant en travail la demande de travail augmente donc le salaire "
  "monte, et les écarts de rémunération entre pays tendent à diminuer. Le "
  "cours formule ainsi le théorème et en précise aussitôt les réserves : le "
  "résultat vaut sous les hypothèses du modèle, notamment en situation de "
  "spécialisation incomplète, et l’évolution effective des inégalités dépend "
  "aussi du progrès technique, des institutions et des politiques publiques.",
  [("Le commerce comme échange indirect de facteurs",
    "Chaque bien incorpore des services de facteurs : exporter un ordinateur "
    "revient à exporter indirectement du capital et du travail qualifié, "
    "importer un vêtement à importer du travail peu qualifié."),
   ("La modification de la demande de facteurs",
    "La spécialisation accroît la demande du facteur dont les exportations "
    "sont intensives : dans le pays abondant en travail qualifié, la demande "
    "de qualifications augmente."),
   ("L’augmentation indirecte de l’offre du facteur importé",
    "Importer des biens intensifs en travail peu qualifié équivaut à une "
    "augmentation indirecte de l’offre de ce facteur, ce qui pèse sur sa "
    "rémunération relative."),
   ("Le recul des secteurs concurrencés",
    "Les secteurs intensifs en travail non qualifié domestique reculent : la "
    "baisse de la demande domestique s’ajoute à la hausse de l’offre "
    "indirecte."),
   ("La hausse du prix du facteur abondant dans chaque pays",
    "Après spécialisation, la demande du facteur abondant augmente dans "
    "chaque pays, donc son prix monte : capital dans le pays A, travail dans "
    "le pays B."),
   ("Le rapprochement international des prix",
    "Les facteurs initialement abondants et peu chers voyant leur "
    "rémunération augmenter, les écarts de rémunération entre pays tendent à "
    "diminuer."),
   ("La substitution partielle à la mobilité des facteurs",
    "Même si capital et travail ne franchissent pas directement les "
    "frontières, l’échange de biens produit en partie l’effet qu’aurait leur "
    "mobilité.")],
  [{'a': "Le théorème relie le commerce et la répartition des revenus par un "
         "mécanisme explicite et non par une corrélation.",
    'cond': "Il suppose de lire le commerce des biens comme un échange "
            "indirect de facteurs, ce que le cours établit avec l’exemple de "
            "l’ordinateur et du pyjama.",
    'lim': "Le cours rappelle que l’évolution effective des inégalités "
           "dépend aussi du progrès technique, des institutions et des "
           "politiques publiques."},
   {'a': "Il rend prévisibles les gagnants et les perdants internes à partir "
         "des dotations factorielles du pays.",
    'cond': "La prévision suppose que l’on connaisse le facteur relativement "
            "abondant et l’intensité factorielle des biens échangés.",
    'lim': "Le modèle de base ne distingue que capital et travail : le cours "
           "juge nécessaire d’ajouter la distinction entre travail qualifié "
           "et non qualifié."},
   {'a': "Le résultat international explique une tendance à la convergence "
         "sans supposer la mobilité des facteurs.",
    'cond': "La convergence suppose une spécialisation incomplète, condition "
            "que le cours mentionne explicitement.",
    'lim': "Une spécialisation complète ferait disparaître le mécanisme : le "
           "théorème n’opère que si les deux pays continuent de produire les "
           "deux biens."},
   {'a': "Il montre la symétrie des effets selon le niveau de développement, "
         "ce qui évite une conclusion unique sur les inégalités.",
    'cond': "La symétrie suppose que le facteur abondant soit le travail "
            "qualifié dans les pays avancés et le travail peu qualifié dans "
            "les pays en développement.",
    'lim': "Le cours ne vérifie pas empiriquement cette hypothèse de "
           "dotations : elle est posée pour dériver le résultat."},
   {'a': "Il fournit un argument théorique contre la protection, puisque "
         "celle-ci modifie aussi les salaires réels.",
    'cond': "L’argument suppose que les effets de la protection soient "
            "symétriques de ceux de l’ouverture, ce que le titre de "
            "l’article de 1941 indique.",
    'lim': "Le cours ne développe pas cette conséquence protectionniste : il "
           "retient surtout le résultat distributif de l’ouverture."}],
  [{'t': "L’ouverture accentue les inégalités salariales dans les économies "
         "avancées, au détriment des travailleurs peu qualifiés.",
    'qui': "Wolfgang Stolper et Paul Samuelson, dans leur article de 1941.",
    'rep': "Le cours maintient la symétrie du théorème : dans un pays "
           "abondant en travail peu qualifié, le mécanisme est inversé et "
           "l’ouverture peut augmenter le salaire réel des moins qualifiés, "
           "réduisant certaines inégalités internes."},
   {'t': "Les inégalités viennent du progrès technique et non du commerce : "
         "le théorème attribue au second ce qui relève du premier.",
    'qui': "L’objection que le cours formule lui-même en nuançant le "
           "résultat.",
    'rep': "Le cours retient cette nuance comme une limite et non comme une "
           "réfutation : le théorème fournit un mécanisme reliant commerce et "
           "répartition, mais l’évolution effective dépend aussi du progrès "
           "technique, des institutions et des politiques publiques."},
   {'t': "La convergence internationale des rémunérations n’est pas "
         "observée : les écarts de salaire entre pays restent considérables.",
    'qui': "L’objection empirique au résultat international du théorème.",
    'rep': "Le cours encadre le résultat par ses hypothèses : il vaut sous "
           "les hypothèses du modèle et notamment en situation de "
           "spécialisation incomplète, ce qui en limite la portée "
           "prédictive."},
   {'t': "Le commerce ne peut pas remplacer la mobilité des facteurs : les "
         "migrations et les investissements directs ont des effets propres.",
    'qui': "L’objection tirée de la levée de l’hypothèse ricardienne "
           "d’immobilité des facteurs.",
    'rep': "Le cours formule le résultat avec prudence : le commerce peut "
           "partiellement substituer la mobilité des biens à celle des "
           "facteurs, le mot partiellement limitant lui-même la portée."}],
  [{'n': "Wolfgang Stolper",
    'i': "Le commerce international modifie la rémunération des facteurs de "
         "production.",
    'p': "Le cours renvoie à Protection and Real Wages, publié avec "
         "Samuelson en 1941, et donne la lecture fondatrice : le commerce "
         "international peut être interprété comme un échange indirect de "
         "facteurs de production, un ordinateur contre un pyjama."},
   {'n': "Paul Samuelson",
    'i': "Le libre-échange tend à rapprocher les prix des facteurs entre "
         "pays.",
    'p': "Le cours en donne le mécanisme : en augmentant la rémunération des "
         "facteurs initialement abondants et peu chers, le commerce rapproche "
         "le prix des facteurs, sous les hypothèses du modèle et notamment en "
         "situation de spécialisation incomplète."},
   {'n': "Bertil Ohlin",
    'i': "Un facteur relativement abondant est relativement moins cher.",
    'p': "Le cours renvoie à Interregional and International Trade de 1933 : "
         "c’est cette relation entre abondance relative et prix relatif du "
         "facteur qui rend possible le résultat d’égalisation, puisque la "
         "spécialisation accroît la demande du facteur initialement bon "
         "marché."},
   {'n': "Eli Heckscher",
    'i': "Le commerce extérieur a des effets sur la distribution du revenu.",
    'p': "Le cours renvoie au titre même de son article de 1919, The Effects "
         "of Foreign Trade on the Distribution of Income : la question "
         "distributive est donc présente dès l’origine du modèle et non "
         "ajoutée par Stolper et Samuelson."}],
  [{'f': "Stolper et Samuelson publient en 1941 Protection and Real Wages, où "
         "le commerce des biens est lu comme un échange indirect de facteurs.",
    'p': "La date et le titre montrent que le résultat distributif est "
         "formulé à l’intérieur de la théorie du commerce et non contre "
         "elle."},
   {'f': "Le cours prend l’exemple d’un ordinateur contre un pyjama, le "
         "premier intensif en capital et travail qualifié, le second en "
         "travail peu qualifié.",
    'p': "L’exemple rend le mécanisme tangible : il montre qu’un échange de "
         "biens déplace la demande de facteurs sans qu’aucun facteur ne "
         "franchisse la frontière."},
   {'f': "Le cours énonce le théorème : le libre-échange tend à rapprocher "
         "les prix des facteurs entre pays, notamment en situation de "
         "spécialisation incomplète.",
    'p': "La condition de spécialisation incomplète est décisive : elle "
         "signifie que les deux pays doivent continuer de produire les deux "
         "biens pour que le mécanisme opère."},
   {'f': "Le cours rappelle que l’évolution effective des inégalités dépend "
         "aussi du progrès technique, des institutions et des politiques "
         "publiques.",
    'p': "La réserve montre que le théorème isole un canal parmi d’autres : "
         "il ne prétend pas expliquer à lui seul l’évolution observée des "
         "inégalités."}],
  [{'q': "Sujet sur commerce international et inégalités",
    'f': "Le théorème Stolper-Samuelson fournit le mécanisme le plus précis. "
         "Le commerce des biens est lu comme un échange indirect de "
         "facteurs : dans un pays avancé abondant en travail qualifié, la "
         "demande de qualifications augmente et les salaires qualifiés "
         "montent, tandis que les importations de biens intensifs en travail "
         "peu qualifié équivalent à une augmentation indirecte de l’offre de "
         "ce facteur et pèsent sur sa rémunération relative.",
    'r': "On montre que l’effet distributif découle du mécanisme "
         "d’allocation lui-même, ce qui rend les gagnants et les perdants "
         "prévisibles à partir des dotations.",
    'ex': "L’exemple du cours : un ordinateur contre un pyjama, le premier "
          "intensif en capital et travail qualifié."},
   {'q': "Sujet sur la convergence des économies",
    'f': "Le commerce peut rapprocher les rémunérations sans mobilité des "
         "facteurs. Le cours en donne le mécanisme : après spécialisation, la "
         "demande du facteur abondant augmente dans chaque pays, donc son "
         "prix monte, et les écarts de rémunération entre pays tendent à "
         "diminuer. Le théorème conclut que le libre-échange tend à "
         "rapprocher les prix des facteurs, en situation de spécialisation "
         "incomplète.",
    'r': "On montre que l’échange de biens produit en partie l’effet qu’aurait "
         "la mobilité des facteurs, ce qui relie commerce et convergence sans "
         "supposer de migrations.",
    'ex': "La formule du cours : le commerce peut partiellement substituer la "
          "mobilité des biens à celle des facteurs."},
   {'q': "Sujet sur les effets ambivalents de l’ouverture",
    'f': "Le même théorème produit des conclusions inverses selon les pays. "
         "Dans une économie avancée relativement abondante en travail "
         "qualifié, l’ouverture peut accentuer les inégalités salariales. "
         "Dans un pays en développement où le facteur abondant est le travail "
         "peu qualifié, la spécialisation accroît la demande de ce facteur et "
         "peut augmenter le salaire réel des moins qualifiés, réduisant "
         "certaines inégalités internes.",
    'r': "On montre que le signe de l’effet dépend de la dotation du pays, "
         "ce qui interdit toute conclusion générale sur l’ouverture et les "
         "inégalités.",
    'ex': "Le mécanisme inversé que le cours décrit pour les pays en "
          "développement abondants en travail peu qualifié."},
   {'q': "Sujet sur les limites des modèles de commerce international",
    'f': "Le cours encadre soigneusement la portée du théorème. Il vaut sous "
         "les hypothèses du modèle et notamment en situation de "
         "spécialisation incomplète ; et il ne suffit pas à expliquer "
         "l’évolution observée, puisque celle-ci dépend aussi du progrès "
         "technique, des institutions et des politiques publiques. Le "
         "théorème fournit donc un canal, non une explication complète.",
    'r': "On distingue le mécanisme isolé par le modèle et le résultat "
         "observé, qui agrège plusieurs mécanismes, ce qui évite de réfuter "
         "un théorème par une observation globale.",
    'ex': "La réserve du cours sur le rôle du progrès technique, des "
          "institutions et des politiques publiques."}],
  voisins=['n16-dotations-factorielles', 'n16-repartition-gains',
           'n16-avantages-comparatifs', 'n16-termes-echange'])


d('n16-commerce-interbranche-intrabranche', 16,
  "Commerce interbranche et intrabranche",
  "Échanger des biens différents, ou les mêmes biens différemment",
  "Le commerce interbranche est l’échange de biens appartenant à des branches "
  "différentes, celui que les théories traditionnelles expliquent ; le "
  "commerce intrabranche est l’échange de biens appartenant à la même "
  "branche. Le cours en souligne le poids : le commerce intrabranche "
  "représente environ quarante à cinquante pour cent des échanges, et son "
  "poids a fortement augmenté depuis les années 1960.",
  "Le cours introduit cette distinction comme un défi adressé aux théories "
  "traditionnelles, et c’est sous cette forme qu’il faut la traiter. Le "
  "constat de départ est quantitatif : les théories traditionnelles "
  "expliquent principalement pourquoi des pays différents échangent des biens "
  "différents, mais le commerce intrabranche représente une part "
  "considérable du commerce international, de l’ordre de quarante à cinquante "
  "pour cent des échanges, et son poids a fortement augmenté depuis les "
  "années 1960. La question est donc nette : pourquoi des pays disposant de "
  "niveaux de développement et de dotations relativement proches échangent-ils "
  "massivement des biens appartenant aux mêmes branches ? Les modèles "
  "classiques ne peuvent pas y répondre, puisqu’ils font dépendre l’échange "
  "de différences, de productivité chez Ricardo ou de dotations dans le "
  "modèle HOS. Le cours en tire la conséquence méthodologique : il faut "
  "regarder non seulement du côté de l’offre, mais également du côté de la "
  "demande. Deux analyses sont alors mobilisées. La première est celle de "
  "Lassudrie-Duchêne, qui introduit une demande de différence : deux "
  "économies proches peuvent produire dans la même branche, mais leurs "
  "produits ne sont pas nécessairement perçus comme parfaitement identiques, "
  "et les consommateurs peuvent rechercher la différence, ce qui permet de "
  "comprendre que la France et l’Allemagne échangent des voitures contre des "
  "voitures. La logique ne repose donc plus sur des dotations factorielles "
  "fondamentalement différentes mais sur la différenciation des produits, et "
  "pour formaliser cette idée Lassudrie-Duchêne reprend l’analyse de la "
  "concurrence monopolistique développée par Chamberlin en 1933. La seconde "
  "est celle de Linder, qui introduit la demande représentative : la "
  "proximité des niveaux de vie rapproche les structures de demande, un bien "
  "conçu pour les consommateurs d’un pays ayant davantage de chances d’être "
  "demandé dans une économie dont les préférences et le pouvoir d’achat sont "
  "similaires, de sorte que les pays de niveau de vie comparable ont tendance "
  "à davantage échanger entre eux. Le cours ajoute enfin une troisième "
  "explication, du côté de l’offre cette fois : il faut introduire "
  "explicitement les rendements croissants et les économies d’échelle, ce qui "
  "est l’apport central de Krugman.",
  [("Le constat du commerce entre semblables",
    "Des pays de niveaux de développement et de dotations proches échangent "
    "massivement des biens de la même branche, ce que les théories "
    "traditionnelles n’expliquent pas."),
   ("L’échec des explications par la différence",
    "Les modèles classiques font dépendre l’échange d’une différence, de "
    "productivité ou de dotations : entre économies semblables, ils ne "
    "prédisent donc aucun échange."),
   ("Le déplacement vers la demande",
    "Le cours en tire la conséquence : il faut regarder non seulement du côté "
    "de l’offre mais également du côté de la demande."),
   ("La demande de différence",
    "Avec Lassudrie-Duchêne, les produits d’une même branche ne sont pas "
    "perçus comme identiques et les consommateurs peuvent rechercher la "
    "différence : d’où un échange de voitures contre des voitures."),
   ("La demande représentative",
    "Avec Linder, la proximité des niveaux de vie rapproche les structures de "
    "demande : un bien conçu pour un pays trouve preneur dans un pays de "
    "pouvoir d’achat comparable."),
   ("L’explication par les rendements croissants",
    "Le cours ajoute qu’il faut introduire explicitement les rendements "
    "croissants et les économies d’échelle, ce qui est l’apport central de "
    "Krugman.")],
  [{'a': "La distinction rend compte d’une part majoritaire du commerce "
         "contemporain que les théories classiques laissaient inexpliquée.",
    'cond': "Le constat suppose la mesure du cours : environ quarante à "
            "cinquante pour cent des échanges, en forte hausse depuis les "
            "années 1960.",
    'lim': "Le partage entre les deux types dépend de la définition de la "
           "branche : plus la nomenclature est fine, plus le commerce "
           "intrabranche se réduit."},
   {'a': "Elle oblige à introduire la demande dans l’analyse, ce qui "
         "complète une théorie construite entièrement du côté de l’offre.",
    'cond': "L’argument suppose que les préférences des consommateurs "
            "diffèrent de la simple maximisation d’une quantité homogène.",
    'lim': "Le cours montre que l’explication par la demande ne suffit pas "
           "non plus : il faut y ajouter les rendements croissants avec "
           "Krugman."},
   {'a': "Elle donne un contenu théorique à la différenciation des produits, "
         "par la concurrence monopolistique.",
    'cond': "La formalisation suppose l’analyse de Chamberlin en 1933, selon "
            "laquelle la différenciation procure un pouvoir de marché.",
    'lim': "Ce cadre rompt avec la concurrence pure et parfaite retenue par "
           "Ricardo : il n’est donc pas compatible avec le modèle classique "
           "qu’il complète."},
   {'a': "Elle explique la géographie observée des échanges, concentrés "
         "entre pays de niveau de vie comparable.",
    'cond': "L’explication suppose, avec Linder, que la proximité des "
            "niveaux de vie rapproche effectivement les structures de "
            "demande.",
    'lim': "Elle n’explique pas les échanges entre pays très inégaux, qui "
           "relèvent du commerce interbranche et des théories "
           "traditionnelles."},
   {'a': "Elle éclaire la nature du gain : il porte sur la variété plutôt que "
         "sur l’allocation des facteurs.",
    'cond': "Le gain de variété suppose que les consommateurs valorisent "
            "l’accès à des produits différenciés.",
    'lim': "Ce gain est difficile à mesurer, puisqu’il porte sur la "
           "satisfaction et non sur un volume de production supplémentaire."}],
  [{'t': "L’échange suppose une différence : entre économies semblables, il "
         "ne devrait pas y avoir de commerce.",
    'qui': "La conséquence des théories traditionnelles, de Ricardo au "
           "modèle HOS, que le cours met à l’épreuve.",
    'rep': "Le cours objecte par la mesure : le commerce intrabranche "
           "représente environ quarante à cinquante pour cent des échanges et "
           "son poids a fortement augmenté depuis les années 1960."},
   {'t': "La cause du commerce intrabranche est la demande : les "
         "consommateurs recherchent la différence.",
    'qui': "Lassudrie-Duchêne, dont le cours expose la demande de "
           "différence.",
    'rep': "Le cours complète par l’offre : il faut introduire explicitement "
           "les rendements croissants et les économies d’échelle, ce qui est "
           "l’apport central de Krugman."},
   {'t': "La cause est la proximité des niveaux de vie, qui rapproche les "
         "structures de demande entre pays.",
    'qui': "Linder, dont le cours expose la demande représentative.",
    'rep': "Le cours retient les deux analyses comme complémentaires : la "
           "demande de différence explique la variété recherchée, la demande "
           "représentative la géographie des partenaires."},
   {'t': "La cause véritable est l’offre : c’est l’ouverture qui crée "
         "l’avantage par les économies d’échelle, indépendamment des "
         "préférences.",
    'qui': "Paul Krugman, dont le cours date l’article de 1979.",
    'rep': "Le cours présente ces explications comme cumulatives : la "
           "demande explique pourquoi la variété est désirée, les rendements "
           "croissants pourquoi elle est produite dans un petit nombre de "
           "lieux."}],
  [{'n': "Lassudrie-Duchêne",
    'i': "Les consommateurs peuvent rechercher la différence, ce qui engendre "
         "un échange de produits différenciés entre pays semblables.",
    'p': "Le cours précise que la logique ne repose plus sur des dotations "
         "factorielles fondamentalement différentes mais sur la "
         "différenciation des produits, et qu’il reprend pour la formaliser "
         "l’analyse de la concurrence monopolistique de Chamberlin."},
   {'n': "Staffan Burenstam Linder",
    'i': "La proximité des niveaux de vie rapproche les structures de "
         "demande.",
    'p': "Le cours en tire la conséquence sur la géographie des échanges : "
         "un bien conçu pour les consommateurs d’un pays a davantage de "
         "chances d’être demandé dans une économie dont les préférences et le "
         "pouvoir d’achat sont similaires, de sorte que les pays de niveau de "
         "vie comparable échangent davantage entre eux."},
   {'n': "Edward Chamberlin",
    'i': "Les entreprises peuvent différencier leurs produits, ce qui leur "
         "procure un certain pouvoir de marché.",
    'p': "Le cours date son analyse de 1933 et distingue deux formes de "
         "différenciation, horizontale et verticale, la première ne reposant "
         "pas sur une différence objective de qualité mais sur la perception "
         "du consommateur."},
   {'n': "Paul Krugman",
    'i': "Les rendements croissants et les économies d’échelle expliquent le "
         "commerce entre économies semblables.",
    'p': "Le cours renvoie à son article de 1979 sur les rendements "
         "croissants, la concurrence monopolistique et le commerce "
         "international, et le présente comme la révolution théorique "
         "nécessaire après les analyses par la demande."}],
  [{'f': "Le commerce intrabranche représente environ quarante à cinquante "
         "pour cent des échanges internationaux.",
    'p': "Le chiffre mesure l’ampleur du défi adressé aux théories "
         "traditionnelles : c’est presque la moitié du commerce qu’elles "
         "n’expliquent pas."},
   {'f': "Le poids du commerce intrabranche a fortement augmenté depuis les "
         "années 1960.",
    'p': "La tendance montre que le phénomène n’est pas marginal mais "
         "croissant, ce qui explique le renouvellement théorique des années "
         "1960 à 1980."},
   {'f': "Le cours prend l’exemple des échanges entre la France et "
         "l’Allemagne, voitures contre voitures.",
    'p': "L’exemple rend le problème immédiat : deux économies de dotations "
         "proches échangent dans la même branche, ce qu’aucune différence de "
         "productivité ou de facteurs n’explique."},
   {'f': "Chamberlin formule en 1933 l’analyse de la concurrence "
         "monopolistique, qui distingue différenciation horizontale et "
         "verticale.",
    'p': "La référence montre que l’explication du commerce intrabranche "
         "importe en économie internationale un outil de microéconomie des "
         "marchés imparfaits."}],
  [{'q': "Sujet sur les limites des théories traditionnelles du commerce",
    'f': "Une part majoritaire du commerce échappe aux théories classiques. "
         "Le cours l’établit par la mesure : le commerce intrabranche "
         "représente environ quarante à cinquante pour cent des échanges, et "
         "son poids a fortement augmenté depuis les années 1960. Or les "
         "théories traditionnelles expliquent principalement pourquoi des "
         "pays différents échangent des biens différents, et non pourquoi des "
         "pays semblables échangent dans la même branche.",
    'r': "On montre que les modèles classiques font dépendre l’échange d’une "
         "différence, ce qui les rend structurellement incapables d’expliquer "
         "le commerce entre économies semblables.",
    'ex': "Les échanges entre la France et l’Allemagne, voitures contre "
          "voitures."},
   {'q': "Sujet sur le rôle de la demande dans les échanges",
    'f': "Le commerce intrabranche impose d’introduire la demande dans "
         "l’analyse. Le cours mobilise deux apports : Lassudrie-Duchêne "
         "montre que les consommateurs peuvent rechercher la différence, les "
         "produits d’une même branche n’étant pas perçus comme identiques ; "
         "Linder montre que la proximité des niveaux de vie rapproche les "
         "structures de demande, de sorte que les pays de niveau de vie "
         "comparable échangent davantage entre eux.",
    'r': "On montre que les deux analyses répondent à des questions "
         "distinctes, la nature des biens échangés et l’identité des "
         "partenaires, ce qui les rend complémentaires.",
    'ex': "La concurrence monopolistique de Chamberlin en 1933, que "
          "Lassudrie-Duchêne reprend pour formaliser la demande de "
          "différence."},
   {'q': "Sujet sur les nouvelles théories du commerce international",
    'f': "Expliquer le commerce entre semblables a exigé deux "
         "renouvellements. Du côté de la demande, les analyses de "
         "Lassudrie-Duchêne et de Linder montrent que l’échange ne repose pas "
         "uniquement sur l’offre. Du côté de l’offre, le cours indique qu’une "
         "autre révolution théorique est nécessaire : introduire "
         "explicitement les rendements croissants et les économies d’échelle, "
         "ce qui est l’apport central de Krugman.",
    'r': "On montre que les deux renouvellements sont cumulatifs, la demande "
         "expliquant la variété désirée et les rendements croissants sa "
         "concentration géographique.",
    'ex': "L’article de Krugman de 1979 sur les rendements croissants, la "
          "concurrence monopolistique et le commerce international."},
   {'q': "Sujet sur la nature des gains du commerce",
    'f': "Le commerce intrabranche procure un gain d’une autre nature que le "
         "commerce interbranche. Dans le commerce interbranche, le gain vient "
         "de l’allocation des facteurs selon les avantages comparatifs. Dans "
         "le commerce intrabranche entre économies semblables, il vient de "
         "l’accès à la variété, puisque les consommateurs peuvent rechercher "
         "la différence, et des économies d’échelle que l’élargissement du "
         "marché rend possibles.",
    'r': "On montre que la nature du gain change avec le type de commerce, "
         "ce qui explique que l’ouverture entre économies semblables soit "
         "moins conflictuelle que l’ouverture entre économies inégales.",
    'ex': "La différenciation horizontale de Chamberlin, qui ne repose pas "
          "sur une différence objective de qualité mais sur la perception du "
          "consommateur."}],
  voisins=['n16-differenciation-produits', 'n16-demande-representative',
           'n16-economies-echelle', 'n16-gains-echange'])


d('n16-differenciation-produits', 16, "Différenciation des produits",
  "Des biens de la même branche qui ne sont pas les mêmes",
  "La différenciation des produits est le fait que des biens appartenant à la "
  "même branche ne soient pas perçus comme identiques. Le cours la rattache à "
  "la concurrence monopolistique de Chamberlin en 1933, dont il distingue "
  "deux formes : la différenciation horizontale, qui ne repose pas sur une "
  "différence objective de qualité mais sur la perception du consommateur, et "
  "la différenciation verticale.",
  "Le cours mobilise la différenciation des produits pour résoudre un "
  "problème précis, celui du commerce intrabranche, et c’est cette fonction "
  "qui en fixe le contenu. Le point de départ est l’échec du modèle "
  "ricardien sur ce point : parmi ses hypothèses figure l’homogénéité des "
  "produits, le vin portugais et le vin anglais étant supposés identiques, de "
  "même que les draps, de sorte qu’il n’y a pas de différenciation. Or cette "
  "hypothèse interdit d’expliquer que des pays semblables échangent dans la "
  "même branche. Lassudrie-Duchêne lève l’hypothèse : deux économies proches "
  "peuvent produire dans la même branche, mais leurs produits ne sont pas "
  "nécessairement perçus comme parfaitement identiques, et les consommateurs "
  "peuvent rechercher la différence, ce qui permet de comprendre que la "
  "France et l’Allemagne échangent des voitures contre des voitures. La "
  "logique ne repose donc plus sur des dotations factorielles "
  "fondamentalement différentes mais sur la différenciation des produits. "
  "Pour formaliser cette idée, Lassudrie-Duchêne reprend l’analyse de la "
  "concurrence monopolistique développée par Chamberlin en 1933 : Chamberlin "
  "montre que les entreprises peuvent différencier leurs produits, et que "
  "cette différenciation leur permet de disposer d’un certain pouvoir de "
  "marché. Le cours distingue alors deux formes. La différenciation "
  "horizontale ne repose pas sur une différence objective de qualité mais sur "
  "la perception du consommateur : deux biens peuvent être objectivement "
  "comparables et pourtant préférés l’un à l’autre. La différenciation "
  "verticale correspond en revanche à des écarts de qualité, et le cours la "
  "relie aux spécialisations par gamme. Les conséquences théoriques sont "
  "importantes. D’abord le cadre de la concurrence pure et parfaite est "
  "abandonné, puisque la différenciation procure un pouvoir de marché : le "
  "cours relie d’ailleurs cette analyse au chapitre sur la concurrence "
  "imparfaite. Ensuite le gain du commerce change de nature, puisqu’il porte "
  "sur la variété offerte aux consommateurs plutôt que sur l’allocation des "
  "facteurs. Enfin la différenciation permet de penser la concurrence "
  "autrement que par le prix, par la marque, la qualité perçue et la "
  "position dans la gamme, ce qui éclaire la stratégie des firmes autant que "
  "la structure des échanges.",
  [("L’abandon de l’homogénéité",
    "Le modèle ricardien supposait des produits identiques, le vin portugais "
    "et le vin anglais étant indifférenciés : lever cette hypothèse est le "
    "préalable de toute analyse de la différenciation."),
   ("La perception d’une différence",
    "Les produits d’une même branche ne sont pas nécessairement perçus comme "
    "parfaitement identiques : c’est la perception, et non la seule "
    "caractéristique objective, qui fonde la différence."),
   ("La recherche de la variété",
    "Les consommateurs peuvent rechercher la différence : la demande porte "
    "alors sur un ensemble de variétés et non sur une quantité d’un bien "
    "homogène."),
   ("L’acquisition d’un pouvoir de marché",
    "Avec Chamberlin, la différenciation permet à l’entreprise de disposer "
    "d’un certain pouvoir de marché : elle n’est plus simple preneuse de "
    "prix."),
   ("La distinction des deux formes",
    "La différenciation horizontale repose sur la perception du consommateur "
    "sans différence objective de qualité ; la différenciation verticale "
    "repose sur des écarts de qualité."),
   ("L’échange croisé dans la même branche",
    "Chaque pays exporte ses variétés et importe celles des autres : le "
    "commerce intrabranche devient la conséquence normale de la "
    "différenciation.")],
  [{'a': "La différenciation explique le commerce entre économies semblables, "
         "que les théories fondées sur la différence ne peuvent pas "
         "produire.",
    'cond': "Elle suppose que les consommateurs valorisent la variété, ce "
            "que le cours formule comme une demande de différence.",
    'lim': "Le cours montre que l’explication par la demande ne suffit pas : "
           "il faut y ajouter les rendements croissants pour comprendre la "
           "concentration géographique de la production."},
   {'a': "Elle fournit un fondement microéconomique solide, par la "
         "concurrence monopolistique de Chamberlin.",
    'cond': "Le fondement suppose que la différenciation procure "
            "effectivement un pouvoir de marché, ce que Chamberlin établit "
            "en 1933.",
    'lim': "Ce cadre rompt avec la concurrence pure et parfaite du modèle "
           "ricardien : il complète la théorie classique en changeant ses "
           "hypothèses."},
   {'a': "La distinction entre différenciation horizontale et verticale "
         "permet d’analyser les spécialisations par gamme.",
    'cond': "La distinction suppose que l’on puisse séparer l’écart objectif "
            "de qualité de la seule perception du consommateur.",
    'lim': "Cette séparation est délicate en pratique : une marque peut "
           "produire une qualité perçue sans écart technique mesurable."},
   {'a': "Elle change la nature du gain du commerce, qui porte sur la variété "
         "plutôt que sur l’allocation.",
    'cond': "Le gain suppose que l’accès à des variétés étrangères accroisse "
            "effectivement la satisfaction des consommateurs.",
    'lim': "Ce gain est difficile à mesurer : il ne se traduit pas par un "
           "volume de production supplémentaire comme le gain d’allocation."},
   {'a': "Elle éclaire la stratégie des firmes autant que la structure des "
         "échanges, par la concurrence hors prix.",
    'cond': "L’argument suppose que la concurrence puisse porter sur la "
            "marque, la qualité perçue et la position dans la gamme.",
    'lim': "Le cours montre que ce pouvoir de marché a un coût collectif : "
           "la concurrence imparfaite éloigne de l’optimum concurrentiel."}],
  [{'t': "Les produits sont homogènes : le vin portugais et le vin anglais "
         "sont identiques, de même que les draps.",
    'qui': "David Ricardo, dans les hypothèses du modèle que le cours "
           "énumère.",
    'rep': "Le cours objecte que cette hypothèse interdit d’expliquer près "
           "de la moitié du commerce observé : le commerce intrabranche "
           "représente environ quarante à cinquante pour cent des échanges."},
   {'t': "La différenciation n’est qu’une illusion entretenue par la "
         "publicité : elle ne correspond à aucune différence réelle.",
    'qui': "L’objection que suggère la définition de la différenciation "
           "horizontale dans le cours.",
    'rep': "Le cours ne tranche pas sur la réalité de la différence mais sur "
           "son effet : la différenciation horizontale repose sur la "
           "perception du consommateur, et cette perception suffit à produire "
           "un échange et un pouvoir de marché."},
   {'t': "La cause du commerce intrabranche n’est pas la différenciation mais "
         "les économies d’échelle, qui concentrent la production de chaque "
         "variété.",
    'qui': "Paul Krugman, dont le cours date l’article de 1979.",
    'rep': "Le cours présente les deux explications comme "
           "complémentaires : la différenciation explique pourquoi plusieurs "
           "variétés sont demandées, les rendements croissants pourquoi "
           "chacune est produite en un seul lieu."},
   {'t': "La différenciation permet aux entreprises d’échapper à la "
         "concurrence, ce qui réduit le bien-être des consommateurs.",
    'qui': "L’analyse de la concurrence imparfaite que le cours développe "
           "dans le chapitre sur les stratégies des entreprises.",
    'rep': "Le cours tient les deux effets : la différenciation procure un "
           "pouvoir de marché, mais elle offre aussi aux consommateurs la "
           "variété qu’ils recherchent, ce qui constitue un gain propre."}],
  [{'n': "Edward Chamberlin",
    'i': "Les entreprises peuvent différencier leurs produits, ce qui leur "
         "procure un certain pouvoir de marché.",
    'p': "Le cours date son analyse de 1933 et en fait le cadre théorique de "
         "la concurrence monopolistique, dont il tire la distinction entre "
         "différenciation horizontale, fondée sur la perception du "
         "consommateur, et différenciation verticale."},
   {'n': "Lassudrie-Duchêne",
    'i': "Les consommateurs peuvent rechercher la différence, ce qui engendre "
         "un échange entre pays semblables.",
    'p': "Le cours précise que deux économies proches peuvent produire dans "
         "la même branche sans que leurs produits soient perçus comme "
         "parfaitement identiques, et qu’il reprend l’analyse de Chamberlin "
         "pour formaliser cette demande de différence."},
   {'n': "David Ricardo",
    'i': "Le modèle du commerce suppose l’homogénéité parfaite des "
         "produits échangés entre les pays.",
    'p': "Le cours range cette hypothèse parmi les quatre du modèle "
         "ricardien : le vin portugais et le vin anglais sont supposés "
         "identiques, de même que les draps, de sorte qu’il n’y a pas de "
         "différenciation des produits."},
   {'n': "Paul Krugman",
    'i': "Les rendements croissants expliquent pourquoi chaque variété est "
         "produite en un petit nombre de lieux.",
    'p': "Le cours renvoie à son article de 1979 sur les rendements "
         "croissants, la concurrence monopolistique et le commerce "
         "international : la différenciation crée la demande de variétés, les "
         "économies d’échelle en concentrent la production."}],
  [{'f': "Le modèle ricardien suppose l’homogénéité des produits : le vin "
         "portugais et le vin anglais sont supposés identiques.",
    'p': "L’hypothèse montre que la différenciation est exclue par "
         "construction des théories classiques, ce qui explique leur silence "
         "sur le commerce intrabranche."},
   {'f': "Chamberlin formule en 1933 l’analyse de la concurrence "
         "monopolistique, où la différenciation procure un pouvoir de marché.",
    'p': "La référence datée montre que l’outil préexistait à son "
         "application au commerce international, importé par "
         "Lassudrie-Duchêne."},
   {'f': "Le cours distingue différenciation horizontale, fondée sur la "
         "perception du consommateur sans différence objective de qualité, et "
         "différenciation verticale.",
    'p': "La distinction permet d’analyser séparément la variété, qui porte "
         "sur des goûts, et la gamme, qui porte sur des niveaux de qualité."},
   {'f': "Le cours prend l’exemple des échanges franco-allemands de voitures "
         "contre voitures.",
    'p': "L’exemple montre que la différenciation suffit à produire un "
         "échange croisé dans une même branche entre deux économies de "
         "dotations proches."}],
  [{'q': "Sujet sur la différenciation et les échanges internationaux",
    'f': "La différenciation lève l’hypothèse qui interdisait d’expliquer le "
         "commerce entre économies semblables. Le cours rappelle que le "
         "modèle ricardien suppose l’homogénéité des produits, le vin "
         "portugais et le vin anglais étant supposés identiques. "
         "Lassudrie-Duchêne lève cette hypothèse : les produits d’une même "
         "branche ne sont pas nécessairement perçus comme parfaitement "
         "identiques et les consommateurs peuvent rechercher la différence.",
    'r': "On montre que le commerce intrabranche découle logiquement de "
         "l’abandon d’une seule hypothèse, ce qui éclaire le rôle des "
         "hypothèses dans la portée d’un modèle.",
    'ex': "Les échanges franco-allemands de voitures contre voitures, que le "
          "cours donne comme illustration."},
   {'q': "Sujet sur la concurrence imparfaite et le commerce",
    'f': "La différenciation fait sortir l’analyse du commerce du cadre "
         "concurrentiel. Le cours s’appuie sur Chamberlin en 1933 : les "
         "entreprises peuvent différencier leurs produits, et cette "
         "différenciation leur permet de disposer d’un certain pouvoir de "
         "marché. Le commerce international cesse donc d’être analysable dans "
         "le cadre strict de la concurrence pure et parfaite retenu par "
         "Ricardo.",
    'r': "On montre que l’explication du commerce observé exige des "
         "hypothèses de marché imparfait, ce qui rapproche l’économie "
         "internationale de la microéconomie des structures de marché.",
    'ex': "La distinction du cours entre différenciation horizontale et "
          "verticale."},
   {'q': "Sujet sur la nature des gains de l’échange",
    'f': "La différenciation change ce que l’on gagne à échanger. Dans le "
         "modèle classique, le gain vient de l’allocation des facteurs selon "
         "les avantages comparatifs. Avec la différenciation, il vient de "
         "l’accès à la variété : les consommateurs peuvent rechercher la "
         "différence, et l’ouverture leur donne accès aux variétés produites "
         "ailleurs, sans qu’aucune réallocation de facteurs soit nécessaire.",
    'r': "On montre que le gain de variété est d’une autre nature que le "
         "gain d’allocation, ce qui explique qu’il ne se mesure pas par un "
         "supplément de production.",
    'ex': "La demande de différence de Lassudrie-Duchêne, formalisée par la "
          "concurrence monopolistique."},
   {'q': "Sujet sur la compétitivité hors prix",
    'f': "La différenciation permet de penser la concurrence autrement que "
         "par le prix. Avec Chamberlin, la différenciation procure un pouvoir "
         "de marché, et le cours distingue la différenciation horizontale, "
         "fondée sur la perception du consommateur sans écart objectif de "
         "qualité, de la différenciation verticale, fondée sur la qualité. La "
         "position dans la gamme devient alors un déterminant de la "
         "compétitivité.",
    'r': "On montre que la compétitivité ne se réduit pas au coût, ce qui "
         "explique qu’un pays à salaires élevés puisse exporter massivement.",
    'ex': "Les échanges intrabranche entre économies avancées, qui "
          "représentent environ quarante à cinquante pour cent du commerce."}],
  voisins=['n16-commerce-interbranche-intrabranche',
           'n16-economies-echelle', 'n16-demande-representative',
           'n16-gains-echange'])


d('n16-economies-echelle', 16, "Économies d’échelle",
  "Produire plus pour produire moins cher, et le cercle qui s’ensuit",
  "Les économies d’échelle désignent la baisse du coût unitaire lorsque la "
  "production augmente. Le cours en fait l’apport central de Krugman en "
  "économie internationale : l’ouverture agrandit le marché, ce qui accroît "
  "la production, engendre des économies d’échelle, abaisse les coûts et "
  "renforce la compétitivité, de sorte que l’avantage comparatif est "
  "lui-même renforcé par l’échange.",
  "Le cours fait des économies d’échelle le pivot d’un renversement "
  "théorique, et c’est ce renversement qu’il faut mettre au centre. Les "
  "théories traditionnelles suivent un ordre fixe : avantage comparatif, puis "
  "spécialisation, puis ouverture et échanges. Krugman inverse cet ordre : "
  "ouverture, puis marché plus grand, puis production accrue, puis économies "
  "d’échelle, puis coûts réduits, puis compétitivité accrue, puis avantage "
  "comparatif renforcé. Le cours en tire la formule décisive : un pays ne se "
  "contente pas d’exporter parce qu’il est compétitif, il peut devenir plus "
  "compétitif parce qu’il exporte. Cela crée un mécanisme cumulatif, "
  "c’est-à-dire que l’avantage s’auto-renforce au lieu d’être donné. Les "
  "références sont datées par le cours : l’article de 1979 sur les rendements "
  "croissants, la concurrence monopolistique et le commerce international, et "
  "Geography and Trade en 1991. Le second apport est géographique et découle "
  "du premier : si la production d’une variété se concentre pour exploiter "
  "les économies d’échelle, alors les activités économiques tendent à "
  "s’agglomérer durablement dans certains territoires, ce que le cours "
  "nomme la nouvelle géographie économique. L’implication est forte, puisque "
  "la localisation cesse d’être déterminée par les dotations naturelles pour "
  "dépendre de l’histoire et des rendements croissants. Le troisième apport "
  "est une explication du commerce intrabranche : si chaque variété doit être "
  "produite à grande échelle pour être rentable, alors chaque pays ne peut "
  "produire qu’un petit nombre de variétés et importe les autres, ce qui "
  "engendre des échanges croisés dans une même branche entre économies "
  "semblables. Le cours relie enfin les économies d’échelle à d’autres "
  "chapitres : elles figurent parmi les avantages dont dispose une firme "
  "multinationale, aux côtés du financement, des technologies, de la marque "
  "et du réseau mondial, ce qui explique que les entreprises locales ne "
  "puissent pas rivaliser et qu’un effet d’éviction apparaisse ; et elles "
  "expliquent la pression à la concentration que la mondialisation exerce sur "
  "les entreprises, obligées d’atteindre une taille internationale.",
  [("La baisse du coût unitaire",
    "Lorsque la production augmente, les coûts fixes se répartissent sur "
    "davantage d’unités et le coût unitaire baisse : c’est le mécanisme "
    "élémentaire des rendements croissants."),
   ("L’élargissement du marché par l’ouverture",
    "L’ouverture donne accès à un marché plus grand que le marché "
    "national : la production peut donc atteindre une échelle inaccessible en "
    "autarcie."),
   ("Le renforcement de la compétitivité",
    "Coûts réduits signifie compétitivité accrue : le pays exporte davantage, "
    "ce qui agrandit encore son marché et abaisse encore ses coûts."),
   ("Le caractère cumulatif",
    "Le cours insiste : un pays peut devenir plus compétitif parce qu’il "
    "exporte, ce qui crée un mécanisme cumulatif et non un équilibre "
    "déterminé par les dotations."),
   ("La concentration géographique",
    "Si chaque variété doit être produite à grande échelle, sa production se "
    "concentre : les activités tendent à s’agglomérer durablement dans "
    "certains territoires."),
   ("La spécialisation par variété",
    "Chaque pays ne pouvant produire qu’un petit nombre de variétés à grande "
    "échelle, il importe les autres : d’où les échanges croisés dans une même "
    "branche."),
   ("L’avantage de taille des firmes",
    "Les économies d’échelle figurent parmi les avantages d’une firme "
    "multinationale, ce qui explique que les entreprises locales fragiles "
    "disparaissent.")],
  [{'a': "Le renversement de causalité explique des spécialisations que les "
         "dotations ne prédisent pas.",
    'cond': "Il suppose des rendements croissants effectifs, donc des coûts "
            "fixes importants relativement aux coûts variables.",
    'lim': "Dans les activités à rendements constants, le mécanisme ne joue "
           "pas : le cours ne l’applique pas aux spécialisations primaires."},
   {'a': "Il rend compte de la persistance des positions acquises, par le "
         "caractère cumulatif du mécanisme.",
    'cond': "La persistance suppose que l’avantage de coût obtenu par "
            "l’échelle ne soit pas rattrapé par un concurrent entrant.",
    'lim': "Le cours montre que les positions peuvent se déplacer : la "
           "Chine monte progressivement en gamme, ce qui suppose un "
           "rattrapage possible."},
   {'a': "Il explique le commerce intrabranche du côté de l’offre, là où Linder "
         "et Lassudrie-Duchêne l’expliquaient par la seule demande.",
    'cond': "L’explication suppose que chaque variété doive être produite à "
            "grande échelle pour être rentable.",
    'lim': "Le cours présente les deux explications comme cumulatives et non "
           "concurrentes : la demande crée le besoin de variété, l’échelle en "
           "concentre la production."},
   {'a': "Il fonde la nouvelle géographie économique, qui explique "
         "l’agglomération durable des activités.",
    'cond': "L’agglomération suppose que les économies d’échelle l’emportent "
            "sur les coûts de transport et de congestion.",
    'lim': "Le cours relie l’agglomération à la baisse des coûts de "
           "transport : une remontée de ces coûts pourrait inverser le "
           "mouvement, ce qu’il évoque avec la relocalisation."},
   {'a': "Il éclaire la pression à la concentration que la mondialisation "
         "exerce sur la taille des entreprises.",
    'cond': "La pression suppose que la concurrence soit mondiale, ce que le "
            "cours établit en notant que la mondialisation oblige les "
            "entreprises à atteindre une taille internationale.",
    'lim': "Le cours relève le coût de cette concentration : les "
           "entreprises locales fragiles disparaissent, et l’effet "
           "d’éviction apparaît."}],
  [{'t': "L’avantage comparatif précède l’échange : c’est lui qui détermine "
         "la spécialisation puis l’ouverture.",
    'qui': "Les théories traditionnelles, de Ricardo au modèle HOS, que le "
           "cours expose.",
    'rep': "Le cours souligne le renversement de Krugman : un pays ne se "
           "contente pas d’exporter parce qu’il est compétitif, il peut "
           "devenir plus compétitif parce qu’il exporte."},
   {'t': "Le commerce intrabranche s’explique par la demande de variété des "
         "consommateurs et non par les conditions de l’offre.",
    'qui': "Lassudrie-Duchêne et Linder, dont le cours expose les analyses.",
    'rep': "Le cours indique qu’une autre révolution théorique est "
           "nécessaire après ces analyses : introduire explicitement les "
           "rendements croissants et les économies d’échelle, ce qui est "
           "l’apport central de Krugman."},
   {'t': "Les économies d’échelle avantagent systématiquement les grandes "
         "firmes, au détriment du tissu productif local.",
    'qui': "L’analyse de l’effet d’éviction que le cours développe à propos "
           "des multinationales.",
    'rep': "Le cours maintient l’ambivalence : l’entrée d’une multinationale "
           "peut dynamiser le tissu productif local mais également évincer "
           "des entreprises domestiques, selon le pays, le secteur et la "
           "position dans la chaîne de valeur."},
   {'t': "Le mécanisme cumulatif condamne les retardataires : l’avantage "
         "acquis ne peut plus être rattrapé.",
    'qui': "La conséquence pessimiste du caractère cumulatif que le cours "
           "décrit.",
    'rep': "Le cours fournit le contre-exemple chinois : utilisant d’abord "
           "les chaînes de valeur mondiales comme pays atelier, la Chine "
           "monte progressivement en gamme et augmente la part de valeur "
           "ajoutée domestique dans ses exportations."}],
  [{'n': "Paul Krugman",
    'i': "L’ouverture crée et renforce l’avantage comparatif par les "
         "économies d’échelle.",
    'p': "Le cours renvoie à son article de 1979 sur les rendements "
         "croissants, la concurrence monopolistique et le commerce "
         "international, et résume le mécanisme cumulatif : ouverture, marché "
         "plus grand, production accrue, économies d’échelle, coûts réduits, "
         "compétitivité accrue, avantage renforcé."},
   {'n': "Paul Krugman",
    'i': "Les activités économiques tendent à s’agglomérer durablement dans "
         "certains territoires.",
    'p': "Le cours renvoie à Geography and Trade, publié en 1991, et pose la "
         "problématique : comment l’ouverture elle-même peut-elle créer et "
         "renforcer les avantages comparatifs, et pourquoi les activités "
         "s’agglomèrent-elles durablement."},
   {'n': "Edward Chamberlin",
    'i': "La différenciation des produits procure un pouvoir de marché aux "
         "entreprises.",
    'p': "Le cours date son analyse de 1933 : c’est le cadre de concurrence "
         "monopolistique que Krugman mobilise, puisque les rendements "
         "croissants supposent que les entreprises ne soient pas de simples "
         "preneuses de prix."},
   {'n': "Richard Baldwin",
    'i': "La baisse des coûts de transport et de communication transforme la "
         "géographie de la production.",
    'p': "Le cours l’associe aux coûts de transport et aux chaînes de valeur "
         "mondiales : c’est cette baisse qui permet d’exploiter les économies "
         "d’échelle en séparant géographiquement les étapes d’un même "
         "processus productif."}],
  [{'f': "Le cours résume le renversement de Krugman : ouverture, marché plus "
         "grand, production accrue, économies d’échelle, coûts réduits, "
         "compétitivité accrue, avantage comparatif renforcé.",
    'p': "La chaîne inverse l’ordre traditionnel : elle fait de l’échange la "
         "cause de l’avantage et non sa conséquence, ce qui rend la "
         "spécialisation dépendante de l’histoire."},
   {'f': "Krugman publie son article sur les rendements croissants en 1979 et "
         "Geography and Trade en 1991.",
    'p': "Les deux dates distinguent les deux apports : l’explication du "
         "commerce entre semblables d’abord, l’analyse de l’agglomération "
         "ensuite."},
   {'f': "Le cours formule la conclusion : un pays peut devenir plus "
         "compétitif parce qu’il exporte.",
    'p': "La formule montre que l’avantage est en partie endogène, ce qui "
         "ouvre un espace à la politique commerciale et industrielle."},
   {'f': "Le cours range les économies d’échelle parmi les avantages d’une "
         "firme multinationale, aux côtés du financement, des technologies, "
         "de la marque et du réseau mondial.",
    'p': "Le fait montre que le mécanisme opère au niveau des firmes autant "
         "qu’à celui des pays, ce qui explique l’effet d’éviction sur les "
         "entreprises locales."}],
  [{'q': "Sujet sur les nouvelles théories du commerce international",
    'f': "Krugman inverse la relation traditionnelle entre avantage "
         "comparatif et commerce. Le cours oppose les deux chaînes : dans les "
         "théories traditionnelles, avantage comparatif puis spécialisation "
         "puis ouverture ; chez Krugman, ouverture puis marché plus grand "
         "puis production accrue puis économies d’échelle puis coûts réduits "
         "puis avantage comparatif renforcé. D’où la formule : un pays peut "
         "devenir plus compétitif parce qu’il exporte.",
    'r': "On montre que le renversement rend l’avantage endogène, ce qui "
         "transforme la spécialisation d’une donnée naturelle en un résultat "
         "historique.",
    'ex': "L’article de Krugman de 1979 sur les rendements croissants, la "
          "concurrence monopolistique et le commerce international."},
   {'q': "Sujet sur la localisation des activités économiques",
    'f': "Les économies d’échelle expliquent la concentration géographique. "
         "Le cours pose la problématique de Krugman dans Geography and Trade, "
         "publié en 1991 : pourquoi les activités économiques ont-elles "
         "tendance à s’agglomérer durablement dans certains territoires ? La "
         "réponse est que les rendements croissants rendent la concentration "
         "plus rentable que la dispersion, de sorte que l’histoire fixe la "
         "localisation.",
    'r': "On montre que la localisation dépend de rendements croissants et "
         "non de dotations naturelles, ce qui explique la persistance des "
         "territoires industriels.",
    'ex': "La nouvelle géographie économique de Krugman, que le cours "
          "rattache à Geography and Trade."},
   {'q': "Sujet sur l’explication du commerce entre pays semblables",
    'f': "Les économies d’échelle complètent les explications par la "
         "demande. Si chaque variété doit être produite à grande échelle pour "
         "être rentable, alors chaque pays ne peut produire qu’un petit "
         "nombre de variétés et importe les autres : d’où des échanges "
         "croisés dans une même branche entre économies semblables. Le cours "
         "présente cet apport comme la révolution théorique nécessaire après "
         "Lassudrie-Duchêne et Linder.",
    'r': "On montre que la demande explique pourquoi plusieurs variétés sont "
         "souhaitées et l’échelle pourquoi chacune est produite en un seul "
         "lieu, ce qui rend les deux explications complémentaires.",
    'ex': "Le commerce intrabranche, qui représente environ quarante à "
          "cinquante pour cent des échanges."},
   {'q': "Sujet sur la taille des entreprises dans la mondialisation",
    'f': "Les économies d’échelle opèrent au niveau des firmes autant que "
         "des pays. Le cours les range parmi les avantages d’une firme "
         "multinationale, aux côtés du financement, des technologies, de la "
         "marque et du réseau mondial, et en tire la conséquence : les "
         "entreprises locales ne peuvent pas rivaliser, de sorte que les plus "
         "fragiles disparaissent et qu’un effet d’éviction apparaît.",
    'r': "On montre que le même mécanisme qui procure un gain collectif "
         "produit une asymétrie entre acteurs, ce qui explique l’ambivalence "
         "des effets de la mondialisation productive.",
    'ex': "La formule du cours : la mondialisation oblige les entreprises à "
          "atteindre une taille internationale."}],
  voisins=['n16-commerce-interbranche-intrabranche',
           'n16-differenciation-produits', 'n16-avantages-comparatifs',
           'n17-chaines-valeur'])
