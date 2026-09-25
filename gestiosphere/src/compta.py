"""Matière : Comptabilité des sociétés (6 documents)."""
from lib import ul, P, fr
import compta_cours as C
from compta_sujets import sujets
from calc_compta import plan_lineaire, plan_degressif
from svg import Plot, boxes, COL

DOCS = ['Compta des sociétés — intro et amortissement (24 diapos)', 'Provisions pour dépréciations (8 diapos)', 'Autres provisions (9 diapos)',
        'Régularisations (10 diapos)', 'Documents de synthèse (7 diapos)', 'Poly de TD L2 (18 pages, dont DS de novembre 2019)']


def chapitres():
    c0, c1, c2, c3, c4 = C.ch0(), C.ch1(), C.ch2(), C.ch3(), C.ch4()
    return [
        dict(id='compta-0', num=0, titre='Introduction : principes comptables et inventaire', sous='Inventaire comptable · écritures d\'inventaire · 8 principes · plan de comptes',
             desc='Pourquoi et comment on clôture un exercice : travaux d\'inventaire, balance avant et après inventaire, principes (prudence, séparation des exercices, image fidèle…).',
             tags=['Inventaire', 'Principes', 'Plan de comptes'], sources=[C.SRC_INTRO], cours=c0.html, notions=c0.notions,
             methode=P('Pour toute écriture d\'inventaire, pose-toi trois questions : <b>quel principe</b> la justifie (prudence, séparation des exercices, coût historique) ; <b>quel chapitre</b> (amortissement, dépréciation, provision, régularisation) ; <b>quel impact</b> sur le bilan et sur le résultat.'),
             fiches=[dict(q='Quels sont les trois documents des comptes annuels ?', a='Le bilan, le compte de résultat et l\'annexe.'),
                     dict(q='Quels sont les deux objets des écritures d\'inventaire ?', a='Reporter les conséquences des évaluations extra-comptables et rattacher les charges et produits à l\'exercice qui convient.'),
                     dict(q='Quelles classes du plan de comptes vont au bilan ?', a='Les classes 1 à 5 (capitaux, immobilisations, stocks, tiers, financiers). Les classes 6 et 7 sont des comptes de gestion.'),
                     dict(q='Quel principe interdit de comptabiliser une plus-value latente ?', a='Le principe de prudence (et celui du coût historique).')],
             quiz=[dict(type='qcm', q='Quel est le point de départ des travaux d\'inventaire ?', opts=['La balance avant inventaire', 'Le bilan de l\'exercice précédent', 'Le compte de résultat', 'L\'annexe'], ans=0, exp='La balance avant inventaire récapitule les comptes après les opérations courantes ; les écritures d\'inventaire mènent à la balance après inventaire.'),
                   dict(type='vf', q='Les comptes de la classe 6 et 7 figurent au bilan.', ans=False, exp='Ce sont des comptes de gestion : ils forment le compte de résultat et sont remis à zéro chaque exercice.'),
                   dict(type='qcm', q='Quel principe justifie les charges à payer et les produits constatés d\'avance ?', opts=['Séparation des exercices', 'Coût historique', 'Permanence des méthodes', 'Entité'], ans=0, exp='Les charges et produits doivent être rattachés à l\'exercice qu\'ils concernent.'),
                   dict(type='qcm', q='Quelle classe regroupe les comptes de tiers (clients, fournisseurs, État) ?', opts=['Classe 4', 'Classe 3', 'Classe 5', 'Classe 1'], ans=0, exp='Classe 4 : comptes de tiers.'),
                   dict(type='vf', q='Le principe de prudence conduit à provisionner les moins-values probables mais pas les plus-values probables.', ans=True, exp='Asymétrie voulue : on anticipe les pertes, pas les gains.'),
                   dict(type='qcm', q='Que permet la partie double ?', opts=['Tout débit s\'accompagne d\'un crédit de même montant', 'Enregistrer deux fois chaque facture', 'Séparer charges et produits', 'Tenir deux journaux'], ans=0, exp='Tout débit a une contrepartie au crédit de même montant.'),
                   dict(type='qcm', q='Lequel n\'est PAS un travail d\'inventaire extra-comptable ?', opts=['L\'enregistrement d\'une facture de vente courante', 'Le comptage des stocks', 'L\'évaluation des créances', 'L\'évaluation des immobilisations'], ans=0, exp='Une facture courante est une opération de l\'exercice, pas un travail d\'inventaire.')],
             carte=dict(core='L\'inventaire comptable', branches=[
                 dict(t='Objectif', items=['Comptes annuels : bilan, CR, annexe', 'Résultat et valeur des actifs/passifs', 'Au moins une fois par an']),
                 dict(t='Deux types de travaux', items=['Inventaire extra-comptable : recenser, évaluer', 'Écritures d\'inventaire : reporter, rattacher']),
                 dict(t='Écritures d\'inventaire', items=['Variations de stocks (ch.3)', 'Amortissements (ch.1)', 'Dépréciations et provisions (ch.2)', 'Ajustement charges/produits (ch.3)']),
                 dict(t='Principes', items=['Prudence', 'Séparation des exercices', 'Coût historique', 'Continuité, permanence', 'Régularité, sincérité, image fidèle']),
                 dict(t='Plan de comptes', items=['Classes 1-5 : bilan', 'Classes 6-7 : gestion', '28/29/39/49/59 : comptes soustractifs'])],
                 schemas=[dict(t='Chaîne de la clôture', steps=['Opérations courantes', 'Balance avant inventaire', 'Écritures d\'inventaire', 'Balance après inventaire', 'Bilan + CR + annexe'])]),
             liens=[dict(ch='compta-1', pourquoi='Les amortissements sont la première famille d\'écritures d\'inventaire (continuité d\'exploitation, coût historique).'),
                    dict(ch='compta-2', pourquoi='Les dépréciations et provisions appliquent la prudence et la séparation des exercices.'),
                    dict(ch='compta-3', pourquoi='Les régularisations sont l\'application directe de la séparation des exercices.'),
                    dict(ch='compta-4', pourquoi='Le bilan, le compte de résultat et l\'annexe sont le produit final de l\'inventaire.')]),
        dict(id='compta-1', num=1, titre='Les amortissements', sous='Linéaire · dégressif · dérogatoire · cession des immobilisations',
             desc='Plan d\'amortissement au prorata temporis, coefficients dégressifs, amortissements dérogatoires (145), cession avec plus ou moins-value.',
             tags=['6811', '28', 'Dégressif', '145', 'Cession'], sources=[C.SRC_AMORT, C.SRC_TD + ' (ex. 1, 2, 3)'], cours=c1.html, notions=c1.notions,
             methode=ul(['Déterminer la <b>valeur d\'entrée</b> (prix + frais accessoires, HT).', 'Linéaire : taux = 1/durée, prorata en <b>jours / 360</b> depuis la <b>mise en service</b>.', 'Dégressif : taux linéaire × coefficient (1,25 / 1,75 / 2,25), prorata en <b>mois</b> depuis le <b>1er du mois d\'acquisition</b>, bascule au linéaire quand 1/durée restante > taux dégressif.', 'Dérogatoire = dégressif − linéaire (6872/145 ou 145/7872).', 'Cession : dotation complémentaire → reprise du dérogatoire → sortie (28 + 675 / 21) → prix (512 / 775 + 44571).']),
             fiches=[dict(q='Coefficients fiscaux du dégressif ?', a='1,25 pour 3 ou 4 ans ; 1,75 pour 5 ou 6 ans ; 2,25 au-delà de 6 ans.'),
                     dict(q='Comment se forme le numéro du compte d\'amortissement de 2183 ?', a='On intercale un 8 : 28183 Amortissement du matériel informatique.'),
                     dict(q='Quand passe-t-on du taux dégressif au linéaire ?', a='Dès que le taux linéaire calculé sur la durée restante devient supérieur au taux dégressif.'),
                     dict(q='Que devient le compte 145 lors de la cession du bien ?', a='Il est soldé : les amortissements dérogatoires restants sont repris (145 / 7872).'),
                     dict(q='Différence entre date d\'acquisition et date de mise en service ?', a='Le linéaire part de la mise en service (en jours), le dégressif du 1er jour du mois d\'acquisition (en mois).')],
             quiz=[dict(type='qcm', q='Une machine de 60 000 € amortie sur 6 ans en dégressif : quel est le taux dégressif ?', opts=['29,17 %', '16,67 %', '20,83 %', '37,5 %'], ans=0, exp='Taux linéaire 16,67 % × coefficient 1,75 = 29,17 %.', tag='calcul'),
                   dict(type='qcm', q='Mise en service le 16/03/N, bien de 36 000 € amorti sur 5 ans en linéaire. Première annuité (année de 360 jours) ?', opts=['5 680 €', '7 200 €', '5 400 €', '6 000 €'], ans=0, exp='7 200 × 284/360 = 5 680 € (14 jours en mars + 9 mois × 30 = 284).', tag='calcul'),
                   dict(type='qcm', q='Quel compte enregistre la dotation aux amortissements des immobilisations ?', opts=['6811', '6872', '6866', '6817'], ans=0, exp='6811 Dotations aux amortissements des immobilisations incorporelles et corporelles.', tag='compte'),
                   dict(type='vf', q='Le fonds commercial est amortissable.', ans=False, exp='Le cours classe le fonds commercial (207) parmi les immobilisations non amortissables.'),
                   dict(type='vf', q='L\'amortissement est une charge décaissée.', ans=False, exp='C\'est une charge calculée, non décaissée.'),
                   dict(type='qcm', q='Dégressif > linéaire : quelle écriture pour l\'excédent ?', opts=['6872 à 145', '145 à 7872', '6811 à 28', '681 à 491'], ans=0, exp='Dotation aux provisions réglementées (6872) au crédit du 145 Amortissements dérogatoires.', tag='compte'),
                   dict(type='qcm', q='Bien de 20 000 €, amortissements cumulés 14 000 €, vendu 5 000 €. Résultat de cession ?', opts=['Moins-value de 1 000 €', 'Plus-value de 5 000 €', 'Moins-value de 15 000 €', 'Plus-value de 1 000 €'], ans=0, exp='VNC = 6 000 ; 5 000 − 6 000 = −1 000.', tag='calcul'),
                   dict(type='qcm', q='Où figure le compte 28 au bilan ?', opts=['En déduction de l\'actif (colonne amortissements)', 'Au passif, en provisions', 'En capitaux propres', 'Au compte de résultat'], ans=0, exp='Compte d\'actif soustractif : brut − amortissements = net.'),
                   dict(type='vf', q='Le dégressif peut s\'appliquer à un bien d\'occasion.', ans=False, exp='Il est réservé aux biens neufs d\'une durée d\'au moins 3 ans et éligibles.'),
                   dict(type='qcm', q='Durée d\'usage fiscale d\'une voiture particulière selon le cours ?', opts=['5 ans', '4 ans', '10 ans', '3 ans'], ans=0, exp='Voitures particulières : 5 ans ; poids lourds : 4 ans.'),
                   dict(type='qcm', q='Bien de 28 000 € acquis le 2 janvier, dégressif 5 ans (35 %). 2ᵉ annuité ?', opts=['6 370 €', '9 800 €', '5 600 €', '4 140,50 €'], ans=0, exp='An 1 : 9 800, VNC 18 200 ; an 2 : 18 200 × 35 % = 6 370.', tag='calcul'),
                   dict(type='qcm', q='Lors d\'une cession, quel compte enregistre la valeur nette du bien sorti ?', opts=['675', '775', '681', '462'], ans=0, exp='675 Valeurs comptables des éléments d\'actif cédés.', tag='compte'),
                   dict(type='vf', q='Avant de sortir un bien cédé, il faut comptabiliser une dotation complémentaire jusqu\'à la date de cession.', ans=True, exp='Première étape de la cession : mettre à jour l\'amortissement.')],
             carte=dict(core='Les amortissements', branches=[
                 dict(t='Justification', items=['Usure physique', 'Obsolescence technique', 'Raisons juridiques et fiscales', 'Charge calculée non décaissée']),
                 dict(t='Linéaire (comptable)', items=['Taux = 1/durée', 'Prorata jours/360 dès la mise en service', '6811 / 28…']),
                 dict(t='Dégressif (fiscal)', items=['Coef 1,25 / 1,75 / 2,25', '× VNC début', 'Prorata mois dès le mois d\'acquisition', 'Bascule au linéaire en fin de plan']),
                 dict(t='Dérogatoire', items=['Dégressif − linéaire', '6872 / 145 puis 145 / 7872', 'Capitaux propres, pas l\'actif']),
                 dict(t='Cession', items=['Dotation complémentaire', 'Sortie : 28 + 675 / 21', 'Prix : 512 / 775 + 44571', '± value = 775 − 675']),
                 dict(t='Non amortissables', items=['Terrains', 'Fonds commercial, droit au bail', 'Immobilisations en cours', 'Immobilisations financières'])],
                 schemas=[dict(t='Cession d\'une immobilisation', steps=['Dotation jusqu\'à la cession', 'Reprise du dérogatoire', 'Sortie du bien à la VNC (675)', 'Prix de cession (775)', 'Plus ou moins-value']),
                          dict(t='Du fiscal au comptable', steps=['Dégressif (fiscal)', '− linéaire (comptable)', '= dérogatoire', 'Provision réglementée 145', 'Impôt différé'])]),
             liens=[dict(ch='compta-0', pourquoi='Coût historique et continuité d\'exploitation justifient l\'amortissement.'),
                    dict(ch='compta-2', pourquoi='Le dérogatoire est une provision réglementée ; les titres immobilisés se déprécient au lieu de s\'amortir.'),
                    dict(ch='compta-4', pourquoi='Tableaux des immobilisations et des amortissements de l\'annexe ; présentation brut / amortissements / net.')]),
        dict(id='compta-2', num=2, titre='Les provisions', sous='Dépréciations (titres, créances, stocks) · risques et charges · provisions réglementées · écarts de conversion',
             desc='Dépréciations d\'actifs (29, 39, 49, 59), provisions pour risques et charges (15), provisions réglementées (14), écarts de conversion (476/477).',
             tags=['Prudence', '491', '6866', '15', '476/477'], sources=[C.SRC_DEP, C.SRC_AUTRES, C.SRC_TD + ' (ex. 4 à 7)'], cours=c2.html, notions=c2.notions,
             methode=ul(['Construire un <b>tableau d\'ajustement</b> : existante → nécessaire → dotation ou reprise.', 'Titres : ligne par ligne, <b>sans compensation</b>.', 'Créances : transfert TTC au 416, dépréciation sur le <b>HT</b>.', 'Risques et charges : choisir la nature (exploitation 6815, financière 6865, exceptionnelle 6875).', 'Toujours reprendre ce qui devient sans objet.']),
             fiches=[dict(q='Base de la dépréciation d\'une créance douteuse ?', a='Le montant HT de la créance (la TVA sera récupérée si la créance devient irrécouvrable).'),
                     dict(q='Où se place une provision pour risques au bilan ?', a='Au passif, entre les capitaux propres et les dettes (classe 15).'),
                     dict(q='Gain de change latent : que fait-on ?', a='On ajuste la créance ou la dette par un 477 écart de conversion passif, sans constater de produit.'),
                     dict(q='Perte de change latente : que fait-on ?', a='476 écart de conversion actif + provision pour perte de change (6865 / 1515).'),
                     dict(q='Valeur actuelle d\'une VMP cotée à l\'inventaire ?', a='Le cours moyen du dernier mois.'),
                     dict(q='Provision pour hausse des prix : de quoi s\'agit-il ?', a='Provision réglementée qui évite la surestimation des stocks en période de hausse des prix, pour la fraction de hausse qui dépasse 10 % sur 1 ou 2 ans.')],
             quiz=[dict(type='qcm', q='Créance de 6 000 € TTC (TVA 20 %), perte probable 40 %. Dépréciation ?', opts=['2 000 €', '2 400 €', '3 000 €', '1 600 €'], ans=0, exp='6 000 / 1,2 = 5 000 HT × 40 % = 2 000 €.', tag='calcul'),
                   dict(type='qcm', q='Quel compte crédite-t-on pour déprécier des VMP ?', opts=['590', '2971', '491', '397'], ans=0, exp='590 Dépréciation des VMP.', tag='compte'),
                   dict(type='qcm', q='Amende fiscale probable : quelle dotation ?', opts=['6875 (exceptionnelle)', '6815 (exploitation)', '6865 (financière)', '6817'], ans=0, exp='Le cours classe l\'amende fiscale en caractère exceptionnel (687).', tag='compte'),
                   dict(type='vf', q='On peut compenser la moins-value latente d\'un titre avec la plus-value latente d\'un autre titre de nature différente.', ans=False, exp='Interdit par le principe de prudence.'),
                   dict(type='vf', q='Une provision pour risques n\'est constituée que s\'il existe une obligation envers un tiers.', ans=True, exp='Condition rappelée par le cours.'),
                   dict(type='qcm', q='Titres : 100 actions achetées 50 €, cours de fin 42 €, dépréciation existante 300 €. Écriture ?', opts=['Dotation de 500 €', 'Reprise de 300 €', 'Dotation de 800 €', 'Aucune'], ans=0, exp='Nécessaire 800, existante 300 → dotation 500.', tag='calcul'),
                   dict(type='qcm', q='Dans quel compte transfère-t-on une créance devenue douteuse ?', opts=['416', '491', '654', '411'], ans=0, exp='416 Clients douteux ou litigieux, pour le montant TTC.', tag='compte'),
                   dict(type='qcm', q='Contrepartie d\'une dotation aux provisions réglementées ?', opts=['Compte 14 (capitaux propres)', 'Compte 15 (provisions)', 'Compte 29', 'Compte 49'], ans=0, exp='Les provisions réglementées sont en capitaux propres (14).', tag='compte'),
                   dict(type='qcm', q='Quand les écritures d\'écart de conversion sont-elles contrepassées ?', opts=['Au 1er janvier de l\'exercice suivant', 'Au règlement de la facture', 'Jamais', 'À la fin de l\'exercice suivant'], ans=0, exp='Contrepassées au 1er janvier ; la provision pour perte de change est reprise au règlement.'),
                   dict(type='vf', q='La dépréciation des stocks compare le coût d\'entrée au prix de vente net des coûts de distribution.', ans=True, exp='Valeur actuelle = prix de vente net des coûts de distribution.'),
                   dict(type='qcm', q='Créance irrécouvrable de 1 200 € TTC : montant de la perte au 654 ?', opts=['1 000 €', '1 200 €', '200 €', '800 €'], ans=0, exp='Perte HT 1 000, TVA de 200 récupérée.', tag='calcul')],
             carte=dict(core='Les provisions', branches=[
                 dict(t='Dépréciations d\'actif', items=['Titres : 2961, 2971, 590 / 6866-7866', 'Créances : 416, 491 / 6817-7817', 'Stocks : 391, 395, 397 / 6817-7817', 'Pas de compensation (prudence)']),
                 dict(t='Risques et charges (15)', items=['Obligation envers un tiers', 'Litiges, garanties, amendes, change', '6815 / 6865 / 6875', 'Passif, avant les dettes']),
                 dict(t='Réglementées (14)', items=['Dispositions fiscales', 'Hausse des prix, dérogatoire', '6872 / 7872', 'Capitaux propres']),
                 dict(t='Écarts de conversion', items=['476 actif = perte latente', '477 passif = gain latent', 'Provision 1515 si perte', 'Contrepassation au 1/1']),
                 dict(t='Règle d\'ajustement', items=['Nécessaire − existante', '> 0 : dotation', '< 0 : reprise', 'Sans objet : reprise totale'])],
                 schemas=[dict(t='Créance douteuse → irrécouvrable', steps=['411 → 416 (TTC)', 'Dépréciation sur le HT (491)', 'Ajustement chaque clôture', 'Perte certaine : 654 + 44571', 'Reprise du 491']),
                          dict(t='Perte de change latente', steps=['Facture en devises', 'Devise défavorable à la clôture', '476 écart actif', 'Provision 6865 / 1515', 'Reprise au règlement'])]),
             liens=[dict(ch='compta-0', pourquoi='Prudence (pas de plus-value latente, pas de compensation) et séparation des exercices (risques nés dans l\'exercice).'),
                    dict(ch='compta-1', pourquoi='Les amortissements dérogatoires sont des provisions réglementées (145).'),
                    dict(ch='compta-3', pourquoi='Dépréciation des stocks, à passer avec la variation de stocks.'),
                    dict(ch='compta-4', pourquoi='Tableau des provisions de l\'annexe ; place au bilan (actif, provisions, capitaux propres).')]),
        dict(id='compta-3', num=3, titre='Les régularisations de fin d\'exercice', sous='Variations de stocks · charges à payer · produits à recevoir · CCA / PCA',
             desc='Remplacer le stock initial par le stock final (603, 713) et rattacher charges et produits au bon exercice (408, 418, 486, 487…).',
             tags=['603', '713', '486', '487', '408'], sources=[C.SRC_REGUL, C.SRC_TD + ' (ex. 8, 9)'], cours=c3.html, notions=c3.notions,
             methode=ul(['Stocks : annuler le SI, constater le SF ; vérifier le sens (achats SI − SF, produits SF − SI).', 'Pour chaque facture à cheval : la pièce est-elle <b>reçue/émise</b> ? Non → charge à payer / produit à recevoir. Oui mais le service concerne N+1 → CCA / PCA.', 'Calculer au prorata du temps (mois) et en HT.', 'Ne pas oublier la contrepassation au 1er janvier.']),
             fiches=[dict(q='Loyer trimestriel de 3 000 € payé le 1er décembre : écriture au 31/12 ?', a='CCA de 2 000 € (janvier et février) : 486 à 613.'),
                     dict(q='Que signifie un 603 créditeur ?', a='Le stock a augmenté (SF > SI) : la variation vient en déduction des charges.'),
                     dict(q='Compte des factures non parvenues ?', a='408 (4081) Fournisseurs, factures non parvenues.'),
                     dict(q='Compte des factures à établir ?', a='418 (4181) Clients, factures à établir.')],
             quiz=[dict(type='qcm', q='SI marchandises 20 000, SF 26 000. Solde du 6037 ?', opts=['Créditeur de 6 000', 'Débiteur de 6 000', 'Débiteur de 46 000', 'Créditeur de 26 000'], ans=0, exp='SI − SF = −6 000 : solde créditeur, le stock a augmenté.', tag='calcul'),
                   dict(type='qcm', q='Produits finis : SI 50 000, SF 42 000. Production stockée ?', opts=['−8 000', '+8 000', '+42 000', '−50 000'], ans=0, exp='SF − SI = −8 000 : déstockage.', tag='calcul'),
                   dict(type='qcm', q='Assurance annuelle de 1 200 € payée le 1er octobre N : CCA au 31/12/N ?', opts=['900 €', '300 €', '1 200 €', '0 €'], ans=0, exp='9 mois concernent N+1 : 1 200 × 9/12 = 900 €.', tag='calcul'),
                   dict(type='qcm', q='Compte de régularisation d\'un produit constaté d\'avance ?', opts=['487', '486', '4181', '4687'], ans=0, exp='487 Produits constatés d\'avance.', tag='compte'),
                   dict(type='vf', q='Une charge à payer se passe pour son montant TTC au débit du compte de charge.', ans=False, exp='Charge au HT ; dette au TTC ; TVA au 44586.'),
                   dict(type='vf', q='Les écritures de régularisation sont contrepassées au premier jour de l\'exercice suivant.', ans=True, exp='Cela permet d\'enregistrer ensuite normalement la facture.'),
                   dict(type='qcm', q='Les coûts administratifs entrent-ils dans le coût de production des stocks ?', opts=['Non, ils sont exclus', 'Oui, toujours', 'Oui, pour les marchandises', 'Seulement s\'ils sont fixes'], ans=0, exp='Le cours précise que les coûts administratifs sont exclus.'),
                   dict(type='qcm', q='Intérêts courus sur un emprunt, non échus au 31/12 : compte de dette ?', opts=['1688', '4686', '5186', '428'], ans=0, exp='1688 Intérêts courus sur emprunts.', tag='compte')],
             carte=dict(core='Les régularisations', branches=[
                 dict(t='Stocks achetés', items=['31, 32, 37 / 603', 'Annuler SI : 603 à 3…', 'SF : 3… à 603', 'Variation = SI − SF (charge)']),
                 dict(t='Stocks produits', items=['35 / 713', 'Annuler SI : 713 à 35', 'SF : 35 à 713', 'Production stockée = SF − SI']),
                 dict(t='Pièce pas encore reçue/émise', items=['Charge à payer : 6… + 44586 / 408, 428…', 'Produit à recevoir : 418, 468 / 7… + 44587']),
                 dict(t='Pièce déjà enregistrée', items=['CCA : 486 / 6…', 'PCA : 7… / 487', 'Prorata en mois, HT']),
                 dict(t='Principe', items=['Séparation des exercices', 'Contrepassation au 1er janvier'])],
                 schemas=[dict(t='Choisir la bonne régularisation', steps=['La facture est-elle enregistrée ?', 'Non : charge à payer / produit à recevoir', 'Oui, mais concerne N+1 : CCA / PCA', 'Contrepasser au 1/1'])]),
             liens=[dict(ch='compta-0', pourquoi='Application directe du principe de séparation des exercices.'),
                    dict(ch='compta-2', pourquoi='Dépréciation des stocks, calculée au même moment que la variation de stocks.'),
                    dict(ch='compta-4', pourquoi='Postes de régularisation au bilan (486, 487) ; variations de stocks et production stockée au compte de résultat.')]),
        dict(id='compta-4', num=4, titre='Les documents de synthèse', sous='Bilan · compte de résultat · annexe · liens entre les tableaux',
             desc='Structure du bilan et du compte de résultat, correspondance comptes → postes, lien par le résultat, usages en analyse financière et en comptabilité analytique.',
             tags=['Bilan', 'Compte de résultat', 'Annexe'], sources=[C.SRC_SYNTH, C.SRC_TD + ' (ex. 10, 11)'], cours=c4.html, notions=c4.notions,
             methode=ul(['Classer chaque compte de la balance : classes 1-5 au bilan, 6-7 au compte de résultat.', 'Soustraire 28/29/39/49/59 dans la colonne du milieu de l\'actif.', 'Retrancher les RRR (609, 709) des achats et des ventes.', 'Calculer le résultat au CR, le reporter au passif, vérifier l\'égalité actif = passif.']),
             fiches=[dict(q='Seul élément commun au bilan et au compte de résultat ?', a='Le résultat de l\'exercice.'),
                     dict(q='Image du bilan et du compte de résultat selon le cours ?', a='Le bilan est une photographie (patrimoine) ; le compte de résultat est un film (formation du résultat).'),
                     dict(q='Poste du bilan des comptes 16 et 51 créditeurs ?', a='Emprunts et dettes assimilées.')],
             quiz=[dict(type='qcm', q='Dans quel poste figure le compte 145 ?', opts=['Capitaux propres (provisions réglementées)', 'Provisions pour risques', 'Actif immobilisé', 'Dettes'], ans=0, exp='145 est une provision réglementée (14) : capitaux propres.'),
                   dict(type='qcm', q='Où se place le compte 487 ?', opts=['Au passif', 'À l\'actif', 'Au compte de résultat', 'Dans l\'annexe seulement'], ans=0, exp='Produits constatés d\'avance : passif.'),
                   dict(type='qcm', q='Balance : ventes 100, RRR accordés 5, achats 60, RRR obtenus 2. Marge simplifiée (ventes nettes − achats nets) ?', opts=['37', '43', '40', '33'], ans=0, exp='(100 − 5) − (60 − 2) = 95 − 58 = 37.', tag='calcul'),
                   dict(type='vf', q='Les comptes du compte de résultat sont remis à zéro à chaque fin d\'exercice.', ans=True, exp='Ils mesurent les flux d\'un exercice.'),
                   dict(type='qcm', q='Dans quelle partie du compte de résultat figurent 675 et 775 ?', opts=['Exceptionnel', 'Exploitation', 'Financier', 'Impôt'], ans=0, exp='Opérations en capital : exceptionnel.'),
                   dict(type='qcm', q='6031 débiteur de 10 000, SF de matières 40 000 : stock initial ?', opts=['50 000', '30 000', '40 000', '10 000'], ans=0, exp='SI − SF = 10 000 → SI = 50 000.', tag='calcul'),
                   dict(type='vf', q='Le transfert d\'une créance de 411 à 416 modifie le résultat.', ans=False, exp='C\'est une écriture purement bilancielle.')],
             carte=dict(core='Les documents de synthèse', branches=[
                 dict(t='Bilan (photographie)', items=['Actif : immobilisé, circulant', 'Passif : capitaux propres, provisions, dettes', 'Comptes cumulatifs']),
                 dict(t='Compte de résultat (film)', items=['Exploitation', 'Financier', 'Exceptionnel', 'Impôt → résultat net']),
                 dict(t='Annexe', items=['Tableau des immobilisations', 'Tableau des amortissements', 'Tableau des provisions', 'Méthodes']),
                 dict(t='Liens', items=['Le résultat, élément commun', 'Actif = passif', 'Analyse financière', 'Comptabilité analytique'])],
                 schemas=[dict(t='De la balance aux comptes annuels', steps=['Balance après inventaire', 'Classes 6-7 → CR', 'Résultat', 'Classes 1-5 + résultat → bilan', 'Contrôle actif = passif'])]),
             liens=[dict(ch='compta-1', pourquoi='Tableaux des immobilisations et des amortissements.'), dict(ch='compta-2', pourquoi='Tableau des provisions ; place des 14, 15, 29-59.'),
                    dict(ch='compta-3', pourquoi='Variations de stocks et comptes de régularisation.'), dict(ch='compta-0', pourquoi='Image fidèle : objectif des comptes annuels.')]),
    ]


