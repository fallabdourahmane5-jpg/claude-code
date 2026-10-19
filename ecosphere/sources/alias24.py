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
