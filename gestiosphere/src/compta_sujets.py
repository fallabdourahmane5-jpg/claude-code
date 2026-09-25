"""Comptabilité — sujets : exercices du poly de TD (et DS de novembre 2019) avec corrigés calculés."""
from lib import E_, journal, table, fr, eur, r2, P, H3, H4, NOTE, WARN, FORM, ul, ol
from calc_compta import plan_lineaire, plan_degressif, jours_restants, jours_ecoules

TVA = 0.20
SRC = 'Poly de TD'


def pct(x):
    return fr(x * 100, 2).rstrip('0').rstrip(',') + ' %'


def tab_lin(rows):
    return table(['Exercice', 'Base', 'Taux', 'Annuité', 'Cumul', 'VNC fin'],
                 [[a, b, pct(t), d, cu, v] for a, b, t, d, cu, v in rows], num_cols=(1, 3, 4, 5))


def tab_deg(rows):
    return table(['Exercice', 'VNC début', 'Taux lin. restant', 'Taux dégressif', 'Annuité', 'Cumul', 'VNC fin'],
                 [[a, vd, pct(tl) if tl <= 1 else '— (fin de plan)', pct(td), d, cu, vf] for a, vd, tl, td, d, cu, vf in rows], num_cols=(1, 4, 5, 6))


