# -*- coding: utf-8 -*-
"""Courbes transversales : État et consommation (ch. 1), monnaie et inflation
(ch. 2), cycles (ch. 8), démographie (ch. 7)."""

import math
from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     cloche, courbe_dec, inter, y_de, x_de, bouge)

L = []

# ------------------------------------------------------------ courbe de Laffer
LAF = cloche(0.0, 1.0, 0.02, 0.84, n=17, pic=0.5)

L.append(fiche(
 id='laffer',
 t='La courbe de Laffer',
 st='« Trop d’impôt tue l’impôt » — et pourquoi cette courbe est contestée.',
 cat='macro', an=1, ch=['1'],
 type='schema',
 q='Une hausse du taux d’imposition accroît-elle toujours les recettes de '
   'l’État, et que vaut empiriquement l’argument du « trop d’impôt tue '
   'l’impôt » ?',
 axes={'x': 'Taux d’imposition', 'y': 'Recettes fiscales'},
 depart='Un taux d’imposition nul, donc des recettes nulles.',
 hyp=['L’argument suppose que les contribuables modifient leur comportement '
      'en réaction au taux d’imposition : au-delà d’un certain seuil, ils '
      'travaillent moins, se délocalisent ou contournent l’impôt.',
      'Il s’inscrit dans la discussion sur la crise de l’État-providence '
      'analysée par Pierre Rosanvallon en 1981 : problème de financement, '
      'crise d’efficacité, crise de légitimité.',
      'Le cours souligne que cette courbe ne relève pas de faits empiriques '
      'selon certains économistes : c’est un argument théorique.'],
 pente=[{'s': 'Branche montante', 'd': 'tant que le taux reste modéré, une '
         'hausse du taux augmente les recettes : l’assiette ne se dérobe pas '
         'encore.'},
        {'s': 'Branche descendante', 'd': 'au-delà du taux optimal, l’effet '
         'de découragement l’emporte : l’assiette se contracte plus vite que '
         'le taux n’augmente, donc les recettes baissent.'}],
 fig={'series': [
   pol('lf', 'Recettes fiscales', LAF, 'ac', ep=3.4, lp=[0.82, 0.70]),
 ]},
 etapes=[
  etape('Les deux points extrêmes',
        'À taux nul, l’État ne perçoit rien. À taux de 100 %, plus personne '
        'n’a intérêt à déclarer une activité : les recettes sont nulles '
        'aussi. La courbe part de zéro et y revient.',
        on=['lf'],
        add=[pt('a', '', 0.0, 0.02, 'gr'), pt('b', '', 1.0, 0.02, 'gr')],
        vif=['lf', 'a', 'b']),
  etape('Entre les deux, les recettes passent par un maximum',
        'Puisque la courbe part de zéro et y revient en restant positive, '
        'elle atteint nécessairement un maximum : c’est le taux qui procure '
        'le plus de recettes.',
        add=[pt('m', '', 0.5, 0.84, 'ac2'),
             rep('rm', 0.5, 0.84, lx='t*', ly='R max', c='ac2')],
        vif=['m', 'rm']),
  etape('La branche montante : l’effet de taux',
        'Tant qu’on se situe à gauche du maximum, augmenter le taux augmente '
        'les recettes. L’effet mécanique de la hausse du taux l’emporte sur '
        'le découragement qu’elle provoque.',
        add=[fl('f1', 'effet de taux', 0.1, 0.3, 0.36, 0.68, 'ok')],
        vif=['f1']),
  etape('La branche descendante : l’effet d’assiette',
        'À droite du maximum, le raisonnement s’inverse : une fiscalité très '
        'élevée pousse les contribuables à travailler moins, à se délocaliser '
        'ou à contourner l’impôt. L’assiette se réduit plus vite que le taux '
        'n’augmente.',
        add=[fl('f2', 'effet d’assiette', 0.66, 0.66, 0.9, 0.26, 'ko')],
        off=['f1'],
        vif=['f2']),
  etape('L’argument politique : « trop d’impôt tue l’impôt »',
        'Le cours en donne la formulation populaire : si la fiscalité est '
        'élevée, les travailleurs se disent que cela ne sert à rien de '
        'travailler quand une grande partie de leur salaire part en impôts.',
        add=[txt('tp', '« trop d’impôt tue l’impôt »', 0.26, 0.95, 'ac2',
                 taille=16, gras=True)],
        off=['f2'],
        vif=['tp']),
  etape('Les reproches faits à la courbe',
        'Cette courbe ne relève pas de faits empiriques selon certains '
        'économistes : personne ne sait où se situe réellement le sommet. '
        'Elle est un raisonnement, pas une mesure.',
        add=[txt('tc', 'où se situe t* ? personne ne le sait', 0.22, 0.1,
                 'ko', taille=15, gras=True)],
        off=['tp'],
        vif=['tc']),
  etape('L’objection du délai d’ajustement',
        'Certaines études montrent qu’à moyen terme une hausse du taux '
        'd’imposition n’a pas d’effet : les gens ne changent pas toujours '
        'leur comportement immédiatement après une hausse d’impôts.',
        add=[txt('td', 'les comportements ne s’ajustent pas immédiatement',
                 0.14, 0.04, 'jn', taille=14, gras=True)],
        vif=['td']),
 ],
 pieges=[
  {'t': 'La courbe ne dit pas où se situe le sommet',
   'd': 'Dire « nous sommes à droite du maximum, il faut baisser les impôts » '
        'ne se déduit pas de la courbe : cela suppose une mesure que la '
        'courbe ne fournit pas.'},
  {'t': 'Symétrie du dessin, pas du monde',
   'd': 'On dessine souvent une cloche symétrique dont le sommet tombe à '
        '50 %. Rien ne le justifie : la forme du dessin n’est pas un '
        'résultat.'},
  {'t': 'Un argument sur les recettes, pas sur la justice fiscale',
   'd': 'La courbe parle du rendement de l’impôt. Elle ne dit rien sur sa '
        'répartition entre contribuables, ni sur les fonctions de l’État que '
        'ces recettes financent.'},
 ],
 main=[
  'Trace les axes : le taux d’imposition en abscisse, les recettes fiscales '
  'en ordonnée.',
  'Place deux points à zéro : à taux nul et à taux de 100 %.',
  'Relie-les par une cloche et marque le sommet, en le projetant sur l’axe '
  'des abscisses.',
  'Annote la branche montante — effet de taux — et la branche descendante — '
  'effet d’assiette.',
  'Écris en marge la critique : la position du sommet n’est pas connue.',
 ],
 phrase='La courbe de Laffer traduit l’idée que « trop d’impôt tue l’impôt » : '
        'au-delà d’un certain taux, le découragement des contribuables '
        'contracte l’assiette plus vite que le taux n’augmente, de sorte que '
        'les recettes diminuent ; mais cette courbe, contestée parce qu’elle '
        'ne repose pas sur des faits empiriques solides, ne permet jamais de '
        'dire où se situe réellement le taux optimal.',
 liens=[{'c': '1', 'b': 470, 'l': 'La courbe de Laffer : trop d’impôt tue l’impôt'},
        {'c': '1', 'b': 471, 'l': 'Les reproches faits à la courbe de Laffer'},
        {'c': '1', 'b': 465, 'l': 'La crise de l’État-providence selon Rosanvallon'}],
 mots=['Laffer', 'fiscalité', 'recettes fiscales', 'État-providence',
       'Rosanvallon', 'assiette fiscale'],
))

