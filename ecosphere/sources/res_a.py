# -*- coding: utf-8 -*-
"""Résumés des chapitres 1 à 5 (première année).

Structure de chaque résumé :
  q     la question centrale, en une phrase
  ess   l'essentiel en quelques lignes
  idees les grandes idées dans l'ordre du chapitre : t titre, d ce que la
        partie démontre, v ce qu'elle ouvre sur la suivante
  ae    auteurs et exemples incontournables : n nom, k 'a' auteur ou 'e'
        exemple, i l'idée qu'il illustre
  arg   les arguments mobilisables en dissertation
  deb   les débats du chapitre
  lien  les liens avec les autres chapitres : c numéro, p nature du lien
  min   à retenir en une minute
"""

R = {}

# =========================================================== CHAPITRE 1
R['1'] = {
 'q': "Comment la comptabilité nationale permet-elle de comprendre qui crée la richesse, "
      "qui la reçoit et qui la redistribue — et jusqu’où l’État peut-il corriger cette "
      "répartition sans rendre ses finances insoutenables ?",
 'ess':
  "Le chapitre part d’un constat : le capitalisme contemporain est en « polycrise » "
  "(Plihon). Pour en parler sérieusement, il faut d’abord un instrument de mesure : la "
  "comptabilité nationale, qui décrit l’économie comme un circuit entre six secteurs "
  "institutionnels. On suit alors le circuit dans son ordre logique. Les entreprises "
  "produisent une valeur ajoutée, dont le partage détermine leur taux de marge et leur "
  "capacité à investir ; l’investissement obéit au multiplicateur et à l’accélérateur. "
  "Cette production distribue des revenus primaires, que la redistribution transforme en "
  "revenu disponible, puis en niveau de vie par unité de consommation. La consommation "
  "qui en découle n’est pas mécanique : la fonction keynésienne est corrigée par Friedman, "
  "Duesenberry et Modigliani. Reste la question de la pauvreté monétaire, mesurée par un "
  "seuil relatif, qui conduit à l’État : ses trois fonctions (Musgrave), ses prélèvements, "
  "sa dette. Le chapitre se referme sur la mesure elle-même : le PIB décrit mal le "
  "bien-être, ce qui relativise tout l’édifice.",
 'idees': [
  {'t': "I. Un capitalisme en polycrise",
   'd': "Plihon décrit quatre crises simultanées — économique et sociale, climatique, "
        "démocratique, géopolitique — et Orain ajoute l’idée d’un capitalisme « de la "
        "finitude » : privatisation des espaces, retour des monopoles, entreprises aussi "
        "puissantes que des États. Le capitalisme repose sur quatre fondements (accumulation "
        "du capital, propriété privée, salariat, régulation marchande) mais a changé de "
        "forme, du capitalisme libéral au capitalisme interventionniste.",
   'v': "Si le capitalisme est contesté, encore faut-il savoir le mesurer : d’où le passage "
        "à l’outil statistique qui décrit l’activité."},
  {'t': "II. Les agents économiques dans un circuit : la comptabilité nationale",
   'd': "La comptabilité nationale agrège les données microéconomiques pour représenter "
        "l’économie par six secteurs institutionnels (SNF, SF, APU, ménages, ISBLSM, reste "
        "du monde). Elle décrit un circuit : production → revenus → redistribution → "
        "consommation et investissement → financement. Les agents qui épargnent plus qu’ils "
        "n’investissent dégagent une capacité de financement, les autres un besoin de "
        "financement.",
   'v': "Le circuit commence par la production : on entre donc dans l’entreprise."},
  {'t': "III. Les entreprises : production, investissement, revenus et consommation",
   'd': "La valeur ajoutée se partage : ce qui reste après salaires, cotisations et impôts "
        "forme l’excédent brut d’exploitation, d’où le taux de marge (32 % en France en "
        "2022) et le taux d’autofinancement. L’investissement (FBCF) répond au multiplicateur "
        "keynésien k = 1/(1−c) et à l’accélérateur d’Aftalion. Les revenus primaires "
        "deviennent revenu disponible puis niveau de vie par unité de consommation. La "
        "consommation suit la loi psychologique fondamentale de Keynes (propension marginale "
        "≈ 0,8), mais les faits d’après-guerre obligent à la corriger : revenu permanent chez "
        "Friedman, revenu relatif et effet de cliquet chez Duesenberry, cycle de vie chez "
        "Modigliani, déformation de la structure de consommation chez Engel.",
   'v': "Dès lors que les revenus sont inégalement répartis et que la pauvreté se mesure par "
        "un seuil relatif, l’intervention publique devient la question centrale."},
  {'t': "IV. L’État : fonctions, prélèvements et endettement",
   'd': "Musgrave (1959) distingue trois fonctions : allocation, stabilisation, "
        "redistribution. Les prélèvements n’ont pas le même effet : l’impôt sur le revenu est "
        "progressif, la TVA est régressive bien qu’elle rapporte davantage. Les niches "
        "fiscales (474 en France) et la courbe de Laffer alimentent la critique, que "
        "Rosanvallon synthétise par les trois crises de l’État-providence : financement, "
        "efficacité, légitimité. Le financement par l’emprunt impose une distinction "
        "décisive : le déficit est un flux annuel, la dette un stock cumulé, et c’est la "
        "charge d’intérêts, non le stock, qui pèse chaque année sur le budget.",
   'v': "Reste à savoir si l’indicateur sur lequel tout ce raisonnement s’appuie — le PIB — "
        "mesure bien la richesse."},
  {'t': "V. Mesurer la richesse : la synthèse et les limites du PIB",
   'd': "Le PIB se mesure par la production, les revenus ou les dépenses, en valeur ou en "
        "volume, effectif ou potentiel (l’écart entre les deux, l’output gap, signale les "
        "tensions inflationnistes). Mais il ignore le travail domestique, qui représente plus "
        "d’heures que le travail rémunéré, ne retranche pas la consommation de capital fixe "
        "(PIN) ni les dommages environnementaux (PINA, −4 %), et ne dit rien de la "
        "répartition. Depuis novembre 2024, l’Insee publie des comptes de la nation augmentée "
        "intégrant la redistribution élargie.",
   'v': "Le chapitre se referme sur une tension : l’instrument qui sert à juger le "
        "capitalisme est lui-même contesté."},
 ],
 'ae': [
  {'n': "Dominique Plihon, Les capitalismes contemporains", 'k': 'a',
   'i': "La polycrise : quatre crises simultanées rendent inopérante l’idée d’une crise "
        "conjoncturelle isolée."},
  {'n': "Arnaud Orain, Le monde confisqué", 'k': 'a',
   'i': "Le capitalisme de la finitude : la concurrence recule devant les monopoles et des "
        "empires privés aussi puissants que des États."},
  {'n': "John Maynard Keynes", 'k': 'a',
   'i': "Loi psychologique fondamentale et multiplicateur : la consommation dépend du revenu "
        "courant, et une dépense initiale produit un effet amplifié sur l’activité."},
  {'n': "Albert Aftalion (1909)", 'k': 'a',
   'i': "L’accélérateur : une variation de la demande provoque une variation plus que "
        "proportionnelle de l’investissement."},
  {'n': "Milton Friedman", 'k': 'a',
   'i': "Le revenu permanent : les ménages lissent leur consommation sur le revenu anticipé, "
        "ce qui affaiblit l’efficacité d’une relance temporaire."},
  {'n': "James Duesenberry", 'k': 'a',
   'i': "Effet de démonstration et effet de cliquet : la consommation dépend du revenu "
        "relatif et résiste à la baisse."},
  {'n': "Franco Modigliani", 'k': 'a',
   'i': "Le cycle de vie : désépargne des jeunes, épargne des actifs, désépargne des "
        "retraités — valable surtout en retraite par capitalisation."},
  {'n': "Richard Musgrave, Théorie des finances publiques (1959)", 'k': 'a',
   'i': "Les trois fonctions de l’État : allocation, stabilisation, redistribution."},
  {'n': "Pierre Rosanvallon, La crise de l’État-providence (1981)", 'k': 'a',
   'i': "Crise de financement, crise d’efficacité et crise de légitimité se renforcent."},
  {'n': "Arthur Laffer", 'k': 'a',
   'i': "« Trop d’impôt tue l’impôt » — argument très mobilisé, mais empiriquement peu "
        "vérifié, ce que le cours souligne."},
  {'n': "Gabriel Zucman", 'k': 'a',
   'i': "Un impôt plancher de 2 % sur les patrimoines supérieurs à 100 millions d’euros : "
        "un débat de justice fiscale plus qu’une solution budgétaire."},
  {'n': "Roosevelt, New Deal (1933)", 'k': 'e',
   'i': "Le basculement vers un capitalisme interventionniste : l’investissement public "
        "soutient la demande globale."},
  {'n': "Le « quoi qu’il en coûte » et les prêts garantis par l’État (2020-2021)", 'k': 'e',
   'i': "140 à 170 milliards d’euros garantis à 90 % : l’État assureur en dernier ressort, "
        "et l’effet de ciseau qui en résulte sur les finances publiques."},
  {'n': "Le pacte Dutreil", 'k': 'e',
   'i': "Une niche fiscale qui exonère jusqu’à 75 % de la valeur d’une entreprise transmise : "
        "l’exemple type d’une dépense fiscale contestée."},
 ],
 'arg': [
  "La redistribution n’est pas marginale : en niveau de vie élargi, l’écart entre les plus "
  "modestes et les plus aisés passe d’environ ×18 à ×4, et 53 % des ménages sont "
  "bénéficiaires nets.",
  "Dette et déficit ne se discutent pas de la même manière : le déficit est un flux annuel "
  "qui alimente un stock ; la soutenabilité se juge sur la charge d’intérêts rapportée au PIB "
  "et sur l’écart entre taux d’intérêt et taux de croissance.",
  "La structure des prélèvements compte autant que leur niveau : un système qui repose sur la "
  "TVA (environ 200 milliards d’euros) redistribue moins qu’un système reposant sur un impôt "
  "progressif, acquitté par 45 % seulement des contribuables.",
  "La fonction de consommation keynésienne reste un point de départ indispensable, mais une "
  "copie solide montre qu’elle a été corrigée par Friedman, Duesenberry et Modigliani.",
  "Critiquer le PIB n’est pas le rejeter : le travail domestique, le PINA et les comptes de la "
  "nation augmentée montrent qu’on peut compléter l’indicateur sans renoncer à mesurer.",
 ],
 'deb': [
  "Relance ou austérité : la dépense publique soutient la demande, mais le multiplicateur est "
  "d’autant plus faible que l’économie est ouverte et que les ménages anticipent une hausse "
  "future des impôts.",
  "Taxer les très hauts patrimoines : question de rendement budgétaire (20 milliards face à "
  "170 milliards de déficit) ou question de justice et de consentement à l’impôt ?",
  "Le niveau des prélèvements est-il la cause ou la conséquence de la crise de légitimité "
  "décrite par Rosanvallon ?",
  "Faut-il remplacer le PIB, le compléter par des indicateurs alternatifs, ou accepter qu’un "
  "indicateur de production ne mesure pas le bien-être ?",
 ],
 'lien': [
  {'c': 2, 'p': "Le financement du déficit renvoie au marché de la dette, aux taux directeurs "
                "et au policy mix : les deux chapitres se lisent ensemble."},
  {'c': 6, 'p': "La mesure du PIB, de ses limites et des inégalités de revenu prépare "
                "directement l’analyse de la croissance et de la courbe de Kuznets."},
  {'c': 7, 'p': "La pauvreté relative française s’oppose à la pauvreté absolue mondiale, et la "
                "dette publique interne à la dette extérieure des pays en développement."},
  {'c': 5, 'p': "Les fonctions de Musgrave reprennent les justifications microéconomiques de "
                "l’intervention publique : défaillances de marché."},
  {'c': 10, 'p': "Le niveau de vie et les inégalités de revenu se prolongent dans les "
                 "inégalités salariales et la structure des emplois."},
 ],
 'min': [
  "Polycrise (Plihon) : économique et sociale, climatique, démocratique, géopolitique.",
  "Six secteurs institutionnels, un circuit : production → revenus → redistribution → dépense.",
  "Taux de marge = EBE / VA (32 % en 2022) ; multiplicateur k = 1/(1−c) ; accélérateur "
  "d’Aftalion.",
  "Consommation : Keynes (revenu courant), Friedman (revenu permanent), Duesenberry (revenu "
  "relatif, cliquet), Modigliani (cycle de vie).",
  "Seuil de pauvreté 2023 : 1 288 € à 60 % du médian (9,8 millions de personnes) ; 1 073 € à "
  "50 % (5,4 millions).",
  "Musgrave : allocation, stabilisation, redistribution. Rosanvallon : financement, "
  "efficacité, légitimité.",
  "Déficit = flux annuel (≈ 170 Md€ en 2024) ; dette = stock (≈ 3 400 Md€, ≈ 114 % du PIB au "
  "premier semestre 2025) ; Maastricht : 3 % et 60 %.",
  "Le PIB ignore le travail domestique, la consommation de capital fixe et les dommages "
  "environnementaux (PIN, PINA).",
 ],
}

