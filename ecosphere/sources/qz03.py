# -*- coding: utf-8 -*-
"""Chapitre 3 — Grands courants de l'analyse économique."""

SP = {
 'c3-01': 'Mercantilistes et physiocrates : Bodin, Colbert, Quesnay',
 'c3-02': 'Les classiques : Smith, Ricardo, division du travail et échange',
 'c3-03': 'Malthus, Say et Marx : population, débouchés et plus-value',
 'c3-04': 'Les néoclassiques et le marginalisme',
 'c3-05': 'Keynes : demande effective et équilibre de sous-emploi',
 'c3-06': 'Keynes face aux « classiques » : points communs et ruptures',
 'c3-07': 'Nouvelle économie keynésienne : rigidités et imperfections',
 'c3-08': 'Institutionnalistes, régulation et renouvellements contemporains',
}

DROP = []


def f(**kw):
    return kw


FIX = {

# =============================== c3-01 · mercantilistes et physiocrates
'ch3-qcm-1': f(niv='connaitre', sp='c3-01',
 exp="Le mercantilisme couvre les XVIᵉ-XVIIIᵉ siècles : il accompagne la "
     "formation des États modernes et des empires coloniaux. Sa thèse "
     "centrale est que la richesse d’une nation se mesure à son stock de "
     "métaux précieux, ce qui justifie protectionnisme et excédent "
     "commercial.",
 why=["Les XIVᵉ-XVIᵉ siècles précèdent la doctrine constituée.",
      "Les XVIIIᵉ-XIXᵉ siècles sont ceux des physiocrates puis des "
      "classiques.",
      "Les XIXᵉ-XXᵉ siècles relèvent des néoclassiques et de Keynes."]),

'ch3-qcm-2': f(niv='connaitre', sp='c3-01',
 exp="« Il n’est richesse ni force que d’hommes » : Bodin fait de la "
     "population la source de la puissance. D’où le natalisme mercantiliste "
     "— plus un pays est peuplé, plus il produit, commerce et peut lever des "
     "armées.",
 why=["« Laissez faire les hommes » est la formule de Vincent de Gournay, "
      "physiocrate.",
      "Faire venir la richesse du travail industriel est une thèse "
      "classique, postérieure.",
      "« Private vices, public benefits » est de Mandeville."]),

'ch3-qcm-3': f(niv='connaitre', sp='c3-01',
 exp="Mandeville publie La Fable des abeilles, où il soutient que les vices "
     "privés — luxe, vanité, cupidité — produisent le bien public en "
     "alimentant l’activité. C’est une préfiguration du raisonnement de la "
     "main invisible, mais formulée en termes moraux et provocateurs.",
 why=["Quesnay écrit le Tableau économique (1758).",
      "Smith publie La Richesse des nations (1776).",
      "Colbert est un ministre, non un théoricien auteur d’un ouvrage."]),

'ch3-qcm-4': f(niv='connaitre', sp='c3-01',
 exp="Le colbertisme est la version française du mercantilisme : il mise sur "
     "l’industrie et les manufactures soutenues par l’État, le "
     "protectionnisme extérieur et l’unification du marché intérieur. "
     "L’État crée des manufactures royales et leur accorde un monopole de "
     "dix ans.",
 why=["Le mercantilisme agricole est plutôt espagnol ou italien selon les "
      "variantes ; ce n’est pas la marque de Colbert.",
      "Les physiocrates sont postérieurs et opposés au colbertisme.",
      "Le libre-échange est exactement ce que Colbert refuse à l’extérieur."]),

'ch3-qcm-5': f(niv='connaitre', sp='c3-01',
 exp="Pour les physiocrates, seule l’agriculture dégage un produit net, "
     "c’est-à-dire une richesse supérieure aux avances consommées. "
     "L’industrie et le commerce ne font que transformer ou déplacer : ils "
     "forment la classe stérile.",
 why=["Le commerce ne crée rien, il transporte : c’est la thèse "
      "physiocratique.",
      "L’industrie est rangée dans la classe stérile.",
      "La monnaie est le critère mercantiliste, que les physiocrates "
      "rejettent."]),

'ch3-qcm-6': f(niv='connaitre', sp='c3-01',
 exp="Le produit net est l’excédent de la production annuelle sur les "
     "avances consommées pour l’obtenir. C’est la première formulation d’un "
     "surplus économique : il revient aux propriétaires fonciers, ce qui "
     "justifie chez les physiocrates l’impôt unique sur la terre.",
 why=["Le bénéfice brut est une notion comptable d’entreprise.",
      "Le revenu national corrigé de l’inflation est une grandeur de "
      "comptabilité nationale moderne.",
      "La valeur ajoutée industrielle est précisément ce que les "
      "physiocrates refusent de considérer comme une richesse nouvelle."]),

'ch3-qcm-7': f(niv='connaitre', sp='c3-01',
 exp="La formule « Laissez faire les hommes, laissez passer les "
     "marchandises » est attribuée à Vincent de Gournay. Elle résume la "
     "politique physiocrate : non-intervention, liberté du commerce des "
     "grains, confiance dans un ordre naturel.",
 why=["Quesnay construit le Tableau économique ; la formule n’est pas de "
      "lui.",
      "Colbert défend exactement l’inverse, l’intervention de l’État.",
      "Turgot applique des idées physiocrates mais n’est pas l’auteur de la "
      "formule."]),

'ch3-qcm-8': f(niv='connaitre', sp='c3-01',
 exp="La Richesse des nations paraît en 1776, l’année de la déclaration "
     "d’indépendance américaine. Smith y fonde l’économie politique "
     "classique : division du travail, main invisible, critique du "
     "mercantilisme.",
 why=["1750 est la période physiocrate.",
      "1789 est la Révolution française.",
      "1817 est la date des Principes de Ricardo."]),

'ch3-qcm-16': f(niv='comprendre', sp='c3-01',
 exp="Est orthodoxe l’économiste qui travaille dans le cadre dominant issu "
     "du courant classique puis néoclassique ; est hétérodoxe celui qui en "
     "conteste les fondements — rationalité, équilibre, autorégulation. La "
     "distinction porte sur le paradigme, non sur la position politique.",
 why=["La correspondance interventionniste / libéral est trop simple : il y "
      "a des orthodoxes interventionnistes.",
      "Ni l’une ni l’autre ne se définit par l’échelle d’analyse.",
      "Keynésiens et monétaristes appartiennent tous deux à des traditions "
      "qui ont été dominantes."]),

'ch3-qcm-17': f(niv='connaitre', sp='c3-01',
 exp="Le chapitre présente cinq courants : classique, marxiste, "
     "néoclassique, institutionnaliste et keynésien. Mercantilisme et "
     "physiocratie les précèdent, comme préhistoire de l’économie politique.",
 why=["Le monétarisme est un prolongement du courant néoclassique, non un "
      "des cinq courants retenus.",
      "Mercantilistes et physiocrates sont présentés en amont des cinq "
      "courants.",
      "« Libéral, socialiste, structuraliste » n’est pas la nomenclature du "
      "cours."]),

'ch3-qcm-18': f(niv='connaitre', sp='c3-01',
 exp="Quesnay publie le Tableau économique en 1758, version définitive en "
     "1766. C’est la première représentation de l’économie comme circuit : "
     "les flux circulent entre trois classes et bouclent, ce qui annonce "
     "aussi bien la comptabilité nationale que le circuit keynésien.",
 why=["Smith raisonne sur la division du travail, non sur un circuit "
      "formalisé.",
      "Ricardo construit la théorie de la rente et de l’avantage comparatif.",
      "Say formule la loi des débouchés."]),

'ch3-qcm-21': f(niv='connaitre', sp='c3-01',
 exp="Colbert fait créer par l’État des manufactures royales auxquelles il "
     "accorde un monopole de dix ans, le temps de les établir face à la "
     "concurrence étrangère. C’est une politique industrielle avant la "
     "lettre, fondée sur la protection temporaire.",
 why=["Colbert fait au contraire venir des savoir-faire étrangers mais "
      "confie la gestion à des entrepreneurs français.",
      "La liberté d’installation contredit le principe même du dispositif.",
      "Le monopole est accordé à la manufacture, non réservé à la "
      "noblesse."],
 diss="Le monopole temporaire de Colbert est l’ancêtre de l’argument de "
      "l’industrie dans l’enfance, repris par List puis par les politiques "
      "industrielles contemporaines."),

'ch3-qcm-22': f(niv='comprendre', sp='c3-01',
 exp="Mandeville soutient que les comportements jugés vicieux — luxe, "
     "vanité, recherche du gain — soutiennent l’activité et enrichissent la "
     "collectivité, tandis que la frugalité vertueuse l’appauvrirait. "
     "L’intérêt particulier produit ainsi un résultat collectif non "
     "intentionnel.",
 why=["La charité privée est précisément ce que Mandeville juge "
      "insuffisant.",
      "La vertu individuelle est ce dont il montre l’inefficacité "
      "économique.",
      "Il ne demande pas la punition des vices : il en décrit l’utilité."]),

'ch3-qcm-23': f(niv='comprendre', sp='c3-01',
 exp="Quesnay est le premier à représenter l’économie comme un circuit "
     "fermé : la production agricole se distribue entre trois classes, "
     "circule par les dépenses et revient au point de départ. Keynes "
     "reprendra cette logique de circuit, et la comptabilité nationale "
     "l’institutionnalisera.",
 why=["Smith analyse la division du travail et l’échange, non un circuit "
      "formalisé.",
      "Keynes s’inscrit dans cette tradition mais deux siècles plus tard.",
      "Marx analyse les rapports de production et la reproduction du "
      "capital, après Quesnay."]),

'ch3-qcm-25': f(niv='connaitre', sp='c3-01',
 exp="Saint-Gobain, manufacture royale des glaces créée sous Colbert, "
     "existe toujours. L’exemple sert à montrer la longévité de certaines "
     "créations de la politique industrielle d’État.",
 why=["Renault est une entreprise du XXᵉ siècle.",
      "Air France est créée en 1933.",
      "La Poste descend des services postaux royaux mais n’est pas une "
      "manufacture colbertiste."]),

'ch3-qcm-26': f(niv='comprendre', sp='c3-01',
 exp="Dans le Tableau, le produit net dégagé par la classe productive est "
     "versé aux propriétaires sous forme de rente ; ceux-ci le dépensent "
     "auprès de la classe productive et de la classe stérile, laquelle "
     "achète à son tour des produits agricoles. Le flux boucle et la "
     "reproduction se répète à l’identique.",
 why=["La classe productive ne conserve pas le produit net : elle le verse "
      "en rente.",
      "L’État n’est pas le destinataire du produit net dans le schéma.",
      "Le partage n’est pas égalitaire : il est fonctionnel, selon le rôle "
      "de chaque classe."]),

'ch3-qcm-27': f(niv='comprendre', sp='c3-01',
 exp="Les mercantilistes sont natalistes : la population est une ressource "
     "de puissance — main-d’œuvre, soldats, contribuables. Bodin le résume "
     "par « il n’est richesse ni force que d’hommes ». C’est l’exact opposé "
     "de la thèse malthusienne, formulée deux siècles plus tard.",
 why=["Le pessimisme démographique est la position de Malthus (1798).",
      "La question démographique est au contraire centrale chez eux.",
      "Le recours à l’immigration n’est pas leur raisonnement : ils misent "
      "sur la natalité."]),

'ch3-qcm-29': f(niv='connaitre', sp='c3-01',
 exp="Quesnay distingue trois avances : les avances annuelles — semences, "
     "salaires de l’année ; les avances foncières — aménagements durables du "
     "sol ; les avances primitives — outillage et bétail, immobilisés sur "
     "plusieurs années. C’est l’ancêtre de la distinction entre capital "
     "circulant et capital fixe.",
 why=["La nomenclature immobilière et financière est moderne.",
      "Le classement par durée existe, mais ce ne sont pas les termes de "
      "Quesnay.",
      "La distinction public / privé n’a pas de sens dans son schéma."]),

'ch3-vf-1': f(niv='connaitre', sp='c3-01',
 exp="Les mercantilistes sont protectionnistes : puisque la richesse se "
     "mesure au stock de métaux précieux, il faut exporter plus "
     "qu’importer, donc protéger le marché intérieur par des droits de "
     "douane. Le libre-échange sera la thèse des classiques, un siècle et "
     "demi plus tard."),

'ch3-vf-5': f(niv='comprendre', sp='c3-01',
 exp="Mandeville soutient l’inverse : ce sont les vices privés — luxe, "
     "vanité, intérêt — qui engendrent le bien public, tandis qu’une "
     "société vertueuse et frugale verrait son activité s’effondrer. La "
     "provocation morale sert une thèse économique."),

'ch3-vf-6': f(niv='connaitre', sp='c3-01',
 exp="Le Tableau économique (1758) est bien la première représentation "
     "d’ensemble de la circulation des richesses entre classes sociales. "
     "Son originalité est de montrer que les dépenses des uns sont les "
     "revenus des autres, et que le circuit doit boucler pour que la "
     "reproduction se poursuive."),

'ch3-vf-13': f(niv='connaitre', sp='c3-01',
 exp="Vincent de Gournay appartient au courant physiocrate et lui donne sa "
     "formule politique : « Laissez faire les hommes, laissez passer les "
     "marchandises ». Elle condense la confiance dans un ordre naturel que "
     "l’intervention ne ferait que troubler."),

'ch3-vf-14': f(niv='comprendre', sp='c3-01',
 exp="C’est bien la logique colbertiste : la puissance passe par "
     "l’industrie et les manufactures, soutenues par l’État et protégées de "
     "la concurrence étrangère. Les physiocrates lui reprocheront "
     "précisément de négliger l’agriculture, seule source de produit net à "
     "leurs yeux."),

'ch3-vf-15': f(niv='connaitre', sp='c3-01',
 exp="Pour les mercantilistes, la richesse vient du commerce extérieur et de "
     "l’accumulation de métaux précieux qu’il permet, non de l’agriculture. "
     "C’est la physiocratie qui fera de la terre la seule source de richesse "
     "nouvelle."),

'ch3-vf-16': f(niv='comprendre', sp='c3-01',
 exp="Le Tableau décrit une reproduction à l’identique : les mêmes flux se "
     "répètent d’une année sur l’autre, sans accumulation ni croissance. "
     "C’est une économie stationnaire, ce qui marque la limite du modèle et "
     "ce que les classiques lui reprocheront."),

'ch3-vf-19': f(niv='connaitre', sp='c3-01',
 exp="L’expression désigne l’intervention volontaire et visible de l’État "
     "dans l’économie, par opposition à la main invisible de Smith. Elle "
     "convient au colbertisme : manufactures créées par l’État, monopoles "
     "octroyés, protection organisée."),

'ch3-vf-20': f(niv='comprendre', sp='c3-01',
 exp="Les physiocrates sont les premiers à fonder une doctrine libérale sur "
     "l’idée d’un ordre naturel : l’économie obéit à des lois analogues aux "
     "lois physiques, que l’intervention humaine ne peut que perturber. "
     "D’où le laissez-faire de Gournay."),

'ch3-open-15': f(niv='comprendre', sp='c3-01',
 ans={'modele': "Un paradigme est un cadre de pensée dominant : il fixe les "
      "questions légitimes, les concepts admis et les méthodes acceptées. "
      "En économie, le paradigme classique puis néoclassique a longtemps "
      "défini l’orthodoxie ; les courants hétérodoxes en contestent les "
      "fondements. Un paradigme change quand ses anomalies deviennent trop "
      "visibles, comme la stagflation pour le keynésianisme.",
      'cles': [{'f': ['cadre', 'dominant', 'pensee'], 'l': 'c’est un cadre de pensée dominant'},
               {'f': ['question', 'methode', 'concept'],
                'l': 'il fixe les questions et les méthodes admises'},
               {'f': ['orthodox', 'heterodox', 'conteste'],
                'l': 'il définit l’orthodoxie, que les hétérodoxes contestent'}]},
 exp="Le cours s’en sert pour organiser les cinq courants : ce ne sont pas "
     "des opinions mais des cadres rivaux, chacun avec ses hypothèses sur la "
     "coordination, la valeur et le rôle de l’État."),

# ================================= c3-02 · les classiques
'ch3-qcm-9': f(niv='connaitre', sp='c3-02',
 exp="Smith illustre la division du travail par la manufacture d’épingles : "
     "l’opération décomposée en dix-huit tâches fait passer la production "
     "d’un ouvrier de 20 à 4 800 épingles par jour. Trois causes : "
     "l’habileté acquise, le temps gagné sur les changements de tâche, "
     "l’invention de machines.",
 why=["La sidérurgie n’est pas l’exemple retenu.",
      "L’agriculture sert d’exemple chez les physiocrates.",
      "Le textile illustrera plutôt la révolution industrielle."]),

'ch3-qcm-11': f(niv='comprendre', sp='c3-02',
 exp="L’avantage absolu, chez Smith, désigne la capacité à produire un bien "
     "avec moins de travail qu’un autre pays. Chaque pays se spécialise là "
     "où il est le meilleur en valeur absolue. La limite est immédiate : un "
     "pays sans aucun avantage absolu serait exclu de l’échange.",
 why=["Le coût d’opportunité est le critère de Ricardo, qui lève justement "
      "cette limite.",
      "La spécialisation primaire n’est pas la définition de l’avantage "
      "absolu.",
      "Les droits de douane relèvent du protectionnisme, que Smith combat."]),

'ch3-qcm-12': f(niv='comprendre', sp='c3-02',
 exp="L’avantage comparatif de Ricardo repose sur le coût d’opportunité : "
     "chaque pays se spécialise là où il renonce au moins, même s’il est "
     "moins productif partout. C’est la levée de la limite de Smith : "
     "l’échange devient mutuellement avantageux y compris pour un pays "
     "dominé en tout.",
 why=["Se spécialiser là où l’on est le plus productif dans l’absolu, c’est "
      "l’avantage absolu de Smith.",
      "Il n’est pas question d’imposition d’un pays à un autre : le modèle "
      "est volontaire et réciproque.",
      "Ricardo montre au contraire que l’échange reste avantageux même en "
      "cas de supériorité générale d’un pays."],
 diss="L’enchaînement Smith → Ricardo est la base de tout sujet sur le "
      "commerce : il montre qu’un argument en faveur de l’ouverture a été "
      "renforcé en élargissant sa portée, et non abandonné."),

'ch3-qcm-13': f(niv='comprendre', sp='c3-02',
 exp="La loi des rendements décroissants énonce qu’à technique inchangée, "
     "chaque unité supplémentaire de facteur appliquée à une terre donnée "
     "produit un supplément de récolte de plus en plus faible. Ricardo en "
     "tire la rente différentielle et la baisse tendancielle du profit.",
 why=["Des coûts qui diminuent avec la production décrivent des rendements "
      "croissants.",
      "La productivité croissant avec la taille du marché est l’idée de "
      "Smith sur l’étendue du marché.",
      "L’égalité épargne-investissement est une tout autre proposition."]),

'ch3-qcm-14': f(niv='comprendre', sp='c3-02',
 exp="L’état stationnaire est l’aboutissement du raisonnement de Ricardo : "
     "la mise en culture de terres de moins en moins fertiles élève la rente "
     "et comprime le profit ; quand le profit s’annule, l’investissement "
     "cesse et la croissance s’arrête. C’est une vision pessimiste du "
     "capitalisme.",
 why=["C’est l’inverse : l’état stationnaire est le terme de la croissance.",
      "L’équilibre général est un concept walrasien, postérieur.",
      "L’inflation n’intervient pas dans ce raisonnement réel."]),

'ch3-qcm-15': f(niv='connaitre', sp='c3-02',
 exp="Ricardo publie les Principes de l’économie politique et de l’impôt en "
     "1817. L’ouvrage contient la théorie de la rente différentielle, la loi "
     "des rendements décroissants et l’avantage comparatif.",
 why=["1776 est la date de La Richesse des nations de Smith.",
      "1798 est celle de l’Essai sur le principe de population de Malthus.",
      "1867 est celle du livre I du Capital de Marx."]),

'ch3-qcm-19': f(niv='comprendre', sp='c3-02',
 exp="Malthus partage le pessimisme de Ricardo : la population croissant "
     "plus vite que les subsistances, l’économie bute sur une limite. Les "
     "deux s’opposent ainsi à l’optimisme de Smith, qui voit dans la "
     "division du travail une source de progrès continu.",
 why=["L’optimisme smithien n’est pas celui de Malthus.",
      "Sa position est explicitement pessimiste, non neutre.",
      "Malthus annonce certaines intuitions keynésiennes sur la demande, "
      "mais il n’est pas interventionniste au sens de Keynes."]),

'ch3-qcm-20': f(niv='comprendre', sp='c3-02',
 exp="Le coût d’opportunité est la valeur de ce à quoi l’on renonce en "
     "choisissant une production plutôt qu’une autre. C’est le fondement de "
     "l’avantage comparatif : ce qui compte n’est pas la productivité "
     "absolue, mais ce que l’on sacrifie pour produire.",
 why=["Le coût de production en termes absolus est le critère de Smith.",
      "La différence prix-coût marginal est une marge, notion "
      "microéconomique.",
      "Le coût d’entrée sur un marché est une barrière à l’entrée."]),

'ch3-qcm-24': f(niv='raisonner', sp='c3-02',
 exp="À mesure que la population croît, il faut cultiver des terres moins "
     "fertiles. Le prix du blé s’aligne sur le coût de la terre la plus "
     "coûteuse, ce qui enrichit les propriétaires des meilleures terres — la "
     "rente — et comprime le profit des fermiers, le salaire restant au "
     "niveau de subsistance. Le profit tend donc à disparaître.",
 why=["Les profits ne suivent pas la production agricole : ils sont rognés "
      "par la rente.",
      "La stabilité par le progrès technique est l’objection faite à "
      "Ricardo, non sa thèse.",
      "Les rentes augmentent, elles ne baissent pas."],
 diss="Ce mécanisme est la première analyse d’un conflit de répartition : "
      "rente, profit et salaire ne peuvent croître ensemble, ce que Marx "
      "radicalisera."),

'ch3-qcm-30': f(niv='comprendre', sp='c3-02',
 exp="Les classiques reprochent à Quesnay de réserver la création de "
     "richesse à l’agriculture et de qualifier de stérile le travail "
     "industriel et commercial. Smith montre au contraire que c’est le "
     "travail, dans toutes ses branches, qui est la source de la valeur.",
 why=["La surévaluation de la monnaie est le reproche adressé aux "
      "mercantilistes.",
      "La fiscalité agricole est au cœur de la doctrine physiocrate, non de "
      "la critique classique.",
      "Le Tableau est au contraire stationnaire, donc peu optimiste."]),

'ch3-qcm-31': f(niv='appliquer', sp='c3-02',
 exp="La mise en culture de terres moins fertiles élève le coût de "
     "production marginal, donc le prix du blé. Les propriétaires des terres "
     "les plus fertiles encaissent la différence sous forme de rente, tandis "
     "que les fermiers voient leur profit comprimé. C’est la rente "
     "différentielle.",
 why=["Les rentes augmentent : c’est l’inverse.",
      "Les salaires restent au niveau de subsistance dans le modèle.",
      "Le prix du blé augmente, puisqu’il s’aligne sur la terre la plus "
      "coûteuse."]),

'ch3-qcm-32': f(niv='comprendre', sp='c3-02',
 exp="Le gain à l’échange vient de la réallocation : en se spécialisant "
     "selon les avantages comparatifs, la production mondiale totale "
     "augmente, et chaque pays peut consommer davantage qu’en autarcie. Le "
     "gain est donc collectif avant d’être réparti.",
 why=["L’écart de revenus entre pays ne mesure pas le gain à l’échange.",
      "Le bénéfice des barrières douanières est l’argument inverse.",
      "Le gain ne se limite pas aux exportations : il porte sur la "
      "consommation totale."]),

'ch3-vf-3': f(niv='comprendre', sp='c3-02',
 exp="Smith est optimiste : la division du travail, l’extension du marché et "
     "l’accumulation entretiennent une croissance durable. Ricardo est "
     "pessimiste : les rendements décroissants conduisent à l’état "
     "stationnaire. Cette opposition structure le courant classique."),

'ch3-vf-4': f(niv='comprendre', sp='c3-02',
 exp="C’est la position de Smith, et précisément celle que Ricardo dépasse. "
     "Chez Ricardo, la spécialisation suit l’avantage comparatif, fondé sur "
     "le coût d’opportunité : un pays désavantagé partout gagne encore à "
     "l’échange."),

'ch3-vf-7': f(niv='comprendre', sp='c3-02',
 exp="Colbert pratique un protectionnisme sélectif vers l’extérieur, tout en "
     "unifiant et libérant les échanges à l’intérieur du royaume. La "
     "combinaison est cohérente : protéger la production nationale "
     "naissante, mais supprimer les péages internes qui l’entravent."),

'ch3-vf-8': f(niv='connaitre', sp='c3-02',
 exp="Smith et Ricardo adhèrent tous deux à une théorie de la valeur "
     "travail : la valeur d’un bien dépend de la quantité de travail "
     "nécessaire à sa production. C’est cette théorie que les néoclassiques "
     "remplaceront par la valeur-utilité, et que Marx prolongera jusqu’à la "
     "plus-value."),

'ch3-vf-10': f(niv='connaitre', sp='c3-02',
 exp="L’autarcie désigne au contraire l’absence d’échanges avec l’extérieur. "
     "C’est la situation de référence dans les démonstrations de Smith et "
     "Ricardo : on compare la consommation en autarcie et après "
     "spécialisation pour mesurer le gain à l’échange."),

'ch3-vf-11': f(niv='connaitre', sp='c3-02',
 exp="C’est bien la définition du coût d’opportunité, et le fondement de "
     "l’avantage comparatif : le choix de produire un bien se paie du "
     "renoncement à produire l’autre, et c’est ce rapport de renoncement, "
     "non la productivité absolue, qui commande la spécialisation."),

'ch3-vf-12': f(niv='comprendre', sp='c3-02',
 exp="L’état stationnaire est au contraire la conclusion pessimiste de "
     "Ricardo : lorsque la rente a absorbé le surplus, le profit s’annule, "
     "l’investissement cesse et la croissance s’arrête. Le capitalisme porte "
     "en lui sa propre limite."),

'ch3-vf-17': f(niv='comprendre', sp='c3-02',
 exp="C’est la proposition de Smith : la division du travail est limitée par "
     "l’étendue du marché. Spécialiser les tâches n’a de sens que si les "
     "quantités écoulées le justifient, ce qui fait du commerce — intérieur "
     "comme extérieur — une condition du progrès de la productivité."),

'ch3-vf-18': f(niv='connaitre', sp='c3-02',
 exp="Ricardo est le pessimiste du courant classique : rendements "
     "décroissants, rente qui absorbe le surplus, état stationnaire. "
     "L’optimiste est Smith, qui fait de la division du travail un moteur "
     "durable d’enrichissement."),

'ch3-open-1': f(niv='connaitre', sp='c3-02',
 ans={'modele': "La main invisible désigne le mécanisme par lequel la "
      "poursuite de l’intérêt individuel aboutit, sans intention ni "
      "coordination, à un résultat collectivement favorable. Les prix "
      "transmettent l’information et orientent les ressources là où la "
      "demande est la plus forte. Smith ne dit pas que le marché est "
      "parfait : il décrit une coordination non intentionnelle.",
      'cles': [{'f': ['interet individuel', 'intérêt individuel', 'egoisme'],
                'l': 'elle part de l’intérêt individuel'},
               {'f': ['interet general', 'collectif', 'bien commun'],
                'l': 'elle aboutit à un résultat collectif'},
               {'f': ['prix', 'marche', 'coordination'],
                'l': 'la coordination passe par les prix, sans intention'}]},
 exp="La formule n’apparaît que rarement sous la plume de Smith : elle "
     "résume une intuition, non une démonstration d’optimalité, laquelle "
     "viendra avec Walras et Pareto."),

'ch3-open-2': f(niv='comprendre', sp='c3-02',
 ans={'modele': "Chaque pays se spécialise dans la production pour laquelle "
      "son coût d’opportunité est le plus faible, c’est-à-dire là où il est "
      "relativement le meilleur — ou le moins mauvais — puis échange. La "
      "production mondiale totale augmente et chaque pays consomme plus "
      "qu’en autarcie. L’échange reste avantageux même pour un pays moins "
      "productif dans tous les secteurs : c’est l’apport décisif par rapport "
      "à l’avantage absolu de Smith.",
      'cles': [{'f': ['cout d opportunite', 'coût d’opportunité', 'relatif'],
                'l': 'la spécialisation suit le coût d’opportunité'},
               {'f': ['specialis'], 'l': 'chaque pays se spécialise'},
               {'f': ['autarcie', 'consomme plus', 'gain'],
                'l': 'chacun consomme plus qu’en autarcie'},
               {'f': ['absolu', 'smith', 'moins productif'],
                'l': 'l’échange vaut même pour un pays désavantagé partout'}]},
 exp="L’exemple canonique du cours — Portugal et Angleterre, vin et drap — "
     "sert à vérifier que l’on raisonne bien en renoncements et non en "
     "productivités absolues."),
}

