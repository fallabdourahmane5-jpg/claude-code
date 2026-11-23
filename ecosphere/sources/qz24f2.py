# -*- coding: utf-8 -*-
"""Chapitre 24 — corrections des questions héritées, sous-parties c24-03 à c24-06."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c24-03
'ch24-qcm-3': f(niv='connaitre', sp='c24-03', b=362,
 why=["Un accord plurilatéral n’est pas nécessairement régional : il ne "
      "suppose aucune proximité géographique.",
      "Un accord engageant tous les membres de l’OMC relève du "
      "multilatéralisme.",
      "L’expression « décision unilatérale collective » est contradictoire : "
      "l’unilatéralisme exclut la négociation."],
 diss="Point de vigilance fréquent : plurilatéralisme et régionalisme ne se "
      "confondent pas."),
'ch24-qcm-20': f(niv='connaitre', sp='c24-03', b=420,
 why=["Krugman travaille sur les rendements croissants et la nouvelle "
      "géographie économique.",
      "Viner analyse la création et le détournement de trafic dans les "
      "unions douanières.",
      "Balassa propose la typologie des cinq étapes de l’intégration "
      "régionale."]),
'ch24-qcm-21': f(niv='appliquer', sp='c24-03', b=465,
 why=["(4 ; 4) correspond à la coopération mutuelle, situation "
      "collectivement la meilleure.",
      "(2 ; 3) ne correspond pas à cette case de la matrice.",
      "(5 ; 3) inverserait les rôles : ce serait le leader qui profiterait "
      "de la coopération du suiveur."],
 diss="Lecture à retenir : le leader supporte le coût du bien public, le "
      "suiveur en bénéficie sans payer."),
'ch24-qcm-22': f(niv='raisonner', sp='c24-03', b=463,
 why=["Dans un dilemme du prisonnier classique, les deux joueurs ont la même "
      "structure d’incitations, ce qui n’est pas le cas ici.",
      "La matrice comporte bien un équilibre : l’absence d’équilibre n’est "
      "pas en cause.",
      "Les deux équilibres symétriques supposeraient une symétrie des rôles, "
      "précisément absente."],
 diss="Nuance que peu de copies font : la stabilité hégémonique repose sur "
      "une asymétrie assumée, non sur un dilemme symétrique."),
'ch24-qcm-23': f(niv='connaitre', sp='c24-03', b=492,
 why=["40 % de la production et 50 % des réserves d’or sous-estiment "
      "nettement la position américaine de 1945.",
      "La maîtrise exclusive de l’arme nucléaire est une donnée militaire, "
      "non la base économique de l’hégémonie décrite.",
      "Les États-Unis n’ont pas connu d’excédent commercial permanent : le "
      "déficit devient même structurel à partir des années 1970."]),
'ch24-qcm-24': f(niv='connaitre', sp='c24-03', b=525,
 why=["23 pays sont les signataires du GATT en 1947.",
      "33 pays participent au cycle d’Annecy en 1949.",
      "106 est le nombre de participants au lancement de l’Uruguay Round."],
 diss="Quatre nombres à ne pas confondre : 44 (Bretton Woods, 1944), 23 "
      "(GATT, 1947), 123 (conclusion de l’Uruguay Round), 166 (membres de "
      "l’OMC en 2026)."),
'ch24-questi-123': f(niv='raisonner', sp='c24-03', b=492),
'ch24-questi-124': f(niv='raisonner', sp='c24-03', b=408),

# =============================================================== c24-04
'ch24-qcm-26': f(niv='connaitre', sp='c24-04', b=544,
 why=["Les pays n’ont pas refusé toute règle commune : ils ont au contraire "
      "conclu un accord commercial.",
      "Le FMI traite des questions monétaires et de balance des paiements, "
      "non du commerce.",
      "L’ONU ne s’est pas opposée au projet : c’est la non-ratification "
      "américaine qui l’a fait échouer."],
 diss="Conséquence durable : pendant près de cinquante ans, le commerce "
      "mondial est régi par un accord et non par une institution."),
'ch24-qcm-27': f(niv='connaitre', sp='c24-04', b=580,
 why=["L’article III pose le traitement national.",
      "L’article XI interdit en principe les restrictions quantitatives.",
      "L’article XIX fonde les mesures de sauvegarde."],
 diss="Quatre articles à mémoriser ensemble : I (NPF), III (traitement "
      "national), XI (restrictions quantitatives), XIX (sauvegardes), "
      "auxquels s’ajoute XXIV (accords régionaux)."),
'ch24-qcm-28': f(niv='comprendre', sp='c24-04', b=573,
 why=["La taxation selon le pays d’origine n’est pas le principe : le "
      "traitement national compare le produit importé au produit national.",
      "Aucun avantage fiscal n’est exigé : seule la non-discrimination "
      "l’est.",
      "L’exonération de droits de douane concernerait la frontière, alors que "
      "le traitement national s’applique une fois le produit entré."],
 diss="Distinction essentielle : la NPF interdit de discriminer entre pays "
      "étrangers, le traitement national entre produits étrangers et "
      "nationaux."),
'ch24-qcm-29': f(niv='comprendre', sp='c24-04', b=628,
 why=["Les droits de douane ne protègent pas mieux : un quota peut bloquer "
      "totalement les importations.",
      "Le montant des recettes n’est pas le critère retenu, bien que les "
      "droits en procurent et les quotas non.",
      "C’est précisément l’article XI qui interdit les restrictions "
      "quantitatives, et non les droits de douane."],
 diss="Principe à nommer : la transparence — on ne peut négocier que ce que "
      "l’on peut mesurer."),
'ch24-qcm-30': f(niv='connaitre', sp='c24-04', b=656,
 exp="L’article XI du GATT interdit en principe les restrictions "
     "quantitatives, dont le contingentement : celles-ci peuvent bloquer "
     "directement les échanges, sans qu’aucun prix ne permette de les "
     "contourner. Cette interdiction traduit le principe de transparence : "
     "les droits de douane sont préférés parce qu’ils sont identifiables, "
     "mesurables et donc négociables, alors qu’un quota rend la protection "
     "difficile à évaluer et la rente invisible.",
 why=["Les subventions à l’exportation relèvent de l’Accord SMC, et non de "
      "l’article XI.",
      "Les droits antidumping sont au contraire autorisés sous conditions.",
      "Les accords régionaux relèvent de l’article XXIV."]),
'ch24-qcm-31': f(niv='connaitre', sp='c24-04', b=703,
 why=["L’article I est précisément la clause à laquelle les accords "
      "régionaux dérogent.",
      "L’article III porte sur le traitement national.",
      "L’Accord SMC encadre les subventions et mesures compensatoires."]),
'ch24-qcm-33': f(niv='connaitre', sp='c24-04', b=749,
 why=["La Chine n’a pas annoncé quitter l’OMC.",
      "Son statut de pays en développement n’a pas été formellement "
      "supprimé.",
      "Ses avantages existants n’ont pas automatiquement disparu : "
      "l’annonce ne porte que sur les demandes nouvelles."],
 diss="Nuance juridique importante : renoncer à demander de nouveaux "
      "avantages n’équivaut pas à perdre un statut."),
'ch24-vraifa-100': f(niv='connaitre', sp='c24-04', b=580),
'ch24-vraifa-101': f(niv='comprendre', sp='c24-04', b=703),
'ch24-questi-125': f(niv='raisonner', sp='c24-04', b=580),

# =============================================================== c24-05
'ch24-qcm-32': f(niv='connaitre', sp='c24-05', b=751,
 why=["La réciprocité stricte est précisément ce à quoi le SGP fait "
      "exception.",
      "Le SGP ne porte pas spécifiquement sur l’agriculture.",
      "Le tarif extérieur commun caractérise une union douanière."],
 diss="Exemple de traitement spécial et différencié : l’égalité des règles "
      "est écartée au nom de l’équité du développement."),
'ch24-qcm-34': f(niv='comprendre', sp='c24-05', b=904,
 why=["La preuve d’un dumping fonde un droit antidumping, non une "
      "sauvegarde.",
      "La preuve d’une subvention étrangère fonde un droit compensateur.",
      "Aucun accord préalable de tous les membres n’est requis : une enquête "
      "nationale suffit, dans les conditions prévues."],
 diss="Trois instruments à ne jamais confondre : antidumping (prix déloyal), "
      "droits compensateurs (subvention), sauvegarde (choc d’importations "
      "sans déloyauté)."),
'ch24-qcm-35': f(niv='connaitre', sp='c24-05', b=858,
 why=["La catégorie orange regroupe les subventions contestables, dont les "
      "effets défavorables doivent être démontrés.",
      "La catégorie verte, qui autorisait certaines aides, a expiré en 1999.",
      "L’Accord SMC couvre bien ces subventions : les exclure serait une "
      "erreur."]),
'ch24-qcm-36': f(niv='connaitre', sp='c24-05', b=898,
 why=["L’autorisation définitive des aides environnementales est exactement "
      "ce que le cours met en garde contre.",
      "La catégorie verte n’a pas été créée en 2015 : elle a expiré bien "
      "avant.",
      "Elle ne concernait pas uniquement l’agriculture, mais aussi certaines "
      "aides à la recherche et régionales."],
 diss="Erreur très fréquente à éviter : affirmer qu’une subvention verte est "
      "aujourd’hui automatiquement licite."),
'ch24-qcm-37': f(niv='connaitre', sp='c24-05', b=941,
 why=["En 1947, le GATT n’est qu’un accord : il ne comporte pas d’organe "
      "juridictionnel de ce type.",
      "Le Tokyo Round de 1979 porte sur les obstacles non tarifaires et les "
      "subventions.",
      "2001 est l’année du lancement du cycle de Doha et de l’adhésion "
      "chinoise."],
 diss="Information décisive pour la suite : l’affaiblissement de cet organe "
      "est l’un des symptômes majeurs de la crise du multilatéralisme."),

# =============================================================== c24-06
'ch24-qcm-38': f(niv='connaitre', sp='c24-06', b=979,
 why=["L’inversion des deux chiffres contredit la hiérarchie constante entre "
      "les deux secteurs.",
      "Un taux identique de 7 % effacerait précisément l’exception "
      "agricole.",
      "4 % dans les deux secteurs correspondrait à peu près au seul niveau "
      "industriel."],
 diss="Chiffre à citer tel quel : 15,9 % contre 3 % en 2019 — l’exception "
      "agricole se mesure, elle ne se devine pas."),
'ch24-qcm-39': f(niv='connaitre', sp='c24-06', b=992,
 why=["1929 est l’année du krach boursier, non de cette loi.",
      "1947 est l’année du GATT.",
      "1962 est l’année de la mise en œuvre de la PAC."],
 diss="Parallèle efficace : soutien agricole américain en 1933, européen en "
      "1962 — la protection agricole précède largement le GATT."),
'ch24-qcm-40': f(niv='connaitre', sp='c24-06', b=1007,
 why=["1951 est l’année de la CECA.",
      "1957 est celle du traité de Rome, qui prévoit la PAC sans encore la "
      "mettre en œuvre.",
      "1986 est l’année du lancement de l’Uruguay Round."],
 diss="Cinq objectifs initiaux à connaître : productivité, niveau de vie "
      "équitable, stabilisation des marchés, sécurité des approvisionnements, "
      "prix raisonnables."),
'ch24-qcm-41': f(niv='connaitre', sp='c24-06', b=1056,
 why=["Les importateurs nets ont au contraire intérêt à des prix mondiaux "
      "bas sans libéralisation de leur propre marché.",
      "Les membres fondateurs du GATT sont les 23 signataires de 1947.",
      "Les pays les moins avancés constituent une catégorie distincte, aux "
      "intérêts souvent différents."],
 diss="Exemple précis à mobiliser : le contentieux sur le coton américain et "
      "ses effets sur les producteurs africains."),
'ch24-qcm-42': f(niv='connaitre', sp='c24-06', b=1093,
 why=["10 % sous-estime très largement le poids historique de la filière.",
      "25 % reste inférieur au maximum atteint.",
      "60 % surestime la part retenue par le cours."]),
'ch24-qcm-43': f(niv='connaitre', sp='c24-06', b=1084,
 why=["Une interdiction totale des importations alimentaires n’a pas été "
      "décidée.",
      "La spécialisation accrue dans l’arachide est précisément ce que le "
      "tournant cherche à corriger.",
      "Le Sénégal ne s’est pas retiré de l’OMC."],
 diss="Nuance à conserver : l’intensification rizicole pose elle-même un "
      "problème de sols, d’où la recherche de diversification vers le mil, "
      "les fruits et les légumes."),
'ch24-qcm-46': f(niv='connaitre', sp='c24-06', b=1167,
 why=["L’OMC est créée en 1995, au terme de l’Uruguay Round.",
      "L’Accord sur les subventions et les mesures compensatoires relève du "
      "Tokyo Round puis de l’Uruguay Round.",
      "Le démantèlement de l’accord multifibres est organisé par l’Uruguay "
      "Round et s’achève en 2005."],
 diss="Progression des cycles à retenir : tarifs d’abord, puis pratiques "
      "déloyales, puis obstacles non tarifaires, puis services et propriété "
      "intellectuelle."),
'ch24-questi-126': f(niv='raisonner', sp='c24-06', b=979),
'ch24-questi-127': f(niv='raisonner', sp='c24-06', b=1093),

}
