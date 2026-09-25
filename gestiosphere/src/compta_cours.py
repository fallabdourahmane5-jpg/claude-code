"""Comptabilité des sociétés — cours rédigés pour être compris (style Écosphère),
d'après le poly de diapos : intro et amortissements, provisions pour dépréciation,
autres provisions, régularisations, documents de synthèse."""
from lib import Cours, E_, journal

SRC_INTRO = 'Compta des sociétés — intro et amortissement (diapos 1-8)'
SRC_AMORT = 'Compta des sociétés — intro et amortissement (diapos 9-24)'
SRC_DEP = 'Provisions pour dépréciations (8 diapos)'
SRC_AUTRES = 'Autres provisions (9 diapos)'
SRC_REGUL = 'Régularisations (10 diapos)'
SRC_SYNTH = 'Documents de synthèse (7 diapos)'
SRC_TD = 'Poly de TD L2 — Comptabilité des sociétés'


def ch0():
    c = Cours()
    c.intro('De quoi parle ce cours ?',
            'Pendant l\'année, la comptabilité enregistre les opérations au fil de l\'eau : achats, ventes, paiements. Mais à la fin de l\'exercice, ces enregistrements ne suffisent pas à donner une image exacte de l\'entreprise. Des machines ont perdu de la valeur, des clients ne paieront peut-être pas, des factures concernent l\'année suivante… La <b>comptabilité des sociétés</b> étudiée ici est celle de la <b>clôture</b> : tout ce qu\'il faut faire pour passer des enregistrements de l\'année à des comptes annuels justes.',
            ['Pourquoi faut-il des écritures spéciales en fin d\'année ?', 'Sur quels principes s\'appuient ces écritures ?', 'Comment le plan de comptes est-il organisé ?'])

    c.sec('I. L\'inventaire comptable : pourquoi et comment ?')
    c.idee('Une entreprise doit faire le point <b>au moins une fois par an</b>. Ce point, ce sont les <b>comptes annuels</b> : le bilan, le compte de résultat et l\'annexe. On les prépare grâce aux <b>travaux d\'inventaire</b>.')
    c.df('Travaux d\'inventaire', 'Travaux qui ont pour but de déterminer le résultat et la valeur des actifs et des passifs à la clôture de l\'exercice comptable. On distingue l\'inventaire extra-comptable et les écritures d\'inventaire.')
    c.p('Ces travaux se font en deux temps.')
    c.df('Inventaire extra-comptable', 'Recensement et évaluation des éléments existants à la clôture : stocks, créances et dettes, immobilisations.')
    c.autrement('on sort de la comptabilité pour aller <b>constater la réalité</b> : on compte les stocks, on vérifie quels clients risquent de ne pas payer, on examine l\'état des machines.')
    c.df('Écritures d\'inventaire', 'Écritures passées à la clôture pour reporter en comptabilité les conséquences des évaluations extra-comptables et pour rattacher les charges et les produits au bon exercice.')
    c.autrement('une fois la réalité constatée, on <b>corrige la comptabilité</b> pour qu\'elle y corresponde.')
    c.p('Les écritures d\'inventaire sont de trois familles, qui correspondent aux chapitres du cours :')
    c.ul(['la comptabilisation des <b>variations de stocks</b> (chapitre 3) ;',
          'l\'enregistrement des <b>amortissements</b> (chapitre 1), des <b>dépréciations</b> et des <b>provisions</b> (chapitre 2) ;',
          'l\'<b>ajustement des charges et des produits</b> : charges à payer, produits à recevoir, charges et produits constatés d\'avance (chapitre 3).'])
    c.df('Balance avant inventaire', 'Récapitulatif de la situation des comptes telle qu\'elle résulte de l\'enregistrement des opérations courantes de l\'exercice : c\'est le point de départ de l\'inventaire.')
    c.df('Balance après inventaire', 'Balance obtenue après les écritures d\'inventaire ; elle sert de base à l\'établissement du compte de résultat et du bilan.')
    c.f('Balance avant inventaire → écritures d\'inventaire → balance après inventaire → bilan + compte de résultat + annexe')
    c.retenir(['Inventaire = constater la réalité (extra-comptable) puis corriger les comptes (écritures d\'inventaire).', 'Point de départ : la balance avant inventaire ; point d\'arrivée : la balance après inventaire, puis les comptes annuels.', 'Trois familles d\'écritures : stocks, amortissements/dépréciations/provisions, régularisations des charges et produits.'])
    c.transition('Ces écritures ne sont pas passées au hasard : elles appliquent des <b>principes comptables</b>. Les connaître permet de savoir <i>pourquoi</i> on passe chaque écriture.')

    c.sec('II. Les principes comptables à maîtriser')
    c.idee('Les principes sont les « règles du jeu » de la comptabilité. Presque chaque écriture d\'inventaire en applique un : si tu sais lequel, tu comprends l\'écriture au lieu de l\'apprendre par cœur.')
    c.df('Principe de l\'entité', 'L\'entreprise est une entité distincte de ses propriétaires : seules ses propres opérations sont enregistrées.')
    c.df('Séparation (indépendance) des exercices', 'Seuls les produits acquis pendant l\'exercice et les charges engagées pour les obtenir sont rattachés à cet exercice, indépendamment des dates d\'encaissement et de paiement.')
    c.autrement('ce qui compte, c\'est l\'année où la charge ou le produit « se produit », pas l\'année où l\'argent circule. Un loyer de janvier payé en décembre appartient à janvier.')
    c.df('Coût historique', 'Les biens sont enregistrés à leur valeur d\'entrée (coût d\'acquisition ou de production) ; les plus-values latentes ne sont pas constatées.')
    c.df('Prudence', 'On ne comptabilise pas les gains probables mais on constate les pertes probables : les moins-values latentes sont provisionnées, les plus-values latentes ignorées.')
    c.pourquoi('Pourquoi traiter différemment les gains et les pertes probables ?', 'Pour ne pas présenter une entreprise plus riche qu\'elle ne l\'est. Un gain probable peut ne jamais arriver : si on l\'enregistrait, on risquerait de distribuer un bénéfice qui n\'existe pas. Une perte probable, elle, doit être anticipée pour protéger les créanciers.')
    c.df('Continuité de l\'exploitation', 'Les comptes sont établis en supposant que l\'entreprise poursuivra son activité ; c\'est ce qui justifie l\'évaluation au coût historique et la répartition des coûts par l\'amortissement.')
    c.df('Permanence des méthodes', 'Les méthodes d\'évaluation et de présentation sont conservées d\'un exercice à l\'autre pour que les comptes restent comparables.')
    c.df('Régularité et sincérité', 'Les comptes respectent les règles en vigueur (régularité) et les appliquent de bonne foi, en traduisant la connaissance que les dirigeants ont de la réalité (sincérité).')
    c.df('Image fidèle', 'Objectif final des comptes annuels : donner une représentation exacte du patrimoine, de la situation financière et du résultat de l\'entreprise.')
    c.tab(['Principe', 'Écritures qu\'il justifie'], [['Prudence', 'Dépréciations des titres, des créances, des stocks ; interdiction de compenser plus et moins-values (ch. 2)'], ['Séparation des exercices', 'Charges à payer, produits à recevoir, CCA/PCA (ch. 3) ; provisions pour risques et charges (ch. 2)'],
                                                          ['Coût historique + continuité', 'Amortissement : on répartit le coût d\'entrée sur la durée d\'utilisation (ch. 1)'], ['Image fidèle', 'Objectif de toutes les écritures d\'inventaire (ch. 4)']])
    c.retenir(['Prudence : pertes probables constatées, gains probables ignorés.', 'Séparation des exercices : rattacher à l\'année qui est concernée, pas à celle du paiement.', 'Image fidèle : c\'est le but final.'])
    c.transition('Avant de passer aux écritures, il faut être à l\'aise avec le vocabulaire de base : actif, passif, débit, crédit et plan de comptes.')

    c.sec('III. Rappels : actif, passif, débit, crédit')
    c.df('Actif du bilan', 'Emplois de l\'entreprise : biens utilisés (immobilisations, stocks), créances et liquidités.')
    c.df('Passif du bilan', 'Ressources de l\'entreprise, c\'est-à-dire ses sources de financement : capitaux propres, provisions, dettes.')
    c.autrement('l\'actif dit <b>ce que l\'entreprise possède</b>, le passif dit <b>d\'où vient l\'argent</b> qui a permis de le financer. Les deux totaux sont donc toujours égaux.')
    c.df('Partie double', 'Principe d\'enregistrement selon lequel tout débit s\'accompagne d\'un crédit de même montant, et réciproquement.')
    c.p('Le <b>débit</b> est la colonne de gauche d\'un compte, le <b>crédit</b> la colonne de droite. Exemple : une vente à crédit débite le compte 411 Clients (le client nous doit de l\'argent) ; quand il paie, on crédite le 411 (sa dette disparaît).')
    c.h3('L\'organisation du plan de comptes')
    c.tab(['Classe', 'Contenu', 'Document'], [
        ['1', 'Capitaux (capital, réserves, résultat, provisions réglementées 14, provisions pour risques 15, emprunts)', 'Bilan'],
        ['2', 'Immobilisations (et leurs amortissements 28, dépréciations 29)', 'Bilan'], ['3', 'Stocks et en-cours (et leurs dépréciations 39)', 'Bilan'],
        ['4', 'Tiers (clients, fournisseurs, État, personnel, régularisations 48)', 'Bilan'], ['5', 'Financiers (VMP, banque, caisse)', 'Bilan'],
        ['6', 'Charges', 'Compte de résultat'], ['7', 'Produits', 'Compte de résultat']])
    c.note('Astuce de lecture : un <b>8</b> ou un <b>9</b> en deuxième position signale un compte qui <b>diminue</b> un actif. 28 = amortissements des immobilisations (2) ; 39 = dépréciations des stocks (3) ; 49 = dépréciations des tiers (4) ; 59 = dépréciations des VMP (5).')
    c.warn('Examen : le poly des diapos est autorisé. Viens avec ton <b>plan de comptes</b> et ta <b>calculatrice</b>. Évaluation : un DS et un examen final.')
    c.df('Journal', 'Livre où les opérations sont enregistrées chronologiquement, en partie double.')
    c.df('Comptes annuels', 'Ensemble formé du bilan, du compte de résultat et de l\'annexe, préparés par les travaux d\'inventaire.')
    c.retenir(['Actif = emplois ; passif = ressources ; total actif = total passif.', 'Classes 1 à 5 : bilan ; classes 6 et 7 : compte de résultat.', '28, 29, 39, 49, 59 : comptes qui viennent diminuer un actif.'])
    c.synthese(['La clôture sert à passer des enregistrements de l\'année à une <b>image fidèle</b> de l\'entreprise.', 'Deux temps : constater la réalité (inventaire extra-comptable), puis corriger les comptes (écritures d\'inventaire).',
                'Chaque écriture applique un principe : surtout la <b>prudence</b> et la <b>séparation des exercices</b>.', 'Le reste du cours détaille les écritures : amortissements (ch. 1), provisions (ch. 2), régularisations (ch. 3), puis la présentation des comptes (ch. 4).'])
    return c


