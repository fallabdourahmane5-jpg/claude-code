# -*- coding: utf-8 -*-
"""Courbes du chapitre 4 — le producteur, les coûts, l'équilibre de marché."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     hyper, courbe_dec, courbe_cro, inter, y_de, x_de, bouge)

L = []

# -------------------------------------------------- isoquantes et isocoût
Q1 = [p for p in hyper(0.1898, 0.20, 0.97, 17) if p[1] <= 1.05]
Q0 = [p for p in hyper(0.11, 0.115, 0.97, 17) if p[1] <= 1.05]
Q2 = [p for p in hyper(0.30, 0.305, 0.97, 17) if p[1] <= 1.05]
IC = (0.07, 0.90, 0.72, 0.06)

L.append(fiche(
 id='isoquante-isocout',
 t='Isoquantes et droite d’isocoût',
 st='Le programme du producteur : produire au moindre coût en combinant '
    'travail et capital.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Comment un producteur choisit-il la combinaison de travail et de capital '
   'qui lui permet de produire un niveau donné au coût le plus faible ?',
 axes={'x': 'Travail L', 'y': 'Capital K'},
 depart='Un producteur qui doit choisir sa combinaison de facteurs, avec des '
        'prix de facteurs donnés : le salaire w et le coût du capital r.',
 hyp=['On raisonne à long terme : les deux facteurs sont variables. À court '
      'terme, au moins un facteur est fixe — en général le capital.',
      'Pour les néoclassiques, le temps n’est pas chronologique mais logique : '
      'le court terme est défini par la fixité d’au moins un facteur, non par '
      'une durée.',
      'La substituabilité entre capital et travail est imparfaite : il '
      'n’existe pas, dans ce cadre théorique, de machine capable de remplacer '
      'parfaitement un travailleur.'],
 pente=[{'s': 'Isoquante', 'd': 'décroissante et convexe : utiliser moins de '
         'capital oblige à employer plus de travail pour produire autant. Sa '
         'pente est le taux marginal de substitution technique, négatif.'},
        {'s': 'Droite d’isocoût', 'd': 'décroissante, de pente égale à '
         'l’opposé du rapport des prix des facteurs : elle réunit toutes les '
         'combinaisons de K et de L ayant le même coût total.'},
        {'s': 'TMST décroissant', 'd': 'plus on utilise de travail, moins '
         'chaque unité supplémentaire permet de remplacer de capital, parce '
         'que les facteurs ne sont pas parfaitement substituables.'}],
 fig={'series': [
   pol('q1', 'Q₁', Q1, 'ac', ep=3),
 ]},
 etapes=[
  etape('Une isoquante : un niveau de production',
        'Elle réunit toutes les combinaisons de travail et de capital '
        'permettant d’obtenir le même niveau de production. Beaucoup de '
        'capital et peu de travail, ou l’inverse : le résultat produit est '
        'identique.',
        on=['q1'],
        add=[pt('a', 'A', 0.22, round(0.1898 / 0.22, 4), 'ac2'),
             pt('b', 'B', 0.6, round(0.1898 / 0.6, 4), 'ac2'),
             txt('tq', 'même production', 0.34, 0.6, 'ac2', taille=14)],
        vif=['q1', 'a', 'b', 'tq']),
  etape('Le taux marginal de substitution technique',
        'La pente de l’isoquante mesure la quantité de capital à laquelle le '
        'producteur peut renoncer s’il emploie une unité de travail de plus, '
        'sans changer sa production. Elle est négative : c’est un arbitrage.',
        add=[fl('ft', 'TMST < 0', 0.24, 0.62, 0.4, 0.4, 'jn')],
        off=['tq'],
        vif=['ft']),
  etape('Le TMST égale le rapport des productivités marginales',
        'Le producteur compare ce que rapporte une unité de travail '
        'supplémentaire à ce que rapporte une unité de capital '
        'supplémentaire : le TMST est le rapport des productivités '
        'marginales des deux facteurs.',
        add=[txt('tpm', 'TMST = Pm(L) / Pm(K)', 0.42, 0.9, 'jn', taille=15,
                 gras=True)],
        vif=['tpm']),
  etape('Les autres niveaux de production',
        'À chaque niveau de production correspond une isoquante. Elles ne se '
        'croisent jamais : sinon une même combinaison de facteurs donnerait '
        'deux productions différentes, ce qui serait illogique.',
        add=[pol('q0', 'Q₀', Q0, 'gr', ep=2.2),
             pol('q2', 'Q₂', Q2, 'ok', ep=2.4),
             fl('fq', 'production croissante', 0.28, 0.3, 0.6, 0.62, 'ok')],
        off=['ft', 'tpm', 'a', 'b'],
        vif=['q0', 'q2', 'fq']),
  etape('La droite d’isocoût',
        'Le travail coûte un salaire w, le capital un prix r. La droite '
        'd’isocoût réunit toutes les combinaisons de facteurs ayant le même '
        'coût total ; sa pente est l’opposé du rapport de ces deux prix.',
        add=[lin('ic', 'Isocoût', *IC, c='ac2', ep=3, lp=[0.74, 0.16])],
        off=['fq'],
        vif=['ic']),
  etape('L’optimum du producteur',
        'Le producteur choisit le point de tangence entre la droite d’isocoût '
        'et l’isoquante la plus élevée qu’il peut atteindre : Q₂ est hors de '
        'portée, Q₀ serait produite à un coût inutilement élevé.',
        add=[pt('e', 'E', 0.3832, 0.4953, 'ok'),
             rep('re', 0.3832, 0.4953, lx='L*', ly='K*', c='ok')],
        vif=['e', 're', 'q1', 'ic']),
  etape('Un choc sur le prix d’un facteur',
        'Une hausse des cotisations sociales renchérit le travail : la droite '
        'd’isocoût devient plus raide et le producteur remplace du travail '
        'par du capital. C’est un effet de substitution technique — et son '
        'budget réel diminue aussi.',
        add=[lin('ic2', 'Isocoût après hausse de w', 0.07, 0.9, 0.47, 0.06,
                 'ko', ep=2.6, lp=[0.30, 0.02]),
             fl('fw', 'w ↑ : K remplace L', 0.5, 0.2, 0.32, 0.3, 'ko')],
        vif=['ic2', 'fw']),
 ],
 pieges=[
  {'t': 'Isoquante n’est pas isocoût',
   'd': 'L’isoquante est une courbe : elle décrit une technique, un niveau de '
        'production. L’isocoût est une droite : elle décrit une dépense. '
        'C’est leur rencontre qui donne la décision.'},
  {'t': 'Rendements factoriels et rendements d’échelle',
   'd': 'Les rendements factoriels relèvent du court terme : un seul facteur '
        'varie, et la productivité marginale finit par décroître. Les '
        'rendements d’échelle relèvent du long terme : tous les facteurs '
        'varient dans les mêmes proportions, à intensité capitalistique '
        'constante.'},
  {'t': 'Le parallèle avec le consommateur n’est pas une identité',
   'd': 'Le raisonnement est le même — tangence entre une courbe et une '
        'droite — mais le producteur ne maximise pas une utilité : il cherche '
        'à produire un niveau donné au moindre coût.'},
 ],
 main=[
  'Trace les axes : le travail L en abscisse, le capital K en ordonnée.',
  'Trace une isoquante décroissante et convexe, puis une plus basse et une '
  'plus haute.',
  'Trace la droite d’isocoût et cherche l’isoquante la plus élevée qu’elle '
  'touche sans la couper.',
  'Marque le point de tangence E et projette-le sur les deux axes.',
  'Redessine une droite d’isocoût plus raide pour figurer une hausse du coût '
  'du travail, et marque la substitution du capital au travail.',
 ],
 phrase='Le programme du producteur consiste à atteindre un niveau de '
        'production donné au moindre coût : l’optimum se situe au point de '
        'tangence entre la droite d’isocoût et l’isoquante la plus élevée '
        'accessible, c’est-à-dire là où le taux marginal de substitution '
        'technique — rapport des productivités marginales des facteurs — '
        'égale le rapport de leurs prix.',
 liens=[{'c': '4', 'b': 383, 'l': 'L’isoquante, équivalent de la courbe d’indifférence'},
        {'c': '4', 'b': 405, 'l': 'La droite d’isocoût et le point de tangence'},
        {'c': '4', 'b': 415, 'l': 'Le taux marginal de substitution technique'},
        {'c': '4', 'b': 326, 'l': 'Rendements factoriels et rendements d’échelle'}],
 mots=['isoquante', 'isocoût', 'TMST', 'productivité marginale',
       'intensité capitalistique', 'rendements d’échelle'],
))

# ---------------------------------------------- productivité du travail
def _pm_pml():
    a, c, k = 0.62, 0.44, 3.287
    pml, pm = [], []
    x = 0.05
    while x <= 0.87:
        y = a - k * (x - c) ** 2
        if y >= 0.015:
            pml.append((round(x, 4), round(y, 4)))
        x += 0.04
    x = 0.05
    while x <= 0.61:
        y = a - k * (x - c) * (3 * x - c)
        if y >= 0.015:
            pm.append((round(x, 4), round(y, 4)))
        x += 0.035
    return pml, pm


PML, PMARG = _pm_pml()

L.append(fiche(
 id='productivite-travail',
 t='Productivité moyenne et productivité marginale du travail',
 st='Pourquoi la productivité marginale coupe la moyenne exactement à son '
    'maximum.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Que se passe-t-il sur la production quand on ajoute des travailleurs à '
   'capital constant, et comment se placent les deux courbes de '
   'productivité ?',
 axes={'x': 'Quantité de travail L', 'y': 'Productivité'},
 depart='Une entreprise à court terme : son capital est fixe, elle n’ajuste '
        'que le travail.',
 hyp=['On raisonne à court terme : le capital est fixe, seul le travail '
      'varie. C’est l’étude des rendements factoriels.',
      'Loi de la productivité marginale décroissante : à capital fixe, '
      'l’augmentation du travail entraîne à terme une baisse de la '
      'productivité marginale.',
      'Cette hypothèse se justifie parce que le travail est flexible — on '
      'peut embaucher ou allonger les heures — alors que le capital prend du '
      'temps à être modifié.'],
 pente=[{'s': 'Productivité marginale', 'd': 'elle monte d’abord — la '
         'division du travail s’améliore — puis décroît : chaque travailleur '
         'supplémentaire dispose de moins de capital.'},
        {'s': 'Productivité moyenne', 'd': 'elle suit la marginale avec un '
         'retard : elle monte tant que la marginale lui est supérieure, '
         'baisse dès que la marginale lui est inférieure.'},
        {'s': 'Le croisement', 'd': 'la productivité marginale coupe la '
         'productivité moyenne exactement au maximum de celle-ci — ce n’est '
         'pas une coïncidence mais une propriété mathématique.'}],
 fig={'series': [
   pol('pml', 'Productivité moyenne (PM)', PML, 'ac', ep=3.2, lp=[0.82, 0.10]),
 ]},
 etapes=[
  etape('La productivité moyenne',
        'Elle mesure la production par unité de travail : combien produit un '
        'travailleur en moyenne. Elle augmente d’abord, atteint un maximum, '
        'puis diminue.',
        on=['pml'], vif=['pml']),
  etape('La productivité marginale',
        'Elle mesure la variation de production provoquée par l’embauche '
        'd’une unité de travail supplémentaire : ce que rapporte le dernier '
        'travailleur embauché. Elle monte plus haut et redescend plus tôt.',
        add=[pol('pm', 'Productivité marginale (Pm)', PMARG, 'ac2', ep=3.2, lp=[0.22, 0.95])],
        vif=['pm']),
  etape('La loi des rendements factoriels décroissants',
        'Au début, ajouter du travail augmente fortement la production. '
        'Au-delà d’un certain point, chaque travailleur supplémentaire '
        'apporte moins que le précédent : la productivité marginale décroît.',
        add=[fl('fd', 'rendements décroissants', 0.33, 0.86, 0.55, 0.42, 'ko'),
             rep('rp', 0.2933, 0.8322, c='ac2')],
        vif=['fd', 'rp']),
  etape('Le croisement au maximum de la moyenne',
        'Tant que le dernier travailleur produit plus que la moyenne, il tire '
        'la moyenne vers le haut. Dès qu’il produit moins, il la tire vers le '
        'bas. La marginale coupe donc la moyenne exactement à son maximum.',
        add=[pt('x', '', 0.44, 0.62, 'ok'),
             rep('rx', 0.44, 0.62, lx='L₁', c='ok'),
             txt('tx', 'Pm coupe PM en son maximum', 0.46, 0.9, 'ok',
                 taille=15, gras=True)],
        off=['fd', 'rp'],
        vif=['x', 'rx', 'tx']),
  etape('La zone où la marginale devient négative',
        'Plus loin encore, la productivité marginale passe sous zéro : le '
        'travailleur supplémentaire fait baisser la production totale, faute '
        'de capital pour travailler. Aucune entreprise rationnelle ne va '
        'jusque-là.',
        add=[txt('tn', 'Pm < 0 : zone à éviter', 0.44, 0.05, 'ko', taille=14)],
        off=['tx'],
        vif=['tn']),
  etape('Le lien avec les coûts',
        'Le coût marginal varie en sens inverse de la productivité marginale, '
        'et le coût moyen en sens inverse de la productivité moyenne. La '
        'forme en U des courbes de coûts est l’image inversée de ces deux '
        'courbes.',
        add=[txt('tc', 'Cm = image inversée de Pm', 0.52, 0.95, 'bl',
                 taille=15, gras=True)],
        off=['tn'],
        vif=['tc', 'pm', 'pml']),
 ],
 pieges=[
  {'t': 'Décroissant ne veut pas dire négatif',
   'd': 'La productivité marginale décroît bien avant de devenir négative. '
        'Tant qu’elle est positive, la production totale continue '
        'd’augmenter, seulement de moins en moins vite.'},
  {'t': 'Le croisement n’est pas arbitraire',
   'd': 'Dire que la marginale coupe la moyenne en son maximum n’est pas une '
        'convention de dessin : c’est la conséquence du fait que la moyenne '
        'monte tant que la marginale lui est supérieure. Dessiner le '
        'croisement ailleurs est une faute.'},
  {'t': 'Rendements factoriels, pas rendements d’échelle',
   'd': 'Ici un seul facteur varie, à capital fixe : c’est du court terme. '
        'Les rendements d’échelle supposent au contraire que tous les '
        'facteurs varient dans les mêmes proportions.'},
 ],
 main=[
  'Trace les axes : la quantité de travail en abscisse, la productivité en '
  'ordonnée.',
  'Trace une courbe en cloche aplatie : c’est la productivité moyenne, et '
  'marque son sommet.',
  'Trace une seconde cloche, plus haute et dont le sommet est plus à gauche : '
  'c’est la productivité marginale.',
  'Vérifie que la marginale redescend en coupant la moyenne exactement au '
  'sommet de celle-ci — corrige ton tracé si ce n’est pas le cas.',
  'Écris en marge : « Cm varie en sens inverse de Pm » pour faire le lien '
  'avec les coûts.',
 ],
 phrase='À court terme, le capital étant fixe, la productivité marginale du '
        'travail croît d’abord puis décroît en vertu de la loi des rendements '
        'factoriels décroissants ; comme la productivité moyenne augmente '
        'tant que le dernier travailleur produit plus que la moyenne, la '
        'courbe de productivité marginale coupe nécessairement la courbe de '
        'productivité moyenne en son maximum.',
 liens=[{'c': '4', 'b': 309, 'l': 'La productivité, mesure de l’efficacité des facteurs'},
        {'c': '4', 'b': 315, 'l': 'La loi de la productivité marginale décroissante'},
        {'c': '4', 'b': 492, 'l': 'La productivité du travail à court terme'},
        {'c': '4', 'b': 501, 'l': 'Le lien entre productivité et coûts'}],
 mots=['productivité marginale', 'productivité moyenne',
       'rendements décroissants', 'rendements factoriels', 'court terme'],
))

# ----------------------------------------------------- courbes de coûts
def _couts():
    c, q0, d, F = 0.30, 0.52, 2.381, 0.04
    cm, cmg, cvm, cfm = [], [], [], []
    q = 0.10
    while q <= 0.985:
        cm.append((round(q, 4), round(c + d * (q - q0) ** 2, 4)))
        cfm.append((round(q, 4), round(F / q, 4)))
        cvm.append((round(q, 4), round(c + d * (q - q0) ** 2 - F / q, 4)))
        q += 0.045
    q = 0.10
    while q <= 0.715:
        cmg.append((round(q, 4), round(c + d * (q - q0) * (3 * q - q0), 4)))
        q += 0.035
    return cm, cmg, cvm, [p for p in cfm if p[1] <= 1.0]


CM, CMG, CVM, CFM = _couts()

L.append(fiche(
 id='couts-production',
 t='Les courbes de coûts et les deux seuils',
 st='Coût moyen, coût variable moyen, coût marginal — et où l’entreprise '
    'cesse de produire.',
 cat='micro', an=1, ch=['4'],
 type='schema',
 q='Comment les coûts évoluent-ils avec la production, et à partir de quel '
   'prix une entreprise est-elle rentable ou doit-elle fermer ?',
 axes={'x': 'Quantité produite Q', 'y': 'Coût unitaire'},
 depart='Une entreprise qui augmente progressivement sa production, avec des '
        'coûts fixes donnés.',
 hyp=['Les coûts fixes ne dépendent pas du niveau de production : ils '
      'existent même si la production est nulle.',
      'Les coûts variables dépendent de la quantité produite.',
      'On se place dans une démarche de concurrence pure et parfaite : '
      'l’entreprise ne fixe pas son prix, elle le subit.'],
 pente=[{'s': 'Coût fixe moyen', 'd': 'strictement décroissant : le coût fixe '
         'est constant, donc rapporté à une production croissante il diminue '
         'toujours.'},
        {'s': 'Coût variable moyen et coût moyen', 'd': 'en U : ils diminuent '
         'd’abord grâce à une meilleure organisation, puis augmentent sous '
         'l’effet des rendements décroissants.'},
        {'s': 'Coût marginal', 'd': 'en U également, mais plus creusé et plus '
         'tôt : il coupe le coût variable moyen et le coût moyen en leurs '
         'minimums respectifs.'}],
 fig={'series': [
   pol('cm', 'Coût moyen (CM)', CM, 'ac', ep=3.2, lp=[0.86, 0.95]),
 ]},
 etapes=[
  etape('Le coût moyen',
        'C’est le coût total rapporté à la quantité produite : le coût par '
        'unité. Il diminue d’abord, atteint un minimum, puis remonte. C’est '
        'la courbe en U.',
        on=['cm'], vif=['cm']),
  etape('Pourquoi un U : deux forces opposées',
        'Au départ le coût fixe moyen s’écrase sur une production croissante, '
        'ce qui tire le coût moyen vers le bas. Plus tard les rendements '
        'décroissants l’emportent et le tirent vers le haut.',
        add=[pol('cfm', 'Coût fixe moyen (CFM)', CFM, 'gr', ep=2.2, lp=[0.60, 0.07]),
             fl('f1', 'CFM s’écrase', 0.14, 0.52, 0.34, 0.2, 'gr')],
        vif=['cfm', 'f1']),
  etape('Le coût variable moyen',
        'Il ne retient que les coûts qui dépendent de la production. Il est '
        'lui aussi en U, mais il passe sous le coût moyen : l’écart entre les '
        'deux est précisément le coût fixe moyen.',
        add=[pol('cvm', 'Coût variable moyen (CVM)', CVM, 'ac2', ep=2.8, lp=[0.26, 0.56])],
        off=['f1'],
        vif=['cvm']),
  etape('Le coût marginal',
        'C’est le coût de la dernière unité produite : combien coûte une '
        'unité supplémentaire. Il est en U mais beaucoup plus creusé, et il '
        'remonte vite.',
        add=[pol('cmg', 'Coût marginal (Cm)', CMG, 'ok', ep=3.2, lp=[0.44, 0.96])],
        off=['cfm'],
        vif=['cmg']),
  etape('Les deux croisements à ne jamais rater',
        'Le coût marginal coupe le coût variable moyen en son minimum, puis '
        'le coût moyen en son minimum. La raison est la même que pour les '
        'productivités : la moyenne baisse tant que la marginale lui est '
        'inférieure.',
        add=[pt('x1', '', 0.4845, 0.2204, 'ac2'),
             pt('x2', '', 0.52, 0.30, 'ac'),
             rep('r1', 0.4845, 0.2204, c='ac2'),
             rep('r2', 0.52, 0.30, c='ac')],
        vif=['x1', 'x2', 'r1', 'r2']),
  etape('Le seuil de rentabilité',
        'L’entreprise est rentable lorsque le prix couvre au moins son coût '
        'moyen. Le minimum du coût moyen est donc le seuil de rentabilité : '
        'en dessous de ce prix, elle perd de l’argent.',
        add=[lin('pr', 'seuil de rentabilité : P = min CM', 0.0, 0.30, 1.0,
                 0.30, 'ac', ep=2),
             txt('tr', 'P ≥ CM : rentable', 0.62, 0.36, 'ac', taille=14)],
        off=['r1', 'r2'],
        vif=['pr', 'tr', 'x2']),
  etape('Le seuil de fermeture',
        'À court terme, l’entreprise peut continuer tant que le prix couvre '
        'au moins le coût variable moyen : même sans couvrir ses coûts fixes, '
        'elle limite ses pertes. En dessous du minimum du coût variable '
        'moyen, elle doit arrêter.',
        add=[lin('pf', 'seuil de fermeture : P = min CVM', 0.0, 0.2204, 1.0,
                 0.2204, 'ac2', ep=2),
             txt('tf', 'P < CVM : arrêter', 0.62, 0.16, 'ko', taille=14)],
        vif=['pf', 'tf', 'x1']),
  etape('La courbe d’offre de l’entreprise',
        'Puisqu’en concurrence l’entreprise subit le prix, elle produit là où '
        'le coût marginal égale ce prix. Sa courbe d’offre est donc la partie '
        'croissante du coût marginal située au-dessus du seuil de fermeture.',
        add=[fl('fo', '', 0.60, 0.44, 0.70, 0.76, 'bl'),
             txt('tof', 'offre = partie croissante de Cm au-dessus du seuil',
                 0.1, 0.9, 'bl', taille=14, gras=True)],
        off=['tf', 'tr'],
        vif=['fo', 'tof', 'cmg']),
 ],
 pieges=[
  {'t': 'Coût moyen n’est pas coût marginal',
   'd': 'Le coût moyen répond à « combien me coûte en moyenne chaque unité », '
        'le coût marginal à « combien me coûte la prochaine ». C’est le '
        'second qui commande la décision de produire une unité de plus.'},
  {'t': 'Deux seuils, pas un',
   'd': 'Le seuil de rentabilité (minimum du coût moyen) dit si l’entreprise '
        'gagne de l’argent. Le seuil de fermeture (minimum du coût variable '
        'moyen) dit si elle a intérêt à continuer à court terme. Entre les '
        'deux, elle produit à perte mais limite ses pertes.'},
  {'t': 'Le long terme enveloppe les courts termes',
   'd': 'La courbe de coût de longue période est l’enveloppe des courbes de '
        'courte période : à court terme on choisit le minimum d’une courbe '
        'donnée, à long terme on choisit la courbe elle-même. C’est là que '
        'jouent les économies d’échelle.'},
 ],
 main=[
  'Trace les axes : la quantité produite en abscisse, le coût unitaire en '
  'ordonnée.',
  'Trace le coût moyen en U et, en pointillés sous lui, le coût fixe moyen '
  'strictement décroissant.',
  'Trace le coût variable moyen en U, toujours sous le coût moyen.',
  'Trace le coût marginal, plus creusé, en vérifiant qu’il coupe le coût '
  'variable moyen puis le coût moyen exactement en leurs minimums.',
  'Trace les deux horizontales correspondantes et nomme-les : seuil de '
  'rentabilité et seuil de fermeture.',
 ],
 phrase='Les courbes de coût moyen et de coût variable moyen sont en U parce '
        'que l’écrasement du coût fixe moyen l’emporte d’abord, avant que les '
        'rendements décroissants ne prennent le dessus, et le coût marginal '
        'les coupe en leurs minimums respectifs : le minimum du coût moyen '
        'définit le seuil de rentabilité, celui du coût variable moyen le '
        'seuil au-delà duquel l’entreprise doit cesser de produire.',
 liens=[{'c': '4', 'b': 451, 'l': 'Les coûts de production : fixes et variables'},
        {'c': '4', 'b': 466, 'l': 'Les coûts moyens'},
        {'c': '4', 'b': 480, 'l': 'Le coût marginal et ses croisements'},
        {'c': '4', 'b': 504, 'l': 'Rentabilité et seuil de rentabilité'},
        {'c': '4', 'b': 514, 'l': 'La courbe de longue période, enveloppe des courtes périodes'}],
 mots=['coût moyen', 'coût marginal', 'coût variable moyen',
       'seuil de rentabilité', 'économies d’échelle', 'courbe en U'],
))

# ----------------------------------------- équilibre de marché et chocs
OFF = courbe_cro(0.08, 0.1, 0.95, 0.9, n=9, creux=0.78)
DEM = courbe_dec(0.08, 0.92, 0.95, 0.1, n=9, creux=0.78)
OD = (0.08, 0.1, 0.95, 0.9)
DD = (0.08, 0.92, 0.95, 0.1)
EM = inter(OD, DD)

L.append(fiche(
 id='equilibre-cpp',
 t='L’équilibre de marché en concurrence pure et parfaite',
 st='Le modèle de référence : une offre, une demande, un prix qui équilibre.',
 cat='micro', an=1, ch=['3', '4'],
 type='schema',
 q='Comment la confrontation de l’offre et de la demande détermine-t-elle un '
   'prix et une quantité d’équilibre, et sous quelles hypothèses ce résultat '
   'tient-il ?',
 axes={'x': 'Quantités', 'y': 'Prix'},
 depart='Un marché isolé — un seul bien — étudié toutes choses égales par '
        'ailleurs, selon la démarche d’équilibre partiel de Marshall.',
 hyp=['Homogénéité des produits : ils sont parfaitement interchangeables.',
      'Atomicité des agents : offreurs et demandeurs sont trop nombreux et '
      'trop petits pour influencer le prix, qui est donc subi.',
      'Mobilité parfaite des facteurs de production.',
      'Libre entrée et libre sortie du marché, sans barrière.',
      'Transparence de l’information : tous les agents connaissent les prix '
      'et les caractéristiques des produits.'],
 pente=[{'s': 'Courbe d’offre', 'd': 'croissante : un prix plus élevé rend '
         'rentable la production d’unités supplémentaires, dont le coût '
         'marginal est plus élevé.'},
        {'s': 'Courbe de demande', 'd': 'décroissante : un prix plus élevé '
         'réduit les quantités demandées, par effet de substitution et par '
         'effet de revenu.'}],
 fig={'series': [
   lin('o', 'Offre', *OD, c='ac', ep=3.2),
   lin('d', 'Demande', *DD, c='ac2', ep=3.2),
   pt('e', 'E', EM[0], EM[1], 'ok'),
   rep('re', EM[0], EM[1], lx='Q*', ly='P*', c='ok'),
 ]},
 etapes=[
  etape('Les deux courbes',
        'L’offre monte avec le prix, la demande descend. En concurrence pure '
        'et parfaite, aucun agent n’a le pouvoir de fixer le prix : il résulte '
        'de la confrontation des deux.',
        on=['o', 'd'], vif=['o', 'd']),
  etape('Le prix et la quantité d’équilibre',
        'Au point de croisement, la quantité offerte égale la quantité '
        'demandée. Le marché détermine simultanément un prix P* et une '
        'quantité Q* : c’est l’équilibre.',
        on=['e', 're'], vif=['e', 're']),
  etape('Au-dessus du prix d’équilibre : excès d’offre',
        'À un prix plus élevé, les producteurs veulent vendre davantage que '
        'ce que les consommateurs souhaitent acheter. L’invendu pousse les '
        'prix à la baisse : le marché revient vers l’équilibre.',
        add=[lin('ph', '', 0.0, 0.72, 1.0, 0.72, 'gr', ep=1.6),
             txt('th', 'offre > demande : le prix baisse', 0.3, 0.76, 'ko',
                 taille=14),
             fl('fh', '', 0.9, 0.7, 0.9, 0.56, 'ko')],
        vif=['ph', 'th', 'fh']),
  etape('En dessous : excès de demande',
        'À un prix plus bas, les consommateurs veulent acheter plus que ce '
        'qui est produit. La pénurie pousse les prix à la hausse. Cette '
        'double force est l’auto-régulation par les prix.',
        add=[lin('pb', '', 0.0, 0.28, 1.0, 0.28, 'gr', ep=1.6),
             txt('tb', 'demande > offre : le prix monte', 0.3, 0.2, 'ok',
                 taille=14),
             fl('fb', '', 0.9, 0.3, 0.9, 0.44, 'ok')],
        off=['ph', 'th', 'fh'],
        vif=['pb', 'tb', 'fb']),
  etape('Le surplus des agents',
        'Au-dessus du prix, l’aire sous la demande mesure ce que les '
        'consommateurs auraient accepté de payer en plus : leur surplus. En '
        'dessous, l’aire au-dessus de l’offre mesure celui des producteurs. '
        'C’est en ce sens que l’allocation est jugée efficace.',
        add=[zone('sc', 'surplus du consommateur',
                  [(0.08, 0.92), (EM[0], EM[1]), (0.08, EM[1])], 'ac2'),
             zone('sp', 'surplus du producteur',
                  [(0.08, 0.1), (EM[0], EM[1]), (0.08, EM[1])], 'ac')],
        off=['pb', 'tb', 'fb'],
        vif=['sc', 'sp']),
  etape('Un modèle de référence, pas une description',
        'Ces cinq hypothèses sont rarement vérifiées : différenciation des '
        'produits, concentration des entreprises, barrières à l’entrée, '
        'information asymétrique. Dès qu’une condition est violée, le marché '
        'devient imparfait et des défaillances apparaissent.',
        add=[txt('tl', '5 hypothèses violées = défaillances de marché',
                 0.16, 0.96, 'jn', taille=15, gras=True)],
        off=['sc', 'sp'],
        vif=['tl']),
  etape('La limite de l’équilibre partiel',
        'Raisonner sur un marché isolé est un outil, pas la réalité : les '
        'marchés sont interdépendants, un choc se propage et revient. '
        'Sonnenschein et Mantel montrent qu’on ne connaît pas avec certitude '
        'la forme de la courbe de demande agrégée.',
        add=[txt('ts', 'ceteris paribus : une simplification', 0.2, 0.9,
                 'ko', taille=14)],
        off=['tl'],
        vif=['ts']),
 ],
 pieges=[
  {'t': 'Le prix n’est pas choisi, il est subi',
   'd': 'Dans la logique néoclassique, le producteur n’a pas le pouvoir de '
        'fixer le prix : c’est le marché qui le fixe, du fait de '
        'l’atomicité. L’entreprise choisit seulement sa quantité.'},
  {'t': 'Équilibre partiel et équilibre général',
   'd': 'L’équilibre partiel étudie un marché à la fois, selon le ceteris '
        'paribus de Marshall. L’équilibre général walrasien cherche la '
        'compatibilité simultanée de tous les marchés. Le second est bien '
        'plus exigeant.'},
  {'t': 'Efficace ne veut pas dire juste',
   'd': 'L’allocation est dite efficace au sens de la maximisation des '
        'surplus, sous les cinq hypothèses. Cela ne dit rien de la '
        'répartition : la microéconomie standard a abandonné les classes '
        'sociales au profit des préférences individuelles.'},
 ],
 main=[
  'Trace les axes : les quantités en abscisse, le prix en ordonnée.',
  'Trace une offre croissante et une demande décroissante, puis marque leur '
  'intersection E et projette-la sur les deux axes.',
  'Trace une horizontale au-dessus de P* : repère l’excès d’offre et la '
  'flèche de baisse du prix.',
  'Trace une horizontale en dessous : repère l’excès de demande et la flèche '
  'de hausse.',
  'Hachure enfin les deux triangles de surplus, de part et d’autre du prix '
  'd’équilibre.',
 ],
 phrase='En concurrence pure et parfaite, la confrontation d’une offre '
        'croissante et d’une demande décroissante détermine un prix et une '
        'quantité d’équilibre vers lesquels le marché revient de lui-même '
        'par l’auto-régulation des prix ; mais ce résultat repose sur cinq '
        'hypothèses — homogénéité, atomicité, mobilité des facteurs, libre '
        'entrée et transparence — dont la violation fait précisément '
        'apparaître les défaillances de marché.',
 liens=[{'c': '3', 'b': 570, 'l': 'La concurrence pure et parfaite, modèle de référence'},
        {'c': '3', 'b': 580, 'l': 'Les cinq hypothèses et leurs limites'},
        {'c': '4', 'b': 533, 'l': 'De l’équilibre partiel à l’équilibre général'},
        {'c': '4', 'b': 1026, 'l': 'Le lien avec la concurrence pure et parfaite'},
        {'c': '4', 'b': 525, 'l': 'L’approche de Marshall et le ceteris paribus'}],
 mots=['concurrence pure et parfaite', 'CPP', 'équilibre partiel',
       'Marshall', 'Walras', 'surplus', 'atomicité', 'auto-régulation'],
))

# --------------------------------------------------------------- chocs
L.append(fiche(
 id='chocs-offre-demande',
 t='Chocs d’offre et chocs de demande',
 st='La distinction qui décide de tout : se déplacer sur la courbe ou '
    'déplacer la courbe.',
 cat='micro', an=1, ch=['3', '4'],
 type='schema',
 q='Quand faut-il faire glisser un point le long d’une courbe et quand faut-il '
   'déplacer la courbe elle-même, et que devient l’équilibre dans chaque cas ?',
 axes={'x': 'Quantités', 'y': 'Prix'},
 depart='Un marché à l’équilibre en E, avant tout choc.',
 hyp=['Toutes choses égales par ailleurs : on isole un marché, en gardant le '
      'reste de l’économie inchangé.',
      'Une variation du prix du bien lui-même ne déplace jamais les courbes : '
      'elle fait seulement lire une autre quantité sur la même courbe.',
      'Seule la modification d’un déterminant autre que le prix du bien — '
      'coûts, revenus, préférences, prix des autres biens, technologie — '
      'déplace une courbe.'],
 pente=[{'s': 'Offre', 'd': 'croissante, parce que produire des unités '
         'supplémentaires coûte plus cher à la marge.'},
        {'s': 'Demande', 'd': 'décroissante, par effet de substitution et par '
         'effet de revenu.'},
        {'s': 'Déplacement', 'd': 'une courbe qui se déplace vers la droite '
         'signifie « plus de quantité à chaque prix » ; vers la gauche, '
         '« moins de quantité à chaque prix ».'}],
 fig={'series': [
   lin('o', 'Offre', *OD, c='ac', ep=3.2),
   lin('d', 'Demande', *DD, c='ac2', ep=3.2),
   pt('e', 'E', EM[0], EM[1], 'ok'),
   rep('re', EM[0], EM[1], lx='Q*', ly='P*', c='ok'),
 ]},
 etapes=[
  etape('L’équilibre de départ',
        'Le marché est en E : un prix P*, une quantité Q*. Ce point servira '
        'de référence à chacun des trois cas qui suivent.',
        on=['o', 'd', 'e', 're'], vif=['e', 're']),
  etape('Premier cas : un simple changement de prix',
        'Si seul le prix change — par exemple à cause d’une taxe payée par '
        'l’acheteur ou d’un prix administré — on ne déplace rien : on lit une '
        'autre quantité sur les mêmes courbes. On glisse SUR les courbes.',
        add=[lin('ph', '', 0.0, 0.72, 1.0, 0.72, 'jn', ep=1.8),
             pt('g1', '', round(x_de(DD, 0.72), 4), 0.72, 'jn'),
             pt('g2', '', round(x_de(OD, 0.72), 4), 0.72, 'jn'),
             txt('tg', 'déplacement SUR les courbes', 0.26, 0.8, 'jn',
                 taille=15, gras=True)],
        vif=['ph', 'g1', 'g2', 'tg']),
  etape('Deuxième cas : un choc de demande',
        'Le revenu des ménages augmente, ou leurs préférences changent. À '
        'chaque prix ils demandent davantage : la courbe de demande se '
        'déplace vers la droite. Le prix d’équilibre monte et la quantité '
        'augmente.',
        add=[lin('d1', 'D₁', *bouge(DD, 0.17, 0), c='ko', ep=2.8),
             pt('e1', 'E₁', *inter(OD, {'p': bouge(DD, 0.17, 0)}), c='ko'),
             rep('r1', *inter(OD, {'p': bouge(DD, 0.17, 0)}), lx='Q₁',
                 ly='P₁', c='ko')],
        off=['ph', 'g1', 'g2', 'tg'],
        vif=['d1', 'e1', 'r1']),
  etape('Lecture du choc de demande',
        'Prix et quantité varient dans le même sens : c’est la signature d’un '
        'choc de demande. Si on observe une hausse du prix accompagnée d’une '
        'hausse des quantités, le choc vient de la demande.',
        add=[txt('tdd', 'choc de demande : P ↑ et Q ↑', 0.3, 0.95, 'ko',
                 taille=15, gras=True)],
        vif=['tdd']),
  etape('Troisième cas : un choc d’offre défavorable',
        'Les coûts de production augmentent — un choc pétrolier, par exemple. '
        'À chaque prix les producteurs offrent moins : la courbe d’offre se '
        'déplace vers la gauche, ce qui revient à la remonter.',
        add=[lin('o1', 'O₁', *bouge(OD, -0.17, 0), c='bl', ep=2.8),
             pt('e2', 'E₂', *inter({'p': bouge(OD, -0.17, 0)}, DD), c='bl'),
             rep('r2', *inter({'p': bouge(OD, -0.17, 0)}, DD), lx='Q₂',
                 ly='P₂', c='bl')],
        off=['d1', 'e1', 'r1', 'tdd'],
        vif=['o1', 'e2', 'r2']),
  etape('Lecture du choc d’offre',
        'Prix et quantité varient en sens contraire : le prix monte, la '
        'quantité baisse. C’est la signature d’un choc d’offre — et, au '
        'niveau macroéconomique, la configuration qui produit la stagflation.',
        add=[txt('too', 'choc d’offre : P ↑ et Q ↓', 0.3, 0.95, 'bl',
                 taille=15, gras=True)],
        vif=['too']),
  etape('La règle à retenir',
        'Le prix du bien lui-même ne déplace jamais la courbe de ce bien. '
        'Tout autre déterminant — coûts, revenus, préférences, technologie, '
        'prix des autres biens — déplace la courbe. Cette règle évite la '
        'moitié des erreurs de graphique.',
        add=[txt('tr1', 'prix du bien → on glisse SUR la courbe', 0.1, 0.9,
                 'jn', taille=14, gras=True),
             txt('tr2', 'autre déterminant → la courbe SE DÉPLACE', 0.1, 0.83,
                 'ok', taille=14, gras=True)],
        off=['too'],
        vif=['tr1', 'tr2']),
 ],
 pieges=[
  {'t': 'L’erreur la plus coûteuse de tout le programme',
   'd': 'Déplacer la courbe de demande parce que le prix du bien a changé est '
        'un contresens : la courbe de demande dit déjà quelle quantité est '
        'demandée à chaque prix. Changer le prix, c’est lire la courbe '
        'ailleurs, pas la redessiner.'},
  {'t': 'Vers la gauche ou vers le haut ?',
   'd': 'Pour une courbe d’offre croissante, « se déplacer vers la gauche » '
        'et « se déplacer vers le haut » décrivent le même mouvement. '
        'L’important est de dire ce que cela signifie : moins offert à chaque '
        'prix.'},
  {'t': 'Le sens de variation permet d’identifier le choc',
   'd': 'Même sens pour le prix et la quantité : choc de demande. Sens '
        'contraires : choc d’offre. C’est le raisonnement à utiliser quand un '
        'sujet donne des faits et demande d’en déduire l’origine du '
        'déséquilibre.'},
 ],
 main=[
  'Trace les axes, une offre croissante, une demande décroissante, et marque '
  'l’équilibre E.',
  'Trace une horizontale à un autre prix et marque les deux points lus sur '
  'les courbes : écris « on glisse SUR les courbes ».',
  'Déplace la demande vers la droite et marque E₁ : vérifie que prix et '
  'quantité montent tous les deux.',
  'Reviens à la demande initiale, déplace l’offre vers la gauche et marque '
  'E₂ : vérifie que le prix monte et la quantité baisse.',
  'Écris en bas de page les deux règles : prix du bien → on glisse ; autre '
  'déterminant → la courbe se déplace.',
 ],
 phrase='Une variation du prix du bien lui-même ne déplace aucune courbe : '
        'elle fait simplement lire une autre quantité sur la même courbe, '
        'tandis que la modification de tout autre déterminant déplace la '
        'courbe elle-même ; dès lors, un choc de demande fait varier prix et '
        'quantité dans le même sens, alors qu’un choc d’offre les fait varier '
        'en sens contraire.',
 liens=[{'c': '4', 'b': 534, 'l': 'L’analyse de l’équilibre partiel'},
        {'c': '4', 'b': 559, 'l': 'Les effets venus d’ailleurs et les boucles de rétroaction'},
        {'c': '3', 'b': 578, 'l': 'L’allocation efficace sous les hypothèses de la CPP'},
        {'c': '2', 'b': 367, 'l': 'Le choc pétrolier : hausse des coûts, inflation et chômage'}],
 mots=['choc d’offre', 'choc de demande', 'déplacement de courbe',
       'équilibre', 'ceteris paribus', 'stagflation'],
))
