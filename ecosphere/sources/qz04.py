# -*- coding: utf-8 -*-
"""Chapitre 4 — Analyse microéconomique (I) : le consommateur."""

SP = {
 'c4-01': 'Préférences, courbes d’indifférence et taux marginal de substitution',
 'c4-02': 'Les élasticités de la demande',
 'c4-03': 'La théorie du producteur : rendements, productivité et coûts',
 'c4-04': 'De l’équilibre partiel à l’équilibre général',
 'c4-05': 'L’équilibre existe-t-il ? Arrow-Debreu et Sonnenschein-Mantel-Debreu',
 'c4-06': 'Rationalité limitée, biais cognitifs et économie comportementale',
}

DROP = []


def f(**kw):
    return kw


FIX = {

# ================================ c4-01 · préférences et courbes d'indifférence
'ch4-qcm-1': f(niv='connaitre', sp='c4-01',
 exp="Walras est le marginaliste cité en ouverture : il veut mettre "
     "l’économie en équation pour lui donner la rigueur des sciences "
     "naturelles. Ce projet de formalisation est l’acte de naissance de la "
     "microéconomie moderne.",
 why=["Marshall formalise l’équilibre partiel, mais le projet d’une "
      "économie mathématisée est associé à Walras.",
      "Pigou travaille sur le bien-être et les externalités.",
      "Pareto prolonge Walras sur l’optimum, il n’en est pas l’initiateur."]),

'ch4-qcm-3': f(niv='connaitre', sp='c4-01',
 exp="Une courbe d’indifférence relie toutes les combinaisons de deux biens "
     "qui procurent le même niveau de satisfaction : le consommateur est "
     "donc indifférent entre tous les points de la courbe. Sa pente est le "
     "taux marginal de substitution.",
 why=["L’évolution du revenu dans le temps est une série chronologique.",
      "La contrainte budgétaire est une droite, distincte de la courbe "
      "d’indifférence.",
      "La relation utilité-prix n’est pas représentée par cette courbe."]),

'ch4-qcm-4': f(niv='connaitre', sp='c4-01',
 exp="La non-satiété signifie que le consommateur préfère toujours "
     "davantage : aucun panier n’est jamais « assez ». C’est elle qui rend "
     "les courbes d’indifférence éloignées de l’origine préférables, et qui "
     "garantit que la contrainte budgétaire est saturée à l’optimum.",
 why=["La rationalité est une autre hypothèse : elle porte sur la cohérence "
      "des choix.",
      "La décroissance de la satisfaction est la loi de Gossen, qui porte "
      "sur l’utilité marginale, non sur la non-satiété.",
      "Le revenu illimité contredirait la contrainte budgétaire."],
 diss="C’est l’hypothèse que Kate Raworth conteste : dans un monde aux "
      "limites écologiques, « toujours plus » cesse d’être une description "
      "innocente du comportement."),

'ch4-qcm-5': f(niv='connaitre', sp='c4-01',
 exp="La transitivité exige que les préférences s’enchaînent sans "
     "contradiction : si A est préféré à B et B à C, alors A doit être "
     "préféré à C. C’est elle qui interdit aux courbes d’indifférence de se "
     "croiser.",
 why=["Pouvoir se prononcer sur toute combinaison est l’hypothèse de "
      "complétude.",
      "La variation progressive renvoie à la continuité.",
      "La divisibilité infinie est également l’hypothèse de continuité."]),

'ch4-qcm-6': f(niv='connaitre', sp='c4-01',
 exp="Steve Keen publie L’imposture économique (2014) : il y reproche à la "
     "microéconomie standard son abstraction et son éloignement des "
     "comportements réels. Le cours l’utilise pour introduire la critique "
     "interne des hypothèses.",
 why=["Samuelson est un des grands formalisateurs de l’économie standard.",
      "Raworth critique la non-satiété et la croissance, dans un autre "
      "ouvrage.",
      "Walras est l’un des fondateurs du programme critiqué."]),

'ch4-qcm-7': f(niv='connaitre', sp='c4-01',
 exp="Le taux marginal de substitution mesure le nombre d’unités d’un bien "
     "auxquelles on renonce pour obtenir une unité supplémentaire de "
     "l’autre, en restant au même niveau de satisfaction. C’est la pente de "
     "la courbe d’indifférence, donc un arbitrage subjectif.",
 why=["L’inflation appliquée au revenu n’a aucun rapport.",
      "Le rapport des prix est la pente de la droite de budget : il n’est "
      "égal au TMS qu’à l’optimum.",
      "La pente de la contrainte budgétaire est précisément cet autre "
      "objet."]),

'ch4-qcm-8': f(niv='comprendre', sp='c4-01',
 exp="Le TMS est négatif parce qu’il traduit un renoncement : pour rester "
     "sur la même courbe d’indifférence, toute unité gagnée d’un bien doit "
     "être compensée par une perte sur l’autre. La courbe est donc "
     "décroissante.",
 why=["La relation entre consommation et revenu n’intervient pas ici.",
      "La positivité des prix ne détermine pas le signe du TMS.",
      "L’utilité marginale est décroissante, non croissante : c’est "
      "d’ailleurs ce qui rend la courbe convexe."]),

'ch4-qcm-9': f(niv='comprendre', sp='c4-01',
 exp="À l’optimum, le taux auquel le consommateur accepte d’échanger les "
     "deux biens — le TMS — égale le taux auquel le marché le lui permet — "
     "le rapport des prix. Tant que les deux diffèrent, un réarrangement "
     "améliore la satisfaction à budget constant.",
 why=["Égaliser utilité totale et utilité marginale n’a pas de sens "
      "dimensionnel.",
      "L’égalité revenu-dépenses est la contrainte budgétaire saturée : "
      "nécessaire, mais pas suffisante.",
      "L’égalité des prix des deux biens n’a aucune raison d’être vérifiée."],
 diss="Cette condition est le modèle de tout raisonnement marginaliste : "
      "l’optimum est atteint quand le taux d’échange subjectif rejoint le "
      "taux d’échange objectif."),

'ch4-qcm-10': f(niv='connaitre', sp='c4-01',
 exp="La loi de Gossen énonce la décroissance de l’utilité marginale : "
     "chaque unité supplémentaire consommée procure une satisfaction moindre "
     "que la précédente. L’utilité totale continue d’augmenter, mais de "
     "moins en moins vite — elle est croissante et concave.",
 why=["Le lien revenu-consommation est une autre relation.",
      "La baisse de la demande quand le prix monte est la loi de la "
      "demande : elle découle de Gossen, mais ne s’y confond pas.",
      "La relation épargne-revenu relève de la macroéconomie."]),

'ch4-qcm-11': f(niv='comprendre', sp='c4-01',
 exp="L’effet de substitution isole l’effet du changement de prix relatif : "
     "le bien devenu moins cher est substitué à l’autre, à satisfaction "
     "inchangée. On se déplace le long de la même courbe d’indifférence.",
 why=["Acheter moins du bien devenu moins cher contredit la logique de "
      "substitution.",
      "La baisse du revenu réel correspondrait à une hausse de prix, non à "
      "une baisse.",
      "L’épargne n’intervient pas dans ce modèle à deux biens."]),

'ch4-qcm-12': f(niv='appliquer', sp='c4-01',
 exp="Par construction, l’effet de substitution est mesuré à satisfaction "
     "constante : on reste sur la même courbe d’indifférence et l’on se "
     "déplace vers le point où la pente égale le nouveau rapport des prix. "
     "C’est l’effet revenu qui fait changer de courbe.",
 why=["Passer sur une courbe supérieure est l’effet revenu.",
      "Passer sur une courbe inférieure correspondrait à une perte de "
      "pouvoir d’achat, donc encore à l’effet revenu.",
      "Les courbes d’indifférence ne se déplacent pas : elles décrivent des "
      "préférences stables."]),

'ch4-qcm-13': f(niv='appliquer', sp='c4-01',
 exp="Une baisse de prix élève le pouvoir d’achat à revenu nominal "
     "inchangé : c’est l’effet revenu, qui permet d’atteindre une courbe "
     "d’indifférence plus élevée et, pour des biens normaux, d’augmenter la "
     "consommation des deux biens.",
 why=["Le revenu nominal ne change pas : seul le revenu réel augmente.",
      "La baisse du revenu réel correspondrait à une hausse du prix.",
      "La substitution d’un bien à l’autre est l’autre effet, distinct."]),

'ch4-qcm-14': f(niv='connaitre', sp='c4-01',
 exp="La carte du consommateur est l’ensemble de ses courbes "
     "d’indifférence : chacune correspond à un niveau de satisfaction, et "
     "plus elle est éloignée de l’origine, plus ce niveau est élevé. Les "
     "courbes ne se croisent jamais.",
 why=["Un tableau de dépenses est une donnée comptable.",
      "La droite de budget relève des contraintes, non des préférences.",
      "La relation prix-quantité est la courbe de demande, qui se déduit de "
      "la carte."]),

'ch4-qcm-15': f(niv='raisonner', sp='c4-01',
 exp="La continuité est une hypothèse de commodité mathématique : elle "
     "permet de dériver, donc d’écrire des conditions d’optimum. On la "
     "conserve en sachant qu’elle est fausse pour les biens indivisibles — "
     "le cours cite les médicaments vendus par boîtes de trente.",
 why=["La divisibilité réelle de tous les biens est précisément ce qui est "
      "faux.",
      "Le comportement continu des individus n’est pas l’argument.",
      "La continuité des prix est une autre question, indépendante des "
      "préférences."],
 diss="Bon exemple pour traiter du statut des hypothèses : une hypothèse "
      "peut être fausse et utile, à condition que l’on sache ce qu’elle "
      "coûte en réalisme."),

'ch4-qcm-16': f(niv='comprendre', sp='c4-01',
 exp="Les vérifications empiriques montrent que les préférences ne sont pas "
     "toujours cohérentes : les individus peuvent préférer A à B, B à C et "
     "pourtant C à A. Ces cycles de préférences invalident la transitivité "
     "et nourrissent l’économie comportementale.",
 why=["Affirmer la transitivité réelle contredit les observations.",
      "L’incapacité à comparer relève du défaut de complétude.",
      "Le croisement des courbes serait une conséquence, non la cause."]),

'ch4-qcm-17': f(niv='connaitre', sp='c4-01',
 exp="Kate Raworth conteste la non-satiété dans le cadre de l’économie du "
     "donut : un modèle qui suppose un désir illimité est incompatible avec "
     "des limites planétaires. L’hypothèse n’est donc pas neutre, elle "
     "porte une norme.",
 why=["Keen critique l’abstraction générale du modèle, pas spécialement la "
      "non-satiété.",
      "Walras fonde au contraire ce programme.",
      "Pareto en prolonge l’analyse."]),

'ch4-qcm-18': f(niv='connaitre', sp='c4-01',
 exp="L’utilité marginale est la satisfaction supplémentaire procurée par la "
     "dernière unité consommée. C’est elle, et non l’utilité totale, qui "
     "commande la décision d’acheter une unité de plus.",
 why=["La satisfaction totale est l’utilité totale, somme des utilités "
      "marginales.",
      "Le prix d’équilibre résulte de la confrontation offre-demande.",
      "La part du revenu consacrée à un bien est le coefficient "
      "budgétaire."]),

'ch4-qcm-19': f(niv='comprendre', sp='c4-01',
 exp="La courbe d’indifférence représente un arbitrage entre deux biens à "
     "satisfaction donnée ; la courbe d’utilité représente la satisfaction "
     "procurée par les quantités d’un seul bien. L’une raisonne en "
     "substitution, l’autre en niveau.",
 why=["Les deux objets ne se confondent pas : ils n’ont ni les mêmes axes "
      "ni la même lecture.",
      "La dimensionnalité est inversée dans cette proposition.",
      "Aucune des deux courbes ne porte les prix en abscisse."]),

'ch4-qcm-20': f(niv='connaitre', sp='c4-01',
 exp="La complétude signifie que le consommateur sait toujours ordonner deux "
     "paniers : il les préfère ou les juge équivalents, sans jamais être "
     "incapable de se prononcer. C’est une hypothèse forte sur la "
     "connaissance de ses propres goûts.",
 why=["Consommer tout son revenu est une conséquence de la non-satiété.",
      "La disponibilité illimitée des biens n’est pas une hypothèse sur les "
      "préférences.",
      "La maximisation est l’hypothèse de comportement, distincte de la "
      "structure des préférences."]),

'ch4-qcm-21': f(niv='comprendre', sp='c4-01',
 exp="Plus une courbe d’indifférence est éloignée de l’origine, plus les "
     "paniers qu’elle rassemble contiennent de biens : en vertu de la "
     "non-satiété, ils procurent une satisfaction plus élevée. L’objectif du "
     "consommateur est donc d’atteindre la courbe la plus éloignée "
     "compatible avec son budget.",
 why=["Un niveau plus bas correspond aux courbes proches de l’origine.",
      "Le revenu détermine la droite de budget, pas la position des courbes "
      "d’indifférence.",
      "Les prix fixent la pente de la droite de budget, non le niveau de la "
      "courbe atteinte."]),

'ch4-qcm-23': f(niv='connaitre', sp='c4-01',
 exp="Le programme du consommateur est de maximiser son utilité sous "
     "contrainte budgétaire : c’est un problème d’optimisation sous "
     "contrainte, dont la solution est le point de tangence entre la droite "
     "de budget et la plus haute courbe d’indifférence accessible.",
 why=["Minimiser la dépense sans objectif de satisfaction n’a pas de sens "
      "dans ce cadre.",
      "L’épargne n’apparaît pas dans le modèle statique à deux biens.",
      "L’arbitrage consommation-investissement relève d’un autre modèle, "
      "intertemporel."]),

'ch4-qcm-24': f(niv='raisonner', sp='c4-01',
 exp="Si deux courbes se croisaient, le point d’intersection appartiendrait "
     "à deux niveaux de satisfaction différents, ce qui contredirait la "
     "transitivité : on aurait A équivalent à B, B équivalent à C, mais A "
     "préféré à C. La cohérence des préférences interdit donc le "
     "croisement.",
 why=["La complétude dit qu’on peut comparer, non que les comparaisons sont "
      "cohérentes.",
      "La non-satiété ordonne les niveaux, elle ne règle pas la question du "
      "croisement.",
      "La continuité porte sur la divisibilité, non sur la cohérence."]),

'ch4-qcm-25': f(niv='comprendre', sp='c4-01',
 exp="La dérivée dY/dX mesure la pente de la courbe d’indifférence en un "
     "point : c’est le taux marginal de substitution calculé localement. Il "
     "varie le long de la courbe, ce qui traduit la convexité des "
     "préférences.",
 why=["La pente de la droite budgétaire est − Px/Py, et elle est constante.",
      "Le rapport utilité marginale sur utilité totale n’a pas de sens ici.",
      "La variation du revenu face aux prix est un autre objet."]),

'ch4-qcm-26': f(niv='comprendre', sp='c4-01',
 exp="Le projet marginaliste, tel que Walras le formule, est de mettre "
     "l’économie en équation pour lui donner la rigueur des sciences "
     "naturelles. L’individualisme méthodologique et le raisonnement à la "
     "marge en sont les instruments.",
 why=["La réforme fiscale n’est pas l’objectif théorique du programme.",
      "La théorie des classes est marxienne.",
      "L’analyse des cycles relève d’autres traditions."]),

'ch4-qcm-28': f(niv='connaitre', sp='c4-01',
 exp="La droite de budget rassemble toutes les combinaisons accessibles "
     "compte tenu du revenu et des prix : Px·X + Py·Y = R. Sa pente est "
     "− Px/Py, et elle se déplace parallèlement quand le revenu change.",
 why=["Le graphique de l’utilité totale est une autre représentation.",
      "La courbe d’indifférence la plus éloignée est l’objectif, non la "
      "contrainte.",
      "La relation prix-quantité demandée est la courbe de demande."]),

'ch4-qcm-29': f(niv='appliquer', sp='c4-01',
 exp="La droite de budget s’écrit Y = R/Py − (Px/Py)·X : sa pente vaut donc "
     "− Px/Py. Elle mesure le taux d’échange objectif permis par le marché, "
     "que l’optimum égalise au taux subjectif qu’est le TMS.",
 why=["− Py/Px inverse le rapport des prix.",
      "Le produit des prix n’a pas de signification géométrique ici.",
      "R/Px est l’ordonnée à l’origine sur l’axe de X, pas la pente."]),

'ch4-qcm-30': f(niv='appliquer', sp='c4-01',
 exp="Un médicament vendu par boîtes de trente comprimés n’est pas "
     "divisible : on ne peut pas en acheter 1,7 boîte. L’exemple met en "
     "défaut l’hypothèse de continuité, qui suppose des quantités "
     "indéfiniment fractionnables.",
 why=["La complétude concerne la capacité à comparer les paniers.",
      "La transitivité concerne la cohérence des préférences.",
      "La non-satiété concerne la préférence pour des quantités plus "
      "grandes."]),

'ch4-qcm-31': f(niv='appliquer', sp='c4-01',
 exp="La baisse du prix du burger rend la glace relativement plus chère : "
     "l’effet de substitution réduit donc la consommation de glace. Mais le "
     "pouvoir d’achat augmente, et l’effet revenu peut au contraire "
     "l’augmenter. Le résultat net dépend de la force respective des deux "
     "effets.",
 why=["Une hausse systématique ignorerait l’effet de substitution.",
      "Une consommation identique supposerait que les deux effets se "
      "compensent exactement, ce qui n’a aucune raison d’arriver.",
      "L’effet revenu joue ici à la hausse, puisque le pouvoir d’achat "
      "augmente."],
 diss="Savoir décomposer un changement de prix en deux effets de sens "
      "éventuellement contraires est ce qui distingue l’analyse "
      "microéconomique d’une intuition."),

'ch4-qcm-32': f(niv='connaitre', sp='c4-01',
 exp="Le salaire réel est le salaire nominal corrigé du niveau des prix : il "
     "mesure le pouvoir d’achat effectif. Deux salaires nominaux identiques "
     "ne donnent pas le même salaire réel si les prix diffèrent.",
 why=["La correction des cotisations donne le salaire net, notion "
      "comptable.",
      "Le salaire après impôts est encore une autre notion.",
      "Le salaire minimum légal est une norme, non une mesure réelle."]),

'ch4-vf-1': f(niv='connaitre', sp='c4-01',
 exp="C’est l’hypothèse fondatrice du modèle standard : l’Homo œconomicus "
     "est parfaitement rationnel, informé et capable de calcul. Le cours "
     "souligne aussitôt sa fragilité, que l’économie comportementale de "
     "Kahneman et Thaler met en évidence."),

'ch4-vf-2': f(niv='connaitre', sp='c4-01',
 exp="La loi de Gossen énonce la décroissance de l’utilité marginale : la "
     "satisfaction apportée par chaque unité supplémentaire diminue. "
     "L’utilité totale, elle, continue de croître, mais de moins en moins "
     "vite."),

'ch4-vf-3': f(niv='raisonner', sp='c4-01',
 exp="Les courbes d’indifférence ne peuvent jamais se croiser, en vertu de "
     "la transitivité : un point d’intersection appartiendrait à deux "
     "niveaux de satisfaction différents. L’argument porte sur la cohérence "
     "logique des préférences à un instant donné, non sur leur stabilité "
     "dans le temps."),

'ch4-vf-4': f(niv='connaitre', sp='c4-01',
 exp="C’est bien la définition de la complétude : pour tout couple de "
     "paniers, le consommateur sait dire lequel il préfère, ou s’il les juge "
     "équivalents. Aucune indécision n’est admise dans le modèle."),

'ch4-vf-5': f(niv='comprendre', sp='c4-01',
 exp="Le TMS est négatif : il mesure un renoncement, puisque rester sur la "
     "même courbe d’indifférence impose de céder une partie d’un bien pour "
     "en obtenir davantage de l’autre. On raisonne souvent sur sa valeur "
     "absolue, mais le signe traduit l’arbitrage."),

'ch4-vf-6': f(niv='comprendre', sp='c4-01',
 exp="L’effet de substitution se mesure à satisfaction constante : il "
     "maintient le consommateur sur la même courbe d’indifférence. C’est "
     "l’effet revenu qui, en augmentant le pouvoir d’achat, permet "
     "d’atteindre une courbe plus élevée."),

'ch4-vf-7': f(niv='comprendre', sp='c4-01',
 exp="L’utilité totale est croissante — la non-satiété l’impose — mais "
     "concave, car ses accroissements successifs diminuent : c’est "
     "exactement la décroissance de l’utilité marginale énoncée par Gossen."),

'ch4-vf-8': f(niv='comprendre', sp='c4-01',
 exp="C’est l’hypothèse de continuité, que le modèle retient pour pouvoir "
     "dériver et poser des conditions d’optimum. Le cours en signale "
     "l’irréalisme avec l’exemple des médicaments vendus par boîtes de "
     "trente comprimés."),

'ch4-vf-10': f(niv='comprendre', sp='c4-01',
 exp="C’est la condition d’optimum : le taux d’échange subjectif, le TMS, "
     "égale le taux d’échange objectif, le rapport des prix. Graphiquement, "
     "la droite de budget est tangente à la courbe d’indifférence la plus "
     "élevée accessible."),

'ch4-vf-11': f(niv='comprendre', sp='c4-01',
 exp="Raworth conteste précisément cette hypothèse : dans l’économie du "
     "donut, les besoins doivent se tenir entre un plancher social et un "
     "plafond écologique. Supposer que « toujours plus » est toujours "
     "préférable revient à ignorer ces limites."),

'ch4-vf-12': f(niv='comprendre', sp='c4-01',
 exp="C’est l’inverse : plus la courbe est éloignée de l’origine, plus les "
     "paniers contiennent de biens et plus la satisfaction est élevée, en "
     "vertu de la non-satiété."),

'ch4-vf-13': f(niv='connaitre', sp='c4-01',
 exp="La droite de budget a pour équation Px·X + Py·Y = R, soit une pente "
     "de − Px/Py. Une variation du prix d’un bien en modifie la pente ; une "
     "variation du revenu la déplace parallèlement."),

'ch4-vf-14': f(niv='comprendre', sp='c4-01',
 exp="Les travaux empiriques montrent des choix intransitifs : préférences "
     "cycliques, renversements selon la présentation des options. "
     "L’hypothèse est donc commode mais empiriquement démentie, ce que "
     "l’économie comportementale a systématisé."),

'ch4-vf-15': f(niv='comprendre', sp='c4-01',
 exp="Sous l’hypothèse de non-satiété, l’utilité totale croît toujours avec "
     "la quantité consommée. Ce qui décroît, c’est le supplément apporté par "
     "chaque unité — l’utilité marginale — d’où une courbe croissante et "
     "concave."),

'ch4-vf-16': f(niv='connaitre', sp='c4-01',
 exp="C’est le projet marginaliste tel que le cours le présente : mettre "
     "l’économie en équation pour lui donner la rigueur des sciences "
     "naturelles. Les Éléments d’économie politique pure (1874) en sont la "
     "réalisation."),

'ch4-vf-17': f(niv='comprendre', sp='c4-01',
 exp="Le programme est inverse : le consommateur maximise son utilité sous "
     "contrainte budgétaire. L’épargne n’apparaît pas dans le modèle "
     "statique à deux biens ; elle relève des modèles intertemporels."),

'ch4-vf-18': f(niv='appliquer', sp='c4-01',
 exp="Une hausse du revenu n’affecte pas les prix relatifs : la pente "
     "− Px/Py est inchangée et la droite se déplace parallèlement vers la "
     "droite, ouvrant l’accès à des courbes d’indifférence plus élevées."),

'ch4-vf-19': f(niv='appliquer', sp='c4-01',
 exp="Une variation du prix d’un seul bien modifie le rapport Px/Py, donc la "
     "pente de la droite : celle-ci pivote autour du point d’intersection "
     "avec l’axe du bien dont le prix n’a pas changé."),

'ch4-vf-20': f(niv='raisonner', sp='c4-01',
 exp="Pour un bien inférieur, les deux effets s’opposent : la baisse du prix "
     "pousse à en consommer davantage par substitution, mais la hausse du "
     "pouvoir d’achat pousse à en consommer moins, puisque la demande d’un "
     "bien inférieur décroît avec le revenu. Si l’effet revenu l’emporte, on "
     "obtient le cas limite du bien de Giffen."),

'ch4-open-3': f(niv='comprendre', sp='c4-01',
 ans={'modele': "L’utilité marginale décroît parce que les besoins les plus "
      "intenses sont satisfaits en premier : la première unité répond à un "
      "besoin pressant, les suivantes à des besoins de moins en moins "
      "urgents. Le premier verre d’eau après une marche procure beaucoup de "
      "satisfaction, le dixième presque aucune. C’est la loi de Gossen, qui "
      "fonde la décroissance de la courbe de demande.",
      'cles': [{'f': ['besoin', 'intense', 'urgent'],
                'l': 'les besoins les plus intenses sont satisfaits en premier'},
               {'f': ['decroissant', 'decroit', 'moins'],
                'l': 'chaque unité apporte moins que la précédente'},
               {'f': ['gossen', 'demande'],
                'l': 'c’est la loi de Gossen, fondement de la courbe de demande'}]},
 exp="La portée est plus large qu’il n’y paraît : si l’utilité marginale "
     "décroît, alors le consentement à payer décroît aussi, ce qui donne sa "
     "pente à la demande et fonde la notion de surplus du consommateur."),

'ch4-open-4': f(niv='connaitre', sp='c4-01',
 ans={'modele': "Une courbe d’indifférence relie tous les paniers de deux "
      "biens qui procurent le même niveau de satisfaction. Elle est "
      "décroissante — car il faut céder d’un bien pour obtenir de l’autre — "
      "et convexe — car le TMS diminue à mesure qu’on se spécialise. Deux "
      "courbes ne peuvent pas se croiser, et plus une courbe est éloignée de "
      "l’origine, plus la satisfaction est élevée.",
      'cles': [{'f': ['meme niveau', 'même niveau', 'indifferent'],
                'l': 'même niveau de satisfaction'},
               {'f': ['decroissante', 'décroissante', 'pente'],
                'l': 'elle est décroissante'},
               {'f': ['convexe', 'tms'], 'l': 'elle est convexe, le TMS diminuant'},
               {'f': ['croise', 'croisent', 'eloignee'],
                'l': 'les courbes ne se croisent pas et s’ordonnent par éloignement'}]},
 exp="Ces quatre propriétés découlent des hypothèses : non-satiété pour "
     "l’ordre des courbes, transitivité pour l’absence de croisement, "
     "décroissance du TMS pour la convexité."),

'ch4-open-6': f(niv='comprendre', sp='c4-01',
 ans={'modele': "L’optimum est atteint au point de tangence entre la droite "
      "de budget et la plus haute courbe d’indifférence accessible : le TMS "
      "y égale le rapport des prix. Le consommateur y dépense tout son "
      "revenu — par non-satiété — et aucun réarrangement ne peut plus "
      "améliorer sa satisfaction.",
      'cles': [{'f': ['tangence', 'tangent'], 'l': 'c’est un point de tangence'},
               {'f': ['tms'], 'l': 'le TMS y égale le rapport des prix'},
               {'f': ['budget', 'revenu', 'contrainte'],
                'l': 'la contrainte budgétaire est saturée'},
               {'f': ['plus haute', 'plus elevee', 'maximis'],
                'l': 'on atteint la courbe la plus élevée accessible'}]},
 exp="La condition d’optimum traduit une égalité entre deux taux d’échange, "
     "l’un subjectif et l’autre objectif : tant qu’ils diffèrent, un gain de "
     "satisfaction reste possible à budget constant."),

'ch4-open-7': f(niv='comprendre', sp='c4-01',
 ans={'modele': "L’effet de substitution isole la modification des prix "
      "relatifs : lorsque le prix d’un bien augmente, il devient "
      "relativement plus cher et le consommateur lui substitue l’autre "
      "bien, à satisfaction inchangée. On se déplace le long d’une même "
      "courbe d’indifférence.",
      'cles': [{'f': ['prix relatif', 'relativement', 'cher'],
                'l': 'il naît de la modification des prix relatifs'},
               {'f': ['remplace', 'substitue', 'reporte'],
                'l': 'le consommateur substitue un bien à l’autre'},
               {'f': ['meme courbe', 'satisfaction', 'constante'],
                'l': 'à satisfaction constante'}]},
 exp="C’est la moitié de l’explication d’un changement de consommation : "
     "l’autre moitié est l’effet revenu, et c’est leur somme que l’on "
     "observe."),

'ch4-open-8': f(niv='comprendre', sp='c4-01',
 ans={'modele': "L’effet revenu traduit la variation du pouvoir d’achat : "
      "lorsqu’un prix augmente, le revenu réel diminue à revenu nominal "
      "inchangé, et le consommateur doit réduire sa consommation. Il change "
      "alors de courbe d’indifférence. Pour un bien normal l’effet joue dans "
      "le même sens que la substitution ; pour un bien inférieur, en sens "
      "contraire.",
      'cles': [{'f': ['pouvoir d achat', 'revenu reel', 'revenu réel'],
                'l': 'il traduit la variation du pouvoir d’achat'},
               {'f': ['nominal', 'inchange'],
                'l': 'à revenu nominal inchangé'},
               {'f': ['normal', 'inferieur', 'sens'],
                'l': 'son sens dépend de la nature du bien'}]},
 exp="C’est la distinction entre les deux effets qui permet d’expliquer les "
     "cas particuliers — biens inférieurs, biens de Giffen — sans renoncer "
     "au modèle."),

'ch4-open-9': f(niv='connaitre', sp='c4-01',
 ans={'modele': "Un bien normal est un bien dont la demande augmente "
      "lorsque le revenu augmente : son élasticité-revenu est positive. Les "
      "biens supérieurs ou de luxe en sont le cas extrême, avec une "
      "élasticité supérieure à 1.",
      'cles': [{'f': ['demande augmente', 'augmente avec le revenu'],
                'l': 'sa demande augmente avec le revenu'},
               {'f': ['elasticite', 'élasticité', 'positive'],
                'l': 'son élasticité-revenu est positive'}]},
 exp="La catégorie se définit par la réaction au revenu, non par la nature "
     "du bien : un même produit peut être normal dans un pays et inférieur "
     "dans un autre."),

'ch4-open-10': f(niv='connaitre', sp='c4-01',
 ans={'modele': "Un bien inférieur est un bien dont la demande diminue "
      "quand le revenu augmente : son élasticité-revenu est négative. Les "
      "ménages s’en détournent au profit de produits jugés meilleurs dès "
      "que leur pouvoir d’achat le permet.",
      'cles': [{'f': ['diminue', 'baisse'], 'l': 'sa demande diminue quand le revenu augmente'},
               {'f': ['revenu'], 'l': 'la relation porte sur le revenu'},
               {'f': ['negative', 'négative', 'remplace', 'substitue'],
                'l': 'élasticité-revenu négative, substitution vers d’autres produits'}]},
 exp="C’est pour ces biens que l’effet revenu contrarie l’effet de "
     "substitution, jusqu’au cas limite du bien de Giffen, où la demande "
     "augmente avec le prix."),

'ch4-open-14': f(niv='comprendre', sp='c4-01',
 ans={'modele': "Le surplus du consommateur est la différence entre ce que "
      "le consommateur était prêt à payer — son consentement à payer, donné "
      "par l’utilité marginale — et ce qu’il paie effectivement, le prix de "
      "marché. Graphiquement, c’est l’aire comprise entre la courbe de "
      "demande et la droite de prix.",
      'cles': [{'f': ['pret a payer', 'prêt à payer', 'consentement'],
                'l': 'il part du consentement à payer'},
               {'f': ['prix', 'paye', 'paie'], 'l': 'auquel on retranche le prix payé'},
               {'f': ['aire', 'surface', 'courbe de demande'],
                'l': 'c’est l’aire sous la courbe de demande au-dessus du prix'}]},
 exp="Le surplus est l’instrument de mesure du gain à l’échange en "
     "microéconomie : c’est lui que l’on compare avant et après une taxe, un "
     "quota ou l’ouverture d’un marché."),
}

