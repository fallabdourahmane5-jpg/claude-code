# -*- coding: utf-8 -*-
"""Courbes des chapitres 6 et 7 — croissance, inégalités, développement
et soutenabilité."""

import math
from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     cloche, inter, y_de, x_de, bouge)

L = []


def _rac(coef, a=0.02, b=0.985, n=22):
    out = []
    for j in range(n):
        k = a + (b - a) * j / (n - 1.0)
        out.append((round(k, 4), round(coef * math.sqrt(k), 4)))
    return out


# ------------------------------------------------------------------ Solow
FK = _rac(0.95)
SFK = _rac(0.38)
SFK2 = _rac(0.5225)

L.append(fiche(
 id='solow',
 t='Le modèle de Solow et l’état stationnaire',
 st='Pourquoi l’accumulation du capital finit par s’épuiser, et ce qui peut '
    'repousser cette limite.',
 cat='croissance', an=1, ch=['6'],
 type='schema',
 q='Pourquoi la croissance par tête s’éteint-elle à long terme dans le modèle '
   'de Solow, et par quels leviers peut-on repousser l’état stationnaire ?',
 axes={'x': 'Capital par tête k', 'y': 'Production par tête'},
 depart='Une économie dotée d’un stock de capital par tête inférieur à son '
        'état stationnaire.',
 hyp=['Long terme : tous les facteurs sont variables et les facteurs sont '
      'substituables entre eux, contrairement à Harrod-Domar.',
      'Productivité marginale du capital décroissante, mais rendements '
      'd’échelle constants.',
      'La totalité de l’épargne est investie : S = I.',
      'Prix et salaires flexibles, ce qui rend les ajustements possibles, et '
      'concurrence pure et parfaite.',
      'Le progrès technique est exogène : le modèle en montre le rôle décisif '
      'sans expliquer d’où il vient.'],
 pente=[{'s': 'Production par tête f(k)', 'd': 'croissante mais concave : '
         'plus de capital par travailleur donne plus de production par '
         'travailleur, mais de moins en moins, parce que la productivité '
         'marginale du capital décroît.'},
        {'s': 'Investissement s·f(k)', 'd': 'même forme, simplement plus '
         'basse : c’est la fraction épargnée, donc investie, de la '
         'production.'},
        {'s': 'Amortissement δk', 'd': 'une droite issue de l’origine, de '
         'pente δ : plus le stock de capital est élevé, plus il faut en '
         'remplacer chaque année.'}],
 fig={'series': [
   pol('fk', 'f(k) — production par tête', FK, 'ac', ep=3.2, lp=[0.62, 0.86]),
 ]},
 etapes=[
  etape('La fonction de production par tête',
        'Solow raisonne par tête : f(k) relie la production par travailleur '
        'au capital par travailleur. Elle est croissante — plus de capital, '
        'plus de production — mais concave, car la productivité marginale du '
        'capital décroît.',
        on=['fk'], vif=['fk']),
  etape('L’épargne devient l’investissement',
        'Une fraction s de la production est épargnée, et comme l’épargne est '
        'intégralement investie, la courbe s·f(k) représente l’investissement '
        'par tête. Elle a la même forme, en plus bas.',
        add=[pol('sfk', 's·f(k) — investissement', SFK, 'ok', ep=3,
                 lp=[0.58, 0.17])],
        vif=['sfk']),
  etape('Mais une partie sert seulement à remplacer l’usure',
        'L’amortissement δk est une droite issue de l’origine : plus le stock '
        'de capital par tête est élevé, plus il faut en remplacer. Investir '
        'ne signifie donc pas automatiquement accumuler.',
        add=[lin('dk', 'δk — amortissement', 0.0, 0.0, 0.985, 0.6107, 'ac2',
                 ep=3, lp=[0.27, 0.06])],
        vif=['dk']),
  etape('L’état stationnaire k*',
        'Au point où les deux courbes se croisent, l’investissement compense '
        'exactement l’usure : le capital par tête cesse de varier. C’est '
        'l’état stationnaire.',
        add=[pt('e', 'k*', 0.3756, 0.2329, 'jn'),
             rep('re', 0.3756, 0.2329, lx='k*', c='jn')],
        vif=['e', 're']),
  etape('Pourquoi l’économie y converge par la gauche',
        'En deçà de k*, l’investissement dépasse l’amortissement : le capital '
        'par tête augmente et l’économie se rapproche de k*. C’est le '
        'rattrapage des pays peu dotés en capital.',
        add=[fl('fg', 's·f(k) > δk', 0.12, 0.08, 0.3, 0.08, 'ok')],
        vif=['fg']),
  etape('Et par la droite',
        'Au-delà de k*, l’investissement ne suffit plus à compenser l’usure : '
        'le capital par tête diminue et l’économie revient vers k*. '
        'L’économie converge donc naturellement vers l’état stationnaire.',
        add=[fl('fd', 'δk > s·f(k)', 0.78, 0.08, 0.46, 0.08, 'ko')],
        off=['fg'],
        vif=['fd']),
  etape('La conséquence : la croissance par tête s’éteint',
        'À l’état stationnaire, le capital par tête est constant, donc la '
        'production par tête aussi. Si rien ne change, la croissance du '
        'niveau de vie s’arrête : c’est la limite interne du modèle.',
        add=[txt('tc', 'k constant → y constant → croissance par tête nulle',
                 0.1, 0.95, 'ko', taille=15, gras=True)],
        off=['fd'],
        vif=['tc']),
  etape('Premier levier : élever le taux d’épargne',
        'Un taux d’épargne plus élevé déplace la courbe d’investissement vers '
        'le haut : le nouvel état stationnaire correspond à un capital par '
        'tête et à un niveau de vie supérieurs. Mais la croissance s’y éteint '
        'à nouveau.',
        add=[pol('sfk2', 's′·f(k)', SFK2, 'bl', ep=2.8, lp=[0.88, 0.62]),
             pt('e2', 'k**', 0.7102, 0.4403, 'bl'),
             rep('r2', 0.7102, 0.4403, lx='k**', c='bl')],
        off=['tc'],
        vif=['sfk2', 'e2', 'r2']),
  etape('Le levier décisif : le progrès technique',
        'Seul le progrès technique peut déplacer vers le haut la fonction de '
        'production elle-même et entretenir durablement la croissance par '
        'tête. Mais Solow le laisse exogène : il en montre le rôle sans '
        'expliquer comment il est produit.',
        add=[txt('tp', 'progrès technique exogène : le moteur… non expliqué',
                 0.1, 0.95, 'jn', taille=15, gras=True)],
        vif=['tp']),
 ],
 pieges=[
  {'t': 'Ce n’est pas la production qui est comparée à l’amortissement',
   'd': 'C’est l’investissement s·f(k), donc la fraction épargnée. Comparer '
        'directement f(k) à δk donne un état stationnaire faux, très à '
        'droite.'},
  {'t': 'Hausse de l’épargne : niveau, pas croissance',
   'd': 'Épargner davantage élève le niveau de vie à l’état stationnaire, '
        'mais la croissance par tête finit toujours par s’éteindre. C’est la '
        'distinction la plus discriminante sur ce modèle.'},
  {'t': 'Convergence conditionnelle, pas automatique',
   'd': 'Les pays à faible capital par tête ont un rendement du capital plus '
        'élevé et rattrapent plus vite, mais seulement vers LEUR propre état '
        'stationnaire, qui dépend de leur taux d’épargne et de leur '
        'technologie.'},
 ],
 main=[
  'Trace les axes : le capital par tête en abscisse, la production par tête '
  'en ordonnée.',
  'Trace f(k) croissante et concave, puis s·f(k) de même forme mais plus '
  'basse.',
  'Trace la droite δk issue de l’origine.',
  'Marque leur intersection avec s·f(k) : c’est k*, l’état stationnaire ; '
  'projette-le sur l’axe.',
  'Ajoute les deux flèches de convergence, l’une venant de la gauche, l’autre '
  'de la droite, puis une seconde courbe d’investissement plus haute pour '
  'figurer la hausse de l’épargne.',
 ],
 phrase='Dans le modèle de Solow, la productivité marginale décroissante du '
        'capital fait que l’investissement s·f(k) finit par être exactement '
        'compensé par l’amortissement δk : l’économie converge vers un état '
        'stationnaire où le capital et la production par tête sont constants, '
        'de sorte que seule l’élévation du taux d’épargne — qui en relève le '
        'niveau — et surtout le progrès technique — laissé exogène — peuvent '
        'repousser cette limite.',
 liens=[{'c': '6', 'b': 2321, 'l': 'Le modèle de Solow : croissance équilibrée et état stationnaire'},
        {'c': '6', 'b': 2331, 'l': 'Les hypothèses structurantes du modèle'},
        {'c': '6', 'b': 2354, 'l': 'Amortissement et contrainte de renouvellement'},
        {'c': '6', 'b': 2364, 'l': 'Le mécanisme de convergence vers k*'},
        {'c': '6', 'b': 2373, 'l': 'Repousser l’état stationnaire : les leviers'}],
 mots=['Solow', 'état stationnaire', 'convergence', 'progrès technique',
       'amortissement', 'capital par tête', 'résidu'],
))

