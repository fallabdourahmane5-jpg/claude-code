# -*- coding: utf-8 -*-
"""Courbes du chapitre 5 — analyse microéconomique (II) : les défaillances
du marché."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone,
                     inter, y_de, x_de, bouge)

L = []

# ------------------------------------------------------- monopole naturel
def _cm_monopole():
    out = []
    q = 0.14
    while q <= 0.97:
        out.append((round(q, 4), round(0.12 / q + 0.12, 4)))
        q += 0.055
    return [p for p in out if p[1] <= 1.05]


CMN = _cm_monopole()
DEMM = (0.05, 0.95, 0.98, 0.06)
RMM = (0.05, 0.9023, 0.52, 0.0)

L.append(fiche(
 id='monopole-naturel',
 t='Le monopole naturel',
 st='Quand une seule entreprise produit moins cher que plusieurs — et '
    'pourquoi c’est une défaillance.',
 cat='micro', an=1, ch=['5'],
 type='schema',
 q='Pourquoi un monopole naturel empêche-t-il l’égalité entre le prix et le '
   'coût marginal, et quelles solutions l’État peut-il mettre en œuvre ?',
 axes={'x': 'Quantité produite Q', 'y': 'Prix et coûts'},
 depart='Un secteur à très fortes charges fixes — eau, électricité, gaz, '
        'chemins de fer, télécommunications, réseaux.',
 hyp=['Les coûts fixes sont très élevés et les coûts marginaux très faibles : '
      'les rendements sont croissants.',
      'Il en résulte qu’une seule entreprise produit à moindre coût que '
      'plusieurs entreprises concurrentes.',
      'Pour être efficace, une allocation exige l’égalité entre le prix et le '
      'coût marginal : c’est cette condition que le monopole naturel rend '
      'impossible à atteindre sans perte.'],
 pente=[{'s': 'Coût moyen', 'd': 'strictement décroissant : le coût fixe très '
         'élevé s’écrase sur une production croissante et le coût marginal, '
         'très faible, ne le fait jamais remonter. C’est la signature du '
         'monopole naturel.'},
        {'s': 'Coût marginal', 'd': 'quasiment constant et très bas : '
         'produire une unité de plus sur un réseau déjà construit ne coûte '
         'presque rien.'},
        {'s': 'Demande', 'd': 'décroissante : contrairement à une firme en '
         'concurrence, le monopole fait face à la demande du marché tout '
         'entier.'}],
 fig={'series': [
   pol('cm', 'Coût moyen (CM)', CMN, 'ac', ep=3.2, lp=[0.3, 0.72]),
   lin('cmg', 'Coût marginal (Cm)', 0.05, 0.12, 0.98, 0.12, 'ok', ep=2.6,
       lp=[0.62, 0.06]),
   lin('d', 'Demande', *DEMM, c='ac2', ep=3, lp=[0.86, 0.3]),
 ]},
 etapes=[
  etape('Un coût moyen qui ne remonte jamais',
        'Les charges fixes sont considérables et le coût marginal presque '
        'nul : le coût moyen décroît sur toute la plage de production. Plus '
        'l’entreprise produit, moins chaque unité lui coûte.',
        on=['cm', 'cmg'], vif=['cm', 'cmg']),
  etape('Pourquoi une seule entreprise s’impose',
        'Si deux entreprises se partageaient le marché, chacune produirait '
        'moins et supporterait un coût moyen plus élevé. Le monopole n’est '
        'pas ici le fruit d’une manœuvre : il découle de la structure des '
        'coûts.',
        add=[txt('tn', 'rendements croissants → une seule firme',
                 0.3, 0.9, 'ac', taille=15, gras=True)],
        vif=['tn']),
  etape('L’optimum collectif : P = Cm',
        'L’allocation serait efficace si le prix égalait le coût marginal. '
        'Ce point existe bien sur la demande, très à droite, avec un prix '
        'très bas et une quantité élevée.',
        on=['d'],
        add=[pt('eo', 'A', 0.9173, 0.12, 'ok'),
             rep('ro', 0.9173, 0.12, c='ok'),
             txt('tqa', 'Q_A', 0.88, 0.04, 'ok', taille=14, gras=True)],
        off=['tn'],
        vif=['d', 'eo', 'ro', 'tqa']),
  etape('Mais à ce prix l’entreprise perd de l’argent',
        'À cette quantité, le coût moyen reste nettement supérieur au coût '
        'marginal, donc au prix. Vendre au coût marginal ne couvre pas les '
        'charges fixes : l’entreprise est structurellement déficitaire.',
        add=[pt('cx', '', 0.9173, round(0.12 / 0.9173 + 0.12, 4), 'ko'),
             fl('fp', 'perte', 0.9173, 0.23, 0.9173, 0.14, 'ko')],
        vif=['cx', 'fp']),
  etape('Le blocage structurel',
        'Le marché ne peut pas résoudre seul ce problème : aucune entreprise '
        'privée ne produira durablement à perte. C’est ce blocage qui fait du '
        'monopole naturel une véritable défaillance de marché.',
        add=[txt('tb', 'aucune firme ne produira à perte → défaillance',
                 0.18, 0.95, 'ko', taille=15, gras=True)],
        vif=['tb']),
  etape('Laissé à lui-même, le monopole fait pire',
        'Sans régulation, le monopole choisit la quantité qui maximise son '
        'profit, bien en deçà de l’optimum : prix trop élevé, quantité trop '
        'faible. C’est le reproche central adressé au monopole.',
        add=[lin('rm', 'Recette marginale', *RMM, c='jn', ep=2.4,
                 lp=[0.2, 0.3]),
             pt('em', 'M', 0.4587, 0.5589, 'ko'),
             rep('rm2', 0.4587, 0.5589, lx='Q_M', ly='P_M', c='ko')],
        off=['tb', 'fp', 'cx'],
        vif=['rm', 'em', 'rm2']),
  etape('Première solution : la tarification au coût moyen',
        'L’État peut imposer un prix égal au coût moyen : l’entreprise couvre '
        'exactement ses coûts, sans profit ni perte. La quantité est plus '
        'élevée qu’en monopole libre, mais reste inférieure à l’optimum.',
        add=[pt('ec', 'B', 0.7501, 0.2801, 'ac'),
             rep('rc', 0.7501, 0.2801, lx='Q_B', ly='P=CM', c='ac')],
        off=['rm', 'em', 'rm2'],
        vif=['ec', 'rc']),
  etape('Les autres solutions publiques',
        'L’État peut aussi nationaliser l’entreprise, réguler les prix par un '
        'prix plafond, ou verser une subvention qui permet de tarifer au coût '
        'marginal en couvrant la perte. L’intervention publique est '
        'indispensable.',
        add=[txt('ts', 'nationalisation · prix plafond · P = CM · subvention pour P = Cm',
                 0.06, 0.95, 'bl', taille=14, gras=True)],
        vif=['ts', 'eo', 'ec']),
 ],
 pieges=[
  {'t': 'Monopole naturel n’est pas monopole d’innovation',
   'd': 'Le monopole naturel vient de la structure des coûts et dure tant que '
        'cette structure dure. Le monopole d’innovation vient d’un brevet, '
        'droit de propriété intellectuelle limité dans le temps — vingt ans '
        'au plus — et sur un territoire donné : il est temporaire.'},
  {'t': 'La défaillance n’est pas « le monopole est méchant »',
   'd': 'C’est l’impossibilité d’atteindre P = Cm sans perte qui constitue la '
        'défaillance. Le raisonnement est technique, pas moral : même une '
        'entreprise bienveillante ne pourrait pas tarifer au coût marginal '
        'sans subvention.'},
  {'t': 'Trois points, trois logiques',
   'd': 'Le point de monopole libre maximise le profit, le point P = CM '
        'assure l’équilibre budgétaire, le point P = Cm réalise l’optimum '
        'collectif. Confondre ces trois quantités rend la comparaison '
        'impossible.'},
 ],
 main=[
  'Trace les axes : les quantités en abscisse, les prix et coûts en ordonnée.',
  'Trace un coût moyen qui décroît sans jamais remonter, et un coût marginal '
  'horizontal très bas en dessous.',
  'Trace la demande décroissante, puis marque le point où elle coupe le coût '
  'marginal : c’est l’optimum P = Cm.',
  'Remonte verticalement jusqu’au coût moyen et hachure l’écart : c’est la '
  'perte par unité.',
  'Marque enfin les deux autres points : l’intersection de la demande et du '
  'coût moyen, et le point de monopole, plus à gauche et plus haut.',
 ],
 phrase='Le monopole naturel résulte de coûts fixes très élevés et de coûts '
        'marginaux très faibles qui rendent le coût moyen continûment '
        'décroissant : une seule entreprise produit alors à moindre coût que '
        'plusieurs, mais la tarification au coût marginal — condition de '
        'l’allocation efficace — la condamnerait à des pertes, ce qui rend '
        'l’intervention publique indispensable.',
 liens=[{'c': '5', 'b': 50, 'l': 'Le monopole naturel, véritable défaillance de marché'},
        {'c': '5', 'b': 63, 'l': 'Pourquoi le monopole naturel est une défaillance'},
        {'c': '5', 'b': 70, 'l': 'Le rôle de l’État face au monopole naturel'},
        {'c': '5', 'b': 77, 'l': 'Les monopoles d’innovation, temporaires'},
        {'c': '5', 'b': 135, 'l': 'Prix, recette marginale et coût marginal en monopole'}],
 mots=['monopole naturel', 'rendements croissants', 'coûts fixes',
       'tarification au coût marginal', 'nationalisation', 'brevet'],
))

# ----------------------------------------------------------- externalités
CMP = (0.05, 0.08, 0.95, 0.80)
CMSN = (0.05, 0.26, 0.95, 0.98)
CMSP = (0.18, 0.004, 0.95, 0.62)
DEX = (0.05, 0.92, 0.95, 0.12)
EMAR = (0.5474, 0.4779)
EOPT = (0.4408, 0.5726)
EOPP = (0.6539, 0.3831)

L.append(fiche(
 id='externalites',
 t='Externalités négatives et positives',
 st='Le marché se trompe de prix parce qu’il ignore un coût — ou un bénéfice.',
 cat='micro', an=1, ch=['5'],
 type='schema',
 q='Pourquoi un marché laissé à lui-même produit-il trop d’un bien polluant '
   'et pas assez d’un bien socialement bénéfique ?',
 axes={'x': 'Quantité', 'y': 'Prix et coûts'},
 depart='Un marché à l’équilibre, où l’offre ne reflète que les coûts '
        'supportés par les entreprises elles-mêmes.',
 hyp=['Une externalité est la répercussion, positive ou négative, de '
      'l’activité d’un agent sur un autre, sans contrepartie monétaire.',
      'L’offre de marché repose sur le coût marginal privé : le coût '
      'effectivement supporté par l’entreprise.',
      'Le coût marginal social est le coût pour la collectivité. « Social » '
      'signifie ici collectif, au sens microéconomique — pas social au sens '
      'courant.'],
 pente=[{'s': 'Offre (coût marginal privé)', 'd': 'croissante : produire une '
         'unité de plus coûte plus cher à la marge.'},
        {'s': 'Coût marginal social', 'd': 'parallèle au coût privé, décalé '
         'vers le haut lorsqu’il existe un coût caché, vers le bas lorsqu’il '
         'existe un bénéfice non rémunéré. L’écart entre les deux courbes est '
         'l’externalité elle-même.'}],
 fig={'series': [
   lin('cmp', 'Coût marginal privé (CmP)', *CMP, c='ac', ep=3,
       lp=[0.84, 0.72]),
   lin('d', 'Demande', *DEX, c='ac2', ep=3, lp=[0.86, 0.22]),
   pt('e', 'E', EMAR[0], EMAR[1], 'ac2'),
   rep('re', EMAR[0], EMAR[1], lx='Q_E', ly='P_E', c='ac2'),
 ]},
 variantes=[
  {'lib': 'Externalité négative',
   'etapes': [
     etape('L’équilibre observé sur le marché',
           'L’offre repose sur le coût marginal privé : le coût supporté par '
           'l’entreprise seule, qui ne comprend ni la pollution ni les '
           'nuisances. Le marché s’équilibre en E.',
           on=['cmp', 'd', 'e', 're'], vif=['e', 're']),
     etape('Le prix est artificiellement trop bas',
           'Il ne couvre que les coûts privés, pas le coût réel de la '
           'production pour la société. Une partie du coût est cachée : le '
           'cours parle d’un « mensonge économique ».',
           add=[txt('tm', 'prix trop bas : une partie du coût est cachée',
                    0.2, 0.08, 'ko', taille=14, gras=True)],
           vif=['tm']),
     etape('Le coût marginal social est au-dessus',
           'Le vrai coût pour la collectivité ajoute au coût privé le coût '
           'externe. La courbe du coût marginal social se place donc '
           'au-dessus de celle du coût privé, l’écart mesurant l’externalité.',
           add=[lin('cms', 'Coût marginal social (CmS)', *CMSN, c='ko', ep=3,
                    lp=[0.44, 0.92]),
                fl('fe', 'externalité', 0.50, 0.62, 0.50, 0.80, 'ko')],
           off=['tm'],
           vif=['cms', 'fe']),
     etape('L’optimum collectif se situe plus à gauche',
           'En tenant compte du coût social, l’équilibre souhaitable associe '
           'un prix plus élevé et une quantité plus faible : moins produit, '
           'mais au prix vrai.',
           add=[pt('eo', 'E*', EOPT[0], EOPT[1], 'ok'),
                rep('ro', EOPT[0], EOPT[1], lx='Q*', ly='P*', c='ok')],
           off=['fe'],
           vif=['eo', 'ro']),
     etape('La conclusion : surproduction',
           'L’externalité négative conduit à une surproduction et à une '
           'sous-évaluation du prix. Le marché n’alloue pas correctement les '
           'ressources : il produit trop d’un bien socialement coûteux.',
           add=[zone('ps', '',
                     [(EOPT[0], EOPT[1]), (EMAR[0], EMAR[1]),
                      (EMAR[0], 0.6579)], 'ko'),
                txt('tps', 'perte collective', 0.16, 0.2, 'ko', taille=14,
                    gras=True),
                fl('fq', 'trop produit', EOPT[0], 0.06, EMAR[0], 0.06, 'ko')],
           vif=['ps', 'tps', 'fq']),
     etape('La réponse de Pigou',
           'Puisque le coût n’est pas payé par celui qui le provoque, l’État '
           'peut le lui faire payer : c’est la logique de la taxe, qui '
           'relève le coût privé jusqu’au coût social. Un coût ne devrait '
           'jamais être gratuit.',
           add=[txt('tp', 'taxe : ramener le coût privé au coût social',
                    0.14, 0.95, 'bl', taille=15, gras=True)],
           off=['fq'],
           vif=['tp']),
   ]},
  {'lib': 'Externalité positive',
   'etapes': [
     etape('Le même équilibre de départ',
           'Le marché raisonne toujours avec le coût marginal privé et '
           's’équilibre au même point E. La différence est ailleurs : '
           'l’activité crée ici un avantage pour d’autres, sans être payée '
           'pour cela.',
           on=['cmp', 'd', 'e', 're'], vif=['e', 're']),
     etape('Un bénéfice réel mais gratuit',
           'La proximité d’une université pour un commerce, par exemple : il '
           'existe un gain réel pour la collectivité, mais personne ne le '
           'facture. Le marché l’ignore donc totalement.',
           add=[txt('tb', 'un bénéfice collectif que personne ne facture',
                    0.2, 0.08, 'ok', taille=14, gras=True)],
           vif=['tb']),
     etape('Le coût marginal social est en dessous',
           'Pour la société, le coût réel est plus faible que ce que supporte '
           'l’entreprise seule : on retranche le bénéfice externe. La courbe '
           'du coût social passe donc sous celle du coût privé.',
           add=[lin('cms', 'Coût marginal social (CmS)', *CMSP, c='ok', ep=3,
                    lp=[0.86, 0.5]),
                fl('fe', 'bénéfice externe', 0.5, 0.44, 0.5, 0.26, 'ok')],
           off=['tb'],
           vif=['cms', 'fe']),
     etape('L’optimum collectif se situe plus à droite',
           'En tenant compte du bénéfice externe, l’équilibre souhaitable '
           'associe une quantité plus élevée et un prix plus faible : il '
           'faudrait produire davantage.',
           add=[pt('eo', 'E*', EOPP[0], EOPP[1], 'bl'),
                rep('ro', EOPP[0], EOPP[1], lx='Q*', ly='P*', c='bl')],
           off=['fe'],
           vif=['eo', 'ro']),
     etape('La conclusion : sous-production',
           'L’externalité positive conduit à une sous-production et à une '
           'sur-évaluation du prix. Le marché empêche une activité '
           'socialement bénéfique de se développer suffisamment.',
           add=[fl('fq', 'pas assez produit', EMAR[0], 0.06, EOPP[0], 0.06,
                   'bl')],
           vif=['fq']),
     etape('La réponse symétrique',
           'Puisque le bénéfice n’est pas rémunéré, l’État peut le rémunérer : '
           'c’est la logique de la subvention, qui abaisse le coût privé '
           'jusqu’au coût social et pousse la production vers l’optimum.',
           add=[txt('tp', 'subvention : rémunérer le bénéfice externe',
                    0.14, 0.95, 'bl', taille=15, gras=True)],
           off=['fq'],
           vif=['tp']),
   ]},
 ],
 pieges=[
  {'t': 'Le sens du décalage se déduit, il ne se retient pas',
   'd': 'Coût caché non payé : le coût social est AU-DESSUS du coût privé. '
        'Bénéfice gratuit non rémunéré : le coût social est EN DESSOUS. '
        'Reconstruire le raisonnement vaut mieux que mémoriser le dessin.'},
  {'t': '« Social » signifie collectif',
   'd': 'Le coût marginal social n’a rien à voir avec les questions sociales '
        'au sens courant : il désigne le coût pour l’ensemble de la '
        'collectivité, entreprise comprise.'},
  {'t': 'Les deux cas sont des défaillances',
   'd': 'On retient souvent que l’externalité positive est « bonne ». Elle '
        'est bénéfique, mais elle constitue tout autant une défaillance de '
        'marché, puisque le marché en produit trop peu.'},
 ],
 main=[
  'Trace les axes, une offre croissante — le coût marginal privé — et une '
  'demande décroissante ; marque l’équilibre de marché E.',
  'Pour l’externalité négative, trace une parallèle au-dessus de l’offre : '
  'c’est le coût marginal social.',
  'Marque son intersection avec la demande : E* est à gauche et plus haut — '
  'écris « surproduction ».',
  'Pour l’externalité positive, trace la parallèle en dessous et marque E* à '
  'droite et plus bas — écris « sous-production ».',
  'Dans les deux cas, hachure le triangle compris entre les deux équilibres : '
  'c’est la perte collective.',
 ],
 phrase='En présence d’une externalité négative, le coût marginal privé est '
        'inférieur au coût marginal social, ce qui conduit à une '
        'surproduction et à un prix trop faible par rapport à l’optimum '
        'collectif ; en présence d’une externalité positive, le coût marginal '
        'privé est au contraire supérieur au coût marginal social, ce qui '
        'conduit à une sous-production et à un prix trop élevé.',
 liens=[{'c': '5', 'b': 487, 'l': 'Définition générale d’une externalité'},
        {'c': '5', 'b': 563, 'l': 'Le faux prix du marché dans une externalité négative'},
        {'c': '5', 'b': 582, 'l': 'L’externalité positive : un bénéfice non rémunéré'},
        {'c': '5', 'b': 542, 'l': 'Le résumé : coût privé, coût social et optimum'}],
 mots=['externalité', 'Pigou', 'coût marginal social', 'coût marginal privé',
       'surproduction', 'sous-production', 'taxe', 'subvention'],
))

# ------------------------------------------------- prix plafond et plancher
OPP = (0.08, 0.1, 0.95, 0.9)
DPP = (0.08, 0.92, 0.95, 0.1)
EPP = (0.5204, 0.5050)

L.append(fiche(
 id='prix-plafond-plancher',
 t='Prix plafond et prix plancher',
 st='Deux interventions opposées, un même résultat : une perte sèche.',
 cat='micro', an=1, ch=['5'],
 type='schema',
 q='Que se passe-t-il quand l’État fixe un prix minimum ou un prix maximum '
   'qui s’écarte du prix d’équilibre, et qui y gagne ou y perd ?',
 axes={'x': 'Quantités', 'y': 'Prix'},
 depart='Un marché concurrentiel à l’équilibre en E, avant toute '
        'intervention de l’État.',
 hyp=['L’intervention n’a d’effet que si elle est contraignante : un prix '
      'plancher inférieur au prix d’équilibre, ou un prix plafond supérieur, '
      'ne change rien et le marché fonctionne normalement.',
      'La quantité réellement échangée est toujours la plus petite des deux : '
      'on ne peut ni vendre ce que personne n’achète, ni acheter ce qui n’est '
      'pas produit.',
      'On raisonne en équilibre partiel : le reste de l’économie est supposé '
      'inchangé.'],
 pente=[{'s': 'Offre', 'd': 'croissante : plus le prix est élevé, plus les '
         'producteurs souhaitent vendre.'},
        {'s': 'Demande', 'd': 'décroissante : plus le prix est élevé, moins '
         'les consommateurs souhaitent acheter.'},
        {'s': 'Le côté court', 'd': 'c’est lui qui fixe la quantité échangée, '
         'et c’est là que naît la perte sèche.'}],
 fig={'series': [
   lin('o', 'Offre', *OPP, c='ac', ep=3.2, lp=[0.9, 0.78]),
   lin('d', 'Demande', *DPP, c='ac2', ep=3.2, lp=[0.9, 0.2]),
   pt('e', 'E', EPP[0], EPP[1], 'ok'),
   rep('re', EPP[0], EPP[1], lx='Q_E', ly='P_E', c='ok'),
 ]},
 variantes=[
  {'lib': 'Prix plancher',
   'etapes': [
     etape('L’équilibre concurrentiel',
           'Sans intervention, le marché s’équilibre en E : un prix P_E et '
           'une quantité Q_E. C’est la référence par rapport à laquelle on '
           'mesurera tous les écarts.',
           on=['o', 'd', 'e', 're'], vif=['e', 're']),
     etape('L’État fixe un prix minimum au-dessus de l’équilibre',
           'Un prix plancher est un prix minimum sous lequel il est interdit '
           'de vendre : le SMIC sur le marché du travail, les prix garantis '
           'agricoles de la PAC. Il n’est contraignant que s’il dépasse le '
           'prix d’équilibre.',
           add=[lin('pp', 'Prix plancher', 0.0, 0.68, 1.0, 0.68, 'ko', ep=2.6,
                    lp=[0.2, 0.72])],
           vif=['pp']),
     etape('Les producteurs offrent beaucoup, les acheteurs demandent peu',
           'À ce prix artificiellement élevé, la quantité offerte dépasse '
           'largement la quantité demandée. Il y a excès d’offre, c’est-à-dire '
           'surproduction.',
           add=[pt('qo', '', 0.7108, 0.68, 'ac'),
                pt('qd', '', 0.3346, 0.68, 'ac2'),
                fl('fx', 'excès d’offre', 0.3346, 0.78, 0.7108, 0.78, 'ko')],
           vif=['qo', 'qd', 'fx']),
     etape('La quantité échangée tombe du côté court',
           'On ne vend que ce qui trouve preneur : la quantité échangée est '
           'celle de la demande, inférieure à Q_E. On produit Q₀ au lieu de '
           'Q_E : ce n’est ni la bonne quantité, ni le bon prix.',
           add=[rep('rq', 0.3346, 0.68, lx='Q₀', c='ko')],
           off=['fx'],
           vif=['rq']),
     etape('Le gaspillage des ressources',
           'Les quantités produites en trop ne trouvent pas preneur : stocks '
           'détruits de lait, de beurre ou de céréales sur les marchés '
           'agricoles ; travailleurs sans emploi sur le marché du travail.',
           add=[txt('tg', 'stocks invendus · chômage', 0.52, 0.86, 'ko',
                    taille=14, gras=True)],
           vif=['tg']),
     etape('La perte sèche',
           'Le triangle compris entre l’offre, la demande et la quantité '
           'échangée mesure la richesse collective qui disparaît : personne '
           'ne la récupère, ni les producteurs, ni les consommateurs.',
           add=[zone('ps', 'perte sèche',
                     [(0.3346, 0.68), (0.3346, 0.3340), EPP], 'ko')],
           off=['tg'],
           vif=['ps']),
     etape('La distorsion des surplus',
           'Le surplus du producteur augmente — il s’empare d’une partie du '
           'surplus du consommateur — celui du consommateur diminue, et le '
           'surplus total baisse. S’y ajoute une incitation à l’illégalité : '
           'travail au noir, paiement en dessous du SMIC.',
           add=[txt('td', 'surplus producteur ↑ · consommateur ↓ · total ↓',
                    0.12, 0.95, 'jn', taille=14, gras=True)],
           vif=['td']),
     etape('La nuance du monopsone',
           'Le prix plancher n’est pas toujours néfaste : analysant la PAC, '
           'l’Institut des politiques publiques souligne qu’il peut être '
           'efficace en situation de monopsone, lorsque c’est l’acheteur qui '
           'devient faiseur de prix.',
           add=[txt('tmo', 'monopsone : l’acheteur est price maker',
                    0.12, 0.88, 'bl', taille=14, gras=True)],
           off=['td'],
           vif=['tmo']),
   ]},
  {'lib': 'Prix plafond',
   'etapes': [
     etape('Le même équilibre concurrentiel',
           'On repart exactement du même marché, du même point E : seule '
           'l’intervention publique change de sens. C’est ce qui permet de '
           'comparer les deux dispositifs.',
           on=['o', 'd', 'e', 're'], vif=['e', 're']),
     etape('L’État fixe un prix maximum en dessous de l’équilibre',
           'Un prix plafond est un prix maximum au-dessus duquel il est '
           'interdit de vendre : encadrement des loyers, prix alimentaires en '
           'période de crise. Il n’est contraignant que s’il est inférieur au '
           'prix d’équilibre.',
           add=[lin('pf', 'Prix plafond', 0.0, 0.33, 1.0, 0.33, 'ko', ep=2.6,
                    lp=[0.2, 0.27])],
           vif=['pf']),
     etape('Les acheteurs demandent beaucoup, les producteurs offrent peu',
           'À ce prix artificiellement bas, la quantité demandée dépasse '
           'largement la quantité offerte : il manque des biens sur le '
           'marché. C’est la pénurie.',
           add=[pt('qo', '', 0.3302, 0.33, 'ac'),
                pt('qd', '', 0.7060, 0.33, 'ac2'),
                fl('fx', 'pénurie', 0.3302, 0.22, 0.7060, 0.22, 'ko')],
           vif=['qo', 'qd', 'fx']),
     etape('La quantité échangée tombe du côté court',
           'On n’achète que ce qui est produit : la quantité échangée est '
           'celle de l’offre, inférieure à Q_E. Le marché du logement '
           'parisien en donne l’image — beaucoup de locataires, pas assez de '
           'logements.',
           add=[rep('rq', 0.3302, 0.33, lx='Q₁', c='ko')],
           off=['fx'],
           vif=['rq']),
     etape('Moins d’échanges bénéfiques',
           'Des échanges qui auraient profité aux deux parties n’ont pas '
           'lieu : c’est une richesse perdue pour la collectivité, et une '
           'inefficacité globale.',
           add=[txt('tg', 'des échanges profitables n’ont pas lieu',
                    0.46, 0.14, 'ko', taille=14, gras=True)],
           vif=['tg']),
     etape('La perte sèche, à nouveau',
           'Le même triangle apparaît, entre l’offre, la demande et la '
           'quantité échangée. Le dispositif est inverse, le résultat '
           'collectif est de même nature.',
           add=[zone('ps', 'perte sèche',
                     [(0.3302, 0.6842), (0.3302, 0.33), EPP], 'ko')],
           off=['tg'],
           vif=['ps']),
     etape('La distorsion des surplus, inversée',
           'Cette fois le surplus du consommateur augmente et celui du '
           'producteur diminue, mais le surplus total baisse encore. '
           'S’ajoutent l’économie illégale — loyers au noir, dessous-de-table '
           '— et la dégradation de la qualité, faute d’entretien.',
           add=[txt('td', 'surplus consommateur ↑ · producteur ↓ · total ↓',
                    0.12, 0.95, 'jn', taille=14, gras=True)],
           vif=['td']),
     etape('Le bilan commun',
           'Dans les deux cas : allocation sous-optimale, perte sèche, '
           'inefficacité économique. Lorsque l’État impose un prix '
           'contraignant, le marché s’éloigne de l’équilibre concurrentiel et '
           'la richesse collective diminue.',
           add=[txt('tb', 'deux dispositifs opposés, une même perte sèche',
                    0.14, 0.88, 'ac', taille=15, gras=True)],
           off=['td'],
           vif=['tb', 'ps']),
   ]},
 ],
 pieges=[
  {'t': 'Un prix administré non contraignant ne fait rien',
   'd': 'Un prix plancher sous l’équilibre, ou un prix plafond au-dessus, '
        'n’a aucun effet : le marché s’équilibre comme avant. Le dessiner du '
        'mauvais côté de l’équilibre annule tout le raisonnement.'},
  {'t': 'Plancher au-dessus, plafond en dessous',
   'd': 'Contre-intuitif mais logique : un prix « plancher » empêche de '
        'descendre, il se trace donc au-dessus de l’équilibre ; un prix '
        '« plafond » empêche de monter, il se trace en dessous.'},
  {'t': 'La quantité échangée n’est jamais la plus grande des deux',
   'd': 'C’est toujours le côté court qui l’emporte — l’offre en cas de '
        'pénurie, la demande en cas d’excès d’offre. Lire la quantité du '
        'mauvais côté fait disparaître la perte sèche.'},
 ],
 main=[
  'Trace les axes, l’offre croissante, la demande décroissante et marque '
  'l’équilibre E.',
  'Trace une horizontale au-dessus de P_E : c’est le prix plancher ; lis les '
  'deux quantités et marque l’excès d’offre.',
  'Entoure la plus petite des deux : c’est la quantité échangée, et hachure '
  'le triangle jusqu’à E — la perte sèche.',
  'Recommence avec une horizontale en dessous de P_E : c’est le prix plafond, '
  'et cette fois c’est l’offre qui est le côté court.',
  'Écris sous chaque cas le sens de variation des trois surplus : '
  'consommateur, producteur, total.',
 ],
 phrase='Lorsque l’État impose un prix plancher au-dessus du prix '
        'd’équilibre ou un prix plafond en dessous, la quantité échangée est '
        'fixée par le côté court du marché et devient inférieure à la '
        'quantité d’équilibre : il en résulte dans les deux cas une '
        'allocation sous-optimale, une perte sèche que personne ne récupère '
        'et une diminution du surplus total, même si la redistribution entre '
        'producteurs et consommateurs est de sens opposé.',
 liens=[{'c': '5', 'b': 807, 'l': 'Prix plancher, prix plafond et allocation sous-optimale'},
        {'c': '5', 'b': 821, 'l': 'Le prix plancher et ses effets'},
        {'c': '5', 'b': 860, 'l': 'Le prix plafond et ses effets'},
        {'c': '5', 'b': 898, 'l': 'La comparaison synthétique et la conclusion'},
        {'c': '5', 'b': 806, 'l': 'La nuance du monopsone'}],
 mots=['prix plafond', 'prix plancher', 'perte sèche', 'pénurie',
       'surproduction', 'SMIC', 'encadrement des loyers', 'surplus'],
))
