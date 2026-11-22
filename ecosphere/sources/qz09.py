# -*- coding: utf-8 -*-
"""Chapitre 9 — Concentration, pouvoir de marché, théories de la firme et
politiques de concurrence."""

SP = {
 'c9-01': 'Concentration, General Electric, cartel de Phoebus, croissance interne et externe',
 'c9-02': 'Les trois formes de concentration : horizontale (Rockefeller), verticale (amont/aval)',
 'c9-03': 'Conglomérat, décote de conglomérat et causes de la concentration',
 'c9-04': 'Les dangers de la concentration : fiscal, économique, politique, souveraineté, trust',
 'c9-05': 'Les PME : forces, faiblesses, « too big to fail », ETI',
 'c9-06': 'Firme-réseau, effets d’agglomération, districts industriels, François et Lemercier',
 'c9-07': 'Théories de la firme : approche contractuelle et approche transactionnelle',
 'c9-08': 'La firme néoclassique, le travail en équipe, nœud de contrats, faire ou faire faire',
 'c9-09': 'Pouvoir de marché et abus de position dominante : vente liée, prix prédateurs',
 'c9-10': 'Les sources du pouvoir de marché : différenciation, Chamberlin, monopole discriminant',
 'c9-11': 'Cartels et ententes : Combe, dilemme du prisonnier, clémence, parallélisme',
 'c9-12': 'Barrières à l’entrée et marchés contestables (Baumol, Panzar, Willig)',
 'c9-13': 'Économie industrielle : modèle SCP, indice de Lerner, approches standard et élargie',
 'c9-14': 'Les politiques de concurrence : antitrust, TFUE, Autorité de la concurrence, DMA',
 'c9-15': 'Démantèlement et conclusion : RSE, coopération et conflit, Simon, Chandler',
}

# Questions écartées : chacune reprend à l'identique, sous forme de vrai/faux
# inversé, une question déjà posée en QCM — ce n'est pas une question
# réellement distincte.
DROP = [
 'ch9-vf-3',    # ≡ ch9-qcm-20 (la position dominante n'est pas condamnée)
 'ch9-vf-5',    # ≡ ch9-qcm-17 (le dilemme du prisonnier et l'instabilité)
 'ch9-vf-8',    # ≡ ch9-qcm-29 (le brevet, barrière tolérée)
 'ch9-vf-10',   # ≡ ch9-qcm-33 (approche élargie et contestabilité)
 'ch9-vf-11',   # ≡ ch9-qcm-26 (différenciation et élasticité-prix)
 'ch9-vf-18',   # ≡ ch9-qcm-41 (forme U / forme M)
 'ch9-qcm-11',  # ≡ ch9-qcm-12 (même bloc, même réponse, même formulation)
]


def f(**kw):
    return kw


