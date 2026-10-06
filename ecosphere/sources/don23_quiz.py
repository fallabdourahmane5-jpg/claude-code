# -*- coding: utf-8 -*-
"""Quiz du chapitre 3 de deuxieme annee : connaissances et raisonnement.

Chaque entree : (type, question, options, index de la bonne reponse,
explication, tags thematiques).
"""

Q = []
def q(t, question, opts, ans, exp, tags):
    Q.append((t, question, opts, ans, exp, tags))

# ---------------------------------------------------------------- QCM
q('qcm', "L’analyse positive du commerce international consiste à :",
  ["Évaluer si l’ouverture est souhaitable",
   "Expliquer pourquoi les pays échangent et ce qu’ils échangent",
   "Mesurer les inégalités mondiales",
   "Défendre le libre-échange"], 1,
  "Bonne réponse : B. L’analyse positive explique ce qui est ; c’est l’analyse normative qui évalue les conséquences et se prononce sur le caractère souhaitable de l’ouverture.",
  ['méthode', 'commerce international'])
q('qcm', "Chez Smith, un pays sans aucun avantage absolu :",
  ["Se spécialise là où son coût d’opportunité est le plus faible",
   "Reste en principe exclu de l’échange",
   "Exporte ses facteurs de production",
   "Gagne automatiquement au commerce"], 1,
  "Bonne réponse : B. C’est précisément la limite que Ricardo lève : chez Smith la spécialisation suppose un avantage absolu, chez Ricardo elle repose sur l’avantage comparatif.",
  ['smith', 'avantage absolu', 'libre-échange'])
q('qcm', "Les trois gains de la spécialisation chez Smith sont :",
  ["Variété, concurrence, dimension",
   "Dextérité accrue, réduction des pertes de temps, incitation à innover",
   "Recettes fiscales, emploi, balance commerciale",
   "Économies d’échelle internes, externes et d’agglomération"], 1,
  "Bonne réponse : B. Ce sont les trois effets de la division du travail transposés à l’échelle internationale. La réponse A énonce les trois gains de Krugman.",
  ['smith', 'division du travail', 'gains à l’échange'])
q('qcm', "Dans l’exemple ricardien (drap 90/100, vin 80/120 en hommes-années) :",
  ["Le Portugal a un avantage absolu dans le vin seulement",
   "L’Angleterre a un avantage absolu dans le drap",
   "Le Portugal a un avantage absolu dans les deux productions",
   "Les deux pays sont également productifs"], 2,
  "Bonne réponse : C. Le Portugal utilise moins de travail dans les deux cas ; c’est ce qui rend l’exemple démonstratif, puisque l’échange reste avantageux malgré ce double avantage absolu.",
  ['ricardo', 'avantage absolu', 'avantage comparatif'])
q('qcm', "Le coût d’opportunité du drap au Portugal, dans l’exemple de Ricardo, vaut :",
  ["0,83 vin", "1,125 vin", "0,88 drap", "1,2 drap"], 1,
  "Bonne réponse : B. 90/80 = 1,125 : produire une unité de drap coûte au Portugal 1,125 unité de vin, contre 0,83 en Angleterre (100/120), d’où l’avantage comparatif anglais dans le drap.",
  ['ricardo', 'coût d’opportunité', 'avantage comparatif'])
q('qcm', "Les deux gains que Ricardo tire de la spécialisation sont :",
  ["Une hausse de la production mondiale et une économie de facteurs",
   "Une baisse des prix et une hausse des salaires",
   "Un excédent commercial et des recettes douanières",
   "Une variété accrue et une concurrence renforcée"], 0,
  "Bonne réponse : A. À facteurs inchangés la production mondiale augmente ; à production inchangée, le même volume est obtenu avec moins de travail — soit 30 unités économisées dans l’exemple du cours.",
  ['ricardo', 'gains à l’échange', 'spécialisation'])
q('qcm', "L’apport propre de John Stuart Mill à la théorie ricardienne est :",
  ["De démontrer l’existence du gain à l’échange",
   "De déterminer les bornes entre lesquelles le prix international doit se situer",
   "D’introduire les dotations factorielles",
   "De montrer que les facteurs sont mobiles"], 1,
  "Bonne réponse : B. Ricardo établit l’existence du gain, Mill en analyse le partage : hors des bornes (0,88 < Pv/d < 1,2 dans l’exemple), un pays préfère l’autarcie.",
  ['mill', 'termes de l’échange', 'gains à l’échange'])
q('qcm', "Selon Marx, les économies capitalistes cherchent des débouchés extérieurs parce que :",
  ["Leurs consommateurs demandent de la variété",
   "La compression des salaires rend la demande intérieure insuffisante",
   "Leurs dotations factorielles sont rares",
   "Leur monnaie est sous-évaluée"], 1,
  "Bonne réponse : B. L’armée industrielle de réserve maintient les salaires bas ; la demande intérieure est alors trop faible pour absorber la production, ce qui impose l’exportation.",
  ['marx', 'débouchés', 'libre-échange'])
q('qcm', "Parmi les cinq caractéristiques de l’impérialisme chez Lénine ne figure pas :",
  ["La fusion du capital bancaire et du capital industriel",
   "L’importance des exportations de capitaux",
   "La mobilité internationale parfaite du travail",
   "Le partage des territoires entre grandes puissances"], 2,
  "Bonne réponse : C. Lénine retient la concentration et les monopoles, la fusion banque-industrie, les exportations de capitaux, le partage des marchés et celui des territoires.",
  ['lénine', 'impérialisme'])
q('qcm', "La thèse de Prebisch (1950) porte sur :",
  ["L’échange inégal par les salaires",
   "La dégradation tendancielle des termes de l’échange des produits primaires",
   "La croissance appauvrissante",
   "La désindustrialisation précoce"], 1,
  "Bonne réponse : B. Sur 1875-1938, les prix des produits primaires progressent moins vite que ceux des manufacturés : il faut exporter plus pour importer autant.",
  ['prebisch', 'termes de l’échange', 'développement'])
q('qcm', "Chez Arghiri Emmanuel, l’inégalité de l’échange provient :",
  ["Des écarts de productivité", "Des écarts de salaires",
   "Des droits de douane", "Des coûts de transport"], 1,
  "Bonne réponse : B. À productivité comparable, des salaires très bas se répercutent dans des prix d’exportation très bas : l’échange transfère de la valeur sans qu’aucune contrainte formelle soit exercée.",
  ['arghiri emmanuel', 'échange inégal', 'développement'])