COMPTES = [
    ('101', 'Capital', 'compta-4'), ('106', 'Réserves', 'compta-4'), ('14', 'Provisions réglementées', 'compta-2'), ('145', 'Amortissements dérogatoires', 'compta-1'),
    ('1511', 'Provisions pour litiges', 'compta-2'), ('1512', 'Provisions pour garanties données aux clients', 'compta-2'), ('1514', 'Provisions pour amendes et pénalités', 'compta-2'), ('1515', 'Provisions pour pertes de change', 'compta-2'),
    ('164', 'Emprunts auprès des établissements de crédit', 'compta-4'), ('1688', 'Intérêts courus sur emprunts', 'compta-3'),
    ('201', 'Frais d\'établissement', 'compta-1'), ('205', 'Concessions, brevets, licences', 'compta-1'), ('207', 'Fonds commercial', 'compta-1'), ('211', 'Terrains', 'compta-1'), ('213', 'Constructions', 'compta-1'),
    ('2154', 'Matériel industriel', 'compta-1'), ('2182', 'Matériel de transport', 'compta-1'), ('2183', 'Matériel de bureau et informatique', 'compta-1'), ('2184', 'Mobilier', 'compta-1'),
    ('261', 'Titres de participation', 'compta-2'), ('271', 'Titres immobilisés (droit de propriété)', 'compta-2'), ('28', 'Amortissements des immobilisations', 'compta-1'),
    ('2961', 'Dépréciation des titres de participation', 'compta-2'), ('2971', 'Dépréciation des titres immobilisés', 'compta-2'),
    ('31', 'Stocks de matières premières', 'compta-3'), ('326', 'Emballages', 'compta-3'), ('355', 'Stocks de produits finis', 'compta-3'), ('37', 'Stocks de marchandises', 'compta-3'),
    ('391', 'Dépréciation des stocks de matières premières', 'compta-2'), ('395', 'Dépréciation des stocks de produits', 'compta-2'), ('397', 'Dépréciation des stocks de marchandises', 'compta-2'),
    ('401', 'Fournisseurs', 'compta-4'), ('404', 'Fournisseurs d\'immobilisations', 'compta-1'), ('4081', 'Fournisseurs, factures non parvenues', 'compta-3'), ('411', 'Clients', 'compta-2'),
    ('416', 'Clients douteux ou litigieux', 'compta-2'), ('4181', 'Clients, factures à établir', 'compta-3'), ('4198', 'Clients, RRR à accorder', 'compta-3'), ('428', 'Personnel, charges à payer', 'compta-3'),
    ('4386', 'Organismes sociaux, charges à payer', 'compta-3'), ('44562', 'TVA déductible sur immobilisations', 'compta-1'), ('44571', 'TVA collectée', 'compta-2'),
    ('4458', 'État, TVA à régulariser', 'compta-3'), ('44586', 'TVA sur factures non parvenues', 'compta-3'), ('44587', 'TVA sur factures à établir', 'compta-3'),
    ('4486', 'État, charges à payer', 'compta-3'), ('462', 'Créances sur cessions d\'immobilisations', 'compta-1'), ('4686', 'Divers, charges à payer', 'compta-3'), ('4687', 'Divers, produits à recevoir', 'compta-3'),
    ('476', 'Différences de conversion actif', 'compta-2'), ('477', 'Différences de conversion passif', 'compta-2'), ('486', 'Charges constatées d\'avance', 'compta-3'), ('487', 'Produits constatés d\'avance', 'compta-3'),
    ('491', 'Dépréciation des comptes clients', 'compta-2'), ('503', 'VMP — actions', 'compta-2'), ('512', 'Banque', 'compta-4'), ('590', 'Dépréciation des VMP', 'compta-2'),
    ('6031', 'Variation des stocks de matières premières', 'compta-3'), ('6037', 'Variation des stocks de marchandises', 'compta-3'), ('607', 'Achats de marchandises', 'compta-4'), ('613', 'Locations', 'compta-3'),
    ('654', 'Pertes sur créances irrécouvrables', 'compta-2'), ('666', 'Pertes de change', 'compta-2'), ('667', 'Charges nettes sur cessions de VMP', 'compta-2'),
    ('6712', 'Pénalités, amendes fiscales et pénales', 'compta-2'), ('675', 'Valeurs comptables des éléments d\'actif cédés', 'compta-1'),
    ('6811', 'Dotations aux amortissements des immobilisations', 'compta-1'), ('6815', 'Dotations aux provisions d\'exploitation (risques et charges)', 'compta-2'),
    ('6817', 'Dotations aux dépréciations des actifs circulants', 'compta-2'), ('6865', 'Dotations aux provisions financières (risques et charges)', 'compta-2'),
    ('6866', 'Dotations aux dépréciations des éléments financiers', 'compta-2'), ('6872', 'Dotations aux provisions réglementées', 'compta-1'), ('6875', 'Dotations aux provisions exceptionnelles', 'compta-2'),
    ('695', 'Impôts sur les bénéfices', 'compta-4'), ('707', 'Ventes de marchandises', 'compta-4'), ('7135', 'Variation des stocks de produits', 'compta-3'), ('752', 'Revenus des immeubles non affectés', 'compta-3'),
    ('766', 'Gains de change', 'compta-2'), ('767', 'Produits nets sur cessions de VMP', 'compta-2'), ('775', 'Produits des cessions d\'éléments d\'actif', 'compta-1'),
    ('7815', 'Reprises sur provisions d\'exploitation (risques et charges)', 'compta-2'), ('7817', 'Reprises sur dépréciations des actifs circulants', 'compta-2'),
    ('7866', 'Reprises sur dépréciations des éléments financiers', 'compta-2'), ('7872', 'Reprises sur provisions réglementées', 'compta-1'), ('7875', 'Reprises sur provisions exceptionnelles', 'compta-2'),
]

