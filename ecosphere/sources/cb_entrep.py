# -*- coding: utf-8 -*-
"""Courbes des chapitres 9, 22, 23 et 24 — entreprises, chaînes de valeur,
commerce international et intégration régionale."""

from cb_base import (fiche, etape, lin, pol, pt, fl, txt, rep, zone, barre,
                     en_u, courbe_dec, courbe_cro, inter, y_de, x_de, bouge)

L = []

# ------------------------------------------------------- courbe du sourire
SOUR = en_u(0.05, 0.97, 0.86, 0.22, n=15, creux=0.5)
SOUR2 = en_u(0.05, 0.97, 0.96, 0.1, n=15, creux=0.5)

L.append(fiche(
 id='courbe-sourire',
 t='La courbe du sourire de Stan Shih',
 st='Où la valeur se crée le long d’une chaîne de valeur mondiale.',
 cat='entreprise', an=2, ch=['21', '22'],
 type='schema',
 q='Pourquoi la valeur ajoutée se concentre-t-elle aux deux extrémités d’une '
   'chaîne de valeur mondiale et non au moment de la fabrication ?',
 axes={'x': 'Étapes de la chaîne de valeur', 'y': 'Valeur ajoutée créée'},
 depart='Une chaîne de valeur complète, de la recherche et du développement '
        'jusqu’aux services après-vente.',
 hyp=['En abscisse figurent les étapes successives de la chaîne de valeur ; '
      'en ordonnée, la valeur ajoutée créée à chaque étape.',
      'La localisation internationale des tâches reflète les avantages '
      'comparatifs : les activités intensives en qualification restent '
      'davantage dans les pays avancés.',
      'Le critère d’implantation diffère selon l’étape : qualification en '
      'amont et en aval, coût salarial unitaire au centre.'],
 pente=[{'s': 'Branche gauche descendante', 'd': 'la recherche, le '
         'développement et la conception créent beaucoup de valeur ; en '
         's’approchant de la fabrication, la valeur créée diminue.'},
        {'s': 'Branche droite montante', 'd': 'après la production, le '
         'marketing et les services recréent de la valeur, et de plus en '
         'plus à mesure qu’on s’éloigne de l’assemblage.'},
        {'s': 'Le creux', 'd': 'l’assemblage, activité relativement '
         'routinière qui demande peu de qualifications rares, est l’étape qui '
         'crée le moins de valeur.'}],
 fig={'series': [
   pol('s1', 'Valeur ajoutée', SOUR, 'ac', ep=3.4, lp=[0.5, 0.62]),
   txt('e1', 'R&D, conception', 0.02, 0.05, 'ok', taille=14),
   txt('e2', 'assemblage', 0.44, 0.05, 'ko', taille=14),
   txt('e3', 'marketing, services', 0.74, 0.05, 'bl', taille=14),
 ]},
 etapes=[
  etape('La forme d’un sourire',
        'La courbe part haut à gauche, descend au centre et remonte à droite. '
        'Forte valeur ajoutée en amont, forte valeur ajoutée en aval, mais '
        'faible valeur ajoutée au centre.',
        on=['s1', 'e1', 'e2', 'e3'], vif=['s1']),
  etape('En amont : la recherche et la conception',
        'Les fonctions situées en amont de la chaîne — la recherche et '
        'développement, la conception — génèrent une forte valeur ajoutée et '
        'se localisent généralement dans les pays avancés, où se trouvent les '
        'qualifications.',
        add=[pt('a', '', 0.07, round(SOUR[0][1], 4), 'ok'),
             txt('ta', 'pays avancés', 0.04, 0.6, 'ok', taille=14, gras=True)],
        vif=['a', 'ta']),
  etape('Au centre : l’assemblage',
        'L’assemblage est souvent une activité relativement routinière, qui '
        'demande moins de qualifications rares. Le principal critère '
        'd’implantation devient donc le coût salarial unitaire.',
        add=[pt('b', '', 0.51, 0.22, 'ko'),
             txt('tb', 'pays à coûts plus faibles', 0.3, 0.1, 'ko', taille=14,
                 gras=True)],
        off=['ta'],
        vif=['b', 'tb']),
  etape('En aval : le marketing et les services',
        'Les activités situées après la production créent elles aussi '
        'beaucoup de valeur et se localisent largement sur les grands '
        'marchés, là où se trouvent les consommateurs solvables.',
        add=[pt('c', '', 0.95, round(SOUR[-1][1], 4), 'bl'),
             txt('tc', 'grands marchés', 0.72, 0.6, 'bl', taille=14,
                 gras=True)],
        off=['tb'],
        vif=['c', 'tc']),
  etape('La division internationale du processus productif',
        'Conception vers les pays avancés, assemblage vers les pays à coûts '
        'plus faibles, marketing et services vers les grands marchés : la '
        'courbe du sourire est la traduction graphique de la DIPP.',
        add=[txt('td', 'une étape, un critère de localisation', 0.18, 0.96,
                 'ac', taille=15, gras=True)],
        off=['tc'],
        vif=['td']),
  etape('Baldwin : le sourire s’est creusé',
        'En comparant les années 1970 et les années 2000, Baldwin montre que '
        'la courbe devient de plus en plus creusée : la valeur ajoutée monte '
        'en amont et en aval, tandis que celle de l’assemblage baisse.',
        add=[pol('s2', 'années 2000', SOUR2, 'ac2', ep=3, lp=[0.70, 0.70]),
             fl('fh', '', 0.12, 0.8, 0.12, 0.92, 'ac2'),
             fl('fb', '', 0.5, 0.2, 0.5, 0.12, 'ac2')],
        off=['td'],
        vif=['s2', 'fh', 'fb']),
  etape('Pourquoi l’écart se creuse',
        'Les pays avancés se spécialisent dans des activités toujours plus '
        'qualifiées, tandis que l’approfondissement de la division '
        'internationale du processus productif banalise encore l’assemblage.',
        add=[txt('te', 'approfondissement de la DIPP', 0.3, 0.52, 'jn',
                 taille=15, gras=True)],
        off=['fh', 'fb'],
        vif=['te']),
 ],
 pieges=[
  {'t': 'L’abscisse n’est ni un temps ni une quantité',
   'd': 'Ce sont des étapes d’un processus productif, rangées dans l’ordre '
        'chronologique de la fabrication. Il n’y a donc ni pente économique '
        'ni équilibre à chercher.'},
  {'t': 'Faible valeur ajoutée n’est pas faible production',
   'd': 'L’assemblage peut représenter l’essentiel des volumes produits et '
        'des emplois tout en captant une faible part de la valeur. C’est '
        'précisément le problème que pose la courbe.'},
  {'t': 'Le creusement est un résultat, pas une hypothèse',
   'd': 'Dire que le sourire s’est creusé suppose la comparaison de deux '
        'dates, celle de Baldwin entre les années 1970 et 2000. Sans cette '
        'comparaison, on ne dispose que d’une forme.'},
 ],
 main=[
  'Trace les axes : les étapes de la chaîne de valeur en abscisse, la valeur '
  'ajoutée en ordonnée.',
  'Trace un U largement ouvert — un sourire — et marque ses deux extrémités '
  'hautes.',
  'Annote les trois zones : R&D et conception à gauche, assemblage au centre, '
  'marketing et services à droite.',
  'Écris sous chaque zone le critère de localisation correspondant.',
  'Trace par-dessus, en pointillés, un sourire plus creusé : la comparaison '
  'de Baldwin entre les années 1970 et 2000.',
 ],
 phrase='La courbe du sourire de Stan Shih montre que la valeur ajoutée se '
        'concentre aux deux extrémités de la chaîne de valeur — recherche et '
        'conception en amont, marketing et services en aval — alors que '
        'l’assemblage, activité routinière dont le critère d’implantation est '
        'le coût salarial unitaire, en crée le moins ; et Baldwin montre que '
        'ce sourire s’est encore creusé avec l’approfondissement de la '
        'division internationale du processus productif.',
 liens=[{'c': '22', 'b': 839, 'l': 'Stan Shih : la courbe du sourire'},
        {'c': '22', 'b': 855, 'l': 'En amont : les activités à forte valeur ajoutée'},
        {'c': '22', 'b': 862, 'l': 'Au centre : l’assemblage'},
        {'c': '22', 'b': 877, 'l': 'Baldwin : le sourire s’est creusé'},
        {'c': '21', 'b': 934, 'l': 'La courbe du sourire et la firme globale (ch. 1 de 2ᵉ année)'}],
 mots=['courbe du sourire', 'Stan Shih', 'Baldwin', 'chaîne de valeur',
       'DIPP', 'valeur ajoutée', 'assemblage'],
))

