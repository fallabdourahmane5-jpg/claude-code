# -*- coding: utf-8 -*-
"""Courbes du chapitre 4 — analyse microéconomique (I) : le consommateur."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     hyper, concave, courbe_dec, inter, y_de, x_de, bouge)

L = []

# ------------------------------------------------- utilité et loi de Gossen
UT = concave(0.04, 0.06, 0.96, 0.9, n=13, force=0.46)
UM = [(0.04, 0.9), (0.14, 0.72), (0.25, 0.58), (0.37, 0.46), (0.5, 0.36),
      (0.63, 0.27), (0.76, 0.2), (0.88, 0.15), (0.96, 0.12)]

L.append(fiche(
 id='utilite-gossen',
 t='Utilité totale et utilité marginale',
 st='Pourquoi la satisfaction augmente toujours, mais de moins en moins vite.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Comment la satisfaction d’un consommateur évolue-t-elle quand il consomme '
   'une unité supplémentaire d’un même bien, et que signifie la loi de '
   'Gossen ?',
 axes={'x': 'Quantité consommée du bien X', 'y': 'Utilité'},
 depart='Un consommateur qui augmente progressivement la quantité consommée '
        'd’un seul bien, les autres restant inchangés.',
 hyp=['On raisonne sur un seul bien : la courbe d’utilité est un outil '
      'unidimensionnel, à ne pas confondre avec la courbe d’indifférence, qui '
      'porte sur deux biens.',
      'L’hypothèse de non-satiété est retenue : le consommateur préfère '
      'toujours plus de biens à moins de biens, et n’atteint jamais le point '
      'de satiété.',
      'Le bien est supposé parfaitement divisible, ce qui permet de raisonner '
      'sur des variations infinitésimales.'],
 pente=[{'s': 'Utilité totale', 'd': 'croissante mais concave : la pente '
         'reste positive — on gagne toujours de la satisfaction — mais elle '
         'diminue à mesure que la quantité augmente.'},
        {'s': 'Utilité marginale', 'd': 'décroissante : c’est exactement la '
         'pente de la courbe d’utilité totale, et cette pente s’aplatit. '
         'C’est la loi de Gossen.'}],
 fig={'series': [
   pol('ut', 'Utilité totale', UT, 'ac', ep=3.4),
 ]},
 variantes=[
  {'lib': 'Utilité totale',
   'axes': {'y': 'Utilité totale'},
   'etapes': [
     etape('Une courbe croissante',
           'Plus le consommateur consomme de X, plus son utilité totale '
           'augmente. L’hypothèse de non-satiété interdit qu’elle cesse de '
           'croître : il n’existe pas de courbe maximale.',
           on=['ut'], vif=['ut']),
     etape('Mais une courbe concave',
           'Elle croît de moins en moins vite : la courbe s’infléchit vers le '
           'bas. C’est la concavité, et c’est elle qui porte toute '
           'l’information économique.',
           add=[fl('f1', 'forte hausse', 0.08, 0.22, 0.2, 0.46, 'ok'),
                fl('f2', 'faible hausse', 0.76, 0.78, 0.9, 0.85, 'ko')],
           vif=['f1', 'f2']),
     etape('La pente se lit en deux points',
           'Entre les deux premières unités, le gain d’utilité est important ; '
           'entre les deux dernières, il est faible. Le même ajout de '
           'quantité ne rapporte plus la même satisfaction.',
           add=[rep('r1', 0.2, round(UT[2][1], 4), c='ok'),
                rep('r2', 0.9, round(UT[11][1], 4), c='ko')],
           vif=['r1', 'r2']),
     etape('Le point de satiété reste théorique',
           'Il existerait une quantité à partir de laquelle consommer plus '
           'n’augmenterait plus l’utilité : la courbe deviendrait horizontale. '
           'La microéconomie standard suppose qu’on ne l’atteint jamais.',
           add=[lin('sat', 'point de satiété (exclu par hypothèse)',
                    0.6, 0.95, 0.98, 0.95, 'gr', ep=2)],
           vif=['sat']),
   ]},
  {'lib': 'Utilité marginale',
   'axes': {'y': 'Utilité marginale'},
   'etapes': [
     etape('Ce que mesure l’utilité marginale',
           'C’est l’utilité supplémentaire apportée par la consommation d’une '
           'unité supplémentaire du bien : non pas la satisfaction totale, '
           'mais le gain apporté par la dernière unité.',
           on=[],
           add=[pol('um', 'Utilité marginale', UM, 'ac2', ep=3.4)],
           vif=['um']),
     etape('Elle est décroissante : c’est la loi de Gossen',
           'Chaque unité supplémentaire apporte moins de satisfaction que la '
           'précédente. Le premier verre d’eau d’un assoiffé vaut beaucoup '
           'plus que le cinquième.',
           add=[fl('fg', 'loi de Gossen', 0.22, 0.66, 0.62, 0.34, 'ko')],
           vif=['fg']),
     etape('Décroissante ne veut pas dire négative',
           'L’utilité marginale diminue, mais elle reste positive : c’est '
           'pour cela que l’utilité totale continue d’augmenter. Tant que le '
           'gain marginal est positif, le total monte.',
           add=[txt('tp', 'Um > 0 : le total continue de croître',
                    0.3, 0.76, 'ok', taille=15, gras=True)],
           vif=['tp', 'um']),
     etape('Le lien entre les deux courbes',
           'L’utilité marginale est la pente de la courbe d’utilité totale. '
           'Comme cette pente diminue, la courbe d’utilité totale est '
           'croissante mais concave : les deux graphiques disent la même '
           'chose.',
           add=[txt('tl', 'Um = pente de Ut', 0.42, 0.86, 'ac', taille=16,
                    gras=True)],
           vif=['tl']),
   ]},
 ],
 pieges=[
  {'t': 'Courbe d’utilité ≠ courbe d’indifférence',
   'd': 'La courbe d’utilité porte en abscisse la quantité d’un seul bien et '
        'en ordonnée l’utilité : c’est un outil unidimensionnel. La courbe '
        'd’indifférence porte deux biens sur les deux axes : c’est un outil '
        'bidimensionnel. Confondre les deux rend toute lecture impossible.'},
  {'t': 'Utilité totale qui monte, utilité marginale qui baisse',
   'd': 'Ce n’est pas une contradiction : le total augmente précisément parce '
        'que chaque unité apporte encore quelque chose, seulement de moins en '
        'moins. Dire « l’utilité diminue » sans préciser laquelle est la '
        'faute la plus fréquente.'},
  {'t': 'La non-satiété est une hypothèse, pas un constat',
   'd': 'Elle est nécessaire pour des raisons mathématiques — sans elle les '
        'courbes d’indifférence pourraient devenir discontinues ou mal '
        'ordonnées. Des économistes comme Kate Raworth la contestent au nom '
        'des limites écologiques.'},
 ],
 main=[
  'Trace les axes : la quantité du bien X en abscisse, l’utilité en ordonnée.',
  'Trace une courbe croissante que tu infléchis progressivement vers le bas : '
  'c’est l’utilité totale, croissante et concave.',
  'Marque deux paires de pointillés, une au début et une à la fin, pour '
  'montrer que le même ajout de quantité rapporte moins.',
  'Sur un second repère, trace une courbe décroissante qui reste au-dessus de '
  'l’axe : c’est l’utilité marginale.',
  'Écris sous les deux graphiques : « l’utilité marginale est la pente de '
  'l’utilité totale ».',
 ],
 phrase='La loi de Gossen énonce que l’utilité marginale est décroissante : '
        'chaque unité supplémentaire consommée apporte une satisfaction '
        'moindre que la précédente, de sorte que la courbe d’utilité totale '
        'est croissante mais concave, sa pente — qui est précisément '
        'l’utilité marginale — s’aplatissant à mesure que la consommation '
        'augmente.',
 liens=[{'c': '4', 'b': 104, 'l': 'La courbe d’utilité et ses axes'},
        {'c': '4', 'b': 114, 'l': 'L’utilité marginale et la loi de Gossen'},
        {'c': '4', 'b': 123, 'l': 'Le lien entre utilité totale et utilité marginale'},
        {'c': '4', 'b': 29, 'l': 'L’hypothèse de non-satiété et ses critiques'}],
 mots=['utilité', 'utilité marginale', 'Gossen', 'non-satiété', 'concavité',
       'marginalisme'],
))

# ---------------------------------------- courbes d'indifférence et budget
U0 = [p for p in hyper(0.166, 0.185, 0.97, 17) if p[1] <= 1.05]
U1 = [p for p in hyper(0.2568, 0.27, 0.97, 17) if p[1] <= 1.05]
UB = [p for p in hyper(0.10, 0.115, 0.97, 17) if p[1] <= 1.05]
B0 = (0.07, 0.90, 0.62, 0.06)

L.append(fiche(
 id='indifference-budget',
 t='Courbes d’indifférence et contrainte de budget',
 st='Le programme du consommateur : maximiser son utilité sous contrainte.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Comment un consommateur choisit-il la combinaison de deux biens qui lui '
   'procure la plus grande satisfaction compte tenu de son revenu ?',
 axes={'x': 'Quantité du bien X', 'y': 'Quantité du bien Y'},
 depart='Un consommateur qui arbitre entre deux biens X et Y, avec un revenu '
        'donné et des prix donnés.',
 hyp=['Complétude : le consommateur peut toujours se prononcer sur n’importe '
      'quelle combinaison de biens.',
      'Transitivité : ses choix sont logiquement cohérents — c’est ce qui '
      'interdit aux courbes d’indifférence de se croiser.',
      'Non-satiété : une courbe plus éloignée de l’origine correspond '
      'toujours à une utilité plus élevée.',
      'Continuité et divisibilité des biens : les courbes sont lisses, sans '
      'marches d’escalier, ce qui permet de les dériver et d’optimiser.'],
 pente=[{'s': 'Courbe d’indifférence', 'd': 'décroissante et convexe : pour '
         'rester au même niveau de satisfaction, consommer plus de X oblige à '
         'renoncer à du Y. Sa pente en un point est le taux marginal de '
         'substitution, négatif par construction.'},
        {'s': 'Droite de budget', 'd': 'décroissante, de pente égale à '
         'l’opposé du rapport des prix : elle délimite ce que le revenu '
         'permet d’acheter.'},
        {'s': 'TMS décroissant', 'd': 'plus on consomme de X, moins on '
         'accepte de renoncer à du Y pour une unité de X supplémentaire : '
         'c’est ce qui donne la convexité.'}],
 fig={'series': [
   pol('u0', 'U₁', U0, 'ac', ep=3, lp=[0.9, 0.3]),
 ]},
 etapes=[
  etape('Une courbe d’indifférence',
        'Elle regroupe toutes les combinaisons de X et de Y qui procurent le '
        'même niveau de satisfaction : le consommateur est indifférent entre '
        'tous les points de cette courbe.',
        on=['u0'],
        add=[pt('p1', 'A', 0.24, round(0.166 / 0.24, 4), 'ac2'),
             pt('p2', 'B', 0.52, round(0.166 / 0.52, 4), 'ac2'),
             txt('tm', 'même utilité', 0.36, 0.58, 'ac2', taille=14)],
        vif=['u0', 'p1', 'p2', 'tm']),
  etape('Le taux marginal de substitution',
        'La pente de la courbe en un point mesure le nombre d’unités de Y '
        'auxquelles il faut renoncer pour consommer une unité de X '
        'supplémentaire sans changer de satisfaction. Il est négatif : c’est '
        'un renoncement.',
        add=[fl('ftms', 'TMS < 0', 0.26, 0.6, 0.42, 0.37, 'jn')],
        off=['tm'],
        vif=['ftms']),
  etape('La carte du consommateur',
        'À chaque niveau de satisfaction correspond une courbe. Leur ensemble '
        'forme la carte du consommateur. Grâce à la non-satiété, une courbe '
        'plus éloignée de l’origine correspond toujours à une utilité plus '
        'élevée.',
        add=[pol('ub', 'U₀', UB, 'gr', ep=2.2, lp=[0.9, 0.04]),
             pol('u1', 'U₂', U1, 'ok', ep=2.4, lp=[0.9, 0.42]),
             fl('fu', 'utilité croissante', 0.3, 0.3, 0.62, 0.62, 'ok')],
        off=['ftms', 'p1', 'p2'],
        vif=['ub', 'u1', 'fu']),
  etape('Les courbes ne se croisent jamais',
        'Si deux courbes d’indifférence se coupaient, une même combinaison '
        'procurerait deux niveaux de satisfaction différents : cela '
        'contredirait l’hypothèse de transitivité.',
        add=[txt('tx', 'transitivité → aucun croisement possible', 0.3, 0.95,
                 'jn', taille=14)],
        off=['fu'],
        vif=['tx']),
  etape('La contrainte de budget',
        'Le revenu et les prix limitent les combinaisons accessibles : la '
        'droite de budget relie ce que le consommateur pourrait acheter s’il '
        'dépensait tout en Y, puis tout en X. Sa pente est l’opposé du '
        'rapport des prix.',
        add=[lin('b0', 'Droite de budget', *B0, c='ac2', ep=3, lp=[0.16, 0.18]),
             zone('zb', '', [(0.02, 0.02), (0.62, 0.02), (0.07, 0.9)], 'ac2'),
             txt('tz', 'zone accessible', 0.10, 0.07, 'ac2', taille=13)],
        off=['tx'],
        vif=['b0', 'zb', 'tz']),
  etape('L’optimum du consommateur',
        'Le consommateur choisit le point de tangence entre sa droite de '
        'budget et la courbe d’indifférence la plus élevée qu’il peut '
        'atteindre : U₂ est hors de portée, U₀ est atteignable mais laisse de '
        'la satisfaction inexploitée.',
        add=[pt('e', 'E', 0.3297, 0.5036, 'ok'),
             rep('re', 0.3297, 0.5036, lx='X*', ly='Y*', c='ok')],
        off=['zb', 'tz'],
        vif=['e', 're', 'u0', 'b0']),
  etape('La condition d’optimum',
        'En ce point, la pente de la courbe d’indifférence égale celle de la '
        'droite de budget : le taux marginal de substitution est égal au '
        'rapport des prix des deux biens. Ce que le consommateur est prêt à '
        'échanger coïncide avec ce que le marché lui impose d’échanger.',
        add=[txt('tc', 'TMS = rapport des prix', 0.44, 0.84, 'ok', taille=16,
                 gras=True)],
        vif=['tc']),
 ],
 pieges=[
  {'t': 'Convexe ne veut pas dire « n’importe quelle forme décroissante »',
   'd': 'La convexité traduit un fait économique : le consommateur préfère un '
        'mélange des deux biens plutôt que tout l’un ou tout l’autre. Des '
        'courbes en angle droit ou en escalier contrediraient cette idée et '
        'rendraient la dérivation impossible.'},
  {'t': 'Le TMS est négatif, sa valeur absolue est décroissante',
   'd': 'Dire « le TMS est décroissant » signifie que la valeur absolue de la '
        'pente diminue quand on se déplace vers la droite. Le signe, lui, '
        'reste négatif partout : il traduit le renoncement.'},
  {'t': 'Déplacement sur la courbe ou changement de courbe',
   'd': 'Se déplacer sur une même courbe d’indifférence laisse l’utilité '
        'inchangée : c’est un arbitrage. Passer à une autre courbe change le '
        'niveau de satisfaction : cela suppose un revenu ou des prix '
        'différents, donc une autre droite de budget.'},
 ],
 main=[
  'Trace les axes : le bien X en abscisse, le bien Y en ordonnée.',
  'Trace une courbe décroissante et convexe, puis deux autres parallèles, '
  'l’une plus proche et l’autre plus éloignée de l’origine.',
  'Trace la droite de budget en joignant les deux points extrêmes : tout en '
  'Y, puis tout en X.',
  'Cherche la courbe d’indifférence la plus haute qui touche encore la droite '
  'sans la couper : marque le point de tangence E.',
  'Descends et projette E sur les deux axes, et écris à côté : « TMS = '
  'rapport des prix ».',
 ],
 phrase='Le programme du consommateur consiste à maximiser son utilité sous '
        'contrainte de budget : l’optimum se situe au point de tangence entre '
        'la droite de budget et la courbe d’indifférence la plus élevée '
        'accessible, c’est-à-dire là où le taux marginal de substitution '
        'égale le rapport des prix des deux biens.',
 liens=[{'c': '4', 'b': 15, 'l': 'La courbe d’indifférence et la carte du consommateur'},
        {'c': '4', 'b': 22, 'l': 'Les quatre hypothèses sur les préférences'},
        {'c': '4', 'b': 65, 'l': 'Le taux marginal de substitution'},
        {'c': '4', 'b': 127, 'l': 'La maximisation sous contrainte de budget'}],
 mots=['courbe d’indifférence', 'TMS', 'contrainte budgétaire', 'optimum',
       'transitivité', 'convexité', 'carte du consommateur'],
))

# ------------------------------------------- effet substitution / revenu
B1 = (0.07, 0.90, 1.0, 0.06)
BP = (0.03, 0.7473, 0.84, 0.0157)

L.append(fiche(
 id='substitution-revenu',
 t='Effet de substitution et effet de revenu',
 st='Décomposer en deux temps ce que fait une baisse de prix.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Quand le prix d’un bien baisse, pourquoi faut-il distinguer deux effets, '
   'et dans quel cas peuvent-ils jouer en sens contraire ?',
 axes={'x': 'Quantité du bien X', 'y': 'Quantité du bien Y'},
 depart='Un consommateur à son optimum initial A, avant la baisse du prix de '
        'X.',
 hyp=['Le prix du bien Y et le revenu nominal restent inchangés : seul le '
      'prix de X baisse.',
      'Les néoclassiques raisonnent en termes réels : une baisse de prix '
      'augmente le pouvoir d’achat, donc le revenu réel, même si le revenu '
      'nominal ne bouge pas.',
      'La décomposition en deux effets est un artifice d’analyse : le '
      'consommateur, lui, passe directement de A à B.'],
 pente=[{'s': 'Droite de budget', 'd': 'sa pente est l’opposé du rapport des '
         'prix : quand le prix de X baisse, elle pivote autour de son point '
         'd’ordonnée et devient moins raide.'},
        {'s': 'Droite fictive', 'd': 'parallèle à la nouvelle droite — donc '
         'aux nouveaux prix — mais ramenée au niveau de satisfaction '
         'd’origine : elle isole le seul effet de substitution.'}],
 fig={'series': [
   pol('u0', 'U₀', U0, 'ac', ep=2.6, lp=[0.92, 0.27]),
   lin('b0', 'Budget initial', *B0, c='ac2', ep=2.8, lp=[0.26, 0.72]),
   pt('a', 'A', 0.3297, 0.5036, 'ac2'),
   rep('ra', 0.3297, 0.5036, lx='X₀', c='ac2'),
 ]},
 etapes=[
  etape('La situation initiale',
        'Le consommateur est en A, au point de tangence entre sa droite de '
        'budget et la courbe d’indifférence U₀. Il consomme X₀ unités du bien '
        'X.',
        on=['u0', 'b0', 'a', 'ra'], vif=['a', 'ra']),
  etape('Le prix de X baisse : la droite de budget pivote',
        'Le revenu nominal et le prix de Y n’ont pas bougé, donc le point sur '
        'l’axe des Y reste le même. Mais avec le même revenu on peut acheter '
        'davantage de X : la droite pivote vers l’extérieur et devient moins '
        'raide.',
        add=[lin('b1', 'Nouveau budget', *B1, c='bl', ep=2.8, lp=[0.72, 0.42]),
             fl('fp', 'P(X) ↓', 0.66, 0.26, 0.86, 0.17, 'bl')],
        vif=['b1', 'fp']),
  etape('Premier temps : l’effet de substitution',
        'On trace une droite fictive, parallèle à la nouvelle — donc aux '
        'nouveaux prix — mais ramenée à la satisfaction d’origine. Le '
        'consommateur glisse de A en C le long de U₀ : il remplace du Y par '
        'du X, devenu relativement moins cher.',
        add=[lin('bp', 'Budget fictif', *BP, c='jn', ep=2.4, lp=[0.62, 0.17]),
             pt('c', 'C', 0.4288, 0.3871, 'jn'),
             rep('rc', 0.4288, 0.3871, lx='X_s', c='jn'),
             fl('fs', 'effet de substitution', 0.34, 0.46, 0.42, 0.4, 'jn')],
        off=['fp'],
        vif=['bp', 'c', 'rc', 'fs']),
  etape('Deuxième temps : l’effet de revenu',
        'La baisse du prix a augmenté le pouvoir d’achat. On revient à la '
        'vraie nouvelle droite de budget : le consommateur passe de C à B, '
        'sur une courbe d’indifférence plus élevée. Sa satisfaction augmente.',
        add=[pol('u1', 'U₁', U1, 'ok', ep=2.6, lp=[0.92, 0.4]),
             pt('b', 'B', 0.5332, 0.4816, 'ok'),
             rep('rb', 0.5332, 0.4816, lx='X₁', c='ok'),
             fl('fr', 'effet de revenu', 0.45, 0.4, 0.52, 0.47, 'ok')],
        off=['fs'],
        vif=['u1', 'b', 'rb', 'fr']),
  etape('L’effet prix total',
        'Ce que l’on observe réellement, c’est le passage direct de A à B : '
        'l’effet prix est la somme des deux effets. Ici, ils vont dans le '
        'même sens et la consommation de X augmente nettement, de X₀ à X₁.',
        add=[fl('ft', 'effet prix total', 0.33, 0.1, 0.53, 0.1, 'ac')],
        off=['fr', 'bp', 'c', 'rc'],
        vif=['ft', 'ra', 'rb']),
  etape('Et si le bien est inférieur ?',
        'Pour un bien inférieur, la hausse du pouvoir d’achat pousse à en '
        'consommer moins : l’effet de revenu joue en sens contraire de '
        'l’effet de substitution et vient rogner le résultat. La consommation '
        'de X augmente encore, mais beaucoup moins.',
        add=[pt('bi', 'B′', 0.47, 0.5386, 'ac2'),
             rep('rbi', 0.47, 0.5386, lx='X′', c='ac2'),
             txt('tbi', 'bien inférieur : les deux effets s’opposent',
                 0.2, 0.96, 'ac2', taille=14)],
        off=['ft', 'b', 'rb'],
        vif=['bi', 'rbi', 'tbi']),
  etape('Le cas limite du bien de Giffen',
        'Dans un contexte de pauvreté extrême, l’effet de revenu peut '
        'l’emporter sur l’effet de substitution : la consommation de X '
        'diminue alors que son prix a baissé. La demande devient croissante. '
        'C’est le bien de Giffen, un cas très particulier.',
        add=[pt('bg', 'B″', 0.30, 0.6922, 'ko'),
             rep('rbg', 0.30, 0.6922, lx='X″', c='ko'),
             txt('tbg', 'Giffen : l’effet de revenu l’emporte', 0.2, 0.96,
                 'ko', taille=14)],
        off=['bi', 'rbi', 'tbi'],
        vif=['bg', 'rbg', 'tbg']),
 ],
 pieges=[
  {'t': 'La décomposition est un outil, pas une chronologie',
   'd': 'Le consommateur ne passe pas d’abord par C puis par B : il va '
        'directement de A à B. C et la droite fictive n’existent que pour '
        'séparer analytiquement deux forces.'},
  {'t': 'Bien de Giffen ≠ bien de Veblen',
   'd': 'Le bien de Giffen est un bien inférieur consommé par contrainte, '
        'dans un contexte de pauvreté extrême. Le bien de Veblen est un bien '
        'supérieur acheté par affichage social, dans un contexte de richesse. '
        'Les deux ont une demande croissante, pour des raisons opposées.'},
  {'t': 'Le revenu nominal n’a pas changé',
   'd': 'L’effet de revenu ne vient pas d’une hausse du salaire mais d’une '
        'hausse du pouvoir d’achat : à revenu nominal constant, une baisse de '
        'prix enrichit réellement le consommateur.'},
 ],
 main=[
  'Trace les deux axes, une courbe d’indifférence U₀ et la droite de budget '
  'initiale, tangentes en A.',
  'Fais pivoter la droite de budget autour de son point sur l’axe des Y : '
  'c’est la baisse du prix de X.',
  'Trace une droite fictive parallèle à la nouvelle, tangente à U₀ : marque '
  'le point C — c’est l’effet de substitution, de A à C.',
  'Reviens sur la vraie nouvelle droite, tangente à U₁ : marque B — c’est '
  'l’effet de revenu, de C à B.',
  'Projette A, C et B sur l’axe des abscisses et nomme chaque segment ; ajoute '
  'enfin, en pointillés, le point d’un bien inférieur puis celui d’un bien de '
  'Giffen.',
 ],
 phrase='Toute variation de prix se décompose en un effet de substitution, '
        'par lequel le consommateur remplace le bien devenu relativement plus '
        'cher par l’autre à satisfaction inchangée, et un effet de revenu, '
        'par lequel la variation du pouvoir d’achat modifie l’ensemble de ses '
        'consommations : lorsque le bien est inférieur, ces deux effets '
        'jouent en sens contraire, et dans le cas limite du bien de Giffen le '
        'second l’emporte.',
 liens=[{'c': '4', 'b': 129, 'l': 'Effet de substitution et effet de revenu'},
        {'c': '4', 'b': 554, 'l': 'Pourquoi la demande n’est pas toujours prévisible'},
        {'c': '4', 'b': 202, 'l': 'Bien de Giffen et bien de Veblen : ne pas confondre'}],
 mots=['effet de substitution', 'effet de revenu', 'effet prix', 'Giffen',
       'Veblen', 'bien inférieur', 'pouvoir d’achat'],
))

# ------------------------------------------------------------ élasticités
DEL = courbe_dec(0.1, 0.62, 0.95, 0.12, n=9, creux=0.75)
DIN = [(0.42, 0.95), (0.46, 0.78), (0.5, 0.6), (0.53, 0.42), (0.56, 0.24),
       (0.58, 0.08)]

L.append(fiche(
 id='elasticite-demande',
 t='L’élasticité-prix de la demande',
 st='La même hausse de prix, deux réactions opposées des quantités.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Pourquoi une même hausse de prix fait-elle chuter la demande d’un bien et '
   'presque pas celle d’un autre, et qu’est-ce que cela change pour le '
   'producteur ?',
 axes={'x': 'Quantité demandée', 'y': 'Prix'},
 depart='Un même point de départ — le même prix, la même quantité — pour deux '
        'biens dont la demande réagit différemment.',
 hyp=['L’élasticité est un rapport entre deux variations : la variation '
      'relative de la quantité demandée rapportée à la variation relative du '
      'prix.',
      'L’élasticité n’est pas une constante : elle dépend du temps, de '
      'l’existence de substituts et de la finesse de la catégorie de biens '
      'retenue.',
      'La hausse de prix appliquée est la même dans les deux cas, ce qui '
      'permet de comparer les réactions.'],
 pente=[{'s': 'Demande élastique', 'd': 'courbe plate : une petite variation '
         'de prix provoque une forte variation des quantités, parce qu’il '
         'existe des substituts.'},
        {'s': 'Demande inélastique', 'd': 'courbe raide : même une forte '
         'hausse de prix ne fait presque pas reculer les quantités, parce '
         'qu’il n’existe pas d’alternative.'}],
 fig={'series': [
   lin('p0', '', 0.0, 0.42, 1.0, 0.42, 'gr', ep=1.6),
   lin('p1', '', 0.0, 0.72, 1.0, 0.72, 'gr', ep=1.6),
   txt('tp0', 'prix initial', 0.84, 0.36, 'gr', taille=13),
   txt('tp1', 'prix après hausse', 0.78, 0.76, 'gr', taille=13),
 ]},
 variantes=[
  {'lib': 'Demande élastique',
   'etapes': [
     etape('Une courbe de demande plate',
           'Le bien a de nombreux substituts proches : un yaourt d’une marque '
           'précise, par exemple. Le consommateur peut changer de produit '
           'sans difficulté.',
           on=['p0', 'p1', 'tp0', 'tp1'],
           add=[pol('de', 'Demande élastique', DEL, 'ok', ep=3.2),
                pt('e0', '', 0.44, 0.42, 'ac2'),
                rep('r0', 0.44, 0.42, lx='Q₀', c='ac2')],
           vif=['de', 'e0', 'r0']),
     etape('Le prix augmente',
           'On applique une hausse de prix, la même que dans l’autre cas. Il '
           'faut maintenant lire la nouvelle quantité demandée au croisement '
           'de la courbe et du nouveau niveau de prix.',
           add=[fl('fp', '', 0.12, 0.46, 0.12, 0.68, 'ac2')],
           vif=['fp', 'p1']),
     etape('Les quantités s’effondrent',
           'La nouvelle quantité est très inférieure à la précédente : le '
           'consommateur a changé de produit ou réduit sa consommation. Pour '
           'lui, c’est un avantage : il n’est pas prisonnier d’un prix.',
           add=[pt('e1', '', 0.167, 0.72, 'ko'),
                rep('r1', 0.167, 0.72, lx='Q₁', c='ko'),
                fl('fq', 'forte baisse', 0.42, 0.18, 0.18, 0.18, 'ko')],
           vif=['e1', 'r1', 'fq']),
     etape('Le chiffre d’affaires du producteur recule',
           'Le prix a monté mais les quantités ont chuté davantage : le '
           'produit prix × quantité diminue. Augmenter ses prix est risqué '
           'pour un producteur dont la demande est élastique.',
           add=[txt('tca', 'CA = P × Q  →  en baisse', 0.3, 0.92, 'ko',
                    taille=16, gras=True)],
           vif=['tca']),
   ]},
  {'lib': 'Demande inélastique',
   'etapes': [
     etape('Une courbe de demande raide',
           'Le bien n’a pas de substitut immédiat : le pétrole au moment des '
           'chocs pétroliers, ou une catégorie très large comme les produits '
           'laitiers. Le consommateur ne peut pas s’en passer.',
           on=['p0', 'p1', 'tp0', 'tp1'],
           add=[pol('di', 'Demande inélastique', DIN, 'ac2', ep=3.2),
                pt('f0', '', 0.5, 0.42, 'ac2'),
                rep('q0', 0.5, 0.42, lx='Q₀', c='ac2')],
           vif=['di', 'f0', 'q0']),
     etape('Le prix augmente — exactement de la même manière',
           'Même hausse de prix que dans le cas précédent : c’est la '
           'condition pour que la comparaison ait un sens. Seule la forme de '
           'la courbe diffère.',
           add=[fl('fp2', '', 0.12, 0.46, 0.12, 0.68, 'ac2')],
           vif=['fp2', 'p1']),
     etape('Les quantités bougent à peine',
           'La nouvelle quantité est presque identique : le consommateur est '
           'coincé, il ne peut pas substituer et doit payer plus. Ses '
           'dépenses augmentent mécaniquement.',
           add=[pt('f1', '', 0.455, 0.72, 'ok'),
                rep('q1', 0.455, 0.72, lx='Q₁', c='ok'),
                fl('fq2', 'faible baisse', 0.5, 0.18, 0.46, 0.18, 'ok')],
           vif=['f1', 'q1', 'fq2']),
     etape('Le chiffre d’affaires du producteur augmente',
           'Le prix a monté et les quantités n’ont presque pas reculé : le '
           'produit prix × quantité augmente. Pour le producteur, '
           'l’inélasticité est une assurance — mais aussi le signe que '
           'baisser ses prix ne servirait à rien.',
           add=[txt('tca2', 'CA = P × Q  →  en hausse', 0.3, 0.92, 'ok',
                    taille=16, gras=True)],
           vif=['tca2']),
   ]},
 ],
 pieges=[
  {'t': 'L’élasticité n’est pas une propriété fixe du bien',
   'd': 'Un même bien est plus élastique à long terme qu’à court terme, parce '
        'que les substituts apparaissent avec le temps. Les chocs pétroliers '
        'l’illustrent : demande inélastique dans l’immédiat, beaucoup plus '
        'élastique une fois les procédés de production modifiés.'},
  {'t': 'Plus la catégorie est précise, plus la demande est élastique',
   'd': 'Le skyr d’une marque a de nombreux substituts, les yaourts en '
        'général moins, les produits laitiers encore moins. Annoncer une '
        'élasticité sans préciser le périmètre du bien n’a pas de sens.'},
  {'t': 'Élastique n’est pas « bon » ou « mauvais » en soi',
   'd': 'Pour le consommateur, l’élasticité est un avantage : une marge de '
        'manœuvre. Pour le producteur, c’est un risque. L’inélasticité '
        'inverse exactement les rôles.'},
 ],
 main=[
  'Trace les axes : les quantités en abscisse, le prix en ordonnée.',
  'Trace deux horizontales : le prix initial et le prix après hausse, '
  'identiques pour les deux cas.',
  'Trace d’abord une demande très plate, lis les deux quantités et constate '
  'l’écart important.',
  'Trace ensuite, sur un second repère, une demande très raide : les deux '
  'quantités sont presque confondues.',
  'Écris sous chaque graphique le sens de variation du chiffre d’affaires, '
  'produit du prix par la quantité.',
 ],
 phrase='L’élasticité-prix de la demande mesure la sensibilité des quantités '
        'demandées à une variation de prix : plus un bien dispose de '
        'substituts et plus l’horizon est long, plus la demande est '
        'élastique, de sorte qu’une hausse de prix fait chuter les quantités '
        'et réduit le chiffre d’affaires, alors qu’une demande inélastique '
        'permet au producteur d’augmenter ses prix sans risque.',
 liens=[{'c': '4', 'b': 134, 'l': 'L’élasticité de la demande : définition'},
        {'c': '4', 'b': 155, 'l': 'Le point de vue du producteur'},
        {'c': '4', 'b': 248, 'l': 'Le rôle fondamental du temps'},
        {'c': '4', 'b': 268, 'l': 'L’élasticité dépend de la catégorie de biens'}],
 mots=['élasticité', 'élasticité-prix', 'substituts', 'chiffre d’affaires',
       'choc pétrolier', 'élasticité croisée', 'élasticité-revenu'],
))
