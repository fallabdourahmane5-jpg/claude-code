# -*- coding: utf-8 -*-
"""Frise chronologique : items du chapitre 4 de deuxieme annee.

NOUVEAUX : items ajoutes. Aucun auteur n'est date lorsque le document de cours
ne fournit qu'une initiale ou aucune date de naissance etablie : dans ce cas
seule la publication, dont l'annee est certaine, est portee sur la frise.
MAJ : items deja presents auxquels le chapitre 24 est ajoute.
"""

MAJ = {
 # auteurs deja presents
 'a199': "Karl Marx", 'a243': "Branko Milanovic", 'a323': "Paul Krugman",
 'a244': "Dani Rodrik", 'c23_a09': "Jagdish Bhagwati", 'c22_383': "Lionel Fontagné",
 # periodes et evenements
 'f001': "Première mondialisation", 'f003': "Entre-deux-guerres et démondialisation",
 'f006': "Hypermondialisation", 'f018': "Crise de 1929 et Grande Dépression",
 'f020': "Tarif Hawley-Smoot", 'f023': "Accords de Bretton Woods",
 'f028': "Fin de la convertibilité dollar-or", 'f035': "Consensus de Washington",
 'c23_e04': "Signature du GATT", 'c23_e05': "Création de l’OMC",
 'c23_e06': "Lancement du cycle de Doha",
 'c23_e07': "Engagement du G20 contre le protectionnisme",
 'c23_e08': "Guerre commerciale sino-américaine",
 'c23_e10': "Accord commercial dit de « phase one »",
 # ouvrages
 'o119': "The Globalization Paradox",
 # theories deja presentes
 'c22_372': "La grande convergence (Baldwin)",
}

G = "Gouvernance mondiale"
NOUVEAUX = []


def it(idn, type_, an, titre, resume, portee, fam, courant=G,
       auteur=None, fin=None, vivant=None, oeuvres=None):
    d = {'id': 'c24_' + idn, 'type': type_, 'an': an, 'titre': titre,
         'resume': resume, 'portee': portee, 'courant': courant,
         'ch': [24], 'fam': fam}
    if auteur:
        d['auteur'] = auteur
    if fin is not None:
        d['fin'] = fin
    if vivant is not None:
        d['vivant'] = vivant
    if oeuvres:
        d['oeuvres'] = oeuvres
    NOUVEAUX.append(d)


# ------------------------------------------------------------------ auteurs
it('a01', 'auteur', 1689, "Montesquieu",
   "Formule la thèse du « doux commerce » : le commerce crée une interdépendance qui rend le conflit coûteux.",
   "Montesquieu fonde l’argument pacificateur de l’ouverture sur un calcul de coût, non sur une vertu morale.",
   'classique', "Lumières", auteur="Montesquieu", fin=1755, vivant=False,
   oeuvres=["De l’esprit des lois (1748)"])
it('a02', 'auteur', 1892, "Jacob Viner",
   "Montre qu’une union douanière produit simultanément création et détournement de trafic.",
   "Viner fournit le critère d’évaluation de tout accord régional : comparer les deux effets, jamais les volumes.",
   'neoclassique', "Économie internationale", auteur="Jacob Viner", fin=1970, vivant=False,
   oeuvres=["The Customs Union Issue (1950)"])
it('a03', 'auteur', 1910, "Charles Kindleberger",
   "Établit qu’un ordre économique international stable suppose un leader acceptant le coût des biens publics.",
   "Kindleberger explique la stabilité d’après-guerre et, par contraste, la crise d’hégémonie contemporaine.",
   'keynesien', "Économie internationale", auteur="Charles Kindleberger", fin=2003,
   vivant=False, oeuvres=["La Grande Dépression mondiale, 1929-1939 (1973)",
                          "« Dominance and Leadership in the International Economy » (1981)"])