# ---------------------------------------------------- avantage comparatif
FPP_P = (0.06, 0.90, 0.86, 0.02)
FPP_A = (0.06, 0.78, 0.96, 0.02)

L.append(fiche(
 id='avantage-comparatif',
 t='L’avantage comparatif de Ricardo',
 st='Pourquoi un pays moins productif partout a quand même intérêt à '
    'échanger.',
 cat='inter', an=2, ch=['23'],
 type='schema',
 q='Comment un pays absolument moins productif que son partenaire dans toutes '
   'les productions peut-il néanmoins gagner à se spécialiser et à échanger ?',
 axes={'x': 'Drap', 'y': 'Vin'},
 depart='Deux pays, le Portugal et l’Angleterre, chacun doté d’une quantité '
        'donnée de travail.',
 hyp=['Les produits sont homogènes : le drap anglais et le drap portugais '
      'sont considérés comme identiques.',
      'Dans l’exemple de Ricardo, le Portugal utilise moins de travail dans '
      'les deux productions : il possède donc un avantage absolu dans le '
      'drap comme dans le vin.',
      'L’Angleterre a donc un désavantage absolu dans les deux productions — '
      'ce qui permet précisément de montrer que les avantages absolus ne '
      'suffisent pas à déterminer les possibilités d’échange.'],
 pente=[{'s': 'Frontière des possibilités de production', 'd': 'elle est '
         'rectiligne et décroissante : produire davantage de vin signifie '
         'renoncer à une certaine quantité de drap. Sa pente mesure donc le '
         'coût d’opportunité.'},
        {'s': 'Les deux pentes diffèrent', 'd': 'et c’est tout le modèle : '
         'même si un pays est plus productif partout, ses coûts relatifs ne '
         'sont pas les mêmes que ceux de l’autre.'}],
 fig={'series': [
   lin('fp', 'Portugal', *FPP_P, c='ac', ep=3.2, lp=[0.28, 0.6]),
 ]},
 etapes=[
  etape('Les données de Ricardo',
        'Pour produire une unité, le Portugal emploie 90 unités de travail '
        'pour le drap et 80 pour le vin ; l’Angleterre, 100 pour le drap et '
        '120 pour le vin. Le Portugal est donc absolument plus productif dans '
        'les deux.',
        on=['fp'],
        add=[txt('td', 'Portugal : drap 90, vin 80', 0.42, 0.9, 'ac',
                 taille=15, gras=True),
             txt('ta', 'Angleterre : drap 100, vin 120', 0.42, 0.82, 'ac2',
                 taille=15, gras=True)],
        vif=['td', 'ta']),
  etape('La frontière des possibilités du Portugal',
        'Avec son travail disponible, le Portugal peut répartir sa production '
        'entre drap et vin le long d’une droite. Sa pente dit combien de vin '
        'il doit sacrifier pour une unité de drap : 1,125.',
        add=[txt('tp', 'Portugal : 1 drap coûte 1,125 vin', 0.26, 0.26, 'ac',
                 taille=14, gras=True)],
        off=['td', 'ta'],
        vif=['fp', 'tp']),
  etape('Celle de l’Angleterre est moins pentue',
        'L’Angleterre produit moins dans l’absolu, mais sa droite est moins '
        'inclinée : pour elle, une unité de drap ne coûte que 0,83 unité de '
        'vin. Les coûts relatifs diffèrent.',
        add=[lin('fa', 'Angleterre', *FPP_A, c='ac2', ep=3.2, lp=[0.66, 0.4]),
             txt('tang', 'Angleterre : 1 drap coûte 0,83 vin', 0.26, 0.18,
                 'ac2', taille=14, gras=True)],
        vif=['fa', 'tang']),
  etape('Le coût d’opportunité décide de la spécialisation',
        'Le coût d’opportunité du drap est plus faible en Angleterre : elle '
        'possède donc un avantage comparatif dans le drap — ou, puisqu’elle '
        'est moins productive partout, son désavantage comparatif y est le '
        'moins fort.',
        add=[fl('f1', 'Angleterre → drap', 0.56, 0.1, 0.84, 0.06, 'ac2')],
        off=['tp', 'tang'],
        vif=['f1']),
  etape('Le raisonnement symétrique pour le Portugal',
        'Le coût d’opportunité du vin est de 0,88 drap au Portugal contre 1,2 '
        'en Angleterre : il est plus faible au Portugal, qui possède donc un '
        'avantage comparatif dans le vin.',
        add=[fl('f2', 'Portugal → vin', 0.2, 0.62, 0.1, 0.84, 'ac')],
        off=['f1'],
        vif=['f2']),
  etape('Premier gain : la production mondiale augmente',
        'Avant spécialisation, chaque pays produit du vin et du drap, soit au '
        'total deux unités de chaque. Après spécialisation complète, la '
        'production mondiale augmente sans que la quantité totale de facteurs '
        'ait changé.',
        add=[txt('tg', 'plus de production mondiale, à facteurs constants',
                 0.12, 0.96, 'ok', taille=15, gras=True)],
        off=['f2'],
        vif=['tg']),
  etape('Deuxième gain : l’économie de facteurs',
        'Le même résultat peut se présenter autrement : on peut conserver la '
        'même production totale — deux unités de vin, deux de drap — en '
        'utilisant moins de travail. Les ressources sont mieux allouées.',
        add=[txt('tg2', 'ou la même production avec moins de travail',
                 0.12, 0.88, 'ok', taille=15, gras=True)],
        vif=['tg2']),
  etape('Ce que le modèle démontre vraiment',
        'Les avantages absolus ne déterminent pas l’échange. C’est la '
        'comparaison des coûts d’opportunité — donc des pentes — qui fixe la '
        'spécialisation, et elle laisse toujours une place aux deux '
        'partenaires.',
        add=[txt('tf', 'ce sont les pentes qui décident, pas les niveaux',
                 0.1, 0.96, 'jn', taille=15, gras=True)],
        off=['tg', 'tg2'],
        vif=['tf']),
 ],
 pieges=[
  {'t': 'Avantage absolu et avantage comparatif',
   'd': 'L’avantage absolu compare des productivités entre pays pour un même '
        'bien. L’avantage comparatif compare, à l’intérieur d’un même pays, '
        'le coût d’un bien en termes de l’autre. Les deux notions ne se '
        'lisent pas au même endroit du tableau.'},
  {'t': 'Un pays moins productif partout a toujours un avantage comparatif',
   'd': 'C’est le résultat central : il ne peut pas être le moins bon partout '
        'en termes relatifs, puisque les coûts relatifs se compensent par '
        'construction. Son désavantage est simplement moins fort quelque '
        'part.'},
  {'t': 'Les pentes, pas la position des droites',
   'd': 'Le Portugal produit davantage dans l’absolu, donc sa droite peut '
        'être plus haute. Ce qui compte pour l’échange, ce n’est pas sa '
        'position mais son inclinaison.'},
 ],
 main=[
  'Trace les axes : le drap en abscisse, le vin en ordonnée.',
  'Trace la droite du Portugal, plus pentue, et écris son coût d’opportunité '
  'du drap : 1,125 vin.',
  'Trace celle de l’Angleterre, moins pentue, et écris le sien : 0,83 vin.',
  'Compare les deux pentes et entoure le pays dont le coût d’opportunité du '
  'drap est le plus faible : c’est lui qui se spécialise dans le drap.',
  'Écris en bas les deux gains : plus de production mondiale, ou la même avec '
  'moins de travail.',
 ],
 phrase='La spécialisation ricardienne se détermine par les coûts '
        'd’opportunité et non par les avantages absolus : dans l’exemple du '
        'Portugal et de l’Angleterre, le Portugal est absolument plus '
        'productif dans les deux productions, mais comme une unité de drap '
        'lui coûte 1,125 unité de vin contre seulement 0,83 à l’Angleterre, '
        'chacun gagne à se spécialiser là où son coût de renoncement est le '
        'plus faible, ce qui accroît la production mondiale à facteurs '
        'constants.',
 liens=[{'c': '23', 'b': 490, 'l': 'L’exemple du Portugal et de l’Angleterre'},
        {'c': '23', 'b': 506, 'l': 'L’avantage comparatif repose sur le coût d’opportunité'},
        {'c': '23', 'b': 514, 'l': 'La détermination des avantages comparatifs'},
        {'c': '23', 'b': 541, 'l': 'Premier gain : la production mondiale augmente'},
        {'c': '23', 'b': 555, 'l': 'Deuxième gain : l’économie de facteurs'}],
 mots=['Ricardo', 'avantage comparatif', 'avantage absolu',
       'coût d’opportunité', 'spécialisation', 'Portugal', 'Angleterre'],
))