# ----------------------------------------------------------- Harrod-Domar
GEFF = [(0.03, 0.52), (0.12, 0.58), (0.2, 0.47), (0.28, 0.56), (0.36, 0.44),
        (0.44, 0.60), (0.52, 0.36), (0.6, 0.68), (0.68, 0.26), (0.78, 0.8),
        (0.88, 0.14), (0.97, 0.92)]

L.append(fiche(
 id='harrod-domar',
 t='Harrod-Domar et le fil du rasoir',
 st='Trois taux de croissance déterminés indépendamment — et rien pour les '
    'réconcilier.',
 cat='croissance', an=1, ch=['6'],
 type='schema',
 q='Pourquoi la croissance est-elle structurellement instable chez Harrod et '
   'Domar, et que recouvrent les trois taux de croissance du modèle ?',
 axes={'x': 'Temps', 'y': 'Taux de croissance'},
 depart='Une économie dont le taux de croissance effectif part au voisinage '
        'du taux garanti.',
 hyp=['Économie fermée, court terme, approche post-keynésienne.',
      'Facteurs de production complémentaires : pas de substituabilité entre '
      'capital et travail.',
      'Coefficients techniques stables : le rapport capital sur production '
      'est rigide et ne s’ajuste pas.',
      'Aucun mécanisme automatique d’ajustement, aucune coordination '
      'spontanée des agents.',
      'La croissance dépend de la demande effective, pas de l’offre '
      'auto-régulée.'],
 pente=[{'s': 'Taux garanti g_w', 'd': 'horizontal : il vaut le taux '
         'd’épargne divisé par le coefficient de capital. Il est purement '
         'économique et ne dépend pas de la démographie.'},
        {'s': 'Taux naturel g_n', 'd': 'horizontal lui aussi : il dépend de '
         'la croissance de la population active, donc de la démographie, et '
         'non de l’épargne.'},
        {'s': 'Taux effectif g', 'd': 'erratique : il dépend de la '
         'conjoncture, des anticipations et des chocs. Rien ne le ramène vers '
         'les deux autres.'}],
 fig={'series': [
   lin('gw', 'Taux garanti g_w', 0.0, 0.52, 1.0, 0.52, 'ok', ep=3,
       lp=[0.18, 0.56]),
 ]},
 etapes=[
  etape('Le taux garanti : l’équilibre sur le marché des biens',
        'C’est le taux qui assure l’égalité entre épargne et investissement, '
        'donc l’équilibre du marché des biens. Il vaut le taux d’épargne '
        'divisé par le coefficient de capital.',
        on=['gw'],
        add=[txt('tf', 'g_w = s / v', 0.03, 0.44, 'ok', taille=16, gras=True)],
        vif=['gw', 'tf']),
  etape('Le coefficient de capital, clé du modèle',
        'Il mesure la quantité de capital nécessaire pour produire une unité '
        'de richesse. Comme les facteurs sont complémentaires et qu’il n’y a '
        'pas de substituabilité, il est rigide : produire plus exige '
        'proportionnellement plus de capital.',
        add=[txt('tv', 'v élevé → il faut beaucoup investir pour 1 point de croissance',
                 0.05, 0.95, 'ac', taille=14)],
        vif=['tv']),
  etape('Le taux naturel : le plein emploi',
        'C’est le taux compatible avec le plein emploi : il est déterminé par '
        'la croissance de la population active et la participation au marché '
        'du travail. Il ne dépend ni de l’épargne ni de l’investissement.',
        add=[lin('gn', 'Taux naturel g_n', 0.0, 0.68, 1.0, 0.68, 'ac2', ep=3,
                 lp=[0.18, 0.72])],
        off=['tv'],
        vif=['gn']),
  etape('Deux taux, deux mécanismes totalement indépendants',
        'Le garanti dépend du comportement d’épargne et de la structure '
        'productive ; le naturel, de la démographie. Rien ne fait qu’ils '
        'coïncident : leur écart est le premier déséquilibre du modèle.',
        add=[fl('fe', 'aucun lien entre les deux', 0.86, 0.54, 0.86, 0.66,
                'jn')],
        vif=['fe']),
  etape('Le taux effectif : ce que l’on observe',
        'C’est le taux réellement constaté, qui dépend de la conjoncture, des '
        'anticipations des entreprises, des chocs d’offre et de demande. Il '
        'est empirique et fluctuant.',
        add=[pol('g', 'Taux effectif g', GEFF, 'ko', ep=3, lp=[0.5, 0.05])],
        off=['fe'],
        vif=['g']),
  etape('Pourquoi l’écart se creuse au lieu de se résorber',
        'Si le taux effectif dépasse le garanti, les entreprises constatent '
        'des capacités insuffisantes, investissent davantage et accélèrent '
        'encore. S’il lui est inférieur, elles constatent des capacités '
        'excédentaires et freinent. L’écart s’amplifie.',
        add=[fl('fh', 'surchauffe cumulative', 0.72, 0.84, 0.95, 0.9, 'ko'),
             fl('fb', 'dépression cumulative', 0.72, 0.2, 0.88, 0.12, 'ko')],
        vif=['fh', 'fb']),
  etape('Le fil du rasoir',
        'Le chemin de la croissance équilibrée exigerait que les trois taux '
        'coïncident exactement. Ce chemin est si étroit qu’il relève du '
        'hasard : la croissance n’est pas auto-stabilisatrice.',
        add=[txt('tr', 'g = g_w = g_n : un chemin si étroit qu’il relève du hasard',
                 0.05, 0.95, 'jn', taille=15, gras=True)],
        off=['fh', 'fb'],
        vif=['tr']),
 ],
 pieges=[
  {'t': 'Ne pas confondre les trois taux',
   'd': 'Effectif : ce qu’on observe. Garanti : ce qui équilibre le marché '
        'des biens, s/v. Naturel : ce qui assure le plein emploi, fixé par la '
        'démographie. Les trois répondent à trois questions différentes.'},
  {'t': 'L’instabilité n’est pas un accident',
   'd': 'Elle découle des hypothèses : complémentarité des facteurs, '
        'coefficient de capital rigide, absence de mécanisme d’ajustement. '
        'C’est précisément ce que Solow renversera en supposant les facteurs '
        'substituables et les prix flexibles.'},
  {'t': 'L’axe des ordonnées porte des taux, pas des niveaux',
   'd': 'Le graphique montre des rythmes de croissance. Un taux effectif qui '
        'descend sans devenir négatif signifie que la production continue '
        'd’augmenter, plus lentement.'},
 ],
 main=[
  'Trace les axes : le temps en abscisse, le taux de croissance en ordonnée.',
  'Trace une première horizontale : le taux garanti, et écris g_w = s/v à '
  'côté.',
  'Trace une seconde horizontale à un autre niveau : le taux naturel, fixé '
  'par la démographie.',
  'Trace une courbe erratique qui oscille autour du garanti en s’en écartant '
  'de plus en plus : c’est le taux effectif.',
  'Ajoute les deux flèches divergentes, vers le haut et vers le bas, et écris '
  '« fil du rasoir ».',
 ],
 phrase='Chez Harrod et Domar, le taux de croissance garanti — rapport du '
        'taux d’épargne au coefficient de capital — et le taux naturel — fixé '
        'par la croissance de la population active — sont déterminés par des '
        'mécanismes entièrement indépendants, et aucun mécanisme d’ajustement '
        'ne ramène le taux effectif vers eux : la croissance équilibrée '
        'relève donc du hasard, ce que Harrod résume par l’image du fil du '
        'rasoir.',
 liens=[{'c': '6', 'b': 2087, 'l': 'Harrod-Domar : auteurs, contexte et nature du modèle'},
        {'c': '6', 'b': 2108, 'l': 'Les hypothèses fondamentales'},
        {'c': '6', 'b': 2142, 'l': 'Le coefficient de capital, clé du modèle'},
        {'c': '6', 'b': 2177, 'l': 'Les trois taux de croissance'},
        {'c': '6', 'b': 2223, 'l': 'La condition d’équilibre global'}],
 mots=['Harrod', 'Domar', 'fil du rasoir', 'taux garanti', 'taux naturel',
       'coefficient de capital', 'demande effective'],
))

