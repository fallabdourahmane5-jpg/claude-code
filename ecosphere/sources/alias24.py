# -*- coding: utf-8 -*-
"""Expressions de recherche propres à certains dossiers.

Le découpage automatique d'un libellé en mots-clés échoue sur les intitulés
longs ou composés : ces expressions-là sont écrites à la main. Elles servent
uniquement à mesurer la couverture par les cours, jamais à produire du contenu.
"""

ALIAS = {
 "Trappe à pauvreté": ["trappe a pauvrete", "piege a pauvrete", "cercle vicieux de la pauvrete"],
 "Malédiction des ressources naturelles": ["malediction des ressources", "maledic"],
 "Syndrome hollandais": ["syndrome hollandais", "dutch disease"],
 "Aide au développement": ["aide publique au developpement", "apd", "aide au developpement"],
 "Externalités environnementales": ["externalite", "pollution"],
 "Marchés de quotas d’émission": ["quotas d'emission", "marche carbone", "permis d'emettre", "quotas carbone"],
 "Discrimination par les prix": ["discrimination par les prix", "discrimination tarifaire"],
 "Marchés incomplets": ["marche incomplet", "marches incomplets"],
 "Capture du régulateur": ["capture du regulateur", "capture reglementaire"],
 "Filière inversée": ["filiere inversee", "galbraith"],
 "Biais comportementaux": ["biais", "economie comportementale", "kahneman"],
 "Financiarisation de l’entreprise": ["financiarisation"],
 "Motivation au travail": ["motivation"],
 "Autonomie au travail": ["autonomie"],
 "Flexibilité organisationnelle": ["flexibilite"],
 "Chômage frictionnel": ["chomage frictionnel", "frictionnel"],
 "Chômage de longue durée": ["chomage de longue duree", "longue duree"],
 "Hystérèse du chômage": ["hysterese", "hysteresis"],
 "Salaire d’efficience": ["salaire d'efficience", "salaire d efficience"],
 "Segmentation du marché du travail": ["segmentation", "marche du travail segmente", "dualisme du marche du travail"],
 "Insiders et outsiders": ["insider", "outsider"],
 "Polarisation des emplois": ["polarisation"],
 "Employabilité": ["employabilite"],
 "Politiques actives et passives de l’emploi": ["politique de l'emploi", "politiques de l'emploi", "politique active", "politique passive"],
 "Confiance monétaire": ["confiance"],
 "Monnaie bancaire": ["monnaie bancaire", "monnaie scripturale"],
 "Préférence pour la liquidité": ["preference pour la liquidite"],
 "Refinancement bancaire": ["refinancement"],
 "Intermédiation financière": ["intermediation", "intermediaire financier"],
 "Allocation de l’épargne": ["allocation de l'epargne", "orienter l'epargne", "drainer l'epargne"],
 "Efficience des marchés": ["efficience", "marches efficients", "fama"],
 "Mimétisme": ["mimetisme", "mimetique", "comportement moutonnier"],
 "Bulles financières": ["bulle"],
 "Crises de demande": ["crise de demande", "insuffisance de la demande", "sous-consommation"],
 "Accélérateur d’investissement": ["accelerateur"],
 "Cycle du crédit": ["cycle du credit", "credit cycle"],
 "Instabilité financière": ["instabilite financiere", "instabilite"],
 "Paradoxe de la tranquillité": ["paradoxe de la tranquillite", "minsky"],
 "Surendettement": ["surendettement", "endettement excessif"],
 "Déflation par la dette": ["deflation par la dette", "debt deflation", "fisher"],
 "Panique bancaire": ["panique bancaire", "run bancaire", "ruee vers les guichets"],
 "Contagion financière": ["contagion"],
 "Aléa moral des sauvetages": ["alea moral", "too big to fail", "sauvetage"],
 "Régulation macroprudentielle": ["macroprudentiel", "bale", "prudentiel"],
 "Inflation par la demande": ["inflation par la demande", "inflation de demande"],
 "Inflation par les coûts": ["inflation par les couts", "inflation importee"],
 "Boucle prix-salaires": ["boucle prix-salaires", "spirale prix-salaires", "indexation des salaires"],
 "Crédibilité monétaire": ["credibilite"],
 "Ancrage des anticipations": ["ancrage", "anticipations d'inflation"],
 "État minimal": ["etat minimal", "etat gendarme"],
 "État interventionniste": ["etat interventionniste", "interventionnisme", "etat providence"],
 "Fonctions d’allocation, de redistribution et de stabilisation": ["musgrave", "allocation", "redistribution", "stabilisation"],
 "Politique de rigueur": ["rigueur", "austerite", "consolidation budgetaire"],
 "Multiplicateur budgétaire": ["multiplicateur"],
 "Stabilisateurs automatiques": ["stabilisateur"],
 "Équivalence ricardienne": ["equivalence ricardienne", "barro"],
 "Modèles IS-LM et IS-LM-BP": ["is-lm", "mundell-fleming", "mundell fleming"],
 "Répartition des gains du commerce": ["repartition des gains", "gains a l'echange", "partage des gains"],
 "Égalisation des rémunérations factorielles": ["egalisation", "stolper-samuelson", "stolper samuelson", "remuneration des facteurs"],
 "Investissement direct à l’étranger": ["investissement direct", "ide a l'etranger", "idé"],
 "Sous-traitance internationale": ["sous-traitance", "externalisation internationale"],
 "Attractivité territoriale": ["attractivite"],
 "Effets d’entraînement des IDE": ["effet d'entrainement", "retombee", "transfert de technologie"],
 "Pouvoir des multinationales": ["pouvoir des firmes", "pouvoir de negociation des fmn", "firmes multinationales"],
 "Subventions à la production": ["subvention"],
 "Parité des taux d’intérêt": ["parite des taux", "parite non couverte", "parite couverte"],
 "Condition de Marshall-Lerner": ["marshall-lerner", "marshall lerner"],
 "Crise de change": ["crise de change", "attaque speculative"],
 "Étalon-or": ["etalon-or", "etalon or", "gold standard"],
 "Hégémonie du dollar": ["dollar", "privilege exorbitant"],
 "Zone monétaire optimale": ["zone monetaire optimale", "zmo"],
 "Convergence européenne": ["convergence", "criteres de convergence", "maastricht"],
 "Chocs asymétriques": ["choc asymetrique", "chocs asymetriques"],
 "Inégalités de chances": ["egalite des chances", "inegalite des chances"],
 "Travailleurs pauvres": ["travailleur pauvre", "travailleurs pauvres", "working poor"],
 "Exclusion sociale": ["exclusion"],
 "Répartition primaire des revenus": ["repartition primaire", "revenu primaire"],
 "Partage de la valeur ajoutee": ["partage de la valeur ajoutee"],
 "Partage de la valeur ajoutée": ["partage de la valeur ajoutee", "valeur ajoutee"],
 "Méritocratie": ["meritocratie", "merite"],
 "Stratification sociale": ["stratification", "hierarchie sociale"],
 "Rapports de classe": ["rapport de classe", "lutte des classes", "classes sociales"],
 "Conscience de classe": ["conscience de classe", "classe pour soi"],
 "Moyennisation": ["moyennisation", "classe moyenne"],
 "Mobilité intergénérationnelle": ["mobilite intergenerationnelle", "mobilite sociale"],
 "Mobilité structurelle": ["mobilite structurelle"],
 "Fluidité sociale": ["fluidite sociale", "fluidite"],
 "Habitus": ["habitus", "bourdieu"],
 "Trajectoires sociales": ["trajectoire"],
 "Déviance": ["deviance", "deviant"],
 "Incitations sélectives": ["incitation selective", "olson"],
 "Transformation de la famille": ["famille"],
 "Massification scolaire": ["massification", "scolarisation"],
 "Arguments en faveur du libre-échange et conditions de validité":
   ["libre-echange", "gains a l'echange", "avantage comparatif"],
 "Coûts de l’ouverture et ajustements économiques et sociaux":
   ["cout de l'ouverture", "perdants", "ajustement", "desindustrialisation"],
 "Ouverture commerciale progressive et maîtrisée":
   ["ouverture progressive", "liberalisation progressive", "ouverture maitrisee", "sequencage"],
 "Protection des industries vieillissantes ou en déclin":
   ["industries vieillissantes", "industrie vieillissante", "en declin", "secteur en declin"],
 "Protectionnisme temporaire et protectionnisme permanent":
   ["protection temporaire", "protection permanente", "temporaire"],
 "Protectionnisme sélectif et protectionnisme généralisé":
   ["protection selective", "selectif", "generalise"],
 "Protectionnisme tarifaire : droits de douane": ["droit de douane", "droits de douane", "tarifaire"],
 "Protectionnisme non tarifaire : quotas, licences, normes et procédures administratives":
   ["non tarifaire", "barriere non tarifaire", "quota", "norme", "licence"],
 "Subventions à la production et aux exportations": ["subvention", "subvention a l'exportation"],
 "Marchés publics et préférence nationale": ["marche public", "marches publics", "preference nationale", "buy american"],
 "Exigences de contenu local": ["contenu local", "local content"],
 "Dumping et mesures antidumping": ["dumping", "antidumping", "anti-dumping"],
 "Mesures de sauvegarde": ["sauvegarde", "clause de sauvegarde"],
 "Réciprocité commerciale": ["reciprocite"],
 "Représailles et guerres commerciales": ["represaille", "guerre commerciale", "retorsion"],
 "Détournement des échanges": ["detournement de trafic", "detournement de commerce", "detournement des echanges"],
 "Coûts du protectionnisme pour les consommateurs et les entreprises utilisatrices de produits importés":
   ["cout du protectionnisme", "consommateur", "consommation intermediaire", "intrant"],
 "Recherche de rente et maintien artificiel d’activités inefficaces":
   ["recherche de rente", "rent seeking", "rente"],
 "Protection commerciale, sécurité économique et souveraineté":
   ["securite economique", "souverainete", "securite nationale"],
}

