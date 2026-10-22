# -*- coding: utf-8 -*-
"""Ensemble 8 — L’entreprise, l’entrepreneur et la gouvernance (2/4)."""

from doss_base import d

d('n8-relation-agence', 8, "Relation d’agence",
  "Déléguer un pouvoir à quelqu’un qui sait mieux que vous",
  "La relation d’agence est le contrat par lequel une personne ou plusieurs, "
  "le principal, fait appel à une autre personne, l’agent, pour exécuter en "
  "son nom une tâche impliquant la délégation d’un certain pouvoir. Le cours "
  "lui attribue deux caractéristiques constitutives : l’incertitude et "
  "l’asymétrie d’information, cette dernière jouant en faveur de l’agent.",
  "La théorie de l’agence est l’outil par lequel le cours explique le retour "
  "du pouvoir des actionnaires, et elle se déploie en quatre temps. Premier "
  "temps, la situation : dans la grande entreprise, le principal est "
  "l’actionnaire et l’agent le manager. Deuxième temps, le problème, qui "
  "comporte deux volets indissociables. La divergence d’intérêts d’abord : les "
  "managers peuvent chercher à maximiser leur pouvoir, leur rémunération ou la "
  "croissance de l’entreprise plutôt que le profit des actionnaires. "
  "L’asymétrie d’information ensuite : les managers disposent "
  "d’informations supérieures sur la marche réelle de l’entreprise, ce qui "
  "rend leur comportement difficilement vérifiable. Troisième temps, le coût : "
  "le contrôle de l’agent par le principal occasionne des coûts d’agence, "
  "c’est-à-dire pour l’essentiel des coûts de surveillance. L’enjeu pour le "
  "principal est donc de mettre en place des incitations afin que l’agent "
  "serve ses intérêts. Quatrième temps, les instruments : des dispositifs de "
  "contrôle, conseil d’administration et audit, et des dispositifs "
  "d’incitation, au premier rang desquels les stock-options, options d’achat "
  "sur des actions attribuées à des salariés, le plus souvent des cadres, à un "
  "prix souvent plus faible que celui du marché et avec une fiscalité "
  "avantageuse lorsque les actions sont conservées un certain temps. "
  "L’objectif est explicite : aligner les intérêts des managers sur ceux des "
  "actionnaires, donc les inciter à augmenter la valeur actionnariale. Le "
  "cours formule ensuite la limite sous forme de question : l’entreprise "
  "n’est-elle qu’une chaîne de relations d’agence, le tout gouverné par "
  "l’actionnaire ? Et il relève un effet non voulu, documenté par Nicholas "
  "Bloom, puisque les incitations s’ajoutent à la rémunération des managers.",
  [("La délégation de pouvoir",
    "Le principal confie à l’agent l’exécution d’une tâche en son nom, ce qui "
    "implique de lui transférer un pouvoir de décision : sans cette "
    "délégation il n’y aurait pas de relation d’agence, mais une simple "
    "prestation entièrement spécifiée."),
   ("La divergence d’intérêts",
    "L’agent poursuit ses objectifs propres, maximiser son pouvoir, sa "
    "rémunération ou la croissance de l’entreprise, qui ne coïncident pas "
    "avec le profit du principal : la délégation ouvre donc un écart entre ce "
    "qui est voulu et ce qui est fait."),
   ("L’asymétrie d’information en faveur de l’agent",
    "L’agent connaît mieux que le principal la situation réelle et ses propres "
    "efforts : le principal ne peut pas observer directement le comportement "
    "qu’il paie, ce qui rend le contrat incomplet et la vérification "
    "coûteuse."),
   ("Les coûts d’agence",
    "Pour limiter cet écart, le principal doit surveiller : les coûts "
    "d’agence sont essentiellement des coûts de surveillance, auxquels "
    "s’ajoutent les coûts des dispositifs d’incitation, de sorte que le "
    "contrôle n’est jamais gratuit."),
   ("L’alignement par l’incitation",
    "Plutôt que de surveiller indéfiniment, le principal intéresse l’agent au "
    "résultat : stock-options et rémunérations variables font dépendre le "
    "revenu du manager de la valeur de l’action, de sorte qu’il ait "
    "intérêt à l’augmenter.")],
  [{'a': "La théorie de l’agence explique précisément pourquoi la "
         "gouvernance d’entreprise devient un problème dès que propriété et "
         "direction se séparent.",
    'cond': "Elle suppose que les actionnaires soient réellement les "
            "mandants, c’est-à-dire qu’ils disposent de droits de contrôle "
            "effectifs sur les dirigeants.",
    'lim': "Le cours relève que cette lecture réduit l’entreprise à une "
           "chaîne de relations d’agence gouvernée par l’actionnaire, ce "
           "qu’il présente explicitement comme la limite de l’approche."},
   {'a': "Les mécanismes d’incitation résolvent un problème d’information "
         "sans exiger une surveillance permanente et coûteuse.",
    'cond': "L’incitation ne fonctionne que si l’indicateur retenu, ici le "
            "cours de l’action, reflète effectivement la performance "
            "attribuable au dirigeant.",
    'lim': "Si l’indicateur est manipulable ou de court terme, l’incitation "
           "oriente le comportement vers la performance boursière immédiate "
           "plutôt que vers la valeur de long terme."},
   {'a': "Les dispositifs de contrôle, conseil d’administration et audit, "
         "réduisent effectivement l’asymétrie d’information entre "
         "actionnaires et dirigeants.",
    'cond': "Ils supposent des organes réellement indépendants et des "
            "informations comptables fiables, condition qui définit la "
            "qualité de la gouvernance.",
    'lim': "Le scandale Enron en 2001, marqué par des manipulations "
           "comptables, montre que ces dispositifs peuvent être contournés "
           "par ceux qu’ils sont censés contrôler."},
   {'a': "Le raisonnement se généralise bien au-delà du couple "
         "actionnaire-manager, puisque toute délégation de pouvoir en relève.",
    'cond': "La généralisation exige que l’on identifie clairement, dans "
            "chaque cas, qui est le principal, qui est l’agent et sur quoi "
            "porte l’asymétrie.",
    'lim': "Crozier montre que les acteurs peuvent avoir intérêt à maintenir "
           "les asymétries plutôt qu’à les réduire, ce qui contredit "
           "l’objectif même de la théorie."}],
  [{'t': "L’entreprise n’est qu’un nœud de relations contractuelles "
         "bilatérales, c’est-à-dire une structure de contrôle des "
         "comportements.",
    'qui': "Michael Jensen et William Meckling, dans la théorie de l’agence.",
    'rep': "Le cours pose lui-même la question qui la limite : l’entreprise "
           "n’est-elle qu’une chaîne de relations d’agence gouvernée par "
           "l’actionnaire ? Elle est aussi un lieu de coopération, de culture "
           "et de rapports de pouvoir."},
   {'t': "Les incitations financières alignent les intérêts des managers sur "
         "ceux des actionnaires sans effet pervers notable.",
    'qui': "La logique de la corporate governance des années 1990.",
    'rep': "Nicholas Bloom montre que ces incitations s’ajoutent à la "
           "rémunération des managers et participent au creusement des écarts "
           "de revenus entre entreprises, ce qui fait de la gouvernance "
           "actionnariale une source d’inégalités."},
   {'t': "Il faut réduire les asymétries d’information pour que la relation "
         "d’agence fonctionne correctement.",
    'qui': "La lecture économique de l’information imparfaite, que le cours "
           "rattache à Williamson et à Akerlof.",
    'rep': "Crozier objecte que les acteurs peuvent au contraire avoir "
           "intérêt à maintenir certaines asymétries, parce qu’une "
           "information que les autres n’ont pas constitue une ressource de "
           "pouvoir."}],
  [{'n': "Michael Jensen",
    'i': "La relation d’agence lie un principal, par exemple les "
         "actionnaires, à un agent, par exemple le manager.",
    'p': "Avec William Meckling, dans Theory of the Firm : Managerial "
         "Behavior, Agency Costs and Ownership Structure, en 1976, il analyse "
         "les contrats par lesquels le principal délègue un pouvoir, et "
         "identifie deux caractéristiques de la relation : l’incertitude et "
         "l’asymétrie d’information."},
   {'n': "William Meckling",
    'i': "La firme est un nœud de relations contractuelles bilatérales "
         "analysables comme des relations d’agence.",
    'p': "Le cours en tire la formule décisive : pour Jensen et Meckling, la "
         "firme est avant tout une structure de contrôle des comportements. "
         "Par des incitations, le principal fait en sorte que l’agent serve "
         "ses intérêts plutôt que les siens."},
   {'n': "Nicholas Bloom",
    'i': "Les écarts de revenus sont restés constants au sein des entreprises "
         "mais ont crû entre les entreprises.",
    'p': "Le cours rattache ce constat à Corporations in the Age of "
         "Inequality, publié dans la Harvard Business Review en 2017, et "
         "l’articule aux stock-options : les incitations destinées à aligner "
         "les managers alimentent la hausse de leurs rémunérations."},
   {'n': "Michel Crozier",
    'i': "Les acteurs peuvent avoir intérêt à maintenir une asymétrie "
         "d’information plutôt qu’à la réduire.",
    'p': "Le cours en fait une objection directe à la logique de l’agence : "
         "alors que les analyses économiques cherchent à réduire "
         "l’information imparfaite, l’acteur qui détient une information rare "
         "préserve une zone d’incertitude et renforce son pouvoir."}],
  [{'f': "Les stock-options sont des options d’achat sur des actions "
         "attribuées à des salariés, le plus souvent des cadres, à un prix "
         "souvent plus faible que celui du marché, avec une fiscalité "
         "avantageuse en cas de conservation.",
    'p': "Le détail du dispositif montre comment l’incitation est construite "
         "techniquement : elle lie mécaniquement le patrimoine du dirigeant "
         "au cours de l’action, donc à la valeur actionnariale."},
   {'f': "Le scandale Enron, en 2001, est marqué par des manipulations "
         "comptables et une faillite retentissante.",
    'p': "Le cas démontre que les dispositifs de contrôle peuvent être "
         "détournés par les dirigeants eux-mêmes : la relation d’agence ne "
         "garantit pas la sincérité de l’information sur laquelle elle "
         "repose."},
   {'f': "Le cours distingue deux familles de remèdes : des dispositifs de "
         "contrôle, conseil d’administration et audit, et des dispositifs "
         "d’incitation, notamment la distribution de stock-options.",
    'p': "La distinction montre que le problème d’agence admet deux "
         "traitements de nature différente, l’un par la vérification, l’autre "
         "par l’intéressement, dont les effets pervers ne sont pas les "
         "mêmes."}],
  [{'q': "Qui dirige réellement l’entreprise ?",
    'f': "La théorie de l’agence répond que personne ne dirige entièrement : "
         "les actionnaires détiennent le droit de décider mais pas "
         "l’information, les managers détiennent l’information mais pas la "
         "propriété. La gouvernance d’entreprise consiste précisément à "
         "organiser cette dissociation pour que celui qui sait agisse dans "
         "l’intérêt de celui qui possède.",
    'r': "On montre que le pouvoir se décompose en droits de décision et en "
         "information, puis que leur séparation suffit à produire le problème "
         "de gouvernance, sans supposer de malveillance.",
    'ex': "Jensen et Meckling définissent en 1976 la firme comme une "
          "structure de contrôle des comportements."},
   {'q': "Les incitations suffisent-elles à aligner les intérêts ?",
    'f': "Les stock-options font dépendre le revenu du dirigeant du cours de "
         "l’action, ce qui aligne formellement son intérêt sur celui de "
         "l’actionnaire. Mais l’alignement porte sur un indicateur, non sur "
         "la performance réelle : il encourage la hausse du cours à court "
         "terme et nourrit, comme le montre Bloom, la divergence des "
         "rémunérations.",
    'r': "Le raisonnement distingue l’objectif visé de l’indicateur utilisé, "
         "et montre que l’incitation agit toujours sur le second, d’où les "
         "effets non voulus.",
    'ex': "Bloom constate en 2017 des écarts de revenus croissants entre "
          "entreprises américaines."},
   {'q': "L’entreprise se réduit-elle à une chaîne de relations d’agence ?",
    'f': "La formulation est celle du cours lui-même, qui en fait la limite "
         "de l’approche contractuelle : réduire la firme à des contrats et à "
         "des calculs laisse de côté les relations humaines, la culture "
         "d’entreprise et les rapports de pouvoir, que l’analyse "
         "transactionnelle et la sociologie des organisations rétablissent.",
    'r': "On prend au sérieux la puissance du modèle, puis on montre ce "
         "qu’il laisse hors de son champ, en s’appuyant sur les objections "
         "que le cours formule explicitement.",
    'ex': "Crozier montre que les acteurs entretiennent les asymétries "
          "d’information au lieu de les réduire."}],
  voisins=['n8-propriete-controle', 'n8-gouvernance', 'n6-asymetries',
           'n8-valeur-actionnariale'])


