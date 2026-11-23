# -*- coding: utf-8 -*-
"""Chapitre 23 — questions nouvelles, sous-parties c23-06 à c23-10."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c23-06
f(id='q23-n23', sp='c23-06', niv='connaitre', type='qcm', b=1394,
  q="Quel déplacement Eli Heckscher opère-t-il en 1919 par rapport à "
    "Ricardo ?",
  opts=["Il explique l’avantage comparatif par les différences de dotations "
        "en facteurs de production, et non plus seulement par les écarts de "
        "productivité",
        "Il introduit les économies d’échelle croissantes",
        "Il montre que les facteurs circulent librement entre les pays",
        "Il abandonne la notion d’avantage comparatif"],
  ans=0,
  why=["Les économies d’échelle sont introduites bien plus tard, par "
       "Krugman.",
       "Le modèle conserve au contraire l’immobilité internationale des "
       "facteurs.",
       "Heckscher conserve l’avantage comparatif : il en change l’origine."],
  exp="La dotation factorielle correspond à la quantité de facteurs de "
      "production dont dispose une économie. Heckscher remet en cause "
      "l’explication exclusivement ricardienne par les différentiels de "
      "productivité et propose de regarder les différences de dotations. "
      "Ohlin complétera en 1933 en montrant que ce qui compte n’est pas la "
      "quantité absolue de capital ou de travail, mais leur abondance "
      "relative.",
  diss="Enchaînement à citer avec les dates : Heckscher 1919 (dotations), "
       "Ohlin 1933 (abondance relative), Stolper-Samuelson 1941 (effets "
       "distributifs), Rybczynski 1955 (dotations évolutives)."),

f(id='q23-n24', sp='c23-06', niv='comprendre', type='qcm', b=1410,
  q="Que signifie, chez Ohlin, qu’un pays est « relativement abondant » dans "
    "un facteur ?",
  opts=["Qu’il possède une quantité absolue élevée de ce facteur",
        "Qu’il dispose d’une quantité plus importante de ce facteur "
        "relativement à l’autre facteur que son partenaire commercial",
        "Que ce facteur y est plus productif qu’ailleurs",
        "Que ce facteur y est plus cher qu’ailleurs"],
  ans=1,
  why=["La quantité absolue ne suffit pas : un grand pays peut être abondant "
       "en tout, ce qui n’indique aucune spécialisation.",
       "La productivité relève de l’explication ricardienne, que HOS écarte "
       "en supposant des technologies identiques.",
       "Un facteur relativement abondant est au contraire relativement moins "
       "cher."],
  exp="L’analyse d’Ohlin est fondamentalement relative : un pays n’est pas "
      "simplement « riche en capital » ou « riche en travail », il est "
      "davantage doté dans un facteur par rapport à l’autre et relativement "
      "à ses partenaires. C’est cette double relativité — entre facteurs et "
      "entre pays — qui rend la comparaison possible et qui fait du modèle "
      "une théorie de la spécialisation et non de la richesse.",
  diss="Erreur classique à éviter : comparer des niveaux de dotations au lieu "
       "de comparer des rapports."),

f(id='q23-n25', sp='c23-06', niv='appliquer', type='ordre', b=1470,
  q="Remettez dans l’ordre le mécanisme complet du théorème "
    "Heckscher-Ohlin.",
  ans=["Le pays A dispose relativement de davantage de capital que le pays B",
       "Le capital y est donc relativement moins coûteux : son prix relatif "
       "est plus faible",
       "Le coût de la production intensive en capital y est relativement plus "
       "faible",
       "Le pays A acquiert un avantage comparatif dans cette production",
       "Il s’y spécialise et l’exporte, tandis que le pays B exporte le bien "
       "intensif en travail"],
  exp="Le modèle met en relation deux différences relatives : les pays "
      "diffèrent par leurs dotations factorielles, les biens diffèrent par "
      "l’intensité avec laquelle ils utilisent ces facteurs. Une production "
      "est intensive dans un facteur lorsqu’elle utilise relativement "
      "davantage de ce facteur que l’autre production. La rareté relative "
      "détermine le prix des facteurs — r pour le capital, w pour le "
      "travail — et c’est ce prix qui engendre l’avantage comparatif.",
  diss="Restituer les deux relativités est ce qui distingue une bonne copie : "
       "dotations relatives des pays, intensités relatives des biens."),

f(id='q23-n26', sp='c23-06', niv='raisonner', type='qcm', b=1498,
  q="Pourquoi Ricardo ne faisait-il apparaître qu’un seul facteur de "
    "production ?",
  opts=["Parce qu’il ignorait l’existence du capital",
        "Parce que, chez les classiques, le capital peut être réduit à du "
        "« travail incorporé », ce qui ramène tous les coûts à une seule "
        "unité",
        "Parce que le capital était négligeable à son époque",
        "Parce qu’il supposait le capital parfaitement mobile entre pays"],
  ans=1,
  why=["Ricardo analyse largement le capital : ce n’est pas une question "
       "d’ignorance.",
       "L’importance quantitative du capital n’est pas l’argument retenu par "
       "le cours.",
       "La mobilité internationale du capital est au contraire exclue par ces "
       "modèles."],
  exp="Pour les classiques, la valeur d’un bien peut se ramener à la somme "
      "des heures de travail nécessaires à sa fabrication, machines incluses, "
      "puisque celles-ci ont elles-mêmes été produites par du travail. "
      "L’analyse ricardienne exprime donc tous les coûts dans une seule "
      "unité. HOS rompt avec cette réduction en traitant le capital et le "
      "travail comme deux facteurs autonomes, ce qui est la condition même du "
      "raisonnement sur les dotations.",
  diss="Point de méthode : passer d’un à deux facteurs n’est pas un détail "
       "technique, c’est ce qui rend possible une théorie de la répartition."),

# ------------------------------------------------------------- c23-07
f(id='q23-n27', sp='c23-07', niv='comprendre', type='qcm', b=1570,
  q="Pourquoi le commerce des biens peut-il être lu comme un commerce "
    "indirect des facteurs de production ?",
  opts=["Parce que les travailleurs migrent en même temps que les "
        "marchandises",
        "Parce qu’en exportant un bien, un pays exporte les services des "
        "facteurs incorporés dans ce bien, et importe ceux contenus dans les "
        "biens étrangers",
        "Parce que les entreprises délocalisent leur capital",
        "Parce que les prix des facteurs sont fixés au niveau mondial"],
  ans=1,
  why=["Les migrations ne sont pas en cause : les facteurs sont supposés "
       "immobiles internationalement.",
       "La délocalisation du capital est un autre phénomène, celui de l’IDE.",
       "L’égalisation des prix des facteurs est une conséquence de ce "
       "mécanisme, non sa cause."],
  exp="Lorsqu’un pays exporte un produit intensif en capital et en travail "
      "qualifié, il exporte indirectement les services de ces facteurs ; en "
      "important un produit intensif en travail peu qualifié, il importe "
      "indirectement les services de ce travail. Le commerce modifie donc "
      "l’offre et la demande des différents facteurs à l’intérieur de chaque "
      "pays, ce qui explique ses effets sur leurs rémunérations.",
  diss="Conséquence forte : le commerce peut partiellement substituer la "
       "mobilité des biens à celle des facteurs, et tend ainsi à rapprocher "
       "leurs rémunérations internationales."),

f(id='q23-n28', sp='c23-07', niv='appliquer', type='ordre', b=1594,
  q="Remettez dans l’ordre le mécanisme par lequel l’ouverture peut accentuer "
    "les inégalités salariales dans une économie avancée.",
  ans=["Le pays, relativement abondant en travail qualifié, importe des "
       "produits intensifs en travail peu qualifié",
       "Cela équivaut à une augmentation indirecte de l’offre de travail peu "
       "qualifié",
       "Les secteurs domestiques intensifs en travail non qualifié reculent",
       "La demande de travail peu qualifié diminue tandis que celle de "
       "qualifications augmente",
       "La rémunération relative des travailleurs peu qualifiés subit une "
       "pression à la baisse"],
  exp="C’est l’application du théorème Stolper-Samuelson à un pays avancé. La "
      "même mécanique produit l’effet inverse dans une économie relativement "
      "abondante en travail peu qualifié : la spécialisation exportatrice y "
      "augmente la demande de ce travail et peut soutenir les bas salaires, "
      "contribuant à réduire certaines inégalités internes.",
  diss="Nuance indispensable : le commerce n’explique pas à lui seul les "
       "inégalités, qui dépendent aussi du progrès technique et des "
       "institutions du marché du travail."),

f(id='q23-n29', sp='c23-07', niv='raisonner', type='courte', b=1708,
  q="Comment un État peut-il construire de nouvelles dotations factorielles, "
    "et avec quelle conséquence sur la nature de la concurrence "
    "internationale ?",
  ans={'modele': "Le théorème de Rybczynski (1955) rend les dotations "
       "endogènes : l’accroissement d’un facteur augmente plus que "
       "proportionnellement la production du bien qui l’utilise "
       "intensivement. Une modification de la population, des ressources ou "
       "du stock de capital déplace donc les spécialisations. Un État peut "
       "alors agir volontairement sur ses dotations : investir dans "
       "l’éducation et la formation pour accroître la dotation en travail "
       "qualifié, dans la R&D pour développer le savoir technologique, dans "
       "le capital productif pour élever le stock de capital. Plusieurs "
       "économies parties d’une abondance relative en travail peu qualifié et "
       "peu coûteux ont ainsi déplacé leur spécialisation vers des activités "
       "à plus forte valeur ajoutée. La conséquence est décisive : lorsque "
       "les États cherchent à acquérir les mêmes capacités technologiques que "
       "leurs concurrents, l’avantage comparatif cesse d’être hérité pour "
       "devenir un objet de stratégie industrielle, et la transformation des "
       "dotations devient une dimension de la rivalité technologique "
       "internationale.",
       'cles': [{'f': ['rybczynski', 'plus que proportionnel', 'endogene'],
                 'l': "Rybczynski rend les dotations endogènes"},
                {'f': ['education', 'formation', 'qualification'],
                 'l': "investir dans l'éducation et les qualifications"},
                {'f': ['r&d', 'recherche', 'technologi'],
                 'l': "investir dans la R&D et la technologie"},
                {'f': ['capital', 'accumulation', 'investissement productif'],
                 'l': "accumuler du capital productif"},
                {'f': ['valeur ajoutee', 'gamme', 'deplacer'],
                 'l': "déplacer la spécialisation vers des activités à plus forte valeur ajoutée"},
                {'f': ['strateg', 'rivalite', 'politique industrielle',
                       'competition technologique'],
                 'l': "l'avantage comparatif devient stratégique"}]},
  exp="Les avantages comparatifs peuvent être construits : l’investissement "
      "dans l’éducation, la R&D et le capital productif modifie "
      "progressivement les dotations factorielles et permet de déplacer la "
      "spécialisation. L’avantage cesse alors d’être hérité pour devenir un "
      "objet de stratégie industrielle.",
  diss="Charnière du chapitre : c’est ce résultat qui rend légitime de parler "
       "de politique commerciale et industrielle dans un cadre pourtant "
       "libéral."),

f(id='q23-n30', sp='c23-07', niv='comprendre', type='qcm', b=1832,
  q="Pourquoi la fragmentation internationale de la production redonne-t-elle "
    "de la pertinence aux avantages comparatifs ?",
  opts=["Parce qu’elle supprime les différences entre pays",
        "Parce que les firmes ne localisent plus un bien entier dans un pays "
        "mais répartissent chaque tâche selon les dotations les plus "
        "avantageuses",
        "Parce qu’elle rend les coûts de transport négligeables",
        "Parce qu’elle uniformise les technologies utilisées"],
  ans=1,
  why=["La fragmentation exploite au contraire les différences entre "
       "territoires.",
       "Les coûts de transport restent un déterminant de la localisation.",
       "L’uniformisation technologique n’est ni constatée ni nécessaire au "
       "raisonnement."],
  exp="Le raisonnement s’applique désormais non plus à un bien entier mais à "
      "chaque tâche : conception, fabrication de composants, assemblage, "
      "services. On parle alors d’un commerce de tâches, dans lequel "
      "l’avantage comparatif détermine la localisation de chaque étape. "
      "L’intuition ricardienne retrouve ainsi une grande pertinence dans les "
      "chaînes de valeur mondiales, alors même que les biens ne sont plus "
      "produits intégralement dans un seul pays.",
  diss="Articulation avec le chapitre précédent : la DIPP de Baldwin donne au "
       "raisonnement ricardien son terrain d’application contemporain."),

# ------------------------------------------------------------- c23-08
f(id='q23-n31', sp='c23-08', niv='connaitre', type='qcm', b=1894,
  q="Dans quels domaines la France présente-t-elle, selon le cours, des "
    "avantages comparatifs révélés ?",
  opts=["L’aéronautique, certains produits de luxe et plusieurs services",
        "Les matières premières énergétiques et la métallurgie de base",
        "L’électronique grand public et le textile",
        "Les terres rares et les batteries"],
  ans=0,
  why=["Les ressources énergétiques absentes du territoire figurent au "
       "contraire parmi les désavantages français.",
       "L’électronique grand public et le textile relèvent de spécialisations "
       "que la France a largement perdues.",
       "Les terres rares et les batteries sont des domaines de dépendance, "
       "non d’avantage."],
  exp="Les avantages comparatifs français reflètent une combinaison de "
      "compétences technologiques, de capital humain, de savoir-faire "
      "historiques et de spécialisation dans certains services, tandis que "
      "les désavantages concernent notamment les ressources énergétiques "
      "absentes du territoire et certaines industries manufacturières. La "
      "comparaison avec la Chine — nombreux produits manufacturés et "
      "technologiques, mais dépendance à plusieurs matières premières — et le "
      "Brésil — avantages fortement orientés vers le primaire — montre la "
      "diversité des structures.",
  diss="Méthode à rappeler : ces avantages sont révélés, c’est-à-dire "
       "inférés de la structure observée des flux, et non calculés à partir "
       "de coûts d’opportunité."),

f(id='q23-n32', sp='c23-08', niv='connaitre', type='qcm', b=1918,
  q="Qu’appelle-t-on reprimarisation ?",
  opts=["Le retour de l’agriculture de subsistance",
        "Le processus par lequel les secteurs primaires reprennent une place "
        "croissante dans les exportations et la structure productive d’une "
        "économie",
        "La hausse du prix des matières premières sur les marchés mondiaux",
        "La nationalisation des industries extractives"],
  ans=1,
  why=["L’agriculture de subsistance est un mode de production, non une "
       "évolution de la structure des exportations.",
       "La hausse des prix est la cause possible du phénomène, non le "
       "phénomène lui-même.",
       "La nationalisation est une décision de politique économique, "
       "distincte de cette évolution structurelle."],
  exp="La reprimarisation apparaît lorsque la hausse de rentabilité des "
      "matières premières attire les facteurs de production vers les secteurs "
      "primaires et réduit relativement l’importance de l’industrie "
      "manufacturière. Elle est particulièrement problématique si elle "
      "intervient avant que le pays ait atteint un niveau de développement "
      "élevé — ce qui rejoint la désindustrialisation précoce analysée par "
      "Rodrik. Le Brésil en fournit l’illustration.",
  diss="Mécanisme à expliciter : c’est le marché qui réalloue les facteurs, "
       "sans qu’aucune décision politique ne l’organise."),

f(id='q23-n33', sp='c23-08', niv='raisonner', type='qcm', b=1933,
  q="Pourquoi la désindustrialisation précoce est-elle particulièrement "
    "problématique, selon Rodrik ?",
  opts=["Parce que les services ne créent aucun emploi",
        "Parce que l’économie abandonne les activités manufacturières avant "
        "qu’elles aient permis d’accumuler suffisamment de productivité, de "
        "capital et de revenus",
        "Parce que l’agriculture ne peut pas se moderniser",
        "Parce que le commerce international devient impossible"],
  ans=1,
  why=["Les services créent des emplois, mais pas nécessairement avec les "
       "mêmes gains de productivité.",
       "La modernisation agricole n’est pas l’objet de cette analyse.",
       "Le commerce international n’est nullement empêché."],
  exp="L’industrie constitue historiquement le secteur des gains de "
      "productivité les plus importants : s’en détourner trop tôt prive le "
      "pays du principal moteur de rattrapage. Dans les économies avancées, "
      "la désindustrialisation est intervenue après une longue phase "
      "d’industrialisation et de hausse des niveaux de vie ; la "
      "désindustrialisation précoce intervient au contraire à un niveau de "
      "revenu très inférieur.",
  diss="À relier aux dépendances : un avantage comparatif peut créer des "
       "vulnérabilités, car exporter un produit ne signifie pas maîtriser "
       "l’ensemble des intrants nécessaires."),

f(id='q23-n34', sp='c23-08', niv='comprendre', type='qcm', b=1815,
  q="Qu’est-ce que le commerce inter-branche, et quel modèle l’explique le "
    "mieux ?",
  opts=["Un pays exporte et importe des biens de la même branche ; Krugman "
        "l’explique",
        "Un pays exporte des biens de certaines branches et importe des biens "
        "d’autres branches ; HOS l’explique particulièrement bien",
        "Un pays n’échange qu’avec ses voisins immédiats ; Linder l’explique",
        "Un pays n’exporte que des services ; Vernon l’explique"],
  ans=1,
  why=["L’échange croisé dans la même branche est le commerce intra-branche, "
       "que HOS ne peut pas expliquer.",
       "La proximité géographique n’est pas le critère : Linder raisonne sur "
       "la similarité des demandes.",
       "La spécialisation dans les services n’est pas l’objet de cette "
       "distinction."],
  exp="HOS est particulièrement performant pour expliquer le commerce "
      "inter-branche entre économies aux dotations très différentes : chaque "
      "pays exporte les produits intensifs dans ses facteurs relativement "
      "abondants. C’est le « commerce de différences ». Sa limite décisive "
      "est le commerce intra-branche entre pays comparables, qui exige de "
      "mobiliser la différenciation des produits et la demande de différence.",
  diss="Répartition des rôles à annoncer clairement : HOS pour le commerce "
       "Nord-Sud, les théories contemporaines pour le commerce Nord-Nord."),

f(id='q23-n35', sp='c23-08', niv='appliquer', type='assoc', b=1896,
  q="Associez chaque structure de spécialisation révélée au pays qu’elle "
    "caractérise, d’après le cours.",
  ans=[["Des positions fortes dans l’aéronautique, certains produits de luxe "
        "et plusieurs services", "France"],
       ["De nombreux produits manufacturés et technologiques, mais une "
        "dépendance à plusieurs matières premières", "Chine"],
       ["Des avantages fortement orientés vers les productions primaires",
        "Brésil"]],
  exp="Ces trois profils montrent que les spécialisations révélées diffèrent "
      "fortement selon les économies, et qu’elles portent la trace de "
      "l’histoire productive de chaque pays : compétences technologiques et "
      "savoir-faire pour la France, montée en gamme manufacturière pour la "
      "Chine, abondance en ressources naturelles pour le Brésil. Aucun de ces "
      "profils n’est définitif, puisque les dotations peuvent être "
      "construites.",
  diss="Comparaison fructueuse : la Chine illustre la montée en gamme "
       "réussie, le Brésil le risque de reprimarisation."),

f(id='q23-n36', sp='c23-08', niv='raisonner', type='vf', b=1940,
  q="Détenir un avantage comparatif dans une production garantit de maîtriser "
    "l’ensemble des intrants nécessaires à cette production.",
  ans=False,
  exp="Le cours souligne au contraire qu’un avantage comparatif peut "
      "s’accompagner de dépendances : exporter un produit ne signifie pas "
      "maîtriser l’ensemble des intrants nécessaires à sa fabrication. Une "
      "économie peut donc être très compétitive dans l’assemblage ou la "
      "transformation d’un bien tout en dépendant entièrement de fournisseurs "
      "étrangers pour ses composants, ses matériaux critiques ou son énergie. "
      "La performance commerciale et la sécurité d’approvisionnement sont "
      "deux questions distinctes.",
  diss="Articulation avec le chapitre précédent : c’est exactement le "
       "raisonnement qui fonde la notion de souveraineté industrielle "
       "sélective."),

# ------------------------------------------------------------- c23-09
f(id='q23-n37', sp='c23-09', niv='comprendre', type='qcm', b=2178,
  q="En quoi l’introduction du capital humain prolonge-t-elle l’approche "
    "néo-factorielle ?",
  opts=["Elle remplace les dotations factorielles par la technologie",
        "Elle élargit le raisonnement factoriel : l’avantage peut venir des "
        "investissements accumulés dans les compétences et les connaissances "
        "des travailleurs",
        "Elle supprime la distinction entre travail qualifié et non qualifié",
        "Elle introduit la concurrence imparfaite"],
  ans=1,
  why=["Le remplacement par la technologie caractérise les approches "
       "néo-technologiques.",
       "Elle approfondit au contraire cette distinction en la rendant "
       "cumulative.",
       "La concurrence imparfaite est introduite par les nouvelles théories "
       "du commerce international."],
  exp="Le capital humain désigne l’ensemble des connaissances, compétences et "
      "qualifications incorporées aux individus et susceptibles d’accroître "
      "leur productivité. Son introduction change la nature du facteur "
      "« travail » : la qualification n’est plus une caractéristique fixe du "
      "travailleur mais le résultat d’un investissement, ce qui rend la "
      "dotation construisible. L’approche néo-factorielle conserve donc la "
      "logique de HOS tout en enrichissant la liste des facteurs.",
  diss="Convergence à souligner : capital humain et théorème de Rybczynski "
       "conduisent à la même conclusion, celle d’avantages comparatifs "
       "construits."),

f(id='q23-n38', sp='c23-09', niv='comprendre', type='qcm', b=2195,
  q="Quelle question les approches néo-technologiques cherchent-elles à "
    "résoudre ?",
  opts=["Comment mesurer les dotations factorielles",
        "Pourquoi les productivités diffèrent entre pays — question que "
        "Ricardo constatait sans l’expliquer",
        "Comment répartir le gain à l’échange",
        "Pourquoi les consommateurs recherchent la variété"],
  ans=1,
  why=["La mesure des dotations relève des approches néo-factorielles.",
       "La répartition du gain est la question de John Stuart Mill.",
       "La recherche de variété est l’explication de Lassudrie-Duchêne."],
  exp="Les approches néo-technologiques endogénéisent l’avantage ricardien : "
      "les différences de productivité entre nations sont elles-mêmes "
      "expliquées par des écarts de technologie, de recherche et de capacité "
      "d’innovation. Posner (1961) attribue l’avantage à une avance "
      "technologique temporaire, Vernon (1966) l’inscrit dans le cycle de vie "
      "du produit. Dans les deux cas, l’avantage n’est plus une donnée mais "
      "le résultat d’un effort d’innovation.",
  diss="Distinction à tenir fermement : néo-factoriel = quels facteurs, "
       "néo-technologique = pourquoi les productivités diffèrent."),

f(id='q23-n39', sp='c23-09', niv='appliquer', type='ordre', b=2235,
  q="Remettez dans l’ordre le mécanisme par lequel l’avantage technologique "
    "se dissipe, chez Posner.",
  ans=["Une entreprise d’un pays avancé innove et crée un nouveau produit",
       "La demande du nouveau produit vient d’abord du marché intérieur",
       "Le pays innovateur bénéficie d’un monopole technologique et exporte le "
       "produit",
       "Les exportations diffusent elles-mêmes l’innovation vers les pays "
       "importateurs",
       "Ceux-ci imitent progressivement, et l’écart de productivité initial "
       "se réduit"],
  exp="L’avantage technologique contient donc les germes de sa propre "
      "disparition. La conséquence est importante : l’avantage dépend du flux "
      "d’innovations et non d’un stock, de sorte que seule la capacité à "
      "innover continuellement maintient la spécialisation. Un pays qui "
      "cesse d’innover voit son avantage s’éroder par imitation.",
  diss="Conséquence de politique économique : soutenir la R&D n’est pas un "
       "luxe mais la condition du maintien de la spécialisation."),

f(id='q23-n40', sp='c23-09', niv='comprendre', type='vf', b=2154,
  q="L’approche néo-factorielle de Keesing invalide le modèle HOS.",
  ans=False,
  exp="Elle le réhabilite au contraire, en distinguant les qualités de "
      "travail : les États-Unis n’exportent pas des biens intensifs en "
      "travail en général, mais des biens intensifs en travail qualifié, "
      "facteur dont ils disposent relativement en abondance. La logique du "
      "modèle — spécialisation selon le facteur relativement abondant — est "
      "entièrement conservée ; seule la liste des facteurs est enrichie. "
      "C’est exactement la démarche qui permet à Baldwin de résoudre en 1971 "
      "le paradoxe de Leontief.",
  diss="Leçon épistémologique utile : une anomalie empirique peut conduire à "
       "affiner un modèle plutôt qu’à l’abandonner."),

f(id='q23-n41', sp='c23-09', niv='raisonner', type='qcmm', b=2127,
  q="Quels éléments les théories contemporaines ajoutent-elles aux théories "
    "traditionnelles ? (plusieurs réponses)",
  opts=["L’hétérogénéité du travail",
        "L’innovation et la technologie comme sources d’avantage",
        "La différenciation des produits",
        "Les économies d’échelle et les rendements croissants",
        "Les comportements de demande",
        "L’immobilité internationale des facteurs"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : la qualification devient une dotation à part entière.",
       "Exacte : c’est l’objet des approches néo-technologiques.",
       "Exacte : elle permet d’expliquer le commerce intra-branche.",
       "Exacte : c’est l’apport de Krugman.",
       "Exacte : Lassudrie-Duchêne et Linder déplacent l’analyse vers la "
       "demande.",
       "Inexacte : l’immobilité internationale des facteurs est au contraire "
       "une hypothèse traditionnelle."],
  exp="Les théories contemporaines ne suppriment pas l’intuition des "
      "avantages comparatifs : elles la complètent afin d’expliquer des "
      "échanges que Ricardo et HOS ne permettaient pas de comprendre, à "
      "commencer par le commerce intra-branche entre pays proches. Elles se "
      "divisent en deux ensembles : les prolongements des théories "
      "traditionnelles, qui précisent l’origine de l’avantage, et les "
      "nouvelles théories, qui introduisent échelle, demande et "
      "différenciation.",
  diss="Plan en deux temps directement utilisable : prolonger, puis dépasser "
       "les théories traditionnelles."),

# ------------------------------------------------------------- c23-10
f(id='q23-n42', sp='c23-10', niv='appliquer', type='ordre', b=2334,
  q="Remettez dans l’ordre les quatre phases du cycle de vie international du "
    "produit de Vernon.",
  ans=["Naissance : la production reste près du marché innovateur, car la "
       "technologie est instable et exige R&D, qualifications et "
       "consommateurs à revenu élevé",
       "Croissance : la demande augmente, les volumes réduisent les coûts et "
       "les premières exportations apparaissent",
       "Maturité : le procédé se standardise, la concurrence se déplace vers "
       "les coûts et la production est délocalisée vers des pays à salaires "
       "plus faibles",
       "Le pays initialement innovateur importe désormais le produit qu’il "
       "avait inventé"],
  exp="Vernon transforme l’avantage comparatif en phénomène dynamique : la "
      "localisation optimale d’un produit évolue avec sa maturation "
      "technologique, si bien qu’un même bien peut successivement être "
      "produit et exporté par des pays différents. Les téléviseurs à écran "
      "plat, passés du Japon à la Corée puis à la Chine et au Vietnam, en "
      "fournissent l’illustration.",
  diss="Articulation précieuse : le cycle du produit explique à la fois les "
       "IDE verticaux et les délocalisations étudiés au chapitre précédent."),

f(id='q23-n43', sp='c23-10', niv='connaitre', type='qcm', b=2410,
  q="À quelle analyse Lassudrie-Duchêne recourt-il pour expliquer le commerce "
    "intra-branche ?",
  opts=["La concurrence monopolistique développée par Chamberlin en 1933",
        "La théorie des jeux appliquée aux politiques commerciales",
        "Le modèle HOS enrichi d’un troisième facteur",
        "La théorie de la croissance endogène"],
  ans=0,
  why=["La théorie des jeux est mobilisée pour le dilemme du prisonnier "
       "commercial et pour Brander-Spencer.",
       "L’ajout de facteurs caractérise les approches néo-factorielles.",
       "La croissance endogène n’est pas mobilisée dans ce passage."],
  exp="Deux pays similaires peuvent échanger parce que leurs produits ne sont "
      "pas perçus comme parfaitement identiques : l’explication ne repose pas "
      "sur des dotations factorielles fondamentalement différentes mais sur "
      "la différenciation des produits et sur la préférence des consommateurs "
      "pour la variété. Le cadre de la concurrence monopolistique permet "
      "précisément de penser des producteurs offrant des variétés distinctes "
      "d’un même type de bien.",
  diss="Déplacement théorique majeur à nommer : l’explication passe de "
       "l’offre à la demande."),

f(id='q23-n44', sp='c23-10', niv='appliquer', type='assoc', b=2459,
  q="Classez chaque situation selon le type de différenciation des produits "
    "qu’elle illustre.",
  ans=[["Deux automobiles de gamme équivalente qui se distinguent par la "
        "marque, le design et la réputation", "Différenciation horizontale"],
       ["Deux vins de qualité comparable mais d’origines et de styles "
        "différents", "Différenciation horizontale"],
       ["Une berline d’entrée de gamme et une berline haut de gamme vendues "
        "à des prix très différents", "Différenciation verticale"],
       ["Un textile bas de gamme importé et un textile de luxe exporté par le "
        "même pays", "Différenciation verticale"]],
  exp="La différenciation horizontale distingue des produits de qualité "
      "comparable selon des caractéristiques subjectives, ce qui permet aux "
      "consommateurs de rechercher de la variété sans changer de gamme. La "
      "différenciation verticale repose sur une hiérarchie de qualité et de "
      "gamme : elle explique que deux pays de niveaux de développement "
      "différents puissent échanger dans la même branche, à des prix "
      "différents.",
  diss="Conséquence analytique : seule la différenciation verticale permet un "
       "commerce intra-branche entre pays inégalement développés."),

f(id='q23-n45', sp='c23-10', niv='raisonner', type='courte', b=2514,
  q="Comment Linder explique-t-il que les pays échangent d’autant plus qu’ils "
    "se ressemblent ?",
  ans={'modele': "Chez Linder, l’avantage comparatif peut naître de la "
       "demande intérieure. Une demande domestique représentative, "
       "c’est-à-dire suffisamment importante, permet à une entreprise "
       "d’augmenter sa production, de réaliser des économies d’échelle et de "
       "gagner en compétitivité avant d’exporter : c’est en répondant à son "
       "marché national qu’une industrie acquiert l’échelle et l’expérience "
       "nécessaires. Mais une forte demande domestique ne suffit pas à créer "
       "du commerce : encore faut-il trouver des acheteurs étrangers. Or une "
       "entreprise conçoit ses produits en fonction des caractéristiques de "
       "son marché national ; elle exporte donc plus facilement vers des pays "
       "dont les consommateurs présentent des préférences et un pouvoir "
       "d’achat proches. La proximité des niveaux de vie rapproche les "
       "structures de demande, ce qui explique que les pays de niveau "
       "comparable échangent davantage entre eux — exactement l’inverse de la "
       "prédiction de HOS, qui attend un commerce entre pays dissemblables.",
       'cles': [{'f': ['demande representative', 'demande interieure',
                       'marche domestique'],
                 'l': "une demande intérieure représentative"},
                {'f': ['echelle', 'volume', 'experience', 'competitivite'],
                 'l': "elle permet d'atteindre l'échelle et la compétitivité"},
                {'f': ['concoit', 'caracteristique', 'adapte', 'national'],
                 'l': "les produits sont conçus pour le marché national"},
                {'f': ['ressemble', 'proche', 'similaire', 'niveau de vie'],
                 'l': "ils trouvent preneur dans des pays aux demandes proches"},
                {'f': ['hos', 'inverse', 'dissemblable', 'contraire'],
                 'l': "une prédiction inverse de celle de HOS"}]},
  exp="Pour Linder, la proximité des niveaux de vie rapproche les structures "
      "de demande : un bien conçu pour les consommateurs d’un pays a "
      "davantage de chances d’être demandé dans une économie dont les "
      "préférences et le pouvoir d’achat sont similaires.",
  diss="Opposition très rentable en dissertation : HOS prédit un commerce "
       "entre pays différents, Linder un commerce entre pays semblables — et "
       "ce sont les faits qui tranchent."),

]