q('qcm', "La croissance appauvrissante de Bhagwati (1958) suppose notamment :",
  ["Un pays petit sur le marché mondial",
   "Un pays dont l’offre supplémentaire fait baisser le prix mondial",
   "Une dotation abondante en capital",
   "Un protectionnisme éducateur"], 1,
  "Bonne réponse : B. Il faut que le pays pèse assez sur le marché du produit pour que sa production supplémentaire dégrade le prix, et que cette perte de termes de l’échange dépasse le gain de volume.",
  ['bhagwati', 'croissance appauvrissante', 'termes de l’échange'])
q('qcm', "Une limite majeure des analyses néo-marxistes du commerce est :",
  ["Qu’elles ignorent les salaires",
   "Qu’elles décrivent le contexte de la grande divergence, alors que l’hypermondialisation réduit les écarts entre pays",
   "Qu’elles supposent la concurrence imparfaite",
   "Qu’elles raisonnent en coût d’opportunité"], 1,
  "Bonne réponse : B. Ces analyses sont formulées lorsque l’écart Nord-Sud se creuse ; l’hypermondialisation s’accompagne au contraire d’un rattrapage de nombreux pays émergents.",
  ['développement', 'hypermondialisation', 'échange inégal'])
q('qcm', "Dans le modèle HOS, l’avantage comparatif provient :",
  ["De l’écart de productivité du travail",
   "De l’abondance relative des facteurs",
   "Des rendements d’échelle croissants",
   "De la demande de différence"], 1,
  "Bonne réponse : B. Les technologies et les préférences sont supposées identiques : seules les dotations diffèrent, et c’est leur rapport, non leur niveau absolu, qui compte.",
  ['modèle hos', 'dotations factorielles', 'heckscher-ohlin'])
q('qcm', "Les hypothèses « 2 × 2 × 2 » du modèle HOS désignent :",
  ["Deux pays, deux biens, deux facteurs",
   "Deux périodes, deux prix, deux firmes",
   "Deux théorèmes et deux auteurs",
   "Deux types de protection et deux effets"], 0,
  "Bonne réponse : A. S’y ajoutent l’immobilité internationale des facteurs, leur mobilité intersectorielle, des technologies et préférences identiques et la concurrence parfaite.",
  ['modèle hos', 'hypothèses'])
q('qcm', "Le théorème Stolper-Samuelson établit que l’ouverture :",
  ["Augmente uniformément tous les revenus",
   "Augmente la rémunération du facteur relativement abondant et réduit celle du facteur relativement rare",
   "Égalise les productivités",
   "Réduit la concurrence"], 1,
  "Bonne réponse : B. Le commerce redistribue donc à l’intérieur de chaque pays : les perdants se repèrent au facteur qu’ils détiennent.",
  ['stolper-samuelson', 'inégalités', 'modèle hos'])
q('qcm', "Dans un pays en développement abondant en travail peu qualifié, le théorème Stolper-Samuelson prévoit que l’ouverture :",
  ["Réduit le salaire des moins qualifiés",
   "Augmente le salaire des moins qualifiés",
   "N’a aucun effet sur les salaires",
   "Augmente la rente du capital uniquement"], 1,
  "Bonne réponse : B. Le facteur relativement abondant voit sa rémunération progresser : la même mécanique produit donc des effets de sens opposé selon la dotation du pays.",
  ['stolper-samuelson', 'inégalités', 'développement'])
q('qcm', "Le théorème de Rybczynski (1955) implique que :",
  ["Les dotations sont données une fois pour toutes",
   "L’accroissement d’un facteur augmente plus que proportionnellement la production du bien qui l’utilise intensivement",
   "Les prix des facteurs s’égalisent",
   "Les économies d’échelle sont internes"], 1,
  "Bonne réponse : B. Les avantages comparatifs deviennent donc construits : l’investissement, l’éducation et la R&D modifient la spécialisation.",
  ['rybczynski', 'avantage construit', 'dotations factorielles'])
q('qcm', "Le paradoxe de Leontief (1953) consiste en ce que :",
  ["Les États-Unis exportent des biens plus intensifs en capital que prévu",
   "Les exportations américaines apparaissent moins intensives en capital que les biens substituables aux importations",
   "Les salaires américains sont trop bas",
   "Les droits de douane américains sont trop élevés"], 1,
  "Bonne réponse : B. Résultat contre-intuitif pour le pays le plus abondant en capital ; il conduit à réviser la définition des facteurs plutôt qu’à rejeter le raisonnement.",
  ['leontief', 'paradoxe de leontief', 'modèle hos'])
q('qcm', "La résolution apportée par Baldwin en 1971 est que les exportations américaines sont intensives :",
  ["En terres agricoles", "En travail qualifié et en savoir technologique",
   "En capital financier", "En énergie"], 1,
  "Bonne réponse : B. Le paradoxe disparaît dès que le travail cesse d’être traité comme homogène : la dotation décisive est la qualification.",
  ['robert baldwin', 'paradoxe de leontief', 'capital humain'])
q('qcm', "Les avantages comparatifs révélés sont nécessaires parce que :",
  ["Les coûts d’opportunité en autarcie ne sont pas observables",
   "Les droits de douane faussent les prix",
   "Les dotations sont inconnues",
   "Les firmes ne publient pas leurs coûts"], 0,
  "Bonne réponse : A. Le contrefactuel d’autarcie n’existe pas : on identifie donc les spécialisations a posteriori, à partir de la structure observée des flux.",
  ['avantages comparatifs révélés', 'mesure', 'cepii'])
q('qcm', "La « désindustrialisation précoce » décrite par Rodrik signifie que :",
  ["Les pays avancés se désindustrialisent trop vite",
   "Des pays en développement voient l’industrie reculer à un niveau de revenu très inférieur à celui des pays avancés en leur temps",
   "L’industrie disparaît au profit de l’agriculture",
   "Les services ne créent pas d’emplois"], 1,
  "Bonne réponse : B. Ces pays sont alors privés du principal moteur historique de rattrapage, sans avoir atteint le niveau de revenu correspondant.",
  ['rodrik', 'désindustrialisation précoce', 'développement'])
q('qcm', "Le commerce intra-branche constitue une limite décisive aux théories traditionnelles parce que :",
  ["Il concerne surtout les produits primaires",
   "Il voit des pays comparables échanger des produits de la même branche dans les deux sens",
   "Il suppose des coûts de transport nuls",
   "Il ne concerne que les services"], 1,
  "Bonne réponse : B. Ni les écarts de productivité ni les différences de dotations ne peuvent expliquer que la France exporte et importe simultanément des automobiles.",
  ['commerce intra-branche', 'limites', 'différenciation'])