def s_ex1():
    base = 85000 + 9500 + 3500
    ttc = r2(base * (1 + TVA))
    lin = plan_lineaire(base, 5, 26, 4, 2017)
    deg, coef, td = plan_degressif(base, 5, 4, 2017)
    L = {r[0]: r for r in lin}
    G = {r[0]: r for r in deg}
    der = [(a, G[a][4], L[a][3], r2(G[a][4] - L[a][3])) for a in sorted(L)]
    cum20l = L[2020][4]
    cum20d = G[2020][5]
    der_cum20 = r2(sum(x[3] for x in der if x[0] <= 2020))
    h = H3('1. Facture d\'achat (16/04/2017)')
    h += P(f'Coût d\'acquisition = prix d\'achat + frais accessoires nécessaires à la mise en état d\'utilisation : 85 000 + 9 500 (transport) + 3 500 (montage) = <b>{eur(base)}</b> HT. Hypothèse : TVA 20 %, soit {eur(ttc)} TTC, payés pour moitié comptant et pour moitié à crédit.')
    h += journal(E_('16/04/2017', [('D', '2154', 'Matériel industriel', base), ('D', '44562', 'TVA déductible sur immobilisations', r2(base * TVA)),
                                   ('C', '512', 'Banque (moitié comptant)', r2(ttc / 2)), ('C', '404', 'Fournisseurs d\'immobilisations (moitié à crédit)', r2(ttc / 2))], 'Facture machine DEBROS'))
    h += H3('2. Amortissement linéaire')
    h += P(f'Durée 5 ans → taux 20 %, annuité pleine {eur(base * 0.2)}. Prorata à partir de la <b>mise en service</b> (26/04/2017) : {jours_restants(26, 4)} jours sur 360 (4 jours en avril + 8 mois).')
    h += FORM(f'2017 : {fr(base)} × 20 % × {jours_restants(26, 4)}/360 = {eur(L[2017][3], 2)}')
    h += tab_lin(lin)
    h += journal(E_('31/12/2017', [('D', '6811', 'Dotations aux amortissements', L[2017][3]), ('C', '28154', 'Amortissement du matériel industriel', L[2017][3])]),
                 E_('31/12/2020', [('D', '6811', 'Dotations aux amortissements', L[2020][3]), ('C', '28154', 'Amortissement du matériel industriel', L[2020][3])]))
    h += P(f'<b>Impact</b> : au compte de résultat, charge d\'exploitation de {eur(L[2017][3], 2)} en 2017 et {eur(L[2020][3], 2)} en 2020. Au bilan fin 2020 : brut {eur(base)}, amortissements {eur(cum20l, 2)}, net {eur(L[2020][5], 2)}.')
    h += H3('3. Amortissement dégressif')
    h += P('<b>Conditions</b> : le dégressif est un régime fiscal réservé aux biens <b>neufs</b>, d\'une durée d\'utilisation d\'<b>au moins 3 ans</b>, appartenant aux catégories éligibles (matériels et outillages industriels notamment). Il est calculé à partir du <b>1er jour du mois d\'acquisition</b>.')
    h += FORM(f'Coefficient {fr(coef)} (durée 5 ans) → taux dégressif = 20 % × {fr(coef)} = {pct(td)}<br>2017 : {fr(base)} × 35 % × 9/12 (avril → décembre) = {eur(G[2017][4], 2)}')
    h += tab_deg(deg)
    h += P('En 2020, il reste 2 ans et 3 mois : le taux linéaire sur la durée restante (1/2,25 = 44,44 %) dépasse 35 %, donc on répartit la VNC en parts égales (30 536,19 / 2,25 = 13 571,64 € par an, puis 3 392,91 € pour les 3 derniers mois).')
    h += P('<b>Comptabilisation (méthode du cours)</b> : l\'amortissement comptable reste linéaire (6811 / 28). L\'écart avec le dégressif est un <b>amortissement dérogatoire</b> (6872 / 145 tant que dégressif > linéaire, puis 145 / 7872).')
    h += table(['Exercice', 'Dégressif', 'Linéaire', 'Dérogatoire (+ dotation / − reprise)'], [[a, d, l, x] for a, d, l, x in der], num_cols=(1, 2, 3))
    h += journal(E_('31/12/2017', [('D', '6811', 'Dotations aux amortissements', L[2017][3]), ('C', '28154', 'Amortissement du matériel industriel', L[2017][3])], 'Part linéaire'),
                 E_('31/12/2017', [('D', '6872', 'Dotations aux provisions réglementées', der[0][3]), ('C', '145', 'Amortissements dérogatoires', der[0][3])], 'Excédent dégressif'),
                 E_('31/12/2020', [('D', '6811', 'Dotations aux amortissements', L[2020][3]), ('C', '28154', 'Amortissement du matériel industriel', L[2020][3])], 'Part linéaire'),
                 E_('31/12/2020', [('D', '145', 'Amortissements dérogatoires', -der[3][3]), ('C', '7872', 'Reprises sur provisions réglementées', -der[3][3])], 'Linéaire > dégressif'))
    h += P(f'<b>Impact au bilan fin 2020</b> : l\'actif est identique au cas linéaire (net {eur(L[2020][5], 2)}) ; les capitaux propres comprennent un compte 145 de {eur(der_cum20, 2)} (cumul des dotations {fr(der[0][3], 2)} + {fr(der[1][3], 2)} moins les reprises {fr(-der[2][3], 2)} + {fr(-der[3][3], 2)}), soit l\'écart entre le cumul dégressif ({fr(cum20d, 2)}) et le cumul linéaire ({fr(cum20l, 2)}).')
    h += P(f'<b>Au compte de résultat</b> : 2017, charges exceptionnelles de {eur(der[0][3], 2)} en plus du linéaire (résultat réduit, impôt différé) ; 2020, produit exceptionnel de {eur(-der[3][3], 2)}.')
    return dict(id='cpt-td1', num='TD 1', ch='compta-1', mobiliser=['compta-0', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 1',
                titre='DEBROS : acquisition d\'une machine, plans linéaire et dégressif',
                enonce='<p>L\'entreprise DEBROS achète une machine industrielle : valeur du matériel 85 000 €, frais de transport 9 500 €, frais de montage 3 500 €. Achat le 16 avril 2017, mise en service le 26 avril 2017, durée d\'amortissement 5 ans, paiement moitié comptant, moitié à crédit.</p>' +
                ol(['Enregistrer la facture d\'achat de la machine.', 'Amortissement linéaire : tableau d\'amortissement, écritures au 31/12/2017 et au 31/12/2020, impact sur le bilan et le compte de résultat.',
                    'Amortissement dégressif : rappeler les conditions, tableau, écritures au 31/12/2017 et au 31/12/2020, impact sur le bilan et le compte de résultat.']),
                pourquoi='Chapitre 1 pour les calculs d\'amortissement ; introduction pour le coût historique (valeur d\'entrée) ; chapitre 4 pour la lecture de l\'impact sur le bilan et le compte de résultat.',
                commentaire=ul(['Les frais de transport et de montage font partie du <b>coût d\'acquisition</b> (valeur d\'entrée), la TVA récupérable non.', 'Linéaire : prorata en <b>jours</b> depuis la <b>mise en service</b> ; dégressif : prorata en <b>mois</b> depuis le <b>1er jour du mois d\'acquisition</b>.', 'Pense au passage au linéaire en fin de plan dégressif.', 'Méthode du cours : l\'amortissement comptable est linéaire, l\'excédent fiscal passe en dérogatoire (145).']),
                corrige=h)


def s_ex2():
    # camion cédé
    cam_ann = 19000 / 5
    cam_dot = r2(cam_ann * jours_ecoules(1, 4) / 360)
    cam_cum = r2(950 + cam_dot)
    cam_vnc = r2(19000 - cam_cum)
    prix = 9500
    mv = r2(prix - cam_vnc)
    # BWR
    bwr = 23500 + 500
    deg, coef, td = plan_degressif(bwr, 4, 9, 2016)
    j = jours_restants(10, 9)
    bwr_lin = r2(bwr / 4 * j / 360)
    bwr_der = r2(deg[0][4] - bwr_lin)
    cons = 2000.0
    azt = r2(22100 / 6)
    ordi = 1600.0
    tot6811 = r2(cons + azt + ordi + bwr_lin)
    h = H3('1. Vente du camion (01/04/2016) et achat de la machine BWR (10/09/2016)')
    h += P(f'Avant de sortir le camion, on <b>met à jour son amortissement</b> jusqu\'à la date de cession : {fr(19000)} / 5 × {jours_ecoules(1, 4)}/360 = {eur(cam_dot, 2)}. Cumul à la cession : 950 + {fr(cam_dot)} = {eur(cam_cum)} ; VNC = {eur(cam_vnc)}. Hypothèse : prix de 9 500 € HT, TVA 20 %.')
    h += journal(E_('01/04/2016', [('D', '6811', 'Dotations aux amortissements', cam_dot), ('C', '28182', 'Amortissement du matériel de transport', cam_dot)], 'Complément d\'amortissement du camion'),
                 E_('01/04/2016', [('D', '28182', 'Amortissement du matériel de transport', cam_cum), ('D', '675', 'Valeurs comptables des éléments d\'actif cédés', cam_vnc), ('C', '2182', 'Matériel de transport', 19000)], 'Sortie du camion'),
                 E_('01/04/2016', [('D', '512', 'Banque', r2(prix * 1.2)), ('C', '775', 'Produits des cessions d\'éléments d\'actif', prix), ('C', '44571', 'TVA collectée', r2(prix * 0.2))], 'Prix de cession'),
                 E_('10/09/2016', [('D', '2154', 'Matériel industriel (machine BWR)', bwr), ('D', '44562', 'TVA sur immobilisations', r2(bwr * 0.2)), ('C', '404', 'Fournisseurs d\'immobilisations', r2(bwr * 1.2))], 'Achat à crédit, frais d\'installation inclus'))
    h += P(f'Résultat de cession : {fr(prix)} − {fr(cam_vnc)} = <b>{eur(mv)}</b> (moins-value).')
    h += H3('2. Plan d\'amortissement dégressif de la machine BWR')
    h += FORM(f'Base = 23 500 + 500 = {eur(bwr)} · durée 4 ans → coefficient {fr(coef)} → taux {pct(td)}<br>2016 : {fr(bwr)} × 31,25 % × 4/12 (septembre → décembre) = {eur(deg[0][4], 2)}')
    h += tab_deg(deg)
    h += P('En 2018, il reste 2 ans et 8 mois : 1/2,667 = 37,5 % > 31,25 %, donc on passe au linéaire sur la durée restante.')
    h += H3('3. Dotations aux amortissements 2016')
    h += table(['Immobilisation', 'Calcul', 'Dotation 2016'], [
        ['Constructions', '40 000 / 20 (année pleine)', cons], ['Machine AZT', '22 100 / 6 (année pleine, fin du plan en 2018)', azt],
        ['Camion', f'19 000 / 5 × 90/360 (jusqu\'à la cession, déjà enregistré le 01/04)', cam_dot], ['Ordinateur', '8 000 / 5 (année pleine)', ordi],
        ['Machine BWR — linéaire comptable', f'24 000 / 4 × {j}/360 (mise en service supposée le 10/09)', bwr_lin],
        ['Machine BWR — dérogatoire', f'{fr(deg[0][4], 2)} (dégressif) − {fr(bwr_lin, 2)} (linéaire)', bwr_der]], num_cols=(2,))
    h += H3('4. Écritures de fin d\'exercice (31/12/2016)')
    h += journal(E_('31/12/2016', [('D', '6811', 'Dotations aux amortissements', tot6811), ('C', '2813', 'Amortissement des constructions', cons), ('C', '28154', 'Amortissement du matériel industriel (AZT + BWR)', r2(azt + bwr_lin)), ('C', '28183', 'Amortissement du matériel informatique', ordi)]),
                 E_('31/12/2016', [('D', '6872', 'Dotations aux provisions réglementées', bwr_der), ('C', '145', 'Amortissements dérogatoires', bwr_der)], 'Machine BWR'))
    h += NOTE('Si l\'on suit l\'énoncé à la lettre (« machine amortie en dégressif ») sans distinguer comptable et fiscal, on doterait directement 2 500 € au 6811. Le cours retient la méthode du dérogatoire : les deux présentations donnent la même charge totale.')
    h += H3('5. Immobilisations corporelles au bilan du 31/12/2016')
    rows = [['Constructions', 40000, 25000], ['Machine AZT', 22100, r2(12380.10 + azt)], ['Ordinateur', 8000, r2(2733.33 + ordi)], ['Machine BWR', bwr, bwr_lin]]
    rows = [[n, b, a, r2(b - a)] for n, b, a in rows]
    tb, ta = sum(x[1] for x in rows), r2(sum(x[2] for x in rows))
    rows.append(['Total', tb, ta, r2(tb - ta)])
    h += table(['Immobilisation', 'Brut', 'Amortissements', 'Net'], rows, num_cols=(1, 2, 3), tot=True)
    h += P(f'Le camion est sorti de l\'actif. Au passif, les capitaux propres comprennent {eur(bwr_der, 2)} d\'amortissements dérogatoires.')
    return dict(id='cpt-td2', num='TD 2', ch='compta-1', mobiliser=['compta-2', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 2',
                titre='TRAVELLA : cession d\'un camion, achat d\'une machine en dégressif, inventaire 2016',
                enonce='<p>État des immobilisations au 31/12/2015 : constructions (acquises le 18/05/2004, en service le 01/07/2004, 40 000 €, linéaire 20 ans, cumul 23 000 €) ; machine AZT (20/08/2012, 22 100 €, linéaire 6 ans, cumul 12 380,10 €) ; camion (acquis le 16/09/2015, en service le 30/09/2015, 19 000 €, linéaire 5 ans, cumul 950 €) ; ordinateur (acquis le 12/04/2014, en service le 15/04/2014, 8 000 €, linéaire 5 ans, cumul 2 733,33 €).</p><p>En 2016 : vente au comptant du camion le 1er avril pour 9 500 € ; achat à crédit le 10 septembre d\'une machine BWR à 23 500 € HT + 500 € HT de frais d\'installation, amortie en dégressif sur 4 ans.</p>' +
                ol(['Enregistrer la vente du camion et l\'achat de la machine BWR.', 'Établir le plan d\'amortissement de la machine BWR.', 'Calculer toutes les dotations aux amortissements de 2016.', 'Enregistrer toutes les écritures de fin d\'exercice.', 'Présenter les immobilisations corporelles au bilan du 31/12/2016.']),
                pourquoi='Le chapitre 1 est central (dotations, dégressif, cession). Le chapitre 2 intervient pour les provisions réglementées : le dérogatoire est une provision réglementée (compte 145). Le chapitre 4 sert à la présentation au bilan.',
                commentaire=ul(['Une cession commence <b>toujours</b> par la dotation complémentaire jusqu\'à la date de sortie.', 'Les frais d\'installation s\'ajoutent au coût d\'acquisition.', 'Vérifie les données : les cumuls de l\'énoncé se retrouvent avec une année de 360 jours (AZT : 130 jours en 2012).']),
                corrige=h)


def s_ex3():
    immo = [('Terrains', 33200, 0, 0), ('Constructions', 97100, 87390, 60000), ('Outillage industriel', 487210, 977100, 45010),
            ('Matériel de transport', 45530, 100000, 30000), ('Matériel de bureau', 18000, 45000, 8000), ('Titres de participation', 0, 150000, 0)]
    amo = [('Constructions', 66960, 12580, 48000), ('Outillage industriel', 302220, 29670, 27280), ('Matériel de transport', 37470, 30280, 30000), ('Matériel de bureau', 17905, 16120, 7200)]
    ti = [[n, d, a, s, d + a - s] for n, d, a, s in immo]
    ta = [[n, d, a, s, d + a - s] for n, d, a, s in amo]
    tot = lambda t: ['Total'] + [sum(r[i] for r in t) for i in range(1, 5)]
    fin_amo = {r[0]: r[4] for r in ta}
    actif = [[r[0], r[4], fin_amo.get(r[0], 0), r[4] - fin_amo.get(r[0], 0)] for r in ti]
    actif.append(['Total actif immobilisé', sum(r[1] for r in actif), sum(r[2] for r in actif), sum(r[3] for r in actif)])
    ces = [('Constructions', 60000, 48000, 53000), ('Outillage industriel', 45010, 27280, 10000), ('Matériel de transport', 30000, 30000, 5000), ('Matériel de bureau', 8000, 7200, 1000)]
    pv = [[n, b, a, b - a, p, p - (b - a)] for n, b, a, p in ces]
    h = H3('1. Tableaux de l\'annexe')
    h += FORM('Valeur fin = valeur début + augmentations − diminutions')
    h += H4('Tableau des immobilisations')
    h += table(['Immobilisation', 'Valeur début', 'Augmentations', 'Diminutions', 'Valeur fin'], ti + [tot(ti)], num_cols=(1, 2, 3, 4), tot=True)
    h += H4('Tableau des amortissements')
    h += P('Augmentations = dotations de l\'exercice ; diminutions = amortissements cumulés des biens cédés (ils sortent avec le bien).')
    h += table(['Immobilisation', 'Valeur début', 'Augmentations', 'Diminutions', 'Valeur fin'], ta + [tot(ta)], num_cols=(1, 2, 3, 4), tot=True)
    h += H3('2. Actif immobilisé au 31/12/2017')
    h += table(['Poste', 'Brut', 'Amortissements', 'Net'], actif, num_cols=(1, 2, 3), tot=True)
    h += H4('Pour aller plus loin : résultats de cession')
    h += table(['Bien cédé', 'Brut', 'Amort.', 'VNC (675)', 'Prix (775)', 'Plus/moins-value'], pv, num_cols=(1, 2, 3, 4, 5))
    h += P(f'Résultat global de cession : {eur(sum(r[5] for r in pv))}.')
    return dict(id='cpt-td3', num='TD 3', ch='compta-1', mobiliser=['compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 3',
                titre='CERFI : tableaux des immobilisations et des amortissements de l\'annexe, actif du bilan',
                enonce='<p>Au 31/12/2016 (valeurs brutes / amortissements cumulés) : terrains 33 200 / — ; constructions 97 100 / 66 960 ; outillage industriel 487 210 / 302 220 ; matériel de transport 45 530 / 37 470 ; matériel de bureau 18 000 / 17 905.</p><p>Dotations 2017 : constructions 12 580 ; outillage 29 670 ; transport 30 280 ; bureau 16 120. Acquisitions 2017 (HT) : constructions 87 390 ; outillage 977 100 ; transport 100 000 ; bureau 45 000 ; titres de participation 150 000. Cessions 2017 (valeur brute / amortissement à la date de vente / prix) : constructions 60 000 / 48 000 / 53 000 ; outillage 45 010 / 27 280 / 10 000 ; transport 30 000 / 30 000 / 5 000 ; bureau 8 000 / 7 200 / 1 000.</p>' +
                ol(['Les amortissements correspondant au linéaire, présenter les tableaux de l\'annexe.', 'Établir l\'actif du bilan au 31/12/2017.']),
                pourquoi='Le chapitre 1 fournit la mécanique des amortissements et des cessions ; le chapitre 4 la présentation de l\'annexe et de l\'actif.',
                commentaire=ul(['Les titres de participation ne s\'amortissent pas : ils figurent au tableau des immobilisations mais pas au tableau des amortissements.', 'Les amortissements des biens cédés viennent en <b>diminution</b> du tableau des amortissements.']),
                corrige=h)


def s_ex4():
    t = [('Actions A', 'Titres de participation', 450, 285, 297, 330, '2961'), ('Actions B', 'Titres de participation', 300, 303, 297, 330, '2961'),
         ('Actions C', 'Titres immobilisés', 150, 289, 300, 285, '2971'), ('Actions D', 'VMP', 60, 360, 315, 330, '590'), ('Obligations E', 'VMP', 45, 645, 612, 618, '590')]
    rows = []
    for n, cat, q, ve, c16, c17, cpt in t:
        ex = max(0, (ve - c16) * q)
        ne = max(0, (ve - c17) * q)
        rows.append([n, q, ve, c17, ex, ne, max(0, ne - ex), max(0, ex - ne)])
    h = H3('1. Tableau d\'ajustement des dépréciations')
    h += P('Pour chaque ligne : dépréciation existante = (valeur d\'entrée − cours 2016) × quantité si positif ; dépréciation nécessaire = (valeur d\'entrée − cours 2017) × quantité si positif. <b>Pas de compensation</b> entre lignes (prudence) : la plus-value latente sur A ne compense rien.')
    h += table(['Titres', 'Nb', 'Valeur d\'entrée', 'Cours 2017', 'Existante', 'Nécessaire', '+ Dotation', '− Reprise'], rows, num_cols=(1, 2, 3, 4, 5, 6, 7))
    h += H3('2. Écritures au 31/12/2017')
    h += journal(E_('31/12/2017', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 600), ('C', '2971', 'Dépréciation des titres immobilisés', 600)], 'Actions C'),
                 E_('31/12/2017', [('D', '2961', 'Dépréciation des titres de participation', 1800), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 1800)], 'Actions B : dépréciation devenue sans objet'),
                 E_('31/12/2017', [('D', '590', 'Dépréciation des VMP', 1170), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 1170)], 'Actions D (900) et obligations E (270)'))
    h += H3('3. Bilan et compte de résultat')
    h += table(['Actif', 'Brut', 'Dépréciations', 'Net'], [['Titres de participation (A + B)', 128250 + 90900, 0, 219150], ['Autres titres immobilisés (C)', 43350, 600, 42750],
                                                           ['VMP (D + E)', 21600 + 29025, 1800 + 1215, 50625 - 3015]], num_cols=(1, 2, 3))
    h += P('Compte de résultat : <b>charges financières</b> 6866 = 600 € ; <b>produits financiers</b> 7866 = 1 800 + 1 170 = 2 970 €. Effet net sur le résultat : +2 370 €.')
    return dict(id='cpt-td4', num='TD 4', ch='compta-2', mobiliser=['compta-0', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 4',
                titre='LEMEE : dépréciation d\'un portefeuille de titres',
                enonce='<p>Portefeuille au 31/12/2017 (quantité · valeur d\'entrée unitaire · date d\'acquisition · cours moyen 2016 · cours moyen 2017) :</p>' +
                table(['Titres', 'Quantité', 'Valeur d\'entrée', 'Acquisition', 'Cours 2016', 'Cours 2017'], [['Titres de participation — Actions A', 450, 285, 'mars 2012', 297, 330], ['Titres de participation — Actions B', 300, 303, 'juin 2013', 297, 330],
                                                                                                               ['Titres immobilisés — Actions C', 150, 289, 'avril 2010', 300, 285], ['VMP — Actions D', 60, 360, 'juin 2015', 315, 330], ['VMP — Obligations E', 45, 645, 'octobre 2016', 612, 618]], num_cols=(1, 2, 4, 5)) +
                ol(['Établir le tableau des ajustements de provisions.', 'Enregistrer les écritures au 31/12/2017.', 'Présenter l\'actif du bilan concernant ces titres et le compte de résultat.']),
                pourquoi='Le chapitre 2 s\'applique (dépréciation des titres). Le principe de prudence (introduction) interdit les compensations, et le chapitre 4 sert à la présentation.',
                commentaire=ul(['Les dépréciations existantes se calculent avec le cours <b>2016</b>, les nécessaires avec le cours <b>2017</b>.', 'Un 9 en 2ᵉ position : 2961, 2971, 590.', 'Les dotations et reprises sur titres sont <b>financières</b> (6866/7866).']),
                corrige=h)


def s_ex5():
    h = H3('1. Opérations de 2017')
    h += P('Rappel au 31/12/2016 : A 200 × 260 = 52 000 (dépréciation 5 000) ; B 165 × 300 = 49 500 ; C 120 × 140 = 16 800 (dépréciation 4 800) ; D 135 × 110 = 14 850 (dépréciation 675).')
    h += journal(E_('Avril 2017', [('D', '512', 'Banque', 12750), ('C', '775', 'Produits des cessions d\'éléments d\'actif', 12750)], 'Vente de 50 titres A × 255'),
                 E_('Avril 2017', [('D', '675', 'Valeurs comptables des éléments d\'actif cédés', 13000), ('C', '261', 'Titres de participation', 13000)], 'Sortie : 50 × 260'),
                 E_('Juin 2017', [('D', '512', 'Banque', 7380), ('D', '667', 'Charges nettes sur cessions de VMP', 1020), ('C', '503', 'VMP — actions', 8400)], '60 actions C vendues 123 (coût 140)'),
                 E_('Octobre 2017', [('D', '271', 'Titres immobilisés', 22800), ('C', '512', 'Banque', 22800)], 'Achat de 95 titres E × 240'),
                 E_('Octobre 2017', [('D', '512', 'Banque', 16200), ('C', '503', 'VMP — actions', 14850), ('C', '767', 'Produits nets sur cessions de VMP', 1350)], '135 actions D vendues 120 (coût 110)'))
    h += NOTE('Cession de titres de participation (immobilisations financières) = opération en capital → 675/775 (exceptionnel). Cession de VMP = opération financière → résultat net en 667 ou 767.')
    h += H3('2. État des titres au 31/12/2017')
    rows = [['A — participation', 150, 260, 39000, 250, 1500, 5000], ['B — immobilisés', 165, 300, 49500, 310, 0, 0], ['E — immobilisés', 95, 240, 22800, 246, 0, 0],
            ['C — VMP', 60, 140, 8400, 135, 300, 4800], ['D — VMP (vendus)', 0, 110, 0, '—', 0, 675]]
    rows = [r + [max(0, r[5] - r[6]), max(0, r[6] - r[5])] for r in rows]
    h += table(['Titres', 'Nb', 'Valeur d\'entrée', 'Coût total', 'Valeur 31/12', 'Nécessaire', 'Existante', '+ Dotation', '− Reprise'], rows, num_cols=(1, 2, 3, 4, 5, 6, 7, 8))
    h += P('La dépréciation existante des titres vendus (1 250 pour A, 2 400 pour C, 675 pour D) est reprise avec l\'ajustement de fin d\'année : elle est devenue sans objet.')
    h += H3('3. Régularisation des dépréciations, bilan et compte de résultat')
    h += journal(E_('31/12/2017', [('D', '2961', 'Dépréciation des titres de participation', 3500), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 3500)], 'A : 5 000 → 1 500'),
                 E_('31/12/2017', [('D', '590', 'Dépréciation des VMP', 5175), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 5175)], 'C : 4 800 → 300 ; D : 675 → 0'))
    h += table(['Actif', 'Brut', 'Dépréciations', 'Net'], [['Titres de participation', 39000, 1500, 37500], ['Autres titres immobilisés (B + E)', 72300, 0, 72300], ['VMP', 8400, 300, 8100]], num_cols=(1, 2, 3))
    h += table(['Compte de résultat', 'Charges', 'Produits'], [['Financier : cessions de VMP (667 / 767)', 1020, 1350], ['Financier : reprises 7866', '', 8675], ['Exceptionnel : cession des titres A (675 / 775)', 13000, 12750]], num_cols=(1, 2))
    return dict(id='cpt-td5', num='TD 5', ch='compta-2', mobiliser=['compta-1', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 5',
                titre='DEFOUR : cessions et achats de titres, ajustement des dépréciations',
                enonce='<p>Portefeuille au 31/12/2016 (nombre · valeur d\'entrée · dépréciation existante) : titres de participation A 200 · 260 · 5 000 ; titres immobilisés B 165 · 300 · — ; VMP actions C 120 · 140 · 4 800 ; VMP actions D 135 · 110 · 675.</p><p>En 2017 : avril, vente de 50 titres A à 255 € (valeur au 31/12/2017 : 250 €) ; juin, vente de 60 actions C à 123 € (valeur au 31/12 : 135 €) ; octobre, achat de 95 titres immobilisés E à 240 € (valeur au 31/12 : 246 €) ; octobre, vente des 135 actions D à 120 €. Titres B au 31/12/2017 : 310 €.</p>' +
                ol(['Enregistrer les opérations de 2017.', 'Présenter l\'état des titres au 31/12/2017.', 'Enregistrer la régularisation des provisions ; établir le bilan de ces titres et le compte de résultat.']),
                pourquoi='Le chapitre 2 est central (dépréciation des titres). Le chapitre 1 fournit la logique de cession d\'une immobilisation (titres de participation, 675/775) et le chapitre 4 la présentation.',
                commentaire=ul(['Distinguer la cession d\'une <b>immobilisation financière</b> (675/775) de celle de <b>VMP</b> (667/767).', 'Les dépréciations se recalculent sur les titres <b>restants</b> ; celles des titres vendus sont reprises.']),
                corrige=h)


def s_ex6():
    data = [('ATTENOT', 2392, 400, 0.40, 'douteux'), ('BUTUIN', 8372, 0, 0.30, 'nouveau'), ('CAMUS', 23920, 20000, 1.0, 'douteux'), ('HUGOT', 897, 0, 0, 'sain'), ('PIERRE', 7415.20, 2000, None, 'irrecouvrable')]
    rows = []
    dot = rep = 0
    for n, ttc, ex, p, st in data:
        ht = r2(ttc / 1.2)
        if p is None:
            nec = 0
            perte = ht
            tva = r2(ttc - ht)
        else:
            nec = r2(ht * p)
            perte = 0
            tva = 0
        d = max(0, r2(nec - ex))
        r = max(0, r2(ex - nec))
        dot += d
        rep += r
        rows.append([n, ttc, ht, ex, nec, d, r, perte, tva])
    dot, rep = r2(dot), r2(rep)
    h = H3('1. Tableau d\'ajustement des dépréciations')
    h += P('Dépréciation calculée sur le <b>HT</b> (TTC / 1,20). ATTENOT : 40 % ; BUTUIN : on récupère 70 %, la perte probable est donc de 30 % ; CAMUS : la liquidation rend la perte totale probable, on déprécie 100 % du HT ; HUGOT : aucun risque ; PIERRE : perte définitive, la créance est irrécouvrable.')
    h += table(['Client', 'Créance TTC', 'Créance HT', 'Existante', 'Nécessaire', '+ Dotation', '− Reprise', 'Perte HT', 'TVA à récupérer'], rows, num_cols=tuple(range(1, 9)))
    h += WARN('CAMUS : la dépréciation existante (20 000) dépasse le HT de la créance (19 933,33) ; la dépréciation ne peut pas couvrir la TVA, d\'où une <b>reprise</b> de 66,67 €.')
    h += H3('2. Écritures au 31/12/2016')
    h += journal(E_('31/12/2016', [('D', '416', 'Clients douteux', 8372), ('C', '411', 'Clients', 8372)], 'Transfert de la créance BUTUIN (TTC)'),
                 E_('31/12/2016', [('D', '6817', 'Dotations aux dépréciations des actifs circulants', dot), ('C', '491', 'Dépréciation des comptes clients', dot)], 'ATTENOT 397,33 + BUTUIN 2 093'),
                 E_('31/12/2016', [('D', '491', 'Dépréciation des comptes clients', 66.67), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 66.67)], 'CAMUS'),
                 E_('31/12/2016', [('D', '654', 'Pertes sur créances irrécouvrables', 6179.33), ('D', '44571', 'TVA collectée', 1235.87), ('C', '416', 'Clients douteux', 7415.20)], 'PIERRE'),
                 E_('31/12/2016', [('D', '491', 'Dépréciation des comptes clients', 2000), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 2000)], 'PIERRE : dépréciation sans objet'))
    h += H3('3. Bilan et compte de résultat')
    brut416 = 2392 + 8372 + 23920
    dep = r2(797.33 + 2093 + 19933.33)
    h += table(['Actif circulant', 'Brut', 'Dépréciations', 'Net'], [['Clients (411 : HUGOT)', 897, 0, 897], ['Clients douteux (416 : ATTENOT, BUTUIN, CAMUS)', brut416, dep, r2(brut416 - dep)], ['Total créances clients', 897 + brut416, dep, r2(897 + brut416 - dep)]], num_cols=(1, 2, 3), tot=True)
    h += P(f'Compte de résultat : charges d\'exploitation 6817 = {eur(dot, 2)} et 654 = 6 179,33 € ; produits d\'exploitation 7817 = {eur(rep, 2)} (CAMUS 66,67 + PIERRE 2 000).')
    return dict(id='cpt-td6', num='TD 6', ch='compta-2', mobiliser=['compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 6',
                titre='Créances douteuses : ajustement des dépréciations et créance irrécouvrable',
                enonce='<p>Créances de l\'exercice 2016 (TVA 20 %) :</p>' + table(['Client', 'Factures non réglées (TTC)', 'Provisions existantes', 'Observations'],
                                                                                  [['ATTENOT', 2392, 400, 'Perte probable de 40 %'], ['BUTUIN (nouvelle créance)', 8372, '', 'On pense récupérer 70 % de la créance'], ['CAMUS', 23920, 20000, 'Liquidation de la société'], ['HUGOT (nouvelle créance)', 897, '', 'Engagement ferme de règlement'], ['PIERRE', 7415.20, 2000, 'Solde définitivement impayé']], num_cols=(1, 2)) +
                ol(['Établir le tableau d\'ajustement des provisions des créances douteuses.', 'Enregistrer les écritures nécessaires.', 'Présenter la ligne du bilan des créances et le compte de résultat.']),
                pourquoi='Le chapitre 2 est central (dépréciation des créances, créance irrécouvrable) et le chapitre 4 sert à la présentation.',
                commentaire=ul(['Toujours raisonner en <b>HT</b> pour la dépréciation, en <b>TTC</b> pour le transfert au 416.', '« Récupérer 70 % » veut dire une perte de 30 %.', 'Créance irrécouvrable : perte HT (654), TVA récupérée (44571), reprise de l\'ancienne dépréciation.']),
                corrige=h)


def s_ex7():
    h = H3('1. Écritures au 31/12/2015')
    h += journal(E_('31/12/2015', [('D', '6875', 'Dotations aux provisions exceptionnelles', 15000), ('C', '1514', 'Provisions pour amendes et pénalités', 15000)], 'Pénalités fiscales prévues'),
                 E_('31/12/2015', [('D', '6815', 'Dotations aux provisions d\'exploitation', 11500), ('C', '1511', 'Provisions pour litiges', 11500)], 'Litige DUTHOIT : 50 % × 23 000'),
                 E_('31/12/2015', [('D', '6815', 'Dotations aux provisions d\'exploitation', 9000), ('C', '1512', 'Provisions pour garanties données aux clients', 9000)], '6 000 × 5 % × 30 €'),
                 E_('31/12/2015', [('D', '1512', 'Provisions pour garanties données aux clients', 2000), ('C', '7815', 'Reprises sur provisions d\'exploitation', 2000)], 'Garantie des ventes 2014 expirée'))
    h += NOTE('La provision pour garanties de 2 000 € au début de 2015 couvre les ventes de 2014, dont la garantie de 12 mois a expiré : on la reprend et on constitue la nouvelle. Un ajustement net (+7 000) donne le même résultat.')
    h += H3('2. Tableau des provisions et bilan au 31/12/2015')
    h += table(['Provisions pour risques et charges', 'Début', 'Augmentations', 'Diminutions', 'Fin'],
               [['Litiges', 0, 11500, 0, 11500], ['Garanties clients', 2000, 9000, 2000, 9000], ['Amendes et pénalités', 0, 15000, 0, 15000], ['Perte de change', 4000, 0, 0, 4000], ['Total 2', 6000, 35500, 2000, 39500]], num_cols=(1, 2, 3, 4), tot=True)
    h += P('Ventilation : exploitation (dotations 20 500, reprises 2 000) ; exceptionnel (dotations 15 000). Au bilan, poste <b>Provisions pour risques</b> (entre capitaux propres et dettes) : 39 500 €.')
    h += H3('3. Écritures de 2016')
    h += journal(E_('20/06/2016', [('D', '6712', 'Pénalités, amendes fiscales et pénales', 18000), ('C', '512', 'Banque', 18000)], 'Paiement des pénalités notifiées'),
                 E_('31/12/2016', [('D', '1514', 'Provisions pour amendes et pénalités', 15000), ('C', '7875', 'Reprises sur provisions exceptionnelles', 15000)], 'Provision devenue sans objet'),
                 E_('31/12/2016', [('D', '6815', 'Dotations aux provisions d\'exploitation', 6900), ('C', '1511', 'Provisions pour litiges', 6900)], 'DUTHOIT : risque porté à 18 400'),
                 E_('31/12/2016', [('D', '1512', 'Provisions pour garanties données aux clients', 9000), ('C', '7815', 'Reprises sur provisions d\'exploitation', 9000)], 'Garantie des ventes 2015 expirée'),
                 E_('31/12/2016', [('D', '6815', 'Dotations aux provisions d\'exploitation', 6720), ('C', '1512', 'Provisions pour garanties données aux clients', 6720)], '8 000 × 3 % × 28 €'))
    h += P('La charge réelle de la pénalité (18 000) est en partie couverte par la reprise (15 000) : l\'impact net sur 2016 est de −3 000 €.')
    h += H3('4. Tableau des provisions et bilan au 31/12/2016')
    h += table(['Provisions pour risques et charges', 'Début', 'Augmentations', 'Diminutions', 'Fin'],
               [['Litiges', 11500, 6900, 0, 18400], ['Garanties clients', 9000, 6720, 9000, 6720], ['Amendes et pénalités', 15000, 0, 15000, 0], ['Perte de change', 4000, 0, 0, 4000], ['Total 2', 39500, 13620, 24000, 29120]], num_cols=(1, 2, 3, 4), tot=True)
    h += P('Ventilation : exploitation (dotations 13 620, reprises 9 000) ; exceptionnel (reprises 15 000). Provisions au bilan : 29 120 €. La provision pour perte de change de 4 000 € est maintenue faute d\'information.')
    return dict(id='cpt-td7', num='TD 7', ch='compta-2', mobiliser=['compta-0', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 7',
                titre='SADA : provisions pour risques et charges (pénalités, litige, garanties) sur deux exercices',
                enonce='<p>Au 31/12/2015 : suite à un contrôle fiscal, 15 000 € de pénalités sont prévues ; litige avec le client DUTHOIT qui réclame 23 000 € (provision de 50 % sur conseil de l\'avocat) ; 6 000 unités vendues à 75 € HT, 5 % tomberont en panne pendant la garantie de 12 mois, réparation moyenne 30 € HT. Le tableau des provisions indique en début d\'exercice 2 000 € de provisions pour garanties et 4 000 € pour perte de change.</p><p>En 2016 : notification le 20 juin de pénalités de 18 000 €, réglées par chèque le jour même ; procès DUTHOIT toujours en cours, risque de condamnation passé à 18 400 € ; 8 000 produits vendus à 90 € HT, taux de panne ramené à 3 %, coût moyen de réparation 28 € HT.</p>' +
                ol(['Écritures au 31/12/2015.', 'Tableau des provisions de l\'annexe et bilan au 31/12/2015.', 'Écritures de 2016 (en cours d\'exercice et à l\'inventaire).', 'Tableau des provisions et bilan au 31/12/2016.']),
                pourquoi='Le chapitre 2 est central (provisions pour risques et charges). L\'introduction fournit le principe de séparation des exercices qui les justifie, et le chapitre 4 la présentation au bilan.',
                commentaire=ul(['Choisir la bonne nature de dotation : litige et garanties → exploitation (6815) ; amende fiscale → exceptionnel (6875).', 'Une provision devenue sans objet (charge payée, garantie expirée) est <b>reprise</b>.']),
                corrige=h)


def s_ex8():
    h = H3('Écritures de régularisation au 31/12/N')
    h += journal(E_('31/12/N', [('D', '6037', 'Variation des stocks de marchandises', 31000), ('C', '37', 'Stocks de marchandises', 31000)], 'Annulation SI'),
                 E_('31/12/N', [('D', '37', 'Stocks de marchandises', 38000), ('C', '6037', 'Variation des stocks de marchandises', 38000)], 'SF'),
                 E_('31/12/N', [('D', '6032', 'Variation des stocks des autres approvisionnements', 13000), ('C', '326', 'Emballages', 13000)], 'Annulation SI'),
                 E_('31/12/N', [('D', '326', 'Emballages', 32000), ('C', '6032', 'Variation des stocks des autres approvisionnements', 32000)], 'SF'),
                 E_('31/12/N', [('D', '7135', 'Variation des stocks de produits', 67500), ('C', '355', 'Produits finis', 67500)], 'Annulation SI'),
                 E_('31/12/N', [('D', '355', 'Produits finis', 83000), ('C', '7135', 'Variation des stocks de produits', 83000)], 'SF'),
                 E_('31/12/N', [('D', '397', 'Dépréciation des stocks de marchandises', 500), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 500)], 'Marchandises : 3 000 → 2 500'),
                 E_('31/12/N', [('D', '6817', 'Dotations aux dépréciations des actifs circulants', 1700), ('C', '392', 'Dépréciation des autres approvisionnements', 700), ('C', '3955', 'Dépréciation des produits finis', 1000)], 'Emballages 600 → 1 300 ; produits finis 3 100 → 4 100'))
    h += NOTE('Variante admise : annuler toute l\'ancienne dépréciation (reprise) et constituer toute la nouvelle (dotation). Le résultat est identique.')
    h += H3('Impact')
    h += table(['Bilan (actif)', 'Brut', 'Dépréciation', 'Net'], [['Marchandises', 38000, 2500, 35500], ['Emballages', 32000, 1300, 30700], ['Produits finis', 83000, 4100, 78900]], num_cols=(1, 2, 3))
    h += table(['Compte de résultat', 'Montant', 'Lecture'], [['6037 Variation de stock de marchandises', '−7 000', 'SI − SF : le stock a augmenté, la charge diminue'], ['6032 Variation de stock d\'approvisionnements', '−19 000', 'SI − SF'],
                                                             ['7135 Production stockée', '+15 500', 'SF − SI : produit'], ['6817 Dotations', '1 700', 'Charge d\'exploitation'], ['7817 Reprises', '500', 'Produit d\'exploitation']])
    return dict(id='cpt-td8', num='TD 8', ch='compta-3', mobiliser=['compta-2', 'compta-4'], type='Exercice de TD', source=SRC + ' — Exercice 8',
                titre='CREDOU : variations de stocks et dépréciations des stocks',
                enonce='<p>Stocks et dépréciations de la société CREDOU :</p>' + table(['', 'Stock 31/12/N-1', 'Dépréciation N-1', 'Stock 31/12/N', 'Dépréciation N'], [['Marchandises', 31000, 3000, 38000, 2500], ['Emballages perdus', 13000, 600, 32000, 1300], ['Produits finis', 67500, 3100, 83000, 4100]], num_cols=(1, 2, 3, 4)) +
                ol(['Procéder aux écritures de régularisation.', 'Montrer l\'impact dans le bilan et le compte de résultat.']),
                pourquoi='Le chapitre 3 fournit la variation des stocks, le chapitre 2 la dépréciation des stocks et le chapitre 4 la lecture du bilan et du compte de résultat.',
                commentaire=ul(['Marchandises et approvisionnements : variation <b>SI − SF</b> en charges (603) ; produits finis : <b>SF − SI</b> en produits (713).', 'Dépréciation des stocks : 39 + chiffre de la classe (392, 395, 397).']),
                corrige=h)


def s_ex9():
    h = P('Hypothèse : les marchandises « vendues pour 21 000 € » sont retenues à leur coût d\'achat, ce qui donne un stock final de 38 000 + 15 000 − 21 000 = 32 000 €. Pour la garantie, le coût d\'échange (coût de production de 75 €) est provisionné. La condamnation de 15 000 € a été payée en cours d\'année.')
    h += journal(E_('31/12/2015', [('D', '6037', 'Variation des stocks de marchandises', 38000), ('C', '37', 'Stocks de marchandises', 38000)], 'Annulation SI'),
                 E_('31/12/2015', [('D', '37', 'Stocks de marchandises', 32000), ('C', '6037', 'Variation des stocks de marchandises', 32000)], 'SF = 38 000 + 15 000 − 21 000'),
                 E_('31/12/2015', [('D', '752', 'Revenus des immeubles', 1200), ('C', '487', 'Produits constatés d\'avance', 1200)], 'Loyer reçu le 1/12 pour 3 mois : janvier et février 2016'),
                 E_('31/12/2015', [('D', '6811', 'Dotations aux amortissements', 28537), ('C', '28184', 'Amortissement du mobilier', 10532), ('C', '28182', 'Amortissement du matériel de transport', 11280), ('C', '28183', 'Amortissement du matériel informatique', 6725)], 'Linéaire'),
                 E_('31/12/2015', [('D', '6872', 'Dotations aux provisions réglementées', 4350), ('C', '145', 'Amortissements dérogatoires', 4350)], 'Transport : 15 630 − 11 280'),
                 E_('31/12/2015', [('D', '1511', 'Provisions pour litiges', 12000), ('C', '7815', 'Reprises sur provisions d\'exploitation', 12000)], 'Litige soldé par la condamnation'),
                 E_('31/12/2015', [('D', '486', 'Charges constatées d\'avance', 1500), ('C', '613', 'Locations', 1500)], 'Loyer trimestriel payé le 1/11 : janvier 2016'),
                 E_('31/12/2015', [('D', '601', 'Achats de matières premières', 14000), ('D', '44586', 'TVA sur factures non parvenues', 2800), ('C', '4081', 'Fournisseurs, factures non parvenues', 16800)], 'Livraison du 20/12 sans facture'),
                 E_('31/12/2015', [('D', '6815', 'Dotations aux provisions d\'exploitation', 60000), ('C', '1512', 'Provisions pour garanties données aux clients', 60000)], '40 000 × 2 % × 75 €'))
    h += NOTE('Chaque écriture relève d\'un chapitre : stocks et régularisations (ch. 3), amortissements et dérogatoire (ch. 1), provisions (ch. 2). Les charges à payer et les charges et produits constatés d\'avance seront <b>contrepassés au 1er janvier 2016</b>.')
    return dict(id='cpt-td9', num='TD 9', ch='compta-3', mobiliser=['compta-1', 'compta-2'], type='Exercice de TD', source=SRC + ' — Exercice 9',
                titre='Toutes les écritures de fin d\'exercice 2015 (synthèse)',
                enonce=ul(['Stock de marchandises au 31/12/2014 : 38 000 € ; en 2015, achats de 15 000 € et marchandises vendues pour 21 000 €.', 'Le locataire de l\'entrepôt a versé le 1er décembre 2015 1 800 € HT pour 3 mois de loyer d\'avance.',
                           'Dotations : mobilier (linéaire) 10 532 € ; matériel de transport (dégressif) : linéaire 11 280 €, dégressif 15 630 € ; matériel informatique (linéaire) 6 725 €.',
                           'Le 10 avril 2015, condamnation à payer 15 000 € de dommages et intérêts à un client ; au 1er janvier, le compte 1511 présentait à ce titre 12 000 €.', 'Le 1er novembre 2015, paiement d\'avance du loyer trimestriel des locaux administratifs : 4 500 €.',
                           'Livraison de 14 000 € HT de matières premières le 20 décembre sans facture (envoyée en janvier).', '40 000 exemplaires d\'un nouveau produit vendus 100 € HT, garantie d\'un an : 2 % pourraient tomber en panne ; échange contre un neuf, coût de production 75 €.']) + P('Enregistrer toutes les écritures de fin d\'exercice 2015.'),
                pourquoi='Exercice de synthèse qui mobilise trois chapitres : régularisations (ch. 3), amortissements (ch. 1) et provisions (ch. 2).',
                commentaire=ul(['Faire une écriture par information, en se demandant à chaque fois quel principe s\'applique.', 'Le loyer <b>reçu</b> d\'avance donne un produit constaté d\'avance (487) ; le loyer <b>payé</b> d\'avance une charge constatée d\'avance (486).']),
                corrige=h)


def s_ex10():
    imm = [['Terrain', 22800, 0, 0], ['Construction', 80000, 0, 0], ['Matériel industriel', 325200, 50000, 25000], ['Matériel de bureau et informatique', 18500, 0, 0], ['Immobilisations financières', 55000, 0, 0]]
    imm = [r + [r[1] + r[2] - r[3]] for r in imm]
    amo = [['Construction', 62500, 4000, 0], ['Matériel industriel', 178000, 58200, 22500], ['Matériel de bureau et informatique', 9250, 3700, 0]]
    amo = [r + [r[1] + r[2] - r[3]] for r in amo]
    prov = [['Provisions réglementées', 0, 0, 0, 0], ['Provisions pour risques et charges (litiges)', 2200, 700, 0, 2900], ['Dépréciation des immobilisations financières', 1200, 750, 0, 1950],
            ['Dépréciation du stock de matières premières', 0, 3200, 0, 3200], ['Dépréciation des clients', 17400, 6400, 3100, 20700]]
    h = H3('1. Tableaux de l\'annexe')
    h += H4('Immobilisations')
    h += table(['', 'Début', 'Augmentations', 'Diminutions', 'Fin'], imm, num_cols=(1, 2, 3, 4))
    h += H4('Amortissements')
    h += table(['', 'Début', 'Augmentations', 'Diminutions', 'Fin'], amo, num_cols=(1, 2, 3, 4))
    h += H4('Provisions')
    h += table(['', 'Début', 'Augmentations', 'Diminutions', 'Fin'], prov, num_cols=(1, 2, 3, 4))
    h += P('Ventilation : <b>exploitation</b> dotations 700 + 3 200 + 6 400 = 10 300, reprises 3 100 ; <b>financier</b> dotations 750 ; exceptionnel néant.')
    h += H3('2. Éléments du compte de résultat')
    h += table(['Poste', 'Calcul', 'Montant'], [
        ['Variation de stock de matières premières (charge)', 'SI − SF = 155 200 − 151 000', 4200], ['Variation de stock de marchandises (charge)', '10 200 − 12 450', -2250],
        ['Production stockée (produit)', 'SF − SI = 97 200 − 65 500', 31700], ['Dotations aux amortissements', '4 000 + 58 200 + 3 700', 65900],
        ['Dotations aux provisions d\'exploitation', '700 + 3 200 + 6 400', 10300], ['Reprises sur provisions d\'exploitation', 'clients', 3100], ['Dotations financières', 'immobilisations financières', 750],
        ['Produit net sur cession de VMP (767)', 'prix 3 000 − coût sorti (35 500 − 32 700 = 2 800)', 200],
        ['Charges exceptionnelles sur opérations en capital (675)', 'VNC machine = 25 000 − 22 500', 2500], ['Produits exceptionnels sur opérations en capital (775)', 'prix de vente de la machine', 1000]], num_cols=(2,))
    h += P('Moins-value sur la machine : 1 000 − 2 500 = −1 500 €.')
    h += H3('3. Bilan au 31/12/N (partiel)')
    b = [['Terrain', 22800, 0], ['Construction', 80000, 66500], ['Matériel industriel', 350200, 213700], ['Matériel de bureau et informatique', 18500, 12950], ['Immobilisations financières', 55000, 1950],
         ['Stock de matières premières', 151000, 3200], ['Stock de marchandises', 12450, 0], ['Stock de produits finis', 97200, 0], ['Créances clients', 195800, 20700], ['VMP', 32700, 0]]
    b = [r + [r[1] - r[2]] for r in b]
    h += table(['Actif', 'Brut', 'Amort. et prov.', 'Net'], b, num_cols=(1, 2, 3))
    h += P('Passif : provisions pour risques et charges 2 900 € (pas de provisions réglementées).')
    return dict(id='cpt-td10', num='TD 10', ch='compta-4', mobiliser=['compta-1', 'compta-2', 'compta-3'], type='Exercice de TD', source=SRC + ' — Exercice 10',
                titre='Annexe (immobilisations, amortissements, provisions), bilan et compte de résultat à partir des éléments d\'inventaire',
                enonce='<p>Immobilisations au 1/1/N : terrain 22 800 ; construction 80 000 ; matériel industriel 325 200 ; matériel de bureau et informatique 18 500 ; immobilisations financières 55 000. Investissement N : matériel industriel 50 000. Vente d\'une machine : prix 1 000, valeur d\'achat 25 000.</p><p>Amortissements au 1/1/N : construction 62 500 ; matériel industriel 178 000 ; bureau 9 250. Dotations N : 4 000 ; 58 200 ; 3 700. Amortissements supprimés (cession) : matériel industriel 22 500.</p><p>Provisions au 1/1/N : immobilisations financières 1 200 ; litiges 2 200 ; créances clients 17 400. Dotations N : immobilisations financières 750 ; litiges 700 ; stock de matières premières 3 200 ; créances clients 6 400. Reprises N : créances clients 3 100.</p><p>Actif au 1/1 et au 31/12 : stock de matières premières 155 200 / 151 000 ; marchandises 10 200 / 12 450 ; produits finis 65 500 / 97 200 ; créances clients 175 000 / 195 800 ; VMP 35 500 / 32 700.</p>' +
                ol(['Compléter les tableaux de l\'annexe.', 'Compléter le bilan et le compte de résultat, sachant que l\'entreprise a revendu des VMP au prix de 3 000 € (ne pas chercher à équilibrer).']),
                pourquoi='Exercice de synthèse de la mise en forme (ch. 4) qui reprend les amortissements (ch. 1), les provisions (ch. 2) et les variations de stocks (ch. 3).',
                commentaire=ul(['Bien séparer les trois tableaux de l\'annexe.', 'La baisse du poste VMP (2 800) correspond au coût des titres vendus, en l\'absence d\'achat.']),
                corrige=h)


BAL11 = {  # compte: (intitulé, débit, crédit)
    '101': ('Capital', 0, 2000000), '106': ('Réserves', 0, 3202000), '14': ('Provisions réglementées', 0, 60000), '151': ('Provisions pour risques', 0, 40000),
    '157': ('Provisions pour charges', 0, 85000), '164': ('Emprunts auprès des établissements de crédit', 0, 4030000), '201': ('Frais d\'établissement', 50000, 0),
    '207': ('Fonds commercial', 900000, 0), '211': ('Terrains', 1300000, 0), '213': ('Constructions', 3000000, 0), '215': ('Installations techniques', 1700000, 0),
    '2182': ('Matériel de transport', 120000, 0), '2183': ('Matériel de bureau et informatique', 75000, 0), '2184': ('Mobilier', 60000, 0), '261': ('Titres de participation', 2200000, 0),
    '275': ('Dépôts et cautionnements versés', 800, 0), '2801': ('Amortissement des frais d\'établissement', 0, 30000), '2813': ('Amortissement des constructions', 0, 500000),
    '2815': ('Amortissement des installations techniques', 0, 600000), '28182': ('Amortissement du matériel de transport', 0, 40000), '28183': ('Amortissement du matériel de bureau', 0, 25000),
    '28184': ('Amortissement du mobilier', 0, 30000), '2961': ('Dépréciation des titres de participation', 0, 120000), '31': ('Stocks de matières premières', 700000, 0),
    '355': ('Stocks de produits finis', 300000, 0), '37': ('Stocks de marchandises', 650000, 0), '391': ('Dépréciation des stocks de matières premières', 0, 40000),
    '401': ('Fournisseurs', 0, 1550000), '408': ('Fournisseurs, factures non parvenues', 0, 53300), '411': ('Clients', 1900000, 0), '416': ('Clients douteux', 400000, 0),
    '4181': ('Clients, factures à établir', 181600, 0), '421': ('Personnel, rémunérations dues', 0, 145000), '431': ('Sécurité sociale', 0, 130000), '437': ('Autres organismes sociaux', 0, 94000),
    '444': ('État, impôt sur les bénéfices', 0, 310000), '44551': ('TVA à décaisser', 0, 120000), '481': ('Charges à répartir', 80000, 0), '486': ('Charges constatées d\'avance', 2000, 0),
    '487': ('Produits constatés d\'avance', 0, 400), '491': ('Dépréciation des clients', 0, 41000), '503': ('VMP actions', 70000, 0), '512': ('Banque', 101800, 0), '53': ('Caisse', 3000, 0),
    '59': ('Dépréciation des VMP', 0, 6000), '601': ('Achats de matières premières', 4500000, 0), '602': ('Achats d\'autres approvisionnements', 195000, 0), '6031': ('Variation des stocks de matières premières', 510000, 0),
    '6037': ('Variation des stocks de marchandises', 0, 30000), '606': ('Achats non stockés', 300000, 0), '607': ('Achats de marchandises', 3920000, 0), '6097': ('RRR obtenus sur achats de marchandises', 0, 30000),
    '615': ('Entretien et réparations', 1080000, 0), '616': ('Primes d\'assurance', 325000, 0), '626': ('Frais postaux et télécommunications', 900000, 0), '627': ('Services bancaires', 60400, 0),
    '631': ('Impôts et taxes', 900000, 0), '641': ('Rémunérations du personnel', 3200000, 0), '645': ('Charges de sécurité sociale et de prévoyance', 1600000, 0), '654': ('Pertes sur créances irrécouvrables', 3600, 0),
    '661': ('Charges d\'intérêts', 710000, 0), '667': ('Charges nettes sur cessions de VMP', 12900, 0), '675': ('Valeurs comptables des éléments d\'actif cédés', 9600, 0),
    '6811': ('Dotations aux amortissements (immobilisations)', 240000, 0), '6812': ('Dotations aux amortissements des charges à répartir', 20000, 0), '6815': ('Dotations aux provisions d\'exploitation', 30000, 0),
    '6817': ('Dotations aux dépréciations des actifs circulants', 41000, 0), '686': ('Dotations financières', 3000, 0), '6872': ('Dotations aux provisions réglementées', 21000, 0), '695': ('Impôts sur les bénéfices', 310000, 0),
    '701': ('Ventes de produits finis', 0, 15000000), '707': ('Ventes de marchandises', 0, 4111200), '7091': ('RRR accordés sur ventes de produits finis', 72000, 0), '713': ('Variation des stocks de produits finis', 0, 60000),
    '72': ('Production immobilisée', 0, 30000), '74': ('Subventions d\'exploitation', 0, 10000), '761': ('Revenus des titres de participation', 0, 180000), '764': ('Revenus des VMP', 0, 7200),
    '767': ('Produits nets sur cessions de VMP', 0, 800), '775': ('Produits des cessions d\'éléments d\'actif', 0, 2500), '7817': ('Reprises sur dépréciations des actifs circulants', 0, 9000),
    '786': ('Reprises financières', 0, 300), '791': ('Transferts de charges d\'exploitation', 0, 35000),
}


def s_ex11():
    B = BAL11
    td = sum(v[1] for v in B.values())
    tc = sum(v[2] for v in B.values())
    assert td == tc == 32757700, (td, tc)
    s = lambda *k: sum(B[x][1] - B[x][2] for x in k)
    cexp = [('Achats de marchandises (607 − 6097)', s('607', '6097')), ('Variation de stocks de marchandises (6037)', s('6037')), ('Achats de matières premières (601)', s('601')),
            ('Variation de stocks de matières premières (6031)', s('6031')), ('Autres approvisionnements (602)', s('602')), ('Achats non stockés (606)', s('606')),
            ('Services extérieurs (615, 616, 626, 627)', s('615', '616', '626', '627')), ('Impôts et taxes (631)', s('631')), ('Rémunérations (641)', s('641')), ('Charges sociales (645)', s('645')),
            ('Dotations aux amortissements (6811 + 6812)', s('6811', '6812')), ('Dotations aux provisions (6815)', s('6815')), ('Dotations aux dépréciations d\'actifs circulants (6817)', s('6817')), ('Autres charges (654)', s('654'))]
    pexp = [('Ventes de marchandises (707)', -s('707')), ('Ventes de produits finis (701 − 7091)', -s('701', '7091')), ('Production stockée (713)', -s('713')), ('Production immobilisée (72)', -s('72')),
            ('Subventions d\'exploitation (74)', -s('74')), ('Reprises sur dépréciations (7817)', -s('7817')), ('Transferts de charges (791)', -s('791'))]
    cfin = [('Intérêts (661)', s('661')), ('Charges nettes sur cessions de VMP (667)', s('667')), ('Dotations financières (686)', s('686'))]
    pfin = [('Revenus des participations (761)', -s('761')), ('Revenus des VMP (764)', -s('764')), ('Produits nets sur cessions de VMP (767)', -s('767')), ('Reprises financières (786)', -s('786'))]
    cexc = [('Sur opérations en capital (675)', s('675')), ('Dotations aux provisions réglementées (6872)', s('6872'))]
    pexc = [('Sur opérations en capital (775)', -s('775'))]
    tot = lambda l: sum(x[1] for x in l)
    CE, PE, CF, PF, CX, PX = map(tot, (cexp, pexp, cfin, pfin, cexc, pexc))
    IS = s('695')
    RES = (PE + PF + PX) - (CE + CF + CX + IS)
    rows = []
    for (a, b), (c, d) in zip(cexp + [('', '')] * 0, pexp + [('', '')] * (len(cexp) - len(pexp))):
        rows.append([a, b, c, d])
    cr = table(['Charges d\'exploitation', 'Montant', 'Produits d\'exploitation', 'Montant'], rows + [['Sous-total 1', CE, 'Sous-total 1', PE]], num_cols=(1, 3), tot=True)
    rows2 = [[a, b, c, d] for (a, b), (c, d) in zip(cfin + [('', '')], pfin)] + [['Sous-total 2', CF, 'Sous-total 2', PF]]
    cr += table(['Charges financières', 'Montant', 'Produits financiers', 'Montant'], rows2, num_cols=(1, 3), tot=True)
    rows3 = [[cexc[0][0], cexc[0][1], pexc[0][0], pexc[0][1]], [cexc[1][0], cexc[1][1], '', ''], ['Sous-total 3', CX, 'Sous-total 3', PX]]
    cr += table(['Charges exceptionnelles', 'Montant', 'Produits exceptionnels', 'Montant'], rows3, num_cols=(1, 3), tot=True)
    cr += table(['Synthèse', 'Montant'], [['Total des produits', PE + PF + PX], ['Total des charges hors impôt', CE + CF + CX], ['Impôt sur les bénéfices (695)', IS], ['Résultat net (bénéfice)', RES]], num_cols=(1,), tot=True)
    # Bilan
    net = lambda b, a: [b, a, b - a]
    actif = [['Frais d\'établissement'] + net(50000, 30000), ['Fonds commercial'] + net(900000, 0), ['Terrains'] + net(1300000, 0), ['Constructions'] + net(3000000, 500000),
             ['Installations techniques'] + net(1700000, 600000), ['Autres immobilisations corporelles (2182, 2183, 2184)'] + net(255000, 95000),
             ['Participations'] + net(2200000, 120000), ['Autres immobilisations financières (275)'] + net(800, 0)]
    AI = [sum(r[i] for r in actif) for i in (1, 2, 3)]
    circ = [['Matières premières'] + net(700000, 40000), ['Produits finis'] + net(300000, 0), ['Marchandises'] + net(650000, 0),
            ['Créances clients (411 + 416 + 4181)'] + net(2481600, 41000), ['VMP'] + net(70000, 6000), ['Disponibilités (512 + 53)'] + net(104800, 0),
            ['Charges constatées d\'avance'] + net(2000, 0), ['Charges à répartir (481)'] + net(80000, 0)]
    AC = [sum(r[i] for r in circ) for i in (1, 2, 3)]
    TA = AI[2] + AC[2]
    CP = 2000000 + 3202000 + RES + 60000
    passif = [['Capital', 2000000], ['Réserves', 3202000], ['Résultat de l\'exercice', RES], ['Provisions réglementées', 60000], ['Total capitaux propres', CP],
              ['Provisions pour risques', 40000], ['Provisions pour charges', 85000], ['Emprunts auprès des établissements de crédit', 4030000],
              ['Fournisseurs (401 + 408)', 1603300], ['Dettes fiscales et sociales (421, 431, 437, 444, 44551)', 145000 + 130000 + 94000 + 310000 + 120000], ['Produits constatés d\'avance', 400]]
    TP = CP + 40000 + 85000 + 4030000 + 1603300 + 799000 + 400
    assert TA == TP, (TA, TP)
    bil = table(['Actif immobilisé', 'Brut', 'Amort./dépréc.', 'Net'], actif + [['Sous-total actif immobilisé'] + AI], num_cols=(1, 2, 3), tot=True)
    bil += table(['Actif circulant', 'Brut', 'Amort./dépréc.', 'Net'], circ + [['Sous-total actif circulant'] + AC], num_cols=(1, 2, 3), tot=True)
    bil += table(['Passif', 'Montant'], passif + [['TOTAL PASSIF', TP]], num_cols=(1,), tot=True)
    h = H3('Vérification de la balance')
    h += P(f'Total débit = total crédit = {eur(td)} : la balance est équilibrée.')
    h += H3('1. Compte de résultat')
    h += NOTE('Les RRR se retranchent des achats (6097) ou des ventes (7091). Le 713 est créditeur : la production stockée est positive (+60 000). Le 6037 est créditeur : le stock de marchandises a augmenté, la variation (−30 000) vient en déduction des charges.')
    h += cr
    h += H3('2. Bilan')
    h += bil
    h += P(f'Contrôle : total actif net = {eur(TA)} = total passif. Le résultat ({eur(RES)}) est bien l\'élément commun aux deux tableaux.')
    h += NOTE('Présentation : les charges à répartir (481) figurent sous le total de l\'actif circulant, dans une rubrique distincte du modèle officiel. Elles sont regroupées ici pour simplifier.')
    h += H3('3. Nature de l\'entreprise')
    h += P('Elle vend des <b>produits finis</b> qu\'elle fabrique (701, stocks de matières premières et de produits finis, production stockée et immobilisée) <b>et</b> des <b>marchandises</b> achetées pour être revendues (607, 707) : c\'est une entreprise <b>industrielle et commerciale</b>.')
    h += H3('4. Résultat de cession des immobilisations')
    h += FORM('775 − 675 = 2 500 − 9 600 = −7 100 € (moins-value)')
    h += H3('5. Stocks au 1er janvier')
    h += table(['Stock', 'Raisonnement', 'SI'], [['Matières premières', '6031 = SI − SF = 510 000 (débiteur) → SI = 700 000 + 510 000', 1210000], ['Marchandises', '6037 = SI − SF = −30 000 (créditeur) → SI = 650 000 − 30 000', 620000],
                                                ['Produits finis', '713 = SF − SI = 60 000 (créditeur) → SI = 300 000 − 60 000', 240000]], num_cols=(2,))
    return dict(id='cpt-td11', num='TD 11', ch='compta-4', mobiliser=['compta-1', 'compta-2', 'compta-3'], type='Exercice de TD', source=SRC + ' — Exercice 11',
                titre='Société Monceau : compte de résultat et bilan à partir de la balance après inventaire',
                enonce='<p>La société Monceau remet l\'extrait de sa balance après inventaire (total débit = total crédit = 32 757 700 €) :</p>' +
                table(['Compte', 'Intitulé', 'Débit', 'Crédit'], [[k, v[0], v[1] or '', v[2] or ''] for k, v in B.items()], num_cols=(2, 3)) +
                ol(['Établir le compte de résultat.', 'Établir le bilan.', 'Quelle est la nature de l\'entreprise ?', 'Calculer la plus ou moins-value de cession des immobilisations.', 'Calculer le montant des stocks au 1er janvier.']),
                pourquoi='Le chapitre 4 est central (passer de la balance aux documents de synthèse). Il faut aussi relire les amortissements (ch. 1), les provisions (ch. 2) et les variations de stocks (ch. 3).',
                commentaire=ul(['Classer chaque compte : classes 1 à 5 → bilan, classes 6 et 7 → compte de résultat.', 'Les comptes 28, 29, 39, 49, 59 viennent en déduction de l\'actif (colonne du milieu).', 'Le résultat calculé au compte de résultat doit équilibrer le bilan : c\'est le meilleur contrôle.']),
                corrige=h)


def s_ds_q():
    vf = [('Les amortissements dérogatoires ne modifient pas l\'actif du bilan.', True, 'Ils figurent en capitaux propres (145) ; l\'actif ne contient que l\'amortissement comptable.'),
          ('Les pertes de change potentielles donnent lieu à des provisions pour charges exceptionnelles.', False, 'Ce sont des provisions pour risques (1515), dotées en charges financières (6865).'),
          ('Les terrains peuvent être amortis en dégressif ou en linéaire, au choix.', False, 'Les terrains ne sont pas amortissables (pas de durée d\'utilisation limitée).'),
          ('Un loyer déjà encaissé pour l\'année suivante est un produit constaté d\'avance.', True, 'Il est retiré des produits de l\'exercice (compte 487).'),
          ('Les logiciels ne s\'usent pas, ils ne sont donc pas amortis.', False, 'L\'amortissement couvre aussi l\'obsolescence technique : les logiciels sont des immobilisations incorporelles amortissables.'),
          ('La TVA collectée sur les créances envers les clients douteux doit être payée même si ceux-ci n\'ont pas payé leur dû.', True, 'Elle n\'est récupérée que si la créance devient irrécouvrable ; c\'est pourquoi la dépréciation porte sur le HT.'),
          ('Lorsqu\'on cède des titres immobilisés, il faut reprendre les amortissements correspondants.', False, 'Les titres ne s\'amortissent pas ; on reprend les éventuelles dépréciations.'),
          ('Les provisions pour litiges avec un client doivent être reprises quand l\'issue du litige est connue, même s\'il y a perte.', True, 'La provision devient sans objet : on la reprend et on enregistre la charge réelle.')]
    h = H3('1. Vrai ou faux')
    h += table(['Affirmation', 'Réponse', 'Justification'], [[a, 'Vrai' if v else 'Faux', j] for a, v, j in vf])
    h += H3('2. Séparation des exercices')
    h += P('Le principe de séparation (indépendance) des exercices impose de rattacher à chaque exercice les produits qui y ont été acquis et les charges engagées pour les obtenir, <b>quelles que soient les dates d\'encaissement ou de paiement</b> et les dates des pièces. Conséquences : un produit enregistré d\'avance (loyer encaissé pour l\'an prochain) est retiré par un <b>produit constaté d\'avance</b> (débit 7…, crédit 487). Un produit acquis mais pas encore facturé est ajouté par un <b>produit à recevoir</b> (débit 4181 ou 4687, crédit 7… et 44587). Ces écritures sont contrepassées au 1er janvier.')
    h += H3('3. Provisions réglementées')
    h += P('Ce sont des provisions qui ne correspondent ni à une dépréciation ni à un risque, mais à des <b>dispositions fiscales</b> : amortissements dérogatoires, provision pour hausse des prix, provisions propres à certaines professions. Dotées par le 687 (6872…) et inscrites en <b>capitaux propres</b> (14), elles <b>réduisent le résultat imposable</b> (impôt différé, trésorerie améliorée). Comme elles restent dans les capitaux propres, les ressources libérées <b>restent dans l\'entreprise</b> et ne sont pas distribuées. Elles sont généralement reprises plus tard (787).')
    return dict(id='cpt-ds-q', num='DS', ch='compta-0', mobiliser=['compta-1', 'compta-2', 'compta-3'], type='DS (questions de cours)', source='DS de novembre 2019 — Questions (8 points)',
                titre='DS 2019 : vrai/faux et questions de cours (dérogatoire, écarts de conversion, séparation des exercices, provisions réglementées)',
                enonce='<p>TVA à 20 %.</p>' + ol(['Les affirmations suivantes sont-elles vraies ou fausses ?' + ul([x[0] for x in vf]), 'Expliquer le principe comptable de séparation des exercices et ses conséquences sur les produits constatés d\'avance ou à recevoir.', 'Que sont les provisions réglementées et quel en est l\'intérêt pour les entreprises ?']),
                pourquoi='Questions transversales : principes (intro), amortissements (ch. 1), provisions (ch. 2), régularisations (ch. 3).',
                commentaire=ul(['Pour chaque vrai/faux, justifie par une règle du cours en une phrase.']), corrige=h)


def s_ds_ex1():
    j = jours_restants(15, 5)
    dot_new = r2(50000 / 15 * j / 360)
    h = H3('1. Écritures de 2019')
    h += journal(E_('15/05/2019', [('D', '213', 'Constructions', 50000), ('D', '44562', 'TVA sur immobilisations', 10000), ('C', '404', 'Fournisseurs d\'immobilisations', 60000)], 'Achat à crédit du bâtiment'),
                 E_('05/09/2019', [('D', '512', 'Banque', 30000), ('C', '775', 'Produits des cessions d\'éléments d\'actif', 30000)], 'Vente des titres de participation'),
                 E_('05/09/2019', [('D', '675', 'Valeurs comptables des éléments d\'actif cédés', 25000), ('C', '261', 'Titres de participation', 25000)], 'Sortie des titres'))
    h += H3('2. Dotation 2019 du nouveau bâtiment')
    h += FORM(f'50 000 / 15 = 3 333,33 par an · du 15/05 au 31/12 : {j} jours → 3 333,33 × {j}/360 = {eur(dot_new, 2)}')
    h += H3('3. Écritures de fin d\'année 2019')
    tot = r2(200 + 15000 + 25000 + dot_new)
    h += journal(E_('31/12/2019', [('D', '6811', 'Dotations aux amortissements', tot), ('C', '2805', 'Amortissement des brevets', 200), ('C', '2813', 'Amortissement des constructions', r2(15000 + dot_new)), ('C', '2815', 'Amortissement des installations techniques', 25000)]),
                 E_('31/12/2019', [('D', '2961', 'Dépréciation des titres de participation', 4500), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 4500)], 'Titres cédés : dépréciation sans objet'))
    h += P('Résultat de cession des titres : 30 000 − 25 000 = +5 000 €, auquel s\'ajoute la reprise de 4 500 € (le gain par rapport à la valeur nette de 20 500 € est de 9 500 €).')
    h += H3('4. Annexe')
    h += table(['Immobilisations', 'Début', 'Augm.', 'Dim.', 'Fin'], [['Brevet', 12000, 0, 0, 12000], ['Terrains', 300000, 0, 0, 300000], ['Constructions', 160000, 50000, 0, 210000], ['Installations techniques', 500000, 0, 0, 500000], ['Titres de participation', 25000, 0, 25000, 0]], num_cols=(1, 2, 3, 4))
    h += table(['Amortissements', 'Début', 'Augm.', 'Dim.', 'Fin'], [['Brevet', 3000, 200, 0, 3200], ['Constructions', 110000, r2(15000 + dot_new), 0, r2(125000 + dot_new)], ['Installations techniques', 300000, 25000, 0, 325000]], num_cols=(1, 2, 3, 4))
    h += table(['Provisions (dépréciations)', 'Début', 'Augm.', 'Dim.', 'Fin'], [['Titres de participation', 4500, 0, 4500, 0]], num_cols=(1, 2, 3, 4))
    h += H3('5. Actif immobilisé au 31/12/2019')
    rows = [['Brevet', 12000, 3200], ['Terrains', 300000, 0], ['Constructions', 210000, r2(125000 + dot_new)], ['Installations techniques', 500000, 325000]]
    rows = [r + [r2(r[1] - r[2])] for r in rows]
    rows.append(['Total', sum(r[1] for r in rows), r2(sum(r[2] for r in rows)), r2(sum(r[3] for r in rows))])
    h += table(['Poste', 'Brut', 'Amort./dépréc.', 'Net'], rows, num_cols=(1, 2, 3), tot=True)
    return dict(id='cpt-ds-ex1', num='DS', ch='compta-1', mobiliser=['compta-2', 'compta-4'], type='DS (exercice)', source='DS de novembre 2019 — Exercice 1 (6 points)',
                titre='DUMONT : acquisition d\'un bâtiment, cession de titres, annexe et actif immobilisé 2019',
                enonce='<p>Actif immobilisé au 31/12/2018 (brut / amortissements et provisions / net) : brevet 12 000 / 3 000 / 9 000 ; terrains 300 000 / — / 300 000 ; constructions 160 000 / 110 000 / 50 000 ; installations techniques 500 000 / 300 000 / 200 000 ; titres de participation 25 000 / 4 500 / 20 500.</p><p>En 2019 : acquisition à crédit d\'un bâtiment de 50 000 € HT le 15 mai, amorti sur 15 ans en linéaire ; vente des titres de participation pour 30 000 € le 5 septembre. Dotations 2019 : brevets 200, anciennes constructions 15 000, installations techniques 25 000.</p>' +
                ol(['Écritures de l\'année 2019.', 'Dotation 2019 du nouveau bâtiment.', 'Écritures de fin d\'année.', 'Annexes (immobilisations, amortissements, provisions).', 'Actif immobilisé au 31/12/2019.']),
                pourquoi='Le chapitre 1 est central (dotation au prorata). Le chapitre 2 intervient pour la reprise de la dépréciation des titres cédés et le chapitre 4 pour l\'annexe et le bilan.',
                commentaire=ul(['La dépréciation des titres vendus devient sans objet : on la reprend.', 'Le prorata court à partir du 15/05 (hypothèse : mise en service à la date d\'acquisition).']),
                corrige=h)