FORMULES = [
    dict(titre='Amortissements', ch='compta-1', items=[
        dict(t='Taux linéaire', f='t = 100 % / n'), dict(t='Annuité linéaire', f='A = Valeur d\'entrée × t'),
        dict(t='1ʳᵉ annuité (prorata)', f='A × jours depuis la mise en service / 360', note='Année commerciale, mois de 30 jours'),
        dict(t='Taux dégressif', f='t × coefficient (1,25 · 1,75 · 2,25)', note='3-4 ans · 5-6 ans · > 6 ans'), dict(t='Annuité dégressive', f='VNC début × taux dégressif (× mois / 12 la 1ʳᵉ année)'),
        dict(t='Bascule au linéaire', f='si 1 / durée restante > taux dégressif → VNC / durée restante'), dict(t='VNC', f='Valeur brute − cumul des amortissements'),
        dict(t='Dérogatoire', f='Dégressif − linéaire (> 0 : 6872/145 ; < 0 : 145/7872)'), dict(t='Résultat de cession', f='Prix de cession (775) − VNC (675)')]),
    dict(titre='Provisions et dépréciations', ch='compta-2', items=[
        dict(t='Ajustement', f='Nécessaire − existante : > 0 dotation, < 0 reprise'), dict(t='Dépréciation d\'une créance', f='TTC / 1,20 × % de perte probable'),
        dict(t='Dépréciation de titres', f='(Valeur d\'entrée − valeur actuelle) × nombre, si positif'), dict(t='Garanties', f='Quantités vendues × % de pannes × coût unitaire de réparation'),
        dict(t='Créance irrécouvrable', f='654 = HT ; 44571 = TVA ; 416 = TTC')]),
    dict(titre='Régularisations', ch='compta-3', items=[
        dict(t='Variation de stock (achats)', f='SI − SF (603)'), dict(t='Production stockée', f='SF − SI (713)'), dict(t='Achats consommés', f='Achats + SI − SF'),
        dict(t='CCA / PCA', f='Montant HT × durée sur N+1 / durée totale'), dict(t='Charge à payer', f='6… (HT) + 44586 (TVA) = 408… (TTC)')]),
    dict(titre='Documents de synthèse', ch='compta-4', items=[
        dict(t='Équilibre du bilan', f='Actif = Capitaux propres + Provisions + Dettes'), dict(t='Résultat', f='Produits − Charges'),
        dict(t='Résultat par niveaux', f='Exploitation + Financier + Exceptionnel − IS'), dict(t='Net à l\'actif', f='Brut − amortissements et dépréciations')]),
]

