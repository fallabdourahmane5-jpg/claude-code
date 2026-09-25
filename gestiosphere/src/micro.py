"""Matière : Microéconomie (13 documents : intro, chapitre 1 en 6 fichiers, chapitre 2 en 3 séances, 3 dossiers de TD)."""
import math
from lib import Cours, table, ul, ol, P, H3, H4, NOTE, WARN, FORM, fr
from svg import Plot, COL

SRC_INTRO = 'Intro — Cours magistral de microéconomie (33 diapos)'
SRC_C1 = ['Chap 1 (1) — contrainte budgétaire (27 diapos)', 'Séance 2 — utilité, préférences, courbes d\'indifférence (29)', 'Séance 3 — TMS, optimum (33)', 'Séance 4 — optimum, Lagrangien, cas particuliers, demande (29)', 'Séance 5 — élasticités, variations de prix et de revenu (44)', 'Séance 6 — consommation-revenu, Engel, effets de Hicks (34)']
SRC_C2 = ['Séance 7 — facteurs, fonction de production, productivités, rendements, TMST (40)', 'Séance 8 — isocoûts, minimisation du coût (26)', 'Séance 9 — sentier d\'expansion, demande de facteurs, coûts (41)']
SRC_TD = ['Dossier TD consommateur (TD 1 à 3)', 'Dossier TD producteur (TD 1 et 2)', 'TD sur les élasticités']
DOCS = [SRC_INTRO] + SRC_C1 + SRC_C2 + SRC_TD


def ch0():
    c = Cours()
    c.sec('I. Qu\'est-ce que la microéconomie ?')
    c.p('Cadre conceptuel qui permet de mieux comprendre certains faits économiques. La micro s\'intéresse aux <b>comportements des agents</b> (le consommateur et le producteur) et à la manière dont ils prennent leurs décisions.')
    c.df('Microéconomie', 'Analyse des choix et des comportements des agents individuels (consommateurs, producteurs) ; elle adopte la démarche de l\'individualisme méthodologique.')
    c.df('Macroéconomie', 'Analyse des agrégats économiques qui gomme la diversité des comportements en recourant à un agent représentatif.')
    c.f('Demande totale = Σ demandes individuelles · Offre totale = Σ offres individuelles')
    c.h3('Deux hypothèses fondamentales')
    c.df('Principe de rationalité', 'Les agents ont des objectifs bien déterminés qu\'ils cherchent à atteindre au mieux en respectant les contraintes qui limitent leurs choix ; la micro ne s\'interroge pas sur l\'origine de ces objectifs.')
    c.p('C\'est la question de l\'<b>allocation des ressources rares sous contraintes</b> avec un objectif de maximisation.')
    c.df('Échange marchand', 'Échange au prix du marché, volontaire et mutuellement avantageux.')
    c.df('Marché', 'Mécanisme qui assure la confrontation, à un moment donné, de l\'offre et de la demande d\'un bien ou d\'un service et conduit à la détermination d\'un prix.')

    c.sec('II. La concurrence pure et parfaite (CPP)')
    c.p('Cinq hypothèses : les trois premières définissent une concurrence <b>pure</b>, les deux dernières la rendent <b>parfaite</b>.')
    c.df('Atomicité des acteurs', 'Nombre d\'offreurs et de demandeurs très élevé : l\'offre ou la demande de chaque agent est négligeable, chacun est preneur de prix (price taker).')
    c.df('Homogénéité des produits', 'Les biens échangés sur un marché sont interchangeables : les consommateurs sont indifférents à l\'identité du vendeur ; un marché par nature de bien.')
    c.df('Libre entrée et libre sortie', 'Chaque agent peut entrer sur le marché et en sortir à tout moment sans coût : pas de barrières (brevets, investissements élevés ou spécifiques, lois, frais de résiliation).')
    c.df('Transparence de l\'information', 'L\'information nécessaire aux choix des agents est librement disponible et connue de tous.')
    c.df('Mobilité parfaite des facteurs', 'Libre circulation du capital et du travail, qui assure une allocation efficace des moyens de production.')

    c.sec('III. Offre, demande et équilibre')
    c.df('Courbe de demande', 'Quantité que les acheteurs sont disposés à acheter pour chaque niveau de prix, toutes choses égales par ailleurs ; pour la plupart des biens, la demande diminue avec le prix.')
    c.df('Courbe d\'offre', 'Quantité que les vendeurs sont disposés à vendre pour chaque niveau de prix, toutes choses égales par ailleurs ; l\'offre augmente avec le prix.')
    c.p('Deux grands types d\'acteurs : les <b>demandeurs</b> (ménages, entreprises) et les <b>offreurs</b> (entreprises, travailleurs).')
    c.p('Autres variables que le prix qui déplacent la <b>demande</b> : le revenu des demandeurs, le prix des autres biens. Pour l\'<b>offre</b> : les coûts de production (prix des matières premières, salaires).')
    c.tab(['', 'Courbe de demande', 'Courbe d\'offre'], [['Seul le prix du bien varie', 'Déplacement <b>le long</b> de la courbe', 'Déplacement <b>le long</b> de la courbe'], ['Une autre variable que le prix change', 'Déplacement <b>de</b> la courbe', 'Déplacement <b>de</b> la courbe']])
    c.df('Mécanisme de marché', 'Ajustement des prix jusqu\'à l\'équilibre : au-dessus de P*, excès d\'offre qui fait baisser le prix ; en dessous, excès de demande qui le fait monter.')
    c.df('Équilibre de marché', 'Prix P* et quantité Q* pour lesquels l\'offre est égale à la demande.')
    c.sec('IV. Organisation du cours')
    c.ul(['Cours magistral de 27 h (9 séances de 3 h) et TD de 12 h (8 séances de 1 h 30).', 'Deux contrôles continus en amphi (CC1 vers mi-novembre, CC2 début janvier) et deux interrogations de 30 minutes en TD.', 'Moyenne = 0,5 × [0,5 × CC1 + 0,5 × TD] + 0,5 × CC2.',
          'Plan : chapitre 1, théorie du consommateur (utilité, préférences, TMS, optimum, demande et effets de substitution et de revenu) ; chapitre 2, théorie du producteur (production, TMST, minimisation du coût, sentier d\'expansion, coûts).'])
    c.warn('Attention : ces documents sont marqués « Licence 2 — S3 » (Université de Lille). Ils ont été intégrés tels quels à ton programme de L3.')
    return c


