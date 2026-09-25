"""Comptabilité des sociétés — cours (d'après le poly de diapos : intro et amortissements,
provisions pour dépréciation, autres provisions, régularisations, documents de synthèse)."""
from lib import Cours, E_, table, fr

SRC_INTRO = 'Compta des sociétés — intro et amortissement (diapos 1-8)'
SRC_AMORT = 'Compta des sociétés — intro et amortissement (diapos 9-24)'
SRC_DEP = 'Provisions pour dépréciations (8 diapos)'
SRC_AUTRES = 'Autres provisions (9 diapos)'
SRC_REGUL = 'Régularisations (10 diapos)'
SRC_SYNTH = 'Documents de synthèse (7 diapos)'
SRC_TD = 'Poly de TD L2 — Comptabilité des sociétés'


def ch0():
    c = Cours()
    c.sec('I. L\'inventaire comptable : pourquoi et comment')
    c.p('La situation et les résultats de l\'entreprise doivent faire l\'objet d\'une <b>synthèse périodique</b>, '
        'au moins une fois par an à la clôture de l\'exercice (et souvent plus). Cette synthèse, ce sont les '
        '<b>comptes annuels</b> : le bilan, le compte de résultat et l\'annexe. Ils sont préparés par les <b>travaux d\'inventaire</b>.')
    c.df('Travaux d\'inventaire', 'Travaux qui ont pour but de déterminer le résultat et la valeur des actifs et des passifs à la clôture de l\'exercice comptable. On distingue l\'inventaire extra-comptable et les écritures d\'inventaire.')
    c.df('Inventaire extra-comptable', 'Recensement et évaluation des éléments existants à la clôture : stocks, créances et dettes, immobilisations.')
    c.df('Écritures d\'inventaire', 'Écritures passées à la clôture pour reporter en comptabilité les conséquences des évaluations extra-comptables et pour rattacher les charges et les produits au bon exercice.')
    c.p('Les écritures d\'inventaire comprennent notamment :')
    c.ul(['la comptabilisation des <b>variations de stocks</b> (chapitre 3) ;',
          'l\'enregistrement des <b>amortissements</b> (chapitre 1), des <b>dépréciations</b> et des <b>provisions</b> (chapitre 2) ;',
          'l\'<b>ajustement des charges et des produits</b> : charges à payer, produits à recevoir, charges et produits constatés d\'avance (chapitre 3).'])
    c.df('Balance avant inventaire', 'Récapitulatif de la situation des comptes telle qu\'elle résulte de l\'enregistrement des opérations courantes de l\'exercice : c\'est le point de départ de l\'inventaire.')
    c.df('Balance après inventaire', 'Balance obtenue après les écritures d\'inventaire ; elle sert de base à l\'établissement du compte de résultat et du bilan.')
    c.raw('<div class="formula">Balance avant inventaire → écritures d\'inventaire → balance après inventaire → bilan + compte de résultat + annexe</div>')

    c.sec('II. Les principes comptables à maîtriser')
    c.p('Le cours liste huit principes. Ils justifient presque toutes les écritures d\'inventaire : garde-les en tête pour expliquer <i>pourquoi</i> on passe une écriture.')
    c.df('Principe de l\'entité', 'L\'entreprise est une entité distincte de ses propriétaires : seules ses propres opérations sont enregistrées.')
    c.df('Séparation (indépendance) des exercices', 'Seuls les produits acquis pendant l\'exercice et les charges engagées pour les obtenir sont rattachés à cet exercice, indépendamment des dates d\'encaissement et de paiement.')
    c.df('Coût historique', 'Les biens sont enregistrés à leur valeur d\'entrée (coût d\'acquisition ou de production) ; les plus-values latentes ne sont pas constatées.')
    c.df('Prudence', 'On ne comptabilise pas les gains probables mais on constate les pertes probables : les moins-values latentes sont provisionnées, les plus-values latentes ignorées.')
    c.df('Continuité de l\'exploitation', 'Les comptes sont établis en supposant que l\'entreprise poursuivra son activité ; c\'est ce qui justifie l\'évaluation au coût historique et la répartition des coûts par l\'amortissement.')
    c.df('Permanence des méthodes', 'Les méthodes d\'évaluation et de présentation sont conservées d\'un exercice à l\'autre pour que les comptes restent comparables.')
    c.df('Régularité et sincérité', 'Les comptes respectent les règles en vigueur (régularité) et les appliquent de bonne foi, en traduisant la connaissance que les dirigeants ont de la réalité (sincérité).')
    c.df('Image fidèle', 'Objectif final des comptes annuels : donner une représentation exacte du patrimoine, de la situation financière et du résultat de l\'entreprise.')
    c.note('Exemples de liens : la <b>prudence</b> justifie les dépréciations (ch. 2) et interdit de compenser plus et moins-values entre titres ; la <b>séparation des exercices</b> justifie les charges à payer et les charges constatées d\'avance (ch. 3) ainsi que les provisions pour risques et charges (ch. 2).')

    c.sec('III. Rappels : actif, passif, débit, crédit')
    c.df('Actif du bilan', 'Emplois de l\'entreprise : biens utilisés (immobilisations, stocks), créances et liquidités.')
    c.df('Passif du bilan', 'Ressources de l\'entreprise, c\'est-à-dire ses sources de financement : capitaux propres, provisions, dettes.')
    c.df('Partie double', 'Principe d\'enregistrement selon lequel tout débit s\'accompagne d\'un crédit de même montant, et réciproquement.')
    c.p('Le <b>débit</b> est la colonne de gauche d\'un compte, le <b>crédit</b> la colonne de droite. Exemple des comptes clients : une vente à crédit débite le compte 411 Clients ; le règlement du client le crédite.')
    c.h3('L\'organisation du plan de comptes')
    c.tab(['Classe', 'Contenu', 'Nature'], [
        ['1', 'Comptes de capitaux (capital, réserves, résultat, provisions réglementées, provisions pour risques et charges, emprunts)', 'Bilan'],
        ['2', 'Comptes d\'immobilisations (et leurs amortissements 28, dépréciations 29)', 'Bilan'],
        ['3', 'Comptes de stocks et en-cours (et leurs dépréciations 39)', 'Bilan'],
        ['4', 'Comptes de tiers (clients, fournisseurs, État, personnel, régularisations 48)', 'Bilan'],
        ['5', 'Comptes financiers (VMP, banque, caisse)', 'Bilan'],
        ['6', 'Comptes de charges', 'Gestion'],
        ['7', 'Comptes de produits', 'Gestion'],
    ])
    c.warn('Aux examens, le poly des diapos est autorisé et il faut venir avec ton <b>plan de comptes</b> et ta <b>calculatrice</b>. Organisation : cours et TD, un DS, un examen final.')
    c.sec('IV. Les documents comptables')
    c.df('Journal', 'Livre où les opérations sont enregistrées chronologiquement, en partie double.')
    c.df('Comptes annuels', 'Ensemble formé du bilan, du compte de résultat et de l\'annexe, préparés par les travaux d\'inventaire.')
    c.p('Le bilan, le compte de résultat et l\'annexe sont détaillés au chapitre 4.')
    return c


