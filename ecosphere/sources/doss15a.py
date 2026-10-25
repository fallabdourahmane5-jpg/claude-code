# -*- coding: utf-8 -*-
"""Ensemble 15 — L’État et les politiques économiques (1/5)."""

from doss_base import d

d('n15-etat-minimal', 15, "État minimal",
  "L’État qui se borne au cadre, parce que le marché coordonne mieux",
  "L’État minimal désigne la conception selon laquelle l’intervention "
  "publique doit se limiter au cadre de l’échange, le marché assurant "
  "lui-même la coordination. Le cours ne consacre pas de section à cette "
  "expression mais en donne tous les éléments : la main invisible chez Smith, "
  "la supériorité du marché comme mécanisme de coordination, et la formule de "
  "la nouvelle économie classique selon laquelle la meilleure politique "
  "économique est l’absence de politique économique.",
  "Le cours construit la position de l’État minimal par étapes successives, "
  "et cette construction en montre à la fois la cohérence et les versions "
  "distinctes. La première étape est classique. Les classiques comme les "
  "néoclassiques considèrent que le marché est le meilleur mécanisme de "
  "coordination des activités économiques : chez Adam Smith en 1776 cette "
  "idée repose sur la main invisible, chez les néoclassiques sur l’ajustement "
  "de l’offre et de la demande par les prix. Dans les deux cas le marché est "
  "vu comme l’institution qui rend l’intervention superflue, puisque la "
  "poursuite des intérêts particuliers produit un résultat collectif "
  "satisfaisant sans direction centrale. La deuxième étape est "
  "informationnelle, et le cours la rattache à Hayek : l’information "
  "économique étant dispersée et subjective, aucun agent ni aucun "
  "planificateur n’en dispose globalement, et ce sont les prix qui la "
  "transmettent. Le marché est alors un processus de découverte, et c’est "
  "précisément parce que l’information est imparfaite que la concurrence est "
  "utile. L’argument est plus fort que le précédent : il ne dit pas seulement "
  "que l’État est inutile, mais qu’il ne peut pas savoir ce qu’il faudrait "
  "savoir pour agir correctement. La troisième étape est celle des "
  "anticipations, et le cours la situe dans la nouvelle économie classique. "
  "Dans cette perspective, l’intervention de l’État est non seulement "
  "inutile, mais dangereuse : les politiques discrétionnaires créent de "
  "l’incertitude, perturbent les anticipations et accentuent l’instabilité "
  "économique. Le cours en tire la formule la plus radicale qu’il rapporte : "
  "la meilleure politique économique est donc l’absence de politique "
  "économique, et seules sont acceptées des règles simples, crédibles et "
  "stables dans le temps. Pour la nouvelle économie classique, les marchés "
  "sont efficaces, les agents parfaitement rationnels, la monnaie neutre, et "
  "l’État inutile voire nuisible. La quatrième étape est monétariste : "
  "Friedman propose de laisser faire le marché, de laisser le chômage revenir "
  "à son niveau naturel et de contrôler la croissance de la masse monétaire "
  "par une règle. Le cours ne conclut pourtant pas en faveur de cette "
  "position : il la place en vis-à-vis de l’analyse keynésienne et des "
  "défaillances de marché, externalités, biens collectifs et asymétries "
  "d’information, qui justifient au contraire l’intervention publique.",
  [("La coordination par les prix",
    "Les prix transmettent l’information nécessaire à la décision : le "
    "marché assure l’ajustement de l’offre et de la demande sans qu’aucune "
    "instance n’ait à connaître l’ensemble des besoins."),
   ("La main invisible",
    "Chez Adam Smith en 1776, la poursuite des intérêts particuliers produit "
    "un résultat collectif satisfaisant : le cours en fait le fondement "
    "classique de la supériorité du marché."),
   ("L’impossibilité du calcul central",
    "Avec Hayek, l’information est dispersée et subjective, et aucun "
    "planificateur n’en dispose globalement : l’État ne peut donc pas savoir "
    "ce qu’il faudrait savoir pour agir à bon escient."),
   ("La perturbation des anticipations",
    "Les politiques discrétionnaires créent de l’incertitude et perturbent "
    "les anticipations : l’intervention devient non seulement inutile mais "
    "dangereuse."),
   ("La neutralisation par les agents",
    "Les agents parfaitement rationnels anticipent la politique et ajustent "
    "salaires et prix : l’effet réel disparaît et il ne reste que les "
    "variables nominales."),
   ("Le retrait au profit de règles",
    "Seules sont acceptées des règles simples, crédibles et stables dans le "
    "temps : l’État ne disparaît pas, il cesse de décider au coup par coup.")],
  [{'a': "La position évite de supposer que l’État dispose d’une information "
         "qu’aucun agent ne possède, ce qui est l’argument le plus solide "
         "contre la planification.",
    'cond': "L’argument suppose, comme chez Hayek, que l’information "
            "économique soit dispersée et subjective et que les prix la "
            "transmettent effectivement.",
    'lim': "Le cours montre que les prix peuvent cesser de transmettre "
           "l’information : avec les produits structurés, l’investisseur ne "
           "voit plus la qualité réelle des créances."},
   {'a': "Elle met en évidence un coût réel de l’intervention, "
         "l’incertitude qu’elle crée pour les décisions privées.",
    'cond': "Le coût suppose que les agents réagissent à la politique "
            "suivie, hypothèse que les anticipations rationnelles "
            "formalisent.",
    'lim': "Le cours oppose la nouvelle économie keynésienne : rigidités, "
           "asymétries d’information et concurrence imparfaite font que "
           "l’économie peut rester durablement en sous-emploi sans "
           "intervention."},
   {'a': "Elle fonde la préférence pour les règles, qui donne de la "
         "prévisibilité sans supprimer toute action publique.",
    'cond': "La préférence suppose que la règle soit crédible et stable dans "
            "le temps, faute de quoi elle n’apporte pas la prévisibilité "
            "attendue.",
    'lim': "Une règle rigide prive l’autorité de réaction en cas de choc : "
           "le cours montre qu’après 2008 il a fallu des instruments non "
           "conventionnels non prévus par aucune règle."},
   {'a': "Elle oblige à justifier chaque intervention par une défaillance de "
         "marché identifiée plutôt que par une préférence générale.",
    'cond': "L’exigence suppose que l’on puisse caractériser la "
            "défaillance, ce que le cours fait pour les externalités, les "
            "biens collectifs et les asymétries d’information.",
    'lim': "Le cours montre que ces défaillances sont nombreuses et "
           "ordinaires : l’exigence ne conduit donc pas à un État minimal "
           "mais à un État spécialisé."},
   {'a': "Elle éclaire le rôle de l’État comme garant du cadre juridique, "
         "qui conditionne l’investissement et l’innovation.",
    'cond': "Le rôle suppose que la croissance dépende de la crédibilité des "
            "règles, de la sécurité juridique et de la protection de la "
            "propriété, comme le cours l’établit.",
    'lim': "Cet État du cadre n’est pas minimal au sens budgétaire : le "
           "cours montre avec Barro que les dépenses publiques productives "
           "augmentent elles-mêmes la productivité privée."}],
  [{'t': "L’emploi dépend de la demande globale et non du seul marché du "
         "travail : face à l’instabilité du marché, l’État doit intervenir.",
    'qui': "John Maynard Keynes, dont le cours expose la conclusion "
           "centrale.",
    'rep': "La nouvelle économie classique répond que les agents anticipent "
           "et neutralisent l’effet réel : le cours rapporte que la monnaie "
           "est puissante mais que la politique monétaire est impuissante."},
   {'t': "Le marché est structurellement défaillant : externalités, biens "
         "collectifs et asymétries d’information empêchent l’allocation "
         "optimale.",
    'qui': "L’analyse des défaillances de marché que le cours développe, "
           "avec Pigou pour les externalités et Akerlof pour l’information.",
    'rep': "Les tenants du marché répondent que la défaillance publique "
           "existe aussi : le cours en donne un exemple avec l’aléa moral "
           "public, où l’État cesse de maîtriser son déficit s’il sait "
           "pouvoir compter sur la banque centrale."},
   {'t': "La croissance exige une intervention structurelle, notamment dans "
         "l’éducation, la recherche et les infrastructures.",
    'qui': "Robert Barro et les théories de la croissance endogène que le "
           "cours expose.",
    'rep': "Le cours maintient une condition d’efficacité qui limite "
           "l’argument : si les dépenses publiques sont excessives, il y a "
           "effet d’éviction du capital privé, et il existe un niveau optimal "
           "de capital public."},
   {'t': "L’État doit assurer les trois fonctions d’allocation, de "
         "stabilisation et de redistribution, que le marché ne remplit pas.",
    'qui': "Richard Musgrave, dans la théorie des finances publiques que le "
           "cours date de 1959.",
    'rep': "Le cours rapporte la critique de cet État étendu avec "
           "Rosanvallon : la crise de l’État providence conjugue un problème "
           "de financement, une crise d’efficacité et une crise de "
           "légitimité."}],
  [{'n': "Adam Smith",
    'i': "La main invisible fait que la poursuite des intérêts particuliers "
         "sert l’intérêt général.",
    'p': "Le cours situe cette idée en 1776 et en fait le fondement "
         "classique de la supériorité du marché : les classiques comme les "
         "néoclassiques considèrent que le marché est le meilleur mécanisme "
         "de coordination des activités économiques, les seconds par "
         "l’ajustement des prix."},
   {'n': "Friedrich Hayek",
    'i': "Le marché est un processus de découverte dans un monde "
         "d’information dispersée.",
    'p': "Le cours précise le raisonnement : l’information économique étant "
         "dispersée et subjective, aucun agent ni aucun planificateur n’en "
         "dispose globalement, et ce sont les prix qui la transmettent ; "
         "c’est précisément parce que l’information est imparfaite que la "
         "concurrence est utile."},
   {'n': "Milton Friedman",
    'i': "Il faut laisser faire le marché et laisser le chômage revenir à "
         "son niveau naturel.",
    'p': "Le cours résume sa solution en trois points, dont le troisième est "
         "de contrôler la croissance de la masse monétaire par une règle : "
         "l’État ne disparaît pas mais cesse d’agir discrétionnairement sur "
         "la conjoncture."},
   {'n': "Thomas Sargent",
    'i': "Une politique annoncée n’agit que sur les variables nominales, "
         "puisque les agents en intègrent les effets par avance.",
    'p': "Le cours en tire la préférence pour les règles plutôt que pour la "
         "discrétion, et la formule la plus radicale qu’il rapporte : la "
         "meilleure politique économique est l’absence de politique "
         "économique."}],
  [{'f': "Le cours rapporte que pour la nouvelle économie classique "
         "l’intervention de l’État est non seulement inutile, mais "
         "dangereuse.",
    'p': "La formulation marque le passage d’un argument d’inefficacité à un "
         "argument de nuisance : l’État n’est plus seulement superflu, il "
         "devient une source d’instabilité."},
   {'f': "Le cours résume la position de la nouvelle économie classique : "
         "marchés efficaces, agents parfaitement rationnels, monnaie neutre, "
         "État inutile voire nuisible.",
    'p': "L’énumération montre que la conclusion sur l’État découle "
         "d’hypothèses précises : elle tombe si l’une d’elles est levée, ce "
         "que fait la nouvelle économie keynésienne."},
   {'f': "Le cours relève que la croissance dépend de la crédibilité des "
         "règles, de la sécurité juridique et de la protection de la "
         "propriété.",
    'p': "Le fait montre que même la position la plus favorable au marché "
         "suppose un État : sans sécurité juridique, personne n’investit, "
         "personne n’innove et le capital fuit."},
   {'f': "Le cours illustre ce cadre institutionnel par l’Angleterre après "
         "la Glorieuse Révolution de 1688, avec limitation du pouvoir royal "
         "et renforcement du Parlement.",
    'p': "L’exemple montre que l’État minimal au sens budgétaire n’est pas "
         "l’État absent : c’est la construction d’un État de droit qui a "
         "rendu l’investissement privé possible."}],
  [{'q': "Sujet sur le rôle de l’État dans l’économie",
    'f': "La position la plus restrictive sur l’État n’est pas une "
         "préférence mais une conclusion tirée d’hypothèses. Le cours la "
         "résume pour la nouvelle économie classique : marchés efficaces, "
         "agents parfaitement rationnels, monnaie neutre, État inutile voire "
         "nuisible, d’où la formule selon laquelle la meilleure politique "
         "économique est l’absence de politique économique. Lever une seule "
         "de ces hypothèses rétablit un rôle pour l’intervention.",
    'r': "On montre que la conclusion dépend entièrement du jeu "
         "d’hypothèses, ce qui permet de discuter la thèse sans la caricaturer "
         "ni l’adopter.",
    'ex': "L’opposition que le cours établit avec la nouvelle économie "
          "keynésienne : rigidités, asymétries d’information et concurrence "
          "imparfaite."},
   {'q': "Sujet sur le marché comme mécanisme de coordination",
    'f': "L’argument le plus fort en faveur du marché est "
         "informationnel. Le cours le formule avec Hayek : l’information "
         "économique étant dispersée et subjective, aucun agent ni aucun "
         "planificateur n’en dispose globalement, et ce sont les prix qui la "
         "transmettent. C’est précisément parce que l’information est "
         "imparfaite que la concurrence est utile, et donc qu’un calcul "
         "central est impossible.",
    'r': "On montre que l’argument porte sur la capacité de connaître et non "
         "sur la volonté d’agir, ce qui le rend indépendant du jugement porté "
         "sur l’État.",
    'ex': "La main invisible chez Adam Smith en 1776, que le cours donne "
          "comme première formulation de cette coordination sans direction."},
   {'q': "Sujet sur les règles et la politique économique",
    'f': "L’État minimal ne signifie pas l’absence de l’État mais le "
         "remplacement de la décision par la règle. Le cours l’énonce pour la "
         "nouvelle économie classique : seules sont acceptées des règles "
         "simples, crédibles et stables dans le temps. Friedman en propose "
         "une application monétaire, le contrôle de la croissance de la masse "
         "monétaire, puisque la monnaie détermine l’inflation à long terme.",
    'r': "On distingue le volume de l’intervention et son mode d’exercice, "
         "ce qui montre que le débat porte autant sur la prévisibilité que "
         "sur l’étendue.",
    'ex': "La règle de pourcentage constant de croissance de la masse "
          "monétaire que Friedman propose."},
   {'q': "Sujet sur l’État et les conditions de la croissance",
    'f': "Même les analyses favorables au marché supposent un État. Le cours "
         "l’affirme nettement : la croissance dépend de la crédibilité des "
         "règles, car sans sécurité juridique personne n’investit, personne "
         "n’innove et le capital fuit. Avec Barro, les dépenses publiques "
         "productives augmentent même la productivité du secteur privé, bien "
         "qu’un excès entraîne un effet d’éviction du capital privé.",
    'r': "On distingue l’État du cadre et l’État de la conjoncture, pour "
         "montrer que la critique de l’intervention discrétionnaire ne "
         "conclut pas à l’État minimal au sens budgétaire.",
    'ex': "La Glorieuse Révolution de 1688 en Angleterre, que le cours "
          "donne comme exemple de stabilité institutionnelle favorable à "
          "l’investissement."}],
  voisins=['n15-etat-interventionniste', 'n15-regles-discretion',
           'n15-anticipations', 'n15-fonctions-musgrave'])


