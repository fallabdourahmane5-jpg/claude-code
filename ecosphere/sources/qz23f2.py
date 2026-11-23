# -*- coding: utf-8 -*-
"""Chapitre 23 — corrections des questions héritées, sous-parties c23-08 à c23-14."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c23-08
'ch23-qcm-22': f(niv='comprendre', sp='c23-08', b=1936,
 exp="Dans les économies avancées, la désindustrialisation est intervenue "
     "après une longue phase d’industrialisation et de hausse des niveaux de "
     "vie. Rodrik montre que plusieurs pays en développement voient au "
     "contraire l’industrie reculer à un niveau de revenu très inférieur à "
     "celui qu’avaient atteint les pays avancés au même stade. Ces pays sont "
     "alors privés du principal moteur historique de rattrapage, l’industrie "
     "concentrant les gains de productivité, sans avoir accumulé "
     "suffisamment de capital ni de revenus.",
 why=["Les pays avancés se désindustrialisent effectivement, mais c’est le "
      "calendrier des pays en développement qui définit le concept.",
      "L’industrie ne disparaît pas au profit de l’agriculture : la "
      "reprimarisation est un phénomène distinct et plus spécifique.",
      "Les services créent des emplois, mais pas nécessairement avec les "
      "mêmes gains de productivité."],
 diss="À articuler avec la reprimarisation : la hausse de rentabilité des "
      "matières premières attire les facteurs vers le primaire et réduit "
      "relativement l’industrie."),
'ch23-qcm-23': f(niv='comprendre', sp='c23-08', b=2052,
 exp="Les théories traditionnelles expliquent le commerce par des différences "
     "— de productivité chez Ricardo, de dotations dans HOS — et prévoient "
     "donc un commerce inter-branche entre pays dissemblables. Or le commerce "
     "intra-branche voit des pays comparables échanger des produits de la "
     "même branche dans les deux sens : ni les écarts de productivité ni les "
     "différences de dotations ne peuvent expliquer que la France exporte et "
     "importe simultanément des automobiles.",
 why=["Le commerce intra-branche concerne surtout les produits manufacturés "
      "différenciés, non les produits primaires.",
      "L’hypothèse de coûts de transport nuls appartient aux modèles "
      "traditionnels eux-mêmes.",
      "Le commerce intra-branche concerne largement les biens, et non "
      "seulement les services."],
 diss="C’est la limite décisive : elle oblige à mobiliser la différenciation "
      "des produits, la concurrence monopolistique et la demande de "
      "différence."),
'ch23-questi-83': f(niv='raisonner', sp='c23-08', b=2052),

# =============================================================== c23-09
'ch23-qcm-24': f(niv='connaitre', sp='c23-09', b=2143,
 exp="L’apport de Keesing (1966) est de faire de la qualification du travail "
     "une dotation factorielle à part entière : les exportations américaines "
     "incorporent relativement davantage de travail qualifié, les "
     "importations davantage de travail peu qualifié. C’est le cœur de "
     "l’approche néo-factorielle : le modèle HOS est conservé, mais sa liste "
     "de facteurs est enrichie. Le capital humain élargira ensuite encore "
     "cette nomenclature.",
 why=["L’introduction des économies d’échelle est l’apport de Krugman.",
      "La mesure des termes de l’échange renvoie aux travaux de Prebisch.",
      "La formalisation du protectionnisme éducateur est également due à "
      "Krugman, à partir de List."],
 diss="Vocabulaire à employer avec précision : les approches néo-factorielles "
      "enrichissent la liste des facteurs, les néo-technologiques expliquent "
      "les écarts de productivité."),
'ch23-qcm-25': f(niv='comprendre', sp='c23-09', b=2218,
 exp="Pour Posner (1961), l’innovation procure au pays innovateur un monopole "
     "technologique qui lui permet d’exporter le nouveau produit, mais cet "
     "avantage est temporaire : les exportations diffusent elles-mêmes "
     "l’innovation vers les pays importateurs, qui finissent par l’imiter et "
     "réduisent l’écart de productivité initial. L’avantage dépend donc du "
     "flux d’innovations et non d’un stock : seule la capacité à innover "
     "continuellement maintient la spécialisation.",
 why=["Un avantage définitif contredirait le mécanisme d’imitation au cœur de "
      "l’analyse.",
      "L’avantage est au contraire entièrement fondé sur la technologie.",
      "La dotation en capital est l’explication du modèle HOS, non celle de "
      "Posner."],
 diss="Formule frappante : l’avantage technologique contient les germes de "
      "sa propre disparition."),
'ch23-questi-84': f(niv='comprendre', sp='c23-09', b=2129),

# =============================================================== c23-10
'ch23-qcm-26': f(niv='comprendre', sp='c23-10', b=2321,
 exp="Dans le cycle de vie du produit de Vernon (1966), la phase de maturité "
     "se caractérise par la standardisation du procédé : la technologie "
     "devenant stable et banalisée, la concurrence se déplace de l’innovation "
     "vers les coûts, et la firme est incitée à délocaliser tout ou partie de "
     "sa production vers des économies à salaires plus faibles. Le pays "
     "innovateur finit par importer le produit qu’il a créé.",
 why=["L’exportation massive par le pays innovateur caractérise la phase de "
      "croissance, qui précède la maturité.",
      "La demande ne disparaît pas : elle est au contraire élevée et "
      "banalisée.",
      "Les coûts fixes ne sont pas le facteur déterminant de cette phase."],
 diss="Quatre phases à restituer dans l’ordre : naissance, croissance et "
      "premières exportations, maturité et délocalisation, importation par le "
      "pays innovateur."),
'ch23-qcm-27': f(niv='appliquer', sp='c23-10', b=2366,
 exp="L’industrie des écrans plats illustre le cycle international du "
     "produit : innovation japonaise, puis production coréenne, puis chinoise "
     "et vietnamienne. Le déplacement suit exactement la banalisation du "
     "procédé : tant que la technologie est instable, la production reste "
     "près du marché innovateur ; dès qu’elle est standardisée, le coût "
     "devient le critère déterminant de localisation.",
 why=["Le théorème H-O expliquerait un échange entre pays aux dotations "
      "différentes, mais pas ce déplacement successif dans le temps.",
      "La croissance appauvrissante suppose une dégradation du prix mondial "
      "liée au volume exporté.",
      "Le paradoxe de Bairoch porte sur la relation entre protection et "
      "croissance au XIXᵉ siècle."],
 diss="Exemple à mobiliser pour montrer que la spécialisation est un "
      "processus et non un état."),
'ch23-qcm-28': f(niv='comprendre', sp='c23-10', b=2474,
 exp="La demande de différence de Lassudrie-Duchêne explique le commerce "
     "intra-branche entre pays semblables : les consommateurs recherchent, à "
     "l’intérieur d’une même branche, des produits différents de l’offre "
     "nationale. L’explication vient donc de la demande et non de l’offre, ce "
     "qui permet de comprendre des échanges croisés entre économies aux "
     "dotations proches. Lassudrie-Duchêne mobilise à cet effet la "
     "concurrence monopolistique développée par Chamberlin en 1933.",
 why=["Le commerce inter-branche est précisément celui que les théories "
      "traditionnelles expliquent déjà.",
      "La dégradation des termes de l’échange est la thèse de Prebisch.",
      "Les pics tarifaires relèvent de l’analyse de la protection."],
 diss="Point d’articulation : la variété devient une source de gain à "
      "l’échange, indépendamment de tout écart de coût."),
'ch23-qcm-29': f(niv='connaitre', sp='c23-10', b=2459,
 exp="La différenciation verticale repose sur une hiérarchie de qualité et de "
     "gamme à l’intérieur d’une même branche. Elle explique que deux pays "
     "puissent produire le même type de bien tout en se spécialisant dans des "
     "gammes différentes, ce qui alimente un commerce intra-branche fondé sur "
     "les écarts de qualité et de prix — y compris entre pays de niveaux de "
     "développement différents. La différenciation horizontale distingue au "
     "contraire des produits de qualité comparable selon des caractéristiques "
     "subjectives comme la marque, le design ou la réputation.",
 why=["Des caractéristiques distinctes à qualité comparable définissent la "
      "différenciation horizontale.",
      "La différence de pays d’origine ne constitue pas en soi une "
      "différenciation du produit.",
      "Le circuit de distribution n’est pas un critère de différenciation du "
      "produit lui-même."],
 diss="Distinction opératoire : horizontale = variété à gamme égale, "
      "verticale = montée ou descente en gamme."),
'ch23-qcm-30': f(niv='comprendre', sp='c23-10', b=2495,
 exp="Chez Linder, la structure de la demande intérieure participe à la "
     "construction de la compétitivité : une demande domestique "
     "représentative, c’est-à-dire suffisamment importante, permet à une "
     "industrie d’augmenter sa production, de réaliser des économies "
     "d’échelle et de gagner en compétitivité avant d’exporter. Il en résulte "
     "une seconde conséquence : les pays échangent d’autant plus qu’ils se "
     "ressemblent, puisque la proximité des niveaux de vie rapproche les "
     "structures de demande.",
 why=["La dotation en capital est l’explication de HOS.",
      "La subvention publique relève de la politique industrielle, non de "
      "cette analyse de la demande.",
      "La sous-évaluation monétaire est un instrument de compétitivité-prix, "
      "étranger au raisonnement de Linder."],
 diss="Renversement à souligner : l’avantage comparatif peut venir du marché "
      "intérieur et non des coûts."),
'ch23-vraifa-60': f(niv='raisonner', sp='c23-10', b=1633,
 exp="Le cours insiste sur la pluralité des causes : le théorème "
     "Stolper-Samuelson fournit bien un mécanisme reliant commerce et "
     "répartition des revenus, mais l’évolution effective des inégalités "
     "dépend aussi du progrès technique biaisé en faveur des qualifications, "
     "des institutions du marché du travail et des politiques publiques. "
     "Attribuer au seul commerce la montée des inégalités salariales dans les "
     "pays avancés est donc un raccourci.",
 diss="Argument de Krugman dans La mondialisation n’est pas coupable (1996) : "
      "le progrès technique et l’évolution de la demande pèsent davantage que "
      "la seule concurrence internationale."),
'ch23-questi-85': f(niv='comprendre', sp='c23-10', b=2336),

# =============================================================== c23-11
'ch23-qcm-31': f(niv='connaitre', sp='c23-11', b=2584,
 exp="Les trois gains de l’ouverture chez Krugman sont la sélection par la "
     "concurrence, qui élimine les firmes les moins productives et pousse les "
     "autres à innover ; le gain de variété, qui élargit le choix des "
     "consommateurs mais aussi celui des entreprises en intrants et en "
     "fournisseurs ; et l’effet de dimension, qui agrandit le marché, "
     "augmente les volumes et permet d’exploiter des économies d’échelle. Ces "
     "gains existent même entre pays strictement identiques, puisqu’ils ne "
     "reposent pas sur des différences mais sur la taille du marché.",
 why=["Dextérité, temps et innovation sont les trois gains de la division du "
      "travail chez Smith.",
      "Recettes, emploi et change relèvent d’une lecture mercantiliste.",
      "Production mondiale et économie de facteurs sont les deux gains de "
      "Ricardo."],
 diss="L’effet de dimension est l’apport décisif : il rend le gain à "
      "l’échange indépendant de toute différence entre pays."),
'ch23-qcm-32': f(niv='connaitre', sp='c23-11', b=2618,
 exp="Une économie d’échelle externe correspond à une baisse du coût unitaire "
     "liée à la taille du secteur ou du territoire, et non à celle de "
     "l’entreprise : la firme bénéficie de la présence des autres. C’est le "
     "fondement des districts industriels et des effets d’agglomération — la "
     "compétitivité d’une firme dépend alors du lieu où elle est implantée, "
     "indépendamment de ses propres caractéristiques.",
 why=["La taille de l’entreprise définit les économies d’échelle internes.",
      "La baisse des salaires réduit les coûts mais ne relève pas des "
      "rendements croissants.",
      "La hausse des droits de douane renchérit au contraire les intrants "
      "importés."],
 diss="Conséquence majeure : avec des économies externes, la géographie "
      "devient un déterminant autonome de la compétitivité."),
'ch23-qcm-33': f(niv='connaitre', sp='c23-11', b=2666,
 exp="Marshall (1890) identifie trois externalités expliquant la "
     "concentration géographique : un réseau dense de fournisseurs "
     "spécialisés, un vaste bassin de main-d’œuvre qualifiée — qui réduit "
     "simultanément le risque de pénurie de compétences pour les entreprises "
     "et le risque de chômage pour les travailleurs — et la circulation des "
     "connaissances, les savoir-faire n’étant pas parfaitement brevetables ni "
     "appropriables. Elles expliquent que la productivité d’une firme dépende "
     "du lieu où elle est implantée.",
 why=["Transport, énergie et fiscalité sont des coûts de localisation, non "
      "les externalités marshalliennes.",
      "Capital, travail et terre sont les facteurs de production classiques.",
      "Variété, prix et qualité sont des caractéristiques de l’offre de "
      "produits."],
 diss="Mécanisme cumulatif à nommer : ces trois externalités rendent les "
      "territoires déjà spécialisés de plus en plus attractifs."),
'ch23-vraifa-64': f(niv='raisonner', sp='c23-11', b=2584,
 exp="C’est l’apport décisif de Krugman : les trois gains — sélection par la "
     "concurrence, variété, effet de dimension — existent même entre pays "
     "strictement identiques, puisqu’ils reposent sur la taille du marché et "
     "non sur des différences de dotations ou de productivité. L’ouverture "
     "ne se contente donc plus d’exploiter un avantage préexistant : elle "
     "peut elle-même créer et renforcer la compétitivité grâce aux économies "
     "d’échelle.",
 diss="Rupture théorique à exploiter : avec Krugman, le commerce n’a plus "
      "besoin de différences pour être avantageux."),
'ch23-questi-86': f(niv='raisonner', sp='c23-11', b=2541),

# =============================================================== c23-12
'ch23-qcm-34': f(niv='appliquer', sp='c23-12', b=2763,
 exp="Bangalore illustre un effet d’agglomération amorcé par une implantation "
     "initiale : celle de Texas Instruments dans les années 1980. Cette "
     "première installation attire main-d’œuvre, fournisseurs et concurrents, "
     "qui renforcent à leur tour l’attractivité du lieu, jusqu’à faire de "
     "Bangalore un grand pôle de services informatiques et technologiques. "
     "L’avantage est donc acquis, non hérité : c’est une illustration de la "
     "dépendance au sentier.",
 why=["Le protectionnisme éducateur suppose une protection temporaire du "
      "marché, absente de cet exemple.",
      "La croissance appauvrissante concerne la dégradation du prix mondial "
      "d’un produit exporté.",
      "Le dumping monétaire renvoie à la sous-évaluation du taux de change."],
 diss="Deux autres exemples à garder en réserve : Toulouse, où la décision "
      "publique crée le noyau initial, et la Silicon Valley, où "
      "l’infrastructure scientifique joue ce rôle."),
'ch23-qcm-35': f(niv='appliquer', sp='c23-12', b=2812,
 exp="Avec des rendements croissants, il faut distinguer avantage potentiel "
     "et avantage acquis. Le Vietnam peut disposer d’une courbe de coût moyen "
     "potentiellement inférieure à celle de la Chine, mais à faible "
     "production son coût unitaire reste supérieur au prix chinois : il ne "
     "peut atteindre le seuil Q0 à partir duquel les économies d’échelle "
     "jouent. Un producteur potentiellement plus efficace est donc exclu par "
     "la seule antériorité de son concurrent — ce qui réhabilite "
     "partiellement le protectionnisme éducateur.",
 why=["Ses coûts potentiels sont au contraire plus faibles : c’est tout "
      "l’intérêt de l’exemple.",
      "La dotation en travail n’est pas en cause dans ce raisonnement.",
      "Le niveau des droits de douane vietnamiens n’intervient pas ici."],
 diss="Notion à mobiliser : le seuil Q0 fonctionne comme une barrière à "
      "l’entrée créée par les volumes accumulés."),

# =============================================================== c23-13
'ch23-qcm-36': f(niv='connaitre', sp='c23-13', b=2987,
 exp="Le libre-échange et le protectionnisme sont d’abord des situations "
     "concrètes, donc des faits : dans le premier cas les échanges circulent "
     "sans obstacles importants, dans le second ils sont volontairement "
     "entravés. Le libre-échangisme et le mercantilisme sont en revanche les "
     "doctrines qui recommandent ces situations : le premier considère "
     "l’échange comme un jeu à somme positive, le second comme une compétition "
     "pour les marchés et la puissance.",
 why=["Une situation mesurable correspond au libre-échange lui-même, non à la "
      "doctrine.",
      "Un accord commercial est un instrument juridique.",
      "Un instrument tarifaire est un moyen de politique commerciale."],
 diss="Rigueur de vocabulaire payante en dissertation : on n’oppose pas une "
      "situation à une doctrine."),

# =============================================================== c23-14
'ch23-qcm-38': f(niv='comprendre', sp='c23-14', b=3544,
 exp="Le droit de douane relève le prix intérieur : la production nationale "
     "augmente, la consommation et les importations diminuent, et l’État "
     "perçoit des recettes. Le surplus des producteurs augmente, celui des "
     "consommateurs diminue davantage. La différence comprend les recettes "
     "douanières, qui ne sont qu’un transfert, mais aussi deux pertes sèches : "
     "une distorsion à la production, car des unités nationales coûteuses "
     "remplacent des importations moins chères, et une distorsion à la "
     "consommation, car certains achats sont abandonnés. Ces deux pertes ne "
     "sont récupérées par personne.",
 why=["Recettes douanières et rente des importateurs sont des transferts, "
      "précisément pas des pertes sèches.",
      "Perte de change et perte d’emploi ne figurent pas dans l’analyse en "
      "surplus.",
      "La baisse du prix mondial ne concerne qu’un grand pays, et la hausse "
      "du prix intérieur est la cause des pertes, non les pertes "
      "elles-mêmes."],
 diss="Méthode à maîtriser : identifier successivement les transferts "
      "(producteurs, État) puis les triangles de perte sèche."),
'ch23-qcm-39': f(niv='raisonner', sp='c23-14', b=3574,
 exp="Un grand pays n’est pas price taker : en réduisant fortement ses "
     "importations, il diminue la demande mondiale adressée aux exportateurs "
     "étrangers et fait donc baisser le prix mondial. Il paie ses "
     "importations moins cher : c’est un gain de termes de l’échange, qui "
     "peut dépasser les deux pertes sèches. Mais ce gain s’obtient aux dépens "
     "des partenaires et appelle des représailles qui l’annulent ; il suppose "
     "en outre un pouvoir de marché suffisant.",
 why=["Les consommateurs paient au contraire plus cher, puisque le prix "
      "intérieur augmente du montant du droit.",
      "Les recettes douanières ne sont qu’un transfert interne, elles ne "
      "créent aucun gain collectif.",
      "Les pertes sèches ne disparaissent pas : elles sont simplement "
      "comparées au gain de termes de l’échange."],
 diss="Condition à toujours mentionner : le raisonnement suppose que les "
      "partenaires ne réagissent pas."),
'ch23-qcm-40': f(niv='comprendre', sp='c23-14', b=3589,
 exp="Le droit de douane fixe un prix et laisse le marché déterminer les "
     "quantités ; le quota fixe le volume importé et laisse le marché "
     "déterminer le prix, ce qui crée une rente. La différence essentielle "
     "tient donc à la destination de cette rente : le Trésor dans le cas du "
     "droit de douane, les détenteurs de licences dans celui du quota, voire "
     "les producteurs étrangers dans certaines restrictions volontaires aux "
     "exportations. À protection équivalente, les effets distributifs "
     "diffèrent.",
 why=["Ce sont les droits de douane, et non les quotas, qui procurent des "
      "recettes à l’État.",
      "Rien n’impose qu’un quota soit temporaire.",
      "Les restrictions quantitatives sont encadrées, non interdites par "
      "principe."],
 diss="Question à se poser systématiquement devant un instrument "
      "protectionniste : qui capte la rente ?"),
'ch23-qcm-54': f(niv='comprendre', sp='c23-14', b=3634,
 exp="L’efficacité est l’atteinte de l’objectif : la mesure a-t-elle "
     "effectivement protégé la production visée ? L’efficience rapporte le "
     "résultat obtenu à son coût. L’exemple du cours est éclairant : si un "
     "droit de douane sauve 1 000 emplois tandis que consommateurs et "
     "entreprises supportent 200 millions d’euros de coûts supplémentaires, "
     "la mesure est efficace mais représente 200 000 euros par emploi "
     "sauvegardé. L’équité porte enfin sur la répartition : qui paie, qui "
     "gagne ?",
 why=["La compatibilité juridique des moyens est une quatrième question, "
      "distincte de l’efficience.",
      "La comparaison des gagnants et des perdants relève de l’équité.",
      "La comparaison du tarif appliqué et du tarif consolidé est une "
      "question technique de politique commerciale."],
 diss="Grille complète à appliquer à toute mesure : efficacité, efficience, "
      "équité, et compatibilité des moyens avec les engagements "
      "internationaux."),
'ch23-questi-88': f(niv='appliquer', sp='c23-14', b=3546),
'ch23-questi-89': f(niv='raisonner', sp='c23-14', b=3576),
'ch23-questi-90': f(niv='appliquer', sp='c23-14', b=3651),
'ch23-questi-91': f(niv='raisonner', sp='c23-14', b=3667),

}
