# -*- coding: utf-8 -*-
"""Inventaire des dossiers de la section « Autour d'une notion ».

Reprend exactement les 28 ensembles demandés : pour chacun, le titre, la liste
des dossiers et les questions de dissertation associées. Aucun dossier n'est
inventé ici ; la couverture réelle par les cours est vérifiée séparément.
"""

ENSEMBLES = []


def ens(num, titre, dossiers, questions):
    ENSEMBLES.append({'num': num, 'titre': titre,
                      'dossiers': dossiers, 'questions': questions})


ens(1, "La croissance économique et ses moteurs", [
    "Croissance économique", "Croissance extensive et croissance intensive",
    "Accumulation du capital", "Investissement",
    "Productivité et gains de productivité", "Productivité globale des facteurs",
    "Progrès technique", "Croissance endogène", "Capital humain",
    "Recherche et développement", "Infrastructures et capital public",
    "Institutions et croissance", "Droits de propriété",
    "Convergence et divergence des économies", "Rattrapage économique",
    "Stagnation séculaire", "Croissance potentielle",
    "Mesure de la richesse et limites du PIB",
], [
    "D’où vient la croissance économique ?",
    "L’accumulation du capital suffit-elle à expliquer la croissance ?",
    "Pourquoi certains pays rattrapent-ils les pays développés tandis que d’autres restent en retard ?",
    "La croissance peut-elle s’entretenir elle-même ?",
    "Les institutions sont-elles la cause fondamentale de la prospérité ?",
    "Sommes-nous condamnés au ralentissement de la croissance ?",
    "Produire davantage signifie-t-il vivre mieux ?",
])

ens(2, "L’innovation et les transformations du capitalisme", [
    "Invention et innovation", "Entrepreneur innovateur", "Destruction créatrice",
    "Grappes d’innovations", "Révolutions industrielles", "Révolutions technologiques",
    "Diffusion des innovations", "Innovation de produit et innovation de procédé",
    "Innovations radicales et incrémentales", "Brevets et propriété intellectuelle",
    "Rentes d’innovation", "Frontière technologique", "Économie numérique",
    "Intelligence artificielle", "Effets de réseau", "Capitalisme de plateforme",
], [
    "L’innovation profite-t-elle à tous ?",
    "La destruction créatrice conduit-elle nécessairement au progrès ?",
    "La concurrence stimule-t-elle toujours l’innovation ?",
    "Les monopoles peuvent-ils favoriser le progrès technique ?",
    "Pourquoi certaines innovations se diffusent-elles difficilement ?",
    "L’intelligence artificielle constitue-t-elle une nouvelle révolution industrielle ?",
    "Le capitalisme peut-il fonctionner sans innovation ?",
])

ens(3, "Le développement et les stratégies de rattrapage", [
    "Développement économique", "Sous-développement", "Développement humain",
    "Capabilités", "Pauvreté multidimensionnelle", "Émergence",
    "Pays les moins avancés", "Cercle vicieux de la pauvreté", "Trappe à pauvreté",
    "Trappe à revenu intermédiaire", "Transformation structurelle",
    "Dualisme économique", "Industrialisation par substitution aux importations",
    "Industrialisation par promotion des exportations", "État développeur",
    "Dépendance économique", "Malédiction des ressources naturelles",
    "Syndrome hollandais", "Aide au développement", "Ajustement structurel",
    "Consensus de Washington",
], [
    "La croissance suffit-elle au développement ?",
    "Existe-t-il une voie unique vers le développement ?",
    "Faut-il s’ouvrir pour se développer ?",
    "L’industrialisation est-elle indispensable au développement ?",
    "L’abondance de ressources naturelles constitue-t-elle une richesse ?",
    "Pourquoi les trajectoires asiatiques et africaines diffèrent-elles ?",
    "Un pays peut-il se développer sans État fort ?",
])

