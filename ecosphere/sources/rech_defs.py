# -*- coding: utf-8 -*-
"""Définitions créées pour des notions que les cours traitent sans les définir.

Chaque entrée est rédigée à partir du passage du cours indiqué par `anc`
(l'intitulé de la section) et n'ajoute rien qui ne s'y trouve. Elles
complètent les 742 définitions moissonnées directement dans les cours et les
définitions déjà présentes ailleurs dans ÉcoSphère.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias)
DEFS = [

 ("Taux marginal de substitution", ['4'], "L’idée de base est l’arbitrage",
  "Le taux marginal de substitution mesure le nombre d’unités du bien Y "
  "auxquelles un individu doit renoncer pour obtenir une unité supplémentaire "
  "du bien X, tout en restant sur la même courbe d’indifférence. Il traduit "
  "donc un arbitrage, et il est par définition négatif, le signe négatif "
  "marquant le renoncement. Son équivalent du côté de la production est le "
  "taux marginal de substitution technique, qui mesure la quantité de capital "
  "à laquelle le producteur peut renoncer lorsqu’il emploie une unité "
  "supplémentaire de travail à production inchangée.",
  ["tms", "tmst", "taux marginal de substitution technique",
   "renoncement entre deux biens"]),

 ("Économie d’endettement", ['2'], "Économie d’endettement",
  "Une économie d’endettement est une économie dans laquelle le financement "
  "est dominé par les banques : le crédit bancaire y joue le rôle central et "
  "l’intermédiation bancaire y est forte. Les agents qui ont besoin de "
  "financement s’adressent d’abord aux banques plutôt qu’aux marchés de "
  "capitaux.",
  ["economie d endettement", "financement intermedie"]),

 ("Économie de marchés financiers", ['2'], "Les modalités du financement",
  "Une économie de marchés financiers est une économie dans laquelle les "
  "agents se financent davantage par les marchés de capitaux, en émettant et "
  "en échangeant des titres, plutôt que par le crédit bancaire. Le cours "
  "précise que cette opposition avec l’économie d’endettement doit être "
  "nuancée : les banques restent centrales, mais elles interviennent "
  "elles-mêmes largement sur les marchés.",
  ["financement direct", "economie de marche financier"]),

 ("Taux directeurs", ['2'], "Objectifs",
  "Les taux directeurs sont les taux auxquels la banque centrale refinance "
  "les banques : ils fixent le prix de la liquidité et commandent le coût du "
  "crédit dans l’économie. Une baisse des taux directeurs rend le crédit "
  "moins cher, ce qui soutient l’investissement des entreprises, la "
  "consommation des ménages, donc la demande globale et la croissance.",
  ["taux directeur", "taux de refinancement"]),

 ("Allocation sous-optimale des ressources", ['5'],
  "Allocation sous-optimale des ressources",
  "Une allocation sous-optimale des ressources désigne une situation dans "
  "laquelle le marché ne conduit ni à la bonne quantité ni au bon prix : on "
  "produit une quantité inférieure à celle qui égaliserait coût et "
  "disposition à payer. Une partie de la richesse collective disparaît sans "
  "que personne ne la récupère, ni les producteurs ni les consommateurs, et "
  "les surplus sont redistribués au détriment du consommateur.",
  ["allocation sous optimale", "perte de surplus collectif"]),

 ("Société hyper-industrielle", ['6'], "La société hyper-industrielle",
  "La société hyper-industrielle est la formule par laquelle Pierre Veltz "
  "décrit une économie d’autant plus dépendante d’infrastructures "
  "industrielles lourdes qu’elle paraît immatérielle : l’industrie structure "
  "les flux mondiaux, fournit les équipements du numérique et organise les "
  "réseaux logistiques globaux. Le numérique y apparaît comme une industrie "
  "cachée, et la frontière entre industrie et services se brouille.",
  ["societe hyper industrielle", "veltz", "industrie cachee"]),

 ("Demande intérieure", ['1', '7', '21', '22', '23'],
  "La balance des paiements",
  "La demande intérieure est la demande adressée à l’économie par ses "
  "propres résidents : consommation des ménages, investissement des "
  "entreprises et dépenses publiques. Elle se distingue de la demande "
  "extérieure, formée par les exportations. Son augmentation porte en partie "
  "sur des produits nationaux et en partie sur des importations, ce qui "
  "explique le lien entre relance intérieure et dégradation du solde "
  "extérieur.",
  ["demande interne", "demande domestique"]),

 ("Économie socialiste de marché", ['7'], "économie socialiste de marché",
  "L’économie socialiste de marché désigne le régime économique chinois issu "
  "des réformes engagées à la fin des années 1970 : le marché y organise une "
  "part croissante des échanges et des prix, mais la propriété publique, la "
  "planification et le contrôle du Parti sur les grandes entreprises et sur "
  "l’allocation du crédit sont maintenus. L’ouverture y est sélective et "
  "pilotée par l’État plutôt que générale.",
  ["socialisme de marche", "modele chinois"]),

 ("RNB par habitant en parité de pouvoir d’achat", ['7'],
  "RNB par habitant en PPA",
  "Le revenu national brut par habitant en parité de pouvoir d’achat rapporte "
  "le revenu national à la population en corrigeant les écarts de prix entre "
  "pays. Le cours justifie ce choix : un simple taux de change de marché "
  "dépend de la spéculation, des mouvements de capitaux et des anticipations, "
  "et ne traduit pas ce qu’un revenu permet réellement d’acheter. La parité "
  "de pouvoir d’achat permet au contraire de comparer le volume de biens et "
  "de services effectivement accessibles.",
  ["rnb par habitant", "rnb ppa", "parite de pouvoir d achat",
   "ppa", "revenu national brut par habitant"]),

 ("Accroissement naturel", ['7'], "L’accroissement naturel",
  "L’accroissement naturel est la différence entre les naissances et les "
  "décès d’une population sur une période : lorsque les naissances sont "
  "supérieures aux décès, la population augmente naturellement, sans que les "
  "migrations y soient pour quelque chose. C’est l’une des deux sources de la "
  "croissance démographique, à côté du solde migratoire.",
  ["solde naturel", "croissance naturelle de la population"]),

 ("Stratégie des industries industrialisantes", ['7'],
  "La stratégie des industries industrialisantes",
  "La stratégie des industries industrialisantes, dont le terme vient de "
  "François Perroux, consiste à donner la priorité à l’industrie lourde et "
  "aux secteurs d’amont — sidérurgie, chimie, énergie, biens d’équipement — "
  "pour qu’ils entraînent ensuite le reste de l’économie. Elle relève d’une "
  "logique de développement autocentré : forte intervention de l’État qui "
  "administre les prix, planifie et nationalise, protection vis-à-vis de "
  "l’extérieur et recherche d’autarcie, le développement étant censé se faire "
  "hors du marché.",
  ["industries industrialisantes", "industrie industrialisante",
   "developpement autocentre"]),

 ("Risques physiques du changement climatique", ['7'],
  "La tragédie des horizons",
  "Les risques physiques sont les dommages directs causés par le changement "
  "climatique : inondations, incendies, canicules, tempêtes, sécheresses. Ils "
  "se traduisent par la destruction d’actifs — maisons, infrastructures — par "
  "une hausse des coûts d’assurance et d’indemnisation, et parfois par le "
  "refus d’assurer les zones trop exposées. Avec les risques de transition et "
  "les risques de responsabilité, ils forment la typologie des risques "
  "climatiques pour le système financier.",
  ["risque physique", "risques climatiques physiques"]),

 ("Risques de transition", ['7'], "Risques de transition",
  "Les risques de transition sont les pertes provoquées non par le climat "
  "lui-même mais par le passage à une économie décarbonée : une "
  "réglementation nouvelle, une taxe carbone ou un changement technologique "
  "peuvent dévaloriser brutalement des actifs liés aux énergies fossiles. Ils "
  "complètent les risques physiques et les risques de responsabilité dans "
  "l’analyse des risques climatiques pour le système financier.",
  ["risque de transition", "actifs echoues"]),

 ("Temps partiel subi", ['8'], "Temps partiel subi",
  "Le temps partiel subi est la situation d’un salarié qui travaille à temps "
  "partiel faute de pouvoir obtenir davantage d’heures. Le cours en fait une "
  "forme de précarité, à distinguer du temps partiel choisi, retenu "
  "volontairement, notamment pour des raisons de vie familiale.",
  ["temps partiel contraint", "sous emploi"]),

 ("Économie du partage", ['8'], "L’économie du partage",
  "L’économie du partage désigne les activités par lesquelles des plateformes "
  "permettent la location de logements et la mutualisation des usages, de "
  "sorte que l’usage d’un bien tend parfois à remplacer sa propriété. Elle "
  "fait partie des transformations que la révolution numérique produit sur "
  "les modèles économiques.",
  ["economie collaborative", "plateforme de partage"]),

 ("Logique actionnariale", ['8', '9'], "Logique actionnariale",
  "La logique actionnariale est le mode de gouvernance qui donne la priorité "
  "à la rentabilité servie aux apporteurs de capitaux et au pouvoir des "
  "investisseurs sur la conduite de l’entreprise. Le cours l’oppose à une "
  "gouvernance devenue hybride, où elle coexiste avec la prise en compte "
  "d’autres parties prenantes et avec la responsabilité sociale de "
  "l’entreprise.",
  ["gouvernance actionnariale", "shareholder value",
   "primaute de l actionnaire"]),

 ("Concentration des entreprises", ['9'], "La concentration des entreprises",
  "La concentration des entreprises est la réduction du nombre d’acteurs "
  "présents sur un marché, par rachat de concurrents ou par croissance "
  "interne. Elle donne du pouvoir de marché : l’entreprise augmente ses parts "
  "de marché, réduit l’atomicité et peut devenir dominante, de sorte que la "
  "concentration peut transformer une situation de concurrence en oligopole "
  "ou en monopole. Elle prend trois formes : horizontale, verticale et "
  "conglomérale.",
  ["concentration du marche", "concentration industrielle"]),

 ("Théorie des marchés contestables", ['9'],
  "La théorie des marchés contestables",
  "La théorie des marchés contestables, développée dans les années 1980 par "
  "William Baumol, John Panzar et Robert Willig, soutient que le véritable "
  "critère de la concurrence n’est pas le nombre d’entreprises présentes mais "
  "la liberté d’entrée et de sortie du marché. Même seule sur son marché, une "
  "entreprise menacée par une entrée possible peut se comporter comme si elle "
  "était en concurrence.",
  ["marches contestables", "baumol panzar willig", "concurrence potentielle"]),

 ("Dynamique de groupe", ['10'], "La dynamique de groupe",
  "La dynamique de groupe désigne les effets propres à la décision "
  "collective. Un groupe peut en théorie décider mieux qu’un individu seul : "
  "il réunit davantage d’informations, confronte les idées et corrige "
  "mutuellement les erreurs. Mais il peut aussi produire du conformisme et "
  "dégrader la qualité de la décision, ce que Christian Morel mobilise pour "
  "expliquer les décisions absurdes.",
  ["conformisme de groupe", "decision collective"]),

 ("Effet volume", ['21'], "Effet volume",
  "L’effet volume désigne la transmission d’un ralentissement chinois au "
  "reste du monde par les quantités échangées : la Chine étant un très grand "
  "importateur de matières premières, de produits intermédiaires et de "
  "produits agricoles, une baisse de sa croissance réduit ses importations et "
  "donc les volumes exportés par ses partenaires commerciaux.",
  ["canal du volume", "ralentissement chinois"]),

 ("Deuxième dégroupage", ['21'], "Deuxième dégroupage",
  "Le deuxième dégroupage, analysé par Richard Baldwin, sépare les étapes du "
  "processus productif lui-même : la conception et l’assemblage cessent "
  "d’être réalisés au même endroit — conçu en Californie, assemblé en Chine — "
  "et ce sont des biens intermédiaires qui s’échangent, d’où l’expression de "
  "« commerce de tâches ». Il se distingue du premier dégroupage, qui avait "
  "séparé le lieu de production du lieu de consommation, et caractérise "
  "l’hypermondialisation.",
  ["second degroupage", "commerce de taches", "unbundling",
   "premier degroupage"]),

 ("Zones économiques spéciales", ['21'], "Les zones économiques spéciales",
  "Les zones économiques spéciales sont des territoires dans lesquels les "
  "entreprises étrangères bénéficient de conditions particulièrement "
  "favorables : fiscalité attractive, règles administratives simplifiées, "
  "infrastructures adaptées, main-d’œuvre abondante et accès facilité au "
  "marché national. La Chine les développe à partir de la fin des années 1970 "
  "et du début des années 1980 : elle n’ouvre donc pas son territoire de "
  "manière uniforme mais expérimente l’ouverture sur des espaces délimités.",
  ["zes", "zone economique speciale", "ouverture selective"]),

 ("Montée en gamme chinoise", ['21', '22'], "La montée en gamme chinoise",
  "La montée en gamme chinoise désigne le déplacement de la Chine vers des "
  "activités à plus forte valeur ajoutée et à plus fort contenu "
  "technologique. Le cours la documente par le plan Made in China 2025, "
  "lancé en 2015 pour produire davantage de technologies sur le territoire "
  "chinois et réduire la dépendance technologique étrangère, et par "
  "l’exemple de l’iPhone : la valeur ajoutée chinoise passe d’environ 4 % "
  "pour l’iPhone 3G de 2009 à environ 25 % pour l’iPhone X de 2018.",
  ["made in china 2025", "montee en gamme de la chine"]),

 ("Mondialisation productive", ['21', '22'], "Mondialisation productive",
  "La mondialisation productive est la dimension de la mondialisation qui "
  "porte sur la localisation de la production plutôt que sur les seuls "
  "échanges de biens : elle procède des investissements directs à l’étranger "
  "réalisés par les firmes multinationales, qui créent une filiale, achètent "
  "une entreprise étrangère ou construisent une usine à l’étranger. Elle se "
  "distingue de la mondialisation commerciale et de la mondialisation "
  "financière.",
  ["mondialisation de la production", "internationalisation de la production"]),

 ("Secteurs stratégiques", ['22', '21'], "Les secteurs stratégiques",
  "Les secteurs stratégiques sont ceux dont l’interruption bloquerait une "
  "grande partie de l’économie : le cours cite l’alimentation, "
  "l’électronique, les télécommunications et les matières premières "
  "critiques. Ces dernières constituent un cas particulièrement révélateur, "
  "puisque leur disponibilité conditionne à la fois les transitions "
  "énergétique, numérique et militaire.",
  ["secteur strategique", "filiere critique", "matieres premieres critiques"]),

 ("Services associés", ['22'], "La recherche de la compétitivité",
  "Les services associés sont les prestations qui accompagnent un produit et "
  "dont dépend sa valeur autant que de ses caractéristiques techniques : "
  "maintenance, financement, service après-vente, réseau de distribution. Ils "
  "constituent l’une des composantes de la compétitivité hors-prix.",
  ["service associe", "service apres vente"]),
]