# =========================================================== CHAPITRE 2
R['2'] = {
 'q': "Comment la monnaie est-elle créée, pilotée et transformée en financement de "
      "l’économie — et que révèlent les crises sur les limites de ce circuit ?",
 'ess':
  "Le chapitre suit la monnaie du concept à la crise. La monnaie est d’abord un fait de "
  "confiance : trois fonctions, plusieurs formes, dont 91 % de scripturale. Elle est ensuite "
  "créée par le crédit : « les crédits font les dépôts », donc la monnaie est endogène, ce "
  "qui renverse la théorie quantitative et l’idée d’une monnaie-voile. Cette création doit "
  "alors être pilotée : la BCE agit par ses trois taux directeurs encadrant le marché "
  "interbancaire, et sa décision se transmet par quatre canaux. La crise de 2008 montre les "
  "limites de cet arsenal et ouvre l’ère des politiques non conventionnelles. En parallèle, "
  "le financement lui-même s’est déplacé : de l’économie d’endettement à l’économie de "
  "marchés financiers, sous l’effet des trois D. Le chapitre se termine sur le prix de cette "
  "transformation : titrisation, aléa moral, risque systémique.",
 'idees': [
  {'t': "I. Formes et fonctions de la monnaie",
   'd': "Trois fonctions héritées d’Aristote — unité de compte, intermédiaire des échanges, "
        "réserve de valeur — et un fondement unique : la confiance. La monnaie scripturale "
        "représente 91 % de la masse monétaire en zone euro, à ne pas confondre avec ses "
        "supports (chèque, carte, virement). Les agrégats M1, M2, M3 emboîtent les actifs du "
        "plus liquide au moins liquide. À l’échelle internationale, Krugman distingue six "
        "rôles, que le dollar remplit tous ; le triangle de Mundell montre qu’on ne peut "
        "cumuler change fixe, liberté des capitaux et autonomie monétaire.",
   'v': "Reste à savoir d’où vient cette monnaie : elle n’est pas donnée, elle est créée."},
  {'t': "II. La création monétaire : « les crédits font les dépôts »",
   'd': "Les banques commerciales créent de la monnaie scripturale en accordant des crédits, "
        "et la détruisent au remboursement : la monnaie est endogène, c’est-à-dire tirée par "
        "la demande de financement. Le multiplicateur de crédit, avec un taux de fuite en "
        "billets, décrit la limite de cette création ; les réserves obligatoires et la "
        "liquidité de banque centrale la contraignent. Cette approche s’oppose à la théorie "
        "quantitative (MV = PT, Fisher) et à l’idée que la monnaie ne serait qu’un voile sur "
        "l’économie réelle.",
   'v': "Si les banques créent la monnaie, la banque centrale doit pouvoir en orienter le "
        "coût et le volume."},
  {'t': "III. La politique monétaire conventionnelle et ses canaux",
   'd': "La BCE poursuit une cible d’inflation de 2 % à moyen terme. Elle agit par trois taux "
        "directeurs formant un corridor : facilité de dépôt (plancher), facilité de prêt "
        "(plafond), et surtout taux de refinancement à une semaine, principal signal "
        "monétaire ; entre les deux évolue l’€STR, ex-EONIA. Les décisions se transmettent par "
        "quatre canaux : taux d’intérêt, prix des actifs (effet de richesse), anticipations, "
        "taux de change.",
   'v': "Cet arsenal suppose que les taux puissent encore baisser : 2008 détruit cette "
        "hypothèse."},
  {'t': "IV. 2008 et les politiques non conventionnelles",
   'd': "Face au plancher des taux nominaux, les banques centrales achètent massivement des "
        "titres (quantitative easing), ciblent certains segments du crédit (qualitative "
        "easing), orientent les anticipations (forward guidance) et refinancent à long terme "
        "(LTRO, TLTRO). Les limites sont explicites : aléa moral, inflation des prix d’actifs "
        "donc effets inégalitaires, difficulté de la sortie. Les propositions extrêmes — "
        "hélicoptère monétaire, théorie monétaire moderne héritée de Lerner et popularisée par "
        "Kelton — brouillent la frontière entre politique monétaire et budgétaire. Éric Monnet "
        "y voit l’émergence d’une « banque providence » à démocratiser.",
   'v': "Si la banque centrale a pris tant de place, c’est aussi parce que le mode de "
        "financement de l’économie avait changé."},
  {'t': "V. De l’économie d’endettement à l’économie de marchés financiers",
   'd': "Le financement intermédié, où la banque s’interpose entre prêteurs et emprunteurs, "
        "a cédé du terrain au financement direct : c’est la désintermédiation, troisième des "
        "trois D de Bourguinat avec la déréglementation et le décloisonnement. Le marché "
        "primaire émet, le marché secondaire assure la liquidité ; l’action est un titre de "
        "propriété à revenu variable, l’obligation un titre de créance à revenu fixe. Le "
        "marché monétaire finance le court terme, avec des titres d’au moins 150 000 euros.",
   'v': "Cette liquidité nouvelle a un prix : elle diffuse le risque au lieu de le supprimer."},
  {'t': "VI. Les risques du système financier",
   'd': "La titrisation transforme des créances en titres négociables, les CDO les découpent "
        "en tranches de risque, les CDS assurent contre le défaut et permettent de spéculer "
        "sur la faillite. Le shadow banking exerce des fonctions bancaires hors régulation. "
        "L’opacité et l’interconnexion produisent la contagion, et les établissements « too "
        "big to fail » créent un aléa moral permanent : c’est le risque systémique révélé en "
        "2008. Les crypto-actifs, très volatils et surtout thésaurisés, ne remplissent pas "
        "réellement les trois fonctions de la monnaie.",
   'v': "La boucle se ferme : la confiance, qui fondait la monnaie au début du chapitre, est "
        "ce que la crise détruit."},
 ],
 'ae': [
  {'n': "Aristote", 'k': 'a',
   'i': "Les trois fonctions de la monnaie, matrice de tout le chapitre."},
  {'n': "Irving Fisher", 'k': 'a',
   'i': "MV = PT : identité comptable devenue théorie quantitative sous l’hypothèse de "
        "stabilité de V."},
  {'n': "Milton Friedman", 'k': 'a',
   'i': "L’inflation est partout un phénomène monétaire : la monnaie est exogène et doit "
        "croître à taux fixe."},
  {'n': "Robert Mundell", 'k': 'a',
   'i': "Le triangle d’incompatibilité : change fixe, mobilité des capitaux et autonomie "
        "monétaire ne peuvent coexister."},
  {'n': "Paul Krugman", 'k': 'a',
   'i': "Les six fonctions de la monnaie internationale, trois pour le secteur privé et trois "
        "pour les banques centrales."},
  {'n': "Henri Bourguinat", 'k': 'a',
   'i': "Les trois D — déréglementation, décloisonnement, désintermédiation — expliquent le "
        "basculement vers l’économie de marchés financiers."},
  {'n': "Éric Monnet, La Banque providence (2021)", 'k': 'a',
   'i': "Les banques centrales sont devenues des acteurs de la gouvernance économique : il "
        "faut en débattre démocratiquement."},
  {'n': "Abba Lerner, puis Stephanie Kelton, Le mythe du déficit (2021)", 'k': 'a',
   'i': "Théorie monétaire moderne : un État souverain monétairement n’a pas de contrainte "
        "de financement, seulement une contrainte d’inflation."},
  {'n': "William Phillips (1958)", 'k': 'a',
   'i': "La relation inflation-chômage, invalidée par la stagflation des années 1970, qui "
        "légitime l’indépendance des banques centrales."},
  {'n': "Le système de John Law (1716-1720)", 'k': 'e',
   'i': "Première grande bulle de papier-monnaie en France : les actions passent de 150 à "
        "4 100 livres avant l’effondrement."},
  {'n': "La crise de 2008", 'k': 'e',
   'i': "Titrisation, CDO et CDS transforment des défauts immobiliers américains en crise "
        "systémique mondiale."},
  {'n': "Le Système monétaire européen et l’ECU", 'k': 'e',
   'i': "Des marges de ± 2,5 % autour d’une unité de compte, jusqu’à l’effondrement de "
        "1992-1993 : l’euro naît de cet échec."},
  {'n': "Le bitcoin (2008, Satoshi Nakamoto)", 'k': 'e',
   'i': "Plafond de 21 millions d’unités, forte volatilité : un crypto-actif plutôt qu’une "
        "monnaie."},
 ],
 'arg': [
  "La monnaie endogène change la lecture de l’inflation : si les crédits font les dépôts, "
  "contrôler la masse monétaire est un objectif intermédiaire, pas un levier direct.",
  "Une hausse des taux directeurs agit simultanément sur quatre canaux : le raisonnement "
  "complet vaut mieux que le seul canal du crédit.",
  "Les politiques non conventionnelles ont sauvé la liquidité mais nourri le prix des actifs : "
  "argument central pour relier politique monétaire et inégalités de patrimoine.",
  "La désintermédiation n’a pas supprimé le risque : elle l’a dispersé, ce qui rend la "
  "contagion plus rapide et la régulation plus difficile.",
  "L’indépendance de la banque centrale se justifie par la crédibilité anti-inflationniste, "
  "mais se discute dès que la banque centrale achète de la dette publique.",
 ],
 'deb': [
  "Monnaie exogène ou endogène : la banque centrale contrôle-t-elle la quantité de monnaie ou "
  "seulement son prix ?",
  "La monnaie est-elle neutre ? Le voile monétaire des classiques contre la monnaie active "
  "des keynésiens et des post-keynésiens.",
  "Faut-il élargir le mandat de la BCE au climat et à l’emploi, comme le suggère Monnet, ou "
  "s’en tenir à la stabilité des prix ?",
  "La théorie monétaire moderne : libération d’une contrainte artificielle ou négation de la "
  "contrainte d’inflation ?",
  "Les crypto-actifs peuvent-ils devenir une monnaie, ou leur volatilité même les en "
  "empêche-t-elle ?",
 ],
 'lien': [
  {'c': 1, 'p': "Le financement des administrations publiques, la charge de la dette et le "
                "policy mix prolongent directement ce chapitre."},
  {'c': 6, 'p': "Le coût du capital et le financement de l’investissement conditionnent la "
                "croissance potentielle et la transition écologique."},
  {'c': 7, 'p': "La hiérarchie monétaire internationale et le péché originel éclairent la "
                "dette en devises des pays en développement."},
  {'c': 21, 'p': "Le dollar comme monnaie de réserve et d’intervention est l’une des clés des "
                 "déséquilibres mondiaux et du privilège exorbitant américain."},
  {'c': 8, 'p': "La financiarisation nourrit le capitalisme actionnarial et la gouvernance "
                "d’entreprise."},
 ],
 'min': [
  "Trois fonctions (Aristote), une confiance ; 91 % de monnaie scripturale en zone euro.",
  "« Les crédits font les dépôts » : la monnaie est endogène, détruite au remboursement.",
  "MV = PT (Fisher) : identité comptable, théorie seulement sous hypothèses fortes.",
  "Trois taux directeurs formant un corridor ; cible d’inflation de 2 % à moyen terme.",
  "Quatre canaux de transmission : taux, prix des actifs, anticipations, taux de change.",
  "Après 2008 : QE, qualitative easing, forward guidance, LTRO/TLTRO — et aléa moral.",
  "Les trois D de Bourguinat font passer de l’économie d’endettement à l’économie de marchés "
  "financiers.",
  "Titrisation, CDO, CDS, shadow banking, too big to fail : le risque est dispersé, pas "
  "supprimé.",
 ],
}