ens(4, "L’environnement et les limites de la croissance", [
    "Développement durable", "Soutenabilité faible et soutenabilité forte",
    "Capital naturel", "Limites écologiques", "Externalités environnementales",
    "Biens communs", "Tragédie des communs", "Gouvernance des communs",
    "Changement climatique", "Justice climatique", "Transition énergétique",
    "Découplage entre croissance et pressions environnementales", "Effet rebond",
    "Croissance verte", "Décroissance", "Sobriété", "Économie circulaire",
    "Fiscalité écologique", "Taxe carbone", "Marchés de quotas d’émission",
    "Réglementation environnementale", "Innovation verte",
], [
    "Une croissance infinie est-elle possible dans un monde fini ?",
    "Peut-on concilier croissance et protection de l’environnement ?",
    "Le progrès technique peut-il résoudre la crise écologique ?",
    "Faut-il donner un prix à la nature ?",
    "Le marché peut-il protéger l’environnement ?",
    "Comment répartir le coût de la transition écologique ?",
    "Les pays pauvres doivent-ils supporter les mêmes contraintes que les pays riches ?",
])

ens(5, "Le marché, les prix et la concurrence", [
    "Marché", "Coordination par les prix", "Offre et demande", "Équilibre de marché",
    "Concurrence pure et parfaite", "Surplus du consommateur et du producteur",
    "Efficacité économique", "Optimum de Pareto", "Monopole", "Oligopole",
    "Concurrence monopolistique", "Pouvoir de marché", "Barrières à l’entrée",
    "Concentration économique", "Ententes", "Discrimination par les prix",
    "Marchés contestables", "Politique de la concurrence",
], [
    "Le marché assure-t-il une allocation efficace des ressources ?",
    "Les prix transmettent-ils toute l’information nécessaire ?",
    "La concurrence bénéficie-t-elle toujours au consommateur ?",
    "Une grande entreprise est-elle nécessairement moins concurrentielle ?",
    "Faut-il lutter contre tous les monopoles ?",
    "Efficacité économique et justice sociale sont-elles compatibles ?",
])

ens(6, "Les défaillances du marché et les limites de l’intervention publique", [
    "Externalités positives et négatives", "Biens collectifs", "Biens communs",
    "Passager clandestin", "Asymétries d’information", "Sélection adverse",
    "Aléa moral", "Marchés incomplets", "Coûts de transaction",
    "Défaillances de coordination", "Réglementation", "Taxation et subventions",
    "Défaillances de l’État", "Capture du régulateur", "Recherche de rente",
    "Bureaucratie", "Choix publics",
], [
    "Quand l’intervention de l’État est-elle nécessaire ?",
    "L’État fait-il toujours mieux que le marché ?",
    "Une subvention peut-elle améliorer l’efficacité économique ?",
    "Pourquoi certaines activités sont-elles insuffisamment produites par le marché ?",
    "Comment corriger une défaillance sans en créer une autre ?",
    "Qui doit réguler les régulateurs ?",
])

ens(7, "La consommation, l’épargne et les comportements économiques", [
    "Consommation", "Utilité et préférences", "Contrainte budgétaire",
    "Choix du consommateur", "Effet revenu et effet substitution", "Élasticités",
    "Consommation ostentatoire", "Effets d’imitation et de distinction",
    "Consommation de masse", "Filière inversée", "Revenu disponible",
    "Revenu permanent", "Cycle de vie", "Épargne de précaution",
    "Propension à consommer", "Rationalité limitée", "Biais comportementaux",
], [
    "Le consommateur est-il souverain ?",
    "Consommons-nous uniquement pour satisfaire des besoins ?",
    "Le revenu détermine-t-il entièrement la consommation ?",
    "Pourquoi les ménages épargnent-ils ?",
    "Une hausse de l’épargne favorise-t-elle toujours l’économie ?",
    "Les comportements individuels sont-ils toujours rationnels ?",
])

ens(8, "L’entreprise, l’entrepreneur et la gouvernance", [
    "Entreprise", "Entrepreneur", "Profit", "Risque et incertitude",
    "Frontières de la firme", "Coûts de transaction", "Relation d’agence",
    "Séparation entre propriété et contrôle", "Capitalisme entrepreneurial",
    "Capitalisme managérial", "Capitalisme actionnarial", "Gouvernance d’entreprise",
    "Valeur actionnariale", "Parties prenantes",
    "Responsabilité sociale des entreprises",
    "Concentration et croissance des entreprises", "Intégration verticale",
    "Externalisation", "Financiarisation de l’entreprise",
], [
    "Pourquoi les entreprises existent-elles ?",
    "Qui dirige réellement l’entreprise ?",
    "Le profit constitue-t-il son seul objectif ?",
    "Les intérêts des actionnaires et des salariés sont-ils compatibles ?",
    "La grande entreprise est-elle plus efficace ?",
    "La responsabilité sociale transforme-t-elle le capitalisme ?",
])