def ch1():
    c = Cours()
    c.sec('Introduction : le consommateur et les biens')
    c.df('Consommateur', 'Agent économique (personne seule, foyer, ménage, communauté) qui acquiert et consomme des biens et services grâce à un revenu donné, pour en retirer une satisfaction.')
    c.p('Question centrale : <b>quelle quantité de biens consommer pour maximiser sa satisfaction compte tenu de son budget ?</b>')
    c.df('Biens divisibles', 'Biens qui peuvent être achetés exactement dans la quantité souhaitée ; en microéconomie, on suppose les biens divisibles.')
    c.df('Panier de consommation', 'Combinaison de quantités de biens (x1 ; x2) ; il en existe une infinité.')
    c.p('Le consommateur peut <b>classer</b> tous les paniers : A ≻ B (A strictement préféré), A ≺ B, A ~ B (indifférence). Hypothèse de <b>non-satiété</b>.')

    c.sec('0. La contrainte budgétaire')
    c.df('Contrainte budgétaire', 'Le consommateur ne peut pas dépenser plus que son revenu : D = p1x1 + p2x2 ≤ R.')
    c.df('Droite de budget', 'Ensemble des paniers pour lesquels la dépense égale exactement le revenu : R = p1x1 + p2x2.')
    c.f('x2 = R/p2 − (p1/p2) · x1 · ordonnée à l\'origine R/p2 · abscisse à l\'origine R/p1 · pente = −p1/p2')
    c.df('Prix relatif (pente en valeur absolue)', 'p1/p2 : valeur du bien 1 exprimée en unités de bien 2 du point de vue du marché ; pour 1 unité de plus de bien 1, il faut renoncer à p1/p2 unités de bien 2.')
    c.ex('Exercice du cours (R = 100, p1 = 2, p2 = 5)', ul(['Contrainte : 2x1 + 5x2 ≤ 100 ; droite : x2 = 20 − 0,4 x1.', 'Intersections : (0 ; 20) et (50 ; 0).', 'P1 (10 ; 20) : D = 120 > 100, inaccessible. P2 (10 ; 5) : D = 45 < 100, accessible (avec x1 = 10, on peut aller jusqu\'à x2 = 16).', 'Pente en valeur absolue 0,4 : 1 unité de bien 1 vaut 0,4 unité de bien 2 sur le marché.']))
    c.p('Effets sur la droite : une hausse de <b>R</b> la déplace parallèlement vers l\'extérieur ; une hausse de <b>p1</b> la fait pivoter autour de R/p2 (l\'abscisse R/p1 recule) ; une hausse de <b>p2</b> la fait pivoter autour de R/p1.')

    c.sec('1. Les notions d\'utilité')
    c.df('Utilité', 'Satisfaction qu\'un agent retire de la consommation d\'un panier de biens.')
    c.df('Fonction d\'utilité', 'Relation U(x1 ; x2) qui associe un niveau d\'utilité à chaque panier ; pour chaque bien, elle est croissante à taux décroissant (dérivée première positive, dérivée seconde négative).')
    c.h3('A. Deux interprétations de l\'utilité')
    c.df('Utilité cardinale', 'Mesure quantitative de la satisfaction : si l\'utilité d\'un panier est le double de celle d\'un autre, il est préféré deux fois plus.')
    c.p('Exemple du cours (U = x1·√x2) : panier 1 (3 ; 9) → U = 3 × 3 = 9 ; panier 2 (9 ; 4) → U = 9 × 2 = 18, soit +100 % : l\'agent « préfère deux fois plus » le second panier. <b>Limites</b> : l\'utilité est subjective et abstraite, impossible à mesurer avec précision ; le consommateur veut seulement trouver le meilleur panier, pas mesurer des écarts.')
    c.df('Utilité ordinale', 'Indice relatif qui sert seulement à classer les paniers : U(A) > U(B) signifie seulement que A est préféré à B.')
    c.p('Plusieurs fonctions d\'utilité représentent le même ordre de préférence : une fonction d\'utilité est définie <b>à une transformation monotone croissante près</b> (ex. U = x1<sup>0,5</sup>x2<sup>0,5</sup> et V = 20 x1<sup>0,5</sup>x2<sup>0,5</sup> + 20).')
    c.h3('B. L\'utilité marginale')
    c.df('Utilité marginale', 'Satisfaction supplémentaire obtenue par la consommation d\'une unité supplémentaire d\'un bien, toutes choses égales par ailleurs : Um1 = ∂U/∂x1.')
    c.p('L\'utilité marginale est généralement <b>positive</b> (l\'utilité totale croît) et <b>décroissante</b> (l\'utilité totale croît à taux décroissant).')

    c.sec('2. Les préférences')
    c.h3('A. Quatre hypothèses')
    c.df('Complétude', 'Le consommateur est capable de comparer tous les paniers de biens : l\'ordre de préférence est complet.')
    c.df('Transitivité', 'Si A ≻ B et B ≻ C, alors A ≻ C (idem pour ~) : hypothèse de cohérence des préférences.')
    c.df('Monotonie', 'Non-satiété : plus l\'agent dispose de biens, plus sa satisfaction est élevée.')
    c.df('Convexité des préférences', 'Goût pour la diversité : l\'agent préfère les paniers diversifiés aux paniers « extrêmes ».')
    c.h3('B-C. Courbes et cartes d\'indifférence')
    c.df('Courbe d\'indifférence (CI)', 'Ensemble des paniers qui procurent au consommateur la même satisfaction (isoquant d\'utilité).')
    c.df('Carte d\'indifférence', 'Ensemble des courbes d\'indifférence d\'un consommateur ; plus une CI est éloignée de l\'origine, plus l\'utilité est élevée.')
    c.h3('D. Forme des courbes d\'indifférence')
    c.tab(['Propriété', 'Hypothèse qui la justifie'], [['Plus elles sont éloignées de l\'origine, plus l\'utilité est élevée', 'Monotonie'], ['Pente négative (substitution entre les biens)', 'Monotonie (non-satiété)'], ['Convexes', 'Convexité (goût pour la diversité)'], ['Ne se croisent pas', 'Transitivité']])
    c.h3('E. Cas particuliers')
    c.df('Biens parfaitement substituables', 'Biens substituables à taux fixe : les CI sont des droites (TMS constant).')
    c.df('Biens parfaitement complémentaires', 'Biens consommés dans des proportions fixes : les CI sont coudées, en forme de L.')

    c.sec('3. Le taux marginal de substitution (TMS)')
    c.df('Taux marginal de substitution (TMS)', 'Quantité de bien 2 à laquelle le consommateur est prêt à renoncer pour obtenir une unité supplémentaire de bien 1 en gardant sa satisfaction constante ; c\'est la valeur du bien 1 exprimée en bien 2.')
    c.f('Définition 1 : TMS = −Δx2/Δx1 = − pente de la CI (valeur absolue de la pente)<br>Définition 2 : TMS = Um1 / Um2')
    c.p('Démonstration : le long d\'une CI, dU = Um1·dx1 + Um2·dx2 = 0, donc −dx2/dx1 = Um1/Um2.')
    c.ul(['Exemple : pour 1 unité de bien 1 en plus, il faut renoncer à 0,5 unité de bien 2 → TMS = −(−0,5/1) = 0,5.',
          'Lecture inverse : TMS = 0,6 signifie aussi que l\'agent veut récupérer 0,6 unité de bien 2 s\'il renonce à 1 unité de bien 1.',
          '<b>TMS décroissant</b> le long d\'une CI : c\'est ce qui rend la CI convexe.'])
    c.ex('Exemples du cours', '<p>U = x1<sup>0,5</sup>x2<sup>0,5</sup> : Um1 = 0,5 x1<sup>−0,5</sup>x2<sup>0,5</sup>, Um2 = 0,5 x1<sup>0,5</sup>x2<sup>−0,5</sup>, donc <b>TMS = x2/x1</b>. Panier A (4 ; 9) : U = 6, TMS = 2,25. Panier B (36 ; 1) : U = 6, TMS = 0,028. Avec U = 20 x1<sup>0,5</sup>x2<sup>0,5</sup> + 20, le TMS est le même (x2/x1) : A (16 ; 9) U = 260, TMS = 0,5625.</p>')

    c.sec('4. L\'optimum du consommateur')
    c.p('Le consommateur maximise son utilité sous contrainte budgétaire. Le panier optimal doit (1) <b>appartenir à la droite de budget</b> (pas d\'épargne ni d\'emprunt) et (2) être sur la <b>CI la plus éloignée possible</b> de l\'origine.')
    c.h3('A. Approche graphique')
    c.df('Optimum du consommateur', 'Panier situé au point de tangence entre la droite de budget et la courbe d\'indifférence la plus haute possible : TMS = p1/p2.')
    c.f('À l\'optimum : TMS = p1/p2 (pente de la CI = pente de la droite de budget)')
    c.ul(['<b>TMS > p1/p2</b> (ex. 0,7 contre 0,5) : l\'agent est prêt à céder 0,7 unité de bien 2 mais le marché n\'en demande que 0,5. Il échange : plus de bien 1, moins de bien 2, et son utilité augmente jusqu\'à l\'égalité.',
          '<b>TMS < p1/p2</b> (ex. 0,3 contre 0,5) : lecture inverse, il cède du bien 1 pour récupérer 0,5 unité de bien 2 alors que 0,3 lui suffisait. Il consomme moins de bien 1 et plus de bien 2.'])
    c.h3('B. Approche mathématique')
    c.f('Programme : Max U(x1 ; x2) sous contrainte R = p1x1 + p2x2')
    c.df('Lagrangien', 'Fonction à trois variables L(x1 ; x2 ; λ) = U(x1 ; x2) + λ(R − p1x1 − p2x2) dont on annule les dérivées partielles pour trouver l\'optimum sous contrainte.')
    c.f('CPO : ∂L/∂x1 = Um1 − λp1 = 0 · ∂L/∂x2 = Um2 − λp2 = 0 · ∂L/∂λ = R − p1x1 − p2x2 = 0<br>⇒ Um1/p1 = Um2/p2 (= λ) ⇔ Um1/Um2 = p1/p2')
    c.p('Conditions du second ordre : supposées vérifiées ; les CPO sont nécessaires et suffisantes quand les CI sont convexes. <b>Méthode 2</b> : résoudre directement le système { TMS = p1/p2 ; R = p1x1 + p2x2 }.')
    c.ex('Exemples du cours', '<p>1) U = x1<sup>0,5</sup>x2<sup>0,5</sup>, R = 100, p1 = 2, p2 = 5 : x2/x1 = 0,4 ⇒ 100 − 2x1 − 2x1 = 0 ⇒ <b>x1 = 25, x2 = 10</b>.</p><p>2) U = x1<sup>0,25</sup>x2<sup>0,75</sup>, R = 400, p1 = 10, p2 = 20 : TMS = x2/(3x1) = 0,5 ⇒ x2 = 1,5x1 ⇒ 400 = 10x1 + 30x1 ⇒ <b>x1 = 10, x2 = 15</b>.</p>')
    c.note('Avec U = x1<sup>a</sup>x2<sup>b</sup>, l\'agent consacre la part a/(a+b) de son revenu au bien 1 : x1 = a/(a+b) · R/p1 et x2 = b/(a+b) · R/p2. C\'est un bon moyen de vérifier un résultat.')
    c.h3('C. Cas particuliers')
    c.df('Solution en coin', 'Optimum où l\'agent ne consomme qu\'un seul des deux biens : TMS ≠ p1/p2 à l\'extrémité de la droite de budget.')
    c.ul(['Substituts parfaits (CI droites) : si p1/p2 = TMS, tous les paniers de la droite de budget sont optimaux ; si p1/p2 < TMS, l\'agent ne consomme que du bien 1 ; si p1/p2 > TMS, que du bien 2.', 'Compléments parfaits (CI en L) : l\'optimum est au coin de la CI, dans la proportion fixe.'])

    c.sec('5. Fonction de demande, variation du prix et du revenu')
    c.h3('A. La fonction de demande')
    c.df('Fonction de demande', 'Expression des quantités optimales en fonction des prix et du revenu : elle donne tous les paniers optimaux ; en tout point de la courbe de demande, l\'agent maximise son utilité.')
    c.ex('Exemple du cours', '<p>TMS = x2/(2x1). À l\'optimum : x2 = 2(p1/p2)x1, donc R = 3p1x1 ⇒ <b>x1 = R/(3p1)</b> et <b>x2 = 2R/(3p2)</b>. Avec R = 120 : x1 = 40/p1, x2 = 80/p2 ; pour p1 = 5 et p2 = 8, le panier optimal est (8 ; 10).</p>')
    c.h3('Rappel : les élasticités')
    c.df('Élasticité', 'Pourcentage de variation d\'une variable suite à une variation de 1 % d\'une autre variable.')
    c.f('E(y/x) = Δy% / Δx% = (Δy/Δx) · (x/y) → (∂y/∂x) · (x/y)')
    c.ul(['Ex. : x : 2 → 4, y : 10 → 14 ⇒ E = 20 % / 100 % = 0,4.', 'y = 2x + 6 en x = 2 (y = 10) : E = 2 × 2/10 = 0,4. y = −5x + 20 en x = 2 : E = −5 × 2/10 = −1.'])
    c.df('Élasticité-prix directe', 'Variation en % de la quantité demandée d\'un bien suite à une hausse de 1 % de son propre prix ; en général négative.')
    c.p('Exemple : x = −20p + 1000 en p = 25 (x = 500) : E = −20 × 25/500 = −1. Entre −1 et 1, la demande est <b>inélastique</b> (courbe très verticale) ; au-delà, elle est <b>élastique</b> (courbe très aplatie).')
    c.tab(['Élasticité-prix directe', 'Type de bien'], [['E < 0', 'Bien ordinaire'], ['E > 0', 'Bien de Giffen, effet Veblen']])
    c.df('Bien de Giffen', 'Bien inférieur dont la demande augmente quand son prix augmente, parce que l\'effet revenu l\'emporte sur l\'effet de substitution.')
    c.df('Effet Veblen', 'Hausse de la demande d\'un bien quand son prix augmente, parce que le prix élevé signale un statut (consommation ostentatoire).')
    c.df('Élasticité-revenu', 'Variation en % de la quantité demandée suite à une hausse de 1 % du revenu : E = (∂x/∂R) · (R/x).')
    c.p('Exemples : R 100 → 130 (+30 %), x 4 → 6 (+50 %) ⇒ E = 1,67. Pour x = R/(3p), l\'élasticité-revenu vaut toujours 1.')
    c.tab(['Élasticité-revenu', 'Type de bien'], [['E < 0', 'Bien inférieur'], ['E > 0', 'Bien normal'], ['0 < E < 1', 'Bien de première nécessité'], ['E > 1', 'Bien de luxe (supérieur)']])
    c.p('Illustration : quand le revenu passe de 20 à 60, l\'alimentation passe de 15 à 30 (première nécessité) et le cinéma de 5 à 30 (luxe).')
    c.df('Élasticité-prix croisée', 'Variation en % de la quantité demandée d\'un bien suite à une hausse de 1 % du prix d\'un autre bien : positive pour des substituts, négative pour des compléments.')
    c.p('Exemple : py 5 → 8 (+60 %), x 5 → 6 (+20 %) ⇒ E = 0,33 : biens substituables.')
    c.tab(['', 'La demande augmente', 'La demande diminue'], [['Le prix du bien augmente', 'Biens de Giffen, effet Veblen', 'Biens ordinaires'], ['Le revenu augmente', 'Biens normaux (première nécessité, luxe)', 'Biens inférieurs'], ['Le prix d\'un autre bien augmente', 'Biens substituables', 'Biens complémentaires']])
    c.h3('B. Variation du prix et du revenu')
    c.df('Courbe de consommation-prix', 'Lieu des paniers optimaux quand le prix d\'un bien varie (revenu et autre prix constants) ; elle permet de déduire la courbe de demande.')
    c.p('Exemple du cours : R = 20, p2 = 2, p1 = 2 → 1 → 0,5 : les droites de budget pivotent, les optimums A, B, C forment la courbe de consommation-prix ; en reportant (x1 ; p1) on obtient la courbe de demande du bien 1. Le long de la courbe de demande, l\'agent maximise son utilité (TMS = p1/p2), mais son niveau d\'utilité change.')
    c.df('Courbe de consommation-revenu', 'Lieu des paniers optimaux quand le revenu varie (prix constants) ; chaque hausse de revenu déplace la courbe de demande.')
    c.p('Exemple : p1 = 1, p2 = 2, R = 10 → 20 → 30 : optimums A, B, C. Pour un <b>bien inférieur</b>, la courbe de consommation-revenu revient vers l\'axe du bien concerné.')
    c.df('Courbe d\'Engel', 'Courbe qui relie la quantité consommée d\'un bien au revenu de l\'agent (une courbe par bien) ; croissante pour un bien normal, décroissante pour un bien inférieur.')
    c.h3('C. Effet de substitution et effet de revenu')
    c.df('Effet-prix (effet total)', 'Variation de la quantité demandée d\'un bien suite à la variation de son prix ; il se décompose en effet de substitution et effet de revenu (décomposition de Hicks).')
    c.df('Effet de substitution (ES)', 'Variation de la demande liée à la seule variation des prix relatifs, à utilité constante : le bien devenu relativement moins cher est davantage consommé.')
    c.df('Effet de revenu (ER)', 'Variation de la demande liée à la variation du pouvoir d\'achat provoquée par la variation de prix (le revenu nominal est inchangé).')
    c.p('Exemple : avec 100 € et un bien à 10 €, le pouvoir d\'achat est de 10 unités ; si le prix passe à 5 €, il est de 20 unités alors que le revenu nominal n\'a pas changé.')
    c.df('Méthode de Hicks', 'Décomposition en trois paniers : initial (prix et revenu initiaux), intermédiaire (nouveaux prix, utilité initiale, revenu « compensé » R\'), final (nouveaux prix, revenu initial). ES = initial → intermédiaire ; ER = intermédiaire → final.')
    c.tab(['Situation', 'Droite de budget', 'Rapport des prix'], [['Initiale', 'R/p1 ; R/p2', 'p1/p2'], ['« Intermédiaire »', 'R\'/p1\' ; R\'/p2 (tangente à la CI initiale)', 'p1\'/p2'], ['Finale', 'R/p1\' ; R/p2', 'p1\'/p2']])
    c.tab(['Si p1 diminue', 'Effet sur x1', 'Effet sur x2'], [['ES', 'Hausse', 'Baisse'], ['ER (biens normaux)', 'Hausse', 'Hausse'], ['ET', 'Hausse : bien ordinaire', 'Hausse si ER > ES, baisse si ER < ES']])
    c.p('<b>Bien inférieur</b> (bien 1), toujours si p1 diminue : ES en hausse, ER en baisse. Si ER > ES, x1 baisse : c\'est un <b>bien de Giffen</b>. Si ER < ES, c\'est un bien ordinaire (mais inférieur).')
    c.ex('Exemple chiffré du cours', '<p>U = x1<sup>0,25</sup>x2<sup>0,75</sup>, R = 1 000, p2 = 2, p1 passe de 10 à 5. Initial : (25 ; 375). Final : (50 ; 375). Intermédiaire (même utilité, p1/p2 = 2,5) : (42 ; 315).</p>' +
         table(['', 'x1', 'x2'], [['ES', '+17', '−60'], ['ER', '+8', '+60'], ['ET', '+25', '0']]) + '<p>ER > 0 : biens normaux ; le bien 1 est un bien ordinaire ; pour x2, ER = ES en valeur absolue : les biens sont indépendants (la demande de bien 2 ne dépend pas de p1).</p>')
    c.p('Pour déterminer les deux effets selon Hicks : (1) panier optimal initial ; (2) panier final (nouveaux prix, revenu initial) ; (3) panier intermédiaire à partir de l\'utilité initiale et des nouveaux prix (revenu indéterminé).')
    return c