FIX = {

# =============================================================== c9-01
'ch9-qcm-1': f(niv='connaitre', sp='c9-01', b=44,
 exp="La concentration désigne le processus par lequel les entreprises "
     "augmentent leur taille : par rachats, fusions, regroupements, prises de "
     "participation ou alliances. Elle s’accompagne d’une augmentation des "
     "capacités de production et d’une réduction du nombre d’acteurs présents "
     "sur le marché.",
 why=["La concentration n’est pas une réduction d’effectifs : c’est un "
      "mouvement de croissance de la firme.",
      "La spécialisation sur un seul produit est le contraire de la "
      "diversification conglomérale : ce n’est pas la définition de la "
      "concentration.",
      "La baisse des prix peut être une conséquence possible des économies "
      "d’échelle, jamais la définition du phénomène."],
 diss="Point de départ du chapitre : la théorie suppose des entreprises "
      "nombreuses et petites, la réalité observe des firmes qui grandissent "
      "sans cesse."),
'ch9-qcm-2': f(niv='comprendre', sp='c9-01', b=147,
 exp="La croissance interne, dite aussi croissance organique, repose sur les "
     "investissements propres de l’entreprise : elle construit de nouvelles "
     "usines, embauche, développe de nouveaux produits. Elle augmente ses "
     "capacités de production sans racheter d’autre firme. Le cours prend "
     "l’exemple d’Amazon.",
 why=["Le rachat de concurrents est précisément la définition de la "
      "croissance externe.",
      "Une entente avec les fournisseurs relève de la coordination entre "
      "firmes, pas d’un mode de croissance.",
      "La vente d’actifs réduit la taille de l’entreprise : c’est une "
      "cession, non une croissance."]),
'ch9-qcm-3': f(niv='comprendre', sp='c9-01', b=159,
 exp="La croissance externe passe par la fusion ou le rachat d’entreprises "
     "existantes. Son intérêt est la rapidité : l’entreprise acquiert d’un "
     "coup des capacités de production, des marques, une clientèle et des "
     "parts de marché qu’il aurait fallu des années à construire.",
 why=["L’autofinancement finance des investissements propres : c’est le "
      "levier de la croissance interne.",
      "L’embauche de salariés accroît les capacités de l’entreprise "
      "elle-même : croissance interne.",
      "L’innovation de procédé transforme la production interne ; elle ne "
      "fait pas changer la firme de périmètre."]),
'ch9-qcm-4': f(niv='connaitre', sp='c9-01', b=176,
 exp="La concentration horizontale réunit des entreprises aux activités "
     "similaires, donc concurrentes directes. Sa logique est double : réduire "
     "l’intensité de la concurrence et réaliser des économies d’échelle en "
     "répartissant les coûts fixes sur une production plus importante. Le "
     "cours cite LVMH-Tiffany et FDJ-Kindred.",
 why=["Le lien de famille entre dirigeants ne définit aucune forme de "
      "concentration économique.",
      "Les entreprises situées en amont et en aval relèvent de la "
      "concentration verticale.",
      "L’appartenance à des pays différents décrit une opération "
      "transfrontalière, pas une forme de concentration."]),
'ch9-qcm-6': f(niv='connaitre', sp='c9-01', b=189,
 exp="La concentration conglomérale regroupe des entreprises sans lien direct "
     "entre leurs activités. L’objectif n’est plus de contrôler un marché ou "
     "une chaîne de production mais de diversifier les risques : si un secteur "
     "fonctionne mal, les autres peuvent compenser. Samsung et General "
     "Electric en sont les exemples du cours.",
 why=["La fusion entre concurrents directs est la concentration "
      "horizontale.",
      "L’intégration en amont, vers les fournisseurs, est la concentration "
      "verticale.",
      "Une entente sur les prix est un cartel : les entreprises restent "
      "indépendantes, il n’y a pas de regroupement de capital."]),
'ch9-qcm-8': f(niv='connaitre', sp='c9-01', b=85,
 exp="Le cartel de Phoebus réunit General Electric, Osram et Philips, "
     "principalement entre 1929 et 1939, autour des ampoules électriques. Les "
     "membres fixent des quotas de production, se répartissent "
     "géographiquement les marchés et limitent la durée de vie des lampes.",
 why=["Le pétrole renvoie à Rockefeller et à la Standard Oil, autre exemple "
      "du chapitre, mais pas à un cartel international de ce type.",
      "L’automobile sert au chapitre d’exemple de concentration horizontale "
      "et de différenciation, pas de cartel.",
      "Le textile n’est pas mobilisé ici ; il appartient au chapitre sur les "
      "révolutions industrielles."]),
'ch9-qcm-9': f(niv='comprendre', sp='c9-01', b=105,
 exp="L’obsolescence programmée consiste à réduire volontairement la durée de "
     "vie d’un produit afin de pousser le consommateur à le racheter. Le "
     "cartel de Phoebus ramène ainsi la durée de vie des ampoules d’environ "
     "2 000 heures à environ 1 000 heures : limiter la qualité permet de "
     "soutenir la demande et les prix.",
 why=["Améliorer la durabilité est exactement l’inverse de l’obsolescence "
      "programmée.",
      "La baisse des prix n’a rien à voir : le cartel cherche au contraire à "
      "maintenir des prix élevés.",
      "Breveter une innovation protège une invention ; cela ne dégrade pas "
      "volontairement un produit."],
 diss="Exemple très rentable : il montre qu’une entente peut nuire au "
      "consommateur autrement que par le prix — par la qualité et la "
      "durabilité du produit."),
'ch9-qcm-13': f(niv='connaitre', sp='c9-01', b=207,
 exp="Un monopole naturel correspond à la situation dans laquelle une seule "
     "entreprise est plus efficace que plusieurs entreprises concurrentes. "
     "Cela arrive lorsque les coûts fixes sont très élevés : dupliquer les "
     "infrastructures — rails, réseaux électriques, télécommunications — "
     "serait trop coûteux.",
 why=["C’est l’inverse : si plusieurs entreprises étaient plus efficaces, il "
      "n’y aurait aucune raison de tolérer le monopole.",
      "Le monopole naturel tient à la structure des coûts, pas à une "
      "interdiction juridique : un monopole légal est autre chose.",
      "Des coûts fixes nuls rendraient au contraire l’entrée très facile et "
      "le marché très concurrentiel."]),
'ch9-qcm-15': f(niv='connaitre', sp='c9-01', b=90,
 exp="Le cartel est une entente entre entreprises indépendantes qui cherchent "
     "à limiter la concurrence en fixant ensemble les prix, les quantités ou "
     "le partage du marché. Point essentiel : ce n’est pas une fusion ni un "
     "rachat — chaque entreprise reste juridiquement indépendante mais se "
     "coordonne comme un « monopole à plusieurs ».",
 why=["Une fusion fait disparaître juridiquement les entreprises "
      "absorbées : le cartel les laisse exister.",
      "Une aide publique est un transfert de l’État, pas un accord entre "
      "firmes.",
      "Un brevet collectif organiserait un partage de droits de propriété "
      "intellectuelle, non un partage de marché."]),
'ch9-qcm-23': f(niv='comprendre', sp='c9-01', b=168,
 exp="La différenciation verticale consiste à proposer des produits de "
     "qualités et de prix différents afin de toucher plusieurs catégories de "
     "consommateurs. Les consommateurs peuvent classer les produits selon une "
     "hiérarchie de qualité : le produit le plus cher est présenté comme "
     "meilleur, ce qui justifie l’écart de prix.",
 why=["La couleur est une caractéristique secondaire : elle relève de la "
      "différenciation horizontale.",
      "La localisation du point de vente est l’exemple type de "
      "différenciation horizontale donné par le cours.",
      "L’image de marque seule ne suffit pas : la différenciation verticale "
      "suppose une hiérarchie objective de gamme."]),
'ch9-vf-2': f(niv='comprendre', sp='c9-01', b=147,
 exp="C’est la croissance externe qui repose sur les fusions et les rachats. "
     "La croissance interne mobilise les investissements propres de "
     "l’entreprise : nouvelles usines, embauches, nouveaux produits. Les deux "
     "se distinguent par la vitesse : la croissance externe permet un "
     "changement de taille immédiat, la croissance interne est progressive.",
 diss="Confusion la plus fréquente du chapitre : retenir « interne = "
      "j’investis moi-même », « externe = j’achète quelqu’un d’autre »."),
'ch9-vf-4': f(niv='comprendre', sp='c9-01', b=105,
 exp="Les fabricants réunis dans le cartel de Phoebus limitent volontairement "
     "la durée de vie des ampoules, d’environ 2 000 heures à environ 1 000 "
     "heures, pour pousser au rachat. Le cartel est donc devenu l’exemple "
     "historique le plus célèbre d’obsolescence programmée organisée par une "
     "entente."),
'ch9-vf-7': f(niv='comprendre', sp='c9-01', b=207,
 exp="Le monopole naturel se justifie précisément par l’importance des coûts "
     "fixes : quand les infrastructures coûtent très cher, une seule "
     "entreprise produit plus efficacement que plusieurs, car dupliquer les "
     "réseaux serait un gaspillage. C’est la raison pour laquelle certains "
     "monopoles sont autorisés par les autorités de concurrence.",
 diss="À articuler avec les effets de réseau : coûts fixes élevés et effets "
      "de réseau donnent au premier entrant un avantage durable."),
'ch9-vf-19': f(niv='connaitre', sp='c9-01', b=226,
 exp="La Commission européenne a refusé la fusion en 2019. Les deux groupes "
     "invoquaient la création d’un « champion européen » capable de "
     "concurrencer les entreprises chinoises ; la Commission a estimé que "
     "l’opération créerait une position dominante sur le marché ferroviaire "
     "européen. Tout dépend du marché pertinent retenu : européen ou mondial.",
 diss="Exemple central du débat sur l’échelle de la concurrence : une firme "
      "peut être dominante en Europe et concurrencée au niveau mondial."),
'ch9-open-1': f(niv='comprendre', sp='c9-01', b=146,
 exp="La croissance interne repose sur les investissements propres de "
     "l’entreprise : elle augmente ses capacités de production, embauche et "
     "développe de nouveaux produits sans racheter d’autre firme — c’est "
     "l’exemple d’Amazon développant ses propres entrepôts et services. La "
     "croissance externe passe au contraire par la fusion ou le rachat "
     "d’entreprises existantes, ce qui permet une augmentation de taille "
     "beaucoup plus rapide : William Durant construit General Motors en "
     "rachetant Buick, Chevrolet et Cadillac.",
 diss="La croissance externe est aussi le point d’entrée des politiques de "
      "concurrence : seules les fusions-acquisitions sont soumises au "
      "contrôle des concentrations."),
'ch9-open-6': f(niv='comprendre', sp='c9-10', b=1678,
 exp="La différenciation verticale repose sur des différences de qualité : "
     "pour un même type de produit il existe plusieurs niveaux de gamme, et "
     "les consommateurs peuvent les classer selon une hiérarchie, ce qui "
     "justifie des écarts de prix. La différenciation horizontale repose sur "
     "des caractéristiques secondaires : style, goût, couleur, localisation. "
     "Les produits sont globalement équivalents mais ne plaisent pas aux mêmes "
     "consommateurs, comme dans l’exemple des agendas ou du commerce de "
     "proximité. Dans les deux cas, la différenciation réduit la "
     "substituabilité entre les biens.",
 diss="Les deux formes débouchent sur le même résultat : une demande moins "
      "élastique, donc un pouvoir de marché — c’est le mécanisme de la "
      "concurrence monopolistique de Chamberlin."),
'ch9-aut195-2': f(niv='connaitre', sp='c9-01', b=162,
 exp="William Durant développe General Motors par croissance externe, en "
     "rachetant Buick, Chevrolet et Cadillac. La croissance externe lui "
     "procure d’un coup des capacités de production, des marques et des "
     "clientèles ; ces marques permettent ensuite une différenciation "
     "verticale, de Chevrolet à Cadillac, pour couvrir plusieurs segments de "
     "prix.",
 why=["La construction de nouvelles usines serait de la croissance interne : "
      "ce n’est pas la méthode de Durant.",
      "Le cours n’évoque aucune alliance entre General Motors et Ford.",
      "L’introduction en bourse est un mode de financement, pas un mode de "
      "croissance."]),

# =============================================================== c9-02
'ch9-qcm-5': f(niv='connaitre', sp='c9-02', b=344,
 exp="La concentration verticale regroupe des entreprises aux activités "
     "complémentaires, situées à différentes étapes de la production. "
     "L’entreprise cherche à maîtriser la chaîne de l’amont — fournisseurs, "
     "matières premières, consommations intermédiaires — à l’aval — "
     "distribution, vente, consommateur final.",
 why=["Racheter un concurrent direct relève de la concentration "
      "horizontale.",
      "Diversifier ses activités sans lien entre elles est la concentration "
      "conglomérale.",
      "Réduire sa taille est l’inverse : c’est une cession ou une scission."],
 diss="Les deux justifications économiques à retenir : sécuriser les "
      "approvisionnements et supprimer les marges des intermédiaires "
      "(Rockefeller et ses tonneaux, de 2,5 à 1 dollar)."),
'ch9-open-2': f(niv='comprendre', sp='c9-02', b=280,
 exp="La concentration horizontale réunit des entreprises aux activités "
     "similaires, donc concurrentes directes, afin d’accroître les parts de "
     "marché, de réduire l’intensité de la concurrence et de réaliser des "
     "économies d’échelle : Rockefeller rachetant ses concurrents du "
     "raffinage, LVMH rachetant Tiffany. La concentration verticale regroupe "
     "des activités complémentaires et permet de contrôler plusieurs étapes "
     "de la chaîne, en amont vers les fournisseurs ou en aval vers la "
     "distribution : Rockefeller fabriquant ses propres tonneaux, Amazon "
     "rachetant MGM et iRobot. La concentration conglomérale regroupe des "
     "activités sans lien direct, dans une logique de diversification des "
     "risques : Samsung.",
 diss="Les trois formes ne répondent pas aux mêmes objectifs : pouvoir de "
      "marché, maîtrise de la chaîne, dispersion du risque."),

# =============================================================== c9-03
'ch9-qcm-7': f(niv='comprendre', sp='c9-03', b=457,
 exp="La décote de conglomérat désigne une situation où la valeur boursière "
     "d’un groupe diversifié est inférieure à la somme de la valeur de "
     "chacune de ses activités prises séparément. Les investisseurs préfèrent "
     "des entreprises spécialisées, plus lisibles ; les groupes se scindent "
     "donc ou se recentrent, comme General Electric séparé en plusieurs pôles.",
 why=["Une baisse des coûts de production serait un gain d’efficacité, pas "
      "une sanction boursière.",
      "La décote n’a rien de fiscal : elle est un jugement du marché "
      "financier.",
      "C’est l’inverse d’une hausse du cours : la diversification pénalise "
      "ici la valorisation."],
 diss="À relier au capitalisme actionnarial : la priorité donnée à la valeur "
      "pour l’actionnaire peut conduire à démanteler des groupes "
      "industriellement cohérents."),
'ch9-qcm-30': f(niv='connaitre', sp='c9-03', b=511,
 exp="Les effets de réseau signifient que la valeur d’une plateforme augmente "
     "avec le nombre de ses utilisateurs : plus elle est utilisée, plus elle "
     "devient attractive, donc plus elle attire d’utilisateurs. Ce mécanisme "
     "cumulatif favorise l’émergence de gigantesques plateformes mondiales "
     "(GAFAM, BATX, NATU) et verrouille le marché au profit du premier entrant.",
 why=["Des coûts qui augmentent avec la production décrivent des rendements "
      "décroissants : c’est l’inverse de la logique des plateformes.",
      "Rien n’impose une baisse mécanique des prix ; la position dominante "
      "permet au contraire de les tenir.",
      "L’inélasticité de la demande peut être une conséquence du "
      "verrouillage, pas la définition des effets de réseau."]),
'ch9-aut195-3': f(niv='connaitre', sp='c9-03', b=563,
 exp="Suzanne Berger montre qu’il existe une première mondialisation entre "
     "1870 et 1914, fondée sur la division internationale du travail : chaque "
     "pays se spécialise dans un produit, selon la logique ricardienne. La "
     "mondialisation contemporaine repose au contraire sur la division "
     "internationale des processus productifs : un même produit est fabriqué "
     "dans plusieurs pays, comme l’iPhone dont les composants viennent de "
     "partout et l’assemblage de Chine.",
 why=["L’opposition finance / commerce n’est pas celle que retient le cours.",
      "L’échelle régionale ou globale n’est pas le critère de distinction "
      "employé ici.",
      "Les deux mondialisations concernent toutes deux des biens : ce n’est "
      "pas l’opposition biens / services."],
 diss="Enjeu pour le chapitre : la DIPP impose aux firmes une taille "
      "internationale et rend les dépendances séquentielles, donc la "
      "concentration plus probable."),

# =============================================================== c9-04
'ch9-qcm-12': f(niv='connaitre', sp='c9-04', b=698,
 exp="Le pouvoir de marché correspond à la capacité d’une entreprise à "
     "influencer les prix ou les quantités, et plus largement l’accès des "
     "concurrents au marché. En concurrence pure et parfaite il n’existe pas : "
     "l’entreprise est price taker. En concurrence imparfaite, certaines "
     "firmes deviennent price makers.",
 why=["Produire au coût le plus bas est un avantage de compétitivité : cela "
      "peut donner un pouvoir de marché, ce n’en est pas la définition.",
      "La liberté d’embauche relève du droit du travail, non de la structure "
      "du marché.",
      "Exporter est une stratégie de débouchés, sans rapport direct avec le "
      "pouvoir sur les prix."]),
'ch9-qcm-14': f(niv='connaitre', sp='c9-04', b=682,
 exp="Le trust est une forme particulière de concentration : les entreprises "
     "restent juridiquement indépendantes mais confient leur direction à une "
     "structure centrale commune. Il se distingue donc de la fusion "
     "classique, dans laquelle les entreprises absorbées disparaissent "
     "juridiquement.",
 why=["Le trust n’est pas un impôt : la confusion vient du vocabulaire "
      "« antitrust ».",
      "Il ne s’agit pas d’une organisation de salariés mais d’un "
      "regroupement d’entreprises.",
      "Une autorité de régulation combat les trusts : elle n’en est pas un."],
 diss="Mot-clé des lois antitrust américaines : Sherman Act 1890, Clayton "
      "Act 1914 — le droit se construit contre cette forme précise de "
      "concentration."),

# =============================================================== c9-05
'ch9-vf-13': f(niv='comprendre', sp='c9-05', b=763,
 exp="La montée des grands groupes n’a pas supprimé les PME : elles "
     "représentent une part majeure de l’emploi et de la production et "
     "constituent l’essentiel du tissu productif de nombreux pays. Le "
     "capitalisme contemporain repose sur la coexistence entre très grandes "
     "firmes et petites entreprises, articulées par la sous-traitance et les "
     "réseaux.",
 diss="Résultat central de la partie : la concentration ne produit pas un "
      "capitalisme uniforme de géants, mais une articulation de formes "
      "d’entreprise différentes."),
'ch9-vf-14': f(niv='comprendre', sp='c9-06', b=903,
 exp="La firme-réseau est une organisation dans laquelle une grande "
     "entreprise coordonne un ensemble de partenaires et de sous-traitants "
     "spécialisés. Le lien n’est pas la propriété du capital mais le contrat : "
     "la grande firme est à la fois une très grande entreprise et le centre "
     "d’un vaste réseau d’entreprises qu’elle ne possède pas.",
 diss="Différence décisive avec l’intégration verticale : dans la "
      "firme-réseau, la coordination reste contractuelle, pas hiérarchique."),
'ch9-open-10': f(niv='raisonner', sp='c9-05', b=779,
 exp="Les PME conservent des atouts liés à leur petite taille : une "
     "organisation hiérarchique simple avec peu de niveaux, des circuits de "
     "décision rapides sans lourdeur administrative, une proximité avec les "
     "clients et le marché local qui permet de détecter vite les changements "
     "de demande, et donc une forte réactivité à la conjoncture. Elles "
     "présentent en revanche des fragilités : moyens financiers limités, "
     "accès difficile aux marchés financiers et forte dépendance bancaire, "
     "difficulté à exporter, sensibilité aux retournements de conjoncture. "
     "Alors que certaines très grandes entreprises sont jugées « too big to "
     "fail », les PME servent parfois de variable d’ajustement.",
 diss="Les ETI, entreprises de taille intermédiaire, sont présentées comme la "
      "tentative de combiner souplesse des PME et moyens des grands groupes."),
'ch9-open-11': f(niv='comprendre', sp='c9-06', b=903,
 exp="La firme-réseau est une grande entreprise reliée à un ensemble de PME "
     "et de partenaires par des relations contractuelles plutôt que par la "
     "propriété : elle coordonne un réseau productif de sous-traitants "
     "spécialisés. Elle repose sur une production modulaire, où différentes "
     "entreprises réalisent des modules ensuite assemblés, logique renforcée "
     "par la mondialisation et la division internationale des processus "
     "productifs. Amazon combine d’ailleurs les deux logiques : intégration "
     "verticale de ses entrepôts et de sa logistique, et plateforme ouverte à "
     "des milliers de PME.",
 diss="À rapprocher de François et Lemercier : entreprises distribuées et "
      "entreprises intégrées coexistent au lieu de se succéder."),

# =============================================================== c9-06
'ch9-vf-15': f(niv='connaitre', sp='c9-06', b=944,
 exp="Dans ses Principes d’économie politique, publiés en 1890, Alfred "
     "Marshall développe la notion de district industriel : une concentration "
     "locale d’entreprises spécialisées, de compétences et d’institutions. Il "
     "considère que cette proximité crée une « atmosphère industrielle » "
     "favorable à la croissance. Le cours cite les districts de l’Italie du "
     "Nord dans les années 1980.",
 diss="Marshall permet de montrer que les effets d’agglomération ne sont pas "
      "une nouveauté de la Silicon Valley : ils sont observés dès le "
      "XIXe siècle."),
'ch9-aut195-1': f(niv='comprendre', sp='c9-06', b=970,
 exp="François et Lemercier refusent une vision linéaire du capitalisme : les "
     "entreprises distribuées — réseaux d’entreprises de tailles différentes, "
     "spécialisées, reliées par des contrats — et les entreprises intégrées — "
     "très grandes, hiérarchisées, centralisées, intégrées verticalement — "
     "coexistent durablement parce qu’elles répondent à des exigences "
     "différentes. La taille ne mesure donc pas la modernité.",
 why=["Ils prolongent au contraire l’analyse marshallienne des districts "
      "industriels.",
      "Les coûts de transaction relèvent de Coase et Williamson : ce n’est "
      "pas la cible de leur critique.",
      "Ils ne discutent pas l’intérêt de la croissance externe mais la "
      "chronologie des formes d’organisation."]),

# =============================================================== c9-07
'ch9-qcm-38': f(niv='connaitre', sp='c9-07', b=1190,
 exp="Les coûts de transaction correspondent aux coûts liés au recours au "
     "marché : recherche d’information, négociation, rédaction des contrats, "
     "contrôle de leur exécution, règlement des litiges. Ce sont eux qui "
     "expliquent, chez Coase puis Williamson, pourquoi il peut être moins "
     "coûteux d’internaliser une activité que de l’acheter.",
 why=["Les coûts de production en usine sont des coûts techniques : ils "
      "existent quel que soit le mode de coordination.",
      "Les salaires sont un coût de production du facteur travail ; seuls "
      "les coûts d’embauche, de contrôle et de contractualisation sont des "
      "coûts de transaction.",
      "Les impôts sont un prélèvement public, sans lien avec la coordination "
      "marchande."]),
'ch9-qcm-39': f(niv='comprendre', sp='c9-07', b=1270,
 exp="Pour Williamson, la firme constitue une alternative au marché parce "
     "qu’elle permet de réduire les coûts de transaction, l’incertitude et "
     "l’opportunisme. Ses deux hypothèses centrales sont la rationalité "
     "limitée, reprise d’Herbert Simon, qui rend les contrats incomplets, et "
     "l’opportunisme des agents, qui rend le recours au marché risqué.",
 why=["La firme n’existe pas pour réduire les salaires : l’internalisation "
      "les augmente souvent (cotisations, formation, congés).",
      "La fiscalité n’entre pas dans l’arbitrage faire / faire faire décrit "
      "par Williamson.",
      "Les prix de vente relèvent de la stratégie commerciale, pas de la "
      "frontière de la firme."],
 diss="Formule à retenir : la comparaison entre coûts de transaction et coûts "
      "d’internalisation détermine la taille de l’entreprise."),
'ch9-vf-16': f(niv='comprendre', sp='c9-07', b=1200,
 exp="Avec Coase, la firme est un mode de coordination centralisé, "
     "hiérarchique : l’entrepreneur agit par autorité, alors que le marché "
     "fonctionne par les prix. La firme est donc par nature différente du "
     "marché, et elle existe parce que le recours au marché a un coût. C’est "
     "précisément ce que l’approche contractuelle contestera.",
 diss="Opposition structurante du chapitre : firme ≈ marché (Alchian, "
      "Demsetz, Jensen, Meckling) contre firme ≠ marché (Coase, Williamson)."),
'ch9-vf-17': f(niv='comprendre', sp='c9-07', b=1154,
 exp="L’asymétrie d’information fonde bien la théorie de l’agence. Pour "
     "Jensen et Meckling, la firme est un nœud de relations contractuelles "
     "bilatérales qui s’analysent comme des relations d’agence entre un "
     "principal — par exemple l’actionnaire — et un agent — par exemple le "
     "manager —, l’information étant asymétrique en faveur de l’agent. Le "
     "principal doit donc mettre en place des incitations.",
 diss="Le cours insiste sur la généralité du mécanisme : la relation "
      "actionnaire-manager n’est qu’une application d’un schéma plus large de "
      "délégation et d’incitation."),
'ch9-open-12': f(niv='comprendre', sp='c9-07', b=1251,
 exp="Les coûts de transaction sont les coûts liés au recours au marché : "
     "recherche d’information, négociation, rédaction et contrôle des "
     "contrats. Pour Williamson, l’entreprise internalise une activité "
     "lorsque ces coûts deviennent trop élevés. Deux hypothèses fondent le "
     "raisonnement : la rationalité limitée, reprise d’Herbert Simon, qui "
     "rend les contrats nécessairement incomplets puisque les agents ne "
     "peuvent pas tout prévoir ; et l’opportunisme, qui pousse les agents à "
     "exploiter les silences du contrat. Les frontières de la firme dépendent "
     "alors de la nature des actifs gérés et de la fréquence des transactions, "
     "ce qui explique l’intégration verticale — ou le choix de formes "
     "hybrides.",
 diss="La concentration verticale devient ainsi une réponse économique aux "
      "coûts de transaction, et non une simple volonté de puissance."),
'ch9-open-13': f(niv='raisonner', sp='c9-07', b=1168,
 exp="L’approche contractuelle, développée par Alchian et Demsetz puis Jensen "
     "et Meckling, considère que la firme est un « nœud de contrats » : marché "
     "et firme reposent tous deux sur des contrats passés entre individus "
     "rationnels, la firme ajoutant seulement des contrats de travail aux "
     "contrats commerciaux. Il n’y a donc pas de différence de nature, et "
     "cette approche reste proche de la théorie néoclassique. L’approche "
     "transactionnelle, issue de Coase et prolongée par Williamson, affirme au "
     "contraire que la firme existe précisément parce que le marché est "
     "imparfait et coûteux : elle coordonne par l’autorité quand le marché "
     "coordonne par les prix. Sa limite, soulignée par le cours : en faisant "
     "de l’opportunisme le ressort central, elle réduit l’entreprise à un lieu "
     "de triche, alors qu’elle est aussi un lieu de coopération.",
 diss="Plan possible en dissertation : la firme comme marché / la firme "
      "contre le marché / la firme comme organisation, qui dépasse les deux."),

# =============================================================== c9-09
'ch9-qcm-10': f(niv='connaitre', sp='c9-09', b=1507,
 exp="En concurrence pure et parfaite, aucune entreprise ne peut influencer "
     "le marché : elle est preneuse de prix, price taker. Les prix "
     "s’imposent à elle comme une donnée. En concurrence imparfaite, certaines "
     "entreprises deviennent au contraire price makers et peuvent fixer ou "
     "influencer les prix.",
 why=["« Donneuse de prix » (price maker) caractérise la concurrence "
      "imparfaite, pas le modèle de concurrence parfaite.",
      "Le monopole est la situation opposée : un offreur unique disposant "
      "d’un pouvoir sur les prix.",
      "Un brevet confère un monopole temporaire : il est incompatible avec "
      "l’atomicité supposée."]),
'ch9-qcm-20': f(niv='comprendre', sp='c9-09', b=1528,
 exp="La position dominante n’est pas condamnée en elle-même : une entreprise "
     "peut être dominante parce qu’elle a innové, réduit ses coûts ou mieux "
     "satisfait les consommateurs. Ce que sanctionnent les autorités, c’est "
     "l’abus de position dominante, c’est-à-dire l’utilisation de cette "
     "domination pour éliminer les concurrents ou empêcher leur entrée.",
 why=["La position dominante n’est pas interdite : ce serait sanctionner la "
      "réussite économique.",
      "Elle n’est donc pas toujours sanctionnée — seul l’abus l’est.",
      "Elle n’a rien de propre aux monopoles publics : les plateformes "
      "numériques privées en sont l’illustration contemporaine."],
 diss="Critère pratique donné par le cours : l’entreprise dominante ne pose "
      "pas problème si elle se comporte comme si elle était en concurrence."),
'ch9-qcm-21': f(niv='connaitre', sp='c9-09', b=1546,
 exp="La vente liée consiste à vendre plusieurs produits ensemble en "
     "empêchant le consommateur de les acheter séparément : l’entreprise "
     "utilise sa domination sur un produit pour imposer un autre produit. "
     "Elle n’est pas toujours négative — une voiture vendue avec ses pneus — "
     "et ne devient anticoncurrentielle que lorsqu’elle ferme l’accès au "
     "marché aux concurrents.",
 why=["Vendre à perte pour éliminer les concurrents, c’est la pratique des "
      "prix prédateurs.",
      "Vendre à l’étranger est une stratégie d’exportation, sans rapport "
      "avec un abus.",
      "La vente en ligne est un canal de distribution, pas une pratique "
      "anticoncurrentielle."],
 diss="Exemples du cours : Microsoft avec son système d’exploitation, Google "
      "avec ses services intégrés."),
'ch9-qcm-22': f(niv='comprendre', sp='c9-09', b=1571,
 exp="Les prix prédateurs consistent à pratiquer des prix très bas, voire à "
     "vendre temporairement à perte, afin d’éliminer les concurrents puis de "
     "remonter les prix. L’indice retenu par le cours est un prix inférieur au "
     "coût variable moyen : en dessous de ce seuil, l’entreprise ne couvre même "
     "plus ses coûts courants, la baisse ne peut donc pas s’expliquer par une "
     "logique productive normale.",
 why=["Un prix supérieur au coût total correspond à une activité rentable : "
      "rien d’anticoncurrentiel.",
      "Un prix administré par l’État relève de la réglementation, pas de la "
      "stratégie de la firme.",
      "Un prix stable n’indique aucune stratégie d’éviction."],
 diss="À manier avec prudence : le cours insiste sur l’ambiguïté — la riposte "
      "des compagnies traditionnelles aux low-cost a été jugée concurrence "
      "normale."),
'ch9-qcm-28': f(niv='connaitre', sp='c9-12', b=2221,
 exp="Les coûts irrécupérables, ou sunk costs, sont les coûts qu’une "
     "entreprise ne peut pas récupérer si elle quitte le marché : "
     "investissements spécifiques, installations non revendables, dépenses de "
     "lancement. Leur importance est ce qui rend l’entrée risquée : un marché "
     "n’est réellement contestable qu’en l’absence de coûts irrécupérables "
     "importants.",
 why=["C’est exactement l’inverse : s’ils étaient récupérables, ils ne "
      "seraient pas une barrière.",
      "Ils ne sont pas définis par leur caractère variable : beaucoup sont "
      "des coûts fixes d’investissement.",
      "Un financement public ne change pas leur nature ; il peut au mieux en "
      "réduire le poids."]),
'ch9-open-5': f(niv='comprendre', sp='c9-09', b=1512,
 exp="La position dominante décrit le fait de disposer d’un pouvoir de marché "
     "important : capacité d’influencer les prix, les quantités ou l’accès des "
     "concurrents au marché. Elle n’est pas condamnée en elle-même, car elle "
     "peut résulter d’une réussite économique — innovation, baisse des coûts, "
     "satisfaction des consommateurs. L’abus apparaît lorsque l’entreprise "
     "utilise cette domination pour éliminer ses concurrents, les empêcher "
     "d’entrer ou leur imposer des conditions défavorables. Le cours en "
     "détaille les formes : vente liée, prix prédateurs, pratiques "
     "discriminatoires, dénigrement, accords d’exclusivité, exploitation d’un "
     "avantage historique comme le fichier client d’Engie.",
 diss="Articulation juridique à citer : article 102 du TFUE pour l’abus, "
      "article 101 pour les ententes."),

# =============================================================== c9-10
'ch9-qcm-24': f(niv='comprendre', sp='c9-10', b=1693,
 exp="La différenciation horizontale repose sur des différences de "
     "caractéristiques secondaires : style, goût, couleur, image, "
     "localisation. Les produits sont globalement équivalents en qualité mais "
     "ne plaisent pas aux mêmes consommateurs. L’exemple de la localisation "
     "est explicite : un commerce proche crée une valeur supplémentaire sans "
     "que le produit soit meilleur.",
 why=["La qualité objective, hiérarchisable, définit la différenciation "
      "verticale.",
      "Le coût de production est une donnée interne : il ne définit aucune "
      "forme de différenciation.",
      "Le taux de marge est un résultat de la différenciation, pas son "
      "support."]),
'ch9-qcm-25': f(niv='connaitre', sp='c9-10', b=1730,
 exp="Edward Chamberlin développe en 1933 l’analyse de la concurrence "
     "monopolistique : plusieurs entreprises sont en concurrence, mais chacune "
     "cherche à rendre son produit unique afin de se comporter comme un petit "
     "monopole sur sa clientèle. L’entreprise est donc à la fois en "
     "concurrence et détentrice d’un pouvoir de marché, grâce à la "
     "différenciation.",
 why=["Schumpeter analyse l’innovation et la destruction créatrice, non la "
      "concurrence monopolistique.",
      "Marshall intervient dans ce chapitre pour les districts industriels "
      "de 1890.",
      "Coase est l’auteur de l’analyse de la firme par les coûts de "
      "transaction, en 1937."]),
'ch9-qcm-26': f(niv='comprendre', sp='c9-10', b=1745,
 exp="La différenciation réduit l’élasticité-prix de la demande : quand un "
     "consommateur considère qu’un produit est unique, il devient moins "
     "sensible au prix et accepte de payer davantage. L’exemple du cours est "
     "celui des yaourts : un consommateur attaché à Yoplait ne le remplacera "
     "pas facilement par Danone. La marque réduit la substituabilité.",
 why=["Augmenter l’élasticité-prix serait l’effet inverse : cela rendrait le "
      "consommateur plus sensible au prix.",
      "La différenciation s’appuie précisément sur les marques, elle ne les "
      "supprime pas.",
      "Elle permet au contraire de maintenir, voire d’augmenter les prix."],
 diss="Mécanisme à retenir pour toute dissertation sur le pouvoir de marché : "
      "différenciation → moindre substituabilité → demande moins élastique → "
      "marge."),
'ch9-qcm-27': f(niv='connaitre', sp='c9-10', b=1749,
 exp="Un monopole discriminant pratique des prix différents selon les "
     "consommateurs, en cherchant à faire payer chacun selon sa disposition à "
     "payer. On parle aussi de tarification différentielle ou de yield "
     "management : les consommateurs peu sensibles au prix paient davantage, "
     "les plus sensibles bénéficient de prix plus bas — séances de cinéma du "
     "matin contre séances aux horaires demandés.",
 why=["Le prix unique est la pratique du monopole simple, non discriminant.",
      "La gratuité n’est pas une stratégie de discrimination tarifaire.",
      "Un prix fixé par l’État relève de la réglementation, pas de la "
      "stratégie du monopoleur."],
 diss="Nuance importante : la tarification différentielle n’est pas toujours "
      "condamnée — elle devient problématique en monopole, car le "
      "consommateur n’a pas d’alternative."),
'ch9-vf-1': f(niv='comprendre', sp='c9-10', b=1672,
 exp="La concentration donne du pouvoir de marché parce qu’elle réduit le "
     "nombre d’acteurs : l’entreprise qui rachète ses concurrents augmente ses "
     "parts de marché, réduit l’atomicité et peut devenir dominante. Elle peut "
     "donc transformer une situation de concurrence en oligopole, voire en "
     "monopole. C’est la première des quatre sources du pouvoir de marché "
     "identifiées par le cours.",
 diss="Les trois autres sources à citer avec elle : la différenciation des "
      "produits, les ententes et les barrières à l’entrée."),

# =============================================================== c9-11
'ch9-qcm-16': f(niv='connaitre', sp='c9-11', b=1818,
 exp="Dans La politique de la concurrence (2016), Emmanuel Combe étudie 111 "
     "cartels entre 1969 et 2009. Il en dégage des régularités : une durée "
     "moyenne d’environ sept ans, des prix supérieurs d’environ 15 % aux prix "
     "concurrentiels, une forte présence dans les produits intermédiaires et "
     "une fréquence élevée sur les marchés oligopolistiques.",
 why=["Ni le nombre ni la période ne correspondent à l’étude citée par le "
      "cours.",
      "Le cours ne mentionne pas d’étude portant sur 200 cartels depuis "
      "1945.",
      "L’échantillon n’est pas limité à vingt cartels européens."],
 diss="Chiffres très utiles : +15 % de prix et sept ans de durée moyenne "
      "montrent que les cartels sont à la fois nuisibles et instables."),
'ch9-qcm-17': f(niv='comprendre', sp='c9-11', b=1840,
 exp="Le dilemme du prisonnier explique l’instabilité des cartels. Avec les "
     "gains du cours — 5 chacun si les deux respectent l’accord, 8 contre 0 si "
     "l’une triche seule, 3 chacun si les deux trichent —, tricher rapporte "
     "davantage quelle que soit la décision de l’autre. L’intérêt individuel "
     "s’oppose donc à l’intérêt collectif des membres.",
 why=["La loi de l’offre et de la demande décrit la formation des prix, pas "
      "la stratégie des membres d’une entente.",
      "Le multiplicateur keynésien concerne la demande globale : hors sujet "
      "ici.",
      "Les effets de réseau expliquent le verrouillage des plateformes, pas "
      "la fragilité des ententes."],
 diss="Objection à savoir traiter : le dilemme du prisonnier suppose "
      "l’absence de communication, alors qu’un cartel repose sur une entente. "
      "Réponse du cours : distinguer la coordination initiale et l’exécution "
      "de l’accord, où joue l’opportunisme au sens de Williamson."),
'ch9-qcm-18': f(niv='connaitre', sp='c9-11', b=1907,
 exp="La procédure de clémence consiste à réduire, voire supprimer, la "
     "sanction d’une entreprise qui dénonce le cartel auquel elle "
     "participait : elle peut obtenir une baisse d’amende ou une exonération "
     "complète. Comme les cartels sont secrets, c’est un outil de détection "
     "essentiel, qui renforce l’instabilité déjà mise en évidence par le "
     "dilemme du prisonnier.",
 why=["La clémence réduit les sanctions de celui qui dénonce : elle ne les "
      "aggrave pas.",
      "Elle ne rend pas les ententes licites : elle sert à les détecter et à "
      "les sanctionner.",
      "Elle n’a aucun rapport avec la propriété intellectuelle."]),
'ch9-qcm-19': f(niv='connaitre', sp='c9-11', b=2002,
 exp="Le parallélisme des comportements désigne une situation où plusieurs "
     "entreprises adoptent des stratégies similaires sans accord explicite : "
     "elles réagissent aux mêmes coûts, à la même demande, au même choc, ou "
     "imitent un leader. Il ne suffit donc pas à prouver un cartel : les "
     "autorités doivent établir l’existence d’une coordination réelle.",
 why=["Un accord écrit serait au contraire la preuve recherchée par les "
      "autorités.",
      "Une fusion horizontale est une opération de capital, pas un "
      "comportement de marché.",
      "Une aide d’État est un transfert public : autre domaine de la "
      "politique de concurrence."],
 diss="Cœur du problème de la preuve : hausses simultanées de prix ≠ entente. "
      "C’est ce qui rend la procédure de clémence indispensable."),
'ch9-vf-6': f(niv='comprendre', sp='c9-11', b=1925,
 exp="Les autorités distinguent les ententes anticoncurrentielles des "
     "coopérations économiques légitimes. Une coordination peut être tolérée "
     "si elle améliore l’efficacité économique, favorise l’innovation, "
     "bénéficie aux consommateurs et ne verrouille pas le marché : ententes "
     "technologiques pour partager les coûts de recherche pharmaceutique, "
     "ententes verticales préservant la qualité de distribution ou l’image "
     "d’une marque de luxe.",
 diss="Nuance à exploiter : la politique de concurrence ne combat pas la "
      "coopération entre firmes, mais la restriction de concurrence sans "
      "contrepartie pour le consommateur."),
'ch9-open-3': f(niv='raisonner', sp='c9-11', b=1868,
 exp="Le cartel repose sur un accord de limitation de la concurrence, mais "
     "chaque membre a intérêt à tricher pour capter un profit supplémentaire. "
     "Le dilemme du prisonnier le montre : si l’autre respecte l’accord, "
     "tricher rapporte 8 au lieu de 5 ; si l’autre triche, tricher rapporte 3 "
     "au lieu de 0. La tricherie est donc individuellement rationnelle quelle "
     "que soit la décision de l’autre, ce qui rend l’accord fragile. "
     "L’objection — un cartel suppose de la communication, le dilemme suppose "
     "son absence — se résout en distinguant la coordination initiale et "
     "l’exécution de l’accord : les firmes s’entendent, puis adoptent un "
     "comportement opportuniste au sens de Williamson. Cette instabilité "
     "interne est enfin renforcée par la procédure de clémence, qui incite "
     "chaque membre à dénoncer les autres.",
 diss="Résultat paradoxal utile : les cartels durent quand même sept ans en "
      "moyenne selon Combe — l’instabilité théorique ne suffit pas à les "
      "faire disparaître, d’où la nécessité d’une politique active."),
'ch9-open-4': f(niv='connaitre', sp='c9-11', b=1907,
 exp="La procédure de clémence permet de réduire, voire de supprimer, la "
     "sanction d’une entreprise qui dénonce le cartel auquel elle "
     "participait : baisse d’amende ou exonération complète. Comme les cartels "
     "sont secrets et que le parallélisme des comportements ne suffit pas à "
     "prouver une entente, elle constitue un outil essentiel de détection. Son "
     "effet économique est double : elle permet de découvrir les ententes et "
     "elle les fragilise par avance, puisque chaque membre doit se demander si "
     "l’un des autres ne va pas le dénoncer pour échapper à la sanction."),

# =============================================================== c9-12
'ch9-qcm-29': f(niv='comprendre', sp='c9-12', b=2079,
 exp="Le brevet est une barrière à l’entrée tolérée, dans une logique "
     "schumpétérienne : le profit temporaire récompense l’innovation et incite "
     "les entreprises à investir. Il protège donc temporairement l’innovation "
     "et permet à l’entreprise innovatrice de rentabiliser ses dépenses de "
     "recherche, ce qui justifie l’atteinte provisoire à la libre entrée.",
 why=["Le brevet n’est pas interdit : il est au contraire un droit de "
      "propriété reconnu.",
      "Il a un effet réel sur la concurrence : il empêche la copie "
      "immédiate.",
      "Il n’est nullement réservé aux PME."]),
'ch9-qcm-31': f(niv='connaitre', sp='c9-12', b=2216,
 exp="Un marché contestable est un marché sur lequel une entreprise peut "
     "entrer et sortir librement : absence de barrières à l’entrée comme à la "
     "sortie, accès possible à la technologie, absence de coûts "
     "irrécupérables importants. Même une entreprise seule sur ce marché se "
     "comporte comme si elle était en concurrence, car elle craint l’arrivée "
     "de concurrents potentiels.",
 why=["Le nombre d’entreprises est précisément le critère que cette théorie "
      "écarte.",
      "La réglementation des prix est une intervention publique, sans lien "
      "avec la contestabilité.",
      "La présence de l’État au capital ne dit rien de la liberté d’entrée."],
 diss="Conséquence politique forte : le monopole n’est pas un problème en "
      "soi ; le problème est le monopole protégé, sur un marché fermé."),
'ch9-qcm-32': f(niv='connaitre', sp='c9-12', b=2209,
 exp="Dans les années 1980, William Baumol, John Panzar et Robert Willig "
     "développent la théorie des marchés contestables : le vrai critère de la "
     "concurrence n’est pas le nombre d’entreprises présentes mais la liberté "
     "d’entrée et de sortie. La menace d’entrée de concurrents potentiels "
     "suffit à discipliner les firmes installées.",
 why=["Mason et Bain sont les auteurs du modèle SCP, dans les années 1950.",
      "Alchian et Demsetz développent l’approche contractuelle de la firme.",
      "Marshall travaille sur les districts industriels, Chamberlin sur la "
      "concurrence monopolistique."]),
'ch9-vf-9': f(niv='comprendre', sp='c9-12', b=2221,
 exp="Un marché contestable suppose bien l’absence de coûts irrécupérables "
     "importants. C’est la condition qui rend l’entrée et la sortie réellement "
     "libres : si un entrant doit engager des dépenses qu’il ne pourra pas "
     "récupérer en cas d’échec, la menace d’entrée perd sa crédibilité et "
     "l’entreprise installée retrouve son pouvoir de marché.",
 diss="À relier aux nouvelles politiques de concurrence : limiter les coûts "
      "irrécupérables et les verrouillages technologiques plutôt que "
      "multiplier artificiellement le nombre d’entreprises."),
'ch9-vf-12': f(niv='comprendre', sp='c9-12', b=2117,
 exp="Les prix prédateurs réduisent la concurrence de deux manières : ils "
     "peuvent éliminer les entreprises déjà présentes, ce qui porte atteinte à "
     "l’atomicité ; et ils dissuadent les nouveaux entrants, qui ne peuvent "
     "pas supporter aussi longtemps des prix aussi faibles, ce qui porte "
     "atteinte à la libre entrée. L’entreprise dominante utilise sa puissance "
     "financière pour rendre le marché inaccessible."),
'ch9-open-7': f(niv='comprendre', sp='c9-12', b=2227,
 exp="Un marché contestable est un marché sur lequel une entreprise peut "
     "entrer et sortir librement : il n’y a ni barrières à l’entrée ni "
     "barrières à la sortie, la technologie est accessible et les coûts "
     "irrécupérables sont faibles. Développée dans les années 1980 par "
     "William Baumol, John Panzar et Robert Willig, cette théorie déplace le "
     "critère de la concurrence : ce n’est plus l’atomicité qui compte, mais "
     "la menace crédible d’une entrée nouvelle. Même un marché très concentré "
     "peut rester concurrentiel, car l’entreprise installée, craignant "
     "l’entrée, se comporte comme si elle était en concurrence. Le cours "
     "ajoute que la contestabilité concerne aussi les consommateurs : la "
     "portabilité du numéro en téléphonie mobile a réduit leurs coûts de "
     "sortie et renforcé la pression concurrentielle.",
 diss="Cette théorie est le socle de l’approche élargie de la concurrence "
      "chez Emmanuel Combe."),

# =============================================================== c9-13
'ch9-qcm-33': f(niv='comprendre', sp='c9-13', b=2446,
 exp="Dans l’approche élargie, la concurrence n’est pas une structure mais un "
     "processus de sélection des entreprises les plus efficaces : une firme "
     "peut devenir dominante parce qu’elle a réussi. Le critère central n’est "
     "donc plus le nombre d’entreprises mais la contestabilité du marché, "
     "c’est-à-dire la possibilité pour de nouveaux concurrents d’entrer.",
 why=["Le nombre d’entreprises est le critère de l’approche standard, fondée "
      "sur l’atomicité.",
      "Le taux de marge mesure le résultat (indice de Lerner), pas "
      "l’ouverture du marché.",
      "La taille des firmes n’est pas en elle-même un indicateur de "
      "concurrence dans cette approche."],
 diss="Opposition à retenir, chez Emmanuel Combe : approche standard = "
      "lutter contre la concentration ; approche élargie = maintenir la "
      "contestabilité."),
'ch9-qcm-34': f(niv='connaitre', sp='c9-13', b=2292,
 exp="SCP signifie Structure – Comportements – Performances. La structure du "
     "marché — nombre d’entreprises, concentration, barrières à l’entrée — "
     "détermine les comportements des firmes — prix, ententes, "
     "différenciation, innovation —, qui déterminent ensuite leurs "
     "performances — profits, marges, parts de marché, rentabilité.",
 why=["« Stratégie – Concurrence – Profit » n’est pas la décomposition du "
      "modèle.",
      "« Société – Capital – Production » ne correspond à rien dans le "
      "chapitre.",
      "« Salaire – Coût – Prix » relève de l’analyse des coûts, pas de "
      "l’économie industrielle."]),
'ch9-qcm-35': f(niv='connaitre', sp='c9-13', b=2288,
 exp="Le modèle SCP est associé à Edward Mason, puis à Joe Bain dans les "
     "années 1950. Il naît de l’économie industrielle, à partir d’analyses "
     "historiques des marchés américains : les économistes observent que "
     "certaines structures de marché favorisent certains comportements "
     "d’entreprises.",
 why=["Coase et Williamson analysent la firme par les coûts de transaction.",
      "Simon travaille sur la rationalité limitée, Chandler sur les formes U "
      "et M.",
      "Baumol et Panzar sont les auteurs des marchés contestables, dans les "
      "années 1980."]),
'ch9-qcm-36': f(niv='connaitre', sp='c9-13', b=2343,
 exp="L’indice de Lerner s’écrit L = (P – Cm)/P : il mesure l’écart entre le "
     "prix et le coût marginal, rapporté au prix, c’est-à-dire la part de la "
     "marge dans le prix. Plus l’indice est élevé, plus l’entreprise peut "
     "fixer un prix supérieur à son coût marginal, donc plus son pouvoir de "
     "marché est fort.",
 why=["P × Q est le chiffre d’affaires, pas une mesure de pouvoir de "
      "marché.",
      "Cm/P inverse le raisonnement : ce rapport diminue quand le pouvoir de "
      "marché augmente.",
      "(P + Cm)/2 est une moyenne sans signification économique ici."]),
'ch9-qcm-37': f(niv='comprendre', sp='c9-13', b=2359,
 exp="En concurrence pure et parfaite, l’entreprise est preneuse de prix et "
     "le prix s’égalise au coût marginal : le numérateur (P – Cm) tend vers "
     "zéro, donc l’indice de Lerner tend vers 0. L’entreprise ne dispose "
     "d’aucun pouvoir de marché. À l’inverse, un indice élevé signale une "
     "marge importante et un pouvoir de marché.",
 why=["Un indice proche de 1 signalerait un pouvoir de marché maximal, donc "
      "l’inverse de la concurrence parfaite.",
      "Un indice négatif supposerait un prix inférieur au coût marginal : "
      "situation de perte, non d’équilibre concurrentiel.",
      "L’indice est parfaitement déterminé : il vaut 0 à la limite."]),
'ch9-open-8': f(niv='raisonner', sp='c9-13', b=2390,
 exp="Le modèle SCP, associé à Edward Mason puis Joe Bain dans les années "
     "1950, relie la Structure du marché — nombre d’entreprises, degré de "
     "concentration, barrières à l’entrée, pouvoir de marché —, les "
     "Comportements des firmes — politique de prix, ententes, "
     "différenciation, innovation, prix prédateurs — et leurs Performances — "
     "profits, marges, parts de marché, efficacité productive. La structure "
     "détermine les comportements, qui déterminent les résultats. Sa limite "
     "principale est son caractère trop mécanique : la causalité peut "
     "s’inverser. Une entreprise qui différencie fortement son produit "
     "fidélise ses clients, rend la demande moins élastique, augmente ses "
     "profits et peut ensuite racheter des concurrents : le comportement "
     "transforme alors la structure. Le modèle sous-estime donc le rôle actif "
     "des stratégies d’entreprise.",
 diss="Cette limite conduit directement à l’approche élargie de la "
      "concurrence et à la théorie des marchés contestables."),
'ch9-open-9': f(niv='comprendre', sp='c9-13', b=2346,
 exp="L’indice de Lerner mesure le pouvoir de marché d’une entreprise par la "
     "formule L = (P – Cm)/P, c’est-à-dire la part de la marge dans le prix. "
     "Un indice faible signifie que le prix est proche du coût marginal, que "
     "la marge est faible et que le marché est très concurrentiel. Un indice "
     "élevé signifie au contraire que le prix est largement supérieur au coût "
     "marginal : l’entreprise dispose d’un pouvoir de marché. En concurrence "
     "pure et parfaite, le prix égalise le coût marginal et l’indice tend vers "
     "0. C’est l’un des indicateurs mobilisés par l’approche standard de la "
     "concurrence, aux côtés du nombre d’entreprises, des parts de marché et "
     "du degré de concentration."),

# =============================================================== c9-14
'ch9-qcm-42': f(niv='connaitre', sp='c9-14', b=2629,
 exp="Le Digital Markets Act est un règlement européen adopté en 2022 qui "
     "vise les grandes plateformes numériques, qualifiées de « contrôleurs "
     "d’accès » : Google, Amazon, Apple, Meta, Microsoft. Ces plateformes "
     "contrôlent l’accès à des marchés numériques essentiels, ce qui justifie "
     "un encadrement spécifique.",
 why=["Les PME industrielles ne sont pas visées : le DMA cible les acteurs "
      "systémiques du numérique.",
      "Les banques relèvent d’une régulation financière distincte.",
      "L’agriculture n’est pas concernée par ce règlement."]),
'ch9-vf-20': f(niv='connaitre', sp='c9-14', b=2651,
 exp="Le DMA prévoit des sanctions très lourdes : les amendes peuvent "
     "atteindre 10 % du chiffre d’affaires mondial, et jusqu’à 20 % en cas de "
     "récidive. Il interdit notamment aux plateformes de favoriser leurs "
     "propres produits, d’exploiter les données de leurs concurrents contre "
     "eux, d’imposer certains services ou de rendre les utilisateurs captifs.",
 diss="Le DMA marque un déplacement des politiques de concurrence : on "
      "n’attend plus l’abus constaté, on interdit a priori certaines "
      "pratiques aux acteurs désignés comme contrôleurs d’accès."),
'ch9-open-15': f(niv='connaitre', sp='c9-14', b=2544,
 exp="Le moyen mnémotechnique du cours est « État contre carabus ». La "
     "politique de concurrence surveille d’abord les aides d’État, en "
     "principe interdites lorsqu’elles faussent la concurrence, même si "
     "certaines sont tolérées — recherche, PME, transition écologique, crise. "
     "Elle contrôle ensuite les concentrations, en autorisant ou en refusant "
     "les fusions : seulement 1 % environ ont été refusées entre 2010 et 2020 "
     "selon Emmanuel Combe, et le refus de la fusion Alstom-Siemens en 2019 "
     "montre l’importance de la définition du marché pertinent. Elle "
     "sanctionne les cartels et les ententes, détectés notamment par la "
     "procédure de clémence. Elle réprime enfin les abus de position "
     "dominante, désormais complétée par le DMA pour les plateformes "
     "numériques.",
 diss="Cadres juridiques à citer : Sherman Act 1890, Clayton Act 1914 et "
      "Federal Trade Commission Act 1914 aux États-Unis ; articles 101 et 102 "
      "du TFUE en Europe ; DGCCRF et Autorité de la concurrence en France."),

# =============================================================== c9-15
'ch9-qcm-40': f(niv='connaitre', sp='c9-15', b=2777,
 exp="Herbert Simon montre que les agents économiques ne disposent pas d’une "
     "rationalité parfaite : l’information est imparfaite, le temps limité, "
     "les capacités cognitives bornées et l’avenir incertain. Ils prennent "
     "donc une décision satisfaisante plutôt qu’optimale. Williamson reprend "
     "cette hypothèse pour expliquer l’incomplétude des contrats.",
 why=["Coase introduit les coûts de transaction, en 1937.",
      "Chandler analyse les formes d’organisation U et M.",
      "Joe Bain est l’un des auteurs du modèle SCP."]),
'ch9-qcm-41': f(niv='connaitre', sp='c9-15', b=2851,
 exp="La forme M désigne une organisation multidivisionnelle : l’entreprise "
     "est divisée en unités correspondant à un produit, un marché, une zone "
     "géographique ou une activité. Alfred Chandler montre que cette forme "
     "devient nécessaire lorsque l’entreprise grandit et se diversifie, car "
     "une grande firme ne peut pas être gérée comme une petite structure "
     "centralisée.",
 why=["L’organisation fonctionnelle, par grandes fonctions, est la forme U.",
      "« Matricielle familiale » ne figure pas dans la typologie de "
      "Chandler.",
      "« Monopolistique » décrit une position de marché, pas une structure "
      "interne."]),
'ch9-open-14': f(niv='comprendre', sp='c9-15', b=2859,
 exp="La forme U est une organisation fonctionnelle, structurée par grandes "
     "fonctions — production, finance, marketing, ressources humaines : elle "
     "convient à des entreprises relativement centralisées, de taille "
     "modeste. La forme M est multidivisionnelle : l’entreprise est divisée en "
     "unités correspondant à un produit, un marché, une zone géographique ou "
     "une activité, chacune disposant d’une autonomie de gestion. Alfred "
     "Chandler montre que la croissance de la firme impose cette "
     "transformation : la grande entreprise diversifiée ne peut pas être gérée "
     "comme une petite structure centralisée, car la taille modifie la "
     "hiérarchie, la circulation de l’information, la division du travail et "
     "les besoins de coordination.",
 diss="À relier aux entreprises intégrées de François et Lemercier : la "
      "forme M est la structure typique du grand groupe verticalement "
      "intégré."),

}