# ----------------------------------------------------------- carré magique
L.append(fiche(
 id='carre-magique',
 t='Le carré magique de Kaldor',
 st='Quatre objectifs qu’aucune politique n’atteint en même temps.',
 cat='macro', an=1, ch=['1'],
 type='schema',
 q='Pourquoi les quatre grands objectifs de la politique économique ne '
   'peuvent-ils pas être atteints simultanément ?',
 axes={'x': '', 'y': '', 'sans': 1},
 depart='Quatre axes partant d’un centre, un pour chaque objectif de la '
        'politique économique.',
 hyp=['Le carré est dit « magique » précisément parce qu’atteindre les quatre '
      'objectifs simultanément est impossible.',
      'Le solde extérieur est mesuré en pourcentage du PIB : solde de la '
      'balance des transactions courantes rapporté au PIB, multiplié par '
      'cent.',
      'La balance des transactions courantes est elle-même l’addition des '
      'trois balances qui la composent.'],
 pente=[{'s': 'Lecture du graphique', 'd': 'ce n’est pas une courbe mais un '
         'diagramme à quatre axes : plus le point se situe loin du centre sur '
         'un axe, meilleure est la performance sur cet objectif.'},
        {'s': 'Surface du quadrilatère', 'd': 'plus elle est grande, '
         'meilleure est la performance d’ensemble. Sa déformation montre '
         'quels objectifs ont été privilégiés.'}],
 fig={'series': [
   lin('ax1', '', 0.5, 0.5, 0.5, 0.96, 'gr', ep=1.6),
   lin('ax2', '', 0.5, 0.5, 0.96, 0.5, 'gr', ep=1.6),
   lin('ax3', '', 0.5, 0.5, 0.5, 0.04, 'gr', ep=1.6),
   lin('ax4', '', 0.5, 0.5, 0.04, 0.5, 'gr', ep=1.6),
   txt('t1', 'Croissance', 0.4, 0.99, 'ac', taille=15, gras=True),
   txt('t2', 'Plein emploi', 0.84, 0.53, 'ac', taille=15, gras=True),
   txt('t3', 'Stabilité des prix', 0.37, 0.0, 'ac', taille=15, gras=True),
   txt('t4', 'Solde extérieur', 0.02, 0.53, 'ac', taille=15, gras=True),
 ]},
 etapes=[
  etape('Quatre objectifs, quatre axes',
        'Croissance, plein emploi, stabilité des prix et équilibre extérieur. '
        'Chaque axe part du centre : plus on s’éloigne du centre, meilleure '
        'est la performance sur cet objectif.',
        on=['ax1', 'ax2', 'ax3', 'ax4', 't1', 't2', 't3', 't4'],
        vif=['ax1', 'ax2', 'ax3', 'ax4']),
  etape('Le carré idéal',
        'Si les quatre objectifs étaient atteints au plus haut niveau, on '
        'obtiendrait un grand carré régulier. C’est la situation de '
        'référence, jamais observée.',
        add=[zone('ideal', '', [(0.5, 0.9), (0.9, 0.5), (0.5, 0.1),
                                (0.1, 0.5)], 'ok')],
        vif=['ideal']),
  etape('La réalité : un quadrilatère déformé',
        'Dans les faits, les performances diffèrent d’un objectif à l’autre. '
        'Le quadrilatère observé est plus petit et déformé : il révèle ce '
        'qu’une économie a privilégié et ce qu’elle a sacrifié.',
        add=[zone('reel', '', [(0.5, 0.74), (0.72, 0.5), (0.5, 0.26),
                               (0.3, 0.5)], 'ac2')],
        vif=['reel']),
  etape('Pourquoi « magique » : les objectifs s’opposent',
        'Une relance soutient la croissance et l’emploi mais nourrit '
        'l’inflation et gonfle les importations, donc dégrade le solde '
        'extérieur. Une rigueur fait l’inverse. Les gains sur deux axes se '
        'paient sur les deux autres.',
        add=[fl('f1', 'relance', 0.56, 0.72, 0.68, 0.58, 'ko'),
             fl('f2', '', 0.44, 0.3, 0.36, 0.44, 'ko')],
        vif=['f1', 'f2']),
  etape('Ce que mesure chaque axe',
        'La croissance se lit en taux de variation du PIB, le plein emploi '
        'par le taux de chômage, la stabilité des prix par le taux '
        'd’inflation, et le solde extérieur par le rapport de la balance des '
        'transactions courantes au PIB, en pourcentage.',
        add=[txt('tm', 'solde extérieur = BTC / PIB × 100', 0.2, 0.86, 'bl',
                 taille=14, gras=True)],
        off=['f1', 'f2'],
        vif=['tm']),
  etape('L’usage en dissertation',
        'Le carré sert à comparer deux périodes ou deux pays : on superpose '
        'les quadrilatères et l’on commente les arbitrages. Les Trente '
        'Glorieuses donnent un carré ample, les années 1970 un carré rétréci '
        'sur les axes des prix et de l’emploi.',
        add=[zone('r2', '', [(0.5, 0.62), (0.62, 0.5), (0.5, 0.38),
                             (0.38, 0.5)], 'ko')],
        off=['tm'],
        vif=['r2']),
 ],
 pieges=[
  {'t': 'Ce n’est pas une courbe',
   'd': 'Aucun axe ne porte une variable en fonction d’une autre : c’est un '
        'diagramme radar à quatre dimensions. Chercher une pente ou un '
        'équilibre n’a aucun sens ici.'},
  {'t': 'S’éloigner du centre, c’est toujours « mieux »',
   'd': 'Les axes sont orientés de sorte qu’une bonne performance éloigne du '
        'centre : taux de chômage faible et inflation faible éloignent du '
        'centre, elles aussi. Inverser un axe rend la figure illisible.'},
  {'t': 'L’impossibilité est un constat, pas une loi',
   'd': 'Le carré décrit l’arbitrage habituel entre objectifs. Il n’interdit '
        'pas qu’une période rare — les Trente Glorieuses — s’en rapproche '
        'nettement.'},
 ],
 main=[
  'Trace deux axes croisés en un centre : une verticale et une horizontale.',
  'Nomme les quatre extrémités : croissance, plein emploi, stabilité des '
  'prix, solde extérieur.',
  'Place un point sur chaque axe selon la performance et relie-les : tu '
  'obtiens le quadrilatère observé.',
  'Trace par-dessus, en pointillés, le carré idéal, bien plus ample.',
  'Annote un arbitrage : une flèche qui gagne sur un axe et qui perd sur un '
  'autre.',
 ],
 phrase='Le carré magique de Kaldor représente sur quatre axes les quatre '
        'grands objectifs de la politique économique — croissance, plein '
        'emploi, stabilité des prix et équilibre extérieur — et il est dit '
        'magique parce que les atteindre simultanément est impossible : tout '
        'gain sur deux axes se paie généralement sur les deux autres.',
 liens=[{'c': '1', 'b': 445, 'l': 'Kaldor et le carré magique'},
        {'c': '1', 'b': 446, 'l': 'La mesure du solde extérieur'},
        {'c': '1', 'b': 449, 'l': 'Les trois fonctions de l’État selon Musgrave'}],
 mots=['carré magique', 'Kaldor', 'politique économique', 'plein emploi',
       'solde extérieur', 'arbitrage'],
))

