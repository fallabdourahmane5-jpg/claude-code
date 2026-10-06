# -*- coding: utf-8 -*-
"""Carte mentale et fiche methode du chapitre 3 de deuxieme annee.

La structure reprend exactement celle de la carte mentale transmise : cinq
branches (introduction et evolution de l'analyse, theories traditionnelles,
theories contemporaines, politiques publiques et concurrence internationale,
debat libre-echange / protectionnisme) et leurs sous-branches. Les feuilles
sont detaillees a partir du document de cours.
"""

VMAP = {
 'title': "Deuxième année, chapitre 3 — L’analyse économique du commerce international",
 'core': "L’analyse économique du commerce international",
 'branches': [

  {'title': "Introduction et évolution de l’analyse", 'children': [
    {'title': "Questions fondamentales", 'children': [
      "Déterminants : pourquoi les pays échangent-ils et comment se spécialisent-ils ?",
      "Conséquences : effets sur la croissance, les prix, l’emploi, les salaires et les inégalités",
      "Effets sur la structure productive des économies"]},
    {'title': "Évolution historique de la pensée", 'children': [
      "Vision traditionnelle : optimisme sur les gains de l’ouverture",
      "Hypermondialisation : critiques sur la désindustrialisation et les coûts localisés",
      "Des hypothèses fortes de concurrence pure et parfaite…",
      "…à leur relâchement : concurrence imparfaite, économies d’échelle, différenciation",
      "Krugman, La mondialisation n’est pas coupable (1996), puis son réexamen de 2019"]},
    {'title': "Approches positive et normative", 'children': [
      "Analyse positive : expliquer ce qui est et les faits observés",
      "Analyse normative : évaluer les conséquences et le bien-être",
      "Gagnants, perdants et légitimité éventuelle du protectionnisme"]},
    {'title': "Coûts politiques et retour du protectionnisme", 'children': [
      "Milanović : courbe de l’éléphant et stagnation des classes populaires du Nord",
      "Gains agrégés possibles mais coûts très concentrés",
      "Le retour du protectionnisme comme paradoxe seulement apparent"]},
  ]},

  {'title': "Théories traditionnelles de l’échange", 'children': [
    {'title': "Adam Smith et l’avantage absolu", 'children': [
      "Division du travail étendue à l’échelle internationale (1776)",
      "Avantage absolu fondé sur la productivité",
      "Trois gains : dextérité, économie de temps, innovation",
      "Jeu à somme positive augmentant la richesse totale",
      "Importance des importations : elles sont la finalité de l’échange"]},
    {'title': "David Ricardo et l’avantage comparatif", 'children': [
      "Modèle ricardien et hypothèses de concurrence pure (Principes, 1817)",
      "Immobilité internationale des facteurs de production",
      "Coût d’opportunité comme fondement de la spécialisation",
      "Portugal / Angleterre : 90-100 pour le drap, 80-120 pour le vin",
      "Gains : hausse de la production mondiale (4 → 4,325) ou économie de 30 unités de travail",
      "Réserves : rendements d’échelle, rapports de force, traité anglo-portugais"]},
    {'title': "John Stuart Mill et la répartition du gain", 'children': [
      "Prix relatif international compris entre les bornes nationales (1848)",
      "Bornes de l’exemple ricardien : 0,88 < Pv/d < 1,2 et 0,83 < Pd/v < 1,125",
      "Inégalité de partage du gain entre partenaires selon la position du prix"]},
    {'title': "Modèle HOS et dotations factorielles", 'children': [
      "Heckscher (1919) et Ohlin (1933) : abondance relative des facteurs",
      "Théorème H-O : spécialisation selon le facteur relativement abondant",
      "Hypothèses 2 × 2 × 2 et homogénéité du travail",
      "Stolper-Samuelson (1941) : impact sur la rémunération des facteurs",
      "Égalisation internationale du prix des facteurs (Samuelson)",
      "Rybczynski (1955) : dotations construites — Corée du Sud, Chine",
      "Paradoxe de Leontief (1953) et hétérogénéité du travail (Baldwin, 1971)"]},
    {'title': "Critiques marxistes et structuralistes", 'children': [
      "Marx (1848) : le libre-échange prolonge la domination capitaliste",
      "Lénine (1916) : impérialisme et exportation de capitaux",
      "Prebisch (1950) : dégradation des termes de l’échange, 1875-1938",
      "Arghiri Emmanuel (1969) : théorie de l’échange inégal",
      "Bhagwati (1958) : croissance appauvrissante",
      "Amin : déconnexion — limite : analyses nées de la grande divergence"]},
    {'title': "Vérifications empiriques et limites", 'children': [
      "Avantages comparatifs révélés (CEPII) : France, Brésil, Chine",
      "Reprimarisation et désindustrialisation précoce (Rodrik)",
      "Dépendances d’intrants et lecture par la balance courante",
      "Limite décisive : le commerce intra-branche France-Allemagne"]},
  ]},

  {'title': "Théories contemporaines du commerce", 'children': [
    {'title': "Approches néo-factorielles et néo-technologiques", 'children': [
      "Capital humain et qualifications du travail (Keesing, 1966)",
      "Posner (1961) : écart technologique temporaire érodé par l’imitation",
      "Vernon (1966) : cycle de vie international du produit en quatre phases",
      "Téléviseurs à écran plat : Japon, Corée, Chine, Vietnam"]},
    {'title': "Rôle de la demande et différenciation", 'children': [
      "Lassudrie-Duchêne : demande de différence et variété",
      "Chamberlin (1933) : concurrence monopolistique et différenciation",
      "Différenciation horizontale (caractéristiques) et verticale (gamme)",
      "Linder : demande représentative et similarité des marchés"]},
    {'title': "Krugman et la nouvelle géographie économique", 'children': [
      "Rendements croissants et économies d’échelle internes et externes",
      "Trois gains : sélection par la concurrence, variété, effet de dimension",
      "Effets d’agglomération et districts industriels de Marshall (1890)",
      "Bangalore, Toulouse, Silicon Valley : avantages acquis",
      "Seuil critique Q0 et réhabilitation du protectionnisme éducateur"]},
  ]},

  {'title': "Politiques publiques et concurrence internationale", 'children': [
    {'title': "Interventions économiques de l’État", 'children': [
      "Politique fiscale et compétitivité des entreprises",
      "Politique industrielle et soutien à l’innovation",
      "Politique de la concurrence et abus de position dominante",
      "Politique industrielle et concurrence internationale"]},
    {'title': "Politique commerciale", 'children': [
      "Politiques d’ouverture et réduction des barrières",
      "Politiques protectionnistes et néo-mercantilisme",
      "Politique commerciale et concurrence internationale",
      "Rattrapage des émergents et concurrence intra-branche (véhicules électriques)"]},
  ]},

  {'title': "Débat entre libre-échange et protectionnisme", 'children': [
    {'title': "Arguments pour la libéralisation", 'children': [
      "Allocation efficace des ressources et productivité",
      "Économies d’échelle, spécialisation, apprentissage et innovation",
      "Effet variété pour les consommateurs et les entreprises",
      "Pouvoir d’achat, loi d’Engel et demande extérieure",
      "Concurrence et sélection des producteurs les plus efficaces"]},
    {'title': "Les perdants de l’ouverture", 'children': [
      "Malédiction des ressources et insertion dominée",
      "Travailleurs peu qualifiés des secteurs exposés (Stolper-Samuelson)",
      "Coûts d’ajustement et chômage d’inadéquation",
      "Toutes les spécialisations ne se valent pas"]},
    {'title': "Instruments et coûts du protectionnisme", 'children': [
      "Protection tarifaire : droits de douane, tarifs consolidés, pics tarifaires, pertes sèches",
      "Protection non tarifaire : quotas, normes, contenu local et subventions",
      "Analyse en surplus : petit pays, grand pays et gain de termes de l’échange",
      "Asymétrie de Pareto (1906) : gains concentrés et pertes diffuses",
      "Léo Charles : constitution d’un bloc social protectionniste",
      "Guerres commerciales, dilemme du prisonnier et représailles",
      "Tariff jumping, détournement des flux et gains des pays tiers"]},
    {'title': "Arguments théoriques du protectionnisme", 'children': [
      "Argument fiscal : faible au Nord, significatif dans certains PED",
      "Keynes : multiplicateur, fuites et De l’autosuffisance nationale (1933)",
      "List (1841) après Hamilton : trois phases, Zollverein et Bismarck",
      "Krugman : seuil critique et trois conditions de réussite",
      "Kaldor (1966) : industries vieillissantes et « canards boiteux »",
      "Brander et Spencer (1983) : Airbus-Boeing et guerre des subventions"]},
    {'title': "Institutions et multilatéralisme", 'children': [
      "Leçons de la crise de 1929 et de l’entre-deux-guerres (Hawley-Smoot, 1930)",
      "GATT (1947) et OMC (1995) : règles communes négociées",
      "Principes de la nation la plus favorisée et réciprocité",
      "Échec du cycle de Doha et crise du multilatéralisme"]},
    {'title': "Le protectionnisme dans l’histoire", 'children': [
      "Bairoch : « océan de protectionnisme » et paradoxe du XIXe siècle",
      "Jean-Marc Daniel : « les pratiques sont tendanciellement protectionnistes »",
      "Protectionnisme furtif et mesures non tarifaires",
      "Crise de 2008 et engagements du G20"]},
    {'title': "Retour contemporain et fragmentation", 'children': [
      "Trump I (2018) : acier 25 %, aluminium 10 % ; Chine de 3,1 % à 21,5 %",
      "Biden : véhicules électriques de 25 % à 100 % ; IRA et CHIPS Act (2022)",
      "Trump II : « Liberation Day » du 2 avril 2025, droit moyen de 5 % à 23,7 %",
      "Sections 201, 301, 701 et 731 : la logique du rapport de force",
      "Guimbard, Vicard et Wibaux : négocier, diversifier ou confronter"]},
    {'title': "Les habits neufs du protectionnisme", 'children': [
      "Vuillemey (2022) : protectionnisme social et environnemental",
      "Rodrik (2022) : paradigme productiviste",
      "Emlinger, Guimbard et Lefebvre (2023) : nouvelle hiérarchie des objectifs",
      "Environnement : effets de distance, d’échelle et de composition",
      "Grossman et Krueger (1995), SEQE et MACF",
      "Sécurité : approvisionnements, friend-shoring, arsenalisation"]},
  ]},
 ],
}