from qz09n1 import L as _N1
from qz09n2 import L as _N2
from qz09n3 import L as _N3
from qz09n4 import L as _N4

NEW = _N1 + _N2 + _N3 + _N4


# Les quinze questions ouvertes héritées n'avaient aucune grille de
# correction : le corrigé rédigé sert de réponse modèle, et l'on explicite
# les éléments que la réponse doit contenir.
CLES = {
 'ch9-open-1': [
   {'f': ['investissement propre', 'propres investissement', 'usine', 'interne'],
    'l': 'la croissance interne mobilise les investissements propres'},
   {'f': ['fusion', 'rachat', 'acquisition'],
    'l': 'la croissance externe passe par la fusion ou le rachat'},
   {'f': ['rapide', 'rapidite', 'coup', 'immediat'],
    'l': 'la croissance externe est beaucoup plus rapide'}],
 'ch9-open-2': [
   {'f': ['horizontal'], 'l': 'la concentration horizontale : des concurrents directs'},
   {'f': ['vertical', 'amont', 'aval'], 'l': 'la concentration verticale : la chaîne de production'},
   {'f': ['conglomeral', 'diversif'], 'l': 'la concentration conglomérale : la diversification'}],
 'ch9-open-3': [
   {'f': ['tricher', 'dilemme', 'prisonnier'],
    'l': 'tricher est individuellement rationnel : le dilemme du prisonnier'},
   {'f': ['opportunis', 'execution', 'coordination initiale', 'williamson'],
    'l': 'la coordination initiale n’empêche pas l’opportunisme ensuite'},
   {'f': ['clemence', 'denonc', 'autorite'],
    'l': 'la procédure de clémence renforce l’instabilité'}],
 'ch9-open-4': [
   {'f': ['reduire', 'supprimer', 'exoner', 'amende'],
    'l': 'une réduction voire une exonération de sanction'},
   {'f': ['secret', 'detect', 'preuve'],
    'l': 'un outil de détection, car les cartels sont secrets'},
   {'f': ['incite', 'denonc', 'instabilite'],
    'l': 'elle incite à la dénonciation et fragilise l’entente'}],
 'ch9-open-5': [
   {'f': ['pas condamnee', 'n est pas condamnee', 'reussite', 'legale'],
    'l': 'la position dominante n’est pas condamnée en elle-même'},
   {'f': ['abus', 'elimin', 'empecher'],
    'l': 'l’abus consiste à éliminer ou empêcher les concurrents'},
   {'f': ['vente liee', 'prix predateur', 'exclusivite', 'denigrement'],
    'l': 'les formes concrètes de l’abus'}],
 'ch9-open-6': [
   {'f': ['qualite', 'gamme'], 'l': 'la différenciation verticale porte sur la qualité'},
   {'f': ['style', 'gout', 'localisation', 'couleur'],
    'l': 'la différenciation horizontale porte sur des caractéristiques secondaires'},
   {'f': ['substituabilite', 'elasticite'],
    'l': 'les deux réduisent la substituabilité entre les biens'}],
 'ch9-open-7': [
   {'f': ['entrer et sortir', 'libre entree', 'libre sortie', 'sans barriere'],
    'l': 'l’entrée et la sortie sont libres'},
   {'f': ['baumol', 'panzar', 'willig'],
    'l': 'la théorie de Baumol, Panzar et Willig'},
   {'f': ['menace', 'concurrent potentiel', 'discipline'],
    'l': 'la menace d’entrée suffit à discipliner les firmes installées'}],
 'ch9-open-8': [
   {'f': ['structure', 'comportement', 'performance'],
    'l': 'structure → comportements → performances'},
   {'f': ['mason', 'bain', 'economie industrielle'],
    'l': 'le modèle vient de l’économie industrielle (Mason, Bain)'},
   {'f': ['mecanique', 'inverse', 'strategie transforme', 'sous estime'],
    'l': 'la limite : les comportements peuvent transformer la structure'}],
 'ch9-open-9': [
   {'f': ['p cm', 'cout marginal'], 'l': 'la formule L = (P – Cm)/P'},
   {'f': ['marge', 'pouvoir de marche'], 'l': 'il mesure la marge, donc le pouvoir de marché'},
   {'f': ['zero', '0', 'concurrence parfaite'],
    'l': 'en concurrence parfaite, l’indice tend vers 0'}],
 'ch9-open-10': [
   {'f': ['souple', 'rapide', 'proximite', 'reactiv'],
    'l': 'souplesse, rapidité de décision, proximité du marché'},
   {'f': ['financ', 'bancaire', 'capitaux', 'export'],
    'l': 'fragilité financière et dépendance bancaire'},
   {'f': ['conjoncture', 'crise', 'too big to fail', 'ajustement'],
    'l': 'sensibilité à la conjoncture, à l’inverse du « too big to fail »'}],
 'ch9-open-11': [
   {'f': ['contractuel', 'contrat', 'sous trait'],
    'l': 'un lien contractuel plutôt que patrimonial'},
   {'f': ['modulaire', 'module', 'specialis'],
    'l': 'une production modulaire'},
   {'f': ['dipp', 'mondialisation', 'amazon', 'apple'],
    'l': 'une logique renforcée par la mondialisation et la DIPP'}],
 'ch9-open-12': [
   {'f': ['information', 'negociation', 'contrat', 'recours au marche'],
    'l': 'les coûts liés au recours au marché'},
   {'f': ['rationalite limitee', 'simon', 'incomplet'],
    'l': 'la rationalité limitée rend les contrats incomplets'},
   {'f': ['opportunis'], 'l': 'l’opportunisme des agents'},
   {'f': ['internalis', 'integration verticale', 'frontiere'],
    'l': 'l’internalisation et les frontières de la firme'}],
 'ch9-open-13': [
   {'f': ['noeud de contrats', 'alchian', 'demsetz', 'jensen'],
    'l': 'l’approche contractuelle : la firme comme nœud de contrats'},
   {'f': ['coase', 'williamson', 'autorite', 'imparfait'],
    'l': 'l’approche transactionnelle : la firme existe contre les imperfections du marché'},
   {'f': ['cooperation', 'triche', 'limite'],
    'l': 'la limite : l’entreprise est aussi un lieu de coopération'}],
 'ch9-open-14': [
   {'f': ['fonctionnelle', 'fonction', 'production finance'],
    'l': 'la forme U est fonctionnelle'},
   {'f': ['multidivision', 'division', 'produit', 'zone'],
    'l': 'la forme M est multidivisionnelle'},
   {'f': ['croissance', 'taille', 'diversif', 'chandler'],
    'l': 'la croissance de la firme impose ce changement de structure'}],
 'ch9-open-15': [
   {'f': ['aide d etat', 'aides d etat', 'subvention'], 'l': 'les aides d’État'},
   {'f': ['concentration', 'fusion'], 'l': 'le contrôle des concentrations'},
   {'f': ['cartel', 'entente'], 'l': 'les cartels et les ententes'},
   {'f': ['abus de position dominante', 'dma'],
    'l': 'les abus de position dominante, et le DMA pour les plateformes'}],
}

for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'modele': FIX[_id]['exp'], 'cles': _c}