# --------------------------------------------------------- cycle de vie
REV = cloche(0.04, 0.80, 0.08, 0.86, n=15, pic=0.56)
CONS = [(0.04, 0.42), (0.2, 0.46), (0.4, 0.5), (0.6, 0.52), (0.8, 0.52),
        (0.97, 0.5)]
PAT = [(0.04, 0.3), (0.14, 0.23), (0.24, 0.2), (0.34, 0.26), (0.46, 0.42),
       (0.58, 0.62), (0.7, 0.76), (0.78, 0.8), (0.86, 0.66), (0.97, 0.42)]

L.append(fiche(
 id='cycle-vie-modigliani',
 t='Le cycle de vie de Modigliani',
 st='Trois âges, trois comportements : s’endetter, épargner, désépargner.',
 cat='macro', an=1, ch=['1'],
 type='schema',
 q='Pourquoi la consommation d’un ménage ne suit-elle pas les variations de '
   'son revenu courant, et comment l’âge explique-t-il l’épargne ?',
 axes={'x': 'Âge', 'y': 'Revenu, consommation et patrimoine'},
 depart='Un individu au début de sa vie adulte, dont le revenu est encore '
        'faible.',
 hyp=['Modigliani introduit, à côté du revenu courant, le patrimoine et '
      'l’âge comme variables explicatives de la consommation.',
      'L’individu est supposé rationnel et prévoyant : il planifie son niveau '
      'de vie en fonction de ses revenus attendus, de sa richesse et de sa '
      'durée de vie.',
      'Il cherche à lisser sa consommation dans le temps pour éviter de '
      'fortes variations de son niveau de vie, même lorsque ses revenus '
      'changent.'],
 pente=[{'s': 'Revenu', 'd': 'en cloche : faible chez les jeunes, maximal en '
         'milieu de vie active, il chute à la retraite. C’est le constat de '
         'départ de Modigliani : le revenu est réparti de façon inégale sur '
         'la durée de la vie.'},
        {'s': 'Consommation', 'd': 'quasi plate : c’est le lissage. Elle ne '
         'suit pas les variations du revenu courant.'},
        {'s': 'Patrimoine', 'd': 'négatif au début — c’est l’endettement — '
         'puis croissant pendant la vie active, puis décroissant à la '
         'retraite.'}],
 fig={'series': [
   pol('rev', 'Revenu', REV, 'ac', ep=3.2, lp=[0.88, 0.22]),
   pol('cons', 'Consommation', CONS, 'ac2', ep=3.2, lp=[0.9, 0.58]),
 ]},
 etapes=[
  etape('Le revenu varie beaucoup au cours de la vie',
        'Le constat de départ de Modigliani : le revenu est réparti de façon '
        'inégale sur la durée de la vie. Il est faible dans la jeunesse, '
        'maximal en milieu de carrière, et chute à la retraite.',
        on=['rev'], vif=['rev']),
  etape('La consommation, elle, est lissée',
        'L’individu rationnel et prévoyant planifie son niveau de vie sur '
        'l’ensemble de son existence. Sa consommation est donc beaucoup plus '
        'stable que son revenu : c’est le lissage.',
        on=['cons'], vif=['cons']),
  etape('Phase A — les jeunes s’endettent',
        'Tant que le revenu est inférieur à la consommation, il faut bien '
        'financer l’écart : les jeunes s’endettent. Leur patrimoine est '
        'négatif.',
        add=[zone('za', 'A — endettement',
                  [(0.04, 0.42), (0.2, 0.46), (0.28, 0.48), (0.28, 0.44),
                   (0.2, 0.3), (0.04, 0.08)], 'ko')],
        vif=['za']),
  etape('Phase B — les actifs épargnent',
        'En milieu de vie active, le revenu dépasse la consommation : '
        'l’individu épargne. L’objectif est explicite chez Modigliani : ne '
        'pas voir sa consommation baisser substantiellement durant la '
        'retraite.',
        add=[zone('zb', 'B — épargne',
                  [(0.28, 0.48), (0.44, 0.76), (0.56, 0.86), (0.68, 0.74),
                   (0.76, 0.52), (0.6, 0.52), (0.44, 0.5), (0.28, 0.48)],
                  'ok')],
        off=['za'],
        vif=['zb']),
  etape('Phase C — les retraités désépargnent',
        'Le revenu chute à la retraite, mais la consommation reste au même '
        'niveau : l’individu puise dans ce qu’il a épargné au cours de sa '
        'vie. C’est la désépargne.',
        add=[zone('zc', 'C — désépargne',
                  [(0.76, 0.52), (0.88, 0.52), (0.97, 0.5), (0.97, 0.18),
                   (0.86, 0.14)], 'jn')],
        off=['zb'],
        vif=['zc']),
  etape('La courbe de patrimoine résume les trois phases',
        'Négatif au début — c’est l’endettement — le patrimoine croît pendant '
        'la vie active puis décroît à la retraite. Modigliani montre ainsi '
        'comment les décisions individuelles se traduisent au niveau global '
        'par la structure du capital.',
        add=[pol('pat', 'Patrimoine', PAT, 'bl', ep=3, lp=[0.74, 0.9])],
        off=['zc'],
        vif=['pat']),
  etape('Ce que le modèle ajoute à Keynes',
        'Keynes fait dépendre la consommation du seul revenu courant. '
        'Modigliani y ajoute la richesse et l’âge : la consommation varie '
        'selon la position dans le cycle de vie, ce que le modèle keynésien '
        'ne faisait pas.',
        add=[txt('tk', 'C = f(revenu courant, patrimoine, âge)', 0.1, 0.95,
                 'ac', taille=15, gras=True)],
        vif=['tk']),
  etape('Le lien avec Friedman et les limites',
        'Comme Friedman, Modigliani fait de l’individu un agent rationnel qui '
        'ne consomme pas de manière impulsive. Son modèle décrit bien les '
        'États-Unis des années 1950, où l’héritage est peu courant et où le '
        'patrimoine est accumulé plutôt qu’hérité.',
        add=[txt('tl', 'modèle calé sur une société où l’on hérite peu',
                 0.1, 0.88, 'jn', taille=14, gras=True)],
        off=['tk'],
        vif=['tl']),
 ],
 pieges=[
  {'t': 'Ce n’est pas le temps calendaire mais l’âge',
   'd': 'L’abscisse suit un individu au fil de sa vie. Y lire une conjoncture '
        'ou une évolution historique est un contresens.'},
  {'t': 'Désépargner n’est pas s’appauvrir brutalement',
   'd': 'C’est consommer son patrimoine comme prévu : le modèle suppose '
        'précisément que l’épargne de la vie active a été constituée pour '
        'cela.'},
  {'t': 'Modigliani complète Keynes, il ne le réfute pas',
   'd': 'La consommation dépend toujours en partie du revenu courant. Ce que '
        'Modigliani ajoute, c’est le patrimoine et l’âge — et c’est ce qui '
        'résout l’énigme de la consommation.'},
 ],
 main=[
  'Trace les axes : l’âge en abscisse, le revenu et la consommation en '
  'ordonnée.',
  'Trace le revenu en cloche : faible, puis maximal, puis en chute à la '
  'retraite.',
  'Trace la consommation presque horizontale, qui coupe le revenu à deux '
  'reprises.',
  'Hachure les trois zones et nomme-les : A endettement, B épargne, '
  'C désépargne.',
  'Ajoute enfin la courbe de patrimoine : négative, puis croissante, puis '
  'décroissante.',
 ],
 phrase='Le modèle du cycle de vie de Modigliani montre que la consommation '
        'des ménages ne dépend pas seulement du revenu courant mais aussi du '
        'patrimoine et de l’âge : comme l’individu rationnel lisse sa '
        'consommation sur l’ensemble de son existence alors que son revenu '
        'suit une cloche, il s’endette dans sa jeunesse, épargne pendant sa '
        'vie active et désépargne à la retraite.',
 liens=[{'c': '1', 'b': 373, 'l': 'Modigliani et l’énigme de la consommation'},
        {'c': '1', 'b': 376, 'l': 'L’inégale répartition du revenu sur la vie'},
        {'c': '1', 'b': 378, 'l': 'Les trois phases A, B et C'},
        {'c': '1', 'b': 384, 'l': 'Les trois atouts du modèle'},
        {'c': '1', 'b': 437, 'l': 'Les critiques du modèle de Modigliani'}],
 mots=['Modigliani', 'cycle de vie', 'lissage', 'désépargne', 'patrimoine',
       'consommation', 'Friedman'],
))

