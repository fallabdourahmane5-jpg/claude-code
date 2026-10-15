# -*- coding: utf-8 -*-
"""Carte mentale et fiche methode du chapitre 4 de deuxieme annee.

La structure reprend exactement celle de la carte mentale transmise : six
branches (mondialisation et interdependances, gouvernance mondiale et
multilateralisme, systeme commercial et regles de l'OMC, cycles de negociation
et bilan, regionalisation et accords commerciaux, gouvernance hybride et defis
contemporains) et leurs sous-branches. Les feuilles sont detaillees a partir du
document de cours.
"""

VMAP = {
 'title': "Deuxième année, chapitre 4 — Régionalisation, gouvernance et régulations internationales",
 'core': "Réguler la mondialisation",
 'branches': [

  {'title': "Mondialisation et interdépendances", 'children': [
    {'title': "Évolution de la mondialisation", 'children': [
      "Mondialisation heureuse : consensus des années 1990 sur l’ouverture et le multilatéralisme",
      "Mondialisation dangereuse : les interdépendances deviennent vulnérabilités et dépendances",
      "Fragmentation géoéconomique : blocs, friendshoring et rivalités de puissance",
      "Baldwin : le commerce passe du statut d’opportunité à celui de vulnérabilité stratégique"]},
    {'title': "Acteurs de la mondialisation", 'children': [
      "États : politiques commerciales (ouverture ou protection, discriminante ou non)",
      "États : politiques industrielles — montée en gamme au Sud, réindustrialisation au Nord",
      "Firmes multinationales : architectes des chaînes de valeur par les IDE horizontaux et verticaux",
      "FMN structurellement favorables à l’ouverture : revenir sur les CVM est complexe et coûteux",
      "Société civile : citoyens, syndicats et ONG ; Fontagné et les préférences contradictoires",
      "Un même individu gagne comme consommateur et épargnant, perd comme travailleur exposé"]},
    {'title': "Interdépendance et paix", 'children': [
      "Montesquieu, De l’esprit des lois (1748) : « partout où il y a du commerce, il y a des mœurs douces »",
      "Mécanisme : commerce → interdépendance → coût plus élevé d’un conflit → incitation à la paix",
      "CECA (1951) : six pays mettent en commun charbon et acier pour rendre la guerre impossible",
      "Marx et les analyses marxistes : des échanges asymétriques produisent dépendance et domination"]},
    {'title': "Retour de la géoéconomie", 'children': [
      "Luttwak (1990) : après 1989, l’affrontement militaire devient affrontement économique",
      "Les droits de douane américains dépassent la protection : domination technologique et rapport de force",
      "Puissance américaine : technologique, commerciale et monétaire (privilège exorbitant du dollar)",
      "Dérisquage et friendshoring : chercher le partenaire fiable plutôt que le plus efficace",
      "Paradoxe : moins d’interdépendance = conflit moins coûteux = tensions potentiellement accrues"]},
  ]},

  {'title': "Gouvernance mondiale et multilatéralisme", 'children': [
    {'title': "Formes de coordination internationale", 'children': [
      "Unilatéralisme : un État décide seul de sa politique et de ses règles",
      "Bilatéralisme : deux États négocient directement des concessions réciproques",
      "Plurilatéralisme : accord entre un groupe limité de pays, sans proximité géographique nécessaire",
      "Régionalisme : coopération organisée dans le cadre d’un accord commercial régional",
      "Multilatéralisme : règles négociées entre au moins trois États, fondées sur réciprocité et équité"]},
    {'title': "Biens publics mondiaux", 'children': [
      "Non-rivalité : la consommation par un acteur n’empêche pas les autres d’en bénéficier",
      "Non-exclusion : il est difficile d’empêcher un acteur d’en bénéficier",
      "Exemples : climat et biodiversité, stabilité financière, stabilité du commerce, règles équitables",
      "Passager clandestin : chaque État a intérêt à laisser les autres supporter le coût",
      "Résultat : équilibre de Nash sous-optimal, d’où la nécessité de règles de bonne conduite"]},
    {'title': "Du GATT à l’OMC", 'children': [
      "GATT (1947) : 23 pays, à défaut de l’OIC que la Charte de La Havane n’a pu créer",
      "OMC (1995) : accords de Marrakech, cadre institutionnel permanent et organe de règlement",
      "Contestations : PED (règles favorables au Nord), pays avancés (concurrence déloyale)",
      "Société civile : inégalités et environnement associés à la mondialisation",
      "Crise de légitimité : rapport de l’OMC de juillet 2026 — « tournant décisif pour le multilatéralisme »"]},
    {'title': "Transformations idéologiques", 'children': [
      "Milanovic : grande transformation du néolibéralisme au « libéralisme de marché national »",
      "Libéralisme à l’intérieur des frontières, mercantilisme dans les relations extérieures",
      "Orain, Le Monde confisqué (2025) : le capitalisme de la finitude et ses trois âges",
      "Finitude des ressources et des débouchés → commerce perçu comme jeu à somme nulle",
      "Kesslassy et Rodrigues (2026) : politique reprenant la main, recul du multilatéralisme, captation des ressources"]},
  ]},

  {'title': "Système commercial et règles de l’OMC", 'children': [
    {'title': "Principes fondamentaux", 'children': [
      "Non-discrimination : clause de la nation la plus favorisée (article I)",
      "Non-discrimination : traitement national (article III), un produit importé ne peut être moins bien traité",
      "Réciprocité : donnant-donnant qui rend l’ouverture politiquement acceptable",
      "Krugman : cette logique de « mercantilisme éclairé » produit pourtant la libéralisation",
      "Transparence : privilégier le droit de douane, identifiable et négociable, aux mesures opaques"]},
    {'title': "Interdictions majeures", 'children': [
      "Interdiction de discriminer arbitrairement entre partenaires commerciaux",
      "Interdiction des restrictions quantitatives et du contingentement (article XI)",
      "Encadrement du dumping préjudiciable et des pratiques faussant la concurrence"]},
    {'title': "Exceptions encadrées", 'children': [
      "Accords commerciaux régionaux : dérogation à la clause NPF autorisée par l’article XXIV",
      "Traitement spécial et différencié : flexibilités reconnues aux pays en développement",
      "Système généralisé de préférences : préférences tarifaires sans réciprocité équivalente",
      "Mesures de sauvegarde (article XIX et Accord de 1994) : protection temporaire en cas de dommage grave",
      "Accord SMC (1995) : subventions prohibées, subventions contestables, catégorie verte expirée en 1999"]},
    {'title': "Règlement des différends", 'children': [
      "Organe de règlement des différends créé avec l’OMC en 1995",
      "Les États-Unis et l’Union européenne sont les acteurs majeurs des plaintes (1995-2010)",
      "L’institutionnalisation n’élimine pas les conflits : elle les traite dans un cadre juridique"]},
    {'title': "Protection agricole", 'children': [
      "Droits de douane moyens en 2019 : 15,9 % dans l’agriculture contre 3 % dans l’industrie",
      "Justifications : sécurité alimentaire, revenus agricoles, territoires ruraux, souveraineté",
      "Agricultural Adjustment Act (1933) puis Farm Bills aux États-Unis",
      "Politique agricole commune (1962) : productivité, revenus, stabilité, approvisionnements, prix",
      "Groupe de Cairns et coalitions du Sud : contestation des subventions du Nord (coton américain)",
      "Sénégal : filière arachide jusqu’à 40 % des terres, émeutes de la faim de 2007-2008, riziculture puis diversification"]},
  ]},

  {'title': "Cycles de négociation et bilan du multilatéralisme", 'children': [
    {'title': "Théorie de la stabilité hégémonique", 'children': [
      "Kindleberger (1973, 1981) : un ordre stable exige qu’une puissance assume le coût collectif",
      "Biens publics internationaux : monnaie stable, marchés ouverts, liquidités, coopération",
      "Matrice du cours : coopération mutuelle (4 ; 4), défection du suiveur (3 ; 5), double défection (2 ; 3)",
      "États-Unis après 1945 : environ 60 % de la production mondiale et 70 % des réserves d’or",
      "Trois piliers : BIRD et plan Marshall, FMI et Bretton Woods (1944, 44 pays), GATT (1947)"]},
    {'title': "Cycles historiques du GATT", 'children': [
      "Premiers rounds : Genève 1947 (23), Annecy 1949 (33), Torquay 1951 (34), Genève 1955-1956 (34)",
      "Kennedy Round (1964-1967) : 48 participants, cible d’environ 7 %, premier code antidumping",
      "Tokyo Round (1973-1979) : 99 participants, environ 5 %, obstacles non tarifaires et subventions (1979)",
      "Uruguay Round (1986-1994) : 106 puis 123 participants, environ 4 %, création de l’OMC",
      "Accord multifibres (1974) démantelé : fin des quotas textiles le 1er janvier 2005",
      "Conférence de Seattle (1999) : contestation altermondialiste et crise de légitimité",
      "Cycle de Doha (2001) : programme pour le développement, 21 thèmes, engagement unique, enlisement"]},
    {'title': "Bilan de la libéralisation", 'children': [
      "Droits de douane : environ 40 % au départ, 3 à 4 % aujourd’hui sur les manufacturés",
      "Findlay et O’Rourke (2002) : revenus 67 %, droits de douane 25 %, coûts de transport 8 %",
      "Élargissement : 23 pays en 1947, 123 à l’Uruguay Round, 166 membres de l’OMC en 2026",
      "Extension des domaines : du tarif au dumping, aux subventions, à l’agriculture, aux services, aux brevets",
      "Limites : hétérogénéité des intérêts, retour des intérêts nationaux, déplacement vers les ACR"]},
  ]},

  {'title': "Régionalisation et accords commerciaux", 'children': [
    {'title': "Typologie de Bela Balassa (1961)", 'children': [
      "Zone de libre-échange : droits internes supprimés, politiques extérieures autonomes (ACEUM, RCEP)",
      "Union douanière : zone de libre-échange plus tarif extérieur commun (Union européenne)",
      "Marché commun : libre circulation du travail et du capital en plus des marchandises",
      "Union économique et monétaire : coordination des politiques, éventuelle monnaie commune",
      "Intégration totale : autorité supranationale, l’intégration économique devient politique"]},
    {'title': "Effets de Jacob Viner (1950)", 'children': [
      "Création de trafic : une production domestique coûteuse remplacée par une importation moins chère",
      "Détournement de trafic : un fournisseur mondial efficace remplacé par un partenaire moins efficace",
      "Le bilan d’un accord dépend de l’effet qui domine, non du volume des échanges intra-zone"]},
    {'title': "Exemples d’intégration régionale", 'children': [
      "ASEAN (1967) : 5 puis 10 membres, origine géopolitique, insertion dans les chaînes asiatiques",
      "ASEAN : environ 4 % des exportations mondiales en 1990, environ 8 % aujourd’hui",
      "ZLECAf : 13,9 % du commerce africain intra-africain en 2020, projection de 26,8 % en 2045",
      "Limite africaine : structures productives proches, complémentarité et infrastructures insuffisantes",
      "642 ACR notifiés à l’OMC et 388 en vigueur au 1er septembre 2026 ; 181 notifications pour l’Europe"]},
    {'title': "Intégration profonde et complexité", 'children': [
      "Lawrence (1996) : intégration superficielle aux frontières, intégration profonde des règles internes",
      "Accords profonds : normes sociales et environnementales (UE-Vietnam et conventions de l’OIT)",
      "UE-Mercosur : gains industriels européens, exposition agricole, débat sur la réciprocité des normes",
      "Bhagwati (1995) : « bol de spaghettis », règles d’origine multiples et coûts administratifs",
      "Effet domino : plus les blocs se forment, plus le coût d’en rester exclu augmente",
      "Baldwin : « multilatéralisme sans OMC » et ordre commercial en système solaire"]},
  ]},

  {'title': "Gouvernance hybride et défis contemporains", 'children': [
    {'title': "Architecture de la régulation", 'children': [
      "Gouvernance hybride : OMC, États, ACR, FMN, G7-G20, organisations régionales, société civile",
      "Risque : multiplication des normes, coordination plus difficile, règles contradictoires",
      "Pouvoir indirect des FMN : chantage à la localisation et moins-disant fiscal, social, réglementaire",
      "Propriété intellectuelle et accès aux médicaments : trithérapies, flexibilités, Covid-19",
      "G20 : ministres dès 1999, sommet des chefs d’État en novembre 2008, Union africaine en 2023",
      "Coordination fiscale : taux minimum de 15 % pour certaines grandes multinationales"]},
    {'title': "Trilemme de Dani Rodrik", 'children': [
      "Hypermondialisation, démocratie et souveraineté nationale : deux termes au maximum",
      "Souveraineté et démocratie → limiter l’hypermondialisation (compromis de Bretton Woods)",
      "Hypermondialisation et souveraineté → autonomie démocratique réduite (« camisole dorée »)",
      "Hypermondialisation et démocratie → gouvernance supranationale très approfondie",
      "Base sociale du rejet : PIB par habitant et revenu médian divergent aux États-Unis depuis 1984",
      "Rodrik : chercher des « good jobs » en élevant la productivité des services, pas seulement réindustrialiser"]},
    {'title': "Scénarios d’avenir et coûts", 'children': [
      "Sébastien Jean (2019) : continuité sous tensions, guerre froide économique ou réforme de l’OMC",
      "Fragmentation déjà observable : +40 % d’échanges entre alliés américains, −80 % avec les alliés russes",
      "Bolhuis, Chen et Kett (FMI, 2023) : −0,3 % pour un découplage limité, −2,3 % pour deux blocs, jusqu’à −7 %",
      "OMC 2026 : monde fragmenté −5,1 % de PIB et −18,6 % d’exportations à l’horizon 2050",
      "OMC 2026 : monde d’accords préférentiels −6,9 % et −26,9 % ; coopération renforcée +2,9 % et +17,9 %",
      "Menace sur la grande convergence : les PED dépendent des marchés, des IDE et des technologies"]},
    {'title': "Défis mondiaux et position de l’Europe", 'children': [
      "Climat : bien public mondial, passager clandestin, besoin d’un acteur moteur",
      "Minerais critiques : extraction concentrée, raffinage plus concentré encore, rôle central de la Chine",
      "Union européenne : 450 millions de consommateurs, puissance normative, MACF comme instrument climatique",
      "Bensidoun et Péron (2026) : l’Europe prise dans un étau entre America First et concurrence chinoise",
      "Atouts européens : chimie, pharmacie, automobile, aéronautique, spatial, défense, capital humain",
      "Europe « construite pour un autre monde » : logique de règles face à des logiques de puissance",
      "Crise d’hégémonie : ni les États-Unis ni la Chine ne cumulent puissance et légitimité",
      "Issue possible : plusieurs leaderships sectoriels plutôt qu’un hégémon unique"]},
  ]},
 ],
}