ens(9, "L’organisation du travail et la sociologie des organisations", [
    "Division du travail", "Taylorisme", "Fordisme", "Toyotisme", "Bureaucratie",
    "Organisation scientifique du travail", "École des relations humaines",
    "Motivation au travail", "Coopération", "Autorité et pouvoir",
    "Règles formelles et informelles", "Zones d’incertitude", "Acteur stratégique",
    "Culture d’entreprise", "Autonomie au travail", "Contrôle du travail",
    "Flexibilité organisationnelle", "Souffrance et sens du travail",
], [
    "Organiser le travail consiste-t-il seulement à rechercher l’efficacité ?",
    "La division du travail libère-t-elle ou aliène-t-elle ?",
    "Peut-on supprimer les conflits dans une organisation ?",
    "Les règles suffisent-elles à expliquer le fonctionnement d’une entreprise ?",
    "L’autonomie des salariés réduit-elle réellement le contrôle ?",
    "Les nouvelles organisations du travail rompent-elles avec le taylorisme ?",
])

ens(10, "Le travail, l’emploi et le chômage", [
    "Travail et emploi", "Marché du travail", "Population active",
    "Chômage conjoncturel et structurel", "Chômage classique et keynésien",
    "Chômage frictionnel", "Chômage de longue durée", "Hystérèse du chômage",
    "Appariement", "Salaire minimum", "Salaire d’efficience",
    "Segmentation du marché du travail", "Insiders et outsiders", "Flexibilité",
    "Précarité", "Polarisation des emplois", "Progrès technique biaisé",
    "Employabilité", "Politiques actives et passives de l’emploi",
], [
    "Le chômage s’explique-t-il par un coût du travail trop élevé ?",
    "La croissance suffit-elle à créer des emplois ?",
    "Le progrès technique détruit-il le travail ?",
    "La flexibilité réduit-elle le chômage ?",
    "Le salaire minimum protège-t-il ou exclut-il ?",
    "Faut-il protéger les emplois ou les travailleurs ?",
])

ens(11, "La monnaie, les banques et le crédit", [
    "Fonctions de la monnaie", "Confiance monétaire", "Création monétaire",
    "Monnaie bancaire", "Crédit", "Banques commerciales", "Banque centrale",
    "Liquidité", "Taux d’intérêt nominal et réel", "Préférence pour la liquidité",
    "Multiplicateur et diviseur de crédit", "Refinancement bancaire",
    "Prêteur en dernier ressort", "Indépendance de la banque centrale",
    "Neutralité de la monnaie", "Monnaie et activité économique",
], [
    "Pourquoi accepte-t-on la monnaie ?",
    "Qui crée la monnaie ?",
    "Les banques prêtent-elles seulement l’épargne qu’elles collectent ?",
    "La monnaie influence-t-elle durablement la production ?",
    "Le crédit est-il indispensable à la croissance ?",
    "Une banque centrale doit-elle être indépendante ?",
])

ens(12, "Le financement de l’économie et la finance", [
    "Besoin et capacité de financement", "Autofinancement",
    "Financement direct et indirect", "Intermédiation financière",
    "Désintermédiation", "Actions et obligations", "Marchés financiers",
    "Allocation de l’épargne", "Diversification du risque",
    "Efficience des marchés", "Spéculation", "Mimétisme", "Bulles financières",
    "Financiarisation", "Finance et croissance", "Régulation financière",
], [
    "La finance favorise-t-elle la croissance ?",
    "Les marchés financiers allouent-ils efficacement le capital ?",
    "La spéculation est-elle utile ?",
    "Peut-il y avoir trop de finance ?",
    "Le financement par les banques est-il préférable au financement par les marchés ?",
    "Comment mettre la finance au service de l’investissement productif ?",
])

ens(13, "Les crises et l’instabilité économique", [
    "Cycles économiques", "Crises de surproduction", "Crises de demande",
    "Chocs d’offre et de demande", "Accélérateur d’investissement",
    "Cycle du crédit", "Instabilité financière", "Paradoxe de la tranquillité",
    "Surendettement", "Déflation par la dette", "Crise bancaire",
    "Panique bancaire", "Risque systémique", "Contagion financière",
    "Aléa moral des sauvetages", "Régulation macroprudentielle",
], [
    "Les crises sont-elles inhérentes au capitalisme ?",
    "Pourquoi la stabilité peut-elle préparer l’instabilité ?",
    "Comment une crise financière devient-elle une crise économique ?",
    "Faut-il toujours sauver les banques ?",
    "Peut-on prévenir les crises ?",
    "Pourquoi les crises se répètent-elles malgré les régulations ?",
])