d('n8-propriete-controle', 8, "Séparation entre propriété et contrôle",
  "Ceux qui possèdent ne dirigent plus, ceux qui dirigent ne possèdent pas",
  "La séparation entre propriété et contrôle désigne la situation des grandes "
  "entreprises modernes dans lesquelles les actionnaires détiennent le capital "
  "tandis que les managers assurent la direction effective. Le cours l’oppose "
  "au capitalisme entrepreneurial, où la propriété du capital et le pouvoir de "
  "décision sont confondus dans la personne de l’entrepreneur.",
  "La séparation entre propriété et contrôle est le pivot du chapitre sur la "
  "gouvernance, et le cours en expose la cause, la formulation théorique, "
  "l’approfondissement et la conséquence. La cause est matérielle : avec les "
  "révolutions industrielles, les techniques deviennent plus complexes, "
  "sidérurgie, chemins de fer, machines sophistiquées, les infrastructures se "
  "développent, l’organisation de la production s’élargit, et l’entreprise "
  "devient difficile à diriger par une seule personne. Il faut mobiliser des "
  "savoirs spécialisés, d’où la montée des ingénieurs formés dans les écoles "
  "techniques, puis celle des managers, la gestion devenant une activité "
  "spécialisée répartie en fonctions, production, finance, ressources "
  "humaines, stratégie. Henri Fayol montre dans Administration industrielle et "
  "générale, en 1916, que diriger repose sur cinq fonctions, prévoir, "
  "organiser, commander, coordonner, contrôler, et devient donc une compétence "
  "enseignable. La formulation théorique est celle de Berle et Means dans The "
  "Modern Corporation and Private Property, en 1932 : le capital est dispersé "
  "entre de nombreux actionnaires qui ne disposent ni du temps, ni des "
  "compétences, ni de l’information nécessaires pour gérer l’entreprise, et "
  "qui délèguent donc le pouvoir aux managers. Le résultat est net : ceux qui "
  "possèdent ne dirigent plus, ceux qui dirigent ne possèdent pas "
  "nécessairement. L’approfondissement vient de Galbraith : dans Le Nouvel "
  "État industriel, en 1967, il montre que la domination des managers ne "
  "s’explique pas seulement par la dispersion du capital mais par la maîtrise "
  "de l’information et des compétences, et il nomme technostructure "
  "l’ensemble des dirigeants, cadres, ingénieurs et experts qui participent à "
  "la direction effective. La conséquence est le problème de gouvernance : "
  "comment s’assurer que les managers agissent dans l’intérêt des "
  "actionnaires ?",
  [("La complexification technique",
    "Les techniques et les infrastructures deviennent trop complexes pour "
    "être maîtrisées par une seule personne : il faut mobiliser des savoirs "
    "spécialisés, ce qui fait monter les ingénieurs puis les managers dans la "
    "direction des entreprises."),
   ("La professionnalisation de la gestion",
    "La direction se divise en fonctions distinctes, production, finance, "
    "ressources humaines, stratégie, et devient une compétence enseignable "
    "dans des écoles dédiées : posséder ne suffit plus, il faut savoir "
    "coordonner."),
   ("La dispersion du capital",
    "Le capital se répartit entre de nombreux actionnaires qui n’ont ni le "
    "temps, ni les compétences, ni l’information pour gérer : la délégation du "
    "pouvoir aux managers devient une nécessité organisationnelle et non un "
    "choix."),
   ("Le déplacement du pouvoir vers l’information",
    "Le pouvoir effectif suit la maîtrise des connaissances techniques, "
    "financières et organisationnelles : la technostructure détient le "
    "pouvoir réel parce qu’elle détient les informations nécessaires à la "
    "décision."),
   ("L’ouverture du problème de gouvernance",
    "Dès que la propriété et la direction ne coïncident plus, il faut un "
    "dispositif pour que les managers agissent dans l’intérêt des "
    "actionnaires : c’est l’origine même de la corporate governance et de la "
    "théorie de l’agence.")],
  [{'a': "La séparation explique un fait massif que le modèle du "
         "propriétaire-dirigeant ne peut pas rendre : la direction des "
         "grandes entreprises par des salariés non propriétaires.",
    'cond': "Elle suppose une dispersion effective du capital, qui rend "
            "impossible le contrôle direct par les actionnaires.",
    'lim': "Elle décrit mal les entreprises à capital concentré, familiales "
           "ou détenues par un actionnaire de référence, où le contrôle "
           "demeure attaché à la propriété."},
   {'a': "La gouvernance managériale privilégie la stabilité, l’innovation et "
         "la planification de long terme, que la pression actionnariale tend "
         "à sacrifier.",
    'cond': "Cet avantage suppose que les managers poursuivent effectivement "
            "la croissance et l’organisation efficace, et non leur seul "
            "intérêt personnel.",
    'lim': "C’est précisément l’hypothèse que la théorie de l’agence refuse : "
           "les managers peuvent maximiser leur pouvoir ou leur rémunération "
           "plutôt que le profit."},
   {'a': "Faire du savoir la source du pouvoir permet de comprendre pourquoi "
         "les actionnaires ne peuvent pas reprendre facilement le contrôle.",
    'cond': "L’argument vaut tant que l’information technique reste "
            "difficilement accessible à ceux qui n’appartiennent pas à "
            "l’organisation.",
    'lim': "Le développement des marchés financiers, des audits et des "
           "analystes a réduit cette opacité, ce qui rend possible le retour "
           "des actionnaires à partir des années 1970."},
   {'a': "La professionnalisation de la direction améliore la qualité de la "
         "gestion, puisqu’elle substitue des compétences enseignables à "
         "l’intuition du propriétaire.",
    'cond': "Elle suppose que la gestion soit effectivement rationalisable "
            "autour de règles générales applicables à toutes les "
            "entreprises, comme le soutient Fayol.",
    'lim': "Cette rationalisation peut engendrer une bureaucratisation et une "
           "rigidité, comme le montre le cercle vicieux bureaucratique mis en "
           "évidence par Crozier."}],
  [{'t': "Les actionnaires, trop nombreux et trop peu informés, doivent "
         "déléguer le pouvoir aux managers, qui détiennent dès lors le "
         "pouvoir effectif.",
    'qui': "Adolf Berle et Gardiner Means, dans The Modern Corporation and "
           "Private Property, en 1932.",
    'rep': "Le cours ne conteste pas le constat mais sa portée durable : à "
           "partir des années 1970, le développement des marchés financiers "
           "permet aux actionnaires de reprendre du pouvoir par les "
           "dispositifs de la corporate governance."},
   {'t': "Le pouvoir dans l’entreprise appartient aux experts qui maîtrisent "
         "l’information, et non aux propriétaires du capital.",
    'qui': "John Kenneth Galbraith, avec la technostructure, dans Le Nouvel "
           "État industriel, en 1967.",
    'rep': "La thèse éclaire la période managériale mais sous-estime la "
           "capacité des marchés financiers à discipliner les dirigeants : la "
           "financiarisation a précisément réduit l’avantage informationnel "
           "des managers."},
   {'t': "La direction d’entreprise peut devenir une science organisée, avec "
         "des règles générales applicables à toutes les entreprises.",
    'qui': "Henri Fayol, dans Administration industrielle et générale, en "
           "1916.",
    'rep': "L’analyse fonde la professionnalisation de la gestion, mais la "
           "sociologie des organisations montre ensuite qu’aucune règle "
           "formelle ne détermine entièrement le fonctionnement réel d’une "
           "organisation."}],
  [{'n': "Adolf Berle",
    'i': "Dans les grandes entreprises modernes, les actionnaires détiennent "
         "le capital mais les managers assurent la direction.",
    'p': "Avec Gardiner Means, dans The Modern Corporation and Private "
         "Property, en 1932, il établit que la dispersion du capital prive "
         "les actionnaires du temps, des compétences et de l’information "
         "nécessaires à la gestion, ce qui rend la délégation inévitable."},
   {'n': "Gardiner Means",
    'i': "La délégation du pouvoir aux managers est une nécessité "
         "organisationnelle et non un choix des actionnaires.",
    'p': "Le cours en tire la formule qui résume le capitalisme managérial : "
         "ceux qui possèdent ne dirigent plus, ceux qui dirigent ne possèdent "
         "pas nécessairement, de sorte que le pouvoir effectif se déplace "
         "vers les managers."},
   {'n': "John Kenneth Galbraith",
    'i': "La technostructure réunit dirigeants, cadres, ingénieurs et experts "
         "qui participent à la direction effective de l’entreprise.",
    'p': "Dans Le Nouvel État industriel, en 1967, il montre que ce groupe "
         "détient le pouvoir réel parce qu’il maîtrise les connaissances "
         "nécessaires à la décision : le pouvoir repose sur l’information et "
         "les compétences, non sur la propriété du capital."},
   {'n': "Henri Fayol",
    'i': "Diriger une entreprise repose sur cinq fonctions : prévoir, "
         "organiser, commander, coordonner, contrôler.",
    'p': "Le cours souligne la rupture : avant Fayol, diriger relève de "
         "l’expérience personnelle ou du talent individuel ; avec lui, la "
         "gestion devient une science organisée, donc une activité technique "
         "enseignable et professionnalisable."}],
  [{'f': "Le cours prend l’exemple d’une grande entreprise sidérurgique ou "
         "ferroviaire, qui ne peut plus être dirigée à l’intuition par son "
         "propriétaire.",
    'p': "L’exemple montre la cause matérielle de la séparation : il faut "
         "planifier la production, coordonner des milliers de salariés, gérer "
         "les finances et organiser les approvisionnements."},
   {'f': "La professionnalisation de la direction s’accompagne du "
         "développement des écoles de commerce et de formations dédiées à la "
         "gestion.",
    'p': "L’apparition d’institutions de formation démontre que la "
         "compétence de direction est devenue un savoir transmissible, "
         "distinct de la possession du capital."},
   {'f': "La montée des managers s’accompagne de nouvelles structures : la "
         "forme unitaire, centralisée par fonctions, et la forme "
         "multidivisionnelle, décentralisée en unités autonomes avec une "
         "direction stratégique centrale.",
    'p': "Ces structures prouvent que la séparation entre propriété et "
         "contrôle n’est pas seulement juridique : elle transforme "
         "l’organisation interne de l’entreprise."}],
  [{'q': "La propriété donne-t-elle le pouvoir dans l’entreprise ?",
    'f': "Dans le capitalisme entrepreneurial, la réponse va de soi puisque "
         "le propriétaire dirige. Dans la grande entreprise moderne, Berle et "
         "Means montrent en 1932 que le capital dispersé ne donne plus le "
         "pouvoir effectif, et Galbraith ajoute que celui-ci suit la maîtrise "
         "de l’information : la propriété confère un droit, l’expertise "
         "confère le pouvoir.",
    'r': "Le raisonnement distingue les titres juridiques des capacités "
         "effectives, puis montre que leur disjonction définit le "
         "capitalisme managérial.",
    'ex': "La technostructure que Galbraith décrit en 1967 réunit des "
          "dirigeants, des cadres, des ingénieurs et des experts."},
   {'q': "La séparation entre propriété et contrôle est-elle un progrès ?",
    'f': "Elle améliore la gestion, puisqu’elle substitue des compétences "
         "spécialisées à l’intuition du propriétaire, et elle favorise la "
         "stabilité et la planification de long terme. Mais elle crée "
         "simultanément un problème inédit : rien ne garantit plus que celui "
         "qui décide poursuive l’intérêt de celui qui possède.",
    'r': "On met en balance un gain de compétence et une perte de contrôle, "
         "puis on montre que le second effet appelle les dispositifs de "
         "gouvernance qui apparaissent ensuite.",
    'ex': "La corporate governance des années 1990 naît précisément pour "
          "discipliner les managers des sociétés anonymes."},
   {'q': "Le pouvoir managérial était-il durable ?",
    'f': "Le capitalisme managérial repose sur un avantage informationnel des "
         "dirigeants sur des actionnaires dispersés. Or cet avantage "
         "s’érode : à partir des années 1970, le développement des marchés "
         "financiers, la mondialisation et la libéralisation renforcent les "
         "investisseurs, qui reprennent progressivement le contrôle et "
         "imposent la logique actionnariale.",
    'r': "Le raisonnement identifie la condition de la domination "
         "managériale, puis montre que son affaiblissement explique le "
         "basculement vers le capitalisme actionnarial.",
    'ex': "Bourguinat résume cette transformation financière par la "
          "désintermédiation, le décloisonnement et la déréglementation."}],
  voisins=['n8-capitalisme-managerial', 'n8-relation-agence',
           'n8-gouvernance', 'n8-capitalisme-actionnarial'])