# =========================================================== CHAPITRE 3
R['3'] = {
 'q': "Comment les grands courants de la pensée économique répondent-ils différemment à une "
      "même question — le marché peut-il s’autoréguler et produire une croissance durable ?",
 'ess':
  "Le chapitre est une histoire raisonnée, non un catalogue. Les mercantilistes identifient "
  "la richesse aux métaux précieux et à l’excédent commercial ; les physiocrates la déplacent "
  "vers la terre et inventent, avec Quesnay, le premier circuit économique. Les classiques "
  "déplacent à nouveau la source de la valeur vers le travail : Smith, optimiste, mise sur la "
  "division du travail et la main invisible ; Ricardo et Malthus, pessimistes, annoncent "
  "l’état stationnaire et le piège démographique. Marx retourne la valeur-travail contre le "
  "capitalisme en y lisant l’exploitation. La révolution marginaliste fonde la valeur sur "
  "l’utilité et construit l’équilibre général, que la critique interne de Sonnenschein, "
  "Mantel et Debreu fragilisera. Keynes rompt en 1936 : la demande effective, et non l’offre, "
  "détermine l’emploi. Les courants contemporains héritent de ces lignes de fracture.",
 'idees': [
  {'t': "I. Avant les classiques : mercantilistes et physiocrates",
   'd': "Du XVIᵉ au XVIIIᵉ siècle, les mercantilistes identifient la richesse aux métaux "
        "précieux : il faut exporter plus qu’on n’importe, d’où le colbertisme et ses "
        "manufactures d’État. Mandeville renverse la morale : les vices privés font le bien "
        "public. Les physiocrates déplacent la richesse vers l’agriculture : seule la terre "
        "produit un produit net. Quesnay construit le Tableau économique (1758, version "
        "définitive 1766), premier modèle de circuit, qui répartit la société en trois classes "
        "— productive, stérile, propriétaires — et distingue trois types d’avances. De "
        "Gournay vient le « laissez faire, laissez passer ».",
   'v': "La richesse vient-elle vraiment de la terre ? Smith répond qu’elle vient du travail."},
  {'t': "II. Les classiques : du travail comme source de valeur à l’état stationnaire",
   'd': "Smith (1776) fonde la valeur sur le travail et la croissance sur la division du "
        "travail — l’atelier d’épingles passe de 20 à 4 800 épingles par ouvrier — tandis que "
        "la main invisible fait converger intérêts privés et bien commun. Say ajoute la loi "
        "des débouchés : l’offre crée sa propre demande, donc pas de surproduction durable. "
        "Mais le courant se scinde : Ricardo (1817) montre que la mise en culture de terres "
        "moins fertiles fait baisser les rendements, monter la rente et les salaires, donc "
        "chuter le taux de profit jusqu’à l’état stationnaire ; il fonde aussi la théorie des "
        "avantages comparatifs. Malthus (1798, remanié 1803) décrit un piège démographique et, "
        "contre Say, soutient que la demande peut manquer.",
   'v': "Si la valeur vient du travail, que devient le profit ? Marx en fait une question "
        "d’exploitation."},
  {'t': "III. Marx : la valeur-travail retournée contre le capitalisme",
   'd': "La valeur d’un bien est la quantité de travail socialement nécessaire ; la plus-value "
        "est l’écart entre la valeur créée par le travailleur et son salaire : l’exploitation "
        "est donc inscrite dans le rapport salarial, non dans une injustice accidentelle. Le "
        "matérialisme historique lit l’histoire par les rapports de production et les luttes "
        "de classes, et annonce des crises de surproduction, la concentration du capital et la "
        "baisse tendancielle du taux de profit.",
   'v': "La réponse théorique à Marx ne viendra pas d’une défense morale du profit, mais d’un "
        "changement complet de fondement de la valeur."},
  {'t': "IV. La révolution marginaliste et les néoclassiques",
   'd': "Entre 1871 et 1874, Jevons, Menger et Walras fondent la valeur non plus sur le coût "
        "de production mais sur l’utilité marginale (loi de Gossen) ; Marshall (1890) "
        "réconcilie offre et demande comme les deux lames d’une paire de ciseaux. Walras "
        "construit l’équilibre général, dont Arrow et Debreu démontreront l’existence sous "
        "sept conditions très restrictives. L’équilibre walrassien est un optimum de Pareto : "
        "efficace, mais pas nécessairement juste.",
   'v': "La critique la plus forte de ce modèle viendra de l’intérieur, avant que Keynes ne "
        "déplace complètement la question."},
  {'t': "V. Keynes et la rupture de 1936",
   'd': "Dans la Théorie générale, le niveau d’emploi est déterminé par la demande effective, "
        "c’est-à-dire la demande anticipée par les entrepreneurs : une économie peut donc "
        "s’installer durablement dans un équilibre de sous-emploi avec chômage involontaire. "
        "La trappe à liquidité rend la politique monétaire inefficace, ce qui justifie la "
        "politique budgétaire — « à long terme, nous serons tous morts ». Keynes range sous "
        "l’étiquette « classiques » tous ceux qui croient à l’autorégulation.",
   'v': "La rupture n’est pas la fin de l’histoire : elle ouvre un siècle de synthèses et de "
        "contre-offensives."},
  {'t': "VI. Les prolongements contemporains",
   'd': "Les nouveaux keynésiens fondent microéconomiquement les rigidités : coûts de "
        "changement des prix chez Mankiw, asymétries d’information, concurrence imparfaite ; "
        "Clower distingue demande notionnelle et demande effective, Malinvaud sépare chômage "
        "keynésien et chômage classique — ce qui détermine l’efficacité d’une relance. "
        "L’institutionnalisme, de Veblen (1904) aux travaux contemporains, insiste sur les "
        "règles et les comportements collectifs. Le courant du Public Choice (Buchanan, "
        "Stigler) retourne l’analyse vers les défaillances de l’État.",
   'v': "Les cinq grands courants du chapitre ne se succèdent pas : ils continuent de "
        "s’affronter sur la même question initiale."},
 ],
 'ae': [
  {'n': "François Quesnay, Tableau économique (1758)", 'k': 'a',
   'i': "Le premier circuit économique : trois classes, trois types d’avances, un produit net "
        "d’origine agricole."},
  {'n': "Bernard de Mandeville, La Fable des abeilles", 'k': 'a',
   'i': "« Vices privés, bénéfices publics » : la prospérité naît de la dépense, non de "
        "l’épargne vertueuse."},
  {'n': "Adam Smith, Richesse des nations (1776)", 'k': 'a',
   'i': "Division du travail et main invisible : la coordination marchande sans intention "
        "collective."},
  {'n': "David Ricardo, Principes (1817)", 'k': 'a',
   'i': "Rendements décroissants, rente différentielle, baisse tendancielle du taux de profit "
        "et état stationnaire — et avantages comparatifs."},
  {'n': "Thomas Malthus, Essai sur le principe de population (1798)", 'k': 'a',
   'i': "Le piège démographique, et contre Say l’idée que la demande peut faire défaut : "
        "Keynes le reconnaîtra comme précurseur."},
  {'n': "Jean-Baptiste Say", 'k': 'a',
   'i': "La loi des débouchés : l’offre crée sa propre demande, cible explicite de Keynes."},
  {'n': "Karl Marx", 'k': 'a',
   'i': "Valeur-travail, plus-value et matérialisme historique : le capitalisme produit ses "
        "propres contradictions."},
  {'n': "Walras, Jevons, Menger (1871-1874), puis Marshall (1890)", 'k': 'a',
   'i': "La révolution marginaliste : la valeur vient de l’utilité marginale, et l’équilibre "
        "général devient l’horizon de la discipline."},
  {'n': "Arrow et Debreu", 'k': 'a',
   'i': "L’existence de l’équilibre général est démontrable, mais sous sept conditions très "
        "restrictives."},
  {'n': "Sonnenschein, Mantel et Debreu (1972-1974)", 'k': 'a',
   'i': "Critique interne décisive : l’existence d’un équilibre ne garantit ni sa stabilité "
        "ni la convergence vers lui."},
  {'n': "John Maynard Keynes, Théorie générale (1936)", 'k': 'a',
   'i': "La demande effective détermine l’emploi : l’équilibre de sous-emploi est possible."},
  {'n': "Thorstein Veblen, Théorie de l’entreprise d’affaires (1904)", 'k': 'a',
   'i': "L’institutionnalisme : les comportements économiques sont encastrés dans des règles "
        "et des rapports de prestige."},
  {'n': "L’atelier d’épingles de Smith", 'k': 'e',
   'i': "20 épingles par ouvrier sans division du travail, 4 800 avec : la productivité est "
        "une affaire d’organisation."},
  {'n': "Le Portugal et l’Angleterre, le vin et le drap", 'k': 'e',
   'i': "L’exemple canonique de l’avantage comparatif, repris tel quel en deuxième année."},
 ],
 'arg': [
  "Les courants ne se distinguent pas d’abord par leurs conclusions politiques mais par leur "
  "théorie de la valeur : travail chez les classiques et Marx, utilité chez les néoclassiques.",
  "Le clivage optimistes / pessimistes traverse le courant classique lui-même : Smith contre "
  "Ricardo et Malthus — une nuance qui évite de parler des « classiques » en bloc.",
  "La critique la plus solide de l’équilibre général est interne (Sonnenschein-Mantel-Debreu) : "
  "c’est un argument bien plus fort qu’une critique externe de l’irréalisme des hypothèses.",
  "Keynes ne nie pas le marché : il montre qu’un équilibre peut être atteint avec du chômage "
  "involontaire, ce qui déplace le débat de l’existence de l’équilibre vers son niveau.",
  "La distinction de Malinvaud entre chômage keynésien et chômage classique permet de ne pas "
  "répondre mécaniquement « relance » à toute question de chômage.",
 ],
 'deb': [
  "Le marché s’autorégule-t-il ? Main invisible et loi de Say contre demande effective et "
  "équilibre de sous-emploi.",
  "D’où vient la valeur : du travail incorporé ou de l’utilité marginale perçue ?",
  "La croissance est-elle durable ou conduit-elle à un état stationnaire ? Ricardo, Malthus, "
  "et la reprise contemporaine de la question par l’écologie.",
  "Le modèle d’équilibre général est-il un outil de référence ou un cadre dont la critique "
  "interne a montré les limites ?",
  "L’État corrige-t-il les défaillances du marché, ou ajoute-t-il les siennes (Public "
  "Choice) ?",
 ],
 'lien': [
  {'c': 4, 'p': "L’utilité marginale, la CPP et l’équilibre général y sont formalisés : le "
                "chapitre 4 est la mise en équations du courant néoclassique."},
  {'c': 5, 'p': "Les défaillances de marché donnent le contenu microéconomique de la critique "
                "de l’autorégulation."},
  {'c': 23, 'p': "Ricardo et les avantages comparatifs ouvrent toute l’analyse du commerce "
                 "international de deuxième année."},
  {'c': 6, 'p': "L’état stationnaire de Ricardo et la question des limites réapparaissent dans "
                "le débat croissance / soutenabilité."},
  {'c': 1, 'p': "Keynes y fournit la fonction de consommation, le multiplicateur et la "
                "justification de l’intervention budgétaire."},
 ],
 'min': [
  "Cinq grands courants : classique, marxiste, néoclassique, institutionnaliste, keynésien.",
  "Mercantilistes : la richesse est dans les métaux et l’excédent commercial (XVIᵉ-XVIIIᵉ).",
  "Quesnay (1758) : premier circuit, trois classes, produit net agricole.",
  "Smith (1776) optimiste ; Ricardo (1817) et Malthus (1798) pessimistes : l’état stationnaire "
  "et le piège démographique.",
  "Marx : valeur-travail, plus-value, matérialisme historique.",
  "1871-1874 : révolution marginaliste ; Walras construit l’équilibre général, optimum de "
  "Pareto.",
  "Keynes (1936) : la demande effective détermine l’emploi ; équilibre de sous-emploi.",
  "Sonnenschein-Mantel-Debreu (1972-1974) : l’équilibre existe, mais rien ne garantit qu’on "
  "l’atteigne.",
 ],
}