ens(14, "L’inflation et la stabilité des prix", [
    "Inflation", "Désinflation", "Déflation", "Hyperinflation",
    "Inflation par la demande", "Inflation par les coûts", "Inflation importée",
    "Boucle prix-salaires", "Anticipations d’inflation", "Courbe de Phillips",
    "Stagflation", "Pouvoir d’achat", "Crédibilité monétaire",
    "Ancrage des anticipations",
], [
    "L’inflation est-elle toujours un phénomène monétaire ?",
    "Qui gagne et qui perd avec l’inflation ?",
    "Faut-il rechercher une inflation nulle ?",
    "Peut-on réduire l’inflation sans augmenter le chômage ?",
    "Pourquoi la déflation peut-elle être dangereuse ?",
    "Comment réagir à une inflation provoquée par un choc d’offre ?",
])

ens(15, "L’État et les politiques économiques", [
    "État minimal", "État interventionniste",
    "Fonctions d’allocation, de redistribution et de stabilisation",
    "Politique budgétaire", "Politique monétaire", "Politique de relance",
    "Politique de rigueur", "Multiplicateur budgétaire", "Stabilisateurs automatiques",
    "Effet d’éviction", "Équivalence ricardienne", "Déficit public", "Dette publique",
    "Soutenabilité de la dette", "Policy mix", "Règles et discrétion",
    "Anticipations", "Contrainte extérieure", "Modèles IS-LM et IS-LM-BP",
    "Trappe à liquidité",
], [
    "L’État peut-il stabiliser l’économie ?",
    "Dans quelles conditions une relance est-elle efficace ?",
    "La dette publique constitue-t-elle nécessairement un problème ?",
    "Faut-il coordonner les politiques budgétaire et monétaire ?",
    "Une politique efficace en économie fermée le reste-t-elle en économie ouverte ?",
    "Faut-il privilégier les règles ou la liberté d’action des gouvernements ?",
])

ens(16, "Le commerce international et la spécialisation", [
    "Libre-échange", "Avantages absolus", "Avantages comparatifs",
    "Dotations factorielles", "Spécialisation internationale",
    "Division internationale du travail", "Gains à l’échange",
    "Répartition des gains du commerce", "Égalisation des rémunérations factorielles",
    "Commerce interbranche et intrabranche", "Différenciation des produits",
    "Économies d’échelle", "Demande représentative", "Écart technologique",
    "Cycle de vie du produit", "Termes de l’échange", "Croissance appauvrissante",
    "Dépendance commerciale",
], [
    "Pourquoi les pays échangent-ils ?",
    "Le commerce international est-il toujours un jeu à somme positive ?",
    "Tous les groupes sociaux bénéficient-ils du libre-échange ?",
    "Toutes les spécialisations se valent-elles ?",
    "Les avantages comparatifs sont-ils donnés ou construits ?",
    "Le commerce entre pays semblables remet-il en cause les théories traditionnelles ?",
])

ens(17, "La mondialisation et ses transformations historiques", [
    "Mondialisation", "Internationalisation", "Intégration économique",
    "Première mondialisation", "Hypermondialisation", "Ouverture commerciale",
    "Interdépendance", "Coûts de transport", "Migrations internationales",
    "Mobilité internationale du capital", "Fragmentation de la production",
    "Chaînes de valeur mondiales", "Dépendances stratégiques", "Démondialisation",
    "Fragmentation géoéconomique", "Relocalisation",
], [
    "La mondialisation actuelle est-elle sans précédent ?",
    "Qu’avons-nous retenu de la première mondialisation ?",
    "La mondialisation est-elle réversible ?",
    "L’interdépendance favorise-t-elle la paix ou la vulnérabilité ?",
    "Assiste-t-on à une démondialisation ou à une recomposition des échanges ?",
    "Faut-il réduire les dépendances internationales ?",
])