q('qcm', "L’apport de Keesing (1966) consiste à :",
  ["Introduire les économies d’échelle",
   "Faire de la qualification du travail une dotation factorielle",
   "Mesurer les termes de l’échange",
   "Formaliser le protectionnisme éducateur"], 1,
  "Bonne réponse : B. C’est le cœur de l’approche néo-factorielle : le modèle HOS est conservé, sa liste de facteurs est enrichie.",
  ['keesing', 'approches néo-factorielles', 'capital humain'])
q('qcm', "Chez Posner (1961), l’avantage lié à l’innovation est :",
  ["Définitif", "Temporaire, parce que l’imitation réduit l’écart",
   "Indépendant de la technologie", "Lié aux dotations en capital"], 1,
  "Bonne réponse : B. L’avantage dépend donc du flux d’innovations et non d’un stock : c’est la capacité à innover continuellement qui maintient la spécialisation.",
  ['posner', 'approches néo-technologiques', 'innovation'])
q('qcm', "Dans le cycle de vie du produit de Vernon (1966), à la phase de maturité :",
  ["Le pays innovateur exporte massivement",
   "La production se standardise et se délocalise vers des pays à coûts plus faibles",
   "La demande disparaît",
   "Les coûts fixes augmentent"], 1,
  "Bonne réponse : B. Le procédé étant banalisé, le coût devient le critère déterminant : le pays innovateur finit par importer le produit qu’il a créé.",
  ['vernon', 'cycle de vie du produit', 'délocalisation'])
q('qcm', "L’exemple des téléviseurs à écran plat illustre :",
  ["Le théorème H-O", "Le cycle international du produit",
   "La croissance appauvrissante", "Le paradoxe de Bairoch"], 1,
  "Bonne réponse : B. Innovation japonaise, puis production coréenne, puis chinoise et vietnamienne : le déplacement suit la banalisation du procédé.",
  ['vernon', 'cycle de vie du produit', 'asie'])
q('qcm', "La « demande de différence » de Lassudrie-Duchêne explique :",
  ["Le commerce inter-branche",
   "Le commerce intra-branche entre pays semblables",
   "La dégradation des termes de l’échange",
   "Les pics tarifaires"], 1,
  "Bonne réponse : B. Les consommateurs recherchent, dans la même branche, des produits différents de l’offre nationale : l’explication vient de la demande, non de l’offre.",
  ['lassudrie-duchêne', 'demande de différence', 'commerce intra-branche'])
q('qcm', "La différenciation verticale se définit par :",
  ["Des caractéristiques distinctes à qualité comparable",
   "Une hiérarchie de qualité et de gamme à l’intérieur d’une branche",
   "Une différence de pays d’origine",
   "Une différence de circuit de distribution"], 1,
  "Bonne réponse : B. Elle permet à des pays de niveaux de développement différents d’échanger dans la même branche, à des prix différents.",
  ['différenciation', 'commerce intra-branche', 'chamberlin'])
q('qcm', "Chez Linder, un avantage comparatif apparaît d’abord :",
  ["Grâce à une dotation en capital",
   "Grâce à une forte demande intérieure",
   "Grâce à une subvention publique",
   "Grâce à une monnaie sous-évaluée"], 1,
  "Bonne réponse : B. C’est en répondant à son marché domestique qu’une industrie acquiert l’échelle et l’expérience nécessaires à l’exportation ; les pays échangent donc d’autant plus qu’ils se ressemblent.",
  ['linder', 'demande représentative', 'commerce intra-branche'])
q('qcm', "Les trois gains de l’ouverture chez Krugman sont :",
  ["Dextérité, temps, innovation",
   "Sélection par la concurrence, variété, effet de dimension",
   "Recettes, emploi, change",
   "Production mondiale, économie de facteurs, pouvoir d’achat"], 1,
  "Bonne réponse : B. Ces gains existent même entre pays strictement identiques, puisqu’ils ne reposent pas sur des différences mais sur la taille du marché.",
  ['krugman', 'gains à l’échange', 'économies d’échelle'])
q('qcm', "Une économie d’échelle externe se définit comme une baisse du coût unitaire liée :",
  ["À la taille de l’entreprise",
   "À la taille du secteur ou du territoire",
   "À la baisse des salaires",
   "À la hausse des droits de douane"], 1,
  "Bonne réponse : B. La firme bénéficie de la présence des autres : c’est le fondement des districts industriels et des effets d’agglomération.",
  ['économies d’échelle', 'marshall', 'agglomération'])
q('qcm', "Les trois externalités marshalliennes sont :",
  ["Transport, énergie, fiscalité",
   "Fournisseurs spécialisés, bassin de main-d’œuvre qualifiée, circulation des connaissances",
   "Capital, travail, terre",
   "Variété, prix, qualité"], 1,
  "Bonne réponse : B. Elles expliquent que la productivité d’une firme dépende du lieu où elle est implantée, indépendamment de ses propres caractéristiques.",
  ['marshall', 'district industriel', 'agglomération'])
q('qcm', "L’exemple de Bangalore illustre :",
  ["Le protectionnisme éducateur",
   "Un effet d’agglomération amorcé par une implantation initiale",
   "La croissance appauvrissante",
   "Le dumping monétaire"], 1,
  "Bonne réponse : B. Une première implantation attire main-d’œuvre, fournisseurs et concurrents, qui renforcent à leur tour l’attractivité du lieu : l’avantage est acquis, non hérité.",
  ['agglomération', 'krugman', 'inde'])
q('qcm', "Dans l’exemple Chine-Vietnam de Krugman, le Vietnam peut rester hors du marché parce que :",
  ["Ses coûts potentiels sont plus élevés",
   "Il ne peut atteindre le seuil de production Q0 à partir duquel les économies d’échelle jouent",
   "Il n’a pas de dotation en travail",
   "Ses droits de douane sont trop faibles"], 1,
  "Bonne réponse : B. Un producteur potentiellement plus efficace est exclu par l’antériorité du concurrent : c’est ce qui réhabilite partiellement le protectionnisme éducateur.",
  ['krugman', 'seuil critique', 'protectionnisme éducateur'])
q('qcm', "Le libre-échangisme se distingue du libre-échange en ce qu’il est :",
  ["Une situation mesurable", "Une doctrine normative",
   "Un accord commercial", "Un instrument tarifaire"], 1,
  "Bonne réponse : B. Le libre-échange et le protectionnisme sont des faits ; le libre-échangisme et le mercantilisme sont les doctrines qui les recommandent.",
  ['libre-échange', 'protectionnisme', 'méthode'])
