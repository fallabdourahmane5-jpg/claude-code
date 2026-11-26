# -*- coding: utf-8 -*-
"""Graphiques de données des chapitres 21 et 24."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre)

L = []

# ------------------------------- part de valeur ajoutée domestique (ch. 21)
VAD = [(0.03, 0.88), (0.12, 0.87), (0.22, 0.84), (0.32, 0.79), (0.42, 0.72),
       (0.52, 0.64), (0.62, 0.56), (0.72, 0.50), (0.82, 0.46), (0.92, 0.44),
       (0.99, 0.44)]

L.append(fiche(
 id='va-domestique-exportations',
 t='La part domestique du « made in »',
 st='Ce que nos exportations contiennent encore de production nationale.',
 cat='inter', an=2, ch=['21'],
 type='donnees',
 q='Que mesure la valeur ajoutée intérieure contenue dans les exportations, '
   'et que révèle sa baisse depuis les années 1960 ?',
 axes={'x': 'Années', 'y': 'Part de valeur ajoutée domestique',
       'yu': '% de la valeur exportée',
       'gx': [[0.03, '1960'], [0.35, '1980'], [0.67, '2000'],
              [0.99, 'aujourd’hui']],
       'gy': [[0.44, '≈ 70 %'], [0.88, '85-90 %']]},
 depart='Les principales économies européennes dans les années 1960, dont les '
        'exportations étaient encore très largement produites sur place.',
 hyp=['La valeur ajoutée intérieure des exportations mesure la part de la '
      'valeur exportée qui a réellement été produite sur le territoire '
      'national.',
      'Une valeur ajoutée intérieure élevée signifie beaucoup de production '
      'domestique ; une valeur ajoutée intérieure faible, une forte '
      'dépendance aux intrants étrangers.',
      'Le cours ne chiffre que les deux extrémités de la période : la '
      'trajectoire intermédiaire est une allure.'],
 pente=[{'s': 'Courbe décroissante', 'd': 'elle traduit l’internationalisation '
         'croissante des processus productifs : une part grandissante de ce '
         'que l’on exporte a d’abord été importée.'}],
 src={'so': 'Cours de deuxième année, chapitre 1 — données commentées au '
            'point sur la baisse du « made in » domestique dans les '
            'principales économies européennes.',
      'pe': 'années 1960 — période récente',
      'un': 'part, en pourcentage, de la valeur ajoutée produite sur le '
            'territoire national dans la valeur totale des exportations',
      'nb': 'Deux repères seulement sont chiffrés par le cours : environ '
            '85 à 90 % dans les années 1960 et près de 70 % aujourd’hui. La '
            'pente intermédiaire ne doit pas être lue comme une série '
            'annuelle.'},
 fig={'series': [
   pol('va', 'Valeur ajoutée domestique', VAD, 'ac', ep=3.4, lp=[0.70, 0.64]),
 ]},
 etapes=[
  etape('Ce que mesure l’indicateur',
        'Il indique quelle fraction de la valeur exportée a réellement été '
        'produite sur le territoire national. Le reste correspond à des '
        'intrants achetés à l’étranger et simplement réexportés après '
        'transformation.',
        on=['va'], vif=['va']),
  etape('Le point de départ : 85 à 90 % dans les années 1960',
        'À cette époque, l’essentiel de ce qu’une économie européenne '
        'exportait avait été produit chez elle. Le « made in » national '
        'correspondait à peu près à la réalité.',
        add=[pt('a', '', 0.03, 0.88, 'ok'),
             rep('ra', 0.03, 0.88, c='ok')],
        vif=['a', 'ra']),
  etape('Le point d’arrivée : près de 70 % aujourd’hui',
        'Près d’un tiers de la valeur exportée vient désormais de '
        'l’étranger. La baisse est continue et traduit '
        'l’internationalisation croissante des processus productifs.',
        add=[pt('b', '', 0.99, 0.44, 'ko'),
             rep('rb', 0.99, 0.44, c='ko')],
        vif=['b', 'rb']),
  etape('La contrepartie : l’efficacité',
        'Cette fragmentation permet à chaque étape d’être réalisée là où elle '
        'coûte le moins. L’interdépendance est d’abord une source '
        'd’efficacité : c’est la logique même des chaînes de valeur '
        'mondiales.',
        add=[txt('te', 'interdépendance = efficacité…', 0.3, 0.3, 'ok',
                 taille=15, gras=True)],
        vif=['te']),
  etape('Mais aussi la vulnérabilité',
        'La même interdépendance est une source de vulnérabilité : une '
        'rupture d’approvisionnement en intrants étrangers paralyse la '
        'production nationale. La dépendance devient stratégique lorsqu’elle '
        'porte sur des matériaux critiques.',
        add=[txt('tv', '… et vulnérabilité', 0.46, 0.2, 'ko', taille=15,
                 gras=True)],
        vif=['tv']),
  etape('Pourquoi ce graphique éclaire la « démondialisation »',
        'C’est cette dépendance mesurée que les politiques de substitution '
        'aux importations, de filtrage des investissements étrangers ou de '
        'relocalisation cherchent à réduire depuis 2008.',
        add=[txt('td', 'ce que la démondialisation cherche à inverser',
                 0.16, 0.95, 'bl', taille=15, gras=True)],
        off=['te', 'tv'],
        vif=['td']),
 ],
 pieges=[
  {'t': 'Une part, pas un volume',
   'd': 'La part domestique baisse alors que les exportations totales '
        'augmentent : la valeur produite sur place peut très bien croître en '
        'volume. Conclure à une désindustrialisation à partir de ce seul '
        'graphique serait abusif.'},
  {'t': 'Deux repères ne font pas une série',
   'd': 'Le cours chiffre le début et la fin de la période. La régularité de '
        'la pente intermédiaire est une commodité de tracé, pas une donnée.'},
  {'t': 'Dépendance n’est pas faiblesse',
   'd': 'Le cours insiste sur la double lecture : la même interdépendance est '
        'source d’efficacité et de vulnérabilité. Ne retenir qu’un des deux '
        'versants donne un commentaire orienté.'},
 ],
 main=[
  'Trace les axes : les années en abscisse, la part de valeur ajoutée '
  'domestique en pourcentage en ordonnée — écris l’unité.',
  'Place le repère de départ en haut à gauche, entre 85 et 90 %.',
  'Place le repère d’arrivée à droite, vers 70 %.',
  'Relie-les par une courbe régulièrement décroissante et annote la pente : '
  'internationalisation des processus productifs.',
  'Écris en marge les deux lectures : efficacité et vulnérabilité.',
 ],
 phrase='La part de valeur ajoutée domestique dans les exportations des '
        'principales économies européennes est passée d’environ 85 à 90 % '
        'dans les années 1960 à près de 70 % aujourd’hui : cette baisse '
        'mesure l’internationalisation des processus productifs, qui est à la '
        'fois une source d’efficacité et une source de vulnérabilité '
        'lorsqu’elle porte sur des intrants difficilement substituables.',
 liens=[{'c': '21', 'b': 3811, 'l': 'La hausse de la valeur ajoutée étrangère dans les exportations'},
        {'c': '21', 'b': 3812, 'l': 'Une baisse du « made in » domestique'},
        {'c': '21', 'b': 3821, 'l': 'Les matériaux critiques : une vulnérabilité stratégique'},
        {'c': '21', 'b': 6316, 'l': 'Les deux sens du mot démondialisation'}],
 mots=['chaîne de valeur', 'valeur ajoutée domestique', 'DIPP',
       'démondialisation', 'vulnérabilité', 'intrants'],
))

# ------------------------------------ protection agricole et industrielle
L.append(fiche(
 id='droits-douane-secteurs',
 t='L’agriculture, secteur le plus protégé',
 st='Cinq fois plus de droits de douane que l’industrie.',
 cat='inter', an=2, ch=['24'],
 type='donnees',
 q='Pourquoi l’agriculture constitue-t-elle une exception majeure à la '
   'libéralisation commerciale multilatérale ?',
 axes={'x': 'Secteurs', 'y': 'Droit de douane moyen',
       'yu': 'en % de la valeur importée',
       'gy': [[0.14, '3 %'], [0.74, '15,9 %']]},
 depart='Le niveau moyen de protection tarifaire atteint dans le monde après '
        'plusieurs décennies de négociations multilatérales.',
 hyp=['Les droits de douane comparés sont des moyennes mondiales par secteur, '
      'mesurées en 2019.',
      'Une moyenne masque de fortes disparités : le cours précise que les '
      'droits peuvent être concentrés dans certains secteurs '
      'particulièrement sensibles.',
      'Le graphique compare des secteurs, pas des pays : les écarts entre '
      'niveaux de développement sont une autre dimension.'],
 pente=[{'s': 'Lecture des barres', 'd': 'ce graphique ne possède pas de '
         'pente : il compare deux niveaux. Toute l’information tient dans '
         'leur rapport, d’environ un à cinq.'}],
 src={'so': 'Cours de deuxième année, chapitre 4 — tableau des droits de '
            'douane moyens par secteur, commenté au point sur l’agriculture '
            'comme exception à la libéralisation.',
      'pe': '2019',
      'un': 'droit de douane moyen, en pourcentage de la valeur importée',
      'nb': 'Le cours donne deux moyennes mondiales. Il précise par ailleurs '
            'que le graphique d’origine distingue aussi les niveaux de '
            'développement, dimension que ces deux chiffres ne restituent '
            'pas.'},
 fig={'series': [
   barre('ba', '', 0.26, 0.74, 0.16, 'ac2'),
   barre('bi', '', 0.68, 0.14, 0.16, 'ac'),
   txt('la', 'Agriculture mondiale', 0.08, -0.08, 'ac2', taille=15,
       gras=True),
   txt('li', 'Industrie mondiale', 0.54, -0.08, 'ac', taille=15, gras=True),
 ]},
 etapes=[
  etape('L’agriculture : 15,9 % en moyenne',
        'C’est le secteur le plus protégé du commerce mondial. Après des '
        'décennies de négociations multilatérales, la protection tarifaire y '
        'reste élevée.',
        on=['ba', 'la'],
        add=[txt('va', '15,9 %', 0.21, 0.78, 'ac2', taille=17, gras=True)],
        vif=['ba', 'va']),
  etape('L’industrie : 3 % en moyenne',
        'Le contraste est net : les droits de douane industriels sont environ '
        'cinq fois plus faibles. La libéralisation a donc très inégalement '
        'progressé selon les secteurs.',
        on=['bi', 'li'],
        add=[txt('vi', '3 %', 0.655, 0.18, 'ac', taille=17, gras=True),
             fl('fr', '× 5 environ', 0.4, 0.5, 0.6, 0.26, 'ok')],
        vif=['bi', 'vi', 'fr']),
  etape('Pourquoi l’agriculture résiste',
        'Elle porte plusieurs enjeux que les négociateurs refusent de laisser '
        'au seul marché : sécurité alimentaire, maintien des revenus '
        'agricoles, stabilité des territoires ruraux, souveraineté, '
        'protection contre la volatilité des prix mondiaux.',
        add=[txt('t1', 'sécurité alimentaire · revenus agricoles',
                 0.08, 0.95, 'jn', taille=14, gras=True),
             txt('t2', 'territoires ruraux · souveraineté · volatilité',
                 0.08, 0.88, 'jn', taille=14, gras=True)],
        off=['fr'],
        vif=['t1', 't2']),
  etape('Une exception ancienne, pas récente',
        'Cette protection ne constitue pas un phénomène récent : elle '
        's’inscrit dans une longue tradition d’intervention publique, aux '
        'États-Unis puis en Europe.',
        add=[txt('t3', 'une longue tradition d’intervention publique',
                 0.1, 0.6, 'bl', taille=15, gras=True)],
        off=['t1', 't2'],
        vif=['t3']),
  etape('Ce que ces deux chiffres ne montrent pas',
        'Le graphique d’origine distingue aussi les niveaux de '
        'développement : la protection n’est pas la même partout. Deux '
        'moyennes mondiales ne disent rien de cette dispersion.',
        add=[txt('t4', 'deux moyennes ne disent rien de la dispersion',
                 0.06, 0.95, 'ko', taille=15, gras=True)],
        off=['t3'],
        vif=['t4']),
 ],
 pieges=[
  {'t': 'Un droit de douane moyen n’est pas le droit appliqué',
   'd': 'Une moyenne agrège des lignes tarifaires très différentes : '
        'certains produits agricoles supportent des droits bien supérieurs à '
        '15,9 %, d’autres sont libres.'},
  {'t': 'Protection tarifaire n’est pas protection totale',
   'd': 'Les droits de douane ne sont qu’un instrument parmi d’autres : '
        'quotas, normes et subventions protègent également, sans apparaître '
        'dans ce graphique.'},
  {'t': 'Comparer des secteurs, pas des pays',
   'd': 'Ces deux chiffres sont des moyennes mondiales. En tirer une '
        'conclusion sur la politique commerciale d’un pays donné serait une '
        'extrapolation.'},
 ],
 main=[
  'Trace les axes : les secteurs en abscisse, le droit de douane moyen en '
  'pourcentage en ordonnée — écris l’unité et l’année.',
  'Dessine une barre haute pour l’agriculture et inscris 15,9 % au-dessus.',
  'Dessine une barre environ cinq fois plus basse pour l’industrie et inscris '
  '3 %.',
  'Relie les deux par une flèche portant le rapport, environ cinq.',
  'Écris en marge les cinq justifications de la protection agricole.',
 ],
 phrase='Avec un droit de douane moyen de 15,9 % en 2019 contre 3 % pour '
        'l’industrie, l’agriculture demeure environ cinq fois plus protégée '
        'et constitue l’exception majeure à la libéralisation commerciale '
        'multilatérale, parce qu’elle porte des enjeux de sécurité '
        'alimentaire, de revenus agricoles, de stabilité des territoires '
        'ruraux et de souveraineté que les États refusent de confier au seul '
        'marché.',
 liens=[{'c': '24', 'b': 963, 'l': 'L’agriculture, exception majeure à la libéralisation'},
        {'c': '24', 'b': 964, 'l': 'L’agriculture demeure beaucoup plus protégée que l’industrie'},
        {'c': '24', 'b': 979, 'l': 'La lecture du graphique du cours'},
        {'c': '24', 'b': 980, 'l': 'Une protection ancienne'}],
 mots=['droits de douane', 'protectionnisme', 'agriculture', 'OMC', 'GATT',
       'sécurité alimentaire', 'libéralisation'],
))