def ch2():
    c = Cours()
    c.sec('Introduction : le producteur')
    c.df('Production', 'Opération qui transforme certains biens et services existants (inputs) en d\'autres biens et services (output).')
    c.df('Entreprise', 'Agent qui organise l\'activité de production et en tire un profit ; contrairement au consommateur, elle fabrique avant de vendre.')
    c.df('Technologie de production', 'Façon dont les inputs (intrants, facteurs de production) sont transformés en output (extrant) ; les inputs génèrent des coûts.')
    c.p('Contraintes : la technologie et les prix (facteurs et bien produit). <b>Objectif</b> : trouver la combinaison de facteurs qui minimise le coût de production, puis la quantité à produire qui maximise le profit.')

    c.sec('1. Activité de production, facteurs et fonction de production')
    c.h3('Les facteurs de production')
    c.p('Trois types d\'inputs : <b>travail</b>, <b>matières premières</b>, <b>capital</b>.')
    c.df('Facteur fixe', 'Facteur dont la quantité ne varie pas (à court terme).')
    c.df('Facteur variable', 'Facteur dont la quantité varie avec le niveau de production ; à long terme, tous les facteurs sont variables.')
    c.df('Facteurs substituables', 'Facteurs qui peuvent se remplacer l\'un l\'autre en maintenant la production.')
    c.df('Facteurs complémentaires', 'Facteurs combinés dans des proportions fixes.')
    c.df('Fonction de production', 'Relation technique y = f(K, L) qui donne, pour chaque combinaison d\'inputs, le niveau maximal d\'output.')
    c.h3('Productivités')
    c.df('Productivité moyenne (PM)', 'Quantité produite par unité d\'input : PML = f(K, L)/L ; PMK = f(K, L)/K.')
    c.df('Productivité marginale (Pm)', 'Accroissement de la production dû à l\'utilisation d\'une unité supplémentaire d\'un facteur, toutes choses égales par ailleurs : PmL = Δf/ΔL → ∂f/∂L.')
    c.warn('Notation du cours : <b>PML</b> = productivité <b>moyenne</b>, <b>PmL</b> = productivité <b>marginale</b> (m minuscule = marginal).')
    c.tab(['L', 'K', 'y', 'PML (moyenne)', 'PmL (marginale)'], [[0, 10, 0, '—', '—'], [1, 10, 10, 10, 10], [2, 10, 30, 15, 20], [3, 10, 60, 20, 30], [4, 10, 80, 20, 20], [5, 10, 94, '18,80', 14], [6, 10, 103, '17,17', 9], [7, 10, 107, '15,29', 4], [8, 10, 107, '13,38', 0], [9, 10, 104, '11,56', -3]], num_cols=(0, 1, 2, 3, 4))
    c.p('Deux propriétés de la productivité marginale : elle est <b>positive</b> a priori, et elle obéit à la <b>loi des rendements marginaux décroissants</b>.')
    c.df('Loi des rendements marginaux décroissants', 'Au-delà d\'un certain seuil, chaque unité supplémentaire d\'un facteur variable (l\'autre étant fixe) accroît de moins en moins la production.')
    c.p('Graphiquement, la PmL coupe la PML <b>en son maximum</b> : tant que PmL > PML, la moyenne augmente ; quand PmL < PML, elle diminue.')
    c.h3('Les rendements d\'échelle')
    c.df('Rendements d\'échelle', 'Taux auquel la production augmente quand toutes les quantités de facteurs augmentent dans la même proportion (analyse de long terme).')
    c.f('Pour λ > 1 : f(λz1, …, λzn) > λf(z) → croissants · = λf(z) → constants · < λf(z) → décroissants')
    c.note('Pour y = K<sup>α</sup>L<sup>β</sup> : f(λK, λL) = λ<sup>α+β</sup>y. Rendements croissants si α + β > 1, constants si = 1, décroissants si < 1.')

    c.sec('2. Isoquantes et TMST')
    c.df('Isoquante', 'Courbe qui relie toutes les combinaisons de facteurs permettant d\'obtenir le même niveau de production ; un ensemble d\'isoquantes forme une carte d\'isoquantes.')
    c.p('Exemple du cours : (L ; K) = (1 ; 5), (2 ; 3), (3 ; 2), (5 ; 1) produisent tous 100. Propriétés : isoquantes <b>décroissantes</b> et <b>convexes</b> ; la production augmente en s\'éloignant de l\'origine.')
    c.df('Taux marginal de substitution technique (TMST)', 'Réduction de la quantité de capital qui permet de maintenir la production constante quand on utilise une unité de travail en plus.')
    c.f('Définition 1 : TMST = −ΔK/ΔL = − pente de l\'isoquante<br>Définition 2 : TMST = PmL / PmK')
    c.p('Démonstration : le long d\'une isoquante, dy = PmK·dK + PmL·dL = 0, donc −dK/dL = PmL/PmK. Le TMST est décroissant (diminution de K de plus en plus faible), d\'où la convexité.')
    c.ul(['Facteurs parfaitement substituables : isoquantes droites.', 'Fonction de production à proportions fixes : isoquantes en L.'])

    c.sec('3. Minimisation du coût de production')
    c.df('Droite d\'isocoût', 'Ensemble des combinaisons de capital et de travail qui coûtent le même montant : C = pK·K + pL·L ; équivalent de la droite de budget.')
    c.f('K = C/pK − (pL/pK) · L · pente = −pL/pK')
    c.p('La pente en valeur absolue pL/pK est la valeur relative du travail par rapport au capital du point de vue du marché (si elle vaut 2, 1 unité de travail vaut 2 unités de capital).')
    c.ex('Illustration du cours', '<p>y = K<sup>0,5</sup>L<sup>0,5</sup>, on veut y = 10 avec pK = 1 € et pL = 2 € : (K = 1 ; L = 100) coûte 201 € ; (2 ; 50) coûte 102 € ; (10 ; 10) coûte 30 €. Toutes produisent 10 : il faut trouver la moins chère.</p>')
    c.h3('Approche graphique')
    c.df('Combinaison optimale de facteurs', 'Point de tangence entre l\'isoquante du niveau de production voulu et la droite d\'isocoût la plus proche de l\'origine : TMST = pL/pK.')
    c.h3('Approche mathématique')
    c.f('Min C = pK·K + pL·L sous contrainte y = f(K, L)<br>L(K, L, λ) = pK·K + pL·L + λ(ȳ − f(K, L))<br>CPO : pK = λ·PmK · pL = λ·PmL · ȳ = f(K, L) ⇒ PmL/PmK = pL/pK')
    c.p('Les CPO sont nécessaires et suffisantes quand les isoquantes sont strictement convexes. Système à résoudre : { TMST = pL/pK ; f(K, L) = ȳ }.')
    c.ex('Exemple du cours', '<p>y = K<sup>0,5</sup>L<sup>0,5</sup>, ȳ = 10, pK = 1, pL = 2 : TMST = K/L = 2 ⇒ K = 2L (L = K/2) ; 10 = (2L)<sup>0,5</sup>L<sup>0,5</sup> = √2·L ⇒ <b>L = 7,07 ; K = 14,14</b> ; coût minimal ≈ 28,28 €.</p><p>Autre exemple : y = K<sup>0,4</sup>L<sup>0,4</sup>, pK = 25, pL = 16, y = 100 : Min C = 25K + 16L sous 100 = K<sup>0,4</sup>L<sup>0,4</sup>.</p>')

    c.sec('4. Sentier d\'expansion et fonction de demande de facteurs')
    c.df('Sentier (chemin) d\'expansion', 'Courbe qui relie les combinaisons de facteurs qui minimisent le coût pour chaque niveau d\'output ; son équation K = f(L) découle de TMST = pL/pK.')
    c.p('Exemple : y = K<sup>0,5</sup>L<sup>0,5</sup>, pK = 1, pL = 2 ⇒ TMST = K/L = 2 ⇒ sentier <b>K = 2L</b>.')
    c.df('Fonction de demande de facteurs', 'Quantité de chaque facteur qui minimise le coût en fonction des prix des facteurs et de la quantité produite (une fonction par facteur).')
    c.p('Exemple : K = 2y/2<sup>0,5</sup> = √2·y et L = y/2<sup>0,5</sup> = y/√2.')

    c.sec('5. Les coûts')
    c.h3('Les coûts de court terme')
    c.p('À court terme, certains facteurs sont fixes. D\'où deux catégories de coûts :')
    c.df('Coût fixe (CF)', 'Coût qui ne varie pas avec le niveau de production et ne peut être éliminé qu\'en cessant l\'activité.')
    c.df('Coût variable (CV)', 'Coût qui varie avec le niveau de production.')
    c.df('Coût moyen (CM)', 'Coût total par unité produite : CM = C/y = CVM + CFM.')
    c.df('Coût marginal (Cm)', 'Coût de production d\'une unité supplémentaire : Cm = ΔC/Δy = ΔCV/Δy → ∂C/∂y.')
    c.f('C = CV + CF · CM = C/y = CVM + CFM · CVM = pL/PML · Cm = pL/PmL')
    c.tab(['y', 'CF', 'CV', 'CT', 'CM', 'CFM', 'CVM', 'Cm'], [[1, 50, 50, 100, 100, 50, 50, 50], [2, 50, 78, 128, 64, 25, 39, 28], [3, 50, 98, 148, '49,3', '16,7', '32,7', 20], [4, 50, 112, 162, '40,5', '12,5', 28, 14], [5, 50, 130, 180, 36, 10, 26, 18],
                                                                    [6, 50, 150, 200, '33,3', '8,3', 25, 20], [7, 50, 175, 225, '32,1', '7,1', 25, 25], [8, 50, 204, 254, '31,8', '6,3', '25,5', 29], [9, 50, 242, 292, '32,4', '5,6', '26,9', 38], [10, 50, 300, 350, 35, 5, 30, 58], [11, 50, 385, 435, '39,5', '4,5', 35, 85]], num_cols=tuple(range(8)))
    c.p('Relation coûts et productivité : quand la productivité marginale du travail augmente, le coût marginal baisse, et inversement. Le Cm coupe le CVM et le CM <b>en leur minimum</b>.')
    c.h3('Les coûts de long terme')
    c.df('Courbe de coût minimal (coût total de long terme)', 'Courbe qui relie, pour chaque niveau d\'output, le coût minimum de production ; elle contient la même information que le chemin d\'expansion.')
    c.p('Exemple : C = pK·K + pL·L = 1 × 2y/√2 + 2 × y/√2 = <b>4y/√2 = 2√2·y</b>. CM = C/y, Cm = ∂C/∂y.')
    c.tab(['Rendements d\'échelle', 'Coût total de long terme'], [['Croissants', 'Le coût augmente relativement moins vite que la production (courbe concave)'], ['Constants', 'Le coût augmente aussi vite que la production (droite)'], ['Décroissants', 'Le coût augmente relativement plus vite que la production (courbe convexe)']])
    c.p('À long terme, tous les facteurs sont variables : <b>C<sub>LT</sub> ≤ C<sub>CT</sub></b>. À court terme, on reste bloqué sur la quantité de capital fixée, en dehors du sentier d\'expansion.')
    c.h3('Prolongement : quelle quantité produire ?')
    c.df('Profit', 'Différence entre les recettes et les coûts de l\'entreprise : π = RT − C = p·y − C.')
    return c


def plot_budget_opt():
    p = Plot(55, 24, 'x1', 'x2').axes(xticks=[0, 10, 25, 50], yticks=[0, 10, 20])
    p.area([(0, 0), (0, 20), (50, 0)], COL[0], 0.1)
    p.fn(lambda x: 20 - 0.4 * x, 0, 50, color=COL[1], label='Droite de budget : x2 = 20 − 0,4 x1', lpos=(20, 13.5))
    for u, col in ((math.sqrt(250) * 0.6, '#4d5874'), (math.sqrt(250), COL[2]), (math.sqrt(250) * 1.35, '#4d5874')):
        p.fn(lambda x, u=u: u * u / x if x > 0 else None, 2, 55, color=col, width=1.8)
    p.point(25, 10, '#e8eaf2', 'Optimum (25 ; 10) : TMS = p1/p2 = 0,4', dx=6, dy=-10)
    p.dashes(25, 10)
    p.text(8, 3, 'Possible', COL[0], 11)
    return p.svg()


def plot_cpp():
    p = Plot(100, 100, 'Quantité', 'Prix unitaire').axes()
    p.fn(lambda q: 90 - 0.8 * q, 5, 100, color=COL[0], label='Demande', lpos=(88, 22))
    p.fn(lambda q: 10 + 0.8 * q, 0, 100, color=COL[1], label='Offre', lpos=(88, 82))
    p.point(50, 50, '#e8eaf2', 'E', dx=8, dy=4)
    p.dashes(50, 50, xl='Q*', yl='P*')
    p.curve([(25, 70), (75, 70)], '#f7e66a', 1.4, dash='3 3', label='Excès d\'offre (P > P*)', lpos=(26, 72))
    p.curve([(25, 30), (75, 30)], '#f76ab4', 1.4, dash='3 3', label='Excès de demande (P < P*)', lpos=(26, 24))
    return p.svg()


def plot_ci():
    p = Plot(10, 10, 'x1', 'x2').axes()
    for k, (u, lab) in enumerate(((6, 'CI1'), (12, 'CI2'), (20, 'CI3'))):
        p.fn(lambda x, u=u: u / x, u / 9.5, 9.6, color=[COL[0], COL[2], COL[1]][k], label=lab, lpos=(9.2, u / 9.6 + 0.3))
    p.arrow(3, 3, 5, 5)
    p.text(5.2, 5.4, 'utilité croissante', '#f7e66a', 10)
    p.curve([(1.5, 9), (2, 7), (3, 4), (4, 3)], '#e8eaf2', 0.001)
    p.point(2, 3, '#e8eaf2', 'A').point(3, 2, '#e8eaf2', 'B', dy=12)
    return p.svg()


def plot_substituts():
    p = Plot(10, 10, 'x1', 'x2', w=250, h=230, pad=(30, 10, 16, 36)).axes()
    for k in (3, 6, 9):
        p.curve([(0, k), (k, 0)], COL[2], 1.8)
    p.text(5, 9, 'Substituts parfaits', '#c4c9d8', 10)
    g1 = p.svg()
    q = Plot(10, 10, 'x1', 'x2', w=250, h=230, pad=(30, 10, 16, 36)).axes()
    for k in (2, 4, 6):
        q.curve([(k, 9.5), (k, k), (9.5, k)], COL[1], 1.8)
    q.text(5, 9, 'Compléments parfaits', '#c4c9d8', 10)
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">{g1}{q.svg()}</div>'


def plot_hicks():
    R, p2, p1, p1b = 1000, 2, 10, 5
    xs = 0.25 * R / p1
    ys = 0.75 * R / p2
    u0 = xs ** 0.25 * ys ** 0.75
    xi = u0 / 7.5 ** 0.75
    yi = 7.5 * xi
    xf = 0.25 * R / p1b
    yf = ys
    Rc = p1b * xi + p2 * yi
    uf = xf ** 0.25 * yf ** 0.75
    p = Plot(210, 520, 'x1', 'x2').axes(xticks=[0, 25, 42, 50, 100, 200], yticks=[0, 250, 500])
    p.curve([(0, R / p2), (R / p1, 0)], COL[1], 2, label='DB1 (p1 = 10)', lpos=(60, 150))
    p.curve([(0, R / p2), (R / p1b, 0)], COL[1], 2, label='DB2 (p1 = 5)', lpos=(150, 110))
    p.curve([(0, Rc / p2), (Rc / p1b, 0)], '#f7e66a', 1.5, dash='5 4', label='Droite compensée', lpos=(120, 90))
    p.fn(lambda x: (u0 / x ** 0.25) ** (1 / 0.75), 8, 205, color=COL[2], width=1.8, label='U initiale', lpos=(185, 250))
    p.fn(lambda x: (uf / x ** 0.25) ** (1 / 0.75), 14, 205, color=COL[0], width=1.8, label='U finale', lpos=(185, 400))
    p.point(xs, ys, '#e8eaf2', 'E (25 ; 375)', dx=-4, dy=-10, anchor='end')
    p.point(xi, yi, '#f7e66a', 'E\' (42 ; 315)', dx=6, dy=14)
    p.point(xf, yf, '#e8eaf2', 'E\'\' (50 ; 375)', dx=8, dy=-8)
    return p.svg()


def plot_prod():
    ys = [0, 10, 30, 60, 80, 94, 103, 107, 107, 104]
    p = Plot(9.5, 115, 'Travail L', 'y', h=250, pad=(40, 20, 20, 36)).axes(xticks=range(0, 10), yticks=[0, 50, 100])
    p.curve(list(enumerate(ys)), COL[0], label='Production totale', lpos=(6.5, 108))
    g1 = p.svg()
    q = Plot(9.5, 32, 'Travail L', '', h=250, pad=(40, 20, 20, 36), ymin=-5).axes(xticks=range(0, 10), yticks=[0, 10, 20, 30])
    pml = [(L, ys[L] / L) for L in range(1, 10)]
    pm = [(L, ys[L] - ys[L - 1]) for L in range(1, 10)]
    q.curve(pml, COL[2], label='PML (moyenne)', lpos=(7, 15))
    q.curve(pm, COL[1], label='PmL (marginale)', lpos=(6.2, 4))
    return f'<div style="display:grid;gap:4px">{g1}{q.svg()}</div>'