it('a04', 'auteur', 1928, "Bela Balassa",
   "Construit la typologie en cinq étapes de l’intégration économique régionale.",
   "Balassa permet de hiérarchiser les accords : du libre-échange simple à l’intégration politique.",
   'neoclassique', "Intégration économique", auteur="Bela Balassa", fin=1991, vivant=False,
   oeuvres=["The Theory of Economic Integration (1961)"])
it('a05', 'auteur', 1942, "Edward Luttwak",
   "Annonce dès 1990 le déplacement de la rivalité de puissance du terrain militaire vers le terrain économique.",
   "Luttwak fournit la matrice d’analyse du retour des droits de douane comme instruments stratégiques.",
   'mondialisation', "Géoéconomie", auteur="Edward Luttwak", vivant=True,
   oeuvres=["« From Geopolitics to Geo-Economics » (1990)"])
it('a06', 'auteur', 1949, "Robert Lawrence",
   "Distingue l’intégration superficielle, limitée aux frontières, et l’intégration profonde des règles internes.",
   "Lawrence explique la transformation des accords commerciaux en instruments de diffusion de normes.",
   'neoclassique', "Économie internationale", auteur="Robert Lawrence", vivant=True,
   oeuvres=["Regionalism, Multilateralism and Deeper Integration (1996)"])
it('a07', 'auteur', 1958, "Richard Baldwin",
   "Résume le renversement contemporain : le commerce passe du statut d’opportunité à celui de vulnérabilité.",
   "Baldwin donne sa formule à la « mondialisation dangereuse » et propose l’image du système solaire commercial.",
   'neoclassique', "Économie internationale", auteur="Richard Baldwin", vivant=True,
   oeuvres=["Travaux sur les chaînes de valeur mondiales et le régionalisme"])

# ----------------------------------------------------------------- ouvrages
it('o01', 'ouvrage', 1748, "De l’esprit des lois",
   "Montesquieu : « partout où il y a du commerce, il y a des mœurs douces » ; deux nations qui commercent deviennent dépendantes.",
   "Source canonique de la thèse pacificatrice du commerce, reprise par la construction européenne.",
   'classique', "Lumières", auteur="Montesquieu")
it('o02', 'ouvrage', 1950, "The Customs Union Issue",
   "Viner démontre qu’une union douanière peut réduire le bien-être si le détournement de trafic l’emporte sur la création.",
   "Fonde l’évaluation économique des accords régionaux, toujours utilisée pour juger un ACR.",
   'neoclassique', "Économie internationale", auteur="Jacob Viner")
it('o03', 'ouvrage', 1961, "The Theory of Economic Integration",
   "Balassa distingue zone de libre-échange, union douanière, marché commun, union économique et monétaire, intégration totale.",
   "Typologie de référence pour situer tout accord et mesurer le transfert de souveraineté qu’il implique.",
   'neoclassique', "Intégration économique", auteur="Bela Balassa")
it('o04', 'ouvrage', 1973, "La Grande Dépression mondiale, 1929-1939",
   "Kindleberger y développe la théorie de la stabilité hégémonique : sans leader, les biens publics internationaux sont sous-produits.",
   "Explication de l’effondrement des années 1930 et de la construction de l’ordre d’après-guerre.",
   'keynesien', "Économie internationale", auteur="Charles Kindleberger")
it('o05', 'ouvrage', 1981, "« Dominance and Leadership in the International Economy »",
   "Kindleberger formalise le problème du passager clandestin entre leader et suiveurs dans la fourniture des biens publics.",
   "Référence précise à citer pour l’argument hégémonique, distincte de l’ouvrage de 1973.",
   'keynesien', "Économie internationale", auteur="Charles Kindleberger")
it('o06', 'ouvrage', 1990, "« From Geopolitics to Geo-Economics »",
   "Luttwak soutient que la fin de la guerre froide déplace la rivalité vers le commerce, les investissements et les technologies.",
   "Texte fondateur de la géoéconomie, à mobiliser sur l’arsenalisation des interdépendances.",
   'mondialisation', "Géoéconomie", auteur="Edward Luttwak")