# ------------------------------------------------------------ Lorenz-Gini
def _lorenz(p):
    return [(round(x / 20.0, 4), round((x / 20.0) ** p, 4)) for x in range(21)]


LR = _lorenz(2.2)
LRP = _lorenz(4.2)

L.append(fiche(
 id='lorenz-gini',
 t='La courbe de Lorenz et le coefficient de Gini',
 st='Lire la concentration des revenus dans l’écart à la diagonale.',
 cat='croissance', an=1, ch=['6'],
 type='schema',
 q='Comment la courbe de Lorenz représente-t-elle la répartition des revenus, '
   'et que mesure exactement le coefficient de Gini qu’on en déduit ?',
 axes={'x': 'Population cumulée', 'y': 'Revenu ou patrimoine cumulé',
       'gx': [[0.0, '0 %'], [0.5, '50 %'], [1.0, '100 %']],
       'gy': [[0.0, '0 %'], [0.5, '50 %'], [1.0, '100 %']]},
 depart='Une population classée par revenu croissant, du plus pauvre au plus '
        'riche.',
 hyp=['En abscisse, la population cumulée de 0 à 100 % ; en ordonnée, le '
      'revenu ou le patrimoine cumulé de 0 à 100 %.',
      'La population est toujours rangée par ordre croissant de revenu : '
      'c’est ce qui garantit que la courbe est convexe.',
      'Contrairement au rapport interdécile ou au rapport de Palma, '
      'l’indicateur prend en compte toute la distribution, pas seulement deux '
      'groupes.'],
 pente=[{'s': 'Droite d’équirépartition', 'd': 'la diagonale : 10 % de la '
         'population détiendraient 10 % du revenu, 50 % en détiendraient '
         '50 %. C’est l’égalité parfaite.'},
        {'s': 'Courbe de Lorenz', 'd': 'toujours en dessous de la diagonale, '
         'et convexe : les premiers déciles, les plus pauvres, cumulent peu. '
         'Plus la courbe s’éloigne de la diagonale, plus les inégalités sont '
         'fortes.'}],
 fig={'series': [
   lin('eq', 'Équirépartition', 0.0, 0.0, 1.0, 1.0, 'gr', ep=2.4,
       lp=[0.3, 0.42]),
 ]},
 etapes=[
  etape('La droite d’équirépartition',
        'Si la société était parfaitement égalitaire, 10 % de la population '
        'auraient 10 % du revenu, 50 % en auraient 50 %, 100 % en auraient '
        '100 %. On obtiendrait exactement la diagonale.',
        on=['eq'], vif=['eq']),
  etape('La réalité passe en dessous',
        'Dans les faits, la moitié la plus pauvre de la population détient '
        'bien moins de la moitié du revenu. La courbe réelle — la courbe de '
        'Lorenz — se situe donc sous la diagonale.',
        add=[pol('lr', 'Lorenz — revenus', LR, 'ac', ep=3.2, lp=[0.54, 0.40]),
             pt('m', '', 0.5, 0.2176, 'ac'),
             rep('rm', 0.5, 0.2176, ly='≈ 22 %', c='ac')],
        vif=['lr', 'm', 'rm']),
  etape('L’écart à la diagonale, c’est l’inégalité',
        'Plus la courbe s’éloigne de la droite d’équirépartition, plus les '
        'inégalités sont fortes. Une courbe confondue avec la diagonale '
        'signifierait l’égalité parfaite.',
        add=[zone('g', '', [(0.0, 0.0), (0.25, 0.0367), (0.5, 0.2176),
                            (0.75, 0.5296), (1.0, 1.0), (0.75, 0.75),
                            (0.5, 0.5), (0.25, 0.25)], 'jn'),
             txt('tg', 'aire entre les deux courbes', 0.42, 0.62, 'jn',
                 taille=14)],
        vif=['g', 'tg']),
  etape('Le coefficient de Gini',
        'Il synthétise cet écart en un seul chiffre compris entre 0 et 1 : '
        '0 pour l’égalité parfaite, 1 pour l’inégalité totale — une seule '
        'personne détiendrait tout.',
        add=[txt('tn', 'Gini : 0 = égalité parfaite · 1 = inégalité totale',
                 0.06, 0.95, 'ok', taille=15, gras=True)],
        off=['tg'],
        vif=['tn']),
  etape('Les ordres de grandeur',
        'Les pays égalitaires se situent autour de 0,25 à 0,30 ; les pays '
        'très inégalitaires entre 0,45 et 0,60. La France est autour de 0,29, '
        'environ 0,297 en 2023 : des inégalités modérées mais persistantes.',
        add=[txt('tf', 'France ≈ 0,297 en 2023', 0.06, 0.87, 'ac', taille=15,
                 gras=True)],
        vif=['tf']),
  etape('Le patrimoine est toujours plus concentré que le revenu',
        'Dans tous les pays, le Gini du patrimoine dépasse celui du revenu : '
        'le patrimoine se transmet, il génère lui-même du revenu et il '
        's’accumule dans le temps. Sa courbe de Lorenz est donc bien plus '
        'creusée.',
        add=[pol('lp', 'Lorenz — patrimoines', LRP, 'ko', ep=3,
                 lp=[0.84, 0.1])],
        off=['tn', 'tf', 'g'],
        vif=['lp']),
  etape('Ce que le Gini ne dit pas',
        'Un chiffre unique est peu intuitif et ne dit pas où se situent les '
        'écarts : au sommet, en bas, ou dans les classes moyennes. Deux pays '
        'peuvent avoir le même Gini avec des structures très différentes, et '
        'il peut rester stable alors que le top 1 % s’enrichit fortement.',
        add=[txt('tl', 'même Gini ≠ même société', 0.1, 0.95, 'jn', taille=15,
                 gras=True)],
        vif=['tl']),
 ],
 pieges=[
  {'t': 'La courbe ne peut jamais passer au-dessus de la diagonale',
   'd': 'Puisque la population est classée par revenu croissant, les premiers '
        'cumulent nécessairement moins que leur part de population. Dessiner '
        'la courbe au-dessus est impossible.'},
  {'t': 'Le Gini est un indicateur de concentration, pas de pauvreté',
   'd': 'Un pays peut voir son Gini baisser alors que tout le monde '
        's’appauvrit. Il mesure un écart relatif, pas un niveau de vie.'},
  {'t': 'Revenu et patrimoine donnent deux courbes différentes',
   'd': 'Toujours préciser laquelle on commente. Les inégalités patrimoniales '
        'sont structurellement plus fortes, et ne pas le dire fausse toute '
        'comparaison internationale.'},
 ],
 main=[
  'Trace un carré : population cumulée de 0 à 100 % en abscisse, revenu '
  'cumulé de 0 à 100 % en ordonnée.',
  'Trace la diagonale et nomme-la droite d’équirépartition.',
  'Trace sous elle une courbe convexe partant de l’origine et rejoignant le '
  'coin opposé : c’est la courbe de Lorenz.',
  'Hachure l’aire entre les deux : c’est ce que mesure le coefficient de '
  'Gini.',
  'Trace enfin une seconde courbe encore plus creusée pour le patrimoine, et '
  'note les ordres de grandeur du Gini.',
 ],
 phrase='Le coefficient de Gini mesure la concentration globale des '
        'inégalités à partir de la courbe de Lorenz, qui porte en abscisse la '
        'population cumulée et en ordonnée le revenu cumulé : compris entre 0 '
        'et 1, il synthétise l’écart à la droite d’équirépartition, mais il '
        'ne dit ni où se situent les écarts ni s’ils se creusent au sommet, '
        'et il est systématiquement plus élevé pour le patrimoine que pour le '
        'revenu.',
 liens=[{'c': '6', 'b': 1870, 'l': 'Le principe de la courbe de Lorenz'},
        {'c': '6', 'b': 1884, 'l': 'La définition du coefficient de Gini'},
        {'c': '6', 'b': 1901, 'l': 'Revenus et patrimoine : deux concentrations'},
        {'c': '6', 'b': 1909, 'l': 'Les limites du coefficient de Gini'}],
 mots=['Lorenz', 'Gini', 'équirépartition', 'inégalités', 'patrimoine',
       'concentration', 'interdécile'],
))