AUTEURS = [
    dict(nom='Plan comptable général (PCG)', kind='Texte de référence', dates='Règlement ANC n° 2014-03', courant='Normalisation comptable', source='cours', chapitres=['compta-0', 'compta-4'],
         idee='Nomenclature des comptes (classes 1 à 7) et règles d\'évaluation et de présentation des comptes annuels ; ton cours demande d\'apporter ton plan de comptes à l\'examen.',
         desc='Le cours s\'appuie sur l\'organisation du plan de comptes (classes, numérotation des amortissements et dépréciations par insertion d\'un 8 ou d\'un 9) et sur les postes des documents de synthèse.',
         phrase='« Conformément au PCG, la dépréciation est inscrite dans un compte de la classe correspondante avec un 9 en deuxième position. »'),
    dict(nom='Code de commerce', kind='Texte de référence', dates='Articles L123-12 et suivants', courant='Droit comptable', source='compl', chapitres=['compta-0', 'compta-4'],
         idee='Pose l\'obligation pour les commerçants de faire un inventaire au moins une fois tous les douze mois et d\'établir des comptes annuels réguliers, sincères et donnant une image fidèle.',
         phrase='« Les comptes annuels doivent être réguliers, sincères et donner une image fidèle du patrimoine, de la situation financière et du résultat. »'),
    dict(nom='Code général des impôts', kind='Texte de référence', dates='Art. 39 A (dégressif) · art. 39-1-5° (provisions)', courant='Droit fiscal', source='compl', chapitres=['compta-1', 'compta-2'],
         idee='Encadre les amortissements et provisions déductibles : coefficients de l\'amortissement dégressif, conditions de déduction des provisions. C\'est la source des amortissements dérogatoires et des provisions réglementées.',
         phrase='« La différence entre l\'amortissement fiscal et l\'amortissement comptable est constatée en amortissements dérogatoires. »'),
    dict(nom='Luca Pacioli', kind='Auteur', dates='v. 1445 – 1517', courant='Origines de la comptabilité', source='compl', chapitres=['compta-0'], oeuvres=['Summa de arithmetica, geometria, proportioni et proportionalita (1494)'],
         idee='Premier exposé imprimé de la comptabilité en partie double : tout débit a pour contrepartie un crédit de même montant.',
         phrase='« La partie double, formalisée par Pacioli dès 1494, garantit l\'égalité des débits et des crédits. »'),
    dict(nom='Ordonnance du commerce (Colbert)', kind='Texte historique', dates='1673', courant='Origines du droit comptable', source='compl', chapitres=['compta-0'],
         idee='Première obligation légale française de tenir des livres et de dresser périodiquement un inventaire : l\'ancêtre de l\'inventaire annuel.',
         phrase='« Dès 1673, l\'ordonnance de Colbert impose aux marchands la tenue de livres et l\'établissement d\'inventaires. »'),
    dict(nom='Autorité des normes comptables (ANC)', kind='Institution', dates='Créée en 2009', courant='Normalisation comptable', source='compl', chapitres=['compta-0'],
         idee='Organisme qui élabore les règlements comptables français, dont le PCG en vigueur (règlement 2014-03).', phrase=''),
]

