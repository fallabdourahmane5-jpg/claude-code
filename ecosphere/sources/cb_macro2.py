# -*- coding: utf-8 -*-
"""Courbes du chapitre 5 de deuxième année — deuxième volet : la famille
IS-LM, les politiques conjoncturelles, le policy mix et le modèle OG-DG."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone,
                     inter, y_de, x_de, bouge, courbe_dec, courbe_cro)

IS = lin('is', 'IS', 0.08, 0.88, 0.95, 0.16, 'ac')
LM = lin('lm', 'LM', 0.08, 0.20, 0.95, 0.86, 'ok')
E = inter(IS, LM)
IS1 = bouge(IS, 0.18, 0)
E1 = inter({'p': IS1}, LM)
YSANS = round(x_de({'p': IS1}, E[1]), 4)          # revenu si r restait fixe
LM1 = bouge(LM, 0.18, 0)
EM1 = inter(IS, {'p': LM1})

L = [

# ------------------------------------------------------------------ IS
fiche(
 id='courbe-is',
 t='La courbe IS',
 st='Tous les couples revenu–taux d’intérêt qui équilibrent le marché des '
    'biens et services.',
 cat='macro', an=2, ch=['25'],
 type='schema',
 q='Pourquoi l’équilibre du marché des biens exige-t-il un revenu d’autant '
   'plus faible que le taux d’intérêt est élevé ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Une économie où l’investissement dépend négativement du taux '
        'd’intérêt et où la demande commande la production.',
 hyp=['Les prix sont fixes : l’ajustement passe par les quantités.',
      'L’investissement décroît avec le taux d’intérêt, qui en détermine le '
      'coût de financement.',
      'La consommation dépend du revenu par la propension marginale à '
      'consommer.'],
 pente=[{'s': 'IS', 'd': 'décroissante : un taux d’intérêt plus élevé '
         'décourage l’investissement, donc la demande globale, donc le revenu '
         'd’équilibre. À chaque taux correspond un seul revenu qui égalise '
         'l’épargne et l’investissement.'}],
 fig={'series': [
   IS,
   pt('a', 'A', 0.26, round(y_de(IS, 0.26), 4), 'ac2'),
   rep('ra', 0.26, round(y_de(IS, 0.26), 4), lx='Y₁', ly='r₁', c='ac2'),
   pt('b', 'B', 0.74, round(y_de(IS, 0.74), 4), 'bl'),
   rep('rb', 0.74, round(y_de(IS, 0.74), 4), lx='Y₂', ly='r₂', c='bl'),
   fl('f', '', 0.33, 0.73, 0.68, 0.33, 'gr'),
   txt('t1', 'r ↓ → I ↑ → demande ↑ → Y ↑', 0.3, 0.14, 'ac', taille=14),
 ]},
 etapes=[
  etape('Un premier point d’équilibre',
        'Partons d’un taux d’intérêt élevé r₁. L’investissement est faible, '
        'donc la demande globale est faible, donc le revenu d’équilibre Y₁ '
        'est faible : c’est le point A.',
        on=['is', 'a', 'ra'], vif=['a', 'ra']),
  etape('Un taux plus faible',
        'Abaissons le taux à r₂. L’investissement devient plus rentable, la '
        'demande globale augmente, et le multiplicateur porte le revenu '
        'd’équilibre à Y₂ : c’est le point B.',
        on=['b', 'rb'], vif=['b', 'rb']),
  etape('La courbe IS relie ces points',
        'En répétant l’opération pour chaque taux, on obtient tous les '
        'couples (Y, r) compatibles avec l’équilibre du marché des biens. '
        'Leur ensemble est la courbe IS, décroissante.',
        on=['f', 't1'], vif=['is', 'f', 't1']),
  etape('Ce qui déplace IS, et ce qui ne la déplace pas',
        'Une variation du taux d’intérêt fait glisser l’économie le long de '
        'IS. Une hausse des dépenses publiques, de la consommation autonome '
        'ou de l’investissement autonome déplace la courbe elle-même vers la '
        'droite.',
        add=[lin('is1', 'IS’', *IS1, c='ac2'),
             fl('f2', 'relance budgétaire', 0.4, 0.6, 0.58, 0.6, 'ac2')],
        vif=['is1', 'f2']),
 ],
 pieges=[
  {'t': 'Pente et déplacement',
   'd': 'La pente d’IS traduit la sensibilité de l’investissement au taux '
        'd’intérêt. Son déplacement traduit une variation des dépenses '
        'autonomes. Confondre les deux conduit à faire dire au graphique '
        'l’inverse de ce qu’il montre.'},
  {'t': 'IS n’est pas une courbe de demande',
   'd': 'Chaque point d’IS est déjà un équilibre entre épargne et '
        'investissement : la courbe relie des équilibres, elle ne représente '
        'pas les quantités offertes ou demandées d’un bien.'},
 ],
 main=[
  'Trace les axes : revenu national Y en abscisse, taux d’intérêt r en '
  'ordonnée.',
  'Place un premier point A en haut à gauche — taux élevé, revenu faible — '
  'avec ses deux pointillés.',
  'Place un second point B en bas à droite — taux faible, revenu élevé.',
  'Relie A et B par une droite décroissante et nomme-la IS.',
  'Ajoute la flèche du raisonnement : r baisse, I augmente, la demande '
  'augmente, Y augmente.',
 ],
 phrase='La courbe IS réunit tous les couples de revenu et de taux d’intérêt '
        'qui équilibrent le marché des biens et services : elle est '
        'décroissante parce qu’un taux plus faible stimule l’investissement, '
        'donc la demande globale, donc le revenu d’équilibre par le jeu du '
        'multiplicateur.',
 liens=[{'c': '25', 'b': 338, 'l': 'La courbe IS : l’équilibre du marché des biens'},
        {'c': '25', 'b': 1426, 'l': 'La courbe IS représente l’équilibre sur le marché des biens'}],
 mots=['IS', 'investissement', 'taux d’intérêt', 'Hicks', 'multiplicateur'],
),

# ------------------------------------------------------------------ LM
fiche(
 id='courbe-lm',
 t='La courbe LM et ses trois phases',
 st='Pourquoi l’équilibre monétaire exige un taux d’intérêt d’autant plus '
    'élevé que le revenu est grand — sauf aux deux extrêmes.',
 cat='macro', an=2, ch=['25'],
 type='schema',
 q='Pourquoi la courbe LM est-elle croissante, et pourquoi devient-elle '
   'horizontale à taux très bas et verticale à taux très élevé ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Une offre de monnaie fixée par la banque centrale et une demande de '
        'monnaie qui dépend du revenu et du taux d’intérêt.',
 hyp=['L’offre de monnaie est exogène et constante le long de la courbe.',
      'La demande de monnaie comprend une composante liée au revenu '
      '(transaction et précaution) et une composante liée au taux '
      '(spéculation).',
      'Les prix sont fixes, de sorte que l’offre réelle de monnaie ne varie '
      'pas.'],
 pente=[{'s': 'La phase croissante', 'd': 'une hausse du revenu accroît les '
         'besoins de monnaie pour transaction ; à offre constante, le taux '
         'doit monter pour réduire d’autant la demande spéculative et libérer '
         'la monnaie nécessaire.'},
        {'s': 'La phase horizontale', 'd': 'dans la trappe à liquidité, la '
         'demande spéculative absorbe toute monnaie supplémentaire : le taux '
         'ne bouge plus.'},
        {'s': 'La phase verticale', 'd': 'dans la zone classique, la demande '
         'spéculative est négligeable : le revenu compatible avec '
         'l’équilibre monétaire est fixé, quel que soit le taux.'}],
 fig={'series': [
   lin('lm1', '', 0.08, 0.2, 0.33, 0.2, 'ok', ep=3.4),
   lin('lm2', 'LM', 0.33, 0.2, 0.72, 0.74, 'ok', ep=3.4),
   lin('lm3', '', 0.72, 0.74, 0.72, 0.95, 'ok', ep=3.4),
   txt('t1', 'trappe à liquidité', 0.09, 0.13, 'ko', taille=14),
   txt('t2', 'zone normale', 0.4, 0.44, 'ok', taille=14),
   txt('t3', 'zone classique', 0.56, 0.9, 'bl', taille=14),
 ]},
 etapes=[
  etape('La phase croissante : le cas normal',
        'Une hausse du revenu accroît la demande de monnaie pour transaction. '
        'À offre de monnaie inchangée, le taux d’intérêt doit augmenter pour '
        'que les agents réduisent leurs encaisses spéculatives. D’où une '
        'relation croissante entre Y et r.',
        on=['lm2', 't2'], vif=['lm2', 't2']),
  etape('La phase horizontale : la trappe à liquidité',
        'À taux très faible, les agents anticipent sa remontée et conservent '
        'toute monnaie supplémentaire. Le taux ne peut plus baisser : la '
        'courbe devient horizontale.',
        on=['lm1', 't1'], vif=['lm1', 't1']),
  etape('La phase verticale : la zone classique',
        'À taux très élevé, la demande spéculative devient négligeable : la '
        'demande de monnaie ne dépend plus que du revenu. À offre donnée, le '
        'revenu compatible avec l’équilibre monétaire est fixé — la courbe '
        'devient verticale.',
        on=['lm3', 't3'], vif=['lm3', 't3']),
  etape('Ce que chaque phase change pour les politiques',
        'Dans la trappe, la politique budgétaire est efficace et la politique '
        'monétaire impuissante : la relance ne fait pas remonter le taux. '
        'Dans la zone classique, c’est l’inverse. Dans la phase normale, les '
        'deux agissent.',
        vif=['lm1', 'lm3']),
  etape('Ce qui déplace LM',
        'Une hausse de l’offre de monnaie déplace LM vers la droite, ce qui '
        'abaisse le taux d’équilibre à revenu donné. Une hausse des prix, en '
        'réduisant l’offre réelle de monnaie, la déplace vers la gauche.',
        add=[lin('lma', 'LM’', 0.26, 0.2, 0.51, 0.2, 'bl', ep=2.6),
             lin('lmb', '', 0.51, 0.2, 0.9, 0.74, 'bl', ep=2.6),
             fl('f', 'offre de monnaie ↑', 0.45, 0.33, 0.63, 0.33, 'bl')],
        vif=['lma', 'lmb', 'f']),
 ],
 pieges=[
  {'t': 'La pente de LM n’est pas une opinion',
   'd': 'Elle dépend de la sensibilité relative de la demande de monnaie au '
        'revenu et au taux. Une LM très pentue signale une forte réaction du '
        'taux au revenu ; une LM plate, l’inverse.'},
  {'t': 'Déplacement le long de LM ou de LM',
   'd': 'Une variation du revenu fait glisser l’économie le long de la '
        'courbe. Seule une variation de l’offre de monnaie — ou du niveau '
        'des prix — déplace la courbe elle-même.'},
 ],
 main=[
  'Trace les axes : revenu en abscisse, taux d’intérêt en ordonnée.',
  'Commence par un segment horizontal en bas à gauche : la trappe à '
  'liquidité.',
  'Prolonge par un segment croissant : la zone normale.',
  'Termine par un segment vertical en haut : la zone classique.',
  'Annote les trois zones et rappelle en marge quelle politique est efficace '
  'dans chacune.',
 ],
 phrase='La courbe LM est croissante parce qu’une hausse du revenu accroît la '
        'demande de monnaie pour transaction et impose, à offre constante, '
        'une hausse du taux d’intérêt ; elle devient horizontale dans la '
        'trappe à liquidité et verticale dans la zone classique, ce qui '
        'commande l’efficacité relative des politiques budgétaire et '
        'monétaire.',
 liens=[{'c': '25', 'b': 1326, 'l': 'La courbe LM est croissante'},
        {'c': '25', 'b': 1387, 'l': 'La courbe LM présente trois phases'},
        {'c': '25', 'b': 1610, 'l': 'L’efficacité des politiques selon la configuration'}],
 mots=['LM', 'trappe à liquidité', 'zone classique', 'offre de monnaie'],
),

# -------------------------------------------------------------- IS-LM
fiche(
 id='is-lm',
 t='Le modèle IS-LM',
 st='L’équilibre simultané du marché des biens et du marché de la monnaie, '
    'et ce qu’il ne garantit pas.',
 cat='macro', an=2, ch=['25', '3'],
 type='schema',
 q='Comment déterminer en même temps le revenu national et le taux d’intérêt '
   'd’une économie, et cet équilibre assure-t-il le plein emploi ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Une économie fermée, à prix fixes, dont les deux marchés sont '
        'représentés par IS et LM.',
 hyp=['Les prix sont fixes : c’est la principale limite du modèle, levée '
      'ensuite par OG-DG.',
      'L’offre de monnaie est exogène.',
      'L’économie est fermée : l’ouverture sera introduite par la courbe BP.'],
 pente=[{'s': 'IS', 'd': 'décroissante : un taux élevé décourage '
         'l’investissement et abaisse le revenu d’équilibre.'},
        {'s': 'LM', 'd': 'croissante : un revenu élevé accroît la demande de '
         'monnaie et, à offre constante, élève le taux d’équilibre.'}],
 fig={'series': [
   IS, LM,
   pt('e', 'E', E[0], E[1], 'ac2'),
   rep('re', E[0], E[1], lx='Y*', ly='r*', c='ac2'),
   lin('ype', 'Plein emploi', 0.78, 0, 0.78, 0.95, 'ko', ep=2, lp=[0.78, 0.99]),
   zone('ecart', '', [(E[0], 0.04), (0.78, 0.04), (0.78, 0.1), (E[0], 0.1)], 'ko'),
   txt('tec', 'sous-emploi', 0.56, 0.17, 'ko', taille=13),
 ]},
 etapes=[
  etape('Les deux conditions d’équilibre',
        'IS réunit les couples qui équilibrent le marché des biens, LM ceux '
        'qui équilibrent le marché de la monnaie. Chacune, prise seule, '
        'laisse une infinité de possibilités.',
        on=['is', 'lm'], vif=['is', 'lm']),
  etape('L’équilibre simultané',
        'Leur intersection est le seul couple (Y*, r*) qui satisfait les deux '
        'conditions en même temps. Le taux d’intérêt et le revenu sont donc '
        'déterminés ensemble, par l’articulation de la sphère réelle et de '
        'la sphère monétaire.',
        on=['e', 're'], vif=['e', 're']),
  etape('Rien ne garantit le plein emploi',
        'On reporte le revenu de plein emploi : l’équilibre IS-LM se situe à '
        'sa gauche. L’économie est stabilisée, les deux marchés sont '
        'équilibrés, et pourtant une partie de la main-d’œuvre reste sans '
        'emploi.',
        on=['ype', 'ecart', 'tec'], vif=['ype', 'ecart', 'tec']),
  etape('Deux leviers pour s’en rapprocher',
        'Déplacer IS vers la droite par une relance budgétaire, ou déplacer '
        'LM vers la droite par une expansion monétaire : ce sont les deux '
        'façons d’amener l’équilibre vers le plein emploi, avec des effets '
        'opposés sur le taux d’intérêt.',
        add=[fl('f1', 'relance budgétaire', 0.38, 0.66, 0.56, 0.66, 'ac'),
             fl('f2', 'expansion monétaire', 0.36, 0.3, 0.54, 0.3, 'ok')],
        vif=['f1', 'f2']),
 ],
 pieges=[
  {'t': 'Un équilibre n’est pas un optimum',
   'd': 'L’intersection IS-LM dit seulement que les deux marchés sont '
        'équilibrés. Elle ne dit rien du chômage : c’est pourquoi il faut '
        'toujours reporter le revenu de plein emploi sur le graphique.'},
  {'t': 'Le modèle raisonne à prix fixes',
   'd': 'Toute conclusion sur l’inflation est hors de portée de ce '
        'graphique : il faut passer au modèle OG-DG, qui met le niveau '
        'général des prix en ordonnée.'},
  {'t': 'La formalisation n’est pas Keynes lui-même',
   'd': 'Hicks et Hansen traduisent Keynes dans un cadre d’équilibre '
        'simultané : certains keynésiens leur reprochent d’avoir transformé '
        'une théorie du déséquilibre en un modèle d’équilibre.'},
 ],
 main=[
  'Trace les axes : revenu Y en abscisse, taux d’intérêt r en ordonnée.',
  'Trace IS décroissante du haut à gauche vers le bas à droite.',
  'Trace LM croissante du bas à gauche vers le haut à droite.',
  'Marque E à l’intersection, puis descends et projette les pointillés vers '
  'Y* et r*.',
  'Place enfin la verticale du plein emploi à droite de Y* et hachure '
  'l’écart.',
 ],
 phrase='Le modèle IS-LM détermine simultanément le revenu national et le '
        'taux d’intérêt compatibles avec l’équilibre du marché des biens et '
        'du marché de la monnaie ; mais cet équilibre peut s’établir en '
        'dessous du plein emploi, ce qui justifie le recours aux politiques '
        'conjoncturelles.',
 liens=[{'c': '25', 'b': 360, 'l': 'L’intersection IS-LM : l’équilibre simultané'},
        {'c': '25', 'b': 1441, 'l': 'L’intersection IS-LM détermine un équilibre simultané'},
        {'c': '25', 'b': 1454, 'l': 'L’équilibre IS-LM ne garantit pas le plein emploi'},
        {'c': '3', 'b': 963, 'l': 'Hicks (1937) et la représentation graphique de Keynes'}],
 mots=['IS-LM', 'Hicks', 'Hansen', 'équilibre', 'plein emploi',
       'synthèse néoclassique'],
),

# --------------------------------------------- politique budgétaire + éviction
fiche(
 id='is-lm-budgetaire',
 t='Relance budgétaire et effet d’éviction',
 st='Pourquoi une relance augmente le revenu moins que ne le promettait le '
    'multiplicateur.',
 cat='macro', an=2, ch=['25'],
 type='schema',
 q='Que devient le revenu lorsque l’État relance la demande, et pourquoi le '
   'gain est-il inférieur à celui qu’annonce le multiplicateur ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Un équilibre initial E à l’intersection d’IS et de LM.',
 hyp=['L’offre de monnaie reste inchangée : la banque centrale '
      'n’accompagne pas la relance.',
      'L’économie n’est ni dans la trappe à liquidité ni dans la zone '
      'classique : LM a sa pente normale.',
      'Les prix restent fixes.'],
 pente=[{'s': 'LM', 'd': 'c’est sa pente qui fait tout : plus elle est '
         'raide, plus la hausse du revenu se traduit en hausse du taux, donc '
         'plus l’éviction est forte.'}],
 fig={'series': [
   IS, LM,
   pt('e', 'E', E[0], E[1], 'ac2'),
   rep('re', E[0], E[1], lx='Yₑ', ly='rₑ', c='ac2'),
 ]},
 etapes=[
  etape('L’équilibre de départ',
        'L’économie est au point E : revenu Yₑ, taux d’intérêt rₑ. Les deux '
        'marchés sont équilibrés.',
        on=['is', 'lm', 'e', 're'], vif=['e']),
  etape('La relance déplace IS vers la droite',
        'Une hausse des dépenses publiques, une augmentation des prestations '
        'sociales ou une baisse des impôts accroît la demande globale à '
        'chaque taux d’intérêt : toute la courbe IS se déplace vers la '
        'droite.',
        add=[lin('is1', 'IS’', *IS1, c='ac2'),
             fl('f1', '', 0.36, 0.69, 0.53, 0.69, 'ac2')],
        vif=['is1', 'f1']),
  etape('Ce que le multiplicateur promettait',
        'Si le taux d’intérêt restait à rₑ, le revenu atteindrait Y’’ : c’est '
        'le plein effet du multiplicateur, lu horizontalement sur IS’.',
        add=[pt('b', '', YSANS, E[1], 'bl'),
             rep('rb', YSANS, E[1], lx='Y’’', c='bl')],
        vif=['b', 'rb']),
  etape('Mais la demande de monnaie augmente',
        'La hausse de l’activité accroît les besoins de monnaie pour '
        'transaction. À offre de monnaie inchangée, le taux d’intérêt doit '
        'monter : l’économie remonte le long de LM.',
        add=[fl('f2', '', 0.63, 0.55, 0.6, 0.59, 'ok')],
        vif=['lm', 'f2']),
  etape('Le nouvel équilibre',
        'Il se forme en E’ : le revenu atteint Y’, inférieur à Y’’, et le '
        'taux s’établit à r’. L’écart entre Y’’ et Y’ est l’effet '
        'd’éviction : la hausse du taux a découragé une partie de '
        'l’investissement privé.',
        add=[pt('e1', 'E’', E1[0], E1[1], 'ok'),
             rep('re1', E1[0], E1[1], lx='Y’', ly='r’', c='ok'),
             zone('ev', '', [(E1[0], 0.04), (YSANS, 0.04), (YSANS, 0.1),
                             (E1[0], 0.1)], 'ko'),
             txt('tev', 'effet d’éviction', 0.58, 0.16, 'ko', taille=13)],
        vif=['e1', 're1', 'ev', 'tev']),
  etape('Comment limiter l’éviction',
        'Si la banque centrale accompagne la relance en augmentant l’offre de '
        'monnaie, LM se déplace à son tour vers la droite : le taux remonte '
        'moins, l’éviction se réduit. C’est la logique d’un policy mix '
        'accommodant. Dans la trappe à liquidité, où LM est horizontale, '
        'l’éviction disparaît.',
        add=[lin('lmA', 'LM’', *LM1, c='bl'),
             pt('e2', 'E’’', *inter({'p': IS1}, {'p': LM1}), c='bl')],
        vif=['lmA', 'e2']),
 ],
 pieges=[
  {'t': 'L’éviction n’annule pas la relance',
   'd': 'Le revenu augmente quand même : il passe de Yₑ à Y’. L’éviction dit '
        'seulement que le gain est inférieur à celui qu’aurait donné le '
        'multiplicateur à taux constant.'},
  {'t': 'Tout dépend de la pente de LM',
   'd': 'Avec une LM horizontale — trappe à liquidité — l’éviction est nulle '
        'et la relance déploie tout son effet. Avec une LM verticale — zone '
        'classique — l’éviction est totale et le revenu ne bouge pas.'},
  {'t': 'Ne pas confondre les trois critiques',
   'd': 'L’éviction porte sur le taux d’intérêt et l’investissement. Le '
        'revenu permanent porte sur la réaction de la consommation. '
        'L’équivalence ricardienne porte sur l’épargne des ménages qui '
        'anticipent l’impôt futur.'},
 ],
 main=[
  'Trace IS et LM, marque E et ses deux pointillés Yₑ et rₑ.',
  'Trace IS’ parallèle à droite d’IS, avec une flèche horizontale entre les '
  'deux.',
  'Prolonge l’horizontale de rₑ jusqu’à IS’ : tu obtiens Y’’, l’effet pur du '
  'multiplicateur.',
  'Place E’ à l’intersection d’IS’ et de LM, puis descends Y’ et projette r’.',
  'Hachure le segment entre Y’ et Y’’ et écris « effet d’éviction ».',
 ],
 phrase='Une relance budgétaire déplace IS vers la droite, mais la hausse de '
        'l’activité accroît la demande de monnaie et, à offre constante, fait '
        'monter le taux d’intérêt : l’investissement privé est partiellement '
        'évincé, de sorte que le revenu augmente moins que ne le promettait '
        'le multiplicateur — sauf si la politique monétaire accompagne la '
        'relance ou si l’économie est dans la trappe à liquidité.',
 liens=[{'c': '25', 'b': 1483, 'l': 'La politique budgétaire déplace la courbe IS'},
        {'c': '25', 'b': 1505, 'l': 'L’effet d’éviction limite l’efficacité de la relance'},
        {'c': '25', 'b': 2012, 'l': 'Effet théorique de la relance et effet effectif'},
        {'c': '25', 'b': 2018, 'l': 'Une politique monétaire accommodante peut limiter l’éviction'}],
 mots=['effet d’éviction', 'relance', 'politique budgétaire', 'multiplicateur',
       'policy mix'],
),

# -------------------------------------------------- politique monétaire
fiche(
 id='is-lm-monetaire',
 t='Politique monétaire dans IS-LM',
 st='Comment une expansion monétaire abaisse le taux d’intérêt et relance le '
    'revenu — et quand elle n’y parvient plus.',
 cat='macro', an=2, ch=['25'],
 type='schema',
 q='Par quel canal une augmentation de l’offre de monnaie agit-elle sur '
   'l’activité, et dans quelle configuration ce canal est-il bloqué ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Un équilibre initial E, dans la phase normale de la courbe LM.',
 hyp=['Les dépenses publiques et la fiscalité ne changent pas : IS reste '
      'immobile.',
      'Les prix sont fixes, donc l’offre réelle de monnaie augmente bien '
      'quand la banque centrale accroît l’offre nominale.',
      'L’investissement réagit au taux d’intérêt.'],
 pente=[{'s': 'IS', 'd': 'c’est sa pente qui commande l’efficacité : plus '
         'l’investissement est sensible au taux, plus IS est plate et plus la '
         'baisse du taux se traduit en revenu.'}],
 fig={'series': [
   IS, LM,
   pt('e', 'E', E[0], E[1], 'ac2'),
   rep('re', E[0], E[1], lx='Yₑ', ly='rₑ', c='ac2'),
 ]},
 etapes=[
  etape('L’équilibre de départ',
        'L’économie est en E, à l’intersection d’IS et de LM : le revenu vaut '
        'Yₑ et le taux d’intérêt rₑ. Les dépenses publiques et la fiscalité '
        'ne bougeront pas dans ce qui suit, donc IS restera immobile.',
        on=['is', 'lm', 'e', 're'], vif=['e']),
  etape('L’offre de monnaie augmente',
        'La banque centrale accroît la quantité de monnaie. À chaque niveau '
        'de revenu, le taux qui équilibre le marché monétaire est plus bas : '
        'la courbe LM se déplace vers la droite, c’est-à-dire vers le bas.',
        add=[lin('lm1', 'LM’', *LM1, c='bl'),
             fl('f1', '', 0.42, 0.33, 0.6, 0.33, 'bl')],
        vif=['lm1', 'f1']),
  etape('Le taux baisse et l’investissement repart',
        'Le nouvel équilibre se forme en E’ : le taux d’intérêt tombe à r’, '
        'ce qui rend des projets d’investissement rentables. La demande '
        'globale augmente, et avec elle le revenu, qui atteint Y’.',
        add=[pt('e1', 'E’', EM1[0], EM1[1], 'bl'),
             rep('re1', EM1[0], EM1[1], lx='Y’', ly='r’', c='bl')],
        vif=['e1', 're1']),
  etape('L’économie glisse le long d’IS',
        'Noter que IS n’a pas bougé : c’est l’économie qui se déplace le long '
        'de la courbe, du point E au point E’. La politique monétaire agit '
        'par le taux, pas par la demande autonome.',
        vif=['is']),
  etape('Quand le canal se bloque',
        'Dans la trappe à liquidité, LM est horizontale : la déplacer ne fait '
        'plus baisser le taux et le revenu ne bouge pas. Dans la zone '
        'classique au contraire, LM est verticale et la politique monétaire '
        'déploie tout son effet.',
        add=[txt('tt', 'dans la trappe : aucun effet sur r', 0.12, 0.1, 'ko',
                 taille=14)],
        vif=['tt']),
 ],
 pieges=[
  {'t': 'Déplacement de LM, glissement le long d’IS',
   'd': 'L’expansion monétaire déplace LM ; elle ne déplace pas IS. Le '
        'revenu augmente parce que l’économie parcourt IS vers la droite, pas '
        'parce que la demande autonome a changé.'},
  {'t': 'L’effet dépend de deux pentes',
   'd': 'Si IS est verticale — investissement insensible au taux — la baisse '
        'du taux ne relance rien. Si LM est horizontale, le taux ne baisse '
        'même pas. Les deux cas annulent la politique monétaire, pour des '
        'raisons différentes.'},
 ],
 main=[
  'Trace IS, LM et l’équilibre E avec ses pointillés.',
  'Trace LM’ parallèle à droite de LM, avec une flèche horizontale.',
  'Place E’ à l’intersection d’IS et de LM’.',
  'Descends Y’ et projette r’ : vérifie que r’ est plus bas que rₑ et Y’ plus '
  'grand que Yₑ.',
  'Écris en marge le mécanisme : offre de monnaie ↑ → r ↓ → I ↑ → Y ↑.',
 ],
 phrase='Une politique monétaire expansionniste déplace la courbe LM vers la '
        'droite : le taux d’intérêt baisse, l’investissement repart et le '
        'revenu augmente ; mais cet enchaînement suppose que le taux puisse '
        'encore baisser — dans la trappe à liquidité, le canal est bloqué.',
 liens=[{'c': '25', 'b': 1555, 'l': 'La politique monétaire déplace la courbe LM'},
        {'c': '25', 'b': 1569, 'l': 'La politique monétaire expansionniste stimule le revenu'},
        {'c': '25', 'b': 1610, 'l': 'L’efficacité selon la configuration du modèle'}],
 mots=['politique monétaire', 'LM', 'taux d’intérêt', 'trappe à liquidité'],
),
]

# ------------------------------------------------------------- policy mix
_PM = [IS, LM, pt('e', 'E', E[0], E[1], 'ac2'), rep('re', E[0], E[1], c='ac2')]
ISg = bouge(IS, -0.16, 0)
LMd = bouge(LM, 0.16, 0)
LMg = bouge(LM, -0.14, 0)

L.append(fiche(
 id='policy-mix',
 t='Le policy mix : deux combinaisons historiques',
 st='Ce que donne l’association d’une politique budgétaire et d’une politique '
    'monétaire, selon qu’elles vont dans le même sens ou non.',
 cat='macro', an=2, ch=['25'],
 type='schema',
 q='Pourquoi deux pays qui mènent chacun une politique budgétaire et une '
   'politique monétaire obtiennent-ils des résultats opposés ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Un même équilibre initial E dans les deux configurations.',
 hyp=['Les prix restent fixes.',
      'Les deux instruments sont décidés par des autorités distinctes : le '
      'budget par le gouvernement, la monnaie par la banque centrale.',
      'On raisonne en économie fermée, ce qui met de côté les effets de '
      'change.'],
 pente=[{'s': 'Le sens des déplacements', 'd': 'la politique budgétaire '
         'déplace IS, la politique monétaire déplace LM : c’est la '
         'combinaison des deux déplacements qui donne le résultat final.'}],
 fig={'series': _PM},
 variantes=[
  {'lib': 'Clinton-Greenspan : consolidation + monnaie accommodante',
   'etapes': [
     etape('L’équilibre de départ',
           'L’économie est en E. Les États-Unis cherchent à réduire un '
           'déficit budgétaire important sans provoquer de récession.',
           on=['is', 'lm', 'e', 're'], vif=['e']),
     etape('La consolidation budgétaire déplace IS vers la gauche',
           'La réduction du déficit diminue la demande globale : IS recule. '
           'Prise seule, cette politique ferait baisser le revenu.',
           add=[lin('isg', 'IS₁', *ISg, c='ac2'),
                fl('fg', 'consolidation', 0.45, 0.72, 0.3, 0.72, 'ac2')],
           vif=['isg', 'fg']),
     etape('La politique monétaire accompagne',
           'La Réserve fédérale soutient les conditions de financement : LM '
           'se déplace vers la droite, ce qui abaisse le taux d’intérêt.',
           add=[lin('lmd', 'LM₁', *LMd, c='bl'),
                fl('fd', 'monnaie accommodante', 0.38, 0.3, 0.56, 0.3, 'bl')],
           vif=['lmd', 'fd']),
     etape('Le résultat : les finances s’assainissent sans récession',
           'Le nouvel équilibre associe un taux d’intérêt nettement plus bas '
           'et un revenu proche du niveau initial : l’effet récessif de la '
           'consolidation est compensé par la baisse du coût du '
           'financement.',
           add=[pt('e1', 'E₁', *inter({'p': ISg}, {'p': LMd}), c='ok'),
                rep('r1', *inter({'p': ISg}, {'p': LMd}), c='ok')],
           vif=['e1', 'r1']),
   ]},
  {'lib': 'Réunification allemande : relance + monnaie restrictive',
   'etapes': [
     etape('L’équilibre de départ',
           'Même point de départ E. La réunification impose à l’Allemagne une '
           'forte impulsion budgétaire.',
           on=['is', 'lm', 'e', 're'], vif=['e']),
     etape('La relance budgétaire déplace IS vers la droite',
           'Les dépenses liées à la réunification soutiennent la demande : IS '
           'se déplace vers la droite.',
           add=[lin('isd', 'IS₁', *IS1, c='ac2'),
                fl('fd2', 'impulsion budgétaire', 0.38, 0.72, 0.56, 0.72, 'ac2')],
           vif=['isd', 'fd2']),
     etape('La Bundesbank resserre',
           'Craignant l’inflation, la banque centrale mène une politique '
           'monétaire restrictive : LM se déplace vers la gauche, c’est-à-dire '
           'vers le haut.',
           add=[lin('lmg', 'LM₁', *LMg, c='ko'),
                fl('fg2', 'resserrement', 0.5, 0.3, 0.34, 0.3, 'ko')],
           vif=['lmg', 'fg2']),
     etape('Le résultat : des taux d’intérêt nettement plus élevés',
           'Les deux politiques tirent en sens contraire. Le revenu progresse '
           'peu, tandis que le taux d’intérêt s’élève fortement — avec des '
           'conséquences pour tous les partenaires européens liés au mark.',
           add=[pt('e2', 'E₁', *inter({'p': IS1}, {'p': LMg}), c='ko'),
                rep('r2', *inter({'p': IS1}, {'p': LMg}), c='ko')],
           vif=['e2', 'r2']),
   ]},
 ],
 pieges=[
  {'t': 'Un policy mix n’est pas forcément cohérent',
   'd': 'Les deux instruments peuvent tirer dans le même sens ou en sens '
        'contraire. Le cours insiste : les autorités peuvent parfaitement '
        'combiner des orientations opposées, et c’est souvent le cas quand '
        'elles ne dépendent pas des mêmes institutions.'},
  {'t': 'Ne pas conclure de l’exemple à la règle',
   'd': 'Le policy mix Clinton-Greenspan illustre une possibilité ; il ne '
        'démontre pas que la seule politique monétaire explique la croissance '
        'américaine des années 1990.'},
  {'t': 'Le cas de la zone euro',
   'd': 'La politique monétaire y est unique, les politiques budgétaires '
        'restent nationales et encadrées : la combinaison est '
        'institutionnellement asymétrique, ce qui complique tout policy mix.'},
 ],
 main=[
  'Trace IS, LM et l’équilibre E : c’est le point de départ commun aux deux '
  'cas.',
  'Pour le cas américain, trace IS₁ à gauche, puis LM₁ à droite, et place le '
  'nouvel équilibre.',
  'Pour le cas allemand, repars du même E, trace IS₁ à droite, puis LM₁ à '
  'gauche.',
  'Dans chaque cas, compare la position du nouvel équilibre à l’ancien sur '
  'les deux axes : c’est la lecture qui compte.',
  'Note en marge quel instrument déplace quelle courbe.',
 ],
 phrase='Le policy mix désigne l’articulation des politiques budgétaire et '
        'monétaire : lorsqu’elles vont dans le même sens, comme aux '
        'États-Unis dans les années 1990, la consolidation budgétaire peut '
        'être menée sans récession ; lorsqu’elles s’opposent, comme en '
        'Allemagne après la réunification, le revenu progresse peu et les '
        'taux d’intérêt s’envolent.',
 liens=[{'c': '25', 'b': 1771, 'l': 'Le policy mix : combinaison des deux politiques'},
        {'c': '25', 'b': 1799, 'l': 'Le policy mix Clinton-Greenspan'},
        {'c': '25', 'b': 1852, 'l': 'La réunification allemande'},
        {'c': '25', 'b': 1896, 'l': 'Le policy mix particulier de la zone euro'}],
 mots=['policy mix', 'Clinton', 'Greenspan', 'Bundesbank', 'réunification',
       'zone euro'],
))

# ------------------------------------------------------------- OG-DG
OG = pol('og', 'OG court terme', courbe_cro(0.1, 0.18, 0.92, 0.88, 9, 0.75), 'ok')
DGl = lin('dg', 'DG', 0.08, 0.9, 0.95, 0.14, 'ac')
EOG = (0.5, 0.52)

L.append(fiche(
 id='og-dg',
 t='Le modèle OG-DG et le choc d’offre',
 st='Le seul graphique du programme qui montre en même temps la production et '
    'le niveau général des prix.',
 cat='macro', an=2, ch=['25', '2', '3'],
 type='schema',
 q='Comment représenter une situation où la production recule pendant que les '
   'prix augmentent, ce que le modèle IS-LM à prix fixes ne peut pas faire ?',
 axes={'x': 'Production (PIB réel)', 'y': 'Niveau général des prix'},
 depart='Un équilibre initial E₁ entre offre globale de court terme et '
        'demande globale.',
 hyp=['Les prix sont désormais variables : c’est ce qui distingue ce modèle '
      'd’IS-LM.',
      'L’offre globale de court terme est croissante : les entreprises '
      'produisent davantage lorsque les prix montent.',
      'La demande globale est décroissante par rapport au niveau général des '
      'prix.'],
 pente=[{'s': 'OG', 'd': 'croissante à court terme : une hausse des prix '
         'accroît la marge des producteurs et les incite à produire plus.'},
        {'s': 'DG', 'd': 'décroissante : un niveau général des prix plus '
         'élevé réduit la valeur réelle des encaisses et la demande '
         'adressée à l’économie.'}],
 fig={'series': [
   OG, DGl,
   pt('e1', 'E₁', EOG[0], EOG[1], 'ac2'),
   rep('r1', EOG[0], EOG[1], lx='Y₁', ly='P₁', c='ac2'),
 ]},
 etapes=[
  etape('Les deux courbes',
        'En abscisse la production globale, en ordonnée le niveau général des '
        'prix. L’offre globale de court terme est croissante, la demande '
        'globale décroissante.',
        on=['og', 'dg'], vif=['og', 'dg']),
  etape('L’équilibre initial',
        'Leur intersection détermine simultanément un niveau de production Y₁ '
        'et un niveau général des prix P₁.',
        on=['e1', 'r1'], vif=['e1', 'r1']),
  etape('Un choc d’offre négatif',
        'Un renchérissement brutal de l’énergie augmente les coûts de '
        'production : à chaque niveau de prix, les entreprises offrent moins. '
        'La courbe d’offre globale se déplace vers la gauche.',
        add=[pol('og1', 'OG’', [(x - 0.17, y) for x, y in
                                courbe_cro(0.1, 0.18, 0.92, 0.88, 9, 0.75)], 'ko'),
             fl('f', '', 0.52, 0.72, 0.37, 0.72, 'ko')],
        vif=['og1', 'f']),
  etape('Le nouvel équilibre : stagflation',
        'La production recule et les prix montent en même temps. C’est '
        'exactement la configuration des années 1970, que les modèles '
        'keynésiens à prix fixes ne savaient pas représenter : la '
        'stagflation.',
        add=[pt('e2', 'E₂', 0.38, 0.63, 'ko'),
             rep('r2', 0.38, 0.63, lx='Y₂', ly='P₂', c='ko'),
             txt('ts', 'production ↓ et prix ↑', 0.44, 0.24, 'ko', taille=14,
                 gras=True)],
        vif=['e2', 'r2', 'ts']),
  etape('Ce que le modèle change pour la politique économique',
        'Relancer la demande déplacerait DG vers la droite : la production se '
        'redresserait, mais les prix monteraient encore. D’où le retour des '
        'politiques d’offre, qui cherchent à déplacer OG vers la droite en '
        'agissant sur les capacités de production.',
        add=[fl('f2', 'politique d’offre', 0.3, 0.12, 0.5, 0.12, 'ok')],
        vif=['f2']),
 ],
 pieges=[
  {'t': 'OG-DG n’est pas un marché agrandi',
   'd': 'En abscisse, il y a la production totale, pas la quantité d’un bien ; '
        'en ordonnée, le niveau général des prix, pas un prix relatif. Les '
        'raisonnements microéconomiques ne s’y transposent pas directement.'},
  {'t': 'Choc d’offre et choc de demande',
   'd': 'Un choc d’offre négatif fait reculer la production et monter les '
        'prix. Un choc de demande négatif fait reculer les deux. Le sens de '
        'variation des prix permet donc d’identifier la nature du choc.'},
 ],
 main=[
  'Trace les axes : production en abscisse, niveau général des prix en '
  'ordonnée.',
  'Trace l’offre globale croissante et la demande globale décroissante, puis '
  'place E₁ et ses pointillés.',
  'Déplace l’offre globale vers la gauche pour le choc d’offre, avec une '
  'flèche horizontale.',
  'Place E₂ à la nouvelle intersection, puis projette Y₂ et P₂.',
  'Vérifie la lecture : Y₂ < Y₁ et P₂ > P₁ — c’est la stagflation.',
 ],
 phrase='Le modèle offre globale–demande globale met le niveau général des '
        'prix en ordonnée : un choc d’offre négatif y déplace l’offre globale '
        'vers la gauche et produit simultanément une baisse de la production '
        'et une hausse des prix, configuration que les modèles keynésiens à '
        'prix fixes ne pouvaient pas représenter.',
 liens=[{'c': '25', 'b': 415, 'l': 'Le modèle OG-DG : les effets des chocs'},
        {'c': '25', 'b': 428, 'l': 'Un choc d’offre négatif fait monter les prix'},
        {'c': '25', 'b': 435, 'l': 'Le retour des politiques d’offre'}],
 mots=['OG-DG', 'stagflation', 'choc d’offre', 'niveau général des prix',
       'politiques d’offre'],
))