d('n8-capitalisme-entrepreneurial', 8, "Capitalisme entrepreneurial",
  "Le moment où posséder et diriger sont une même chose",
  "Le capitalisme entrepreneurial désigne la forme de gouvernance des débuts "
  "du capitalisme industriel, dans laquelle la propriété du capital et le "
  "pouvoir de décision sont confondus dans la personne de l’entrepreneur. Le "
  "cours souligne qu’il s’agit fréquemment d’un capitalisme familial, dans "
  "lequel l’entreprise est étroitement liée à la famille fondatrice et "
  "transmise de génération en génération.",
  "Le capitalisme entrepreneurial est le premier des trois régimes de "
  "gouvernance que distingue le cours, et il se définit par une confusion plus "
  "que par une organisation. Au dix-neuvième siècle, l’entreprise est de "
  "petite taille, peu complexe, et repose sur une personne centrale : "
  "l’entrepreneur cumule la propriété du capital, la direction de l’entreprise "
  "et souvent l’activité productive elle-même. Le cours formule l’idée clé "
  "sans nuance : confusion totale entre propriété et contrôle. Cette "
  "concentration du pouvoir s’explique par la nature même des entreprises de "
  "l’époque, souvent familiales, transmises de génération en génération, liées "
  "à une dynastie, au point que le nom de l’entreprise reflète celui de la "
  "famille, comme Peugeot ou Hermès. Elle s’appuie aussi sur un régime "
  "juridique précis : l’entrepreneur individuel ne sépare pas son patrimoine "
  "personnel de celui de l’entreprise et engage donc ses biens professionnels "
  "mais aussi ses biens personnels. Le risque maximal renforce son pouvoir, "
  "car il supporte personnellement les conséquences de ses décisions. Cette "
  "figure est enfin valorisée : Weber y voit une domination possiblement "
  "charismatique, Schumpeter un innovateur moteur du capitalisme, tandis que "
  "le récit dominant du fondateur génial et solitaire en fait un héros, "
  "représentation qu’Anthony Galluzzo critique en 2023. Mais le cours insiste "
  "sur la limite interne de ce régime : avec les révolutions industrielles, "
  "les entreprises grandissent, les techniques deviennent plus complexes, la "
  "gestion devient plus difficile, et une seule personne ne peut plus tout "
  "contrôler efficacement. La séparation entre propriété et direction commence "
  "alors à apparaître.",
  [("Le cumul de la propriété et de la direction",
    "L’entrepreneur réunit l’apport de capital, la direction et souvent la "
    "production : il n’existe pas d’organe distinct de gouvernance, puisque "
    "le propriétaire est lui-même l’instance de décision de l’entreprise."),
   ("La transmission familiale",
    "L’entreprise est liée à une dynastie et transmise de génération en "
    "génération : la continuité du pouvoir ne repose pas sur une procédure de "
    "nomination mais sur l’hérédité, ce qui stabilise le contrôle sur longue "
    "période."),
   ("La responsabilité illimitée",
    "Faute de séparation des patrimoines, l’entrepreneur engage ses biens "
    "personnels dans l’activité : cette exposition maximale fonde la "
    "légitimité de son pouvoir et aligne naturellement décision et "
    "conséquence."),
   ("La légitimation par le charisme et l’innovation",
    "L’autorité de l’entrepreneur se double d’une valorisation : charisme "
    "chez Weber, innovation chez Schumpeter, récit du fondateur dans le "
    "discours commun, ce qui transforme une position économique en figure "
    "exemplaire."),
   ("L’épuisement du modèle",
    "La croissance de la taille et de la complexité technique rend la "
    "direction personnelle impraticable : il faut des compétences "
    "spécialisées, ingénieurs puis managers, ce qui amorce la séparation "
    "entre propriété et direction.")],
  [{'a': "Le modèle décrit fidèlement la gouvernance des entreprises au "
         "début du capitalisme industriel, où la petite taille rend possible "
         "la direction personnelle.",
    'cond': "La validité est historiquement bornée : elle exige des "
            "entreprises peu complexes qu’une seule personne puisse "
            "maîtriser entièrement.",
    'lim': "Dès que les techniques se complexifient et que la taille "
           "augmente, la direction personnelle devient inefficace et le "
           "modèle cesse de décrire la réalité."},
   {'a': "La confusion entre propriété et contrôle évite tout problème "
         "d’agence, puisque celui qui décide est celui qui supporte le "
         "résultat.",
    'cond': "Elle suppose la responsabilité illimitée, qui fait porter à "
            "l’entrepreneur les pertes comme les gains de ses décisions.",
    'lim': "Cette absence de conflit d’intérêts se paie par une absence de "
           "contrôle : rien ne corrige les erreurs du propriétaire-dirigeant, "
           "et le capital disponible reste limité à son patrimoine."},
   {'a': "Le capitalisme familial assure une continuité de long terme et un "
         "attachement à l’entreprise que la logique financière ne produit "
         "pas.",
    'cond': "L’avantage suppose que la succession familiale fournisse "
            "effectivement des dirigeants compétents.",
    'lim': "La transmission par l’hérédité ne sélectionne pas sur la "
           "compétence, ce qui est exactement l’argument qui justifiera "
           "ensuite le recrutement de managers professionnels."},
   {'a': "La figure de l’entrepreneur éclaire un ressort réel de la "
         "dynamique capitaliste : la prise de risque et l’innovation.",
    'cond': "Il faut que l’innovation provienne effectivement d’initiatives "
            "individuelles capables de rompre les routines, comme le soutient "
            "Schumpeter.",
    'lim': "Galluzzo montre que l’innovation est collective et souvent "
           "financée par l’État, ce qui déplace le moteur de l’individu vers "
           "l’organisation."}],
  [{'t': "Dans le capitalisme entrepreneurial, la propriété du capital et le "
         "pouvoir de décision sont confondus dans la personne de "
         "l’entrepreneur.",
    'qui': "L’analyse du cours sur les débuts du capitalisme industriel.",
    'rep': "Le constat est exact mais historiquement daté : la croissance des "
           "entreprises et la complexité technique imposent ensuite la "
           "séparation entre propriété et direction, qui définit le "
           "capitalisme managérial."},
   {'t': "La réussite entrepreneuriale résulte du mérite d’un individu "
       "seul, " "parti de rien et devenu riche par son seul travail.",
    'qui': "Le récit du fondateur, critiqué par Anthony Galluzzo en 2023.",
    'rep': "Galluzzo montre que l’innovation est collective, que les "
           "salariés, ingénieurs et chercheurs y jouent un rôle majeur, que "
           "l’État finance souvent une part essentielle des innovations et "
           "que beaucoup d’entrepreneurs viennent de milieux favorisés."},
   {'t': "Le capitalisme entrepreneurial est intrinsèquement un capitalisme "
         "familial, la propriété et la direction se transmettant ensemble.",
    'qui': "Le cours, qui cite Peugeot et Hermès comme dynasties "
           "industrielles.",
    'rep': "La transmission familiale explique la stabilité du contrôle mais "
           "constitue aussi sa faiblesse : elle sélectionne les dirigeants "
           "par l’hérédité et non par la compétence, ce qui ouvre la voie aux "
           "managers professionnels."}],
  [{'n': "Max Weber",
    'i': "L’entrepreneur peut incarner une domination charismatique, fondée "
         "sur une qualité personnelle plutôt que sur la richesse.",
    'p': "Le cours rattache cette lecture aux trois formes de domination, "
         "rationnelle-légale, traditionnelle et charismatique, et en tire "
         "que si les individus suivent l’entrepreneur, ce n’est pas seulement "
         "parce qu’il est propriétaire, mais parce qu’il inspire et fédère."},
   {'n': "Joseph Schumpeter",
    'i': "L’entrepreneur est un innovateur et un preneur de risque, à "
         "l’origine de la croissance économique.",
    'p': "Le cours en fait le moteur du capitalisme : l’économie n’avance pas "
         "toute seule, elle progresse grâce à des individus qui cassent les "
         "routines, introduisent de nouveaux produits, de nouvelles "
         "techniques et de nouveaux marchés."},
   {'n': "Anthony Galluzzo",
    'i': "L’image héroïque de l’entrepreneur sert à légitimer l’ordre "
         "économique et social.",
    'p': "Dans Le mythe de l’entrepreneur, en 2023, il énumère ce que ce "
         "récit dissimule : le caractère collectif de l’innovation, le rôle "
         "des salariés et des chercheurs, le financement public, l’origine "
         "sociale favorisée des fondateurs et le poids des réseaux."}],
  [{'f': "Le nom de l’entreprise reflète souvent celui de la famille "
         "fondatrice, comme le montrent les cas de Peugeot et d’Hermès que "
         "cite le cours.",
    'p': "Le fait établit le caractère dynastique du capitalisme "
         "entrepreneurial : l’entreprise n’est pas une personne morale "
         "autonome mais le prolongement d’une famille."},
   {'f': "À l’origine, l’entrepreneur individuel ne distingue pas son "
         "patrimoine personnel de celui de l’entreprise et engage ses biens "
         "propres dans l’activité.",
    'p': "Ce régime juridique montre que la concentration du pouvoir avait "
         "une contrepartie réelle : le dirigeant supportait personnellement "
         "l’intégralité du risque économique."},
   {'f': "Avec les révolutions industrielles, les entreprises grandissent, "
         "les techniques deviennent plus complexes et la gestion devient plus "
         "difficile, notamment dans la sidérurgie et les chemins de fer.",
    'p': "Cette évolution démontre que la fin du capitalisme entrepreneurial "
         "n’est pas idéologique mais technique : une seule personne ne peut "
         "plus contrôler efficacement l’entreprise."}],
  [{'q': "Qui dirige l’entreprise aux origines du capitalisme ?",
    'f': "La réponse est d’une simplicité trompeuse : celui qui possède "
         "l’entreprise la dirige, et souvent y travaille. Mais cette "
         "confusion n’est pas une propriété du capitalisme en général ; elle "
         "résulte d’une taille réduite, d’une faible complexité technique et "
         "d’un régime de responsabilité illimitée qui aligne décision et "
         "exposition au risque.",
    'r': "On montre que la figure de l’entrepreneur-dirigeant est le produit "
         "de conditions objectives, ce qui permet d’annoncer sa disparition "
         "dès que ces conditions changent.",
    'ex': "Le cours relève que les entreprises du dix-neuvième siècle sont de "
          "petite taille et peu complexes."},
   {'q': "Le capitalisme entrepreneurial est-il un capitalisme familial ?",
    'f': "Le cours répond que le capitalisme entrepreneurial est fréquemment "
         "familial : l’entreprise est transmise de génération en génération "
         "et liée à une dynastie. Cette forme de transmission garantit la "
         "continuité du contrôle, mais elle sélectionne les dirigeants par "
         "l’hérédité, ce qui devient une faiblesse dès que la direction exige "
         "des compétences spécialisées.",
    'r': "Le raisonnement transforme un trait descriptif en argument : la "
         "transmission familiale explique à la fois la force et la fragilité "
         "du régime.",
    'ex': "Le cours cite Peugeot et Hermès comme exemples de ce lien entre "
          "entreprise et famille fondatrice."},
   {'q': "Faut-il nuancer la figure de l’entrepreneur ?",
    'f': "La représentation dominante repose sur un récit puissant, celui du "
         "fondateur génial et solitaire parti de rien. Galluzzo montre en "
         "2023 que ce récit remplit une fonction de légitimation et masque "
         "une réalité collective : l’innovation vient aussi des salariés, des "
         "ingénieurs et des chercheurs, et l’État en finance souvent une part "
         "essentielle.",
    'r': "On distingue la fonction économique, qui résiste, de son "
         "attribution exclusive à un individu, qui ne résiste pas à "
         "l’examen sociologique.",
    'ex': "Galluzzo souligne que beaucoup d’entrepreneurs viennent déjà de "
          "milieux favorisés."}],
  voisins=['n8-entrepreneur', 'n8-capitalisme-managerial',
           'n8-propriete-controle', 'n8-risque-incertitude'])