# ------------------------------------------------------ rendements croissants
def _cmdec(a, b, n=16, k=0.1, c=0.1):
    out = []
    for j in range(n):
        q = a + (b - a) * j / (n - 1.0)
        out.append((round(q, 4), round(k / q + c, 4)))
    return [p for p in out if p[1] <= 1.05]


CMC = _cmdec(0.12, 0.97, k=0.085, c=0.06)
CME = _cmdec(0.12, 0.97, k=0.135, c=0.18)

L.append(fiche(
 id='rendements-croissants',
 t='Rendements croissants et spécialisation cumulative',
 st='Pourquoi, chez Krugman, l’avantage se construit au lieu de préexister.',
 cat='inter', an=2, ch=['23'],
 type='schema',
 q='Comment les rendements croissants transforment-ils un avantage initial en '
   'avantage durable, et pourquoi l’avantage comparatif peut-il être acquis '
   'plutôt que donné ?',
 axes={'x': 'Quantité produite', 'y': 'Coût moyen'},
 depart='Deux économies — la Chine et l’Europe — produisent chacune leurs '
        'propres boutons avant l’ouverture.',
 hyp=['Les rendements croissants signifient qu’une augmentation de la '
      'production réduit les coûts unitaires : les courbes de coût moyen sont '
      'donc décroissantes.',
      'Avant l’ouverture, chaque économie produit pour ses propres '
      'consommateurs ; après l’ouverture, la demande adressée au producteur '
      'le plus compétitif devient la demande mondiale.',
      'Dans l’exemple du cours, le coût moyen chinois est inférieur au coût '
      'moyen européen pour chaque niveau de production : la Chine dispose '
      'd’un avantage initial.'],
 pente=[{'s': 'Coût moyen décroissant', 'd': 'c’est la traduction graphique '
         'des rendements croissants : plus on produit, moins chaque unité '
         'coûte.'},
        {'s': 'Deux courbes superposées', 'd': 'celle de la Chine est en '
         'dessous à tous les niveaux de production, d’où un prix d’équilibre '
         'initialement plus bas.'}],
 fig={'series': [
   pol('cmc', 'Coût moyen — Chine', CMC, 'ac', ep=3.2, lp=[0.74, 0.08]),
   pol('cme', 'Coût moyen — Europe', CME, 'ac2', ep=3.2, lp=[0.74, 0.42]),
 ]},
 etapes=[
  etape('Avant l’ouverture : chacun produit pour soi',
        'La Chine et l’Europe produisent chacune leurs propres boutons. Les '
        'rendements croissants rendent les deux courbes de coût moyen '
        'décroissantes.',
        on=['cmc', 'cme'], vif=['cmc', 'cme']),
  etape('L’avantage initial de la Chine',
        'Pour chaque niveau de production, le coût moyen chinois est '
        'inférieur au coût moyen européen. Le prix d’équilibre chinois est '
        'donc déjà plus bas : la Chine dispose d’un avantage initial.',
        add=[pt('q1', 'Q₁', 0.3, round(0.085 / 0.3 + 0.06, 4), 'ac'),
             rep('r1', 0.3, round(0.085 / 0.3 + 0.06, 4), lx='Q₁', c='ac'),
             pt('e1', '', 0.3, round(0.135 / 0.3 + 0.18, 4), 'ac2')],
        vif=['q1', 'r1', 'e1']),
  etape('L’ouverture additionne les deux demandes',
        'La demande adressée à la Chine devient la somme de la demande '
        'chinoise et de la demande européenne : c’est la demande mondiale. '
        'Sa production passe de Q₁ à Q₂.',
        add=[pt('q2', 'Q₂', 0.78, round(0.085 / 0.78 + 0.06, 4), 'ok'),
             rep('r2', 0.78, round(0.085 / 0.78 + 0.06, 4), lx='Q₂', c='ok'),
             fl('fq', 'demande mondiale', 0.34, 0.1, 0.72, 0.1, 'ok')],
        vif=['q2', 'r2', 'fq']),
  etape('Les économies d’échelle font baisser encore le coût',
        'En captant la demande étrangère, le producteur augmente ses volumes '
        'et descend le long de sa courbe : son coût unitaire baisse encore. '
        'L’avantage initial s’amplifie.',
        add=[fl('fc', 'le coût baisse encore', 0.4, 0.4, 0.72, 0.16, 'ok')],
        off=['fq'],
        vif=['fc']),
  etape('Les deux partenaires y gagnent',
        'L’Europe importe des boutons à un prix inférieur à celui qu’elle '
        'aurait obtenu en les produisant elle-même, et peut réaffecter ses '
        'facteurs vers des productions à plus forte valeur ajoutée. La Chine '
        'augmente sa production.',
        add=[txt('tg', 'Europe : importations moins chères + réaffectation',
                 0.1, 0.96, 'bl', taille=14, gras=True)],
        off=['fc'],
        vif=['tg']),
  etape('La spécialisation devient cumulative',
        'C’est le cœur de l’analyse de Krugman : l’avantage ne se constate '
        'pas, il se renforce. Plus on produit, moins on coûte ; moins on '
        'coûte, plus on vend. Cela explique la stabilité géographique de '
        'certaines spécialisations.',
        add=[txt('tk', 'produire plus → coûter moins → vendre plus',
                 0.14, 0.88, 'jn', taille=15, gras=True)],
        off=['tg'],
        vif=['tk']),
  etape('Avantage potentiel et avantage acquis',
        'Dans les théories traditionnelles, l’avantage comparatif existe '
        'avant l’échange. Chez Krugman, il peut se construire au cours du '
        'temps : une implantation initiale, parfois accidentelle, suffit à '
        'déclencher un processus cumulatif. C’est l’effet d’agglomération.',
        add=[txt('ta', 'l’avantage peut venir de l’histoire, pas de la nature',
                 0.06, 0.96, 'ko', taille=15, gras=True)],
        off=['tk'],
        vif=['ta']),
  etape('La conséquence pour un nouvel entrant',
        'Un pays peut disposer de coûts structurellement plus faibles et '
        'rester pourtant incapable d’entrer sur le marché, faute de volumes '
        'de production suffisants. L’écart entre avantage potentiel et '
        'avantage acquis devient une barrière.',
        add=[txt('tn', 'coûts potentiels bas ≠ capacité à entrer',
                 0.14, 0.88, 'ko', taille=15, gras=True)],
        vif=['tn']),
 ],
 pieges=[
  {'t': 'Coût moyen décroissant n’est pas coût moyen en U',
   'd': 'Ici, les rendements sont croissants sur toute la plage : la courbe '
        'ne remonte jamais. Y dessiner un U, comme en microéconomie '
        'standard, détruit le mécanisme cumulatif.'},
  {'t': 'Krugman ne contredit pas Ricardo, il le complète',
   'd': 'Ricardo explique le commerce entre pays différents par les coûts '
        'relatifs. Krugman explique le commerce entre pays semblables par les '
        'rendements croissants et la différenciation. Les deux cohabitent.'},
  {'t': 'Cumulatif ne veut pas dire irréversible',
   'd': 'Le processus renforce une position, il ne la verrouille pas '
        'définitivement. Mais il explique pourquoi certaines spécialisations '
        'restent stables longtemps.'},
 ],
 main=[
  'Trace les axes : la quantité produite en abscisse, le coût moyen en '
  'ordonnée.',
  'Trace deux courbes décroissantes qui ne remontent jamais, celle de la '
  'Chine sous celle de l’Europe.',
  'Marque Q₁ sur la courbe chinoise : la production d’avant l’ouverture.',
  'Marque Q₂ beaucoup plus à droite et plus bas : la production après '
  'l’ouverture au marché européen.',
  'Écris la boucle sous le graphique : produire plus, coûter moins, vendre '
  'plus.',
 ],
 phrase='Avec des rendements croissants, la spécialisation devient cumulative : '
        'en captant la demande étrangère, le producteur augmente ses volumes, '
        'abaisse encore ses coûts unitaires et fournit à ses partenaires un '
        'bien moins cher que celui qu’ils produisaient en autarcie, de sorte '
        'qu’un avantage comparatif peut résulter de l’histoire — une '
        'implantation initiale parfois accidentelle — davantage que de '
        'conditions naturelles.',
 liens=[{'c': '23', 'b': 2620, 'l': 'Rendements croissants internes et externes'},
        {'c': '23', 'b': 2688, 'l': 'Chine-Europe : les courbes de coût moyen décroissantes'},
        {'c': '23', 'b': 2708, 'l': 'La spécialisation devient cumulative'},
        {'c': '23', 'b': 2718, 'l': 'Avantage potentiel et avantage acquis'},
        {'c': '23', 'b': 2733, 'l': 'L’effet d’agglomération'}],
 mots=['Krugman', 'rendements croissants', 'économies d’échelle',
       'avantage acquis', 'agglomération', 'spécialisation cumulative'],
))