ALIAS.update({
 "Gains du commerce et répartition de ces gains":
   ["gains a l'echange", "gain a l'echange", "repartition des gains", "surplus", "perdants"],
 "Protectionnisme défensif":
   ["defensif", "kaldor", "industrie vieillissante", "industries vieillissantes",
    "canard boiteux", "canards boiteux", "secteur en declin"],
 "Protectionnisme offensif":
   ["offensif", "brander", "spencer", "politique commerciale strategique",
    "champion national", "champions nationaux"],
 "Politique commerciale stratégique":
   ["brander", "spencer", "politique commerciale strategique", "oligopole",
    "champion national", "subvention a la recherche"],
 "Protectionnisme agricole":
   ["agricole", "agriculture", "politique agricole commune", "cairns", "arachide"],
 "Protectionnisme environnemental":
   ["macf", "mecanisme d'ajustement carbone", "fuite de carbone", "prix du carbone",
    "protectionnisme vert", "transition ecologique"],
 "Protectionnisme social":
   ["norme sociale", "normes sociales", "dumping social", "droit du travail",
    "clause sociale", "conditions de travail"],
 "Ouverture commerciale progressive et maîtrisée":
   ["ouverture progressive", "liberalisation progressive", "sequencage",
    "stade de developpement", "ouverture maitrisee", "progressivement"],
 "Marchés publics et préférence nationale":
   ["marche public", "marches publics", "preference nationale", "buy american",
    "commande publique", "achat public"],
 "Détournement des échanges":
   ["detournement de trafic", "detournement de commerce", "detournement des echanges",
    "reorientation des echanges", "friendshoring"],
 "Protection commerciale, sécurité économique et souveraineté":
   ["securite economique", "souverainete", "securite nationale", "dependance strategique",
    "autonomie strategique"],
 "Coûts du protectionnisme pour les consommateurs et les entreprises utilisatrices de produits importés":
   ["cout du protectionnisme", "prix a la consommation", "consommation intermediaire",
    "intrant", "pouvoir d'achat", "surplus du consommateur"],
})

