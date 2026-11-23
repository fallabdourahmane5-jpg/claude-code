# -*- coding: utf-8 -*-
"""Chapitre 10 — questions nouvelles, sous-parties c10-10 à c10-13."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c10-10
f(id='q10-n40', sp='c10-10', niv='connaitre', type='qcm', b=1639,
  q="Quels éléments caractérisent la démarche de Michel Crozier ?",
  opts=["Il raisonne exclusivement à partir d’idéaux-types construits a priori",
        "Il fait connaître en France les travaux de chercheurs américains "
        "comme Herbert Simon, Robert Merton et James March, crée le Centre de "
        "sociologie des organisations en 1961 et fonde son analyse sur des "
        "enquêtes de terrain",
        "Il réalise des expériences en laboratoire sur de petits groupes",
        "Il analyse les organisations à partir de données statistiques "
        "nationales"],
  ans=1,
  why=["L’idéal-type est l’outil de Weber ; Crozier confronte précisément "
       "cet idéal-type au terrain.",
       "Les expériences en laboratoire renvoient à Asch ou à la Test Room de "
       "Mayo.",
       "Crozier n’est pas un statisticien : il observe des employés, leurs "
       "relations, leurs conflits et leurs stratégies réelles."],
  exp="L’originalité de Crozier est sa méthode : il ne se contente pas de "
      "théoriser l’entreprise, il réalise des enquêtes de terrain permettant "
      "d’observer concrètement les comportements des acteurs et les relations "
      "de pouvoir. Ses ouvrages principaux sont Le Phénomène bureaucratique "
      "(1963) et L’Acteur et le système (1977), écrit avec Erhard Friedberg.",
  diss="Le lien avec Herbert Simon n’est pas anecdotique : la rationalité "
       "limitée est au cœur de l’analyse stratégique."),

f(id='q10-n41', sp='c10-10', niv='comprendre', type='assoc', b=1701,
  q="Associez chaque élément au monde de l’organisation dont il relève chez "
    "Crozier.",
  ans=[["Les règles, les fonctions, la hiérarchie, les procédures et la rationalité affichée", "Le monde formel"],
       ["L’organigramme, établi par la direction : ce qui devrait officiellement se passer", "Le monde formel"],
       ["Les relations réelles entre les individus, les affects et les rapports de pouvoir informels", "Le monde informel"],
       ["Le sociogramme, établi par le sociologue : ce qui se passe réellement", "Le monde informel"]],
  exp="La distinction est décisive : l’organigramme ne montre pas "
      "nécessairement qui influence réellement qui dans l’entreprise. Le "
      "fonctionnement d’une organisation ne correspond jamais parfaitement à "
      "son fonctionnement officiel, et c’est l’écart entre les deux que "
      "l’enquête de terrain fait apparaître.",
  diss="Outil d’analyse réutilisable : toute organisation peut être lue en "
       "superposant son organigramme et son sociogramme."),

f(id='q10-n42', sp='c10-10', niv='connaitre', type='qcm', b=1738,
  q="Quelle entreprise Crozier étudie-t-il sous le nom de « monopole "
    "industriel » dans Le Phénomène bureaucratique (1963) ?",
  opts=["La Western Electric Company",
        "La SEITA, Service d’Exploitation Industrielle des Tabacs et "
        "Allumettes, créée en 1926 et détentrice jusqu’en 1976 du monopole de "
        "la fabrication et de la vente des tabacs et allumettes",
        "General Electric",
        "La Régie Renault"],
  ans=1,
  why=["La Western Electric est l’usine des expériences de Mayo, près de "
       "Chicago.",
       "General Electric est l’exemple de conglomérat du chapitre "
       "d’économie.",
       "Le cours ne mentionne pas d’enquête chez Renault."],
  exp="Crozier observe les ateliers de production de cette entreprise pour "
      "comparer la hiérarchie officielle et les véritables rapports de "
      "pouvoir. L’organisation officielle est simple : des chefs d’atelier "
      "dirigent les ouvrières de production, tandis que les ouvriers "
      "d’entretien dépendent d’un ingénieur technique peu présent. L’enquête "
      "révélera un tout autre équilibre réel."),

f(id='q10-n43', sp='c10-10', niv='appliquer', type='qcm', b=1764,
  q="Quel paradoxe l’enquête de la SEITA met-elle au jour ?",
  opts=["Les ouvrières se plaignent surtout de leurs chefs d’atelier",
        "L’organigramme donne aux chefs d’atelier une autorité importante sur "
        "les ouvrières, alors qu’en réalité celles-ci leur accordent peu "
        "d’importance et se sentent surtout dépendantes des ouvriers "
        "d’entretien",
        "Les ouvriers d’entretien sont les supérieurs hiérarchiques des "
        "ouvrières",
        "L’ingénieur technique dirige directement les ateliers"],
  ans=1,
  why=["C’est l’inverse : elles entretiennent généralement de bonnes "
       "relations avec leurs chefs d’atelier.",
       "Précisément non : les ouvriers d’entretien ne sont pas leurs "
       "supérieurs, et c’est ce qui rend leur pouvoir remarquable.",
       "L’ingénieur technique intervient peu directement dans les ateliers."],
  exp="La hiérarchie réelle ne correspond pas à la hiérarchie formelle. Les "
      "ouvrières accordent relativement peu d’importance aux chefs d’atelier, "
      "avec lesquels elles s’entendent plutôt bien, mais se sentent très "
      "dépendantes des ouvriers d’entretien, seuls capables de réparer les "
      "machines dont dépendent leur production et leurs primes.",
  diss="Enquête fondatrice : elle démontre empiriquement que le pouvoir n’est "
       "pas un attribut de la position hiérarchique."),

# ------------------------------------------------------------- c10-11
f(id='q10-n44', sp='c10-11', niv='connaitre', type='qcm', b=1810,
  q="Comment Crozier définit-il le pouvoir ?",
  opts=["La capacité de donner des ordres en vertu d’une position "
        "hiérarchique",
        "La capacité d’un acteur à influencer d’autres acteurs en utilisant à "
        "son avantage les ressources dont il dispose et qui lui permettent de "
        "maîtriser des zones d’incertitude",
        "La propriété des moyens de production",
        "La légitimité reconnue aux détenteurs d’une fonction"],
  ans=1,
  why=["La position hiérarchique n’est qu’une source de pouvoir parmi "
       "d’autres chez Crozier.",
       "La propriété du capital est la définition marxienne du pouvoir "
       "économique, que Crozier discute.",
       "La légitimité de la fonction est la domination légale-rationnelle de "
       "Weber."],
  exp="Deux conséquences majeures découlent de cette définition. D’abord le "
      "pouvoir n’est pas un attribut : une personne ne possède pas du pouvoir "
      "parce qu’elle détient un titre, le pouvoir existe dans une relation "
      "avec d’autres acteurs. Ensuite il n’est pas réservé au sommet : un "
      "salarié situé plus bas dans l’organisation peut détenir un pouvoir "
      "important s’il contrôle une ressource essentielle pour les autres.",
  diss="Définition à citer : elle contient à la fois le caractère relationnel "
       "du pouvoir et son fondement dans l’incertitude."),

f(id='q10-n45', sp='c10-11', niv='comprendre', type='qcm', b=1872,
  q="Pourquoi la même zone d’incertitude est-elle à la fois un problème pour "
    "l’organisation et une ressource pour un acteur ?",
  opts=["Parce que l’organisation ignore son existence",
        "Parce qu’elle rend les comportements moins prévisibles et le "
        "fonctionnement moins contrôlable — ce que l’organisation cherche à "
        "réduire —, mais qu’elle rend dépendants de lui tous ceux qui ne la "
        "maîtrisent pas",
        "Parce qu’elle n’apparaît que dans les organisations mal gérées",
        "Parce qu’elle disparaît dès qu’une règle nouvelle est édictée"],
  ans=1,
  why=["L’organisation connaît le problème : c’est précisément pourquoi elle "
       "cherche à réduire ces zones.",
       "Toutes les organisations en possèdent, puisque aucune règle ne peut "
       "tout prévoir.",
       "Les nouvelles règles déplacent l’incertitude plutôt qu’elles ne la "
       "suppriment — c’est le cercle vicieux bureaucratique."],
  exp="Pour l’organisation, l’incertitude est une contrainte : les "
      "comportements deviennent moins prévisibles, certaines décisions plus "
      "difficiles, le fonctionnement moins contrôlable. Pour l’acteur, elle "
      "est une ressource : s’il sait quelque chose que les autres ne savent "
      "pas, ou s’il maîtrise une compétence indispensable, les autres "
      "deviennent dépendants de lui, et il peut rendre son propre comportement "
      "moins prévisible tout en limitant leur liberté d’action.",
  diss="Idée forte : le pouvoir naît de ce que la règle ne dit pas."),

f(id='q10-n46', sp='c10-11', niv='connaitre', type='assoc', b=1895,
  q="Associez chaque exemple à la source de pouvoir correspondante chez "
    "Crozier.",
  ans=[["Les ouvriers d’entretien de la SEITA savent réparer les machines", "La maîtrise d’une compétence"],
       ["Un individu situé entre plusieurs groupes peut communiquer avec plusieurs catégories et contrôler leurs relations : le marginal sécant", "La maîtrise des relations dans l’organisation"],
       ["Un acteur choisit ce qu’il transmet, quand et à qui", "La maîtrise de la communication et de l’information"],
       ["Un acteur connaît mieux que les autres les marges que laissent les textes et sait quand les mobiliser", "La maîtrise des règles de l’organisation"]],
  exp="Les quatre sources de pouvoir identifiées par Crozier sont autant de "
      "manières de maîtriser une zone d’incertitude : une compétence rare, "
      "une position relationnelle, le contrôle de l’information et la "
      "connaissance des règles. Le marginal sécant tire son pouvoir de sa "
      "position à l’intersection de plusieurs univers sociaux, car il peut "
      "servir d’intermédiaire entre des groupes qui communiquent "
      "difficilement.",
  diss="Liste très rentable en dissertation : elle montre que le pouvoir se "
       "distribue dans toute l’organisation, y compris chez des acteurs sans "
       "titre."),

f(id='q10-n47', sp='c10-11', niv='comprendre', type='qcm', b=1906,
  q="Qu’est-ce qu’un « marginal sécant » ?",
  opts=["Un salarié exclu des décisions de l’organisation",
        "Un individu situé entre plusieurs univers ou plusieurs groupes, qui "
        "peut communiquer avec plusieurs catégories et contrôler certaines "
        "relations, maîtrisant ainsi une zone d’incertitude relationnelle",
        "Un acteur qui refuse de respecter les règles",
        "Un intermédiaire extérieur à l’organisation, comme un consultant"],
  ans=1,
  why=["Le marginal sécant n’est pas exclu : sa position intermédiaire est "
       "précisément sa ressource.",
       "Il n’y a pas de transgression dans cette notion : il s’agit d’une "
       "position dans le réseau des relations.",
       "Il appartient à l’organisation : c’est sa double appartenance qui "
       "compte."],
  exp="Sa position intermédiaire lui permet de communiquer avec plusieurs "
      "catégories et de contrôler certaines relations : il devient un passage "
      "obligé entre des groupes qui communiquent difficilement entre eux. Il "
      "maîtrise donc une zone d’incertitude relationnelle, l’une des quatre "
      "sources de pouvoir.",
  diss="Exemple de pouvoir parfaitement invisible sur un organigramme : il "
       "n’apparaît que sur un sociogramme."),

f(id='q10-n48', sp='c10-11', niv='raisonner', type='qcm', b=1842,
  q="Comment le cours distingue-t-il l’analyse du pouvoir chez Marx et chez "
    "Crozier ?",
  opts=["Marx et Crozier situent tous deux le pouvoir au sommet de la "
        "structure économique",
        "Pour Marx, le pouvoir économique provient principalement de la "
        "propriété du capital et se situe donc en haut de la structure ; pour "
        "Crozier, il est relationnel et distribué, chaque acteur pouvant "
        "exercer une influence s’il contrôle une ressource stratégique",
        "Marx analyse le pouvoir comme une relation, Crozier comme une "
        "propriété",
        "Crozier nie l’existence de rapports de domination dans l’entreprise"],
  ans=1,
  why=["C’est précisément ce qui les sépare : Crozier montre le pouvoir "
       "diffus.",
       "L’inversion est fausse : c’est Crozier qui pense le pouvoir comme "
       "relation.",
       "Crozier étudie au contraire les rapports de pouvoir : il les montre "
       "simplement plus dispersés."],
  exp="Chez Marx, le pouvoir est principalement situé en haut de la "
      "structure économique, du côté des détenteurs du capital. Chez Crozier, "
      "il est davantage distribué : chaque acteur peut disposer d’une "
      "ressource lui permettant d’exercer une certaine influence. Les deux "
      "analyses ne portent pas sur le même niveau — rapports de production "
      "d’un côté, fonctionnement concret des organisations de l’autre.",
  diss="Comparaison utile pour nuancer : dire que le pouvoir est diffus "
       "n’exclut pas qu’il reste très inégalement réparti."),

# ------------------------------------------------------------- c10-12
f(id='q10-n49', sp='c10-12', niv='comprendre', type='qcm', b=1960,
  q="Que refuse Crozier dans l’analyse stratégique des organisations ?",
  opts=["De considérer que les règles existent réellement",
        "De considérer le salarié comme un agent passif : même dans une "
        "organisation très réglementée, il conserve une certaine liberté et "
        "développe des stratégies",
        "De reconnaître l’existence d’une hiérarchie",
        "D’étudier les organisations publiques"],
  ans=1,
  why=["Crozier ne nie pas les règles : il montre qu’elles ne déterminent pas "
       "totalement les comportements.",
       "La hiérarchie existe bien : elle est l’une des sources de pouvoir, "
       "mais pas la seule.",
       "Son enquête la plus célèbre porte précisément sur une entreprise "
       "publique en situation de monopole."],
  exp="L’analyse stratégique considère l’individu comme un acteur disposant "
      "de marges de manœuvre et capable de développer des stratégies afin de "
      "défendre ses intérêts au sein de l’organisation. Les règles "
      "structurent l’organisation mais ne déterminent jamais totalement les "
      "comportements : il reste toujours des marges, et donc des zones "
      "d’incertitude à conquérir.",
  diss="Opposition explicite à Taylor : l’ouvrier n’est pas un exécutant mais "
       "un acteur stratégique."),

f(id='q10-n50', sp='c10-12', niv='comprendre', type='qcm', b=1976,
  q="En quel sens la rationalité de l’acteur est-elle limitée chez Crozier ?",
  opts=["L’acteur n’est pas rationnel : il agit par habitude",
        "L’acteur est rationnel, mais il ne possède pas toutes les "
        "informations, ne peut pas anticiper toutes les conséquences et agit "
        "dans un environnement contraint : il cherche donc une solution "
        "satisfaisante",
        "L’acteur est parfaitement rationnel dans les limites de "
        "l’organisation",
        "La rationalité de l’acteur dépend uniquement de son niveau de "
        "diplôme"],
  ans=1,
  why=["Crozier maintient l’hypothèse de rationalité : il en limite seulement "
       "la portée.",
       "La rationalité parfaite est exactement ce que la notion de "
       "rationalité limitée écarte.",
       "Le diplôme n’intervient pas dans cette analyse."],
  exp="C’est la reprise de l’hypothèse d’Herbert Simon, dont Crozier a "
      "contribué à faire connaître les travaux en France : l’acteur cherche "
      "une solution satisfaisante dans les limites de ce qu’il sait et de ce "
      "qu’il peut faire, plutôt qu’une solution optimale. Sa stratégie est "
      "réelle, mais tâtonnante et contrainte.",
  diss="Articulation précieuse : la même hypothèse de rationalité limitée "
       "sert à Williamson en économie et à Crozier en sociologie des "
       "organisations."),

f(id='q10-n51', sp='c10-12', niv='raisonner', type='qcm', b=2004,
  q="Que signifie l’expression « relations de coopération conflictuelles » "
    "chez Crozier ?",
  opts=["Que les acteurs coopèrent tant qu’aucun conflit n’apparaît",
        "Que les acteurs doivent coopérer parce qu’ils sont interdépendants, "
        "mais que cette coopération passe par des négociations et des "
        "rapports de pouvoir, chacun défendant des intérêts différents",
        "Que la coopération est impossible dans une organisation "
        "hiérarchique",
        "Que le conflit doit être éliminé pour que la coopération soit "
        "possible"],
  ans=1,
  why=["L’expression désigne une simultanéité, non une succession : on "
       "coopère et l’on s’oppose en même temps.",
       "La coopération est au contraire nécessaire : personne ne peut agir "
       "totalement seul.",
       "Crozier considère que le conflit n’est pas forcément un "
       "dysfonctionnement."],
  exp="L’expression paraît paradoxale et elle est essentielle : dans une "
      "entreprise, les individus sont interdépendants et ont besoin les uns "
      "des autres — les ouvrières de la SEITA dépendent des ouvriers "
      "d’entretien, qui font eux-mêmes partie d’un système collectif de "
      "production. Mais ils défendent des intérêts différents et cherchent à "
      "conserver leur pouvoir. Le conflit apparaît donc parce que les acteurs "
      "ont des intérêts et des ressources différents tout en dépendant les uns "
      "des autres : il reflète les interdépendances plutôt qu’une mauvaise "
      "organisation.",
  diss="Réponse directe à l’une des questions d’introduction du chapitre : "
       "comment expliquer à la fois la coopération et les conflits dans "
       "l’entreprise."),

f(id='q10-n52', sp='c10-12', niv='raisonner', type='qcm', b=2036,
  q="Pourquoi les organisations sont-elles difficiles à réformer, selon "
    "Crozier ?",
  opts=["Parce que les salariés sont par nature hostiles au changement",
        "Parce qu’une modification des règles remet en cause l’équilibre des "
        "pouvoirs et les zones d’incertitude sur lesquels les acteurs ont "
        "construit leurs stratégies : certains risquent de perdre une "
        "compétence stratégique ou une position avantageuse",
        "Parce que les directions manquent d’information sur leur propre "
        "organisation",
        "Parce que le droit du travail interdit les réorganisations"],
  ans=1,
  why=["Ce n’est pas une explication psychologique : la résistance est "
       "stratégique et rationnelle.",
       "Le défaut d’information existe, mais ce n’est pas l’argument retenu "
       "ici.",
       "Aucune interdiction juridique n’est évoquée par le cours."],
  exp="Les groupes d’acteurs développent progressivement des stratégies "
      "adossées à l’équilibre des pouvoirs existant. Réformer, c’est donc "
      "menacer des positions acquises : ceux qui perdraient une compétence "
      "stratégique ou une position avantageuse peuvent résister au changement. "
      "La résistance n’est pas une irrationalité mais la défense cohérente "
      "d’une ressource.",
  diss="Conséquence pratique très citable : une réforme ne se heurte pas à de "
       "l’inertie, elle se heurte à des intérêts."),

f(id='q10-n53', sp='c10-12', niv='raisonner', type='qcm', b=2073,
  q="En quoi Crozier se distingue-t-il des analyses économiques des "
    "asymétries d’information de Williamson et Akerlof ?",
  opts=["Il nie l’existence des asymétries d’information",
        "Là où ces analyses cherchent généralement à réduire l’information "
        "imparfaite, Crozier montre que les acteurs peuvent avoir intérêt à "
        "maintenir certaines asymétries, car une information que les autres "
        "n’ont pas devient une ressource de pouvoir",
        "Il considère que l’information est toujours parfaite dans les "
        "organisations",
        "Il applique leurs conclusions sans les modifier"],
  ans=1,
  why=["Il les met au contraire au centre de son analyse du pouvoir.",
       "L’information imparfaite est le point de départ commun aux trois "
       "auteurs.",
       "Il en inverse précisément la conclusion normative."],
  exp="Williamson et Akerlof montrent que l’information peut être imparfaite "
      "et asymétrique, une partie disposant de plus d’informations qu’une "
      "autre, et l’objectif est alors de réduire ces asymétries. Crozier "
      "montre que les acteurs peuvent stratégiquement les exploiter et les "
      "entretenir, pour préserver une zone d’incertitude et renforcer leur "
      "pouvoir.",
  diss="Renversement de perspective à souligner : ce qui est un problème à "
       "corriger pour l’économiste est une ressource à défendre pour "
       "l’acteur."),

f(id='q10-n54', sp='c10-12', niv='raisonner', type='ordre', b=2089,
  q="Remettez dans l’ordre la logique générale de l’analyse stratégique des "
    "organisations.",
  ans=["L’organisation fixe des règles, mais ces règles ne déterminent jamais "
       "totalement les comportements",
       "Les acteurs disposent donc de marges de manœuvre",
       "Ils cherchent à maîtriser des zones d’incertitude",
       "Cette maîtrise leur donne du pouvoir, qu’ils utilisent pour "
       "poursuivre leurs objectifs",
       "Comme ils dépendent aussi des autres, ils doivent négocier et "
       "coopérer : la relation devient une coopération conflictuelle"],
  exp="Cet enchaînement est la colonne vertébrale de l’analyse stratégique. "
      "Il explique à la fois pourquoi le fonctionnement réel d’une "
      "organisation ne correspond jamais à son organigramme, pourquoi le "
      "conflit y est normal, et pourquoi les réformes sont difficiles.",
  diss="Enchaînement à savoir dérouler : règles → marges → zones "
       "d’incertitude → pouvoir → négociation et coopération conflictuelle."),

f(id='q10-n55', sp='c10-12', niv='comprendre', type='qcm', b=2052,
  q="Qu’oppose Crozier à la conception taylorienne du travail ?",
  opts=["Que la division du travail est inefficace économiquement",
        "Que l’ouvrier n’est pas passif : il communique, développe des "
        "stratégies et possède des marges de manœuvre ; et que la division du "
        "travail peut aussi produire de mauvaises communications entre les "
        "groupes",
        "Que la séparation entre conception et exécution doit être renforcée",
        "Que les ingénieurs doivent organiser plus précisément le travail"],
  ans=1,
  why=["Crozier ne discute pas l’efficacité productive de la division du "
       "travail, mais ses effets sur les relations.",
       "C’est la position de Taylor, que Crozier critique.",
       "Renforcer l’organisation scientifique du travail est exactement la "
       "logique taylorienne."],
  exp="Pour Taylor, conception et exécution doivent être séparées, les "
      "ingénieurs organisent le travail et la division du travail augmente "
      "l’efficacité : l’ouvrier est un exécutant. Crozier en fait au "
      "contraire un acteur stratégique, capable d’utiliser les failles de "
      "l’organisation pour développer son pouvoir, et souligne que la "
      "division du travail peut dégrader la communication entre groupes.",
  diss="Mayo et Crozier convergent contre Taylor, mais par des chemins "
       "différents : le groupe et ses normes informelles chez Mayo, la "
       "stratégie et le pouvoir chez Crozier."),

# ------------------------------------------------------------- c10-13
f(id='q10-n56', sp='c10-13', niv='connaitre', type='qcm', b=2156,
  q="Quelles sont les deux fonctions fondamentales que la société exerce sur "
    "les individus selon Durkheim ?",
  opts=["La production et la répartition",
        "L’intégration et la régulation",
        "La socialisation et la sanction",
        "La coopération et le conflit"],
  ans=1,
  why=["Production et répartition sont des fonctions économiques, non des "
       "fonctions sociales au sens de Durkheim.",
       "La socialisation est le mécanisme qui permet ces deux fonctions, et "
       "non l’une d’elles.",
       "Coopération et conflit renvoient à l’analyse des organisations, chez "
       "Crozier."],
  exp="Ces deux mécanismes sont essentiels pour assurer la cohésion sociale. "
      "La régulation consiste à borner les désirs individuels : l’individu ne "
      "peut pas fixer seul une limite à ses désirs, la société doit donc lui "
      "imposer des bornes. L’intégration est le processus par lequel la "
      "société relie l’individu à des groupes sociaux. Leur défaut produit "
      "respectivement l’anomie et l’égoïsme.",
  diss="Tableau à mémoriser : régulation ↔ anomie, intégration ↔ égoïsme."),

f(id='q10-n57', sp='c10-13', niv='comprendre', type='qcm', b=2160,
  q="Quel rôle la socialisation joue-t-elle dans ce raisonnement ?",
  opts=["Elle permet à l’individu de choisir librement ses propres normes",
        "Elle permet à l’individu d’intérioriser les normes et les valeurs "
        "collectives qui encadrent ses comportements et lui permettent de "
        "vivre avec les autres",
        "Elle désigne l’apprentissage d’un métier",
        "Elle désigne la contrainte exercée par l’État sur les individus"],
  ans=1,
  why=["L’individu n’invente pas ses normes : elles lui sont transmises par "
       "la société.",
       "L’apprentissage professionnel n’est qu’un cas particulier : la "
       "socialisation est plus large.",
       "Il ne s’agit pas d’une contrainte étatique mais d’une intériorisation "
       "de normes collectives."],
  exp="Grâce à la socialisation, l’individu apprend ce qu’il doit faire, ce "
      "qu’il ne doit pas faire, et acquiert la capacité de contrôler certains "
      "désirs et d’adhérer à des valeurs collectives. C’est le point de départ "
      "des deux fonctions : la société peut réguler et intégrer parce que les "
      "individus ont intériorisé ses normes.",
  diss="Conséquence méthodologique : l’individu n’agit pas indépendamment de "
       "la société, ce qui justifie le holisme durkheimien."),

f(id='q10-n58', sp='c10-13', niv='comprendre', type='qcm', b=2213,
  q="Qu’appelle-t-on « passion de l’infini » chez Durkheim ?",
  opts=["L’ambition légitime de progresser socialement",
        "La situation dans laquelle, la société ne parvenant plus à limiter "
        "les désirs, l’individu veut toujours davantage sans disposer de "
        "normes lui indiquant jusqu’où aller",
        "Le désir de connaissance scientifique",
        "L’attachement excessif au groupe professionnel"],
  ans=1,
  why=["Il ne s’agit pas d’une ambition ordinaire mais d’une absence de "
       "borne.",
       "La connaissance n’est pas en cause : le concept porte sur les désirs "
       "et leur limitation.",
       "C’est l’inverse : le groupe professionnel est précisément ce qui "
       "régule."],
  exp="L’expression décrit l’effet de l’anomie, défaut de régulation : "
      "lorsque les normes collectives sont affaiblies, floues ou absentes, "
      "l’individu ne sait plus quelles règles suivre ni ce qu’il peut "
      "légitimement attendre, et ses désirs deviennent illimités. Il est alors "
      "désorienté, non libéré.",
  diss="Idée contre-intuitive très forte : l’absence de norme ne produit pas "
       "la liberté mais le malaise."),

f(id='q10-n59', sp='c10-13', niv='comprendre', type='assoc', b=2200,
  q="Associez chaque notion durkheimienne à ce qu’elle désigne.",
  ans=[["Le processus par lequel la société fixe des limites morales aux désirs individuels", "La régulation"],
       ["L’affaiblissement, le flou ou l’absence des normes collectives", "L’anomie"],
       ["Le processus par lequel la société rattache l’individu à des groupes sociaux", "L’intégration"],
       ["La situation d’un individu insuffisamment intégré, donc isolé", "L’égoïsme"]],
  exp="Le couple est symétrique : à chaque fonction correspond un défaut. "
      "L’anomie est un défaut de régulation, l’égoïsme un défaut "
      "d’intégration. Le travail, et plus précisément le groupe "
      "professionnel, intervient parce qu’il agit simultanément sur les deux : "
      "il rattache à un collectif et fournit des règles.",
  diss="Attention au vocabulaire : « égoïsme » n’a pas chez Durkheim le sens "
       "moral courant, il désigne un défaut d’intégration."),

f(id='q10-n60', sp='c10-13', niv='comprendre', type='qcmm', b=2277,
  q="Quels cadres traditionnels d’intégration se fragilisent, selon le "
    "constat de Durkheim ? (plusieurs réponses)",
  opts=["La famille, notamment affectée par la montée des divorces",
        "La religion",
        "Les communautés locales, les grandes villes prenant de l’importance "
        "par rapport aux petits villages",
        "Le groupe professionnel, qui disparaît avec l’industrialisation",
        "La nation, dissoute par la démocratie"],
  ans=[0, 1, 2],
  why=["Exacte : la montée des divorces est l’exemple donné par le cours.",
       "Exacte : elle perd une partie de sa force intégratrice.",
       "Exacte : dans les villages, les relations entre individus étaient "
       "souvent plus denses ; en ville elles peuvent devenir plus anonymes.",
       "Au contraire : le groupe professionnel est présenté comme la solution, "
       "le nouveau support possible de la cohésion.",
       "Le cours ne parle pas d’une dissolution de la nation."],
  exp="Durkheim observe au XIXᵉ siècle de profondes transformations — "
      "industrialisation, transformations politiques et démocratiques, "
      "affaiblissement de certains cadres traditionnels — qui rendent la "
      "cohésion sociale moins évidente. C’est face à cette fragilisation qu’il "
      "voit dans le monde professionnel un nouveau support de cohésion.",
  diss="Enchaînement du raisonnement : fragilisation des cadres traditionnels "
       "→ risque pour la cohésion → le groupe professionnel comme solution."),

f(id='q10-n61', sp='c10-13', niv='raisonner', type='courte', b=2296,
  q="Pourquoi le groupe professionnel occupe-t-il une place centrale dans la "
    "solution proposée par Durkheim ?",
  ans={'modele': "Parce qu’il remplit à lui seul les deux fonctions que la "
       "société doit assurer. Contre l’égoïsme, défaut d’intégration, il "
       "permet à l’individu d’appartenir à un collectif et d’entretenir des "
       "relations régulières : le travailleur n’est pas isolé. Contre "
       "l’anomie, défaut de régulation, il partage des règles communes et une "
       "morale professionnelle qui encadrent les comportements et limitent les "
       "désirs. Cette solution prend tout son sens dans le contexte observé "
       "par Durkheim : la famille, affectée par la montée des divorces, la "
       "religion et les communautés locales, concurrencées par l’urbanisation, "
       "perdent une partie de leur force intégratrice, de sorte que la "
       "cohésion sociale ne va plus de soi. Le monde professionnel peut alors "
       "devenir le nouveau support de cette cohésion.",
       'cles': [{'f': ['egoisme', 'collectif', 'isole', 'integration'],
                 'l': 'il lutte contre l’égoïsme en rattachant à un collectif'},
                {'f': ['anomie', 'regle', 'morale', 'regulation'],
                 'l': 'il lutte contre l’anomie en fournissant des règles'},
                {'f': ['famille', 'religion', 'village', 'traditionnel', 'divorce'],
                 'l': 'les cadres traditionnels d’intégration se fragilisent'}]},
  exp="Le cours est explicite : le groupe professionnel permet à l’individu "
      "d’appartenir à un collectif, d’entretenir des relations régulières, de "
      "partager des règles communes et d’être encadré par une morale "
      "professionnelle. Il remplit donc simultanément l’intégration et la "
      "régulation."),

]
