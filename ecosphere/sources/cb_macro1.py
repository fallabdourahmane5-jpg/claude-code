# -*- coding: utf-8 -*-
"""Courbes du chapitre 5 de deuxième année — premier volet : l'équilibre
keynésien en économie fermée, le marché du travail et le marché de la
monnaie. Chaque fiche est construite à partir du passage du cours indiqué
dans ses renvois."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone,
                     inter, y_de, bouge, courbe_dec, courbe_cro, en_u)

# ------------------------------------------------- repères du diagramme 45°
BIS = lin('bis', '45°', 0, 0, 0.95, 0.95, 'gr', ep=2, lp=[0.88, 0.93])
CONS = lin('c', 'C = C₀ + cY', 0, 0.14, 0.95, 0.6625, 'bl')
DG = lin('dg', 'DG = C + I', 0, 0.25, 0.95, 0.7725, 'ac')
E0 = inter(DG, BIS)                      # (0.5556, 0.5556)
DG1 = bouge(DG, 0, 0.074)
E1 = inter({'p': DG1}, BIS)              # plein emploi
DG2 = bouge(DG, 0, 0.16)
E2 = inter({'p': DG2}, BIS)

L = [

fiche(
 id='keynes-45',
 t='Le diagramme à 45° de Samuelson',
 st='Comment la demande globale détermine le revenu national, et pourquoi '
    'l’équilibre peut s’établir en dessous du plein emploi.',
 cat='macro', an=2, ch=['25', '3'],
 type='schema',
 q='À quel niveau de production une économie se stabilise-t-elle lorsque ce '
   'sont les dépenses anticipées, et non les capacités de production, qui '
   'commandent l’activité ?',
 axes={'x': 'Revenu national Y', 'y': 'Demande globale'},
 depart='Une économie fermée sans État, où l’investissement est provisoirement '
        'considéré comme autonome.',
 hyp=['Les prix et les salaires sont fixes : l’ajustement se fait par les '
      'quantités produites, non par les prix.',
      'La consommation dépend du revenu courant : C = C₀ + cY, avec une '
      'propension marginale à consommer c comprise entre 0 et 1.',
      'L’investissement est autonome, c’est-à-dire indépendant du revenu '
      'courant dans cette représentation.'],
 pente=[{'s': 'La bissectrice', 'd': 'elle a une pente de 1 : en chacun de ses '
         'points, la demande globale est exactement égale au revenu. C’est '
         'donc le lieu de tous les équilibres possibles.'},
        {'s': 'La fonction de consommation', 'd': 'sa pente est la propension '
         'marginale à consommer, inférieure à 1 : quand le revenu augmente de '
         '100, la consommation augmente de moins de 100. C’est la loi '
         'psychologique fondamentale.'},
        {'s': 'La demande globale', 'd': 'elle est parallèle à la '
         'consommation, située au-dessus d’un montant égal à '
         'l’investissement autonome.'}],
 fig={'series': [
   BIS, CONS, DG,
   lin('ype', 'Plein emploi', 0.72, 0, 0.72, 0.95, 'ko', ep=2, lp=[0.72, 0.99]),
   pt('e0', 'E', E0[0], E0[1], 'ac2'),
   rep('r0', E0[0], E0[1], lx='Y*', ly='', c='ac2'),
   txt('i', 'I₀ = écart entre C et DG', 0.12, 0.237, 'ac', taille=13),
 ]},
 etapes=[
  etape('Le repère et la bissectrice',
        'En abscisse le revenu national, en ordonnée la demande globale. La '
        'bissectrice à 45° réunit tous les points où la demande égale '
        'exactement le revenu : c’est sur elle, et seulement sur elle, que '
        'l’économie peut être à l’équilibre.',
        on=['bis'], vif=['bis']),
  etape('La fonction de consommation',
        'On trace C = C₀ + cY. Elle coupe l’axe vertical en C₀, la '
        'consommation autonome, et monte moins vite que la bissectrice '
        'puisque la propension marginale à consommer est inférieure à 1.',
        on=['c'], vif=['c']),
  etape('La demande globale',
        'On ajoute l’investissement autonome : la droite de demande globale '
        'est parallèle à la consommation, décalée vers le haut d’un montant '
        'égal à I₀. C’est elle qui commande la production.',
        on=['dg', 'i'], vif=['dg', 'i']),
  etape('L’équilibre',
        'L’économie se stabilise là où la demande globale coupe la '
        'bissectrice : au point E, la production est exactement égale aux '
        'dépenses anticipées. Rien ne pousse les entreprises à produire '
        'davantage ni moins.',
        on=['e0', 'r0'], vif=['e0', 'r0']),
  etape('Un équilibre de sous-emploi',
        'On reporte le revenu de plein emploi. L’équilibre E se situe à sa '
        'gauche : l’économie est bien à l’équilibre, mais à un niveau '
        'd’activité qui ne permet pas d’employer toute la population active. '
        'C’est l’apport décisif de Keynes.',
        on=['ype'], vif=['ype', 'e0']),
  etape('La relance déplace la demande globale',
        'Une hausse des dépenses publiques ou de l’investissement déplace la '
        'droite de demande globale vers le haut, parallèlement à elle-même. '
        'Le nouvel équilibre se forme plus à droite : le revenu atteint le '
        'plein emploi.',
        add=[lin('dg1', 'DG’', *DG1, c='ok'),
             pt('e1', 'E’', E1[0], E1[1], 'ok'),
             rep('r1', E1[0], E1[1], lx='Yₚₑ', c='ok'),
             fl('f1', 'déplacement de DG', 0.3, 0.43, 0.3, 0.505, 'ok')],
        vif=['dg1', 'e1', 'f1']),
  etape('Si la relance va trop loin : l’écart inflationniste',
        'Poussée au-delà du plein emploi, la demande globale coupe la '
        'bissectrice à droite de Yₚₑ. L’économie ne peut plus produire '
        'davantage : la main-d’œuvre devient rare, les salaires et les prix '
        'montent. L’excès de demande se transforme en inflation.',
        add=[lin('dg2', 'DG’’', *DG2, c='jn'),
             pt('e2', 'E’’', E2[0], E2[1], 'ko'),
             zone('ecart', '', [(0.72, 0.72), (E2[0], E2[1]), (E2[0], 0.72)], 'ko'),
             txt('tec', 'écart inflationniste', 0.76, 0.66, 'ko', taille=13)],
        vif=['dg2', 'e2', 'ecart', 'tec']),
 ],
 pieges=[
  {'t': 'Équilibre ne veut pas dire plein emploi',
   'd': 'Sur ce graphique, l’équilibre est le point où DG croise la '
        'bissectrice, pas le point de plein emploi. Les deux ne coïncident '
        'que par hasard : c’est toute la rupture avec l’analyse classique.'},
  {'t': 'Déplacement sur la courbe ou de la courbe',
   'd': 'Une variation du revenu fait glisser l’économie le long de DG. Une '
        'variation de l’investissement, des dépenses publiques ou de la '
        'consommation autonome déplace la droite DG tout entière, vers le '
        'haut ou vers le bas.'},
  {'t': 'Le modèle suppose des prix fixes',
   'd': 'L’écart inflationniste se lit comme un excès de demande sur l’axe '
        'horizontal : le diagramme ne représente pas directement l’inflation, '
        'il signale seulement que la demande dépasse les capacités. C’est le '
        'modèle OG-DG qui fait apparaître les prix.'},
 ],
 main=[
  'Trace les deux axes : le revenu national Y en abscisse, la demande globale '
  'en ordonnée, avec la même échelle sur les deux — c’est indispensable pour '
  'que la bissectrice ait bien 45°.',
  'Trace la bissectrice en partant de l’origine, et écris « 45° » à côté.',
  'Place C₀ sur l’axe vertical, puis trace la fonction de consommation, moins '
  'inclinée que la bissectrice.',
  'Trace DG parallèle à C, au-dessus, et marque la distance verticale entre '
  'les deux : c’est I₀.',
  'Marque le point E à l’intersection de DG et de la bissectrice, puis '
  'descends un pointillé vers l’axe des abscisses : c’est Y*.',
  'Place Yₚₑ à droite de Y* et hachure l’écart : tu as ton équilibre de '
  'sous-emploi.',
  'Pour la relance, trace DG’ parallèle au-dessus de DG et place E’ sur la '
  'bissectrice ; ajoute une flèche verticale entre DG et DG’.',
 ],
 phrase='Le diagramme à 45° montre que l’économie se stabilise là où la '
        'demande globale anticipée égale le revenu : l’équilibre peut donc '
        's’établir durablement en dessous du plein emploi, ce qui légitime '
        'une intervention publique destinée à déplacer la demande globale '
        'vers le haut.',
 liens=[{'c': '25', 'b': 464, 'l': 'Samuelson (1949) : le diagramme à 45°'},
        {'c': '25', 'b': 533, 'l': 'Keynes montre qu’un équilibre de sous-emploi peut exister'},
        {'c': '25', 'b': 602, 'l': 'Le second dysfonctionnement : l’écart inflationniste'},
        {'c': '3', 'b': 800, 'l': 'L’équilibre keynésien par la demande effective'}],
 mots=['Samuelson', 'demande effective', 'sous-emploi', 'écart inflationniste',
       'propension à consommer', 'bissectrice'],
),
]

# ------------------------------------------------ le multiplicateur en vagues
_vagues = [100, 80, 64, 51.2, 41.0, 32.8, 26.2, 21.0]
_bar = []
_cum = []
_tot = 0.0
for _i, _v in enumerate(_vagues):
    _x = 0.07 + _i * 0.112
    _h = _v / 100.0 * 0.78
    _bar.append(zone('b%d' % _i, '', [(_x, 0), (_x, _h), (_x + 0.072, _h),
                                      (_x + 0.072, 0)], 'ac'))
    _tot += _v
    _cum.append((_x + 0.036, _tot / 500.0 * 0.86))

L.append(fiche(
 id='multiplicateur-vagues',
 t='Le multiplicateur : les vagues de dépense',
 st='Pourquoi une dépense de 100 engendre finalement 500 de revenu, et '
    'pourquoi la série s’arrête.',
 cat='macro', an=2, ch=['25', '1'],
 type='schema',
 q='Pourquoi une dépense publique initiale produit-elle une augmentation du '
   'revenu national plus que proportionnelle, et qu’est-ce qui en borne '
   'l’ampleur ?',
 axes={'x': 'Vagues successives de dépense', 'y': 'Montant dépensé'},
 depart='Une dépense initiale de 100, avec une propension marginale à '
        'consommer de 0,8.',
 hyp=['La propension marginale à consommer est constante et vaut 0,8 : chaque '
      'bénéficiaire d’un revenu supplémentaire en dépense 80 %.',
      'L’économie est fermée et sans État dans la version simple : la seule '
      'fuite est l’épargne.',
      'Les capacités de production permettent de répondre à la demande '
      'supplémentaire, conformément à l’hypothèse de prix fixes.'],
 pente=[{'s': 'La hauteur des barres', 'd': 'chaque vague vaut 0,8 fois la '
         'précédente : la série est géométrique de raison c, ce qui la fait '
         'décroître et converger.'},
        {'s': 'La courbe cumulée', 'd': 'elle s’aplatit progressivement : la '
         'somme tend vers 1/(1 − c) fois la dépense initiale, soit 5 fois 100.'}],
 fig={'series': _bar + [
   pol('cum', 'Revenu cumulé', _cum, 'ok'),
   txt('t100', '100', 0.085, 0.82, 'ac', taille=14),
   txt('t80', '80', 0.2, 0.655, 'ac', taille=13),
   txt('t64', '64', 0.31, 0.53, 'ac', taille=13),
   txt('tfin', '→ 500 au total', 0.63, 0.93, 'ok', taille=15, gras=True),
   txt('tep', 'ce qui manque à chaque barre part en épargne', 0.3, 0.17,
       'ac2', taille=13),
 ]},
 etapes=[
  etape('La dépense initiale',
        'L’État engage 100 millions d’euros. Cette commande devient '
        'immédiatement un revenu pour les entreprises qui exécutent les '
        'travaux et pour leurs salariés : c’est la première barre.',
        on=['b0', 't100'], vif=['b0', 't100']),
  etape('La deuxième vague',
        'Les bénéficiaires consomment 80 % de ce revenu supplémentaire, soit '
        '80. Cette consommation devient à son tour un revenu pour d’autres '
        'agents. La deuxième barre vaut donc 0,8 fois la première.',
        on=['b1', 't80'], vif=['b1', 't80']),
  etape('Les vagues suivantes s’amortissent',
        'Le mécanisme se répète : 64, puis 51,2, puis 41… Chaque vague vaut '
        '0,8 fois la précédente. Les barres décroissent parce qu’à chaque '
        'tour une fraction du revenu est épargnée au lieu d’être dépensée.',
        on=['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 't64', 'tep'],
        vif=['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'tep']),
  etape('La somme converge',
        'La courbe cumulée s’aplatit : la somme des vagues tend vers '
        '1/(1 − 0,8) = 5 fois la dépense initiale, soit 500. Le '
        'multiplicateur n’est rien d’autre que la somme de cette série '
        'géométrique.',
        on=['cum', 'tfin'], vif=['cum', 'tfin']),
  etape('Ce que chaque fuite retire au multiplicateur',
        'Si l’on ajoute l’impôt puis les importations, chaque vague perd '
        'davantage : la raison de la série diminue et le multiplicateur '
        'tombe. Le cours montre ainsi qu’en économie ouverte il passe de 5 à '
        '2,5.',
        vif=['tep']),
 ],
 pieges=[
  {'t': 'Le multiplicateur n’est pas un gain gratuit',
   'd': 'Il mesure la somme des dépenses engendrées, pas une création de '
        'richesse à partir de rien : chaque vague suppose des capacités de '
        'production disponibles. Au plein emploi, l’effet se reporte sur les '
        'prix.'},
  {'t': 'Multiplicateur keynésien et multiplicateur de crédit',
   'd': 'Ici, une dépense engendre des revenus successifs. Le multiplicateur '
        'de crédit, lui, relie la base monétaire à la masse monétaire : ce '
        'sont deux mécanismes différents qui portent le même nom.'},
 ],
 main=[
  'Trace un axe horizontal gradué en vagues successives et un axe vertical '
  'pour les montants.',
  'Dessine la première barre à 100, puis chaque barre suivante à 80 % de la '
  'précédente : 80, 64, 51, 41…',
  'Écris la raison 0,8 au-dessus de la deuxième barre et note que c’est la '
  'propension marginale à consommer.',
  'Trace la courbe cumulée qui s’aplatit, et inscris le total 500 au bout.',
  'Annote en bas que la part manquante de chaque barre, soit 20 %, part en '
  'épargne : c’est la fuite qui fait converger la série.',
 ],
 phrase='La dépense initiale devient le revenu d’autres agents, qui en '
        'consomment une fraction égale à la propension marginale à '
        'consommer : la somme de ces vagues successives donne un revenu final '
        'multiplié par 1/(1 − c), et chaque fuite — épargne, impôt, '
        'importations — réduit d’autant ce coefficient.',
 liens=[{'c': '25', 'b': 747, 'l': 'Kahn (1931) et Keynes (1936) : le principe du multiplicateur'},
        {'c': '25', 'b': 777, 'l': 'L’épargne constitue une fuite à chaque période'},
        {'c': '25', 'b': 1070, 'l': 'Les importations, deuxième fuite du circuit'}],
 mots=['Kahn', 'Keynes', 'fuite', 'propension marginale à consommer',
       'économie ouverte'],
))

# ------------------------------------------------- marché du travail classique
OT = lin('ot', 'Offre de travail', 0.12, 0.14, 0.9, 0.9, 'ok')
DT = lin('dt', 'Demande de travail', 0.12, 0.9, 0.9, 0.16, 'ac')
EQT = inter(OT, DT)
SR = 0.72                      # salaire réel rigide, au-dessus de l'équilibre
XO = round((SR - 0.14) / (0.9 - 0.14) * (0.9 - 0.12) + 0.12, 4)
XD = round((SR - 0.9) / (0.16 - 0.9) * (0.9 - 0.12) + 0.12, 4)

L.append(fiche(
 id='marche-travail-classique',
 t='Le marché du travail néoclassique',
 st='Le chômage comme excès d’offre de travail provoqué par un salaire réel '
    'trop élevé — et la réponse de Keynes.',
 cat='macro', an=2, ch=['25', '3'],
 type='schema',
 q='Comment l’analyse néoclassique explique-t-elle le chômage, et en quoi '
   'Keynes renverse-t-il ce raisonnement ?',
 axes={'x': 'Quantité de travail', 'y': 'Salaire réel W/P'},
 depart='Un marché du travail où le salaire réel équilibre librement l’offre '
        'et la demande.',
 hyp=['Le travail est échangé sur un marché comme n’importe quel autre bien.',
      'L’offre de travail croît avec le salaire réel : plus il est élevé, '
      'plus d’individus acceptent de travailler.',
      'La demande de travail décroît avec le salaire réel : plus il est '
      'élevé, plus le coût du travail pèse sur les entreprises.'],
 pente=[{'s': 'L’offre de travail', 'd': 'croissante : un salaire réel plus '
         'élevé rend l’arbitrage favorable au travail plutôt qu’au loisir.'},
        {'s': 'La demande de travail', 'd': 'décroissante : l’entreprise '
         'embauche tant que la productivité marginale du travail couvre son '
         'coût réel ; au-delà, elle réduit ses effectifs.'}],
 fig={'series': [
   OT, DT,
   pt('eq', 'E', EQT[0], EQT[1], 'ac2'),
   rep('req', EQT[0], EQT[1], lx='L*', ly='(W/P)*', c='ac2'),
   lin('sr', 'Salaire rigide', 0.12, SR, 0.9, SR, 'ko', ep=2.4, lp=[0.3, SR + 0.05]),
   pt('a', 'A', XD, SR, 'ko'),
   pt('b', 'B', XO, SR, 'ko'),
   zone('cho', '', [(XD, SR), (XO, SR), (XO, SR - 0.05), (XD, SR - 0.05)], 'ko'),
   txt('tcho', 'chômage', (XD + XO) / 2 - 0.06, SR - 0.11, 'ko', taille=14, gras=True),
 ]},
 etapes=[
  etape('Les deux courbes du marché du travail',
        'L’offre de travail des salariés est croissante avec le salaire '
        'réel ; la demande de travail des entreprises est décroissante. Les '
        'axes portent la quantité de travail en abscisse et le salaire réel '
        'W/P en ordonnée.',
        on=['ot', 'dt'], vif=['ot', 'dt']),
  etape('L’équilibre concurrentiel',
        'À l’intersection, le salaire réel équilibre exactement l’offre et '
        'la demande de travail. Toute personne qui souhaite travailler à ce '
        'salaire trouve un emploi : il n’y a pas de chômage involontaire.',
        on=['eq', 'req'], vif=['eq', 'req']),
  etape('Un salaire réel maintenu trop haut',
        'Supposons maintenant que le salaire réel se maintienne au-dessus de '
        'son niveau d’équilibre — conventions, salaire minimum, négociation '
        'collective. La droite horizontale représente ce salaire rigide.',
        on=['sr'], vif=['sr']),
  etape('L’excès d’offre de travail',
        'À ce salaire, les entreprises ne demandent que la quantité du point '
        'A, alors que les salariés en offrent celle du point B. La différence '
        'entre les deux est un excès d’offre de travail : dans cette '
        'représentation, c’est le chômage.',
        on=['a', 'b', 'cho', 'tcho'], vif=['a', 'b', 'cho', 'tcho']),
  etape('Le remède néoclassique, et la réponse de Keynes',
        'Pour les néoclassiques, la flexibilité du salaire réel doit '
        'résorber cet écart : il suffirait de laisser le salaire baisser. '
        'Keynes inverse le raisonnement : le chômage peut venir d’une '
        'demande globale insuffisante, et baisser les salaires pèserait '
        'alors sur les revenus et la consommation, sans ramener le plein '
        'emploi.',
        vif=['cho']),
 ],
 pieges=[
  {'t': 'Salaire nominal et salaire réel',
   'd': 'L’axe porte le salaire réel W/P, pas le salaire affiché. Une hausse '
        'des prix fait baisser le salaire réel à salaire nominal inchangé : '
        'c’est pourquoi l’inflation peut jouer sur ce graphique sans qu’aucun '
        'salaire nominal ne bouge.'},
  {'t': 'Chômage classique et chômage keynésien',
   'd': 'Ici le chômage vient du prix du travail et se corrige par la '
        'flexibilité. Dans l’analyse keynésienne, il vient de l’insuffisance '
        'de la demande de biens, et la flexibilité salariale peut l’aggraver. '
        'Ce ne sont pas deux versions du même diagnostic.'},
 ],
 main=[
  'Trace les axes : la quantité de travail en abscisse, le salaire réel W/P '
  'en ordonnée.',
  'Trace l’offre de travail croissante et la demande de travail décroissante, '
  'et marque leur intersection E avec ses deux pointillés L* et (W/P)*.',
  'Trace une horizontale au-dessus de (W/P)* : c’est le salaire rigide.',
  'Place A sur la demande et B sur l’offre, à la hauteur de cette '
  'horizontale.',
  'Hachure le segment AB et écris « chômage » : c’est l’excès d’offre de '
  'travail.',
 ],
 phrase='Dans la représentation néoclassique, le chômage est un excès d’offre '
        'de travail provoqué par un salaire réel supérieur à son niveau '
        'd’équilibre, que la flexibilité salariale devrait résorber ; Keynes '
        'objecte que le chômage peut être involontaire et provenir d’une '
        'insuffisance de la demande effective, auquel cas la baisse des '
        'salaires déprime les revenus sans rétablir le plein emploi.',
 liens=[{'c': '25', 'b': 551, 'l': 'La vision néoclassique du marché du travail'},
        {'c': '25', 'b': 567, 'l': 'Le chômage néoclassique s’explique par un salaire réel trop élevé'},
        {'c': '3', 'b': 822, 'l': 'Le marché du travail keynésien'}],
 mots=['chômage classique', 'salaire réel', 'flexibilité', 'Keynes',
       'chômage involontaire'],
))

# ---------------------------------------------------- marché de la monnaie
DM = pol('dm', 'Demande de monnaie', courbe_dec(0.1, 0.92, 0.95, 0.12, 9, 0.5), 'ac')
OM = lin('om', 'Offre de monnaie', 0.52, 0, 0.52, 0.95, 'ok', ep=3)
EM = (0.52, round(y_de([0.1, 0.92, 0.95, 0.12], 0.52), 4))

L.append(fiche(
 id='marche-monnaie',
 t='L’équilibre du marché de la monnaie',
 st='Comment le taux d’intérêt s’établit par la rencontre d’une demande de '
    'monnaie décroissante et d’une offre exogène.',
 cat='macro', an=2, ch=['25', '2'],
 type='schema',
 q='Qu’est-ce qui détermine le taux d’intérêt chez Keynes, et que se '
   'passe-t-il quand la banque centrale augmente la quantité de monnaie ?',
 axes={'x': 'Quantité de monnaie', 'y': 'Taux d’intérêt r'},
 depart='Une offre de monnaie fixée par les autorités monétaires, donc '
        'indépendante du taux d’intérêt.',
 hyp=['L’offre de monnaie est exogène : elle est décidée en dehors du modèle '
      'et ne dépend pas du taux d’intérêt, d’où sa représentation verticale.',
      'La demande de monnaie répond à trois motifs : transaction et '
      'précaution, qui dépendent du revenu, et spéculation, qui dépend du '
      'taux d’intérêt.',
      'Le revenu national est donné : on raisonne à revenu constant.'],
 pente=[{'s': 'La demande de monnaie', 'd': 'décroissante : plus le taux '
         'd’intérêt est élevé, plus il est coûteux de conserver de la '
         'monnaie plutôt que des titres, donc moins les agents en demandent '
         'pour motif de spéculation.'},
        {'s': 'L’offre de monnaie', 'd': 'verticale : la quantité offerte est '
         'donnée, quel que soit le taux d’intérêt.'}],
 fig={'series': [
   DM, OM,
   pt('e', 'E', EM[0], EM[1], 'ac2'),
   rep('re', EM[0], EM[1], ly='r*', c='ac2'),
 ]},
 etapes=[
  etape('La demande de monnaie',
        'Elle décroît avec le taux d’intérêt : lorsque les titres rapportent '
        'beaucoup, détenir de la monnaie coûte cher en rendement abandonné, '
        'et les agents en conservent moins. C’est la préférence pour la '
        'liquidité.',
        on=['dm'], vif=['dm']),
  etape('L’offre de monnaie',
        'Elle est supposée exogène : fixée par les autorités monétaires, elle '
        'ne dépend pas du taux d’intérêt et se représente par une verticale. '
        'Le cours rappelle que c’est une simplification.',
        on=['om'], vif=['om']),
  etape('Le taux d’intérêt d’équilibre',
        'À l’intersection, la quantité de monnaie offerte correspond '
        'exactement à celle que les agents souhaitent détenir. Le taux '
        'd’intérêt r* est donc déterminé sur le marché monétaire, et non par '
        'la confrontation de l’épargne et de l’investissement.',
        on=['e', 're'], vif=['e', 're']),
  etape('Une politique monétaire expansionniste',
        'La banque centrale augmente l’offre de monnaie : la verticale se '
        'déplace vers la droite. Les agents détiennent plus de monnaie qu’ils '
        'ne le souhaitent, achètent des titres, dont le prix monte — donc le '
        'taux d’intérêt baisse jusqu’au nouvel équilibre.',
        add=[lin('om1', 'O’', 0.74, 0, 0.74, 0.95, 'bl', ep=3),
             pt('e1', 'E’', 0.74, round(y_de([0.1, 0.92, 0.95, 0.12], 0.74), 4), 'bl'),
             rep('re1', 0.74, round(y_de([0.1, 0.92, 0.95, 0.12], 0.74), 4),
                 ly='r’', c='bl'),
             fl('f', '', 0.56, 0.28, 0.7, 0.28, 'bl')],
        vif=['om1', 'e1', 're1', 'f']),
  etape('Pourquoi ce marché commande la courbe LM',
        'À chaque niveau de revenu correspond une demande de monnaie '
        'différente, donc un taux d’équilibre différent. En reportant ces '
        'couples (revenu, taux) dans un autre repère, on obtient la courbe '
        'LM.',
        vif=['e', 'e1']),
 ],
 pieges=[
  {'t': 'Ce n’est pas le marché des fonds prêtables',
   'd': 'Chez les classiques, le taux d’intérêt équilibre l’épargne et '
        'l’investissement. Ici, il équilibre l’offre et la demande de '
        'monnaie : il est le prix du renoncement à la liquidité, non le prix '
        'de l’épargne.'},
  {'t': 'Une hausse du revenu déplace la courbe, elle ne la parcourt pas',
   'd': 'Une variation du taux d’intérêt fait glisser l’économie le long de '
        'la demande de monnaie. Une hausse du revenu, elle, déplace toute la '
        'courbe vers la droite, puisqu’elle accroît les besoins de monnaie '
        'pour transaction.'},
 ],
 main=[
  'Trace les axes : quantité de monnaie en abscisse, taux d’intérêt en '
  'ordonnée.',
  'Trace la demande de monnaie décroissante, qui s’aplatit vers le bas à '
  'droite.',
  'Trace l’offre de monnaie comme une verticale, et note à côté qu’elle est '
  'exogène.',
  'Marque E à l’intersection et reporte r* en pointillé sur l’axe vertical.',
  'Pour l’expansion monétaire, trace une seconde verticale à droite, place E’ '
  'et montre par une flèche que r baisse.',
 ],
 phrase='Chez Keynes, le taux d’intérêt se détermine sur le marché de la '
        'monnaie par la confrontation d’une demande décroissante, fondée sur '
        'la préférence pour la liquidité, et d’une offre exogène : une '
        'expansion monétaire déplace l’offre vers la droite et fait baisser '
        'le taux, ce qui constitue le premier maillon de la politique '
        'monétaire.',
 liens=[{'c': '25', 'b': 1285, 'l': 'L’équilibre du marché monétaire'},
        {'c': '25', 'b': 1299, 'l': 'L’offre de monnaie est supposée exogène'},
        {'c': '25', 'b': 1133, 'l': 'La monnaie, actif recherché pour sa liquidité'}],
 mots=['préférence pour la liquidité', 'offre de monnaie', 'taux d’intérêt',
       'politique monétaire'],
))

# --------------------------------------------- demande spéculative et trappe
L.append(fiche(
 id='trappe-liquidite',
 t='La demande spéculative et la trappe à liquidité',
 st='Pourquoi la demande de monnaie devient horizontale à taux très faible, '
    'et ce que cela interdit à la politique monétaire.',
 cat='macro', an=2, ch=['25', '2'],
 type='schema',
 q='Pourquoi, à taux d’intérêt très bas, une augmentation de la quantité de '
   'monnaie ne fait-elle plus baisser le taux d’intérêt ?',
 axes={'x': 'Demande de monnaie pour motif de spéculation', 'y': 'Taux d’intérêt r'},
 depart='Une demande spéculative décroissante, qui devient parfaitement '
        'élastique à un taux plancher.',
 hyp=['Le prix des obligations varie en sens inverse du taux d’intérêt : '
      'c’est l’« effet balançoire ».',
      'Les agents comparent le taux courant à un taux qu’ils jugent normal : '
      'au-dessus, ils anticipent une baisse, en dessous, une remontée.',
      'À un taux jugé très faible, tous anticipent une remontée, donc une '
      'perte en capital sur les titres.'],
 pente=[{'s': 'La partie décroissante', 'd': 'un taux élevé fait anticiper sa '
         'baisse, donc une hausse du cours des obligations : les agents '
         'préfèrent les titres et conservent peu de monnaie.'},
        {'s': 'La partie horizontale', 'd': 'au taux plancher, chacun '
         'anticipe une remontée et donc une perte en capital : toute monnaie '
         'supplémentaire est thésaurisée au lieu d’acheter des titres.'}],
 fig={'series': [
   pol('l2', 'Demande spéculative',
       [(0.1, 0.9), (0.2, 0.74), (0.33, 0.58), (0.5, 0.42), (0.66, 0.31),
        (0.78, 0.26), (0.95, 0.25)], 'ac'),
   lin('plancher', '', 0.1, 0.25, 0.95, 0.25, 'gr', ep=1.6),
   txt('tp', 'taux plancher : la trappe à liquidité', 0.4, 0.17, 'ko', taille=14),
   txt('th', 'zone normale : le taux réagit', 0.14, 0.95, 'ac', taille=13),
 ]},
 etapes=[
  etape('La relation décroissante',
        'Dans la zone normale, la demande de monnaie pour motif de '
        'spéculation décroît avec le taux d’intérêt : un taux élevé rend les '
        'titres attractifs et détourne de la monnaie.',
        on=['l2', 'th'], vif=['l2', 'th']),
  etape('Le taux devient très faible',
        'Lorsque le taux descend très bas, les agents jugent qu’il ne peut '
        'plus guère baisser : ils anticipent sa remontée, donc une chute du '
        'cours des obligations et une perte en capital.',
        on=['plancher'], vif=['plancher']),
  etape('La courbe devient horizontale',
        'Tous préfèrent alors conserver la monnaie : la demande devient '
        'parfaitement élastique. C’est la trappe à liquidité — toute monnaie '
        'supplémentaire est absorbée sans que le taux bouge.',
        on=['tp'], vif=['tp', 'l2']),
  etape('La politique monétaire perd son canal habituel',
        'Augmenter l’offre de monnaie ne fait plus baisser le taux : le canal '
        'conventionnel est bloqué. Cela ne signifie pas que toute politique '
        'monétaire devient inefficace, mais que la baisse des taux ne peut '
        'plus servir de levier.',
        add=[fl('f', 'offre de monnaie ↑', 0.55, 0.33, 0.85, 0.33, 'bl'),
             txt('tr', 'r ne bouge plus', 0.62, 0.1, 'bl', taille=14, gras=True)],
        vif=['f', 'tr']),
  etape('La conséquence sur la courbe LM',
        'Reportée dans le repère IS-LM, cette zone donne la partie '
        'horizontale de LM : la politique budgétaire y devient au contraire '
        'particulièrement efficace, puisque la relance ne fait pas remonter '
        'le taux d’intérêt.',
        vif=['tp']),
 ],
 pieges=[
  {'t': 'La trappe n’est pas une absence de demande de monnaie',
   'd': 'C’est au contraire une demande devenue insatiable au taux plancher : '
        'les agents absorbent toute la monnaie offerte. Ce n’est pas un vide, '
        'c’est une préférence absolue pour la liquidité.'},
  {'t': 'Taux plancher n’est pas forcément zéro',
   'd': 'Le plancher est le taux que les agents jugent anormalement bas, pas '
        'nécessairement le zéro arithmétique. Des taux négatifs ont d’ailleurs '
        'été pratiqués sur la facilité de dépôt après 2008.'},
 ],
 main=[
  'Trace les axes : demande spéculative de monnaie en abscisse, taux '
  'd’intérêt en ordonnée.',
  'Trace une courbe décroissante qui s’aplatit nettement vers le bas à '
  'droite.',
  'Trace l’horizontale du taux plancher et prolonge la courbe le long de '
  'cette horizontale.',
  'Annote la partie inclinée « le taux réagit » et la partie plate « trappe à '
  'liquidité ».',
  'Ajoute une flèche horizontale dans la zone plate pour montrer qu’une '
  'hausse de l’offre de monnaie ne déplace plus le taux.',
 ],
 phrase='Lorsque le taux d’intérêt atteint un niveau que les agents jugent '
        'anormalement bas, ils anticipent sa remontée et préfèrent conserver '
        'toute monnaie supplémentaire : la demande de monnaie devient '
        'parfaitement élastique, le canal conventionnel de la politique '
        'monétaire se bloque, et la politique budgétaire retrouve son '
        'efficacité.',
 liens=[{'c': '25', 'b': 1259, 'l': 'La trappe à liquidité, cas extrême de préférence pour la monnaie'},
        {'c': '25', 'b': 1209, 'l': 'Le prix des obligations varie en sens inverse du taux'},
        {'c': '25', 'b': 2234, 'l': 'La trappe redonne un intérêt à la politique budgétaire'}],
 mots=['trappe à liquidité', 'préférence pour la liquidité', 'obligations',
       'politique monétaire', 'Keynes', '2008'],
))