ALIAS.update({
 "Syndrome hollandais":
   ["syndrome hollandais", "dutch disease", "maladie hollandaise"],
 "Dépendance économique":
   ["dependance economique", "dependance exterieure", "dependance commerciale",
    "theorie de la dependance", "dependantiste", "echange inegal",
    "insertion subordonnee"],
 "Aide au développement":
   ["aide au developpement", "aide publique au developpement", "aide financiere",
    "annulation de la dette", "allegement", "reechelonnement", "ppte"],
 "Ajustement structurel":
   ["ajustement structurel", "plan d'ajustement structurel",
    "plans d'ajustement structurel", "conditionnalite"],
 "Consensus de Washington":
   ["consensus de washington", "williamson", "neoliberale",
    "dereglementation"],
})

ALIAS["Malédiction des ressources naturelles"] = [
    "malediction des ressources", "paradoxe de l'abondance",
    "economie de rente", "ressources naturelles", "matieres premieres",
    "institutions extractives"]

ALIAS["Malédiction des ressources naturelles"] = [
    "malediction des ressources", "paradoxe de l'abondance",
    "economie de rente", "institutions extractives"]
ALIAS["Consensus de Washington"] = [
    "consensus de washington", "williamson", "neoliberal"]

ALIAS["Consensus de Washington"] = [
    "consensus de washington", "williamson", "plan d'ajustement structurel",
    "plans d'ajustement structurel"]

ALIAS["Consensus de Washington"] = [
    "consensus de washington", "john williamson",
    "plan d'ajustement structurel", "plans d'ajustement structurel"]

ALIAS.update({
 "Discrimination par les prix":
   ["monopole discriminant", "tarification differentielle",
    "yield management", "tarification differenciee", "elasticite-prix"],
 "Coordination par les prix":
   ["coordination par les prix", "signal-prix", "systeme de prix",
    "prix d'equilibre", "main invisible"],
 "Équilibre de marché":
   ["equilibre de marche", "prix d'equilibre", "offre et demande",
    "equilibre partiel"],
 "Optimum de Pareto":
   ["optimum de pareto", "pareto", "efficacite allocative",
    "optimum collectif"],
 "Politique de la concurrence":
   ["politique de la concurrence", "politique de concurrence",
    "autorite de la concurrence", "droit de la concurrence",
    "sherman act", "antitrust"],
 "Concentration économique":
   ["concentration economique", "concentration horizontale",
    "concentration verticale", "fusion", "concentration conglomerale"],
 "Efficacité économique":
   ["efficacite economique", "efficacite allocative",
    "allocation optimale", "optimum collectif"],
})

ALIAS.update({
 "Marchés incomplets":
   ["marches complets", "marche incomplet", "marches incomplets",
    "arrow-debreu", "marche a terme"],
 "Capture du régulateur":
   ["capturees par des interets prives", "capture", "lobbying",
    "groupes organises", "public choice"],
 "Défaillances de coordination":
   ["defaillance de coordination", "defaillances de coordination",
    "probleme de coordination", "dilemme du prisonnier",
    "equilibre de nash"],
 "Recherche de rente":
   ["recherche de rente", "chercheurs de rente", "rent seeking",
    "lobbying", "public choice"],
 "Défaillances de l’État":
   ["defaillance de l'etat", "defaillances de l'etat", "public choice",
    "choix publics", "buchanan", "tullock"],
 "Choix publics":
   ["choix publics", "public choice", "buchanan", "tullock", "stigler",
    "marche politique"],
 "Bureaucratie":
   ["bureaucratie", "bureaucratique", "weber", "organisation",
    "hauts fonctionnaires"],
})

ALIAS.update({
 "Filière inversée": ["filiere inversee"],
 "Contrainte budgétaire":
   ["contrainte budgetaire", "droite de budget", "droite budgetaire",
    "ensemble budgetaire", "revenu et prix"],
 "Choix du consommateur":
   ["choix du consommateur", "panier optimal", "courbe d'indifference",
    "tms", "maximisation de l'utilite"],
 "Élasticités":
   ["elasticite", "elasticites", "elasticite-prix", "elasticite-revenu",
    "elasticite croisee"],
 "Effets d’imitation et de distinction":
   ["imitation", "emulation sociale", "distinction", "veblen",
    "consommation ostentatoire", "effet de mode"],
 "Propension à consommer":
   ["propension a consommer", "propension marginale", "propension moyenne",
    "multiplicateur"],
})