def ch1():
    c = Cours()
    c.intro('De quoi parle ce chapitre ?',
            'Quand une entreprise achète une machine 98 000 €, elle ne s\'appauvrit pas de 98 000 € d\'un coup : elle échange de l\'argent contre un bien qu\'elle va utiliser plusieurs années. Mais ce bien va s\'user. L\'<b>amortissement</b> sert à faire « payer » chaque année la part de la machine qui a été consommée.',
            ['Pourquoi et quoi amortir ?', 'Comment calculer un amortissement linéaire, puis dégressif ?', 'Que faire de l\'écart entre les deux (amortissement dérogatoire) ?', 'Comment enregistrer la vente d\'une immobilisation ?'])

    c.sec('I. Définition et justification de l\'amortissement')
    c.idee('Une immobilisation perd de la valeur avec le temps. Cette perte est une <b>charge</b> pour l\'entreprise, même si elle ne sort pas d\'argent de la banque.')
    c.p('Les immobilisations dont la durée d\'utilisation est limitée sont <b>amortissables</b>. Trois raisons à cette perte de valeur :')
    c.ul(['l\'<b>usure physique</b> (une machine s\'use) ;', 'l\'<b>obsolescence technique</b> (un ordinateur devient dépassé, même s\'il fonctionne) ;', 'des raisons <b>juridiques et fiscales</b> (un brevet expire).'])
    c.df('Amortissement', 'Répartition systématique du montant amortissable d\'une immobilisation sur les exercices pendant lesquels elle est utilisée ; c\'est une charge calculée et non décaissée.')
    c.df('Charge calculée', 'Charge qui ne donne lieu à aucun décaissement (amortissements, dépréciations, provisions) : elle diminue le résultat sans diminuer la trésorerie.')
    c.autrement('l\'amortissement est une <b>charge sur le papier</b>. Il réduit le bénéfice (et donc l\'impôt) sans faire sortir un euro de la trésorerie.')
    c.df('Montant amortissable', 'Valeur d\'entrée (brute) de l\'immobilisation diminuée de sa valeur résiduelle en fin d\'utilisation, le plus souvent nulle.')
    c.pourquoi('Pourquoi répartir le coût au lieu de le passer entièrement en charge l\'année de l\'achat ?', 'Parce que la machine va produire pendant plusieurs années. Mettre tout son coût sur la première année ferait apparaître une grosse perte cette année-là, puis de gros bénéfices ensuite : ce serait faux. L\'amortissement rapproche chaque année le coût de la machine des profits qu\'elle permet de réaliser (principe de séparation des exercices).')
    c.df('Valeur nette comptable (VNC)', 'Montant inscrit à l\'actif : valeur d\'entrée diminuée du cumul des amortissements (et des éventuelles dépréciations).')
    c.f('VNC = Valeur brute − Cumul des amortissements (− dépréciations)')
    c.h3('Quelles immobilisations sont amortissables ?')
    c.tab(['Compte', 'Nature', 'Amortissable ?'], [
        ['201', 'Frais d\'établissement', 'Oui'], ['203', 'Frais de recherche et développement', 'Oui'], ['205', 'Concessions, brevets, licences', 'Oui'], ['206', 'Droit au bail', 'Non'], ['207', 'Fonds commercial', 'Non'],
        ['211', 'Terrains', 'Non'], ['212', 'Aménagements des terrains', 'Oui'], ['213', 'Constructions', 'Oui'], ['215', 'Installations techniques, matériels et outillages', 'Oui'], ['218', 'Autres immobilisations corporelles', 'Oui'],
        ['23', 'Immobilisations en cours', 'Non'], ['26/27', 'Immobilisations financières', 'Non']])
    c.pourquoi('Pourquoi un terrain ne s\'amortit-il pas ?', 'Parce qu\'il ne s\'use pas et que sa durée d\'utilisation n\'est pas limitée. De même, des titres ne s\'usent pas : s\'ils perdent de la valeur, on les <b>déprécie</b> (chapitre 2), on ne les amortit pas.')
    c.h3('Durées d\'usage préconisées par l\'administration fiscale')
    c.tab(['Bien', 'Durée'], [['Bâtiments administratifs et commerciaux', '25 ans'], ['Bâtiments industriels', '20 ans'], ['Matériel industriel', '10 ans'], ['Mobilier de bureau', '10 ans'], ['Voitures particulières', '5 ans'], ['Poids lourds', '4 ans'], ['Brevets, concessions', 'durée d\'exclusivité conférée']])
    c.retenir(['Amortissement = charge calculée, non décaissée, qui constate l\'usure.', 'On amortit ce qui s\'use (constructions, matériels, brevets) ; pas les terrains, le fonds commercial ni les titres.', 'VNC = brut − amortissements cumulés.'])
    c.transition('Reste à savoir <b>combien</b> amortir chaque année. La méthode de base est l\'amortissement linéaire.')

    c.sec('II. L\'amortissement linéaire')
    c.idee('On étale le coût de la machine <b>en parts égales</b> sur sa durée d\'utilisation. La première année, on ne compte que la période réellement utilisée.')
    c.p('Les normes imposent d\'établir un <b>plan d\'amortissement</b> dès la mise en service. En principe, l\'amortissement doit suivre la façon dont le bien procure ses avantages ; en pratique, on applique le <b>linéaire</b> par défaut.')
    c.df('Amortissement linéaire', 'Mode d\'amortissement à annuités constantes, calculées au prorata temporis à partir de la date de mise en service du bien.')
    c.df('Prorata temporis', 'Réduction de la première annuité au prorata du temps écoulé entre la mise en service et la fin de l\'exercice (et de la dernière annuité pour compléter le plan).')
    c.f('Taux linéaire = 100 % / durée · Annuité = Valeur d\'entrée × taux · 1ʳᵉ annuité = Annuité × jours depuis la mise en service / 360')
    c.note('Convention des TD : année commerciale de <b>360 jours</b> et mois de 30 jours. On le vérifie sur l\'exercice 2 du poly : une machine mise en service le 20/08/2012 compte 130 jours en 2012, soit 10 jours en août et 4 mois × 30.')
    c.pas('Exemple pas à pas : machine de 98 000 € mise en service le 26/04/N, durée 5 ans', [
        'Taux : 100 % / 5 = 20 % ; annuité pleine : 98 000 × 20 % = 19 600 €.',
        'Jours utilisés en N : du 26 au 30 avril, 4 jours, puis mai à décembre, 8 × 30 = 240 jours. Total : 244 jours.',
        '1ʳᵉ annuité : 19 600 × 244 / 360 = 13 284,44 €.',
        'De N+1 à N+4 : 19 600 € par an.',
        'N+5 : ce qui reste pour atteindre 98 000 €, soit 19 600 − 13 284,44 = 6 315,56 €.'],
        'Le plan dure donc 6 exercices : la première et la dernière annuité se complètent pour faire une annuité pleine.')
    c.df('Amortissement par composants', 'Lorsque les éléments principaux d\'une immobilisation ont des durées d\'utilisation différentes, chacun est amorti séparément sur sa propre durée.')
    c.h3('Comment l\'enregistrer ?')
    c.p('Deux effets à traduire : une <b>charge</b> (on débite le <b>6811</b> Dotations aux amortissements) et une <b>perte de valeur</b> de l\'immobilisation (on crédite un compte <b>28</b>). Le compte 28 reprend le numéro de l\'immobilisation avec un 8 : 2183 Matériel informatique → <b>28183</b>.')
    c.ecr(E_('31/12/N', [('D', '6811', 'Dotations aux amortissements', 13284.44), ('C', '28154', 'Amortissement du matériel industriel', 13284.44)], 'Annuité N'))
    c.pourquoi('Pourquoi ne crédite-t-on pas directement le compte 2154 Matériel industriel ?', 'Pour garder la trace du prix d\'achat. Au bilan, on montre à la fois ce que la machine a coûté (brut), ce qu\'elle a perdu (amortissements) et ce qu\'elle vaut encore (net). Le lecteur voit ainsi si les équipements sont neufs ou vieillissants.')
    c.tab(['Actif immobilisé', 'Brut', 'Amort. et dépréc.', 'Net'], [['Matériel industriel (fin N)', 98000, 13284.44, 84715.56]], num_cols=(1, 2, 3))
    c.retenir(['Linéaire : annuités égales, 1ʳᵉ annuité au prorata en <b>jours / 360</b> à partir de la <b>mise en service</b>.', 'Écriture : débit 6811, crédit 28…', 'Bilan : brut, amortissements, net.'])
    c.transition('Le fisc autorise une autre méthode, plus rapide au début : l\'amortissement dégressif.')

    c.sec('III. L\'amortissement dégressif')
    c.idee('Le dégressif amortit <b>beaucoup les premières années, puis de moins en moins</b>. C\'est un avantage fiscal : plus de charges au début, donc moins d\'impôt tout de suite.')
    c.p('La charge d\'amortissement est <b>déductible</b> du bénéfice imposable : les durées et les calculs sont donc réglementés par le code des impôts. Il faut distinguer l\'amortissement <b>comptable</b> (linéaire) de celui pratiqué pour des raisons <b>fiscales</b> (dégressif).')
    c.df('Amortissement dégressif', 'Mode d\'amortissement fiscal où l\'annuité est obtenue en appliquant un taux dégressif à la valeur nette comptable du début d\'exercice : les annuités sont fortes au début puis décroissent.')
    c.f('Taux dégressif = taux linéaire × coefficient · Coefficients : 1,25 (3-4 ans) · 1,75 (5-6 ans) · 2,25 (plus de 6 ans) · Annuité = VNC début × taux dégressif')
    c.autrement('au lieu d\'appliquer toujours le même taux au prix d\'achat, on applique un taux plus fort à ce qui <b>reste</b> à amortir. Comme ce reste diminue, l\'annuité diminue aussi.')
    c.p('Deux règles propres au dégressif :')
    c.ul(['La 1ʳᵉ annuité se calcule <b>à partir du premier jour du mois d\'acquisition</b> : prorata en <b>mois</b>, pas en jours.',
          'Sans correction, l\'annuité ne tomberait jamais à zéro. Donc, <b>dès que le taux linéaire sur la durée restante dépasse le taux dégressif</b>, on bascule : on partage la VNC restante en parts égales.'])
    c.pas('Exemple du cours pas à pas : machine de 28 000 € achetée le 2 janvier, 5 ans', [
        'Coefficient 1,75 (5 ans) : taux dégressif = 20 % × 1,75 = 35 %.',
        'Année 1 : 28 000 × 35 % = 9 800 € (janvier, donc année pleine). VNC 18 200 €.',
        'Année 2 : 18 200 × 35 % = 6 370 €. VNC 11 830 €.',
        'Année 3 : 11 830 × 35 % = 4 140,50 €. VNC 7 689,50 €.',
        'Année 4 : il reste 2 ans, le taux linéaire restant vaut 1/2 = 50 %, plus que 35 %. On bascule au linéaire.',
        'Années 4 et 5 : 7 689,50 / 2 = 3 844,75 € chacune.'],
        'Autre exemple : machine-outil sur 10 ans, taux linéaire 10 % × 2,25 = 22,5 %.')
    c.h3('Comment l\'enregistrer ? L\'amortissement dérogatoire')
    c.p('La comptabilité garde le <b>linéaire</b> comme amortissement « normal ». L\'écart avec le dégressif est isolé dans un compte à part.')
    c.df('Amortissement dérogatoire', 'Différence entre l\'amortissement fiscal (dégressif) et l\'amortissement comptable (linéaire) ; il est enregistré en provision réglementée dans les capitaux propres (compte 145).')
    c.p('<b>Les premières années (dégressif > linéaire)</b> : on dote le linéaire normalement (6811 / 28). L\'excédent est une charge exceptionnelle déductible, <b>6872</b> Dotations aux provisions réglementées (« 687 » dans le cours), portée au crédit du <b>145</b>.')
    c.ecr(E_('31/12/N', [('D', '6811', 'Dotations aux amortissements (linéaire)', 13284.44), ('C', '28154', 'Amortissement du matériel industriel', 13284.44)], 'Part comptable'),
          E_('31/12/N', [('D', '6872', 'Dotations aux provisions réglementées (dérogatoire)', 12440.56), ('C', '145', 'Amortissements dérogatoires', 12440.56)], 'Excédent fiscal : 25 725 (dégressif) − 13 284,44 (linéaire)'))
    c.p('<b>Les dernières années (linéaire > dégressif)</b> : on « rend » le dérogatoire. On débite le <b>145</b> et on crédite <b>7872</b> Reprises sur provisions réglementées (« 787 » dans le cours), un produit exceptionnel.')
    c.ecr(E_('31/12/N+2', [('D', '145', 'Amortissements dérogatoires', 3157.44), ('C', '7872', 'Reprises sur provisions réglementées', 3157.44)], 'Linéaire 19 600 − dégressif 16 442,56'))
    c.pourquoi('Pourquoi ne pas simplement passer le dégressif en 6811 ?', 'Parce que le dégressif est un calcul <b>fiscal</b>, qui ne décrit pas l\'usure réelle du bien. En mettant l\'excédent en 145 (capitaux propres), l\'actif continue de montrer l\'usure « comptable » linéaire, tout en profitant de la déduction fiscale.')
    c.df('Intérêt du dégressif', 'Réduire la charge d\'impôt en début d\'utilisation : cela lisse l\'impôt, facilite la gestion de trésorerie et permet de réinvestir rapidement.')
    c.note('Sur toute la durée du plan, les dotations et les reprises de dérogatoire se compensent : l\'impôt n\'est pas supprimé, il est <b>décalé dans le temps</b>. C\'est un gain de trésorerie.')
    c.retenir(['Taux dégressif = taux linéaire × 1,25 / 1,75 / 2,25.', 'Prorata en <b>mois</b> depuis le mois d\'acquisition ; bascule au linéaire en fin de plan.', 'Dérogatoire = dégressif − linéaire : 6872/145 au début, 145/7872 à la fin.', 'Le 145 est en capitaux propres : l\'actif ne change pas.'])
    c.transition('Une immobilisation finit souvent par être vendue avant la fin de son plan. Il faut alors la faire sortir du bilan.')

    c.sec('IV. La cession des immobilisations')
    c.idee('Quand on vend un bien, on compare <b>ce qu\'il rapporte</b> (le prix de vente) et <b>ce qu\'il valait encore</b> dans les comptes (sa VNC). La différence est une plus-value ou une moins-value.')
    c.p('Deux façons de voir la cession. <b>Patrimoniale</b> : le bien sort du patrimoine à sa valeur nette comptable. <b>Par les flux</b> : la sortie du bien est une charge (675), l\'argent reçu est un produit (775).')
    c.df('Plus ou moins-value de cession', 'Différence entre le prix de cession (775) et la valeur comptable de l\'élément cédé (675) : positive = plus-value, négative = moins-value.')
    c.f('Résultat de cession = Prix de cession (775) − VNC à la date de cession (675)')
    c.p('Les étapes, dans cet ordre :')
    c.ul(['<b>Mettre à jour l\'amortissement</b> jusqu\'à la date de cession (6811 / 28). Sinon la VNC serait fausse.', 'Si le bien avait du dérogatoire : le <b>reprendre</b> (145 / 7872).', '<b>Sortir le bien</b> : débit 28 (amortissements cumulés) et 675 (VNC), crédit 21… (valeur brute).', '<b>Constater le prix</b> : débit 512 (ou 462), crédit 775 et 44571 (TVA collectée).'])
    c.ex('Exemple', '<p>Camion acquis 19 000 € HT, amorti en linéaire sur 5 ans, avec un cumul de 1 900 € au jour de la vente. Il est cédé 9 500 € HT (TVA 20 %) :</p>' +
         journal(E_('Date de cession', [('D', '28182', 'Amortissement du matériel de transport', 1900), ('D', '675', 'Valeurs comptables des éléments d\'actif cédés', 17100), ('C', '2182', 'Matériel de transport', 19000)], 'Sortie du bien'),
                 E_('Date de cession', [('D', '512', 'Banque', 11400), ('C', '775', 'Produits des cessions d\'éléments d\'actif', 9500), ('C', '44571', 'TVA collectée', 1900)], 'Prix de cession')) +
         '<p>Moins-value : 9 500 − 17 100 = −7 600 €. Le camion valait encore 17 100 € dans les comptes et n\'a été vendu que 9 500 €.</p>')
    c.retenir(['Toujours commencer par la dotation complémentaire jusqu\'à la date de cession.', 'Résultat = 775 − 675 ; ces deux comptes sont en exceptionnel.'])

    c.sec('V. Récapitulatif et documents de synthèse')
    c.tab(['Opération', 'Débit', 'Crédit'], [['Dotation (linéaire)', '6811', '28…'], ['Dérogatoire : dégressif > linéaire', '6872', '145'], ['Dérogatoire : linéaire > dégressif', '145', '7872'], ['Cession : sortie du bien', '28… + 675', '21…'], ['Cession : prix', '512 / 462', '775 + 44571']])
    c.p('<b>Bilan</b> : brut, amortissements cumulés (linéaire) et net à l\'actif ; amortissements dérogatoires en capitaux propres. <b>Compte de résultat</b> : 6811 en exploitation ; 6872/7872 et 675/775 en exceptionnel. <b>Annexe</b> : tableau des immobilisations et tableau des amortissements (début, augmentations, diminutions, fin).')
    c.synthese(['L\'amortissement traduit l\'usure : c\'est une charge calculée, non décaissée.', 'Linéaire = comptable (jours / 360 depuis la mise en service) ; dégressif = fiscal (mois depuis le mois d\'acquisition, coefficient, bascule finale).',
                'L\'écart entre les deux passe en <b>amortissements dérogatoires</b> (145, capitaux propres).', 'Cession : dotation complémentaire, sortie à la VNC (675), prix (775). La différence donne la plus ou moins-value.'])
    return c