# --------------------------------------------------------------- Kuznets
KZ = cloche(0.05, 0.97, 0.16, 0.86, n=15, pic=0.46)
KZR = [(0.72, 0.6577), (0.8, 0.62), (0.86, 0.68), (0.92, 0.78), (0.97, 0.88)]

L.append(fiche(
 id='kuznets',
 t='La courbe de Kuznets',
 st='Les inégalités montent puis redescendent avec le développement — à '
    'condition que l’État intervienne.',
 cat='croissance', an=1, ch=['6'],
 type='schema',
 q='Les inégalités sont-elles un phénomène transitoire du développement ou '
   'une caractéristique structurelle du capitalisme moderne ?',
 axes={'x': 'Niveau de développement', 'y': 'Niveau des inégalités'},
 depart='Une économie encore largement agricole, au tout début de son '
        'industrialisation.',
 hyp=['Simon Kuznets formule son hypothèse en 1955, à partir de l’évolution '
      'des inégalités aux États-Unis entre 1913 et 1948.',
      'L’hypothèse porte sur une trajectoire nationale de long terme, pas sur '
      'les inégalités mondiales.',
      'La relation supposée entre croissance et inégalités prend la forme '
      'd’une courbe en cloche, c’est-à-dire d’un U inversé.'],
 pente=[{'s': 'Branche montante', 'd': 'le passage d’une économie agricole à '
         'une économie industrielle creuse les écarts : les différences de '
         'productivité entre secteurs sont importantes et les salaires '
         'industriels plus élevés.'},
        {'s': 'Branche descendante', 'd': 'la généralisation de l’éducation, '
         'la diffusion du progrès technique, l’urbanisation complète et la '
         'montée de la classe moyenne réduisent les écarts — mais surtout la '
         'redistribution.'}],
 fig={'series': [
   pol('kz', 'Inégalités', KZ, 'ac', ep=3.4, lp=[0.88, 0.30]),
 ]},
 etapes=[
  etape('Phase 1 : les inégalités augmentent',
        'Au début du développement, l’économie passe de l’agriculture à '
        'l’industrie. Les différences de productivité entre secteurs sont '
        'importantes, les salaires industriels plus élevés : les écarts se '
        'creusent entre secteurs.',
        on=['kz'],
        add=[fl('f1', 'industrialisation', 0.1, 0.3, 0.36, 0.72, 'ko')],
        vif=['kz', 'f1']),
  etape('Le sommet de la cloche',
        'Les inégalités atteignent un maximum à un stade intermédiaire de '
        'développement. C’est le point de retournement de la courbe.',
        add=[pt('s', '', 0.4832, 0.86, 'ac2'),
             rep('rs', 0.4832, 0.86, c='ac2')],
        off=['f1'],
        vif=['s', 'rs']),
  etape('Phase 2 : les inégalités diminuent',
        'À un stade avancé, la généralisation de l’éducation, la diffusion du '
        'progrès technique, l’urbanisation complète et la montée de la classe '
        'moyenne resserrent les écarts.',
        add=[fl('f2', 'éducation · classe moyenne', 0.58, 0.78, 0.86, 0.36,
                'ok')],
        off=['s', 'rs'],
        vif=['f2']),
  etape('Mais surtout : la redistribution',
        'C’est le ressort décisif de la descente : développement de la '
        'redistribution, hausse des recettes fiscales, politiques sociales. '
        'L’État corrige les inégalités produites par le marché.',
        add=[txt('tr', 'l’État corrige ce que le marché produit', 0.26, 0.2,
                 'ok', taille=15, gras=True)],
        off=['f2'],
        vif=['tr']),
  etape('La limite : rien n’est automatique',
        'La baisse n’est pas mécanique. Elle dépend du niveau de '
        'redistribution, du système fiscal, des institutions et du degré de '
        'protection sociale. Les inégalités sont aussi un choix de société.',
        add=[txt('tl', 'les inégalités sont aussi un choix de société',
                 0.2, 0.95, 'jn', taille=15, gras=True)],
        off=['tr'],
        vif=['tl']),
  etape('Le démenti empirique depuis les années 1980',
        'Dans de nombreux pays développés, les inégalités de revenus '
        'remontent, les patrimoines se concentrent et le top 1 % explose. La '
        'dynamique récente contredit la phase descendante prévue par '
        'Kuznets.',
        add=[pol('kr', 'depuis les années 1980', KZR, 'ko', ep=3,
                 lp=[0.86, 0.16])],
        off=['tl'],
        vif=['kr']),
  etape('Pourquoi il faut élargir l’échelle',
        'L’analyse strictement nationale de Kuznets devient insuffisante : '
        'les transformations de l’économie mondiale appellent une lecture '
        'globale, que proposeront les travaux de Milanovic.',
        add=[txt('tm', 'passer de l’échelle nationale à l’échelle mondiale',
                 0.14, 0.95, 'bl', taille=15, gras=True)],
        vif=['tm']),
 ],
 pieges=[
  {'t': 'Kuznets 1955 n’est pas la courbe environnementale',
   'd': 'La courbe d’origine porte sur les inégalités. Sa transposition à '
        'l’environnement est une autre courbe, associée à Grossman et '
        'Krueger, avec d’autres axes et d’autres limites.'},
  {'t': 'L’hypothèse n’est pas une loi',
   'd': 'Kuznets observe une période et un pays précis — les États-Unis de '
        '1913 à 1948 — et en tire une hypothèse. En faire une loi générale du '
        'développement est exactement ce que l’évolution récente dément.'},
  {'t': 'L’abscisse n’est pas le temps',
   'd': 'C’est le niveau de développement. Deux pays au même moment peuvent '
        'se situer à des endroits très différents de la courbe.'},
 ],
 main=[
  'Trace les axes : le niveau de développement en abscisse, les inégalités en '
  'ordonnée.',
  'Trace une cloche — un U inversé — qui monte puis redescend.',
  'Annote la montée : passage de l’agriculture à l’industrie, écarts de '
  'productivité.',
  'Annote la descente : éducation, classe moyenne, et surtout redistribution.',
  'Ajoute en pointillés une remontée finale à droite pour figurer le retour '
  'des inégalités depuis les années 1980.',
 ],
 phrase='Kuznets propose en 1955 une relation en U inversé entre croissance '
        'et inégalités, celles-ci se creusant d’abord sous l’effet des écarts '
        'de productivité entre agriculture et industrie, avant de se réduire '
        'grâce à l’éducation et surtout à la redistribution ; mais la remontée '
        'des inégalités dans les pays développés depuis les années 1980 '
        'montre que cette descente n’a rien d’automatique et dépend de choix '
        'politiques.',
 liens=[{'c': '6', 'b': 1929, 'l': 'La théorie de la courbe de Kuznets'},
        {'c': '6', 'b': 1938, 'l': 'Les mécanismes explicatifs de Kuznets'},
        {'c': '6', 'b': 1957, 'l': 'Les limites de la courbe de Kuznets'},
        {'c': '6', 'b': 1979, 'l': 'Vers l’analyse mondiale de Milanovic'}],
 mots=['Kuznets', 'inégalités', 'U inversé', 'redistribution',
       'classe moyenne', 'top 1 %'],
))