MAP = {
 'title': "Deuxième année, chapitre 4 — Régionalisation, gouvernance et régulations internationales",
 'sub': "Acteurs et interdépendances · gouvernance mondiale et biens publics · règles du GATT et de l’OMC · "
        "cycles de négociation · régionalisation des échanges · gouvernance hybride et fragmentation géoéconomique.",
 'core': "Réguler la mondialisation",
 'branches': [],
 'legend': [
  {'k': "Auteurs",
   'v': "Montesquieu, Marx, Luttwak, R. Baldwin, Fontagné, Milanovic, Arnaud Orain, Kesslassy et "
        "Rodrigues, Kindleberger, Krugman, Balassa, Viner, Lawrence, Bhagwati, Rodrik, Sébastien Jean, "
        "Bolhuis, Chen et Kett, Bensidoun et Péron, Ricardo, Heckscher-Ohlin-Samuelson, Nash, Roosevelt."},
  {'k': "Pièges",
   'v': "Multilatéralisme (au moins trois États, règles communes) ≠ bilatéralisme ≠ plurilatéralisme ≠ "
        "régionalisme ; gouvernance mondiale ≠ gouvernement mondial ; zone de libre-échange ≠ union "
        "douanière (le tarif extérieur commun fait la différence) ; création de trafic ≠ hausse des "
        "échanges intra-zone ; la catégorie verte de l’Accord SMC a expiré en 1999 ; la Chine n’a pas "
        "perdu son statut de pays en développement, elle a renoncé en septembre 2025 à demander de "
        "nouveaux avantages ; le GATT n’est pas une organisation mais un accord, l’OIC ayant échoué."},
  {'k': "Chiffres",
   'v': "GATT 1947, 23 pays ; Bretton Woods 1944, 44 pays ; États-Unis ≈ 60 % de la production mondiale "
        "et 70 % des réserves d’or ; rounds : 48 participants (Kennedy), 99 (Tokyo), 106 puis 123 "
        "(Uruguay) ; droits de douane ≈ 40 % au départ, 12 % en 1962, 7 %, 5 %, 4 % ; OMC 166 membres "
        "en 2026 ; agriculture 15,9 % contre industrie 3 % en 2019 ; Findlay et O’Rourke 67 / 25 / 8 ; "
        "642 ACR notifiés et 388 en vigueur en 2026 ; ASEAN 4 % → 8 % des exportations mondiales ; "
        "ZLECAf 13,9 % en 2020 → 26,8 % projetés en 2045 ; Sénégal : arachide jusqu’à 40 % des terres ; "
        "FMI : −0,3 %, −2,3 %, jusqu’à −7 % de PIB mondial ; OMC 2026 : −5,1 %, −6,9 %, +2,9 % ; "
        "UE 450 millions de consommateurs ; taux minimum d’imposition 15 %."},
  {'k': "Transitions",
   'v': "Des acteurs de la mondialisation à la transformation du regard porté sur l’interdépendance "
        "(Montesquieu → Marx → Luttwak → Baldwin) ; de la vulnérabilité perçue au paradoxe de la "
        "fragmentation ; des biens publics mondiaux à la nécessité d’un hégémon (Nash → Kindleberger) ; "
        "des principes du GATT à leurs exceptions, puis aux rounds qui les ont produites ; de "
        "l’enlisement de Doha à la régionalisation (Balassa → Viner → Lawrence → Bhagwati) ; de la "
        "gouvernance hybride au trilemme de Rodrik, puis au coût chiffré de la fragmentation."},
 ],
}