# ----------------------------------------- création et détournement de trafic
OD24 = (0.06, 0.06, 0.95, 0.9)
DD24 = (0.06, 0.94, 0.95, 0.1)

L.append(fiche(
 id='creation-detournement',
 t='Création et détournement de trafic',
 st='Un accord régional améliore-t-il le bien-être ? Tout dépend de l’effet '
    'qui domine.',
 cat='inter', an=2, ch=['24'],
 type='schema',
 q='Pourquoi la suppression d’un droit de douane entre deux partenaires '
   'peut-elle, selon les cas, améliorer ou dégrader l’efficacité économique ?',
 axes={'x': 'Quantités', 'y': 'Prix'},
 depart='Un marché national protégé par un droit de douane appliqué à tous '
        'les fournisseurs étrangers.',
 hyp=['L’analyse est celle de Jacob Viner : un accord régional n’est '
      'favorable au libre-échange mondial que si les créations de trafic '
      'qu’il engendre dépassent les détournements.',
      'Le fournisseur mondial le plus efficace n’est pas nécessairement le '
      'partenaire de l’accord : c’est de là que vient le détournement.',
      'On raisonne sur un seul produit et en équilibre partiel.'],
 pente=[{'s': 'Offre nationale', 'd': 'croissante : les producteurs '
         'nationaux n’offrent davantage qu’à prix plus élevé.'},
        {'s': 'Demande nationale', 'd': 'décroissante : les consommateurs '
         'achètent davantage quand le prix baisse.'},
        {'s': 'Les prix étrangers', 'd': 'horizontaux : ces fournisseurs sont '
         'supposés pouvoir livrer toute quantité à leur prix.'}],
 fig={'series': [
   lin('o', 'Offre nationale', *OD24, c='ac', ep=3.2, lp=[0.9, 0.78]),
   lin('d', 'Demande nationale', *DD24, c='ac2', ep=3.2, lp=[0.9, 0.2]),
 ]},
 etapes=[
  etape('Le marché protégé',
        'Avec le droit de douane, les importations arrivent à un prix élevé. '
        'Les consommateurs paient cher et les producteurs nationaux couvrent '
        'une large part du marché.',
        on=['o', 'd'],
        add=[lin('pt', 'prix avec droit de douane', 0.0, 0.62, 1.0, 0.62,
                 'ko', ep=2.6, lp=[0.26, 0.66]),
             pt('q1', '', round(x_de(OD24, 0.62), 4), 0.62, 'ac'),
             pt('q2', '', round(x_de(DD24, 0.62), 4), 0.62, 'ac2')],
        vif=['pt', 'q1', 'q2']),
  etape('L’accord supprime le droit de douane avec un partenaire',
        'Le prix payé par les consommateurs baisse jusqu’au prix du '
        'partenaire. La lecture de référence du cours est exactement '
        'celle-ci : la suppression du droit de douane réduit le prix payé par '
        'les consommateurs et augmente leurs importations.',
        add=[lin('pp', 'prix du partenaire', 0.0, 0.4, 1.0, 0.4, 'ok',
                 ep=2.6, lp=[0.26, 0.44]),
             fl('fp', '', 0.14, 0.6, 0.14, 0.44, 'ok')],
        vif=['pp', 'fp']),
  etape('La création de trafic',
        'À ce prix plus bas, la production nationale recule et la '
        'consommation augmente : des importations nouvelles apparaissent, qui '
        'remplacent une production nationale moins efficace. C’est un gain.',
        add=[pt('q3', '', round(x_de(OD24, 0.4), 4), 0.4, 'ac'),
             pt('q4', '', round(x_de(DD24, 0.4), 4), 0.4, 'ac2'),
             zone('zc1', 'gain production',
                  [(round(x_de(OD24, 0.4), 4), 0.4),
                   (round(x_de(OD24, 0.62), 4), 0.62),
                   (round(x_de(OD24, 0.4), 4), 0.62)], 'ok'),
             zone('zc2', 'gain consommation',
                  [(round(x_de(DD24, 0.4), 4), 0.4),
                   (round(x_de(DD24, 0.62), 4), 0.62),
                   (round(x_de(DD24, 0.62), 4), 0.4)], 'ok')],
        off=['fp'],
        vif=['q3', 'q4', 'zc1', 'zc2']),
  etape('Mais le partenaire n’est pas le plus efficace du monde',
        'Il existe un fournisseur mondial dont le prix est encore plus bas. '
        'Avant l’accord, le droit de douane s’appliquait à tous ; '
        'désormais il ne frappe plus que lui.',
        add=[lin('pm', 'prix du fournisseur mondial', 0.0, 0.3, 1.0, 0.3,
                 'bl', ep=2.6, lp=[0.3, 0.24])],
        off=['zc1', 'zc2'],
        vif=['pm']),
  etape('Le détournement de trafic',
        'Les importations se reportent du fournisseur le plus efficace vers '
        'le partenaire de l’accord, seulement parce qu’il est exempté de '
        'droits. Un fournisseur plus efficace est abandonné : c’est une '
        'perte.',
        add=[fl('fd', 'report vers le partenaire', 0.62, 0.3, 0.62, 0.4,
                 'ko'),
             zone('zd', 'perte de détournement',
                  [(round(x_de(OD24, 0.4), 4), 0.3),
                   (round(x_de(DD24, 0.4), 4), 0.3),
                   (round(x_de(DD24, 0.4), 4), 0.4),
                   (round(x_de(OD24, 0.4), 4), 0.4)], 'ko')],
        vif=['fd', 'zd']),
  etape('Le bilan dépend de l’effet qui domine',
        'Si la création de trafic l’emporte sur le détournement, l’accord '
        'améliore globalement le bien-être : la spécialisation est plus '
        'efficace. Dans le cas inverse, il peut réduire l’efficience.',
        add=[txt('tb', 'création > détournement → gain ; sinon → perte',
                 0.08, 0.96, 'jn', taille=15, gras=True)],
        off=['fd'],
        vif=['tb']),
  etape('La conclusion de Viner',
        'Pour Viner, le régionalisme n’est favorable au libre-échange mondial '
        'que lorsque les créations de trafic qu’il engendre dépassent les '
        'détournements. Le régionalisme n’est donc ni bon ni mauvais en soi.',
        add=[txt('tv', 'le régionalisme n’est ni bon ni mauvais en soi',
                 0.1, 0.88, 'ac', taille=15, gras=True)],
        off=['tb'],
        vif=['tv']),
  etape('Comment trancher en pratique',
        'La distinction permet d’évaluer concrètement les expériences '
        'd’intégration régionale. Certaines zones réussissent à augmenter '
        'simultanément les échanges entre leurs membres et leur insertion '
        'dans le commerce mondial : l’ASEAN en est l’exemple le plus net.',
        add=[txt('te', 'ASEAN : intégration régionale ET insertion mondiale',
                 0.06, 0.96, 'bl', taille=15, gras=True)],
        off=['tv'],
        vif=['te']),
 ],
 pieges=[
  {'t': 'Création et détournement coexistent toujours',
   'd': 'Un accord régional produit les deux effets en même temps. La '
        'question n’est jamais « lequel se produit ? » mais « lequel '
        'l’emporte ? ».'},
  {'t': 'Le détournement vient de la discrimination, pas de la baisse de prix',
   'd': 'Le consommateur paie moins cher dans les deux cas. Ce qui est perdu, '
        'c’est l’écart entre le prix du partenaire et celui du fournisseur '
        'mondial, plus efficace mais toujours taxé.'},
  {'t': 'Le libre-échange régional n’est pas le libre-échange mondial',
   'd': 'Supprimer les droits avec quelques partenaires tout en les '
        'maintenant avec les autres crée une discrimination. C’est '
        'exactement ce que Viner met en évidence.'},
 ],
 main=[
  'Trace les axes, une offre nationale croissante et une demande nationale '
  'décroissante.',
  'Trace une horizontale haute : le prix avec droit de douane, et lis les '
  'deux quantités.',
  'Trace une horizontale plus basse : le prix du partenaire — hachure les '
  'deux triangles de création de trafic.',
  'Trace une troisième horizontale encore plus basse : le prix du fournisseur '
  'mondial.',
  'Hachure le rectangle compris entre les deux derniers prix sur les '
  'importations : c’est la perte de détournement.',
 ],
 phrase='La suppression d’un droit de douane à l’intérieur d’un accord '
        'régional produit simultanément une création de trafic — des '
        'importations nouvelles remplacent une production nationale moins '
        'efficace — et un détournement de trafic — les achats se reportent '
        'd’un fournisseur mondial plus efficace vers le partenaire exempté de '
        'droits ; pour Viner, le régionalisme n’est donc favorable au '
        'libre-échange mondial que lorsque le premier effet l’emporte sur le '
        'second.',
 liens=[{'c': '24', 'b': 1860, 'l': 'Création et détournement : la condition de Viner'},
        {'c': '24', 'b': 1866, 'l': 'Le bilan dépend de l’effet qui domine'},
        {'c': '24', 'b': 1881, 'l': 'La lecture du graphique du cours'},
        {'c': '24', 'b': 1888, 'l': 'L’ASEAN : intégration régionale et insertion mondiale'}],
 mots=['Viner', 'création de trafic', 'détournement de trafic',
       'régionalisme', 'droit de douane', 'ASEAN', 'intégration régionale'],
))