# -------------------------------------------------- courbe de l'éléphant
ELE = [(0.05, 0.27), (0.1, 0.32), (0.2, 0.52), (0.3, 0.67), (0.4, 0.80),
       (0.5, 0.87), (0.55, 0.89), (0.6, 0.82), (0.7, 0.52), (0.75, 0.32),
       (0.8, 0.12), (0.85, 0.27), (0.9, 0.42), (0.95, 0.57), (0.99, 0.72)]

L.append(fiche(
 id='courbe-elephant',
 t='La courbe de l’éléphant',
 st='Qui a gagné et qui a perdu à la mondialisation, de 1988 à 2008.',
 cat='croissance', an=1, ch=['6', '21'],
 type='donnees',
 q='Pourquoi les inégalités entre pays diminuent-elles alors que les '
   'inégalités à l’intérieur des pays augmentent, et qui sont les perdants '
   'relatifs de la mondialisation ?',
 axes={'x': 'Percentile de revenu mondial', 'y': 'Croissance du revenu réel',
       'gx': [[0.05, '5'], [0.3, '30'], [0.55, '55'], [0.99, '99']],
       'gy': [[0.52, '+40 %']]},
 depart='La population mondiale entière, classée par revenu initial du plus '
        'pauvre au plus riche.',
 hyp=['En abscisse, la population mondiale classée par revenu initial ; en '
      'ordonnée, le taux de croissance du revenu réel sur la période.',
      'Les revenus sont mesurés en termes réels, déflatés, et en parité de '
      'pouvoir d’achat : les résultats ne sont donc biaisés ni par '
      'l’inflation ni par les taux de change financiers.',
      'Chaque point représente un percentile de revenu mondial, pas un pays : '
      'un même pays se retrouve réparti sur plusieurs points.'],
 pente=[{'s': 'Le dos de l’éléphant', 'd': 'la forte progression des '
         'percentiles intermédiaires, portée par la classe moyenne des pays '
         'émergents.'},
        {'s': 'Le creux de la trompe', 'd': 'la stagnation autour du 80ᵉ '
         'percentile, qui correspond aux classes moyennes occidentales.'},
        {'s': 'Le bout de la trompe', 'd': 'la forte remontée au sommet, qui '
         'correspond au top 1 % mondial.'}],
 src={'so': 'Cours de première année, chapitre 6 — courbe de l’éléphant de '
            'Branko Milanovic, Global Inequality, 2016, telle que le cours la '
            'commente (points A, B, C et stagnation du 80ᵉ percentile).',
      'pe': '1988 — 2008',
      'un': 'croissance cumulée du revenu réel en %, en parité de pouvoir '
            'd’achat ; abscisse en percentiles de revenu mondial',
      'nb': 'Le cours chiffre quatre repères : environ +15 % pour les plus '
            'pauvres, +70 à +80 % pour la classe moyenne émergente, une '
            'croissance proche de 0 % autour du 80ᵉ percentile et environ '
            '+60 % pour le top 1 %. Le tracé entre ces repères est une '
            'allure, non une série de données.'},
 fig={'series': [
   pol('ele', '', ELE, 'ac', ep=3.4),
   lin('z', '', 0.0, 0.12, 1.0, 0.12, 'gr', ep=1.6),
 ]},
 etapes=[
  etape('D’abord, comprendre les axes',
        'L’abscisse n’est pas le temps mais la position dans la distribution '
        'mondiale des revenus. L’ordonnée n’est pas un niveau de revenu mais '
        'un taux de croissance. Sans cela, la courbe est illisible.',
        on=['ele', 'z'], vif=['ele']),
  etape('Point A — les plus pauvres du monde',
        'Leur revenu réel progresse d’environ 15 % sur vingt ans : une '
        'amélioration limitée. Les plus pauvres bénéficient peu de la '
        'mondialisation.',
        add=[pt('a', 'A', 0.05, 0.27, 'ac2'),
             rep('ra', 0.05, 0.27, ly='+15 %', c='ac2')],
        vif=['a', 'ra']),
  etape('Point B — la classe moyenne des pays émergents',
        'Croissance très forte, de 70 à 80 %, essentiellement en Chine, en '
        'Inde et en Asie. Ce sont les grands gagnants de la mondialisation, '
        'et c’est ce qui explique la réduction des inégalités entre pays.',
        add=[pt('b', 'B', 0.55, 0.89, 'ok'),
             rep('rb', 0.55, 0.89, ly='≈ +75 %', c='ok')],
        vif=['b', 'rb']),
  etape('Le creux — les classes moyennes occidentales',
        'Situées autour du 80ᵉ percentile mondial, elles connaissent une '
        'croissance réelle proche de zéro. D’où un sentiment de '
        'déclassement, qui éclaire la montée des tensions sociales et '
        'politiques.',
        add=[pt('c', '', 0.8, 0.12, 'ko'),
             rep('rc', 0.8, 0.12, lx='80ᵉ', ly='≈ 0 %', c='ko'),
             txt('tc', 'perdants relatifs', 0.64, 0.22, 'ko', taille=14,
                 gras=True)],
        vif=['c', 'rc', 'tc']),
  etape('Point C — le top 1 % mondial',
        'Forte hausse des revenus, environ 60 %. Les gains se concentrent au '
        'sommet : environ la moitié de cette élite est américaine, et '
        'Milanovic parle d’une ploutocratie mondiale.',
        add=[pt('d', 'C', 0.99, 0.72, 'jn'),
             rep('rd', 0.99, 0.72, ly='≈ +60 %', c='jn')],
        off=['tc'],
        vif=['d', 'rd']),
  etape('Gains relatifs et gains absolus',
        'En pourcentage, la classe moyenne émergente progresse plus vite que '
        'le sommet. Mais en valeur absolue, le top 1 % capte la plus grande '
        'part du surplus mondial : la mondialisation enrichit massivement le '
        'sommet.',
        add=[txt('tg', 'en %, B gagne le plus · en valeur, C capte le plus',
                 0.08, 0.96, 'jn', taille=15, gras=True)],
        vif=['tg']),
  etape('Le paradoxe que la courbe résume',
        'Les inégalités entre pays diminuent — convergence des émergents — '
        'tandis que les inégalités à l’intérieur des pays augmentent — '
        'divergence au sein des sociétés nationales. Un seul graphique porte '
        'les deux mouvements.',
        add=[txt('tp', 'entre pays : convergence · dans les pays : divergence',
                 0.06, 0.96, 'bl', taille=15, gras=True)],
        off=['tg'],
        vif=['tp']),
  etape('Ce que la courbe ne montre pas : la rente de citoyenneté',
        'Pour Milanovic, l’inégalité majeure aujourd’hui provient du lieu de '
        'naissance : naître dans un pays riche procure un revenu '
        'structurellement plus élevé et un avantage durable. La nationalité '
        'devient un facteur central d’inégalité mondiale.',
        off=['tp'],
        vif=['ele']),
 ],
 pieges=[
  {'t': 'L’abscisse n’est pas une chronologie',
   'd': 'Lire la courbe de gauche à droite comme une évolution dans le temps '
        'est le contresens le plus fréquent. On parcourt la distribution '
        'mondiale des revenus, du plus pauvre au plus riche, à période fixée.'},
  {'t': 'Un percentile n’est pas un pays',
   'd': 'Le 80ᵉ percentile mondial regroupe des individus de nombreux pays. '
        'Dire « le 80ᵉ percentile, c’est la France » est faux, même si les '
        'classes moyennes occidentales y sont surreprésentées.'},
  {'t': 'Perdants relatifs, pas perdants absolus',
   'd': 'Une croissance proche de zéro ne signifie pas un appauvrissement, '
        'mais une stagnation pendant que d’autres progressent fortement. '
        'C’est précisément ce décalage qui nourrit le sentiment de '
        'déclassement.'},
 ],
 main=[
  'Trace les axes : les percentiles de revenu mondial en abscisse, la '
  'croissance du revenu réel en ordonnée — et marque le zéro.',
  'Place le point A tout à gauche, un peu au-dessus de zéro : environ +15 %.',
  'Monte jusqu’au dos de l’éléphant vers le 50ᵉ-55ᵉ percentile : +70 à +80 %.',
  'Redescends jusqu’au creux au 80ᵉ percentile, exactement sur le zéro.',
  'Remonte jusqu’au bout de la trompe au 99ᵉ percentile, vers +60 %, et nomme '
  'les quatre repères.',
 ],
 phrase='La courbe de l’éléphant de Branko Milanovic montre que, de 1988 à '
        '2008, la classe moyenne des pays émergents a vu son revenu réel '
        'progresser de 70 à 80 % tandis que les classes moyennes '
        'occidentales, situées autour du 80ᵉ percentile mondial, '
        'connaissaient une croissance quasi nulle et que le top 1 % gagnait '
        'environ 60 % : les inégalités entre pays se réduisent donc au moment '
        'même où celles qui existent à l’intérieur des pays se creusent.',
 liens=[{'c': '6', 'b': 1987, 'l': 'La courbe de l’éléphant (1988-2008)'},
        {'c': '6', 'b': 1997, 'l': 'Lecture des points A, B et C'},
        {'c': '6', 'b': 2013, 'l': 'La stagnation des classes moyennes occidentales'},
        {'c': '6', 'b': 2018, 'l': 'Gains relatifs et gains absolus'},
        {'c': '6', 'b': 2026, 'l': 'La rente de citoyenneté'},
        {'c': '21', 'b': 1614, 'l': 'Mondialisation, inégalités et courbe de l’éléphant (ch. 1 de 2ᵉ année)'}],
 mots=['Milanovic', 'éléphant', 'mondialisation', 'classe moyenne',
       'top 1 %', 'déclassement', 'rente de citoyenneté'],
))