FIX.update({

# ============================ c3-03 · Malthus, Say et Marx
'ch3-open-3': f(niv='connaitre', sp='c3-03',
 ans={'modele': "La loi des débouchés de Jean-Baptiste Say énonce que "
      "« l’offre crée sa propre demande » : toute production distribue des "
      "revenus — salaires, profits, rentes — qui seront dépensés pour "
      "acheter d’autres produits. Une crise générale de surproduction est "
      "donc impossible ; seuls des déséquilibres sectoriels, temporaires, "
      "peuvent apparaître. La thésaurisation est supposée nulle ou "
      "marginale.",
      'cles': [{'f': ['offre cree sa propre demande', 'offre crée sa propre demande', 'offre cree'],
                'l': 'l’offre crée sa propre demande'},
               {'f': ['revenu', 'distribue'],
                'l': 'la production distribue des revenus'},
               {'f': ['surproduction', 'crise generale', 'impossible'],
                'l': 'la crise générale de surproduction est exclue'}]},
 exp="La loi suppose que la monnaie n’est qu’un intermédiaire : si les "
     "agents en conservent, la boucle se rompt. C’est précisément ce que "
     "contesteront Malthus puis Keynes avec la demande effective.",
 diss="Say est la cible explicite de Keynes : opposer les deux permet de "
      "construire une partie entière sur la possibilité d’un équilibre de "
      "sous-emploi."),

'ch3-open-5': f(niv='comprendre', sp='c3-03',
 ans={'modele': "Marx reproche au capitalisme l’exploitation du travail. "
      "L’ouvrier vend sa force de travail pour un salaire correspondant au "
      "coût de sa reproduction, mais produit dans la journée une valeur "
      "supérieure : la différence, non rémunérée, est la plus-value, "
      "appropriée par le capitaliste. Le capital constant — machines — ne "
      "crée aucune valeur nouvelle ; seul le capital variable, le travail "
      "vivant, en crée.",
      'cles': [{'f': ['force de travail'], 'l': 'l’ouvrier vend sa force de travail'},
               {'f': ['plus value', 'plus-value'], 'l': 'la différence non payée est la plus-value'},
               {'f': ['salaire', 'subsistance', 'reproduction'],
                'l': 'le salaire couvre la reproduction de la force de travail'},
               {'f': ['capital variable', 'capital constant', 'travail vivant'],
                'l': 'seul le capital variable crée de la valeur'}]},
 exp="La critique est structurelle, non morale : l’exploitation n’est pas "
     "une faute individuelle du capitaliste mais la condition de "
     "fonctionnement d’un rapport social de production."),

'ch3-open-11': f(niv='comprendre', sp='c3-03',
 ans={'modele': "La valeur-travail, défendue par Smith, Ricardo et Marx, "
      "fait dépendre la valeur d’un bien du temps de travail socialement "
      "nécessaire à sa production : elle est du côté de l’offre et du passé. "
      "La valeur-utilité, défendue par les néoclassiques, la fait dépendre "
      "de la satisfaction que le bien procure au dernier consommateur : elle "
      "est du côté de la demande et de l’usage. L’une explique la valeur par "
      "le coût, l’autre par le désir.",
      'cles': [{'f': ['travail', 'temps de travail'],
                'l': 'la valeur-travail dépend du travail incorporé'},
               {'f': ['utilite', 'utilité', 'satisfaction'],
                'l': 'la valeur-utilité dépend de la satisfaction procurée'},
               {'f': ['marginal', 'derniere unite', 'consommateur', 'demande'],
                'l': 'la seconde raisonne à la marge, du côté de la demande'}]},
 exp="Le basculement est le cœur de la révolution marginaliste des années "
     "1870 : il déplace l’explication de la production vers le choix, et "
     "fonde l’analyse microéconomique."),

'ch3-open-12': f(niv='comprendre', sp='c3-08',
 ans={'modele': "L’école de la régulation analyse le capitalisme comme un "
      "système historique et institutionnel : il n’est pas spontanément "
      "stable, et sa croissance dépend de règles, de normes et de compromis "
      "sociaux. Elle articule un régime d’accumulation — la façon dont "
      "production, répartition et consommation s’ajustent — et un mode de "
      "régulation, l’ensemble des institutions qui le rendent viable.",
      'cles': [{'f': ['institution'], 'l': 'les institutions sont au centre'},
               {'f': ['historique', 'periode', 'crise'],
                'l': 'le capitalisme est analysé comme système historique'},
               {'f': ['regime d accumulation', 'accumulation', 'regulation'],
                'l': 'régime d’accumulation et mode de régulation'},
               {'f': ['stable', 'auto', 'compromis'],
                'l': 'il n’est pas naturellement stable'}]},
 exp="La thèse centrale est qu’une période de croissance durable suppose la "
     "cohérence entre la façon de produire et la façon de répartir : c’est "
     "la rupture de cette cohérence qui fait les grandes crises."),

# =============================== c3-04 · les néoclassiques
'ch3-open-9': f(niv='comprendre', sp='c3-04',
 ans={'modele': "Le courant néoclassique part de l’individu : c’est "
      "l’individualisme méthodologique. L’agent est supposé rationnel — "
      "l’Homo œconomicus — et maximise son utilité sous contrainte de "
      "ressources. Les grandeurs collectives s’expliquent par l’agrégation "
      "de ces choix. Le raisonnement se fait à la marge, et l’équilibre "
      "résulte de la confrontation de l’offre et de la demande.",
      'cles': [{'f': ['individu', 'individualisme'],
                'l': 'l’analyse part de l’individu'},
               {'f': ['rationnel', 'homo'], 'l': 'l’agent est supposé rationnel'},
               {'f': ['utilite', 'utilité', 'maximis'],
                'l': 'il maximise son utilité'},
               {'f': ['contrainte', 'budget', 'ressources'],
                'l': 'sous contrainte de ressources'}]},
 exp="Trois auteurs fondent simultanément ce programme au début des années "
     "1870 : Jevons (1871), Menger (1871) et Walras (1874), rejoints par "
     "Marshall (1890)."),

'ch3-open-10': f(niv='connaitre', sp='c3-04',
 ans={'modele': "L’utilité marginale est la satisfaction supplémentaire "
      "procurée par la consommation d’une unité additionnelle d’un bien. "
      "Elle est décroissante : chaque unité supplémentaire apporte moins que "
      "la précédente. C’est de cette décroissance que découle la pente de la "
      "courbe de demande, et la résolution du paradoxe de l’eau et du "
      "diamant.",
      'cles': [{'f': ['supplementaire', 'additionnelle', 'unite'],
                'l': 'elle porte sur une unité supplémentaire'},
               {'f': ['satisfaction', 'utilite'],
                'l': 'elle mesure la satisfaction procurée'},
               {'f': ['decroissante', 'décroissante', 'diminue'],
                'l': 'elle est décroissante'}]},
 exp="Le raisonnement à la marge est la vraie rupture : ce n’est plus la "
     "valeur totale d’un bien qui explique son prix, mais la valeur de sa "
     "dernière unité disponible."),

'ch3-open-14': f(niv='comprendre', sp='c3-04',
 ans={'modele': "L’économie comportementale conteste l’hypothèse de "
      "rationalité parfaite du modèle standard. Elle montre, par "
      "l’expérimentation, que les décisions sont affectées par des biais "
      "cognitifs, des émotions, des effets de contexte et de cadrage, et "
      "que les agents disposent d’une rationalité limitée. Les préférences "
      "ne sont ni stables ni toujours cohérentes.",
      'cles': [{'f': ['rationalite', 'rationnel', 'rationalité'],
                'l': 'elle conteste la rationalité parfaite'},
               {'f': ['biais'], 'l': 'elle met en évidence des biais cognitifs'},
               {'f': ['emotion', 'contexte', 'cadrage', 'limitee'],
                'l': 'émotions, contexte et rationalité limitée pèsent sur les choix'}]},
 exp="La portée est méthodologique : si les préférences dépendent de la "
     "présentation des options, l’optimalité du marché n’est plus garantie, "
     "et l’action publique peut agir sur l’architecture des choix."),

'ch3-aut195-2': f(niv='raisonner', sp='c3-04',
 exp="Pour l’école autrichienne, aucun agent ne détient une vision globale "
     "du système : l’information est dispersée entre des millions "
     "d’individus. Les prix la résument et la transmettent sans que "
     "personne n’ait à la rassembler. La concurrence est donc un processus "
     "de découverte, non un état d’équilibre à atteindre.",
 why=["Hayek soutient exactement l’inverse : l’information est imparfaite et "
      "dispersée, c’est le point de départ de son analyse.",
      "L’équilibre général est la préoccupation walrasienne, que Hayek juge "
      "peu pertinente.",
      "L’élimination des profits décrirait la concurrence pure et parfaite, "
      "autre cadre."],
 diss="Opposition féconde avec Walras : chez l’un, le marché est un "
      "mécanisme d’allocation optimale ; chez l’autre, un procédé de "
      "production d’information. Les politiques de concurrence s’en "
      "trouvent justifiées différemment."),

# ====================== c3-05 et c3-06 · Keynes et « les classiques »
'ch3-qcm-10': f(niv='connaitre', sp='c3-02',
 exp="Smith rapporte qu’un ouvrier seul produirait au mieux une vingtaine "
     "d’épingles par jour, tandis que la division du travail en dix-huit "
     "opérations permet d’en produire 4 800 par ouvrier. Le gain vient de "
     "l’habileté acquise, du temps économisé et de la mécanisation.",
 why=["10 → 1 000 sous-estime l’écart décrit par Smith.",
      "50 → 10 000 ne correspond pas aux chiffres de l’exemple.",
      "100 → 20 000 non plus."]),

'ch3-qcm-28': f(niv='connaitre', sp='c3-02',
 exp="La main invisible désigne la coordination non intentionnelle des "
     "décisions individuelles par le marché : chacun poursuivant son "
     "intérêt, les prix orientent les ressources et le résultat collectif "
     "est satisfaisant sans qu’aucune autorité ne l’ait voulu.",
 why=["L’intervention de l’État en est exactement l’opposé.",
      "Le contrôle de la monnaie par la banque centrale est une "
      "institution, non un mécanisme spontané.",
      "La régulation par les syndicats est une coordination intentionnelle."]),

'ch3-open-6': f(niv='connaitre', sp='c3-05',
 ans={'modele': "La demande effective est la demande que les entrepreneurs "
      "anticipent et sur laquelle ils règlent leur production et leurs "
      "embauches. Elle est donc la variable déterminante du niveau "
      "d’activité et d’emploi, à l’inverse de la loi de Say pour qui "
      "l’offre commande. Rien ne garantit qu’elle corresponde au niveau de "
      "plein emploi.",
      'cles': [{'f': ['anticipe', 'anticipée', 'entrepreneur'],
                'l': 'c’est la demande anticipée par les entrepreneurs'},
               {'f': ['production', 'emploi'],
                'l': 'elle détermine la production et l’emploi'},
               {'f': ['say', 'offre'], 'l': 'elle renverse la loi de Say'}]},
 exp="Le cours rappelle que Malthus en avait eu l’intuition cent cinquante "
     "ans plus tôt : si les revenus sont trop faibles, la demande solvable "
     "manque et la production recule."),

'ch3-open-7': f(niv='comprendre', sp='c3-05',
 ans={'modele': "L’équilibre de sous-emploi est une situation stable où "
      "production et demande s’égalisent à un niveau inférieur au plein "
      "emploi. Comme l’ajustement se fait par les quantités et non par les "
      "prix, rien ne ramène spontanément l’économie au plein emploi : les "
      "entreprises produisent ce qu’elles anticipent de vendre, et des "
      "anticipations pessimistes se vérifient d’elles-mêmes. D’où la "
      "nécessité d’une intervention publique sur la demande.",
      'cles': [{'f': ['sous emploi', 'sous-emploi', 'chomage'],
                'l': 'l’équilibre peut s’établir sous le plein emploi'},
               {'f': ['demande effective', 'demande'],
                'l': 'la demande effective est insuffisante'},
               {'f': ['quantite', 'quantité', 'prix'],
                'l': 'l’ajustement se fait par les quantités'},
               {'f': ['etat', 'État', 'intervention', 'relance'],
                'l': 'd’où la justification de l’intervention publique'}]},
 exp="Le mot « équilibre » est décisif : il ne s’agit pas d’un déséquilibre "
     "transitoire que le marché corrigerait, mais d’une position stable."),

'ch3-open-4': f(niv='comprendre', sp='c3-06',
 ans={'modele': "Pour les classiques, la monnaie n’est qu’un voile : elle "
      "facilite les échanges mais n’affecte pas les grandeurs réelles — "
      "production, emploi, prix relatifs. Une variation de la quantité de "
      "monnaie ne modifie que le niveau général des prix. C’est la thèse de "
      "la neutralité, formalisée par la théorie quantitative.",
      'cles': [{'f': ['voile', 'neutre', 'neutralite'],
                'l': 'la monnaie est un voile, elle est neutre'},
               {'f': ['echange', 'intermediaire'],
                'l': 'elle facilite les échanges'},
               {'f': ['prix'], 'l': 'elle n’agit que sur le niveau général des prix'},
               {'f': ['reel', 'réel', 'production'],
                'l': 'elle n’affecte pas les grandeurs réelles'}]},
 exp="Keynes rompt avec cette thèse : la monnaie est désirée pour "
     "elle-même, par préférence pour la liquidité, et le taux d’intérêt "
     "devient un phénomène monétaire qui agit sur l’investissement, donc sur "
     "l’activité."),

'ch3-open-8': f(niv='comprendre', sp='c3-06',
 ans={'modele': "L’État doit soutenir la demande globale lorsque "
      "l’initiative privée est insuffisante : dépenses publiques, grands "
      "travaux, baisse d’impôts, politique monétaire accommodante. "
      "L’objectif n’est pas de remplacer le marché mais de corriger son "
      "fonctionnement spontané pour ramener l’économie vers le plein emploi.",
      'cles': [{'f': ['demande'], 'l': 'il soutient la demande globale'},
               {'f': ['budgetaire', 'depense', 'relance', 'travaux'],
                'l': 'par la dépense publique ou la fiscalité'},
               {'f': ['plein emploi'], 'l': 'l’objectif est le plein emploi'}]},
 exp="Le cours insiste : Keynes ne rejette pas le marché, il en critique la "
     "coordination spontanée. La nuance évite la caricature d’un Keynes "
     "planificateur."),

'ch3-aut195-1': f(niv='raisonner', sp='c3-06',
 exp="Clower distingue la demande notionnelle — ce que les agents "
     "souhaiteraient demander s’ils n’étaient pas contraints — de la demande "
     "effective — ce qu’ils peuvent effectivement demander compte tenu de "
     "leur revenu réalisé. Un agent rationné sur un marché transmet sa "
     "contrainte aux autres : le chômeur consomme moins, ce qui réduit la "
     "demande adressée aux entreprises.",
 why=["L’épargne de précaution et de spéculation sont des motifs de demande "
      "de monnaie chez Keynes.",
      "Chômage frictionnel et structurel relèvent d’une typologie du "
      "chômage, non de la théorie du déséquilibre.",
      "Prix relatifs et prix absolus sont une distinction de théorie "
      "monétaire."],
 diss="Cette distinction donne le fondement microéconomique du multiplicateur : "
      "elle explique pourquoi un déséquilibre se propage au lieu de se "
      "corriger."),

'ch3-aut195-4': f(niv='raisonner', sp='c3-06',
 exp="Chez Malinvaud, la quantité échangée est le minimum de l’offre et de "
     "la demande. Le chômage peut donc provenir d’une demande insuffisante — "
     "chômage keynésien, qu’une relance corrige — ou d’une rentabilité "
     "insuffisante — chômage classique, qu’une relance aggraverait en "
     "augmentant les coûts. Le diagnostic précède donc le choix de la "
     "politique.",
 why=["Justifier toute relance est précisément ce que l’analyse interdit.",
      "L’autorégulation du marché du travail est la thèse opposée.",
      "Le taux de chômage naturel est une notion de Friedman, d’une autre "
      "famille d’analyse."],
 diss="Référence décisive pour éviter le plaidoyer : « cela dépend du régime "
      "de déséquilibre » est la réponse rigoureuse à un sujet sur "
      "l’efficacité des politiques de relance."),

# ===================== c3-07 · nouvelle économie keynésienne
'ch3-vf-2': f(niv='connaitre', sp='c3-01',
 exp="Quesnay range l’industrie et le commerce dans la classe stérile : ils "
     "transforment ou déplacent la richesse sans en créer. Seule "
     "l’agriculture dégage un produit net, c’est-à-dire un surplus sur les "
     "avances consommées."),

'ch3-vf-9': f(niv='connaitre', sp='c3-01',
 exp="La classe stérile comprend les artisans, les commerçants et les "
     "industriels. Les propriétaires fonciers forment une troisième classe, "
     "distincte : ils ne produisent pas mais perçoivent le produit net sous "
     "forme de rente et le remettent en circulation par leurs dépenses."),

# L'énoncé d'origine attribuait la nouvelle économie keynésienne à « Akerlof,
# Stiglitz, Mankiw ». Stiglitz et Mankiw n'apparaissent dans aucun cours :
# l'énoncé est réécrit sans liste d'auteurs.
'ch3-aut195-3': f(niv='raisonner', sp='c3-07',
 q="Quelle est la rupture de la nouvelle économie keynésienne avec la "
   "nouvelle économie classique ?",
 exp="La nouvelle économie keynésienne accepte l’exigence de microfondements "
     "posée par la nouvelle économie classique : partir de comportements "
     "individuels rationnels. Mais elle montre que les marchés réels sont "
     "imparfaits — rigidités de prix et de salaires, asymétries "
     "d’information, concurrence imparfaite — ce qui rétablit la "
     "possibilité d’un chômage involontaire.",
 why=["Elle ne rejette pas la rationalité : elle la conserve et ajoute les "
      "imperfections.",
      "Elle revendique au contraire l’héritage keynésien, qu’elle "
      "reformule.",
      "Le chômage involontaire est précisément ce qu’elle rétablit."],
 diss="C’est l’exemple d’une synthèse théorique : accepter la méthode de "
      "l’adversaire pour retrouver, par elle, les conclusions que l’on "
      "défend."),
})