q('qcm', "Dans la logique mercantiliste, le commerce est perçu comme :",
  ["Un jeu à somme positive", "Un jeu de puissance proche d’une somme nulle",
   "Un mécanisme de convergence", "Un échange de variétés"], 1,
  "Bonne réponse : B. La richesse étant identifiée à l’accumulation monétaire, le gain d’un pays correspond à la perte d’un autre — ce que Smith conteste explicitement.",
  ['mercantilisme', 'doctrines'])
q('qcm', "Les deux pertes sèches d’un droit de douane dans un petit pays sont :",
  ["Les recettes douanières et la rente des importateurs",
   "Une distorsion à la production et une distorsion à la consommation",
   "La perte de change et la perte d’emploi",
   "La baisse du prix mondial et la hausse du prix intérieur"], 1,
  "Bonne réponse : B. Des unités nationales coûteuses remplacent des importations moins chères, et des achats sont renoncés : ces deux pertes ne sont récupérées par personne.",
  ['droit de douane', 'perte sèche', 'analyse en surplus'])
q('qcm', "Un grand pays peut théoriquement gagner à un droit de douane parce que :",
  ["Ses consommateurs paient moins cher",
   "La baisse de sa demande fait reculer le prix mondial : gain de termes de l’échange",
   "Ses recettes douanières sont plus élevées",
   "Ses pertes sèches disparaissent"], 1,
  "Bonne réponse : B. Le gain de termes de l’échange peut dépasser les deux pertes sèches, mais il s’obtient aux dépens des partenaires et appelle des représailles.",
  ['droit de douane', 'termes de l’échange', 'grand pays'])
q('qcm', "Le quota diffère du droit de douane en ce qu’il :",
  ["Procure des recettes à l’État",
   "Fixe le volume et laisse le marché déterminer le prix, créant une rente",
   "Est toujours temporaire",
   "Est interdit par l’OMC"], 1,
  "Bonne réponse : B. La rente va aux détenteurs de licences plutôt qu’au Trésor : à protection équivalente, les effets distributifs diffèrent.",
  ['quota', 'protectionnisme non tarifaire', 'instruments'])
q('qcm', "La clause de la nation la plus favorisée impose que :",
  ["Les pays en développement bénéficient de tarifs réduits",
   "Toute concession accordée à un membre soit étendue à tous les autres",
   "Les droits de douane soient nuls",
   "Les subventions soient interdites"], 1,
  "Bonne réponse : B. Elle généralise les baisses de droits et rend l’adhésion au système d’autant plus attractive qu’il s’élargit ; les tarifs préférentiels en sont une dérogation.",
  ['gatt', 'omc', 'nation la plus favorisée'])
q('qcm', "Le tarif Hawley-Smoot (1930) est l’exemple canonique :",
  ["Du protectionnisme éducateur",
   "D’une guerre commerciale aggravant une crise",
   "D’une politique commerciale stratégique",
   "D’un ajustement carbone aux frontières"], 1,
  "Bonne réponse : B. Portant les droits américains à environ 50 %, il déclenche des représailles généralisées et l’effondrement du commerce mondial.",
  ['hawley-smoot', 'guerre commerciale', 'entre-deux-guerres'])
q('qcm', "Le paradoxe de Bairoch établit que, au XIXe siècle :",
  ["Les pays les plus ouverts croissent le plus vite",
   "Les pays les plus protégés connaissent une croissance plus rapide",
   "Le protectionnisme a disparu",
   "Les droits de douane étaient uniformes"], 1,
  "Bonne réponse : B. Il faut toutefois le lire comme une réfutation de l’automatisme libre-échangiste, et non comme une démonstration de l’efficacité du protectionnisme.",
  ['bairoch', 'histoire', 'protectionnisme'])
q('qcm', "Les trois conditions de réussite du protectionnisme éducateur sont :",
  ["Un tarif élevé, un quota et une subvention",
   "Un marché intérieur suffisant, le maintien d’une concurrence interne, un caractère strictement temporaire",
   "Un excédent courant, une monnaie forte, une banque centrale indépendante",
   "Une dotation en capital, une main-d’œuvre qualifiée, des infrastructures"], 1,
  "Bonne réponse : B. L’absence de l’une des trois transforme la protection en rente durable : sans concurrence interne, l’incitation à progresser disparaît.",
  ['list', 'protectionnisme éducateur', 'conditions'])
q('qcm', "Chez Brander et Spencer (1983), une subvention peut être efficace parce qu’elle :",
  ["Réduit le prix payé par les consommateurs",
   "Modifie les gains anticipés et peut dissuader le concurrent étranger d’entrer",
   "Augmente les recettes publiques",
   "Égalise le prix des facteurs"], 1,
  "Bonne réponse : B. Dans un marché trop étroit pour deux producteurs, elle transfère la rente du concurrent vers l’économie nationale — à condition que l’État anticipe correctement le jeu.",
  ['brander et spencer', 'politique commerciale stratégique', 'airbus-boeing'])
q('qcm', "L’argument de Kaldor (1966) sur les industries vieillissantes exige :",
  ["Un tarif permanent",
   "Un objectif explicite : étaler la disparition de l’activité ou financer une montée en gamme",
   "Un quota",
   "Une dévaluation"], 1,
  "Bonne réponse : B. Sans objectif daté, la protection se borne à entretenir des « canards boiteux » : c’est l’objectif, non l’instrument, qui la légitime.",
  ['kaldor', 'industries vieillissantes', 'politique industrielle'])
q('qcm', "Le « tariff jumping » désigne :",
  ["Le relèvement successif des droits de douane",
   "Le contournement d’un droit de douane par l’investissement direct dans le pays protégé",
   "La hausse des pics tarifaires",
   "Le passage d’un quota à un tarif"], 1,
  "Bonne réponse : B. La firme produit à l’intérieur du marché protégé plutôt que d’exporter vers lui : l’effet de la protection sur ses ventes est annulé.",
  ['tariff jumping', 'contournement', 'ide'])
q('qcm', "La courbe environnementale de Kuznets de Grossman et Krueger (1995) décrit :",
  ["Une relation croissante entre revenu et pollution",
   "Une relation en cloche entre revenu par habitant et pollution",
   "Une relation décroissante dès le début",
   "L’absence de lien entre revenu et pollution"], 1,
  "Bonne réponse : B. La pollution augmente d’abord avec l’industrialisation, puis diminue au-delà d’un seuil — par recomposition sectorielle, innovation et exigence sociale, donc grâce à des institutions.",
  ['grossman et krueger', 'environnement', 'courbe de kuznets'])