# =========================================================== CHAPITRE 4
R['4'] = {
 'q': "Le modèle microéconomique standard — un consommateur et un producteur rationnels sur "
      "des marchés concurrentiels — décrit-il réellement les comportements et aboutit-il à un "
      "équilibre stable ?",
 'ess':
  "Le chapitre construit le modèle standard, puis le démonte méthodiquement. On part du "
  "consommateur : il maximise une utilité sous contrainte de revenu, et l’équilibre se lit "
  "comme un point de tangence où le taux marginal de substitution égale le rapport des prix. "
  "Les élasticités traduisent ce comportement en termes mesurables et font apparaître les "
  "premiers cas rebelles, biens de Giffen et de Veblen. On passe ensuite au producteur : "
  "rendements factoriels à court terme, rendements d’échelle à long terme, famille de coûts, "
  "seuils de rentabilité et de fermeture, et la règle P = Cm en concurrence pure et parfaite. "
  "L’agrégation conduit à l’équilibre général d’Arrow-Debreu, dont la critique interne "
  "Sonnenschein-Mantel-Debreu montre qu’il n’est ni nécessairement stable ni atteignable. "
  "L’économie comportementale achève de déplacer le modèle.",
 'idees': [
  {'t': "I. L’homo œconomicus et la démarche microéconomique",
   'd': "La microéconomie part d’un individu théorique : parfaitement rationnel, informé, aux "
        "préférences complètes, transitives, non saturées et convexes. Le cours distingue "
        "d’emblée démarche positive (décrire) et démarche normative (prescrire), distinction "
        "qui servira à juger les conclusions du modèle.",
   'v': "Ces hypothèses posées, on peut représenter le choix du consommateur."},
  {'t': "II. Le consommateur : utilité, courbes d’indifférence et équilibre",
   'd': "La loi de Gossen énonce que l’utilité marginale décroît : la courbe d’utilité est "
        "croissante et concave. Les courbes d’indifférence réunissent les paniers de même "
        "satisfaction ; elles sont décroissantes, convexes et ne se croisent jamais — sans "
        "quoi la transitivité serait violée. Leur pente est le taux marginal de substitution, "
        "nécessairement négatif. La contrainte budgétaire PxX + PyY = R a pour pente −Px/Py : "
        "l’équilibre est le point de tangence, où TMS = Px/Py.",
   'v': "Pour sortir du graphique et mesurer les comportements, il faut des élasticités."},
  {'t': "III. Les élasticités et les cas limites",
   'd': "L’élasticité-prix mesure la sensibilité de la demande au prix : élastique si "
        "|e| > 1, inélastique si |e| < 1, et plus forte à long terme, le temps que des "
        "substituts apparaissent. L’élasticité-revenu classe les biens : inférieur (e < 0), "
        "normal (0 < e < 1), supérieur (e > 1), ce qui rejoint la loi d’Engel. L’élasticité "
        "croisée distingue substituables (positive) et complémentaires (négative). Une baisse "
        "de prix se décompose en effet de substitution et effet de revenu. Deux cas "
        "contredisent la loi de la demande : le bien de Giffen, par extrême pauvreté, et le "
        "bien de Veblen, par distinction sociale.",
   'v': "Le même raisonnement marginaliste s’applique désormais à celui qui produit."},
  {'t': "IV. Le producteur : rendements, coûts et seuils",
   'd': "À court terme, un seul facteur varie : la productivité marginale croît puis décroît "
        "(rendements factoriels décroissants). À long terme, tous les facteurs varient : les "
        "rendements d’échelle sont croissants, constants ou décroissants. De là découle la "
        "famille des coûts — total, moyen, variable moyen, marginal — et deux seuils à ne pas "
        "confondre : le seuil de rentabilité, où le profit s’annule, et le seuil de fermeture, "
        "atteint si le prix passe sous le coût variable moyen. En concurrence pure et "
        "parfaite, le producteur est preneur de prix et produit jusqu’à P = Cm.",
   'v': "Reste à savoir si tous ces équilibres partiels peuvent tenir ensemble."},
  {'t': "V. De l’équilibre partiel à l’équilibre général — et sa critique interne",
   'd': "La concurrence pure et parfaite suppose cinq conditions : atomicité, homogénéité, "
        "libre entrée et sortie, transparence, mobilité des facteurs. Walras pose la question "
        "de la compatibilité simultanée de tous les marchés ; Arrow et Debreu démontrent "
        "l’existence d’un équilibre sous sept conditions. Mais le théorème de Sonnenschein, "
        "repris par Mantel et Debreu puis par Keen, établit que la demande agrégée peut "
        "prendre presque n’importe quelle forme : l’existence n’entraîne ni l’unicité, ni la "
        "stabilité, ni la convergence.",
   'v': "Si le modèle vacille de l’intérieur, l’observation des comportements réels achève de "
        "le déplacer."},
  {'t': "VI. Les limites comportementales du modèle",
   'd': "Simon oppose rationalité substantielle et rationalité procédurale : faute "
        "d’information, de temps et de capacités, les agents cherchent une solution "
        "satisfaisante plutôt qu’optimale. Kahneman distingue un Système 1 rapide et intuitif "
        "d’un Système 2 lent et coûteux, d’où des biais systématiques — confirmation, ancrage. "
        "Thaler en tire le nudge, qui modifie l’architecture des choix sans contraindre. "
        "Raworth conteste enfin la non-satiété en proposant un plancher social et un plafond "
        "écologique.",
   'v': "Le chapitre ne détruit pas le modèle standard : il en fait un point de départ dont "
        "il faut connaître les conditions de validité."},
 ],
 'ae': [
  {'n': "Hermann Gossen", 'k': 'a',
   'i': "L’utilité marginale décroissante, fondement de toute la représentation des "
        "préférences."},
  {'n': "Léon Walras", 'k': 'a',
   'i': "L’équilibre général : tous les marchés s’équilibrent simultanément."},
  {'n': "Kenneth Arrow et Gérard Debreu", 'k': 'a',
   'i': "L’existence de l’équilibre est démontrée, mais au prix de sept hypothèses très "
        "exigeantes."},
  {'n': "Hugo Sonnenschein, Rolf Mantel, Gérard Debreu (1972-1974)", 'k': 'a',
   'i': "La critique interne : ni stabilité ni convergence garanties — argument décisif en "
        "dissertation."},
  {'n': "Steve Keen", 'k': 'a',
   'i': "Reprise contemporaine du théorème pour contester la légitimité du modèle standard."},
  {'n': "Herbert Simon", 'k': 'a',
   'i': "Rationalité limitée : on « satisfait » au lieu de maximiser, par rationalité "
        "procédurale."},
  {'n': "Daniel Kahneman (2011)", 'k': 'a',
   'i': "Système 1 et Système 2 : les biais cognitifs ne sont pas des accidents mais la règle."},
  {'n': "Richard Thaler (Nobel 2017)", 'k': 'a',
   'i': "Le nudge : orienter les comportements sans interdire ni obliger."},
  {'n': "George Akerlof (1970)", 'k': 'a',
   'i': "L’asymétrie d’information suffit à faire échouer un marché pourtant concurrentiel."},
  {'n': "Kate Raworth, l’économie du donut", 'k': 'a',
   'i': "Contre la non-satiété : un plancher social et un plafond écologique encadrent "
        "l’activité."},
  {'n': "Le don d’organes par défaut", 'k': 'e',
   'i': "Une case déjà cochée change massivement le comportement : la preuve empirique du "
        "nudge."},
  {'n': "Le marché des voitures d’occasion", 'k': 'e',
   'i': "L’exemple des lemons, repris au chapitre 5 : la qualité invisible évince les bons "
        "produits."},
 ],
 'arg': [
  "L’équilibre du consommateur n’est pas une description psychologique mais une condition "
  "mathématique : TMS = Px/Py, à citer précisément plutôt qu’à paraphraser.",
  "La distinction seuil de rentabilité / seuil de fermeture permet d’expliquer qu’une "
  "entreprise continue de produire à perte à court terme — un argument souvent décisif.",
  "Critiquer l’équilibre général par son irréalisme est faible ; le critiquer par "
  "Sonnenschein-Mantel-Debreu est fort, car la critique est interne au cadre lui-même.",
  "Les biens de Giffen et de Veblen ne sont pas des curiosités : ils montrent que la loi de la "
  "demande dépend du contexte social, pas seulement du calcul.",
  "L’économie comportementale ne remplace pas le modèle standard, elle en déplace la frontière "
  "de validité : c’est la nuance attendue en copie.",
 ],
 'deb': [
  "L’homo œconomicus est-il une hypothèse de travail utile ou une description fausse qui "
  "fausse les conclusions ?",
  "Le marché conduit-il à un optimum ? Optimum de Pareto, critère de Hicks-Kaldor, et la "
  "distinction entre efficacité et justice.",
  "Le nudge est-il une politique publique respectueuse de la liberté ou une manipulation des "
  "choix ?",
  "La concurrence pure et parfaite est-elle un idéal normatif ou un simple point de "
  "référence analytique ?",
 ],
 'lien': [
  {'c': 3, 'p': "Ce chapitre formalise le courant néoclassique issu de la révolution "
                "marginaliste de 1871-1874."},
  {'c': 5, 'p': "Les cinq conditions de la CPP servent de grille aux quatre défaillances de "
                "marché : chaque défaillance est la violation d’une condition."},
  {'c': 9, 'p': "L’abandon de l’atomicité ouvre l’analyse de la concurrence imparfaite, du "
                "pouvoir de marché et des oligopoles."},
  {'c': 10, 'p': "La rationalité limitée de Simon irrigue la sociologie des organisations et "
                 "l’analyse des décisions absurdes."},
  {'c': 1, 'p': "Les élasticités et la loi d’Engel éclairent la structure de la consommation "
                "des ménages et les dépenses pré-engagées."},
 ],
 'min': [
  "Préférences : complètes, transitives, non saturées, convexes ; utilité marginale "
  "décroissante (Gossen).",
  "Équilibre du consommateur : TMS = Px/Py, tangence entre contrainte budgétaire et courbe "
  "d’indifférence.",
  "Élasticité-prix |e| > 1 ou < 1 ; élasticité-revenu e < 0, 0 < e < 1, e > 1 ; croisée "
  "positive ou négative.",
  "Giffen (pauvreté) et Veblen (distinction) : deux exceptions à la loi de la demande.",
  "Court terme : rendements factoriels ; long terme : rendements d’échelle. Seuil de "
  "rentabilité ≠ seuil de fermeture (P < CVM).",
  "CPP : cinq conditions, et la règle P = Cm.",
  "Arrow-Debreu : sept conditions pour l’existence ; Sonnenschein-Mantel-Debreu : ni "
  "stabilité ni convergence.",
  "Simon, Kahneman, Thaler : rationalité limitée, biais, nudge.",
 ],
}