it('o07', 'ouvrage', 1995, "« US Trade Policy: The Infatuation with Free Trade Agreements »",
   "Bhagwati y critique la multiplication des accords préférentiels et propose l’image du « bol de spaghettis ».",
   "Argument central contre le régionalisme : la superposition des règles d’origine renchérit les échanges.",
   'neoclassique', "Économie internationale", auteur="Jagdish Bhagwati")
it('o08', 'ouvrage', 1996, "Regionalism, Multilateralism and Deeper Integration",
   "Lawrence oppose l’intégration superficielle, aux frontières, et l’intégration profonde, qui harmonise les règles internes.",
   "Grille indispensable pour analyser les accords contemporains et leurs clauses sociales et environnementales.",
   'neoclassique', "Économie internationale", auteur="Robert Lawrence")
it('o09', 'ouvrage', 2019, "« Le commerce international en crise systémique »",
   "Sébastien Jean distingue trois scénarios : continuité sous tensions, guerre froide économique, ou réforme de l’OMC.",
   "Cadre de prospective le plus directement mobilisable sur l’avenir du système commercial.",
   'neoclassique', "Économie internationale", auteur="Sébastien Jean")
it('o10', 'ouvrage', 2023, "« Les coûts de la fragmentation géoéconomique »",
   "Bolhuis, Chen et Kett (FMI) estiment les pertes : ≈ 0,3 % du PIB mondial pour un découplage limité, ≈ 2,3 % pour deux blocs, jusqu’à 7 %.",
   "Chiffrage de référence pour montrer que la fragmentation détruit une partie des gains de la spécialisation.",
   'neoclassique', "Économie internationale", auteur="M. Bolhuis, J. Chen et B. Kett")
it('o11', 'ouvrage', 2025, "Le Monde confisqué. Essai sur le capitalisme de la finitude",
   "Orain analyse le retour d’un capitalisme de la finitude : contrôle des actifs rares, monopoles, recul de la liberté commerciale.",
   "Explique le soubassement matériel du néo-mercantilisme : ressources et débouchés perçus comme finis.",
   'histoire', "Histoire de la pensée", auteur="Arnaud Orain")
it('o12', 'ouvrage', 2026, "« Quelle place pour l’Europe dans un monde de rapports de force ? »",
   "Bensidoun et Péron décrivent une Union européenne prise dans un étau entre America First et concurrence industrielle chinoise.",
   "Diagnostic européen le plus utilisable : le problème n’est pas l’absence de ressources mais leur conversion en puissance.",
   'neoclassique', "Économie internationale", auteur="I. Bensidoun et M. Péron")

# ---------------------------------------------------------------- théories
it('t01', 'theorie', 1748, "Le doux commerce",
   "Commerce → interdépendance → coût plus élevé d’un conflit → incitation à la paix.",
   "Argument pacificateur fondé sur un calcul de coût ; matrice intellectuelle de la CECA.",
   'classique', "Lumières", auteur="Montesquieu")
it('t02', 'theorie', 1950, "Création et détournement de trafic",
   "Une union régionale remplace une production coûteuse par une importation moins chère, mais peut aussi évincer un fournisseur plus efficace.",
   "Le bilan d’un accord dépend de l’effet dominant : la hausse du commerce intra-zone ne prouve rien.",
   'neoclassique', "Économie internationale", auteur="Jacob Viner")
it('t03', 'theorie', 1961, "Les cinq étapes de l’intégration économique",
   "Zone de libre-échange, union douanière, marché commun, union économique et monétaire, intégration totale.",
   "Chaque étape ajoute une dimension et réduit d’autant l’autonomie économique des États membres.",
   'neoclassique', "Intégration économique", auteur="Bela Balassa")
it('t04', 'theorie', 1973, "Théorie de la stabilité hégémonique",
   "La stabilité internationale suppose une puissance acceptant de fournir les biens publics internationaux malgré le passager clandestin.",
   "Explique l’ordre de 1945 et, a contrario, la crise contemporaine du multilatéralisme.",
   'keynesien', "Économie internationale", auteur="Charles Kindleberger")