ens(18, "Les firmes multinationales et l’attractivité", [
    "Firme multinationale", "Investissement direct à l’étranger", "Délocalisation",
    "Sous-traitance internationale", "Stratégies horizontales et verticales",
    "Internalisation", "Attractivité territoriale", "Transferts de technologie",
    "Effets d’entraînement des IDE", "Concurrence fiscale", "Optimisation fiscale",
    "Prix de transfert", "Pouvoir des multinationales",
    "Rapports entre firmes et États",
], [
    "Pourquoi les entreprises s’internationalisent-elles ?",
    "Les multinationales favorisent-elles le développement des pays d’accueil ?",
    "Les délocalisations appauvrissent-elles les pays d’origine ?",
    "Les États contrôlent-ils encore les multinationales ?",
    "Faut-il attirer les IDE à tout prix ?",
    "L’attractivité d’un territoire repose-t-elle principalement sur ses coûts ?",
])

ens(19, "La compétitivité, l’industrie et la souveraineté économique", [
    "Compétitivité-prix", "Compétitivité-coût", "Compétitivité hors prix",
    "Productivité et coût salarial unitaire", "Montée en gamme",
    "Désindustrialisation", "Réindustrialisation", "Politique industrielle",
    "Industries stratégiques", "Champions nationaux", "Économies d’agglomération",
    "Clusters", "Subventions à la production", "Politique commerciale stratégique",
    "Souveraineté économique", "Autonomie stratégique",
], [
    "Qu’est-ce qu’une économie compétitive ?",
    "Un pays doit-il être géré comme une entreprise ?",
    "Réduire les salaires améliore-t-il nécessairement la compétitivité ?",
    "Peut-on prospérer sans industrie ?",
    "L’État peut-il choisir les secteurs d’avenir ?",
    "Comment concilier concurrence et politique industrielle ?",
    "La souveraineté économique suppose-t-elle l’autosuffisance ?",
])

ens(20, "Les changes et les déséquilibres internationaux", [
    "Balance des paiements", "Balance commerciale", "Solde courant",
    "Position extérieure nette", "Épargne et investissement en économie ouverte",
    "Capacité et besoin de financement extérieur",
    "Taux de change nominal et réel", "Appréciation et dépréciation",
    "Dévaluation et réévaluation", "Parité de pouvoir d’achat",
    "Parité des taux d’intérêt", "Condition de Marshall-Lerner", "Courbe en J",
    "Changes fixes et flottants", "Triangle d’incompatibilité", "Crise de change",
    "Déséquilibres mondiaux",
], [
    "Un déficit commercial signifie-t-il qu’un pays est peu compétitif ?",
    "Un excédent courant est-il toujours souhaitable ?",
    "Une dévaluation améliore-t-elle nécessairement les échanges extérieurs ?",
    "Une monnaie forte est-elle un avantage ?",
    "Les changes flottants stabilisent-ils l’économie mondiale ?",
    "Combien de temps un pays peut-il financer un déficit extérieur ?",
])

ens(21, "La régionalisation, l’Europe et la gouvernance mondiale", [
    "Régionalisation", "Accords commerciaux régionaux", "Zone de libre-échange",
    "Union douanière", "Marché commun", "Union économique et monétaire",
    "Création et détournement de commerce", "Multilatéralisme",
    "Gouvernance mondiale", "Coopération internationale", "Biens publics mondiaux",
    "OMC", "FMI", "Système monétaire international", "Étalon-or", "Bretton Woods",
    "Monnaie internationale", "Hégémonie du dollar", "Zone monétaire optimale",
    "Convergence européenne", "Chocs asymétriques",
    "Coordination des politiques économiques",
], [
    "La régionalisation favorise-t-elle la mondialisation ?",
    "Les accords régionaux renforcent-ils ou fragilisent-ils le multilatéralisme ?",
    "Pourquoi la coopération internationale est-elle difficile ?",
    "Peut-on réguler la mondialisation sans gouvernement mondial ?",
    "Une monnaie unique rapproche-t-elle nécessairement les économies ?",
    "L’union monétaire peut-elle fonctionner sans union budgétaire ?",
    "Une monnaie nationale peut-elle durablement servir de monnaie mondiale ?",
])