q('qcm', "Les trois effets environnementaux de l’ouverture distingués par le cours sont :",
  ["Distance, échelle, composition",
   "Production, consommation, redistribution",
   "Variété, prix, qualité",
   "Tarif, quota, norme"], 0,
  "Bonne réponse : A. L’effet de distance accroît les émissions du transport, l’effet d’échelle le volume produit, l’effet de composition modifie la structure sectorielle et peut jouer dans les deux sens.",
  ['environnement', 'mondialisation', 'émissions'])
q('qcm', "Le mécanisme d’ajustement carbone aux frontières vise à :",
  ["Protéger l’emploi industriel européen en général",
   "Rétablir l’équivalence du prix du carbone entre producteurs européens et importations",
   "Interdire les importations polluantes",
   "Financer la transition des pays en développement"], 1,
  "Bonne réponse : B. Son objectif déclaré est de limiter les fuites de carbone en alignant le coût du carbone incorporé aux importations sur celui du marché carbone européen.",
  ['macf', 'environnement', 'union européenne'])
q('qcm', "La courbe de l’éléphant de Milanović montre que, entre 1988 et 2008, la croissance des revenus réels a été la plus faible pour :",
  ["Le centile le plus riche",
   "Les classes moyennes des pays émergents",
   "Les classes populaires et moyennes des pays avancés",
   "Les plus pauvres de la planète"], 2,
  "Bonne réponse : C. C’est précisément ce creux qui donne à la mondialisation son coût politique dans les démocraties avancées.",
  ['milanovic', 'courbe de l’éléphant', 'inégalités'])
q('qcm', "Dans l’analyse de Guimbard, Vicard et Wibaux, le tournant protectionniste américain entraîne surtout :",
  ["La disparition du commerce international",
   "Une recomposition géographique des échanges",
   "Une baisse uniforme des échanges mondiaux",
   "La fin des accords régionaux"], 1,
  "Bonne réponse : B. Les volumes résistent : les flux se réorientent vers d’autres partenaires, et certains pays tiers en bénéficient.",
  ['guimbard', 'fragmentation géo-économique', 'cepii'])
q('qcm', "L’IRA et le CHIPS Act (2022) posent un problème au regard des règles multilatérales parce qu’ils :",
  ["Augmentent les droits de douane",
   "Subordonnent des aides à l’utilisation ou à la production de biens nationaux",
   "Interdisent les importations",
   "Instaurent des quotas"], 1,
  "Bonne réponse : B. Le traitement national (article III du GATT) et la prohibition des subventions liées au contenu local sont directement en cause.",
  ['ira', 'chips act', 'politique industrielle'])
q('qcm', "L’efficience d’une politique commerciale consiste à comparer :",
  ["L’objectif et les moyens juridiques",
   "Le résultat obtenu et son coût",
   "Les gagnants et les perdants",
   "Le tarif appliqué et le tarif consolidé"], 1,
  "Bonne réponse : B. L’efficacité est l’atteinte de l’objectif, l’efficience le rapport entre le résultat et son coût, l’équité la répartition : l’exemple du coût par emploi sauvé illustre la distinction.",
  ['efficacité', 'efficience', 'évaluation'])

# ---------------------------------------------------------------- vrai / faux
q('vrai/faux', "Chez Ricardo, un pays absolument moins productif dans toutes les productions est exclu de l’échange.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est précisément la démonstration de Ricardo : ce qui compte est le coût d’opportunité, de sorte qu’un pays désavantagé partout conserve un avantage comparatif.",
  ['ricardo', 'avantage comparatif'])
q('vrai/faux', "Pour Smith, les importations sont une perte qu’il convient de limiter.",
  ["Vrai", "Faux"], 1,
  "Faux. Smith soutient l’inverse : les importations sont la finalité de l’échange, les exportations n’étant que le moyen de les financer. L’idée que l’importation appauvrit est mercantiliste.",
  ['smith', 'mercantilisme', 'importations'])
q('vrai/faux', "Le modèle de Ricardo suppose la mobilité internationale des facteurs de production.",
  ["Vrai", "Faux"], 1,
  "Faux. Il suppose au contraire leur immobilité internationale et leur mobilité à l’intérieur du pays — hypothèse que la réalité des reconversions dément largement.",
  ['ricardo', 'hypothèses', 'mobilité'])
q('vrai/faux', "Le théorème H-O suppose des technologies identiques dans les deux pays.",
  ["Vrai", "Faux"], 0,
  "Vrai. C’est ce qui en fait l’originalité par rapport à Ricardo : à technologies identiques, les seules différences de dotations suffisent à engendrer l’échange.",
  ['modèle hos', 'hypothèses', 'heckscher-ohlin'])
q('vrai/faux', "Le théorème Stolper-Samuelson implique que l’ouverture profite à tous les travailleurs d’un pays.",
  ["Vrai", "Faux"], 1,
  "Faux. Il établit exactement le contraire : la rémunération du facteur relativement rare diminue, ce qui crée des perdants internes identifiables.",
  ['stolper-samuelson', 'inégalités'])
q('vrai/faux', "Le commerce international explique à lui seul la montée des inégalités salariales dans les pays avancés.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours insiste sur la pluralité des causes : commerce international, progrès technique biaisé et institutions du marché du travail interviennent conjointement.",
  ['inégalités', 'progrès technique', 'institutions'])
q('vrai/faux', "Le paradoxe de Leontief invalide définitivement le modèle HOS.",
  ["Vrai", "Faux"], 1,
  "Faux. Il oblige à redéfinir les facteurs : en intégrant la qualification et le savoir technologique, Baldwin montre en 1971 que le raisonnement reste valide.",
  ['leontief', 'robert baldwin', 'modèle hos'])
q('vrai/faux', "Les avantages comparatifs révélés se calculent à partir des coûts d’opportunité en autarcie.",
  ["Vrai", "Faux"], 1,
  "Faux. L’autarcie n’est pas observable : ils se déduisent de la structure observée des exportations comparée à celle du commerce mondial.",
  ['avantages comparatifs révélés', 'mesure'])
q('vrai/faux', "Le commerce intra-branche domine les échanges entre pays de niveau de développement comparable.",
  ["Vrai", "Faux"], 0,
  "Vrai. France et Allemagne échangent massivement des produits de la même branche, ce que ni Ricardo ni HOS ne peuvent expliquer.",
  ['commerce intra-branche', 'différenciation'])