METHODE = (
 '<div class="nb"><h2>✏️ Méthode — Deuxième année, chapitre 4</h2>'
 '<h3>Réflexes de copie</h3><ul>'
 '<li><strong>Quatre formes de relations commerciales</strong> : unilatéralisme (décision seule), '
 'bilatéralisme (deux États), plurilatéralisme (groupe limité), multilatéralisme (au moins trois États '
 'et règles communes). Le régionalisme est une coopération entre pays proches : il peut être '
 'plurilatéral sans être multilatéral. Poser ces distinctions en introduction évite les contresens.</li>'
 '<li><strong>Gouvernance ≠ gouvernement</strong> : il n’existe aucune autorité mondiale souveraine. '
 'La gouvernance mondiale désigne la production coordonnée de règles par des acteurs qui restent '
 'juridiquement indépendants — d’où sa fragilité structurelle.</li>'
 '<li><strong>Bien public mondial</strong> : toujours démontrer les deux propriétés (non-rivalité et '
 'non-exclusion) avant d’en déduire le passager clandestin, puis l’équilibre de Nash sous-optimal. '
 'C’est cette chaîne, et non la seule invocation du climat, qui justifie la coopération.</li>'
 '<li><strong>Le GATT n’est pas une organisation</strong> : c’est un accord, faute de ratification de '
 'la Charte de La Havane créant l’OIC. L’institution ne naît qu’en 1995 avec l’OMC. L’erreur est '
 'fréquente et visible.</li>'
 '<li><strong>Zone de libre-échange / union douanière</strong> : la différence tient au tarif extérieur '
 'commun. Si deux membres peuvent appliquer des droits différents au même produit chinois, il s’agit '
 'd’une zone de libre-échange — et la question des règles d’origine devient décisive.</li>'
 '<li><strong>Viner</strong> : ne jamais conclure d’une hausse du commerce intra-zone qu’un accord est '
 'bénéfique. Il faut comparer création et détournement de trafic : le second augmente aussi les '
 'échanges internes tout en dégradant l’efficience mondiale.</li>'
 '<li><strong>Exceptions ≠ échec des règles</strong> : ACR, traitement spécial et différencié, '
 'sauvegardes et subventions encadrées font partie du système. Les présenter comme des trahisons du '
 'multilatéralisme revient à ignorer qu’elles ont rendu son élargissement possible.</li>'
 '<li><strong>Catégorie verte de l’Accord SMC</strong> : elle a expiré en 1999. Écrire que les '
 'subventions vertes sont automatiquement autorisées est une erreur de droit.</li>'
 '<li><strong>Trilemme de Rodrik</strong> : il n’oppose pas mondialisation et démocratie en général, '
 'mais démontre l’incompatibilité de trois objectifs poussés simultanément à leur maximum. Nommer '
 'les trois sommets et choisir explicitement celui que l’on sacrifie.</li>'
 '<li><strong>Fragmentation ≠ démondialisation</strong> : les flux ne disparaissent pas, ils se '
 'réorientent selon les alliances. Les chiffres du FMI et de l’OMC servent à mesurer le coût de cette '
 'réorientation, pas à prouver un effondrement du commerce.</li>'
 '</ul>'
 '<h3>Couples d’auteurs à mobiliser</h3><ul>'
 '<li>Montesquieu (1748) et Marx (1848) : l’interdépendance pacifie-t-elle ou domine-t-elle ?</li>'
 '<li>Luttwak (1990) et R. Baldwin : de l’annonce du retour de la géoéconomie à son constat.</li>'
 '<li>Nash et Kindleberger (1973) : de l’équilibre sous-optimal à la nécessité d’un hégémon.</li>'
 '<li>Ricardo (1817) et Krugman : la théorie dit que l’importation est le gain, la négociation la traite '
 'comme une concession — c’est le mercantilisme éclairé.</li>'
 '<li>Balassa (1961) et Lawrence (1996) : la profondeur institutionnelle et la profondeur réglementaire '
 'sont deux dimensions distinctes de l’intégration.</li>'
 '<li>Viner (1950) et Bhagwati (1995) : le coût statique du détournement et le coût administratif du '
 'bol de spaghettis.</li>'
 '<li>Milanovic et Orain (2025) : la renationalisation du libéralisme et la perception de la finitude.</li>'
 '<li>Rodrik et Bensidoun-Péron (2026) : le trilemme théorique et sa traduction européenne concrète.</li>'
 '<li>Sébastien Jean (2019) et Bolhuis-Chen-Kett (2023) : les scénarios et leur chiffrage.</li>'
 '<li>Fontagné et Rodrik : l’ambivalence individuelle et la base sociale du rejet de l’hypermondialisation.</li>'
 '</ul>'
 '<h3>Plans à ne pas reproduire</h3>'
 '<p>Le plan du cours — institutions d’après-guerre, régionalisation, gouvernance hybride — est un plan '
 'd’exposition chronologique, pas un plan de dissertation. Le recopier conduit à raconter l’histoire du '
 'GATT au lieu de répondre à une question. Construire plutôt la problématique autour d’une tension : '
 'efficacité contre souveraineté, règles universelles contre préférences régionales, besoin croissant de '
 'coopération contre volonté décroissante de coopérer. Le chapitre fournit une ressource rare en '
 'dissertation : des contre-exemples chiffrés, puisque les simulations de l’OMC montrent qu’un monde '
 'd’accords préférentiels serait plus coûteux encore qu’un monde de blocs.</p>'
 '<h3>Erreurs d’attribution à éviter</h3><ul>'
 '<li>La typologie en cinq étapes est de Balassa (1961), la distinction superficiel / profond de '
 'Lawrence (1996) : ce sont deux grilles différentes, pas deux versions de la même.</li>'
 '<li>Le « bol de spaghettis » est de Bhagwati (1995) ; Baldwin l’illustre en 2008 sur l’Amérique '
 'latine et propose l’image du système solaire — ne pas intervertir.</li>'
 '<li>La théorie de la stabilité hégémonique est de Kindleberger, pas de Krugman ; le mercantilisme '
 'éclairé est de Krugman, pas de Kindleberger.</li>'
 '<li>Le groupe de Cairns rassemble des pays exportateurs agricoles favorables à la libéralisation : '
 'ce n’est pas une coalition protectionniste.</li>'
 '</ul></div>'
)