REPERES = [
    dict(date='1494', t='Luca Pacioli publie le premier exposé imprimé de la partie double.'),
    dict(date='1673', t='Ordonnance du commerce de Colbert : obligation de tenir des livres et de faire des inventaires.'),
    dict(date='1947', t='Premier plan comptable général en France.'), dict(date='1957', t='Révision du plan comptable général.'),
    dict(date='1978', t='4ᵉ directive européenne sur les comptes annuels (notion d\'image fidèle).'),
    dict(date='1982', t='Nouveau PCG, qui intègre la 4ᵉ directive.'), dict(date='1983', t='Loi comptable du 30 avril 1983 : les principes (régularité, sincérité, image fidèle) entrent dans le Code de commerce.'),
    dict(date='1999', t='PCG réécrit (règlement CRC 99-03).'), dict(date='2005', t='Normes IFRS obligatoires pour les comptes consolidés des sociétés cotées de l\'UE (les comptes individuels restent au PCG).'),
    dict(date='2014', t='Règlement ANC 2014-03 : PCG actuellement en vigueur.'),
    dict(date='Chaque 31/12', t='Clôture de l\'exercice : inventaire, écritures d\'inventaire, comptes annuels (ton cours).', src='cours'),
]

METHODE = [
    dict(titre='Passer une écriture d\'inventaire sans se tromper', html='<ol><li>Identifier le <b>chapitre</b> : amortissement, dépréciation, provision, stock, régularisation.</li><li>Calculer le <b>montant</b> (prorata, HT, nécessaire − existant).</li><li>Choisir la <b>nature</b> (exploitation, financier, exceptionnel) pour la dotation ou la reprise.</li><li>Écrire débit puis crédit ; vérifier que total débit = total crédit.</li><li>Rédiger un <b>libellé</b> qui montre le calcul.</li></ol>',
         piege='Oublier de reprendre une provision devenue sans objet, ou confondre dotation et reprise quand la provision nécessaire baisse.'),
    dict(titre='Tableau d\'amortissement', html='<ol><li>Valeur d\'entrée HT (+ frais accessoires).</li><li>Linéaire : jours / 360 depuis la mise en service.</li><li>Dégressif : mois depuis le 1er du mois d\'acquisition ; taux × coefficient ; tester chaque année le passage au linéaire.</li><li>Colonnes : année, base, taux, annuité, cumul, VNC.</li><li>Vérifier que le cumul final = la base.</li></ol>',
         piege='Appliquer le prorata en jours au dégressif, ou partir de la date d\'achat au lieu de la mise en service pour le linéaire.'),
    dict(titre='Tableau d\'ajustement des provisions', html='<ol><li>Une ligne par titre ou par client.</li><li>Colonnes : base (coût ou créance HT), existante, nécessaire, dotation, reprise.</li><li>Titres : pas de compensation entre lignes.</li><li>Créances : transfert TTC au 416, perte sur le HT, TVA récupérée si irrécouvrable.</li><li>Une écriture globale de dotation et une de reprise par nature de compte.</li></ol>',
         piege='Calculer la dépréciation d\'une créance sur le TTC.'),
    dict(titre='Construire bilan et compte de résultat depuis une balance', html='<ol><li>Vérifier que la balance est équilibrée.</li><li>Classes 6 et 7 → compte de résultat, ventilé en exploitation, financier et exceptionnel.</li><li>RRR (609/709) en moins des achats et ventes ; variations de stocks à leur place.</li><li>Calculer le résultat, le reporter au passif.</li><li>Classes 1 à 5 → bilan, avec les comptes 28-29-39-49-59 en colonne du milieu.</li><li>Contrôler actif = passif.</li></ol>',
         piege='Mettre les amortissements (28) au passif, ou oublier le résultat dans les capitaux propres.'),
    dict(titre='Répondre à un vrai/faux de cours', html='<p>Réponds, puis <b>justifie par la règle</b> en une phrase (« Faux : les terrains ne sont pas amortissables car leur durée d\'utilisation n\'est pas limitée »). Une réponse non justifiée rapporte rarement tous les points.</p>'),
]