# ------------------------------------------------------- courbe de Phillips
PHI = courbe_dec(0.12, 0.88, 0.95, 0.08, n=11, creux=0.42)
PHI2 = [(x + 0.18, y) for x, y in PHI if x + 0.18 <= 1.0]

L.append(fiche(
 id='phillips',
 t='La courbe de Phillips et sa critique',
 st='L’arbitrage inflation-chômage existe-t-il ? Deux réponses, deux '
    'graphiques.',
 cat='macro', an=1, ch=['2', '3'],
 type='schema',
 q='Peut-on durablement réduire le chômage en acceptant un peu plus '
   'd’inflation, et que change l’hypothèse d’illusion monétaire ?',
 axes={'x': 'Taux de chômage', 'y': 'Taux d’inflation'},
 depart='Une économie où le chômage est élevé et l’inflation modérée.',
 hyp=['En 1958, Alban W. Phillips observe une relation inverse entre le taux '
      'de croissance des salaires nominaux et celui du chômage, à partir '
      'd’une étude empirique sur le Royaume-Uni entre 1861 et 1957.',
      'Cette relation n’est ni linéaire ni stable, et Samuelson et Solow la '
      'confirment pour les États-Unis.',
      'Toute la divergence porte sur une seule hypothèse : les salariés '
      'sont-ils, ou non, victimes d’illusion monétaire ?'],
 pente=[{'s': 'Courbe décroissante et convexe', 'd': 'quand le chômage est '
         'faible, les salariés obtiennent des hausses de salaires, qui '
         'élèvent les coûts puis les prix. D’où la relation inverse entre '
         'chômage et inflation.'},
        {'s': 'Droite verticale', 'd': 'au niveau du chômage naturel : une '
         'inflation plus forte ne change plus rien au chômage, quel que soit '
         'son niveau.'}],
 fig={'series': [
   pol('ph', 'Courbe de Phillips', PHI, 'ac', ep=3.4, lp=[0.74, 0.5]),
   pt('a', 'A', 0.62, round(y_de([0.12, 0.88, 0.95, 0.08], 0.62), 4), 'ac2'),
   rep('ra', 0.62, round(y_de([0.12, 0.88, 0.95, 0.08], 0.62), 4),
       lx='u₀', ly='π₀', c='ac2'),
 ]},
 variantes=[
  {'lib': 'Les keynésiens : l’arbitrage existe',
   'etapes': [
     etape('La relation observée par Phillips',
           'Quand le chômage est faible, les salariés demandent des hausses '
           'de salaires ; plus de salaires signifie des coûts plus élevés, '
           'donc des prix plus élevés, donc de l’inflation. La relation est '
           'inverse.',
           on=['ph', 'a', 'ra'], vif=['ph', 'a', 'ra']),
     etape('Le mécanisme keynésien',
           'L’inflation fait baisser les salaires réels, donc les entreprises '
           'embauchent davantage. Une inflation modérée peut ainsi faire '
           'baisser le chômage.',
           add=[txt('tk', 'inflation → salaires réels ↓ → embauches ↑',
                    0.18, 0.95, 'ok', taille=15, gras=True)],
           vif=['tk']),
     etape('L’État peut donc choisir son point',
           'Les gouvernements des années 1960 et 1970 en tirent une '
           'conclusion politique : « si on accepte un peu d’inflation, on '
           'peut réduire le chômage ». L’arbitrage devient un instrument.',
           add=[pt('b', 'B', 0.3, round(y_de([0.12, 0.88, 0.95, 0.08], 0.3), 4),
                   'ok'),
                rep('rb', 0.3, round(y_de([0.12, 0.88, 0.95, 0.08], 0.3), 4),
                    lx='u₁', ly='π₁', c='ok'),
                fl('fm', 'on se déplace SUR la courbe', 0.58, 0.42, 0.36, 0.66,
                   'ok')],
           off=['tk'],
           vif=['b', 'rb', 'fm']),
     etape('Une relation confirmée empiriquement',
           'Samuelson et Solow confirment la relation pour les États-Unis : '
           'en période de croissance, l’inflation est élevée et le chômage '
           'faible. Le cours rappelle que la relation n’est pour autant ni '
           'linéaire ni stable.',
           add=[txt('ts', 'Samuelson et Solow : confirmation américaine',
                    0.18, 0.95, 'ac', taille=15, gras=True)],
           off=['fm'],
           vif=['ts']),
   ]},
  {'lib': 'Friedman : verticale à long terme',
   'etapes': [
     etape('Le même point de départ',
           'Friedman ne conteste pas l’observation de Phillips. Il conteste '
           'son interprétation : la courbe peut exister à court terme, mais '
           'pour une raison précise.',
           on=['ph', 'a', 'ra'], vif=['ph', 'a', 'ra']),
     etape('À court terme : l’illusion monétaire',
           'La courbe peut exister parce que les salariés sont victimes '
           'd’illusion monétaire : les prix montent, mais ils ne voient pas '
           'tout de suite que leur salaire réel baisse. Ils acceptent donc de '
           'travailler davantage.',
           add=[pt('b', 'B', 0.3, round(y_de([0.12, 0.88, 0.95, 0.08], 0.3), 4),
                   'ok'),
                txt('ti', 'court terme : illusion monétaire', 0.2, 0.95,
                    'ok', taille=15, gras=True)],
           vif=['b', 'ti']),
     etape('À long terme, l’illusion se dissipe',
           'Les salariés voient que les prix montent, ils demandent des '
           'hausses de salaires nominaux, les entreprises doivent augmenter '
           'leurs prix encore. Et les entreprises, anticipant ces hausses, '
           'n’embauchent pas davantage.',
           add=[pol('ph2', 'Phillips anticipée', PHI2, 'ac2', ep=3,
                    lp=[0.92, 0.72]),
                fl('fd', 'la courbe se déplace', 0.42, 0.78, 0.6, 0.78, 'ac2')],
           off=['ti'],
           vif=['ph2', 'fd']),
     etape('Le chômage revient à son niveau naturel',
           'Le chômage retourne au taux naturel, le NAIRU : seule l’inflation '
           'est plus forte. On ne s’est pas déplacé SUR la courbe, c’est la '
           'courbe qui s’est déplacée.',
           add=[pt('c', 'C', 0.62, 0.62, 'ko'),
                lin('nairu', 'Phillips de long terme', 0.62, 0.02, 0.62, 0.96,
                    'ko', ep=3, lp=[0.78, 0.96])],
           off=['fd'],
           vif=['c', 'nairu']),
     etape('La vérification par la stagflation',
           'Lors du choc pétrolier, les firmes voient leurs coûts augmenter '
           'et sont obligées de licencier : inflation ET chômage. La '
           'stagflation détruit expérimentalement la courbe de Phillips, '
           'puisque l’inflation n’a pas fait baisser le chômage.',
           add=[pt('s', '', 0.78, 0.82, 'jn'),
                txt('tst', 'stagflation : les deux montent', 0.06, 0.05, 'jn',
                    taille=15, gras=True)],
           vif=['s', 'tst']),
     etape('La conclusion de Friedman',
           'La monnaie est toute puissante puisqu’elle détermine l’inflation '
           'à long terme, mais la politique monétaire est impuissante '
           'puisque les individus anticipent. D’où sa solution : laisser le '
           'chômage revenir à son niveau naturel et contrôler la croissance '
           'de la masse monétaire selon la règle de k %.',
           add=[txt('tf', 'monnaie puissante, politique monétaire impuissante',
                    0.1, 0.06, 'bl', taille=15, gras=True)],
           off=['tst'],
           vif=['tf']),
   ]},
 ],
 pieges=[
  {'t': 'Déplacement sur la courbe ou déplacement de la courbe',
   'd': 'Les keynésiens font glisser l’économie SUR la courbe : l’arbitrage '
        'est réel. Friedman fait se DÉPLACER la courbe sous l’effet des '
        'anticipations : il n’y a plus d’arbitrage. C’est toute la '
        'controverse, et elle tient dans ce mot.'},
  {'t': 'Courbe originelle et courbe augmentée',
   'd': 'La courbe de 1958 relie chômage et croissance des salaires '
        'nominaux ; la courbe augmentée des anticipations ajoute l’inflation '
        'anticipée. Préciser laquelle on commente évite la confusion.'},
  {'t': 'La stagflation n’invalide pas la courbe de court terme',
   'd': 'Elle montre qu’un choc d’offre déplace la courbe entière. Dire « la '
        'courbe de Phillips est fausse » est trop rapide : elle est instable, '
        'ce qui n’est pas la même chose.'},
 ],
 main=[
  'Trace les axes : le taux de chômage en abscisse, le taux d’inflation en '
  'ordonnée.',
  'Trace une courbe décroissante et convexe, et place un point A dessus.',
  'Pour le cas keynésien, fais glisser le point vers le haut à gauche : moins '
  'de chômage, plus d’inflation.',
  'Pour le cas de Friedman, trace une seconde courbe décalée vers la droite '
  'et une verticale au niveau du chômage naturel.',
  'Marque enfin un point au-dessus et à droite pour la stagflation : '
  'inflation et chômage augmentent ensemble.',
 ],
 phrase='La courbe de Phillips, observée en 1958 sur le Royaume-Uni et '
        'confirmée par Samuelson et Solow, établit une relation inverse entre '
        'chômage et inflation dont les keynésiens tirent un arbitrage '
        'utilisable par l’État ; mais pour Friedman cette relation ne tient '
        'qu’à l’illusion monétaire, de sorte qu’à long terme les '
        'anticipations déplacent la courbe, le chômage revient à son niveau '
        'naturel et la courbe de Phillips devient verticale.',
 liens=[{'c': '2', 'b': 328, 'l': 'Le point de départ keynésien'},
        {'c': '2', 'b': 333, 'l': 'Phillips 1958 et l’étude du Royaume-Uni'},
        {'c': '2', 'b': 341, 'l': 'Ce que disent les monétaristes'},
        {'c': '2', 'b': 366, 'l': 'Pourquoi la courbe ne marche plus dans les années 1970'},
        {'c': '3', 'b': 1065, 'l': 'Le chômage et la remise en cause de la courbe de Phillips'}],
 mots=['Phillips', 'Friedman', 'illusion monétaire', 'NAIRU', 'stagflation',
       'chômage naturel', 'Samuelson', 'Solow'],
))