q('vrai/faux', "Chez Krugman, les gains de l’ouverture supposent que les pays diffèrent.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est l’apport décisif : les trois gains — concurrence, variété, dimension — existent même entre pays strictement identiques, puisqu’ils reposent sur la taille du marché.",
  ['krugman', 'économies d’échelle', 'gains à l’échange'])
q('vrai/faux', "Les économies d’échelle externes bénéficient à l’entreprise en raison de sa propre taille.",
  ["Vrai", "Faux"], 1,
  "Faux. Elles proviennent de la taille du secteur ou du territoire : la firme bénéficie de la présence des autres, d’où les districts industriels.",
  ['économies d’échelle', 'marshall'])
q('vrai/faux', "Un droit de douane procure toujours un gain net au pays qui l’applique.",
  ["Vrai", "Faux"], 1,
  "Faux. Dans un petit pays, les deux pertes sèches sont certaines. Seul un grand pays peut théoriquement gagner, si le gain de termes de l’échange les dépasse — et au prix de représailles probables.",
  ['droit de douane', 'perte sèche', 'grand pays'])
q('vrai/faux', "La baisse du droit de douane moyen mondial, d’environ 40 % en 1947 à 4 % en 2019, signifie que le protectionnisme a disparu.",
  ["Vrai", "Faux"], 1,
  "Faux. Les pics tarifaires sectoriels et les mesures non tarifaires — normes, contenu local, subventions, marchés publics — maintiennent des protections élevées que le tarif moyen masque.",
  ['droits de douane', 'protectionnisme non tarifaire', 'pics tarifaires'])
q('vrai/faux', "Le protectionnisme éducateur de List est conçu comme une politique permanente.",
  ["Vrai", "Faux"], 1,
  "Faux. Son caractère temporaire fait partie du dispositif : la protection ne se justifie qu’à la phase de démarrage industriel, et sa levée est prévue.",
  ['list', 'protectionnisme éducateur'])
q('vrai/faux', "L’argument keynésien en faveur du protectionnisme suppose des capacités de production inemployées.",
  ["Vrai", "Faux"], 0,
  "Vrai. Sans capacités disponibles, la demande détournée des importations se traduit en inflation plutôt qu’en production ; l’argument est donc conditionnel, et vulnérable aux représailles.",
  ['keynes', 'multiplicateur', 'protectionnisme'])
q('vrai/faux', "Pareto montre que le protectionnisme est politiquement fragile parce que ses coûts sont visibles.",
  ["Vrai", "Faux"], 1,
  "Faux. L’analyse est inverse : les gains sont concentrés sur des producteurs organisés, les pertes diffuses sur des consommateurs dispersés — d’où sa viabilité politique malgré son coût collectif.",
  ['pareto', 'groupes de pression', 'économie politique'])
q('vrai/faux', "Le dilemme du prisonnier appliqué au commerce montre que l’ouverture mutuelle n’est pas spontanément stable.",
  ["Vrai", "Faux"], 0,
  "Vrai. Chaque État craignant la protection de l’autre, tous se protègent par prudence : d’où la nécessité d’institutions — GATT, OMC — ou d’un leader hégémonique.",
  ['dilemme du prisonnier', 'gatt', 'coopération'])
q('vrai/faux', "Les mesures protectionnistes américaines de 2018 ont porté le droit moyen appliqué aux importations chinoises de 3,1 % à plus de 20 %.",
  ["Vrai", "Faux"], 0,
  "Vrai. Le cours retrace la montée par vagues — 3,1 %, 12,4 %, 18,4 %, 21,5 % — et montre que l’accord dit de « phase one » de janvier 2020 ne règle pas le conflit structurel.",
  ['trump', 'guerre commerciale', 'chine'])
q('vrai/faux', "Une guerre commerciale peut faire des gagnants parmi les pays tiers.",
  ["Vrai", "Faux"], 0,
  "Vrai. Le détournement des flux profite à des pays non visés — le Vietnam en est l’exemple le plus commenté — et peut même accélérer la montée en gamme du pays visé.",
  ['détournement des flux', 'vietnam', 'guerre commerciale'])
q('vrai/faux', "Pour Vuillemey, le protectionnisme contemporain peut se justifier par la défense de normes sociales et environnementales.",
  ["Vrai", "Faux"], 0,
  "Vrai. Dans Le temps de la démondialisation (2022), il soutient que l’ouverture conduit les États à renoncer à des exigences qu’ils auraient autrement adoptées : la protection défendrait alors une capacité d’action collective.",
  ['vuillemey', 'protectionnisme social', 'environnement'])

# ---------------------------------------------------------------- questions ouvertes
q('question ouverte', "Pourquoi l’avantage comparatif est-il une notion plus générale que l’avantage absolu ?",
  [], 0,
  "L’avantage absolu compare les productivités entre pays : un pays moins productif partout n’a rien à proposer. L’avantage comparatif compare les coûts d’opportunité à l’intérieur de chaque pays : chacun renonce à moins de choses dans une production donnée, et dispose donc toujours d’un avantage relatif. L’échange redevient possible pour tous, ce que Ricardo démontre avec le Portugal — plus productif dans le drap comme dans le vin — et l’Angleterre.",
  ['ricardo', 'smith', 'avantage comparatif'])
q('question ouverte', "Quels sont les deux gains que Ricardo tire de la spécialisation, et comment se mesurent-ils ?",
  [], 0,
  "Premier gain : à facteurs donnés, la production mondiale augmente — dans l’exemple du cours, de 4 à 4,325 unités. Second gain : à production mondiale inchangée, le même volume s’obtient avec moins de travail — une économie de 30 unités. Ce sont deux façons de lire le même effet : la réallocation des facteurs vers les emplois où leur coût d’opportunité est le plus faible accroît l’efficacité productive globale.",
  ['ricardo', 'gains à l’échange', 'spécialisation'])
q('question ouverte', "Expliquez l’apport de J. S. Mill par rapport à Ricardo.",
  [], 0,
  "Ricardo établit que l’échange est mutuellement avantageux mais laisse indéterminé le prix international, donc le partage du gain. Mill montre que ce prix doit rester entre les rapports d’échange internes des deux pays : dans l’exemple ricardien, entre 0,88 et 1,2 pour le vin contre drap. Hors de cet intervalle, un pays préfère l’autarcie. Plus le prix est proche de la borne favorable à un pays, plus son gain est élevé : le même échange peut donc avantager beaucoup plus l’un que l’autre.",
  ['mill', 'termes de l’échange', 'répartition des gains'])