FIX.update({

# ====================================== c4-02 · élasticités
'ch4-qcm-22': f(niv='connaitre', sp='c4-02',
 exp="L’élasticité-prix de la demande mesure la sensibilité de la quantité "
     "demandée à une variation du prix : c’est le rapport de la variation "
     "relative des quantités à la variation relative du prix. Un bien est "
     "dit élastique lorsqu’il y est très sensible, inélastique lorsqu’il "
     "l’est peu.",
 why=["La variation du prix en fonction de la demande inverse le rapport.",
      "Le rapport entre revenu et prix n’est pas une élasticité.",
      "La variation du revenu en fonction des prix décrit un effet de "
      "pouvoir d’achat, non une élasticité de la demande."]),

'ch4-open-11': f(niv='comprendre', sp='c4-02',
 ans={'modele': "L’élasticité-prix de la demande est le rapport entre la "
      "variation relative de la quantité demandée et la variation relative "
      "du prix. Elle est négative pour un bien ordinaire. Si le prix monte "
      "de 1 % et la demande baisse de 5 %, l’élasticité vaut − 5 : la "
      "demande est très élastique. Entre 0 et − 1, elle est inélastique.",
      'cles': [{'f': ['variation relative', 'pourcentage', 'rapport'],
                'l': 'c’est un rapport de variations relatives'},
               {'f': ['quantite demandee', 'demande'],
                'l': 'elle porte sur la quantité demandée'},
               {'f': ['prix'], 'l': 'rapportée à la variation du prix'},
               {'f': ['elastique', 'inelastique', '1'],
                'l': 'le seuil de 1 en valeur absolue sépare élastique et inélastique'}]},
 exp="L’enjeu est pratique : si la demande est inélastique, une hausse de "
     "prix augmente le chiffre d’affaires ; si elle est élastique, elle le "
     "réduit. C’est ce qui commande les politiques de prix et le rendement "
     "d’une taxe."),

'ch4-open-12': f(niv='appliquer', sp='c4-02',
 ans={'modele': "Une demande inélastique varie peu malgré une forte "
      "variation du prix : son élasticité est comprise entre 0 et 1 en "
      "valeur absolue. C’est le cas des biens sans substitut proche et de "
      "consommation contrainte — carburant, médicaments vitaux, tabac pour "
      "un consommateur dépendant. Le consommateur y est captif, ce qui rend "
      "ces biens intéressants à taxer pour le rendement, mais inefficaces "
      "si l’on veut modifier les comportements.",
      'cles': [{'f': ['peu', 'faible', 'inelastique'],
                'l': 'la demande varie peu'},
               {'f': ['prix'], 'l': 'malgré une forte variation du prix'},
               {'f': ['carburant', 'medicament', 'tabac', 'substitut'],
                'l': 'exemples : biens sans substitut proche'}]},
 exp="Le cours ajoute la lecture par point de vue : l’inélasticité est un "
     "avantage pour le producteur, qui peut augmenter ses prix sans perdre "
     "ses clients, et un inconvénient pour le consommateur, prisonnier du "
     "prix."),

# ====================================== c4-03 · le producteur
'ch4-qcm-27': f(niv='comprendre', sp='c4-03',
 exp="« Maximiser sous contrainte » signifie atteindre le niveau de "
     "satisfaction le plus élevé possible compte tenu du revenu et des "
     "prix. La contrainte ne fixe pas l’objectif, elle délimite l’ensemble "
     "des possibles : c’est la structure de tout problème microéconomique, "
     "du consommateur comme du producteur.",
 why=["Consommer sans limite de budget supprimerait la contrainte, donc le "
      "problème.",
      "Minimiser la dépense est un autre programme, dual de celui-ci.",
      "Maximiser la production avec des ressources données est le programme "
      "du producteur, non du consommateur."]),

'ch4-vf-9': f(niv='comprendre', sp='c4-03',
 exp="Keen soutient l’inverse dans L’imposture économique (2014) : la "
     "microéconomie standard serait trop abstraite et déconnectée des "
     "comportements observés. Le cours s’en sert pour montrer que les "
     "critiques les plus vives viennent parfois de l’intérieur de la "
     "discipline."),

'ch4-open-5': f(niv='connaitre', sp='c4-03',
 ans={'modele': "La contrainte budgétaire représente l’ensemble des paniers "
      "accessibles compte tenu du revenu et des prix : Px·X + Py·Y ≤ R. "
      "Graphiquement c’est une droite de pente − Px/Py, qui se déplace "
      "parallèlement quand le revenu varie et qui pivote quand un prix "
      "change.",
      'cles': [{'f': ['revenu'], 'l': 'elle dépend du revenu'},
               {'f': ['prix'], 'l': 'et des prix des biens'},
               {'f': ['combinaison', 'panier', 'accessible', 'possible'],
                'l': 'elle délimite les paniers accessibles'}]},
 exp="C’est la contrainte, et non l’objectif : elle dit ce qui est possible, "
     "la carte d’indifférence dit ce qui est préférable, et l’optimum naît "
     "de leur rencontre."),

'ch4-open-13': f(niv='connaitre', sp='c4-03',
 ans={'modele': "La loi générale de la demande énonce que la quantité "
      "demandée diminue lorsque le prix augmente, toutes choses égales par "
      "ailleurs. Elle découle de la décroissance de l’utilité marginale et "
      "se décompose en effet de substitution et effet revenu. Les "
      "exceptions — biens de Giffen, biens ostentatoires — sont rares et "
      "s’expliquent par la domination de l’un de ces deux effets.",
      'cles': [{'f': ['prix augmente', 'hausse'], 'l': 'quand le prix augmente'},
               {'f': ['demande diminue', 'quantite diminue', 'baisse'],
                'l': 'la quantité demandée diminue'},
               {'f': ['utilite marginale', 'substitution', 'revenu', 'exception'],
                'l': 'elle se fonde sur l’utilité marginale décroissante et connaît des exceptions'}]},
 exp="Le caractère « général » de la loi mérite d’être nuancé : c’est une "
     "régularité fondée sur des hypothèses, non une nécessité logique."),

# ====================================== c4-04 et c4-05 · l'équilibre
'ch4-qcm-2': f(niv='connaitre', sp='c4-04',
 exp="Le panier de consommation désigne l’ensemble des biens et services "
     "consommés par un individu sur une période. C’est l’objet sur lequel "
     "portent les préférences : le consommateur ne classe pas des biens "
     "isolés mais des combinaisons.",
 why=["Un bien particulier n’est qu’un élément du panier.",
      "Le budget disponible est la contrainte, non le panier.",
      "La liste des achats d’un mois en est une mesure empirique, pas la "
      "notion théorique."]),

'ch4-aut195-1': f(niv='raisonner', sp='c4-05',
 exp="Le théorème d’Arrow-Debreu est conditionnel : il établit qu’un "
     "équilibre général existe si sept conditions très restrictives sont "
     "réunies — marchés complets, dotation de survie, absence de coûts "
     "fixes, convexité des préférences, entre autres. En explicitant ces "
     "hypothèses, il rend visible la fragilité de la construction "
     "walrasienne au lieu de la confirmer.",
 why=["Le théorème ne porte pas sur l’économie réelle mais sur un modèle "
      "formel.",
      "La stabilité est précisément ce qu’il n’établit pas : c’est l’objet "
      "du résultat Sonnenschein-Mantel-Debreu.",
      "Il ne dit rien de la fréquence empirique de la concurrence parfaite."],
 diss="Référence décisive pour discuter de la portée des modèles : "
      "démontrer l’existence d’un équilibre sous sept hypothèses, c’est "
      "aussi démontrer qu’il n’a aucune raison d’exister sans elles."),

'ch4-open-2': f(niv='comprendre', sp='c4-05',
 ans={'modele': "La rationalité du consommateur signifie qu’il utilise ses "
      "ressources limitées de la manière la plus efficace pour atteindre le "
      "niveau de satisfaction le plus élevé possible. Elle suppose des "
      "préférences complètes et transitives, une information suffisante et "
      "une capacité de calcul. C’est une hypothèse de cohérence, non de "
      "sagesse : la rationalité ne juge pas les fins poursuivies.",
      'cles': [{'f': ['ressources', 'budget', 'contrainte'],
                'l': 'il compose avec des ressources limitées'},
               {'f': ['maximis', 'satisfaction', 'utilite'],
                'l': 'il vise la satisfaction la plus élevée'},
               {'f': ['coherent', 'cohérent', 'transitif', 'complet'],
                'l': 'la rationalité est une exigence de cohérence'}]},
 exp="C’est cette hypothèse que l’économie comportementale met en cause : "
     "Kahneman montre que les décisions sont le plus souvent prises par le "
     "système 1, intuitif et sujet à des biais systématiques."),

'ch4-aut195-2': f(niv='raisonner', sp='c4-05',
 exp="Le résultat Sonnenschein-Mantel-Debreu porte sur l’agrégation : même "
     "si chaque agent est rationnel, la fonction de demande agrégée peut "
     "prendre presque n’importe quelle forme, à cause des effets de revenu. "
     "Rien ne garantit alors l’unicité ni la stabilité de l’équilibre, donc "
     "la convergence du tâtonnement walrasien.",
 why=["Le théorème ne nie pas l’existence : celle-ci est acquise par "
      "Arrow-Debreu.",
      "Il ne remet pas en cause la rationalité individuelle : c’est "
      "précisément son point de départ.",
      "Il n’affirme pas l’indépendance des marchés, qui serait contraire à "
      "l’esprit de l’équilibre général."],
 diss="Argument puissant contre l’idée que la microéconomie fonde la "
      "macroéconomie : la rationalité individuelle ne se transmet pas "
      "mécaniquement aux comportements agrégés."),

# ====================================== c4-06 · rationalité limitée
'ch4-open-1': f(niv='connaitre', sp='c4-06',
 ans={'modele': "L’Homo œconomicus est la représentation théorique de "
      "l’agent dans le modèle standard : parfaitement rationnel, poursuivant "
      "son intérêt propre, disposant d’une information complète et de "
      "capacités de calcul illimitées, il maximise son utilité sous "
      "contrainte. C’est une fiction méthodologique, non une description de "
      "l’individu réel.",
      'cles': [{'f': ['rationnel'], 'l': 'il est parfaitement rationnel'},
               {'f': ['interet', 'intérêt', 'egoiste'],
                'l': 'il poursuit son intérêt propre'},
               {'f': ['information', 'calcul'],
                'l': 'il dispose d’une information complète et de capacités de calcul'},
               {'f': ['maximis', 'utilite'], 'l': 'il maximise son utilité'}]},
 exp="Le cours en fait aussitôt la critique : même lorsque l’information "
     "est disponible, légale et écrite, elle n’est pas lue ni traitée — "
     "l’exemple des CDO, documentés sur deux cents pages que personne ne "
     "lisait, en est l’illustration."),

'ch4-open-15': f(niv='comprendre', sp='c4-06',
 ans={'modele': "Le coût d’opportunité d’un choix est la valeur de la "
      "meilleure option à laquelle on renonce. Pour un consommateur, "
      "dépenser vingt euros au cinéma, c’est renoncer au livre qu’on "
      "aurait pu acheter. Toute décision sous contrainte a donc un coût, "
      "même lorsque aucune somme supplémentaire n’est déboursée : le temps "
      "consacré à une activité en est l’exemple le plus courant.",
      'cles': [{'f': ['renonce', 'renoncement', 'sacrifice'],
                'l': 'c’est ce à quoi l’on renonce'},
               {'f': ['meilleur', 'alternative', 'autre choix'],
                'l': 'la meilleure option alternative'},
               {'f': ['temps', 'argent', 'exemple'],
                'l': 'il s’applique à l’argent comme au temps'}]},
 exp="C’est la notion qui relie la microéconomie du consommateur à "
     "l’avantage comparatif de Ricardo : dans les deux cas, ce qui compte "
     "n’est pas le coût absolu mais le renoncement."),
})