# ---------------------------------------- courbe environnementale de Kuznets
EKC = cloche(0.05, 0.97, 0.14, 0.84, n=15, pic=0.44)
CO2 = [(0.05, 0.14), (0.2, 0.28), (0.35, 0.42), (0.5, 0.56), (0.65, 0.69),
       (0.8, 0.8), (0.95, 0.9)]

L.append(fiche(
 id='kuznets-environnementale',
 t='La courbe environnementale de Kuznets',
 st='« Polluer d’abord, dépolluer ensuite » : une idée séduisante et très '
    'discutée.',
 cat='croissance', an=1, ch=['6', '22'],
 type='schema',
 q='La croissance finit-elle par protéger l’environnement qu’elle a d’abord '
   'dégradé, et pour quelles pollutions cette thèse tient-elle ?',
 axes={'x': 'Revenu par tête', 'y': 'Dégradation de l’environnement'},
 depart='Un pays à faible revenu, au début de son industrialisation.',
 hyp=['La transposition de la courbe de Kuznets à l’environnement est '
      'associée à Grossman et Krueger, Quarterly Journal of Economics, 1995.',
      'À faible revenu, la priorité va à la croissance ; lorsque le revenu '
      'augmente, les préoccupations environnementales augmentent et la '
      'demande de réglementation avec elles.',
      'La thèse est très proche de la soutenabilité faible : on peut croître, '
      'polluer d’abord, puis dépolluer grâce à la richesse, à la technologie '
      'et à la régulation.'],
 pente=[{'s': 'Branche montante', 'd': 'l’industrialisation accroît la '
         'pollution, et la priorité politique va à la croissance plutôt qu’à '
         'l’environnement.'},
        {'s': 'Branche descendante', 'd': 'une fois riche, la société exige '
         'des normes, finance des technologies propres et déplace sa '
         'production vers les services.'}],
 fig={'series': [
   pol('ekc', 'Pollution', EKC, 'ac', ep=3.4, lp=[0.90, 0.34]),
 ]},
 etapes=[
  etape('À faible revenu, la priorité va à la croissance',
        'Un pays pauvre qui s’industrialise accroît ses pollutions. '
        'L’environnement n’est pas une priorité politique : les '
        'préoccupations immédiates sont ailleurs.',
        on=['ekc'],
        add=[fl('f1', 'industrialisation', 0.1, 0.28, 0.34, 0.7, 'ko')],
        vif=['ekc', 'f1']),
  etape('Le point de retournement',
        'Au-delà d’un certain niveau de revenu, la dégradation cesse '
        'd’augmenter. C’est le sommet de la courbe, le moment où les normes '
        'commencent à mordre.',
        add=[pt('s', '', 0.4548, 0.84, 'ac2'),
             rep('rs', 0.4548, 0.84, c='ac2')],
        off=['f1'],
        vif=['s', 'rs']),
  etape('À revenu élevé, la demande de réglementation augmente',
        'Lorsque le revenu s’élève, les préoccupations environnementales '
        'montent et la demande de réglementation avec elles. La pollution '
        'mesurée sur le territoire recule.',
        add=[fl('f2', 'normes · technologies propres', 0.58, 0.74, 0.88, 0.32,
                'ok')],
        off=['s', 'rs'],
        vif=['f2']),
  etape('Pour quelles pollutions cela semble fonctionner',
        'La courbe paraît valide pour certaines pollutions locales : dioxyde '
        'de soufre, pollution de l’air localisée, certains rejets '
        'industriels. Ce sont des pollutions visibles, mesurables et dont les '
        'effets sont immédiats.',
        add=[txt('tl', 'pollutions locales : SO₂, air, rejets industriels',
                 0.3, 0.2, 'ok', taille=14, gras=True)],
        off=['f2'],
        vif=['tl']),
  etape('Mais pas pour celles qui comptent le plus',
        'Elle fonctionne beaucoup moins bien pour le CO₂, les gaz à effet de '
        'serre, les déchets, les atteintes à la biodiversité et l’épuisement '
        'des ressources — or ce sont précisément les pollutions les plus '
        'décisives aujourd’hui.',
        add=[pol('co2', 'CO₂ et pollutions globales', CO2, 'ko', ep=3,
                 lp=[0.84, 0.97])],
        off=['tl'],
        vif=['co2']),
  etape('Le problème de l’externalisation',
        'Un pays riche peut sembler moins polluer sur son territoire alors '
        'qu’il importe des biens produits ailleurs et délocalise ses '
        'activités polluantes : il « exporte » sa pollution. La baisse '
        'nationale ne signifie pas une baisse de l’empreinte réelle.',
        add=[txt('tx', 'baisse nationale ≠ baisse de l’empreinte réelle',
                 0.12, 0.95, 'jn', taille=15, gras=True)],
        vif=['tx']),
  etape('La critique de la soutenabilité forte',
        'Certaines destructions sont irréversibles, certaines ressources '
        'épuisables, le climat fonctionne par seuils et effets cumulatifs, et '
        'le temps écologique n’est pas le temps économique. On ne peut donc '
        'pas raisonner en « polluons d’abord ».',
        add=[txt('ts', 'irréversibilité · seuils · temps écologique',
                 0.16, 0.88, 'bl', taille=15, gras=True)],
        off=['tx'],
        vif=['ts']),
 ],
 pieges=[
  {'t': 'Un outil de réflexion, pas une loi générale',
   'd': 'Le cours est explicite : la courbe est utile pour penser, mais ne '
        'doit surtout pas être prise comme une loi. La présenter comme '
        'validée est la faute la plus coûteuse sur ce sujet.'},
  {'t': 'L’abscisse est le revenu, pas le temps',
   'd': 'Comme pour la courbe de Kuznets originelle, on compare des niveaux '
        'de développement. Un pays peut rester des décennies au même endroit '
        'de la courbe.'},
  {'t': 'Soutenabilité faible et soutenabilité forte',
   'd': 'La courbe épouse la soutenabilité faible, pour laquelle le capital '
        'produit peut remplacer le capital naturel. La soutenabilité forte le '
        'conteste au nom de l’irréversibilité : c’est le vrai débat de fond.'},
 ],
 main=[
  'Trace les axes : le revenu par tête en abscisse, la dégradation '
  'environnementale en ordonnée.',
  'Trace une cloche, comme la courbe de Kuznets originelle.',
  'Annote la montée — industrialisation — et la descente — normes, '
  'technologies propres.',
  'Ajoute une seconde courbe qui, elle, ne redescend pas : le CO₂ et les '
  'pollutions globales.',
  'Écris en marge les deux critiques : externalisation de la pollution et '
  'irréversibilité.',
 ],
 phrase='Transposée à l’environnement par Grossman et Krueger, la courbe de '
        'Kuznets suppose que la croissance dégrade d’abord l’environnement '
        'puis finit par créer les conditions de sa protection ; mais cette '
        'thèse, proche de la soutenabilité faible, ne vaut que pour certaines '
        'pollutions locales, ignore l’externalisation des activités polluantes '
        'et se heurte à l’irréversibilité des destructions que souligne la '
        'soutenabilité forte.',
 liens=[{'c': '6', 'b': 3027, 'l': 'La courbe environnementale de Kuznets'},
        {'c': '6', 'b': 3056, 'l': 'Les limites de la courbe environnementale'},
        {'c': '6', 'b': 3072, 'l': 'Le problème de l’externalisation'},
        {'c': '22', 'b': 1467, 'l': 'Normes environnementales et niveau de développement'}],
 mots=['Kuznets environnementale', 'Grossman', 'Krueger',
       'soutenabilité faible', 'soutenabilité forte', 'externalisation',
       'CO₂'],
))