q('question ouverte', "Comment Marx renverse-t-il la lecture classique du libre-échange ?",
  [], 0,
  "La concurrence entre capitalistes impose l’accumulation ; la plus-value venant du travail, la hausse de la composition du capital déprime tendanciellement le taux de profit, et l’armée industrielle de réserve maintient les salaires bas. La demande intérieure devient insuffisante pour absorber la production : l’exportation n’est plus un bienfait réciproque mais la résolution provisoire d’une contradiction interne. Le cours note la résonance contemporaine de ce schéma avec les capacités de production chinoises.",
  ['marx', 'débouchés', 'chine'])
q('question ouverte', "Pourquoi les analyses de Prebisch, Emmanuel et Bhagwati conduisent-elles à relativiser le gain à l’échange, et quelles en sont les limites ?",
  [], 0,
  "Prebisch montre que la dégradation des termes de l’échange pénalise les spécialisations primaires ; Emmanuel que les écarts de salaires rendent l’échange inégal ; Bhagwati qu’une croissance peut appauvrir lorsque l’offre supplémentaire dégrade le prix mondial. Ces analyses établissent qu’une spécialisation conforme aux avantages comparatifs peut être défavorable. Leur limite est contextuelle : elles sont formulées pendant la grande divergence, alors que l’hypermondialisation s’accompagne d’un rattrapage de nombreux émergents.",
  ['prebisch', 'arghiri emmanuel', 'bhagwati'])
q('question ouverte', "Énoncez le théorème Heckscher-Ohlin et son mécanisme complet.",
  [], 0,
  "Un pays possède un avantage comparatif dans la production qui utilise intensivement le facteur dont il est relativement le mieux doté. Mécanisme : l’abondance relative d’un facteur fait baisser son prix relatif ; le coût de la production qui l’emploie intensivement baisse donc relativement ; le pays se spécialise dans cette production et l’exporte. Deux conditions sont indispensables : comparer des rapports de dotations entre pays, et comparer les intensités factorielles entre biens.",
  ['heckscher-ohlin', 'modèle hos', 'dotations factorielles'])
q('question ouverte', "En quoi le théorème Stolper-Samuelson transforme-t-il le débat sur le libre-échange ?",
  [], 0,
  "Il déplace la question du gain agrégé vers la répartition : l’ouverture augmente la rémunération réelle du facteur relativement abondant et réduit celle du facteur relativement rare. Dans un pays avancé abondant en qualifications, les travailleurs peu qualifiés des secteurs exposés perdent ; dans un pays abondant en travail peu qualifié, ils gagnent. Le débat devient donc normatif : un pays peut gagner globalement alors que des catégories identifiables perdent, ce qui justifie des politiques d’accompagnement.",
  ['stolper-samuelson', 'inégalités', 'politiques d’accompagnement'])
q('question ouverte', "Comment le théorème de Rybczynski rend-il les avantages comparatifs stratégiques ?",
  [], 0,
  "En montrant que l’accroissement d’une dotation augmente plus que proportionnellement la production du bien qui l’utilise intensivement, Rybczynski rend les dotations endogènes. Un État peut alors les construire : la Corée du Sud par l’éducation et la R&D, la Chine par l’accumulation du capital puis la qualification. La spécialisation cesse d’être une donnée naturelle pour devenir l’objet d’une politique industrielle et éducative, ce qui modifie la portée normative du modèle HOS.",
  ['rybczynski', 'avantage construit', 'corée du sud'])
q('question ouverte', "Pourquoi le commerce intra-branche constitue-t-il la limite décisive des théories traditionnelles ?",
  [], 0,
  "Les théories traditionnelles expliquent le commerce par des différences : de productivité chez Ricardo, de dotations dans HOS. Elles prévoient donc un commerce inter-branche entre pays dissemblables. Or l’essentiel des échanges se fait entre pays comparables, dans les mêmes branches et dans les deux sens. Il faut alors mobiliser la différenciation des produits, la concurrence monopolistique, la demande de différence et les rendements croissants — c’est-à-dire les théories contemporaines.",
  ['commerce intra-branche', 'limites', 'différenciation'])
q('question ouverte', "Distinguez approches néo-factorielles et néo-technologiques.",
  [], 0,
  "Les approches néo-factorielles conservent la logique des dotations mais en enrichissent la liste : Keesing (1966) fait de la qualification un facteur, puis le capital humain élargit encore la nomenclature. Les approches néo-technologiques s’attaquent à ce que Ricardo constatait sans l’expliquer, l’origine des écarts de productivité : Posner (1961) l’attribue à une avance technologique temporaire, Vernon (1966) l’inscrit dans un cycle de vie du produit qui déplace la production au fil de sa banalisation.",
  ['keesing', 'posner', 'vernon'])
q('question ouverte', "Présentez le cycle de vie international du produit de Vernon et son illustration.",
  [], 0,
  "Quatre phases : naissance dans le pays innovateur, où la demande est forte et la technologie encore incertaine ; croissance et premières exportations lorsque la demande étrangère apparaît ; maturité, où le procédé se standardise et la production se délocalise vers des pays à coûts plus faibles ; enfin importation par le pays innovateur. Les téléviseurs à écran plat, passés du Japon à la Corée puis à la Chine et au Vietnam, en fournissent l’exemple : ce n’est pas le pays qui perd son avantage, c’est le produit qui change de nature.",
  ['vernon', 'cycle de vie du produit', 'délocalisation'])
q('question ouverte', "Comment Krugman inverse-t-il la causalité des théories traditionnelles ?",
  [], 0,
  "Dans les théories traditionnelles, la dotation détermine la spécialisation, donc la localisation. Avec des rendements croissants, la relation s’inverse : une implantation initiale, parfois accidentelle, permet d’atteindre un volume qui abaisse les coûts unitaires, ce qui attire d’autres activités et consolide l’avantage. La localisation engendre alors la dotation. Bangalore, Toulouse ou la Silicon Valley l’illustrent : l’avantage comparatif est acquis plutôt qu’hérité.",
  ['krugman', 'agglomération', 'nouvelle géographie économique'])
q('question ouverte', "Pourquoi les rendements croissants réhabilitent-ils partiellement le protectionnisme éducateur ?",
  [], 0,
  "Si les coûts unitaires baissent avec le volume, un producteur potentiellement plus efficace peut rester exclu du marché faute d’atteindre le seuil Q0 face à un concurrent déjà installé. L’ouverture immédiate empêche alors l’apparition d’une industrie viable. Une protection temporaire permet de franchir ce seuil : l’argument de List reçoit ainsi une formalisation. Elle reste toutefois conditionnée par un marché domestique suffisamment vaste, le maintien d’une concurrence interne et une protection strictement temporaire.",
  ['krugman', 'list', 'protectionnisme éducateur'])
