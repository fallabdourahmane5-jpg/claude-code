# -*- coding: utf-8 -*-
"""Courbes du chapitre 5 de deuxième année — troisième volet : l'économie
ouverte, la courbe BP, le modèle Mundell-Fleming et les dilemmes de
politique économique."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone,
                     inter, y_de, x_de, bouge)

IS = lin('is', 'IS', 0.08, 0.88, 0.95, 0.16, 'ac')
LM = lin('lm', 'LM', 0.08, 0.20, 0.95, 0.86, 'ok')
E = inter(IS, LM)
BPH = lin('bp', 'BP (mobilité parfaite)', 0.05, E[1], 0.98, E[1], 'bl', ep=3)
IS1 = bouge(IS, 0.18, 0)
LM1 = bouge(LM, 0.18, 0)

L = [

# ------------------------------------------------------------------- BP
fiche(
 id='courbe-bp',
 t='La courbe BP et sa pente',
 st='L’équilibre extérieur, et ce que la mobilité des capitaux lui fait.',
 cat='ouverte', an=2, ch=['25'],
 type='schema',
 q='À quelles conditions la balance globale d’un pays est-elle équilibrée, et '
   'pourquoi la pente de la courbe BP dépend-elle de la mobilité des '
   'capitaux ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Une économie initialement en équilibre extérieur, au point A.',
 hyp=['L’équilibre extérieur signifie que la balance globale est équilibrée : '
      'le solde courant est compensé par les mouvements autonomes de '
      'capitaux. Il ne signifie pas que les transactions courantes sont à '
      'l’équilibre.',
      'Les importations augmentent avec le revenu national.',
      'Les entrées de capitaux augmentent avec le taux d’intérêt intérieur, '
      'd’autant plus vite que les capitaux sont mobiles.'],
 pente=[{'s': 'BP', 'd': 'croissante : une hausse du revenu gonfle les '
         'importations et dégrade le solde courant ; il faut donc un taux '
         'd’intérêt plus élevé, qui attire des capitaux, pour rétablir '
         'l’équilibre global.'},
        {'s': 'Plus les capitaux sont mobiles', 'd': 'plus une faible hausse '
         'du taux suffit à attirer les capitaux nécessaires : BP devient '
         'plate, jusqu’à être horizontale en mobilité parfaite.'}],
 fig={'series': [
   lin('bp', 'BP', 0.08, 0.26, 0.95, 0.78, 'bl', ep=3),
   pt('a', 'A', 0.35, round(y_de([0.08, 0.26, 0.95, 0.78], 0.35), 4), 'ac2'),
   rep('ra', 0.35, round(y_de([0.08, 0.26, 0.95, 0.78], 0.35), 4),
       lx='Y₁', ly='r₁', c='ac2'),
 ]},
 etapes=[
  etape('Un point d’équilibre extérieur',
        'Au point A, la balance globale est équilibrée : le solde courant est '
        'exactement compensé par les mouvements autonomes de capitaux.',
        on=['bp', 'a', 'ra'], vif=['a', 'ra']),
  etape('Le revenu augmente : le solde se dégrade',
        'À taux d’intérêt inchangé, une hausse du revenu national gonfle les '
        'importations. Le solde courant se dégrade et, faute d’entrées de '
        'capitaux supplémentaires, la balance globale devient déficitaire : '
        'on passe sous la courbe, au point B.',
        add=[pt('b', 'B', 0.72, round(y_de([0.08, 0.26, 0.95, 0.78], 0.35), 4), 'ko'),
             fl('f1', 'Y ↑', 0.4, 0.2, 0.68, 0.2, 'ko'),
             txt('tb', 'sous BP : déficit', 0.62, 0.3, 'ko', taille=13)],
        vif=['b', 'f1', 'tb']),
  etape('La hausse du taux rétablit l’équilibre',
        'Pour revenir sur BP, il faut élever le taux d’intérêt : les capitaux '
        'étrangers affluent et compensent le déficit courant. On remonte au '
        'point C, sur la courbe.',
        add=[pt('c', 'C', 0.72, round(y_de([0.08, 0.26, 0.95, 0.78], 0.72), 4), 'ok'),
             fl('f2', 'r ↑', 0.75, 0.47, 0.75, 0.62, 'ok'),
             rep('rc', 0.72, round(y_de([0.08, 0.26, 0.95, 0.78], 0.72), 4),
                 lx='Y₂', ly='r₂', c='ok')],
        vif=['c', 'f2', 'rc']),
  etape('Au-dessus et en dessous de BP',
        'Tout point situé au-dessus de la courbe correspond à un excédent de '
        'la balance globale — le taux attire plus de capitaux que n’en exige '
        'le solde courant. Tout point en dessous correspond à un déficit.',
        add=[txt('th', 'au-dessus de BP : excédent', 0.17, 0.88, 'bl', taille=13)],
        vif=['th', 'tb']),
  etape('La mobilité des capitaux change la pente',
        'Avec des capitaux très mobiles, une variation minime du taux suffit : '
        'BP s’aplatit, jusqu’à devenir horizontale en mobilité parfaite. Sans '
        'mobilité, seule la variation du revenu peut rétablir l’équilibre : '
        'BP devient verticale.',
        add=[lin('bph', 'BP mobilité parfaite', 0.08, 0.48, 0.95, 0.52, 'ok', ep=2.4,
                 lp=[0.34, 0.56]),
             lin('bpv', 'BP sans mobilité', 0.55, 0.06, 0.6, 0.95, 'ko', ep=2.4)],
        vif=['bph', 'bpv']),
 ],
 pieges=[
  {'t': 'Équilibre extérieur n’est pas équilibre courant',
   'd': 'Un pays peut afficher un excédent courant et une balance globale '
        'déficitaire, si les sorties de capitaux dépassent cet excédent. La '
        'courbe BP porte sur la balance globale, pas sur le solde courant.'},
  {'t': 'La pente n’est pas une propriété du pays',
   'd': 'Elle dépend du degré de mobilité des capitaux, qui a changé avec la '
        'globalisation financière. Les trois D de Bourguinat expliquent '
        'pourquoi BP s’est horizontalisée dans les économies avancées.'},
 ],
 main=[
  'Trace les axes : revenu en abscisse, taux d’intérêt en ordonnée.',
  'Trace BP croissante et place A dessus, avec ses deux pointillés.',
  'Déplace-toi horizontalement vers la droite : tu tombes sous la courbe, en '
  'B — écris « déficit ».',
  'Remonte verticalement jusqu’à la courbe, en C — écris « r ↑ attire les '
  'capitaux ».',
  'Trace enfin, en pointillés, les deux cas extrêmes : BP horizontale et BP '
  'verticale.',
 ],
 phrase='La courbe BP réunit les couples de revenu et de taux d’intérêt pour '
        'lesquels la balance globale est équilibrée : elle est croissante '
        'parce qu’une hausse du revenu gonfle les importations et doit être '
        'compensée par des entrées de capitaux, et sa pente s’aplatit à '
        'mesure que les capitaux deviennent mobiles.',
 liens=[{'c': '25', 'b': 2378, 'l': 'La courbe BP et les conditions de l’équilibre extérieur'},
        {'c': '25', 'b': 2462, 'l': 'La courbe BP est normalement croissante'},
        {'c': '25', 'b': 2527, 'l': 'La pente de BP dépend de la mobilité des capitaux'}],
 mots=['BP', 'Mundell', 'Fleming', 'balance globale', 'mobilité des capitaux',
       'équilibre extérieur'],
),

# ------------------------------------------------------- triple équilibre
fiche(
 id='triple-equilibre',
 t='Le triple équilibre IS-LM-BP',
 st='Trois marchés à équilibrer en même temps — et ce qui se passe quand ils '
    'ne se croisent pas au même point.',
 cat='ouverte', an=2, ch=['25'],
 type='schema',
 q='Que signifie l’équilibre macroéconomique dans une économie ouverte, et '
   'que lit-on lorsque l’intersection IS-LM ne tombe pas sur BP ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Les trois courbes concourantes au même point : le triple équilibre.',
 hyp=['Les prix restent fixes.',
      'La mobilité des capitaux est imparfaite, d’où une courbe BP '
      'croissante.',
      'Le régime de change n’est pas encore précisé : c’est l’objet des '
      'fiches suivantes.'],
 pente=[{'s': 'Les trois courbes', 'd': 'IS décroissante, LM croissante, BP '
         'croissante mais de pente différente de LM : rien n’impose qu’elles '
         'se croisent au même point.'}],
 fig={'series': [
   IS, LM,
   lin('bp', 'BP', 0.08, 0.3, 0.95, 0.72, 'bl', ep=3),
   pt('e', 'E', E[0], E[1], 'ac2'),
   rep('re', E[0], E[1], lx='Y*', ly='r*', c='ac2'),
 ]},
 etapes=[
  etape('Trois conditions, trois courbes',
        'IS pour le marché des biens, LM pour le marché de la monnaie, BP '
        'pour les relations avec le reste du monde. L’équilibre complet '
        'd’une économie ouverte exige les trois à la fois.',
        on=['is', 'lm', 'bp'], vif=['is', 'lm', 'bp']),
  etape('Le triple équilibre',
        'Lorsque les trois courbes concourent au même point, un seul couple '
        '(Y*, r*) assure simultanément l’équilibre interne et l’équilibre '
        'externe. C’est un cas particulier, non la règle.',
        on=['e', 're'], vif=['e', 're']),
  etape('Quand IS-LM tombe sous BP',
        'Si l’intersection IS-LM se situe sous la courbe BP, l’économie est '
        'en équilibre intérieur mais en déficit extérieur : le solde courant '
        'n’est pas compensé par les entrées de capitaux.',
        add=[lin('bp2', 'BP₁', 0.08, 0.44, 0.95, 0.86, 'ko', ep=2.6, lp=[0.62, 0.93]),
             txt('td', 'E sous BP₁ : déficit extérieur', 0.3, 0.2, 'ko', taille=14)],
        vif=['bp2', 'td', 'e']),
  etape('Quand IS-LM passe au-dessus de BP',
        'Dans la configuration inverse, l’économie dégage un excédent de sa '
        'balance globale : les entrées de capitaux dépassent ce qu’exige le '
        'solde courant.',
        add=[lin('bp3', 'BP₂', 0.08, 0.16, 0.95, 0.58, 'jn', ep=2.6),
             txt('tx', 'E au-dessus de BP₂ : excédent', 0.3, 0.1, 'jn', taille=14)],
        off=['bp2', 'td'],
        vif=['bp3', 'tx', 'e']),
  etape('Ce qui ramène vers l’équilibre extérieur',
        'Le mécanisme de retour dépend du régime de change : en changes '
        'flexibles, c’est le taux de change qui s’ajuste ; en changes fixes, '
        'c’est la banque centrale qui intervient et modifie la quantité de '
        'monnaie.',
        vif=['bp']),
 ],
 pieges=[
  {'t': 'Le triple équilibre n’est pas automatique',
   'd': 'Rien ne garantit que les trois courbes se croisent au même point : '
        'c’est précisément de leur non-coïncidence que naissent les dilemmes '
        'de politique économique.'},
  {'t': 'Position par rapport à BP',
   'd': 'Ce n’est pas la position de E par rapport à l’origine qui compte, '
        'mais par rapport à BP : au-dessus, excédent ; en dessous, déficit. '
        'Une erreur de lecture inverse tout le raisonnement.'},
 ],
 main=[
  'Trace IS décroissante et LM croissante, puis marque leur intersection.',
  'Trace BP croissante passant par ce point : tu as le triple équilibre.',
  'Trace ensuite une deuxième BP plus haute : l’intersection IS-LM se '
  'retrouve en dessous — écris « déficit extérieur ».',
  'Trace une troisième BP plus basse : l’intersection passe au-dessus — écris '
  '« excédent ».',
  'Note en marge le mécanisme de retour propre à chaque régime de change.',
 ],
 phrase='En économie ouverte, l’équilibre macroéconomique exige la '
        'compatibilité de trois marchés — biens, monnaie et relations avec le '
        'reste du monde — et rien ne garantit que les trois courbes se '
        'croisent au même point : un équilibre intérieur peut parfaitement '
        'coexister avec un déséquilibre extérieur.',
 liens=[{'c': '25', 'b': 2637, 'l': 'L’équilibre en économie ouverte est un triple équilibre'},
        {'c': '25', 'b': 2655, 'l': 'Un équilibre interne peut coexister avec un déséquilibre extérieur'}],
 mots=['IS-LM-BP', 'Mundell-Fleming', 'triple équilibre', 'équilibre externe'],
),
]

# ------------------------------------- Mundell-Fleming : politique monétaire
_base = [IS, BPH, LM, pt('e', 'E', E[0], E[1], 'ac2'),
         rep('re', E[0], E[1], lx='Y*', ly='r*', c='ac2')]

L.append(fiche(
 id='mundell-monetaire',
 t='Politique monétaire en économie ouverte',
 st='Le même choc initial, deux résultats opposés selon le régime de change.',
 cat='ouverte', an=2, ch=['25', '26'],
 type='schema',
 q='Une banque centrale qui augmente l’offre de monnaie relance-t-elle '
   'l’activité ? La réponse dépend entièrement du régime de change.',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Un triple équilibre en E, avec une mobilité parfaite des capitaux : '
        'la courbe BP est horizontale au niveau du taux d’intérêt mondial.',
 hyp=['Mobilité parfaite des capitaux : le taux intérieur ne peut pas '
      's’écarter durablement du taux mondial, d’où une courbe BP '
      'horizontale.',
      'Les prix restent fixes.',
      'Le choc de départ est le même dans les deux configurations : une '
      'expansion monétaire qui déplace LM vers la droite.'],
 pente=[{'s': 'BP horizontale', 'd': 'en mobilité parfaite, le moindre écart '
         'de taux provoque des mouvements de capitaux massifs : le taux '
         'intérieur est arrimé au taux mondial.'}],
 fig={'series': _base},
 variantes=[
  {'lib': 'Changes fixes',
   'etapes': [
     etape('Le point de départ',
           'Triple équilibre en E. La banque centrale s’engage à maintenir la '
           'parité de la monnaie, et les capitaux circulent librement.',
           on=['is', 'lm', 'bp', 'e', 're'], vif=['e']),
     etape('L’expansion monétaire déplace LM vers la droite',
           'La banque centrale augmente l’offre de monnaie : LM se déplace '
           'vers la droite et le taux d’intérêt intérieur tombe sous le taux '
           'mondial.',
           add=[lin('lm1', 'LM₁', *LM1, c='jn'),
                fl('f1', '', 0.42, 0.3, 0.6, 0.3, 'jn'),
                pt('x', '', *inter(IS, {'p': LM1}), c='jn')],
           vif=['lm1', 'f1', 'x']),
     etape('Les capitaux sortent',
           'Un taux intérieur inférieur au taux mondial provoque des sorties '
           'massives de capitaux et une pression à la dépréciation de la '
           'monnaie.',
           add=[fl('f2', 'sorties de capitaux', 0.55, 0.38, 0.8, 0.44, 'ko')],
           vif=['f2']),
     etape('La défense de la parité annule l’expansion',
           'Pour tenir la parité, la banque centrale doit racheter sa propre '
           'monnaie contre ses réserves de change. Cette intervention '
           'contracte la liquidité intérieure : LM revient exactement à sa '
           'position de départ.',
           add=[fl('f3', 'retour de LM', 0.62, 0.22, 0.44, 0.22, 'ok')],
           off=['lm1', 'x', 'f1'],
           vif=['lm', 'f3']),
     etape('Conclusion : la politique monétaire est inefficace',
           'Le revenu revient à Y*, le taux au taux mondial. En changes fixes '
           'avec mobilité parfaite des capitaux, la politique monétaire perd '
           'toute autonomie : c’est l’un des sommets du triangle de Mundell '
           'qu’il faut abandonner.',
           vif=['e', 're']),
   ]},
  {'lib': 'Changes flexibles',
   'etapes': [
     etape('Le point de départ',
           'Même triple équilibre en E, même mobilité parfaite des capitaux, '
           'mais la banque centrale ne défend aucune parité : le taux de '
           'change flotte.',
           on=['is', 'lm', 'bp', 'e', 're'], vif=['e']),
     etape('L’expansion monétaire déplace LM vers la droite',
           'Exactement le même choc qu’en changes fixes : l’offre de monnaie '
           'augmente, LM se déplace vers la droite, le taux intérieur passe '
           'sous le taux mondial.',
           add=[lin('lm1', 'LM₁', *LM1, c='jn'),
                fl('f1', '', 0.42, 0.3, 0.6, 0.3, 'jn'),
                pt('x', '', *inter(IS, {'p': LM1}), c='jn')],
           vif=['lm1', 'f1', 'x']),
     etape('La monnaie se déprécie',
           'Les sorties de capitaux font baisser la valeur externe de la '
           'monnaie. Comme aucune parité n’est défendue, la dépréciation se '
           'produit librement.',
           add=[fl('f2', 'dépréciation', 0.55, 0.38, 0.8, 0.44, 'ac2')],
           vif=['f2']),
     etape('La dépréciation déplace IS vers la droite',
           'Les produits nationaux deviennent moins chers pour l’étranger : '
           'les exportations nettes augmentent, ce qui déplace IS vers la '
           'droite. L’ajustement du change amplifie l’effet initial.',
           add=[lin('is1', 'IS₁', *IS1, c='ac2'),
                fl('f3', '', 0.38, 0.7, 0.56, 0.7, 'ac2')],
           vif=['is1', 'f3']),
     etape('Conclusion : la politique monétaire est très efficace',
           'Le nouvel équilibre associe le même taux d’intérêt — arrimé au '
           'taux mondial — et un revenu nettement plus élevé. Le canal du '
           'change s’ajoute au canal du taux d’intérêt.',
           add=[pt('e1', 'E₁', *inter({'p': IS1}, {'p': LM1}), c='ok'),
                rep('r1', *inter({'p': IS1}, {'p': LM1}), lx='Y₁', c='ok')],
           vif=['e1', 'r1']),
   ]},
 ],
 pieges=[
  {'t': 'Le choc est le même, le résultat est opposé',
   'd': 'Dans les deux cas LM se déplace vers la droite. Ce qui change, c’est '
        'ce qui suit : la défense de la parité annule le déplacement en '
        'changes fixes, tandis que la dépréciation l’amplifie en changes '
        'flexibles.'},
  {'t': 'Mobilité parfaite n’est pas une description du réel',
   'd': 'C’est une hypothèse simplificatrice, retenue pour représenter '
        'l’intégration financière européenne. Avec une mobilité imparfaite, '
        'les conclusions sont atténuées, non inversées.'},
  {'t': 'Ce n’est pas la monnaie qui agit directement sur les exportations',
   'd': 'En changes flexibles, l’enchaînement passe par le taux d’intérêt, '
        'puis les capitaux, puis le change, puis les exportations nettes. '
        'Sauter des maillons conduit à des contresens.'},
 ],
 main=[
  'Trace IS décroissante, LM croissante et BP horizontale passant par leur '
  'intersection : c’est le triple équilibre.',
  'Déplace LM vers la droite : c’est l’expansion monétaire, commune aux deux '
  'cas.',
  'En changes fixes, trace la flèche de retour de LM vers sa position '
  'initiale et conclus que rien n’a changé.',
  'En changes flexibles, laisse LM déplacée et déplace en plus IS vers la '
  'droite, puis place le nouvel équilibre.',
  'Dans les deux cas, vérifie que le taux d’intérêt final est revenu au '
  'niveau de BP.',
 ],
 phrase='En mobilité parfaite des capitaux, une expansion monétaire déplace '
        'LM vers la droite dans les deux régimes, mais en changes fixes la '
        'défense de la parité oblige la banque centrale à reprendre la '
        'liquidité créée, ce qui annule l’effet, tandis qu’en changes '
        'flexibles la dépréciation stimule les exportations nettes et '
        'amplifie la relance.',
 liens=[{'c': '25', 'b': 3116, 'l': 'Changes fixes : la politique monétaire est inefficace'},
        {'c': '25', 'b': 3331, 'l': 'Changes flexibles : la politique monétaire devient très efficace'},
        {'c': '25', 'b': 3221, 'l': 'Le triangle des incompatibilités de Mundell'}],
 mots=['Mundell-Fleming', 'changes fixes', 'changes flexibles',
       'mobilité des capitaux', 'politique monétaire'],
))

# ------------------------------------ Mundell-Fleming : politique budgétaire
L.append(fiche(
 id='mundell-budgetaire',
 t='Politique budgétaire en économie ouverte',
 st='La relance est amplifiée en changes fixes, neutralisée en changes '
    'flexibles : l’exact inverse de la politique monétaire.',
 cat='ouverte', an=2, ch=['25', '26'],
 type='schema',
 q='Une relance budgétaire produit-elle les mêmes effets selon le régime de '
   'change, lorsque les capitaux circulent librement ?',
 axes={'x': 'Revenu national Y', 'y': 'Taux d’intérêt r'},
 depart='Le même triple équilibre en E, avec BP horizontale au taux mondial.',
 hyp=['Mobilité parfaite des capitaux.',
      'Prix fixes.',
      'Le choc initial est identique dans les deux cas : une hausse des '
      'dépenses publiques qui déplace IS vers la droite.'],
 pente=[{'s': 'BP horizontale', 'd': 'elle fixe le taux d’intérêt intérieur '
         'au niveau mondial : tout écart déclenche des mouvements de capitaux '
         'qui le ramènent.'}],
 fig={'series': _base},
 variantes=[
  {'lib': 'Changes fixes',
   'etapes': [
     etape('Le point de départ',
           'Triple équilibre en E. La banque centrale défend une parité et '
           'les capitaux circulent librement.',
           on=['is', 'lm', 'bp', 'e', 're'], vif=['e']),
     etape('La relance déplace IS vers la droite',
           'La hausse des dépenses publiques accroît la demande globale : IS '
           'se déplace vers la droite et le taux d’intérêt intérieur dépasse '
           'le taux mondial.',
           add=[lin('is1', 'IS₁', *IS1, c='ac2'),
                fl('f1', '', 0.38, 0.72, 0.56, 0.72, 'ac2'),
                pt('x', '', *inter({'p': IS1}, LM), c='ac2')],
           vif=['is1', 'f1', 'x']),
     etape('Les capitaux entrent',
           'Un taux intérieur supérieur au taux mondial attire des capitaux '
           'internationaux et crée une pression à l’appréciation de la '
           'monnaie.',
           add=[fl('f2', 'entrées de capitaux', 0.78, 0.68, 0.6, 0.62, 'bl')],
           vif=['f2']),
     etape('La défense de la parité crée de la monnaie',
           'Pour empêcher l’appréciation, la banque centrale vend sa monnaie '
           'contre des devises : la liquidité intérieure augmente et LM se '
           'déplace vers la droite. La politique budgétaire est accompagnée '
           'par la politique monétaire.',
           add=[lin('lm1', 'LM₁', *LM1, c='ok'),
                fl('f3', '', 0.42, 0.3, 0.6, 0.3, 'ok')],
           vif=['lm1', 'f3']),
     etape('Conclusion : la relance est amplifiée',
           'Le revenu progresse fortement, le taux revient au niveau mondial. '
           'En changes fixes avec mobilité parfaite, la politique budgétaire '
           'bénéficie d’un puissant effet d’accompagnement monétaire.',
           add=[pt('e1', 'E₁', *inter({'p': IS1}, {'p': LM1}), c='ok'),
                rep('r1', *inter({'p': IS1}, {'p': LM1}), lx='Y₁', c='ok')],
           vif=['e1', 'r1']),
   ]},
  {'lib': 'Changes flexibles',
   'etapes': [
     etape('Le point de départ',
           'Même triple équilibre en E, mêmes capitaux parfaitement mobiles, '
           'mais le change flotte librement.',
           on=['is', 'lm', 'bp', 'e', 're'], vif=['e']),
     etape('La relance déplace IS vers la droite',
           'Choc identique au cas précédent : la demande globale augmente, IS '
           'se déplace vers la droite et le taux intérieur dépasse le taux '
           'mondial.',
           add=[lin('is1', 'IS₁', *IS1, c='ac2'),
                fl('f1', '', 0.38, 0.72, 0.56, 0.72, 'ac2'),
                pt('x', '', *inter({'p': IS1}, LM), c='ac2')],
           vif=['is1', 'f1', 'x']),
     etape('La monnaie s’apprécie',
           'Les entrées de capitaux font monter la valeur externe de la '
           'monnaie. Rien ne s’y oppose, puisque aucune parité n’est '
           'défendue.',
           add=[fl('f2', 'appréciation', 0.78, 0.68, 0.6, 0.62, 'ko')],
           vif=['f2']),
     etape('L’appréciation ramène IS vers la gauche',
           'Les produits nationaux deviennent plus chers pour l’étranger : '
           'les exportations nettes reculent, ce qui annule le déplacement '
           'initial d’IS.',
           add=[fl('f3', 'retour d’IS', 0.58, 0.58, 0.4, 0.58, 'ko')],
           off=['is1', 'x', 'f1'],
           vif=['is', 'f3']),
     etape('Conclusion : la relance est neutralisée',
           'Le revenu revient à Y*. En changes flexibles avec mobilité '
           'parfaite, la politique budgétaire perd son efficacité '
           'macroéconomique : elle est absorbée par l’appréciation de la '
           'monnaie.',
           vif=['e', 're']),
   ]},
 ],
 pieges=[
  {'t': 'Le tableau de synthèse se retient par la symétrie',
   'd': 'Politique monétaire : inefficace en changes fixes, très efficace en '
        'changes flexibles. Politique budgétaire : l’inverse exactement. '
        'C’est la même logique de mouvements de capitaux, lue dans les deux '
        'sens.'},
  {'t': 'L’appréciation n’est pas une sanction',
   'd': 'Elle est la conséquence mécanique des entrées de capitaux attirées '
        'par le taux plus élevé. Elle traduit le succès apparent de la '
        'relance, qui finit par la neutraliser.'},
 ],
 main=[
  'Trace le triple équilibre : IS, LM et BP horizontale.',
  'Déplace IS vers la droite : c’est la relance, commune aux deux cas.',
  'En changes fixes, ajoute le déplacement de LM vers la droite et place le '
  'nouvel équilibre très à droite.',
  'En changes flexibles, ramène IS à sa position initiale par une flèche et '
  'conclus que le revenu ne bouge pas.',
  'Dans les deux cas, vérifie que le taux final est revenu sur BP.',
 ],
 phrase='En mobilité parfaite des capitaux, une relance budgétaire élève le '
        'taux d’intérêt au-dessus du taux mondial et attire des capitaux : en '
        'changes fixes, la défense de la parité crée la monnaie qui amplifie '
        'la relance, tandis qu’en changes flexibles l’appréciation réduit les '
        'exportations nettes et neutralise l’effet initial.',
 liens=[{'c': '25', 'b': 3162, 'l': 'Changes fixes : la relance budgétaire est accompagnée'},
        {'c': '25', 'b': 3399, 'l': 'Changes flexibles : la politique budgétaire devient inefficace'},
        {'c': '25', 'b': 3495, 'l': 'Le tableau de synthèse des quatre configurations'}],
 mots=['Mundell-Fleming', 'relance budgétaire', 'changes fixes',
       'changes flexibles', 'appréciation'],
))

# --------------------------------------------- équilibre interne / externe
L.append(fiche(
 id='dilemmes-mundell',
 t='Les quatre situations et la règle de Mundell',
 st='Croiser l’équilibre interne et l’équilibre externe pour voir où naissent '
    'les dilemmes.',
 cat='ouverte', an=2, ch=['25'],
 type='schema',
 q='Dans quelles situations la correction d’un déséquilibre aggrave-t-elle '
   'l’autre, et comment affecter les instruments pour s’en sortir ?',
 axes={'x': 'Situation interne', 'y': 'Situation externe'},
 depart='Un plan partagé en quatre cases par deux axes : le revenu par '
        'rapport au plein emploi, le solde extérieur par rapport à '
        'l’équilibre.',
 hyp=['Deux objectifs : l’équilibre interne — plein emploi sans inflation '
      'excessive — et l’équilibre externe.',
      'Deux instruments : la politique budgétaire et la politique monétaire.',
      'La règle d’affectation suppose que chaque instrument soit affecté à '
      'l’objectif pour lequel il est relativement le plus efficace.'],
 pente=[{'s': 'Les deux axes', 'd': 'ils ne portent pas des quantités mais '
         'des positions : à gauche le sous-emploi, à droite l’inflation ; en '
         'bas le déficit extérieur, en haut l’excédent.'}],
 fig={'series': [
   lin('vx', '', 0.5, 0.02, 0.5, 0.98, 'gr', ep=2),
   lin('hy', '', 0.02, 0.5, 0.98, 0.5, 'gr', ep=2),
   txt('ax1', 'sous-emploi', 0.16, 0.03, 'gr', taille=14),
   txt('ax2', 'inflation', 0.72, 0.03, 'gr', taille=14),
   txt('ay1', 'déficit', 0.0, 0.25, 'gr', taille=14),
   txt('ay2', 'excédent', 0.0, 0.75, 'gr', taille=14),
   zone('c1', '', [(0.03, 0.53), (0.47, 0.53), (0.47, 0.96), (0.03, 0.96)], 'ok'),
   zone('c2', '', [(0.03, 0.04), (0.47, 0.04), (0.47, 0.47), (0.03, 0.47)], 'ko'),
   zone('c3', '', [(0.53, 0.04), (0.96, 0.04), (0.96, 0.47), (0.53, 0.47)], 'ok'),
   zone('c4', '', [(0.53, 0.53), (0.96, 0.53), (0.96, 0.96), (0.53, 0.96)], 'ko'),
   txt('t1', 'sous-emploi + excédent', 0.14, 0.84, 'ok', taille=14, gras=True),
   txt('t1b', 'relancer améliore les deux', 0.14, 0.76, 'ok', taille=13),
   txt('t2', 'sous-emploi + déficit', 0.06, 0.34, 'ko', taille=14, gras=True),
   txt('t2b', 'DILEMME', 0.06, 0.26, 'ko', taille=15, gras=True),
   txt('t3', 'inflation + déficit', 0.56, 0.34, 'ok', taille=14, gras=True),
   txt('t3b', 'la rigueur améliore les deux', 0.56, 0.26, 'ok', taille=13),
   txt('t4', 'inflation + excédent', 0.56, 0.84, 'ko', taille=14, gras=True),
   txt('t4b', 'DILEMME', 0.56, 0.76, 'ko', taille=15, gras=True),
 ]},
 etapes=[
  etape('Les deux axes',
        'À gauche de la verticale, le revenu est inférieur au plein emploi ; '
        'à droite, la demande excède les capacités. En dessous de '
        'l’horizontale, la balance est déficitaire ; au-dessus, '
        'excédentaire.',
        on=['vx', 'hy', 'ax1', 'ax2', 'ay1', 'ay2'],
        vif=['vx', 'hy']),
  etape('Les deux situations sans dilemme',
        'Sous-emploi avec excédent extérieur : une relance rapproche du plein '
        'emploi et réduit l’excédent en gonflant les importations. Inflation '
        'avec déficit : la rigueur calme les prix et réduit les importations. '
        'Une seule orientation suffit.',
        on=['c1', 'c3', 't1', 't1b', 't3', 't3b'],
        vif=['c1', 'c3', 't1b', 't3b']),
  etape('Premier dilemme : sous-emploi et déficit',
        'La relance nécessaire à l’emploi creuse encore le déficit extérieur. '
        'C’est la contrainte extérieure : la France de 1981-1983 en offre '
        'l’exemple, jusqu’au tournant de la rigueur.',
        on=['c2', 't2', 't2b'], vif=['c2', 't2', 't2b']),
  etape('Second dilemme : inflation et excédent',
        'La rigueur nécessaire à la stabilité des prix freine la demande '
        'intérieure et renforce encore l’excédent extérieur. La situation est '
        'symétrique de la précédente.',
        on=['c4', 't4', 't4b'], vif=['c4', 't4', 't4b']),
  etape('La règle d’affectation de Mundell',
        'Puisqu’il y a deux objectifs et deux instruments, il faut affecter '
        'chaque instrument à l’objectif pour lequel il est relativement le '
        'plus efficace : la politique budgétaire à l’équilibre interne, la '
        'politique monétaire à l’équilibre externe par le jeu des taux '
        'd’intérêt et des capitaux.',
        add=[txt('tm', 'budget → interne  ·  monnaie → externe', 0.14, 0.52,
                 'ac', taille=15, gras=True)],
        vif=['tm']),
 ],
 pieges=[
  {'t': 'Un dilemme n’est pas une impasse',
   'd': 'Il signifie seulement qu’un seul instrument ne suffit plus : il faut '
        'soit un second instrument, soit accepter un arbitrage entre les deux '
        'objectifs.'},
  {'t': 'La règle de Mundell se heurte aux institutions',
   'd': 'Dans la zone euro, la politique monétaire est commune et les '
        'politiques budgétaires nationales : l’affectation des instruments '
        'prévue par la règle n’est pas applicable telle quelle.'},
 ],
 main=[
  'Trace une croix : une verticale et une horizontale qui partagent la page '
  'en quatre cases.',
  'Annote les axes : sous-emploi / inflation en abscisse, déficit / excédent '
  'en ordonnée.',
  'Remplis les deux cases sans dilemme — sous-emploi + excédent, inflation + '
  'déficit — et écris l’orientation qui convient.',
  'Hachure les deux cases en dilemme et écris pourquoi les objectifs '
  's’opposent.',
  'Écris sous la croix la règle d’affectation : budget à l’interne, monnaie à '
  'l’externe.',
 ],
 phrase='Le croisement de la situation interne et de la situation externe fait '
        'apparaître quatre configurations, dont deux où la correction d’un '
        'déséquilibre aggrave l’autre : la règle d’affectation de Mundell '
        'propose alors d’affecter la politique budgétaire à l’équilibre '
        'interne et la politique monétaire à l’équilibre externe.',
 liens=[{'c': '25', 'b': 2775, 'l': 'Les quatre situations possibles'},
        {'c': '25', 'b': 2897, 'l': 'La contrainte extérieure'},
        {'c': '25', 'b': 3706, 'l': 'La règle de Mundell et l’affectation des instruments'}],
 mots=['dilemme', 'contrainte extérieure', 'règle de Mundell', 'tournant de la rigueur'],
))
