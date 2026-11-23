# -*- coding: utf-8 -*-
"""Chapitre 24 — corrections des questions héritées, sous-parties c24-07 à c24-11."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c24-07
'ch24-qcm-25': f(niv='connaitre', sp='c24-07', b=1374,
 exp="Vingt-trois pays signent le GATT en 1947. Ce nombre est un repère "
     "central du chapitre, car il mesure l’élargissement ultérieur du "
     "système : 48 participants au Kennedy Round, 99 au Tokyo Round, 106 au "
     "lancement de l’Uruguay Round et 123 à sa conclusion, enfin 166 membres "
     "de l’OMC en 2026. Il ne faut pas le confondre avec les 44 pays de la "
     "conférence de Bretton Woods en 1944.",
 why=["44 pays participent à la conférence de Bretton Woods de 1944.",
      "48 participants concernent le Kennedy Round (1964-1967).",
      "99 participants concernent le Tokyo Round (1973-1979)."]),
'ch24-qcm-44': f(niv='connaitre', sp='c24-07', b=1240,
 why=["1962 est l’année de la mise en œuvre de la PAC.",
      "1986 est l’année du lancement de l’Uruguay Round.",
      "1995 est l’année de création de l’OMC, qui organise au contraire le "
      "démantèlement de cet accord."]),
'ch24-qcm-45': f(niv='connaitre', sp='c24-07', b=1255,
 why=["Le 1er janvier 1995 marque l’entrée en vigueur de l’accord sur les "
      "textiles et les vêtements, point de départ du démantèlement et non son "
      "terme.",
      "Le 1er janvier 2001 ne correspond à aucune étape de ce calendrier.",
      "Le 1er janvier 2010 est postérieur de cinq ans à l’intégration "
      "complète du secteur."],
 diss="Exemple parfait d’une exception durable : il faut trente ans — de 1974 "
      "à 2005 — pour revenir au droit commun."),
'ch24-qcm-47': f(niv='comprendre', sp='c24-07', b=1219,
 why=["La baisse des droits de douane se poursuit, mais elle n’est plus "
      "l’apport essentiel de ce cycle.",
      "L’agriculture n’est intégrée qu’avec l’Uruguay Round.",
      "L’Organe de règlement des différends est créé en 1995 avec l’OMC."],
 diss="Évolution à souligner : lorsque les tarifs sont déjà bas, la "
      "négociation se déplace vers les obstacles non tarifaires, plus "
      "difficiles à mesurer."),
'ch24-qcm-48': f(niv='connaitre', sp='c24-07', b=1374,
 why=["48 participants concernent le Kennedy Round.",
      "99 participants concernent le Tokyo Round.",
      "166 est le nombre de membres de l’OMC en 2026."]),
'ch24-qcm-49': f(niv='comprendre', sp='c24-07', b=1332,
 why=["Le choix sélectif des concessions est exactement ce que l’engagement "
      "unique interdit.",
      "L’engagement unique ne limite pas le nombre de cycles.",
      "Il ne concerne pas la représentation des États mais le contenu de "
      "l’accord."],
 diss="Ambivalence à exploiter : l’engagement unique protège les pays en "
      "développement d’une libéralisation à la carte, mais il multiplie les "
      "possibilités de blocage."),
'ch24-qcm-50': f(niv='comprendre', sp='c24-07', b=1263,
 why=["L’OMC est créée en 1995, quatre ans avant Seattle.",
      "Le cycle de Doha est lancé en 2001.",
      "L’Uruguay Round est conclu en 1994."],
 diss="Point remarquable : PED, pays développés et mouvements "
      "altermondialistes critiquent simultanément l’OMC, mais pour des "
      "raisons opposées."),
'ch24-qcm-52': f(niv='connaitre', sp='c24-07', b=1374,
 why=["123 est le nombre de participants à la conclusion de l’Uruguay "
      "Round.",
      "150 ne correspond à aucun repère du cours.",
      "190 est proche du nombre de membres du FMI, non de l’OMC."]),
'ch24-vraifa-106': f(niv='connaitre', sp='c24-07', b=1363),
'ch24-vraifa-115': f(niv='comprendre', sp='c24-07', b=1240),
'ch24-questi-128': f(niv='connaitre', sp='c24-07', b=1374),
'ch24-questi-129': f(niv='raisonner', sp='c24-07', b=1308),
'ch24-questi-130': f(niv='raisonner', sp='c24-07', b=1374),

# =============================================================== c24-08
'ch24-qcm-51': f(niv='raisonner', sp='c24-08', b=1448,
 why=["La réduction des droits de douane compte pour environ 25 % : réelle, "
      "mais minoritaire.",
      "La baisse des coûts de transport compte pour environ 8 %, "
      "essentiellement par la conteneurisation.",
      "La création du GATT n’est pas un facteur quantifié dans cette "
      "décomposition : son effet passe par les droits de douane."],
 diss="Prudence causale indispensable : la libéralisation accompagne la "
      "croissance du commerce plus qu’elle ne l’explique à elle seule."),

# =============================================================== c24-09
'ch24-qcm-53': f(niv='connaitre', sp='c24-09', b=1627,
 why=["181 correspond aux notifications concernant l’Europe.",
      "642 est le nombre total d’accords notifiés à l’OMC, en vigueur ou "
      "non.",
      "166 est le nombre de membres de l’OMC."],
 diss="Contraste frappant à exploiter : 388 accords régionaux en vigueur "
      "pendant que la négociation multilatérale est à l’arrêt."),
'ch24-qcm-54': f(niv='connaitre', sp='c24-09', b=1723,
 why=["Le tarif extérieur commun caractérise l’union douanière, étape "
      "suivante.",
      "La monnaie commune correspond à l’union économique et monétaire.",
      "Le transfert à une autorité supranationale correspond à l’intégration "
      "totale."],
 diss="Conséquence technique majeure : parce que les tarifs extérieurs "
      "diffèrent, une zone de libre-échange a besoin de règles d’origine."),
'ch24-qcm-55': f(niv='comprendre', sp='c24-09', b=1683,
 why=["Une simple zone de libre-échange laisserait à la France sa propre "
      "politique commerciale, ce qui n’est pas le cas.",
      "L’intégration totale au sens de Balassa supposerait l’unification des "
      "principales politiques économiques sous une autorité supranationale.",
      "L’Union dispose au contraire d’institutions communes très "
      "développées."],
 diss="Exemple concret à citer : la France ne décide pas seule des droits de "
      "douane applicables aux produits extérieurs."),
'ch24-qcm-56': f(niv='connaitre', sp='c24-09', b=1787,
 why=["L’union douanière est la deuxième étape.",
      "Le marché commun est la troisième.",
      "L’union économique et monétaire est la quatrième."],
 diss="Les cinq étapes dans l’ordre : zone de libre-échange, union "
      "douanière, marché commun, union économique et monétaire, intégration "
      "totale."),
'ch24-questi-131': f(niv='connaitre', sp='c24-09', b=1683),

# =============================================================== c24-10
'ch24-qcm-57': f(niv='comprendre', sp='c24-10', b=1827,
 why=["La hausse des échanges avec les pays tiers n’est pas l’objet de cette "
      "notion, qui porte sur les échanges intra-zone.",
      "Le remplacement d’un fournisseur extérieur efficace par un partenaire "
      "moins efficace définit au contraire le détournement de trafic.",
      "La hausse des recettes douanières n’est pas un effet de la création de "
      "trafic : l’union les réduit à l’intérieur de la zone."],
 diss="Critère d’évaluation à retenir : la création de trafic améliore "
      "l’allocation des ressources, le détournement la dégrade."),
'ch24-qcm-58': f(niv='comprendre', sp='c24-10', b=1881,
 why=["Les droits de douane sur les produits internes sont au contraire "
      "supprimés.",
      "Les échanges intra-zone augmentent, loin de disparaître.",
      "Aucune interdiction d’importer n’est en cause : c’est la préférence "
      "tarifaire qui déplace la demande."],
 diss="Mécanisme à expliciter : prix du partenaire sans droit < prix du "
      "fournisseur mondial majoré du droit, alors même que ce dernier est "
      "plus efficace."),
'ch24-qcm-59': f(niv='raisonner', sp='c24-10', b=1881,
 why=["La hausse des échanges intra-zone ne prouve rien : le détournement de "
      "trafic les augmente aussi.",
      "Le niveau du tarif extérieur commun n’est pas le critère : il peut "
      "même aggraver le détournement.",
      "L’homogénéité des niveaux de développement n’est pas une condition de "
      "l’amélioration du bien-être."],
 diss="Erreur classique à éviter absolument : conclure d’une hausse du "
      "commerce intra-zone au succès de l’accord."),
'ch24-qcm-61': f(niv='connaitre', sp='c24-10', b=1929,
 why=["De 2 % à 4 % sous-estime à la fois le niveau initial et le niveau "
      "actuel.",
      "De 8 % à 15 % surestime fortement la progression.",
      "Un recul de 10 % à 8 % inverserait la dynamique observée."],
 diss="Enseignement à tirer : l’intégration régionale y a accompagné, et non "
      "remplacé, une forte insertion mondiale."),
'ch24-qcm-62': f(niv='connaitre', sp='c24-10', b=1995,
 why=["5 % sous-estime nettement la part observée en 2020.",
      "26,8 % est la projection pour 2045 avec la ZLECAf, non la situation de "
      "2020.",
      "40 % dépasse même les projections les plus favorables."],
 diss="Comparaison utile : le commerce intra-africain reste très inférieur au "
      "commerce intra-européen ou intra-asiatique."),
'ch24-qcm-63': f(niv='raisonner', sp='c24-10', b=2016,
 why=["La volonté politique existe : la ZLECAf a précisément été négociée et "
      "ratifiée.",
      "L’OMC n’interdit pas les accords régionaux, qui dérogent à la NPF par "
      "l’article XXIV.",
      "Des droits de douane existent bien et leur suppression est l’objet de "
      "l’accord."],
 diss="Leçon générale : la libéralisation ne crée pas la complémentarité "
      "productive — il y faut aussi des infrastructures et des "
      "spécialisations différentes."),
'ch24-vraifa-117': f(niv='raisonner', sp='c24-10', b=2016),
'ch24-questi-132': f(niv='raisonner', sp='c24-10', b=1827),

# =============================================================== c24-11
'ch24-qcm-64': f(niv='connaitre', sp='c24-11', b=2109,
 why=["La suppression des droits de douane et des quotas définit "
      "l’intégration superficielle.",
      "La monnaie commune relève de l’union monétaire, étape de la typologie "
      "de Balassa.",
      "Le tarif extérieur commun caractérise l’union douanière."],
 diss="Distinction de Lawrence très rentable : superficielle aux frontières, "
      "profonde à l’intérieur des réglementations."),
'ch24-qcm-65': f(niv='connaitre', sp='c24-11', b=2066,
 why=["La limitation aux seuls droits de douane est précisément ce que cet "
      "accord dépasse.",
      "L’Union européenne ne renonce pas à ses normes sanitaires : elle "
      "cherche au contraire à les diffuser.",
      "Les investissements font partie des domaines couverts par les accords "
      "profonds."],
 diss="Exemple concret d’un accord commercial devenu instrument de diffusion "
      "normative : liberté syndicale, droits des travailleurs, conventions "
      "fondamentales de l’OIT."),
'ch24-qcm-66': f(niv='comprendre', sp='c24-11', b=2176,
 why=["L’industrie automobile européenne espère au contraire un meilleur "
      "accès au marché sud-américain.",
      "Les exportateurs de vins et spiritueux figurent parmi les "
      "bénéficiaires attendus.",
      "Les consommateurs sud-américains ne sont pas à l’origine de "
      "l’opposition décrite."],
 diss="Structure du conflit à nommer : l’accord redistribue entre secteurs "
      "d’un même pays, d’où une opposition interne et non entre nations."),
'ch24-qcm-67': f(niv='raisonner', sp='c24-11', b=2172,
 why=["Le niveau des droits de douane n’est pas l’objet de ce débat, qui "
      "porte sur les règles de production.",
      "La monnaie de facturation n’intervient pas dans cette discussion.",
      "Le nombre de signataires est sans rapport avec la question des "
      "normes."],
 diss="Formulation précise à retenir : le débat porte sur l’équivalence des "
      "procédés de production, non sur celle du produit fini."),
'ch24-qcm-68': f(niv='connaitre', sp='c24-11', b=2186,
 why=["Baldwin illustre l’image en 2008 avec le cas de l’Amérique latine, "
      "mais il ne l’a pas créée.",
      "Viner analyse la création et le détournement de trafic.",
      "Balassa propose la typologie des étapes de l’intégration."]),
'ch24-qcm-69': f(niv='comprendre', sp='c24-11', b=2240,
 why=["Un accord n’entraîne pas la dissolution des autres : ils se "
      "superposent, d’où le bol de spaghettis.",
      "Les accords régionaux ne deviennent pas nécessairement des unions "
      "douanières.",
      "Les pays tiers subissent au contraire un désavantage relatif, ce qui "
      "les pousse à conclure à leur tour."],
 diss="Mécanisme auto-entretenu à exploiter : plus les blocs se forment, plus "
      "l’exclusion coûte cher, plus les accords se multiplient."),
'ch24-qcm-70': f(niv='raisonner', sp='c24-11', b=2267,
 why=["Le retrait américain de l’OMC n’est pas ce que désigne "
      "l’expression.",
      "Il ne s’agit pas d’accords secrets mais d’accords publics et "
      "notifiés.",
      "La clause NPF n’est pas supprimée : elle est contournée par les "
      "exceptions de l’article XXIV."],
 diss="Image de Baldwin à citer : un ordre commercial en « système solaire », "
      "où les grandes puissances réglementaires forment les centres."),
'ch24-questi-133': f(niv='raisonner', sp='c24-11', b=2107),
'ch24-questi-134': f(niv='connaitre', sp='c24-11', b=2220),

}