def plot_isocout():
    p = Plot(30, 30, 'L', 'K').axes(xticks=[0, 7.07, 14.14, 21.21], yticks=[0, 14.14, 28.28], fmt=lambda v: fr(v, 2) if v else '0')
    for y, col in ((10, COL[2]), (20, COL[0])):
        p.fn(lambda L, y=y: y * y / L, y * y / 29.5, 29.5, color=col, width=1.8, label=f'Isoquante y = {y}', lpos=(22, y * y / 22 + 1.2))
    for C in (20, 28.28, 40):
        p.curve([(0, C), (C / 2, 0)], '#8890a8' if C != 28.28 else COL[1], 1.3 if C != 28.28 else 2, dash=None if C == 28.28 else '4 3')
    p.fn(lambda L: 2 * L, 0, 14.5, color='#6aa8f7', width=1.4, dash='6 4', label='Sentier d\'expansion K = 2L', lpos=(9, 22))
    p.point(7.07, 14.14, '#e8eaf2', '(7,07 ; 14,14)', dx=8, dy=0)
    p.point(14.14, 28.28, '#e8eaf2')
    p.text(15, 3, 'isocoût C = 28,28', COL[1], 10)
    return p.svg()


def plot_couts():
    y = list(range(1, 12))
    CV = [50, 78, 98, 112, 130, 150, 175, 204, 242, 300, 385]
    CT = [c + 50 for c in CV]
    p = Plot(11.5, 450, 'y', '€', h=260, pad=(44, 20, 20, 36)).axes(xticks=range(0, 12), yticks=[0, 100, 200, 300, 400])
    p.curve([(0, 50)] + list(zip(y, CT)), COL[0], label='CT', lpos=(11, 435))
    p.curve([(0, 0)] + list(zip(y, CV)), '#8890a8', label='CV', lpos=(11, 385))
    p.curve([(0, 50), (11, 50)], COL[1], label='CF', lpos=(10.5, 58))
    g1 = p.svg()
    q = Plot(11.5, 100, 'y', '€ par unité', h=260, pad=(44, 20, 20, 36)).axes(xticks=range(0, 12), yticks=[0, 25, 50, 75, 100])
    CM = [ct / yy for ct, yy in zip(CT, y)]
    CVM = [cv / yy for cv, yy in zip(CV, y)]
    CFM = [50 / yy for yy in y]
    Cm = [50, 28, 20, 14, 18, 20, 25, 29, 38, 58, 85]
    q.curve(list(zip(y, Cm)), COL[1], label='Cm', lpos=(10.6, 88))
    q.curve(list(zip(y, CM)), COL[0], label='CM', lpos=(11.1, 42))
    q.curve(list(zip(y, CVM)), COL[2], label='CVM', lpos=(11.1, 33))
    q.curve(list(zip(y, CFM)), COL[3], label='CFM', lpos=(11.1, 5))
    return f'<div style="display:grid;gap:4px">{g1}{q.svg()}</div>'


def plot_cout_td3():
    p = Plot(2.05, 7.5, 'y (milliers)', '', h=280).axes(xticks=[0, 0.5, 2 / 3, 1, 1.5, 2], yticks=[0, 1, 2, 3, 4, 5, 6, 7], fmt=lambda v: fr(v, 2) if v not in (0, 1, 2) else str(int(v)), xfmt=lambda v: {0: '0', 0.5: '0,5', 1: '1', 1.5: '1,5', 2: '2'}.get(v, '2/3'))
    p.fn(lambda y: 3 * y * y - 4 * y + 3, 0, 2.02, color=COL[1], label='Cm = 3y² − 4y + 3', lpos=(1.55, 6.3))
    p.fn(lambda y: y * y - 2 * y + 3, 0.05, 2.02, color=COL[0], label='CM = y² − 2y + 3', lpos=(1.45, 2.9))
    p.point(1, 2, '#e8eaf2', 'Cm = CM = 2 au minimum du CM', dx=6, dy=16)
    p.point(2 / 3, 5 / 3, COL[1], 'min Cm (2/3 ; 5/3)', dx=-6, dy=18, anchor='end')
    return p.svg()


def plot_engel():
    p = Plot(10, 10, 'Revenu R', 'Quantité', w=520, h=300).axes()
    p.fn(lambda R: 0.9 * R, 0, 10, color=COL[2], label='Bien normal (E > 0)', lpos=(6.9, 5.4))
    p.fn(lambda R: 3 * math.sqrt(R), 0, 10, color=COL[3], label='Première nécessité (0 < E < 1)', lpos=(0.4, 8.9))
    p.fn(lambda R: 0.09 * R * R, 0, 10, color=COL[1], label='Luxe (E > 1)', lpos=(8.5, 9.4))
    p.fn(lambda R: 8 - 0.5 * R, 1, 10, color=COL[4], label='Bien inférieur (E < 0)', lpos=(6.2, 3.9))
    return p.svg()


def plot_elast():
    p = Plot(10, 10, 'Quantité', 'Prix', w=250, h=230, pad=(30, 10, 16, 36)).axes()
    p.curve([(4, 10), (5.2, 0.5)], COL[0], label='Inélastique', lpos=(5.3, 8))
    a = p.svg()
    q = Plot(10, 10, 'Quantité', 'Prix', w=250, h=230, pad=(30, 10, 16, 36)).axes()
    q.curve([(0.5, 6), (9.5, 4.5)], COL[1], label='Très élastique', lpos=(4, 6.6))
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">{a}{q.svg()}</div>'


def plot_rde():
    p = Plot(10, 10, 'y', 'C (long terme)', w=520, h=300).axes()
    p.fn(lambda y: 3.2 * math.sqrt(y), 0, 10, color=COL[2], label='Rendements croissants', lpos=(6.5, 7.6))
    p.fn(lambda y: 0.9 * y, 0, 10, color=COL[0], label='Rendements constants', lpos=(8, 7))
    p.fn(lambda y: 0.1 * y * y, 0, 10, color=COL[1], label='Rendements décroissants', lpos=(7, 9.5))
    return p.svg()