# =========================================================== CHAPITRE 5
R['5'] = {
 'q': "Quand le marché concurrentiel échoue-t-il à allouer efficacement les ressources, et "
      "qui — l’État, le marché lui-même ou la communauté — est le mieux placé pour y "
      "remédier ?",
 'ess':
  "Le chapitre répond d’abord non à la question de l’efficacité systématique du marché, puis "
  "organise cette réponse en quatre défaillances, chacune correspondant à la violation d’une "
  "condition de la concurrence pure et parfaite. Le monopole naturel détruit l’atomicité et "
  "crée une perte sèche. Les biens collectifs échappent à l’excluabilité et au passager "
  "clandestin. Les externalités brisent l’égalité entre coût privé et coût social. Les "
  "asymétries d’information ruinent la transparence et peuvent faire disparaître le marché "
  "lui-même. À chaque fois, le chapitre confronte trois réponses — l’État chez Pigou, le "
  "marché et les droits de propriété chez Coase, la communauté chez Ostrom — avant de "
  "retourner l’analyse contre l’État lui-même : la régulation peut être capturée.",
 'idees': [
  {'t': "I. Le marché concurrentiel est-il toujours efficace ? Non.",
   'd': "La défaillance de marché se définit comme une situation où le marché concurrentiel "
        "n’alloue pas les ressources de façon optimale. Le cours en distingue quatre : "
        "monopole naturel, externalités, biens collectifs, asymétries d’information. Chacune "
        "s’analyse comme la violation d’une condition de la concurrence pure et parfaite.",
   'v': "On commence par celle qui touche la structure même du marché : le nombre d’offreurs."},
  {'t': "II. Le monopole naturel et le pouvoir de marché",
   'd': "Lorsque les coûts fixes sont très élevés et le coût marginal très faible, les "
        "rendements sont croissants : une seule entreprise produit au moindre coût, et "
        "imposer P = Cm la mettrait en perte. Le monopole réduit les quantités et élève les "
        "prix, d’où une perte sèche — le triangle d’Harberger. C’est une défaillance "
        "structurelle, non un abus : eau, électricité, rail. Les effets de réseau produisent "
        "aujourd’hui des concentrations comparables dans le numérique.",
   'v': "Certains biens posent un problème plus radical encore : non seulement un seul "
        "producteur, mais aucune possibilité de faire payer."},
  {'t': "III. Les biens collectifs et le passager clandestin",
   'd': "Croiser rivalité et excluabilité donne quatre statuts : bien privé, bien de club "
        "(non rival mais excluable, comme une autoroute à péage), bien commun, bien collectif "
        "(ni rival ni excluable, comme la défense ou un phare). Pour ce dernier, chacun a "
        "intérêt à profiter sans payer : c’est le passager clandestin qu’Olson théorise en "
        "1965, et la production privée devient non rentable. Seul l’impôt obligatoire résout "
        "le problème. Le statut d’un bien n’est pas figé : la technique et la décision "
        "politique le déplacent.",
   'v': "Le même raisonnement s’applique lorsque l’activité d’un agent affecte les autres sans "
        "passer par un prix."},
  {'t': "IV. Les externalités et la gestion des communs : Pigou, Coase, Ostrom",
   'd': "Une externalité négative fait que le coût privé est inférieur au coût social, d’où "
        "une surproduction ; une externalité positive conduit symétriquement à une "
        "sous-production. Pigou propose d’internaliser par la taxe ou la subvention. Coase "
        "répond que, si les droits de propriété sont bien définis et les coûts de transaction "
        "nuls, les agents négocient eux-mêmes l’optimum — d’où les marchés de quotas. Hardin "
        "(1968) décrit la tragédie des communs ; Ostrom montre empiriquement que des "
        "communautés élaborent des arrangements institutionnels efficaces, surtout en deçà "
        "d’une centaine de personnes. Heller (1998) ajoute la tragédie des anti-communs : "
        "trop de droits de propriété bloquent l’usage, comme pour les brevets.",
   'v': "Reste la défaillance la plus insidieuse : non pas ce que les agents font, mais ce "
        "qu’ils ignorent."},
  {'t': "V. Les asymétries d’information",
   'd': "Akerlof (1970) montre avec le marché des voitures d’occasion que, si la qualité est "
        "invisible, le prix unique chasse les bons produits : c’est la sélection adverse, "
        "forme générale de la loi de Gresham. L’aléa moral intervient après le contrat : "
        "l’assuré prend plus de risques. Les réponses sont le signalement coûteux à imiter "
        "(Spence : le diplôme), la franchise, le bonus-malus, la certification, la garantie "
        "légale de conformité.",
   'v': "Si le marché défaille, l’intervention publique s’impose-t-elle pour autant ?"},
  {'t': "VI. Les défaillances de l’État",
   'd': "Le courant du Public Choice retourne l’analyse : les acteurs publics maximisent aussi "
        "leur intérêt. Stigler (1971) décrit la capture réglementaire, où le régulateur finit "
        "par servir les régulés ; Tullock analyse la recherche de rente, privément rentable et "
        "socialement stérile. Les trois solutions — État, marché, communauté — ne s’excluent "
        "donc pas : elles se choisissent selon le contexte.",
   'v': "La conclusion du chapitre est une règle de méthode : à chaque défaillance "
        "correspondent plusieurs remèdes, dont aucun n’est universel."},
 ],
 'ae': [
  {'n': "Arthur Pigou, L’économie du bien-être (années 1920)", 'k': 'a',
   'i': "Internaliser l’externalité par la taxe ou la subvention : la solution par l’État."},
  {'n': "Ronald Coase", 'k': 'a',
   'i': "Avec des droits de propriété définis et des coûts de transaction faibles, la "
        "négociation privée atteint l’optimum sans l’État."},
  {'n': "Garrett Hardin (1968)", 'k': 'a',
   'i': "La tragédie des communs : l’intérêt individuel épuise la ressource partagée."},
  {'n': "Elinor Ostrom (Nobel 2009)", 'k': 'a',
   'i': "Contre Hardin : des communautés gèrent durablement les communs par des règles, des "
        "tours de rôle et des sanctions graduées."},
  {'n': "Mancur Olson, Logique de l’action collective (1965)", 'k': 'a',
   'i': "Le passager clandestin rend la production privée d’un bien collectif non rentable."},
  {'n': "George Akerlof, The Market for Lemons (1970)", 'k': 'a',
   'i': "La sélection adverse : l’asymétrie d’information peut faire disparaître le marché."},
  {'n': "Michael Spence", 'k': 'a',
   'i': "Le signalement : un diplôme est crédible parce qu’il est coûteux à imiter."},
  {'n': "Michael Heller (1998)", 'k': 'a',
   'i': "La tragédie des anti-communs : trop de droits de propriété paralysent l’innovation."},
  {'n': "George Stigler (1971) et James Buchanan", 'k': 'a',
   'i': "Capture réglementaire et Public Choice : l’État a aussi ses défaillances."},
  {'n': "La taxe carbone britannique (2013)", 'k': 'e',
   'i': "La part du charbon dans l’électricité passe de 40 % en 2012 à 4 % en 2019 : une taxe "
        "pigouvienne qui fonctionne."},
  {'n': "Le brevet, exclusivité de 20 ans", 'k': 'e',
   'i': "Un monopole temporaire volontairement créé pour corriger la sous-production "
        "d’innovation — et, poussé trop loin, une tragédie des anti-communs."},
  {'n': "Les communs numériques : Linux, Wikipédia", 'k': 'e',
   'i': "Le cadre d’Ostrom s’applique à des ressources immatérielles gouvernées "
        "collectivement."},
 ],
 'arg': [
  "Chaque défaillance est la violation d’une condition de la CPP : c’est le fil qui relie ce "
  "chapitre au chapitre 4 et qui structure une dissertation.",
  "Le monopole naturel n’est pas un abus mais une donnée technique : le débat porte sur le "
  "mode de régulation, pas sur l’opportunité du monopole.",
  "Pigou, Coase et Ostrom ne s’opposent pas terme à terme : ils supposent des coûts de "
  "transaction et des tailles de communauté différents.",
  "La sélection adverse (avant le contrat) et l’aléa moral (après) ne se traitent pas avec les "
  "mêmes instruments : confondre les deux coûte cher en copie.",
  "Reconnaître les défaillances du marché n’implique pas l’efficacité de l’État : capture "
  "réglementaire et recherche de rente imposent la symétrie de l’analyse.",
 ],
 'deb': [
  "Taxer ou créer un marché de droits : la taxe pigouvienne fixe le prix, le marché de quotas "
  "fixe la quantité — lequel est préférable sous incertitude ?",
  "Les communs doivent-ils être privatisés, nationalisés ou gouvernés collectivement ? Hardin "
  "contre Ostrom.",
  "Faut-il marchandiser la nature pour la protéger, ou cette marchandisation détruit-elle la "
  "valeur qu’on prétend défendre ?",
  "Le brevet encourage-t-il l’innovation ou la bloque-t-il ? Monopole d’incitation contre "
  "enclosures de la connaissance.",
  "L’État est-il un correcteur neutre ou un acteur intéressé comme les autres ?",
 ],
 'lien': [
  {'c': 4, 'p': "Le chapitre est le négatif du précédent : chaque condition de la CPP y est "
                "levée une à une."},
  {'c': 9, 'p': "Pouvoir de marché, barrières à l’entrée et politique de la concurrence "
                "prolongent l’analyse du monopole."},
  {'c': 1, 'p': "Les trois fonctions de Musgrave donnent la traduction budgétaire de la "
                "correction des défaillances."},
  {'c': 7, 'p': "Climat, haute mer et biens communs mondiaux transposent Hardin et Ostrom à "
                "l’échelle planétaire."},
  {'c': 6, 'p': "Externalités positives de la connaissance et brevets éclairent les théories "
                "de la croissance endogène."},
 ],
 'min': [
  "Quatre défaillances : monopole naturel, externalités, biens collectifs, asymétries "
  "d’information.",
  "Monopole naturel : rendements croissants, perte sèche (triangle d’Harberger), P = Cm "
  "impossible sans pertes.",
  "Rivalité × excluabilité : bien privé, bien de club, bien commun, bien collectif ; passager "
  "clandestin (Olson, 1965).",
  "Externalité négative : coût privé < coût social → surproduction. Solution Pigou : la taxe.",
  "Coase : droits de propriété + coûts de transaction faibles → négociation privée.",
  "Hardin (1968) contre Ostrom (Nobel 2009) ; Heller (1998) : tragédie des anti-communs.",
  "Akerlof (1970) : sélection adverse avant le contrat ; aléa moral après ; Spence : le "
  "signalement.",
  "Public Choice : capture réglementaire (Stigler, 1971), recherche de rente — l’État défaille "
  "aussi.",
 ],
}