# ------------------------------------------------ transition démographique
NAT = [(0.03, 0.82), (0.14, 0.82), (0.26, 0.81), (0.36, 0.78), (0.46, 0.68),
       (0.56, 0.54), (0.66, 0.40), (0.76, 0.28), (0.86, 0.22), (0.97, 0.20)]
MOR = [(0.03, 0.78), (0.12, 0.79), (0.2, 0.74), (0.28, 0.62), (0.36, 0.48),
       (0.46, 0.34), (0.56, 0.24), (0.66, 0.18), (0.76, 0.16), (0.86, 0.17),
       (0.97, 0.19)]

L.append(fiche(
 id='transition-demographique',
 t='La transition démographique',
 st='La mortalité baisse d’abord, la natalité suit avec retard — et entre les '
    'deux, l’explosion démographique.',
 cat='croissance', an=1, ch=['7'],
 type='schema',
 q='Pourquoi le passage d’un régime démographique ancien à un régime moderne '
   'provoque-t-il temporairement une forte hausse de la population ?',
 axes={'x': 'Temps', 'y': 'Taux de natalité et de mortalité'},
 depart='Une société au régime démographique ancien, avant tout recul de la '
        'mortalité.',
 hyp=['La transition démographique est le passage d’un régime de forte '
      'natalité et forte mortalité à un régime de faible natalité et faible '
      'mortalité.',
      'Adolphe Landry formalise ce modèle dans La Révolution démographique '
      '(1934) : les sociétés passent d’un régime ancien à un régime moderne, '
      'avec transformation des comportements de fécondité.',
      'La chronologie est précise et constitue le cœur du modèle : la '
      'mortalité baisse d’abord, la natalité suit avec retard.'],
 pente=[{'s': 'Mortalité', 'd': 'elle décroche la première, sous l’effet des '
         'progrès sanitaires et alimentaires, puis se stabilise bas.'},
        {'s': 'Natalité', 'd': 'elle reste élevée un certain temps avant de '
         'baisser à son tour : les comportements de fécondité mettent une '
         'génération à se transformer.'},
        {'s': 'L’écart entre les deux', 'd': 'c’est l’accroissement naturel. '
         'Il est faible au départ, maximal pendant la transition, faible à '
         'nouveau à la fin.'}],
 fig={'series': [
   pol('nat', 'Natalité', NAT, 'ac2', ep=3.2, lp=[0.62, 0.95]),
   pol('mor', 'Mortalité', MOR, 'ok', ep=3.2, lp=[0.14, 0.62]),
 ]},
 etapes=[
  etape('Le régime démographique ancien',
        'Natalité élevée, mortalité élevée : les deux courbes sont proches et '
        'hautes. L’accroissement naturel est faible et la population augmente '
        'peu.',
        on=['nat', 'mor'],
        add=[txt('t1', 'régime ancien', 0.04, 0.06, 'gr', taille=14,
                 gras=True)],
        vif=['nat', 'mor', 't1']),
  etape('La mortalité baisse d’abord',
        'Progrès sanitaires, alimentaires et médicaux : la mortalité décroche '
        'la première. C’est le point de départ de la transition, et l’ordre '
        'des deux baisses est le cœur du modèle de Landry.',
        add=[fl('fm', 'la mortalité décroche', 0.2, 0.56, 0.42, 0.4, 'ok')],
        vif=['fm', 'mor']),
  etape('Mais la natalité reste élevée un certain temps',
        'Les comportements de fécondité ne se transforment pas '
        'instantanément. Pendant plusieurs décennies, on continue d’avoir '
        'autant d’enfants alors qu’on meurt beaucoup moins.',
        add=[fl('fn', 'la natalité résiste', 0.2, 0.9, 0.4, 0.9, 'ac2')],
        off=['fm'],
        vif=['fn', 'nat']),
  etape('L’écart se creuse : l’explosion démographique',
        'Entre les deux courbes, l’accroissement naturel devient très fort. '
        'C’est la phase de transition, qui donne l’impression d’une explosion '
        'démographique.',
        add=[zone('acc', 'accroissement naturel',
                  [(0.26, 0.81), (0.36, 0.78), (0.46, 0.68), (0.56, 0.54),
                   (0.66, 0.40), (0.66, 0.18), (0.56, 0.24), (0.46, 0.34),
                   (0.36, 0.48), (0.28, 0.62), (0.26, 0.74)], 'jn')],
        off=['fn'],
        vif=['acc']),
  etape('La natalité baisse à son tour',
        'Le développement finit par transformer les comportements : la '
        'natalité rejoint la mortalité et l’accroissement naturel se réduit. '
        'C’est l’entrée dans le régime démographique moderne.',
        add=[txt('t2', 'régime moderne', 0.78, 0.06, 'gr', taille=14,
                 gras=True)],
        off=['acc'],
        vif=['nat', 't2']),
  etape('Pourquoi le développement fait baisser la fécondité',
        'La mortalité infantile recule — on n’a plus besoin de « beaucoup '
        'd’enfants pour en garder quelques-uns » ; le niveau de vie monte et '
        'on arbitre vers moins d’enfants mais davantage investis ; '
        'l’éducation, surtout féminine, l’urbanisation, la contraception et '
        'la protection sociale font le reste.',
        add=[txt('t3', 'moins d’enfants, davantage investis', 0.4, 0.06,
                 'bl', taille=14, gras=True)],
        vif=['t3']),
  etape('Le résultat final : stabilisation et vieillissement',
        'Les deux courbes sont désormais basses et proches. La croissance '
        'démographique ralentit, la population se stabilise, et la structure '
        'par âge se transforme : c’est le vieillissement progressif.',
        add=[txt('t4', 'stabilisation · vieillissement', 0.52, 0.32, 'ac',
                 taille=15, gras=True)],
        off=['t3'],
        vif=['t4']),
  etape('Les limites du modèle',
        'Le cadre est éclairant mais ne s’applique ni partout ni au même '
        'rythme : les trajectoires historiques sont diverses, et le modèle a '
        'été critiqué pour son eurocentrisme. Le cas français, où la natalité '
        'baisse très tôt, en est l’exception la plus connue.',
        add=[txt('t5', 'modèle utile, non universel', 0.2, 0.95, 'jn',
                 taille=15, gras=True)],
        off=['t4'],
        vif=['t5']),
 ],
 pieges=[
  {'t': 'L’ordre des deux baisses est tout le modèle',
   'd': 'Si la natalité baissait d’abord, il n’y aurait aucune explosion '
        'démographique. Inverser les deux courbes rend le phénomène '
        'inexplicable.'},
  {'t': 'L’accroissement naturel est un écart, pas une courbe',
   'd': 'Il ne se trace pas : il se lit entre les deux courbes. Chercher une '
        'troisième courbe sur le graphique est une erreur de lecture '
        'fréquente.'},
  {'t': 'La France est l’exception, pas la règle',
   'd': 'Le modèle a été critiqué pour son eurocentrisme, et la France '
        'elle-même ne le suit pas : sa natalité baisse précocement, bien '
        'avant le schéma standard.'},
 ],
 main=[
  'Trace les axes : le temps en abscisse, les taux de natalité et de '
  'mortalité en ordonnée.',
  'Trace deux courbes hautes et proches à gauche : le régime ancien.',
  'Fais décrocher d’abord la mortalité, puis, plus tard, la natalité.',
  'Hachure l’espace entre les deux courbes pendant la phase de décalage : '
  'c’est l’accroissement naturel.',
  'Termine par deux courbes basses et proches à droite, et écris '
  '« stabilisation, vieillissement ».',
 ],
 phrase='La transition démographique, théorisée par Adolphe Landry dans La '
        'Révolution démographique en 1934, désigne le passage d’un régime de '
        'forte natalité et forte mortalité à un régime où les deux sont '
        'faibles ; comme la mortalité baisse avant la natalité, l’écart entre '
        'les deux courbes — l’accroissement naturel — se creuse '
        'temporairement, ce qui explique l’impression d’explosion '
        'démographique propre à la phase de transition.',
 liens=[{'c': '7', 'b': 1148, 'l': 'La transition démographique : le modèle central'},
        {'c': '7', 'b': 1156, 'l': 'Adolphe Landry, La Révolution démographique'},
        {'c': '7', 'b': 1165, 'l': 'Les grandes phases de la transition'},
        {'c': '7', 'b': 1186, 'l': 'Pourquoi le développement fait baisser la fécondité'},
        {'c': '7', 'b': 1208, 'l': 'Les limites du modèle et le cas français'}],
 mots=['transition démographique', 'Landry', 'natalité', 'mortalité',
       'accroissement naturel', 'fécondité', 'vieillissement'],
))

