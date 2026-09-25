"""Explications détaillées des courbes et schémas (lecture, mécanisme, exemple, à retenir, piège).
Chaque entrée remplace l'explication courte de la courbe du même identifiant."""

EXP = {
    # ---------------- COMPTABILITÉ ----------------
    'cpt-g1': dict(
        axes='En abscisse, les exercices (2017 à 2022). En ordonnée, la valeur nette comptable (VNC) de la machine DEBROS (98 000 €).',
        lecture=['Les deux courbes partent de 98 000 € et arrivent à 0 € en 2022 : les deux méthodes amortissent la même somme au total.', 'La courbe orange (dégressif) plonge plus vite au début : fin 2017, la VNC n\'est plus que de 72 275 €, contre 84 715,56 € en linéaire.', 'Les deux courbes se rapprochent en fin de plan, quand le dégressif bascule au linéaire.'],
        mecanisme='Le linéaire retire chaque année la même somme (19 600 €). Le dégressif retire un pourcentage fixe (35 %) de ce qui reste : beaucoup au début, puis de moins en moins.',
        exemple='2017 : dégressif 25 725 € contre 13 284,44 € en linéaire, soit 12 440,56 € d\'écart. C\'est le montant d\'amortissement dérogatoire de 2017.',
        retenir=['Même total amorti, répartition différente dans le temps.', 'Dégressif = plus de charges au début, donc moins d\'impôt tout de suite.', 'L\'écart vertical entre les deux courbes = amortissements dérogatoires cumulés.'],
        piege='Croire que le dégressif amortit « plus » : sur toute la durée, il amortit exactement la même valeur.'),
    'cpt-g2': dict(
        axes='En abscisse, les exercices. En ordonnée, l\'annuité (la dotation de l\'année). Barres violettes : linéaire ; barres orange : dégressif.',
        lecture=['Linéaire : première barre plus petite (prorata de 244 jours), puis 4 barres identiques de 19 600 €, puis une petite barre finale.', 'Dégressif : grosse barre en 2017-2018, puis décroissance, puis deux barres égales (13 571,64 €) après la bascule au linéaire.', 'La différence de hauteur entre les deux barres d\'une année = la dotation (dégressif plus haut) ou la reprise (linéaire plus haut) de dérogatoire.'],
        mecanisme='Le linéaire applique 20 % au prix d\'achat ; le dégressif applique 35 % à la VNC restante. Quand le taux linéaire sur la durée restante dépasse 35 %, on répartit la VNC restante en parts égales.',
        exemple='2019 : dégressif 16 442,56 € et linéaire 19 600 €. Le linéaire est plus haut : on reprend 3 157,44 € de dérogatoire (145 / 7872).',
        retenir=['Barre orange plus haute que la violette → dotation 6872 / 145.', 'Barre violette plus haute que l\'orange → reprise 145 / 7872.', 'Somme des barres orange = somme des barres violettes = 98 000 €.'],
        piege='Oublier le prorata : la 1ʳᵉ annuité linéaire est en jours (depuis la mise en service), la 1ʳᵉ dégressive en mois (depuis le mois d\'acquisition).'),
    'cpt-g3': dict(
        axes='En abscisse, les exercices. En ordonnée, le solde du compte 145 Amortissements dérogatoires (au passif, dans les capitaux propres).',
        lecture=['La courbe monte en 2017-2018 : on dote du dérogatoire (6872).', 'Elle atteint un sommet (18 136,81 € fin 2018), puis redescend : on reprend (7872).', 'Elle revient à 0 en 2022 : tout le dérogatoire a été repris.'],
        mecanisme='Le 145 stocke l\'avance fiscale : tant que le dégressif dépasse le linéaire, le bénéfice imposable est réduit et le 145 augmente. Ensuite, l\'avantage se « rend » et le 145 diminue.',
        exemple='Solde fin 2018 : 12 440,56 + 5 696,25 = 18 136,81 €. Fin 2020 : 8 951,01 € après les reprises de 2019 et 2020.',
        retenir=['Le dérogatoire ne supprime pas l\'impôt, il le <b>décale</b> : c\'est un gain de trésorerie.', 'Le 145 est une provision réglementée, en capitaux propres.', 'Il ne touche pas l\'actif du bilan.'],
        piege='Mettre le 145 en déduction de l\'actif : il est au passif (capitaux propres).'),
    'cpt-g4': dict(
        axes='En haut, le compte de résultat (charges à gauche, produits à droite). En bas, le bilan (actif à gauche, passif à droite).',
        lecture=['Le compte de résultat se lit par niveaux : exploitation, financier, exceptionnel, puis impôt.', 'La flèche montre que le résultat net quitte le compte de résultat pour entrer dans les capitaux propres du bilan.', 'À l\'actif, chaque poste se présente en brut − amortissements/dépréciations = net.'],
        mecanisme='Le compte de résultat mesure les flux d\'une année (charges et produits, remis à zéro chaque année). Le bilan mesure les stocks de richesse à une date. Le résultat relie les deux : un bénéfice augmente les capitaux propres.',
        exemple='Balance Monceau (TD 11) : le résultat calculé au compte de résultat, reporté au passif, fait tomber l\'actif net et le passif exactement sur le même total.',
        retenir=['Résultat = seul élément commun aux deux tableaux.', 'Classes 6-7 → compte de résultat ; classes 1 à 5 → bilan.', 'Contrôle final : actif = passif.'],
        piege='Placer les amortissements (28) au passif : ils se déduisent de l\'actif.'),
    'cpt-g5': dict(
        axes='Schéma de flux : chaque boîte est une étape de la clôture, les flèches indiquent l\'ordre.',
        lecture=['On part des opérations courantes enregistrées au journal.', 'Elles donnent la balance avant inventaire.', 'L\'inventaire extra-comptable (comptage, évaluations) conduit aux écritures d\'inventaire.', 'On obtient la balance après inventaire, puis les comptes annuels.'],
        mecanisme='La comptabilité de l\'année enregistre des pièces ; l\'inventaire confronte ces enregistrements à la réalité (stocks, créances, usure) et corrige les comptes pour donner une image fidèle.',
        exemple='Un stock compté 38 000 € alors que le compte affiche encore 31 000 € du début d\'année : on annule 31 000 et on constate 38 000 (ch. 3).',
        retenir=['Deux temps : constater (extra-comptable) puis corriger (écritures d\'inventaire).', 'Trois familles d\'écritures : stocks, amortissements/provisions, régularisations.'],
        piege='Confondre balance avant inventaire (point de départ) et balance après inventaire (base des comptes annuels).'),

    # ---------------- MICRO ----------------
    'mic-g0': dict(
        axes='En abscisse, la quantité échangée. En ordonnée, le prix unitaire. Courbe violette : demande ; courbe orange : offre.',
        lecture=['La demande descend : plus le prix est bas, plus on achète.', 'L\'offre monte : plus le prix est haut, plus on veut vendre.', 'Leur intersection E donne le prix d\'équilibre P* et la quantité Q*.', 'Ligne jaune (au-dessus de P*) : excès d\'offre ; ligne rose (en dessous) : excès de demande.'],
        mecanisme='Si le prix est trop haut, des vendeurs ne trouvent pas preneur et baissent leurs prix. S\'il est trop bas, des acheteurs repartent les mains vides et les prix montent. Le prix converge vers P*.',
        exemple='TD élasticités, exercice 3 : Q<sub>D</sub> = 1 760 − 8p et Q<sub>O</sub> = 160p − 1 600 donnent P* = 20 et Q* = 1 600.',
        retenir=['Équilibre : offre = demande.', 'Variation du prix du bien → mouvement le long d\'une courbe.', 'Variation du revenu, des autres prix ou des coûts → déplacement de la courbe.'],
        piege='Dire que « la demande augmente » quand le prix baisse : c\'est la <b>quantité demandée</b> qui augmente, la courbe ne bouge pas.'),
    'mic-g1': dict(
        axes='En abscisse, la quantité de bien 1 (x1). En ordonnée, la quantité de bien 2 (x2). Zone violette : paniers accessibles. Droite orange : droite de budget. Courbes : courbes d\'indifférence.',
        lecture=['La droite coupe les axes en R/p2 = 20 et R/p1 = 50.', 'La courbe verte touche la droite en un seul point, (25 ; 10) : c\'est la CI la plus haute qu\'on peut atteindre.', 'La CI grise du bas coupe la droite en deux points : ces paniers sont accessibles mais moins bons.', 'La CI grise du haut ne touche jamais la droite : elle est inaccessible.'],
        mecanisme='Au point de tangence, la pente de la CI (le TMS) est égale à la pente de la droite (p1/p2) : ce que l\'agent est prêt à échanger correspond exactement à ce que le marché demande.',
        exemple='U = x1<sup>0,5</sup>x2<sup>0,5</sup>, R = 100, p1 = 2, p2 = 5 : TMS = x2/x1 = 10/25 = 0,4 = p1/p2.',
        retenir=['Optimum : sur la droite de budget ET TMS = p1/p2.', 'Graphiquement : tangence entre la droite de budget et la CI la plus haute.'],
        piege='Choisir un point d\'intersection entre une CI et la droite : on peut toujours atteindre une CI plus haute.'),
    'mic-g2': dict(
        axes='En abscisse x1, en ordonnée x2. Trois courbes d\'indifférence (CI1, CI2, CI3) de plus en plus éloignées de l\'origine.',
        lecture=['Chaque courbe relie des paniers qui procurent la même satisfaction : A et B sont sur la même CI.', 'La flèche jaune indique le sens de la hausse de l\'utilité : CI3 > CI2 > CI1.', 'Les courbes descendent et sont bombées vers l\'origine.'],
        mecanisme='Pente négative : pour garder la même satisfaction avec plus de bien 1, il faut moins de bien 2 (monotonie). Convexité : on accepte de céder de moins en moins de bien 2 quand on a déjà beaucoup de bien 1 (TMS décroissant).',
        exemple='TD C1, exercice 2 : de A (5 ; 13) à B (6 ; 10), on cède 3 unités ; de B à C (7 ; 8), seulement 2. Le TMS décroît, la CI est convexe.',
        retenir=['Plus loin de l\'origine = plus d\'utilité.', 'Décroissantes, convexes, ne se croisent jamais (transitivité).'],
        piege='Dessiner deux CI qui se croisent : impossible avec des préférences transitives.'),
    'mic-g3': dict(
        axes='À gauche, les CI de substituts parfaits ; à droite, celles de compléments parfaits. Mêmes axes x1, x2.',
        lecture=['Substituts parfaits : des droites parallèles ; le TMS est constant.', 'Compléments parfaits : des « L » ; seul le coin compte, ajouter un seul des deux biens n\'augmente pas la satisfaction.'],
        mecanisme='Substituts : un bien remplace l\'autre à taux fixe (deux marques de sucre). Compléments : les biens se consomment ensemble en proportion fixe (chaussure gauche et droite).',
        exemple='Substituts avec p1/p2 < TMS : l\'agent ne consomme que du bien 1 (solution en coin). Compléments : l\'optimum est toujours au coin du L.',
        retenir=['Substituts → CI droites, solutions souvent en coin.', 'Compléments → CI en L, consommation en proportions fixes.'],
        piege='Appliquer TMS = p1/p2 dans ces cas : la condition de tangence ne fonctionne pas.'),
    'mic-g4': dict(
        axes='En abscisse x1, en ordonnée x2. Droites orange : budgets avant (p1 = 10) et après (p1 = 5). Droite jaune pointillée : droite compensée. Courbes : utilité initiale (verte) et finale (violette).',
        lecture=['E (25 ; 375) : optimum initial, tangence entre DB1 et la CI verte.', 'E\'\' (50 ; 375) : optimum final, tangence entre DB2 et la CI violette.', 'E\' (42 ; 315) : point imaginaire, sur la CI initiale mais avec les nouveaux prix (droite jaune parallèle à DB2).', 'E → E\' : effet de substitution ; E\' → E\'\' : effet de revenu.'],
        mecanisme='La baisse de p1 a deux effets. Le bien 1 devient relativement moins cher : on le substitue au bien 2 (E → E\'). Et l\'agent devient plus riche en pouvoir d\'achat : il consomme plus des deux biens normaux (E\' → E\'\').',
        exemple='x1 : ES +17, ER +8, ET +25. x2 : ES −60, ER +60, ET 0.',
        retenir=['Droite compensée = nouveaux prix + utilité initiale.', 'ET = ES + ER.', 'ER > 0 → biens normaux ; si l\'ER négatif l\'emporte sur l\'ES → bien de Giffen.'],
        piege='Calculer le panier intermédiaire avec le revenu initial : c\'est l\'utilité initiale qu\'on garde, pas le revenu.'),
    'mic-g5': dict(
        axes='En abscisse, le revenu R. En ordonnée, la quantité consommée d\'un bien. Une courbe d\'Engel par type de bien.',
        lecture=['Vert (droite) : bien normal, la consommation augmente avec le revenu.', 'Jaune (monte de moins en moins) : première nécessité, 0 < E < 1.', 'Orange (monte de plus en plus) : luxe, E > 1.', 'Rose (descend) : bien inférieur, E < 0.'],
        mecanisme='La pente de la courbe d\'Engel traduit l\'élasticité-revenu : un bien de nécessité est vite « rassasié », un bien de luxe prend une part croissante du budget quand on s\'enrichit.',
        exemple='Cours : de 20 à 60 de revenu, l\'alimentation passe de 15 à 30 (nécessité) et le cinéma de 5 à 30 (luxe). TD élasticités, exercice 4 : bien 1, E ≈ 1,30 (luxe) ; bien 2, E ≈ 0,70 (nécessité).',
        retenir=['E < 0 inférieur ; 0 < E < 1 nécessité ; E > 1 luxe.', 'Courbe d\'Engel = quantité en fonction du revenu, à prix constants.'],
        piege='Confondre courbe d\'Engel (quantité / revenu) et courbe de demande (prix / quantité).'),
    'mic-g6': dict(
        axes='Deux courbes de demande : prix en ordonnée, quantité en abscisse.',
        lecture=['À gauche, courbe presque verticale : une forte variation du prix change peu la quantité.', 'À droite, courbe presque plate : une petite variation du prix change beaucoup la quantité.'],
        mecanisme='L\'élasticité-prix mesure la réaction en % de la quantité à une hausse de 1 % du prix. Elle est faible pour les biens indispensables ou sans substitut, forte quand les substituts sont nombreux.',
        exemple='TD élasticités, exercice 3 : E<sub>D</sub> = −0,1 (très inélastique) ; exercice 2 : E ≈ −1,61 (élastique).',
        retenir=['|E| < 1 : inélastique ; |E| > 1 : élastique.', 'E = (∂x/∂p)·(p/x), en général négative.'],
        piege='Juger l\'élasticité à la seule pente de la droite : elle dépend aussi du point (p/x).'),
    'mic-g7': dict(
        axes='En haut : production totale y en fonction du travail L (capital fixé à 10). En bas : productivité moyenne PML (verte) et productivité marginale PmL (orange).',
        lecture=['La production totale monte vite, puis de plus en plus lentement, puis baisse après L = 8.', 'La PmL culmine à 30 (L = 3), puis diminue et devient négative à L = 9.', 'La PML culmine à 20 (L = 3-4), exactement là où la PmL la coupe.'],
        mecanisme='Avec 10 machines seulement, chaque travailleur supplémentaire a moins de capital à sa disposition : son apport finit par diminuer. C\'est la loi des rendements marginaux décroissants.',
        exemple='Du 4ᵉ au 5ᵉ travailleur : y passe de 80 à 94, PmL = 14 ; PML = 94/5 = 18,8.',
        retenir=['PML = y/L ; PmL = Δy/ΔL.', 'La marginale coupe la moyenne en son maximum.', 'Un producteur rationnel n\'embauche pas au point où la PmL devient négative.'],
        piege='Inverser les notations : dans ton cours, PML = moyenne et PmL = marginale.'),
    'mic-g8': dict(
        axes='En abscisse le travail L, en ordonnée le capital K. Courbes : isoquantes (y = 10 et y = 20). Droites : isocoûts. Pointillé bleu : sentier d\'expansion.',
        lecture=['L\'isocoût orange (C ≈ 28,28 €) touche l\'isoquante y = 10 en un seul point, (7,07 ; 14,14) : c\'est la combinaison la moins chère.', 'L\'isocoût gris plus bas ne permet pas de produire 10 ; celui plus haut produit 10 mais coûte plus cher.', 'En reliant les optimums de chaque production, on obtient le sentier d\'expansion K = 2L.'],
        mecanisme='Au point de tangence, TMST = PmL/PmK = pL/pK : le dernier euro dépensé en travail rapporte autant de production que le dernier euro dépensé en capital.',
        exemple='y = K<sup>0,5</sup>L<sup>0,5</sup>, pK = 1, pL = 2 : K/L = 2, puis 10 = √2·L, donc L = 7,07 et K = 14,14. La combinaison (10 ; 10) coûterait 30 €, contre 28,28 €.',
        retenir=['Isoquante = même production ; isocoût = même coût.', 'Optimum : TMST = pL/pK.', 'Sentier d\'expansion = ensemble des optimums quand y varie.'],
        piege='Écrire TMST = pK/pL : le rapport est pL/pK (travail sur capital).'),
    'mic-g9': dict(
        axes='En haut : coûts totaux (CT, CV, CF) en fonction de la production y. En bas : coûts unitaires (Cm, CM, CVM, CFM).',
        lecture=['CF est plat à 50 : il ne dépend pas de y. CT = CF + CV, décalé de 50 au-dessus du CV.', 'CFM descend sans cesse : 50 € répartis sur de plus en plus d\'unités.', 'Le Cm (orange) baisse jusqu\'à y = 4 puis monte fortement.', 'Le Cm coupe le CVM puis le CM en leur minimum.'],
        mecanisme='Le Cm reflète la productivité marginale : Cm = pL/PmL. Quand la PmL baisse (rendements décroissants), chaque unité supplémentaire coûte plus cher, et le Cm monte.',
        exemple='De y = 1 à y = 2, le CT passe de 100 à 128 : Cm = 28. À y = 8, CM = 254/8 = 31,8 ; à y = 9, Cm = 38 > CM, donc le CM remonte (32,4).',
        retenir=['CT = CF + CV ; CM = CFM + CVM.', 'Cm < CM → CM baisse ; Cm > CM → CM monte.', 'Cm = pL/PmL.'],
        piege='Oublier que le CFM baisse toujours : il n\'a jamais de minimum.'),
    'mic-g10': dict(
        axes='En abscisse, la production y (en milliers). En ordonnée, le coût marginal Cm et le coût moyen CM de CT = y³ − 2y² + 3y.',
        lecture=['Le Cm est minimal en y = 2/3 (Cm = 5/3 ≈ 1,67).', 'Le CM est minimal en y = 1 (CM = 2).', 'Les deux courbes se coupent exactement en (1 ; 2).'],
        mecanisme='Cm = dCT/dy = 3y² − 4y + 3 et CM = CT/y = y² − 2y + 3. On trouve leurs minimums en annulant les dérivées : 6y − 4 = 0 et 2y − 2 = 0.',
        exemple='Cm(1) = 3 − 4 + 3 = 2 = CM(1) : la vérification demandée par le TD Producteur 2.',
        retenir=['Le Cm coupe le CM en son minimum.', 'Minimum d\'une fonction : dérivée nulle.'],
        piege='Chercher le minimum du CM en annulant le Cm : il faut annuler la dérivée du CM.'),
    'mic-g11': dict(
        axes='En abscisse, la production y. En ordonnée, le coût total de long terme. Trois formes selon les rendements d\'échelle.',
        lecture=['Vert (concave) : le coût monte moins vite que la production.', 'Violet (droite) : le coût est proportionnel à la production.', 'Orange (convexe) : le coût monte plus vite que la production.'],
        mecanisme='Avec des rendements d\'échelle croissants, doubler les facteurs fait plus que doubler la production : le coût par unité baisse. C\'est l\'inverse avec des rendements décroissants.',
        exemple='y = K<sup>0,5</sup>L<sup>0,5</sup> (0,5 + 0,5 = 1, rendements constants) donne C = 2√2·y : une droite. y = K<sup>0,4</sup>L<sup>0,4</sup> (0,8 < 1) donne C = 40y<sup>1,25</sup> : convexe.',
        retenir=['Cobb-Douglas : α + β > 1 croissants, = 1 constants, < 1 décroissants.', 'À long terme, C<sub>LT</sub> ≤ C<sub>CT</sub>.'],
        piege='Confondre rendements d\'échelle (tous les facteurs augmentent) et rendements marginaux (un seul facteur augmente).'),

    # ---------------- MARKETING ----------------
    'mkt-g1': dict(
        axes='Axe vertical : croissance du marché (faible en bas, forte en haut). Axe horizontal : part de marché de l\'entreprise, croissante vers la droite (orientation de ton cours).',
        lecture=['En haut à gauche, les dilemmes : marché en croissance mais position faible.', 'En haut à droite, les stars : marché en croissance et position forte.', 'En bas à droite, les vaches à lait : marché mûr et position forte.', 'En bas à gauche, les poids morts : marché mûr et position faible.'],
        mecanisme='Une forte part de marché donne des coûts plus bas (effet d\'expérience) donc de la rentabilité. Un marché en croissance demande d\'investir. D\'où l\'idée d\'un circuit financier : les vaches à lait financent les dilemmes prometteurs, qui deviennent des stars puis des vaches à lait.',
        exemple='TD 1 : le produit A (ventes élevées, croissance faible) peut financer B (forte croissance) et le lancement de C ; D (déclin) est à abandonner.',
        retenir=['Dilemmes : investir ou abandonner ; stars : soutenir ; vaches à lait : rentabiliser ; poids morts : abandonner.', 'Un portefeuille équilibré contient des vaches à lait pour financer l\'avenir.'],
        piege='Oublier que ton cours met la forte part de marché à <b>droite</b> (beaucoup de manuels la mettent à gauche) : lis toujours les axes.'),
    'mkt-g2': dict(
        axes='Axe horizontal : maturité de l\'activité (démarrage et croissance à gauche, maturité et déclin à droite). Axe vertical : position concurrentielle (marginale en bas, dominante en haut).',
        lecture=['En haut : bonne rentabilité, grâce à la position dominante.', 'À gauche : fort besoin de cash, parce que le marché est jeune.', 'Le meilleur cas est en haut à droite : rentable et peu gourmand en cash.'],
        mecanisme='Plus l\'activité mûrit, plus les besoins financiers et le risque sectoriel baissent. Plus la position est forte, plus la rentabilité monte et le risque concurrentiel baisse.',
        exemple='Une start-up leader d\'un marché naissant : rentable mais gourmande en cash (en haut à gauche).',
        retenir=['Maturité → besoins de cash ; position → rentabilité.', 'Une PdM élevée amplifie l\'effet d\'expérience.'],
        piege='Confondre ADL (maturité × position) et BCG (croissance × part de marché).'),
    'mkt-g3': dict(
        axes='Axe horizontal : intérêt stratégique du marché (fort à gauche, faible à droite). Axe vertical : position concurrentielle (faible en bas, forte en haut).',
        lecture=['Cases vertes (en haut à gauche) : investir, maintenir sa position de leader.', 'Cases jaunes (diagonale) : rentabiliser, optimiser, sélectionner.', 'Cases roses (en bas à droite) : abandonner.'],
        mecanisme='Plus le marché est attractif et la position forte, plus il faut investir. Sur un marché peu attractif où l\'on est faible, mieux vaut libérer les ressources.',
        exemple='Position forte sur un marché peu attractif → « rentabiliser » : on récolte sans réinvestir.',
        retenir=['3 × 3 cases ; diagonale = zone de sélection.', 'C\'est une aide à la décision, pas une recette.'],
        piege='Appliquer mécaniquement la case : le cours rappelle que le discernement reste de rigueur.'),
    'mkt-g4': dict(
        axes='En lignes, le diagnostic interne (forces en haut, faiblesses en bas). En colonnes, le diagnostic externe (opportunités à gauche, menaces à droite).',
        lecture=['Forces × opportunités : attaque (en profiter au maximum).', 'Forces × menaces : ajustement (consolider ses points forts).', 'Faiblesses × opportunités : défense (contourner les difficultés).', 'Faiblesses × menaces : survie (surveiller la concurrence).'],
        mecanisme='Le SWOT met en regard ce que l\'entreprise <b>est</b> (interne) et ce qui lui <b>arrive</b> (externe) pour choisir une stratégie cohérente.',
        exemple='Cas L&L : opportunités (forte demande, villes universitaires) et menaces (hypermarchés, vente en ligne). Force : le conseil des vendeurs. D\'où une stratégie de spécialisation et de différenciation par le service.',
        retenir=['Interne = forces et faiblesses ; externe = opportunités et menaces.', 'Quatre stratégies : attaque, ajustement, défense, survie.'],
        piege='Classer « la concurrence est agressive » en faiblesse : c\'est une menace (externe).'),
    'mkt-g5': dict(
        axes='Au centre, la rivalité entre concurrents. Autour, les forces qui pèsent sur elle. En bas à gauche, la « +1 » : les pouvoirs publics.',
        lecture=['Au-dessus, les substituts : autres façons de satisfaire le besoin.', 'En dessous, les nouveaux entrants, freinés par les barrières à l\'entrée.', 'À gauche, les clients ; à droite, les fournisseurs, avec leur pouvoir de négociation.'],
        mecanisme='Chaque force capte une partie de la valeur du secteur : des clients puissants font baisser les prix, des fournisseurs puissants font monter les coûts. Plus les forces sont fortes, moins le secteur est rentable.',
        exemple='Smartphones (TD 5) : rivalité très forte (Samsung contre Apple), entrants freinés par la R&D et les brevets, fournisseurs de composants et d\'OS puissants.',
        retenir=['5 forces + pouvoirs publics.', 'Forces fortes → secteur peu attractif.'],
        piege='Réduire la concurrence aux concurrents directs : les substituts et les entrants comptent aussi.'),
    'mkt-g6': dict(
        axes='En abscisse, les années de N-4 à N. En ordonnée, les ventes des quatre produits de l\'exercice 1 du TD.',
        lecture=['A (violet) : très haut mais la courbe s\'aplatit (+50 %, +27 %, +13 %, +5 %) : maturité.', 'B (vert) : accélère (+80 %, +50 %, +78 %, +64 %) : croissance.', 'C (jaune) : vient d\'apparaître (+40 %) : lancement.', 'D (orange) : baisse depuis N-2 : déclin.'],
        mecanisme='C\'est la <b>forme</b> de la courbe, plus que le niveau des ventes, qui situe un produit dans son cycle de vie : on regarde l\'évolution des taux de croissance.',
        exemple='A pèse 4 500 unités sur 7 570 en N, soit environ 59 % : une forte dépendance à un produit mûr.',
        retenir=['Calculer les taux de croissance année par année.', 'Portefeuille équilibré = produits à des phases différentes.'],
        piege='Classer A en croissance parce que ses ventes sont les plus élevées : son rythme ralentit, il est en maturité.'),
    'mkt-g7': dict(
        axes='En abscisse le temps, en ordonnée les ventes d\'un produit. Quatre phases séparées par les pointillés.',
        lecture=['Lancement : ventes faibles, le produit se fait connaître.', 'Croissance : les ventes décollent.', 'Maturité : les ventes plafonnent.', 'Déclin : les ventes baissent.'],
        mecanisme='Chaque phase appelle une politique différente. Côté prix (cours) : pénétration au lancement, prix réactifs en croissance, pression sur les prix en maturité, flexibilité en déclin.',
        exemple='TD 4 : l\'électroménager vieillit désormais en 3 ans au lieu de 5 ; on le modifie régulièrement pour allonger la maturité.',
        retenir=['4 phases : lancement, croissance, maturité, déclin.', 'Relancer un produit = allonger la maturité (design, fonctions, gamme, services).'],
        piege='Penser que toutes les phases ont la même durée : elles varient beaucoup selon les produits.'),
    'mkt-g8': dict(
        axes='En abscisse, la production cumulée (1, 2, 4, 8, 16, 32, 64 : chaque graduation double la précédente). En ordonnée, le coût unitaire.',
        lecture=['À chaque doublement de la production cumulée, le coût unitaire est multiplié par 0,8 : 100 → 80 → 64 → 51,2…', 'La baisse est forte au début, puis de plus en plus lente en valeur absolue.'],
        mecanisme='Plus on a produit depuis le début, mieux on sait produire : apprentissage, améliorations du produit et du procédé, économies d\'échelle. Le leader en volume a donc les coûts les plus bas.',
        exemple='Illustration à 80 % (ton cours donne le principe sans taux) : la 16ᵉ unité coûte 41 % de la 1ʳᵉ.',
        retenir=['Effet d\'expérience : coût × (1 − x %) à chaque doublement de la production <b>cumulée</b>.', 'Base de la domination par les coûts et du cercle vertueux des parts de marché.'],
        piege='Confondre avec l\'économie d\'échelle, qui dépend de la taille d\'une série et non de la production cumulée.'),
    'mkt-g9': dict(
        axes='Schéma de flux : à gauche les bénéfices et les coûts perçus, au centre la valeur perçue, à droite ce qui se passe après l\'achat.',
        lecture=['Bénéfices perçus et coûts perçus forment la valeur perçue avant l\'achat, comparée aux offres concurrentes.', 'Après l\'achat, l\'expérience mène soit à la satisfaction (intention de rachat), soit à l\'insatisfaction (défection).'],
        mecanisme='Le client achète ce qu\'il perçoit comme le meilleur rapport bénéfices / coûts, puis confronte ses attentes à son expérience. La fidélité dépend de cette comparaison.',
        exemple='Drive : mêmes prix qu\'en hypermarché, mais moins de temps et d\'effort (coûts perçus plus bas). Nespresso : bénéfices perçus élevés (grands crus, design, boutiques).',
        retenir=['Valeur perçue = bénéfices perçus / coûts perçus, relative aux concurrents.', 'Avant l\'achat → décision ; après → fidélité ou attrition.'],
        piege='Réduire les coûts perçus au seul prix : le temps, l\'effort et le risque comptent aussi.'),
    'mkt-g10': dict(
        axes='Six étapes dans l\'ordre, de gauche à droite.',
        lecture=['S : analyser la situation (PESTEL, Porter, SWOT).', 'O : fixer des objectifs SMART.', 'S : choisir la stratégie (segmentation, ciblage, positionnement).', 'T : définir les tactiques (4P).', 'A : agir (force de vente).', 'C : contrôler (écarts, retour sur investissement).'],
        mecanisme='Chaque étape découle de la précédente : on ne fixe pas d\'objectifs sans diagnostic, ni de tactiques sans stratégie. Le contrôle ramène au diagnostic suivant.',
        exemple='Objectif SMART : « +5 points de part de marché sur les 18-25 ans en 12 mois » (spécifique, mesurable, ambitieux, réaliste, temporel).',
        retenir=['SOSTAC = Situation, Objectifs, Stratégie, Tactiques, Actions, Contrôle.', 'Stratégie = segmentation, ciblage, positionnement ; tactiques = 4P.'],
        piege='Confondre stratégie (qui viser, quelle image) et tactiques (produit, prix, distribution, communication).'),
}


def render(e):
    h = f'<div class="gx"><div class="gx-l">📐 Ce que montrent les axes</div><p>{e["axes"]}</p>'
    h += '<div class="gx-l">👀 Comment lire le graphique</div><ol>' + ''.join(f'<li>{x}</li>' for x in e['lecture']) + '</ol>'
    h += f'<div class="gx-l">⚙️ Le mécanisme</div><p>{e["mecanisme"]}</p>'
    if e.get('exemple'):
        h += f'<div class="gx-l">🧮 Exemple chiffré</div><p>{e["exemple"]}</p>'
    h += '<div class="gx-r"><div class="gx-l">✅ À retenir pour l\'examen</div><ul>' + ''.join(f'<li>{x}</li>' for x in e['retenir']) + '</ul></div>'
    if e.get('piege'):
        h += f'<div class="gx-p">⚠️ Piège : {e["piege"]}</div>'
    return h + '</div>'


def apply(mats):
    missing = []
    for m in mats:
        for g in m.get('courbes', []):
            if g['id'] in EXP:
                g['exp'] = render(EXP[g['id']])
            else:
                missing.append(g['id'])
    return missing