def sujets():
    S = []
    S.append(dict(id='mic-c1', num='TD C1', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 1 Consommateur — Exercices 1 et 2',
                  titre='Contrainte budgétaire, déplacements de la droite et TMS discret',
                  enonce=H4('Exercice 1') + P('Un consommateur dispose d\'un revenu R pour consommer deux biens x1 et x2 de prix p1 et p2.') + ol(['Équation de la contrainte budgétaire et de la droite de budget ; représentation dans le plan (x1, x2) ; hachurer l\'espace de consommation.', 'Représenter les effets d\'une hausse de p1, de p2 et de R.']) +
                  H4('Exercice 2') + P('Paniers d\'une même CI : A (5 ; 13), B (6 ; 10), C (7 ; 8).') + ol(['De combien varie x2 quand x1 passe de 5 à 6, puis de 6 à 7 ?', 'Que venez-vous de calculer ?', 'Commentez.', 'L\'agent consomme B. On lui propose 1 unité de bien 1 contre 1,5 unité de bien 2 : accepte-t-il ?', 'Même question avec 1 unité contre 2,5 unités de bien 2.']),
                  pourquoi='Chapitre 1, sections 0 (contrainte budgétaire) et 3 (TMS).',
                  commentaire=ul(['Une hausse d\'un prix fait <b>pivoter</b> la droite, une hausse du revenu la <b>déplace</b> parallèlement.', 'Le TMS se lit en valeur absolue.']),
                  corrige=H3('Exercice 1') + FORM('Contrainte : p1x1 + p2x2 ≤ R · Droite : x2 = R/p2 − (p1/p2)x1') + ul(['Espace de consommation : le triangle sous la droite, entre (0 ; R/p2) et (R/p1 ; 0).', 'Hausse de p1 : pivot autour de (0 ; R/p2), l\'abscisse R/p1 se rapproche de l\'origine, la pente devient plus forte.', 'Hausse de p2 : pivot autour de (R/p1 ; 0), l\'ordonnée R/p2 baisse, la pente devient plus faible.', 'Hausse de R : déplacement parallèle vers l\'extérieur (même pente p1/p2).']) +
                  H3('Exercice 2') + ul(['De 5 à 6 : x2 passe de 13 à 10, soit −3. De 6 à 7 : de 10 à 8, soit −2.', 'On a calculé le <b>TMS</b> (en discret) : TMS(A→B) = 3, TMS(B→C) = 2.', 'Le TMS est <b>décroissant</b> : plus l\'agent a de bien 1, moins il est prêt à céder de bien 2 pour une unité supplémentaire. C\'est la convexité de la CI (goût pour la diversité).',
                                                  'En B, pour passer à 7 unités de bien 1 à utilité constante, il accepterait de céder 2 unités (on irait en C). Contre 1,5 seulement, il obtient (7 ; 8,5), qui contient plus de bien 2 que C : il est mieux (monotonie). <b>Il accepte.</b>', 'Contre 2,5 unités : (7 ; 7,5), moins bien que C (7 ; 8) qui est sur sa CI. Son utilité baisserait : <b>il refuse</b>.'])))
    S.append(dict(id='mic-c2', num='TD C1', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 1 Consommateur — Exercice 3',
                  titre='U = x1^0,5 x2^0,5 : utilités marginales, TMS et marche vers l\'optimum',
                  enonce=P('U(x1 ; x2) = x1<sup>0,5</sup>x2<sup>0,5</sup>, R = 100 €, p1 = 2 €, p2 = 5 €. L\'optimum est (25 ; 10) mais l\'agent consomme (20 ; 12).') + ol(['Contrainte budgétaire.', 'Utilités marginales ; les deux hypothèses habituelles sont-elles vérifiées ?', 'Expression du TMS, interprétation.', 'TMS en (20 ; 12), signification.', 'Pente de la droite de budget, signification.', 'Doit-il consommer une unité de bien 1 de plus ?', 'Nouvelle consommation.', 'Nouveau TMS, conclusion.', 'Mêmes questions (9 à 12) à partir du panier (27 ; 9,2).']),
                  pourquoi='Chapitre 1, sections 1 (Um), 3 (TMS) et 4 (optimum : comparer TMS et p1/p2).',
                  commentaire=ul(['Toujours comparer TMS et p1/p2 : si TMS > p1/p2, on achète plus de bien 1 ; sinon, moins.', 'Vérifie que les paniers donnés respectent le budget (2 × 20 + 5 × 12 = 100).']),
                  corrige=ol(['2x1 + 5x2 ≤ 100.', 'Um1 = 0,5 x1<sup>−0,5</sup>x2<sup>0,5</sup> > 0 et Um2 = 0,5 x1<sup>0,5</sup>x2<sup>−0,5</sup> > 0 : <b>positives</b>. ∂Um1/∂x1 = −0,25 x1<sup>−1,5</sup>x2<sup>0,5</sup> < 0 : <b>décroissantes</b>. Les deux hypothèses sont vérifiées.',
                                 'TMS = Um1/Um2 = <b>x2/x1</b> : quantité de bien 2 que l\'agent est prêt à céder pour une unité de bien 1 en plus, à utilité constante.', 'TMS(20 ; 12) = 12/20 = <b>0,6</b> : il est prêt à céder 0,6 unité de bien 2 pour 1 unité de bien 1 en plus.',
                                 'Pente en valeur absolue p1/p2 = 2/5 = <b>0,4</b> : le marché lui demande de céder 0,4 unité de bien 2 pour 1 unité de bien 1.', '<b>Oui</b> : il est prêt à céder 0,6 mais n\'a à céder que 0,4, donc son utilité augmente (TMS > p1/p2).', '(21 ; 11,6) : 2 × 21 + 5 × 11,6 = 100.',
                                 'TMS = 11,6/21 ≈ 0,552 > 0,4 : il doit continuer à substituer du bien 1 au bien 2 jusqu\'à (25 ; 10) où TMS = 10/25 = 0,4 = p1/p2.',
                                 'En (27 ; 9,2) : TMS = 9,2/27 ≈ <b>0,341</b> < 0,4. Pour une unité de bien 1 en plus, il ne céderait que 0,341 alors que le marché exige 0,4 : <b>il refuse</b>. Il a intérêt à faire l\'inverse, céder 1 unité de bien 1 pour récupérer 0,4 de bien 2 : (26 ; 9,6), où TMS = 9,6/26 ≈ 0,369, toujours < 0,4. Il continue jusqu\'à (25 ; 10), où TMS = p1/p2 : c\'est l\'optimum.'])))
    S.append(dict(id='mic-c3', num='TD C2', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 2 Consommateur — Exercices 1 et 2',
                  titre='Pourquoi un point d\'intersection n\'est pas optimal ; optimum sur une carte d\'indifférence',
                  enonce=H4('Exercice 1') + P('Tracer une CI qui coupe la droite de budget en A et B ; expliquer pourquoi A et B ne sont pas optimaux en comparant le TMS et p1/p2.') + H4('Exercice 2') +
                  table(['CI A', '', 'CI B', '', 'CI C', '', 'CI D', '', 'CI E', ''], [['x1', 'x2'] * 5, [1, '9,5', '2,5', 10, 4, 11, 5, '12,5', '6,5', 14], [2, 6, 3, 7, '4,5', 8, 6, 10, 7, '11,5'], ['3,5', 4, 4, 5, '5,5', 6, 7, '8,5', 8, 9], [5, 3, '5,5', '4,5', 7, 5, 9, 7, 10, '8,5']]) +
                  P('Budget 40 €, p1 = 5 €, p2 = 4 €.') + ol(['Représenter les CI ; nom de l\'ensemble.', 'Contrainte et droite de budget.', 'Panier qui maximise l\'utilité.', 'TMS en ce point.']),
                  pourquoi='Chapitre 1, sections 2 (carte d\'indifférence) et 4 (optimum graphique).',
                  commentaire=ul(['Chercher le panier du tableau qui est <b>sur</b> la droite de budget et sur la CI la plus haute.']),
                  corrige=H3('Exercice 1') + P('En A (en haut à gauche), la CI est plus pentue que la droite : TMS > p1/p2. L\'agent gagne à acheter plus de bien 1 et moins de bien 2. En B, la CI est moins pentue : TMS < p1/p2, il gagne à faire l\'inverse. Entre A et B, les paniers de la droite sont au-dessus de la CI : il existe une CI plus haute accessible. L\'optimum est au point de <b>tangence</b>, où TMS = p1/p2.') +
                  H3('Exercice 2') + ol(['L\'ensemble des CI est une <b>carte d\'indifférence</b> ; l\'utilité croît de A vers E.', '5x1 + 4x2 ≤ 40 ; droite x2 = 10 − 1,25x1 (points (0 ; 10) et (8 ; 0)).',
                                                       'On teste les paniers : (4 ; 5) sur la CI B coûte 5 × 4 + 4 × 5 = 40 et se trouve sur la droite ; aucun panier des CI C, D, E n\'est accessible (ex. (4 ; 11) coûte 64). L\'optimum est <b>(4 ; 5)</b> sur la CI B.', 'À l\'optimum, TMS = p1/p2 = 5/4 = <b>1,25</b>.'])))
    S.append(dict(id='mic-c4', num='TD C2', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 2 Consommateur — Exercices 3, 4 et 5',
                  titre='Optimums de fonctions Cobb-Douglas (Lagrangien) et effet d\'un changement de prix relatif',
                  enonce=ol(['U = x1<sup>0,5</sup>x2<sup>0,5</sup>, R = 100, p1 = 2, p2 = 5 : panier optimal.', 'U = x1<sup>0,25</sup>x2<sup>0,75</sup>, R = 400, p1 = 10, p2 = 20 : TMS puis panier optimal.', 'U = x1<sup>1/3</sup>x2<sup>2/3</sup>, R = 12 000, p1 = 5, p2 = 8 : TMS, panier optimal ; les prix passent à p1 = 2,5 et p2 = 10 : (a) TMS à l\'ancien optimum, (b) nouveau rapport des prix, (c) sens de variation des quantités (sans calcul).']),
                  pourquoi='Chapitre 1, section 4 (Lagrangien, méthode TMS = p1/p2).',
                  commentaire=ul(['Méthode rapide : TMS = p1/p2 et contrainte saturée.', 'Contrôle Cobb-Douglas : part du revenu = exposant / somme des exposants.']),
                  corrige=H3('Exercice 3') + FORM('L = x1<sup>0,5</sup>x2<sup>0,5</sup> + λ(100 − 2x1 − 5x2) ⇒ x2/x1 = 2/5 ⇒ x2 = 0,4x1 ⇒ 100 = 4x1 ⇒ x1 = 25, x2 = 10') +
                  H3('Exercice 4') + P('TMS = (0,25 x1<sup>−0,75</sup>x2<sup>0,75</sup>)/(0,75 x1<sup>0,25</sup>x2<sup>−0,25</sup>) = <b>x2/(3x1)</b>.') + FORM('x2/(3x1) = 10/20 ⇒ x2 = 1,5x1 ⇒ 400 = 10x1 + 30x1 ⇒ x1 = 10, x2 = 15') + P('Contrôle : 25 % du revenu sur le bien 1 (100 €), 75 % sur le bien 2 (300 €).') +
                  H3('Exercice 5') + P('TMS = <b>x2/(2x1)</b>.') + FORM('x2/(2x1) = 5/8 ⇒ x2 = 1,25x1 ⇒ 12 000 = 5x1 + 10x1 ⇒ x1 = 800, x2 = 1 000') +
                  ol(['Au panier (800 ; 1 000), TMS = 1 000/1 600 = <b>0,625</b> (= ancien rapport des prix 5/8).', 'Nouveau rapport : 2,5/10 = <b>0,25</b>.', 'TMS (0,625) > p1/p2 (0,25) : pour une unité de bien 1, l\'agent est prêt à céder 0,625 de bien 2 alors que le marché n\'en demande plus que 0,25. Il <b>augmente x1</b> et <b>diminue x2</b> jusqu\'à ce que le TMS redescende à 0,25. Pour vérifier : x1 = 4 000/2,5 = 1 600 et x2 = 8 000/10 = 800.'])))
    S.append(dict(id='mic-c5', num='TD C3', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 3 Consommateur — Exercice 1',
                  titre='Consommation-revenu, courbes d\'Engel, consommation-prix et demande (lecture graphique)',
                  enonce=P('Mêmes courbes d\'indifférence que le TD 2 (ex. 2). R = 40 €, p1 = 5 €, p2 = 4 € ; optimum (4 ; 5).') + ol(['TMS en (4 ; 5).', 'Le revenu passe à 51,5 € : nouvelles quantités.', 'Tracer la courbe de consommation-revenu.', 'Tracer les courbes d\'Engel.', 'p1 passe à 8 € (R = 40 €) : quantités consommées.', 'Tracer la courbe de consommation-prix.', 'En déduire la courbe de demande du bien 1.']),
                  pourquoi='Chapitre 1, section 5 (courbes de consommation-revenu, de consommation-prix, d\'Engel, de demande).',
                  commentaire=ul(['Pour chaque nouvelle droite de budget, chercher dans le tableau le panier qui la sature exactement.']),
                  corrige=ol(['À l\'optimum, TMS = p1/p2 = <b>1,25</b>.', 'Budget 5x1 + 4x2 = 51,5 : le panier (5,5 ; 6) de la CI C coûte 27,5 + 24 = 51,5. Nouvelles quantités : <b>(5,5 ; 6)</b>.', 'Courbe de consommation-revenu : elle relie (4 ; 5) et (5,5 ; 6), puis les optimums pour d\'autres revenus.',
                              'Courbes d\'Engel : x1 = 4 pour R = 40 et 5,5 pour R = 51,5 ; x2 = 5 puis 6. Les deux sont croissantes (biens normaux) ; celle du bien 1 croît plus vite (voir TD élasticités, exercice 4 : bien 1 de luxe, bien 2 de première nécessité).',
                              'Budget 8x1 + 4x2 = 40 : le panier (2 ; 6) de la CI A coûte 16 + 24 = 40. Quantités : <b>(2 ; 6)</b>.', 'Courbe de consommation-prix : elle relie (4 ; 5) pour p1 = 5 et (2 ; 6) pour p1 = 8.', 'Courbe de demande du bien 1 : points (x1 = 4 ; p1 = 5) et (x1 = 2 ; p1 = 8). Elle est décroissante : bien ordinaire.'])))
    xi = (4 ** (1 / 3) * 12 ** (2 / 3)) / 1.5 ** (2 / 3)
    S.append(dict(id='mic-c6', num='TD C3', ch='micro-1', mobiliser=[], type='Exercice de TD', source='TD 3 Consommateur — Exercices 2 et 3',
                  titre='Fonctions de demande d\'une Cobb-Douglas et décomposition de Hicks (effet de substitution, effet de revenu)',
                  enonce=H4('Exercice 2') + P('U = x1<sup>0,5</sup>x2<sup>0,5</sup>.') + ol(['Expressions de x1 et x2 optimales en fonction de p1, p2, R ; que représentent-elles ?', 'R = 100, p1 = 2, p2 = 5 : quantités.', 'p1 passe à 2,5 : nouvelle quantité de bien 1.', 'Tracer la fonction de demande du bien 1.']) +
                  H4('Exercice 3') + P('U = x1<sup>1/3</sup>x2<sup>2/3</sup>, R = 36 €, p1 = 3 €, p2 = 2 €.') + ol(['Panier optimal (panier 1).', 'p1 passe à 1,5 € : panier 2.', 'Interprétation du passage (effet de revenu, effet de substitution).']),
                  pourquoi='Chapitre 1, section 5 : fonction de demande (A) et décomposition de Hicks (C).',
                  commentaire=ul(['Panier intermédiaire : nouveaux prix, <b>utilité initiale</b> (on résout TMS = p1\'/p2 et U = U0).', 'ES = intermédiaire − initial ; ER = final − intermédiaire.']),
                  corrige=H3('Exercice 2') + FORM('TMS = x2/x1 = p1/p2 ⇒ p2x2 = p1x1 ⇒ R = 2p1x1 ⇒ x1 = R/(2p1) ; x2 = R/(2p2)') +
                  P('Ce sont les <b>fonctions de demande</b> (paniers optimaux pour tous prix et revenus). (2) x1 = 100/4 = <b>25</b>, x2 = 100/10 = <b>10</b>. (3) x1 = 100/5 = <b>20</b>. (4) Demande du bien 1 : x1 = 50/p1 (hyperbole décroissante), passant par (25 ; 2) et (20 ; 2,5).') +
                  H3('Exercice 3') + ol(['TMS = x2/(2x1) = 3/2 ⇒ x2 = 3x1 ; 36 = 3x1 + 6x1 ⇒ <b>x1 = 4, x2 = 12</b> (U0 = 4<sup>1/3</sup>·12<sup>2/3</sup> ≈ 8,32).', 'TMS = 1,5/2 ⇒ x2 = 1,5x1 ; 36 = 1,5x1 + 3x1 ⇒ <b>x1 = 8, x2 = 12</b>.',
                                                        f'Panier intermédiaire (nouveaux prix, utilité U0) : x2 = 1,5x1 et x1<sup>1/3</sup>(1,5x1)<sup>2/3</sup> = U0 ⇒ x1 = U0/1,5<sup>2/3</sup> ≈ <b>{fr(xi, 2)}</b>, x2 ≈ <b>{fr(1.5 * xi, 2)}</b> (revenu compensé ≈ {fr(1.5 * xi + 2 * 1.5 * xi, 2)} €).']) +
                  table(['', 'x1', 'x2'], [['ES', f'+{fr(xi - 4, 2)}', f'−{fr(12 - 1.5 * xi, 2)}'], ['ER', f'+{fr(8 - xi, 2)}', f'+{fr(12 - 1.5 * xi, 2)}'], ['ET', '+4', '0']]) +
                  P('La baisse de p1 rend le bien 1 relativement moins cher (ES : +x1, −x2) et augmente le pouvoir d\'achat (ER > 0 sur les deux biens : <b>biens normaux</b>). Le bien 1 est un <b>bien ordinaire</b> ; pour le bien 2, ES et ER se compensent (biens indépendants), comme dans l\'exemple du cours.')))
    S.append(dict(id='mic-e1', num='TD Él.', ch='micro-1', mobiliser=['micro-0'], type='Exercice de TD', source='TD sur les élasticités — Exercices 1 à 5',
                  titre='Élasticités-prix, croisées, revenu ; équilibre de marché et typologie des biens',
                  enonce=ol(['X : quantité de 90 à 80 quand p<sub>x</sub> passe de 8 à 9 € ; Y : de 900 000 à 800 000 quand p<sub>y</sub> passe de 8 à 9 €. Élasticités-prix ; quelle propriété apparaît ?', 'x = R/p<sub>x</sub>² + 7p<sub>y</sub>/p<sub>x</sub>, avec R = 330, p<sub>x</sub> = 6, p<sub>y</sub> = 5 : élasticités directe et croisée.', 'Q<sub>D</sub> = 1 760 − 8p ; 200 producteurs identiques, q<sub>O</sub> = 0,8p − 8 : offre agrégée, équilibre, élasticités au point d\'équilibre.',
                               'R = 40 € : 4 unités de bien 1 (5 €) et 5 de bien 2 (4 €). R = 51,5 € : 5,5 et 6. Caractériser les biens. Puis p1 = 8 € (R = 40 €) : x1 = 2, x2 = 6. Le bien 1 est-il de Giffen ? Élasticité croisée de x2 par rapport à p1.', 'x = R/(2p) : élasticité-prix directe ; valeur pour R = 100 et p = 2.']),
                  pourquoi='Chapitre 1, section 5 (rappel sur les élasticités). L\'introduction (offre, demande, équilibre) sert à l\'exercice 3.',
                  commentaire=ul(['En discret, E = Δ% quantité / Δ% prix, en prenant les valeurs initiales comme base.', 'En continu, E = (∂x/∂p)·(p/x).']),
                  corrige=ol(['X : (−10/90)/(1/8) = −11,11 %/12,5 % = <b>−0,889</b> ; Y : (−100 000/900 000)/(1/8) = <b>−0,889</b>. L\'élasticité est <b>indépendante des unités</b> (sans dimension) : seules les variations relatives comptent.',
                              'x = 330/36 + 35/6 = 15. ∂x/∂p<sub>x</sub> = −2R/p<sub>x</sub>³ − 7p<sub>y</sub>/p<sub>x</sub>² = −3,056 − 0,972 = −4,028 ⇒ E = −4,028 × 6/15 ≈ <b>−1,61</b> (demande élastique, bien ordinaire). ∂x/∂p<sub>y</sub> = 7/p<sub>x</sub> = 1,167 ⇒ E croisée = 1,167 × 5/15 ≈ <b>0,39 > 0</b> : biens substituables.',
                              'Q<sub>O</sub> = 200(0,8p − 8) = <b>160p − 1 600</b>. Équilibre : 1 760 − 8p = 160p − 1 600 ⇒ <b>p* = 20</b>, <b>Q* = 1 600</b>. E<sub>D</sub> = −8 × 20/1 600 = <b>−0,1</b> (demande très inélastique) ; E<sub>O</sub> = 160 × 20/1 600 = <b>2</b> (offre élastique).',
                              'Revenu +28,75 %. Bien 1 : +37,5 % ⇒ E<sub>R</sub> ≈ <b>1,30 > 1</b> : bien normal, de luxe. Bien 2 : +20 % ⇒ E<sub>R</sub> ≈ <b>0,70</b> : bien normal, de première nécessité. Prix du bien 1 +60 % et x1 −50 % : la demande baisse quand le prix monte, donc <b>pas un bien de Giffen</b> (bien ordinaire). Croisée : x2 +20 %/p1 +60 % = <b>0,33 > 0</b> : biens substituables.',
                              '∂x/∂p = −R/(2p²) ⇒ E = −R/(2p²) × p/(R/(2p)) = <b>−1</b> quel que soit p. Pour R = 100, p = 2 : x = 25, E = −1. Élasticité unitaire : la dépense p·x = R/2 = 50 € reste constante quand le prix varie.'])))
    S.append(dict(id='mic-p1', num='TD P1', ch='micro-2', mobiliser=[], type='Exercice de TD', source='TD 1 Producteur — Exercices 1 et 2',
                  titre='Productivités moyenne et marginale, loi des rendements décroissants, rendements d\'échelle d\'une Cobb-Douglas',
                  enonce=P('Tableau de production (L, y, PmL marginale, PML moyenne) à compléter pour L = 0 à 17 (y : 0, 14, 40, 76, 120, ?, 224, 280, 336, 390, 440, 484, 520, 546, 560, 560, 544, 510).') + ol(['Valeurs manquantes.', 'Représenter PmL et PML, justifier leur position.', 'Quelle loi est illustrée ?', 'Que penser de plus de 15 unités de travail ?']) +
                  H4('Exercice 2') + P('y = K<sup>α</sup>L<sup>β</sup>, 0 < α, β < 1.') + ol(['Montrer que doubler les inputs multiplie y par 2<sup>α+β</sup>.', 'Rendements d\'échelle selon α + β.', 'Court ou long terme ?']),
                  pourquoi='Chapitre 2, section 1 (productivités, rendements d\'échelle).',
                  commentaire=ul(['PmL = y(L) − y(L−1) ; PML = y/L.', 'Pour y(5), utiliser la PmL donnée (50).']),
                  corrige=table(['L', 'y', 'PmL', 'PML'], [[1, 14, 14, 14], [2, 40, 26, 20], [3, 76, 36, '25,33'], [4, 120, 44, 30], [5, '170', 50, 34], [6, 224, 54, '37,33'], [7, 280, 56, 40], [8, 336, 56, 42], [9, 390, 54, '43,33'], [10, 440, 50, 44], [11, 484, 44, 44], [12, 520, 36, '43,33'], [13, 546, 26, 42], [14, 560, 14, 40], [15, 560, 0, '37,33'], [16, 544, -16, 34], [17, 510, -34, 30]], num_cols=(0, 1, 2, 3)) +
                  ul(['La PmL croît jusqu\'à L = 7-8 (56), puis décroît. La PML croît tant que PmL > PML et atteint son maximum (44) quand <b>PmL = PML</b>, à L = 11 : la PmL coupe la PML en son maximum.', '<b>Loi des rendements marginaux décroissants</b> : au-delà d\'un seuil, chaque travailleur supplémentaire (capital fixe) ajoute de moins en moins de production.', 'Au-delà de 15, la PmL est <b>négative</b> : la production baisse. Aucun producteur rationnel n\'emploie plus de 15 unités de travail.']) +
                  H3('Exercice 2') + FORM('f(2K, 2L) = (2K)<sup>α</sup>(2L)<sup>β</sup> = 2<sup>α+β</sup>K<sup>α</sup>L<sup>β</sup> = 2<sup>α+β</sup>y') + ul(['α + β > 1 : rendements <b>croissants</b> ; = 1 : <b>constants</b> ; < 1 : <b>décroissants</b>.', 'Tous les facteurs varient : analyse de <b>long terme</b>.'])))
    S.append(dict(id='mic-p2', num='TD P2', ch='micro-2', mobiliser=[], type='Exercice de TD', source='TD Producteur 2 — Exercices 1, 2 et 3',
                  titre='Demande de facteurs, coût minimal, sentier d\'expansion ; coût marginal et coût moyen',
                  enonce=H4('Exercice 1') + P('y = K<sup>0,4</sup>L<sup>0,4</sup>, pK = 25, pL = 16.') + ol(['TMST.', 'Fonctions de demande d\'inputs.', 'Fonction de coût total minimal.', 'Fonction de coût marginal.']) +
                  H4('Exercice 2') + P('y = K<sup>1/3</sup>L<sup>1/3</sup>, pK = pL = 10.') + ol(['TMST.', 'Inputs pour produire 25 unités.', 'Équation du sentier d\'expansion.', 'Fonctions de demande en inputs.']) +
                  H4('Exercice 3') + P('Coût total minimal : CT(y) = y³ − 2y² + 3y (y en milliers).') + ol(['Comment obtient-on cette équation ?', 'Coût marginal et son évolution.', 'Coût moyen et son évolution.', 'Vérifier que le Cm coupe le CM en son minimum.', 'Tableau de y = 0 à 2 par pas de 0,1 ; commenter.']),
                  pourquoi='Chapitre 2, sections 3 (minimisation), 4 (sentier d\'expansion, demande de facteurs) et 5 (coûts).',
                  commentaire=ul(['Système { TMST = pL/pK ; f(K, L) = y }, puis remplacer dans C = pK·K + pL·L.', 'Le minimum d\'une fonction se trouve en annulant sa dérivée.']),
                  corrige=H3('Exercice 1') + FORM('PmL = 0,4K<sup>0,4</sup>L<sup>−0,6</sup> ; PmK = 0,4K<sup>−0,6</sup>L<sup>0,4</sup> ⇒ TMST = PmL/PmK = K/L') +
                  P('K/L = 16/25 ⇒ K = 0,64L ; y = (0,64L)<sup>0,4</sup>L<sup>0,4</sup> = 0,64<sup>0,4</sup>L<sup>0,8</sup> ⇒ <b>L = y<sup>1,25</sup>/0,8</b> et <b>K = 0,8·y<sup>1,25</sup></b>.') +
                  FORM('C = 25 × 0,8y<sup>1,25</sup> + 16 × y<sup>1,25</sup>/0,8 = 20y<sup>1,25</sup> + 20y<sup>1,25</sup> = <b>40y<sup>1,25</sup></b> · Cm = dC/dy = <b>50y<sup>0,25</sup></b>') +
                  P('Exemple : pour y = 100, L ≈ 395,3, K ≈ 253,0, C ≈ 12 649 €. Le Cm est croissant : rendements d\'échelle décroissants (0,4 + 0,4 < 1).') +
                  H3('Exercice 2') + P('TMST = K/L (exposants égaux). K/L = pL/pK = 1 ⇒ <b>sentier d\'expansion K = L</b>. y = K<sup>2/3</sup> = 25 ⇒ <b>K = L = 125</b>. Fonctions de demande : <b>K = L = y<sup>3/2</sup></b>.') +
                  H3('Exercice 3') + ol(['C\'est la fonction de coût minimal : on remplace les fonctions de demande de facteurs dans C = pK·K + pL·L.', 'Cm = <b>3y² − 4y + 3</b> ; dCm/dy = 6y − 4 = 0 en y = 2/3 : le Cm décroît jusqu\'à 2/3 (Cm = 5/3 ≈ 1,67) puis croît.', 'CM = CT/y = <b>y² − 2y + 3</b> ; minimum en y = 1 (CM = 2), décroissant puis croissant.', 'Cm(1) = 3 − 4 + 3 = 2 = CM(1) : le Cm coupe le CM en son minimum.']) +
                  table(['y', 'CT', 'Cm', 'CM'], [[fr(v / 10, 1), fr(round((v / 10) ** 3 - 2 * (v / 10) ** 2 + 3 * v / 10, 3), 3), fr(round(3 * (v / 10) ** 2 - 4 * v / 10 + 3, 2), 2), fr(round((v / 10) ** 2 - 2 * v / 10 + 3, 2), 2) if v else '—'] for v in range(0, 21)], num_cols=(0, 1, 2, 3)) +
                  P('Tant que Cm < CM (y < 1), produire une unité de plus fait baisser le coût moyen ; au-delà, il augmente.')))
    S.append(dict(id='mic-q1', num='Synthèse', ch='micro-1', mobiliser=['micro-2'], type='Question de synthèse', source='D\'après les séances 3, 4 et 8',
                  titre='Comparer l\'optimum du consommateur et la combinaison optimale du producteur',
                  enonce=P('Montrez que le choix du consommateur (maximiser l\'utilité sous contrainte budgétaire) et celui du producteur (minimiser le coût sous contrainte de production) reposent sur la même logique. Précisez les outils qui se correspondent.'),
                  pourquoi='Relie le chapitre 1 (droite de budget, CI, TMS) et le chapitre 2 (isocoût, isoquante, TMST) : le cours lui-même parle d\'« équivalent de la droite de budget » et de « même principe que le TMS ».',
                  commentaire=ul(['Construire un tableau de correspondances, puis expliquer la condition de tangence commune.']),
                  corrige=table(['Consommateur (ch. 1)', 'Producteur (ch. 2)'], [['Fonction d\'utilité U(x1, x2)', 'Fonction de production f(K, L)'], ['Courbe d\'indifférence', 'Isoquante'], ['Droite de budget R = p1x1 + p2x2', 'Droite d\'isocoût C = pK·K + pL·L'], ['TMS = Um1/Um2', 'TMST = PmL/PmK'], ['Optimum : TMS = p1/p2', 'Optimum : TMST = pL/pK'], ['Max U sous contrainte de budget', 'Min C sous contrainte de production'], ['Courbe de consommation-revenu', 'Sentier d\'expansion'], ['Fonctions de demande de biens', 'Fonctions de demande de facteurs']]) +
                  P('Dans les deux cas, l\'agent égalise son <b>taux d\'échange subjectif ou technique</b> (TMS, TMST) avec le <b>taux d\'échange du marché</b> (rapport des prix). Graphiquement, c\'est la tangence d\'une courbe convexe et d\'une droite. Mathématiquement, on résout un Lagrangien dont les CPO donnent Um1/p1 = Um2/p2 ou PmL/pL = PmK/pK. La différence : le consommateur maximise un objectif à budget donné, le producteur minimise un coût à production donnée (programme dual).')))
    return S