def ch2():
    c = Cours()
    c.intro('De quoi parle ce chapitre ?',
            'À la clôture, certains éléments ont <b>probablement</b> perdu de la valeur : des actions ont baissé en bourse, un client est en difficulté, des articles sont démodés. D\'autres fois, l\'entreprise risque de devoir payer quelque chose : un procès, une garantie, une amende. Le principe de <b>prudence</b> impose d\'anticiper ces pertes : c\'est le rôle des <b>provisions</b>.',
            ['Quelle différence entre dépréciation, provision pour risques et provision réglementée ?', 'Comment déprécier des titres, des créances, des stocks ?', 'Comment traiter une facture en devises non réglée à la clôture ?'])

    c.sec('I. Les provisions et leur évaluation')
    c.idee('Une provision, c\'est une <b>perte ou une charge probable</b> que l\'on enregistre dès aujourd\'hui, sans attendre qu\'elle soit certaine.')
    c.df('Provision (au sens large)', 'Constatation, à la clôture, d\'une perte de valeur probable d\'un actif (dépréciation) ou d\'une charge probable envers un tiers dont le montant n\'est pas fixé précisément (provision pour risques et charges).')
    c.p('Le cours distingue trois catégories, qu\'il ne faut pas confondre :')
    c.tab(['Catégorie', 'Ce qu\'elle constate', 'Compte', 'Place au bilan'], [
        ['Dépréciations (provisions pour dépréciation)', 'Un actif vaut probablement moins que sa valeur comptable', '29, 39, 49, 59', 'En déduction de l\'actif'],
        ['Provisions pour risques et charges', 'L\'entreprise devra probablement payer un tiers, montant incertain', '15', 'Passif, entre capitaux propres et dettes'],
        ['Provisions réglementées', 'Un avantage fiscal (dont les amortissements dérogatoires)', '14', 'Capitaux propres']])
    c.p('<b>Enregistrement</b> : la dotation est une charge calculée (681 exploitation, 686 financière, 687 exceptionnelle). La reprise, quand la provision devient inutile ou trop forte, est un produit (781, 786, 787).')
    c.f('Provision nécessaire − Provision existante > 0 → dotation · < 0 → reprise')
    c.autrement('chaque année, on ne passe que <b>l\'ajustement</b> : on compare ce qu\'il faudrait avoir en provision avec ce qu\'on a déjà, et on complète ou on reprend la différence.')
    c.retenir(['Dépréciation = actif qui perd de la valeur ; provision pour risques = dette probable ; provision réglementée = avantage fiscal.', 'Chaque année : nécessaire − existante → dotation ou reprise.'])
    c.transition('Commençons par les dépréciations d\'actifs : titres, créances, stocks.')

    c.sec('II. Les provisions pour dépréciation')
    c.idee('Un actif (autre qu\'une immobilisation amortie) peut perdre de la valeur <b>sans que ce soit définitif</b>. On le constate par une dépréciation, qui peut être reprise si la situation s\'améliore. Si la perte est définitive, on constate une <b>perte</b>.')
    c.df('Dépréciation', 'Constatation d\'une perte de valeur probable et non irréversible d\'un élément d\'actif ; elle réduit la valeur de l\'actif sans le faire sortir du patrimoine.')
    c.ul(['<b>Titres</b> : titres de participation, titres immobilisés ou VMP dont le cours baisse.', '<b>Stocks</b> : avaries, détériorations, articles passés de mode.', '<b>Créances clients</b> : difficultés temporaires qui rendent le paiement incertain.'])
    c.h3('2.1 Les titres financiers')
    c.df('Titres de participation', 'Titres dont la possession durable est estimée utile à l\'activité de l\'entreprise (influence ou contrôle) ; compte 261.')
    c.df('Valeurs mobilières de placement (VMP)', 'Titres acquis en vue de réaliser un gain à brève échéance ; compte 50 (503 actions, 506 obligations).')
    c.tab(['Nature', 'Valeur d\'entrée', 'Valeur actuelle (à l\'inventaire)'], [['Titres de participation', 'Prix d\'achat', 'Valeur d\'utilité (valeur d\'usage)'], ['TIAP (titres immobilisés de l\'activité de portefeuille)', 'Prix d\'achat', 'Valeur de marché compte tenu des perspectives'], ['Autres titres immobilisés, VMP', 'Prix d\'achat', 'Cotés : cours moyen du dernier mois ; non cotés : valeur probable de réalisation']])
    c.ul(['Si la valeur actuelle est <b>inférieure</b> à la valeur d\'entrée : moins-value probable, donc dépréciation.', 'Les plus-values probables ne sont <b>pas</b> comptabilisées (prudence). On ne peut donc pas <b>compenser</b> la baisse d\'un titre par la hausse d\'un autre.',
          'Pour des titres de même nature achetés à des cours différents, on compare la valeur actuelle à la <b>valeur globale d\'origine</b>.', 'Si la baisse s\'accentue, on complète (dotation) ; si elle se réduit, on reprend.'])
    c.pourquoi('Pourquoi interdire de compenser la baisse d\'un titre par la hausse d\'un autre ?', 'Parce que ce serait comptabiliser un gain latent, contraire à la prudence. Chaque ligne est donc jugée seule : si A baisse de 1 000 € et B monte de 5 000 €, on déprécie quand même A de 1 000 €.')
    c.p('<b>Comptes</b> : dotation <b>6866</b>, reprise <b>7866</b>. La diminution de l\'actif se fait avec un <b>9 en deuxième position</b> : <b>2961</b> (participations), <b>2971/2972</b> (titres immobilisés), <b>590</b> (VMP).')
    c.pas('Exemple pas à pas (TD 4, actions C)', ['150 actions achetées 289 € ; cours moyen de fin d\'année : 285 €.', 'Moins-value probable par action : 289 − 285 = 4 €.', 'Dépréciation nécessaire : 4 × 150 = 600 € ; existante : 0.', 'Dotation de 600 € : débit 6866, crédit 2971.'])
    c.ecr(E_('31/12/N', [('D', '6866', 'Dotations aux dépréciations des éléments financiers', 600), ('C', '2971', 'Dépréciation des titres immobilisés', 600)], '150 actions C : (289 − 285) × 150'),
          E_('31/12/N', [('D', '590', 'Dépréciation des VMP', 900), ('C', '7866', 'Reprises sur dépréciations des éléments financiers', 900)], 'Dépréciation des actions D ramenée de 2 700 à 1 800'))
    c.h3('2.2 Les créances clients')
    c.idee('Un client en difficulté ne paiera peut-être pas. On isole sa créance et on déprécie la part qu\'on risque de perdre, <b>hors TVA</b>.')
    c.df('Créance douteuse', 'Créance dont le recouvrement est incertain parce que le client est en difficulté ; elle est transférée au compte 416 Clients douteux ou litigieux.')
    c.df('Créance irrécouvrable', 'Créance définitivement perdue (perte certaine) : on enregistre une perte au 654 (ou 6714) et on régularise la TVA collectée.')
    c.ul(['Perte <b>probable</b> : dépréciation. Perte <b>certaine</b> : créance irrécouvrable.', 'On refait l\'inventaire des créances douteuses à chaque clôture.', 'La créance est transférée <b>TTC</b> du 411 au 416, mais la dépréciation se calcule sur le <b>HT</b>.'])
    c.pourquoi('Pourquoi déprécier seulement le HT ?', 'Parce que la TVA collectée n\'est pas une perte pour l\'entreprise : si le client ne paie jamais, l\'État lui rembourse cette TVA. Seul le hors taxe est réellement perdu.')
    c.f('Dépréciation nécessaire = Créance TTC / 1,20 × % de perte probable')
    c.pas('Exemple pas à pas (TD 6, BUTUIN)', ['Créance de 8 372 € TTC ; on pense récupérer 70 %, donc la perte probable est de 30 %.', 'HT : 8 372 / 1,2 = 6 976,67 €.', 'Dépréciation : 6 976,67 × 30 % = 2 093 €.', 'Écritures : transfert 411 → 416 (TTC), puis dotation 6817 / 491.'])
    c.ecr(E_('31/12/N', [('D', '416', 'Clients douteux ou litigieux', 8372), ('C', '411', 'Clients', 8372)], 'Transfert de la créance douteuse (TTC)'),
          E_('31/12/N', [('D', '6817', 'Dotations aux dépréciations des actifs circulants', 2093), ('C', '491', 'Dépréciation des comptes clients', 2093)], '8 372 / 1,2 × 30 %'),
          E_('Créance irrécouvrable', [('D', '654', 'Pertes sur créances irrécouvrables', 6179.33), ('D', '44571', 'TVA collectée', 1235.87), ('C', '416', 'Clients douteux', 7415.20)], 'Perte HT + récupération de la TVA'),
          E_('Créance irrécouvrable', [('D', '491', 'Dépréciation des comptes clients', 2000), ('C', '7817', 'Reprises sur dépréciations des actifs circulants', 2000)], 'L\'ancienne dépréciation devient sans objet'))
    c.h3('2.3 Les stocks')
    c.p('On compare le <b>coût d\'acquisition (ou de production)</b> et la <b>valeur actuelle</b>, c\'est-à-dire le prix de vente net des coûts de distribution. Dotation : débit <b>6817</b>, crédit du compte de stock avec un <b>9 en deuxième position</b> (<b>391</b> matières, <b>395</b> produits, <b>397</b> marchandises). Reprise : <b>7817</b>.')
    c.retenir(['Titres : ligne par ligne, sans compensation, 6866/7866 ; comptes 2961, 2971, 590.', 'Créances : 411 → 416 en TTC ; dépréciation sur le HT (6817/491) ; perte certaine : 654 + 44571.', 'Stocks : coût vs prix de vente net ; 6817/39…'])
    c.transition('Les dépréciations concernent des actifs. Mais l\'entreprise peut aussi devoir <b>payer</b> quelque chose à un tiers : ce sont les provisions pour risques et charges.')

    c.sec('III. Les provisions pour risques et charges')
    c.idee('À la clôture, l\'entreprise sait qu\'elle devra <b>probablement</b> payer (procès, garanties, amende) sans connaître le montant exact. Elle enregistre dès maintenant une charge et une « dette estimée » : la provision.')
    c.df('Provision pour risques et charges', 'Passif constaté quand, à la clôture, une obligation envers un tiers est probable (risque) ou certaine (charge) mais que son montant n\'est pas fixé de façon précise ; compte 15.')
    c.ul(['Exemples : litige avec un client, un fournisseur ou un salarié ; garanties données aux clients ; amendes ; pertes de change.', 'Au bilan : <b>entre les capitaux propres et les dettes</b> (classe 15).', 'Elles rattachent à l\'exercice les charges nées pendant l\'exercice (<b>séparation des exercices</b>).', 'Elles sont <b>obligatoires</b>, mais uniquement s\'il existe une <b>obligation envers un tiers</b>.'])
    c.tab(['Nature de la charge', 'Dotation', 'Reprise'], [['Activité normale : litige client, fournisseur, salarié ; garanties', '6815 (681)', '7815 (781)'], ['Financière : perte de change', '6865 (686)', '7865 (786)'], ['Exceptionnelle : amende fiscale', '6875 (687)', '7875 (787)']])
    c.p('Comptes utiles : 1511 litiges · 1512 garanties données aux clients · 1514 amendes et pénalités · 1515 pertes de change.')
    c.pas('Exemple pas à pas (TD 7, garanties)', ['6 000 produits vendus ; 5 % tomberont en panne pendant la garantie d\'un an.', 'Nombre de réparations attendues : 6 000 × 5 % = 300.', 'Coût : 300 × 30 € = 9 000 €.', 'Dotation d\'exploitation : 6815 / 1512.'])
    c.ecr(E_('31/12/N', [('D', '6815', 'Dotations aux provisions d\'exploitation', 9000), ('C', '1512', 'Provisions pour garanties données aux clients', 9000)], '6 000 unités × 5 % × 30 €'))
    c.h3('Les écarts de conversion')
    c.idee('Une facture en devises est enregistrée en euros au cours du jour. Si elle n\'est pas payée à la clôture, le cours a pu bouger : on ajuste sa valeur, et on provisionne la <b>perte</b> éventuelle (mais pas le gain : prudence).')
    c.p('Si le règlement intervient pendant l\'exercice, l\'écart est une vraie perte (666) ou un vrai gain (766). S\'il intervient plus tard, on inscrit la différence dans des comptes d\'attente : les <b>écarts de conversion (476 actif / 477 passif)</b>.')
    c.df('Écart de conversion', 'Compte transitoire (476 actif = perte latente, 477 passif = gain latent) qui enregistre à l\'inventaire la variation de valeur en euros d\'une créance ou d\'une dette en devises non encore réglée.')
    c.tab(['Situation', 'Créance en devises', 'Dette en devises', 'Conséquence'], [['Gain latent', 'Devise appréciée : débit 411 / crédit 477', 'Devise dépréciée : débit 401 / crédit 477', 'Aucun produit (prudence)'], ['Perte latente', 'Devise dépréciée : débit 476 / crédit 411', 'Devise appréciée : débit 476 / crédit 401', 'Provision : débit 6865 / crédit 1515']])
    c.p('Les écarts sont <b>contrepassés au 1er janvier</b> ; la provision pour perte de change est <b>reprise lors du règlement</b>.')
    c.retenir(['Provision pour risques = obligation probable envers un tiers, montant incertain ; au passif (15).', 'Choisir la bonne nature : exploitation, financière ou exceptionnelle.', 'Devises : gain latent → 477 sans produit ; perte latente → 476 + provision 1515.'])
    c.transition('Dernière catégorie, à part : les provisions réglementées, qui ne correspondent à aucune perte réelle.')

    c.sec('IV. Les provisions réglementées')
    c.idee('C\'est un <b>cadeau fiscal</b> : l\'État permet de réduire le bénéfice imposable, à condition que l\'argent économisé reste dans l\'entreprise.')
    c.df('Provision réglementée', 'Provision sans rapport avec une perte de valeur ou un risque, autorisée par le droit fiscal pour réduire le résultat imposable tout en gardant les ressources dans l\'entreprise ; sa contrepartie est inscrite en capitaux propres (compte 14).')
    c.pourquoi('Pourquoi l\'inscrire en capitaux propres et pas en dettes ?', 'Parce qu\'elle ne correspond à aucune dette réelle. La placer dans les capitaux propres garantit que ces ressources ne seront pas distribuées à l\'exploitant : elles restent dans l\'entreprise.')
    c.tab(['Opération', 'Débit', 'Crédit'], [['Dotation', '687 (6872, 6873, 6874)', '14 Provisions réglementées'], ['Reprise', '14 Provisions réglementées', '787 (7872…)']])
    c.ul(['<b>Provision pour hausse des prix</b> : évite de surestimer les stocks quand les prix montent, pour la fraction de hausse dépassant 10 % sur un ou deux ans.', 'Provisions propres à certaines professions.', '<b>Amortissements dérogatoires</b> (145, chapitre 1).'])

    c.sec('V. Les documents de synthèse')
    c.tab(['Provision', 'Bilan', 'Compte de résultat'], [['Dépréciation d\'actif', 'Colonne « amortissements et dépréciations » de l\'actif', '6817/6866 · 7817/7866'], ['Risques et charges', 'Passif : « Provisions » (15)', '6815/6865/6875 · 7815/7865/7875'], ['Réglementée', 'Capitaux propres (14)', '6872 · 7872']])
    c.p('Dans l\'annexe, le <b>tableau des provisions</b> présente, pour chaque catégorie, la valeur de début, les augmentations (dotations), les diminutions (reprises) et la valeur de fin, avec la ventilation exploitation / financier / exceptionnel.')
    c.synthese(['Trois familles : dépréciations (actif, 29 à 59), provisions pour risques et charges (passif, 15), provisions réglementées (capitaux propres, 14).', 'Toujours raisonner en <b>ajustement</b> : nécessaire − existante.', '<b>Prudence</b> : pas de compensation entre titres, pas de gain latent, dépréciation des créances sur le HT.', 'Une provision devenue sans objet est <b>reprise</b>.'])
    return c