it('t05', 'theorie', 1990, "Géoéconomie",
   "La rivalité de puissance se poursuit sur le terrain économique : commerce, investissements et technologies deviennent des armes.",
   "Permet de lire les droits de douane contemporains comme instruments stratégiques et non seulement protecteurs.",
   'mondialisation', "Géoéconomie", auteur="Edward Luttwak")
it('t06', 'theorie', 1995, "Le « bol de spaghettis »",
   "La superposition des accords préférentiels multiplie règles d’origine et procédures, et renchérit le commerce.",
   "Argument décisif contre l’idée que la régionalisation serait un substitut neutre au multilatéralisme.",
   'neoclassique', "Économie internationale", auteur="Jagdish Bhagwati")
it('t07', 'theorie', 1996, "Intégration superficielle et intégration profonde",
   "L’intégration superficielle supprime les barrières aux frontières, l’intégration profonde harmonise les règles internes.",
   "Explique pourquoi les accords contemporains portent sur le travail, l’environnement et la concurrence.",
   'neoclassique', "Économie internationale", auteur="Robert Lawrence")
it('t08', 'theorie', 2011, "Trilemme politique de l’économie mondiale",
   "Hypermondialisation, démocratie et souveraineté nationale ne peuvent être poussées simultanément au maximum : deux au plus.",
   "Montre que l’intégration a un coût politique, et que le choix sacrifié doit être explicité.",
   'developpement', "Économie du développement", auteur="Dani Rodrik")
it('t09', 'theorie', 2025, "Capitalisme de la finitude",
   "Ressources et débouchés perçus comme limités : contrôler les actifs rares avant les autres pour obtenir des rentes.",
   "Fondement matériel du retour mercantiliste et de la lecture du commerce comme jeu à somme nulle.",
   'histoire', "Histoire de la pensée", auteur="Arnaud Orain")
it('t10', 'theorie', 2026, "Mondialisation fragmentée",
   "Reprise en main du politique sur le marché, recul de la gouvernance multilatérale, captation des ressources stratégiques.",
   "Décrit la configuration contemporaine sans la confondre avec une démondialisation.",
   'mondialisation', "Économie internationale", auteur="Kesslassy et Rodrigues")

# -------------------------------------------------------------- événements
it('e01', 'evenement', 1933, "Agricultural Adjustment Act",
   "Roosevelt instaure dans le cadre du New Deal un soutien public aux revenus agricoles, prolongé par les Farm Bills.",
   "Origine de l’exception agricole, antérieure de quinze ans au GATT et toujours structurante.",
   'institutionnel', "Politique agricole", auteur="Franklin Delano Roosevelt")
it('e02', 'evenement', 1944, "Conférence de Bretton Woods : 44 pays",
   "Création du FMI et de la BIRD ; changes fixes mais ajustables autour d’un dollar convertible en or pour les autorités monétaires.",
   "Premier pilier de l’ordre d’après-guerre ; à ne pas confondre avec les 23 signataires du GATT en 1947.",
   'institutionnel', "Gouvernance mondiale")
it('e03', 'evenement', 1947, "Plan Marshall et échec de la Charte de La Havane",
   "Le plan Marshall soutient la reconstruction européenne dès 1948 ; faute de ratification américaine, l’OIC ne voit pas le jour.",
   "Explique pourquoi l’ordre commercial repose jusqu’en 1995 sur un accord et non sur une organisation.",
   'institutionnel', "Gouvernance mondiale")
it('e04', 'evenement', 1951, "Création de la CECA",
   "Six pays européens mettent en commun charbon et acier afin de rendre un nouveau conflit plus difficile et plus coûteux.",
   "Application institutionnelle du doux commerce : l’interdépendance comme instrument de paix.",
   'institutionnel', "Construction européenne")
it('e05', 'evenement', 1962, "Mise en œuvre de la politique agricole commune",
   "Cinq objectifs : productivité, niveau de vie équitable, stabilisation des marchés, sécurité des approvisionnements, prix raisonnables.",
   "Pendant européen de l’AAA américain ; source durable des tensions agricoles Nord-Sud.",
   'institutionnel', "Politique agricole")