def quiz1():
    return [dict(q='R = 60, p1 = 3, p2 = 6. Ordonnée à l\'origine de la droite de budget ?', opts=['10', '20', '6', '3'], ans=0, exp='R/p2 = 60/6 = 10.', tag='calcul'),
            dict(q='Que mesure la pente (en valeur absolue) de la droite de budget ?', opts=['Le prix relatif p1/p2', 'Le TMS', 'L\'utilité marginale du bien 1', 'Le revenu réel'], ans=0, exp='Valeur du bien 1 en bien 2 du point de vue du marché.'),
            dict(type='vf', q='Une hausse du revenu fait pivoter la droite de budget.', ans=False, exp='Elle la déplace parallèlement ; une variation de prix la fait pivoter.'),
            dict(q='U = x1^0,5 x2^0,5 : quel est le TMS ?', opts=['x2/x1', 'x1/x2', '0,5', 'x1·x2'], ans=0, exp='TMS = Um1/Um2 = x2/x1.', tag='calcul'),
            dict(q='Quelle hypothèse garantit que deux CI ne se croisent pas ?', opts=['Transitivité', 'Convexité', 'Complétude', 'Divisibilité'], ans=0, exp='Si deux CI se croisaient, la transitivité serait violée.'),
            dict(q='Quelle hypothèse explique la convexité des CI ?', opts=['Le goût pour la diversité', 'La non-satiété', 'La complétude', 'La transitivité'], ans=0, exp='Convexité des préférences : paniers diversifiés préférés aux paniers extrêmes.'),
            dict(q='À l\'optimum intérieur du consommateur :', opts=['TMS = p1/p2', 'TMS = 1', 'Um1 = Um2', 'x1 = x2'], ans=0, exp='Tangence entre CI et droite de budget.'),
            dict(q='En un point, TMS = 0,8 et p1/p2 = 0,5. Que doit faire l\'agent ?', opts=['Consommer plus de bien 1 et moins de bien 2', 'Consommer moins de bien 1', 'Rien, il est à l\'optimum', 'Réduire sa consommation totale'], ans=0, exp='TMS > p1/p2 : le bien 1 lui « coûte » moins qu\'il ne l\'apprécie.', tag='mécanisme'),
            dict(q='U = x1^0,25 x2^0,75, R = 400, p1 = 10, p2 = 20. Optimum ?', opts=['(10 ; 15)', '(20 ; 10)', '(15 ; 10)', '(25 ; 7,5)'], ans=0, exp='x1 = 0,25 × 400/10 = 10 ; x2 = 0,75 × 400/20 = 15.', tag='calcul'),
            dict(type='vf', q='L\'approche ordinale permet de dire qu\'un panier est préféré deux fois plus qu\'un autre.', ans=False, exp='C\'est l\'approche cardinale ; l\'ordinale ne fait que classer.'),
            dict(q='Une fonction d\'utilité est définie à … près.', opts=['une transformation monotone croissante', 'une constante multiplicative négative', 'un facteur 2', 'rien : elle est unique'], ans=0, exp='U et 20U + 20 représentent les mêmes préférences.'),
            dict(q='Biens parfaitement complémentaires : forme des CI ?', opts=['En L (coudées)', 'Droites', 'Hyperboles', 'Verticales'], ans=0, exp='Consommation en proportions fixes.'),
            dict(q='Substituts parfaits avec p1/p2 < TMS : l\'agent…', opts=['ne consomme que du bien 1', 'ne consomme que du bien 2', 'consomme les deux à parts égales', 'ne consomme rien'], ans=0, exp='Solution en coin sur le bien 1.'),
            dict(q='Élasticité-revenu de 1,4 : type de bien ?', opts=['Bien de luxe', 'Bien de première nécessité', 'Bien inférieur', 'Bien de Giffen'], ans=0, exp='E > 1 : bien de luxe (supérieur).', tag='calcul'),
            dict(q='Élasticité-prix croisée négative : les biens sont…', opts=['complémentaires', 'substituables', 'inférieurs', 'indépendants'], ans=0, exp='La hausse du prix de l\'un réduit la demande de l\'autre.'),
            dict(q='x = −20p + 1000 en p = 25. Élasticité-prix ?', opts=['−1', '−20', '−0,5', '−2'], ans=0, exp='−20 × 25/500 = −1.', tag='calcul'),
            dict(q='Un bien de Giffen est…', opts=['un bien inférieur dont l\'ER l\'emporte sur l\'ES', 'un bien de luxe', 'un bien dont l\'élasticité-revenu est > 1', 'un bien complémentaire'], ans=0, exp='La demande augmente avec le prix.'),
            dict(q='Dans la méthode de Hicks, le panier intermédiaire se calcule avec…', opts=['les nouveaux prix et l\'utilité initiale', 'les anciens prix et le nouveau revenu', 'les nouveaux prix et le revenu initial', 'les anciens prix et la nouvelle utilité'], ans=0, exp='On compense le revenu pour rester sur la CI initiale.'),
            dict(q='Si p1 baisse et que les biens sont normaux, l\'effet de revenu sur x2 est…', opts=['positif', 'négatif', 'nul', 'indéterminé'], ans=0, exp='Le pouvoir d\'achat augmente : on consomme plus de chaque bien normal.'),
            dict(q='Que représente la courbe d\'Engel ?', opts=['La quantité consommée d\'un bien en fonction du revenu', 'La quantité demandée en fonction du prix', 'Les paniers optimaux quand un prix varie', 'Le TMS en fonction de x1'], ans=0, exp='Une courbe par bien.'),
            dict(type='vf', q='Le long de la courbe de demande, l\'utilité du consommateur reste constante.', ans=False, exp='L\'agent maximise son utilité en chaque point, mais son niveau d\'utilité change.'),
            dict(q='x = R/(2p) : élasticité-prix directe ?', opts=['−1', '−2', '−0,5', '0'], ans=0, exp='Élasticité unitaire, dépense constante.', tag='calcul')]