def ch1():
    c = Cours()
    c.sec('I. Définition et justification de l\'amortissement')
    c.p('Les immobilisations dont la durée d\'utilisation est limitée sont des <b>immobilisations amortissables</b>. L\'amortissement se justifie par :')
    c.ul(['l\'<b>usure physique</b> ;', 'l\'<b>obsolescence technique</b> ;', 'des raisons <b>juridiques et fiscales</b>.'])
    c.p('Dès lors que le patrimoine perd de sa valeur dans le temps, il s\'agit d\'une perte patrimoniale (diminution d\'actif), c\'est-à-dire d\'une charge.')
    c.df('Amortissement', 'Répartition systématique du montant amortissable d\'une immobilisation sur les exercices pendant lesquels elle est utilisée ; c\'est une charge calculée et non décaissée.')
    c.df('Charge calculée', 'Charge qui ne donne lieu à aucun décaissement (amortissements, dépréciations, provisions) : elle diminue le résultat sans diminuer la trésorerie.')
    c.df('Montant amortissable', 'Valeur d\'entrée (brute) de l\'immobilisation diminuée de sa valeur résiduelle en fin d\'utilisation, le plus souvent nulle.')
    c.df('Valeur nette comptable (VNC)', 'Montant inscrit à l\'actif : valeur d\'entrée diminuée du cumul des amortissements (et des éventuelles dépréciations).')
    c.f('VNC = Valeur brute − Cumul des amortissements (− dépréciations)')
    c.h3('Quelles immobilisations sont amortissables ?')
    c.tab(['Compte', 'Nature', 'Amortissable ?'], [
        ['201', 'Frais d\'établissement', 'Oui'], ['203', 'Frais de recherche et développement', 'Oui'],
        ['205', 'Concessions, brevets, licences', 'Oui'], ['206', 'Droit au bail', 'Non'], ['207', 'Fonds commercial', 'Non'],
        ['211', 'Terrains', 'Non'], ['212', 'Aménagements des terrains', 'Oui'], ['213', 'Constructions', 'Oui'],
        ['215', 'Installations techniques, matériels et outillages', 'Oui'], ['218', 'Autres immobilisations corporelles', 'Oui'],
        ['23', 'Immobilisations en cours', 'Non'], ['26/27', 'Immobilisations financières', 'Non'],
    ])
    c.warn('Terrains, fonds commercial, immobilisations en cours et immobilisations financières ne s\'amortissent pas. Les titres peuvent seulement être <b>dépréciés</b> (chapitre 2).')
    c.h3('Durées d\'usage préconisées par l\'administration fiscale')
    c.tab(['Bien', 'Durée'], [['Bâtiments administratifs et commerciaux', '25 ans'], ['Bâtiments industriels', '20 ans'], ['Matériel industriel', '10 ans'],
                                ['Mobilier de bureau', '10 ans'], ['Voitures particulières', '5 ans'], ['Poids lourds', '4 ans'], ['Brevets, concessions', 'durée d\'exclusivité conférée']])

    c.sec('II. L\'amortissement linéaire')
    c.p('Les normes comptables imposent d\'établir un <b>plan d\'amortissement</b> dès la mise en service de chaque bien. En principe, l\'amortissement suit la répartition dans le temps des avantages économiques ; en pratique, le <b>mode linéaire</b> s\'applique par défaut.')
    c.df('Amortissement linéaire', 'Mode d\'amortissement à annuités constantes, calculées au prorata temporis à partir de la date de mise en service du bien.')
    c.df('Prorata temporis', 'Réduction de la première annuité au prorata du temps écoulé entre la mise en service et la fin de l\'exercice (et de la dernière annuité pour compléter le plan).')
    c.f('Taux linéaire = 100 % / durée d\'utilisation<br>Annuité = Valeur d\'entrée × taux linéaire<br>1ʳᵉ annuité = Annuité × nombre de jours depuis la mise en service / 360')
    c.note('Convention des TD : année commerciale de <b>360 jours</b> (mois de 30 jours). Vérification sur l\'exercice 2 du poly : une machine mise en service le 20/08/2012 compte 130 jours en 2012 (10 jours en août + 4 mois × 30).')
    c.ex('Exemple — plan linéaire', '<p>Machine de 98 000 € HT mise en service le 26/04/N, amortie sur 5 ans (taux 20 %, annuité 19 600 €). 1ʳᵉ annuité : 19 600 × 244/360 = 13 284,44 € (4 jours en avril + 8 mois × 30). La dernière annuité (N+5) complète le plan : 19 600 − 13 284,44 = 6 315,56 €.</p>')
    c.df('Amortissement par composants', 'Lorsque les éléments principaux d\'une immobilisation ont des durées d\'utilisation différentes, chacun est amorti séparément sur sa propre durée.')
    c.h3('Comptabilisation')
    c.p('L\'amortissement est une charge calculée inscrite au <b>débit</b> du compte <b>6811 Dotations aux amortissements</b> (classe 6). La perte de valeur est inscrite au <b>crédit</b> d\'un compte <b>28 Amortissements des immobilisations</b> (classe 2). Le compte 28 se forme à partir du numéro de l\'immobilisation : 2183 Matériel informatique → <b>28183</b>.')
    c.ecr(E_('31/12/N', [('D', '6811', 'Dotations aux amortissements', 13284.44), ('C', '28154', 'Amortissement du matériel industriel', 13284.44)], 'Annuité N'))
    c.h3('Présentation au bilan')
    c.p('L\'actif présente <b>trois colonnes</b> : valeur brute (d\'entrée), amortissements et dépréciations cumulés, valeur nette (par différence). Le compte 28 est un compte d\'actif soustractif : il ne figure jamais au passif.')
    c.tab(['Actif immobilisé', 'Brut', 'Amort. et dépréc.', 'Net'], [['Matériel industriel (fin N)', 98000, 13284.44, 84715.56]], num_cols=(1, 2, 3))

    c.sec('III. L\'amortissement dégressif')
    c.p('La charge d\'amortissement est <b>fiscalement déductible</b> du bénéfice imposable : les durées et le calcul des annuités sont réglementés par le code des impôts. Il faut distinguer l\'<b>amortissement comptable</b> (linéaire) de l\'amortissement pratiqué pour des raisons <b>fiscales</b> (dégressif).')
    c.df('Amortissement dégressif', 'Mode d\'amortissement fiscal où l\'annuité est obtenue en appliquant un taux dégressif à la valeur nette comptable du début d\'exercice : les annuités sont fortes au début puis décroissent.')
    c.f('Taux dégressif = taux linéaire × coefficient fiscal<br>Coefficients : 1,25 (3 ou 4 ans) · 1,75 (5 ou 6 ans) · 2,25 (plus de 6 ans)<br>Annuité = VNC début d\'exercice × taux dégressif')
    c.ul(['La 1ʳᵉ annuité est calculée <b>à partir du premier jour du mois d\'acquisition</b> (prorata en mois, pas en jours).',
          'Pour que l\'annuité ne tende pas vers zéro, <b>dès que le taux linéaire calculé sur la durée restante devient supérieur au taux dégressif</b>, on applique ce taux linéaire (on répartit la VNC restante en parts égales).'])
    c.ex('Exemples du cours', '<p>Machine-outil amortie sur 10 ans : taux linéaire 10 %, taux dégressif 10 % × 2,25 = 22,5 %.</p><p>Machine achetée 28 000 € le 2 janvier, durée 5 ans : coefficient 1,75, taux dégressif 35 %. 1ʳᵉ annuité : 28 000 × 35 % = 9 800 € ; VNC 18 200 €. 2ᵉ : 18 200 × 35 % = 6 370 € ; VNC 11 830 €. 3ᵉ : 11 830 × 35 % = 4 140,50 € ; VNC 7 689,50 €. En 4ᵉ année, il reste 2 ans : le taux linéaire (50 %) dépasse 35 %, donc on passe au linéaire, avec 3 844,75 € en 4ᵉ et en 5ᵉ année.</p>')
    c.h3('Comptabilisation : l\'amortissement dérogatoire')
    c.df('Amortissement dérogatoire', 'Différence entre l\'amortissement fiscal (dégressif) et l\'amortissement comptable (linéaire) ; il est enregistré en provision réglementée dans les capitaux propres (compte 145).')
    c.p('<b>Quand dégressif > linéaire</b> (premières années) : le linéaire est doté normalement (6811 / 28) et l\'excédent est une charge exceptionnelle déductible <b>6872 Dotations aux provisions réglementées</b> (le cours dit « 687 ») portée au crédit du <b>145 Amortissements dérogatoires</b>, qui augmente les capitaux propres.')
    c.ecr(E_('31/12/N', [('D', '6811', 'Dotations aux amortissements (linéaire)', 13284.44), ('C', '28154', 'Amortissement du matériel industriel', 13284.44)], 'Part comptable'),
          E_('31/12/N', [('D', '6872', 'Dotations aux provisions réglementées (dérogatoire)', 12440.56), ('C', '145', 'Amortissements dérogatoires', 12440.56)], 'Excédent fiscal : 25 725 (dégressif) − 13 284,44 (linéaire)'))
    c.p('<b>Quand linéaire > dégressif</b> (dernières années) : on annule progressivement le dérogatoire. On débite le <b>145</b> et on crédite <b>7872 Reprises sur provisions réglementées</b> (le cours dit « 787 »), qui est un produit exceptionnel.')
    c.ecr(E_('31/12/N+2', [('D', '145', 'Amortissements dérogatoires', 3157.44), ('C', '7872', 'Reprises sur provisions réglementées', 3157.44)], 'Linéaire 19 600 − dégressif 16 442,56'))
    c.note('Le dérogatoire <b>ne modifie pas l\'actif</b> : les colonnes « amortissements » du bilan contiennent uniquement le linéaire. Il réduit le bénéfice imposable au début, puis le rehausse. Sur la durée totale, dotations et reprises se compensent.')
    c.df('Intérêt du dégressif', 'Réduire la charge d\'impôt en début d\'utilisation : cela lisse l\'impôt, facilite la gestion de trésorerie et permet de réinvestir rapidement.')

    c.sec('IV. La cession des immobilisations')
    c.p('<b>Interprétation patrimoniale</b> : la cession fait sortir un bien du patrimoine ; il sort à sa <b>valeur nette comptable</b> à la date de cession. <b>Interprétation par les flux</b> : le flux physique de sortie est une charge (675), le flux monétaire d\'entrée un produit (775). La différence est la <b>plus-value</b> ou <b>moins-value de cession</b>.')
    c.df('Plus ou moins-value de cession', 'Différence entre le prix de cession (775) et la valeur comptable de l\'élément cédé (675) : positive = plus-value, négative = moins-value.')
    c.f('Résultat de cession = Prix de cession (775) − VNC à la date de cession (675)')
    c.p('Étapes de comptabilisation :')
    c.ul(['<b>Mettre à jour l\'amortissement</b> : dotation complémentaire au prorata jusqu\'à la date de cession (6811 / 28).',
          'Si le bien a fait l\'objet d\'amortissements dérogatoires : les <b>reprendre</b> (145 / 7872).',
          '<b>Sortir le bien</b> : débit 28 (cumul des amortissements) et 675 (VNC), crédit du compte 21 (valeur brute).',
          '<b>Constater le prix</b> : débit 512 (ou 462 Créances sur cessions d\'immobilisations), crédit 775 Produits des cessions d\'éléments d\'actif et 44571 TVA collectée.'])
    c.ex('Exemple', '<p>Camion acquis 19 000 € HT, amorti en linéaire sur 5 ans, cumul 1 900 € au jour de la vente, cédé 9 500 € HT (TVA 20 %) :</p>' +
         __import__('lib').journal(
             E_('Date de cession', [('D', '28182', 'Amortissement du matériel de transport', 1900), ('D', '675', 'Valeurs comptables des éléments d\'actif cédés', 17100), ('C', '2182', 'Matériel de transport', 19000)], 'Sortie du bien'),
             E_('Date de cession', [('D', '512', 'Banque', 11400), ('C', '775', 'Produits des cessions d\'éléments d\'actif', 9500), ('C', '44571', 'TVA collectée', 1900)], 'Prix de cession')) +
         '<p>Moins-value : 9 500 − 17 100 = −7 600 €.</p>')

    c.sec('V. Récapitulatif et documents de synthèse')
    c.tab(['Opération', 'Débit', 'Crédit'], [
        ['Dotation (linéaire)', '6811', '28…'], ['Dérogatoire : dégressif > linéaire', '6872', '145'], ['Dérogatoire : linéaire > dégressif', '145', '7872'],
        ['Cession : sortie du bien', '28… + 675', '21…'], ['Cession : prix', '512 / 462', '775 + 44571']])
    c.p('Au <b>bilan</b> : valeur brute, amortissements cumulés (linéaire) et net à l\'actif ; amortissements dérogatoires en capitaux propres (provisions réglementées). '
        'Au <b>compte de résultat</b> : 6811 en charges d\'exploitation, 6872/7872 en exceptionnel, 675/775 en exceptionnel sur opérations en capital. '
        'Dans l\'<b>annexe</b> : tableau des immobilisations et tableau des amortissements (valeur début, augmentations, diminutions, valeur fin).')
    return c