# ensembles 8 à 10 : libellés trop larges ou trop pauvres pour le découpage
# automatique. Les expressions restent celles qu'emploient les cours.
ALIAS.update({
 "Entreprise":
   ["theories de la firme", "nœud de contrats", "nature de la firme",
    "l'entreprise comme", "qu'est-ce qu'une entreprise",
    "la firme est", "firme et marche", "approche contractuelle",
    "approche transactionnelle"],
 "Entrepreneur":
   ["entrepreneur", "entrepreneuriat", "esprit d'entreprise",
    "proprietaire-dirigeant"],
 "Profit":
   ["profit", "taux de marge", "creancier residuel", "maximiser le profit"],
 "Risque et incertitude":
   ["incertitude", "prise de risque", "preneur de risque",
    "responsabilite illimitee", "probabilisable", "avenir incertain",
    "aversion au risque"],
 "Frontières de la firme":
   ["frontieres de la firme", "faire ou faire faire", "internaliser",
    "internalisation", "taille de l'entreprise", "firme et marche"],
 "Relation d’agence":
   ["relation d'agence", "relations d'agence", "theorie de l'agence",
    "couts d'agence", "divergence d'interets"],
 "Séparation entre propriété et contrôle":
   ["separation propriete", "propriete et controle", "propriete / controle",
    "berle", "means", "technostructure", "capitalisme managerial"],
 "Gouvernance d’entreprise":
   ["gouvernance d'entreprise", "corporate governance",
    "conseil d'administration", "stock-options"],
 "Valeur actionnariale":
   ["valeur actionnariale", "shareholder", "creation de valeur",
    "rentabilite financiere"],
 "Parties prenantes":
   ["parties prenantes", "stakeholder", "polanyi"],
 "Responsabilité sociale des entreprises":
   ["responsabilite sociale", "loi pacte", "raison d'etre",
    "entreprise a mission", "greenwashing"],
 "Concentration et croissance des entreprises":
   ["concentration des entreprises", "concentration horizontale",
    "concentration verticale", "concentration conglomerale",
    "croissance interne", "croissance externe", "conglomerat"],
 "Intégration verticale":
   ["integration verticale", "concentration verticale",
    "filiere de production"],
 "Externalisation":
   ["externalisation", "externaliser", "sous-traitance", "firme-reseau",
    "firmes-reseaux"],
 "Organisation scientifique du travail":
   ["organisation scientifique du travail", "organisation scientifique",
    "one best way", "chronometrage", "parcellisation",
    "division verticale", "division horizontale", "flanerie systematique"],
 "École des relations humaines":
   ["relations humaines", "mayo", "hawthorne", "western electric",
    "test room", "effet d'observation"],
 "Coopération":
   ["cooperation conflictuelle", "lieu de cooperation", "travail en equipe",
    "equipes semi autonomes", "esprit de groupe", "cohesion du groupe"],
 "Autorité et pouvoir":
   ["autorite", "domination legale", "domination charismatique",
    "domination traditionnelle", "source de pouvoir", "sources de pouvoir",
    "rapports de pouvoir", "relation de subordination", "charisme"],
 "Acteur stratégique":
   ["acteur strategique", "analyse strategique", "marge de manœuvre",
    "marges de manœuvre", "marginal secant", "crozier"],
 "Culture d’entreprise":
   ["culture d'entreprise", "normes informelles", "norme informelle",
    "monde informel", "organisation informelle", "relations informelles",
    "sociogramme", "routines"],
 "Contrôle du travail":
   ["controle du travail", "contremaitre", "instrument de controle",
    "dispositifs de surveillance", "controle des performances",
    "subordination"],
 "Souffrance et sens du travail":
   ["travail en miettes", "alienation", "perte de sens", "sens du travail",
    "souffrance", "penibilite", "monotonie", "intensification du travail"],
 "Travail et emploi":
   ["travail et emploi", "salarisation", "condition salariale",
    "societe salariale", "travail integrateur", "desaffiliation",
    "halo du chomage", "facteur d'integration"],
 "Marché du travail":
   ["marche du travail", "offre de travail", "demande de travail",
    "contrat de travail"],
 "Chômage conjoncturel et structurel":
   ["chomage conjoncturel", "chomage structurel", "chomage durable",
    "chomage de masse", "taux de chomage naturel", "chomage naturel"],
 "Chômage classique et keynésien":
   ["chomage keynesien", "chomage classique", "chomage involontaire",
    "equilibre de sous-emploi", "demande effective", "malinvaud",
    "theorie du desequilibre"],
 "Chômage frictionnel": ["chomage frictionnel"],
 "Chômage de longue durée": ["chomage de longue duree"],
 "Appariement":
   ["appariement sur le marche du travail", "fonction d'appariement",
    "courbe de beveridge"],
 "Salaire minimum":
   ["salaire minimum", "smic", "prix plancher", "trappe a bas salaires",
    "allegements de cotisations"],
 "Précarité":
   ["precarite", "precarisation", "emplois precaires", "pauvrete laborieuse",
    "temps partiel subi", "contrats courts", "uberisation"],
 "Progrès technique biaisé":
   ["progres technique biaise", "biaise en faveur", "biais technologique",
    "demande de travail qualifie", "taches routinieres"],
 "Politiques actives et passives de l’emploi":
   ["politique active de l'emploi", "politiques actives de l'emploi",
    "politique passive de l'emploi", "traitement social du chomage"],
})

