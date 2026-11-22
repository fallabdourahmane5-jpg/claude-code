# -*- coding: utf-8 -*-
"""Chapitre 9 — questions nouvelles, sous-parties c9-01 à c9-03."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c9-01
f(id='q9-n01', sp='c9-01', niv='comprendre', type='qcmm', b=260,
  q="Quelles explications le cours donne-t-il à la concentration des "
    "entreprises ? (plusieurs réponses)",
  opts=["La recherche d’économies d’échelle",
        "Le coût croissant des innovations",
        "La mondialisation et la concurrence internationale",
        "La volonté d’obtenir un pouvoir de marché",
        "L’obligation légale de fusionner au-delà d’une certaine taille"],
  ans=[0, 1, 2, 3],
  why=["Exacte : plus l’entreprise est grande, plus elle répartit ses coûts "
       "fixes sur une production importante.",
       "Exacte : seules les grandes firmes peuvent souvent financer des "
       "dépenses de recherche considérables.",
       "Exacte : la mondialisation oblige les entreprises à atteindre une "
       "taille internationale.",
       "Exacte : la concentration est aussi une arme concurrentielle, qui "
       "réduit l’atomicité du marché.",
       "Aucune obligation de ce type n’existe : le droit de la concurrence "
       "contrôle les fusions, il ne les impose pas."],
  exp="Le cours insiste sur le fait que la concentration ne résulte pas du "
      "hasard : elle répond à des dynamiques précises du capitalisme. Les "
      "transformations techniques — factory system au XIXe siècle, taylorisme "
      "et fordisme, puis plateformes numériques — rendent la grande taille "
      "nécessaire ; la concurrence en fait une arme ; les crises accélèrent "
      "le mouvement (1873-1896, 1929) ; la mondialisation impose une taille "
      "internationale.",
  diss="Enchaînement utile : innovation coûteuse → besoin de taille → "
       "concentration → pouvoir de marché → nécessité d’une politique de "
       "concurrence."),

f(id='q9-n02', sp='c9-01', niv='appliquer', type='qcm', b=66,
  q="Jack Welch dirige General Electric pendant plus de trente ans en "
    "multipliant rachats, restructurations et licenciements massifs, et en "
    "supprimant les activités jugées insuffisamment rentables. Que cette "
    "stratégie illustre-t-elle, selon le cours ?",
  opts=["Le refus de la croissance externe",
        "La financiarisation des grandes entreprises et la recherche d’une "
        "rentabilité maximale",
        "Le retour à une logique de monopole naturel",
        "La transformation de GE en district industriel"],
  ans=1,
  why=["Welch recourt massivement à la croissance externe : il rachète des "
       "entreprises.",
       "Le monopole naturel renvoie à des coûts fixes élevés dans les "
       "réseaux, pas à une stratégie managériale.",
       "Le district industriel est une concentration locale d’entreprises "
       "indépendantes : rien à voir avec un conglomérat."],
  exp="General Electric part de l’électricité et de l’ampoule électrique, "
      "puis devient un conglomérat géant intervenant dans l’électricité, le "
      "pétrole, les médias, la finance et la gestion industrielle. La période "
      "Welch illustre le poids croissant des stratégies managériales et "
      "financières : la rentabilité devient le critère de sélection des "
      "activités et des salariés.",
  diss="GE sert deux fois dans le chapitre : comme exemple de concentration "
       "conglomérale, puis comme exemple de scission pour échapper à la "
       "décote de conglomérat."),

f(id='q9-n03', sp='c9-01', niv='comprendre', type='vf', b=127,
  q="En concurrence imparfaite, les entreprises restent preneuses de prix.",
  ans=False,
  exp="C’est l’inverse : la concurrence imparfaite désigne la situation dans "
      "laquelle certaines entreprises peuvent influencer les prix ou les "
      "quantités produites. Elles deviennent donneuses de prix. Le statut de "
      "preneuse de prix appartient au modèle théorique de concurrence pure et "
      "parfaite, où les entreprises sont nombreuses et aucune ne peut "
      "influencer le prix.",
  diss="Le cours rappelle que la concurrence parfaite est surtout un modèle : "
       "dans les faits, les marchés fonctionnent majoritairement en "
       "concurrence imparfaite."),

# ------------------------------------------------------------- c9-02
f(id='q9-n04', sp='c9-02', niv='connaitre', type='qcm', b=311,
  q="En quelle année John D. Rockefeller fonde-t-il la Standard Oil Company, "
    "et quelle part du raffinage américain finit-il par contrôler ?",
  opts=["1870, et environ 90 % du raffinage américain",
        "1890, et environ 50 % du raffinage américain",
        "1911, et la totalité du raffinage américain",
        "1850, et environ 10 % du raffinage américain"],
  ans=0,
  why=["1890 est la date du Sherman Act, non de la fondation de la Standard "
       "Oil.",
       "1911 est la date du démantèlement de la Standard Oil, pas de sa "
       "fondation.",
       "10 % correspond à la part de départ de Rockefeller, pas à son point "
       "d’arrivée."],
  exp="Rockefeller fonde la Standard Oil en 1870 et rachète progressivement "
      "ses concurrents du raffinage : il passe d’environ 10 % du marché à "
      "environ 90 % du raffinage américain. C’est l’exemple historique majeur "
      "de concentration horizontale, et il devient le symbole des dangers de "
      "la concentration économique, jusqu’au démantèlement de 1911.",
  diss="Rockefeller est l’exemple le plus rentable du chapitre : il illustre "
       "à la fois la concentration horizontale, la concentration verticale, "
       "les prix prédateurs et le démantèlement antitrust."),

f(id='q9-n05', sp='c9-02', niv='appliquer', type='qcm', b=370,
  q="Rockefeller ne se contente pas de raffiner le pétrole : il fabrique "
    "aussi ses propres tonneaux, dont le coût passe d’environ 2,5 dollars à "
    "1 dollar. De quelle stratégie s’agit-il ?",
  opts=["Une concentration horizontale, puisqu’il élimine un concurrent",
        "Une concentration verticale en amont, qui supprime la marge du "
        "fournisseur",
        "Une concentration conglomérale, puisque la tonnellerie n’est pas le "
        "pétrole",
        "Une entente avec les fabricants de tonneaux"],
  ans=1,
  why=["Les tonneliers ne sont pas ses concurrents : ils sont ses "
       "fournisseurs.",
       "Il ne s’agit pas d’une diversification sans lien : le tonneau est une "
       "consommation intermédiaire directement nécessaire à son activité.",
       "Il n’y a pas d’accord entre firmes indépendantes mais internalisation "
       "de l’activité."],
  exp="L’amont correspond aux fournisseurs, aux matières premières et aux "
      "consommations intermédiaires ; l’aval à la distribution, à la vente et "
      "au consommateur final. En fabriquant lui-même ses tonneaux, Rockefeller "
      "remonte la chaîne et supprime la marge de ses fournisseurs : le coût "
      "unitaire est divisé par deux et demi. La concentration verticale "
      "devient ici un instrument de réduction des coûts.",
  diss="Exemple idéal pour montrer que la concentration verticale a une "
       "justification économique — coûts et sécurité d’approvisionnement — "
       "avant d’avoir une justification théorique chez Coase et Williamson."),

f(id='q9-n06', sp='c9-02', niv='connaitre', type='assoc', b=347,
  q="Associez chaque élément de la chaîne productive à sa position.",
  ans=[["Les fournisseurs de l’entreprise", "L’amont"],
       ["Les matières premières et les consommations intermédiaires", "L’amont"],
       ["La distribution et la vente", "L’aval"],
       ["Le consommateur final", "L’aval"]],
  exp="L’entreprise qui se concentre verticalement cherche à maîtriser toutes "
      "les étapes de la chaîne, de l’amont à l’aval. Cette stratégie permet "
      "de sécuriser les approvisionnements, de réduire les coûts, de limiter "
      "la dépendance et d’éviter certains intermédiaires. Amazon l’illustre "
      "aujourd’hui en rachetant MGM et iRobot pour étendre son écosystème.",
  diss="Repère simple : l’amont est du côté de la production, l’aval du côté "
       "du marché final."),

f(id='q9-n07', sp='c9-02', niv='comprendre', type='qcm', b=296,
  q="Pourquoi la concentration horizontale permet-elle de réaliser des "
    "économies d’échelle ?",
  opts=["Parce qu’elle supprime les coûts fixes de l’entreprise",
        "Parce qu’une production plus importante permet de répartir les coûts "
        "fixes sur un plus grand nombre d’unités",
        "Parce que les salaires baissent mécaniquement avec la taille",
        "Parce que les prix de vente augmentent avec la part de marché"],
  ans=1,
  why=["Les coûts fixes ne disparaissent pas : ils sont simplement répartis "
       "différemment.",
       "Le cours ne fait pas dépendre les salaires de la taille de "
       "l’entreprise dans ce passage.",
       "Une hausse des prix est un effet possible du pouvoir de marché, non "
       "la définition des économies d’échelle."],
  exp="Plus l’entreprise devient grande, plus elle peut répartir ses coûts "
      "fixes sur une production importante : le coût unitaire baisse. Elle "
      "peut alors soit baisser ses prix, soit augmenter ses marges. La "
      "concentration horizontale combine donc deux effets : un effet de "
      "pouvoir de marché, puisque les concurrents disparaissent, et un effet "
      "d’efficacité productive.",
  diss="C’est cette dualité qui rend la politique de concurrence difficile : "
       "une fusion peut à la fois nuire à la concurrence et réduire les "
       "coûts."),

f(id='q9-n08', sp='c9-02', niv='connaitre', type='qcmm', b=328,
  q="Quels exemples contemporains de concentration horizontale le cours "
    "retient-il ? (plusieurs réponses)",
  opts=["LVMH rachète Tiffany et renforce sa domination de la joaillerie",
        "La Française des Jeux rachète Kindred / Unibet et se développe dans "
        "les paris en ligne",
        "Amazon rachète MGM et iRobot pour étendre son écosystème",
        "Samsung réunit des dizaines d’activités très différentes",
        "Rockefeller rachète progressivement ses concurrents du raffinage"],
  ans=[0, 1, 4],
  why=["Exacte : deux entreprises du luxe, donc des activités similaires.",
       "Exacte : même secteur des jeux, donc concurrents directs.",
       "Ces rachats relèvent de la concentration verticale et de l’extension "
       "d’écosystème, pas du rachat de concurrents directs.",
       "Samsung est l’exemple emblématique de concentration conglomérale.",
       "Exacte : c’est l’exemple historique majeur de concentration "
       "horizontale."],
  exp="La concentration horizontale réunit des entreprises aux activités "
      "similaires, donc concurrentes directes : sa logique est de réduire "
      "l’intensité de la concurrence et d’augmenter les parts de marché. La "
      "difficulté de l’exercice tient à ce que les mêmes groupes pratiquent "
      "souvent plusieurs formes de concentration en même temps."),

f(id='q9-n09', sp='c9-02', niv='comprendre', type='courte', b=360,
  q="Quels enjeux économiques une entreprise poursuit-elle en se concentrant "
    "verticalement ?",
  ans={'modele': "La concentration verticale permet d’abord de sécuriser les "
       "approvisionnements : en contrôlant ses fournisseurs, l’entreprise ne "
       "dépend plus de leurs décisions ni de leurs ruptures. Elle permet "
       "ensuite de réduire les coûts, en supprimant les marges des "
       "intermédiaires — Rockefeller divise par deux et demi le coût de ses "
       "tonneaux. Elle limite enfin la dépendance à l’égard de partenaires "
       "extérieurs et évite certains intermédiaires, en amont comme en aval. "
       "Williamson ajoute une justification théorique : internaliser une "
       "activité permet de réduire les coûts de transaction liés au recours "
       "au marché, dans un monde où les contrats sont incomplets et les "
       "agents opportunistes.",
       'cles': [{'f': ['securiser', 'approvisionnement'],
                 'l': 'sécuriser les approvisionnements'},
                {'f': ['cout', 'marge', 'intermediaire'],
                 'l': 'réduire les coûts et supprimer les marges des intermédiaires'},
                {'f': ['dependance'],
                 'l': 'limiter la dépendance'},
                {'f': ['transaction', 'williamson'],
                 'l': 'réduire les coûts de transaction (Williamson)'}]},
  exp="Le cours donne quatre enjeux : sécuriser les approvisionnements, "
      "réduire les coûts, limiter la dépendance, éviter certains "
      "intermédiaires. Il relie ensuite explicitement cette stratégie à "
      "Williamson : la concentration verticale devient une réponse aux coûts "
      "de transaction."),

f(id='q9-n10', sp='c9-02', niv='comprendre', type='qcm', b=400,
  q="Quelle est la première hypothèse formulée par Williamson pour expliquer "
    "l’internalisation de certaines activités ?",
  opts=["La rationalité limitée, inspirée d’Herbert Simon : les agents "
        "disposent d’informations imparfaites et ne peuvent pas tout prévoir, "
        "donc les contrats sont incomplets",
        "La rationalité parfaite des agents",
        "L’absence de coûts de production",
        "L’existence d’un monopole naturel"],
  ans=0,
  why=["La rationalité parfaite est l’hypothèse néoclassique que Williamson "
       "abandonne précisément.",
       "Les coûts de production existent toujours : l’enjeu est le coût du "
       "recours au marché.",
       "Le monopole naturel est une structure de marché, pas une hypothèse "
       "sur le comportement des agents."],
  exp="Williamson pose deux hypothèses. La rationalité limitée, reprise "
      "d’Herbert Simon : les agents ont une information imparfaite et ne "
      "peuvent pas tout prévoir, donc les contrats sont nécessairement "
      "incomplets. L’opportunisme : les agents peuvent chercher uniquement "
      "leur intérêt personnel, ce qui crée des asymétries d’information. Dans "
      "ce contexte, le recours au marché devient coûteux et risqué, et "
      "l’entreprise préfère parfois internaliser.",
  diss="Les deux hypothèses sont complémentaires : sans rationalité limitée, "
       "les contrats seraient complets ; sans opportunisme, leur incomplétude "
       "ne poserait pas problème."),

f(id='q9-n11', sp='c9-02', niv='comprendre', type='vf', b=409,
  q="Chez Williamson, l’opportunisme désigne le fait que les agents peuvent "
    "chercher uniquement leur intérêt personnel, ce qui crée des asymétries "
    "d’information.",
  ans=True,
  exp="C’est bien la seconde hypothèse de Williamson. Combinée à la "
      "rationalité limitée, qui rend les contrats incomplets, elle rend le "
      "recours au marché coûteux et risqué : l’autre partie peut exploiter "
      "les silences du contrat. L’entreprise préfère alors internaliser "
      "l’activité, c’est-à-dire la soumettre à l’autorité hiérarchique plutôt "
      "qu’au contrat marchand.",
  diss="Le cours signale lui-même la limite de cette hypothèse : faire de "
       "l’opportunisme le ressort central fait de l’entreprise un lieu de "
       "triche, alors qu’elle est aussi un lieu de coopération."),

f(id='q9-n12', sp='c9-02', niv='raisonner', type='ordre', b=415,
  q="Remettez dans l’ordre le raisonnement qui conduit, chez Williamson, de "
    "l’imperfection du marché à la concentration verticale.",
  ans=["Les agents ont une rationalité limitée : ils ne peuvent pas tout "
       "prévoir",
       "Les contrats sont donc nécessairement incomplets",
       "Les agents peuvent se comporter de façon opportuniste et exploiter "
       "ces silences",
       "Le recours au marché devient coûteux et risqué : les coûts de "
       "transaction s’élèvent",
       "L’entreprise internalise l’activité : la concentration verticale "
       "devient une réponse aux coûts de transaction"],
  exp="L’enchaînement est celui du cours : rationalité limitée, contrats "
      "incomplets, opportunisme, coûts de transaction élevés, "
      "internalisation. La comparaison entre coûts de transaction et coûts "
      "d’internalisation détermine alors la taille de l’entreprise.",
  diss="Cet enchaînement est le cœur de l’approche transactionnelle : la "
       "firme n’est pas un marché, elle existe parce que le marché a un coût."),

f(id='q9-n13', sp='c9-02', niv='raisonner', type='courte', b=308,
  q="En quoi Rockefeller permet-il d’illustrer à la fois l’efficacité et les "
    "dangers de la concentration ?",
  ans={'modele': "Rockefeller illustre d’abord l’efficacité : en rachetant "
       "ses concurrents du raffinage, il réalise des économies d’échelle ; en "
       "intégrant la fabrication de ses tonneaux, il divise le coût unitaire "
       "par deux et demi. La concentration, horizontale puis verticale, est "
       "donc un facteur de réduction des coûts. Mais elle devient un danger "
       "lorsqu’il passe d’environ 10 % à environ 90 % du raffinage américain : "
       "la Standard Oil impose ses conditions tarifaires, met ses concurrents "
       "en difficulté et impose ses tarifs aux compagnies de chemin de fer, "
       "qui ne peuvent refuser un client aussi important. Rockefeller devient "
       "ainsi le symbole de l’entreprise dont la réussite finit par inquiéter "
       "l’État, jusqu’au démantèlement de la Standard Oil en 1911 dans le "
       "cadre des lois antitrust.",
       'cles': [{'f': ['economie d echelle', 'cout', 'tonneau'],
                 'l': 'l’efficacité : économies d’échelle et baisse des coûts'},
                {'f': ['90', 'raffinage', 'monopole'],
                 'l': 'la domination du marché du raffinage'},
                {'f': ['chemin de fer', 'tarif', 'condition'],
                 'l': 'l’imposition de conditions tarifaires aux concurrents et aux chemins de fer'},
                {'f': ['1911', 'demantelement', 'antitrust'],
                 'l': 'le démantèlement de 1911 au titre des lois antitrust'}]},
  exp="Le cours construit Rockefeller comme un cas d’école ambivalent : il "
      "montre la rationalité économique de la concentration, puis son "
      "basculement dans l’abus, et enfin la réponse publique. Il souligne "
      "aussi l’ironie de l’histoire : dans les années 1990, Exxon et Mobil, "
      "issues du démantèlement, refusionnent."),

f(id='q9-n14', sp='c9-02', niv='comprendre', type='qcm', b=423,
  q="Qu’est-ce qui distingue la concentration conglomérale des deux autres "
    "formes de concentration ?",
  opts=["Elle regroupe des entreprises aux activités similaires",
        "Elle ne repose ni sur des activités similaires ni sur des activités "
        "complémentaires : son objectif est de diversifier les risques",
        "Elle suppose un accord sur les prix entre entreprises indépendantes",
        "Elle concerne uniquement les entreprises publiques"],
  ans=1,
  why=["Les activités similaires caractérisent la concentration horizontale.",
       "Un accord sur les prix est un cartel, donc une entente sans "
       "regroupement de capital.",
       "Le statut public ou privé n’intervient pas dans cette typologie."],
  exp="La concentration conglomérale regroupe des entreprises sans lien "
      "direct entre leurs activités. L’objectif n’est plus de contrôler un "
      "marché ou une chaîne de production mais de diversifier les risques : "
      "si un secteur fonctionne mal, les autres peuvent compenser. Samsung en "
      "est l’exemple emblématique, avec des dizaines d’activités différentes."),

# ------------------------------------------------------------- c9-03
f(id='q9-n15', sp='c9-03', niv='raisonner', type='qcm', b=458,
  q="Pour échapper à la décote de conglomérat, quelle stratégie les groupes "
    "diversifiés adoptent-ils généralement ?",
  opts=["Racheter davantage d’activités sans lien entre elles",
        "Se scinder en plusieurs sociétés indépendantes et se recentrer sur "
        "leur activité principale",
        "Demander une aide d’État",
        "Former un cartel avec leurs concurrents"],
  ans=1,
  why=["Davantage de diversification aggraverait la décote au lieu de la "
       "corriger.",
       "Une aide d’État ne modifie pas le jugement des investisseurs sur la "
       "cohérence du groupe, et serait de surcroît surveillée par Bruxelles.",
       "Un cartel porte sur les prix ou les quantités : il n’a aucun effet "
       "sur la valorisation d’un conglomérat."],
  exp="La décote de conglomérat signifie que la valeur boursière d’un groupe "
      "diversifié est inférieure à la somme de la valeur de ses activités "
      "prises séparément : les investisseurs préfèrent des entreprises "
      "spécialisées. Les groupes se scindent donc ou se recentrent. General "
      "Electric, immense conglomérat, finit par se séparer en plusieurs "
      "pôles, dans une logique de valorisation actionnariale.",
  diss="À relier au capitalisme actionnarial : la priorité donnée à la valeur "
       "pour l’actionnaire peut conduire à démanteler des groupes "
       "industriellement cohérents."),

f(id='q9-n16', sp='c9-03', niv='comprendre', type='qcm', b=487,
  q="Pourquoi le coût croissant des innovations favorise-t-il la "
    "concentration ?",
  opts=["Parce que les brevets sont gratuits",
        "Parce que seules les grandes entreprises peuvent souvent financer "
        "des dépenses de recherche et des capacités de recherche "
        "considérables",
        "Parce que l’innovation réduit les coûts fixes",
        "Parce que les PME sont juridiquement exclues de la recherche"],
  ans=1,
  why=["Le brevet est au contraire l’aboutissement d’un investissement "
       "coûteux.",
       "L’innovation exige au contraire des investissements lourds, donc "
       "augmente les coûts fixes.",
       "Rien n’exclut les PME de la recherche : le cours souligne même leur "
       "rôle dans l’innovation."],
  exp="Le cours fait de l’innovation la première grande explication de la "
      "concentration : les innovations deviennent de plus en plus coûteuses "
      "et exigent des capacités de recherche considérables. Cette logique "
      "apparaît dès la révolution industrielle, avec le passage au factory "
      "system qui impose de regrouper les travailleurs dans des usines, "
      "s’amplifie avec le taylorisme et le fordisme, et prend une forme "
      "nouvelle avec l’économie numérique."),

f(id='q9-n17', sp='c9-03', niv='appliquer', type='qcm', b=507,
  q="Une plateforme numérique devient plus attractive à mesure qu’elle "
    "compte d’utilisateurs, ce qui lui en amène d’autres. Quel mécanisme "
    "cette dynamique illustre-t-elle, et quel en est l’effet sur la "
    "structure du marché ?",
  opts=["Les rendements décroissants, qui limitent la taille des plateformes",
        "Les effets de réseau, qui favorisent l’émergence de gigantesques "
        "plateformes mondiales et verrouillent le marché",
        "Les économies d’échelle, qui n’ont aucun effet sur la concurrence",
        "La décote de conglomérat, qui pousse à la scission"],
  ans=1,
  why=["Les rendements décroissants produiraient l’effet inverse : ils "
       "freineraient la croissance de la plateforme.",
       "Les économies d’échelle existent aussi, mais elles ont un effet "
       "direct sur la concurrence : affirmer le contraire est faux.",
       "La décote de conglomérat concerne la valorisation boursière des "
       "groupes diversifiés, pas la dynamique d’usage d’une plateforme."],
  exp="Les effets de réseau signifient que la valeur d’une plateforme "
      "augmente avec le nombre d’utilisateurs. Le mécanisme est cumulatif et "
      "auto-renforçant : utilisateurs, vendeurs, annonceurs et partenaires "
      "affluent vers la plateforme déjà installée. Le premier entrant "
      "conserve donc durablement son avantage, ce qui explique l’émergence "
      "des GAFAM, des BATX chinois et des NATU.",
  diss="Les effets de réseau transforment une barrière économique en barrière "
       "quasi structurelle : c’est l’argument central du DMA."),

f(id='q9-n18', sp='c9-03', niv='comprendre', type='qcm', b=545,
  q="Pourquoi les grandes crises s’accompagnent-elles souvent de vagues de "
    "concentration, comme en 1873-1896 ou après 1929 ?",
  opts=["Parce que les autorités de concurrence suspendent leur contrôle en "
        "période de crise",
        "Parce que les entreprises fragilisées deviennent plus faciles à "
        "absorber",
        "Parce que les crises font disparaître les économies d’échelle",
        "Parce que la demande augmente pendant les crises"],
  ans=1,
  why=["Le cours n’évoque aucune suspension du contrôle des concentrations en "
       "temps de crise.",
       "Les économies d’échelle ne disparaissent pas : elles restent un motif "
       "de rapprochement.",
       "La demande se contracte en crise : c’est précisément ce qui fragilise "
       "les entreprises."],
  exp="La concentration est aussi une arme concurrentielle : augmenter sa "
      "taille permet de réduire les coûts, d’augmenter les profits et de "
      "renforcer son pouvoir de marché. Les périodes de crise accélèrent ce "
      "mouvement parce que les entreprises fragilisées deviennent des cibles "
      "accessibles. Le cours cite la première grande dépression de 1873-1896 "
      "et la crise de 1929, suivies de vagues massives de concentration.",
  diss="Observation utile pour une dissertation d’histoire économique : la "
       "concentration n’est pas un mouvement régulier mais un processus "
       "par vagues, scandé par les crises."),

f(id='q9-n19', sp='c9-03', niv='appliquer', type='assoc', b=565,
  q="Associez chaque situation à la forme de mondialisation qu’elle illustre "
    "selon Suzanne Berger.",
  ans=[["Un pays se spécialise dans un produit et l’échange contre d’autres biens finis", "Première mondialisation (1870-1914) : division internationale du travail"],
       ["Le raisonnement ricardien de la spécialisation", "Première mondialisation (1870-1914) : division internationale du travail"],
       ["Les composants de l’iPhone sont fabriqués dans différents pays et assemblés en Chine", "Mondialisation contemporaine : division internationale des processus productifs"],
       ["Un même produit est fabriqué dans plusieurs pays, étape par étape", "Mondialisation contemporaine : division internationale des processus productifs"]],
  exp="Suzanne Berger montre que la mondialisation ne commence pas dans les "
      "années 1990 : une première mondialisation existe entre 1870 et 1914, "
      "fondée sur la division internationale du travail — chaque pays se "
      "spécialise dans un produit. La mondialisation contemporaine repose sur "
      "la division internationale des processus productifs : la fabrication "
      "d’un même bien est fragmentée entre plusieurs pays.",
  diss="Conséquence pour le chapitre : la DIPP oblige les entreprises à "
       "atteindre une taille internationale et rend les chaînes de "
       "production interdépendantes."),

]