def ch2():
    c = Cours()
    c.sec('I. Les provisions et leur évaluation')
    c.df('Provision (au sens large)', 'Constatation, à la clôture, d\'une perte de valeur probable d\'un actif (dépréciation) ou d\'une charge probable envers un tiers dont le montant n\'est pas fixé précisément (provision pour risques et charges).')
    c.p('Le cours distingue trois catégories :')
    c.tab(['Catégorie', 'Objet', 'Compte au bilan', 'Place au bilan'], [
        ['Provisions (dépréciations) pour dépréciation', 'Perte de valeur probable d\'un actif autre qu\'une immobilisation amortie', '29, 39, 49, 59', 'En déduction de l\'actif'],
        ['Provisions pour risques et charges', 'Obligation probable (risque) ou certaine (charge) envers un tiers, montant incertain', '15', 'Passif, entre capitaux propres et dettes'],
        ['Provisions réglementées', 'Dispositions fiscales (dont amortissements dérogatoires)', '14', 'Capitaux propres']])
    c.p('<b>Enregistrement</b> : la dotation est une charge calculée (68 : 681 exploitation, 686 financière, 687 exceptionnelle). La reprise, quand la provision devient sans objet ou doit être réduite, est un produit (78 : 781, 786, 787).')
    c.f('Provision nécessaire − Provision existante > 0 → dotation · < 0 → reprise')

    c.sec('II. Provisions pour dépréciation')
    c.p('Un élément d\'actif (autre que les immobilisations amorties) peut se déprécier pour des causes dont les effets ne sont <b>pas jugés irréversibles</b> : on constate alors une <b>dépréciation</b>, qui vient réduire la valeur de l\'actif. Si les effets sont irréversibles, on constate une <b>perte</b>.')
    c.df('Dépréciation', 'Constatation d\'une perte de valeur probable et non irréversible d\'un élément d\'actif ; elle réduit la valeur de l\'actif sans le faire sortir du patrimoine.')
    c.ul(['<b>Titres</b> : titres de participation, titres immobilisés ou VMP peuvent baisser en bourse.', '<b>Stocks</b> : avaries, détériorations, articles passés de mode.', '<b>Créances clients</b> : difficultés temporaires qui rendent le recouvrement aléatoire.'])
    c.h3('2.1 Dépréciation des titres financiers')
    c.tab(['Nature', 'Valeur d\'entrée', 'Valeur actuelle (inventaire)'], [
        ['Titres de participation', 'Prix d\'achat', 'Valeur d\'utilité (valeur d\'usage)'],
        ['Titres immobilisés de l\'activité de portefeuille (TIAP)', 'Prix d\'achat', 'Valeur de marché compte tenu des perspectives d\'évolution'],
        ['Autres titres immobilisés, valeurs mobilières de placement', 'Prix d\'achat', 'Titres cotés : cours moyen du dernier mois · non cotés : valeur probable de réalisation']])
    c.df('Titres de participation', 'Titres dont la possession durable est estimée utile à l\'activité de l\'entreprise (influence ou contrôle) ; compte 261.')
    c.df('Valeurs mobilières de placement (VMP)', 'Titres acquis en vue de réaliser un gain à brève échéance ; compte 50 (503 actions, 506 obligations).')
    c.ul(['Si <b>valeur actuelle &lt; valeur d\'entrée</b> : moins-value probable → dépréciation. Seules les moins-values sont comptabilisées.',
          'Les plus-values probables ne sont <b>pas</b> comptabilisées (prudence) : la <b>compensation entre titres de nature différente est interdite</b>.',
          'Titres de même nature acquis à des dates et cours différents : on compare la valeur actuelle à la <b>valeur globale d\'origine</b> de l\'ensemble.',
          'Dépréciation supplémentaire → dotation ; dépréciation qui se réduit → reprise.'])
    c.p('<b>Comptes</b> : charge <b>6866</b> Dotations aux dépréciations des éléments financiers ; reprise <b>7866</b>. Diminution de l\'actif en ajoutant un <b>9 en deuxième position</b> : <b>2961</b> (titres de participation), <b>2971/2972</b> (titres immobilisés), <b>590</b> (VMP).')
    c.ecr(E_('31/12/N', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 600), ('C', '2971', 'Dépréciation des titres immobilisés', 600)], '150 actions C : (289 − 285) × 150'),
          E_('31/12/N', [('D', '590', 'Dépréciation des VMP', 900), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 900)], 'Dépréciation des actions D ramenée de 2 700 à 1 800'))
    c.h3('2.2 Dépréciation des créances clients')
    c.df('Créance douteuse', 'Créance dont le recouvrement est incertain parce que le client est en difficulté ; elle est transférée au compte 416 Clients douteux ou litigieux.')
    c.df('Créance irrécouvrable', 'Créance définitivement perdue (perte certaine) : on enregistre une perte au 654 (ou 6714) et on régularise la TVA collectée.')
    c.ul(['On ne déprécie que si le non-recouvrement est <b>probable</b> ; si la perte est <b>certaine</b>, on enregistre une créance irrécouvrable.',
          'L\'inventaire des créances douteuses est fait à chaque clôture et ajusté s\'il y a lieu.',
          'La dépréciation est limitée au <b>montant HT</b> de la créance : l\'État rembourse la TVA collectée si la créance devient irrécouvrable, la perte ne porte donc pas sur la TVA.',
          'Le montant total <b>TTC</b> de la créance est transféré du 411 au <b>416</b> Clients douteux.'])
    c.f('Dépréciation nécessaire = Créance TTC / 1,20 × % de perte probable')
    c.ecr(E_('31/12/N', [('D', '416', 'Clients douteux ou litigieux', 8372), ('C', '411', 'Clients', 8372)], 'Transfert de la créance douteuse (TTC)'),
          E_('31/12/N', [('D', '6817', 'Dotations aux dépréciations des actifs circulants', 2093), ('C', '491', 'Dépréciation des comptes clients', 2093)], '8 372 / 1,2 × 30 %'),
          E_('Créance irrécouvrable', [('D', '654', 'Pertes sur créances irrécouvrables', 6179.33), ('D', '44571', 'TVA collectée', 1235.87), ('C', '416', 'Clients douteux', 7415.20)], 'Perte HT + récupération de la TVA'),
          E_('Créance irrécouvrable', [('D', '491', 'Dépréciation des comptes clients', 2000), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 2000)], 'Reprise de la dépréciation devenue sans objet'))
    c.h3('2.3 Dépréciation des stocks')
    c.p('On compare le <b>coût d\'acquisition (ou de production)</b> et la <b>valeur actuelle</b> à l\'inventaire, c\'est-à-dire le prix de vente net des coûts de distribution. La dotation débite le <b>6817</b> et crédite le compte de stock avec un <b>9 en deuxième position</b> : <b>391</b> matières premières, <b>395</b> produits, <b>397</b> marchandises. Reprise par le <b>7817</b> (le cours dit « 781 »).')

    c.sec('III. Provisions pour risques et charges')
    c.df('Provision pour risques et charges', 'Passif constaté quand, à la clôture, une obligation envers un tiers est probable (risque) ou certaine (charge) mais que son montant n\'est pas fixé de façon précise ; compte 15.')
    c.ul(['Exemples : litige avec un client, un fournisseur ou un salarié, garanties données aux clients, amendes et pénalités, pertes de change.',
          'Elles apparaissent au bilan <b>entre les capitaux propres et les dettes</b> (classe 15).',
          'Elles affectent à l\'exercice les charges nées pendant l\'exercice (<b>séparation des exercices</b>).',
          'Elles sont <b>obligatoires</b> mais ne se constituent que s\'il existe une <b>obligation envers un tiers</b>.'])
    c.tab(['Nature de la charge provisionnée', 'Dotation (débit)', 'Reprise (crédit)'], [
        ['Activité normale : litige client, fournisseur, salarié, garanties', '6815 (681)', '7815 (781)'],
        ['Financière : perte de change', '6865 (686)', '7865 (786)'],
        ['Exceptionnelle : amende fiscale', '6875 (687)', '7875 (787)']])
    c.p('Principaux comptes : 1511 Provisions pour litiges · 1512 Garanties données aux clients · 1514 Amendes et pénalités · 1515 Pertes de change.')
    c.ecr(E_('31/12/N', [('D', '6815', 'Dotations aux provisions d\'exploitation', 9000), ('C', '1512', 'Provisions pour garanties données aux clients', 9000)], '6 000 unités × 5 % × 30 €'))
    c.h3('Les écarts de conversion')
    c.p('Une facture en devises est convertie en euros <b>au cours du jour</b>. Si le règlement intervient pendant l\'exercice, l\'écart est une perte de change (<b>666</b>) ou un gain de change (<b>766</b>). Si le règlement intervient lors d\'un exercice ultérieur, on enregistre à l\'inventaire la différence de valeur dans des comptes transitoires : les <b>écarts de conversion (476 actif / 477 passif)</b>.')
    c.df('Écart de conversion', 'Compte transitoire (476 actif = perte latente, 477 passif = gain latent) qui enregistre à l\'inventaire la variation de valeur en euros d\'une créance ou d\'une dette en devises non encore réglée.')
    c.tab(['Situation', 'Créance en devises', 'Dette en devises', 'Conséquence'], [
        ['Gain latent', 'Devise appréciée : débit 411 / crédit 477', 'Devise dépréciée : débit 401 / crédit 477', 'Aucun produit constaté (prudence)'],
        ['Perte latente', 'Devise dépréciée : débit 476 / crédit 411', 'Devise appréciée : débit 476 / crédit 401', 'Provision pour perte de change : débit 6865 / crédit 1515']])
    c.p('Les écritures d\'écart de conversion sont <b>contrepassées au 1er janvier</b> de l\'exercice suivant ; la provision pour perte de change est <b>reprise lors du règlement</b> de la facture.')

    c.sec('IV. Provisions réglementées')
    c.df('Provision réglementée', 'Provision sans rapport avec une perte de valeur ou un risque, autorisée par le droit fiscal pour réduire le résultat imposable tout en gardant les ressources dans l\'entreprise ; sa contrepartie est inscrite en capitaux propres (compte 14).')
    c.p('Elles sont l\'analogue des amortissements dérogatoires, mais pour des provisions. Elles permettent de réduire le résultat imposable et de s\'assurer que les ressources ainsi libérées restent dans l\'entreprise et ne sont pas prélevées par l\'exploitant. Elles sont souvent temporaires et reprises ultérieurement.')
    c.tab(['Opération', 'Débit', 'Crédit'], [['Dotation', '687 (6872, 6873, 6874)', '14 Provisions réglementées'], ['Reprise', '14 Provisions réglementées', '787 (7872…)']])
    c.ul(['<b>Provision pour hausse des prix</b> : évite la surestimation des stocks en période de hausse des prix, pour la fraction de hausse excédant 10 % sur une période d\'un ou deux ans.', 'Provisions spécifiques à certaines professions.', '<b>Amortissements dérogatoires</b> (compte 145, chapitre 1).'])

    c.sec('V. Les documents de synthèse')
    c.tab(['Provision', 'Bilan', 'Compte de résultat'], [
        ['Dépréciation d\'actif', 'Colonne « amortissements et dépréciations » de l\'actif (29, 39, 49, 59)', '6817/6866 · 7817/7866'],
        ['Risques et charges', 'Passif : « Provisions » (15)', '6815/6865/6875 · 7815/7865/7875'],
        ['Réglementée', 'Capitaux propres (14)', '6872 · 7872 (exceptionnel)']])
    c.p('L\'annexe comporte un <b>tableau des provisions</b> : pour chaque catégorie (réglementées, risques et charges, dépréciations), valeur début d\'exercice, augmentations (dotations), diminutions (reprises), valeur fin, avec la ventilation des dotations et reprises en exploitation, financier et exceptionnel.')
    return c