ens(22, "Les inégalités, la pauvreté et la justice sociale", [
    "Inégalités de revenus", "Inégalités de patrimoine", "Inégalités de chances",
    "Inégalités entre pays et au sein des pays", "Pauvreté absolue et relative",
    "Travailleurs pauvres", "Exclusion sociale", "Répartition primaire des revenus",
    "Partage de la valeur ajoutée", "Rente", "Héritage", "Courbe de Kuznets",
    "Justice sociale", "Égalité et équité", "Méritocratie", "Redistribution",
    "Fiscalité progressive", "Protection sociale", "État-providence",
    "Assurance et assistance", "Universalité et ciblage",
], [
    "La croissance réduit-elle les inégalités ?",
    "Les inégalités stimulent-elles l’activité économique ?",
    "Peut-on réduire la pauvreté sans réduire les inégalités ?",
    "La mondialisation réduit-elle ou accroît-elle les inégalités ?",
    "Faut-il rechercher l’égalité des chances ou l’égalité des situations ?",
    "La redistribution nuit-elle à l’efficacité économique ?",
    "L’héritage est-il compatible avec la méritocratie ?",
])

ens(23, "La structure sociale et la mobilité", [
    "Classes sociales", "Stratification sociale", "Catégories socioprofessionnelles",
    "Rapports de classe", "Conscience de classe", "Moyennisation",
    "Polarisation sociale", "Mobilité intergénérationnelle", "Mobilité structurelle",
    "Fluidité sociale", "Reproduction sociale",
    "Capital économique, culturel et social", "Habitus", "École et inégalités",
    "Déclassement", "Trajectoires sociales", "Inégalités de genre", "Discriminations",
], [
    "Les classes sociales existent-elles encore ?",
    "Les sociétés deviennent-elles plus ouvertes ?",
    "L’école réduit-elle ou reproduit-elle les inégalités ?",
    "La réussite dépend-elle seulement du mérite ?",
    "L’augmentation de la mobilité signifie-t-elle davantage d’égalité des chances ?",
    "Le déclassement est-il une expérience individuelle ou un phénomène collectif ?",
])

ens(24, "La socialisation, les liens sociaux et l’action collective", [
    "Socialisation primaire et secondaire", "Normes et valeurs", "Rôles et statuts",
    "Identité sociale", "Individualisation", "Individualisme",
    "Solidarité mécanique et organique", "Division du travail social", "Intégration",
    "Régulation sociale", "Anomie", "Déviance", "Contrôle social", "Désaffiliation",
    "Liens sociaux", "Conflits sociaux", "Action collective", "Syndicalisme",
    "Mobilisation", "Incitations sélectives",
], [
    "Comment la société façonne-t-elle les individus ?",
    "L’individualisation affaiblit-elle les liens sociaux ?",
    "La division du travail produit-elle toujours de la solidarité ?",
    "Les conflits menacent-ils ou renforcent-ils la cohésion sociale ?",
    "Pourquoi les individus se mobilisent-ils pour une cause collective ?",
    "Comment expliquer l’absence de mobilisation malgré des intérêts communs ?",
])

ens(25, "La démographie et les transformations des modes de vie", [
    "Transition démographique", "Croissance démographique", "Fécondité",
    "Vieillissement", "Dividende démographique", "Migrations", "Urbanisation",
    "Transformation de la famille", "Activité féminine", "Massification scolaire",
    "Mobilité géographique", "Protection sociale et vieillissement",
], [
    "La croissance démographique favorise-t-elle le développement ?",
    "Une population jeune constitue-t-elle toujours un atout ?",
    "Le vieillissement condamne-t-il la croissance ?",
    "Les migrations sont-elles une réponse aux déséquilibres démographiques ?",
    "Comment les transformations familiales modifient-elles les inégalités ?",
    "Comment financer la protection sociale dans une société vieillissante ?",
])

ens(26, "Les grands débats entre approches économiques et sociologiques", [
    "Marché et État", "Liberté et intervention", "Offre et demande",
    "Production et répartition", "Épargne et investissement",
    "Salaire : coût de production et revenu", "Monnaie neutre et monnaie active",
    "Équilibre et déséquilibre", "Autorégulation et instabilité",
    "Rationalité parfaite et rationalité limitée", "Individu et société",
    "Individualisme méthodologique et holisme", "Coopération et conflit",
    "Efficacité et justice", "Institutions et comportements",
    "Court terme et long terme", "Intérêts individuels et intérêt collectif",
], [
    "La poursuite des intérêts individuels conduit-elle à l’intérêt général ?",
    "Une économie peut-elle spontanément revenir à l’équilibre ?",
    "Ce qui est rationnel individuellement l’est-il collectivement ?",
    "Faut-il expliquer les comportements par les choix individuels ou par les structures sociales ?",
    "Une politique peut-elle être bénéfique à court terme et nuisible à long terme ?",
])