d('n8-capitalisme-managerial', 8, "Capitalisme managérial",
  "Le pouvoir des compétences, la main visible des managers",
  "Le capitalisme managérial désigne la forme de gouvernance caractérisée par "
  "la séparation entre la propriété et la direction de l’entreprise : les "
  "actionnaires détiennent le capital, mais les managers assurent la gestion "
  "effective. Le cours en fait un régime complet, avec ses objectifs propres, "
  "la stabilité et la planification de long terme, et ses structures "
  "organisationnelles spécifiques.",
  "Le capitalisme managérial est le régime intermédiaire du chapitre, et le "
  "cours en expose la naissance, le fondement du pouvoir, les formes "
  "organisationnelles et le déclin. La naissance est fonctionnelle : la "
  "complexification des entreprises fait monter les ingénieurs puis les "
  "managers, la gestion devenant une activité spécialisée organisée en "
  "fonctions, et Fayol établit en 1916 qu’elle peut être enseignée. Le "
  "fondement du pouvoir est double. Berle et Means, en 1932, le rattachent à "
  "la dispersion du capital : les actionnaires n’ont ni le temps, ni les "
  "compétences, ni l’information nécessaires et délèguent. Galbraith, en 1967, "
  "y ajoute la maîtrise de l’information et des compétences : la "
  "technostructure, qui réunit dirigeants, cadres, ingénieurs et experts, "
  "détient le pouvoir réel. Le cours en tire une conséquence normative "
  "assumée : une gouvernance managériale permet de privilégier la stabilité, "
  "l’innovation et la planification de long terme. Les formes "
  "organisationnelles viennent de Chandler, dans La main visible des managers, "
  "en 1977 : historien de l’économie, il explique que le succès de l’économie "
  "américaine après 1840 vient de sa capacité à développer des firmes de "
  "grande taille, intégrées verticalement et horizontalement, efficientes "
  "parce qu’elles réalisent des économies d’échelle, s’appuient sur la "
  "division du travail et font appel aux managers pour coordonner les "
  "activités en dehors du marché. À la main invisible du marché chère à Smith, "
  "Chandler oppose la main visible des managers, écrivant que la main visible "
  "de la gestion remplaçait la main invisible des forces du marché dans la "
  "coordination des flux de marchandises. Il distingue la forme unitaire, "
  "centralisée par fonctions, et la forme multidivisionnelle, décentralisée en "
  "unités autonomes avec une direction stratégique centrale. Le déclin vient "
  "des années 1970-1980, lorsque la montée des marchés financiers permet aux "
  "actionnaires de reprendre le contrôle.",
  [("La délégation par défaut d’information",
    "Les actionnaires dispersés ne peuvent pas gérer : la délégation aux "
    "managers n’est pas un choix mais une nécessité organisationnelle, ce qui "
    "transfère aux dirigeants le pouvoir effectif sans leur transférer la "
    "propriété."),
   ("Le pouvoir fondé sur la compétence",
    "Le pouvoir suit la maîtrise des connaissances techniques, financières et "
    "organisationnelles : la technostructure décide parce qu’elle seule "
    "comprend les décisions à prendre, ce qui rend le contrôle externe "
    "difficile."),
   ("La coordination administrative substituée au marché",
    "Dans la grande firme intégrée, les flux de marchandises sont coordonnés "
    "par la hiérarchie et non par les prix : la main visible de la gestion "
    "remplace la main invisible du marché dans l’organisation de la "
    "production."),
   ("Les économies d’échelle de la grande firme",
    "L’intégration verticale et horizontale permet d’étaler les coûts fixes, "
    "de mieux coordonner et de réduire l’incertitude : la grande entreprise "
    "devient plus efficiente que la seule coordination marchande."),
   ("L’adaptation des structures à la complexité",
    "La forme unitaire centralise par fonctions, la forme multidivisionnelle "
    "décentralise en unités autonomes sous une direction stratégique "
    "centrale : cette dernière permet de gérer des entreprises complexes et "
    "diversifiées.")],
  [{'a': "La gouvernance managériale favorise la stabilité, l’innovation et "
         "la planification de long terme, parce que les dirigeants ne sont "
         "pas soumis à une exigence de rendement immédiat.",
    'cond': "L’avantage suppose que les managers poursuivent effectivement la "
            "croissance et l’organisation efficace de l’entreprise.",
    'lim': "La théorie de l’agence objecte qu’ils peuvent maximiser leur "
           "pouvoir, leur rémunération ou la taille de la firme plutôt que le "
           "profit des propriétaires."},
   {'a': "L’argument de Chandler est historique et non seulement théorique : "
         "la grande firme intégrée explique le succès de l’économie "
         "américaine après 1840.",
    'cond': "Il suppose des marchés suffisamment vastes pour que les "
            "économies d’échelle et l’intégration soient rentables.",
    'lim': "Le cours montre que les petites et moyennes entreprises et les "
           "firmes-réseaux n’ont pas disparu, ce qui interdit de conclure à "
           "la supériorité générale de la grande firme intégrée."},
   {'a': "La professionnalisation de la direction améliore la qualité des "
         "décisions, puisqu’elle substitue des compétences spécialisées à "
         "l’intuition du propriétaire.",
    'cond': "Elle exige que la gestion soit rationalisable autour de "
            "fonctions précises, comme l’établit Fayol en 1916.",
    'lim': "Cette rationalisation peut produire une bureaucratisation, dont "
           "Crozier montre qu’elle engendre rigidité et cercle vicieux "
           "bureaucratique."},
   {'a': "La forme multidivisionnelle résout un problème réel : diriger une "
         "entreprise diversifiée sans paralyser la décision locale.",
    'cond': "Elle suppose que les divisions puissent être évaluées "
            "séparément, par produit ou par zone géographique.",
    'lim': "La décentralisation crée autant de relations d’agence internes "
           "qu’il y a de divisions, chacune reproduisant le problème de "
           "contrôle à un niveau inférieur."}],
  [{'t': "La main visible de la gestion remplace la main invisible des forces "
         "du marché dans la coordination des flux de marchandises.",
    'qui': "Alfred Chandler, dans La main visible des managers, en 1977.",
    'rep': "La thèse explique la supériorité historique de la grande firme "
           "intégrée, mais le cours rappelle que les petites et moyennes "
           "entreprises, les firmes-réseaux et les districts industriels "
           "coexistent durablement avec elle."},
   {'t': "Le pouvoir appartient aux experts et non aux propriétaires, parce "
         "que la maîtrise de l’information devient la véritable source du "
         "pouvoir.",
    'qui': "John Kenneth Galbraith, avec la technostructure.",
    'rep': "L’analyse décrit bien la période managériale, mais la "
           "financiarisation des années 1970-1980 réduit l’avantage "
           "informationnel des managers et permet aux actionnaires de "
           "reprendre le contrôle."},
   {'t': "Les managers, libérés de la pression des propriétaires, "
         "privilégient la croissance de long terme et la stabilité de "
         "l’entreprise.",
    'qui': "La lecture managériale de la gouvernance, que le cours présente "
           "comme un avantage du régime.",
    'rep': "Jensen et Meckling répondent que cette autonomie permet "
           "précisément aux dirigeants de poursuivre leurs objectifs propres, "
           "d’où la nécessité de dispositifs de contrôle et d’incitation."}],
  [{'n': "Alfred Chandler",
    'i': "Le succès de l’économie américaine après 1840 vient de sa capacité "
         "à développer de grandes firmes intégrées.",
    'p': "Dans La main visible des managers, en 1977, il montre que la grande "
         "entreprise est efficiente parce qu’elle réalise des économies "
         "d’échelle, s’appuie sur la division du travail et fait appel aux "
         "managers pour coordonner les activités en dehors du marché."},
   {'n': "Alfred Chandler",
    'i': "La grande entreprise adopte soit une forme unitaire, soit une forme "
         "multidivisionnelle.",
    'p': "Le cours précise la distinction : la forme unitaire est une "
         "organisation centralisée structurée par fonctions, production, "
         "finance et autres ; la forme multidivisionnelle est décentralisée en "
         "unités autonomes par produit ou par zone, avec une direction "
         "stratégique centrale."},
   {'n': "John Kenneth Galbraith",
    'i': "La technostructure détient le pouvoir réel parce qu’elle maîtrise "
         "les connaissances nécessaires à la décision.",
    'p': "Dans Le Nouvel État industriel, en 1967, il désigne par ce terme "
         "l’ensemble des dirigeants, cadres, ingénieurs et experts qui "
         "participent à la direction effective : les grandes entreprises sont "
         "devenues trop complexes pour être contrôlées par les actionnaires."},
   {'n': "Adam Smith",
    'i': "La coordination des activités économiques est assurée par la main "
         "invisible du marché.",
    'p': "Le cours mobilise cette référence comme terme de comparaison : "
         "c’est à cette main invisible que Chandler oppose explicitement la "
         "main visible des managers, les grandes firmes coordonnant "
         "directement l’activité au lieu de passer par les prix."}],
  [{'f': "Chandler, historien de l’économie, appuie son analyse sur "
         "l’expérience américaine postérieure à 1840 et sur le développement "
         "de firmes intégrées verticalement et horizontalement.",
    'p': "L’ancrage historique montre que le capitalisme managérial n’est pas "
         "une construction théorique mais une transformation observée des "
         "structures productives."},
   {'f': "Le cours relève que les managers cherchent la croissance de long "
         "terme, la stabilité, l’innovation et une organisation efficace.",
    'p': "Cet énoncé des objectifs managériaux fournit le point de comparaison "
         "avec le régime suivant, où la rentabilité financière et la "
         "performance boursière deviennent prioritaires."},
   {'f': "La montée des managers s’accompagne du développement des écoles de "
         "commerce et de formations dédiées à la gestion.",
    'p': "L’institutionnalisation de la formation démontre que la direction "
         "d’entreprise est devenue un métier, condition sociale de la "
         "séparation entre propriété et contrôle."}],
  [{'q': "La grande entreprise est-elle plus efficace que le marché ?",
    'f': "Chandler soutient qu’elle l’est, et son argument est précis : la "
         "grande firme réalise des économies d’échelle, s’appuie sur la "
         "division du travail et fait appel aux managers pour coordonner les "
         "activités en dehors du marché, si bien que la main visible de la "
         "gestion remplace la main invisible des forces du marché dans la "
         "coordination des flux de marchandises.",
    'r': "Le raisonnement compare deux modes de coordination sur le même "
         "critère, le coût de l’organisation des flux, et conclut à la "
         "supériorité administrative dans les activités de grande échelle.",
    'ex': "Chandler établit ce résultat à partir de l’économie américaine "
          "postérieure à 1840."},
   {'q': "Sur quoi repose le pouvoir des managers ?",
    'f': "Deux réponses se complètent. Berle et Means l’attribuent en 1932 à "
         "la dispersion du capital, qui prive les actionnaires du temps, des "
         "compétences et de l’information nécessaires. Galbraith y ajoute en "
         "1967 un fondement positif : la technostructure détient le pouvoir "
         "parce qu’elle maîtrise les connaissances nécessaires à la décision.",
    'r': "On distingue une cause négative, l’incapacité des propriétaires, "
         "d’une cause positive, la compétence des dirigeants, et l’on montre "
         "que seule la seconde explique la durée du régime.",
    'ex': "La technostructure réunit dirigeants, cadres, ingénieurs et "
          "experts selon le cours."},
   {'q': "Pourquoi le capitalisme managérial a-t-il décliné ?",
    'f': "Son fondement était un avantage informationnel sur des "
         "actionnaires dispersés. Or à partir des années 1970-1980, le "
         "développement des marchés financiers, la mondialisation et la "
         "libéralisation renforcent les investisseurs : les actionnaires "
         "reprennent du pouvoir et imposent, par la corporate governance, une "
         "discipline aux dirigeants.",
    'r': "Le raisonnement identifie la condition d’existence du régime, puis "
         "montre que sa disparition suffit à expliquer le basculement vers le "
         "capitalisme actionnarial.",
    'ex': "Bourguinat résume cette transformation par la désintermédiation, "
          "le décloisonnement et la déréglementation."}],
  voisins=['n8-propriete-controle', 'n8-capitalisme-actionnarial',
           'n8-capitalisme-entrepreneurial', 'n8-gouvernance'])