def ch3():
    c = Cours()
    c.sec('I. L\'évaluation des stocks')
    c.p('À l\'inventaire, on procède à un <b>inventaire physique</b> des stocks, comme à l\'ouverture de l\'exercice (clôture précédente). Les quantités sont valorisées à un coût unitaire :')
    c.ul(['<b>coût d\'acquisition</b> pour les marchandises et approvisionnements ;', '<b>coût de production</b> pour les produits fabriqués par l\'entreprise ;', 'les <b>coûts administratifs sont exclus</b> de ces coûts.'])
    c.df('Inventaire intermittent', 'Les comptes de stocks ne sont pas mis à jour au fil de l\'année : à la clôture, on annule le stock initial et on constate le stock final.')
    c.p('Comme les stocks ne sont pas actualisés en cours d\'année, il faut <b>remplacer le stock initial (SI) par le stock final (SF)</b>. Les écritures diffèrent selon qu\'il s\'agit de biens achetés (dont l\'achat est une charge) ou de produits fabriqués (dont la constitution est un produit).')
    c.h3('Marchandises, matières premières, approvisionnements (comptes 31, 32, 37 / 603)')
    c.ecr(E_('31/12/N', [('D', '6037', 'Variation des stocks de marchandises', 31000), ('C', '37', 'Stocks de marchandises', 31000)], 'Annulation du stock initial'),
          E_('31/12/N', [('D', '37', 'Stocks de marchandises', 38000), ('C', '6037', 'Variation des stocks de marchandises', 38000)], 'Constatation du stock final'))
    c.p('Le solde du <b>603</b> représente <b>SI − SF</b> : débiteur = diminution du stock (charge supplémentaire), créditeur = augmentation (vient en déduction des charges).')
    c.df('Variation de stock (achats)', 'SI − SF, inscrite en charges (603) : positive si le stock a diminué, négative si le stock a augmenté.')
    c.f('Achats consommés = Achats + (SI − SF)')
    c.h3('Produits fabriqués (compte 35 / 713)')
    c.ecr(E_('31/12/N', [('D', '7135', 'Variation des stocks de produits', 67500), ('C', '355', 'Stocks de produits finis', 67500)], 'Annulation du stock initial'),
          E_('31/12/N', [('D', '355', 'Stocks de produits finis', 83000), ('C', '7135', 'Variation des stocks de produits', 83000)], 'Constatation du stock final'))
    c.df('Production stockée', 'SF − SI des produits fabriqués, inscrite en produits (713) : positive si le stock a augmenté (produit), négative en cas de déstockage.')
    c.f('Production de l\'exercice = production vendue (70) + production stockée (713 = SF − SI) + production immobilisée (72)')
    c.warn('Sens opposés : pour les achats, la variation est <b>SI − SF</b> (charge) ; pour les produits, <b>SF − SI</b> (produit). Une hausse de stock diminue les charges (achats) ou augmente les produits (production).')

    c.sec('II. La régularisation des charges et des produits')
    c.p('Principe de <b>séparation des exercices</b> : seuls les produits acquis pendant l\'exercice et les charges engagées pour les obtenir sont rattachés à l\'exercice, indépendamment des encaissements et paiements. Or les opérations sont enregistrées à la date des pièces (factures) : il peut y avoir un <b>décalage</b> entre enregistrement et rattachement. On le neutralise par des ajustements.')
    c.h3('Charges à payer')
    c.df('Charge à payer', 'Charge imputable à l\'exercice dont la pièce (facture) ne sera enregistrée qu\'à l\'exercice suivant ; on l\'enregistre à l\'inventaire avec une dette dont le numéro porte un 8 en troisième position.')
    c.ul(['Débit du compte de charge pour son montant <b>HT</b> ;', 'crédit d\'un compte de dette pour le montant <b>TTC</b> ;', 'équilibre par le débit du <b>4458 État, TVA à régulariser</b> (44586 pour les factures non parvenues).'])
    c.tab(['Charge', 'Compte de dette'], [['60 Achats · 61/62 Services extérieurs', '4081 Fournisseurs, factures non parvenues'], ['63 Impôts', '4486 État, charges à payer'], ['64 Personnel', '428 Personnel, charges à payer · 4386 Organismes sociaux, charges à payer'],
                                          ['65 Autres charges de gestion courante', '4686 Divers, charges à payer'], ['66 Charges financières', '1688 Intérêts courus sur emprunts · 5186 Banques, intérêts courus à payer']])
    c.note('Le poly de diapos indique « 4486 » sur la ligne 65 : le compte « Divers, charges à payer » du plan comptable est le <b>4686</b>.')
    c.ecr(E_('31/12/N', [('D', '601', 'Achats de matières premières', 14000), ('D', '44586', 'TVA sur factures non parvenues', 2800), ('C', '4081', 'Fournisseurs, factures non parvenues', 16800)], 'Livraison du 20/12 sans facture'))
    c.h3('Produits à recevoir')
    c.df('Produit à recevoir', 'Produit acquis à l\'exercice dont la pièce sera établie à l\'exercice suivant ; symétrique de la charge à payer (créance en débit TTC, produit en crédit HT, TVA au crédit du 4458/44587).')
    c.tab(['Créance (débit TTC)', 'Produit (crédit HT)'], [['4181 Clients, factures à établir', '70 Ventes'], ['4687 Débiteurs divers, produits à recevoir', '75 Autres produits de gestion courante'], ['2768 / 508 Intérêts courus', '76 Produits financiers'], ['709 RRR accordés (débit)', '4198 Clients, RRR à accorder (crédit)']])
    c.p('Toutes ces écritures sont <b>contrepassées au 1er janvier</b> de l\'exercice suivant : on peut alors enregistrer normalement la facture quand elle arrive.')
    c.h3('Charges et produits constatés d\'avance')
    c.p('Cas inverse : la pièce est enregistrée <b>avant</b> que le bien soit livré ou le service rendu.')
    c.df('Charge constatée d\'avance (CCA)', 'Fraction d\'une charge enregistrée dans l\'exercice mais qui concerne l\'exercice suivant : on crédite le compte de charge et on débite le 486 pour le montant HT.')
    c.df('Produit constaté d\'avance (PCA)', 'Fraction d\'un produit enregistré dans l\'exercice mais qui concerne l\'exercice suivant : on débite le compte de produit et on crédite le 487 pour le montant HT.')
    c.ecr(E_('31/12/N', [('D', '486', 'Charges constatées d\'avance', 1500), ('C', '613', 'Locations', 1500)], 'Loyer trimestriel de 4 500 € payé le 1/11 : 1 mois concerne N+1'),
          E_('31/12/N', [('D', '752', 'Revenus des immeubles', 1200), ('C', '487', 'Produits constatés d\'avance', 1200)], 'Loyer de 1 800 € HT reçu le 1/12 pour 3 mois : 2 mois concernent N+1'))
    c.f('CCA (ou PCA) = Montant HT × durée concernant N+1 / durée totale')
    c.p('Ces écritures sont également contrepassées à l\'ouverture de l\'exercice suivant.')
    c.tab(['Décalage', 'Pièce', 'Écriture d\'inventaire', 'Au bilan'], [
        ['Charge à payer', 'Pas encore reçue', 'D 6… (HT) + 44586 / C 408, 428, 438, 448, 468…', 'Dette'],
        ['Produit à recevoir', 'Pas encore émise', 'D 418, 468… / C 7… (HT) + 44587', 'Créance'],
        ['Charge constatée d\'avance', 'Déjà enregistrée', 'D 486 / C 6…', 'Actif (régularisation)'],
        ['Produit constaté d\'avance', 'Déjà enregistrée', 'D 7… / C 487', 'Passif (régularisation)']])
    return c