MAP = {
 'title': "Deuxième année, chapitre 3 — L’analyse économique du commerce international",
 'sub': "Théories traditionnelles et contemporaines de l’échange · gains et perdants du libre-échange · "
        "instruments et évaluation des politiques commerciales · retour du protectionnisme et fragmentation géo-économique.",
 'core': "Commerce international",
 'branches': [],
 'legend': [
  {'k': "Auteurs",
   'v': "Smith, Ricardo, J. S. Mill, Marx, Lénine, Prebisch, Arghiri Emmanuel, Bhagwati, Amin, "
        "Heckscher, Ohlin, Stolper, Samuelson, Rybczynski, Leontief, R. Baldwin, Keesing, Posner, "
        "Vernon, Lassudrie-Duchêne, Chamberlin, Linder, Krugman, Marshall, Rodrik, Milanović, "
        "Pareto, Léo Charles, Jean-Marc Daniel, Bairoch, Keynes, List, Hamilton, Kaldor, Brander et "
        "Spencer, Vuillemey, Emlinger, Guimbard, Grossman et Krueger, Engel."},
  {'k': "Pièges",
   'v': "Avantage absolu ≠ avantage comparatif ; libre-échange (fait) ≠ libre-échangisme (doctrine) ; "
        "un tarif moyen faible n’exclut pas des pics tarifaires élevés ; efficacité ≠ efficience ; "
        "le paradoxe de Bairoch réfute un automatisme, il ne démontre pas l’efficacité du protectionnisme ; "
        "Stolper-Samuelson ne dit pas que l’ouverture appauvrit un pays, mais qu’elle y crée des perdants."},
  {'k': "Chiffres",
   'v': "Ricardo : 90/100 et 80/120 ; bornes de Mill 0,88 < Pv/d < 1,2 ; droit de douane moyen mondial "
        "40 % (1947), 20 % (1960), 4 % (2019) ; Hawley-Smoot ≈ 50 % (1930) ; GATT 1947, 23 pays ; "
        "OMC 1995 ; droits américains sur la Chine 3,1 % → 21,5 % (2018-2019) ; véhicules électriques "
        "25 % → 100 % ; droit moyen américain 5 % → 23,7 % puis 16,1 % (2025) ; déficits américains 2024 : "
        "Chine 295,4 Md$, UE 235,6, Mexique 171,9, Vietnam 123,5 ; Airbus-Boeing : 7,5 Md$ de rétorsion autorisés (2019)."},
  {'k': "Transitions",
   'v': "Des gains à l’échange à leur répartition (Ricardo → Mill) ; des différences de productivité aux "
        "dotations (Ricardo → HOS) ; des différences entre pays aux similitudes (HOS → Krugman et Linder) ; "
        "de l’efficacité agrégée à l’économie politique de la protection (surplus → Pareto et Léo Charles) ; "
        "de la protection sectorielle à la protection des biens communs (List → Vuillemey et Rodrik)."},
 ],
 'schemas': [
  {'title': "L’enchaînement ricardien", 'tag': "Mécanisme",
   'flow': ["Écarts de productivité", "Coûts d’opportunité différents", "Avantage comparatif",
            "Spécialisation", "Hausse de la production mondiale (4 → 4,325)",
            "Économie de facteurs (30 unités de travail)", "Partage du gain selon le prix international (Mill)"],
   'note': "Ricardo établit l’existence du gain, Mill en détermine la répartition : le prix international doit rester entre les prix relatifs internes."},
  {'title': "Le mécanisme Heckscher-Ohlin-Samuelson", 'tag': "Mécanisme",
   'flow': ["Dotation factorielle relative", "Facteur abondant relativement moins cher",
            "Coût relatif plus faible du bien qui l’utilise intensivement", "Spécialisation et exportation",
            "Hausse de la demande du facteur abondant", "Stolper-Samuelson : gagnants et perdants internes",
            "Tendance à l’égalisation internationale du prix des facteurs"],
   'note': "Deux comparaisons sont indispensables : les rapports de dotations entre pays, et les intensités factorielles entre biens."},
  {'title': "Les rendements croissants et le seuil critique", 'tag': "Mécanisme",
   'flow': ["Implantation initiale", "Volume de production", "Baisse du coût unitaire",
            "Gain de compétitivité", "Attraction de fournisseurs et de main-d’œuvre (Marshall)",
            "Effet d’agglomération", "Avantage comparatif acquis et difficilement réversible"],
   'note': "Un concurrent potentiellement plus efficace peut rester sous le seuil Q0 : c’est ce qui fonde, chez Krugman, la réhabilitation partielle du protectionnisme éducateur."},
  {'title': "Les effets d’un droit de douane", 'tag': "Mécanisme",
   'flow': ["Droit de douane", "Hausse du prix intérieur", "Hausse de la production nationale",
            "Baisse de la consommation et des importations", "Recettes douanières (transfert)",
            "Distorsion à la production", "Distorsion à la consommation", "Perte collective nette (petit pays)"],
   'note': "Seul un grand pays peut compenser ces pertes par un gain de termes de l’échange — au prix de représailles probables."},
  {'title': "L’économie politique de la protection", 'tag': "Mécanisme",
   'flow': ["Gains concentrés sur des producteurs organisés", "Pertes diffuses sur les consommateurs",
            "Asymétrie d’information et de mobilisation (Pareto)", "Constitution d’un bloc social (Léo Charles)",
            "Décision protectionniste", "Représailles", "Dilemme du prisonnier et résultat collectif inférieur"],
   'note': "D’où la nécessité d’institutions — GATT, OMC — ou d’un leader hégémonique pour rendre l’ouverture mutuelle soutenable."},
  {'title': "Du protectionnisme sectoriel au protectionnisme des biens communs", 'tag': "Évolution",
   'flow': ["Protection d’une branche (List, Kaldor)", "Protection d’un champion national (Brander et Spencer)",
            "Protection de l’emploi industriel (Trump I)", "Politique industrielle verte (IRA, CHIPS Act)",
            "Protection environnementale (SEQE, MACF)", "Sécurité des approvisionnements et friend-shoring",
            "Fragmentation géo-économique"],
   'note': "La justification se déplace des intérêts sectoriels vers les biens communs, ce qui rend la protection plus difficile à contester — et plus facile à instrumentaliser."},
 ],
}