ens(27, "Les dossiers transversaux", [
    "Innovation", "Productivité", "Institutions", "Confiance", "Incertitude",
    "Pouvoir", "Rente", "Concurrence", "Coopération", "Dépendance", "Crise",
    "Inégalités", "Capital humain", "Industrialisation", "Ouverture", "Régulation",
    "Soutenabilité", "Répartition", "Transformation structurelle", "Souveraineté",
], [
    "Comment une même notion change-t-elle de sens selon le chapitre où elle apparaît ?",
    "Quels raisonnements peut-on transposer d’un chapitre à l’autre ?",
])

ens(28, "Le libre-échange, les protectionnismes et les stratégies commerciales", [
    "Libre-échange",
    "Arguments en faveur du libre-échange et conditions de validité",
    "Gains du commerce et répartition de ces gains",
    "Coûts de l’ouverture et ajustements économiques et sociaux",
    "Ouverture commerciale progressive et maîtrisée",
    "Protectionnisme",
    "Protectionnisme éducateur et industries naissantes",
    "Protectionnisme défensif",
    "Protectionnisme offensif",
    "Protection des industries vieillissantes ou en déclin",
    "Protectionnisme temporaire et protectionnisme permanent",
    "Protectionnisme sélectif et protectionnisme généralisé",
    "Protectionnisme tarifaire : droits de douane",
    "Protectionnisme non tarifaire : quotas, licences, normes et procédures administratives",
    "Subventions à la production et aux exportations",
    "Politique commerciale stratégique",
    "Protectionnisme agricole",
    "Protectionnisme environnemental",
    "Protectionnisme social",
    "Marchés publics et préférence nationale",
    "Exigences de contenu local",
    "Dumping et mesures antidumping",
    "Mesures de sauvegarde",
    "Réciprocité commerciale",
    "Représailles et guerres commerciales",
    "Détournement des échanges",
    "Coûts du protectionnisme pour les consommateurs et les entreprises utilisatrices de produits importés",
    "Recherche de rente et maintien artificiel d’activités inefficaces",
    "Protection commerciale, sécurité économique et souveraineté",
], [
    "Le libre-échange est-il toujours préférable au protectionnisme ?",
    "Dans quelles conditions le libre-échange profite-t-il à un pays ?",
    "Un gain global lié au commerce suffit-il à justifier l’ouverture ?",
    "Faut-il indemniser les perdants du libre-échange ?",
    "Le libre-échange entre économies de niveaux de développement différents est-il équitable ?",
    "Faut-il protéger une industrie avant de l’exposer à la concurrence internationale ?",
    "Le protectionnisme est-il toujours éducateur ?",
    "Quelles sont les conditions d’efficacité d’une protection temporaire ?",
    "Comment empêcher une protection temporaire de devenir permanente ?",
    "Le protectionnisme défensif préserve-t-il l’emploi ou retarde-t-il les reconversions ?",
    "Le protectionnisme offensif peut-il construire de nouveaux avantages comparatifs ?",
    "Protectionnisme offensif et défensif sont-ils toujours clairement séparables ?",
    "Faut-il protéger les industries naissantes ou les industries vieillissantes ?",
    "Les subventions peuvent-elles être plus efficaces que les droits de douane ?",
    "Les normes protègent-elles les consommateurs ou les producteurs nationaux ?",
    "Un pays peut-il améliorer sa situation par la protection sans dégrader celle de ses partenaires ?",
    "Pourquoi les représailles peuvent-elles annuler les bénéfices attendus du protectionnisme ?",
    "Peut-on protéger l’environnement sans créer de protectionnisme déguisé ?",
    "La souveraineté économique justifie-t-elle de limiter les échanges ?",
    "Libre-échange et intervention de l’État sont-ils compatibles ?",
])

TOTAL_DOSSIERS = sum(len(e['dossiers']) for e in ENSEMBLES)
TOTAL_QUESTIONS = sum(len(e['questions']) for e in ENSEMBLES)