def ch4():
    c = Cours()
    c.sec('I. Bilan et compte de résultat : deux tableaux complémentaires')
    c.p('Le bilan et le compte de résultat sont les éléments centraux de la comptabilité : ils permettent d\'évaluer le <b>patrimoine</b>, la <b>performance</b> et la <b>situation</b> de l\'entreprise. Ils sont élaborés lors de l\'inventaire, à partir de la <b>balance</b> après inventaire.')
    c.df('Bilan', 'Photographie de la situation patrimoniale de l\'entreprise à la clôture : actif (emplois, comptes 2, 3, 4, 5) et passif (ressources, comptes 1 et 4) ; ses comptes s\'accumulent d\'un exercice à l\'autre.')
    c.df('Compte de résultat', 'Film de l\'exercice : il retrace les charges et les produits (exploitation, financiers, exceptionnels) qui déterminent le résultat ; ses comptes sont remis à zéro à chaque fin d\'exercice.')
    c.df('Annexe', 'Document qui complète le bilan et le compte de résultat par des tableaux explicatifs (immobilisations, amortissements, provisions…) et des informations sur les méthodes.')
    c.df('Résultat', 'Produits − charges ; seul élément commun aux deux tableaux : il apparaît au passif du bilan (capitaux propres) et comme solde du compte de résultat.')
    c.h3('Structure schématique')
    c.tab(['Compte de résultat — Charges', 'Compte de résultat — Produits'], [
        ['Charges d\'exploitation', 'Produits d\'exploitation'], ['Charges financières', 'Produits financiers'], ['Charges exceptionnelles', 'Produits exceptionnels'], ['Impôt sur les bénéfices', ''], ['Résultat net (bénéfice)', '']])
    c.tab(['Bilan — Actif (emplois)', 'Bilan — Passif (ressources)'], [
        ['<b>Actif immobilisé</b> : immobilisations incorporelles, corporelles, financières', '<b>Capitaux propres</b> : capital, réserves, résultat ±'],
        ['<b>Actif circulant</b> : stocks et en-cours, créances, VMP, disponibilités', '<b>Dettes</b> : financières, d\'exploitation, diverses'],
        ['Total général', 'Total général']])

    c.sec('II. Numéros de comptes et postes du bilan')
    c.tab(['Poste de l\'actif', 'Valeur brute', 'Amort. et dépréciations'], [
        ['Fonds commercial', '206 – 207', '2906 – 2907'], ['Autres immobilisations incorporelles', '201 – 203 – 205 – 208', '280 – 2905 – 2908'],
        ['Immobilisations corporelles', '21 – 22 – 23', '281 – 291'], ['Immobilisations financières', '26 – 27', '296 – 297'],
        ['Stocks (autres que marchandises)', '31 à 35', '391 à 395'], ['Stocks de marchandises', '37', '397'], ['Avances et acomptes versés', '4091', ''],
        ['Clients et comptes rattachés', '41', '491'], ['Autres créances', '40 (sauf 4091), 42, 43, 44, 45, 46', '496'], ['VMP', '50', '590'],
        ['Disponibilités', '51 – 54 – 58 · caisse 53', ''], ['Charges constatées d\'avance', '486', '']])
    c.tab(['Poste du passif', 'Comptes'], [
        ['Capital', '101 – 108'], ['Écarts de réévaluation', '105'], ['Réserve légale · réglementées · autres', '1061 · 1064 · 1063 – 1068'],
        ['Report à nouveau', '110 – 119 (en négatif si débiteur)'], ['Résultat de l\'exercice', 'Report du compte de résultat (en négatif si perte)'],
        ['Provisions réglementées', '14'], ['Provisions (risques et charges)', '15'], ['Emprunts et dettes assimilées', '16 et 51 créditeurs'],
        ['Avances et acomptes reçus', '4191'], ['Fournisseurs et comptes rattachés', '40'], ['Autres dettes', '41 – 42 – 43 – 44 – 45 – 46'], ['Produits constatés d\'avance', '487']])
    c.sec('III. Numéros de comptes et compte de résultat')
    c.tab(['Charges', 'Comptes'], [
        ['Achats de marchandises', '607 – 6097'], ['Variation de stocks de marchandises', '6037'], ['Achats d\'approvisionnements', '601 – 602 – 604 – 605 – 606'], ['Variation de stocks (approvisionnements)', '6031 – 6032'],
        ['Autres charges externes', '61 – 62'], ['Impôts, taxes et assimilés', '63'], ['Rémunération du personnel', '641 – 644'], ['Charges sociales', '645 – 646'],
        ['Dotations aux amortissements', '6811'], ['Dotations aux provisions et dépréciations', '6815 – 6817'], ['Autres charges', '65'],
        ['Charges financières', '66 – 686'], ['Charges exceptionnelles', '67 – 687'], ['Impôt sur les bénéfices', '695 – 697']])
    c.tab(['Produits', 'Comptes'], [
        ['Ventes de marchandises', '707 – 7097'], ['Production vendue', '701 – 706 – 708 – 7091 – 7096 – 7098'], ['Production stockée', '713'], ['Production immobilisée', '72'],
        ['Subventions d\'exploitation', '74'], ['Autres produits', '75 – 781 – 791'], ['Produits financiers', '76 – 786 – 796'], ['Produits exceptionnels', '77 – 787 – 797']])
    c.note('Les rabais, remises et ristournes (609 obtenus, 709 accordés) se retranchent des achats ou des ventes correspondants : ils ne sont pas des produits ou des charges autonomes.')
    c.sec('IV. Liens entre les deux tableaux et avec les autres disciplines')
    c.ul(['Le <b>résultat</b> du compte de résultat est reporté dans les <b>capitaux propres</b> : à l\'équilibre, Actif = Passif.',
          'Chaque écriture d\'inventaire touche en général <b>les deux</b> tableaux : une dotation diminue le résultat (compte de résultat) et diminue l\'actif net ou augmente les provisions (bilan).',
          'Exception : les écritures purement bilancielles (transfert 411 → 416, écarts de conversion) ne touchent pas le résultat.'])
    c.df('Analyse financière', 'Utilisation du bilan, du compte de résultat et de l\'annexe pour évaluer la liquidité, la solvabilité et la performance de l\'entreprise.')
    c.df('Comptabilité analytique', 'Utilisation des flux internes (mouvements de stocks, coûts, ventes) identifiés par la comptabilité générale pour calculer des coûts et des marges.')
    c.f('Actif = Capitaux propres + Provisions + Dettes (+ régularisations)<br>Résultat = Produits − Charges = variation des capitaux propres hors apports et distributions')
    return c