# ------------------------------------------------- concurrence monopolistique
DEL9 = courbe_dec(0.08, 0.82, 0.95, 0.1, n=9, creux=0.8)
DIN9 = [(0.3, 0.95), (0.38, 0.78), (0.46, 0.6), (0.53, 0.42), (0.59, 0.24),
        (0.64, 0.08)]

L.append(fiche(
 id='concurrence-monopolistique',
 t='Différenciation et pouvoir de marché',
 st='Rendre son produit unique pour se comporter comme un petit monopole.',
 cat='entreprise', an=1, ch=['9'],
 type='schema',
 q='Comment la différenciation d’un produit confère-t-elle un pouvoir de '
   'marché à une entreprise qui reste pourtant en concurrence ?',
 axes={'x': 'Quantité demandée à l’entreprise', 'y': 'Prix'},
 depart='Une entreprise dont le produit est, au départ, perçu comme '
        'interchangeable avec ceux de ses concurrents.',
 hyp=['La concurrence monopolistique désigne une situation où plusieurs '
      'entreprises sont en concurrence, mais où chacune cherche à rendre son '
      'produit unique afin de se comporter comme un petit monopole sur sa '
      'clientèle.',
      'Edward Chamberlin développe cette idée en 1933 : les entreprises '
      'peuvent être en concurrence tout en disposant d’un pouvoir de marché '
      'grâce à la différenciation.',
      'La stratégie fonctionne parce que la différenciation modifie '
      'l’élasticité de la demande adressée à l’entreprise.'],
 pente=[{'s': 'Demande très plate', 'd': 'produit peu différencié : le '
         'consommateur considère qu’un yaourt en vaut un autre et change '
         'facilement de marque à la moindre hausse de prix.'},
        {'s': 'Demande raide', 'd': 'produit différencié : le consommateur '
         'fidèle à une marque ne la remplace pas facilement, il accepte un '
         'prix supérieur à celui des concurrents.'}],
 fig={'series': [
   lin('p0', '', 0.0, 0.45, 1.0, 0.45, 'gr', ep=1.6),
   lin('p1', '', 0.0, 0.7, 1.0, 0.7, 'gr', ep=1.6),
   txt('tp0', 'prix initial', 0.84, 0.39, 'gr', taille=13),
   txt('tp1', 'après hausse', 0.84, 0.74, 'gr', taille=13),
 ]},
 etapes=[
  etape('Sans différenciation : une demande très élastique',
        'Si le consommateur considère qu’un yaourt en vaut un autre, il '
        'changera facilement de marque. La demande adressée à l’entreprise '
        'est très plate.',
        on=['p0', 'p1', 'tp0', 'tp1'],
        add=[pol('de', 'Produit banalisé', DEL9, 'ko', ep=3.2,
                 lp=[0.5, 0.06]),
             pt('a', '', 0.48, 0.45, 'ac2'),
             rep('ra', 0.48, 0.45, lx='Q₀', c='ac2')],
        vif=['de', 'a', 'ra']),
  etape('Une hausse de prix lui coûte très cher',
        'À la moindre hausse, la clientèle part chez le concurrent : la '
        'quantité vendue s’effondre. L’entreprise n’a aucun pouvoir de '
        'marché.',
        add=[pt('b', '', 0.172, 0.7, 'ko'),
             rep('rb', 0.172, 0.7, lx='Q₁', c='ko'),
             fl('fb', 'la clientèle part', 0.46, 0.18, 0.2, 0.18, 'ko')],
        vif=['b', 'rb', 'fb']),
  etape('La différenciation change la pente',
        'L’entreprise rend son produit unique — marque, qualité, design. Le '
        'consommateur attaché à une marque ne la remplace plus facilement : '
        'la demande qui lui est adressée devient beaucoup plus raide.',
        add=[pol('di', 'Produit différencié', DIN9, 'ok', ep=3.2,
                 lp=[0.72, 0.9])],
        off=['fb', 'b', 'rb', 'de'],
        vif=['di']),
  etape('La même hausse de prix lui coûte peu',
        'Le consommateur fidèle accepte une hausse de prix, et même un prix '
        'supérieur à celui des concurrents. La quantité vendue recule à '
        'peine : l’entreprise a conquis un pouvoir de marché.',
        add=[pt('c', '', 0.513, 0.45, 'ac2'),
             pt('d', '', 0.437, 0.7, 'ok'),
             rep('rc', 0.513, 0.45, lx='Q₀', c='ac2'),
             rep('rd', 0.437, 0.7, lx='Q₁', c='ok')],
        vif=['c', 'd', 'rc', 'rd']),
  etape('La marque réduit la substituabilité',
        'C’est le mécanisme exact : la différenciation réduit '
        'l’élasticité-prix de la demande, parce que le consommateur fidèle '
        'accepte plus facilement une hausse. La marque est un instrument de '
        'pouvoir de marché.',
        add=[txt('tm', 'différenciation → élasticité ↓ → pouvoir de marché ↑',
                 0.06, 0.95, 'ok', taille=15, gras=True)],
        vif=['tm']),
  etape('Un petit monopole au sein de la concurrence',
        'L’entreprise reste en concurrence — d’autres marques existent — mais '
        'elle se comporte comme un monopole sur sa propre clientèle. C’est '
        'tout le sens de l’expression « concurrence monopolistique ».',
        add=[txt('tc', 'en concurrence, mais monopole sur sa clientèle',
                 0.1, 0.88, 'ac', taille=15, gras=True)],
        off=['tm'],
        vif=['tc']),
  etape('L’autre usage de l’élasticité : la tarification différentielle',
        'Un monopole discriminant pratique des prix différents selon la '
        'disposition à payer et l’élasticité de chaque client : séances de '
        'cinéma moins chères le matin, plus chères aux horaires demandés. '
        'C’est le yield management.',
        add=[txt('ty', 'peu élastique → prix plus élevé ; très élastique → prix bas',
                 0.04, 0.95, 'bl', taille=14, gras=True)],
        off=['tc'],
        vif=['ty']),
 ],
 pieges=[
  {'t': 'Ce n’est pas la demande du marché mais celle de l’entreprise',
   'd': 'En concurrence pure et parfaite, la demande adressée à une firme est '
        'parfaitement élastique — une horizontale. Toute la différenciation '
        'consiste à l’incliner.'},
  {'t': 'Pouvoir de marché n’est pas monopole',
   'd': 'L’entreprise reste concurrencée : elle ne fixe pas son prix sans '
        'limite. Elle dispose seulement d’une marge de manœuvre que le '
        'produit banalisé ne lui donnerait pas.'},
  {'t': 'La tarification différentielle n’est pas toujours condamnée',
   'd': 'Les autorités de concurrence peuvent la tolérer si le marché reste '
        'servi, si les consommateurs trouvent encore une offre et si la '
        'pratique ne ferme pas le marché aux concurrents.'},
 ],
 main=[
  'Trace les axes : la quantité demandée à l’entreprise en abscisse, le prix '
  'en ordonnée.',
  'Trace deux horizontales : le prix initial et le prix après hausse.',
  'Trace d’abord une demande très plate : produit banalisé — lis l’effondrement '
  'des quantités.',
  'Trace ensuite une demande raide : produit différencié — les quantités '
  'bougent à peine.',
  'Écris sous le graphique la chaîne : différenciation, baisse de '
  'l’élasticité, pouvoir de marché.',
 ],
 phrase='La différenciation des produits réduit l’élasticité-prix de la '
        'demande adressée à l’entreprise, car le consommateur fidèle à une '
        'marque accepte plus facilement une hausse de prix : c’est ainsi que, '
        'dans la concurrence monopolistique théorisée par Chamberlin en 1933, '
        'une entreprise peut rester en concurrence tout en se comportant '
        'comme un petit monopole sur sa propre clientèle.',
 liens=[{'c': '9', 'b': 1724, 'l': 'La concurrence monopolistique'},
        {'c': '9', 'b': 1733, 'l': 'Une demande moins élastique'},
        {'c': '9', 'b': 1748, 'l': 'Le monopole discriminant et la tarification différentielle'},
        {'c': '9', 'b': 1773, 'l': 'Pourquoi la tarification différentielle n’est pas toujours condamnée'}],
 mots=['concurrence monopolistique', 'Chamberlin', 'différenciation',
       'pouvoir de marché', 'élasticité', 'yield management', 'marque'],
))