# ------------------------------------------------------ vol d'oies sauvages
def _oie(decal, haut):
    return cloche(0.02 + decal, 0.62 + decal, 0.04, haut, n=13, pic=0.5)


L.append(fiche(
 id='vol-oies-sauvages',
 t='Le vol d’oies sauvages',
 st='Un rattrapage industriel séquencé : importer, produire, exporter, puis '
    'passer la main.',
 cat='croissance', an=1, ch=['7'],
 type='schema',
 q='Comment un pays peut-il rattraper son retard industriel en se '
   'repositionnant successivement sur des productions plus sophistiquées ?',
 axes={'x': 'Temps', 'y': 'Niveau de production industrielle'},
 depart='Une région où un pays leader a commencé son industrialisation avant '
        'les autres.',
 hyp=['Le modèle du vol d’oies sauvages, ou Flying Geese Paradigm, décrit un '
      'processus de rattrapage industriel séquencé.',
      'La séquence pour un même bien est toujours la même : un pays commence '
      'par importer, puis produit, puis exporte, avant de se repositionner '
      'sur des productions plus sophistiquées.',
      'Les activités les plus simples sont alors laissées aux pays suivants '
      'de la formation : le modèle est hiérarchisé et régional.'],
 pente=[{'s': 'Chaque cloche', 'd': 'la montée correspond à la phase où le '
         'pays produit puis exporte le bien ; la descente, au moment où il '
         'abandonne cette production pour monter en gamme.'},
        {'s': 'Le décalage entre les cloches', 'd': 'c’est le rattrapage : '
         'chaque pays reprend la production que le précédent délaisse, avec '
         'un retard régulier.'}],
 fig={'series': [
   pol('p1', 'Pays leader', _oie(0.0, 0.84), 'ac', ep=3.2, lp=[0.22, 0.95]),
 ]},
 etapes=[
  etape('Le pays leader ouvre la marche',
        'Le premier pays industrialise une production donnée : il la fabrique '
        'puis l’exporte massivement. Sa production monte, atteint un sommet, '
        'puis décline.',
        on=['p1'], vif=['p1']),
  etape('La séquence pour un même bien',
        'Pour chaque produit, le pays suit toujours le même enchaînement : '
        'il importe d’abord, puis il produit lui-même, puis il exporte. La '
        'cloche retrace cet enchaînement dans le temps.',
        add=[txt('ts', 'importer → produire → exporter', 0.08, 0.5, 'ac',
                 taille=15, gras=True)],
        vif=['ts']),
  etape('Le repositionnement vers le haut de gamme',
        'Lorsque les salaires montent, le leader abandonne les productions '
        'les plus simples et se repositionne sur des biens plus '
        'sophistiqués : sa cloche redescend sur ce produit, mais une autre '
        'monte ailleurs.',
        add=[fl('fr', 'montée en gamme', 0.4, 0.46, 0.56, 0.62, 'ac')],
        off=['ts'],
        vif=['fr']),
  etape('Le deuxième rang reprend la production délaissée',
        'Le pays suivant hérite de la production que le leader abandonne. Sa '
        'cloche est décalée vers la droite : c’est exactement le rattrapage.',
        add=[pol('p2', 'Deuxième rang', _oie(0.12, 0.72), 'ok', ep=3,
                 lp=[0.44, 0.95])],
        off=['fr'],
        vif=['p2']),
  etape('Et ainsi de suite, en formation',
        'Le troisième rang, puis le quatrième, reprennent à leur tour. Les '
        'cloches successives dessinent une formation en V, comme un vol '
        'd’oies sauvages — d’où le nom du modèle.',
        add=[pol('p3', 'Troisième rang', _oie(0.24, 0.6), 'ac2', ep=3,
                 lp=[0.66, 0.95]),
             pol('p4', 'Quatrième rang', _oie(0.36, 0.48), 'bl', ep=3,
                 lp=[0.88, 0.95])],
        vif=['p3', 'p4']),
  etape('Un modèle hiérarchisé et régional',
        'Le rattrapage ne se fait pas isolément mais à l’intérieur d’une '
        'région organisée autour d’un leader. Les investissements, les '
        'technologies et les commandes circulent du haut vers le bas de la '
        'formation.',
        add=[fl('fh', 'transmission régionale', 0.2, 0.2, 0.74, 0.2, 'jn')],
        vif=['fh']),
  etape('Ce que le modèle combine',
        'Il est important parce qu’il combine plusieurs stratégies de '
        'développement au lieu de les opposer : substitution aux importations '
        'd’abord, promotion des exportations ensuite, pour chaque produit et '
        'pour chaque rang.',
        add=[txt('tc', 'substitution puis promotion des exportations',
                 0.14, 0.32, 'jn', taille=15, gras=True)],
        off=['fh'],
        vif=['tc']),
 ],
 pieges=[
  {'t': 'Les cloches ne sont pas des pays qui déclinent',
   'd': 'Quand la courbe d’un pays redescend sur un produit, ce n’est pas un '
        'appauvrissement : il a monté en gamme. Sa production totale '
        'continue d’augmenter, sur d’autres biens.'},
  {'t': 'Une séquence par produit, pas une trajectoire unique',
   'd': 'Le modèle se lit produit par produit. Un même pays peut être en '
        'phase d’importation sur un bien et en phase d’exportation sur un '
        'autre.'},
  {'t': 'Ce n’est pas une opposition de stratégies',
   'd': 'Le modèle articule substitution aux importations et promotion des '
        'exportations, alors que les manuels les présentent souvent comme '
        'deux voies concurrentes. C’est précisément ce qui en fait l’intérêt.'},
 ],
 main=[
  'Trace les axes : le temps en abscisse, le niveau de production '
  'industrielle en ordonnée.',
  'Trace une première cloche à gauche : le pays leader.',
  'Trace une deuxième cloche décalée vers la droite et un peu plus basse.',
  'Ajoute une troisième et une quatrième, chacune décalée et plus basse : la '
  'formation en V apparaît.',
  'Écris sous le graphique la séquence commune : importer, produire, '
  'exporter, puis monter en gamme.',
 ],
 phrase='Le modèle du vol d’oies sauvages décrit un processus de rattrapage '
        'industriel séquencé, dans lequel un pays commence par importer un '
        'bien, puis le produit, puis l’exporte, avant de se repositionner sur '
        'des productions plus sophistiquées en laissant les activités les '
        'plus simples aux pays suivants : le rattrapage est ainsi '
        'hiérarchisé, régional, et combine substitution aux importations et '
        'promotion des exportations au lieu de les opposer.',
 liens=[{'c': '7', 'b': 2746, 'l': 'La stratégie de développement en vol d’oies sauvages'},
        {'c': '7', 'b': 2752, 'l': 'L’origine du modèle'},
        {'c': '7', 'b': 2766, 'l': 'Le processus de rattrapage séquencé'},
        {'c': '7', 'b': 2821, 'l': 'Pourquoi le modèle combine plusieurs stratégies'}],
 mots=['vol d’oies sauvages', 'Flying Geese', 'rattrapage',
       'montée en gamme', 'substitution aux importations',
       'promotion des exportations'],
))