q('question ouverte', "Analysez les effets d’un droit de douane dans un petit pays à l’aide des surplus.",
  [], 0,
  "Le prix intérieur augmente du montant du droit. La production nationale s’accroît, la consommation et les importations diminuent, et l’État perçoit des recettes douanières. Le surplus des producteurs augmente, celui des consommateurs diminue davantage. La différence comprend les recettes, qui sont un transfert, mais aussi deux pertes sèches : une distorsion à la production, car des unités nationales coûteuses remplacent des importations moins chères, et une distorsion à la consommation, car des achats sont renoncés. Le solde collectif est négatif.",
  ['droit de douane', 'analyse en surplus', 'perte sèche'])
q('question ouverte', "Pourquoi un grand pays peut-il théoriquement gagner à protéger son marché, et pourquoi cet argument reste-t-il fragile ?",
  [], 0,
  "En réduisant sa demande d’importations, un grand pays fait baisser le prix mondial : il paie ses importations moins cher, ce qui constitue un gain de termes de l’échange qui peut excéder les deux pertes sèches. L’argument reste fragile pour trois raisons : le gain s’obtient aux dépens des partenaires, il appelle donc des représailles qui l’annulent ; il suppose une élasticité favorable de l’offre étrangère ; et il ne dit rien de la répartition interne des gains et des pertes.",
  ['grand pays', 'termes de l’échange', 'représailles'])
q('question ouverte', "Distinguez efficacité, efficience et équité d’une politique commerciale, en vous appuyant sur un exemple chiffré.",
  [], 0,
  "L’efficacité est l’atteinte de l’objectif : la mesure a-t-elle préservé l’emploi visé ? L’efficience rapporte le résultat à son coût : 1 000 emplois sauvés pour 200 millions d’euros représentent 200 000 euros par emploi, à comparer à d’autres usages de la même somme. L’équité porte sur la répartition : qui paie, qui gagne ? S’y ajoute la question des moyens, c’est-à-dire de la compatibilité de l’instrument avec les engagements internationaux. Une politique peut être efficace et pourtant inefficiente et inéquitable.",
  ['efficacité', 'efficience', 'équité'])
q('question ouverte', "Expliquez pourquoi le protectionnisme est politiquement viable malgré son coût collectif.",
  [], 0,
  "À partir de Pareto, le cours souligne l’asymétrie d’organisation : les gains sont concentrés sur un petit nombre de producteurs identifiables, qui ont intérêt et capacité à se mobiliser ; les pertes sont diffuses, réparties en petites sommes sur des consommateurs dispersés qui n’ont ni l’information ni l’incitation à se coordonner. Léo Charles montre comment ces intérêts se constituent en bloc social, à l’exemple des céréaliers français de la fin du XIXe siècle.",
  ['pareto', 'léo charles', 'groupes de pression'])
q('question ouverte', "Pourquoi Bairoch et Jean-Marc Daniel invitent-ils à relativiser l’opposition historique entre libre-échange et protectionnisme ?",
  [], 0,
  "Bairoch établit que le XIXe siècle est un « océan de protectionnisme » : le Royaume-Uni est d’abord protectionniste, les États-Unis et l’Allemagne s’industrialisent derrière des tarifs élevés, et les économies les plus protégées croissent alors plus vite. Jean-Marc Daniel résume l’écart entre doctrines et pratiques : « les pratiques sont tendanciellement protectionnistes ». Il faut toutefois se garder d’en conclure à l’efficacité du protectionnisme : ces constats réfutent un automatisme, ils n’établissent pas la relation inverse.",
  ['bairoch', 'jean-marc daniel', 'histoire'])
q('question ouverte', "Présentez la politique commerciale stratégique de Brander et Spencer et ses limites.",
  [], 0,
  "Dans un marché mondial trop étroit pour deux producteurs à coûts fixes élevés, l’avantage du premier entrant décide de l’issue : Boeing entrée la première dissuade Airbus. Une subvention peut renverser l’équilibre, rendre la production profitable au champion national et transférer la rente du concurrent. Trois limites : l’État doit anticiper correctement coûts, demande et réactions — une erreur d’information rend la subvention collectivement coûteuse ; la généralisation déclenche une guerre de subventions ; le conflit Airbus-Boeing, jusqu’aux rétorsions autorisées en 2019 et suspendues en 2021, en montre le caractère potentiellement à somme nulle.",
  ['brander et spencer', 'airbus-boeing', 'politique commerciale stratégique'])
q('question ouverte', "En quoi les « habits neufs du protectionnisme » renouvellent-ils le débat ?",
  [], 0,
  "La protection n’est plus justifiée par la défense d’une branche mais par des biens communs : climat, santé, sécurité des approvisionnements, cohésion sociale. Vuillemey y voit la préservation d’une capacité d’action collective ; Rodrik parle d’un paradigme productiviste ; Emlinger, Guimbard et Lefebvre documentent une nouvelle hiérarchie des objectifs. L’enjeu analytique est double : ces justifications sont plus difficiles à contester que les anciennes, mais elles peuvent aussi servir de prétexte à une protection ordinaire — d’où l’importance des quatre questions d’évaluation.",
  ['vuillemey', 'rodrik', 'protectionnisme environnemental'])
q('question ouverte', "Qu’appelle-t-on fragmentation géo-économique, et quelles stratégies les États adoptent-ils ?",
  [], 0,
  "La fragmentation géo-économique désigne la recomposition du commerce mondial par blocs politiques : les échanges ne disparaissent pas, ils se réorientent selon des critères de sécurité et d’alliance — friend-shoring, sécurisation des approvisionnements, course au leadership technologique, arsenalisation de l’interdépendance. Face au tournant protectionniste américain, les États arbitrent entre trois stratégies : négocier pour obtenir des exemptions, diversifier leurs partenaires pour réduire leur exposition, ou entrer dans la confrontation par des rétorsions. Guimbard, Vicard et Wibaux montrent que les volumes résistent mais que la géographie change.",
  ['fragmentation géo-économique', 'friend-shoring', 'guimbard'])

TYPES = {'qcm': 'qcm', 'vrai/faux': 'vraifa', 'question ouverte': 'questi'}
QUIZ = []
TAGS = {}
for _i, (_t, _q, _o, _a, _e, _g) in enumerate(Q, 1):
    _id = 'ch23-%s-%d' % (TYPES[_t], _i)
    QUIZ.append({'type': _t, 'q': _q, 'opts': _o, 'ans': _a, 'exp': _e, 'ch': 23, 'id': _id})
    TAGS[_id] = _g