def courbes():
    base = 98000
    lin = plan_lineaire(base, 5, 26, 4, 2017)
    deg, _, _ = plan_degressif(base, 5, 4, 2017)
    p = Plot(2022.3, 100000, 'Exercice', 'VNC (€)', xmin=2016.7).axes(xticks=range(2017, 2023), yticks=range(0, 100001, 20000), fmt=lambda v: f'{v:.0f}', xfmt=lambda v: str(v))
    p.curve([(2016.8, base)] + [(r[0], r[5]) for r in lin], COL[0], label='Linéaire', lpos=(2020, lin[3][5] + 6000))
    p.curve([(2016.8, base)] + [(r[0], r[6]) for r in deg], COL[1], label='Dégressif', lpos=(2018.1, deg[1][6] - 9000))
    for r in lin:
        p.point(r[0], r[5], COL[0], r=3)
    for r in deg:
        p.point(r[0], r[6], COL[1], r=3)
    g1 = p.svg()
    p2 = Plot(2022.6, 28000, 'Exercice', 'Annuité (€)', xmin=2016.4).axes(xticks=range(2017, 2023), yticks=range(0, 28001, 7000), fmt=lambda v: f'{v:.0f}')
    p2.bars([(r[0], r[3]) for r in lin], COL[0], width=0.34, offset=-0.18, fmt=lambda v: fr(v, 0))
    p2.bars([(r[0], r[4]) for r in deg], COL[1], width=0.34, offset=0.18, fmt=lambda v: fr(v, 0))
    p2.legend([(COL[0], 'Linéaire (comptable)'), (COL[1], 'Dégressif (fiscal)')], x=330)
    g2 = p2.svg()
    # compte 145
    cum = 0
    pts = [(2016.8, 0)]
    L = {r[0]: r[3] for r in lin}
    for r in deg:
        cum += r[4] - L[r[0]]
        pts.append((r[0], cum))
    p3 = Plot(2022.3, 20000, 'Exercice', 'Solde du 145 (€)', xmin=2016.7).axes(xticks=range(2017, 2023), yticks=range(0, 20001, 5000), fmt=lambda v: f'{v:.0f}')
    p3.area(pts + [(2022, 0)], COL[2], 0.12).curve(pts, COL[2], label='Amortissements dérogatoires cumulés', lpos=(2017.3, 19000))
    g3 = p3.svg()
    g4 = boxes(520, 300, [
        (20, 20, 230, 150, 'CHARGES', ['Exploitation (60 à 65, 681)', 'Financières (66, 686)', 'Exceptionnelles (67, 687)', 'Impôt sur les bénéfices (695)', 'Résultat net (bénéfice)'], COL[1]),
        (270, 20, 230, 150, 'PRODUITS', ['Exploitation (70 à 75, 781)', 'Financiers (76, 786)', 'Exceptionnels (77, 787)', '', ''], COL[2]),
        (20, 190, 230, 95, 'ACTIF', ['Immobilisé (2)', 'Circulant (3, 4, 5)', 'Brut − amort./dépréc. = net'], COL[0]),
        (270, 190, 230, 95, 'PASSIF', ['Capitaux propres (1) + résultat', 'Provisions (15)', 'Dettes (16, 40, 42-44…)'], COL[3])],
        arrows=[(135, 152, 385, 238, 'le résultat passe au bilan')])
    g5 = boxes(520, 250, [
        (10, 20, 150, 70, 'Opérations', ['de l\'exercice', '(journal)'], COL[5]), (185, 20, 150, 70, 'Balance', ['avant inventaire'], COL[0]),
        (360, 20, 150, 70, 'Inventaire', ['extra-comptable', '(recenser, évaluer)'], COL[3]), (185, 140, 150, 80, 'Écritures', ['stocks · amortissements', 'provisions · régul.'], COL[1]),
        (360, 140, 150, 80, 'Comptes annuels', ['bilan · CR · annexe'], COL[2]), (10, 140, 150, 80, 'Balance', ['après inventaire'], COL[0])],
        arrows=[(160, 55, 183, 55, ''), (335, 55, 358, 55, ''), (435, 92, 290, 138, ''), (185, 180, 162, 180, ''), (85, 222, 358, 222, '')])
    return [
        dict(id='cpt-g1', ch='compta-1', titre='VNC : linéaire contre dégressif (machine DEBROS, 98 000 €)', svg=g1, tags=['amortissement', 'VNC'],
             exp=ul(['Le dégressif fait baisser la VNC beaucoup plus vite les premières années (35 % de la VNC chaque année).', 'Les deux courbes se rejoignent à zéro à la fin du plan (2022).', 'Tracé à partir des plans calculés de l\'exercice 1 du TD.'])),
        dict(id='cpt-g2', ch='compta-1', titre='Annuités linéaires et dégressives par exercice', svg=g2, tags=['annuité', 'dégressif'],
             exp=ul(['Annuités linéaires constantes (19 600 €) après une 1ʳᵉ annuité réduite au prorata.', 'Annuités dégressives décroissantes, puis constantes après le passage au linéaire (2020-2021).', 'L\'écart entre les barres, année par année, est l\'amortissement dérogatoire.'])),
        dict(id='cpt-g3', ch='compta-1', titre='Vie du compte 145 Amortissements dérogatoires', svg=g3, tags=['dérogatoire', '145'],
             exp=ul(['Le compte monte tant que le dégressif dépasse le linéaire (dotations 6872).', 'Il redescend ensuite (reprises 7872) et revient à zéro en fin de plan.', 'Au total, l\'impôt est seulement décalé dans le temps : c\'est l\'intérêt du dégressif pour la trésorerie.'])),
        dict(id='cpt-g4', ch='compta-4', titre='Structure du compte de résultat et du bilan', svg=g4, tags=['bilan', 'compte de résultat'],
             exp=ul(['Compte de résultat : trois niveaux (exploitation, financier, exceptionnel) puis l\'impôt.', 'Le résultat est le seul élément commun : il passe dans les capitaux propres.', 'À l\'actif, les amortissements et dépréciations viennent en déduction du brut.'])),
        dict(id='cpt-g5', ch='compta-0', titre='Le cycle de l\'inventaire comptable', svg=g5, tags=['inventaire', 'balance'],
             exp=ul(['Les opérations courantes donnent la balance avant inventaire.', 'L\'inventaire extra-comptable fournit les évaluations.', 'Les écritures d\'inventaire conduisent à la balance après inventaire, puis aux comptes annuels.'])),
    ]


def matiere():
    return dict(id='compta', nom='Comptabilité des sociétés', court='Compta', couleur='#6af7c4',
                sourcesResume='6 documents · 5 chapitres de diapos + poly de TD (11 exercices + DS 2019)', documents=DOCS,
                chapitres=chapitres(), comptes=[dict(num=n, lib=l, ch=c) for n, l, c in COMPTES], formules=FORMULES, auteurs=AUTEURS,
                reperes=REPERES, methode=METHODE, courbes=courbes(), sujets=sujets())
