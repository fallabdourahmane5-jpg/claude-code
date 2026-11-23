# -*- coding: utf-8 -*-
"""Chapitre 23 — corrections des questions héritées, sous-parties c23-01 à c23-07."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c23-01
'ch23-qcm-1': f(niv='connaitre', sp='c23-01', b=115,
 exp="L’analyse positive explique ce qui est : pourquoi les pays échangent, "
     "ce qu’ils échangent, avec qui et dans quelles proportions. L’analyse "
     "normative évalue ce qui devrait être : elle apprécie les conséquences "
     "de l’ouverture sur le bien-être, l’emploi ou les inégalités, et se "
     "prononce donc sur son caractère souhaitable. Les deux registres sont "
     "complémentaires mais ne se confondent pas.",
 why=["Évaluer si l’ouverture est souhaitable relève précisément du registre "
      "normatif.",
      "Mesurer les inégalités mondiales est un travail descriptif, mais ce "
      "n’est pas l’objet propre de la théorie du commerce.",
      "Défendre le libre-échange est une position doctrinale, celle du "
      "libre-échangisme."],
 diss="Distinction à poser dès l’introduction : on ne répond pas de la même "
      "manière à « pourquoi les pays échangent-ils ? » et à « faut-il "
      "s’ouvrir ? »."),
'ch23-qcm-51': f(niv='comprendre', sp='c23-01', b=173,
 exp="La courbe de l’éléphant met en évidence le paradoxe distributif de la "
     "mondialisation : entre 1988 et 2008, les classes moyennes des pays "
     "émergents et le centile le plus riche ont vu leurs revenus réels "
     "fortement progresser, tandis que la croissance a été la plus faible pour "
     "les classes populaires et moyennes des économies avancées. C’est ce "
     "creux qui donne à la mondialisation son coût politique dans les "
     "démocraties avancées.",
 why=["Le centile le plus riche figure au contraire parmi les grands "
      "gagnants de la période.",
      "Les classes moyennes émergentes sont les premières bénéficiaires du "
      "mouvement.",
      "Les plus pauvres de la planète progressent faiblement en valeur "
      "absolue, mais ce n’est pas le creux caractéristique de la courbe."],
 diss="À articuler avec Krugman 2019 : un gain mondial ne garantit pas "
      "l’acceptabilité politique, car les individus jugent la mondialisation "
      "à partir de leur propre situation."),
'ch23-vraifa-56': f(niv='comprendre', sp='c23-01', b=267,
 exp="Smith soutient l’inverse : les importations sont la finalité de "
     "l’échange, les exportations n’étant que le moyen de les financer. "
     "L’idée que l’importation appauvrit est mercantiliste : elle identifie "
     "la richesse à l’accumulation monétaire et fait du commerce un jeu de "
     "puissance proche d’une somme nulle. Le protectionnisme contemporain "
     "prend d’ailleurs souvent une forme néo-mercantiliste, qui consiste à "
     "limiter les importations tout en conservant un accès maximal aux "
     "marchés étrangers.",
 diss="Formule utilisable : chez Smith on exporte pour pouvoir importer ; "
      "chez les mercantilistes on exporte pour accumuler."),

# =============================================================== c23-02
'ch23-qcm-2': f(niv='comprendre', sp='c23-02', b=501,
 exp="Chez Smith, la spécialisation suppose un avantage absolu : un pays doit "
     "être plus productif que les autres dans une production pour avoir "
     "intérêt à s’y spécialiser. Un pays moins productif partout n’a donc "
     "rien à proposer et reste en principe exclu de l’échange. C’est "
     "précisément la limite que Ricardo lève en raisonnant sur les coûts "
     "d’opportunité internes.",
 why=["Se spécialiser selon le coût d’opportunité le plus faible est le "
      "raisonnement de Ricardo, non celui de Smith.",
      "L’exportation de facteurs de production n’est pas envisagée : les "
      "modèles classiques supposent leur immobilité internationale.",
      "Le gain automatique à l’échange est précisément ce que Smith ne peut "
      "garantir à un pays sans avantage absolu."],
 diss="Enchaînement de plan tout prêt : Smith ouvre la question, Ricardo "
      "généralise la réponse."),
'ch23-qcm-3': f(niv='connaitre', sp='c23-02', b=391,
 exp="Smith transpose à l’échelle internationale les trois effets de la "
     "division du travail : une dextérité accrue du producteur qui répète la "
     "même tâche, une réduction des pertes de temps liées au changement "
     "d’activité, et une incitation à innover, l’attention concentrée sur une "
     "opération favorisant l’invention de procédés et de machines. "
     "L’ouverture internationale prolonge donc la division du travail en "
     "élargissant le marché.",
 why=["Variété, concurrence et dimension sont les trois gains de l’ouverture "
      "chez Krugman, deux siècles plus tard.",
      "Recettes fiscales, emploi et balance commerciale relèvent d’une "
      "lecture mercantiliste ou comptable.",
      "Les trois formes d’économies d’échelle appartiennent à l’analyse des "
      "rendements croissants, non à Smith."],
 diss="Ne pas confondre les deux triplets : ceux de Smith viennent de la "
      "division du travail, ceux de Krugman de la taille du marché."),
'ch23-qcm-4': f(niv='appliquer', sp='c23-02', b=501,
 exp="Avec 90 contre 100 hommes-années pour le drap et 80 contre 120 pour le "
     "vin, le Portugal utilise moins de travail dans les deux productions : "
     "il possède donc un avantage absolu dans les deux. C’est ce qui rend "
     "l’exemple démonstratif, puisque l’échange reste mutuellement avantageux "
     "malgré ce double avantage absolu — résultat impossible dans le cadre de "
     "Smith.",
 why=["Le Portugal est également plus productif dans le drap : son avantage "
      "absolu ne se limite pas au vin.",
      "L’Angleterre a besoin de 100 hommes-années contre 90 au Portugal pour "
      "le drap : elle n’y détient donc aucun avantage absolu.",
      "Les deux pays ne sont pas également productifs, puisque les besoins en "
      "travail diffèrent dans les deux productions."],
 diss="Réflexe de méthode : comparer d’abord les productivités entre pays "
      "(avantage absolu), puis les rapports internes (avantage comparatif)."),
'ch23-qcm-37': f(niv='comprendre', sp='c23-02', b=415,
 exp="La richesse étant identifiée à l’accumulation de métaux précieux, le "
     "gain d’un pays correspond à la perte d’un autre : le commerce est "
     "conçu comme une compétition pour les marchés, les ressources et la "
     "puissance. L’État doit donc encourager les exportations et limiter les "
     "importations. C’est très exactement ce que Smith conteste, en montrant "
     "que la spécialisation accroît la production totale et rend l’échange "
     "mutuellement avantageux.",
 why=["Le jeu à somme positive est la conception libre-échangiste, qui "
      "s’oppose au mercantilisme.",
      "La convergence des économies n’est pas un thème mercantiliste.",
      "L’échange de variétés relève des théories contemporaines du commerce "
      "intra-branche."],
 diss="Opposition doctrinale à nommer correctement : libre-échangisme contre "
      "mercantilisme — les faits, eux, sont le libre-échange et le "
      "protectionnisme."),
'ch23-vraifa-55': f(niv='comprendre', sp='c23-02', b=439,
 exp="C’est précisément la démonstration de Ricardo : ce qui compte n’est pas "
     "la productivité absolue mais le coût d’opportunité, c’est-à-dire ce à "
     "quoi un pays renonce en produisant un bien plutôt qu’un autre. Un pays "
     "désavantagé dans toutes les productions conserve donc toujours un "
     "avantage comparatif dans l’une d’elles, et l’échange redevient "
     "mutuellement avantageux. L’avantage comparatif est en ce sens une "
     "notion plus générale que l’avantage absolu.",
 diss="Point de rigueur : un pays ne peut pas être désavantagé "
      "comparativement partout, puisque les coûts d’opportunité sont des "
      "rapports internes."),

# =============================================================== c23-03
'ch23-qcm-5': f(niv='appliquer', sp='c23-03', b=536,
 exp="Le coût d’opportunité du drap au Portugal se calcule en rapportant le "
     "travail nécessaire au drap à celui nécessaire au vin : 90/80 = 1,125. "
     "Produire une unité de drap coûte donc au Portugal 1,125 unité de vin, "
     "contre 100/120 = 0,83 en Angleterre. L’Angleterre renonce à moins de "
     "vin pour produire du drap : c’est là son avantage comparatif.",
 why=["0,83 vin est le coût d’opportunité du drap en Angleterre, non au "
      "Portugal.",
      "Exprimer le coût du drap en unités de drap n’a pas de sens : le coût "
      "d’opportunité se mesure dans l’autre bien.",
      "1,2 drap correspond au coût d’opportunité du vin en Angleterre "
      "(120/100)."],
 diss="Règle de calcul à retenir : coût d’opportunité du bien A = travail "
      "nécessaire à A divisé par travail nécessaire à B, dans le même pays."),
'ch23-qcm-6': f(niv='comprendre', sp='c23-03', b=573,
 exp="Les deux gains sont deux lectures du même effet. À facteurs donnés, la "
     "production mondiale augmente — de 4 à 4,325 unités dans l’exemple du "
     "cours. À production mondiale inchangée, le même volume s’obtient avec "
     "moins de travail, soit 30 unités économisées. Dans les deux cas, la "
     "réallocation des facteurs vers les emplois où leur coût d’opportunité "
     "est le plus faible accroît l’efficacité productive globale.",
 why=["Baisse des prix et hausse des salaires sont des effets possibles, mais "
      "ce ne sont pas les deux gains que Ricardo démontre.",
      "Excédent commercial et recettes douanières relèvent d’une lecture "
      "mercantiliste de l’échange.",
      "Variété et concurrence renforcée sont des gains mis en évidence par "
      "les théories contemporaines, notamment Krugman."],
 diss="Les deux formulations sont interchangeables en dissertation : plus de "
      "production à facteurs donnés, ou autant de production avec moins de "
      "facteurs."),
'ch23-questi-75': f(niv='raisonner', sp='c23-03', b=536),
'ch23-questi-76': f(niv='appliquer', sp='c23-03', b=573),

# =============================================================== c23-04
'ch23-qcm-7': f(niv='comprendre', sp='c23-04', b=738,
 exp="Ricardo établit l’existence du gain à l’échange mais laisse indéterminé "
     "le prix international, donc le partage de ce gain. L’apport propre de "
     "John Stuart Mill est de montrer que ce prix doit se situer entre les "
     "rapports d’échange internes des deux pays — entre 0,88 et 1,2 dans "
     "l’exemple ricardien. Hors de ces bornes, un pays préfère l’autarcie, et "
     "plus le prix est proche de la borne qui lui est favorable, plus son gain "
     "est élevé.",
 why=["La démonstration de l’existence du gain est l’apport de Ricardo "
      "lui-même.",
      "Les dotations factorielles sont introduites par Heckscher et Ohlin.",
      "La mobilité internationale des facteurs est au contraire exclue par "
      "ces modèles."],
 diss="Formule décisive : Ricardo montre que l’échange est avantageux, Mill "
      "montre pour qui il l’est davantage."),
'ch23-qcm-8': f(niv='comprendre', sp='c23-04', b=836,
 exp="Chez Marx, la concurrence entre capitalistes impose l’accumulation, "
     "tandis que l’armée industrielle de réserve maintient les salaires à un "
     "niveau bas. La demande intérieure devient alors insuffisante pour "
     "absorber la production : l’exportation n’est plus un bienfait "
     "réciproque mais la résolution provisoire d’une contradiction interne du "
     "mode de production.",
 why=["La demande de variété est l’explication de Lassudrie-Duchêne, dans un "
      "cadre théorique entièrement différent.",
      "La rareté des dotations factorielles est l’explication du modèle HOS.",
      "La sous-évaluation monétaire est un instrument de politique "
      "commerciale contemporain."],
 diss="Renversement à souligner : le commerce cesse d’être un échange "
      "mutuellement avantageux pour devenir un débouché nécessaire."),
'ch23-questi-77': f(niv='raisonner', sp='c23-04', b=751),
'ch23-questi-78': f(niv='raisonner', sp='c23-04', b=819),

# =============================================================== c23-05
'ch23-qcm-9': f(niv='connaitre', sp='c23-05', b=961,
 exp="Lénine retient cinq caractéristiques de l’impérialisme : la "
     "concentration du capital et l’apparition de monopoles, la fusion du "
     "capital bancaire et du capital industriel, l’importance des "
     "exportations de capitaux, le partage des marchés entre grands groupes "
     "et le partage des territoires entre grandes puissances. La mobilité "
     "internationale parfaite du travail n’en fait pas partie : c’est une "
     "hypothèse de modèle, étrangère à cette analyse.",
 why=["La fusion du capital bancaire et du capital industriel fait bien "
      "partie des cinq caractéristiques.",
      "Les exportations de capitaux en font également partie.",
      "Le partage des territoires entre grandes puissances est la cinquième "
      "caractéristique."],
 diss="Liste à retenir dans l’ordre : monopoles, fusion banque-industrie, "
      "exportation de capitaux, partage des marchés, partage des "
      "territoires."),
'ch23-qcm-10': f(niv='connaitre', sp='c23-05', b=1008,
 exp="La thèse de Prebisch (1950) porte sur la dégradation tendancielle des "
     "termes de l’échange des produits primaires : sur la période 1875-1938, "
     "les prix des produits primaires progressent moins vite que ceux des "
     "produits manufacturés. Un pays spécialisé dans le primaire doit donc "
     "exporter des quantités croissantes pour importer la même quantité de "
     "biens manufacturés : sa spécialisation, conforme à ses avantages "
     "comparatifs, lui devient défavorable.",
 why=["L’échange inégal par les salaires est la thèse d’Arghiri Emmanuel.",
      "La croissance appauvrissante est le mécanisme analysé par Bhagwati "
      "(1958).",
      "La désindustrialisation précoce est le concept de Dani Rodrik."],
 diss="Quatre critiques à distinguer soigneusement : Prebisch (prix "
      "relatifs), Emmanuel (salaires), Bhagwati (effet volume sur le prix "
      "mondial), Rodrik (calendrier de la désindustrialisation)."),
'ch23-qcm-11': f(niv='comprendre', sp='c23-05', b=1064,
 exp="Chez Arghiri Emmanuel, l’inégalité de l’échange provient des écarts de "
     "salaires. À productivité comparable, des salaires très bas se "
     "répercutent dans des prix d’exportation très bas : l’échange transfère "
     "alors de la valeur du pays à bas salaires vers le pays à hauts "
     "salaires, sans qu’aucune contrainte formelle ne soit exercée. "
     "L’inégalité est inscrite dans les prix eux-mêmes.",
 why=["Les écarts de productivité sont l’explication ricardienne de la "
      "spécialisation, non celle de l’échange inégal.",
      "Les droits de douane sont un instrument de politique commerciale, "
      "extérieur à ce mécanisme.",
      "Les coûts de transport jouent sur les prix mais ne constituent pas un "
      "transfert de valeur entre pays."],
 diss="Nuance importante : l’échange inégal n’exige aucune coercition, il "
      "résulte du jeu normal des prix."),
'ch23-qcm-12': f(niv='comprendre', sp='c23-05', b=1074,
 exp="La croissance appauvrissante de Bhagwati (1958) suppose que le pays "
     "pèse suffisamment sur le marché mondial du produit pour que son offre "
     "supplémentaire fasse baisser le prix mondial. Si cette dégradation des "
     "termes de l’échange dépasse le gain de volume, le pays produit "
     "davantage mais s’appauvrit. L’effet n’est donc possible ni pour un "
     "petit pays, ni lorsque la demande mondiale est très élastique.",
 why=["Un pays petit sur le marché mondial est price taker : son offre "
      "supplémentaire ne modifie pas le prix.",
      "L’abondance en capital ne joue aucun rôle dans ce mécanisme.",
      "Le protectionnisme éducateur est l’argument de List, sans rapport avec "
      "cette analyse."],
 diss="Condition à ne jamais oublier : la croissance appauvrissante suppose "
      "un pouvoir de marché, ce qui en limite fortement la portée."),
'ch23-qcm-13': f(niv='raisonner', sp='c23-05', b=1137,
 exp="Ces analyses sont formulées au moment de la grande divergence, lorsque "
     "l’écart entre le Nord et le Sud se creuse : elles décrivent donc "
     "fidèlement leur époque. Or l’hypermondialisation s’accompagne au "
     "contraire du rattrapage de nombreux pays émergents, ce qui limite la "
     "portée d’une lecture faisant de l’échange un mécanisme nécessairement "
     "appauvrissant pour les pays en développement.",
 why=["Les salaires sont au contraire au cœur de l’analyse d’Emmanuel.",
      "Ces analyses ne reposent pas sur l’hypothèse de concurrence "
      "imparfaite, qui appartient aux théories contemporaines.",
      "Le raisonnement en coût d’opportunité est celui de Ricardo, que ces "
      "auteurs critiquent."],
 diss="Position équilibrée : ces critiques restent précieuses pour les "
      "économies restées spécialisées dans le primaire, moins pour celles qui "
      "ont monté en gamme."),
'ch23-questi-79': f(niv='raisonner', sp='c23-05', b=1162),

# =============================================================== c23-06
'ch23-qcm-14': f(niv='comprendre', sp='c23-06', b=1472,
 exp="Dans le modèle HOS, les technologies et les préférences sont supposées "
     "identiques entre pays : seules les dotations factorielles diffèrent. "
     "L’abondance relative d’un facteur en réduit le prix relatif, ce qui "
     "abaisse le coût des productions qui l’utilisent intensivement et crée "
     "l’avantage comparatif. C’est le rapport des dotations, et non leur "
     "niveau absolu, qui est déterminant.",
 why=["L’écart de productivité du travail est l’explication ricardienne, que "
      "HOS cherche précisément à dépasser.",
      "Les rendements d’échelle croissants sont introduits par Krugman.",
      "La demande de différence est l’explication de Lassudrie-Duchêne."],
 diss="Enchaînement complet à restituer : abondance relative → prix relatif "
      "du facteur ↓ → coût relatif du bien intensif ↓ → spécialisation → "
      "exportation."),
'ch23-qcm-15': f(niv='connaitre', sp='c23-06', b=1453,
 exp="Les hypothèses « 2 × 2 × 2 » désignent deux pays, deux biens et deux "
     "facteurs de production. S’y ajoutent l’immobilité internationale des "
     "facteurs, leur mobilité entre secteurs à l’intérieur de chaque pays, "
     "des technologies et des préférences identiques, la concurrence parfaite "
     "et des dotations considérées comme données à un moment déterminé — "
     "c’est-à-dire un cadre statique.",
 why=["Deux périodes, deux prix et deux firmes ne correspondent à aucune "
      "hypothèse du modèle.",
      "Le modèle comporte effectivement plusieurs théorèmes et plusieurs "
      "auteurs, mais ce n’est pas le sens de la notation.",
      "Les types de protection et leurs effets relèvent de la politique "
      "commerciale, non du modèle HOS."],
 diss="Les hypothèses sont le vrai sujet : c’est leur abandon progressif qui "
      "engendre toutes les théories postérieures."),
'ch23-vraifa-57': f(niv='comprendre', sp='c23-06', b=1338,
 exp="Le modèle de Ricardo suppose au contraire l’immobilité internationale "
     "des facteurs et leur mobilité à l’intérieur du pays. Cette seconde "
     "hypothèse est largement démentie par la réalité des reconversions : un "
     "travailleur déplacé par l’ouverture ne dispose pas nécessairement des "
     "compétences requises dans le secteur en expansion, et la mobilité "
     "géographique a elle-même un coût. Ricardo le reconnaît partiellement "
     "dans son analyse des Corn Laws, où il admet qu’une ouverture trop "
     "brutale impose des coûts d’ajustement.",
 diss="Écart très citable entre le modèle abstrait de Ricardo et ses "
      "recommandations concrètes."),
'ch23-questi-80': f(niv='comprendre', sp='c23-06', b=1470),

# =============================================================== c23-07
'ch23-qcm-16': f(niv='comprendre', sp='c23-07', b=1556,
 exp="Le théorème Stolper-Samuelson (1941) établit que l’ouverture augmente "
     "la rémunération réelle du facteur relativement abondant et réduit celle "
     "du facteur relativement rare. Le commerce des biens peut en effet être "
     "lu comme un commerce indirect des facteurs : un pays exporte les "
     "services du facteur incorporé dans ses exportations et importe ceux "
     "contenus dans les biens étrangers. Le commerce redistribue donc à "
     "l’intérieur de chaque pays, et les perdants se repèrent au facteur "
     "qu’ils détiennent.",
 why=["Une hausse uniforme de tous les revenus est exactement ce que le "
      "théorème exclut.",
      "L’égalisation des productivités n’est pas l’objet du théorème, qui "
      "porte sur la rémunération des facteurs.",
      "L’ouverture accroît au contraire la concurrence."],
 diss="Conséquence normative majeure : un pays peut gagner globalement alors "
      "que certains de ses habitants perdent réellement."),
'ch23-qcm-17': f(niv='appliquer', sp='c23-07', b=1613,
 exp="Dans un pays relativement abondant en travail peu qualifié, c’est ce "
     "facteur qui est relativement abondant : la spécialisation exportatrice "
     "en augmente la demande et soutient donc sa rémunération. La même "
     "mécanique produit ainsi des effets de sens opposé selon la dotation du "
     "pays : dans une économie avancée abondante en qualifications, "
     "l’ouverture pèse au contraire sur le salaire relatif des moins "
     "qualifiés.",
 why=["La baisse du salaire des moins qualifiés est la prédiction pour un "
      "pays avancé abondant en travail qualifié.",
      "Le théorème prévoit précisément un effet sur les salaires, et non une "
      "neutralité.",
      "La rente du capital n’est pas le canal retenu ici : le facteur "
      "abondant est le travail peu qualifié."],
 diss="Symétrie à exploiter : le même théorème explique la contestation de la "
      "mondialisation au Nord et son soutien au Sud."),
'ch23-qcm-18': f(niv='comprendre', sp='c23-07', b=1663,
 exp="Le théorème de Rybczynski (1955) établit que l’accroissement d’un "
     "facteur augmente plus que proportionnellement la production du bien qui "
     "l’utilise intensivement. Les dotations deviennent donc endogènes : une "
     "modification de la population, des ressources ou du stock de capital "
     "déplace les spécialisations. Les avantages comparatifs cessent "
     "d’être permanents et peuvent être construits par l’investissement, "
     "l’éducation et la R&D.",
 why=["Des dotations données une fois pour toutes est exactement l’hypothèse "
      "que Rybczynski lève.",
      "L’égalisation du prix des facteurs est une autre conséquence du "
      "modèle, distincte de ce théorème.",
      "Le caractère interne des économies d’échelle relève de l’analyse des "
      "rendements croissants."],
 diss="Point de bascule du chapitre : avec Rybczynski, la spécialisation "
      "devient un objet de politique économique."),
'ch23-qcm-19': f(niv='connaitre', sp='c23-07', b=1750,
 exp="Le test de Leontief (1953) confronte la prédiction de HOS au cas "
     "américain : un pays aussi abondant en capital devrait exporter "
     "principalement des biens intensifs en capital. Or les exportations "
     "américaines apparaissent moins intensives en capital que les biens "
     "substituables aux importations. Le résultat est contre-intuitif pour "
     "l’économie la plus abondante en capital, et il conduit à réviser la "
     "définition des facteurs plutôt qu’à rejeter le raisonnement.",
 why=["C’est l’inverse qui est constaté : les exportations américaines "
      "apparaissent moins, et non plus, intensives en capital que prévu.",
      "Le niveau des salaires américains n’est pas l’objet du test.",
      "Les droits de douane américains ne sont pas en cause dans ce "
      "paradoxe."],
 diss="Leçon de méthode : un résultat empirique contraire invite d’abord à "
      "interroger la mesure des concepts."),
'ch23-qcm-20': f(niv='connaitre', sp='c23-07', b=1802,
 exp="Baldwin montre en 1971, avec une méthodologie proche de celle de "
     "Leontief, que les exportations américaines sont intensives en travail "
     "qualifié et en savoir technologique. Le paradoxe disparaît dès que le "
     "travail cesse d’être traité comme homogène : les États-Unis exportent "
     "moins du travail en général que du travail hautement qualifié, facteur "
     "dont ils sont relativement abondants. La logique factorielle est ainsi "
     "réhabilitée.",
 why=["Les terres agricoles ne sont pas la dotation décisive mise en "
      "évidence.",
      "Le capital financier n’est pas le facteur retenu : le paradoxe porte "
      "précisément sur le capital.",
      "L’énergie n’intervient pas dans cette résolution."],
 diss="Enchaînement complet à restituer : Leontief trouve l’anomalie, "
      "Baldwin la résout en redéfinissant les facteurs."),
'ch23-qcm-21': f(niv='comprendre', sp='c23-07', b=1862,
 exp="Les coûts d’opportunité ricardiens supposent de connaître ce que "
     "produirait un pays en autarcie complète. Or ce contrefactuel n’existe "
     "pas : il n’est pas observable. Les avantages comparatifs révélés "
     "procèdent donc à l’inverse : ils infèrent les spécialisations a "
     "posteriori, à partir de la structure observée des exportations, des "
     "importations et des soldes commerciaux, comparée à celle du commerce "
     "mondial.",
 why=["Les droits de douane faussent effectivement les prix, mais ce n’est "
      "pas la raison invoquée par le cours.",
      "Les dotations factorielles sont au contraire assez bien mesurées.",
      "La publication des coûts par les firmes n’est pas le problème : c’est "
      "la situation d’autarcie qui est inobservable."],
 diss="Conséquence à assumer : les avantages comparatifs révélés décrivent "
      "des spécialisations effectives, non des coûts d’opportunité."),
'ch23-vraifa-58': f(niv='connaitre', sp='c23-09', b=2096,
 exp="C’est bien ce qui fait l’originalité de HOS par rapport à Ricardo : à "
     "technologies identiques, les seules différences de dotations suffisent "
     "à engendrer l’échange. Ricardo partait au contraire d’écarts de "
     "productivité qu’il constatait sans les expliquer. Cette hypothèse est "
     "néanmoins forte, et ce sont précisément les approches "
     "néo-technologiques qui l’abandonneront pour expliquer l’origine des "
     "différences de productivité.",
 diss="Articulation de plan : HOS explique l’origine de l’avantage par les "
      "dotations, les néo-technologiques par l’innovation."),
'ch23-questi-81': f(niv='raisonner', sp='c23-07', b=1633),
'ch23-questi-82': f(niv='raisonner', sp='c23-07', b=1708),

}