def ch3():
    c = Cours()
    c.intro('De quoi parle ce chapitre ?',
            'Deux choses faussent le résultat en fin d\'année. D\'abord, les <b>stocks</b> ne sont pas suivis au jour le jour : le compte de stock affiche encore la valeur du début d\'année. Ensuite, les <b>factures</b> ne tombent pas toujours dans la bonne année : une facture peut arriver en janvier pour une livraison de décembre, ou on peut avoir payé en décembre le loyer de janvier. Les <b>régularisations</b> corrigent ces deux décalages.',
            ['Comment remplacer le stock initial par le stock final ?', 'Comment lire une variation de stock ?', 'Que faire d\'une charge dont la facture n\'est pas arrivée ? d\'une charge payée d\'avance ?'])

    c.sec('I. L\'évaluation des stocks')
    c.idee('Pendant l\'année, les comptes de stock ne bougent pas (inventaire intermittent). À la clôture, on <b>annule le stock du début</b> et on <b>enregistre celui de la fin</b>, après l\'avoir compté.')
    c.p('On compte physiquement les stocks, comme à l\'ouverture. Les quantités sont valorisées :')
    c.ul(['au <b>coût d\'acquisition</b> pour les marchandises et approvisionnements ;', 'au <b>coût de production</b> pour les produits fabriqués ;', 'en <b>excluant les coûts administratifs</b>.'])
    c.df('Inventaire intermittent', 'Les comptes de stocks ne sont pas mis à jour au fil de l\'année : à la clôture, on annule le stock initial et on constate le stock final.')
    c.h3('Biens achetés : marchandises, matières, approvisionnements (31, 32, 37 / 603)')
    c.ecr(E_('31/12/N', [('D', '6037', 'Variation des stocks de marchandises', 31000), ('C', '37', 'Stocks de marchandises', 31000)], 'Annulation du stock initial'),
          E_('31/12/N', [('D', '37', 'Stocks de marchandises', 38000), ('C', '6037', 'Variation des stocks de marchandises', 38000)], 'Constatation du stock final'))
    c.df('Variation de stock (achats)', 'SI − SF, inscrite en charges (603) : positive si le stock a diminué, négative si le stock a augmenté.')
    c.pourquoi('Pourquoi la variation de stock est-elle une charge ?', 'Parce qu\'on veut mesurer ce qui a été <b>réellement consommé</b>, pas seulement acheté. Si j\'ai acheté 100 mais qu\'il me reste 20 de plus qu\'au début, je n\'ai consommé que 80 : la variation (−20) vient réduire les achats.')
    c.f('Achats consommés = Achats + (SI − SF)')
    c.autrement('un 603 <b>débiteur</b> signifie que le stock a baissé (on a puisé dedans, la charge augmente) ; un 603 <b>créditeur</b> signifie qu\'il a monté (on a acheté plus que consommé, la charge diminue).')
    c.h3('Produits fabriqués (35 / 713)')
    c.ecr(E_('31/12/N', [('D', '7135', 'Variation des stocks de produits', 67500), ('C', '355', 'Stocks de produits finis', 67500)], 'Annulation du stock initial'),
          E_('31/12/N', [('D', '355', 'Stocks de produits finis', 83000), ('C', '7135', 'Variation des stocks de produits', 83000)], 'Constatation du stock final'))
    c.df('Production stockée', 'SF − SI des produits fabriqués, inscrite en produits (713) : positive si le stock a augmenté (produit), négative en cas de déstockage.')
    c.pourquoi('Pourquoi une hausse du stock de produits est-elle un produit ?', 'Parce que l\'entreprise a fabriqué plus qu\'elle n\'a vendu : ce qui est stocké, c\'est de la production de l\'année, qui a de la valeur. Sans elle, les charges de fabrication apparaîtraient sans la production correspondante.')
    c.f('Production de l\'exercice = production vendue (70) + production stockée (713 = SF − SI) + production immobilisée (72)')
    c.warn('Attention aux sens opposés : achats → <b>SI − SF</b> en charges ; produits → <b>SF − SI</b> en produits. Dans les deux cas, une hausse du stock <b>améliore</b> le résultat.')
    c.retenir(['Annuler le SI, constater le SF.', 'Achats : variation SI − SF (603). Produits : production stockée SF − SI (713).', 'Une hausse de stock améliore le résultat.'])
    c.transition('Deuxième source de décalage : les factures qui ne tombent pas dans la bonne année.')

    c.sec('II. La régularisation des charges et des produits')
    c.idee('On enregistre les opérations à la date des <b>factures</b>, mais on doit les rattacher à l\'année qu\'elles <b>concernent</b>. Quand les deux ne coïncident pas, on corrige.')
    c.p('C\'est le principe de <b>séparation des exercices</b>. Il y a deux cas de figure, symétriques.')
    c.tab(['La facture…', 'Charge', 'Produit'], [['… n\'est <b>pas encore</b> enregistrée, mais concerne l\'année', 'Charge à payer (on l\'ajoute)', 'Produit à recevoir (on l\'ajoute)'], ['… est <b>déjà</b> enregistrée, mais concerne l\'année suivante', 'Charge constatée d\'avance (on la retire)', 'Produit constaté d\'avance (on le retire)']])
    c.h3('A. Charges à payer')
    c.df('Charge à payer', 'Charge imputable à l\'exercice dont la pièce (facture) ne sera enregistrée qu\'à l\'exercice suivant ; on l\'enregistre à l\'inventaire avec une dette dont le numéro porte un 8 en troisième position.')
    c.ul(['Débit du compte de charge pour le montant <b>HT</b> ;', 'crédit d\'un compte de dette pour le <b>TTC</b> ;', 'la TVA au débit du <b>4458</b> État, TVA à régulariser (44586).'])
    c.tab(['Charge', 'Compte de dette'], [['60 Achats · 61/62 Services extérieurs', '4081 Fournisseurs, factures non parvenues'], ['63 Impôts', '4486 État, charges à payer'], ['64 Personnel', '428 Personnel · 4386 Organismes sociaux, charges à payer'], ['65 Autres charges', '4686 Divers, charges à payer'], ['66 Charges financières', '1688 Intérêts courus sur emprunts · 5186 Banques, intérêts courus']])
    c.note('Le poly indique « 4486 » sur la ligne 65 : le compte « Divers, charges à payer » du plan comptable est le <b>4686</b>.')
    c.pas('Exemple pas à pas (TD 9)', ['Le 20 décembre, livraison de 14 000 € HT de matières premières ; la facture arrivera en janvier.', 'La charge concerne décembre : on l\'enregistre dès maintenant, 601 pour 14 000 € HT.', 'TVA sur facture non parvenue : 14 000 × 20 % = 2 800 € (44586).', 'Dette envers le fournisseur : 16 800 € TTC (4081).'])
    c.ecr(E_('31/12/N', [('D', '601', 'Achats de matières premières', 14000), ('D', '44586', 'TVA sur factures non parvenues', 2800), ('C', '4081', 'Fournisseurs, factures non parvenues', 16800)], 'Livraison du 20/12 sans facture'))
    c.h3('B. Produits à recevoir')
    c.df('Produit à recevoir', 'Produit acquis à l\'exercice dont la pièce sera établie à l\'exercice suivant ; symétrique de la charge à payer (créance en débit TTC, produit en crédit HT, TVA au crédit du 4458/44587).')
    c.tab(['Créance (débit, TTC)', 'Produit (crédit, HT)'], [['4181 Clients, factures à établir', '70 Ventes'], ['4687 Débiteurs divers, produits à recevoir', '75 Autres produits'], ['2768 / 508 Intérêts courus', '76 Produits financiers'], ['709 RRR accordés (débit)', '4198 Clients, RRR à accorder (crédit)']])
    c.p('Toutes ces écritures sont <b>contrepassées au 1er janvier</b> : on les annule pour pouvoir enregistrer normalement la facture quand elle arrive, sans compter la charge deux fois.')
    c.h3('C. Charges et produits constatés d\'avance')
    c.df('Charge constatée d\'avance (CCA)', 'Fraction d\'une charge enregistrée dans l\'exercice mais qui concerne l\'exercice suivant : on crédite le compte de charge et on débite le 486 pour le montant HT.')
    c.df('Produit constaté d\'avance (PCA)', 'Fraction d\'un produit enregistré dans l\'exercice mais qui concerne l\'exercice suivant : on débite le compte de produit et on crédite le 487 pour le montant HT.')
    c.f('CCA (ou PCA) = Montant HT × durée qui concerne N+1 / durée totale')
    c.pas('Exemple pas à pas (TD 9, loyer payé d\'avance)', ['Le 1er novembre, paiement d\'un loyer trimestriel de 4 500 € (novembre, décembre, janvier).', 'Janvier concerne l\'année suivante : 1 mois sur 3.', 'CCA : 4 500 × 1/3 = 1 500 €.', 'On retire 1 500 € des charges de l\'année : débit 486, crédit 613.'])
    c.ecr(E_('31/12/N', [('D', '486', 'Charges constatées d\'avance', 1500), ('C', '613', 'Locations', 1500)], 'Loyer trimestriel de 4 500 € payé le 1/11 : 1 mois concerne N+1'),
          E_('31/12/N', [('D', '752', 'Revenus des immeubles', 1200), ('C', '487', 'Produits constatés d\'avance', 1200)], 'Loyer de 1 800 € HT reçu le 1/12 pour 3 mois : 2 mois concernent N+1'))
    c.retenir(['Pièce pas encore reçue ou émise → charge à payer / produit à recevoir (HT + TVA 4458, dette/créance TTC).', 'Pièce déjà enregistrée pour N+1 → CCA (486) / PCA (487), au HT et au prorata du temps.', 'Tout est contrepassé au 1er janvier.'])
    c.synthese(['Stocks : on annule le SI, on constate le SF. Achats → SI − SF en charges ; produits → SF − SI en produits.', 'Charges et produits : on rattache à l\'année concernée, quelle que soit la date de la facture.', 'Quatre cas : charge à payer, produit à recevoir, CCA, PCA. Tous sont contrepassés au 1er janvier.'])
    return c