# ------------------------------------------------------- triangle de Mundell
L.append(fiche(
 id='triangle-mundell',
 t='Le triangle des incompatibilités de Mundell',
 st='Trois objectifs souhaitables, deux seulement atteignables.',
 cat='ouverte', an=1, ch=['2', '25', '26'],
 type='schema',
 q='Pourquoi un pays ne peut-il pas, en même temps, fixer son change, laisser '
   'circuler les capitaux et garder une politique monétaire autonome ?',
 axes={'x': '', 'y': '', 'sans': 1},
 depart='Un triangle dont chaque sommet porte un objectif de politique '
        'économique.',
 hyp=['Les trois objectifs sont tous souhaitables : stabilité du change, '
      'libre circulation des capitaux, autonomie de la politique monétaire.',
      'Le théorème énonce qu’il est impossible de les avoir tous les trois en '
      'même temps : chaque côté du triangle représente une combinaison de '
      'deux objectifs, obtenue en renonçant au troisième.',
      'Le raisonnement suppose que les mouvements de capitaux réagissent aux '
      'écarts de taux d’intérêt : c’est ce qui crée l’incompatibilité.'],
 pente=[{'s': 'Lecture du schéma', 'd': 'ce n’est pas une courbe mais un '
         'triangle : chaque sommet est un objectif, chaque côté la '
         'combinaison des deux objectifs qu’il relie — donc l’abandon du '
         'troisième.'}],
 fig={'series': [
   lin('c1', '', 0.5, 0.92, 0.1, 0.14, 'ac', ep=3),
   lin('c2', '', 0.5, 0.92, 0.9, 0.14, 'ac', ep=3),
   lin('c3', '', 0.1, 0.14, 0.9, 0.14, 'ac', ep=3),
   pt('s1', '', 0.5, 0.92, 'ac2'),
   pt('s2', '', 0.1, 0.14, 'ac2'),
   pt('s3', '', 0.9, 0.14, 'ac2'),
   txt('t1', 'Stabilité du change', 0.33, 0.97, 'ac2', taille=15, gras=True),
   txt('t2', 'Libre circulation', 0.0, 0.08, 'ac2', taille=15, gras=True),
   txt('t2b', 'des capitaux', 0.02, 0.02, 'ac2', taille=15, gras=True),
   txt('t3', 'Autonomie', 0.78, 0.08, 'ac2', taille=15, gras=True),
   txt('t3b', 'monétaire', 0.79, 0.02, 'ac2', taille=15, gras=True),
 ]},
 etapes=[
  etape('Trois objectifs souhaitables',
        'La stabilité du change rassure les échanges ; la libre circulation '
        'des capitaux finance l’économie ; l’autonomie monétaire permet de '
        'réagir à la conjoncture nationale. Chacun est désirable pris '
        'isolément.',
        on=['s1', 's2', 's3', 't1', 't2', 't2b', 't3', 't3b'],
        vif=['s1', 's2', 's3']),
  etape('Mais on ne peut en retenir que deux',
        'Le théorème énonce l’impossibilité de les atteindre tous les trois '
        'simultanément. Chaque côté du triangle désigne une combinaison de '
        'deux objectifs — et donc le renoncement au troisième.',
        on=['c1', 'c2', 'c3'], vif=['c1', 'c2', 'c3']),
  etape('Premier choix : change fixe et capitaux libres',
        'C’est le côté gauche. On renonce alors à l’autonomie monétaire : la '
        'banque centrale doit consacrer sa politique à défendre la parité. '
        'C’est exactement ce que montre Mundell-Fleming en changes fixes.',
        add=[txt('e1', 'on abandonne l’autonomie monétaire', 0.32, 0.52, 'ko',
                 taille=13, gras=True)],
        seul=['c1', 's1', 's2', 't1', 't2', 't2b', 'e1'],
        vif=['c1', 'e1']),
  etape('Deuxième choix : change fixe et autonomie monétaire',
        'C’est la base du triangle. Pour les tenir ensemble, il faut '
        'contrôler les mouvements de capitaux. C’est le régime de Bretton '
        'Woods, et celui de la France jusqu’aux années 1980.',
        add=[txt('e2', 'on contrôle les capitaux', 0.33, 0.22, 'ko',
                 taille=13, gras=True)],
        seul=['c3', 's2', 's3', 't2', 't2b', 't3', 't3b', 'e2'],
        vif=['c3', 'e2']),
  etape('Troisième choix : capitaux libres et autonomie monétaire',
        'C’est le côté droit. Il faut alors renoncer à la stabilité du '
        'change : la monnaie flotte. C’est la configuration des grandes '
        'économies depuis la fin de Bretton Woods.',
        add=[txt('e3', 'on laisse flotter le change', 0.33, 0.52, 'ko',
                 taille=13, gras=True)],
        seul=['c2', 's1', 's3', 't1', 't3', 't3b', 'e3'],
        vif=['c2', 'e3']),
  etape('Le triangle résume une histoire monétaire',
        'Jean-Marc Daniel écrit que le monde a accompli une sorte de parcours '
        'complet en essayant toutes les éventualités offertes par le '
        'triangle. Chaque régime de change historique en occupe un côté.',
        seul=['c1', 'c2', 'c3', 's1', 's2', 's3', 't1', 't2', 't2b', 't3',
              't3b'],
        add=[txt('eh', 'chaque régime historique occupe un côté', 0.29, 0.44,
                 'bl', taille=13, gras=True)],
        vif=['eh']),
  etape('L’application à la zone euro',
        'Les États membres ont choisi la stabilité absolue du change — la '
        'monnaie unique — et la libre circulation des capitaux. Ils ont donc '
        'abandonné l’autonomie monétaire nationale, transférée à la banque '
        'centrale commune.',
        add=[txt('ez', 'zone euro : change fixe + capitaux libres', 0.28, 0.33,
                 'ok', taille=13, gras=True)],
        off=['eh'],
        vif=['ez', 'c1']),
 ],
 pieges=[
  {'t': 'Les sommets sont les objectifs, les côtés les choix',
   'd': 'On inverse souvent les deux. Un côté relie deux sommets : il '
        'représente la combinaison que l’on retient, donc le sommet opposé '
        'est celui auquel on renonce.'},
  {'t': 'L’incompatibilité vient de la mobilité des capitaux',
   'd': 'Sans mobilité, on peut tenir change fixe et autonomie monétaire. '
        'C’est la mobilité qui transmet instantanément tout écart de taux au '
        'change et crée le dilemme.'},
  {'t': 'Le triangle ne dit pas quel côté choisir',
   'd': 'Il énonce une contrainte, pas une recommandation. Le choix dépend de '
        'la structure de l’économie et des préférences politiques, ce que le '
        'chapitre sur les régimes de change développe longuement.'},
 ],
 main=[
  'Trace un triangle et place un objectif à chaque sommet.',
  'Repasse le côté gauche : change fixe et capitaux libres — barre '
  'l’autonomie monétaire.',
  'Repasse la base : change fixe et autonomie monétaire — barre la libre '
  'circulation des capitaux.',
  'Repasse le côté droit : capitaux libres et autonomie — barre la stabilité '
  'du change.',
  'Associe à chaque côté un exemple historique : zone euro, Bretton Woods, '
  'changes flottants.',
 ],
 phrase='Le triangle des incompatibilités de Mundell révèle que la stabilité '
        'des changes, l’autonomie monétaire et la parfaite mobilité des '
        'capitaux ne peuvent être simultanément garanties : chaque côté du '
        'triangle correspond au renoncement à l’un des trois objectifs, ce '
        'qui impose aux États un arbitrage que l’histoire monétaire a exploré '
        'tour à tour.',
 liens=[{'c': '2', 'b': 169, 'l': 'Le triangle de Mundell (ch. 2, le risque de change)'},
        {'c': '25', 'b': 3221, 'l': 'Le triangle et les limites de l’autonomie monétaire'},
        {'c': '26', 'b': 1691, 'l': 'Trois objectifs souhaitables mais incompatibles'},
        {'c': '26', 'b': 1730, 'l': 'Jean-Marc Daniel : le parcours complet du triangle'}],
 mots=['triangle de Mundell', 'incompatibilités', 'mobilité des capitaux',
       'autonomie monétaire', 'régime de change', 'zone euro'],
))

