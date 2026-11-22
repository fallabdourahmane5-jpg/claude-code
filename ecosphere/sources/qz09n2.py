# -*- coding: utf-8 -*-
"""Chapitre 9 — questions nouvelles, sous-parties c9-04 à c9-07."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c9-04
f(id='q9-n20', sp='c9-04', niv='connaitre', type='qcmm', b=584,
  q="Quels dangers de la concentration le cours identifie-t-il ? (plusieurs "
    "réponses)",
  opts=["Un risque fiscal : l’optimisation fiscale des firmes "
        "multinationales, qui prive les États de recettes",
        "Un risque économique : monopoles, oligopoles et barrières à l’entrée",
        "Un risque politique et démocratique : influence médiatique, "
        "politique et électorale",
        "Un risque de souveraineté : des firmes privées exerçant des "
        "fonctions stratégiques autrefois réservées aux États",
        "Un risque juridique : l’interdiction automatique de toute position "
        "dominante"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les grandes firmes multinationales choisissent les "
       "territoires les plus avantageux fiscalement.",
       "Exacte : Philippe Aghion souligne que certaines grandes entreprises "
       "peuvent freiner l’innovation en empêchant l’entrée de nouveaux "
       "concurrents.",
       "Exacte : le cours prend l’exemple de Cambridge Analytica et de "
       "l’utilisation des données personnelles lors de la campagne de Donald "
       "Trump en 2016.",
       "Exacte : SpaceX travaillant avec la NASA pose la question des "
       "fonctions régaliennes confiées à un acteur privé.",
       "Faux, et c’est le point fondamental : la loi ne condamne pas la "
       "position dominante mais son abus."],
  exp="Le cours classe les dangers selon ceux qu’ils touchent : les États "
      "(recettes fiscales, souveraineté), les consommateurs et les "
      "concurrents (prix, barrières à l’entrée, innovation freinée), et la "
      "démocratie elle-même (influence médiatique et électorale).",
  diss="Progression très exploitable : du danger économique classique au "
       "danger politique, spécifique au capitalisme numérique."),

f(id='q9-n21', sp='c9-04', niv='comprendre', type='qcm', b=604,
  q="Que souligne Philippe Aghion à propos des grandes entreprises et de "
    "l’innovation ?",
  opts=["Que les grandes entreprises sont toujours les plus innovantes",
        "Que certaines grandes entreprises peuvent freiner l’innovation en "
        "empêchant l’entrée de nouveaux concurrents",
        "Que l’innovation ne dépend pas de la taille des entreprises",
        "Que les barrières à l’entrée favorisent l’innovation"],
  ans=1,
  why=["Le cours ne lui fait pas dire que la grande taille garantit "
       "l’innovation : il souligne au contraire un risque.",
       "Son propos porte précisément sur un effet de la structure du marché, "
       "donc de la taille et des barrières.",
       "Les barrières à l’entrée protègent l’entreprise installée : elles "
       "réduisent la pression qui pousse à innover."],
  exp="Le risque économique de la concentration tient aux monopoles, aux "
      "oligopoles et surtout aux barrières à l’entrée qu’elle engendre. Ces "
      "barrières freinent la dynamique concurrentielle : si les nouveaux "
      "entrants ne peuvent pas arriver, l’entreprise installée n’est plus "
      "obligée d’innover pour conserver sa position.",
  diss="Argument central des politiques de concurrence modernes : protéger "
       "l’entrée, c’est protéger l’innovation."),

f(id='q9-n22', sp='c9-04', niv='appliquer', type='qcm', b=619,
  q="L’affaire Cambridge Analytica — utilisation de données personnelles pour "
    "influencer la campagne de Donald Trump en 2016 — illustre lequel des "
    "risques de la concentration ?",
  opts=["Le risque fiscal",
        "Le risque politique et démocratique",
        "Le risque de décote de conglomérat",
        "Le risque de monopole naturel"],
  ans=1,
  why=["Le risque fiscal porte sur l’optimisation fiscale et les recettes "
       "publiques.",
       "La décote de conglomérat est un phénomène boursier, sans lien avec "
       "l’influence politique.",
       "Le monopole naturel est une structure de coûts, pas un enjeu "
       "démocratique."],
  exp="Les grandes entreprises peuvent exercer une influence médiatique, "
      "politique et électorale, et le numérique renforce encore cette "
      "capacité par l’exploitation des données personnelles. Acemoglu et "
      "Johnson, dans Power and Progress (2023), prolongent cette critique : "
      "l’intelligence artificielle et les plateformes numériques peuvent "
      "renforcer les manipulations, accroître les asymétries de pouvoir et "
      "concentrer davantage la richesse et l’influence.",
  diss="Le cours insiste sur un point précis : les algorithmes permettent une "
       "personnalisation extrême de l’information, ce qui favorise la "
       "manipulation des opinions, la polarisation et les fake news."),

f(id='q9-n23', sp='c9-04', niv='connaitre', type='qcm', b=679,
  q="Comment le cours définit-il la souveraineté numérique ?",
  opts=["La capacité d’un État à contrôler ses technologies, ses données et "
        "ses infrastructures numériques",
        "L’obligation pour les plateformes de payer l’impôt dans leur pays "
        "d’origine",
        "Le droit des utilisateurs à effacer leurs données personnelles",
        "La capacité d’une plateforme à fixer ses propres règles"],
  ans=0,
  why=["La fiscalité des plateformes relève du risque fiscal, traité "
       "séparément.",
       "Le droit à l’effacement est une protection individuelle, pas une "
       "question de souveraineté étatique.",
       "C’est exactement l’inverse : la souveraineté numérique est menacée "
       "quand ce sont les plateformes qui fixent les règles."],
  exp="L’enjeu est que les États deviennent dépendants de technologies "
      "privées, d’entreprises mondiales et de dirigeants non élus. Certaines "
      "firmes exercent désormais des fonctions stratégiques, technologiques "
      "voire régaliennes — sécurité, souveraineté, missions stratégiques — "
      "comme le montre SpaceX travaillant avec la NASA. La question posée par "
      "le cours est explicite : peut-on laisser les satellites, l’espace, "
      "l’IA, les données et certaines infrastructures stratégiques entre les "
      "mains d’entreprises privées ?"),

f(id='q9-n24', sp='c9-04', niv='comprendre', type='qcm', b=686,
  q="Qu’est-ce qui distingue un trust d’une fusion classique ?",
  opts=["Dans le trust, les entreprises disparaissent juridiquement",
        "Dans le trust, les entreprises restent juridiquement indépendantes "
        "mais prix, quantités et stratégie sont décidés collectivement par une "
        "structure centrale",
        "Le trust est une entente temporaire sur les prix, sans direction "
        "commune",
        "Le trust est une forme de monopole public"],
  ans=1,
  why=["C’est l’inverse : ce sont les entreprises absorbées par une fusion "
       "qui disparaissent juridiquement.",
       "Le trust va plus loin qu’une simple entente sur les prix : il "
       "comporte une direction commune.",
       "Le trust est une forme privée de concentration, illustrée par la "
       "Standard Oil de Rockefeller."],
  exp="Le trust est une forme particulière de concentration : les entreprises "
      "restent juridiquement indépendantes mais confient leur direction à une "
      "structure centrale commune, qui décide des prix, des quantités et de la "
      "stratégie. Le cours donne la Standard Oil de Rockefeller comme exemple, "
      "ce qui explique le nom des lois antitrust américaines.",
  diss="À distinguer soigneusement du cartel : celui-ci coordonne sans "
       "direction commune, le trust ajoute une structure centrale."),

f(id='q9-n25', sp='c9-04', niv='comprendre', type='qcm', b=703,
  q="Pourquoi le monopole conduit-il, selon le cours, à une allocation "
    "sous-optimale des ressources ?",
  opts=["Parce qu’il augmente les prix et réduit les quantités produites",
        "Parce qu’il produit trop par rapport à la demande",
        "Parce qu’il ne réalise aucune économie d’échelle",
        "Parce qu’il est toujours subventionné par l’État"],
  ans=0,
  why=["Le monopoleur restreint au contraire les quantités pour soutenir le "
       "prix.",
       "Le monopole peut parfaitement réaliser des économies d’échelle : "
       "c’est même l’argument du monopole naturel.",
       "Rien n’impose qu’un monopole soit subventionné."],
  exp="Le monopole dispose d’un pouvoir spécifique sur les prix : il augmente "
      "les prix et réduit les quantités, ce qui aboutit à une allocation "
      "sous-optimale des ressources — certains consommateurs renoncent à "
      "acheter alors qu’ils auraient été prêts à payer un prix proche du coût "
      "de production. C’est le fondement de la méfiance de l’approche "
      "standard à l’égard du monopole.",
  diss="À nuancer immédiatement avec l’approche élargie : si le marché est "
       "contestable, le monopole se comporte comme s’il était en concurrence."),

# ------------------------------------------------------------- c9-05
f(id='q9-n26', sp='c9-05', niv='comprendre', type='qcmm', b=780,
  q="Quelles forces le cours attribue-t-il aux PME ? (plusieurs réponses)",
  opts=["Une organisation hiérarchique simple, avec peu de niveaux et une "
        "chaîne de commandement courte",
        "Des circuits de décision rapides, sans lourdeur administrative",
        "Une proximité des marchés : elles connaissent mieux leurs clients et "
        "détectent vite les changements de demande",
        "Une forte réactivité à la conjoncture et une capacité d’adaptation "
        "rapide",
        "Un accès privilégié aux marchés financiers"],
  ans=[0, 1, 2, 3],
  why=["Exacte : peu de niveaux hiérarchiques, des relations plus directes, "
       "une information qui circule vite.",
       "Exacte : la décision ne doit pas remonter une longue chaîne "
       "hiérarchique.",
       "Exacte : la proximité du marché local est un avantage informationnel.",
       "Exacte : elles peuvent modifier rapidement leur production.",
       "C’est au contraire l’une de leurs faiblesses majeures : elles ont "
       "difficilement accès aux marchés financiers et dépendent des banques."],
  exp="La petite taille donne aux PME de la souplesse et de la réactivité : "
      "organisation simple, décisions rapides, proximité des clients, forte "
      "capacité d’adaptation. C’est ce qui explique leur persistance face aux "
      "géants mondiaux, alors qu’on pouvait croire que le capitalisme moderne "
      "conduirait à leur disparition."),

f(id='q9-n27', sp='c9-05', niv='comprendre', type='qcmm', b=819,
  q="Quelles faiblesses le cours attribue-t-il aux PME ? (plusieurs réponses)",
  opts=["Des moyens financiers limités et un accès restreint aux capitaux",
        "Une forte dépendance bancaire, faute d’accès aux marchés financiers",
        "Une difficulté à conquérir les marchés internationaux et à supporter "
        "les coûts de l’exportation",
        "Une forte sensibilité à la conjoncture, qui en fait parfois une "
        "variable d’ajustement",
        "Une incapacité à innover"],
  ans=[0, 1, 2, 3],
  why=["Exacte : leurs faibles capacités financières limitent "
       "l’investissement.",
       "Exacte : elles dépendent davantage des banques et des créanciers, "
       "donc des conditions de financement.",
       "Exacte : visibilité mondiale et coûts de l’exportation leur sont "
       "difficilement accessibles.",
       "Exacte : leurs commandes diminuent rapidement en période de crise.",
       "Faux : le cours souligne au contraire leur rôle essentiel dans "
       "l’emploi et dans l’innovation."],
  exp="Les PME cumulent trois fragilités : financière, commerciale et "
      "conjoncturelle. Le contraste est saisissant avec les très grandes "
      "entreprises jugées « too big to fail », trop importantes pour être "
      "laissées en faillite : les PME, elles, servent parfois de variable "
      "d’ajustement du marché.",
  diss="Argument utile sur l’asymétrie du traitement public : le sauvetage "
       "des grandes firmes est aussi une distorsion de concurrence."),

f(id='q9-n28', sp='c9-05', niv='connaitre', type='qcm', b=851,
  q="Que signifie l’expression « too big to fail » dans le cours ?",
  opts=["Qu’une entreprise trop grande finit nécessairement par échouer",
        "Que certaines très grandes entreprises sont considérées comme trop "
        "importantes pour être laissées en faillite",
        "Qu’une PME ne peut pas faire faillite",
        "Qu’une entreprise doit atteindre une taille minimale pour exporter"],
  ans=1,
  why=["C’est le contresens inverse : l’expression désigne une protection de "
       "fait, pas une fatalité d’échec.",
       "Les PME sont au contraire les plus vulnérables aux retournements de "
       "conjoncture.",
       "La taille minimale pour exporter est une autre question, celle de la "
       "difficulté d’exportation des PME."],
  exp="L’expression désigne les très grandes entreprises dont la défaillance "
      "aurait des conséquences jugées inacceptables : elles bénéficient donc "
      "d’une forme de protection implicite. Le cours l’oppose explicitement à "
      "la situation des PME, beaucoup plus vulnérables, ce qui éclaire "
      "l’inégalité de traitement entre tailles d’entreprises."),

f(id='q9-n29', sp='c9-05', niv='comprendre', type='qcm', b=861,
  q="Qu’est-ce qu’une ETI et quelle logique cette forme cherche-t-elle à "
    "incarner ?",
  opts=["Une entreprise de taille intermédiaire, qui cherche à combiner la "
        "souplesse des PME et les moyens financiers des grandes entreprises",
        "Une entreprise de technologie et d’innovation, spécialisée dans le "
        "numérique",
        "Une entreprise d’intérêt général, détenue par l’État",
        "Une entreprise transnationale intégrée verticalement"],
  ans=0,
  why=["« Technologie et innovation » n’est pas la signification du sigle.",
       "Le statut public n’intervient pas dans cette catégorie de taille.",
       "L’intégration verticale est une stratégie, pas une classe de taille."],
  exp="ETI signifie entreprise de taille intermédiaire. Les ETI disposent de "
      "moyens financiers plus importants qu’une PME tout en conservant "
      "davantage de flexibilité qu’un grand groupe. Le cours conclut "
      "cependant qu’aucune forme d’entreprise n’est parfaite : chaque "
      "structure possède ses avantages et ses contraintes.",
  diss="Idée à retenir : le capitalisme contemporain n’est pas une course à "
       "la taille unique mais une coexistence de formes."),

f(id='q9-n30', sp='c9-05', niv='raisonner', type='vf', b=756,
  q="La montée des grands groupes a fait des PME un vestige en voie de "
    "disparition dans le capitalisme contemporain.",
  ans=False,
  exp="Le cours part précisément de cette intuition pour la réfuter. Les PME "
      "représentent une part majeure de l’emploi et de la production et "
      "constituent l’essentiel du tissu productif de nombreux pays. Le "
      "capitalisme contemporain repose sur la coexistence entre très grandes "
      "entreprises et petites entreprises, articulées par la sous-traitance, "
      "les firmes-réseaux et les districts industriels.",
  diss="Conclusion générale de la partie : la concentration n’a pas produit "
       "un capitalisme de géants isolés mais une articulation entre grandes "
       "firmes intégrées, réseaux de sous-traitance et effets "
       "d’agglomération."),

# ------------------------------------------------------------- c9-06
f(id='q9-n31', sp='c9-06', niv='connaitre', type='qcm', b=894,
  q="Comment le cours définit-il l’organisation modulaire ?",
  opts=["Une organisation où un seul établissement réalise toutes les étapes "
        "de la production",
        "Une organisation de la production où différentes entreprises "
        "réalisent des modules spécialisés ensuite assemblés",
        "Une organisation par grandes fonctions : production, finance, "
        "marketing",
        "Une organisation où les salariés changent de poste régulièrement"],
  ans=1,
  why=["C’est la description d’une entreprise intégrée, à l’opposé de la "
       "logique modulaire.",
       "L’organisation par grandes fonctions est la forme U de Chandler.",
       "La rotation des postes relève de l’organisation du travail, pas de "
       "l’architecture productive entre firmes."],
  exp="La production fonctionne comme un assemblage de modules spécialisés : "
      "chaque entreprise produit une partie, fournit un composant ou réalise "
      "une tâche précise. Apple en est l’exemple du cours : la firme "
      "travaille avec des dizaines de fournisseurs indépendants répartis dans "
      "plusieurs pays. Cette logique est renforcée par la mondialisation et "
      "la division internationale des processus productifs."),

f(id='q9-n32', sp='c9-06', niv='comprendre', type='qcmm', b=911,
  q="Quels avantages la proximité géographique procure-t-elle aux "
    "entreprises, selon l’analyse des effets d’agglomération ? (plusieurs "
    "réponses)",
  opts=["La circulation des idées et les échanges d’informations",
        "L’innovation",
        "La présence d’une main-d’œuvre qualifiée",
        "Les relations avec les universités et les laboratoires",
        "La suppression de la concurrence entre entreprises voisines"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la proximité facilite la diffusion des connaissances.",
       "Exacte : les effets d’agglomération sont d’abord un facteur "
       "d’innovation.",
       "Exacte : le bassin de main-d’œuvre qualifiée est l’un des avantages "
       "classiques.",
       "Exacte : Stanford joue ce rôle dans la Silicon Valley, par la "
       "formation et la recherche.",
       "Faux : le district industriel combine au contraire concurrence et "
       "coopération."],
  exp="Les effets d’agglomération désignent les avantages liés à la "
      "concentration géographique des activités économiques. La Silicon "
      "Valley en est l’exemple majeur : elle rassemble GAFAM, startups, "
      "investisseurs, laboratoires et universités. Le cours insiste sur le "
      "fait que les universités ne servent pas seulement à former : elles "
      "participent directement à la recherche et à l’innovation "
      "technologique.",
  diss="Attention à ne pas confondre : l’effet d’agglomération n’est pas une "
       "concentration de capital mais une concentration spatiale "
       "d’entreprises distinctes."),

f(id='q9-n33', sp='c9-06', niv='connaitre', type='qcm', b=951,
  q="Quelles dimensions le district industriel marshallien combine-t-il ?",
  opts=["Uniquement la coopération entre entreprises",
        "Concurrence, coopération, spécialisation et innovation",
        "Uniquement la spécialisation productive",
        "Hiérarchie, centralisation et intégration verticale"],
  ans=1,
  why=["La coopération seule ne suffit pas : les entreprises du district "
       "restent concurrentes.",
       "La spécialisation est l’une des dimensions, pas la seule.",
       "Hiérarchie, centralisation et intégration verticale décrivent "
       "l’entreprise intégrée, à l’opposé du district."],
  exp="Le district industriel désigne une concentration locale d’entreprises "
      "spécialisées, reliées entre elles sur un même territoire. Il combine "
      "concurrence, coopération, spécialisation et innovation. Marshall "
      "considère que cette proximité crée une « atmosphère industrielle » "
      "favorable à la croissance. Le cours cite les districts du textile, du "
      "luxe et de la mode en Italie du Nord dans les années 1980.",
  diss="La formule « atmosphère industrielle » est très citable : elle "
       "désigne un actif collectif, immatériel et territorial, que l’on ne "
       "peut pas délocaliser."),

f(id='q9-n34', sp='c9-06', niv='appliquer', type='assoc', b=975,
  q="Associez chaque description à la forme d’organisation correspondante "
    "chez François et Lemercier.",
  ans=[["Réseau d’entreprises de tailles différentes, spécialisées, reliées par des contrats", "Entreprises distribuées"],
       ["Silicon Valley, districts industriels, plateformes numériques", "Entreprises distribuées"],
       ["Très grandes entreprises hiérarchisées, centralisées, intégrées verticalement", "Entreprises intégrées"],
       ["Fordisme et grands conglomérats", "Entreprises intégrées"]],
  exp="François et Lemercier refusent une vision linéaire du capitalisme : "
      "les deux formes coexistent au lieu de se succéder. Les entreprises "
      "distribuées reposent sur la coopération, la complémentarité, la "
      "sous-traitance et la logique de réseau ; les entreprises intégrées sur "
      "une hiérarchie forte et la rationalisation de la production, ce qui "
      "renvoie à l’analyse de Chandler.",
  diss="Thèse à retenir : la taille ne mesure pas la modernité — réseaux et "
       "grands groupes répondent à des exigences différentes."),

f(id='q9-n35', sp='c9-06', niv='raisonner', type='qcm', b=1005,
  q="Pourquoi Amazon est-elle présentée comme combinant les deux logiques "
    "d’organisation ?",
  opts=["Parce qu’elle est à la fois une PME et une grande entreprise",
        "Parce qu’elle intègre verticalement sa logistique tout en "
        "fonctionnant comme une plateforme ouverte à des milliers de PME",
        "Parce qu’elle est à la fois un trust et un cartel",
        "Parce qu’elle appartient à la fois à des actionnaires privés et à "
        "l’État"],
  ans=1,
  why=["La taille d’Amazon n’est pas ambiguë : l’ambivalence porte sur son "
       "mode d’organisation.",
       "Ni trust ni cartel : il n’y a ni direction commune d’entreprises "
       "indépendantes ni entente sur les prix.",
       "La structure de propriété n’est pas en cause dans ce passage."],
  exp="Amazon relève d’une logique intégrée — entrepôts, logistique, "
      "contrôle direct de nombreuses activités, intégration verticale — et "
      "d’une logique distribuée, puisque des milliers de PME utilisent sa "
      "plateforme pour accéder à une clientèle mondiale. Elle est donc à la "
      "fois la firme intégrée et le centre d’un réseau, ce qui illustre le "
      "refus d’une opposition tranchée entre les deux modèles.",
  diss="Exemple idéal pour une conclusion : les formes d’organisation ne se "
       "remplacent pas, elles se combinent au sein d’une même firme."),

f(id='q9-n36', sp='c9-06', niv='raisonner', type='courte', b=1035,
  q="Pourquoi la coexistence des grandes firmes et des PME n’est-elle pas une "
    "simple survivance, mais une organisation productive à part entière ?",
  ans={'modele': "Parce que les PME ne subsistent pas en marge des grandes "
       "firmes : elles sont intégrées à leur fonctionnement. Les grandes "
       "entreprises travaillent avec des sous-traitants, des fournisseurs et "
       "des partenaires spécialisés : c’est la firme-réseau, où le lien est "
       "contractuel et non patrimonial. La production devient modulaire, "
       "chaque entreprise réalisant un module ensuite assemblé, comme chez "
       "Apple et ses dizaines de fournisseurs. La proximité géographique "
       "ajoute des effets d’agglomération — circulation des idées, "
       "main-d’œuvre qualifiée, liens avec les universités — que Marshall "
       "avait déjà repérés dans les districts industriels et que la Silicon "
       "Valley illustre. François et Lemercier en tirent la conclusion "
       "théorique : entreprises distribuées et entreprises intégrées "
       "coexistent durablement parce qu’elles répondent à des exigences "
       "différentes.",
       'cles': [{'f': ['firme reseau', 'sous trait', 'contractuel'],
                 'l': 'la firme-réseau : un lien contractuel, non patrimonial'},
                {'f': ['modulaire', 'module', 'apple'],
                 'l': 'la production modulaire'},
                {'f': ['agglomeration', 'district', 'marshall', 'silicon'],
                 'l': 'les effets d’agglomération et les districts industriels'},
                {'f': ['francois', 'lemercier', 'distribuee', 'integree'],
                 'l': 'la coexistence des entreprises distribuées et intégrées'}]},
  exp="La conclusion du cours est explicite : la concentration des "
      "entreprises n’a pas entraîné la disparition des PME ; le capitalisme "
      "contemporain repose sur l’articulation entre grandes firmes "
      "intégrées, réseaux de sous-traitance et effets d’agglomération "
      "favorisant l’innovation et la spécialisation productive."),

# ------------------------------------------------------------- c9-07
f(id='q9-n37', sp='c9-07', niv='comprendre', type='qcm', b=1074,
  q="Quelle est la grande opposition théorique qui structure la partie sur "
    "les théories de la firme ?",
  opts=["Une firme qui maximise le profit contre une firme qui maximise les "
        "salaires",
        "La firme fonctionne comme le marché, puisqu’elle n’est qu’un "
        "ensemble de contrats, contre la firme existe justement pour échapper "
        "aux limites du marché",
        "La firme publique contre la firme privée",
        "La petite entreprise contre la grande entreprise"],
  ans=1,
  why=["Le partage de la valeur ajoutée n’est pas l’objet de cette "
       "opposition.",
       "La propriété publique ou privée n’intervient pas dans ces deux "
       "approches.",
       "La question de la taille est traitée ailleurs, dans la partie sur les "
       "PME."],
  exp="La première vision, l’approche contractuelle, considère que la firme "
      "n’est qu’un ensemble de contrats : il n’existe pas de différence "
      "fondamentale entre firme et marché. La seconde, l’approche "
      "transactionnelle, affirme que la firme existe précisément parce que le "
      "marché est imparfait et coûteux. La première reste proche de la "
      "théorie néoclassique, la seconde en critique les hypothèses.",
  diss="Question directrice à citer : si le marché fonctionne parfaitement, "
       "pourquoi créer de grandes organisations hiérarchiques ?"),

f(id='q9-n38', sp='c9-07', niv='connaitre', type='qcm', b=1117,
  q="Chez Alchian et Demsetz, quel rôle joue le manager dans la firme conçue "
    "comme un « nœud de contrats » ?",
  opts=["Il exécute les ordres des actionnaires sans marge d’initiative",
        "Il assigne les tâches et il est le « créancier résiduel » : il "
        "perçoit le revenu qui reste une fois tous les apporteurs de facteurs "
        "rémunérés",
        "Il représente les salariés dans la négociation collective",
        "Il fixe les prix de marché des produits de la firme"],
  ans=1,
  why=["L’analyse insiste au contraire sur son pouvoir d’assignation des "
       "tâches et de vente des droits de propriété.",
       "La représentation des salariés n’est pas sa fonction dans ce modèle.",
       "La fixation des prix relève de la structure du marché, pas de la "
       "théorie du nœud de contrats."],
  exp="Pour Alchian et Demsetz, la firme est un nœud de contrats entre des "
      "acteurs aux intérêts divers tenus de travailler ensemble. Le manager "
      "assigne les tâches et il est créancier résiduel : il perçoit ce qui "
      "reste après rémunération de tous les autres apporteurs de facteurs, ce "
      "qui lui donne intérêt à l’efficacité de l’entreprise. Il détient aussi "
      "le pouvoir de vendre l’ensemble des droits de propriété qu’il possède "
      "dans la firme.",
  diss="La notion de créancier résiduel est l’argument incitatif de "
       "l’approche contractuelle : elle explique l’efficacité sans recourir à "
       "l’autorité."),

f(id='q9-n39', sp='c9-07', niv='comprendre', type='qcm', b=1154,
  q="Comment Jensen et Meckling analysent-ils la relation entre actionnaires "
    "et managers ?",
  opts=["Comme un rapport de force collectif entre capital et travail",
        "Comme une relation d’agence entre un principal et un agent, avec une "
        "asymétrie d’information en faveur de l’agent, que le principal "
        "corrige par des incitations",
        "Comme une relation de pure autorité hiérarchique sans contrat",
        "Comme une coopération spontanée fondée sur la confiance"],
  ans=1,
  why=["L’analyse est individuelle et contractuelle, pas en termes de classes "
       "sociales.",
       "L’approche contractuelle refuse précisément de réduire la firme à "
       "l’autorité : tout y est contrat.",
       "La confiance est évoquée dans les prolongements modernes, pas dans le "
       "modèle d’agence."],
  exp="Pour Jensen et Meckling, la firme est un nœud de relations "
      "contractuelles bilatérales, qui s’analysent comme des relations "
      "d’agence : un principal — par exemple l’actionnaire — délègue à un "
      "agent — par exemple le manager —, l’information étant asymétrique en "
      "faveur de l’agent. Par des incitations, le principal fait en sorte que "
      "l’agent serve ses intérêts. La firme devient alors avant tout une "
      "structure de contrôle des comportements.",
  diss="Le cours insiste sur la généralité du mécanisme : la relation "
       "actionnaire-manager n’est qu’une application d’un schéma plus large "
       "de délégation, d’asymétrie d’information et d’incitation."),

f(id='q9-n40', sp='c9-07', niv='comprendre', type='vf', b=1199,
  q="Chez Coase, la comparaison entre coûts de transaction et coûts "
    "d’internalisation permet de déterminer la taille de l’entreprise.",
  ans=True,
  exp="La firme existe parce qu’il y a un coût à recourir au marché — les "
      "coûts de transaction. La comparaison entre ces coûts et les coûts "
      "d’internalisation détermine donc jusqu’où s’étend la firme, sachant "
      "qu’elle cherche à minimiser les coûts de transaction. Avec Coase, la "
      "firme est un mode de coordination centralisé, hiérarchique : "
      "l’entrepreneur agit par autorité, alors que le marché fonctionne par "
      "les prix.",
  diss="Formule efficace : la frontière de la firme est là où "
       "l’internalisation devient plus coûteuse que le recours au marché."),

f(id='q9-n41', sp='c9-07', niv='raisonner', type='qcm', b=1253,
  q="De quoi dépendent les frontières de la firme chez Williamson ?",
  opts=["Du nombre de salariés employés",
        "De la nature des actifs qu’elle gère et de la fréquence des "
        "transactions qu’elle réalise",
        "Du taux d’imposition des bénéfices",
        "De la part de marché détenue par l’entreprise"],
  ans=1,
  why=["L’effectif est une conséquence du périmètre choisi, pas son critère.",
       "La fiscalité n’entre pas dans l’arbitrage décrit par Williamson.",
       "La part de marché relève du pouvoir de marché, pas de la frontière "
       "entre firme et marché."],
  exp="Les frontières de la firme dépendent de la nature des actifs gérés et "
      "de la fréquence des transactions : plus un actif est spécifique et "
      "plus les transactions sont fréquentes, plus l’internalisation devient "
      "avantageuse. Cette approche permet donc d’identifier différentes "
      "stratégies et explique pourquoi certaines firmes choisissent "
      "l’intégration verticale, d’autres des formes hybrides.",
  diss="Nuance à ne pas oublier : Williamson n’impose pas l’intégration — "
       "les formes hybrides sont un résultat de son analyse, non une "
       "exception."),

f(id='q9-n42', sp='c9-07', niv='raisonner', type='qcm', b=1272,
  q="Quelle limite le cours oppose-t-il à l’approche transactionnelle de "
    "Williamson ?",
  opts=["Elle néglige le rôle des prix dans la coordination marchande",
        "En faisant de l’opportunisme le ressort central, elle réduit "
        "l’entreprise à un lieu de triche, alors qu’elle est aussi un lieu de "
        "coopération",
        "Elle suppose une rationalité parfaite des agents",
        "Elle ne s’applique qu’aux entreprises publiques"],
  ans=1,
  why=["Williamson analyse précisément l’alternative entre coordination par "
       "les prix et coordination par l’autorité.",
       "C’est l’inverse : il abandonne la rationalité parfaite au profit de "
       "la rationalité limitée.",
       "Son analyse porte sur toute firme, indépendamment de son statut."],
  exp="Le cours formule deux objections : le comportement opportuniste fait "
      "de l’entreprise un lieu de « triche », alors qu’elle est aussi un lieu "
      "de coopération ; et l’enjeu de l’entreprise n’est peut-être pas "
      "seulement son efficience. La conclusion du chapitre prolonge cette "
      "critique : l’entreprise est à la fois un lieu de coordination et un "
      "lieu de conflictualité.",
  diss="Cette limite ouvre la troisième voie du chapitre : penser "
       "l’entreprise comme organisation, et non seulement comme dispositif "
       "contractuel ou anti-marché."),

]