it('e06', 'evenement', 1964, "Kennedy Round (1964-1967) : 48 participants",
   "Baisse des droits de douane vers une cible d’environ 7 % et adoption d’un premier code antidumping.",
   "Première extension du multilatéralisme au-delà du seul tarif.",
   'mondialisation', "Négociations commerciales")
it('e07', 'evenement', 1973, "Tokyo Round (1973-1979) : 99 participants",
   "Baisse vers environ 5 % et surtout encadrement des obstacles non tarifaires ; accord sur les subventions en 1979.",
   "Le multilatéralisme devient réglementaire dans un contexte de crise économique et monétaire.",
   'mondialisation', "Négociations commerciales")
it('e08', 'evenement', 1974, "Entrée en vigueur de l’accord multifibres",
   "Les pays développés peuvent limiter par des quotas certaines importations textiles face aux producteurs à bas coûts salariaux.",
   "Exemple majeur de dérogation protectionniste durable aux règles générales du GATT.",
   'mondialisation', "Négociations commerciales")
it('e09', 'evenement', 1986, "Uruguay Round (1986-1994) : 106 puis 123 participants",
   "Baisse vers environ 4 % et extension des règles à l’agriculture, au textile, aux services et à la propriété intellectuelle.",
   "Apogée du multilatéralisme commercial, qui débouche sur la création de l’OMC.",
   'mondialisation', "Négociations commerciales")
it('e10', 'evenement', 1999, "Conférence ministérielle de Seattle",
   "La préparation d’un nouveau cycle échoue dans un contexte de manifestations altermondialistes et de contestation triple de l’OMC.",
   "Tournant : le multilatéralisme commercial cesse d’apparaître comme un projet consensuel.",
   'institutionnel', "Gouvernance mondiale")
it('e11', 'evenement', 2005, "Fin du régime de quotas textiles",
   "Le démantèlement de l’accord multifibres s’achève le 1er janvier : le textile est pleinement intégré aux règles de l’OMC.",
   "Montre l’extension du multilatéralisme à un secteur historiquement protégé, et ses effets d’ajustement.",
   'mondialisation', "Négociations commerciales")
it('e12', 'evenement', 2007, "Émeutes de la faim et réorientation agricole du Sénégal",
   "Après 2007-2008, le Sénégal lance un programme d’intensification de la riziculture puis cherche à diversifier vers le mil, les fruits et les légumes.",
   "Cas d’école : une spécialisation soutenue — l’arachide, jusqu’à 40 % des terres — peut fragiliser la sécurité alimentaire.",
   'institutionnel', "Politique agricole")
it('e13', 'evenement', 2016, "Échec confirmé du cycle de Doha",
   "L’incapacité des membres à s’accorder en 2015-2016 confirme l’impasse des négociations globales fondées sur l’engagement unique.",
   "Point de bascule vers la régionalisation : les négociations se déplacent vers des cadres plus restreints.",
   'institutionnel', "Gouvernance mondiale")
it('e14', 'evenement', 2023, "L’Union africaine devient membre permanent du G20",
   "Le forum, réuni au niveau des chefs d’État depuis novembre 2008, s’élargit sans changer d’appellation.",
   "Traduit le déplacement du centre de gravité de l’économie mondiale dans l’architecture de la gouvernance.",
   'institutionnel', "Gouvernance mondiale")
it('e15', 'evenement', 2026, "Rapport de l’OMC : « un tournant décisif pour le multilatéralisme »",
   "642 ACR notifiés et 388 en vigueur ; simulations : −5,1 % de PIB mondial dans un monde fragmenté, −6,9 % dans un monde d’accords préférentiels, +2,9 % avec une coopération renforcée.",
   "Chiffrage institutionnel de l’alternative entre fragmentation et coopération, favorable aux plus petites économies.",
   'institutionnel', "Gouvernance mondiale")