# ensembles 11 à 13 : libellés trop larges, trop pauvres, ou dont le terme
# canonique est absent des cours. Les expressions restent celles des cours.
ALIAS.update({
 "Fonctions de la monnaie":
   ["fonctions de la monnaie", "unite de compte", "intermediaire des echanges",
    "reserve de valeur", "pouvoir liberateur", "monnaie de libelle",
    "monnaie vehiculaire", "monnaie de reserve"],
 "Confiance monétaire":
   ["confiance", "fiducia", "pouvoir liberateur", "monnaie fiduciaire"],
 "Création monétaire":
   ["creation monetaire", "les credits font les depots",
    "monetisation d'une creance", "contreparties a la masse monetaire"],
 "Banques commerciales":
   ["banque commerciale", "banques commerciales", "banque de second rang",
    "banque universelle", "banques universelles", "banque de depot",
    "banques de depots"],
 "Banque centrale":
   ["banque centrale", "bce", "eurosysteme", "taux directeur",
    "taux directeurs"],
 "Liquidité":
   ["liquidite", "actif liquide", "trappe a liquidite"],
 "Taux d’intérêt nominal et réel":
   ["taux d'interet nominal et reel", "taux d'interet reel",
    "taux nominal et taux reel"],
 "Préférence pour la liquidité":
   ["preference pour la liquidite", "prix du renoncement", "thesauriser",
    "thesaurisation", "trappe a liquidite", "garder la monnaie"],
 "Multiplicateur et diviseur de crédit":
   ["multiplicateur de credit", "multiplicateur bancaire",
    "diviseur de credit", "diviseur monetaire", "base monetaire",
    "monnaie centrale", "reserves obligatoires"],
 "Prêteur en dernier ressort":
   ["preteur en dernier ressort", "paniques de liquidite",
    "liquidite du systeme bancaire"],
 "Indépendance de la banque centrale":
   ["independance de la banque centrale", "independance de la bc",
    "monetisation de la dette", "helicoptere monetaire",
    "theorie monetaire moderne"],
 "Neutralité de la monnaie":
   ["neutralite de la monnaie", "monnaie est neutre", "monnaie n'est qu'un voile",
    "monnaie voile", "la monnaie est un voile"],
 "Monnaie et activité économique":
   ["monnaie est endogene", "monnaie endogene", "monnaie exogene",
    "canal des taux", "canaux de transmission", "politique monetaire",
    "sphere monetaire", "sphere reel"],
 "Besoin et capacité de financement":
   ["besoin de financement", "capacite de financement",
    "agents a besoin de financement", "agents a capacite de financement"],
 "Financement direct et indirect":
   ["financement direct", "financement indirect", "financement intermedie",
    "economie d'endettement", "economie de marches financiers",
    "intermediation de marche"],
 "Désintermédiation":
   ["desintermediation", "trois d", "3d", "regle des 3d"],
 "Actions et obligations":
   ["titre de propriete", "titre de creance", "obligataire", "coupon",
    "dividende", "valeurs mobilieres", "emission de titres",
    "marche obligataire", "marche actions"],
 "Marchés financiers":
   ["marche financier", "marches financiers", "marche au comptant",
    "marche a terme", "marche de gre a gre", "bourse", "euronext",
    "marche monetaire"],
 "Allocation de l’épargne":
   ["allocation de l'epargne", "offreurs et demandeurs de capitaux",
    "capital est mal distribue", "projets les plus productifs",
    "allocation du capital", "drainer l'epargne"],
 "Diversification du risque":
   ["diversification du risque", "diversifier les placements",
    "portefeuille diversifie", "couvrir des risques", "couverture contre le risque"],
 "Efficience des marchés":
   ["parfaitement efficace", "information de prix", "opacite",
    "capital est mal distribue", "fournir une information"],
 "Spéculation":
   ["speculation", "speculer", "speculatif", "vente a decouvert",
    "parier sur la baisse"],
 "Bulles financières":
   ["bulle", "krach", "effondrement du cours", "compagnie du mississippi"],
 "Financiarisation":
   ["financiarisation", "globalisation financiere", "shadow banking",
    "titrisation", "produits derives"],
 "Finance et croissance":
   ["financement de l'economie", "finance et croissance",
    "financement de l'investissement", "soutien au credit",
    "capacite de financement de l'economie"],
 "Régulation financière":
   ["regulation financiere", "regles prudentielles", "prudentiel",
    "dereglementation", "too big to fail", "separer les activites",
    "loi bancaire", "surveillance des marches"],
 "Cycles économiques":
   ["cycles economiques", "cycle court", "cycle moyen", "cycle long",
    "juglar", "kitchin", "kondratiev", "grappes d'innovations",
    "phase ascendante", "phase descendante"],
 "Crises de surproduction":
   ["surproduction", "sous-consommation", "demande effective",
    "regulation concurrentielle", "crise de 1929"],
 "Crises de demande":
   ["crise de demande", "insuffisance de la demande", "sous-consommation",
    "demande effective"],
 "Chocs d’offre et de demande":
   ["choc petrolier", "choc de demande", "choc d'offre", "choc asymetrique",
    "choc externe", "stagflation"],
 "Accélérateur d’investissement":
   ["accelerateur", "aftalion", "variation de l'investissement",
    "variation demande"],
 "Cycle du crédit":
   ["cycle du credit", "fluctuations du credit", "emballements speculatifs",
    "blocage du credit", "canal du credit", "surinvestissement"],
 "Instabilité financière":
   ["instabilite financiere", "risque systemique", "crise financiere",
    "titrisation", "shadow banking", "crise de 2008"],
 "Paradoxe de la tranquillité": ["paradoxe de la tranquillite", "minsky"],
 "Surendettement": ["surendettement", "endettement excessif"],
 "Déflation par la dette": ["deflation par la dette", "debt deflation"],
 "Crise bancaire":
   ["crise bancaire", "faillites systemiques", "faillite d'une grande banque",
    "crise des banques", "banque n'a plus de reserves", "risque de liquidite"],
 "Panique bancaire":
   ["panique", "paniques de liquidite", "ruee", "echanger leurs billets"],
 "Risque systémique":
   ["risque systemique", "effet de contagion", "faillites systemiques",
    "too big to fail"],
 "Contagion financière":
   ["contagion", "diffusion mondiale du risque", "se propage",
    "chaine de pertes"],
 "Aléa moral des sauvetages":
   ["alea moral", "too big to fail", "socialisation des pertes",
    "implicitement proteges"],
 "Régulation macroprudentielle":
   ["regulation macroprudentielle", "macroprudentiel", "coussin contracyclique"],
})

# ---- ensemble 14 : l'inflation et la stabilité des prix ----
ALIAS.update({
 "Inflation":
   ["inflation", "niveau general des prix", "indice des prix a la consommation",
    "inflation sous-jacente"],
 "Désinflation":
   ["desinflation", "baisse de l'inflation", "volcker",
    "politique monetaire restrictive"],
 "Déflation":
   ["deflation", "eviter la deflation", "lutte contre la deflation"],
 "Hyperinflation":
   ["hyperinflation", "hyper inflation", "inflation a 2 chiffres"],
 "Inflation par la demande":
   ["inflation par la demande", "la demande augmente + vite que l'offre",
    "tension inflationniste", "surchauffe"],
 "Inflation par les coûts":
   ["inflation par les couts", "hausse des couts", "choc petrolier",
    "stagflation"],
 "Inflation importée":
   ["inflation importee", "importations plus cheres", "spirale inflationniste"],
 "Boucle prix-salaires":
   ["boucle prix-salaires", "hausses de salaires", "salaires nominaux",
    "indexation des salaires"],
 "Anticipations d’inflation":
   ["anticipations d'inflation", "anticipations adaptatives",
    "anticipations rationnelles", "illusion monetaire"],
 "Courbe de Phillips":
   ["courbe de phillips", "phillips", "nairu", "nawru", "chomage naturel"],
 "Stagflation":
   ["stagflation", "choc petrolier", "inflation et chomage"],
 "Pouvoir d’achat":
   ["pouvoir d'achat", "revenu reel", "effet d'encaisse", "effet pigou",
    "fuite devant la monnaie"],
 "Crédibilité monétaire":
   ["credibilite", "regle de k", "regles simples"],
 "Ancrage des anticipations":
   ["ancrer les anticipations", "anticipations d'inflation",
    "forward guidance", "canal des anticipations"],
})