d('n8-capitalisme-actionnarial', 8, "Capitalisme actionnarial",
  "Quand les actionnaires reprennent le contrôle",
  "Le capitalisme actionnarial désigne la forme de gouvernance qui s’impose à "
  "partir des années 1970-1980, dans laquelle les actionnaires reprennent le "
  "pouvoir et recentrent l’entreprise sur la création de valeur pour "
  "l’actionnaire. Le cours le définit par un double mouvement : la "
  "financiarisation, qui renforce les investisseurs, et la corporate "
  "governance, qui encadre l’action des managers.",
  "Le capitalisme actionnarial est le troisième régime du chapitre, et le "
  "cours en expose le contexte, le mécanisme, la justification théorique et la "
  "contestation. Le contexte est financier : le développement des marchés "
  "financiers, la mondialisation et la libéralisation économique renforcent le "
  "rôle des investisseurs, et Henri Bourguinat résume la transformation par "
  "trois dynamiques, la désintermédiation, le décloisonnement et la "
  "déréglementation, qui permettent aux entreprises d’accéder directement aux "
  "marchés financiers et les en rendent dépendantes. De nouveaux acteurs "
  "prennent une place centrale, fonds d’investissement, private equity, "
  "investisseurs institutionnels, et exercent une pression forte pour "
  "améliorer la rentabilité financière. Le mécanisme est disciplinaire : un "
  "ensemble de dispositifs regroupés sous le terme de corporate governance "
  "vise à contrôler les dirigeants et à aligner leurs décisions sur les "
  "intérêts des actionnaires, logique théorisée par Jensen et Meckling à "
  "travers la théorie de l’agence, avec des dispositifs de contrôle, conseil "
  "d’administration et audit, et des dispositifs d’incitation, stock-options "
  "et rémunérations variables. La justification théorique est celle de Milton "
  "Friedman qui soutient, dans The Social Responsibility of Business is to "
  "Increase its Profits, en 1970, que la seule responsabilité de l’entreprise "
  "est de maximiser le profit pour les actionnaires, les dimensions sociales "
  "et environnementales étant secondaires. Les effets observés sont précis : "
  "restructurations, réduction des coûts, licenciements, distribution accrue "
  "de dividendes, hausse des rémunérations des dirigeants liées à la "
  "performance boursière. La contestation porte sur trois points : la logique "
  "de court terme, les dérives dont le scandale Enron en 2001 est l’exemple, "
  "et la hausse des inégalités que Nicholas Bloom documente en 2017. Le cours "
  "conclut que la gouvernance évolue vers un modèle hybride, qui intègre les "
  "parties prenantes.",
  [("La libéralisation financière",
    "La désintermédiation, le décloisonnement et la déréglementation "
    "permettent aux entreprises d’accéder directement aux marchés financiers, "
    "ce qui les rend dépendantes des investisseurs et donne à ces derniers un "
    "moyen de pression."),
   ("La concentration de l’actionnariat institutionnel",
    "Fonds d’investissement, private equity et investisseurs institutionnels "
    "remplacent les actionnaires dispersés de Berle et Means : ils disposent "
    "des moyens d’analyse et du poids nécessaires pour imposer des exigences "
    "aux dirigeants."),
   ("La discipline par la gouvernance",
    "Conseil d’administration, audit et contrôle des performances réduisent "
    "l’asymétrie d’information, tandis que stock-options et rémunérations "
    "variables lient le revenu du dirigeant au cours de l’action : "
    "l’autonomie managériale est encadrée."),
   ("Le recentrage sur la valeur actionnariale",
    "Les décisions sont orientées vers la rentabilité financière : "
    "restructurations, réduction des coûts, licenciements et distribution "
    "accrue de dividendes deviennent les instruments ordinaires de la "
    "création de valeur pour l’actionnaire."),
   ("Le raccourcissement de l’horizon",
    "La pression pour une hausse rapide de la valeur boursière et une "
    "rentabilité immédiate favorise une vision court-termiste, qui sacrifie "
    "les dépenses dont le rendement est lointain, notamment l’investissement "
    "et la formation.")],
  [{'a': "La gouvernance actionnariale résout un problème réel, celui de "
         "l’absence de contrôle des dirigeants dans le capitalisme "
         "managérial.",
    'cond': "Elle suppose des organes de contrôle indépendants et une "
            "information comptable fiable, conditions qui définissent la "
            "qualité de la gouvernance.",
    'lim': "Le scandale Enron, en 2001, montre que ces conditions peuvent "
           "être détruites de l’intérieur par des manipulations comptables."},
   {'a': "Assigner un objectif unique aux dirigeants rend leur performance "
         "mesurable et leur responsabilité identifiable.",
    'cond': "L’indicateur retenu, le cours de l’action, doit refléter la "
            "performance réelle attribuable au dirigeant.",
    'lim': "Un indicateur boursier est sensible au court terme et "
           "manipulable, ce qui oriente les décisions vers la performance "
           "immédiate plutôt que vers la valeur durable."},
   {'a': "La pression des investisseurs impose une discipline de coûts qui "
         "peut corriger des gestions laxistes héritées du régime managérial.",
    'cond': "Le gain d’efficacité suppose que les coûts supprimés "
    "soient " "effectivement improductifs et non des dépenses dont le "
    "rendement " "est simplement plus lointain.",
    'lim': "Le cours montre que cette logique se traduit aussi par des "
           "restructurations et des licenciements, donc par un transfert de "
           "risque vers les salariés plutôt que par un gain d’efficacité."},
   {'a': "La financiarisation élargit l’accès des entreprises aux capitaux et "
         "lève une contrainte de financement.",
    'cond': "Elle exige des marchés financiers profonds et des entreprises "
            "capables d’y accéder, ce qui favorise les grandes firmes.",
    'lim': "Cette dépendance aux marchés rend l’entreprise vulnérable aux "
           "exigences de rentabilité et aux retournements financiers, et "
           "soumet ses décisions à un horizon qui n’est pas le sien."}],
  [{'t': "La seule responsabilité sociale de l’entreprise est de maximiser le "
         "profit pour ses actionnaires, les autres dimensions étant "
         "secondaires.",
    'qui': "Milton Friedman, en 1970, dans l’article qui fonde la légitimité "
           "du modèle actionnarial.",
    'rep': "Le cours oppose à cette position l’approche des parties "
           "prenantes, qui intègre salariés, clients, fournisseurs, État et "
           "environnement, et les analyses de Polanyi sur l’encastrement de "
           "l’économie dans la société."},
   {'t': "Les dispositifs d’incitation alignent les intérêts des dirigeants "
         "sur ceux des actionnaires sans contrepartie sociale négative.",
    'qui': "La logique de la corporate governance des années 1990.",
    'rep': "Nicholas Bloom montre en 2017 que ces incitations s’ajoutent à la "
           "rémunération des managers et nourrissent des écarts de revenus "
           "croissants entre entreprises américaines."},
   {'t': "La discipline des marchés financiers améliore la gestion des "
         "entreprises en sanctionnant les dirigeants inefficaces.",
    'qui': "La justification économique du capitalisme actionnarial.",
    'rep': "Le cours objecte que cette discipline favorise une logique de "
           "court terme, centrée sur la performance financière immédiate, et "
           "qu’elle peut conduire à des dérives spectaculaires comme Enron."}],
  [{'n': "Henri Bourguinat",
    'i': "La transformation financière des années 1970-1980 repose sur trois "
         "dynamiques : désintermédiation, décloisonnement, déréglementation.",
    'p': "Le cours fait de ces trois dynamiques, qu’il appelle les trois D, la "
         "condition du capitalisme actionnarial : elles permettent aux "
         "entreprises d’accéder directement aux marchés financiers et les en "
         "rendent dépendantes, ce qui donne aux investisseurs un pouvoir de "
         "pression."},
   {'n': "Milton Friedman",
    'i': "La seule responsabilité de l’entreprise est de maximiser le profit "
         "pour ses actionnaires.",
    'p': "Dans The Social Responsibility of Business is to Increase its "
         "Profits, en 1970, il fait de l’entreprise un instrument au service "
         "des actionnaires et considère les dimensions sociales et "
         "environnementales comme secondaires, ce qui légitime la priorité "
         "donnée à la rentabilité financière."},
   {'n': "Michael Jensen",
    'i': "La relation entre actionnaires et managers est une relation "
         "d’agence marquée par la divergence d’intérêts et l’asymétrie "
         "d’information.",
    'p': "Avec William Meckling, il fournit le support théorique de la "
         "corporate governance : puisque les managers disposent "
         "d’informations supérieures et peuvent poursuivre leurs propres "
         "objectifs, le principal doit mettre en place contrôle et "
         "incitations."},
   {'n': "Nicholas Bloom",
    'i': "Les écarts de revenus restent constants au sein des entreprises "
         "mais croissent entre les entreprises.",
    'p': "Dans Corporations in the Age of Inequality, paru dans la Harvard "
         "Business Review en 2017, il montre que la gouvernance actionnariale "
         "ne redistribue pas seulement le pouvoir : elle transforme la "
         "structure des inégalités salariales entre firmes."}],
  [{'f': "De nouveaux acteurs prennent une place centrale à partir des années "
         "1970-1980 : fonds d’investissement, private equity, investisseurs "
         "institutionnels.",
    'p': "Leur apparition montre que le retour du pouvoir actionnarial "
         "n’est pas idéologique mais structurel : il suppose des acteurs "
         "capables d’analyser et de peser sur les dirigeants."},
   {'f': "La logique actionnariale se traduit par des restructurations, une "
         "réduction des coûts, des licenciements et une distribution accrue de "
         "dividendes.",
    'p': "L’énumération montre que la création de valeur pour l’actionnaire "
         "n’est pas une abstraction comptable : elle se lit dans des "
         "décisions dont les effets sociaux sont immédiats."},
   {'f': "Le scandale Enron, en 2001, est marqué par des manipulations "
         "comptables et une faillite retentissante.",
    'p': "Le cas démontre que la gouvernance actionnariale peut produire des "
         "dérives graves, puisque la pression sur les résultats incite à "
         "travestir l’information sur laquelle le contrôle repose."}],
  [{'q': "Les intérêts des actionnaires et des salariés sont-ils compatibles ?",
    'f': "Dans le modèle actionnarial, la réponse est négative à court terme : "
         "la création de valeur pour l’actionnaire passe par des "
         "restructurations, des réductions de coûts et des licenciements, "
         "c’est-à-dire par un transfert de risque vers les salariés. "
         "L’approche des parties prenantes propose de réintégrer leurs "
         "intérêts dans la gouvernance, ce qui conduit à un modèle hybride.",
    'r': "On montre que l’incompatibilité ne tient pas à une opposition de "
         "principe mais au choix d’un critère unique de décision, ce qui "
         "ouvre la possibilité d’une gouvernance élargie.",
    'ex': "Le cours relève la pression accrue sur les salariés comme l’une "
          "des critiques du capitalisme actionnarial."},
   {'q': "Le capitalisme actionnarial a-t-il amélioré la gouvernance ?",
    'f': "Il répond à un problème réel, celui de l’autonomie excessive des "
         "managers dans le régime précédent, et il fournit des instruments "
         "précis, contrôle et incitation. Mais le cours montre que ces "
         "instruments produisent trois effets non voulus : court-termisme, "
         "dérives comptables et hausse des inégalités de rémunération.",
    'r': "Le raisonnement juge le régime sur ses propres objectifs, puis sur "
         "ses effets observés, ce qui permet de conclure à une correction "
         "partielle accompagnée de nouveaux coûts.",
    'ex': "Enron en 2001 pour les dérives, Bloom en 2017 pour les "
          "inégalités."},
   {'q': "La gouvernance d’entreprise est-elle devenue hybride ?",
    'f': "Le cours conclut en ce sens : le capitalisme contemporain est "
         "marqué par une tension entre une logique actionnariale centrée sur "
         "la rentabilité et une logique élargie intégrant les parties "
         "prenantes, de sorte que la gouvernance évolue vers un modèle "
         "hybride et que l’entreprise devient un acteur économique, social et "
         "environnemental.",
    'r': "On montre que les deux logiques ne se succèdent pas mais "
         "coexistent, chacune corrigeant les excès de l’autre, ce qui "
         "explique la forme composite des gouvernances actuelles.",
    'ex': "La loi PACTE de 2019 introduit la raison d’être et le statut "
          "d’entreprise à mission."}],
  voisins=['n8-capitalisme-managerial', 'n8-valeur-actionnariale',
           'n8-financiarisation', 'n8-parties-prenantes'],
  comp={'titre': "Capitalisme managérial et capitalisme actionnarial",
        'a': "Capitalisme managérial",
        'b': "Capitalisme actionnarial",
        'lignes': [
          ("Période", "Des grandes firmes intégrées de l’après-1840 jusqu’aux "
           "années 1970", "À partir des années 1970-1980, avec la "
           "libéralisation financière"),
          ("Détenteur du pouvoir effectif", "Les managers, puis la "
           "technostructure décrite par Galbraith", "Les actionnaires, "
           "relayés par les fonds et les investisseurs institutionnels"),
          ("Source du pouvoir", "La maîtrise de l’information et des "
           "compétences nécessaires à la décision", "La dépendance de "
           "l’entreprise aux marchés financiers pour son financement"),
          ("Objectif assigné", "Croissance de long terme, stabilité, "
           "innovation, organisation efficace", "Rentabilité financière, "
           "rendement pour l’actionnaire, performance boursière"),
          ("Référence théorique", "Berle et Means en 1932, Galbraith en 1967, "
           "Chandler en 1977", "Jensen et Meckling en 1976, Friedman en "
           "1970"),
          ("Instruments de gouvernance", "Organisation interne, formes "
           "unitaire et multidivisionnelle, planification",
           "Conseil d’administration, audit, stock-options, rémunérations "
           "variables"),
          ("Mode de coordination", "La main visible des managers remplace "
           "partiellement le marché", "La discipline des marchés financiers "
           "s’impose à la direction"),
          ("Horizon des décisions", "Long terme, compatible avec "
           "l’investissement et l’innovation", "Court terme, orienté vers la "
           "hausse rapide de la valeur boursière"),
          ("Effets sociaux", "Stabilité de l’emploi dans la grande firme "
           "intégrée", "Restructurations, licenciements, dividendes accrus, "
           "écarts de rémunération"),
          ("Limite principale", "Aucun contrôle effectif des dirigeants par "
           "les propriétaires", "Court-termisme, dérives comptables comme "
           "Enron, inégalités documentées par Bloom")]})