# --------------------------------------------------------------- cycles
def _onde(amp, per, dec, base=0.5, n=70, a=0.02, b=0.98):
    out = []
    for j in range(n):
        x = a + (b - a) * j / (n - 1.0)
        out.append((round(x, 4),
                    round(base + amp * math.sin(2 * math.pi * (x - dec) / per),
                          4)))
    return out


L.append(fiche(
 id='cycles-kondratiev',
 t='Kitchin, Juglar, Kondratiev : trois temporalités',
 st='Des cycles courts dans des cycles moyens dans des cycles longs.',
 cat='croissance', an=1, ch=['8'],
 type='schema',
 q='Pourquoi le capitalisme est-il traversé par plusieurs temporalités à la '
   'fois, et pourquoi Schumpeter relie-t-il l’innovation surtout aux cycles '
   'longs ?',
 axes={'x': 'Temps', 'y': 'Activité économique'},
 depart='Une économie dont on suit l’activité sur plusieurs décennies.',
 hyp=['On retient généralement trois grands types de cycles, qui peuvent se '
      'superposer.',
      'Il ne faut pas les penser comme des mécanismes isolés : des cycles '
      'courts peuvent apparaître à l’intérieur d’un cycle moyen, et '
      'plusieurs cycles moyens à l’intérieur d’un cycle long.',
      'Chez Schumpeter, tous les cycles ne s’expliquent pas de la même '
      'manière : seuls les cycles longs sont portés par les grappes '
      'd’innovations.'],
 pente=[{'s': 'Cycle de Kondratiev', 'd': 'une onde longue de 50 à 60 ans, '
         'partagée en une phase ascendante de 25 à 30 ans et une phase '
         'descendante de même durée.'},
        {'s': 'Cycle de Juglar', 'd': 'une oscillation moyenne de 8 à 10 ans, '
         'liée à l’investissement et au crédit, avec ses quatre phases : '
         'reprise, expansion, crise, dépression.'},
        {'s': 'Cycle de Kitchin', 'd': 'une oscillation courte de 3 à 5 ans, '
         'liée aux variations de stocks et aux ajustements rapides de la '
         'production.'}],
 fig={'series': [
   pol('kd', 'Kondratiev — 50 à 60 ans', _onde(0.3, 1.0, 0.25), 'ac', ep=3.4,
       lp=[0.20, 0.87]),
 ]},
 etapes=[
  etape('Le cycle long de Kondratiev',
        'Du nom de l’économiste soviétique Nikolaï Kondratiev (1892-1938), '
        'ce sont des cycles longs d’environ 50 à 60 ans. Une onde ample, qui '
        'traverse plusieurs générations.',
        on=['kd'], vif=['kd']),
  etape('Sa phase ascendante',
        'Elle dure environ 25 à 30 ans et correspond à l’apparition '
        'd’innovations en grappe : plusieurs innovations majeures se '
        'diffusent ensemble et restructurent durablement l’économie.',
        add=[fl('fa', 'grappe d’innovations', 0.3, 0.74, 0.5, 0.82, 'ok')],
        vif=['fa']),
  etape('Sa phase descendante',
        'Elle dure également 25 à 30 ans et correspond à l’essoufflement du '
        'rythme des innovations : la vague s’épuise, une phase de '
        'ralentissement apparaît.',
        add=[fl('fd', 'essoufflement', 0.62, 0.72, 0.82, 0.28, 'ko')],
        off=['fa'],
        vif=['fd']),
  etape('Le cycle moyen de Juglar, à l’intérieur',
        'Huit à dix ans, lié surtout à l’investissement et au crédit, avec '
        'ses quatre phases classiques : reprise, expansion, crise, '
        'dépression. Plusieurs Juglar s’inscrivent dans un seul Kondratiev.',
        add=[pol('jg', 'Juglar — 8 à 10 ans', _onde(0.12, 0.26, 0.05, 0.5),
                 'ok', ep=2.4, lp=[0.66, 0.90])],
        off=['fd'],
        vif=['jg']),
  etape('Le cycle court de Kitchin, à l’intérieur encore',
        'Trois à cinq ans, lié aux variations de stocks, aux ajustements '
        'rapides de la production et aux désajustements entre offre et '
        'demande. Des Kitchin apparaissent à l’intérieur d’un Juglar.',
        add=[pol('kt', 'Kitchin — 3 à 5 ans', _onde(0.05, 0.1, 0.02, 0.5),
                 'ac2', ep=2, lp=[0.42, 0.14])],
        vif=['kt']),
  etape('Trois temporalités simultanées',
        'Le capitalisme est traversé en même temps par une temporalité courte '
        'liée aux stocks, une temporalité moyenne liée à l’investissement et '
        'au crédit, et une temporalité longue liée aux transformations '
        'structurelles.',
        add=[txt('tt', 'stocks · investissement · transformations structurelles',
                 0.08, 0.04, 'bl', taille=14, gras=True)],
        vif=['tt', 'kd', 'jg', 'kt']),
  etape('Le lien avec Schumpeter',
        'Les grappes d’innovations alimentent surtout les cycles longs de '
        'type Kondratiev, tandis que les cycles courts relèvent d’ajustements '
        'conjoncturels. La première révolution industrielle illustre '
        'parfaitement une phase ascendante de cycle long.',
        add=[txt('ts', 'innovation → cycles longs ; conjoncture → cycles courts',
                 0.08, 0.95, 'jn', taille=15, gras=True)],
        off=['tt'],
        vif=['ts']),
 ],
 pieges=[
  {'t': 'Les cycles ne sont pas isolés : ils se superposent',
   'd': 'Dessiner trois graphiques séparés rate l’essentiel. C’est leur '
        'emboîtement qui fait l’idée : plusieurs temporalités agissent en '
        'même temps sur la même économie.'},
  {'t': 'Un cycle n’est pas une crise',
   'd': 'La crise n’est qu’une des quatre phases du Juglar — reprise, '
        'expansion, crise, dépression. Confondre le cycle et sa phase basse '
        'conduit à un commentaire faux.'},
  {'t': 'Schumpeter n’explique pas tous les cycles par l’innovation',
   'd': 'Il l’associe principalement aux cycles longs. Expliquer un cycle de '
        'stocks par une grappe d’innovations est un contresens sur sa '
        'théorie.'},
 ],
 main=[
  'Trace les axes : le temps en abscisse, l’activité économique en ordonnée.',
  'Trace une grande onde ample qui monte sur la moitié du graphique puis '
  'redescend : c’est Kondratiev.',
  'Annote sa phase ascendante — grappe d’innovations — et sa phase '
  'descendante — essoufflement.',
  'Superpose une oscillation plus rapide et plus faible : Juglar.',
  'Superpose enfin une oscillation encore plus rapide et minime : Kitchin.',
 ],
 phrase='Le capitalisme est traversé par trois temporalités simultanées : les '
        'cycles courts de Kitchin, de trois à cinq ans, liés aux variations '
        'de stocks ; les cycles moyens de Juglar, de huit à dix ans, liés à '
        'l’investissement et au crédit ; et les cycles longs de Kondratiev, '
        'de cinquante à soixante ans, que Schumpeter rattache aux grappes '
        'd’innovations majeures qui restructurent durablement l’économie.',
 liens=[{'c': '8', 'b': 1042, 'l': 'Les cycles économiques : Kitchin, Juglar et Kondratiev'},
        {'c': '8', 'b': 1063, 'l': 'Les cycles de Kondratiev et leurs deux phases'},
        {'c': '8', 'b': 1072, 'l': 'Ces cycles peuvent se superposer'},
        {'c': '8', 'b': 1080, 'l': 'Le lien avec Schumpeter : l’innovation et les cycles longs'}],
 mots=['Kondratiev', 'Juglar', 'Kitchin', 'Schumpeter',
       'grappes d’innovations', 'cycles', 'révolution industrielle'],
))