def quiz2():
    return [dict(q='Notation du cours : PmL désigne…', opts=['la productivité marginale du travail', 'la productivité moyenne du travail', 'le prix du travail', 'la production maximale'], ans=0, exp='m minuscule = marginal ; PML = moyenne.'),
            dict(q='y : 80 avec L = 4, 94 avec L = 5. PmL au 5ᵉ travailleur ?', opts=['14', '18,8', '94', '20'], ans=0, exp='94 − 80 = 14.', tag='calcul'),
            dict(q='Où la productivité marginale coupe-t-elle la productivité moyenne ?', opts=['Au maximum de la productivité moyenne', 'Au minimum de la PmL', 'À l\'origine', 'Jamais'], ans=0, exp='Tant que Pm > PM, la moyenne monte.'),
            dict(q='y = K^0,6 L^0,6 : rendements d\'échelle ?', opts=['Croissants', 'Constants', 'Décroissants', 'Nuls'], ans=0, exp='α + β = 1,2 > 1.', tag='calcul'),
            dict(q='Définition du TMST :', opts=['PmL/PmK', 'PmK/PmL', 'pL/pK', 'K/L toujours'], ans=0, exp='TMST = −ΔK/ΔL = PmL/PmK.'),
            dict(q='Condition de minimisation du coût :', opts=['TMST = pL/pK', 'TMST = pK/pL', 'PmL = PmK', 'K = L'], ans=0, exp='Tangence isoquante / isocoût.'),
            dict(q='y = K^0,5 L^0,5, pK = 1, pL = 2 : sentier d\'expansion ?', opts=['K = 2L', 'L = 2K', 'K = L', 'K = 0,5'], ans=0, exp='TMST = K/L = pL/pK = 2.', tag='calcul'),
            dict(q='Même fonction, y = 10 : combinaison optimale ?', opts=['K ≈ 14,14 ; L ≈ 7,07', 'K = 10 ; L = 10', 'K = 2 ; L = 50', 'K = 7,07 ; L = 14,14'], ans=0, exp='√2·L = 10.', tag='calcul'),
            dict(type='vf', q='Le coût fixe peut être éliminé sans cesser l\'activité.', ans=False, exp='Il ne disparaît qu\'en cessant l\'activité.'),
            dict(q='CT = 100 pour y = 1 et 128 pour y = 2. Coût marginal de la 2ᵉ unité ?', opts=['28', '64', '128', '100'], ans=0, exp='128 − 100 = 28.', tag='calcul'),
            dict(q='Le coût marginal coupe le coût moyen…', opts=['en son minimum', 'en son maximum', 'à l\'origine', 'jamais'], ans=0, exp='Propriété vérifiée au TD 2, exercice 3.'),
            dict(q='Rendements d\'échelle croissants : le coût total de long terme…', opts=['augmente moins vite que la production', 'augmente plus vite que la production', 'est constant', 'diminue'], ans=0, exp='Économies d\'échelle.'),
            dict(q='Relation coût-productivité du cours :', opts=['Cm = pL/PmL', 'Cm = PmL/pL', 'CM = pL × PML', 'CVM = PmL'], ans=0, exp='Et CVM = pL/PML.'),
            dict(type='vf', q='À long terme, tous les facteurs de production sont variables.', ans=True, exp='D\'où C_LT ≤ C_CT.'),
            dict(q='Formule du profit :', opts=['π = p·y − C', 'π = C − RT', 'π = p/C', 'π = Cm − CM'], ans=0, exp='Recettes moins coûts.'),
            dict(q='Une isoquante relie…', opts=['les combinaisons de facteurs donnant la même production', 'les combinaisons de même coût', 'les paniers de même utilité', 'les prix des facteurs'], ans=0, exp='L\'isocoût relie les combinaisons de même coût.')]


def quiz0():
    return [dict(q='Laquelle n\'est PAS une hypothèse de la CPP ?', opts=['Différenciation des produits', 'Atomicité', 'Libre entrée et sortie', 'Transparence de l\'information'], ans=0, exp='La CPP suppose l\'homogénéité des produits.'),
            dict(q='Un prix supérieur au prix d\'équilibre provoque…', opts=['un excès d\'offre', 'un excès de demande', 'l\'équilibre', 'une hausse de la demande'], ans=0, exp='Les offreurs veulent vendre plus que ce que les demandeurs achètent.'),
            dict(q='Une hausse du revenu des ménages (bien normal) entraîne…', opts=['un déplacement de la courbe de demande', 'un déplacement le long de la courbe de demande', 'un déplacement de la courbe d\'offre', 'rien'], ans=0, exp='Une variable autre que le prix du bien change.'),
            dict(q='Une hausse des salaires affecte d\'abord…', opts=['la courbe d\'offre (déplacement)', 'la courbe de demande', 'le prix des autres biens', 'l\'atomicité'], ans=0, exp='Coût de production plus élevé.'),
            dict(type='vf', q='En CPP, chaque agent est preneur de prix.', ans=True, exp='Conséquence de l\'atomicité.'),
            dict(q='L\'individualisme méthodologique caractérise…', opts=['la microéconomie', 'la macroéconomie', 'la comptabilité', 'le marketing'], ans=0, exp='Partir des comportements individuels.')]