d('n15-etat-interventionniste', 15, "État interventionniste",
  "L’État providence, ses fonctions et sa crise",
  "L’État interventionniste désigne l’État qui agit sur l’activité, la "
  "répartition et l’allocation des ressources plutôt que de se borner au "
  "cadre de l’échange. Le cours l’organise autour de l’État providence "
  "d’après 1945, de ses trois fonctions selon Musgrave et du carré magique de "
  "Kaldor, puis de sa crise analysée par Pierre Rosanvallon en 1981.",
  "Le cours traite l’État interventionniste en trois moments, et cette forme "
  "chronologique en fait un objet de dissertation immédiatement utilisable. "
  "Premier moment, la justification théorique. Face à l’instabilité du "
  "marché, pour Keynes l’État doit intervenir, avec pour moyens d’action la "
  "politique budgétaire, les dépenses publiques et le déficit, la politique "
  "de relance, le soutien à l’investissement et la stabilisation de "
  "l’économie ; l’État peut créer une demande autonome pour relancer "
  "l’activité. Le cours ajoute l’argument de la nouvelle économie "
  "keynésienne : même dans un cadre de rationalité et de microfondements "
  "néoclassiques, les marchés ne s’auto-ajustent pas parfaitement, et en "
  "raison des rigidités, des asymétries d’information et de la concurrence "
  "imparfaite, l’économie peut rester durablement en situation de sous-emploi, "
  "ce qui justifie un rôle stabilisateur de l’État. Il y ajoute, du côté de "
  "la croissance, l’intervention structurelle justifiée par les externalités "
  "positives de l’éducation et, avec Barro, par le capital public. Deuxième "
  "moment, l’organisation. Le cours énumère les fonctions de l’État "
  "providence et commence par la difficulté : Kaldor et le carré magique, "
  "appelé magique parce qu’atteindre les quatre objectifs simultanément est "
  "impossible. Puis il énonce les trois fonctions de l’État providence selon "
  "Musgrave, dans la théorie des finances publiques de 1959 : fonction "
  "d’allocation des ressources, fonction de stabilisation ou de régulation, "
  "fonction de redistribution. Il distingue enfin deux types de politiques "
  "publiques, conjoncturelles à court terme, monétaire, budgétaire et fiscale, "
  "et structurelles à long terme, politique de la concurrence, politique "
  "fiscale et politique industrielle. Troisième moment, la crise. Le cours "
  "mobilise Pierre Rosanvallon et La crise de l’État providence, publiée en "
  "1981, qui identifie trois crises simultanées : un problème de financement, "
  "une crise d’efficacité et une crise de légitimité. Il en précise le "
  "ressort : avec une fiscalité élevée, les travailleurs se disent qu’il ne "
  "sert à rien de travailler si une grande partie de leur salaire va aux "
  "impôts, idée que la courbe de Laffer résume par la formule selon laquelle "
  "trop d’impôt tue l’impôt. Le cours n’adopte pourtant pas cette conclusion "
  "sans réserve, puisqu’il rapporte aussitôt les reproches faits à cette "
  "courbe.",
  [("Le constat d’une défaillance",
    "Les marchés ne s’auto-ajustent pas parfaitement : rigidités, asymétries "
    "d’information et concurrence imparfaite peuvent laisser l’économie "
    "durablement en sous-emploi."),
   ("La fonction de stabilisation",
    "L’État agit sur la conjoncture par le budget des administrations "
    "publiques ou par la création de monnaie, pour soutenir ou freiner la "
    "demande : relance d’un côté, rigueur de l’autre."),
   ("La fonction d’allocation",
    "L’État produit ou finance ce que le marché n’alloue pas correctement, "
    "en présence d’externalités ou de biens collectifs, et le cours y "
    "rattache le capital public de Barro."),
   ("La fonction de redistribution",
    "Par les prestations sociales et les prélèvements obligatoires, l’État "
    "transforme les revenus primaires en revenu disponible brut : la "
    "répartition devient un objet de politique publique."),
   ("La contrainte des objectifs multiples",
    "Le carré magique de Kaldor rappelle que les quatre objectifs, dont "
    "l’équilibre du solde extérieur, ne peuvent pas être atteints "
    "simultanément : toute politique est un arbitrage."),
   ("La crise du financement",
    "Avec Rosanvallon, l’extension des missions se heurte à un problème de "
    "financement, auquel s’ajoutent une crise d’efficacité et une crise de "
    "légitimité."),
   ("La résistance fiscale",
    "Le cours relève une résistance des acteurs économiques à la hausse des "
    "impôts, et rapporte la formule de la courbe de Laffer selon laquelle "
    "trop d’impôt tue l’impôt.")],
  [{'a': "L’intervention se justifie par une défaillance identifiée et non "
         "par une préférence, ce qui en fait un argument économique.",
    'cond': "La justification suppose que la défaillance soit caractérisée, "
            "externalité, bien collectif, asymétrie d’information ou "
            "insuffisance de demande.",
    'lim': "Le cours rappelle que les dispositifs de protection créent "
           "eux-mêmes de l’aléa moral : la solution est en même temps une "
           "partie du problème."},
   {'a': "Les trois fonctions de Musgrave donnent une grille complète qui "
         "évite de confondre des interventions de nature différente.",
    'cond': "La grille suppose que l’on rattache chaque mesure à sa fonction "
            "dominante, allocation, stabilisation ou redistribution.",
    'lim': "Les fonctions interfèrent : une prestation sociale redistribue "
           "et stabilise à la fois, ce que le cours montre en décrivant la "
           "hausse automatique des dépenses en période de ralentissement."},
   {'a': "Le carré magique de Kaldor impose de raisonner en arbitrages "
         "plutôt qu’en objectifs isolés.",
    'cond': "L’argument suppose que les quatre objectifs soient réellement "
            "concurrents, ce que le cours affirme en les déclarant "
            "impossibles à atteindre simultanément.",
    'lim': "Le cours ne hiérarchise pas ces objectifs : la grille signale le "
           "conflit sans indiquer lequel sacrifier."},
   {'a': "La distinction entre politiques conjoncturelles et structurelles "
         "clarifie l’horizon temporel de chaque instrument.",
    'cond': "La distinction suppose que l’on sache si le problème traité est "
            "un écart passager à la trajectoire ou un trait durable de "
            "l’appareil productif.",
    'lim': "La politique fiscale figure dans les deux catégories selon le "
           "cours : la frontière n’est donc pas étanche."},
   {'a': "L’analyse de la crise par Rosanvallon évite de réduire la "
         "difficulté à une question de financement.",
    'cond': "L’argument suppose que les trois crises soient distinctes, "
            "financement, efficacité et légitimité, et se renforcent "
            "mutuellement.",
    'lim': "Le cours ne tranche pas sur leur hiérarchie, et il relativise "
           "l’argument fiscal en rapportant les critiques adressées à la "
           "courbe de Laffer."}],
  [{'t': "L’intervention de l’État est non seulement inutile mais "
         "dangereuse : elle crée de l’incertitude et accentue l’instabilité.",
    'qui': "La nouvelle économie classique, telle que le cours la présente.",
    'rep': "Le cours maintient l’argument keynésien : l’économie peut rester "
           "durablement en situation de sous-emploi faute de mécanisme "
           "d’ajustement automatique, ce que ni les anticipations ni les "
           "règles ne corrigent."},
   {'t': "Trop d’impôt tue l’impôt : au-delà d’un seuil, la hausse des taux "
         "réduit les recettes en découragent l’activité.",
    'qui': "La courbe de Laffer, que le cours présente dans l’analyse de la "
           "crise de l’État providence.",
    'rep': "Le cours rapporte les reproches faits à cette courbe : elle ne "
           "relève pas de faits empiriques selon certains économistes, et "
           "des études montrent qu’à moyen terme une hausse du taux "
           "d’imposition n’a pas d’effet, les gens ne changeant pas toujours "
           "immédiatement de comportement."},
   {'t': "Les dépenses publiques évincent l’investissement privé plutôt que "
         "de le soutenir, au-delà d’un certain niveau de dépense.",
    'qui': "L’analyse de Robert Barro, que le cours expose dans le modèle de "
           "croissance endogène de 1990.",
    'rep': "Le cours restitue l’argument complet, qui est conditionnel : si "
           "les dépenses publiques sont trop faibles il y a sous-"
           "investissement collectif, si elles sont excessives il y a effet "
           "d’éviction, et il existe un niveau optimal de capital public."},
   {'t': "La politique monétaire est impuissante à réduire le chômage, "
         "puisque les individus anticipent et neutralisent son effet.",
    'qui': "Milton Friedman et l’école monétariste, dont le cours expose la "
           "conclusion.",
    'rep': "Le cours limite la portée de l’objection : elle vise la "
           "politique monétaire conjoncturelle, non les fonctions "
           "d’allocation et de redistribution que Musgrave distingue."}],
  [{'n': "Richard Musgrave",
    'i': "L’État providence remplit trois fonctions : allocation des "
         "ressources, stabilisation et redistribution.",
    'p': "Le cours situe cette analyse dans la théorie des finances "
         "publiques de 1959 et l’articule avec la distinction entre "
         "politiques conjoncturelles, monétaire, budgétaire et fiscale, et "
         "politiques structurelles, concurrence, fiscalité et politique "
         "industrielle."},
   {'n': "Pierre Rosanvallon",
    'i': "L’État providence connaît une crise à trois dimensions : "
         "financement, efficacité et légitimité.",
    'p': "Le cours cite La crise de l’État providence, publiée en 1981, et "
         "en précise le ressort fiscal : avec une fiscalité élevée, les "
         "travailleurs se disent qu’il ne sert à rien de travailler si une "
         "grande partie de leur salaire va aux impôts."},
   {'n': "Nicholas Kaldor",
    'i': "Les quatre objectifs du carré magique ne peuvent pas être atteints "
         "simultanément.",
    'p': "Le cours l’appelle carré magique précisément parce que la "
         "réalisation simultanée des quatre objectifs est impossible, et "
         "retient parmi eux l’équilibre du solde extérieur, mesuré par le "
         "rapport du solde de la balance des transactions courantes au "
         "produit intérieur brut."},
   {'n': "John Maynard Keynes",
    'i': "Face à l’instabilité du marché, l’État doit intervenir et peut "
         "créer une demande autonome.",
    'p': "Le cours énumère ses moyens d’action : politique budgétaire avec "
         "dépenses publiques et déficit, politique de relance, soutien à "
         "l’investissement et stabilisation de l’économie, puisque l’emploi "
         "dépend de la demande globale et non du seul marché du travail."}],
  [{'f': "Le cours attribue à Musgrave, dans la théorie des finances "
         "publiques de 1959, les trois fonctions d’allocation, de "
         "stabilisation ou de régulation, et de redistribution.",
    'p': "La date et le triptyque fournissent la référence canonique de "
         "l’État interventionniste d’après 1945 : l’intervention est "
         "organisée en fonctions distinctes et non laissée à "
         "l’improvisation."},
   {'f': "Le cours relève que le carré magique est dit magique parce que "
         "l’atteinte simultanée des quatre objectifs est impossible.",
    'p': "Le fait montre que l’intervention est structurellement un "
         "arbitrage : il n’existe pas de politique qui satisfasse tous les "
         "objectifs en même temps."},
   {'f': "Pierre Rosanvallon publie La crise de l’État providence en 1981, "
         "identifiant un problème de financement, une crise d’efficacité et "
         "une crise de légitimité.",
    'p': "La référence datée montre que la remise en cause est contemporaine "
         "du tournant libéral des années quatre-vingt, ce qui éclaire le "
         "contexte du basculement doctrinal."},
   {'f': "Le cours relève qu’en France il existe 483 taxes et impôts et 474 "
         "niches fiscales.",
    'p': "Les deux chiffres mesurent la complexité de l’État fiscal "
         "contemporain : ils donnent un contenu concret à la crise "
         "d’efficacité que Rosanvallon identifie."}],
  [{'q': "Sujet sur les fonctions de l’État",
    'f': "L’État interventionniste se décrit mieux par ses fonctions que par "
         "son volume. Le cours retient les trois fonctions de l’État "
         "providence selon Musgrave, dans la théorie des finances publiques "
         "de 1959 : fonction d’allocation des ressources, fonction de "
         "stabilisation ou de régulation, fonction de redistribution. Il y "
         "ajoute la distinction entre politiques conjoncturelles de court "
         "terme et politiques structurelles de long terme.",
    'r': "On montre que chaque fonction répond à une défaillance distincte, "
         "ce qui permet de discuter l’intervention mesure par mesure plutôt "
         "qu’en bloc.",
    'ex': "Le carré magique de Kaldor, qui rappelle que les quatre objectifs "
          "ne peuvent pas être atteints simultanément."},
   {'q': "Sujet sur la crise de l’État providence",
    'f': "La remise en cause de l’État providence n’est pas seulement "
         "budgétaire. Pierre Rosanvallon, dans La crise de l’État providence "
         "publiée en 1981, identifie trois crises : un problème de "
         "financement, une crise d’efficacité et une crise de légitimité. Le "
         "cours en précise le ressort : avec une fiscalité élevée, les "
         "travailleurs se disent qu’il ne sert à rien de travailler si une "
         "grande partie de leur salaire va aux impôts.",
    'r': "On montre que les trois crises se renforcent, le doute sur "
         "l’efficacité alimentant le refus de financer et donc la perte de "
         "légitimité.",
    'ex': "Les reproches faits à la courbe de Laffer, qui selon le cours ne "
          "relève pas de faits empiriques selon certains économistes."},
   {'q': "Sujet sur l’intervention publique et la croissance",
    'f': "L’intervention de l’État n’est pas seulement conjoncturelle, elle "
         "peut être un facteur de croissance de long terme. Le cours le "
         "montre avec Robert Barro en 1990 : le capital public, c’est-à-dire "
         "l’ensemble des dépenses publiques productives qui améliorent la "
         "productivité du secteur privé, entre explicitement dans la fonction "
         "de production. Mais l’intervention doit être mesurée, puisqu’un "
         "excès produit un effet d’éviction du capital privé.",
    'r': "On distingue l’intervention conjoncturelle, contestée par les "
         "monétaristes, de l’intervention structurelle, admise jusque dans "
         "les théories de la croissance endogène.",
    'ex': "Les exemples de capital public du cours : infrastructures, "
          "éducation, financement de la recherche et du développement."},
   {'q': "Sujet sur État et marché",
    'f': "Le débat sur l’État interventionniste porte sur la capacité du "
         "marché à s’ajuster seul. Le cours donne la position keynésienne "
         "renouvelée : même dans un cadre de rationalité et de "
         "microfondements néoclassiques, les marchés ne s’auto-ajustent pas "
         "parfaitement, et en raison des rigidités, des asymétries "
         "d’information et de la concurrence imparfaite, l’économie peut "
         "rester durablement en situation de sous-emploi, ce qui justifie un "
         "rôle stabilisateur de l’État.",
    'r': "On montre que l’argument accepte le cadre adverse pour en tirer "
         "une conclusion inverse, ce qui le rend plus difficile à écarter "
         "qu’une opposition de principe.",
    'ex': "La position de la nouvelle économie keynésienne telle que le cours "
          "la résume, face à l’État inutile voire nuisible de la nouvelle "
          "économie classique."}],
  voisins=['n15-etat-minimal', 'n15-fonctions-musgrave',
           'n15-politique-budgetaire', 'n15-dette-publique'])