# =============================================================== questions neuves
NEW = [

f(id='q4-n01', sp='c4-01', niv='connaitre', type='assoc', b=23,
  q="Associez chaque hypothèse du modèle standard à ce qu’elle affirme.",
  ans=[["Complétude", "Le consommateur sait comparer deux paniers quelconques"],
       ["Transitivité", "Si A est préféré à B et B à C, alors A est préféré à C"],
       ["Non-satiété", "Le consommateur préfère toujours une quantité plus grande"],
       ["Continuité", "Les biens sont supposés indéfiniment divisibles"]],
  exp="Chaque hypothèse a une conséquence géométrique précise : la "
      "complétude permet de dessiner une carte, la transitivité interdit aux "
      "courbes de se croiser, la non-satiété les ordonne par éloignement de "
      "l’origine, la continuité les rend dérivables. Les connaître une à une "
      "permet de dire exactement ce qu’on perd quand l’une tombe.",
  diss="Une copie solide ne se contente pas de citer les hypothèses : elle "
       "montre, pour chacune, le résultat qu’elle rend possible et la "
       "critique empirique qu’elle appelle."),

f(id='q4-n02', sp='c4-01', niv='raisonner', type='ordre', b=128,
  q="Remettez dans l’ordre le raisonnement qui conduit à l’optimum du "
    "consommateur.",
  ans=["Les préférences sont représentées par une carte de courbes d’indifférence",
       "Le revenu et les prix définissent la droite de budget",
       "Le consommateur cherche la courbe d’indifférence la plus élevée accessible",
       "Cette courbe est nécessairement tangente à la droite de budget",
       "Au point de tangence, le TMS égale le rapport des prix"],
  exp="L’enchaînement montre que l’optimum n’est pas une intuition mais le "
      "résultat de la rencontre entre deux objets de nature différente : des "
      "préférences, subjectives, et une contrainte, objective. S’il n’y "
      "avait pas tangence, la courbe couperait la droite et un point voisin "
      "offrirait plus de satisfaction pour le même budget.",
  diss="Reproduire cet enchaînement permet de traiter rigoureusement tout "
       "sujet sur le choix du consommateur, et d’enchaîner ensuite sur ce "
       "qui se passe lorsque les hypothèses tombent."),

f(id='q4-n03', sp='c4-02', niv='appliquer', type='qcm', b=138,
  q="Le prix d’un bien augmente de 10 % et la quantité demandée recule de "
    "4 %. Que vaut l’élasticité-prix, et qu’advient-il du chiffre "
    "d’affaires ?",
  opts=["− 2,5 : la demande est élastique et le chiffre d’affaires baisse",
        "− 0,4 : la demande est inélastique et le chiffre d’affaires augmente",
        "− 0,4 : la demande est inélastique et le chiffre d’affaires baisse",
        "+ 0,4 : la demande est normale et le chiffre d’affaires est inchangé"],
  ans=1,
  why=["− 2,5 serait obtenu en inversant le rapport : c’est l’erreur la plus "
       "fréquente.",
       "Avec une demande inélastique, la hausse du prix l’emporte sur la "
       "baisse des quantités : le chiffre d’affaires augmente.",
       "L’élasticité-prix est négative pour un bien ordinaire : le signe "
       "positif est impossible ici."],
  exp="L’élasticité vaut − 4 % / 10 % = − 0,4. Inférieure à 1 en valeur "
      "absolue, la demande est inélastique : les quantités réagissent moins "
      "que proportionnellement, donc le prix l’emporte et le chiffre "
      "d’affaires progresse d’environ 6 %.",
  diss="Ce calcul fonde les stratégies de prix et le rendement des taxes : "
       "on taxe ce qui est inélastique pour le rendement, et ce qui est "
       "élastique pour modifier les comportements."),

f(id='q4-n04', sp='c4-02', niv='comprendre', type='qcm', b=221,
  q="L’élasticité-prix croisée entre deux biens est négative. Qu’en "
    "conclut-on ?",
  opts=["Les biens sont substituables",
        "Les biens sont complémentaires",
        "Les biens sont indépendants",
        "L’un des deux biens est inférieur"],
  ans=1,
  why=["Des biens substituables donnent une élasticité croisée positive : "
       "la hausse du prix de l’un accroît la demande de l’autre.",
       "L’indépendance correspond à une élasticité croisée nulle.",
       "Le caractère inférieur d’un bien se lit sur l’élasticité-revenu, non "
       "sur l’élasticité croisée."],
  exp="Une élasticité croisée négative signifie que la hausse du prix du "
      "bien B réduit la demande du bien A : les deux vont ensemble, ils sont "
      "complémentaires. L’exemple du cours est limpide : le prix de la place "
      "de cinéma augmente, la consommation de popcorn diminue.",
  diss="L’élasticité croisée est l’outil qui permet de délimiter un marché "
       "pertinent en droit de la concurrence : deux produits très "
       "substituables appartiennent au même marché."),

f(id='q4-n05', sp='c4-02', niv='raisonner', type='vf', b=144,
  q="Une demande élastique est toujours un avantage pour le producteur.",
  ans=False,
  exp="Le cours raisonne par point de vue. Pour le consommateur, "
      "l’élasticité est un avantage : il dispose de substituts et n’est pas "
      "prisonnier du prix d’un seul bien. Pour le producteur, elle est au "
      "contraire une contrainte : toute hausse de prix se paie d’une forte "
      "perte de volume, donc de chiffre d’affaires.",
  diss="Cette lecture asymétrique est utile pour discuter du pouvoir de "
       "marché : la stratégie des entreprises consiste souvent à rendre leur "
       "demande inélastique, par la marque, la fidélisation ou la "
       "différenciation."),

f(id='q4-n06', sp='c4-03', niv='comprendre', type='qcm', b=327,
  q="Quelle est la différence entre rendements factoriels et rendements "
    "d’échelle ?",
  opts=["Les rendements factoriels concernent l’industrie, les rendements "
        "d’échelle les services",
        "Les rendements factoriels font varier un seul facteur, les autres "
        "étant fixes ; les rendements d’échelle font varier tous les "
        "facteurs dans les mêmes proportions",
        "Les rendements factoriels valent à long terme, les rendements "
        "d’échelle à court terme",
        "Les rendements factoriels portent sur les coûts, les rendements "
        "d’échelle sur les prix"],
  ans=1,
  why=["La distinction ne tient pas au secteur d’activité.",
       "C’est l’inverse : les rendements factoriels relèvent du court terme, "
       "les rendements d’échelle du long terme.",
       "Les deux notions portent sur la production, non sur les prix."],
  exp="La distinction est celle de l’horizon. À court terme, au moins un "
      "facteur est fixe : on étudie la productivité marginale du facteur "
      "variable, et la loi des rendements marginaux décroissants. À long "
      "terme, tout varie dans les mêmes proportions — l’intensité "
      "capitalistique restant constante — et l’on étudie l’effet d’un "
      "changement d’échelle.",
  diss="Cette distinction commande le raisonnement : invoquer des économies "
       "d’échelle pour expliquer un phénomène de court terme est une faute "
       "fréquente et repérable."),

f(id='q4-n07', sp='c4-03', niv='connaitre', type='qcmm', b=333,
  q="Quelles propositions sont exactes à propos des rendements d’échelle ? "
    "(plusieurs réponses)",
  opts=["Ils supposent que tous les facteurs varient dans les mêmes proportions",
        "Ils s’étudient à long terme",
        "Ils supposent une intensité capitalistique constante",
        "Ils décrivent l’effet d’une unité de travail supplémentaire à capital fixe",
        "Ils peuvent être croissants, constants ou décroissants"],
  ans=[0, 1, 2, 4],
  why=["Exacte : c’est la définition même du changement d’échelle.",
       "Exacte : à long terme, aucun facteur n’est fixe.",
       "Exacte : le rapport capital sur travail est maintenu constant.",
       "C’est la définition des rendements factoriels, à court terme.",
       "Exacte : le cours distingue les trois types de rendements "
       "d’échelle."],
  exp="L’intensité capitalistique — le rapport du capital au travail — est "
      "l’hypothèse clé : sans elle, on mélangerait un changement d’échelle "
      "et un changement de technique. Cette notion sert aussi aux "
      "comparaisons internationales et à l’analyse de la croissance."),

f(id='q4-n08', sp='c4-03', niv='appliquer', type='qcm', b=505,
  q="Une entreprise vend au prix P et supporte un coût moyen CM. À quelle "
    "condition est-elle rentable ?",
  opts=["P ≥ CM", "P ≤ CM", "P ≥ coût marginal uniquement",
        "P = recette marginale"],
  ans=0,
  why=["P ≤ CM signifie que chaque unité vendue coûte plus qu’elle ne "
       "rapporte : l’entreprise perd de l’argent.",
       "L’égalité du prix et du coût marginal détermine la quantité "
       "optimale en concurrence, mais ne garantit pas la rentabilité "
       "globale.",
       "L’égalisation de la recette marginale au coût marginal est la "
       "condition de maximisation du profit, pas le critère de rentabilité."],
  exp="Le prix doit au moins couvrir le coût moyen, qui inclut l’ensemble "
      "des coûts rapportés à la quantité produite : c’est la condition pour "
      "que le profit total ne soit pas négatif. La condition de "
      "maximisation — produire jusqu’à l’égalité du coût marginal et de la "
      "recette marginale — est une question distincte : elle dit combien "
      "produire, non si l’on peut rester sur le marché."),

f(id='q4-n09', sp='c4-04', niv='comprendre', type='qcm', b=533,
  q="Qu’ajoute l’équilibre général à l’équilibre partiel ?",
  opts=["Il raisonne sur un seul marché avec davantage de précision",
        "Il prend en compte l’interdépendance de tous les marchés, qui "
        "doivent s’équilibrer simultanément",
        "Il introduit l’intervention de l’État",
        "Il remplace les prix par des quantités"],
  ans=1,
  why=["L’équilibre partiel est précisément celui d’un marché isolé, toutes "
       "choses égales par ailleurs.",
       "L’équilibre général est un modèle de marché, sans intervention "
       "publique.",
       "Les prix restent la variable d’ajustement centrale."],
  exp="L’équilibre partiel, à la Marshall, étudie un marché en supposant les "
      "autres inchangés. L’équilibre général, à la Walras, cherche un "
      "système de prix qui équilibre simultanément tous les marchés : ce "
      "qu’on gagne en cohérence, on le paie en difficulté — l’existence, "
      "l’unicité et la stabilité d’une telle solution deviennent des "
      "problèmes redoutables.",
  diss="Opposer les deux niveaux est la bonne manière d’introduire "
       "Arrow-Debreu et Sonnenschein-Mantel-Debreu : ils répondent aux "
       "questions que l’équilibre général soulève."),

f(id='q4-n10', sp='c4-05', niv='raisonner', type='ordre', b=711,
  q="Remettez dans l’ordre les trois questions que la théorie de "
    "l’équilibre général doit résoudre, et leur traitement.",
  ans=["Un système de prix équilibrant tous les marchés peut-il exister ?",
       "Arrow et Debreu démontrent son existence sous des hypothèses très restrictives",
       "Cet équilibre est-il unique et stable, c’est-à-dire atteignable par tâtonnement ?",
       "Sonnenschein, Mantel et Debreu montrent que la demande agrégée peut prendre presque n’importe quelle forme",
       "Rien ne garantit donc la convergence du marché vers l’équilibre"],
  exp="La progression est logique : l’existence d’abord, la stabilité "
      "ensuite. Le premier résultat semble conforter la construction "
      "walrasienne, jusqu’à ce qu’on lise ses hypothèses ; le second ôte "
      "l’espoir qu’un marché livré à lui-même converge vers l’équilibre "
      "dont on a démontré l’existence.",
  diss="Enchaînement très efficace pour montrer qu’une démonstration "
       "mathématique peut affaiblir la thèse qu’elle paraît soutenir."),

f(id='q4-n11', sp='c4-06', niv='comprendre', type='qcm', b=917,
  q="Que recouvre, chez Kahneman, la distinction entre système 1 et "
    "système 2 ?",
  opts=["Deux catégories d’agents économiques, les naïfs et les experts",
        "Deux modes de pensée : l’un rapide, intuitif et émotionnel, l’autre "
        "lent, réfléchi et calculateur",
        "Deux niveaux d’information, publique et privée",
        "Deux formes de rationalité, individuelle et collective"],
  ans=1,
  why=["La distinction porte sur des modes de pensée coexistant chez chacun, "
       "non sur des types d’individus.",
       "Les niveaux d’information relèvent de l’asymétrie d’information, "
       "autre problème.",
       "La rationalité collective est une question d’agrégation, traitée "
       "ailleurs."],
  exp="Le système 1 est rapide, automatique, émotionnel et sujet à l’erreur ; "
      "le système 2 est lent, réfléchi, rationnel mais coûteux en effort. "
      "Comme le second est fatigant, c’est le premier qui décide la plupart "
      "du temps, d’où des biais cognitifs systématiques — c’est-à-dire des "
      "erreurs régulières, prévisibles, et non de simples bruits aléatoires.",
  diss="Cette régularité est l’argument décisif : si les erreurs étaient "
       "aléatoires, elles s’annuleraient à l’agrégation ; étant "
       "systématiques, elles déforment durablement les comportements de "
       "marché."),

f(id='q4-n12', sp='c4-06', niv='raisonner', type='qcm', b=902,
  q="Le cours prend l’exemple des CDO, dont la documentation faisait "
    "parfois deux cents pages. Que montre-t-il ?",
  opts=["Que l’information n’était pas disponible avant la crise",
        "Que la disponibilité de l’information ne suffit pas : encore "
        "faut-il qu’elle soit traitée, ce qui a un coût",
        "Que la réglementation financière était inexistante",
        "Que les investisseurs étaient irrationnels au sens d’un manque de logique"],
  ans=1,
  why=["L’information était au contraire disponible, légale et écrite : "
       "c’est précisément le paradoxe.",
       "La question n’est pas l’absence de règles mais l’usage effectif de "
       "l’information produite.",
       "Ne pas lire deux cents pages techniques n’est pas un défaut de "
       "logique : c’est un arbitrage de temps et d’attention."],
  exp="Le cours déplace le problème : il ne s’agit pas seulement de savoir "
      "si l’information est donnée, mais si elle est traitée. Lire, "
      "comprendre et exploiter une documentation technique coûte du temps et "
      "de l’énergie ; au-delà d’un certain seuil, personne ne le fait, et "
      "l’information disponible reste lettre morte.",
  diss="Cette nuance enrichit considérablement un développement sur les "
       "asymétries d’information : la transparence réglementaire ne suffit "
       "pas si le coût de traitement reste prohibitif."),

f(id='q4-n13', sp='c4-06', niv='comprendre', type='courte', b=909,
  q="Qu’est-ce qu’un biais cognitif, et pourquoi sa nature systématique "
    "est-elle importante pour l’analyse économique ?",
  ans={'modele': "Un biais cognitif est une erreur de jugement régulière "
       "qui éloigne la décision de la rationalité supposée par le modèle "
       "standard. Il naît des raccourcis mentaux du système 1, rapide et "
       "intuitif. Son caractère systématique est décisif : des erreurs "
       "aléatoires se compenseraient à l’échelle du marché, tandis que des "
       "erreurs orientées dans le même sens déforment durablement la demande "
       "et les prix.",
       'cles': [{'f': ['erreur', 'jugement'], 'l': 'c’est une erreur de jugement'},
                {'f': ['systematique', 'systématique', 'regulier'],
                 'l': 'elle est systématique et non aléatoire'},
                {'f': ['raccourci', 'systeme 1', 'intuitif'],
                 'l': 'elle vient des raccourcis mentaux'},
                {'f': ['compens', 'agregation', 'marche', 'rationalite'],
                 'l': 'des erreurs systématiques ne se compensent pas à l’agrégation'}]},
  exp="Kahneman et Thaler fondent sur ce constat l’économie "
      "comportementale : si les écarts à la rationalité sont prévisibles, "
      "ils peuvent être modélisés — et, éventuellement, corrigés par "
      "l’architecture des choix."),

f(id='q4-n14', sp='c4-05', niv='raisonner', type='courte', b=705,
  q="En quoi les théorèmes d’Arrow-Debreu et de Sonnenschein-Mantel-Debreu "
    "nuancent-ils la confiance dans l’autorégulation des marchés ?",
  ans={'modele': "Arrow et Debreu démontrent qu’un équilibre général existe, "
       "mais au prix d’hypothèses très restrictives — marchés complets, "
       "absence de coûts fixes, dotation de survie — que l’économie réelle "
       "ne vérifie pas. Sonnenschein, Mantel et Debreu montrent ensuite que "
       "la demande agrégée peut prendre presque n’importe quelle forme, si "
       "bien que l’équilibre n’est ni nécessairement unique ni stable : rien "
       "ne garantit que le marché y converge.",
       'cles': [{'f': ['existe', 'existence'],
                 'l': 'Arrow-Debreu établit l’existence'},
                {'f': ['hypothese', 'restrictive', 'condition'],
                 'l': 'sous des hypothèses très restrictives'},
                {'f': ['stable', 'stabilite', 'unique'],
                 'l': 'SMD met en cause l’unicité et la stabilité'},
                {'f': ['agreg', 'demande agregee', 'tatonnement'],
                 'l': 'à cause du comportement de la demande agrégée'}]},
  exp="Les deux résultats sont complémentaires, et leur portée est la même : "
      "ils transforment une confiance en un problème. L’autorégulation "
      "devient une propriété à démontrer sous conditions, non un point de "
      "départ.",
  diss="C’est l’argument le plus solide, parce qu’il est interne : il ne "
       "vient pas d’économistes hétérodoxes mais des fondateurs mêmes de la "
       "théorie de l’équilibre général."),
]