def ch4():
    c = Cours()
    c.intro('De quoi parle ce chapitre ?',
            'Toutes les écritures des chapitres précédents aboutissent à deux tableaux : le <b>bilan</b> et le <b>compte de résultat</b>, complétés par l\'<b>annexe</b>. Ce chapitre montre comment ils sont construits, quels comptes vont où, et comment ils sont liés.',
            ['Que montre le bilan ? le compte de résultat ?', 'Dans quel poste va chaque compte ?', 'Quel est le lien entre les deux tableaux ?'])

    c.sec('I. Bilan et compte de résultat : deux tableaux complémentaires')
    c.idee('Le bilan est une <b>photographie</b> (ce que l\'entreprise possède et doit à la date de clôture) ; le compte de résultat est un <b>film</b> (ce qui s\'est passé pendant l\'année).')
    c.p('Ils sont élaborés lors de l\'inventaire, à partir de la <b>balance après inventaire</b>, et permettent d\'évaluer le patrimoine, la performance et la situation de l\'entreprise.')
    c.df('Bilan', 'Photographie de la situation patrimoniale de l\'entreprise à la clôture : actif (emplois, comptes 2, 3, 4, 5) et passif (ressources, comptes 1 et 4) ; ses comptes s\'accumulent d\'un exercice à l\'autre.')
    c.df('Compte de résultat', 'Film de l\'exercice : il retrace les charges et les produits (exploitation, financiers, exceptionnels) qui déterminent le résultat ; ses comptes sont remis à zéro à chaque fin d\'exercice.')
    c.df('Annexe', 'Document qui complète le bilan et le compte de résultat par des tableaux explicatifs (immobilisations, amortissements, provisions…) et des informations sur les méthodes.')
    c.df('Résultat', 'Produits − charges ; seul élément commun aux deux tableaux : il apparaît au passif du bilan (capitaux propres) et comme solde du compte de résultat.')
    c.pourquoi('Pourquoi le résultat se retrouve-t-il dans les deux tableaux ?', 'Parce qu\'un bénéfice enrichit les propriétaires : il augmente les capitaux propres au passif. C\'est ce qui fait « tenir » l\'égalité actif = passif : si l\'entreprise gagne de l\'argent, son actif augmente et, en face, ses capitaux propres augmentent du même montant.')
    c.tab(['Compte de résultat — Charges', 'Compte de résultat — Produits'], [['Charges d\'exploitation', 'Produits d\'exploitation'], ['Charges financières', 'Produits financiers'], ['Charges exceptionnelles', 'Produits exceptionnels'], ['Impôt sur les bénéfices', ''], ['Résultat net (bénéfice)', '']])
    c.tab(['Bilan — Actif (emplois)', 'Bilan — Passif (ressources)'], [['<b>Actif immobilisé</b> : incorporel, corporel, financier', '<b>Capitaux propres</b> : capital, réserves, résultat ±'], ['<b>Actif circulant</b> : stocks, créances, VMP, disponibilités', '<b>Dettes</b> : financières, d\'exploitation, diverses'], ['Total général', 'Total général']])
    c.retenir(['Bilan = photographie (stocks de richesse) ; compte de résultat = film (flux de l\'année).', 'Le résultat relie les deux et fait tenir actif = passif.'])
    c.transition('Concrètement, il faut savoir <b>dans quel poste</b> placer chaque compte de la balance.')

    c.sec('II. Du numéro de compte au poste du bilan')
    c.tab(['Poste de l\'actif', 'Valeur brute', 'Amort. et dépréciations'], [
        ['Fonds commercial', '206 – 207', '2906 – 2907'], ['Autres immobilisations incorporelles', '201 – 203 – 205 – 208', '280 – 2905 – 2908'], ['Immobilisations corporelles', '21 – 22 – 23', '281 – 291'], ['Immobilisations financières', '26 – 27', '296 – 297'],
        ['Stocks (autres que marchandises)', '31 à 35', '391 à 395'], ['Stocks de marchandises', '37', '397'], ['Avances et acomptes versés', '4091', ''], ['Clients et comptes rattachés', '41', '491'],
        ['Autres créances', '40 (sauf 4091), 42 à 46', '496'], ['VMP', '50', '590'], ['Disponibilités', '51 – 54 – 58 · caisse 53', ''], ['Charges constatées d\'avance', '486', '']])
    c.tab(['Poste du passif', 'Comptes'], [['Capital', '101 – 108'], ['Écarts de réévaluation', '105'], ['Réserves (légale, réglementées, autres)', '1061 · 1064 · 1063 – 1068'], ['Report à nouveau', '110 – 119 (en négatif si débiteur)'], ['Résultat de l\'exercice', 'repris du compte de résultat (en négatif si perte)'],
                                           ['Provisions réglementées', '14'], ['Provisions (risques et charges)', '15'], ['Emprunts et dettes assimilées', '16 et 51 créditeurs'], ['Avances et acomptes reçus', '4191'], ['Fournisseurs', '40'], ['Autres dettes', '41 à 46'], ['Produits constatés d\'avance', '487']])
    c.note('Les comptes 28, 29, 39, 49, 59 ne vont <b>jamais</b> au passif : ils se placent dans la colonne du milieu de l\'actif, en déduction du brut.')

    c.sec('III. Du numéro de compte au poste du compte de résultat')
    c.tab(['Charges', 'Comptes'], [['Achats de marchandises', '607 – 6097'], ['Variation de stocks de marchandises', '6037'], ['Achats d\'approvisionnements', '601 à 606'], ['Variation de stocks (approvisionnements)', '6031 – 6032'], ['Autres charges externes', '61 – 62'], ['Impôts et taxes', '63'], ['Salaires / charges sociales', '641 – 644 / 645 – 646'],
                                   ['Dotations aux amortissements', '6811'], ['Dotations aux provisions et dépréciations', '6815 – 6817'], ['Autres charges', '65'], ['Charges financières', '66 – 686'], ['Charges exceptionnelles', '67 – 687'], ['Impôt sur les bénéfices', '695 – 697']])
    c.tab(['Produits', 'Comptes'], [['Ventes de marchandises', '707 – 7097'], ['Production vendue', '701 – 706 – 708 – 7091 – 7096 – 7098'], ['Production stockée', '713'], ['Production immobilisée', '72'], ['Subventions d\'exploitation', '74'], ['Autres produits', '75 – 781 – 791'], ['Produits financiers', '76 – 786 – 796'], ['Produits exceptionnels', '77 – 787 – 797']])
    c.autrement('les rabais, remises et ristournes (609 obtenus, 709 accordés) ne sont ni des produits ni des charges à part : on les <b>retranche</b> des achats ou des ventes.')

    c.sec('IV. Liens entre les deux tableaux et avec les autres disciplines')
    c.ul(['Le résultat passe dans les <b>capitaux propres</b> : c\'est le contrôle final, actif = passif.', 'Une écriture d\'inventaire touche en général <b>les deux</b> tableaux : une dotation diminue le résultat et, au bilan, diminue l\'actif net ou augmente les provisions.', 'Exception : les écritures purement bilancielles (transfert 411 → 416, écarts de conversion) ne touchent pas le résultat.'])
    c.df('Analyse financière', 'Utilisation du bilan, du compte de résultat et de l\'annexe pour évaluer la liquidité, la solvabilité et la performance de l\'entreprise.')
    c.df('Comptabilité analytique', 'Utilisation des flux internes (mouvements de stocks, coûts, ventes) identifiés par la comptabilité générale pour calculer des coûts et des marges.')
    c.f('Actif = Capitaux propres + Provisions + Dettes (+ régularisations) · Résultat = Produits − Charges')
    c.synthese(['Bilan = photographie ; compte de résultat = film ; annexe = explications.', 'Classes 1 à 5 → bilan ; 6 et 7 → compte de résultat ; 28/29/39/49/59 → en déduction de l\'actif.', 'Le résultat est le seul élément commun : il fait tenir actif = passif.', 'Ces documents servent ensuite à l\'analyse financière et à la comptabilité analytique.'])
    return c