d('n15-fonctions-musgrave', 15,
  "Fonctions d’allocation, de redistribution et de stabilisation",
  "Les trois rôles que Musgrave assigne à l’État providence",
  "Le cours énonce les trois fonctions de l’État providence selon Musgrave, "
  "dans la théorie des finances publiques de 1959 : la fonction d’allocation "
  "des ressources, la fonction de stabilisation ou de régulation, et la "
  "fonction de redistribution. Ce triptyque sert dans le cours de grille "
  "générale pour classer les interventions publiques selon le problème "
  "qu’elles traitent.",
  "Le cours introduit les trois fonctions juste après avoir posé la "
  "difficulté du carré magique de Kaldor, et cet ordre est signifiant : "
  "l’État poursuit plusieurs objectifs qu’il ne peut pas atteindre ensemble, "
  "et le triptyque de Musgrave organise ses moyens plutôt que ses buts. La "
  "première fonction est l’allocation des ressources. Elle répond aux "
  "situations où le marché ne conduit pas à un niveau de production "
  "socialement optimal : le cours en fournit les cas dans le chapitre sur les "
  "défaillances, avec les externalités, où le prix de marché ne reflète pas "
  "le coût ou le bénéfice réel pour la société, de sorte qu’une externalité "
  "négative conduit à une surproduction et une externalité positive à une "
  "sous-production. Il y rattache l’intervention justifiée par Pigou, taxes, "
  "subventions ou réglementation, pour corriger les écarts entre coûts privés "
  "et coûts sociaux, et du côté de la croissance le capital public de Barro, "
  "dépenses publiques productives qui améliorent la productivité du secteur "
  "privé. La deuxième fonction est la stabilisation ou la régulation. Le "
  "cours en donne les instruments : les politiques conjoncturelles utilisent "
  "le budget des administrations publiques ou la création de monnaie pour "
  "soutenir ou freiner la demande dans l’économie, politiques de relance dans "
  "le premier cas et politiques de rigueur dans le second. C’est la fonction "
  "que l’analyse keynésienne fonde, l’emploi dépendant de la demande globale "
  "et non du seul marché du travail, et c’est aussi celle que la critique "
  "monétariste conteste le plus directement. La troisième fonction est la "
  "redistribution. Le cours en détaille le mécanisme comptable : on ajuste "
  "les revenus primaires avec les prestations sociales, allocations "
  "familiales, aides au logement, chômage et retraites, et les prélèvements "
  "obligatoires, impôts directs comme l’impôt sur le revenu et cotisations "
  "sociales, pour obtenir le revenu réellement disponible. Il en précise les "
  "instruments et les tensions : l’impôt progressif, dont le taux augmente "
  "avec le revenu, est plus équitable car il réduit les inégalités, tandis "
  "que la taxe sur la valeur ajoutée pèse davantage sur les revenus les plus "
  "faibles et n’est donc pas un impôt juste. Le cours relie enfin les trois "
  "fonctions à la crise de l’État providence que Rosanvallon analyse, "
  "puisque c’est leur extension conjointe qui pose le problème de "
  "financement, d’efficacité et de légitimité.",
  [("Le repérage de la défaillance d’allocation",
    "Le prix de marché ne reflète pas le coût ou le bénéfice réel pour la "
    "société : une externalité négative conduit à une surproduction, une "
    "externalité positive à une sous-production."),
   ("La correction par l’instrument fiscal ou réglementaire",
    "Avec Pigou, taxes, subventions ou réglementation corrigent les écarts "
    "entre coûts privés et coûts sociaux : l’État rétablit le signal-prix "
    "sans se substituer au marché."),
   ("L’action conjoncturelle sur la demande",
    "Les politiques conjoncturelles utilisent le budget des administrations "
    "publiques ou la création de monnaie pour soutenir ou freiner la demande : "
    "relance d’un côté, rigueur de l’autre."),
   ("Le passage des revenus primaires au revenu disponible",
    "On ajoute les prestations sociales et on retire les prélèvements "
    "obligatoires : la redistribution s’opère par cette double opération, "
    "avant toute dépense publique en nature."),
   ("Le choix du barème",
    "Un impôt progressif voit son taux augmenter avec le revenu, ce qui "
    "réduit les inégalités ; un impôt proportionnel sur la consommation pèse "
    "au contraire davantage sur les bas revenus."),
   ("La pondération par la composition du ménage",
    "Le quotient familial divise le revenu imposable par le nombre de parts, "
    "ce qui rend l’impôt à la fois progressif et équitable en tenant compte "
    "de la taille du foyer."),
   ("L’articulation et ses tensions",
    "Les trois fonctions s’exercent sur le même budget : leur extension "
    "conjointe produit le problème de financement que Rosanvallon place au "
    "cœur de la crise de l’État providence.")],
  [{'a': "Le triptyque fournit une grille de classement qui évite de "
         "discuter l’intervention publique en bloc.",
    'cond': "Il suppose que l’on rattache chaque mesure à sa fonction "
            "dominante, allocation, stabilisation ou redistribution.",
    'lim': "Les fonctions se recouvrent en pratique : une allocation "
           "chômage redistribue et stabilise simultanément, comme le montre "
           "sa hausse automatique en période de ralentissement."},
   {'a': "Il relie chaque fonction à une défaillance précise, ce qui donne à "
         "l’intervention un fondement économique et non doctrinal.",
    'cond': "Le fondement suppose que la défaillance soit caractérisée, "
            "externalité pour l’allocation, insuffisance de demande pour la "
            "stabilisation.",
    'lim': "Le cours ne fournit pas de critère équivalent pour la "
           "redistribution, qui relève d’un jugement sur la justice fiscale "
           "autant que d’une défaillance de marché."},
   {'a': "Il permet de distinguer les critiques, puisque la contestation "
         "monétariste porte surtout sur la fonction de stabilisation.",
    'cond': "La distinction suppose que les arguments contre l’intervention "
            "conjoncturelle ne s’appliquent pas mécaniquement aux deux autres "
            "fonctions.",
    'lim': "Le cours montre que la critique s’étend par le financement : "
           "l’extension de toutes les fonctions nourrit la résistance "
           "fiscale que la crise de l’État providence met en évidence."},
   {'a': "Il articule les instruments, puisque la même fiscalité sert à "
         "redistribuer, à allouer et à stabiliser.",
    'cond': "L’articulation suppose que l’État puisse moduler les taux par "
            "assiette, ce que le cours illustre avec les taux différenciés de "
            "la taxe sur la valeur ajoutée.",
    'lim': "La polyvalence crée des conflits : un taux réduit sur un produit "
           "oriente la consommation mais réduit les recettes disponibles pour "
           "la redistribution."},
   {'a': "Il inscrit l’intervention dans le cadre des objectifs multiples du "
         "carré magique, ce qui impose le raisonnement en arbitrages.",
    'cond': "L’inscription suppose que les quatre objectifs soient "
            "réellement concurrents, ce que le cours affirme.",
    'lim': "Le cours ne hiérarchise ni les objectifs ni les fonctions : la "
           "grille organise la discussion sans la trancher."}],
  [{'t': "La redistribution décourage le travail : avec une fiscalité "
         "élevée, les travailleurs estiment qu’il ne sert à rien de "
         "travailler.",
    'qui': "L’argument que le cours rattache à la crise de l’État providence "
           "et à la courbe de Laffer.",
    'rep': "Le cours rapporte les critiques de cette courbe : elle ne relève "
           "pas de faits empiriques selon certains économistes, et des "
           "études montrent qu’à moyen terme une hausse du taux d’imposition "
           "n’a pas d’effet."},
   {'t': "La fonction de stabilisation est inopérante : les agents "
         "anticipent et neutralisent l’effet des politiques conjoncturelles.",
    'qui': "Milton Friedman et la nouvelle économie classique, dont le cours "
           "expose la critique.",
    'rep': "Le cours maintient l’argument keynésien renouvelé : rigidités, "
           "asymétries d’information et concurrence imparfaite peuvent "
           "laisser l’économie durablement en sous-emploi, ce qui justifie un "
           "rôle stabilisateur."},
   {'t': "La fonction d’allocation est inutile : le marché alloue mieux les "
         "ressources que n’importe quelle décision publique.",
    'qui': "La position classique et néoclassique que le cours résume par la "
           "supériorité du marché comme mécanisme de coordination.",
    'rep': "Le cours objecte par les externalités : avec une externalité "
           "négative le coût marginal privé est inférieur au coût marginal "
           "social, ce qui conduit à une surproduction et à une allocation "
           "sous-optimale."},
   {'t': "Les dépenses publiques évincent l’investissement privé plutôt que "
         "d’améliorer l’allocation.",
    'qui': "Robert Barro, dans la condition d’efficacité que le cours "
           "rapporte.",
    'rep': "Le cours restitue l’argument complet : l’effet d’éviction "
           "n’apparaît que si les dépenses sont excessives, un niveau trop "
           "faible produisant au contraire un sous-investissement collectif."}],
  [{'n': "Richard Musgrave",
    'i': "L’État providence remplit trois fonctions distinctes : allocation, "
         "stabilisation, redistribution.",
    'p': "Le cours situe l’analyse dans la théorie des finances publiques de "
         "1959 et la relie à la distinction des politiques publiques, "
         "conjoncturelles à court terme avec la politique monétaire, "
         "budgétaire et fiscale, et structurelles à long terme avec la "
         "concurrence et la politique industrielle."},
   {'n': "Arthur Pigou",
    'i': "L’intervention publique est légitime quand le marché est "
         "défaillant, notamment en présence d’externalités.",
    'p': "Le cours précise ses instruments : taxes, subventions ou "
         "réglementation pour corriger les écarts entre coûts privés et "
         "coûts sociaux, ce qui donne un contenu concret à la fonction "
         "d’allocation."},
   {'n': "Robert Barro",
    'i': "Le capital public améliore la productivité du secteur privé et "
         "soutient la croissance.",
    'p': "Le cours définit ce capital public comme l’ensemble des dépenses "
         "publiques productives, infrastructures, éducation, recherche et "
         "développement, et précise la condition d’efficacité : il existe un "
         "niveau optimal, au-delà duquel apparaît un effet d’éviction du "
         "capital privé."},
   {'n': "John Maynard Keynes",
    'i': "L’État doit stabiliser l’économie, car l’emploi dépend de la "
         "demande globale.",
    'p': "Le cours lui rattache les moyens de la fonction de stabilisation : "
         "politique budgétaire, politique de relance, soutien à "
         "l’investissement, et possibilité de créer une demande autonome pour "
         "relancer l’activité."}],
  [{'f': "Le cours attribue à Musgrave, en 1959, les trois fonctions "
         "d’allocation des ressources, de stabilisation ou de régulation, et "
         "de redistribution.",
    'p': "Le triptyque daté fournit la grille de référence de l’État "
         "providence d’après 1945 : chaque intervention peut être rattachée à "
         "un problème distinct."},
   {'f': "Le cours distingue deux types de politiques : conjoncturelles à "
         "court terme et structurelles à long terme, la politique fiscale "
         "figurant dans les deux.",
    'p': "Le fait montre que les fonctions se distinguent par leur horizon "
         "et non par leurs instruments, un même levier pouvant servir "
         "plusieurs fins."},
   {'f': "Le cours relève que la taxe sur la valeur ajoutée pèse plus sur "
         "les revenus les plus faibles, et qu’elle n’est donc pas un impôt "
         "juste.",
    'p': "Le fait montre que la fonction de redistribution dépend du choix "
         "des assiettes : un même niveau de recettes peut réduire ou "
         "aggraver les inégalités."},
   {'f': "L’État réalise deux cents milliards d’euros de recettes grâce à la "
         "taxe sur la valeur ajoutée.",
    'p': "Le chiffre montre le poids de cet impôt dans le financement des "
         "trois fonctions, et donc l’ampleur de l’arbitrage entre rendement "
         "fiscal et justice fiscale."}],
  [{'q': "Sujet sur les fonctions économiques de l’État",
    'f': "Le cours fournit la grille canonique avec Musgrave, dans la "
         "théorie des finances publiques de 1959 : fonction d’allocation des "
         "ressources, fonction de stabilisation ou de régulation, fonction de "
         "redistribution. L’intérêt de ce triptyque est qu’il rattache chaque "
         "intervention à un problème distinct, ce qui interdit de discuter "
         "l’État en bloc et oblige à examiner chaque fonction selon le "
         "critère qui lui convient.",
    'r': "On montre que les critiques adressées à l’État ne portent pas "
         "toutes sur la même fonction, ce qui permet de distinguer la "
         "contestation monétariste de la contestation libérale classique.",
    'ex': "Les politiques conjoncturelles du cours, qui utilisent le budget "
          "ou la création de monnaie pour soutenir ou freiner la demande."},
   {'q': "Sujet sur la justice fiscale",
    'f': "La fonction de redistribution se joue dans le choix des barèmes "
         "autant que dans le niveau des prélèvements. Le cours oppose l’impôt "
         "progressif, dont le taux augmente avec le revenu et qui est plus "
         "équitable car il réduit les inégalités, et la taxe sur la valeur "
         "ajoutée, qui pèse plus sur les revenus les plus faibles et n’est "
         "donc pas un impôt juste.",
    'r': "On montre que la progressivité n’est pas une propriété du niveau "
         "des recettes mais de leur assiette, ce qui déplace le débat du "
         "montant vers la structure.",
    'ex': "Le quotient familial, que le cours présente comme rendant l’impôt "
          "progressif et équitable en tenant compte de la taille du ménage."},
   {'q': "Sujet sur les défaillances de marché et l’intervention publique",
    'f': "La fonction d’allocation se justifie par une défaillance "
         "caractérisée. Le cours l’établit avec les externalités : le prix de "
         "marché ne reflète pas le coût ou le bénéfice réel pour la société, "
         "de sorte qu’une externalité négative conduit à une surproduction et "
         "une externalité positive à une sous-production. Pigou en tire la "
         "légitimité de taxes, subventions ou réglementations.",
    'r': "On montre que l’intervention ne remplace pas le marché mais "
         "corrige son signal, ce qui en limite l’étendue à l’écart entre "
         "coût privé et coût social.",
    'ex': "Le cas des externalités négatives du cours, où le coût marginal "
          "privé est inférieur au coût marginal social."},
   {'q': "Sujet sur les limites de l’intervention publique",
    'f': "Les trois fonctions s’exercent sur un même budget, et c’est leur "
         "extension conjointe qui fait difficulté. Le cours mobilise "
         "Rosanvallon et La crise de l’État providence de 1981 : problème de "
         "financement, crise d’efficacité, crise de légitimité. S’y ajoute la "
         "contrainte du carré magique de Kaldor, les quatre objectifs ne "
         "pouvant être atteints simultanément.",
    'r': "On montre que la limite n’est pas celle d’une fonction "
         "particulière mais de leur cumul, ce qui explique que la crise ait "
         "porté sur l’État providence dans son ensemble.",
    'ex': "Les 483 taxes et impôts et 474 niches fiscales que le cours "
          "recense en France."}],
  voisins=['n15-etat-interventionniste', 'n15-politique-budgetaire',
           'n15-etat-minimal', 'n15-stabilisateurs-automatiques'])