# ---- ensemble 15 : l'Etat et les politiques economiques ----
ALIAS.update({
 "État minimal":
   ["main invisible", "absence de politique economique",
    "laisser faire le marche", "non seulement inutile", "liberalisme"],
 "État interventionniste":
   ["etat providence", "etat-providence", "interventionnisme",
    "role stabilisateur", "carre magique"],
 "Fonctions d’allocation, de redistribution et de stabilisation":
   ["musgrave", "fonction d'allocation", "fonction de stabilisation",
    "fonction de redistribution", "finances publiques"],
 "Politique budgétaire":
   ["politique budgetaire", "politiques budgetaires", "depenses publiques",
    "policy mix"],
 "Politique monétaire":
   ["politique monetaire", "taux directeurs", "banque centrale europeenne"],
 "Politique de relance":
   ["politique de relance", "politiques de relance", "relance budgetaire",
    "plan biden"],
 "Politique de rigueur":
   ["politique de rigueur", "politiques de rigueur", "austerite",
    "freiner demande"],
 "Multiplicateur budgétaire":
   ["multiplicateur", "hausse des depenses publiques", "propension a consommer"],
 "Stabilisateurs automatiques":
   ["allocations chomage", "prestations sociales", "recettes de l'etat",
    "role stabilisateur"],
 "Effet d’éviction":
   ["effet d'eviction", "eviction du capital prive"],
 "Équivalence ricardienne":
   ["equivalence ricardienne"],
 "Déficit public":
   ["deficit public", "deficits publics", "emission d'obligations"],
 "Dette publique":
   ["dette publique", "dette souveraine", "charge de la dette"],
 "Soutenabilité de la dette":
   ["soutenabilite de la dette", "dette soutenable", "spirale de la dette",
    "insoutenable"],
 "Policy mix":
   ["policy mix", "politique monetaire ou budgetaire",
    "politiques conjoncturelles"],
 "Règles et discrétion":
   ["politiques discretionnaires", "discretionnaire", "regles simples",
    "regle de k", "absence de politique economique"],
 "Anticipations":
   ["anticipations adaptatives", "anticipations rationnelles",
    "illusion monetaire", "canal des anticipations"],
 "Contrainte extérieure":
   ["contrainte exterieure", "triangle de mundell", "autonomie strategique"],
 "Modèles IS-LM et IS-LM-BP":
   ["is-lm", "triangle de mundell", "courbe is", "courbe lm"],
 "Trappe à liquidité":
   ["trappe a liquidite", "helicoptere monetaire", "taux negatifs"],
})

# ---- ensembles 16 et 17 : commerce international et mondialisation ----
ALIAS.update({
 "Avantages absolus": ["avantage absolu", "avantages absolus"],
 "Demande représentative": ["demande representative", "linder"],
 "Écart technologique": ["ecart technologique", "posner"],
 "Dépendance commerciale":
   ["dependance commerciale", "dependance du centre", "montesquieu",
    "doux commerce"],
 "Mobilité internationale du capital":
   ["mobilite internationale du capital", "mobilite des capitaux",
    "libre circulation des capitaux", "flux de capitaux"],
 "Fragmentation de la production":
   ["fragmentation de la production", "fragmentation internationale",
    "chaines de valeur"],
 "Dépendances stratégiques":
   ["dependances strategiques", "dependance strategique",
    "autonomie strategique"],
 "Migrations internationales": ["migrations internationales", "migratoires"],
 "Intégration économique": ["integration economique", "balassa"],
})

# — Ensembles 18 à 20 : resserrage des libellés trop larges —
ALIAS.update({
 "Investissement direct à l’étranger":
   ["investissement direct", "investissements directs", "ide a l'etranger"],
 "Rapports entre firmes et États":
   ["fmn et etats", "rapport entre fmn", "filtrage des ide",
    "concurrence entre territoires"],
 "Firme multinationale": ["firme multinationale", "firmes multinationales"],
 "Stratégies horizontales et verticales":
   ["strategie horizontale", "strategie verticale", "integration verticale",
    "concentration verticale"],
 "Internalisation": ["internalisation"],
 "Transferts de technologie":
   ["transfert de technologie", "transferts de technologie"],
 "Effets d’entraînement des IDE":
   ["effets d'entrainement", "effet d'entrainement", "retombee"],
 "Concurrence fiscale": ["concurrence fiscale", "moins-disant fiscal"],
 "Optimisation fiscale": ["optimisation fiscale"],
 "Prix de transfert": ["prix de transfert"],
 "Pouvoir des multinationales":
   ["pouvoir des firmes", "pouvoir de negociation", "firme multinationale"],
 # — ensemble 19 —
 "Compétitivité-prix": ["competitivite-prix"],
 "Compétitivité-coût": ["competitivite-cout"],
 "Compétitivité hors prix": ["competitivite hors prix", "hors-prix"],
 "Productivité et coût salarial unitaire":
   ["cout salarial unitaire", "cout unitaire du travail"],
 "Montée en gamme": ["montee en gamme"],
 "Industries stratégiques":
   ["industries strategiques", "secteurs strategiques"],
 "Champions nationaux": ["champions nationaux", "champion national"],
 "Économies d’agglomération": ["agglomeration"],
 "Clusters": ["cluster"],
 "Souveraineté économique": ["souverainete economique"],
 "Autonomie stratégique": ["autonomie strategique"],
 # — ensemble 20 —
 "Balance des paiements": ["balance des paiements"],
 "Balance commerciale": ["balance commerciale"],
 "Solde courant": ["solde courant", "deficit courant", "excedent courant"],
 "Position extérieure nette": ["position exterieure"],
 "Épargne et investissement en économie ouverte":
   ["epargne nationale", "epargne et investissement", "epargne interieure"],
 "Capacité et besoin de financement extérieur":
   ["capacite de financement", "besoin de financement"],
 "Taux de change nominal et réel":
   ["taux de change", "cours d'une monnaie", "marche des changes"],
 "Appréciation et dépréciation": ["appreciation", "depreciation"],
 "Dévaluation et réévaluation": ["devaluation", "reevaluation"],
 "Parité de pouvoir d’achat":
   ["parite de pouvoir d'achat", "parite de pouvoir", "en ppa"],
 "Courbe en J": ["courbe en j"],
 "Changes fixes et flottants":
   ["change fixe", "change flottant", "regime de change"],
 "Triangle d’incompatibilité":
   ["triangle d'incompatibilite", "triangle de mundell"],
 "Crise de change":
   ["sudden stop", "dette en devises", "reserves de change"],
 "Déséquilibres mondiaux": ["desequilibres mondiaux"],
})