# la carte « classique » reprend les branches de la carte visuelle, aplaties
for _b in VMAP['branches']:
    _items = []
    for _s in _b['children']:
        _items.append(_s['title'] + " : " + " ; ".join(_s['children']))
    MAP['branches'].append({'title': _b['title'], 'items': _items})


METHODE = (
 '<div class="nb"><h2>✏️ Méthode — Deuxième année, chapitre 3</h2>'
 '<h3>Réflexes de copie</h3><ul>'
 '<li><strong>Avantage absolu / avantage comparatif</strong> : le premier compare les productivités entre pays, '
 'le second les coûts d’opportunité à l’intérieur de chaque pays. Ne jamais dire que Ricardo « généralise » Smith : '
 'il change de critère.</li>'
 '<li><strong>Fait / doctrine</strong> : libre-échange et protectionnisme sont des situations mesurables ; '
 'libre-échangisme et mercantilisme sont des doctrines. La confusion ruine l’introduction.</li>'
 '<li><strong>Tarif moyen</strong> : 4 % en 2019 ne signifie pas la disparition de la protection — citer les pics '
 'tarifaires, les mesures non tarifaires et les tarifs consolidés, qui mesurent la marge de remontée disponible.</li>'
 '<li><strong>Stolper-Samuelson</strong> : il ne dit pas que l’ouverture appauvrit un pays, mais qu’elle y '
 'redistribue — le facteur relativement rare perd. L’effet est donc de sens opposé au Nord et au Sud.</li>'
 '<li><strong>Efficacité ≠ efficience</strong> : rapporter systématiquement le résultat à son coût (1 000 emplois '
 'pour 200 M€, soit 200 000 € par emploi) avant de conclure qu’une mesure « marche ».</li>'
 '<li><strong>Bairoch</strong> : son paradoxe réfute l’automatisme « ouverture = croissance » ; il n’établit pas '
 'l’inverse. Le dire explicitement évite l’erreur la plus fréquente sur ce point.</li>'
 '<li><strong>Protectionnisme éducateur</strong> : toujours citer les trois conditions — marché intérieur suffisant, '
 'concurrence interne maintenue, protection strictement temporaire. Sans elles, l’argument devient une rente.</li>'
 '<li><strong>Grand pays / petit pays</strong> : le gain de termes de l’échange n’existe que si le pays pèse sur le '
 'prix mondial. Préciser le cas retenu avant de conclure sur le bilan d’un droit de douane.</li>'
 '</ul>'
 '<h3>Couples d’auteurs à mobiliser</h3><ul>'
 '<li>Smith (1776) et Ricardo (1817) : du critère absolu au critère relatif.</li>'
 '<li>Ricardo (1817) et Mill (1848) : de l’existence du gain à son partage.</li>'
 '<li>Heckscher-Ohlin (1919-1933) et Stolper-Samuelson (1941) : des causes du commerce à ses effets distributifs.</li>'
 '<li>Leontief (1953) et R. Baldwin (1971) : de l’anomalie empirique à la redéfinition des facteurs.</li>'
 '<li>Posner (1961) et Vernon (1966) : de l’avance technologique au cycle de vie du produit.</li>'
 '<li>Chamberlin (1933) et Lassudrie-Duchêne : de la structure de marché à la demande de différence.</li>'
 '<li>Marshall (1890) et Krugman (1991) : des externalités locales à l’avantage comparatif acquis.</li>'
 '<li>List (1841) et Krugman : de l’argument historique à sa formalisation par les rendements croissants.</li>'
 '<li>List (1841) et Kaldor (1966) : protéger une industrie naissante ou une industrie vieillissante.</li>'
 '<li>Pareto (1906) et Léo Charles : de l’asymétrie d’organisation au bloc social protectionniste.</li>'
 '<li>Bairoch et Jean-Marc Daniel : l’écart durable entre doctrines proclamées et pratiques effectives.</li>'
 '<li>Vuillemey (2022) et Rodrik (2022) : la protection des biens communs et le paradigme productiviste.</li>'
 '</ul>'
 '<h3>Plans à ne pas reproduire</h3>'
 '<p>Le plan du cours — théories traditionnelles, théories contemporaines, débat — est un plan d’exposition, '
 'pas un plan de dissertation. Une copie qui le recopie décrit au lieu de démontrer. Construire au contraire '
 'la problématique autour d’une tension : gains agrégés contre coûts localisés, efficacité contre équité, '
 'avantage hérité contre avantage construit, règles multilatérales contre rapports de force. Les théories '
 'deviennent alors des arguments et non des étapes chronologiques.</p>'
 '</div>'
)