def matiere():
    c0, c1, c2 = ch0(), ch1(), ch2()
    chs = [
        dict(id='micro-0', num=0, titre='Introduction : rationalité, marché et concurrence pure et parfaite', sous='Micro vs macro · rationalité · échange marchand · CPP · offre, demande, équilibre',
             desc='Les deux hypothèses fondamentales, les cinq conditions de la CPP, les courbes d\'offre et de demande et le mécanisme de marché.', tags=['CPP', 'Offre', 'Demande', 'Équilibre'],
             sources=[SRC_INTRO], cours=c0.html, notions=c0.notions, quiz=[dict(type='qcm', **q) if 'type' not in q else q for q in quiz0()],
             methode=ul(['Déplacement <b>le long</b> d\'une courbe : seul le prix du bien varie.', 'Déplacement <b>de</b> la courbe : une autre variable change (revenu, prix des autres biens, coûts).', 'Pour trouver l\'équilibre : poser offre = demande.']),
             fiches=[dict(q='Les 5 hypothèses de la CPP ?', a='Atomicité, homogénéité, libre entrée et sortie (concurrence pure) ; transparence de l\'information, mobilité des facteurs (concurrence parfaite).')],
             carte=dict(core='Marché et CPP', branches=[dict(t='Hypothèses fondamentales', items=['Rationalité', 'Échange marchand']), dict(t='Concurrence pure', items=['Atomicité', 'Homogénéité', 'Libre entrée/sortie']),
                                                         dict(t='Concurrence parfaite', items=['Transparence', 'Mobilité des facteurs']), dict(t='Marché', items=['Demande décroissante', 'Offre croissante', 'Équilibre P*, Q*', 'Excès d\'offre / de demande'])],
                        schemas=[dict(t='Retour à l\'équilibre', steps=['P > P*', 'Excès d\'offre', 'Baisse du prix', 'Offre ↓, demande ↑', 'P = P*'])]),
             liens=[dict(ch='micro-1', pourquoi='La courbe de demande de marché est la somme des demandes individuelles tirées de l\'optimum du consommateur.'), dict(ch='micro-2', pourquoi='La courbe d\'offre découle des coûts du producteur.')]),
        dict(id='micro-1', num=1, titre='Théorie du consommateur', sous='Contrainte budgétaire · utilité · préférences · TMS · optimum · demande, élasticités, effets de Hicks',
             desc='Du budget à la demande : droite de budget, courbes d\'indifférence, TMS, Lagrangien, élasticités, consommation-prix et revenu, courbe d\'Engel, effets de substitution et de revenu.',
             tags=['TMS', 'Lagrangien', 'Élasticités', 'Hicks', 'Engel'], sources=SRC_C1 + [SRC_TD[0], SRC_TD[2]], cours=c1.html, notions=c1.notions, quiz=[dict(type='qcm', **q) if 'type' not in q else q for q in quiz1()],
             methode=ul(['Écrire la contrainte R = p1x1 + p2x2.', 'Calculer Um1, Um2 puis TMS = Um1/Um2.', 'Poser TMS = p1/p2, en déduire x2 en fonction de x1, remplacer dans la contrainte.', 'Vérifier avec la règle des parts de revenu (Cobb-Douglas).', 'Effets de Hicks : initial → intermédiaire (utilité initiale, nouveaux prix) → final.']),
             fiches=[dict(q='Deux définitions du TMS ?', a='TMS = −Δx2/Δx1 (valeur absolue de la pente de la CI) et TMS = Um1/Um2.'), dict(q='Quatre propriétés des CI ?', a='Plus éloignées = plus d\'utilité ; pente négative ; convexes ; ne se croisent pas.'),
                     dict(q='Cobb-Douglas U = x1^a x2^b : demandes ?', a='x1 = a/(a+b) · R/p1 et x2 = b/(a+b) · R/p2.'), dict(q='Typologie selon l\'élasticité-revenu ?', a='< 0 inférieur ; > 0 normal ; entre 0 et 1 première nécessité ; > 1 luxe.')],
             carte=dict(core='Théorie du consommateur', branches=[dict(t='Contrainte budgétaire', items=['R = p1x1 + p2x2', 'Pente −p1/p2', 'R ↑ : déplacement ; p ↑ : pivot']),
                                                                  dict(t='Utilité et préférences', items=['Cardinale / ordinale', 'Um positive décroissante', 'Complétude, transitivité, monotonie, convexité', 'CI et carte d\'indifférence']),
                                                                  dict(t='TMS', items=['−Δx2/Δx1', 'Um1/Um2', 'Décroissant → CI convexe']), dict(t='Optimum', items=['Tangence TMS = p1/p2', 'Lagrangien', 'Solutions en coin, substituts, compléments']),
                                                                  dict(t='Demande et élasticités', items=['Fonction de demande', 'Élasticités prix, revenu, croisée', 'Ordinaire, Giffen, Veblen, luxe…']), dict(t='Variations', items=['Consommation-prix → demande', 'Consommation-revenu → Engel', 'ES + ER = ET (Hicks)'])],
                        schemas=[dict(t='Trouver l\'optimum', steps=['Um1, Um2', 'TMS = Um1/Um2', 'TMS = p1/p2', 'x2 = f(x1)', 'Contrainte saturée', '(x1*, x2*)']), dict(t='Baisse de p1 (biens normaux)', steps=['Prix relatif ↓', 'ES : x1 ↑, x2 ↓', 'Pouvoir d\'achat ↑', 'ER : x1 ↑, x2 ↑', 'ET : x1 ↑'])]),
             liens=[dict(ch='micro-0', pourquoi='La demande de marché agrège les demandes individuelles.'), dict(ch='micro-2', pourquoi='Même logique d\'optimisation : isoquante/CI, isocoût/droite de budget, TMST/TMS.'),
                    dict(ch='marketing-1', pourquoi='Le comportement du consommateur et la sensibilité au prix (élasticités) nourrissent l\'étude de marché et la politique de prix en marketing.')]),
        dict(id='micro-2', num=2, titre='Théorie du producteur', sous='Fonction de production · productivités · rendements d\'échelle · TMST · minimisation du coût · sentier d\'expansion · coûts',
             desc='Productivités moyenne et marginale, loi des rendements décroissants, isoquantes et TMST, isocoûts, Lagrangien de minimisation, demande de facteurs, coûts de court et de long terme.',
             tags=['TMST', 'Isocoût', 'Rendements', 'Cm / CM'], sources=SRC_C2 + [SRC_TD[1]], cours=c2.html, notions=c2.notions, quiz=[dict(type='qcm', **q) if 'type' not in q else q for q in quiz2()],
             methode=ul(['Productivités : PML = y/L ; PmL = Δy/ΔL (ou ∂y/∂L).', 'Minimisation : TMST = PmL/PmK = pL/pK, puis contrainte f(K, L) = y.', 'Demandes de facteurs K(y), L(y) → C(y) = pK·K + pL·L → Cm = C\'(y), CM = C/y.', 'Rendements d\'échelle : comparer f(λK, λL) et λf(K, L) (ou α + β à 1).']),
             fiches=[dict(q='Condition de coût minimal ?', a='TMST = PmL/PmK = pL/pK (tangence isoquante / isocoût).'), dict(q='Relation entre coûts et productivités ?', a='CVM = pL/PML et Cm = pL/PmL.'), dict(q='Cobb-Douglas y = K^α L^β : rendements ?', a='Croissants si α+β > 1, constants si = 1, décroissants si < 1.')],
             carte=dict(core='Théorie du producteur', branches=[dict(t='Production', items=['y = f(K, L)', 'Facteurs fixes / variables', 'Substituables / complémentaires']), dict(t='Productivités', items=['PML = y/L', 'PmL = ∂y/∂L', 'Rendements marginaux décroissants']),
                                                                dict(t='Rendements d\'échelle', items=['f(λz) vs λf(z)', 'α + β vs 1', 'Long terme']), dict(t='Isoquante et TMST', items=['TMST = PmL/PmK', 'Décroissant → convexe']),
                                                                dict(t='Coût minimal', items=['Isocoût C = pK K + pL L', 'TMST = pL/pK', 'Sentier d\'expansion', 'Demandes de facteurs']), dict(t='Coûts', items=['CT = CF + CV', 'CM, CVM, CFM, Cm', 'Cm coupe CM au minimum', 'C_LT ≤ C_CT'])],
                        schemas=[dict(t='Du programme aux coûts', steps=['Min C sous y = f(K, L)', 'TMST = pL/pK', 'K(y), L(y)', 'C(y)', 'Cm, CM'])]),
             liens=[dict(ch='micro-1', pourquoi='Outils symétriques du consommateur (voir le sujet de synthèse).'), dict(ch='micro-0', pourquoi='L\'offre de marché découle des coûts du producteur.'),
                    dict(ch='compta-1', pourquoi='Le coût du capital (amortissement) est une charge calculée en comptabilité ; les coûts fixes et variables se retrouvent dans le compte de résultat.'),
                    dict(ch='marketing-2', pourquoi='Les rendements d\'échelle et l\'effet de volume fondent la stratégie de domination par les coûts.')]),
    ]
    return dict(id='micro', nom='Microéconomie', court='Micro', couleur='#7c6af7', sourcesResume='13 documents · intro + 8 fichiers de cours (9 séances) + 3 dossiers de TD', documents=DOCS, chapitres=chs,
                formules=[dict(titre='Consommateur', ch='micro-1', items=[dict(t='Contrainte budgétaire', f='p1x1 + p2x2 ≤ R'), dict(t='Droite de budget', f='x2 = R/p2 − (p1/p2)x1'), dict(t='Utilité marginale', f='Um1 = ∂U/∂x1'),
                                                                         dict(t='TMS', f='TMS = −Δx2/Δx1 = Um1/Um2'), dict(t='Optimum', f='TMS = p1/p2 ; R = p1x1 + p2x2'), dict(t='Lagrangien', f='L = U(x1, x2) + λ(R − p1x1 − p2x2)'),
                                                                         dict(t='Demandes Cobb-Douglas', f='x1 = a/(a+b)·R/p1 ; x2 = b/(a+b)·R/p2', note='U = x1^a x2^b'), dict(t='Hicks', f='ET = ES + ER')]),
                          dict(titre='Élasticités', ch='micro-1', items=[dict(t='Élasticité', f='E = Δy% / Δx% = (∂y/∂x)(x/y)'), dict(t='Élasticité-prix', f='E = (∂x/∂p)(p/x)', note='< 0 bien ordinaire'), dict(t='Élasticité-revenu', f='E = (∂x/∂R)(R/x)', note='0-1 nécessité ; > 1 luxe ; < 0 inférieur'), dict(t='Élasticité croisée', f='E = (∂x/∂py)(py/x)', note='> 0 substituts ; < 0 compléments')]),
                          dict(titre='Producteur', ch='micro-2', items=[dict(t='Productivité moyenne', f='PML = y/L'), dict(t='Productivité marginale', f='PmL = ∂y/∂L'), dict(t='TMST', f='TMST = −ΔK/ΔL = PmL/PmK'), dict(t='Isocoût', f='C = pK·K + pL·L'),
                                                                        dict(t='Coût minimal', f='TMST = pL/pK ; f(K, L) = ȳ'), dict(t='Rendements (Cobb-Douglas)', f='f(λK, λL) = λ^(α+β) y'), dict(t='Coûts', f='CT = CF + CV ; CM = CT/y = CFM + CVM ; Cm = ∂CT/∂y'),
                                                                        dict(t='Coûts et productivités', f='CVM = pL/PML ; Cm = pL/PmL'), dict(t='Profit', f='π = p·y − C')]),
                          dict(titre='Marché', ch='micro-0', items=[dict(t='Équilibre', f='Offre(P*) = Demande(P*)'), dict(t='Demande de marché', f='Σ demandes individuelles')])],
                auteurs=[dict(nom='Robert Pindyck et Daniel Rubinfeld', kind='Manuel', dates='2009 (7ᵉ éd., Pearson)', courant='Microéconomie', source='cours', chapitres=['micro-0', 'micro-1', 'micro-2'], oeuvres=['Microéconomie, 7ᵉ édition, Pearson Education, 2009'], idee='Manuel recommandé par ton cours : référence complète sur le consommateur, le producteur et les marchés, avec de nombreux exemples.', phrase=''),
                         dict(nom='Pierre Picard', kind='Manuel', dates='2002 (6ᵉ éd., Montchrestien)', courant='Microéconomie', source='cours', chapitres=['micro-1', 'micro-2'], oeuvres=['Éléments de microéconomie, tome 1 : Théorie et applications (2002)'], idee='Ouvrage recommandé par ton cours pour la formalisation (optimisation sous contrainte, Lagrangien).', phrase=''),
                         dict(nom='Pierre Picard et Bruno Jullien', kind='Manuel d\'exercices', dates='2002 (3ᵉ éd., Montchrestien)', courant='Microéconomie', source='cours', chapitres=['micro-1', 'micro-2'], oeuvres=['Éléments de microéconomie, tome 2 : Exercices corrigés (2002)'], idee='Exercices corrigés recommandés par ton cours pour s\'entraîner.', phrase=''),
                         dict(nom='John Hicks', kind='Auteur', dates='1904 – 1989', courant='Néoclassique', source='cours', chapitres=['micro-1'], oeuvres=['Value and Capital (1939)'], idee='Décomposition de l\'effet total d\'une variation de prix en effet de substitution (à utilité constante) et effet de revenu : c\'est la « méthode de Hicks » de ton cours.', phrase='« Selon la décomposition de Hicks, l\'effet total d\'une baisse de prix se décompose en un effet de substitution et un effet de revenu. »'),
                         dict(nom='Robert Giffen', kind='Auteur', dates='1837 – 1910', courant='Statisticien', source='cours', chapitres=['micro-1'], idee='A donné son nom aux biens dont la demande augmente avec le prix (bien inférieur à fort effet revenu).', phrase=''),
                         dict(nom='Thorstein Veblen', kind='Auteur', dates='1857 – 1929', courant='Institutionnalisme', source='cours', chapitres=['micro-1'], oeuvres=['Théorie de la classe de loisir (1899)'], idee='Consommation ostentatoire : la demande de certains biens augmente avec leur prix, qui signale un statut (effet Veblen).', phrase=''),
                         dict(nom='Ernst Engel', kind='Auteur', dates='1821 – 1896', courant='Statisticien', source='cours', chapitres=['micro-1'], idee='La courbe d\'Engel relie la consommation d\'un bien au revenu ; la part de l\'alimentation diminue quand le revenu augmente (loi d\'Engel).', phrase=''),
                         dict(nom='Joseph-Louis Lagrange', kind='Mathématicien', dates='1736 – 1813', courant='Mathématiques', source='cours', chapitres=['micro-1', 'micro-2'], idee='Méthode du multiplicateur de Lagrange pour optimiser sous contrainte, utilisée pour l\'optimum du consommateur et la minimisation du coût.', phrase=''),
                         dict(nom='Charles Cobb et Paul Douglas', kind='Auteurs', dates='1928', courant='Économétrie', source='compl', chapitres=['micro-2', 'micro-1'], oeuvres=['A Theory of Production (1928)'], idee='Fonction y = A·K^α·L^β, utilisée dans presque tous tes exercices, en production comme en utilité (Cobb-Douglas).', phrase=''),
                         dict(nom='Léon Walras', kind='Auteur', dates='1834 – 1910', courant='Néoclassique (marginaliste)', source='compl', chapitres=['micro-0'], oeuvres=['Éléments d\'économie politique pure (1874)'], idee='Équilibre général et mécanisme d\'ajustement des prix par confrontation de l\'offre et de la demande.', phrase=''),
                         dict(nom='Alfred Marshall', kind='Auteur', dates='1842 – 1924', courant='Néoclassique', source='compl', chapitres=['micro-0', 'micro-1'], oeuvres=['Principles of Economics (1890)'], idee='Courbes d\'offre et de demande, équilibre partiel, notion d\'élasticité.', phrase=''),
                         dict(nom='Vilfredo Pareto', kind='Auteur', dates='1848 – 1923', courant='Néoclassique', source='compl', chapitres=['micro-1'], oeuvres=['Manuel d\'économie politique (1906)'], idee='Utilité ordinale et courbes d\'indifférence : il suffit de classer les paniers, pas de mesurer l\'utilité.', phrase='')],
                reperes=[dict(date='1776', t='Adam Smith, La Richesse des nations : l\'échange marchand mutuellement avantageux.'), dict(date='1871-1874', t='Révolution marginaliste (Jevons, Menger, Walras) : l\'utilité marginale.'),
                         dict(date='1890', t='Marshall, Principles of Economics : offre, demande, élasticité.'), dict(date='1906', t='Pareto : utilité ordinale et courbes d\'indifférence.'), dict(date='1928', t='Cobb et Douglas : fonction de production K^α L^β.'),
                         dict(date='1939', t='Hicks, Value and Capital : effet de substitution et effet de revenu.', src='cours')],
                methode=[dict(titre='Résoudre un programme du consommateur', html=ol(['Écrire Max U sous R = p1x1 + p2x2.', 'Calculer Um1, Um2 et TMS = Um1/Um2.', 'TMS = p1/p2 ⇒ relation entre x2 et x1.', 'Remplacer dans la contrainte, en déduire x1 puis x2.', 'Vérifier : budget exactement dépensé ; part du revenu (Cobb-Douglas).']), piege='Inverser le TMS (x1/x2 au lieu de x2/x1) ou oublier de saturer la contrainte.'),
                         dict(titre='Décomposition de Hicks', html=ol(['Panier initial (anciens prix, R).', 'Panier final (nouveaux prix, R).', 'Panier intermédiaire : nouveaux prix et <b>utilité initiale</b> ⇒ TMS = p1\'/p2 et U(x1, x2) = U0.', 'ES = intermédiaire − initial ; ER = final − intermédiaire ; vérifier ES + ER = ET.', 'Conclure : signe de l\'ER (normal/inférieur), signe de l\'ET (ordinaire/Giffen).']), piege='Utiliser le revenu initial pour le panier intermédiaire : c\'est l\'utilité initiale qu\'on garde.'),
                         dict(titre='Calculer une élasticité', html=ol(['Discret : Δ%y / Δ%x avec les valeurs initiales comme base.', 'Continu : (∂y/∂x)·(x/y) au point considéré.', 'Interpréter le signe puis la valeur absolue (> 1 élastique).', 'Conclure sur le type de bien.']), piege='Oublier le signe négatif de l\'élasticité-prix, ou confondre inélastique (|E| < 1) et élastique.'),
                         dict(titre='Minimiser le coût du producteur', html=ol(['Min C = pK·K + pL·L sous f(K, L) = ȳ.', 'TMST = PmL/PmK = pL/pK ⇒ sentier d\'expansion K = f(L).', 'Remplacer dans f(K, L) = ȳ ⇒ demandes de facteurs K(y), L(y).', 'C(y) = pK·K(y) + pL·L(y), puis Cm et CM.']), piege='Écrire TMST = pK/pL (rapport à l\'envers).'),
                         dict(titre='Lire un tableau de productivités ou de coûts', html=ul(['PM = total / quantité ; Pm = différence entre deux lignes.', 'La marginale coupe la moyenne en son extremum.', 'Cm < CM ⇒ CM décroissant ; Cm > CM ⇒ CM croissant.']))],
                courbes=[dict(id='mic-g0', ch='micro-0', titre='Offre, demande et équilibre de marché', svg=plot_cpp(), tags=['équilibre', 'offre', 'demande'], exp=ul(['Demande décroissante, offre croissante : elles se coupent en E (P*, Q*).', 'Au-dessus de P*, excès d\'offre qui fait baisser le prix ; en dessous, excès de demande qui le fait monter.', 'Un choc sur le revenu, les autres prix ou les coûts <b>déplace</b> une courbe.'])),
                         dict(id='mic-g1', ch='micro-1', titre='Droite de budget et optimum du consommateur (R = 100, p1 = 2, p2 = 5)', svg=plot_budget_opt(), tags=['optimum', 'TMS', 'droite de budget'], exp=ul(['Zone ombrée : paniers accessibles.', 'L\'optimum (25 ; 10) est au point de tangence avec la CI la plus haute accessible : TMS = x2/x1 = 0,4 = p1/p2.', 'Exemple du cours avec U = x1<sup>0,5</sup>x2<sup>0,5</sup>.'])),
                         dict(id='mic-g2', ch='micro-1', titre='Carte d\'indifférence', svg=plot_ci(), tags=['courbe d\'indifférence'], exp=ul(['Trois CI de U = x1·x2 : plus on s\'éloigne de l\'origine, plus l\'utilité augmente.', 'Pente négative (monotonie), convexité (TMS décroissant), pas de croisement (transitivité).'])),
                         dict(id='mic-g3', ch='micro-1', titre='Cas particuliers : substituts et compléments parfaits', svg=plot_substituts(), tags=['substituts', 'compléments'], exp=ul(['Substituts parfaits : CI droites, TMS constant, solutions souvent en coin.', 'Compléments parfaits : CI en L, consommation en proportions fixes.'])),
                         dict(id='mic-g4', ch='micro-1', titre='Effet de substitution et effet de revenu (Hicks) — exemple chiffré du cours', svg=plot_hicks(), tags=['Hicks', 'effet de substitution', 'effet de revenu'], exp=ul(['U = x1<sup>0,25</sup>x2<sup>0,75</sup>, R = 1 000, p2 = 2, p1 passe de 10 à 5.', 'E → E\' (droite compensée tangente à la CI initiale) : effet de substitution, x1 + 17.', 'E\' → E\'\' (retour au revenu réel) : effet de revenu, x1 + 8.', 'Effet total : x1 passe de 25 à 50 ; x2 reste à 375.'])),
                         dict(id='mic-g5', ch='micro-1', titre='Courbes d\'Engel selon le type de bien', svg=plot_engel(), tags=['Engel', 'élasticité-revenu'], exp=ul(['Bien normal : croissante.', 'Première nécessité : croissante mais de moins en moins (0 < E < 1).', 'Luxe : de plus en plus pentue (E > 1).', 'Bien inférieur : décroissante (E < 0).'])),
                         dict(id='mic-g6', ch='micro-1', titre='Demande inélastique et demande très élastique', svg=plot_elast(), tags=['élasticité-prix'], exp=ul(['Inélastique : courbe très verticale, une forte variation de prix change peu la quantité.', 'Très élastique : courbe aplatie, une petite variation de prix change beaucoup la quantité.'])),
                         dict(id='mic-g7', ch='micro-2', titre='Production totale, productivités moyenne et marginale (tableau du cours)', svg=plot_prod(), tags=['productivité', 'rendements décroissants'], exp=ul(['K = 10 fixe, L varie de 0 à 9.', 'La PmL culmine (30 à L = 3), puis décroît : loi des rendements marginaux décroissants.', 'La PmL coupe la PML en son maximum ; au-delà de L = 8, la PmL devient négative.'])),
                         dict(id='mic-g8', ch='micro-2', titre='Isoquantes, isocoûts et sentier d\'expansion (y = K^0,5 L^0,5, pK = 1, pL = 2)', svg=plot_isocout(), tags=['isoquante', 'isocoût', 'sentier d\'expansion'], exp=ul(['Pour y = 10, la combinaison optimale est (L = 7,07 ; K = 14,14) : tangence avec l\'isocoût C ≈ 28,28.', 'Les isocoûts pointillés sont soit inaccessibles (trop bas), soit trop chers.', 'Les optimums pour chaque y forment le sentier d\'expansion K = 2L.'])),
                         dict(id='mic-g9', ch='micro-2', titre='Coûts de court terme (tableau du cours)', svg=plot_couts(), tags=['coûts', 'Cm', 'CM'], exp=ul(['CT = CF (50) + CV.', 'CFM décroît sans cesse (le coût fixe est réparti sur plus d\'unités).', 'Le Cm atteint son minimum (14) à y = 4 puis remonte ; il coupe le CVM puis le CM en leur minimum.'])),
                         dict(id='mic-g10', ch='micro-2', titre='TD Producteur 2, exercice 3 : Cm et CM de CT = y³ − 2y² + 3y', svg=plot_cout_td3(), tags=['coût marginal', 'coût moyen'], exp=ul(['Cm minimal en y = 2/3 (Cm = 5/3).', 'CM minimal en y = 1 (CM = 2), où il est coupé par le Cm.'])),
                         dict(id='mic-g11', ch='micro-2', titre='Rendements d\'échelle et coût total de long terme', svg=plot_rde(), tags=['rendements d\'échelle', 'long terme'], exp=ul(['Croissants : le coût croît moins vite que la production (concave).', 'Constants : droite.', 'Décroissants : le coût croît plus vite que la production (convexe).']))],
                sujets=sujets())