# — Ensembles 21 et 22 —
ALIAS.update({
 "Régionalisation": ["regionalisation", "regionalise"],
 "Accords commerciaux régionaux":
   ["accords commerciaux regionaux", "accord commercial regional", "acr "],
 "Zone de libre-échange": ["zone de libre-echange", "zlecaf", "asean"],
 "Union douanière": ["union douaniere", "viner"],
 "Marché commun": ["marche commun", "balassa"],
 "Union économique et monétaire":
   ["union economique et monetaire", "zone euro", "monnaie unique"],
 "Création et détournement de commerce":
   ["creation de trafic", "detournement de trafic",
    "detournement de commerce"],
 "Multilatéralisme": ["multilateralisme"],
 "Gouvernance mondiale": ["gouvernance mondiale"],
 "Coopération internationale":
   ["cooperation internationale", "stabilite hegemonique", "kindleberger"],
 "Biens publics mondiaux": ["biens publics mondiaux", "bien public mondial"],
 "OMC": ["omc", "organisation mondiale du commerce"],
 "FMI": ["fmi", "fonds monetaire international"],
 "Système monétaire international": ["systeme monetaire international"],
 "Bretton Woods": ["bretton woods"],
 "Monnaie internationale": ["monnaie internationale", "monnaie d'ancrage",
                            "monnaie de reserve"],
 "Hégémonie du dollar": ["privilege exorbitant", "role international du dollar",
                         "hegemonie"],
 "Convergence européenne": ["convergence", "zone euro"],
 "Chocs asymétriques": ["choc asymetrique", "chocs asymetriques"],
 "Coordination des politiques économiques":
   ["coordination des politiques", "coordination economique",
    "coordination fiscale"],
 # — ensemble 22 —
 "Inégalités de revenus": ["inegalites de revenu", "inegalite des revenus"],
 "Inégalités de patrimoine": ["inegalites de patrimoine", "patrimoine"],
 "Inégalités entre pays et au sein des pays":
   ["inegalites entre pays", "inegalites au sein des pays",
    "courbe de l'elephant"],
 "Pauvreté absolue et relative":
   ["pauvrete absolue", "pauvrete monetaire", "seuil de pauvrete"],
 "Travailleurs pauvres":
   ["travailleurs pauvres", "travail ne garantit", "sortie de la pauvrete"],
 "Exclusion sociale":
   ["exclusion sociale", "desaffiliation", "question sociale"],
 "Répartition primaire des revenus":
   ["revenu primaire", "revenus primaires", "repartition des revenus"],
 "Partage de la valeur ajoutee": ["taux de marge", "partage de la va"],
 "Partage de la valeur ajoutée":
   ["taux de marge", "part de la va", "excedent brut d'exploitation"],
 "Rente": ["rente de monopole", "rente fonciere", "recherche de rente",
           "captation de rente"],
 "Héritage": ["heritage"],
 "Courbe de Kuznets": ["courbe de kuznets", "kuznets"],
 "Justice sociale": ["justice sociale", "injustice sociale"],
 "Égalité et équité": ["equite", "egalite des revenus"],
 "Redistribution": ["redistribution", "redistribue"],
 "Fiscalité progressive": ["fiscalite progressive", "progressivite"],
 "Protection sociale": ["protection sociale"],
 "État-providence": ["etat-providence", "etat providence"],
})

ALIAS.update({
    'Travailleurs pauvres': ['pauvrete laborieuse', 'travailleurs pauvres',
                             'travail ne garantit', 'temps partiel subi'],
    'Héritage': ['heritage', 'donation', 'transmission intergenerationnelle'],
    'Fiscalité progressive': ['fiscalite progressive', 'impot progressif',
                              'progressivite', 'quotient familial'],
    'Justice sociale': ['justice sociale', 'injustice sociale',
                        'justice fiscale', 'impot juste'],
})

ALIAS.update({
    'Héritage': ['par heritage', 'retour de l\'heritage', 'donation',
                 'transmission intergenerationnelle', 'plus-values latentes',
                 'holding familial', 'abolir l\'heritage'],
})

