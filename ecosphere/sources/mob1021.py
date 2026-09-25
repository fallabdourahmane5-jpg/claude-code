# -*- coding: utf-8 -*-
import json
M10={
1:"Ch. 10 (Weber, rationalisation, bureaucratie ; Crozier, zone d’incertitude) · Ch. 9 (rationalité limitée, théories de la firme) · Ch. 4 (rationalité du producteur) · Ch. 8 (organisation du travail) · Auteurs : Weber, Simon, Crozier, Morel, Bronner",
2:"Ch. 10 (bureaucratie wébérienne, cercle vicieux, monde formel/informel) · Ch. 9 (coûts de transaction, hiérarchie) · Ch. 8 (taylorisme, formes U et M) · Auteurs : Weber (L’Éthique protestante, 1905), Crozier (Le Phénomène bureaucratique, 1963)",
3:"Ch. 10 (holisme et individualisme méthodologiques, fait social, action sociale) · Ch. 3 (méthode et courants en économie) · Ch. 4 (individualisme méthodologique) · Auteurs : Durkheim (Les Règles de la méthode sociologique, 1895), Weber",
4:"Ch. 10 (Crozier, analyse stratégique, SEITA, sources de pouvoir) · Ch. 9 (théorie de l’agence, gouvernance) · Ch. 8 (managers, actionnaires) · Auteurs : Crozier et Friedberg (L’Acteur et le système, 1977), Marx, Weber",
5:"Ch. 10 (Morel, décisions absurdes, métarègles ; Asch, Janis) · Ch. 9 (rationalité limitée, Simon) · Ch. 4 (rationalité du décideur) · Auteurs : Morel, Asch (1951), Janis (Groupthink, 1982), Kahneman, Simon",
6:"Ch. 10 (Bronner, marché cognitif, avarice cognitive, loi de Brandolini) · Ch. 8 (plateformes, capitalisme numérique) · Ch. 9 (pouvoir des plateformes, DMA) · Auteurs : Bronner (La Démocratie des crédules, 2013 ; Apocalypse cognitive, 2021), Kahneman",
7:"Ch. 10 (Durkheim, intégration et régulation ; Castel, désaffiliation) · Ch. 1 (revenu, pauvreté monétaire) · Ch. 8 (salariat, précarisation) · Ch. 7 (inégalités) · Auteurs : Durkheim (De la division du travail social, 1893), Castel (Les Métamorphoses de la question sociale, 1995), Aubenas (Le Quai de Ouistreham, 2010)",
8:"Ch. 10 (solidarités mécanique et organique, anomie, groupe professionnel) · Ch. 8 (division du travail, industrialisation) · Ch. 3 (Smith, division du travail) · Auteurs : Durkheim (De la division du travail social, 1893), Smith",
9:"Ch. 10 (chômage BIT, catégories France Travail, halo du chômage, désaffiliation) · Ch. 1 (revenu, pauvreté) · Ch. 6 (croissance et emploi) · Ch. 7 (inégalités) · Auteurs : Castel, Aubenas",
10:"Ch. 10 (syndicats, taux de syndicalisation, institutionnalisation des conflits) · Ch. 8 (désindustrialisation, monde ouvrier) · Ch. 2ᵉ année ch. 1 (mondialisation, ubérisation) · Auteurs : Durkheim (groupe professionnel), Castel",
11:"Ch. 10 (coopération et conflit, interdépendance, Crozier) · Ch. 9 (théorie de l’agence, nœud de contrats) · Ch. 8 (gouvernance, parties prenantes) · Auteurs : Crozier, Durkheim, Alchian et Demsetz, Jensen et Meckling",
12:"Ch. 10 (conformisme d’Asch, Groupthink de Janis, métarègles de Morel) · Ch. 9 (décision en organisation) · Ch. 4 (rationalité) · Auteurs : Asch (1951), Janis (1982), Morel, Kahneman",
13:"Ch. 10 (idéal-type, bureaucratie, cercle vicieux bureaucratique) · Ch. 9 (hiérarchie et coûts de transaction) · Ch. 3 (méthode et abstraction) · Auteurs : Weber, Crozier (Le Phénomène bureaucratique, 1963 ; L’Acteur et le système, 1977)",
14:"Ch. 10 (rationalisation, désenchantement du monde, cage d’acier) · Ch. 8 (industrialisation, taylorisme) · Ch. 6 (progrès technique) · Ch. 3 (modernité et pensée économique) · Auteurs : Weber (L’Éthique protestante et l’esprit du capitalisme, 1905)",
15:"Ch. 10 (Mayo, effet Hawthorne, École des relations humaines) · Ch. 8 (taylorisme, fordisme, toyotisme) · Ch. 6 (productivité) · Auteurs : Mayo (The Human Problems of an Industrial Civilization, 1933), Taylor",
16:"Ch. 10 (Crozier, marges de manœuvre, zone d’incertitude ; conformisme) · Ch. 9 (rationalité limitée) · Ch. 8 (organisation du travail) · Auteurs : Crozier, Simon, Asch, Morel",
17:"Ch. 10 (société salariale, flexibilité, précarisation, désaffiliation) · Ch. 8 (salariat, protection sociale) · Ch. 1 (revenu, pauvreté laborieuse) · Ch. 7 (inégalités) · Auteurs : Castel (Les Métamorphoses de la question sociale, 1995), Aubenas",
18:"Ch. 10 (monde ouvrier, désindustrialisation, Simone Weil) · Ch. 8 (révolutions industrielles, taylorisme) · Ch. 6 (tertiarisation) · 2ᵉ année ch. 1 (mondialisation et délocalisation) · Auteurs : Simone Weil, Castel, Marx",
19:"Ch. 10 (inégalités de statut, de temps de travail, de salaire, discrimination) · Ch. 7 (inégalités, mesure) · Ch. 1 (revenu, redistribution) · Ch. 8 (précarisation) · Auteurs : Castel, Aubenas",
20:"Ch. 10 (démarche sociologique, idéal-type, neutralité axiologique, enquête) · Ch. 3 (méthode en économie, courants) · Ch. 9 (théories concurrentes de la firme) · Auteurs : Weber, Durkheim, Crozier, Mayo",
}
M21={
1:"2ᵉ année ch. 1 (trois dimensions de l’ouverture, configurations de Michalet) · Ch. 9 (firmes multinationales, DIPP) · Ch. 2 (flux financiers, devises) · Ch. 7 (mondialisation et développement) · Auteurs : Michalet (Qu’est-ce que la mondialisation ?, 2002)",
2:"2ᵉ année ch. 1 (gagnants et perdants, courbe de l’éléphant) · Ch. 7 (inégalités, développement) · Ch. 1 (revenu, pouvoir d’achat) · Ch. 10 (travail et précarisation) · Auteurs : Milanovic, Prebisch, Stolper et Samuelson, Piketty",
3:"2ᵉ année ch. 1 (balance des paiements, identité X−M=(S−I)+(T−G), soutenabilité) · Ch. 1 (épargne, dette publique) · Ch. 2 (financement, capitaux) · Ch. 6 (croissance) · Auteurs : Hélène Rey, Nurkse",
4:"2ᵉ année ch. 1 (taux d’ouverture, commerce en valeur ajoutée, double comptage) · Ch. 9 (chaînes de valeur, DIPP) · Ch. 6 (mesure du PIB) · Auteurs : Baldwin, Bairoch",
5:"2ᵉ année ch. 1 (chaînes de valeur, dépendances, relocalisation) · Ch. 9 (concentration verticale, coûts de transaction) · Ch. 8 (organisation productive) · Auteurs : Baldwin (dégroupages), Williamson",
6:"2ᵉ année ch. 1 (entre-deux-guerres, Hawley-Smoot 1930, slowbalization) · Ch. 3 (libre-échange et protectionnisme) · Ch. 6 (crises et croissance) · Auteurs : Bairoch (Mythes et paradoxes de l’histoire économique, 1993), List",
7:"2ᵉ année ch. 1 (spécialisation, termes de l’échange, malédiction des ressources) · Ch. 3 (Smith, Ricardo, avantages comparatifs) · Ch. 7 (développement, dépendance) · Auteurs : Ricardo, Prebisch, Acemoglu et Robinson",
8:"2ᵉ année ch. 1 (FMN, firme globale, arsenalisation) · Ch. 9 (concentration, pouvoir de marché, DMA) · Ch. 8 (gouvernance, capitalisme) · Auteurs : Michalet, Giraud",
9:"2ᵉ année ch. 1 (déplacement du centre de gravité, BRICS, privilège exorbitant) · Ch. 7 (émergents, rattrapage) · Ch. 6 (croissance comparée) · Auteurs : Michalet, Giraud, Milanovic",
10:"2ᵉ année ch. 1 (balance des paiements, comptes courant et financier) · Ch. 2 (financement de l’économie) · Ch. 1 (épargne, capacité de financement) · Auteurs : Hélène Rey",
11:"2ᵉ année ch. 1 (déséquilibres mondiaux, déficits jumeaux, position extérieure) · Ch. 2 (globalisation financière) · Ch. 6 (croissance déséquilibrée) · Auteurs : Hélène Rey, Volcker (choc de 1979)",
12:"2ᵉ année ch. 1 (première mondialisation, étalon-or, migrations, DIPP) · Ch. 8 (révolutions industrielles) · Ch. 2 (systèmes monétaires) · Auteurs : Bairoch, Baldwin, Béraud",
13:"2ᵉ année ch. 1 (stratégies d’insertion, montée en gamme, malédiction des ressources) · Ch. 7 (stratégies de développement, institutions) · Ch. 9 (montée en gamme des firmes) · Auteurs : Prebisch, Acemoglu et Robinson, Nurkse",
14:"2ᵉ année ch. 1 (courbe de l’éléphant, inégalités entre et dans les pays) · Ch. 7 (inégalités, IDH) · Ch. 1 (revenu, redistribution) · Ch. 10 (précarisation) · Auteurs : Milanovic, Piketty, Stolper et Samuelson",
15:"2ᵉ année ch. 1 (ouverture financière, IDE, capitaux de portefeuille) · Ch. 2 (financement, crises financières) · Ch. 6 (investissement et croissance) · Auteurs : Béraud, Nurkse, Hélène Rey",
16:"2ᵉ année ch. 1 (Giraud, compétition des territoires, attractivité) · Ch. 9 (firmes globales, arbitrage entre sites) · Ch. 1 (fiscalité, État) · Auteurs : Giraud, Michalet",
17:"2ᵉ année ch. 1 (protectionnisme éducateur, entre-deux-guerres, souveraineté) · Ch. 3 (libre-échange, classiques) · Ch. 7 (stratégies de développement) · Auteurs : List (1841), Bairoch, Ricardo",
18:"2ᵉ année ch. 1 (Chine, montée en gamme, rivalité technologique) · Ch. 7 (rattrapage, émergents) · Ch. 9 (concentration, concurrence technologique) · Auteurs : Michalet, Giraud, Milanovic",
19:"2ᵉ année ch. 1 (décrochage européen, parts de marché, compétitivité) · Ch. 6 (croissance comparée) · Ch. 9 (taille critique, Alstom-Siemens) · Auteurs : Giraud, Michalet",
20:"2ᵉ année ch. 1 (dépendances critiques, arsenalisation, relocalisation) · Ch. 9 (souveraineté numérique, DMA) · Ch. 1 (rôle de l’État) · Ch. 7 (dépendance et développement) · Auteurs : Giraud, Baldwin, Williamson",
}
json.dump({"10":M10,"21":M21}, open('mob_1021.json','w'), ensure_ascii=False)
print("mobiliser rédigés : ch10 =", len(M10), "| ch21 =", len(M21))
print("longueur moyenne :", sum(len(v) for v in list(M10.values())+list(M21.values()))//40, "caractères")