# =============================================================== questions neuves
NEW = [

f(id='q3-n01', sp='c3-01', niv='comprendre', type='qcmm', b=42,
  q="Quelles affirmations décrivent correctement le système des trois "
    "classes chez Quesnay ? (plusieurs réponses)",
  opts=["La classe productive est constituée des agriculteurs, seuls à "
        "dégager un produit net",
        "La classe des propriétaires perçoit le produit net sous forme de "
        "rente et le remet en circulation",
        "La classe stérile regroupe artisans, commerçants et industriels",
        "La classe stérile est ainsi nommée parce qu’elle ne travaille pas",
        "Le classement repose sur le statut social, non sur la fonction "
        "économique"],
  ans=[0, 1, 2],
  why=["Exacte : seule l’agriculture produit plus qu’elle ne consomme en "
       "avances.",
       "Exacte : les propriétaires ne produisent pas mais assurent la "
       "circulation du surplus par leurs dépenses.",
       "Exacte : ils transforment ou déplacent, sans créer de richesse "
       "nouvelle au sens physiocratique.",
       "La classe stérile travaille : elle est dite stérile parce qu’elle ne "
       "dégage pas de produit net, non parce qu’elle serait oisive.",
       "Le classement est au contraire fonctionnel : il repose sur le rôle "
       "dans la création du produit net."],
  exp="L’intérêt du schéma est d’être une lecture fonctionnelle : chaque "
      "classe est définie par sa place dans la reproduction, non par son "
      "rang social. C’est en cela que le Tableau annonce la comptabilité "
      "nationale."),

f(id='q3-n02', sp='c3-01', niv='raisonner', type='qcm', b=78,
  q="Pourquoi la physiocratie, qui fait de la terre la seule source de "
    "richesse, est-elle néanmoins considérée comme la première doctrine "
    "libérale ?",
  opts=["Parce qu’elle défend la propriété privée de la terre",
        "Parce qu’elle affirme l’existence d’un ordre naturel que "
        "l’intervention ne peut que troubler",
        "Parce qu’elle prône l’industrialisation",
        "Parce qu’elle refuse tout impôt"],
  ans=1,
  why=["La propriété privée est admise par presque toutes les doctrines de "
       "l’époque : ce n’est pas le critère.",
       "Les physiocrates ne prônent pas l’industrialisation : ils tiennent "
       "l’industrie pour stérile.",
       "Ils défendent au contraire un impôt unique, assis sur le produit "
       "net de la terre."],
  exp="Le libéralisme physiocrate est fondé sur une métaphysique de l’ordre "
      "naturel : l’économie obéit à des lois comparables aux lois "
      "physiques, et l’intervention de l’État ne peut que les contrarier. "
      "D’où le laissez-faire de Gournay et l’opposition au colbertisme.",
  diss="Distinguer les fondements du libéralisme — ordre naturel chez les "
       "physiocrates, efficacité de la division du travail chez Smith, "
       "processus de découverte chez Hayek — évite de traiter « le "
       "libéralisme » comme un bloc."),

f(id='q3-n03', sp='c3-02', niv='appliquer', type='qcm', b=222,
  q="Le Portugal produit une unité de vin en 80 heures et une de drap en "
    "90 ; l’Angleterre, 120 heures pour le vin et 100 pour le drap. Que "
    "prescrit l’avantage comparatif ?",
  opts=["Le Portugal doit tout produire, étant plus efficace partout",
        "Le Portugal se spécialise dans le vin, l’Angleterre dans le drap",
        "L’Angleterre ne peut pas participer à l’échange",
        "Chaque pays produit les deux biens, l’échange étant sans gain"],
  ans=1,
  why=["L’avantage absolu portugais ne dit rien : ce qui compte est le "
       "rapport interne des coûts dans chaque pays.",
       "C’est précisément ce que Ricardo réfute : l’Angleterre, désavantagée "
       "partout, gagne pourtant à l’échange.",
       "L’échange produit un gain dès que les rapports de coûts internes "
       "diffèrent, ce qui est le cas ici."],
  exp="Au Portugal, une unité de drap coûte 90/80 = 1,125 unité de vin ; en "
      "Angleterre, 100/120 = 0,83. Le drap est donc relativement moins cher "
      "en Angleterre, qui s’y spécialise, tandis que le Portugal se "
      "spécialise dans le vin. Chacun gagne, bien que le Portugal soit plus "
      "efficace dans les deux productions.",
  diss="Savoir mener ce calcul en deux lignes vaut mieux que réciter la "
       "théorie : c’est ce qui permet de répondre à l’objection « mais la "
       "Chine est meilleure partout »."),

f(id='q3-n04', sp='c3-02', niv='connaitre', type='assoc', b=172,
  q="Associez chaque auteur classique à sa contribution principale.",
  ans=[["Adam Smith", "Division du travail, main invisible et étendue du marché"],
       ["David Ricardo", "Rente différentielle, rendements décroissants et avantage comparatif"],
       ["Thomas Malthus", "Principe de population et intuition de la demande effective"],
       ["Jean-Baptiste Say", "Loi des débouchés : l’offre crée sa propre demande"]],
  exp="Le courant classique n’est pas homogène : Smith est optimiste, "
      "Ricardo et Malthus pessimistes, Say confiant dans l’autorégulation. "
      "Les distinguer évite l’erreur la plus fréquente, qui consiste à "
      "prêter à l’un les thèses de l’autre.",
  diss="Mentionner que Malthus annonce la demande effective permet de "
       "montrer que la critique de la loi de Say naît à l’intérieur même du "
       "courant classique, bien avant Keynes."),

f(id='q3-n05', sp='c3-03', niv='comprendre', type='qcm', b=349,
  q="En quoi Malthus s’oppose-t-il à Say sur la possibilité d’une "
    "surproduction ?",
  opts=["Il nie que la production distribue des revenus",
        "Il soutient que les travailleurs peuvent être trop pauvres pour "
        "acheter ce qu’ils produisent, d’où une demande solvable "
        "insuffisante",
        "Il affirme que la monnaie circule trop vite",
        "Il considère que les débouchés extérieurs suffisent toujours"],
  ans=1,
  why=["Malthus ne conteste pas la distribution de revenus : il conteste que "
       "ces revenus suffisent à écouler la production.",
       "La vitesse de circulation de la monnaie n’est pas son argument.",
       "Il doute au contraire que les débouchés soient automatiquement "
       "trouvés."],
  exp="Malthus introduit la notion de demande solvable : si les revenus "
      "distribués sont trop faibles, la demande baisse, les entreprises "
      "vendent moins, la production diminue et le chômage augmente. Le cours "
      "y voit « une intuition keynésienne cent cinquante ans avant "
      "Keynes ».",
  diss="À utiliser pour montrer qu’un débat théorique majeur — l’offre ou la "
       "demande commande-t-elle l’activité ? — traverse l’histoire de la "
       "discipline depuis le début du XIXᵉ siècle."),

f(id='q3-n06', sp='c3-03', niv='connaitre', type='vf', b=358,
  q="Malthus a maintenu sans changement sa thèse de 1798 sur la population.",
  ans=False,
  exp="Le cours signale une version révisée en 1803, atténuée après ses "
      "voyages et à la lumière de faits nouveaux : progrès de productivité, "
      "importations de blé, émigration. Le cours ajoute l’erreur de fond "
      "rétrospective : Malthus n’a pas vu que la croissance démographique "
      "venait surtout de la baisse de la mortalité, phénomène que Landry "
      "théorisera sous le nom de transition démographique.",
  diss="Mentionner la révision de 1803 évite la caricature et montre qu’un "
       "auteur peut corriger sa thèse : la nuance est toujours mieux notée "
       "que l’étiquette."),

f(id='q3-n07', sp='c3-03', niv='raisonner', type='ordre', b=423,
  q="Remettez dans l’ordre le raisonnement de Marx qui mène à la baisse "
    "tendancielle du taux de profit.",
  ans=["Le capital variable, c’est-à-dire le travail vivant, est la seule source de valeur nouvelle",
       "La plus-value est la part de valeur créée qui n’est pas versée en salaire",
       "La concurrence pousse les entreprises à mécaniser pour produire moins cher",
       "La composition organique du capital s’élève : plus de machines pour moins de travail",
       "Le taux de profit, rapport de la plus-value au capital total, diminue tendanciellement"],
  exp="Chaque étape commande la suivante. Le point décisif est le "
      "troisième : la mécanisation est rationnelle pour chaque capitaliste "
      "pris isolément, mais elle réduit la part du facteur qui, seul, crée "
      "la valeur. Le résultat collectif contredit l’intérêt individuel — "
      "c’est la forme que prend chez Marx la contradiction du capitalisme. "
      "Le cours précise que l’intensification de l’exploitation ne compense "
      "pas la hausse du capital constant.",
  diss="Enchaînement à maîtriser pour tout sujet sur les crises : il offre "
       "une explication endogène, par opposition aux explications par les "
       "chocs extérieurs."),

f(id='q3-n08', sp='c3-04', niv='connaitre', type='assoc', b=612,
  q="Associez chaque fondateur du marginalisme à son ouvrage et à sa date.",
  ans=[["Léon Walras", "Éléments d’économie politique pure (1874)"],
       ["Alfred Marshall", "Principes d’économie politique (1890)"],
       ["William Stanley Jevons", "Théorie de l’économie politique (1871)"],
       ["Carl Menger", "Fondements d’économie politique (1871)"]],
  exp="La révolution marginaliste est simultanée et indépendante : Jevons en "
      "Angleterre, Menger en Autriche et Walras en Suisse publient à trois "
      "ans d’intervalle, Marshall faisant ensuite la synthèse. Cette "
      "simultanéité est l’indice d’un changement de paradigme plutôt que "
      "d’une influence.",
  diss="Citer les trois fondateurs plutôt que le seul Walras montre que le "
       "marginalisme n’est pas une école nationale mais un tournant général "
       "de la discipline."),

f(id='q3-n09', sp='c3-04', niv='appliquer', type='qcm', b=552,
  q="Un consommateur boit un premier verre d’eau après une marche : la "
    "satisfaction est très forte ; le cinquième ne lui procure presque "
    "rien. Quelle propriété ce comportement illustre-t-il, et qu’en "
    "déduit-on ?",
  opts=["L’utilité totale décroît, donc le bien est inférieur",
        "L’utilité marginale est décroissante, ce qui explique que la "
        "demande diminue quand le prix augmente",
        "La contrainte budgétaire est saturée",
        "Les préférences sont instables"],
  ans=1,
  why=["L’utilité totale continue d’augmenter : c’est son accroissement qui "
       "diminue. Un bien inférieur se définit tout autrement, par "
       "l’élasticité-revenu.",
       "La contrainte budgétaire n’est pas en cause : le raisonnement porte "
       "sur la satisfaction, non sur le revenu.",
       "La décroissance de l’utilité marginale n’est pas une instabilité des "
       "préférences, c’est une régularité supposée stable."],
  exp="L’utilité marginale décroissante est le ressort de la demande "
      "néoclassique : le consommateur n’achète une unité de plus que si son "
      "prix est inférieur à la satisfaction qu’elle procure. Quand le prix "
      "monte, le nombre d’unités qui satisfont cette condition diminue. "
      "C’est aussi la résolution du paradoxe de l’eau et du diamant : "
      "l’abondance de l’eau abaisse l’utilité de sa dernière unité."),

f(id='q3-n10', sp='c3-05', niv='raisonner', type='ordre', b=754,
  q="Remettez dans l’ordre l’enchaînement keynésien qui conduit au chômage.",
  ans=["Les entrepreneurs anticipent une demande insuffisante",
       "Ils réduisent leur production, car produire pour ne pas vendre serait ruineux",
       "Ils emploient moins de travail et distribuent donc moins de revenus",
       "La demande effectivement exprimée diminue à son tour",
       "L’économie se stabilise à un niveau d’activité inférieur au plein emploi"],
  exp="L’enchaînement est circulaire, et c’est ce qui le rend redoutable : "
      "l’anticipation pessimiste se vérifie elle-même. Rien dans ce circuit "
      "ne ramène au plein emploi, puisque l’ajustement se fait par les "
      "quantités. Seule une dépense extérieure au circuit — celle de l’État "
      "— peut inverser le mouvement.",
  diss="Dérouler ce cercle est la meilleure façon de justifier une relance : "
       "l’argument ne porte pas sur la générosité publique mais sur la "
       "nature autoréalisatrice des anticipations."),

f(id='q3-n11', sp='c3-06', niv='comprendre', type='qcmm', b=865,
  q="Que Keynes partage-t-il réellement avec « les classiques » ? "
    "(plusieurs réponses)",
  opts=["L’économie de marché comme cadre de référence",
        "La place centrale des décisions individuelles des ménages et des entreprises",
        "L’objectif d’expliquer le niveau de production et d’emploi",
        "La confiance dans l’autorégulation du marché",
        "La neutralité de la monnaie"],
  ans=[0, 1, 2],
  why=["Exacte : Keynes raisonne dans une économie de marché, non planifiée.",
       "Exacte : les décisions restent privées ; le désaccord porte sur leur "
       "coordination.",
       "Exacte : c’est la question commune, à laquelle les réponses "
       "diffèrent.",
       "C’est précisément le point de rupture : ce qui unit les classiques, "
       "selon Keynes, est la confiance dans l’autorégulation.",
       "Keynes rompt avec la neutralité : la monnaie est désirée pour "
       "elle-même et le taux d’intérêt agit sur l’investissement."],
  exp="Le cours insiste : « Keynes ne rejette pas le marché, il critique son "
      "fonctionnement spontané ». Savoir ce que les adversaires partagent "
      "est la condition pour situer exactement le désaccord — ici, la "
      "coordination et le rôle de la monnaie.",
  diss="Commencer par les points communs avant d’exposer la rupture est une "
       "manière sûre d’éviter la dissertation en deux blocs opposés."),

f(id='q3-n12', sp='c3-07', niv='comprendre', type='qcmm', b=1166,
  q="Selon la nouvelle économie keynésienne, quelles imperfections "
    "expliquent la rigidité des prix et des salaires ? (plusieurs réponses)",
  opts=["Les contrats de long terme",
        "Les coûts de modification des prix, ou menu costs",
        "Les normes sociales et les conventions salariales",
        "L’absence totale de rationalité des agents",
        "La parfaite information sur le marché du travail"],
  ans=[0, 1, 2],
  why=["Exacte : un contrat pluriannuel fige salaire ou prix pour sa durée.",
       "Exacte : changer un prix a un coût, ce qui retarde les ajustements.",
       "Exacte : normes et conventions ralentissent les révisions, "
       "notamment à la baisse.",
       "La NEK conserve la rationalité : elle ajoute des imperfections de "
       "marché, elle ne supprime pas la rationalité.",
       "Elle soutient l’inverse : l’information est asymétrique, "
       "particulièrement sur le marché du travail."],
  exp="Trois familles d’imperfections sont invoquées : rigidités, asymétries "
      "d’information — aléa moral, salaires d’efficience — et concurrence "
      "imparfaite, les entreprises étant price makers. Leur conséquence "
      "commune est le retour du chômage involontaire dans un cadre "
      "pourtant microfondé."),

f(id='q3-n13', sp='c3-08', niv='comprendre', type='qcm', b=1284,
  q="Qu’appelle-t-on « sabotage de la production » chez Veblen ?",
  opts=["La destruction volontaire de machines par les ouvriers",
        "Le freinage volontaire de la production par les hommes d’affaires "
        "pour maintenir des prix et des profits élevés",
        "Le refus des ingénieurs d’innover",
        "La grève organisée par les syndicats"],
  ans=1,
  why=["La destruction de machines par les ouvriers est le luddisme, autre "
       "phénomène.",
       "Les ingénieurs incarnent au contraire, chez Veblen, la logique "
       "industrielle d’efficacité.",
       "La grève est une action salariale, étrangère à l’analyse de "
       "Veblen."],
  exp="Dans Théorie de l’entreprise d’affaires (1904), Veblen oppose la "
      "logique industrielle des ingénieurs, orientée vers l’efficacité, à la "
      "logique financière des hommes d’affaires, qui peuvent freiner la "
      "production, sous-utiliser les capacités ou organiser des raretés "
      "artificielles pour tenir les prix. Le capitalisme en devient à la "
      "fois inefficace et instable.",
  diss="Référence précieuse pour un sujet sur la financiarisation : elle "
       "montre que la critique de la domination de la finance sur "
       "l’industrie a plus d’un siècle."),

f(id='q3-n14', sp='c3-08', niv='connaitre', type='assoc', b=1292,
  q="Associez chaque auteur hétérodoxe contemporain à son apport.",
  ans=[["Thorstein Veblen", "Opposition entre logique industrielle et logique financière (1904)"],
       ["Douglass North", "Les institutions expliquent les différences durables de développement"],
       ["École de la régulation", "Régime d’accumulation et mode de régulation d’un capitalisme historique"],
       ["Kate Raworth", "La théorie du donut : un plancher social et un plafond écologique"]],
  exp="Ces quatre apports partagent un refus : celui de traiter l’économie "
      "comme un mécanisme anhistorique. Les institutions, les compromis "
      "sociaux et les limites naturelles y deviennent des variables "
      "explicatives, et non des contraintes extérieures au modèle.",
  diss="Mobiliser ces auteurs en troisième partie permet de dépasser "
       "l’opposition classique entre marché et État, en introduisant les "
       "règles et les limites comme troisième terme."),

f(id='q3-n15', sp='c3-08', niv='raisonner', type='courte', b=1460,
  q="Dans quel contexte Kate Raworth formule-t-elle sa théorie, et que "
    "reproche-t-elle à l’économie dominante ?",
  ans={'modele': "Raworth écrit après la crise financière de 2008, dans un "
       "contexte d’aggravation des inégalités, d’urgence climatique et de "
       "remise en cause du PIB comme indicateur central. Elle reproche à "
       "l’économie dominante de viser prioritairement la croissance du PIB "
       "sans intégrer les contraintes sociales et écologiques. Son modèle "
       "fixe un plancher social à ne pas franchir vers le bas et un plafond "
       "écologique à ne pas dépasser vers le haut.",
       'cles': [{'f': ['2008', 'crise financiere'], 'l': 'le contexte est celui de l’après-2008'},
                {'f': ['inegalite', 'climat', 'ecologique', 'écologique'],
                 'l': 'inégalités et urgence climatique'},
                {'f': ['pib'], 'l': 'la remise en cause du PIB comme indicateur'},
                {'f': ['social', 'plancher', 'plafond', 'limite'],
                 'l': 'un plancher social et un plafond écologique'}]},
  exp="L’ouvrage de référence est L’économie de demain en 7 principes "
      "(2017). L’apport n’est pas un modèle prédictif mais un cadre "
      "normatif : il déplace l’objectif de la croissance vers un espace sûr "
      "et juste pour l’humanité.",
  diss="Utile en ouverture d’un sujet sur la croissance et ses limites, à "
       "condition de préciser qu’il s’agit d’un cadre d’objectifs et non "
       "d’une théorie explicative."),

f(id='q3-n16', sp='c3-08', niv='comprendre', type='vf', b=1296,
  q="Pour Douglass North, les différences durables de développement entre "
    "pays s’expliquent mal par les seules théories économiques standard.",
  ans=True,
  exp="C’est son point de départ : les modèles standard, qui raisonnent sur "
      "des dotations et des prix, expliquent mal pourquoi des pays aux "
      "ressources comparables suivent des trajectoires durablement "
      "divergentes. North y répond par les institutions — règles formelles "
      "et informelles qui structurent les incitations — dans Structure et "
      "changement dans l’histoire économique (1973) puis Institutions, "
      "changement institutionnel et performance économique (1990).",
  diss="Articulation naturelle avec Acemoglu et Robinson : les institutions "
       "inclusives y deviennent la variable explicative première du "
       "développement."),
]

FIX['ch3-open-13'] = f(niv='connaitre', sp='c3-08',
 ans={'modele': "L’institutionnalisme soutient que les décisions "
      "économiques ne sont pas le fait d’individus isolés : elles sont "
      "façonnées par des institutions — coutumes, normes, lois, "
      "organisations — qui structurent les incitations et stabilisent les "
      "comportements. L’analyse est historique : les institutions évoluent, "
      "et leurs différences expliquent des trajectoires de développement "
      "durablement divergentes.",
      'cles': [{'f': ['institution'], 'l': 'les institutions sont la variable centrale'},
               {'f': ['coutume', 'norme', 'loi', 'regle', 'organisation'],
                'l': 'règles formelles et informelles encadrent les choix'},
               {'f': ['individu', 'isole', 'isolé'],
                'l': 'les agents ne sont pas des individus isolés'},
               {'f': ['histoire', 'historique', 'developpement', 'trajectoire'],
                'l': 'l’analyse est historique et explique des trajectoires'}]},
 exp="Le courant va de Veblen (1904) à la nouvelle économie "
     "institutionnelle de North, en passant par l’école de la régulation. "
     "Son unité tient au refus d’un individu abstrait et anhistorique.")