def s_ds_ex2():
    h = H3('1. Écritures d\'inventaire 2018')
    h += journal(E_('31/12/2018', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 150000), ('C', '2961', 'Dépréciation des titres de participation', 150000)], 'A : 3 000 × (550 − 500)'),
                 E_('31/12/2018', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 270000), ('C', '590', 'Dépréciation des VMP', 270000)], 'C : 10 % × 2 700 000'),
                 E_('31/12/2018', [('D', '416', 'Clients douteux', 120000), ('C', '411', 'Clients', 120000)], 'Client D'),
                 E_('31/12/2018', [('D', '6817', 'Dotations aux dépréciations des actifs circulants', 50000), ('C', '491', 'Dépréciation des comptes clients', 50000)], '50 % × 120 000 / 1,2'))
    h += P('Titres B : valeur actuelle (3 100) supérieure au coût (3 000) → aucune écriture (plus-value latente non comptabilisée).')
    h += H3('2. Écritures de 2019')
    h += journal(E_('04/04/2019', [('D', '512', 'Banque', 1500000), ('C', '506', 'VMP — obligations', 1350000), ('C', '767', 'Produits nets sur cessions de VMP', 150000)], 'Moitié du portefeuille C'),
                 E_('02/09/2019', [('D', '654', 'Pertes sur créances irrécouvrables', 100000), ('D', '44571', 'TVA collectée', 20000), ('C', '416', 'Clients douteux', 120000)], 'Faillite du client D'),
                 E_('31/12/2019', [('D', '491', 'Dépréciation des comptes clients', 50000), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 50000)], 'Dépréciation de D sans objet'),
                 E_('31/12/2019', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 60000), ('C', '2961', 'Dépréciation des titres de participation', 60000)], 'A : 3 000 × (550 − 480) = 210 000, existante 150 000'),
                 E_('31/12/2019', [('D', '590', 'Dépréciation des VMP', 270000), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 270000)], 'C restant : coût 1 350 000 < valeur 1 600 000'))
    h += P('Titres B : 3 050 > 3 000 → toujours aucune dépréciation.')
    return dict(id='cpt-ds-ex2', num='DS', ch='compta-2', mobiliser=['compta-4'], type='DS (exercice)', source='DS de novembre 2019 — Exercice 2 (6 points)',
                titre='Titres (participation, immobilisés, VMP) et client défaillant sur deux exercices',
                enonce='<p><b>Inventaire 2018</b> : 3 000 actions A (titres de participation) achetées 550 € en 2015, évaluées 500 € en 2018 ; 200 obligations B (titres immobilisés) achetées 3 000 €, valeur fin 2018 3 100 € ; portefeuille d\'obligations C (VMP) acheté 2,7 millions €, dépréciation de 10 % constituée en fin d\'année ; créance sur le client D de 120 000 € TTC dépréciée à 50 % au 31/12/2018. Passer les écritures d\'inventaire 2018.</p><p><b>2019</b> : actions A évaluées 480 €, obligations B 3 050 € ; le 4 avril, vente de la moitié du portefeuille C pour 1,5 million € ; en fin d\'année les titres C restants valent 1,6 million € ; faillite du client D le 2 septembre. Passer les écritures de 2019.</p>',
                pourquoi='Le chapitre 2 est central (titres et créances) et le chapitre 4 sert à la lecture des effets.',
                commentaire=ul(['Pour les VMP vendues, la dépréciation correspondante devient sans objet : l\'ajustement global de fin d\'année la reprend.', 'Faillite = créance irrécouvrable : perte HT et récupération de la TVA.']),
                corrige=h)


def sujets():
    return [s_ex1(), s_ex2(), s_ex3(), s_ex4(), s_ex5(), s_ex6(), s_ex7(), s_ex8(), s_ex9(), s_ex10(), s_ex11(), s_ds_q(), s_ds_ex1(), s_ds_ex2()]
