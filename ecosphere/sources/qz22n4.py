# -*- coding: utf-8 -*-
"""Chapitre 22 — questions nouvelles : sous-parties minces et formats manquants."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c22-05
f(id='q22-n78', sp='c22-05', niv='comprendre', type='qcm', b=1634,
  q="Pourquoi une partie de la désindustrialisation mesurée est-elle qualifiée "
    "de « statistique » ?",
  opts=["Parce que les statistiques industrielles sont mal construites",
        "Parce que l’externalisation des services fait basculer dans le "
        "tertiaire des emplois autrefois comptés dans l’industrie, sans "
        "qu’ils disparaissent",
        "Parce que les entreprises refusent de déclarer leurs effectifs",
        "Parce que l’industrie n’est plus définie de la même façon dans tous "
        "les pays"],
  ans=1,
  why=["Il ne s’agit pas d’un défaut de mesure mais d’un effet de "
       "périmètre.",
       "Les déclarations d’effectifs ne sont pas en cause.",
       "L’hétérogénéité internationale des définitions est un autre problème, "
       "qui n’est pas celui-ci."],
  exp="Dans les années 1960-1970, une grande entreprise industrielle "
      "employait directement ses comptables, juristes, informaticiens, "
      "agents de nettoyage et personnel de cantine : tous étaient "
      "comptabilisés dans l’industrie. À partir des années 1980, le "
      "recentrage sur le cœur de métier conduit à externaliser ces services. "
      "Même personne, même tâche, parfois même site : avant, emploi "
      "industriel ; après, emploi tertiaire. Le cours retient qu’environ un "
      "quart du phénomène s’explique par ces changements d’organisation.",
  diss="Chiffre très utile pour relativiser : un quart de la "
       "désindustrialisation mesurée est un effet de périmètre."),

f(id='q22-n79', sp='c22-05', niv='appliquer', type='ordre', b=1655,
  q="Remettez dans l’ordre le mécanisme par lequel le progrès technique "
    "réduit l’emploi industriel.",
  ans=["L’entreprise investit dans de nouvelles machines",
       "La productivité du travail augmente",
       "La quantité produite par salarié s’élève",
       "Le nombre de travailleurs nécessaires pour une production donnée "
       "diminue"],
  exp="C’est le mécanisme du cours : machines ↑ → productivité ↑ → quantité "
      "produite par salarié ↑ → emploi industriel nécessaire ↓. Il s’agit "
      "d’une désindustrialisation en emploi, qui n’implique pas "
      "nécessairement un recul de la production : une économie peut produire "
      "davantage de biens avec moins d’ouvriers. C’est précisément cette "
      "distinction qui permet de comprendre pourquoi la part de l’industrie "
      "recule plus vite en emploi qu’en valeur ajoutée.",
  diss="Argument de Krugman à mobiliser ici : le principal facteur de "
       "transformation de l’emploi est le progrès technique, non la "
       "mondialisation."),

f(id='q22-n80', sp='c22-05', niv='comprendre', type='qcm', b=1680,
  q="Que dit la loi d’Engel, mobilisée pour expliquer la tertiarisation ?",
  opts=["Quand le revenu augmente, la part du budget consacrée à "
        "l’alimentation diminue au profit d’autres postes",
        "Quand le revenu augmente, la consommation alimentaire diminue en "
        "volume",
        "Quand les prix augmentent, la demande diminue proportionnellement",
        "Quand la population augmente, la production agricole augmente "
        "davantage"],
  ans=0,
  why=["La loi porte sur la part du budget, non sur le volume consommé, qui "
       "peut rester stable ou croître.",
       "L’élasticité-prix de la demande est une autre notion.",
       "Il ne s’agit pas d’une loi démographique."],
  exp="La tertiarisation accompagne l’élévation du niveau de vie : lorsque "
      "les besoins matériels se saturent, la demande se déplace "
      "progressivement des biens vers les services — loisirs, santé, "
      "éducation. Le cours ajoute un second mécanisme, lié aux prix : les "
      "prix réels baissent davantage dans les secteurs à forts gains de "
      "productivité, de sorte que les services, moins facilement "
      "automatisables, occupent une part croissante de la valeur ajoutée.",
  diss="À coupler systématiquement avec le déversement de Fourastié, exposé "
       "dans Le Grand Espoir du XXᵉ siècle (1949)."),

f(id='q22-n81', sp='c22-05', niv='raisonner', type='qcmm', b=1774,
  q="Pourquoi la tertiarisation ne compense-t-elle pas mécaniquement les "
    "pertes d’emplois industriels ? (plusieurs réponses)",
  opts=["Les emplois créés diffèrent par leur niveau de qualification",
        "Ils diffèrent par leur rémunération",
        "Ils ne sont pas nécessairement localisés là où les usines ont fermé",
        "L’industrie concentre une part disproportionnée de la R&D et des "
        "gains de productivité",
        "Le secteur tertiaire ne crée aucun emploi"],
  ans=[0, 1, 2, 3],
  why=["Exacte : un ouvrier spécialisé ne trouve pas immédiatement un emploi "
       "tertiaire équivalent.",
       "Exacte : les niveaux de rémunération ne se correspondent pas "
       "nécessairement.",
       "Exacte : c’est le mismatch géographique, et non seulement un "
       "mismatch de qualification.",
       "Exacte : la perte d’industrie pèse donc sur la croissance de long "
       "terme.",
       "Inexacte : le tertiaire crée massivement des emplois, mais pas "
       "nécessairement les mêmes ni aux mêmes endroits."],
  exp="Le cours insiste sur un point décisif : le problème n’est pas "
      "uniquement un mismatch de qualification, c’est aussi un mismatch "
      "géographique. L’industrie ferme dans une région A tandis que les "
      "services se développent dans une région B, et le travailleur de A ne "
      "bénéficie pas automatiquement des emplois de B. La désindustrialisation "
      "constitue donc un choc local persistant.",
  diss="Convergence remarquable avec Autor : effet local, durable et non "
       "compensé par la réallocation attendue."),

f(id='q22-n82', sp='c22-05', niv='connaitre', type='qcm', b=1833,
  q="Quel ordre de grandeur le cours retient-il pour l’emploi industriel "
    "français ?",
  opts=["Environ 5 millions d’emplois en 1975, contre environ 2,7 millions "
        "aujourd’hui",
        "Environ 2 millions d’emplois en 1975, contre environ 5 millions "
        "aujourd’hui",
        "Un niveau stable autour de 4 millions depuis 1975",
        "Environ 8 millions d’emplois en 1975, contre environ 6 millions "
        "aujourd’hui"],
  ans=0,
  why=["L’évolution est inverse : l’emploi industriel a reculé, il n’a pas "
       "progressé.",
       "Le niveau n’est pas resté stable : plus de 2 millions d’emplois ont "
       "disparu.",
       "Ces niveaux ne correspondent pas aux ordres de grandeur du cours."],
  exp="La France comptait environ 5 millions d’emplois industriels en 1975 "
      "contre environ 2,7 millions aujourd’hui, soit plus de 2 millions "
      "d’emplois perdus et une division approximative par deux. Entre 1997 et "
      "2017, l’emploi manufacturier recule d’environ 25 %. La part de "
      "l’industrie manufacturière dans la valeur ajoutée tourne autour de "
      "10 % aujourd’hui — un niveau comparable à celui des États-Unis, où "
      "l’industrie manufacturière représente environ 10 % du PIB en 2025.",
  diss="Comparaison européenne indispensable : la France figure parmi les "
       "économies les plus désindustrialisées, l’Allemagne et plusieurs pays "
       "d’Europe centrale conservant un poids industriel nettement "
       "supérieur."),

f(id='q22-n83', sp='c22-05', niv='raisonner', type='courte', b=1828,
  q="En quoi la désindustrialisation peut-elle devenir un processus "
    "cumulatif ?",
  ans={'modele': "Parce qu’elle détruit les conditions mêmes d’une "
       "réindustrialisation future. En disparaissant, une industrie emporte "
       "avec elle les compétences spécialisées, les fournisseurs locaux et "
       "les infrastructures adaptées qui faisaient son écosystème. Or ces "
       "éléments sont précisément ce qu’une nouvelle implantation "
       "rechercherait : une fois perdus, ils rendent plus coûteux le retour "
       "de la production. S’y ajoutent deux conséquences aggravantes : "
       "l’industrie concentrant une part disproportionnée de la R&D et des "
       "gains de productivité, sa disparition pèse sur la croissance de long "
       "terme ; et la désindustrialisation détériore la balance commerciale, "
       "puisque le pays continue de consommer des biens manufacturés qu’il ne "
       "produit plus suffisamment. Le choc est enfin très localisé, les "
       "territoires touchés ne retrouvant pas nécessairement les emplois "
       "créés ailleurs.",
       'cles': [{'f': ['competence', 'savoir-faire', 'savoir faire',
                       'qualification'],
                 'l': "la perte des compétences spécialisées"},
                {'f': ['fournisseur', 'sous-traitant', 'ecosysteme', 'filiere'],
                 'l': "la disparition des fournisseurs et de l'écosystème"},
                {'f': ['infrastructure', 'equipement', 'site'],
                 'l': "la perte des infrastructures spécialisées"},
                {'f': ['r&d', 'recherche', 'innovation', 'productivite'],
                 'l': "l'industrie concentre R&D et gains de productivité"},
                {'f': ['balance commerciale', 'deficit', 'importation',
                       'reimport'],
                 'l': "la détérioration de la balance commerciale"},
                {'f': ['local', 'territoire', 'region', 'bassin'],
                 'l': "un choc local persistant"}]},
  exp="La désindustrialisation peut devenir cumulative : en détruisant les "
      "compétences, les fournisseurs et les infrastructures spécialisés, elle "
      "réduit elle-même les possibilités futures de réindustrialisation.",
  diss="Argument puissant en faveur d’une intervention précoce : il est moins "
       "coûteux de préserver un écosystème industriel que de le reconstruire."),

# ------------------------------------------------------------- c22-15
f(id='q22-n84', sp='c22-15', niv='comprendre', type='qcm', b=5367,
  q="Qu’est-ce que le « moment 2020 » change dans la façon de penser la "
    "politique industrielle ?",
  opts=["Elle devient un simple instrument de politique monétaire",
        "Elle n’est plus seulement pensée comme un instrument de "
        "compétitivité ou de rattrapage, mais aussi comme un moyen de réduire "
        "les vulnérabilités créées par l’hypermondialisation",
        "Elle est abandonnée au profit du libre-échange",
        "Elle se limite désormais à la recherche fondamentale"],
  ans=1,
  why=["La politique industrielle n’est pas un instrument monétaire.",
       "C’est l’inverse : le moment 2020 marque un recul de la doctrine du "
       "libre-échange intégral.",
       "La recherche fondamentale n’est qu’un de ses volets."],
  exp="L’enchaînement retenu par le cours est le suivant : "
      "hypermondialisation → dépendances révélées par les crises → recherche "
      "de résilience → réindustrialisation → retour des politiques "
      "industrielles verticales. Les économies avancées prennent brutalement "
      "conscience qu’une économie très riche peut connaître des pénuries, que "
      "certaines dépendances concernent des productions vitales, et qu’une "
      "chaîne de valeur très optimisée peut devenir vulnérable lorsqu’un "
      "maillon est interrompu.",
  diss="Formule centrale : l’efficience d’une chaîne de valeur ne garantit "
       "pas sa résilience."),

f(id='q22-n85', sp='c22-15', niv='appliquer', type='ordre', b=5429,
  q="Remettez dans l’ordre les trois étapes du « moment 2020 » distinguées "
    "par Élie Cohen.",
  ans=["La révélation des vulnérabilités : les pénuries montrent qu’une "
       "chaîne de valeur très fragmentée peut rompre",
       "La tentation d’une relocalisation généralisée, qui se heurte à la "
       "rationalité même des chaînes de valeur mondiales",
       "La maturation du diagnostic : on abandonne le retour intégral des "
       "productions pour une réindustrialisation ciblée des activités "
       "stratégiques"],
  exp="La deuxième étape échoue parce que les firmes multinationales ont "
      "fragmenté leur production pour des raisons précises : exploiter des "
      "différences de coûts, bénéficier d’économies d’échelle, se rapprocher "
      "de certains fournisseurs et utiliser des écosystèmes industriels "
      "spécialisés. Tout relocaliser ferait perdre une partie de ces gains. "
      "D’où le passage de « tout relocaliser » à « reconstruire certaines "
      "capacités productives stratégiques ».",
  diss="Distinction de vocabulaire à tenir fermement : relocalisation "
       "intégrale ≠ réindustrialisation stratégique."),

f(id='q22-n86', sp='c22-15', niv='comprendre', type='qcm', b=5673,
  q="Comment le cours distingue-t-il souveraineté et protectionnisme ?",
  opts=["Les deux notions sont équivalentes",
        "Le protectionnisme vise à protéger le marché intérieur contre la "
        "concurrence étrangère, la souveraineté à éviter une dépendance jugée "
        "dangereuse",
        "La souveraineté suppose la fermeture complète de l’économie",
        "Le protectionnisme concerne les capitaux, la souveraineté les "
        "marchandises"],
  ans=1,
  why=["Les confondre conduit précisément à la confusion que le cours "
       "dénonce.",
       "La souveraineté ne suppose pas la fermeture : rechercher la "
       "souveraineté ne signifie pas fermer son économie.",
       "La distinction ne porte pas sur la nature des flux concernés."],
  exp="Le protectionnisme cherche à protéger les producteurs et les emplois "
      "domestiques contre la concurrence étrangère. La souveraineté consiste "
      "à conserver une capacité de décision et d’action sans dépendance "
      "extérieure excessive. Un pays peut donc importer massivement tout en "
      "restant souverain s’il dispose de plusieurs fournisseurs : ce n’est "
      "pas le volume des importations qui crée la vulnérabilité, mais la "
      "concentration de la dépendance.",
  diss="Cette distinction permet d’éviter l’erreur la plus fréquente sur ce "
       "chapitre : assimiler le retour de la souveraineté à un retour du "
       "protectionnisme."),

f(id='q22-n87', sp='c22-15', niv='comprendre', type='qcm', b=5708,
  q="Que vise l’autonomie stratégique européenne, telle que le cours la "
    "présente ?",
  opts=["L’autarcie productive de l’Union européenne",
        "La maîtrise des interdépendances : rester ouvert au commerce tout en "
        "évitant qu’une dépendance trop concentrée devienne un instrument de "
        "coercition",
        "La suppression de tous les investissements étrangers en Europe",
        "L’alignement complet sur la politique commerciale américaine"],
  ans=1,
  why=["L’autarcie est explicitement écartée : l’indépendance absolue est "
       "irréaliste.",
       "La suppression des IDE entrants n’est pas l’objectif : le projet "
       "européen cherche plutôt à les conditionner.",
       "L’autonomie stratégique signifie au contraire pouvoir poursuivre ses "
       "propres intérêts."],
  exp="L’objectif est de pouvoir poursuivre ses intérêts sans « dépendances "
      "indésirables », ce qui conduit à une conception relative de la "
      "souveraineté : non l’absence de dépendance, mais la réduction des "
      "dépendances dangereuses. La différence est pratique : elle permet de "
      "hiérarchiser les dépendances au lieu de chercher à les supprimer "
      "toutes.",
  diss="À articuler avec le mythe du potager : la diversification des "
       "fournisseurs peut offrir plus de résilience que la concentration de "
       "la production sur le territoire national."),

f(id='q22-n88', sp='c22-15', niv='connaitre', type='qcm', b=5433,
  q="Que désignent les PIIEC dans la politique industrielle européenne ?",
  opts=["Les Plans d’investissement industriel en Europe centrale",
        "Les Projets importants d’intérêt européen commun, qui autorisent des "
        "soutiens publics ciblés sur des projets trop coûteux ou trop risqués "
        "pour le seul secteur privé",
        "Les Programmes d’incitation à l’exportation des industries "
        "communautaires",
        "Les Plateformes d’innovation industrielle des États candidats"],
  ans=1,
  why=["Aucun dispositif de ce nom n’existe dans le cours.",
       "Il ne s’agit pas d’un dispositif de soutien à l’exportation.",
       "Les États candidats ne sont pas l’objet de ce cadre."],
  exp="Les PIIEC montrent que l’Union européenne assouplit progressivement sa "
      "doctrine traditionnelle de concurrence en autorisant des soutiens "
      "ciblés lorsque les projets impliquent des coûts fixes élevés, de "
      "fortes externalités technologiques ou un enjeu stratégique commun. Le "
      "cours cite deux exemples : l’hydrogène, avec une chaîne allant de la "
      "R&D aux infrastructures puis aux usages industriels, et la santé, en "
      "réponse à la dépendance pharmaceutique européenne.",
  diss="Articulation nette avec la logique de la DARPA : partenariat "
       "public-privé sur des projets risqués, avec un objectif fixé par la "
       "puissance publique."),

f(id='q22-n89', sp='c22-15', niv='comprendre', type='vf', b=5497,
  q="France 2030 est une politique industrielle horizontale, qui soutient "
    "indistinctement toutes les entreprises.",
  ans=False,
  exp="France 2030 marque au contraire le retour d’un État davantage "
      "stratège : plutôt que de soutenir indistinctement toutes les "
      "entreprises, les pouvoirs publics concentrent une partie de leurs "
      "moyens sur les technologies jugées essentielles à la compétitivité et "
      "à la souveraineté futures. Il s’agit donc d’une politique verticale, "
      "mobilisant notamment des moyens importants pour la transition "
      "numérique et réunissant entreprises, start-up, laboratoires, "
      "universités et financements publics.",
  diss="Limite immédiate à mentionner : l’échelle nationale limite la "
       "puissance d’une telle politique, d’où l’importance de la dimension "
       "européenne."),

# ------------------------------------------------------------- c22-16
f(id='q22-n90', sp='c22-16', niv='comprendre', type='qcm', b=5392,
  q="Que révèle, selon le cours, la fragmentation très poussée de la "
    "production pharmaceutique européenne ?",
  opts=["Que les médicaments européens sont de mauvaise qualité",
        "Qu’une part importante des principes actifs nécessaires aux "
        "médicaments européens est produite hors d’Europe, ce qui crée un "
        "risque de rupture d’approvisionnement",
        "Que l’Europe exporte l’essentiel de sa production pharmaceutique",
        "Que la recherche pharmaceutique européenne a disparu"],
  ans=1,
  why=["La qualité des médicaments n’est pas en cause.",
       "Le problème est celui des approvisionnements entrants, non des "
       "exportations.",
       "La recherche européenne existe : c’est la production des principes "
       "actifs qui est délocalisée."],
  exp="Le mécanisme est le suivant : DIPP très fragmentée → dépendance à "
      "plusieurs fournisseurs étrangers → choc sanitaire, fermeture ou "
      "pénurie → rupture d’approvisionnement → production ou consommation "
      "impossible. La question change donc de nature : il ne s’agit plus "
      "seulement de savoir combien coûte cette production, mais ce qui se "
      "passe si elle ne peut plus parvenir sur le territoire.",
  diss="Illustration retenue par les PIIEC santé, qui visent précisément à "
       "renforcer les capacités de production européennes."),

f(id='q22-n91', sp='c22-16', niv='raisonner', type='qcm', b=5637,
  q="Quel changement de logique le renouveau industriel contemporain "
    "traduit-il ?",
  opts=["Le passage d’une logique de résilience à une logique d’efficience",
        "Le passage d’une logique d’efficience à une logique de résilience : "
        "la localisation d’une production est évaluée non seulement par son "
        "coût mais aussi par le risque géopolitique de la dépendance",
        "Le passage d’une logique industrielle à une logique financière",
        "Le passage d’une logique nationale à une logique exclusivement "
        "mondiale"],
  ans=1,
  why=["Le sens du mouvement est inverse : l’efficience était la logique "
       "antérieure.",
       "La financiarisation est un autre phénomène, traité en début de "
       "chapitre.",
       "C’est au contraire l’échelle mondiale qui est remise en question au "
       "profit du national et de l’européen."],
  exp="Pendant plusieurs décennies, l’objectif était de localiser chaque "
      "étape de production là où elle était la plus efficace. Désormais une "
      "autre question apparaît : peut-on accepter qu’un bien essentiel soit "
      "produit presque exclusivement dans un pays avec lequel une crise "
      "géopolitique est possible ? Le coût n’est donc plus le seul critère de "
      "localisation : le risque politique y est intégré.",
  diss="Formule efficace : la mondialisation a optimisé les coûts, elle a "
       "sous-estimé les risques."),

f(id='q22-n92', sp='c22-16', niv='comprendre', type='qcm', b=5648,
  q="Quel signe institutionnel le cours relève-t-il pour illustrer la "
    "« nouvelle obsession » de la souveraineté industrielle en France ?",
  opts=["La création d’une banque publique d’investissement",
        "L’apparition du terme de souveraineté industrielle dans l’intitulé "
        "du ministère de l’Économie",
        "La nationalisation de plusieurs grandes entreprises",
        "La suppression du Crédit d’impôt recherche"],
  ans=1,
  why=["Bpifrance est créée en 2013, dans une logique de financement de "
       "l’innovation, et non comme marqueur de ce vocabulaire.",
       "Aucune vague de nationalisations françaises n’est évoquée à cette "
       "date.",
       "Le Crédit d’impôt recherche n’a pas été supprimé."],
  exp="L’idée de « produire davantage en France » s’impose dès 2020, et le "
      "terme de souveraineté industrielle apparaît jusque dans l’intitulé du "
      "ministère de l’Économie, auquel d’autres dimensions sont ensuite "
      "ajoutées. Ce changement de vocabulaire traduit une transformation "
      "profonde des priorités publiques — mais il peut aussi créer une "
      "confusion, car rechercher la souveraineté ne signifie pas "
      "nécessairement fermer son économie.",
  diss="Observation méthodologique utile : le vocabulaire officiel est un "
       "indicateur du changement de doctrine économique."),

f(id='q22-n93', sp='c22-16', niv='raisonner', type='vf', b=5733,
  q="Disposer d’un fournisseur unique situé sur le territoire national "
    "supprime le risque d’approvisionnement.",
  ans=False,
  exp="Un fournisseur unique national constitue aussi un risque : un choc "
      "domestique — catastrophe, grève, crise énergétique, accident "
      "industriel — peut interrompre sa production. C’est précisément ce que "
      "Combe et Guillou appellent le « mythe du potager » : croire qu’un pays "
      "serait plus sûr simplement parce qu’il produit tout lui-même. La "
      "souveraineté économique ne consiste donc pas à transformer l’économie "
      "nationale en potager autosuffisant : la diversification géographique "
      "des fournisseurs peut offrir davantage de résilience que la "
      "concentration de toute la production sur le territoire.",
  diss="Conclusion à retenir : ce qui crée la vulnérabilité est la "
       "concentration des sources, non leur caractère étranger."),

f(id='q22-n94', sp='c22-16', niv='appliquer', type='assoc', b=5824,
  q="Classez chaque situation selon qu’elle relève, d’après le cours, d’une "
    "dépendance préoccupante ou d’une dépendance acceptable.",
  ans=[["Un bien essentiel produit presque exclusivement par un pays avec "
        "lequel une crise géopolitique est possible",
        "Dépendance préoccupante"],
       ["Une part très importante des principes actifs pharmaceutiques "
        "produite hors d’Europe par un petit nombre de sites",
        "Dépendance préoccupante"],
       ["Un matériau critique dont une seule source d’approvisionnement "
        "existe",
        "Dépendance préoccupante"],
       ["Un pays qui importe massivement un bien, mais auprès de plusieurs "
        "fournisseurs concurrents", "Dépendance acceptable"],
       ["Un bien banal, aisément substituable, importé d’un marché mondial "
        "très concurrentiel", "Dépendance acceptable"]],
  exp="Le critère n’est ni le volume des importations ni leur origine "
      "étrangère, mais la concentration de la dépendance et la possibilité "
      "qu’elle soit instrumentalisée. La souveraineté industrielle consiste "
      "précisément à empêcher qu’une dépendance particulière devienne "
      "stratégiquement exploitable : elle suppose donc de la sélectivité, "
      "puisqu’il n’est pas rationnel de relocaliser une production simplement "
      "parce qu’elle est importée.",
  diss="Grille applicable à n’importe quel exemple d’actualité : la "
       "dépendance est-elle concentrée, et peut-elle servir de moyen de "
       "pression ?"),

# ------------------- formats complémentaires sur d’autres sous-parties
f(id='q22-n95', sp='c22-01', niv='appliquer', type='assoc', b=49,
  q="Associez chaque décision d’organisation de la production à la logique "
    "qu’elle illustre.",
  ans=[["L’entreprise produit elle-même le composant dans ses propres "
        "ateliers", "Faire : internaliser la production"],
       ["L’entreprise achète le composant à un fournisseur indépendant",
        "Faire faire : recourir au marché"],
       ["L’entreprise crée une filiale à l’étranger pour produire le "
        "composant", "Faire à l’étranger : investir directement"]],
  exp="C’est l’arbitrage que Coase formalise dès 1937 : la firme existe parce "
      "que le recours au marché engendre des coûts de transaction — recherche "
      "d’information, négociation, rédaction et contrôle des contrats — qu’il "
      "faut comparer aux coûts d’organisation liés à l’internalisation. "
      "L’ouverture internationale ajoute une troisième possibilité, qui "
      "combine internalisation du contrôle et localisation à l’étranger : "
      "c’est très exactement ce qu’est un investissement direct à "
      "l’étranger.",
  diss="Structure de raisonnement très utile : l’IDE est une réponse "
       "simultanée à une question d’organisation et à une question de "
       "localisation."),

f(id='q22-n96', sp='c22-04', niv='appliquer', type='assoc', b=1392,
  q="Associez chaque pratique à la forme de dumping dont elle relève, selon "
    "l’acception élargie présentée par le cours.",
  ans=[["Maintenir artificiellement un taux de change faible pour abaisser le "
        "prix des exportations", "Dumping monétaire"],
       ["Entretenir des salaires ou une protection sociale très faibles pour "
        "réduire les coûts de production", "Dumping social"],
       ["Attirer les bénéfices des entreprises par une imposition très "
        "basse", "Dumping fiscal"],
       ["Alléger les normes environnementales pour réduire les coûts de "
        "production", "Dumping environnemental"]],
  exp="Ces quatre formes élargissent la notion de dumping, qui au sens strict "
      "désigne la vente à l’étranger à un prix inférieur à celui pratiqué sur "
      "le marché intérieur. Elles posent toutes la même difficulté "
      "d’interprétation : distinguer un avantage volontairement entretenu "
      "pour fausser la concurrence d’un simple écart de niveau de "
      "développement, qui n’a rien d’illégitime.",
  diss="Nuance à conserver absolument : un pays pauvre à bas salaires ne "
       "pratique pas un dumping social du seul fait qu’il est pauvre."),

f(id='q22-n97', sp='c22-08', niv='raisonner', type='courte', b=2990,
  q="Quelle définition de la compétitivité d’une nation le cours propose-t-il "
    "de retenir malgré les critiques ?",
  ans={'modele': "Le cours propose de conserver le terme à condition de lui "
       "donner un sens précis : la compétitivité d’une nation est sa capacité "
       "à tirer avantage de son insertion internationale tout en améliorant "
       "durablement le niveau de vie de ses citoyens. Cette définition évite "
       "les trois erreurs que Krugman dénonce. Elle n’assimile pas la nation "
       "à une entreprise, puisqu’il ne s’agit pas de survivre sur un marché "
       "mais d’améliorer un niveau de vie. Elle ne fait pas du commerce un "
       "jeu à somme nulle, puisque plusieurs pays peuvent simultanément tirer "
       "avantage de leur insertion. Et elle ne confond pas compétitivité et "
       "solde commercial, puisque le critère retenu est le niveau de vie "
       "intérieur, qui dépend d’abord de la productivité. Conséquence "
       "pratique essentielle : réduire les salaires au maximum n’est pas "
       "nécessairement une stratégie de compétitivité, puisque le niveau de "
       "vie fait partie de l’objectif et non seulement du coût.",
       'cles': [{'f': ['insertion internationale', 'tirer avantage',
                       'ouverture'],
                 'l': "tirer avantage de l'insertion internationale"},
                {'f': ['niveau de vie', 'durablement', 'citoyen', 'population'],
                 'l': "améliorer durablement le niveau de vie"},
                {'f': ['pas une entreprise', 'nation', 'disparait'],
                 'l': "ne pas assimiler la nation à une entreprise"},
                {'f': ['somme nulle', 'mutuel', 'gain'],
                 'l': "le commerce n'est pas un jeu à somme nulle"},
                {'f': ['productivite', 'salaire', 'moins-disant',
                       'moins disant'],
                 'l': "la productivité, non le moins-disant salarial"}]},
  exp="Cette définition permet de conserver un concept utile tout en écartant "
      "les usages que Krugman juge dangereux : l’objectif n’est pas de battre "
      "les autres nations mais d’améliorer durablement le niveau de vie "
      "intérieur grâce à l’ouverture.",
  diss="Articulation possible : coût unitaire du travail et compétitivité "
       "hors-prix sont des moyens, le niveau de vie est la fin."),

f(id='q22-n98', sp='c22-10', niv='comprendre', type='vf', b=3565,
  q="Le Pilier 1 de la réforme fiscale de l’OCDE permet d’imposer une "
    "entreprise dans un pays où elle n’a aucune présence physique.",
  ans=True,
  exp="C’est précisément sa logique : le Pilier 1 réattribue une partie des "
      "droits à taxer vers les pays où se trouvent les consommateurs, même en "
      "l’absence d’établissement sur place. Il répond ainsi au problème posé "
      "par les activités numériques, qui permettent de réaliser un chiffre "
      "d’affaires important dans un pays sans y disposer d’installations. Le "
      "Pilier 2 traite d’une autre question, celle du niveau d’imposition, en "
      "instaurant un taux effectif minimal d’environ 15 %.",
  diss="Mémo : Pilier 1 = où taxer, Pilier 2 = combien taxer au minimum."),

f(id='q22-n99', sp='c22-11', niv='raisonner', type='qcm', b=4078,
  q="Pourquoi soutenir l’innovation sans maintenir de concurrence peut-il "
    "être inefficace, dans la logique néo-schumpétérienne ?",
  opts=["Parce que l’innovation ne dépend pas du financement",
        "Parce que la concurrence assure la sélection et la diffusion des "
        "innovations : sans elle, le soutien public risque de protéger des "
        "rentes",
        "Parce que les entreprises innovantes sont toujours de petite taille",
        "Parce que la concurrence réduit mécaniquement les dépenses de R&D"],
  ans=1,
  why=["Le financement est au contraire décisif, d’où le rôle de l’État "
       "entrepreneur.",
       "La taille des entreprises innovantes n’est pas l’argument retenu.",
       "La concurrence stimule au contraire l’innovation près de la "
       "frontière technologique."],
  exp="L’État facilite l’émergence des innovations en finançant la recherche "
      "et en assumant les risques initiaux ; la concurrence assure ensuite "
      "leur sélection et leur diffusion, en éliminant les projets "
      "inefficaces. Les deux fonctions sont donc complémentaires et non "
      "substituables : sans soutien public, les projets les plus risqués ne "
      "sont pas financés ; sans concurrence, rien n’oblige l’entreprise aidée "
      "à transformer le soutien en gains de productivité.",
  diss="C’est la clé de la synthèse du chapitre : l’efficacité de la "
       "politique industrielle dépend du maintien de la discipline "
       "concurrentielle."),

]
