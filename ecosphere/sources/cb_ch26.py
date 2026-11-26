# -*- coding: utf-8 -*-
"""Courbes du chapitre 6 de deuxième année — taux de change, marché des
changes, courbe en J et condition de Marshall-Lerner."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     inter, y_de, x_de, bouge)

L = []

# -------------------------------------------------- le marché des changes
DD = lin('dd', 'Demande de dollars', 0.08, 0.90, 0.95, 0.18, 'ac')
OO = lin('oo', 'Offre de dollars', 0.08, 0.18, 0.95, 0.90, 'ok')
EQ = inter(DD, OO)
DD1 = bouge(DD, 0.16, 0)
EQ1 = inter({'p': DD1}, OO)

L.append(fiche(
 id='marche-changes',
 t='Le marché des changes',
 st='Une offre, une demande, et le prix d’une monnaie en termes d’une autre.',
 cat='ouverte', an=2, ch=['26'],
 type='schema',
 q='Comment la confrontation de l’offre et de la demande de devises '
   'détermine-t-elle le taux de change en régime de change flottant ?',
 axes={'x': 'Quantité de dollars échangée', 'y': 'Taux de change',
       'yu': 'euros pour un dollar'},
 depart='Un marché des changes à l’équilibre en E, dans un régime de change '
        'flottant où aucune banque centrale n’intervient.',
 hyp=['Le régime de change est flottant : la valeur de la monnaie résulte de '
      'la confrontation de l’offre et de la demande sur le marché.',
      'On raisonne sur un seul couple de monnaies, l’euro et le dollar, en '
      'cotation au certain inversée : l’ordonnée donne le nombre d’euros à '
      'verser pour obtenir un dollar.',
      'Les motifs d’achat et de vente sont multiples : règlement des '
      'importations, encaissement des exportations, placements '
      'internationaux, couverture et spéculation.'],
 pente=[{'s': 'Demande de dollars', 'd': 'décroissante : plus le dollar coûte '
         'cher en euros, plus les produits et les actifs américains sont '
         'onéreux pour un résident de la zone euro, et moins on souhaite de '
         'dollars.'},
        {'s': 'Offre de dollars', 'd': 'croissante : plus le dollar vaut '
         'd’euros, plus il est avantageux pour ses détenteurs de le céder '
         'contre des euros.'}],
 fig={'series': [
   DD, OO, pt('e', 'E', EQ[0], EQ[1], 'ac2'),
   rep('re', EQ[0], EQ[1], lx='Q*', ly='e*', c='ac2'),
 ]},
 etapes=[
  etape('Deux courbes qui se croisent',
        'La demande de dollars émane de ceux qui doivent payer en dollars ou '
        'placer des capitaux aux États-Unis ; l’offre émane de ceux qui '
        'détiennent des dollars et veulent des euros.',
        on=['dd', 'oo'], vif=['dd', 'oo']),
  etape('Le taux de change d’équilibre',
        'Au point E, la quantité de dollars offerte égale la quantité '
        'demandée : le marché détermine un taux de change e*, c’est-à-dire un '
        'prix du dollar en euros.',
        on=['e', 're'], vif=['e', 're']),
  etape('Un choc : la demande de dollars augmente',
        'Les importations européennes de produits facturés en dollars '
        'progressent, ou les placements vers les États-Unis s’intensifient. '
        'La courbe de demande se déplace vers la droite.',
        add=[lin('dd1', 'D₁', *DD1, c='ac2'),
             fl('f1', '', 0.42, 0.56, 0.6, 0.56, 'ac2')],
        vif=['dd1', 'f1']),
  etape('Le dollar s’apprécie, l’euro se déprécie',
        'Le nouveau point d’équilibre est plus haut : il faut davantage '
        'd’euros pour obtenir un dollar. Dire que le dollar s’apprécie et '
        'dire que l’euro se déprécie, c’est décrire le même mouvement.',
        add=[pt('e1', 'E₁', EQ1[0], EQ1[1], 'ko'),
             rep('r1', EQ1[0], EQ1[1], lx='Q₁', ly='e₁', c='ko')],
        vif=['e1', 'r1']),
  etape('Ce qui déplace les courbes',
        'Les échanges commerciaux et les mouvements de capitaux sont les '
        'déterminants essentiels de l’offre et de la demande de monnaies : un '
        'écart de taux d’intérêt, une anticipation, une recherche de sécurité '
        'suffisent à déplacer les courbes, indépendamment des échanges de '
        'biens.',
        vif=['dd', 'dd1']),
  etape('Ce que change un régime de change fixe',
        'En changes fixes, la banque centrale intervient pour empêcher le '
        'taux de sortir de la parité annoncée : elle achète ou vend des '
        'devises, ce qui revient à ajouter sa propre offre ou sa propre '
        'demande sur le marché.',
        add=[lin('par', 'parité défendue', 0.03, EQ[1], 0.98, EQ[1], 'bl', ep=2.4),
             fl('f2', 'intervention', 0.78, EQ1[1], 0.78, round(EQ[1] + 0.02, 4), 'bl')],
        vif=['par', 'f2']),
 ],
 pieges=[
  {'t': 'Déplacement sur la courbe ou déplacement de la courbe',
   'd': 'Un changement du taux de change fait glisser le long des courbes : '
        'on lit une autre quantité au même point de la courbe. Seul un '
        'changement des motifs d’achat ou de vente — commerce, capitaux, '
        'anticipations — déplace la courbe elle-même.'},
  {'t': 'Appréciation du dollar n’est pas dépréciation du dollar',
   'd': 'Avec le dollar en ordonnée exprimé en euros, une hausse du taux lu '
        'sur l’axe est une appréciation du dollar et donc une dépréciation de '
        'l’euro. Inverser la cotation inverse la lecture : il faut toujours '
        'écrire l’unité de l’axe avant d’interpréter.'},
  {'t': 'Les volumes dépassent largement les besoins du commerce',
   'd': 'Le marché des changes est dominé par les acteurs financiers, et les '
        'transactions sont très supérieures aux besoins immédiats du commerce '
        'international : raisonner uniquement en termes d’importations et '
        'd’exportations est insuffisant.'},
 ],
 main=[
  'Trace les axes : quantité de dollars en abscisse, taux de change en euros '
  'par dollar en ordonnée — écris l’unité tout de suite.',
  'Trace une demande décroissante et une offre croissante, place E et ses '
  'deux pointillés.',
  'Déplace la demande vers la droite d’une flèche horizontale.',
  'Place le nouvel équilibre plus haut et plus à droite, et écris « dollar ↑, '
  'euro ↓ ».',
  'Ajoute enfin une horizontale au niveau de départ : c’est la parité '
  'défendue en changes fixes, avec la flèche de l’intervention.',
 ],
 phrase='En régime de change flottant, le taux de change est le prix d’une '
        'monnaie en termes d’une autre, déterminé par la confrontation d’une '
        'offre et d’une demande de devises qui répondent non seulement aux '
        'échanges commerciaux mais aussi, et surtout, aux mouvements '
        'internationaux de capitaux et aux anticipations.',
 liens=[{'c': '26', 'b': 279, 'l': 'Le marché des changes confronte une offre et une demande de devises'},
        {'c': '26', 'b': 293, 'l': 'La formation du taux de change dépend du régime de change'},
        {'c': '26', 'b': 613, 'l': 'Le rôle de la balance des paiements dans l’offre et la demande'}],
 mots=['marché des changes', 'Forex', 'taux de change', 'appréciation',
       'dépréciation', 'devises', 'cotation'],
))

# ------------------------------------------------------------- courbe en J
JPTS = [(0.02, 0.5), (0.08, 0.42), (0.14, 0.33), (0.2, 0.27), (0.26, 0.25),
        (0.33, 0.28), (0.42, 0.37), (0.52, 0.49), (0.63, 0.6), (0.75, 0.68),
        (0.88, 0.73), (0.97, 0.75)]
JFAIBLE = [(0.02, 0.5), (0.1, 0.41), (0.2, 0.32), (0.32, 0.27),
           (0.46, 0.26), (0.62, 0.28), (0.8, 0.31), (0.97, 0.33)]
JEROD = [(0.52, 0.49), (0.62, 0.55), (0.7, 0.56), (0.8, 0.53), (0.9, 0.49),
         (0.97, 0.46)]

L.append(fiche(
 id='courbe-j',
 t='La courbe en J',
 st='Pourquoi une dévaluation dégrade le solde commercial avant de '
    'l’améliorer.',
 cat='ouverte', an=2, ch=['26'],
 type='schema',
 q='Pourquoi les effets bénéfiques d’une dévaluation compétitive sur le solde '
   'commercial ne sont-ils pas immédiats ?',
 axes={'x': 'Temps écoulé depuis la dévaluation', 'y': 'Solde commercial'},
 depart='Le solde commercial à sa valeur initiale, à l’instant où la '
        'dévaluation est décidée.',
 hyp=['Les prix relatifs sont modifiés immédiatement par la dévaluation.',
      'Les volumes échangés sont rigides à court terme : contrats et '
      'commandes sont déjà conclus, et les agents ont besoin de temps pour '
      'changer de fournisseur ou de produit.',
      'Les importations sont facturées en devises et leurs prix restent '
      'inchangés, de sorte que leur coût en monnaie nationale augmente '
      'aussitôt.'],
 pente=[{'s': 'Première branche, descendante', 'd': 'les effets-prix '
         'dominent : la facture des importations se renchérit sans que les '
         'volumes aient encore réagi.'},
        {'s': 'Seconde branche, ascendante', 'd': 'les effets-volume '
         'apparaissent : les acheteurs étrangers se tournent vers les '
         'produits nationaux devenus moins chers, et les importations '
         'reculent.'}],
 fig={'series': [
   pol('j', 'Solde commercial', JPTS, 'ac', ep=3.4),
   lin('z', '', 0.0, 0.5, 0.99, 0.5, 'gr', ep=1.6),
   txt('tz', 'niveau initial du solde', 0.62, 0.52, 'gr', taille=13),
   pt('d0', '', 0.02, 0.5, 'ac2'),
   txt('td0', 'dévaluation', 0.03, 0.56, 'ac2', taille=14, gras=True),
 ]},
 etapes=[
  etape('L’instant de la dévaluation',
        'À l’origine, la monnaie est dévaluée. Le solde commercial part de '
        'son niveau initial, repéré par l’horizontale en pointillés.',
        on=['z', 'tz', 'd0', 'td0'], vif=['d0', 'td0']),
  etape('Phase 1 — les effets-prix dominent',
        'Les contrats sont déjà conclus, les volumes restent rigides. Mais la '
        'dévaluation renchérit immédiatement la facture des importations '
        'facturées en devises : le solde se dégrade, la courbe descend.',
        add=[pol('j1', '', JPTS[:5], 'ko', ep=3.4),
             fl('f1', 'effets-prix', 0.08, 0.2, 0.22, 0.2, 'ko')],
        vif=['j1', 'f1']),
  etape('Le creux du J',
        'La dégradation atteint un minimum. Le délai qui y conduit est le '
        'temps dont les entreprises étrangères ont besoin pour changer de '
        'fournisseur, les consommateurs pour remplacer leurs produits '
        'importés, les producteurs nationaux pour accroître leurs capacités.',
        add=[pt('creux', 'creux', 0.26, 0.25, 'ko'),
             rep('rc', 0.26, 0.25, lx='t₁', c='ko')],
        vif=['creux', 'rc']),
  etape('Phase 2 — les effets-volume apparaissent',
        'Les acheteurs adaptent enfin leurs achats : les exportations '
        'progressent en volume, les importations reculent. Le solde commence '
        'à s’améliorer et la courbe remonte.',
        add=[pol('j2', '', JPTS[4:9], 'ok', ep=3.4),
             fl('f2', 'effets-volume', 0.34, 0.44, 0.52, 0.56, 'ok')],
        vif=['j2', 'f2']),
  etape('Le franchissement du niveau initial',
        'La courbe repasse au-dessus de l’horizontale : le solde est '
        'désormais meilleur qu’avant la dévaluation. La forme en J est '
        'complète, et le délai écoulé explique pourquoi une dévaluation est '
        'politiquement coûteuse à court terme.',
        add=[pt('cross', '', 0.52, 0.5, 'ok'),
             rep('rx', 0.52, 0.5, lx='t₂', c='ok')],
        vif=['cross', 'rx', 'j2']),
  etape('Phase 3 — l’érosion possible des gains',
        'Si l’inflation importée renchérit durablement les coûts nationaux, '
        'les gains de compétitivité-prix se dissipent et la courbe redescend : '
        'le J n’est pas garanti jusqu’au bout.',
        add=[pol('jer', 'érosion des gains', JEROD, 'jn', ep=2.8)],
        vif=['jer']),
  etape('Et si les volumes ne réagissent pas assez ?',
        'Lorsque les élasticités-prix sont trop faibles, la remontée ne '
        'suffit pas à ramener le solde à son niveau initial : la courbe reste '
        'sous l’horizontale. C’est l’objet de la condition de '
        'Marshall-Lerner.',
        add=[pol('jf', 'élasticités trop faibles', JFAIBLE, 'ko', ep=2.6,
                 pale=1)],
        off=['jer'],
        vif=['jf']),
 ],
 pieges=[
  {'t': 'L’axe des abscisses est un temps, pas une quantité',
   'd': 'La courbe en J n’est pas une courbe d’offre ou de demande : elle '
        'retrace une trajectoire temporelle. Il n’y a donc ni déplacement de '
        'courbe ni équilibre à chercher, mais des phases à distinguer.'},
  {'t': 'La dégradation initiale ne vient pas des exportations',
   'd': 'Si les exportateurs maintiennent leurs prix en monnaie nationale, '
        'leurs recettes unitaires ne diminuent pas. La dégradation vient '
        'principalement du renchérissement des importations facturées en '
        'devises.'},
  {'t': 'La remontée n’est pas automatique',
   'd': 'Elle dépend de la sensibilité des quantités exportées et importées '
        'aux variations de prix, des capacités de production disponibles et '
        'de la maîtrise de l’inflation importée. Trois conditions, pas une '
        'mécanique.'},
 ],
 main=[
  'Trace les axes : le temps écoulé depuis la dévaluation en abscisse, le '
  'solde commercial en ordonnée.',
  'Trace une horizontale en pointillés au niveau initial du solde, et marque '
  'l’instant de la dévaluation sur l’axe des ordonnées.',
  'Descends la courbe sur le premier quart — écris « effets-prix » — jusqu’à '
  'un creux que tu repères par un pointillé vers l’axe du temps.',
  'Remonte ensuite la courbe — écris « effets-volume » — et marque le point '
  'où elle recoupe l’horizontale.',
  'Ajoute en pointillés les deux trajectoires alternatives : l’érosion des '
  'gains par l’inflation importée, et la remontée insuffisante si les '
  'élasticités sont trop faibles.',
 ],
 phrase='La courbe en J illustre le décalage entre les effets-prix immédiats '
        'd’une dévaluation, défavorables au solde commercial parce que la '
        'facture des importations se renchérit avant que les volumes ne '
        'réagissent, et les effets-volume différés susceptibles de permettre '
        'son redressement : les effets bénéfiques d’une dévaluation ne sont '
        'donc jamais immédiats.',
 liens=[{'c': '26', 'b': 2074, 'l': 'La courbe en J : les effets bénéfiques ne sont pas immédiats'},
        {'c': '26', 'b': 2082, 'l': 'Phase 1 — la domination des effets-prix'},
        {'c': '26', 'b': 2101, 'l': 'Phase 2 — l’apparition des effets-volume'},
        {'c': '26', 'b': 2105, 'l': 'Phase 3 — amélioration ou érosion des gains'}],
 mots=['courbe en J', 'dévaluation', 'solde commercial', 'effets-prix',
       'effets-volume', 'Plihon'],
))

# ------------------------------------------------------- Marshall-Lerner
L.append(fiche(
 id='marshall-lerner',
 t='La condition de Marshall-Lerner',
 st='Le même choc, deux résultats opposés : tout dépend des élasticités.',
 cat='ouverte', an=2, ch=['26'],
 type='schema',
 q='À quelle condition portant sur les élasticités-prix une dévaluation '
   'améliore-t-elle réellement le solde commercial ?',
 axes={'x': 'Postes comparés', 'y': 'Valeur',
       'yu': 'base 100 avant la dévaluation'},
 depart='Un commerce initialement équilibré : exportations et importations '
        'valent chacune 100, le solde commercial est nul.',
 hyp=['Le théorème des élasticités critiques porte sur la somme des '
      'élasticités-prix des demandes d’exportations et d’importations, prises '
      'en valeur absolue.',
      'La condition simple suppose notamment une situation initiale de '
      'commerce équilibré et des hypothèses particulières de prix et de '
      'facturation.',
      'La dévaluation retenue dans l’illustration est de 10 %, identique dans '
      'les deux cas comparés.'],
 pente=[{'s': 'Lecture des barres', 'd': 'ce graphique n’a pas de pente : il '
         'compare des niveaux. L’information est dans l’écart entre la barre '
         'des exportations et celle des importations.'},
        {'s': 'Seuil de la condition', 'd': 'la somme des deux élasticités en '
         'valeur absolue doit dépasser l’unité ; égale à un, l’effet global '
         'est nul dans le cadre simplifié.'}],
 fig={'series': [
   lin('z', '', 0.0, 0.42, 0.99, 0.42, 'gr', ep=1.8),
   txt('tz', 'base 100 : commerce équilibré', 0.55, 0.44, 'gr', taille=13),
   barre('bx', '', 0.17, 0.42, 0.11, 'ac'),
   barre('bm', '', 0.42, 0.42, 0.11, 'ac2'),
   txt('lx', 'Exportations', 0.09, -0.07, 'ac', taille=14),
   txt('lm', 'Importations', 0.34, -0.07, 'ac2', taille=14),
   txt('ls', 'Solde', 0.68, -0.07, 'ok', taille=14),
 ]},
 variantes=[
  {'lib': 'Élasticités élevées (somme > 1)',
   'etapes': [
     etape('Le point de départ : un commerce équilibré',
           'Exportations et importations valent 100 : le solde commercial est '
           'nul. C’est la situation initiale supposée par la condition '
           'simple.',
           on=['z', 'tz', 'lx', 'lm', 'ls'], vif=['z', 'tz']),
     etape('La dévaluation de 10 % : les exportations progressent',
           'Les acheteurs étrangers réagissent fortement à la baisse des prix '
           'et les volumes exportés augmentent nettement : la valeur des '
           'exportations passe à 108.',
           add=[barre('bx1', '', 0.17, 0.62, 0.11, 'ac'),
                txt('vx1', '108', 0.145, 0.65, 'ac', taille=16, gras=True)],
           off=['bx'],
           vif=['bx1', 'vx1']),
     etape('Les importations augmentent moins vite que leur prix',
           'La facture d’importation se renchérit de 10 %, mais les volumes '
           'importés reculent de 6 % : 100 × 1,10 × 0,94, soit 103,4. La '
           'hausse de la valeur importée est contenue.',
           add=[barre('bm1', '', 0.42, 0.548, 0.11, 'ac2'),
                txt('vm1', '103,4', 0.385, 0.578, 'ac2', taille=16, gras=True)],
           off=['bm'],
           vif=['bm1', 'vm1']),
     etape('Le solde s’améliore',
           'Le solde commercial vaut 108 − 103,4 = +4,6. Les volumes ont '
           'réagi suffisamment pour l’emporter sur l’effet-prix : la '
           'dévaluation améliore le solde commercial.',
           add=[barre('bs1', '', 0.68, 0.49, 0.11, 'ok'),
                txt('vs1', '+4,6', 0.645, 0.52, 'ok', taille=17, gras=True)],
           vif=['bs1', 'vs1']),
     etape('La condition est vérifiée',
           'Dans ce cas, la somme des élasticités-prix en valeur absolue '
           'dépasse l’unité : les volumes réagissent assez pour que les '
           'effets-volume l’emportent sur les effets-prix.',
           add=[txt('tc1', '|εX| + |εM| > 1  →  le solde s’améliore', 0.1, 0.92,
                    'ok', taille=16, gras=True)],
           vif=['tc1']),
   ]},
  {'lib': 'Élasticités faibles (somme < 1)',
   'etapes': [
     etape('Le même point de départ',
           'Exportations et importations valent encore 100 et le solde est '
           'nul. On applique exactement la même dévaluation de 10 %.',
           on=['z', 'tz', 'lx', 'lm', 'ls'], vif=['z', 'tz']),
     etape('Les exportations progressent peu',
           'La demande étrangère réagit faiblement à la baisse des prix : la '
           'valeur des exportations ne monte qu’à 103. C’est le cas d’un pays '
           'spécialisé en compétitivité hors prix, où les acheteurs '
           'privilégient la qualité, l’innovation ou la marque.',
           add=[barre('bx2', '', 0.17, 0.465, 0.11, 'ac'),
                txt('vx2', '103', 0.145, 0.495, 'ac', taille=16, gras=True)],
           off=['bx'],
           vif=['bx2', 'vx2']),
     etape('La facture d’importation s’alourdit',
           'Les importations sont peu substituables — produits indispensables, '
           'intrants, énergie — donc les volumes diminuent à peine, tandis que '
           'leur prix a augmenté de 10 % : la valeur importée atteint 107,8.',
           add=[barre('bm2', '', 0.42, 0.598, 0.11, 'ac2'),
                txt('vm2', '107,8', 0.385, 0.628, 'ac2', taille=16, gras=True)],
           off=['bm'],
           vif=['bm2', 'vm2']),
     etape('Le solde se détériore',
           'Le solde vaut 103 − 107,8 = −4,8. Pour une dévaluation de même '
           'ampleur, le résultat est exactement inverse du cas précédent : la '
           'hausse de la facture d’importation l’emporte sur les gains à '
           'l’exportation.',
           add=[barre('bs2', '', 0.68, 0.33, 0.11, 'ko'),
                txt('vs2', '−4,8', 0.645, 0.27, 'ko', taille=17, gras=True)],
           vif=['bs2', 'vs2']),
     etape('La condition n’est pas vérifiée',
           'La somme des élasticités-prix en valeur absolue est inférieure à '
           'l’unité : les volumes réagissent insuffisamment, et la '
           'dévaluation dégrade le solde commercial au lieu de l’améliorer.',
           add=[txt('tc2', '|εX| + |εM| < 1  →  le solde se dégrade', 0.1, 0.92,
                    'ko', taille=16, gras=True)],
           vif=['tc2']),
   ]},
 ],
 pieges=[
  {'t': 'Ce n’est pas le change qui améliore le solde',
   'd': 'Ce n’est pas la baisse du taux de change qui garantit l’amélioration '
        'du solde commercial, mais la réaction des volumes échangés. La '
        'dévaluation n’est qu’un signal-prix.'},
  {'t': 'Le cas limite de la somme égale à un',
   'd': 'Les effets-volume compensent approximativement les effets-prix : '
        'l’effet global est nul dans le cadre simplifié. Le seuil est donc '
        'l’unité, pas zéro.'},
  {'t': 'Des chiffres qui illustrent, qui ne démontrent pas',
   'd': 'Les calculs présentés sont une illustration simplifiée et non une '
        'démonstration exacte du théorème pour une variation de 10 %. Les '
        'élasticités dépendent elles-mêmes de la spécialisation productive et '
        'de la structure des importations.'},
 ],
 main=[
  'Trace une horizontale repérant la base 100, le commerce équilibré.',
  'Dessine trois emplacements de barres en abscisse : exportations, '
  'importations, solde.',
  'Dans le premier cas, monte la barre des exportations à 108 et celle des '
  'importations à 103,4 ; déduis le solde + 4,6.',
  'Dans le second cas, reprends la même dévaluation : exportations à 103, '
  'importations à 107,8, solde − 4,8 sous la base.',
  'Écris sous chaque cas la condition correspondante sur la somme des '
  'élasticités.',
 ],
 phrase='Selon la condition de Marshall-Lerner, une dévaluation améliore le '
        'solde commercial lorsque la somme des élasticités-prix des demandes '
        'd’exportations et d’importations, prises en valeur absolue, est '
        'supérieure à l’unité : ce n’est donc pas la baisse du taux de change '
        'qui garantit le redressement du solde, mais la réaction des volumes '
        'échangés.',
 liens=[{'c': '26', 'b': 2112, 'l': 'La condition de Marshall-Lerner : les élasticités critiques'},
        {'c': '26', 'b': 2134, 'l': 'Des élasticités fortes ou faibles changent le résultat'},
        {'c': '26', 'b': 2153, 'l': 'Première condition : des exportations sensibles aux prix'},
        {'c': '26', 'b': 2169, 'l': 'Deuxième condition : des importations substituables'}],
 mots=['Marshall-Lerner', 'élasticités critiques', 'élasticité-prix',
       'dévaluation', 'compétitivité-prix', 'compétitivité hors prix'],
))

# --------------------------------------------------- données : euro-dollar
ED = [(0.0, 0.62), (0.07, 0.5), (0.14, 0.36), (0.22, 0.2), (0.3, 0.14),
      (0.38, 0.3), (0.46, 0.44), (0.54, 0.38), (0.62, 0.46), (0.7, 0.42),
      (0.78, 0.52), (0.86, 0.66), (0.94, 0.78), (1.0, 0.8)]

L.append(fiche(
 id='euro-dollar',
 t='L’euro face au dollar depuis son point bas de 2022',
 st='Lecture annotée d’un graphique historique : dates, valeurs, ruptures.',
 cat='ouverte', an=2, ch=['26'],
 type='donnees',
 q='Que lit-on exactement sur un graphique de cours de change, et que '
   'signifie économiquement l’appréciation de l’euro depuis 2022 ?',
 axes={'x': 'Années', 'y': 'Cours de l’euro', 'yu': 'dollars pour un euro',
       'gx': [[0.03, '2022'], [0.28, '2023'], [0.53, '2024'],
              [0.78, '2025'], [0.99, '2026']],
       'gy': [[0.14, '0,97'], [0.47, '1,08'], [0.8, '1,18']]},
 depart='Le cours de l’euro exprimé en dollars, au début de la période '
        'représentée.',
 hyp=['Le cours est donné en dollars pour un euro : une courbe qui monte '
      'signifie que l’euro s’apprécie.',
      'La trajectoire représentée est une allure, reconstruite à partir des '
      'deux repères chiffrés que donne le cours ; seuls ces deux repères, et '
      'le sens général du mouvement, sont des données.',
      'Le cours de change reflète les divergences de politiques monétaires, '
      'les crises, les anticipations et les comportements de recherche de '
      'sécurité, pas seulement les échanges de biens et services.'],
 pente=[{'s': 'Pente descendante', 'd': 'l’euro se déprécie : il faut moins '
         'de dollars pour l’obtenir.'},
        {'s': 'Pente ascendante', 'd': 'l’euro s’apprécie : il faut davantage '
         'de dollars pour l’obtenir, et donc moins d’euros pour obtenir un '
         'dollar.'}],
 src={'so': 'Cours de deuxième année, chapitre 6 — graphique du cours de '
            'l’euro en dollars commenté aux points 23 de la partie '
            '« Ouverture ». Les deux valeurs repères citées sont celles du '
            'cours ; la trajectoire intermédiaire est une allure.',
      'pe': '2022 — début 2026',
      'un': 'dollars des États-Unis pour un euro',
      'nb': 'Deux valeurs seulement sont chiffrées par le cours : le point '
            'bas de 2022 et le niveau du début de 2026. Les variations '
            'intermédiaires ne doivent pas être lues comme des données '
            'précises.'},
 fig={'series': [
   pol('ed', 'Euro en dollars', ED, 'ac', ep=3.4),
   lin('par', 'parité 1 dollar = 1 euro', 0.0, 0.17, 1.0, 0.17, 'gr', ep=1.6),
 ]},
 etapes=[
  etape('D’abord lire les axes et l’unité',
        'En abscisse, les années de 2022 au début de 2026. En ordonnée, le '
        'nombre de dollars nécessaires pour obtenir un euro. Sans cette '
        'unité, le sens de la courbe est indécidable.',
        on=['ed', 'par'], vif=['ed']),
  etape('Le point bas de 2022 : environ 0,97 dollar',
        'Le graphique fait apparaître une forte dépréciation de l’euro en '
        '2022 : le cours atteint environ 0,97 dollar pour un euro, soit un '
        'passage sous la parité — un euro valait alors moins d’un dollar.',
        add=[pt('bas', '0,97', 0.3, 0.14, 'ko'),
             rep('rbas', 0.3, 0.14, c='ko')],
        vif=['bas', 'rbas', 'par']),
  etape('Le redressement, avec des fluctuations',
        'L’euro se redresse ensuite, mais pas en ligne droite : la courbe '
        'alterne des phases de hausse et de repli. Une lecture honnête '
        'distingue la tendance de la volatilité, c’est-à-dire l’ampleur des '
        'variations autour de la trajectoire.',
        add=[fl('fup', 'tendance à l’appréciation', 0.34, 0.26, 0.9, 0.7, 'ok')],
        vif=['fup']),
  etape('Le niveau du début de 2026 : environ 1,18 dollar',
        'Le graphique indique une valeur proche de 1,18 dollar pour un euro '
        'au début de 2026. L’euro s’est donc apprécié face au dollar depuis '
        'son point bas de 2022 : l’écart entre les deux repères est la seule '
        'mesure sûre du mouvement.',
        add=[pt('haut', '1,18', 0.99, 0.8, 'ok'),
             rep('rhaut', 0.99, 0.8, c='ok')],
        vif=['haut', 'rhaut']),
  etape('Ce que l’appréciation produit',
        'Elle réduit le prix des importations facturées en dollars et limite '
        'l’inflation importée dans la zone euro ; elle renchérit en revanche '
        'les exportations européennes pour les acheteurs qui paient en '
        'dollars. Le graphique illustre un arbitrage, non un progrès.',
        add=[txt('t1', '+ : importations moins chères, moins d’inflation importée',
                 0.06, 0.95, 'ok', taille=14),
             txt('t2', '− : exportations renchéries pour les acheteurs en dollars',
                 0.06, 0.88, 'ko', taille=14)],
        vif=['t1', 't2']),
  etape('Pourquoi le commerce ne suffit pas à l’expliquer',
        'Les variations du change ne peuvent pas être expliquées uniquement '
        'par les échanges de biens et services : elles résultent aussi des '
        'mouvements internationaux de capitaux, des décisions des '
        'investisseurs et des anticipations financières.',
        vif=['ed']),
 ],
 pieges=[
  {'t': 'Le sens de la courbe dépend de la cotation',
   'd': 'En dollars pour un euro, une courbe qui monte est une appréciation '
        'de l’euro. En euros pour un dollar, la même appréciation ferait '
        'descendre la courbe. Toujours lire l’unité de l’ordonnée avant de '
        'conclure.'},
  {'t': 'Volatilité et mouvement de long terme',
   'd': 'Les variations peuvent être de faible ampleur et très rapides, ou '
        'importantes et persistantes. Confondre un soubresaut et une '
        'tendance est l’erreur de lecture la plus fréquente sur ce type de '
        'graphique.'},
  {'t': 'Un graphique ne démontre pas une causalité',
   'd': 'Observer une appréciation ne dit pas pourquoi elle a eu lieu. Le '
        'cours insiste ailleurs sur ce point : un graphique de change '
        'illustre un mécanisme mais ne suffit pas, à lui seul, à établir '
        'qu’une décision donnée l’a provoqué.'},
 ],
 main=[
  'Trace les axes et gradue-les : les années en abscisse, les dollars par '
  'euro en ordonnée — écris l’unité.',
  'Place l’horizontale de la parité, là où un euro vaut un dollar.',
  'Marque le point bas de 2022 sous cette horizontale, à environ 0,97, et '
  'annote-le.',
  'Marque le niveau du début de 2026 à environ 1,18, bien au-dessus, et '
  'annote-le.',
  'Relie les deux par une trajectoire irrégulière, puis trace la flèche de '
  'tendance et écris les deux effets, favorable et défavorable.',
 ],
 phrase='Le cours de l’euro, tombé à environ 0,97 dollar en 2022 avant de se '
        'redresser jusqu’à près de 1,18 dollar au début de 2026, montre que '
        'les mouvements de change traduisent des transformations profondes de '
        'la conjoncture financière internationale et qu’une appréciation '
        'constitue toujours un arbitrage : elle contient l’inflation importée '
        'mais renchérit les exportations.',
 liens=[{'c': '26', 'b': 3052, 'l': 'L’appréciation de l’euro face au dollar depuis son point bas de 2022'},
        {'c': '26', 'b': 253, 'l': 'L’évolution de l’euro face au dollar depuis 1999'},
        {'c': '26', 'b': 242, 'l': 'La volatilité du change'}],
 mots=['euro', 'dollar', 'cours de change', 'appréciation', 'volatilité',
       'inflation importée'],
))

# ------------------------------------------------------ données : le Forex
L.append(fiche(
 id='forex-volumes',
 t='L’essor du marché des changes',
 st='Des volumes multipliés par onze, très au-delà des besoins du commerce.',
 cat='ouverte', an=2, ch=['26'],
 type='donnees',
 q='Que révèle la croissance des volumes échangés sur le marché des changes '
   'quant à la financiarisation de l’économie mondiale ?',
 axes={'x': 'Années', 'y': 'Transactions de change',
       'yu': 'milliards de dollars par jour',
       'gy': [[0.07, '880'], [0.78, '9 600']]},
 depart='Le volume quotidien des transactions de change au début de la '
        'période, en 1992.',
 hyp=['Les montants sont des volumes quotidiens de transactions, non des '
      'stocks ni des soldes.',
      'Si les devises étaient principalement demandées pour régler les '
      'échanges commerciaux, les transactions de change devraient évoluer '
      'parallèlement aux échanges de biens et services.',
      'Les deux valeurs extrêmes sont celles du cours ; le profil '
      'intermédiaire n’est pas chiffré.'],
 pente=[{'s': 'Les deux barres', 'd': 'ce graphique compare deux niveaux '
         'séparés d’un peu plus de trois décennies ; il n’a pas de pente mais '
         'un rapport, celui de la multiplication par environ onze.'}],
 src={'so': 'Cours de deuxième année, chapitre 6 — données commentées au '
            'point 12 de la partie I, sur le développement du Forex. Seules '
            'les deux valeurs extrêmes et le facteur de multiplication sont '
            'des données du cours.',
      'pe': '1992 — 2025',
      'un': 'milliards de dollars échangés par jour',
      'nb': 'Le cours ne donne pas de valeurs intermédiaires : on ne peut '
            'donc pas lire sur ce graphique le rythme année par année, '
            'seulement l’ordre de grandeur du point de départ, celui du '
            'point d’arrivée et leur rapport.'},
 fig={'series': [
   barre('b92', '', 0.17, 0.07, 0.14, 'ac'),
   barre('b25', '', 0.62, 0.78, 0.14, 'ac2'),
   txt('l92', '1992', 0.135, -0.07, 'ac', taille=15, gras=True),
   txt('l25', '2025', 0.585, -0.07, 'ac2', taille=15, gras=True),
 ]},
 etapes=[
  etape('Le point de départ : 1992',
        'Le volume quotidien des transactions de change s’élève à environ '
        '880 milliards de dollars. C’est déjà considérable, mais la mesure '
        'n’a de sens que rapportée à ce qu’elle devient ensuite.',
        on=['b92', 'l92'],
        add=[txt('v92', '≈ 880', 0.125, 0.1, 'ac', taille=16, gras=True)],
        vif=['b92', 'v92']),
  etape('Le point d’arrivée : 2025',
        'Le volume atteint près de 9 600 milliards de dollars par jour. La '
        'barre est près de onze fois plus haute que la précédente : le '
        'montant échangé quotidiennement a été multiplié par environ onze en '
        'un peu plus de trois décennies.',
        on=['b25', 'l25'],
        add=[txt('v25', '≈ 9 600', 0.565, 0.81, 'ac2', taille=16, gras=True),
             fl('fx', '× 11 environ', 0.3, 0.3, 0.52, 0.66, 'ok')],
        vif=['b25', 'v25', 'fx']),
  etape('Pourquoi le commerce n’explique pas cette progression',
        'Si les devises étaient demandées surtout pour payer des échanges de '
        'biens et services, les transactions de change devraient suivre à peu '
        'près la même trajectoire que ces échanges. Or les données montrent '
        'une divergence considérable.',
        add=[txt('tdiv', 'les échanges de biens n’ont pas été multipliés par onze',
                 0.08, 0.95, 'jn', taille=14)],
        vif=['tdiv']),
  etape('Trois moteurs se cumulent',
        'L’essor du commerce international, la libéralisation des mouvements '
        'internationaux de capitaux et la multiplication des produits dérivés '
        'expliquent ensemble cette expansion : le premier seul n’y suffit '
        'pas.',
        add=[txt('t1', '1. mondialisation commerciale', 0.08, 0.56, 'ac', taille=14),
             txt('t2', '2. globalisation financière', 0.08, 0.48, 'ok', taille=14),
             txt('t3', '3. produits dérivés : couverture et spéculation',
                 0.08, 0.40, 'bl', taille=14)],
        off=['tdiv'],
        vif=['t1', 't2', 't3']),
  etape('Ce que les chiffres établissent — et ce qu’ils n’établissent pas',
        'Ils établissent que le Forex est devenu un marché mondial, '
        'dématérialisé, très liquide, dominé par les acteurs financiers, dont '
        'les volumes dépassent largement les besoins immédiats du commerce. '
        'Ils n’établissent pas la part exacte de la spéculation, que ces '
        'données ne distinguent pas.',
        vif=['b92', 'b25']),
 ],
 pieges=[
  {'t': 'Un volume quotidien n’est pas un flux annuel',
   'd': 'Comparer 9 600 milliards par jour à un PIB annuel n’a aucun sens. '
        'La seule comparaison légitime porte sur deux volumes quotidiens, ou '
        'sur deux flux de même périodicité.'},
  {'t': 'Un gros volume n’est pas forcément de la spéculation',
   'd': 'Les swaps de change et les opérations à terme servent largement à '
        'la couverture du risque de change. Le même instrument peut servir à '
        'se protéger ou à prendre position : le volume ne dit pas lequel des '
        'deux.'},
  {'t': 'Deux points ne font pas une trajectoire',
   'd': 'Le cours ne donne que 1992 et 2025. On peut en déduire un rapport, '
        'pas un rythme : affirmer que la croissance a été régulière serait '
        'ajouter au graphique ce qu’il ne contient pas.'},
 ],
 main=[
  'Trace les axes : les deux années en abscisse, les milliards de dollars par '
  'jour en ordonnée — écris l’unité et la périodicité.',
  'Dessine une petite barre pour 1992 et inscris ≈ 880 au-dessus.',
  'Dessine une barre environ onze fois plus haute pour 2025 et inscris '
  '≈ 9 600.',
  'Relie les deux par une flèche portant « × 11 environ ».',
  'Écris en marge les trois moteurs : mondialisation commerciale, '
  'globalisation financière, produits dérivés.',
 ],
 phrase='Le volume quotidien des transactions de change, passé d’environ '
        '880 milliards de dollars en 1992 à près de 9 600 milliards en 2025, '
        'a été multiplié par onze en un peu plus de trois décennies, soit '
        'bien plus vite que les échanges de biens et services : cette '
        'divergence révèle que le marché des changes s’est financiarisé et '
        'qu’il sert désormais d’abord à la circulation mondiale des capitaux.',
 liens=[{'c': '26', 'b': 394, 'l': 'Le développement spectaculaire du Forex'},
        {'c': '26', 'b': 400, 'l': 'Une déconnexion croissante entre transactions financières et échanges réels'},
        {'c': '26', 'b': 404, 'l': 'Trois mécanismes expliquent l’expansion du marché des changes'}],
 mots=['Forex', 'financiarisation', 'globalisation financière',
       'produits dérivés', 'volumes de transactions'],
))