# Ensembles 23 à 25. Les expressions sont choisies une par une : chacune doit
# désigner la notion visée et non un homonyme (« régulation » seul renvoie à la
# régulation des marchés, « organique » à la composition organique du capital).
ALIAS.update({
    # 23 — structure sociale
    'Classes sociales': ['classes sociales', 'lutte des classes',
                         'classe de loisir', 'classe productive',
                         'classe sterile', 'bourgeoisie', 'proletariat'],
    'Catégories socioprofessionnelles':
        ['categorie socioprofessionnelle', 'categories socioprofessionnelles',
         'cadres superieurs', 'desindustrialisation',
         'population active'],
    'Rapports de classe': ['lutte des classes', 'plus-value',
                           'exploitation du travail', 'capital constant',
                           'capital variable', 'taux de plus-value'],
    'Conscience de classe': ['identite ouvriere', 'appartenir a une classe',
                             'identite collective', 'monde ouvrier',
                             'conscience de leur exploitation',
                             'taux de syndicalisation'],
    'Moyennisation': ['classe moyenne', 'classes moyennes',
                      'courbe de kuznets', 'u inverse'],
    'Polarisation sociale': ['polarisation', 'coefficient de palma',
                             'courbe du sourire', 'top 1 %'],
    'Reproduction sociale': ['reproduction sociale', 'logique cumulative',
                             'par heritage', 'donation', 'pacte dutreil',
                             'inegalites se reproduisent'],
    'Déclassement': ['declassement', 'inferieur a son niveau de qualification',
                     'valeur des diplomes'],
    'Inégalités de genre': ['inegalites de genre', 'inegalite de genre',
                            'femmes-hommes', 'education des filles',
                            'ecart moyen en equivalent temps plein',
                            'autonomisation'],
    'Discriminations': ['discrimination', 'discriminations',
                        'traitement national', 'non-discrimination'],
    # 24 — socialisation, liens sociaux, action collective
    'Rôles et statuts': ['statut social', 'role social',
                         'domination legale', 'ideal-type',
                         'activite sociale'],
    'Identité sociale': ['identite ouvriere', 'identite collective',
                         'conscience collective', 'appartenance',
                         'reconnaissance sociale'],
    'Individualisme': ['individualisme', 'individualisme methodologique',
                       'paradoxe d\'olson', 'passager clandestin'],
    'Individualisation': ['individualisation', 'autonomie individuelle',
                          'conscience individuelle', 'plus individuel'],
    'Solidarité mécanique et organique':
        ['solidarite mecanique', 'solidarite organique',
         'conscience collective', 'societes segmentaires',
         'societes organisees'],
    'Division du travail social': ['division du travail social',
                                   'de la division du travail',
                                   'solidarite organique', 'corporation'],
    'Régulation sociale': ['regulation sociale', 'defaut de regulation',
                           'passion de l\'infini', 'borner les desirs',
                           'esprit de discipline'],
    'Anomie': ['anomie', 'anomique', 'passion de l\'infini',
               'defaut de regulation'],
    'Contrôle social': ['controle social', 'esprit de discipline',
                        'contrainte morale', 'conformisme',
                        'pouvoir de coercition'],
    'Désaffiliation': ['desaffiliation', 'question sociale',
                       'societe salariale', 'metamorphoses de la question'],
    'Liens sociaux': ['lien social', 'liens sociaux', 'groupes familiaux',
                      'groupe professionnel', 'isolement'],
    'Conflits sociaux': ['conflits sociaux', 'institutionnalisation des conflits',
                         'lutte des classes', 'greve', 'zone d\'incertitude'],
    'Syndicalisme': ['syndicat', 'syndicats', 'syndicalisation',
                     'cgt', 'cfdt', 'force ouvriere'],
    'Mobilisation': ['action collective', 'passager clandestin',
                     'free rider', 'greve', 'revendications sociales'],
    # 25 — démographie et modes de vie
    'Fécondité': ['fecondite', 'seuil de renouvellement', 'natalite',
                  'freins preventifs'],
    'Migrations': ['migrations', 'solde migratoire', 'migratoire',
                   'exode rural'],
    'Urbanisation': ['urbanisation', 'urbaines', 'exode rural'],
    'Transformation de la famille': ['comportements familiaux',
                                     'mariage', 'menages', 'divorces',
                                     'tailles des familles'],
    'Activité féminine': ['education des filles', 'autonomie feminine',
                          'scolarisation feminine', 'femmes-hommes',
                          'temps partiel', 'participation des femmes'],
    'Mobilité géographique': ['mobilite geographique',
                              'mobilite reelle des travailleurs',
                              'mobilite des facteurs', 'exode rural',
                              'cout de la mobilite'],
})

# Ensembles 26 et 27. On n'ajoute d'alias que pour les libellés dont le
# découpage automatique donne des expressions trop rares (« monnaie active »,
# « holisme ») ou trop larges pour être fiables.
ALIAS.update({
    'Monnaie neutre et monnaie active':
        ['monnaie neutre', 'monnaie non neutre', 'neutralite de la monnaie',
         'simple voile', 'illusion monetaire', 'monnaie n\'est pas neutre'],
    'Rationalité parfaite et rationalité limitée':
        ['rationalite limitee', 'rationalite parfaite', 'biais cognitif',
         'satisficing', 'homo economicus', 'systeme 1'],
    'Individualisme méthodologique et holisme':
        ['individualisme methodologique', 'holisme', 'fait social',
         'sociologie comprehensive', 'ideal-type'],
    'Intérêts individuels et intérêt collectif':
        ['interet collectif', 'interet general', 'passager clandestin',
         'free rider', 'bien collectif', 'tragedie des communs'],
    'Coopération':
        ['cooperation', 'gestion collective', 'arrangements institutionnels',
         'action collective', 'surveillance mutuelle'],
    'Transformation structurelle':
        ['transformation structurelle', 'tertiarisation', 'deversement',
         'desindustrialisation', 'dualisme', 'secteur traditionnel'],
    'Soutenabilité':
        ['soutenabilite', 'developpement durable', 'capital naturel',
         'generations futures', 'insoutenabilite'],
    'Capital humain':
        ['capital humain', 'duree moyenne de scolarisation',
         'duree attendue de scolarisation', 'education des filles',
         'diffusion de l\'education'],
    'Autorégulation et instabilité':
        ['autoregulation', 'auto-regulation', 'main invisible',
         'instabilite', 'loi des debouches', 'equilibre de sous-emploi'],
})
