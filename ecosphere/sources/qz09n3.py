# -*- coding: utf-8 -*-
"""Chapitre 9 — questions nouvelles, sous-parties c9-08 à c9-11."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c9-08
f(id='q9-n43', sp='c9-08', niv='comprendre', type='qcm', b=1298,
  q="Dans la théorie néoclassique traditionnelle, quel est le personnage "
    "central de l’analyse de la production ?",
  opts=["L’entreprise considérée comme institution sociale",
        "Le producteur, qui combine les facteurs de production",
        "L’entrepreneur innovateur",
        "Le manager salarié"],
  ans=1,
  why=["C’est précisément ce que la théorie standard n’étudie pas : "
       "l’entreprise comme organisation.",
       "L’entrepreneur innovateur est le personnage de Schumpeter, pas de la "
       "théorie standard.",
       "Le manager salarié apparaît avec le capitalisme managérial et la "
       "théorie de l’agence."],
  exp="Dans la théorie néoclassique classique, l’entreprise n’est pas "
      "vraiment étudiée comme organisation : ce qui compte, c’est le "
      "producteur. La théorie raisonne sur des comportements individuels et "
      "non sur l’entreprise comme institution sociale. Le producteur loue les "
      "services du travail, rémunère les détenteurs du capital et combine les "
      "facteurs — sans être nécessairement propriétaire des moyens de "
      "production.",
  diss="Point de départ indispensable : si la firme n’est qu’un producteur "
       "qui réagit aux prix, toute la partie sur les théories de la firme "
       "consiste à expliquer ce que cette représentation laisse de côté."),

f(id='q9-n44', sp='c9-08', niv='connaitre', type='qcmm', b=1319,
  q="Quelles hypothèses la théorie néoclassique de la firme retient-elle ? "
    "(plusieurs réponses)",
  opts=["La rationalité des agents, qui calculent, anticipent et cherchent "
        "leur intérêt personnel",
        "Les productivités marginales décroissantes",
        "La concurrence pure et parfaite, où les entreprises sont price "
        "takers",
        "L’atomicité du marché : une multitude d’entreprises dont aucune ne "
        "peut le contrôler seule",
        "La rationalité limitée des agents"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est l’hypothèse de comportement de la théorie standard.",
       "Exacte : le gain supplémentaire finit par diminuer quand on ajoute du "
       "travail ou du capital.",
       "Exacte : les entreprises n’ont aucun pouvoir sur les prix.",
       "Exacte : l’atomicité interdit toute domination individuelle.",
       "La rationalité limitée est l’hypothèse d’Herbert Simon, reprise par "
       "Williamson contre la théorie standard."],
  exp="Ces hypothèses ont une conséquence fondamentale : la firme est "
      "totalement soumise au marché. Elle réagit aux prix, aux quantités, aux "
      "signaux du marché — si les prix augmentent, elle produit plus ; si les "
      "coûts augmentent, elle produit moins. La théorie standard donne ainsi "
      "l’image d’une entreprise « automate »."),

f(id='q9-n45', sp='c9-08', niv='raisonner', type='qcm', b=1353,
  q="Quelle contradiction empirique la vision néoclassique traditionnelle de "
    "la firme rencontre-t-elle ?",
  opts=["Les entreprises réagissent trop lentement aux variations de prix",
        "L’atomicité suppose qu’aucune entreprise ne domine, alors que la "
        "réalité montre des multinationales, de grandes firmes et des "
        "concentrations",
        "Les productivités marginales sont en réalité croissantes",
        "Les entreprises ne cherchent pas le profit"],
  ans=1,
  why=["La vitesse de réaction n’est pas le problème soulevé par le cours.",
       "Le cours ne remet pas en cause la décroissance des productivités "
       "marginales.",
       "La recherche du profit n’est pas contestée ici : elle est au "
       "contraire discutée dans la conclusion du chapitre."],
  exp="Dans la concurrence pure et parfaite, aucune entreprise ne devrait "
      "avoir un pouvoir important, puisque l’atomicité suppose beaucoup "
      "d’entreprises et aucune domination individuelle. Or la réalité montre "
      "des multinationales, des grandes firmes, des concentrations et des "
      "groupes géants. D’où les questions nouvelles : pourquoi les entreprises "
      "deviennent-elles grandes ? Pourquoi salarier durablement des "
      "travailleurs, créer des équipes permanentes, intégrer des activités ?",
  diss="C’est cette contradiction qui ouvre tout le programme des théories de "
       "la firme : Coase, Williamson, Alchian et Demsetz, Jensen et Meckling."),

f(id='q9-n46', sp='c9-08', niv='comprendre', type='qcm', b=1376,
  q="Pourquoi le travail en équipe pousse-t-il, selon le cours, au "
    "développement des entreprises ?",
  opts=["Parce que le travail collectif est moins productif que le travail "
        "individuel",
        "Parce que certaines activités nécessitent une coordination "
        "permanente, ce qui pousse à constituer des équipes stables",
        "Parce que la loi impose un nombre minimal de salariés",
        "Parce que les salariés exigent des contrats à durée indéterminée"],
  ans=1,
  why=["Le cours dit l’inverse : le travail collectif est nécessaire à "
       "certaines productions.",
       "Aucune obligation légale de ce type n’est évoquée.",
       "Les revendications salariales ne sont pas l’argument employé ici."],
  exp="Certaines activités nécessitent une coordination permanente : "
      "l’exemple du cours est l’entreprise de déménagement, qui suppose "
      "coordination, confiance et habitudes communes. Le travail collectif "
      "pousse donc à constituer des équipes stables, donc à développer des "
      "entreprises durables plutôt qu’à recourir à des contrats ponctuels sur "
      "le marché.",
  diss="Argument simple et efficace : la firme existe parce que certaines "
       "productions exigent de travailler ensemble de façon répétée."),

f(id='q9-n47', sp='c9-08', niv='comprendre', type='qcm', b=1406,
  q="Pour les auteurs de l’approche contractuelle, quelle est la seule "
    "différence entre le marché et la firme ?",
  opts=["Le marché repose sur des contrats, la firme sur l’autorité",
        "Le marché mobilise des contrats commerciaux, la firme des contrats "
        "commerciaux et des contrats de travail, mais la nature des relations "
        "économiques reste la même",
        "Le marché est rationnel, la firme ne l’est pas",
        "Le marché est public, la firme est privée"],
  ans=1,
  why=["L’opposition contrats / autorité est celle de Coase, c’est-à-dire de "
       "l’approche transactionnelle.",
       "Les deux approches supposent des individus rationnels : ce n’est pas "
       "le critère de distinction.",
       "Marché et firme sont l’un comme l’autre des institutions de "
       "l’économie privée."],
  exp="Marché et firme reposent tous deux sur des contrats passés entre "
      "individus rationnels. Le marché mobilise des contrats commerciaux, la "
      "firme y ajoute des contrats de travail. Mais pour ces auteurs, cela ne "
      "change pas la nature des relations économiques : dans les deux cas, "
      "des individus rationnels passent des accords. D’où la formule du "
      "cours : firme ≈ marché.",
  diss="C’est exactement ce que Coase et Williamson refusent : pour eux, "
       "l’autorité hiérarchique change la nature de la coordination."),

f(id='q9-n48', sp='c9-08', niv='comprendre', type='qcm', b=1419,
  q="Quels avantages le cours attribue-t-il à l’externalisation ?",
  opts=["Elle garantit une qualité de service supérieure",
        "Elle permet de déléguer le recrutement, la formation, le "
        "remplacement des salariés et la gestion des absences et des congés, "
        "donc de réduire la charge administrative",
        "Elle supprime tout coût de transaction",
        "Elle donne à l’entreprise le pouvoir de modifier librement les "
        "tâches du personnel du prestataire"],
  ans=1,
  why=["Le cours n’affirme nulle part une qualité supérieure : il souligne au "
       "contraire les limites du contrat.",
       "L’externalisation crée des coûts de transaction : négociation, "
       "contrôle, renégociation.",
       "C’est précisément l’inverse : seule la subordination salariale permet "
       "à l’employeur de modifier les tâches."],
  exp="En externalisant, l’entreprise délègue le recrutement, la formation, "
      "le remplacement des salariés, la gestion des absences et des congés. "
      "Si le salarié du prestataire est malade, c’est à la société "
      "prestataire de le remplacer. Le résultat est une moindre charge "
      "administrative — mais au prix d’une perte de souplesse dans la "
      "définition des tâches.",
  diss="La question « faire ou faire faire » est la formulation la plus "
       "concrète de l’arbitrage firme / marché."),

f(id='q9-n49', sp='c9-08', niv='appliquer', type='qcm', b=1431,
  q="Un contrat de nettoyage prévoit le lavage des vitres une fois par mois. "
    "Les vitres deviennent soudain très sales. Que montre cet exemple ?",
  opts=["Que le contrat est toujours plus efficace que la hiérarchie",
        "Que le contrat ne peut pas tout prévoir : il faut renégocier et "
        "payer davantage, alors que dans une entreprise intégrée l’employeur "
        "peut modifier les tâches du salarié subordonné",
        "Que l’externalisation supprime les coûts de transaction",
        "Que le prestataire est nécessairement opportuniste"],
  ans=1,
  why=["L’exemple montre exactement le contraire : la limite du contrat face "
       "à l’imprévu.",
       "L’externalisation déplace les coûts de transaction, elle ne les "
       "supprime pas.",
       "L’exemple ne suppose aucune mauvaise foi : il suffit que l’événement "
       "n’ait pas été prévu."],
  exp="L’exemple illustre l’incomplétude des contrats : ce qui n’est pas "
      "prévu doit être renégocié, et la renégociation a un coût. Dans "
      "l’entreprise intégrée, le salarié étant subordonné, l’employeur peut "
      "modifier les tâches sans renégocier. C’est l’avantage de l’autorité "
      "hiérarchique sur le contrat marchand — le cœur de l’argument de Coase "
      "et de Williamson.",
  diss="Exemple très économique à citer : il résume en trois lignes pourquoi "
       "la firme existe."),

f(id='q9-n50', sp='c9-08', niv='comprendre', type='qcmm', b=1447,
  q="Quels coûts l’emploi direct de salariés implique-t-il, et comment le "
    "cours les qualifie-t-il ? (plusieurs réponses)",
  opts=["Les salaires et les cotisations sociales",
        "La retraite, les congés payés et la formation",
        "Le recrutement et le contrôle",
        "Tous ces coûts liés à l’embauche, au contrôle, aux contrats et à "
        "l’organisation sont des coûts de transaction",
        "Ces coûts sont nuls dans une entreprise intégrée"],
  ans=[0, 1, 2, 3],
  why=["Exacte : ce sont les coûts directs de l’emploi.",
       "Exacte : la protection sociale et la formation s’y ajoutent.",
       "Exacte : trouver et surveiller les salariés coûte aussi.",
       "Exacte : c’est la qualification que retient le cours, et c’est elle "
       "qui permet le raisonnement de Williamson.",
       "Faux : c’est précisément l’existence de ces coûts qui rend "
       "l’internalisation parfois moins avantageuse que le marché."],
  exp="L’intérêt de la démonstration est de montrer que l’internalisation "
      "n’est pas gratuite : employer directement coûte, et ces coûts "
      "d’organisation sont eux aussi des coûts de transaction. C’est "
      "précisément cette idée que Williamson développe : le choix entre "
      "marché et firme dépend de la comparaison des coûts de transaction de "
      "part et d’autre."),

f(id='q9-n51', sp='c9-08', niv='raisonner', type='qcm', b=1465,
  q="Quels prolongements modernes le cours ajoute-t-il à l’analyse "
    "contractuelle de la firme ?",
  opts=["Les contrats deviennent de plus en plus formels et complets",
        "Toutes les relations ne sont pas formelles : la confiance, les "
        "habitudes et les routines comptent aussi, ce qui rejoint l’analyse "
        "des institutions de Douglas North",
        "Les routines disparaissent avec l’informatisation",
        "Les relations informelles sont toujours source d’inefficacité"],
  ans=1,
  why=["Le cours soutient l’inverse : l’incomplétude des contrats est "
       "irréductible.",
       "Les routines sont au contraire présentées comme un mode de "
       "fonctionnement durable des entreprises.",
       "Rien de tel n’est affirmé : la confiance est présentée comme un "
       "facteur de stabilité."],
  exp="Une entreprise garde parfois un fournisseur non parce qu’il est le "
      "moins cher, mais parce qu’il est fiable, connu, jugé honnête. Les "
      "entreprises fonctionnent aussi grâce aux habitudes, aux routines et "
      "aux relations informelles. Le cours relie ce constat à Douglas North : "
      "les institutions reposent sur des règles formelles et informelles.",
  diss="Ce prolongement nuance les deux approches : la coordination ne passe "
       "ni uniquement par les prix, ni uniquement par le contrat ou "
       "l’autorité."),

# ------------------------------------------------------------- c9-09
f(id='q9-n52', sp='c9-09', niv='comprendre', type='qcm', b=1522,
  q="Selon quel critère le cours juge-t-il qu’une entreprise dominante ne "
    "pose pas problème ?",
  opts=["Lorsqu’elle détient moins de 50 % du marché",
        "Lorsqu’elle se comporte comme si elle était en concurrence : sans "
        "augmenter artificiellement les prix, restreindre volontairement les "
        "quantités ni bloquer ses concurrents",
        "Lorsqu’elle est contrôlée par l’État",
        "Lorsqu’elle réalise des bénéfices modérés"],
  ans=1,
  why=["Aucun seuil de part de marché n’est donné par le cours comme critère "
       "de licéité.",
       "Le statut public n’exonère pas du droit de la concurrence : les aides "
       "d’État sont même surveillées.",
       "Le niveau de profit n’est pas en soi le critère : c’est le "
       "comportement qui compte."],
  exp="La position dominante peut résulter d’une réussite économique : "
      "innovation, baisse des coûts, satisfaction des consommateurs. Elle "
      "n’est donc pas condamnée. Le critère retenu est comportemental : "
      "l’entreprise dominante ne doit pas se servir de sa position pour "
      "fausser le jeu concurrentiel. C’est l’abus, et non la domination, que "
      "sanctionne l’article 102 du TFUE.",
  diss="Formule à retenir : ce n’est pas la puissance qui est illicite, c’est "
       "l’usage de la puissance pour fermer le marché."),

f(id='q9-n53', sp='c9-09', niv='raisonner', type='qcm', b=1555,
  q="Pourquoi la vente liée n’est-elle pas condamnée en elle-même ?",
  opts=["Parce qu’elle fait toujours baisser les prix",
        "Parce qu’elle est souvent pratique pour le consommateur — une "
        "voiture avec ses pneus, un ordinateur avec son système "
        "d’exploitation —, et ne devient anticoncurrentielle que lorsqu’elle "
        "empêche les concurrents de proposer leurs produits",
        "Parce qu’elle relève du droit de la consommation et non du droit de "
        "la concurrence",
        "Parce qu’elle ne concerne que les entreprises non dominantes"],
  ans=1,
  why=["Rien n’indique un effet systématique à la baisse sur les prix.",
       "La vente liée par une entreprise dominante relève bien du droit de la "
       "concurrence : Microsoft et Google ont été poursuivis.",
       "C’est au contraire la domination qui rend la pratique dangereuse."],
  exp="La vente liée consiste à vendre plusieurs produits ensemble en "
      "empêchant le consommateur de les acheter séparément. Dans beaucoup de "
      "cas, elle est pratique : acheter une voiture déjà équipée de pneus, un "
      "ordinateur avec un système d’exploitation, un téléphone avec des "
      "applications de base. Le problème apparaît quand une entreprise "
      "dominante utilise un produit incontournable pour imposer un autre "
      "produit et fermer l’accès au marché — accusations portées contre "
      "Microsoft et Google.",
  diss="Toutes les pratiques de ce passage sont ambivalentes : c’est ce qui "
       "rend la politique de concurrence difficile et contestée."),

f(id='q9-n54', sp='c9-09', niv='raisonner', type='courte', b=1595,
  q="Pourquoi est-il difficile de prouver des prix prédateurs ?",
  ans={'modele': "Parce qu’une baisse de prix est en elle-même un acte de "
       "concurrence normal : une entreprise a le droit de baisser ses prix, "
       "par exemple lors d’une promotion, d’une baisse temporaire face à un "
       "nouveau concurrent ou d’une adaptation à une nouvelle structure de "
       "coûts. Ce qui est condamné, c’est la baisse durable destinée à "
       "exclure les concurrents : le cours donne comme indice un prix "
       "inférieur au coût variable moyen, puisqu’en dessous de ce seuil la "
       "baisse ne peut plus s’expliquer par une logique productive. "
       "L’ambiguïté est illustrée par la riposte des compagnies aériennes "
       "traditionnelles aux compagnies low-cost : la baisse de leurs prix a "
       "été considérée comme une réaction concurrentielle normale, non comme "
       "une pratique prédatrice. L’autorité doit donc établir à la fois le "
       "niveau de prix et l’intention d’éviction, ainsi que la capacité de "
       "l’entreprise à se refaire ensuite une fois les concurrents éliminés.",
       'cles': [{'f': ['droit de baisser', 'normal', 'promotion', 'concurrence'],
                 'l': 'baisser ses prix est un acte de concurrence licite'},
                {'f': ['cout variable moyen'],
                 'l': 'l’indice du prix inférieur au coût variable moyen'},
                {'f': ['durable', 'exclure', 'eliminer', 'intention'],
                 'l': 'ce qui est condamné est la baisse durable visant l’éviction'},
                {'f': ['low cost', 'aerien'],
                 'l': 'l’exemple des compagnies aériennes face aux low-cost'}]},
  exp="Le cours insiste sur cette difficulté : les prix prédateurs sont la "
      "pratique la plus ambiguë du chapitre, puisqu’ils prennent la forme "
      "même de la concurrence — un prix bas favorable au consommateur à court "
      "terme — tout en visant à le priver de concurrence à long terme."),

f(id='q9-n55', sp='c9-09', niv='appliquer', type='qcm', b=1651,
  q="Engie disposait d’un fichier client hérité de son ancien rôle "
    "historique dans l’énergie. Où le cours situe-t-il exactement le "
    "problème ?",
  opts=["Dans l’existence même du fichier client",
        "Dans le fait d’utiliser ce fichier sans le mettre à la disposition "
        "des concurrents alors que le marché avait été ouvert",
        "Dans la vente de ce fichier à des concurrents",
        "Dans l’absence de protection des données personnelles"],
  ans=1,
  why=["Le fichier est un actif légitime, hérité de l’histoire de "
       "l’entreprise.",
       "Le reproche n’est pas d’avoir cédé le fichier mais de ne pas l’avoir "
       "partagé.",
       "La question des données personnelles est traitée ailleurs, avec "
       "Cambridge Analytica."],
  exp="Certaines entreprises anciennement publiques conservent, lors de "
      "l’ouverture à la concurrence, des avantages historiques : fichier "
      "client, infrastructure, réputation, connaissance du marché, relation "
      "ancienne avec les consommateurs. L’exploitation devient "
      "anticoncurrentielle lorsque l’ancien monopole utilise seul des "
      "ressources issues de sa position historique pour empêcher les nouveaux "
      "concurrents de se développer.",
  diss="Cas précieux pour traiter des libéralisations : ouvrir juridiquement "
       "un marché ne suffit pas à le rendre contestable."),

# ------------------------------------------------------------- c9-10
f(id='q9-n56', sp='c9-10', niv='connaitre', type='qcmm', b=1661,
  q="Quelles sont les quatre grandes sources du pouvoir de marché "
    "identifiées par le cours ? (plusieurs réponses)",
  opts=["La concentration des entreprises",
        "La différenciation des produits",
        "Les ententes",
        "Les barrières à l’entrée",
        "L’optimisation fiscale"],
  ans=[0, 1, 2, 3],
  why=["Exacte : elle réduit le nombre d’acteurs et l’atomicité.",
       "Exacte : elle rompt l’homogénéité des produits supposée par la "
       "concurrence parfaite.",
       "Exacte : elles permettent à des firmes indépendantes de se comporter "
       "comme un monopole collectif.",
       "Exacte : elles protègent l’entreprise installée de la concurrence "
       "potentielle.",
       "L’optimisation fiscale est un danger de la concentration pour les "
       "finances publiques, pas une source de pouvoir de marché."],
  exp="Cette liste organise toute la suite du chapitre : la concentration a "
      "été étudiée dans les premières parties, la différenciation l’est ici, "
      "les ententes dans la partie sur les cartels, les barrières à l’entrée "
      "dans celle sur les marchés contestables.",
  diss="Plan tout fait pour une dissertation sur le pouvoir de marché : "
       "quatre sources, quatre types de réponses de la politique de "
       "concurrence."),

f(id='q9-n57', sp='c9-10', niv='comprendre', type='qcm', b=1677,
  q="En quoi la différenciation des produits remet-elle en cause une "
    "hypothèse de la concurrence pure et parfaite ?",
  opts=["Elle supprime l’atomicité du marché",
        "Elle rompt l’homogénéité supposée des produits et crée une "
        "préférence spécifique chez les consommateurs",
        "Elle supprime la libre entrée sur le marché",
        "Elle supprime la transparence de l’information"],
  ans=1,
  why=["L’atomicité est mise en cause par la concentration, pas par la "
       "différenciation : le nombre d’entreprises peut rester élevé.",
       "La libre entrée est mise en cause par les barrières à l’entrée.",
       "La transparence n’est pas l’hypothèse visée ici, même si la publicité "
       "peut l’affecter."],
  exp="La différenciation consiste à rendre un produit distinct aux yeux des "
      "consommateurs. Elle permet de rompre l’homogénéité supposée par la "
      "concurrence parfaite et de créer une préférence spécifique : le "
      "consommateur ne considère plus les produits comme interchangeables. "
      "C’est ce qui réduit la substituabilité, donc l’élasticité-prix de la "
      "demande, et confère un pouvoir de marché sans qu’il soit nécessaire de "
      "racheter des concurrents.",
  diss="Enchaînement complet à mémoriser : différenciation → fin de "
       "l’homogénéité → moindre substituabilité → demande moins élastique → "
       "pouvoir sur le prix."),

f(id='q9-n58', sp='c9-10', niv='appliquer', type='assoc', b=1692,
  q="Classez chaque situation selon la forme de différenciation qu’elle "
    "illustre.",
  ans=[["De l’électroménager basique à l’électroménager haut de gamme", "Différenciation verticale (qualité, gamme)"],
       ["Des produits hiérarchisés par la qualité, le plus cher étant présenté comme meilleur", "Différenciation verticale (qualité, gamme)"],
       ["Des agendas globalement équivalents, choisis selon le goût du consommateur", "Différenciation horizontale (style, goût)"],
       ["Un commerce choisi parce qu’il est plus proche du domicile", "Différenciation horizontale (localisation)"]],
  exp="La différenciation verticale repose sur des différences de qualité, "
      "classables par les consommateurs selon une hiérarchie de gamme, ce qui "
      "justifie des écarts de prix. La différenciation horizontale repose sur "
      "des caractéristiques secondaires : les produits sont globalement "
      "équivalents mais ne plaisent pas aux mêmes consommateurs. Dans "
      "l’exemple de la localisation, le produit n’est pas meilleur : c’est la "
      "proximité qui crée une valeur supplémentaire.",
  diss="Test simple : si tous les consommateurs classent les produits dans le "
       "même ordre, la différenciation est verticale ; sinon, elle est "
       "horizontale."),

f(id='q9-n59', sp='c9-10', niv='raisonner', type='qcm', b=1773,
  q="Pourquoi la tarification différentielle est-elle jugée plus "
    "problématique en situation de monopole ?",
  opts=["Parce que le monopole ne peut pas connaître la sensibilité au prix "
        "de ses clients",
        "Parce que le consommateur ne dispose pas d’alternative "
        "concurrentielle pour échapper au prix imposé",
        "Parce que le yield management est interdit en monopole",
        "Parce que le monopole doit appliquer un prix unique fixé par l’État"],
  ans=1,
  why=["Le monopole peut au contraire segmenter sa clientèle : c’est tout "
       "l’objet de la discrimination tarifaire.",
       "Le yield management n’est pas interdit en soi : le cours souligne "
       "qu’il est souvent toléré.",
       "Aucune obligation de prix unique n’est mentionnée par le cours."],
  exp="Les autorités peuvent tolérer la tarification différentielle si le "
      "marché reste servi, si les consommateurs trouvent encore une offre, si "
      "la pratique ne ferme pas le marché et ne bloque pas les concurrents. "
      "Sur un marché concurrentiel, un consommateur qui juge la tarification "
      "abusive peut aller chez un concurrent. En monopole, ce choix est limité "
      "ou impossible : le consommateur subit le prix.",
  diss="Critère général de la politique de concurrence dans ce chapitre : ce "
       "qui compte n’est pas la pratique en elle-même mais l’existence "
       "d’alternatives pour le consommateur."),

# ------------------------------------------------------------- c9-11
f(id='q9-n60', sp='c9-11', niv='comprendre', type='qcm', b=1800,
  q="Pourquoi un cartel n’est-il ni une fusion, ni une concentration, ni un "
    "rachat ?",
  opts=["Parce qu’il est toujours temporaire",
        "Parce que chaque entreprise reste juridiquement indépendante, tout "
        "en se coordonnant comme si les firmes formaient une seule entreprise "
        "dominante",
        "Parce qu’il est autorisé par les autorités de concurrence",
        "Parce qu’il ne porte que sur les quantités, jamais sur les prix"],
  ans=1,
  why=["La durée n’est pas le critère : Combe montre qu’un cartel dure sept "
       "ans en moyenne.",
       "Les cartels sont au contraire condamnés : l’article 101 du TFUE "
       "interdit les ententes.",
       "Un cartel peut porter sur les prix, les quantités ou le partage du "
       "marché."],
  exp="Le cartel est un accord entre plusieurs entreprises indépendantes "
      "visant à fixer les prix, les quantités ou le partage du marché. Comme "
      "dans le trust, chaque entreprise reste juridiquement indépendante, "
      "mais elles se coordonnent comme si elles formaient une seule "
      "entreprise dominante : le cours parle d’un « monopole à plusieurs ».",
  diss="Distinction juridique décisive : la concentration passe par le "
       "contrôle des fusions, l’entente par l’interdiction et la sanction."),

f(id='q9-n61', sp='c9-11', niv='connaitre', type='qcmm', b=1820,
  q="Quelles caractéristiques moyennes des cartels Emmanuel Combe met-il en "
    "évidence ? (plusieurs réponses)",
  opts=["Une durée d’environ sept ans",
        "Des prix environ 15 % plus élevés que les prix concurrentiels",
        "Une présence forte dans les produits intermédiaires",
        "Une fréquence élevée sur les marchés oligopolistiques",
        "Une concentration dans les services aux particuliers"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les cartels sont souvent durables malgré leur instabilité "
       "théorique.",
       "Exacte : c’est l’ordre de grandeur du surcoût pour le client.",
       "Exacte : composants, matières premières transformées, biens utilisés "
       "par d’autres entreprises.",
       "Exacte : il est plus facile de s’entendre à quelques-uns qu’à une "
       "multitude d’acteurs.",
       "Faux : les produits intermédiaires dominent, ce qui explique que le "
       "grand public ne voie pas toujours ces cartels."],
  exp="L’étude porte sur 111 cartels entre 1969 et 2009, dans La politique de "
      "la concurrence (2016). Elle apporte une nuance importante : les "
      "cartels apparaissent surtout là où le marché compte peu d’entreprises, "
      "et ils portent souvent sur des biens intermédiaires, donc invisibles "
      "pour le consommateur final, qui en supporte pourtant le surcoût.",
  diss="Les deux chiffres à retenir ensemble : sept ans et +15 % — assez "
       "durables pour être nuisibles, assez fragiles pour être détectés."),

f(id='q9-n62', sp='c9-11', niv='appliquer', type='qcm', b=1850,
  q="Dans la matrice du cours, deux entreprises gagnent 5 chacune si elles "
    "respectent l’accord, 8 contre 0 si l’une triche seule, 3 chacune si "
    "elles trichent toutes les deux. Quelle est la décision rationnelle de "
    "chaque entreprise ?",
  opts=["Respecter l’accord, puisque 5 est supérieur à 3",
        "Tricher, puisque tricher rapporte plus quelle que soit la décision "
        "de l’autre : 8 au lieu de 5 si l’autre respecte, 3 au lieu de 0 si "
        "l’autre triche",
        "Respecter l’accord si l’autre triche, tricher si l’autre respecte",
        "La décision est indéterminée"],
  ans=1,
  why=["Comparer 5 et 3 revient à comparer deux situations collectives, non "
       "les choix individuels à décision de l’autre donnée.",
       "Si l’autre triche, respecter rapporte 0 contre 3 en trichant : "
       "respecter n’est jamais la meilleure réponse.",
       "La décision est au contraire parfaitement déterminée : tricher est "
       "une stratégie dominante."],
  exp="Le raisonnement se fait à décision de l’autre donnée. Si l’autre "
      "respecte l’accord, tricher rapporte 8 au lieu de 5. Si l’autre triche, "
      "tricher rapporte 3 au lieu de 0. Donc, quelle que soit la décision de "
      "l’autre, chaque entreprise a intérêt à tricher. Le résultat collectif "
      "(3, 3) est pourtant inférieur à celui de la coopération (5, 5) : "
      "l’intérêt individuel détruit l’intérêt collectif.",
  diss="C’est la structure même du dilemme du prisonnier : une stratégie "
       "dominante individuellement, un résultat collectivement sous-optimal."),

f(id='q9-n63', sp='c9-11', niv='comprendre', type='assoc', b=1931,
  q="Associez chaque type d’entente à la raison pour laquelle les autorités "
    "peuvent la tolérer.",
  ans=[["Coopération entre laboratoires pharmaceutiques pour développer un médicament", "Entente technologique : partager des coûts de recherche très élevés et accélérer l’innovation"],
       ["Partage de brevets et de licences entre entreprises", "Entente technologique : partager des coûts de recherche très élevés et accélérer l’innovation"],
       ["Accord entre une marque de luxe et ses distributeurs sur les conditions de vente", "Entente verticale : préserver l’image de marque et la qualité de la distribution"],
       ["Accord entre un producteur et son réseau de revendeurs", "Entente verticale : préserver l’image de marque et la qualité de la distribution"]],
  exp="Les autorités distinguent les ententes anticoncurrentielles des "
      "coopérations économiques légitimes. Une coordination peut être tolérée "
      "si elle améliore l’efficacité économique, favorise l’innovation, "
      "bénéficie aux consommateurs et ne verrouille pas le marché. Les "
      "ententes verticales concernent des entreprises situées à différents "
      "niveaux de la chaîne : producteur et distributeur, fabricant et "
      "revendeur, marque et plateforme de vente.",
  diss="Le développement du commerce en ligne complique cet arbitrage : les "
       "pure players, sans magasins ni loyers, vendent moins cher, et les "
       "autorités doivent arbitrer entre baisse des prix et loyauté de la "
       "concurrence avec les distributeurs physiques."),

]