d('n15-politique-budgetaire', 15, "Politique budgétaire",
  "Agir sur l’activité par les dépenses et les recettes publiques",
  "La politique budgétaire utilise le budget des administrations publiques, "
  "dépenses et recettes, pour soutenir ou freiner la demande dans l’économie. "
  "Le cours la classe parmi les politiques conjoncturelles, aux côtés de la "
  "politique monétaire et de la politique fiscale, et distingue selon son "
  "sens les politiques de relance et les politiques de rigueur, leur "
  "articulation avec la politique monétaire formant le policy mix.",
  "Le cours définit la politique budgétaire par son instrument plutôt que par "
  "son objectif, et cette entrée en éclaire toute la mécanique. L’instrument "
  "est le budget des administrations publiques : les politiques "
  "conjoncturelles utilisent ce budget, ou la création de monnaie dans le cas "
  "monétaire, pour soutenir ou freiner la demande dans l’économie. Dans le "
  "premier cas il s’agit de politiques de relance, dans le second de "
  "politiques de rigueur. Le cours distingue ensuite deux degrés d’action. "
  "Le premier est automatique : lorsque la croissance économique est "
  "ralentie, les dépenses des administrations publiques augmentent, puisqu’il "
  "faut verser plus d’allocations chômage parce qu’il y a plus de chômeurs et "
  "plus de prestations sociales parce qu’il y a plus de pauvres, tandis que "
  "les recettes de l’État sont plus faibles, la consommation étant ralentie "
  "la taxe sur la valeur ajoutée rentrant moins dans les caisses et les "
  "cotisations sur les revenus du travail diminuant aussi. Le second est "
  "volontaire : l’État peut être plus volontariste en mettant en œuvre des "
  "mesures spécifiques en termes de dépenses comme de recettes afin "
  "d’influer sur la conjoncture, et le cours renvoie aux mesures du plan "
  "Biden et à leur financement. Le mécanisme attendu est explicite : hausse "
  "des dépenses publiques, donc hausse de la demande, donc hausse de "
  "l’investissement des entreprises, donc hausse du produit intérieur brut. "
  "La contrepartie est également posée : quand les dépenses publiques sont "
  "supérieures aux recettes publiques, l’État crée un déficit public qui doit "
  "être financé par de la dette, c’est-à-dire par émission d’obligations par "
  "l’État. Le cours relie enfin la politique budgétaire à trois débats qu’il "
  "développe ailleurs. Le premier est celui de son efficacité, par le "
  "multiplicateur, dont il chiffre la valeur à cinq en économie fermée pour "
  "une propension à consommer de zéro virgule huit, mais seulement deux et "
  "demi en économie ouverte. Le deuxième est celui de l’éviction, puisque "
  "selon Barro des dépenses publiques excessives produisent un effet "
  "d’éviction du capital privé. Le troisième est celui de la soutenabilité, "
  "puisque la charge de la dette pèse sur le budget de l’État et augmente "
  "fortement avec la hausse des taux d’intérêt.",
  [("La décision budgétaire",
    "L’État modifie ses dépenses ou ses recettes : le cours parle de mesures "
    "spécifiques en termes de dépenses comme de recettes afin d’influer sur "
    "la conjoncture."),
   ("La transmission à la demande",
    "Le mécanisme énoncé par le cours est direct : hausse des dépenses "
    "publiques, puis hausse de la demande, l’État ajoutant une dépense qui ne "
    "dépend pas du revenu courant des agents."),
   ("L’effet multiplicateur",
    "La dépense initiale engendre des revenus qui sont en partie "
    "reconsommés : la variation du revenu égale celle de la dépense "
    "multipliée par un sur un moins la propension à consommer."),
   ("La réaction de l’investissement",
    "Le cours poursuit la chaîne : hausse de la demande, donc hausse de "
    "l’investissement des entreprises, donc hausse du produit intérieur brut, "
    "ce qui mobilise le principe de l’accélérateur."),
   ("Le financement par le déficit",
    "Quand les dépenses publiques excèdent les recettes, l’État crée un "
    "déficit public qui doit être financé par de la dette, c’est-à-dire par "
    "émission d’obligations."),
   ("La contrainte de la charge de la dette",
    "Les intérêts constituent la charge de la dette, qui pèse sur le budget "
    "de l’État : le cours montre qu’elle augmente fortement avec la hausse "
    "des taux d’intérêt.")],
  [{'a': "La politique budgétaire agit directement sur la demande, sans "
         "dépendre de la décision de prêter des banques ni d’emprunter des "
         "agents.",
    'cond': "L’argument suppose que l’économie soit en deçà de ses "
            "capacités, faute de quoi la dépense supplémentaire se transmet "
            "aux prix.",
    'lim': "Le cours montre qu’avec un output gap positif les entreprises "
           "peuvent décider d’augmenter les prix au lieu d’augmenter les "
           "capacités de production."},
   {'a': "Elle reste opérante lorsque la politique monétaire est désarmée par le "
         "plancher des taux nominaux et la prudence des banques.",
    'cond': "L’argument suppose une situation de trappe à liquidité, où les "
            "agents conservent leurs liquidités et où baisser encore les taux "
            "ne suffit plus.",
    'lim': "Son efficacité dépend alors du multiplicateur, que le cours "
           "chiffre à cinq en économie fermée mais à deux et demi seulement "
           "en économie ouverte."},
   {'a': "Elle peut servir la croissance de long terme et non seulement la "
         "conjoncture, par le capital public.",
    'cond': "Le cours conditionne cet effet à la qualité des dépenses et à "
            "leur orientation vers des investissements productifs, "
            "infrastructures, éducation, recherche.",
    'lim': "Barro fixe la limite : si les dépenses sont excessives, il y a "
           "effet d’éviction du capital privé, et il existe un niveau optimal "
           "de capital public."},
   {'a': "Elle fonctionne en partie automatiquement, sans décision nouvelle, "
         "ce qui lui donne une réactivité que la décision n’a pas.",
    'cond': "L’automatisme suppose des prestations liées à la conjoncture, "
            "allocations chômage et prestations sociales, et des recettes "
            "assises sur l’activité.",
    'lim': "Cet automatisme creuse mécaniquement le déficit en bas de "
           "cycle : le cours note que les recettes baissent au moment même où "
           "les dépenses augmentent."},
   {'a': "Elle articule une action de court terme et une contrainte de long "
         "terme, ce qui oblige à juger une relance sur sa soutenabilité.",
    'cond': "Le jugement suppose de comparer le coût du financement à la "
            "croissance attendue, condition que le cours formule pour la "
            "soutenabilité de la dette.",
    'lim': "Le cours décrit une impasse possible : il faudrait augmenter les "
           "impôts pour compenser la charge de la dette, mais les gens n’en "
           "veulent pas."}],
  [{'t': "Les politiques de relance budgétaire sont inflationnistes et "
         "l’intervention discrétionnaire de l’État crée de l’instabilité.",
    'qui': "Les monétaristes autour de Milton Friedman, dont le cours expose "
           "la critique frontale du keynésianisme.",
    'rep': "Le cours maintient la distinction des situations : l’argument "
           "vaut pour une économie proche de ses capacités, alors que "
           "l’analyse keynésienne porte sur une économie bloquée par "
           "l’insuffisance de dépense."},
   {'t': "Les dépenses publiques évincent l’investissement privé plutôt que "
         "de le stimuler, dès qu’elles dépassent le niveau optimal.",
    'qui': "Robert Barro, dans la condition d’efficacité du modèle de 1990 "
           "que le cours rapporte.",
    'rep': "Le cours restitue l’argument conditionnel : l’effet d’éviction "
           "n’apparaît que si les dépenses sont excessives, un niveau trop "
           "faible produisant un sous-investissement collectif."},
   {'t': "L’efficacité de la relance est faible en économie ouverte, une "
         "part de la dépense fuyant vers les importations.",
    'qui': "L’argument que le cours chiffre en comparant les deux valeurs du "
           "multiplicateur.",
    'rep': "Le cours accorde le fait en le mesurant : le multiplicateur "
           "passe de cinq en économie fermée à deux et demi en économie "
           "ouverte, ce qui réduit l’effet sans l’annuler."},
   {'t': "La contrainte n’est pas budgétaire : un État souverain "
         "monétairement peut financer ses dépenses, le seul risque étant "
         "l’inflation.",
    'qui': "Stephanie Kelton, représentante de la théorie monétaire moderne "
           "que le cours présente.",
    'rep': "Le cours objecte par les incitations : l’aléa moral public fait "
           "que l’État cesse de maîtriser son déficit s’il sait pouvoir "
           "compter sur la banque centrale, d’où un risque de dérive "
           "permanente."}],
  [{'n': "Richard Musgrave",
    'i': "La politique budgétaire relève de la fonction de stabilisation de "
         "l’État providence.",
    'p': "Le cours situe cette analyse dans la théorie des finances "
         "publiques de 1959 et classe la politique budgétaire parmi les "
         "politiques conjoncturelles de court terme, aux côtés de la "
         "politique monétaire et de la politique fiscale."},
   {'n': "John Maynard Keynes",
    'i': "L’État peut créer une demande autonome pour relancer l’activité.",
    'p': "Le cours détaille ses moyens d’action : politique budgétaire avec "
         "dépenses publiques et déficit, politique de relance, soutien à "
         "l’investissement et stabilisation de l’économie, parce que l’emploi "
         "dépend de la demande globale et non du seul marché du travail."},
   {'n': "Robert Barro",
    'i': "Les dépenses publiques productives entrent dans la fonction de "
         "production et soutiennent la croissance.",
    'p': "Le cours définit le capital public comme les dépenses publiques "
         "qui améliorent la productivité du secteur privé, infrastructures, "
         "éducation, recherche et développement, et fixe la condition : il "
         "existe un niveau optimal au-delà duquel le capital privé est "
         "évincé."},
   {'n': "Paul Samuelson",
    'i': "Le multiplicateur et l’accélérateur se combinent dans un même "
         "mouvement cumulatif.",
    'p': "Le cours date de 1939 son oscillateur, résumé par l’enchaînement "
         "variation de l’investissement, variation du revenu, variation de la "
         "demande : c’est ce bouclage qui donne à une impulsion budgétaire "
         "son effet amplifié sur l’activité."}],
  [{'f': "Le cours énonce le mécanisme : hausse des dépenses publiques, "
         "hausse de la demande, hausse de l’investissement des entreprises, "
         "hausse du produit intérieur brut.",
    'p': "La chaîne montre que l’effet attendu passe par l’investissement "
         "privé et non seulement par la dépense publique elle-même, ce qui "
         "mobilise multiplicateur et accélérateur."},
   {'f': "Le cours donne en exemple le plan Biden, destiné à construire et "
         "rénover des infrastructures, routes, autoroutes et ponts.",
    'p': "L’exemple montre une relance orientée vers le capital public : "
         "elle soutient la demande immédiate tout en améliorant la "
         "productivité future du secteur privé."},
   {'f': "Quand les dépenses publiques sont supérieures aux recettes, l’État "
         "crée un déficit public financé par de la dette, par émission "
         "d’obligations.",
    'p': "Le fait relie la politique budgétaire au marché financier : la "
         "relance n’est possible que si l’État trouve des créanciers, ce qui "
         "la rend dépendante des taux d’intérêt."},
   {'f': "Le multiplicateur vaut cinq en économie fermée pour une propension "
         "à consommer de zéro virgule huit, mais deux et demi en économie "
         "ouverte.",
    'p': "L’écart chiffré montre que l’ouverture divise par deux l’effet "
           "attendu d’une relance : une part de la dépense fuit vers les "
           "importations."}],
  [{'q': "Sujet sur l’efficacité de la politique budgétaire",
    'f': "L’effet d’une relance budgétaire dépend de deux grandeurs que le "
         "cours chiffre. Le mécanisme est d’abord favorable : hausse des "
         "dépenses publiques, hausse de la demande, hausse de "
         "l’investissement des entreprises, hausse du produit intérieur brut. "
         "Mais le multiplicateur vaut cinq en économie fermée pour une "
         "propension à consommer de zéro virgule huit, et seulement deux et "
         "demi en économie ouverte.",
    'r': "On montre que l’efficacité dépend de l’ouverture de l’économie et "
         "du degré d’utilisation des capacités, ce qui ramène le débat "
         "doctrinal à des conditions observables.",
    'ex': "Le plan Biden de construction et de rénovation des "
          "infrastructures, que le cours donne comme exemple de relance "
          "volontariste."},
   {'q': "Sujet sur le financement de l’action publique",
    'f': "La politique budgétaire est indissociable de son financement. Le "
         "cours l’énonce directement : quand les dépenses publiques sont "
         "supérieures aux recettes publiques, l’État crée un déficit public "
         "qui doit être financé par de la dette, c’est-à-dire par émission "
         "d’obligations par l’État. Les intérêts constituent alors la charge "
         "de la dette, qui pèse sur le budget et augmente fortement avec la "
         "hausse des taux.",
    'r': "On montre que l’instrument budgétaire s’auto-contraint : chaque "
           "relance alourdit la charge future, ce qui réduit la marge des "
           "relances suivantes.",
    'ex': "Les chiffres de la charge de la dette française cités par le "
          "cours : trente-neuf milliards d’euros en 2019, cinquante-huit en "
          "2024."},
   {'q': "Sujet sur politique budgétaire et politique monétaire",
    'f': "Les deux instruments conjoncturels se complètent ou se "
         "contrarient. Le cours les range tous deux parmi les politiques "
         "conjoncturelles et nomme policy mix leur articulation. La politique "
         "budgétaire conserve un avantage décisif en situation de trappe à "
         "liquidité : lorsque baisser encore les taux ne suffit plus, la "
         "dépense publique agit directement sur la demande sans passer par la "
         "décision de prêter des banques.",
    'r': "On montre que la supériorité relative d’un instrument dépend de "
         "l’état du système financier, ce qui justifie leur combinaison "
         "plutôt que leur opposition.",
    'ex': "La trappe à liquidité décrite par le cours, où les banques "
          "restent prudentes malgré des taux très bas."},
   {'q': "Sujet sur les limites de la relance budgétaire",
    'f': "Les objections à la relance ne sont pas toutes de même nature. Le "
         "cours en retient trois : la critique monétariste, selon laquelle "
         "les politiques de relance budgétaire sont inflationnistes et "
         "l’intervention discrétionnaire crée de l’instabilité ; l’effet "
         "d’éviction du capital privé que Barro attache à des dépenses "
         "excessives ; et la contrainte de la charge de la dette, qui "
         "augmente fortement avec les taux d’intérêt.",
    'r': "On distingue l’objection d’inefficacité, l’objection de "
         "substitution et l’objection de soutenabilité, pour montrer qu’elles "
         "n’appellent pas les mêmes réponses.",
    'ex': "L’impasse décrite par le cours : pour compenser la charge de la "
          "dette il faudrait augmenter les impôts, mais les gens n’en "
          "veulent pas."}],
  voisins=['n15-politique-relance', 'n15-multiplicateur-budgetaire',
           'n15-deficit-public', 'n15-policy-mix'])