# --------------------------------------------------------- pyramide des âges
def _pyr(largeurs, cote):
    """Demi-pyramide : une zone par tranche d'âge, à gauche ou à droite."""
    out = []
    h = 0.92 / len(largeurs)
    for i, w in enumerate(largeurs):
        y0, y1 = 0.04 + i * h, 0.04 + (i + 1) * h - 0.008
        if cote < 0:
            x0, x1 = 0.49 - w, 0.49
        else:
            x0, x1 = 0.51, 0.51 + w
        out.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
    return out


JEUNE = [0.42, 0.38, 0.33, 0.28, 0.23, 0.18, 0.13, 0.08, 0.04]
VIEUX = [0.18, 0.2, 0.24, 0.28, 0.3, 0.3, 0.27, 0.2, 0.1]

L.append(fiche(
 id='pyramide-ages',
 t='La pyramide des âges',
 st='La forme de la population raconte son histoire démographique.',
 cat='croissance', an=1, ch=['7'],
 type='schema',
 q='Que lit-on sur une pyramide des âges, et comment sa forme révèle-t-elle '
   'le stade de la transition démographique d’un pays ?',
 axes={'x': 'Effectifs — hommes à gauche, femmes à droite',
       'y': 'Tranches d’âge'},
 depart='Une population représentée par tranches d’âge, des plus jeunes en '
        'bas aux plus âgés en haut.',
 hyp=['La pyramide des âges est une représentation graphique de la population '
      'selon l’âge et le sexe.',
      'Chaque barre horizontale est une tranche d’âge : sa longueur mesure '
      'l’effectif de cette tranche.',
      'Les hommes sont représentés à gauche de l’axe central, les femmes à '
      'droite.'],
 pente=[{'s': 'Base large', 'd': 'une natalité élevée : les tranches jeunes '
         'sont nombreuses. C’est le signe d’une transition démographique '
         'inachevée.'},
        {'s': 'Sommet étroit', 'd': 'une mortalité encore forte aux âges '
         'élevés, ou simplement une population dont les générations '
         'anciennes étaient moins nombreuses.'},
        {'s': 'Forme en urne ou en champignon', 'd': 'une natalité faible '
         'depuis longtemps et une longévité élevée : c’est le vieillissement.'}],
 fig={'series': [
   lin('axe', '', 0.5, 0.0, 0.5, 0.99, 'gr', ep=1.6),
   txt('th', 'Hommes', 0.14, 0.98, 'gr', taille=14),
   txt('tf', 'Femmes', 0.72, 0.98, 'gr', taille=14),
 ]},
 variantes=[
  {'lib': 'Population jeune',
   'etapes': [
     etape('Une base très large',
           'Les tranches d’âge jeunes sont bien plus nombreuses que les '
           'autres : la natalité est élevée. C’est la forme classique d’une '
           'population au début ou au milieu de sa transition '
           'démographique.',
           on=['axe', 'th', 'tf'],
           add=([zone('jh%d' % i, '', p, 'ac')
                 for i, p in enumerate(_pyr(JEUNE, -1))] +
                [zone('jf%d' % i, '', p, 'ac2')
                 for i, p in enumerate(_pyr(JEUNE, 1))]),
           vif=['jh0', 'jf0', 'jh1', 'jf1']),
     etape('Un sommet étroit',
           'Peu de personnes âgées : la mortalité reste élevée aux grands '
           'âges, et les générations anciennes étaient moins nombreuses. La '
           'silhouette est bien celle d’une pyramide.',
           vif=['jh7', 'jf7', 'jh8', 'jf8']),
     etape('Ce que cela implique économiquement',
           'Une population jeune signifie une population active future '
           'abondante, mais aussi une charge éducative lourde dans '
           'l’immédiat. Le rapport entre actifs et inactifs est déterminant.',
           add=[txt('te', 'actifs futurs nombreux', 0.02, 0.88, 'ok', taille=14,
                    gras=True)],
           vif=['te']),
     etape('Un stade de la transition démographique',
           'Cette forme correspond à une phase où la mortalité a déjà baissé '
           'mais où la natalité reste élevée : c’est exactement la phase de '
           'transition, celle de l’accroissement naturel maximal.',
           add=[txt('tt', 'mortalité basse, natalité haute', 0.02, 0.81, 'jn',
                    taille=14, gras=True)],
           off=['te'],
           vif=['tt']),
   ]},
  {'lib': 'Population vieillissante',
   'etapes': [
     etape('Une base étroite',
           'Les jeunes tranches d’âge sont peu nombreuses : la natalité est '
           'faible depuis longtemps. La figure ne ressemble plus à une '
           'pyramide.',
           on=['axe', 'th', 'tf'],
           add=([zone('vh%d' % i, '', p, 'ac')
                 for i, p in enumerate(_pyr(VIEUX, -1))] +
                [zone('vf%d' % i, '', p, 'ac2')
                 for i, p in enumerate(_pyr(VIEUX, 1))]),
           vif=['vh0', 'vf0', 'vh1', 'vf1']),
     etape('Un renflement au milieu et en haut',
           'Les générations nombreuses nées autrefois sont aujourd’hui aux '
           'âges intermédiaires et élevés, et la longévité les y maintient. '
           'La forme devient celle d’une urne, voire d’un champignon.',
           vif=['vh5', 'vf5', 'vh6', 'vf6', 'vh7', 'vf7']),
     etape('La charge du vieillissement',
           'Une population vieillissante signifie une forte dépendance '
           'démographique : les actifs doivent financer les retraites et la '
           'santé d’un nombre croissant d’inactifs âgés.',
           add=[txt('tc', 'forte dépendance démographique', 0.02, 0.88, 'ko',
                    taille=14, gras=True)],
           vif=['tc']),
     etape('Le résultat final de la transition',
           'C’est l’aboutissement du régime démographique moderne : natalité '
           'faible, mortalité faible, et transformation durable de la '
           'structure par âge.',
           add=[txt('tf2', 'natalité et mortalité faibles', 0.02, 0.81, 'jn',
                    taille=14, gras=True)],
           off=['tc'],
           vif=['tf2']),
   ]},
 ],
 pieges=[
  {'t': 'L’abscisse n’est pas un temps',
   'd': 'Elle porte des effectifs, de part et d’autre d’un axe central. C’est '
        'l’ordonnée qui porte l’âge, et donc, indirectement, l’histoire des '
        'générations.'},
  {'t': 'Un creux n’est pas forcément une baisse de natalité',
   'd': 'Il peut traduire une guerre, une épidémie ou une émigration qui a '
        'frappé une génération donnée. Lire la cause dans la seule forme est '
        'imprudent.'},
  {'t': 'Pyramide et transition démographique se lisent ensemble',
   'd': 'La pyramide est une photographie à un instant ; la transition est un '
        'film. L’une s’explique par l’autre : base large pour une transition '
        'inachevée, urne pour une transition achevée.'},
 ],
 main=[
  'Trace un axe vertical au centre de la feuille : les hommes à gauche, les '
  'femmes à droite.',
  'Gradue l’ordonnée en tranches d’âge, des plus jeunes en bas aux plus âgés '
  'en haut.',
  'Pour une population jeune, trace des barres très longues en bas qui se '
  'raccourcissent régulièrement vers le haut.',
  'Pour une population vieillissante, trace une base étroite et un '
  'renflement aux âges intermédiaires et élevés.',
  'Annote chaque forme : base large = natalité élevée ; renflement en haut = '
  'vieillissement.',
 ],
 phrase='La pyramide des âges représente la population par tranches d’âge et '
        'par sexe, et sa forme révèle le stade atteint dans la transition '
        'démographique : une base large signale une natalité encore élevée et '
        'une transition inachevée, tandis qu’une silhouette en urne, étroite '
        'à la base et renflée aux âges élevés, traduit l’achèvement de la '
        'transition et le vieillissement de la population.',
 liens=[{'c': '7', 'b': 988, 'l': 'La pyramide des âges : définition'},
        {'c': '7', 'b': 1245, 'l': 'La pyramide des âges et la structure par âge'},
        {'c': '7', 'b': 1148, 'l': 'La transition démographique, modèle de référence'}],
 mots=['pyramide des âges', 'structure par âge', 'vieillissement',
       'natalité', 'dépendance démographique'],
))
