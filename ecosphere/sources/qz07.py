# -*- coding: utf-8 -*-
"""Chapitre 7 — Développement, sous-développement et soutenabilité."""

SP = {
 'c7-01': 'Croissance et développement : le cas chinois, ODD, indicateurs et RNB',
 'c7-02': 'Pauvreté absolue, recul mondial et recomposition géographique',
 'c7-03': 'Santé, fécondité, éducation : les trois piliers et l’IDH',
 'c7-04': 'Prolongements de l’IDH : IDHI, IIG, IPM, capabilités de Sen',
 'c7-05': 'Portée et limites des indicateurs composites du développement',
 'c7-06': 'Démographie et développement : Malthus, Boserup, transition, dividende',
 'c7-07': 'Limites du modèle démographique ; l’endettement comme levier',
 'c7-08': 'Crise de la dette, PAS et Consensus de Washington',
 'c7-09': 'Dette souveraine financiarisée : le cas argentin et les fonds vautours',
 'c7-10': 'Mondialisation asymétrique : la désindustrialisation de l’Inde (Allen)',
 'c7-11': 'Du retard au blocage : Rostow, Gerschenkron, Perroux, Lewis, Nurkse',
 'c7-12': 'Prebisch, Emmanuel, Amin, Bairoch : dépendance et échange inégal',
 'c7-13': 'Stratégies d’industrialisation : industries industrialisantes, ISI, IPE',
 'c7-14': 'Le vol d’oies sauvages : Akamatsu, Japon, Vernon et HOS',
 'c7-15': 'Le rattrapage japonais : État Meiji, zaibatsu et angles morts du modèle',
 'c7-16': 'La stratégie chinoise : Deng, ZES, OMC, BRI, frontière technologique',
 'c7-17': 'Développement et soutenabilité : IDHP, Hardin, Meadows, Kaya, Carney',
 'c7-18': 'Gouvernance multi-échelles, marché ou règle, économie de rente',
}

# Questions écartées : leur contenu ne s'appuie sur aucun passage du cours de
# ce chapitre, ou bien il est traité ailleurs et la question y est déjà posée.
#   ch7-open-6  : la courbe de l'éléphant de Milanovic relève du chapitre 6.
#   ch7-open-7  : la relation r > g de Piketty n'apparaît dans aucun cours.
#   ch7-qcm-19  : le coefficient de Gini est traité au chapitre 6.
#   ch7-vf-8    : même raison.
#   ch7-qcm-30  : la courbe de Lorenz est traitée au chapitre 6.
#   ch7-qcm-38  : soutenabilité faible / forte : notions du chapitre 6.
#   ch7-vf-16, ch7-open-4, ch7-open-5 : même raison.
#   ch7-open-13 : le capital naturel est défini au chapitre 6.
#   ch7-qcm-17, ch7-vf-17 : le « big push » de Rosenstein-Rodan est absent.
#   ch7-qcm-24, ch7-vf-20 : les BRICS relèvent du cours de deuxième année.
#   ch7-vf-10   : le cours parle du cercle vicieux de Nurkse, non d'une
#                 « trappe à pauvreté » dont il n'énonce jamais la définition.
DROP = ['ch7-open-6', 'ch7-open-7', 'ch7-qcm-19', 'ch7-vf-8', 'ch7-qcm-30',
        'ch7-qcm-38', 'ch7-vf-16', 'ch7-open-4', 'ch7-open-5', 'ch7-open-13',
        'ch7-qcm-17', 'ch7-vf-17', 'ch7-qcm-24', 'ch7-vf-20', 'ch7-vf-10']


def f(**kw):
    return kw


FIX = {

# ----------------------------------------------------- c7-01 cadrage général
'ch7-qcm-1': f(niv='connaitre', sp='c7-01', b=1,
 exp="En septembre 2025, la Chine annonce à l’OMC qu’elle abandonne son "
     "statut de pays en développement. L’événement est techniquement mineur "
     "mais hautement symbolique : il remet en cause la lecture bipolaire du "
     "monde, structurée depuis des décennies autour de l’opposition entre "
     "pays développés et pays en développement.",
 why=["L’entrée de la Chine à l’OMC en 2001 est un autre repère du "
      "chapitre, mobilisé à propos de sa stratégie exportatrice.",
      "Le cours ne retient pas ce classement de PIB comme événement "
      "introductif.",
      "Les ODD de 2015 sont évoqués plus loin, à propos de l’universalisation "
      "du développement."],
 diss="Partir de cet événement permet d’ouvrir sur la thèse du chapitre : la "
      "croissance ne suffit pas à définir le développement, et les catégories "
      "héritées sont devenues trop rigides."),
'ch7-qcm-27': f(niv='comprendre', sp='c7-01', b=23,
 exp="La Chine cumule 1,4 milliard d’habitants, une puissance industrielle et "
     "exportatrice majeure, une place centrale dans les chaînes de valeur — "
     "mais aussi de fortes inégalités internes et des indicateurs sociaux qui "
     "ne la placent pas toujours au niveau des économies les plus avancées. "
     "Elle n’entre donc parfaitement dans aucune des deux catégories.",
 why=["Le cours ne raisonne pas sur une position intermédiaire de PIB.",
      "L’équilibre des échanges n’est pas le critère retenu.",
      "Le caractère mixte du système économique chinois est réel — "
      "« économie socialiste de marché » — mais ce n’est pas ce que désigne "
      "l’expression « pays entre deux »."],
 diss="Le cas chinois est le meilleur argument contre les typologies "
      "binaires : il montre qu’un même pays peut être développé selon un "
      "indicateur et en développement selon un autre."),
'ch7-qcm-6': f(niv='connaitre', sp='c7-01', b=29,
 exp="Le traitement spécial et différencié accorde aux pays en développement "
     "des délais plus longs pour appliquer certaines règles, davantage de "
     "flexibilité dans l’ouverture de leurs marchés et des protections "
     "temporaires pour certains secteurs. L’idée est qu’un pays en phase de "
     "rattrapage ne peut pas être soumis immédiatement aux mêmes contraintes "
     "qu’une économie pleinement industrialisée.",
 why=["Il ne s’agit pas d’un avantage tarifaire accordé à leurs "
      "exportations, mais d’une souplesse dans leurs propres obligations.",
      "Aucune exemption totale n’existe : les pays en développement restent "
      "membres de l’OMC et liés par ses accords.",
      "L’OMC n’est pas un bailleur : elle n’accorde pas d’aide financière."],
 diss="Cette notion est la charnière du cas chinois : renoncer au statut, "
      "c’est renoncer à invoquer ces exceptions."),
'ch7-qcm-7': f(niv='connaitre', sp='c7-01', b=43,
 exp="Le protectionnisme éducateur consiste, pour un pays en retard de "
     "développement, à protéger temporairement ses industries naissantes afin "
     "qu’elles se consolident, gagnent en productivité, atteignent une taille "
     "critique et deviennent compétitives avant d’être pleinement exposées à "
     "la concurrence internationale. La protection n’est pas une fermeture "
     "durable : c’est l’organisation d’un rattrapage.",
 why=["Il ne s’agit pas de subventionner l’éducation : l’adjectif "
      "« éducateur » qualifie l’apprentissage industriel.",
      "Des droits de douane permanents sur toutes les industries seraient "
      "l’inverse de la logique temporaire et ciblée.",
      "Aucune interdiction d’importation de biens éducatifs n’est en cause."],
 diss="Notion à mobiliser dans toute la suite du chapitre : elle fonde l’ISI, "
      "elle explique l’échec indien faute de pouvoir l’utiliser, et elle est "
      "au cœur du modèle du vol d’oies sauvages."),
'ch7-qcm-8': f(niv='connaitre', sp='c7-01', b=177,
 exp="La croissance inclusive ne désigne pas simplement une croissance qui "
     "ajoute des secteurs ou des activités : elle renvoie à une croissance qui "
     "ne laisse pas une partie de la population à l’écart, cherche à réduire "
     "l’exclusion et vise une répartition plus équitable des richesses "
     "produites.",
 why=["Une croissance portée par les seuls secteurs exportateurs serait au "
      "contraire susceptible d’être très peu inclusive.",
      "Le mode de financement, étranger ou national, est indifférent à cette "
      "notion.",
      "La notion ne se limite à aucune catégorie de revenu : elle vaut pour "
      "tous les pays."]),
'ch7-vf-15': f(niv='connaitre', sp='c7-01', b=180,
 exp="C’est la définition même de la croissance inclusive : une croissance "
     "qui ne laisse pas une partie de la population à l’écart et vise une "
     "répartition plus équitable de ses fruits. C’est aussi ce qui montre "
     "qu’un indicateur comme le PIB, bien que central, ne peut suffire à "
     "rendre compte du développement."),
'ch7-qcm-16': f(niv='connaitre', sp='c7-01', b=65,
 exp="Le principe de responsabilités communes mais différenciées structure "
     "les négociations climatiques depuis Kyoto puis l’Accord de Paris : les "
     "pays développés, principaux responsables historiques des émissions, "
     "doivent réduire davantage leurs émissions, financer une partie de la "
     "transition mondiale et aider les pays plus pauvres à se décarboner, "
     "lesquels bénéficient d’une plus grande souplesse et d’un calendrier plus "
     "flexible.",
 why=["Des obligations identiques pour tous seraient exactement l’inverse du "
      "principe.",
      "Les pays en développement ne sont pas exemptés de toute obligation : "
      "ils disposent de souplesse, non d’une dispense.",
      "La différenciation ne porte pas seulement sur le rythme mais sur le "
      "niveau même des engagements et sur le financement."]),
'ch7-qcm-26': f(niv='raisonner', sp='c7-01', b=74,
 exp="Si la Chine cesse d’être perçue comme un pays en développement, elle "
     "pourrait progressivement être considérée comme un pays qui doit "
     "contribuer davantage au financement climatique et assumer des "
     "engagements plus lourds. Autrement dit, elle passerait du camp de ceux "
     "qui reçoivent l’aide à celui de ceux qui doivent contribuer.",
 why=["L’effet est inverse : elle pourrait perdre son accès à certains "
      "financements.",
      "Aucun pays n’est exempté de l’Accord de Paris.",
      "Le changement de statut réduit sa flexibilité, il ne l’augmente pas."],
 diss="L’exemple montre que les catégories statistiques du développement ont "
      "des effets très concrets : commerciaux, diplomatiques et climatiques."),
'ch7-vf-2': f(niv='comprendre', sp='c7-01', b=36,
 exp="En renonçant à ce statut, la Chine ne pourra plus aussi facilement "
     "invoquer les exceptions du traitement spécial et différencié : elle sera "
     "davantage soumise aux mêmes règles que les pays développés et sa "
     "capacité à justifier certaines protections sera plus limitée."),
'ch7-qcm-4': f(niv='connaitre', sp='c7-01', b=159,
 exp="Les Objectifs de Développement Durable sont adoptés par l’ONU en 2015 "
     "pour la période 2015-2030. Ils ne s’adressent pas exclusivement aux "
     "pays du Sud : c’est précisément ce qui marque l’universalisation de "
     "l’objectif de développement.",
 why=["2000 correspond à une autre génération d’objectifs internationaux, que "
      "le cours ne détaille pas.",
      "2008 est l’année de la crise financière, mobilisée ailleurs dans le "
      "chapitre.",
      "2020 est la date de création de l’IDHP, non celle des ODD."]),
'ch7-qcm-29': f(niv='comprendre', sp='c7-01', b=160,
 exp="Depuis les années 2010, les institutions internationales affirment que "
     "le développement est un objectif universel. Les ODD concernent tous les "
     "pays, quel que soit leur niveau de revenu, et impliquent pour toutes les "
     "économies une amélioration des conditions de vie, une réduction des "
     "inégalités et une articulation entre croissance, justice sociale et "
     "soutenabilité environnementale.",
 why=["Les ODD s’adressent explicitement à tous les pays, du Nord comme du "
      "Sud.",
      "L’universalité de l’objectif ne suppose évidemment pas l’égalité des "
      "niveaux de développement.",
      "Les ODD ne se substituent à aucune politique nationale : ils fixent un "
      "cadre d’objectifs."],
 diss="Nuance essentielle que le cours souligne aussitôt : si le "
      "développement est devenu universel, l’économie du développement reste "
      "en pratique centrée sur les pays confrontés aux blocages les plus "
      "forts."),
'ch7-qcm-39': f(niv='comprendre', sp='c7-01', b=159,
 q="Pourquoi les ODD marquent-ils l’universalisation de l’objectif de "
   "développement ?",
 opts=["Parce qu’ils sont financés par l’ensemble des pays du monde",
       "Parce qu’ils s’adressent à tous les pays, quel que soit leur niveau "
       "de revenu, et articulent croissance, justice sociale et soutenabilité",
       "Parce qu’ils imposent les mêmes politiques économiques partout",
       "Parce qu’ils ont été ratifiés sans exception par tous les États"],
 ans=1,
 why=["Le mode de financement n’est pas l’argument retenu par le cours.",
      "Les ODD fixent des objectifs, non des politiques uniformes.",
      "Le cours ne fonde pas l’universalité sur l’unanimité des "
      "ratifications."],
 exp="Adoptés en 2015 pour la période 2015-2030, les ODD font du "
     "développement un objectif qui ne se réduit plus à une logique de "
     "rattrapage économique des pays du Sud : il engage toutes les économies, "
     "y compris celles de l’OCDE."),
'ch7-vf-4': f(niv='connaitre', sp='c7-01', b=160,
 exp="C’est l’inverse : les ODD constituent un agenda universel. Ils "
     "concernent tous les pays du monde, quel que soit leur niveau de revenu, "
     "et c’est précisément ce qui distingue cette génération d’objectifs des "
     "approches antérieures, centrées sur le rattrapage des pays du Sud."),
'ch7-qcm-41': f(niv='connaitre', sp='c7-01', b=29,
 exp="C’est l’OMC qui surveille les règles du commerce mondial et au sein de "
     "laquelle les pays en développement bénéficient du traitement spécial et "
     "différencié. C’est donc à l’OMC que la Chine annonce, en septembre 2025, "
     "renoncer à ce statut.",
 why=["Le FMI intervient sur les équilibres macroéconomiques et, dans ce "
      "chapitre, sur les plans d’ajustement structurel.",
      "L’ONU adopte les ODD mais ne gère pas les règles commerciales.",
      "L’OCDE est un lieu d’expertise entre pays développés, pas une "
      "organisation du commerce mondial."]),
'ch7-qcm-40': f(niv='raisonner', sp='c7-05', b=192,
 exp="Depuis 1990, le PNUD et les institutions internationales ont multiplié "
     "les indicateurs — IDH, puis IDHI, IIG, IPM, IDHP — pour mieux saisir "
     "pauvreté, inégalités et environnement. Mais le cours souligne la tension "
     "qui en résulte : un indicateur unique est trop réducteur, une "
     "prolifération excessive devient illisible. L’enjeu est un compromis "
     "entre richesse analytique et lisibilité statistique.",
 why=["Le coût de production des statistiques n’est pas l’argument retenu.",
      "Les indicateurs ne se contredisent pas systématiquement : ils "
      "éclairent des dimensions différentes.",
      "Le cours ne met pas en cause un contrôle des indicateurs par les pays "
      "développés."],
 diss="C’est aussi pourquoi le PIB et le RNB n’ont pas disparu : simples et "
      "rapidement lisibles, ils restent insuffisants mais utiles."),
'ch7-qcm-9': f(niv='connaitre', sp='c7-17', b=191,
 exp="L’IDHP, créé en 2020, est l’Indicateur de Développement Humain ajusté "
     "aux pressions planétaires : il introduit explicitement la question "
     "écologique dans l’évaluation du développement, en intégrant l’empreinte "
     "écologique, la pression sur les ressources et les émissions liées au "
     "mode de développement.",
 why=["L’ajustement aux inégalités entre femmes et hommes est l’objet de "
      "l’IIG.",
      "La mesure en parité de pouvoir d’achat concerne déjà le RNB utilisé "
      "dans l’IDH classique.",
      "Aucun indicateur du cours ne corrige l’IDH de la corruption."]),
'ch7-vf-13': f(niv='connaitre', sp='c7-17', b=3450,
 exp="L’IDHP ajuste l’IDH aux pressions planétaires. Sa lecture est simple : "
     "si l’IDHP est proche de l’IDH, le pays exerce une faible pression "
     "écologique ; plus l’écart est grand, plus le développement humain "
     "observé repose sur un mode de croissance écologiquement coûteux."),
'ch7-qcm-10': f(niv='connaitre', sp='c7-01', b=109,
 exp="Le cours situe la Chine autour de 0,774 d’IDH : un niveau relativement "
     "élevé, proche du seuil de 0,8, mais encore en dessous des pays les plus "
     "avancés. Position intermédiaire donc : forte progression, mais pas "
     "convergence totale.",
 why=["0,540 correspondrait à un pays à développement humain faible.",
      "0,650 sous-estime nettement le niveau atteint par la Chine.",
      "0,900 est le niveau des pays à très haut développement humain, comme "
      "la Suisse, la Norvège ou l’Islande."]),
'ch7-vf-7': f(niv='connaitre', sp='c7-01', b=114,
 exp="Avec un IDH d’environ 0,774, la Chine est proche du seuil de 0,8 mais "
     "reste en dessous des pays les plus avancés. Le cours ajoute que même cet "
     "indicateur ne suffit pas : l’IPM révèle des formes de vulnérabilité qui "
     "la rapprochent, sur certains aspects, des pays en développement."),
'ch7-open-1': f(niv='comprendre', sp='c7-01', b=79,
 q="Pourquoi la croissance ne suffit-elle pas à définir le développement ?",
 ans={'modele': "La croissance mesure l’augmentation de la richesse "
      "produite : c’est un indicateur utile mais partiel. Un pays peut "
      "connaître une forte croissance sans réduction suffisante de la "
      "pauvreté, sans amélioration homogène des conditions de vie, sans "
      "baisse des inégalités ni meilleure qualité de vie pour l’ensemble de "
      "la population. La croissance ne dit rien, à elle seule, de la "
      "répartition de cette richesse ni du bien-être collectif. Le "
      "développement est au contraire une notion multidimensionnelle : une "
      "amélioration globale des conditions de vie, que l’on saisit en "
      "croisant revenu, santé et éducation.",
      'cles': [{'f': ['quantitatif', 'production', 'pib', 'richesse produite'],
                'l': 'la croissance est quantitative'},
               {'f': ['repartition', 'inegalite', 'pauvrete'],
                'l': 'elle ne dit rien de la répartition'},
               {'f': ['multidimensionnel', 'sante', 'education', 'conditions de vie'],
                'l': 'le développement est multidimensionnel'},
               {'f': ['chine', 'indicateur', 'croiser'],
                'l': 'd’où la nécessité de croiser plusieurs indicateurs'}]},
 exp="Le cas chinois est l’illustration retenue par le cours : puissance "
     "économique incontestable, mais indicateurs de développement plus "
     "nuancés, notamment l’IPM, qui révèle des privations concrètes."),

# ------------------------------------- c7-02 pauvreté mondiale et géographie
'ch7-qcm-22': f(niv='comprendre', sp='c7-02', b=287,
 q="Que révèle la recomposition géographique de la pauvreté mondiale ?",
 opts=["Que la pauvreté a globalement cessé de reculer depuis 1990",
       "Que les pays en développement ne forment pas un bloc homogène mais "
       "un ensemble aux trajectoires profondément inégales",
       "Que les écarts de revenus entre pays se sont résorbés",
       "Que la pauvreté est désormais un phénomène surtout asiatique"],
 ans=1,
 why=["L’extrême pauvreté a au contraire fortement reculé depuis les années "
      "1990.",
      "Les écarts de revenu et de développement restent très marqués : c’est "
      "le point de départ du chapitre.",
      "C’est l’inverse : la pauvreté était majoritairement asiatique dans "
      "les années 1990, elle est aujourd’hui concentrée en Afrique "
      "subsaharienne."],
 exp="Le recul spectaculaire de la pauvreté en Asie et sa concentration "
     "croissante en Afrique subsaharienne — environ les trois quarts de la "
     "pauvreté mondiale — montrent que les trajectoires de développement sont "
     "profondément inégales. La catégorie « pays en développement » conserve "
     "une utilité descriptive, mais elle recouvre des situations très "
     "contrastées.",
 diss="C’est la deuxième des trois questions transversales du chapitre : les "
      "pays en développement forment-ils un ensemble homogène ?"),
'ch7-open-11': f(niv='comprendre', sp='c7-03', b=416,
 ans={'modele': "L’éducation des filles exerce des effets cumulatifs : elle "
      "retarde l’âge de la maternité, améliore la connaissance de la "
      "contraception, réduit les grossesses précoces, abaisse la fécondité, "
      "renforce l’autonomie économique et sociale, améliore la santé "
      "maternelle, favorise une meilleure nutrition et une meilleure prise en "
      "charge des enfants, et accroît l’investissement dans le capital "
      "humain. Elle agit donc simultanément sur la santé, la démographie, la "
      "pauvreté et la transmission intergénérationnelle du développement.",
      'cles': [{'f': ['fecondite', 'maternite', 'contraception', 'naissance'],
                'l': 'elle abaisse la fécondité et retarde les maternités'},
               {'f': ['sante', 'nutrition', 'mortalite'],
                'l': 'elle améliore la santé maternelle et infantile'},
               {'f': ['autonomie', 'emancipation', 'economique'],
                'l': 'elle renforce l’autonomie des femmes'},
               {'f': ['capital humain', 'generation', 'transmission', 'enfant'],
                'l': 'elle accroît le capital humain transmis aux générations suivantes'}]},
 exp="Le cours illustre par l’Inde : dans les régions où la scolarisation des "
     "filles est plus avancée, la fécondité est plus faible. Le développement "
     "est donc inégal non seulement entre pays, mais à l’intérieur même des "
     "pays."),

# ------------------------------------------- c7-03 IDH, santé, éducation
'ch7-qcm-2': f(niv='connaitre', sp='c7-03', b=636,
 exp="L’IDH est l’Indicateur de Développement Humain, créé par le PNUD en "
     "1990. Il combine trois dimensions : le revenu, mesuré par le RNB par "
     "habitant en parité de pouvoir d’achat ; la santé, mesurée par "
     "l’espérance de vie à la naissance ; l’éducation, mesurée par deux "
     "sous-indicateurs de scolarisation.",
 why=["Aucun indicateur de « déficit humanitaire » n’existe dans le cours.",
      "Il ne s’agit pas d’un indice de dépendance.",
      "L’intitulé exact est « développement humain », au singulier, et non "
      "« développement des hommes »."]),
'ch7-qcm-3': f(niv='connaitre', sp='c7-03', b=636,
 exp="L’IDH a été créé par le PNUD, Programme des Nations Unies pour le "
     "Développement, en 1990. C’est également le PNUD qui construira ensuite "
     "l’IDHI, l’IIG, l’IPM et, en 2020, l’IDHP.",
 why=["Le FMI intervient dans ce chapitre sur les plans d’ajustement "
      "structurel.",
      "La Banque mondiale classe les pays par RNB par habitant et mesure la "
      "pauvreté absolue.",
      "L’OMC gère les règles du commerce mondial."]),
'ch7-qcm-31': f(niv='connaitre', sp='c7-03', b=639,
 exp="L’IDH combine trois dimensions : le revenu (RNB par habitant en PPA), "
     "la santé (espérance de vie à la naissance) et l’éducation (durée "
     "moyenne et durée attendue de scolarisation). Sa valeur est comprise "
     "entre 0 et 1.",
 why=["Deux dimensions seulement omettraient l’éducation, pourtant centrale.",
      "L’environnement et les libertés n’entrent pas dans l’IDH : le premier "
      "relève de l’IDHP, les secondes de l’approche théorique de Sen.",
      "Les inégalités ne sont pas intégrées à l’IDH : c’est précisément "
      "l’objet de l’IDHI."]),
'ch7-vf-1': f(niv='connaitre', sp='c7-03', b=637,
 exp="L’IDH repose au contraire sur l’idée que le développement ne se réduit "
     "pas au revenu : il combine revenu, santé et éducation. Sa création en "
     "1990 marque une rupture, en remplaçant une logique purement monétaire "
     "par une approche multidimensionnelle."),
'ch7-vf-12': f(niv='connaitre', sp='c7-03', b=636,
 exp="Le PNUD, Programme des Nations Unies pour le Développement, a créé "
     "l’IDH en 1990 et en publie le classement. Il est également à l’origine "
     "des indicateurs complémentaires : IDHI, IIG, IPM et IDHP."),
'ch7-open-2': f(niv='connaitre', sp='c7-03', b=639,
 ans={'modele': "L’IDH est un indicateur composite créé par le PNUD en 1990. "
      "Il combine trois dimensions : la santé, mesurée par l’espérance de vie "
      "à la naissance ; l’éducation, mesurée par la durée moyenne et la durée "
      "attendue de scolarisation ; le niveau de vie, mesuré par le RNB par "
      "habitant en parité de pouvoir d’achat. Sa valeur est comprise entre 0 "
      "et 1 : plus elle est proche de 1, plus le développement humain est "
      "élevé.",
      'cles': [{'f': ['pnud', '1990'], 'l': 'créé par le PNUD en 1990'},
               {'f': ['esperance de vie', 'sante'],
                'l': 'la santé, par l’espérance de vie'},
               {'f': ['scolarisation', 'education'],
                'l': 'l’éducation, par deux durées de scolarisation'},
               {'f': ['rnb', 'ppa', 'revenu', 'pouvoir d achat'],
                'l': 'le niveau de vie, par le RNB par habitant en PPA'}]},
 exp="Le cours insiste sur le choix du RNB en PPA : le taux de change de "
     "marché, influencé par la spéculation et les mouvements de capitaux, ne "
     "traduit pas ce qu’un revenu permet réellement d’acheter."),

# ------------------------------------------ c7-04 prolongements de l’IDH, Sen
'ch7-qcm-28': f(niv='comprendre', sp='c7-04', b=710,
 exp="Pour Sen, le développement n’est pas l’augmentation du revenu moyen "
     "mais l’élargissement des libertés réelles : les capabilités désignent la "
     "capacité effective des individus à choisir leur vie, à accéder "
     "concrètement aux opportunités, à transformer des ressources en libertés "
     "réelles. Deux personnes au même revenu n’ont pas les mêmes capabilités "
     "si l’une vit dans un désert médical ou subit des discriminations.",
 why=["La mesure par le seul revenu est précisément ce que Sen récuse.",
      "Les droits légaux ne suffisent pas : Sen insiste sur les libertés "
      "réelles, effectivement exerçables.",
      "La production industrielle n’entre pas dans son analyse."],
 diss="L’approche par les capabilités est la justification théorique de "
      "l’IDH : elle explique pourquoi l’indicateur retient la santé et "
      "l’éducation à côté du revenu."),
'ch7-qcm-18': f(niv='connaitre', sp='c7-04', b=870,
 exp="Pour Sen, le développement humain est l’expansion des capabilités, "
     "c’est-à-dire des libertés réelles dont disposent les individus pour "
     "mener la vie qu’ils ont des raisons de valoriser. Son ouvrage de "
     "référence est « Development as Freedom » (1999).",
 why=["La maximisation du PIB par habitant est la vision monétaire que Sen "
      "critique.",
      "L’accès aux soins est une capabilité parmi d’autres, non la "
      "définition.",
      "Réduire la mortalité infantile et l’analphabétisme sont des résultats "
      "du développement, non sa définition."]),
'ch7-vf-5': f(niv='connaitre', sp='c7-04', b=710,
 exp="Sen définit au contraire le développement comme l’expansion des "
     "capabilités, c’est-à-dire des libertés réelles des individus. Avoir un "
     "revenu ne suffit pas : encore faut-il pouvoir se soigner, aller à "
     "l’école, travailler, participer à la vie sociale et politique, vivre "
     "longtemps et dignement."),
'ch7-qcm-5': f(niv='connaitre', sp='c7-04', b=119,
 exp="L’IPM, indice de pauvreté multidimensionnelle, ne se contente pas du "
     "revenu monétaire : il mesure des privations concrètes en matière de "
     "santé, d’éducation, de niveau de vie et d’accès aux services essentiels "
     "— logement, électricité, nutrition, scolarisation. Une personne peut "
     "avoir un revenu légèrement supérieur au seuil monétaire tout en "
     "subissant de fortes privations.",
 why=["La mesure du seul revenu monétaire est précisément ce que l’IPM "
      "dépasse.",
      "Le seuil de pauvreté monétaire relève de l’approche de la Banque "
      "mondiale par la pauvreté absolue.",
      "L’IPM est construit par le PNUD, non par le FMI."],
 diss="Le cours l’applique au cas chinois : l’IPM révèle des vulnérabilités "
      "qui rapprochent la Chine des pays en développement, alors que son IDH "
      "la situe dans une position intermédiaire élevée."),
'ch7-vf-19': f(niv='connaitre', sp='c7-04', b=799,
 exp="L’IPM mesure au contraire la pauvreté comme un ensemble de privations "
     "cumulées en matière de santé, d’éducation et de conditions de vie, et "
     "non comme un simple manque de revenu. Le cours cite l’Inde : malgré une "
     "forte croissance, une partie importante de la population cumulait "
     "encore des privations de logement, d’assainissement et d’accès aux "
     "services essentiels."),
'ch7-open-15': f(niv='comprendre', sp='c7-04', b=735,
 q="Pourquoi le PNUD a-t-il créé l’IDHI, et que mesure l’écart entre IDH et "
   "IDHI ?",
 ans={'modele': "Le grand reproche adressé à l’IDH est de ne donner qu’une "
      "moyenne nationale, sans dire comment les performances sont réparties à "
      "l’intérieur du pays : un pays peut afficher un IDH élevé tout en "
      "connaissant de fortes inégalités internes. L’IDHI reprend les trois "
      "dimensions de l’IDH — revenu, santé, éducation — mais applique un malus "
      "lorsque les inégalités y sont importantes. Plus les inégalités sont "
      "fortes, plus l’écart entre IDH et IDHI est grand et plus le classement "
      "du pays recule.",
      'cles': [{'f': ['moyenne', 'repartition', 'interne'],
                'l': 'l’IDH n’est qu’une moyenne nationale'},
               {'f': ['malus', 'ajuste', 'penalis'],
                'l': 'l’IDHI applique un malus en cas d’inégalités'},
               {'f': ['ecart', 'classement', 'recul'],
                'l': 'l’écart mesure l’ampleur des inégalités internes'}]},
 exp="Le cours cite l’Afrique du Sud et le Brésil : un niveau de "
     "développement humain non négligeable, mais de fortes inégalités "
     "internes qui réduisent davantage l’indicateur ajusté."),

# ------------------------------------------------ c7-06 démographie
'ch7-qcm-33': f(niv='raisonner', sp='c7-03', b=373,
 exp="Le taux de fécondité désigne le nombre moyen d’enfants qu’une femme met "
     "au monde au cours de sa vie. Ce n’est pas un indicateur sanitaire pur, "
     "mais il renseigne indirectement sur le développement par ses liens avec "
     "la santé maternelle, la contraception, la mortalité infantile, la "
     "scolarisation des filles et l’autonomie des femmes. La fécondité baisse "
     "généralement avec le développement : environ 2,2 enfants par femme dans "
     "le monde, 1,4 dans les pays à revenu élevé.",
 why=["Le lien est inverse : une fécondité élevée accompagne plutôt les "
      "niveaux de développement les plus faibles.",
      "Le cours établit précisément des liens étroits entre les deux.",
      "Une fécondité trop faible pose aussi problème : en dessous du seuil de "
      "renouvellement, la population vieillit et se contracte."]),
'ch7-qcm-34': f(niv='connaitre', sp='c7-06', b=1149,
 exp="La transition démographique est le passage d’un régime de forte "
     "natalité et forte mortalité à un régime de faible natalité et faible "
     "mortalité. Le cours insiste sur sa chronologie : la mortalité baisse "
     "d’abord, la natalité suit avec retard, d’où une forte hausse temporaire "
     "de l’accroissement naturel et une impression d’explosion démographique.",
 why=["La hausse rapide de la population n’est qu’une phase intermédiaire de "
      "la transition, non sa définition.",
      "Le vieillissement est une conséquence du régime moderne, pas la "
      "transition elle-même.",
      "L’exode rural est un phénomène migratoire interne, distinct."],
 diss="L’auteur de référence est Adolphe Landry, « La Révolution "
      "démographique » (1934), qui insiste sur une maîtrise croissante de la "
      "fécondité dans les sociétés modernes."),
'ch7-vf-18': f(niv='connaitre', sp='c7-06', b=1149,
 exp="C’est la définition même de la transition démographique. Le cours "
     "précise la chronologie : la mortalité baisse avant la natalité, ce qui "
     "provoque temporairement une forte hausse de l’accroissement naturel."),
'ch7-qcm-36': f(niv='comprendre', sp='c7-06', b=1123,
 exp="Le dividende démographique, étudié par David Bloom et David Canning, "
     "désigne le gain potentiel de croissance lié à l’augmentation temporaire "
     "de la part de la population en âge de travailler : la fécondité baisse, "
     "la part des enfants diminue relativement, les générations nombreuses "
     "arrivent à l’âge actif.",
 why=["Il ne s’agit pas d’un revenu tiré de la natalité, mais d’un effet de "
      "structure par âge.",
      "Les transferts des migrants sont une autre notion, étrangère à ce "
      "mécanisme.",
      "Le vieillissement correspond au contraire à la troisième phase, celle "
      "du retour d’une charge."],
 diss="Le mot décisif est « conditionnel » : le dividende exige emplois, "
      "éducation, santé, infrastructures, institutions efficaces et stabilité "
      "politique. Sans cela, il se traduit en chômage massif, informalité et "
      "tensions sociales."),
'ch7-vf-14': f(niv='comprendre', sp='c7-06', b=1119,
 exp="C’est l’inverse : le dividende démographique est la phase favorable, "
     "celle où la part des actifs augmente et celle des dépendants diminue "
     "relativement. Le vieillissement correspond à la troisième phase de la "
     "séquence, celle du retour d’une charge — retraites, santé, dépendance."),

# ---------------------------------------- c7-07 / c7-08 dette et ajustement
'ch7-qcm-35': f(niv='connaitre', sp='c7-07', b=1374,
 q="Qu’appelle-t-on le service de la dette, et quand une dette est-elle dite "
   "soutenable ?",
 opts=["Le seul paiement des intérêts ; elle est soutenable si les intérêts "
       "sont inférieurs à la croissance",
       "Le remboursement du capital et le paiement des intérêts ; elle est "
       "soutenable si revenus, exportations, recettes publiques et croissance "
       "permettent de l’assurer sans asphyxier l’économie",
       "Le montant total de la dette rapporté au PIB ; elle est soutenable "
       "en dessous de 60 %",
       "Les commissions versées aux banques créancières ; elle est soutenable "
       "si elles restent faibles"],
 ans=1,
 why=["Le service de la dette ne se limite pas aux intérêts : il inclut le "
      "remboursement du capital.",
      "Le ratio dette / PIB est un indicateur d’encours, non le service de la "
      "dette, et le cours ne retient pas ce seuil ici.",
      "Les commissions bancaires n’entrent pas dans cette définition."],
 exp="Ce n’est pas l’existence de la dette qui pose problème, mais son "
     "caractère excessif ou insoutenable. Le cours ajoute un repère pour les "
     "pays en développement : il est préférable que le service de la dette "
     "publique extérieure ne représente pas plus de 15 % des exportations.",
 diss="Cette définition commande toute la partie : l’endettement est un mode "
      "normal de financement du développement, qui ne devient un obstacle "
      "qu’une fois la soutenabilité perdue."),
'ch7-open-12': f(niv='comprendre', sp='c7-07', b=1386,
 ans={'modele': "Lorsque la dette devient trop importante, les intérêts "
      "augmentent, le service de la dette absorbe une part croissante des "
      "ressources, et le pays emprunte à nouveau pour rembourser ses dettes "
      "passées : la spirale s’auto-entretient. L’État ne s’endette plus pour "
      "investir mais pour payer, si bien qu’il ne peut plus financer "
      "l’éducation, la santé ou les infrastructures. S’y ajoute une "
      "dépendance accrue vis-à-vis des banques internationales, des marchés, "
      "des institutions et des États créanciers, qui se traduit par des "
      "conditionnalités et une perte d’autonomie dans la conduite des "
      "politiques économiques.",
      'cles': [{'f': ['service', 'interet', 'absorbe', 'rembours'],
                'l': 'le service de la dette absorbe les ressources'},
               {'f': ['spirale', 'nouveaux emprunts', 'auto entretenue', 'cercle'],
                'l': 'une spirale auto-entretenue'},
               {'f': ['sante', 'education', 'investissement', 'public'],
                'l': 'les dépenses essentielles ne sont plus financées'},
               {'f': ['dependance', 'creancier', 'conditionnalite', 'autonomie'],
                'l': 'et une dépendance aux créanciers'}]},
 exp="Le cours ajoute une critique empirique : au lieu de financer des "
     "investissements productifs, une partie des emprunts a servi à des "
     "dépenses improductives — dépenses militaires, détournements au profit "
     "d’élites politiques, consommations dispendieuses, placements "
     "spéculatifs dans les pays développés."),
'ch7-qcm-15': f(niv='connaitre', sp='c7-08', b=1502,
 exp="Le Consensus de Washington, expression de John Williamson (1989), "
     "désigne un ensemble de politiques d’inspiration néolibérale et "
     "monétariste : stabiliser la monnaie, réduire les déficits, libéraliser "
     "les marchés, ouvrir les économies, privatiser, déréglementer. La "
     "trilogie à retenir est : déréglementation, libéralisation, "
     "privatisation.",
 why=["Interventionnisme, protectionnisme et redistribution sont exactement "
      "l’inverse de ce programme.",
      "La planification et l’ISI relèvent des stratégies autocentrées, "
      "antérieures et opposées.",
      "Nationalisations et contrôle des changes sont contraires à cette "
      "logique."],
 diss="Les PAS sont les programmes concrets par lesquels le FMI et la Banque "
      "mondiale ont appliqué ce consensus, en échange d’une aide financière "
      "ou d’un rééchelonnement."),
'ch7-vf-9': f(niv='connaitre', sp='c7-08', b=1502,
 exp="Le Consensus de Washington préconise l’inverse : libéralisation, "
     "privatisations, austérité budgétaire, déréglementation et ouverture aux "
     "capitaux étrangers. Le cours relève que ces mesures ont souvent "
     "restauré des équilibres financiers de court terme au prix d’un coût "
     "social élevé."),

# --------------------------------- c7-11 / c7-12 théories du sous-développement
'ch7-qcm-25': f(niv='comprendre', sp='c7-11', b=2051,
 q="Qu’appelle-t-on, chez Ragnar Nurkse, le cercle vicieux de la pauvreté ?",
 opts=["Une politique fiscale qui maintient les ménages dans la pauvreté",
       "Un enchaînement où la faiblesse des revenus empêche l’épargne, donc "
       "l’investissement, donc les gains de productivité, ce qui reproduit la "
       "faiblesse des revenus",
       "Un indicateur international de mesure de la pauvreté",
       "Une aide conditionnelle accordée aux pays en développement"],
 ans=1,
 why=["La fiscalité n’est pas en cause dans ce mécanisme.",
      "Il ne s’agit pas d’un indicateur mais d’un mécanisme économique.",
      "La conditionnalité de l’aide relève des PAS, bien plus tard dans le "
      "chapitre."],
 exp="L’enchaînement est : faibles revenus → faible épargne → faible "
     "investissement → faible productivité → faibles revenus à nouveau. La "
     "pauvreté n’est donc pas seulement une conséquence du "
     "sous-développement : elle en est aussi une cause structurelle.",
 diss="L’opposition avec Lewis est très rentable : pour Lewis le dualisme "
      "peut être temporaire, pour Nurkse il devient durable parce qu’il "
      "entretient un cercle vicieux."),
'ch7-qcm-11': f(niv='comprendre', sp='c7-11', b=1996,
 q="Qu’appelle-t-on, chez Arthur Lewis, le dualisme économique ?",
 opts=["La coexistence de deux monnaies dans une même économie",
       "La coexistence d’un secteur traditionnel, surtout agricole et peu "
       "productif, et d’un secteur moderne, urbain et capitaliste, plus "
       "productif mais encore limité",
       "La dépendance économique vis-à-vis de deux puissances étrangères",
       "Le partage des exportations entre deux produits principaux"],
 ans=1,
 why=["Le dualisme n’est pas monétaire.",
      "La dépendance externe est l’objet de l’analyse de Prebisch et des "
      "dépendantistes.",
      "La concentration des exportations est un autre problème, lié à la "
      "spécialisation primaire."],
 exp="Le problème central est que le secteur moderne est trop petit pour "
     "absorber immédiatement toute la main-d’œuvre excédentaire du secteur "
     "traditionnel. Une grande partie de la population reste donc dans des "
     "activités peu productives : la productivité moyenne reste faible, la "
     "demande intérieure étroite, l’investissement limité.",
 diss="Point souvent oublié : ce surplus de main-d’œuvre exerce une pression "
      "à la baisse sur les salaires du secteur moderne, ce qui contient les "
      "coûts de production et favorise la compétitivité des exportations."),
'ch7-qcm-13': f(niv='comprendre', sp='c7-12', b=2184,
 q="Qu’appelle-t-on, chez Raul Prebisch, la détérioration des termes de "
   "l’échange ?",
 opts=["Les pays en développement doivent s’ouvrir au libre-échange pour se "
       "développer",
       "Les prix des produits primaires exportés progressent moins vite que "
       "ceux des produits manufacturés importés : il faut exporter toujours "
       "plus pour importer autant",
       "Les pays développés dépendent des matières premières des pays pauvres",
       "La dépendance technologique est le principal obstacle au "
       "développement"],
 ans=1,
 why=["C’est la thèse libérale, que Prebisch conteste précisément.",
      "Le sens de la dépendance est inverse dans son analyse : c’est la "
      "périphérie qui dépend du centre.",
      "La dépendance technologique est une limite des stratégies "
      "d’industrialisation, non la thèse de Prebisch."],
 exp="Prebisch, premier secrétaire exécutif de la CEPAL créée en 1948, décrit "
     "une économie mondiale organisée entre un centre industrialisé et "
     "dominant et une périphérie spécialisée dans les produits primaires. Le "
     "cours illustre par le tracteur et le café : il faut fournir toujours "
     "plus de café pour acheter le même bien industriel. La contrainte "
     "extérieure se renforce et le pays peine à financer son "
     "industrialisation.",
 diss="Conséquence politique : Prebisch justifie une industrialisation "
      "protégée, une réduction de la spécialisation primaire et des politiques "
      "de substitution aux importations."),
'ch7-vf-11': f(niv='comprendre', sp='c7-12', b=2194,
 q="L’analyse de Prebisch conduit à défendre le libre-échange comme stratégie "
   "de développement.",
 ans=False,
 exp="C’est l’inverse : puisque la division internationale du travail enferme "
     "la périphérie dans une spécialisation primaire défavorable, Prebisch "
     "justifie une industrialisation protégée, une réduction de la dépendance "
     "extérieure, des politiques de substitution aux importations et parfois "
     "une logique de développement autocentré. Le cours relève la limite : "
     "tous les pays n’ont pas la taille ni le marché intérieur nécessaires à "
     "une stratégie purement autocentrée."),
'ch7-qcm-32': f(niv='comprendre', sp='c7-11', b=1990,
 q="Comment François Perroux explique-t-il le sous-développement ?",
 opts=["Par un simple retard chronologique dans le processus de développement",
       "Par la combinaison d’une concurrence imparfaite, de rapports de force "
       "défavorables dans les échanges et d’économies désarticulées",
       "Par un manque de ressources naturelles",
       "Par l’insuffisance de l’aide internationale"],
 ans=1,
 why=["Le retard chronologique est la lecture libérale, celle de Rostow.",
      "Les dotations en ressources naturelles ne sont pas son critère.",
      "L’aide internationale n’intervient pas dans son analyse."],
 exp="Pour Perroux, les pays les moins développés ne sont pas en situation de "
     "concurrence « normale » : les échanges sont marqués par des rapports de "
     "force qui défavorisent les économies les plus faibles. Les gains de "
     "l’échange y sont inégalement répartis, les secteurs modernes restent "
     "trop faibles, la croissance ne devient pas auto-entretenue et "
     "l’économie reste fragmentée. Le marché mondial n’est donc pas neutre.",
 diss="Perroux fait le pont entre l’analyse structuraliste des blocages "
      "internes et l’analyse dépendantiste des rapports de domination."),
'ch7-vf-3': f(niv='connaitre', sp='c7-11', b=2084,
 exp="Le protectionnisme éducateur est au contraire une protection "
     "temporaire : il vise à permettre aux industries naissantes de se "
     "consolider, de gagner en productivité et d’atteindre une taille "
     "critique avant d’affronter la concurrence internationale. C’est l’une "
     "des mesures typiques que les structuralistes assignent à l’État, avec "
     "la politique industrielle et la planification."),
'ch7-qcm-37': f(niv='comprendre', sp='c7-11', b=1948,
 q="Pourquoi les structuralistes estiment-ils que le marché ne suffit pas au "
   "développement ?",
 opts=["Parce que les institutions n’ont aucun effet sur la croissance",
       "Parce que le sous-développement résulte de blocages structurels — "
       "dualisme, désarticulation productive, insuffisance institutionnelle — "
       "que le marché ne corrige pas spontanément",
       "Parce que seules les institutions financières importent",
       "Parce que l’ouverture commerciale est toujours néfaste"],
 ans=1,
 why=["C’est l’inverse de leur position : les institutions sont au cœur de "
      "leur analyse.",
      "Les structuralistes ne réduisent pas les institutions à la sphère "
      "financière.",
      "Ils ne condamnent pas l’ouverture en elle-même : ils refusent qu’elle "
      "suffise."],
 exp="Puisque le sous-développement résulte de structures déséquilibrées, "
     "l’État doit protéger temporairement certains secteurs, orienter "
     "l’investissement, soutenir l’industrialisation, développer les "
     "infrastructures et transformer les structures productives. Le cours "
     "ajoute aussitôt la limite : l’État peut aussi être défaillant — mauvaise "
     "allocation, corruption, inefficacité bureaucratique, protection "
     "excessive de secteurs non compétitifs, rentes.",
 diss="Cette symétrie — défaillances du marché, défaillances de l’État — est "
      "la bonne manière de conclure un sujet sur le rôle de l’État dans le "
      "développement."),

# ------------------------------------------- c7-13 / c7-14 stratégies
'ch7-qcm-20': f(niv='connaitre', sp='c7-13', b=2550,
 exp="L’industrialisation par substitution aux importations consiste à "
     "produire sur place ce que le pays importait, derrière des barrières "
     "douanières. Elle relève d’une logique de développement autocentré avec "
     "priorité à l’industrie légère, puis remontée de filière : biens de "
     "consommation simples, puis biens intermédiaires, puis éventuellement "
     "biens d’équipement.",
 why=["L’exportation de produits industriels est la stratégie opposée, celle "
      "de la promotion des exportations.",
      "Il ne s’agit pas d’un indice statistique mais d’une stratégie.",
      "L’attractivité pour les investissements étrangers caractérise plutôt "
      "les stratégies extraverties."],
 diss="Objectifs à citer : réduire la dépendance extérieure, diminuer le "
      "déficit commercial, économiser des devises, réduire le chômage et "
      "protéger les industries naissantes."),
'ch7-open-8': f(niv='comprendre', sp='c7-13', b=2550,
 ans={'modele': "L’ISI est une stratégie de développement autocentré donnant "
      "la priorité à l’industrie légère : il s’agit de produire nationalement "
      "les biens auparavant importés, derrière des barrières douanières, "
      "selon une logique de protectionnisme éducateur. Le pays procède par "
      "remontée de filière : d’abord les biens de consommation simples, puis "
      "les biens intermédiaires, puis éventuellement les biens d’équipement. "
      "Les objectifs sont de réduire la dépendance extérieure, d’économiser "
      "des devises, de diminuer le déficit commercial et le chômage, et de "
      "protéger les industries naissantes. L’Amérique latine des années 1930 "
      "aux années 1960 en est l’exemple classique.",
      'cles': [{'f': ['produire', 'importait', 'remplace', 'national'],
                'l': 'produire nationalement ce qui était importé'},
               {'f': ['douanier', 'protection', 'barriere', 'educateur'],
                'l': 'derrière des barrières douanières'},
               {'f': ['remontee de filiere', 'legere', 'intermediaire', 'equipement'],
                'l': 'par remontée de filière, de l’industrie légère vers l’amont'},
               {'f': ['dependance', 'devise', 'deficit', 'autocentre'],
                'l': 'pour réduire la dépendance extérieure'}]},
 exp="Limites à connaître : un marché intérieur souvent trop étroit pour "
     "réaliser des économies d’échelle, une dépendance persistante aux biens "
     "d’équipement importés — d’où l’expression de substitution partielle — et "
     "un risque de négligence du secteur agricole."),
'ch7-open-9': f(niv='comprendre', sp='c7-13', b=2576,
 ans={'modele': "L’industrialisation par promotion des exportations relève "
      "d’une logique de développement extraverti, avec priorité à l’industrie "
      "légère exportatrice : le développement passe par la production de "
      "biens manufacturés destinés aux marchés étrangers, en exploitant les "
      "avantages comparatifs. Le pays s’appuie sur une main-d’œuvre abondante "
      "et des salaires faibles, donc une forte compétitivité-prix, ainsi que "
      "sur l’implantation de firmes multinationales attirées par les aides "
      "publiques. Il remonte ensuite les filières, des biens de consommation "
      "vers les biens intermédiaires puis les biens d’équipement. Les "
      "exemples cités sont le Brésil des années 1950, la Corée du Sud à "
      "partir de 1961 et les NPI asiatiques.",
      'cles': [{'f': ['export', 'etranger', 'mondial', 'extraverti'],
                'l': 'produire pour les marchés extérieurs'},
               {'f': ['avantage comparatif', 'main d oeuvre', 'salaire', 'competitivite prix'],
                'l': 'en exploitant les avantages comparatifs'},
               {'f': ['remontee', 'gamme', 'filiere'],
                'l': 'avec remontée de filière et montée en gamme'},
               {'f': ['coree', 'npi', 'bresil', 'asie'],
                'l': 'exemples : Corée du Sud, NPI asiatiques'}]},
 exp="Limites : une forte dépendance à la demande mondiale et à la "
     "conjoncture internationale, des coûts sociaux importants — faibles "
     "rémunérations, faibles protections — et une spécialisation contrainte "
     "par ce que demande le marché mondial plutôt que par les besoins de la "
     "population."),
'ch7-aut195-5': f(niv='connaitre', sp='c7-14', b=2753,
 exp="Kaname Akamatsu (1896-1974) formule le modèle du vol d’oies sauvages "
     "dès 1937 : un pays importe d’abord un produit, puis le produit sur son "
     "territoire, puis l’exporte quand il devient compétitif, avant "
     "d’abandonner les productions les plus simples à des pays suiveurs. "
     "Saburo Okita le popularise internationalement dans les années 1980.",
 why=["Okita popularise le modèle mais ne le formule pas.",
      "Gerschenkron analyse les trajectoires d’industrialisation tardive, "
      "mais ne propose pas ce modèle séquencé.",
      "Rostow propose une succession d’étapes universelles, non une division "
      "régionale du travail."]),
'ch7-aut195-4': f(niv='comprendre', sp='c7-14', b=2962,
 exp="Chez Raymond Vernon, un produit passe par l’innovation, la maturité "
     "puis la standardisation. À mesure que le produit se standardise, la "
     "production peut se déplacer vers des pays à coûts plus faibles, "
     "souvent via filiales ou délocalisations. Le parallèle avec le vol d’oies "
     "sauvages est direct : le pays leader innove, puis les productions mûres "
     "migrent vers des pays plus tardifs.",
 why=["Croissance, maturité et déclin décrivent un cycle de vie commercial, "
      "non les phases retenues par Vernon dans le cours.",
      "Importation, production et exportation sont les trois étapes du modèle "
      "d’Akamatsu.",
      "Expansion, crise et dépression décrivent un cycle économique, sans "
      "rapport avec le cycle du produit."],
 diss="Le modèle du vol d’oies sauvages est ainsi présenté comme compatible "
      "à la fois avec HOS — les dotations factorielles commandent la "
      "spécialisation — et avec Vernon, qui en donne la version dynamique."),

# --------------------------------------------- c7-17 soutenabilité, climat
'ch7-qcm-21': f(niv='connaitre', sp='c7-17', b=3527,
 exp="Le rapport Brundtland de 1987 formalise la notion de développement "
     "durable : un développement qui répond aux besoins du présent sans "
     "compromettre la capacité des générations futures à répondre aux leurs. "
     "Il repose sur trois piliers — économique, social, environnemental — et "
     "ne condamne pas la croissance : il la redéfinit comme devant être "
     "compatible avec la protection de l’environnement et la justice sociale.",
 why=["L’IDH est créé par le PNUD en 1990.",
      "Le Consensus de Washington est l’expression de Williamson, en 1989.",
      "Les ODD sont adoptés par l’ONU en 2015."]),
'ch7-open-3': f(niv='connaitre', sp='c7-17', b=3524,
 ans={'modele': "Le développement durable, défini par le rapport Brundtland "
      "en 1987, est un développement qui répond aux besoins du présent sans "
      "compromettre la capacité des générations futures à répondre aux leurs. "
      "Il repose sur trois piliers : économique, social et environnemental. "
      "Le cours insiste sur un point : il ne s’agit pas de décroissance au "
      "sens strict, car la croissance n’est pas rejetée ; elle doit être "
      "rendue compatible avec la protection de l’environnement et la justice "
      "sociale.",
      'cles': [{'f': ['besoins du present', 'generations futures', 'brundtland'],
                'l': 'répondre aux besoins du présent sans compromettre les générations futures'},
               {'f': ['1987'], 'l': 'rapport Brundtland, 1987'},
               {'f': ['pilier', 'economique', 'social', 'environnemental'],
                'l': 'trois piliers : économique, social, environnemental'},
               {'f': ['decroissance', 'compatible', 'rejette pas'],
                'l': 'ce n’est pas la décroissance'}]},
 exp="Le rapport s’inscrit dans une chronologie : Hardin et la tragédie des "
     "communs en 1968, le rapport Meadows du Club de Rome en 1972, Brundtland "
     "en 1987, la création du GIEC en 1988."),
'ch7-aut195-1': f(niv='connaitre', sp='c7-17', b=3505,
 exp="En 1972, le Club de Rome publie le rapport Meadows, « The Limits to "
     "Growth », traduit en français par « Halte à la croissance ? ». Il alerte "
     "sur l’épuisement des ressources, les limites physiques de la planète et "
     "les risques d’une croissance indéfinie. Souvent qualifié de malthusien, "
     "il est critiqué pour raisonner avec une technologie relativement rigide, "
     "donc pour sous-estimer les capacités d’innovation et d’adaptation.",
 why=["Le rapport Brundtland date de 1987 et porte sur le développement "
      "durable.",
      "Le rapport Stern n’est pas mobilisé par le cours.",
      "Le GIEC est créé en 1988 et publie ses propres rapports de synthèse."]),
'ch7-aut195-2': f(niv='comprendre', sp='c7-17', b=3562,
 exp="L’identité de Kaya décompose les émissions de CO₂ en quatre facteurs : "
     "l’intensité carbone de l’énergie, l’intensité énergétique de la "
     "production, le PIB par habitant et la population. Son intérêt est de "
     "montrer que les progrès réalisés sur les deux premiers facteurs peuvent "
     "être annulés par la hausse des deux autres : on produit plus "
     "efficacement, avec des énergies un peu moins carbonées, mais on produit "
     "et on consomme beaucoup plus.",
 why=["Le PIB est l’un des facteurs de la décomposition, non ce qui est "
      "décomposé.",
      "La PGF relève de la comptabilité de la croissance, étudiée au "
      "chapitre 6.",
      "L’empreinte écologique est un autre indicateur, exprimé en hectares "
      "par habitant."],
 diss="C’est l’outil qui explique le paradoxe central du chapitre : des "
      "progrès techniques réels, et des émissions qui continuent pourtant "
      "d’augmenter."),
'ch7-aut195-3': f(niv='connaitre', sp='c7-17', b=3591,
 exp="En 2015, Mark Carney, alors gouverneur de la Banque d’Angleterre, "
     "formule la « tragédie des horizons » : le climat impose des "
     "investissements de long terme, avec des coûts immédiats et des bénéfices "
     "futurs, tandis que les acteurs économiques raisonnent à court terme, "
     "selon la rentabilité immédiate ou le calendrier politique. Il identifie "
     "trois risques : physiques, de responsabilité et de transition.",
 why=["L’épuisement des ressources est l’objet du rapport Meadows.",
      "La surexploitation des biens communs est la tragédie des communs de "
      "Hardin, en 1968.",
      "L’effet rebond est une autre notion, relative à l’efficacité "
      "énergétique."],
 diss="Avec Carney, le climat devient un enjeu de stabilité financière : "
      "c’est l’argument à mobiliser pour relier environnement et finance."),
'ch7-open-10': f(niv='comprendre', sp='c7-17', b=3439,
 q="Que mesure l’empreinte écologique, et que révèle sa comparaison avec la "
   "biocapacité ?",
 ans={'modele': "L’empreinte écologique mesure l’impact des activités "
      "humaines sur la planète, en hectares par habitant : c’est la surface "
      "théorique de sol productif nécessaire à une population pour subvenir à "
      "sa consommation et à ses besoins d’absorption des déchets. Elle "
      "représente la « demande ». La biocapacité de la planète représente "
      "l’« offre ». Or l’empreinte est aujourd’hui d’environ 2,5 hectares par "
      "personne, contre 0,6 en 1960, alors que la biocapacité n’est que de "
      "1,6 hectare par personne : la demande excède durablement l’offre.",
      'cles': [{'f': ['hectare', 'surface', 'sol productif'],
                'l': 'une surface théorique, en hectares par habitant'},
               {'f': ['consommation', 'dechet', 'absorption'],
                'l': 'pour la consommation et l’absorption des déchets'},
               {'f': ['biocapacite', 'offre', 'demande'],
                'l': 'comparée à la biocapacité, l’« offre » de la planète'},
               {'f': ['2,5', '1,6', 'depasse', 'excede'],
                'l': '2,5 ha contre 1,6 ha : un dépassement'}]},
 exp="Le cours relie ce dépassement à l’anthropocène : une ère où "
     "l’influence humaine sur la biosphère devient une force géologique "
     "majeure, provoquant trois crises — changement climatique, perte de "
     "biodiversité, dégradation des écosystèmes."),

# --------------------------------------- c7-18 économie de rente, gouvernance
'ch7-qcm-12': f(niv='connaitre', sp='c7-01', b=228,
 q="Comment la Banque mondiale classe-t-elle les pays, et à partir de quel "
   "indicateur ?",
 opts=["En trois groupes, à partir du PIB par habitant",
       "En quatre groupes — faible revenu, revenu intermédiaire inférieur, "
       "revenu intermédiaire supérieur, revenu élevé — à partir du RNB par "
       "habitant",
       "En deux groupes, pays développés et pays en développement, à partir "
       "de l’IDH",
       "En cinq groupes, à partir de l’indice de pauvreté multidimensionnelle"],
 ans=1,
 why=["Le classement comporte quatre groupes, et il repose sur le RNB, non "
      "sur le seul PIB.",
      "La Banque mondiale ne classe pas les pays par IDH : c’est le PNUD qui "
      "publie cet indicateur.",
      "L’IPM n’est pas un instrument de classement de la Banque mondiale."],
 exp="Le RNB est préféré au PIB parce qu’il mesure la richesse revenant aux "
     "résidents et non la richesse produite sur le territoire : RNB = PIB + "
     "revenus nets reçus du reste du monde. Ce classement a une portée "
     "pratique : les financements de la Banque mondiale visent surtout les "
     "pays à faible revenu et à revenu intermédiaire.",
 diss="À nuancer immédiatement : un revenu moyen élevé peut masquer de fortes "
      "inégalités, des poches de pauvreté et des privations importantes."),
'ch7-qcm-23': f(niv='comprendre', sp='c7-01', b=170,
 q="Sur quelles catégories de pays l’économie du développement reste-t-elle "
   "centrée en pratique ?",
 opts=["Sur les seuls pays les moins avancés",
       "Sur les pays à faible revenu, à revenu intermédiaire, les pays les "
       "moins avancés et les économies émergentes",
       "Sur l’ensemble des pays du monde, de manière indifférenciée",
       "Sur les pays de l’OCDE, qui concentrent les enjeux de développement "
       "durable"],
 ans=1,
 why=["Les PMA ne sont qu’une des catégories visées.",
      "C’est précisément la tension relevée par le cours : le développement "
      "est devenu un objectif universel, mais le champ d’étude reste "
      "sélectif.",
      "Une grande partie des pays de l’OCDE est au contraire laissée de côté "
      "par ce champ d’analyse."],
 exp="Le cours souligne ce décalage : en théorie, si le développement "
     "concerne toutes les économies, une « économie du développement » "
     "devrait s’appliquer au monde entier. En pratique, académique comme "
     "institutionnelle, elle se concentre sur les pays confrontés aux "
     "blocages les plus forts, alors même que les pays développés sont eux "
     "aussi concernés par les enjeux de soutenabilité."),
'ch7-qcm-14': f(niv='comprendre', sp='c7-18', b=4038,
 q="Qu’appelle-t-on une économie de rente, et à quel risque le cours la "
   "relie-t-il ?",
 opts=["Une économie vivant de revenus financiers ; elle risque l’inflation",
       "Une économie vivant des revenus tirés d’une ressource naturelle ou "
       "d’un atout géographique sans que l’activité productive soit un facteur "
       "de croissance ; elle risque la « maladie hollandaise »",
       "Une économie dont les revenus proviennent surtout de l’aide "
       "internationale ; elle risque la dépendance",
       "Une économie dominée par les rentes de monopole ; elle risque le "
       "sous-investissement"],
 ans=1,
 why=["Les revenus financiers ne sont pas la rente visée ici.",
      "L’aide internationale n’est pas le fondement de cette notion.",
      "Les rentes de monopole relèvent de l’analyse microéconomique de la "
      "concurrence."],
 exp="Le cours illustre par la maladie hollandaise : dans les années 1960, "
     "les Pays-Bas découvrent un important gisement de gaz naturel ; son "
     "exploitation se fait au détriment des autres secteurs industriels, et "
     "vingt ans plus tard l’économie néerlandaise rencontre de fortes "
     "difficultés — chômage élevé, insuffisance de l’investissement.",
 diss="Argument décisif pour montrer qu’une dotation en ressources naturelles "
      "n’est pas en soi un avantage de développement."),
'ch7-vf-6': f(niv='comprendre', sp='c7-18', b=4038,
 q="Selon le cours, l’abondance en ressources naturelles garantit un "
   "développement plus rapide.",
 ans=False,
 exp="Le cours décrit au contraire le risque d’économie de rente : une "
     "économie qui vit des revenus tirés d’une ressource naturelle, mais dont "
     "l’activité productive n’est pas un facteur de croissance. Le cas "
     "néerlandais des années 1960 — la « maladie hollandaise » — montre que "
     "l’exploitation d’un gisement peut se faire au détriment des autres "
     "secteurs industriels et fragiliser durablement l’économie."),
'ch7-open-14': f(niv='comprendre', sp='c7-18', b=4038,
 q="Expliquez le mécanisme de la « maladie hollandaise ».",
 ans={'modele': "Une économie de rente vit des revenus tirés de la "
      "valorisation d’une ressource naturelle ou d’un atout géographique, "
      "alors que son activité productive n’est pas, elle, un facteur de "
      "croissance. Le cas néerlandais en est l’illustration : dans les années "
      "1960, les Pays-Bas découvrent un important gisement de gaz naturel ; "
      "son exploitation se fait au détriment des autres secteurs industriels, "
      "si bien que vingt ans plus tard l’économie connaît un fort taux de "
      "chômage et une insuffisance de l’investissement. La rente détourne "
      "donc les ressources de l’appareil productif au lieu de le renforcer.",
      'cles': [{'f': ['rente', 'ressource naturelle', 'gaz', 'gisement'],
                'l': 'des revenus tirés d’une ressource naturelle'},
               {'f': ['detriment', 'autres secteurs', 'industriel', 'desindustrialis'],
                'l': 'au détriment des autres secteurs industriels'},
               {'f': ['chomage', 'investissement', 'difficulte', 'vingt ans'],
                'l': 'd’où des difficultés durables : chômage, sous-investissement'}]},
 exp="L’intérêt de ce cas est de montrer qu’une bonne nouvelle "
     "— la découverte d’une ressource — peut dégrader la structure productive "
     "si rien n’est fait pour diversifier l’économie."),
}


# =============================================================== questions neuves
NEW = [

# ------------------------------- c7-02 pauvreté absolue et géographie
f(id='q7-n01', sp='c7-02', niv='comprendre', type='qcm', b=246,
  q="En quoi la mesure de la pauvreté mondiale diffère-t-elle de celle "
    "pratiquée dans les pays développés ?",
  opts=["Elle repose sur la pauvreté relative, définie en pourcentage du "
        "revenu médian",
        "Elle repose sur la pauvreté absolue : un seuil minimal de revenu ou "
        "de consommation, sous lequel on dénombre la population",
        "Elle ne mesure que les privations non monétaires",
        "Elle est identique, seuls les montants diffèrent"],
  ans=1,
  why=["La pauvreté relative est justement la définition retenue dans de "
       "nombreux pays riches, par exemple à partir d’un pourcentage du revenu "
       "médian.",
       "Les privations non monétaires sont l’objet de l’IPM, un autre "
       "indicateur.",
       "Les deux approches sont conceptuellement différentes, et non "
       "seulement calibrées différemment."],
  exp="La Banque mondiale fixe un seuil absolu — le plus bas évoqué par le "
      "cours est de l’ordre de 3 dollars par jour — puis estime combien de "
      "personnes vivent en dessous. Ces seuils sont corrigés pour tenir "
      "compte des écarts de prix entre pays, car un même montant monétaire "
      "n’achète pas la même quantité de biens partout.",
  diss="Préciser l’approche retenue évite un contresens fréquent : la "
       "pauvreté peut reculer en termes absolus tout en progressant en termes "
       "relatifs."),

f(id='q7-n02', sp='c7-02', niv='connaitre', type='qcm', b=253,
  q="Quel ordre de grandeur le cours retient-il pour le recul de l’extrême "
    "pauvreté depuis les années 1990 ?",
  opts=["De 2,4 milliards de personnes à environ 880-900 millions",
        "De 1,2 milliard à environ 500 millions",
        "De 3 milliards à environ 2 milliards",
        "De 900 millions à environ 300 millions"],
  ans=0,
  why=["Ces ordres de grandeur ne correspondent pas aux repères du cours.",
       "Le recul est bien plus marqué que cela.",
       "Le point de départ est très sous-estimé."],
  exp="Le nombre de personnes vivant sous les seuils les plus bas de pauvreté "
      "est passé d’environ 2,4 milliards dans les années 1990 à 880-900 "
      "millions. Le cours qualifie ce recul de progrès historique majeur, "
      "tout en soulignant qu’il ne doit pas masquer une transformation "
      "essentielle : la géographie de la pauvreté a profondément changé."),

f(id='q7-n03', sp='c7-02', niv='comprendre', type='qcm', b=263,
  q="Comment la géographie de la pauvreté mondiale s’est-elle recomposée ?",
  opts=["D’une pauvreté majoritairement africaine à une pauvreté asiatique",
        "D’une pauvreté majoritairement asiatique à une concentration "
        "croissante en Afrique subsaharienne",
        "D’une pauvreté rurale à une pauvreté exclusivement urbaine",
        "Elle n’a pas changé depuis les années 1990"],
  ans=1,
  why=["Le mouvement est exactement inverse.",
       "Le cours ne raisonne pas sur l’opposition rural / urbain à cet "
       "endroit.",
       "La recomposition est au contraire l’un des constats majeurs du "
       "chapitre."],
  exp="Dans les années 1990, la pauvreté mondiale concernait très fortement "
      "l’Asie de l’Est et l’Asie du Sud. Aujourd’hui, l’Afrique subsaharienne "
      "regrouperait environ les trois quarts de la pauvreté mondiale : elle "
      "est devenue le principal foyer mondial de pauvreté monétaire.",
  diss="Ce déplacement est l’argument le plus fort contre l’idée d’un bloc "
       "homogène des pays en développement : certains ont réussi un "
       "rattrapage massif, d’autres non."),

f(id='q7-n04', sp='c7-02', niv='connaitre', type='qcm', b=305,
  q="Que sont les DTS, et pourquoi le cours les mentionne-t-il ?",
  opts=["Les droits de tirage spéciaux : une unité de compte internationale, "
        "rappelant que les comparaisons ne peuvent pas se faire à partir d’une "
        "simple lecture nominale des monnaies nationales",
        "Les dépenses de transfert social, qui mesurent la redistribution",
        "Un indicateur de dette à taux variable",
        "Une catégorie de prêts de la Banque mondiale"],
  ans=0,
  why=["Aucune notion de ce nom n’apparaît dans le cours.",
       "Les DTS ne mesurent pas la dette mais servent d’unité de compte.",
       "Ce ne sont pas des prêts mais une unité de comptabilisation."],
  exp="Les droits de tirage spéciaux sont une unité de compte internationale, "
      "mobilisée comme référence dans certains mécanismes de financement, "
      "comme support de règlement entre pays et comme instrument de "
      "comptabilisation multilatérale. Leur mention souligne que les seuils de "
      "pauvreté internationale doivent être ajustés aux écarts de prix."),

f(id='q7-n05', sp='c7-03', niv='appliquer', type='qcm', b=318,
  q="L’espérance de vie est d’environ 55 ans au Tchad et dépasse 85 ans à "
    "Hong Kong. Quel enseignement le cours en tire-t-il ?",
  opts=["Que les données sanitaires sont peu fiables dans les pays pauvres",
        "Qu’un écart de plus de trente ans au sein du même monde contemporain "
        "montre que le revenu ne suffit pas à résumer le développement",
        "Que l’espérance de vie dépend uniquement du climat",
        "Que les pays riches consacrent trop de ressources à la santé"],
  ans=1,
  why=["Le cours ne met pas en cause la fiabilité des données.",
       "Aucune explication climatique n’est avancée.",
       "Le cours relève au contraire l’insuffisance des dépenses de santé "
       "dans les pays pauvres."],
  exp="L’espérance de vie est un indicateur synthétique puissant : elle "
      "reflète la qualité du système de soins, la nutrition, l’accès à l’eau "
      "potable, l’hygiène et la sécurité de l’enfance. Elle ne dit donc pas "
      "seulement combien de temps une population vit, mais la qualité globale "
      "de son environnement sanitaire et social.",
  diss="Ce contraste est l’argument d’ouverture le plus efficace pour "
       "justifier le passage du revenu aux indicateurs sanitaires."),

f(id='q7-n06', sp='c7-03', niv='connaitre', type='qcm', b=338,
  q="Comment s’exprime techniquement le taux de mortalité infantile, et "
    "pourquoi cet indicateur est-il particulièrement révélateur ?",
  opts=["En pourcentage de la population ; il mesure la densité médicale",
        "En nombre de décès pour 1 000 naissances vivantes ; il reflète la "
        "qualité des conditions de vie et influe directement sur l’espérance "
        "de vie moyenne",
        "En années d’espérance de vie perdues ; il mesure le coût économique "
        "de la mortalité",
        "En nombre de décès par médecin ; il mesure l’efficacité du système "
        "de soins"],
  ans=1,
  why=["Ce n’est pas un pourcentage de la population, et l’indicateur ne "
       "mesure pas la densité médicale.",
       "Les années de vie perdues sont une autre construction statistique.",
       "Aucun rapport au nombre de médecins n’est retenu."],
  exp="Le cours précise que l’indicateur est mesuré avant un an dans certains "
      "contextes nationaux, mais qu’il s’agit souvent, dans les tableaux "
      "internationaux, de la mortalité des moins de cinq ans. C’est un "
      "indicateur extrêmement sensible des défaillances sanitaires et "
      "sociales, et la baisse de la mortalité infantile constitue l’un des "
      "leviers les plus puissants d’augmentation de l’espérance de vie."),

f(id='q7-n07', sp='c7-03', niv='appliquer', type='qcm', b=348,
  q="Quels ordres de grandeur le cours retient-il pour les dépenses annuelles "
    "de santé par habitant ?",
  opts=["Environ 300 dollars dans les pays à faible revenu, 2 000 dans les "
        "pays à revenu élevé",
        "Environ 30 dollars dans les pays à faible revenu, 5 800 dans les "
        "pays à revenu élevé",
        "Environ 100 dollars dans les pays à faible revenu, 1 000 dans les "
        "pays à revenu élevé",
        "Environ 30 dollars dans les pays à faible revenu, 500 dans les pays "
        "à revenu élevé"],
  ans=1,
  why=["L’écart retenu par le cours est bien plus considérable.",
       "Ces montants sous-estiment les deux termes de la comparaison.",
       "Le second montant est très inférieur au repère du cours."],
  exp="Le rapport est d’environ 1 à 190 : 30 dollars par habitant et par an "
      "dans les pays à faible revenu contre environ 5 800 dans les pays à "
      "revenu élevé. C’est un indicateur de moyens, qui traduit des capacités "
      "très inégales à financer l’accès généralisé aux soins — même si la "
      "qualité des institutions et des politiques publiques reste également "
      "déterminante."),

f(id='q7-n08', sp='c7-03', niv='appliquer', type='qcm', b=388,
  q="Que désigne le seuil de renouvellement des générations, et à quel niveau "
    "se situe-t-il dans les pays développés ?",
  opts=["Le nombre d’enfants par femme assurant le remplacement de la "
        "génération des parents, hors migrations : environ 2,1",
        "Le nombre d’enfants par femme assurant la croissance de la "
        "population : environ 3",
        "Le taux de natalité minimal compatible avec le plein emploi : "
        "environ 1,5 %",
        "Le nombre d’enfants par femme au-delà duquel la pauvreté augmente : "
        "environ 4"],
  ans=0,
  why=["Le seuil assure le remplacement, non la croissance de la population.",
       "Il ne s’agit pas d’un taux de natalité et il n’a aucun lien avec le "
       "plein emploi.",
       "Aucun seuil de ce type n’est mentionné par le cours."],
  exp="Le seuil n’est pas exactement égal à 2 parce qu’il faut tenir compte "
      "des décès avant l’âge de reproduction, des personnes qui n’auront pas "
      "d’enfants et de certains ajustements statistiques. En dessous, et "
      "durablement, la population vieillit, la population active se réduit à "
      "long terme et des tensions apparaissent sur les retraites, la santé et "
      "le financement de la dépendance.",
  diss="La Corée du Sud, avec une fécondité proche de 0,7 enfant par femme, "
       "est l’exemple extrême : la baisse de la fécondité, signe de "
       "développement, peut devenir elle-même un problème."),

f(id='q7-n09', sp='c7-03', niv='raisonner', type='qcm', b=400,
  q="Comment le cours interprète-t-il la forte fécondité observée dans de "
    "nombreux pays à faible revenu ?",
  opts=["Comme un choix familial librement consenti, sans lien avec le "
        "développement",
        "Comme le reflet de contraintes liées à la pauvreté, à la faiblesse "
        "des systèmes de santé et à l’insuffisante scolarisation des filles",
        "Comme la conséquence directe de politiques natalistes",
        "Comme un phénomène strictement culturel et religieux"],
  ans=1,
  why=["Le cours insiste précisément sur le fait qu’il s’agit moins d’un "
       "simple choix familial que d’un ensemble de contraintes.",
       "Les politiques natalistes ne sont pas l’explication avancée.",
       "Les normes familiales jouent un rôle, mais le cours refuse une "
       "lecture purement culturelle."],
  exp="L’exemple indien montre que ces mécanismes s’observent aussi à "
      "l’intérieur d’un même pays : là où la scolarisation s’est diffusée, où "
      "l’éducation des filles est plus avancée et où l’information sanitaire "
      "est accessible, la fécondité est plus faible. Le développement est "
      "donc inégal entre pays, mais aussi au sein des pays.",
  diss="Cette lecture évite deux écueils symétriques : le déterminisme "
       "culturel et l’explication par le seul revenu."),

f(id='q7-n10', sp='c7-03', niv='comprendre', type='assoc', b=497,
  q="Associez chacun des deux indicateurs éducatifs de l’IDH à ce qu’il "
    "mesure.",
  ans=[["Durée attendue de scolarisation", "Le nombre d’années d’études qu’un enfant entrant aujourd’hui peut espérer suivre : un indicateur prospectif"],
       ["Durée moyenne de scolarisation", "Le nombre moyen d’années effectivement accomplies par la population adulte : un indicateur rétrospectif"],
       ["Durée attendue supérieure à la durée moyenne", "Un système éducatif en progrès : rattrapage et allongement des parcours"],
       ["Durée attendue inférieure à la durée moyenne", "Un signal d’alerte : guerre, crise, déscolarisation, retrait de l’État"]],
  exp="Les deux indicateurs sont des moyennes, mais ils ne portent ni sur la "
      "même population ni sur la même temporalité : l’un mesure un héritage "
      "éducatif — le stock de capital humain déjà constitué — l’autre les "
      "perspectives offertes aux nouvelles générations. Le cours chiffre "
      "l’ampleur des écarts : environ 5,6 ans de durée attendue dans certains "
      "pays, près de 21 ans en Australie.",
  diss="Lire l’écart entre les deux indicateurs permet de diagnostiquer une "
       "dynamique, et pas seulement un niveau : c’est exactement ce qu’attend "
       "un correcteur d’une analyse d’indicateur."),

f(id='q7-n11', sp='c7-03', niv='comprendre', type='qcm', b=557,
  q="Quelle distinction le cours établit-il entre scolarisation et "
    "éducation ?",
  opts=["Les deux termes sont équivalents",
        "La scolarisation renvoie à la fréquentation d’un établissement, "
        "l’éducation à l’acquisition de connaissances et de compétences",
        "La scolarisation concerne le primaire, l’éducation le supérieur",
        "La scolarisation est obligatoire, l’éducation facultative"],
  ans=1,
  why=["Le cours en fait au contraire une distinction essentielle.",
       "La distinction ne porte pas sur le niveau d’enseignement.",
       "C’est l’inverse en droit français : ce qui est juridiquement exigé est "
       "d’abord l’instruction, non la seule présence dans un établissement."],
  exp="L’exemple français l’illustre : certaines formes d’enseignement à "
      "domicile peuvent exister sous contrôle public, parce que l’obligation "
      "porte sur l’instruction. Le développement éducatif ne se réduit donc "
      "pas à la présence dans une salle de classe, même si la scolarisation "
      "reste en pratique le mode dominant."),

f(id='q7-n12', sp='c7-03', niv='raisonner', type='qcmm', b=569,
  q="Quelles inégalités éducatives le cours relève-t-il au détriment des "
    "filles dans de nombreux pays en développement ? (plusieurs réponses)",
  opts=["Une déscolarisation précoce et des interruptions d’études",
        "Le poids des tâches domestiques",
        "Les mariages et les maternités précoces",
        "Une moindre présence dans le secondaire et le supérieur",
        "Un accès plus limité aux seules filières scientifiques"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la première inégalité citée.",
       "Exacte : elle limite le temps disponible pour les études.",
       "Exacte : ils interrompent souvent définitivement la scolarité.",
       "Exacte : l’écart se creuse avec le niveau d’enseignement.",
       "Le cours ne raisonne pas sur l’orientation disciplinaire."],
  exp="Ces inégalités freinent directement l’autonomie féminine, la baisse de "
      "la fécondité, l’amélioration de la santé maternelle et infantile, "
      "l’accumulation de capital humain et le développement humain global. "
      "Elles ne sont pas seulement institutionnelles : elles sont aussi "
      "sociales, territoriales et genrées."),

f(id='q7-n13', sp='c7-03', niv='comprendre', type='courte', b=473,
  q="Pourquoi le cours fait-il de l’éducation le troisième pilier du "
    "développement ?",
  ans={'modele': "L’éducation produit des effets cumulatifs. Elle renforce "
       "d’abord le capital humain : compétences, qualification, productivité, "
       "capacités d’adaptation technologique, innovation. Mais son rôle "
       "dépasse la sphère productive : elle améliore la santé par une "
       "meilleure connaissance des pratiques préventives et un meilleur "
       "recours aux soins, fait baisser la mortalité infantile, améliore la "
       "santé maternelle, favorise la maîtrise de la fécondité — notamment par "
       "l’éducation des filles —, l’autonomie individuelle, la mobilité "
       "sociale et la participation civique. Elle est donc à la fois facteur "
       "de croissance, facteur de développement humain et levier de "
       "transformation sociale.",
       'cles': [{'f': ['capital humain', 'productivite', 'competence', 'qualification'],
                 'l': 'elle renforce le capital humain et la productivité'},
                {'f': ['sante', 'mortalite', 'prevention'],
                 'l': 'elle améliore la santé'},
                {'f': ['fecondite', 'fille', 'autonomie'],
                 'l': 'elle favorise la maîtrise de la fécondité et l’autonomie'},
                {'f': ['mobilite', 'sociale', 'civique', 'transformation'],
                 'l': 'et constitue un levier de transformation sociale'}]},
  exp="Le cours conclut : sans diffusion de l’éducation, le capital humain "
      "reste limité, les gains de productivité fragiles, les inégalités se "
      "reproduisent, la transformation structurelle est freinée et le "
      "développement humain reste inachevé."),

# ---------------------------------- c7-04 IDH : interprétation, IIG, PPA
f(id='q7-n14', sp='c7-04', niv='raisonner', type='qcm', b=660,
  q="Que révèle la comparaison entre le rang d’un pays selon son IDH et son "
    "rang selon son RNB par habitant ?",
  opts=["La fiabilité des statistiques nationales",
        "Si le pays transforme efficacement sa richesse en développement "
        "humain, ou si sa richesse ne se traduit pas pleinement en santé et "
        "en éducation",
        "Le niveau d’inégalités internes du pays",
        "La part de la population vivant sous le seuil de pauvreté"],
  ans=1,
  why=["La comparaison ne porte pas sur la qualité des données.",
       "Les inégalités internes sont captées par l’IDHI, non par cet écart de "
       "rangs.",
       "La pauvreté monétaire relève d’une autre mesure."],
  exp="Deux cas sont possibles. Rang IDH meilleur que le rang RNB : le pays "
      "n’est pas parmi les plus riches mais convertit efficacement son revenu "
      "en santé, éducation et conditions de vie — il surperforme socialement, "
      "comme le Costa Rica. Rang IDH moins bon : le pays est relativement "
      "riche mais transforme mal cette richesse, du fait d’inégalités fortes "
      "ou d’une mauvaise répartition des dépenses publiques — certains États "
      "pétroliers du Golfe, comme le Qatar.",
  diss="C’est la lecture la plus utile de l’IDH : richesse et développement "
       "ne coïncident pas, et l’écart mesure la qualité de la conversion."),

f(id='q7-n15', sp='c7-04', niv='comprendre', type='qcm', b=717,
  q="Pourquoi le RNB utilisé dans l’IDH est-il exprimé en parité de pouvoir "
    "d’achat ?",
  opts=["Pour neutraliser l’inflation sur longue période",
        "Parce que le taux de change de marché, influencé par la spéculation "
        "et les mouvements de capitaux, ne traduit pas ce qu’un revenu permet "
        "réellement d’acheter",
        "Pour faciliter les comparaisons avec le PIB",
        "Parce que le PNUD n’a pas accès aux taux de change officiels"],
  ans=1,
  why=["La correction de l’inflation est une autre opération, le passage au "
       "volume.",
       "La comparaison avec le PIB n’est pas l’objectif : le choix porte sur "
       "la conversion monétaire.",
       "Les taux de change de marché sont parfaitement disponibles : c’est "
       "leur pertinence qui est en cause."],
  exp="Le taux de change de marché dépend de la spéculation, des marchés "
      "financiers, des mouvements de capitaux, des anticipations et des "
      "déséquilibres monétaires. La PPA permet au contraire de comparer le "
      "pouvoir d’achat réel et le volume de biens et services accessibles. "
      "Avec un même revenu en dollars, le niveau de vie réel diffère "
      "fortement entre la Suisse et l’Inde : c’est ce que la PPA corrige."),

f(id='q7-n16', sp='c7-04', niv='comprendre', type='qcm', b=758,
  q="Comment se lit l’indice d’inégalité de genre (IIG) ?",
  opts=["Plus il est élevé, mieux c’est : il mesure l’égalité atteinte",
        "Plus il est faible, mieux c’est : un score proche de 0 signifie peu "
        "d’inégalités de genre, un score proche de 1 de fortes inégalités",
        "Il varie de 0 à 100 et mesure la part des femmes dans l’emploi",
        "Il mesure l’écart de salaire entre femmes et hommes, en pourcentage"],
  ans=1,
  why=["C’est l’inverse de l’IDH et de l’IDHI : attention au sens de lecture.",
       "L’IIG est compris entre 0 et 1 et ne se limite pas à l’emploi.",
       "L’écart salarial n’est pas la dimension retenue."],
  exp="L’IIG repose sur trois ensembles de dimensions : la santé "
      "reproductive — mortalité maternelle, fécondité des adolescentes ; "
      "l’autonomisation — part des sièges parlementaires occupés par des "
      "femmes, niveau d’éducation secondaire ; la participation au marché du "
      "travail, comparée à celle des hommes.",
  diss="Attention au piège classique du sens de lecture : contrairement à "
       "l’IDH et à l’IDHI, un IIG élevé est un mauvais signal."),

f(id='q7-n17', sp='c7-04', niv='connaitre', type='assoc', b=865,
  q="Associez chaque indicateur du PNUD à ce qu’il ajoute à l’IDH.",
  ans=[["IDH", "Mesurer le développement humain : revenu, santé, éducation"],
       ["IDHI", "Intégrer les inégalités internes par un malus sur chaque dimension"],
       ["IIG", "Mesurer les inégalités entre les femmes et les hommes"],
       ["IPM", "Saisir la pauvreté comme un ensemble de privations concrètes"],
       ["IDHP", "Ajuster le développement humain aux pressions planétaires"]],
  exp="Ces indicateurs s’inscrivent tous dans la perspective d’Amartya Sen, "
      "pour qui le développement consiste à élargir les capabilités. Le cours "
      "souligne l’enrichissement considérable de la mesure — et son coût : "
      "plus les indicateurs sont riches, plus leur interprétation devient "
      "délicate.",
  diss="Pouvoir citer cinq indicateurs avec ce qu’ils corrigent chacun est "
       "l’une des manières les plus rapides de montrer la maîtrise du "
       "chapitre."),

# ------------------------- c7-05 portée et limites des indicateurs composites
f(id='q7-n18', sp='c7-05', niv='raisonner', type='qcm', b=829,
  q="Quelle difficulté majeure le cours attribue aux indicateurs composites ?",
  opts=["Ils sont trop coûteux à produire",
        "Quand l’indicateur évolue, on ne sait pas immédiatement ce qui a "
        "changé : il faut revenir au détail des composantes",
        "Ils ne permettent pas de classer les pays",
        "Ils ne sont publiés que tous les dix ans"],
  ans=1,
  why=["Le coût de production n’est pas l’argument retenu.",
       "Les indicateurs composites permettent au contraire de produire des "
       "classements : c’est l’un de leurs intérêts.",
       "L’IDH est publié annuellement par le PNUD."],
  exp="Le cours donne un exemple simple : si un pays passe d’un IDH de 0,70 à "
      "0,75, on sait que sa performance globale s’améliore, mais pas si cette "
      "amélioration vient du revenu, de la santé, de l’éducation ou d’une "
      "combinaison des trois. Le même raisonnement vaut pour l’IDHI, l’IIG et "
      "l’IPM : plus un indicateur restitue la complexité, plus son "
      "interprétation devient difficile.",
  diss="Formule à retenir : la multiplication des indicateurs ne supprime pas "
       "la difficulté d’analyse, elle la déplace — on gagne en précision, on "
       "perd en lisibilité immédiate."),

f(id='q7-n19', sp='c7-05', niv='comprendre', type='qcm', b=846,
  q="Pourquoi le PIB et le RNB restent-ils massivement utilisés malgré leurs "
    "limites ?",
  opts=["Parce qu’ils mesurent le bien-être mieux que les indicateurs "
        "composites",
        "Parce qu’ils sont simples, rapidement lisibles, facilement "
        "comparables et que leur évolution est plus facile à interpréter",
        "Parce que les indicateurs composites ne sont pas calculés pour tous "
        "les pays",
        "Parce que les institutions internationales refusent les indicateurs "
        "du PNUD"],
  ans=1,
  why=["Le cours rappelle précisément qu’ils ne mesurent ni la qualité de "
       "vie, ni la répartition, ni les libertés réelles.",
       "La disponibilité n’est pas l’argument avancé.",
       "Les indicateurs du PNUD sont au contraire largement utilisés par les "
       "institutions internationales."],
  exp="Quand le PIB augmente, on sait globalement que la production augmente ; "
      "quand un indicateur composite varie, il faut décomposer ses "
      "sous-indicateurs, analyser les mécanismes internes et regarder les "
      "effets de classement. Les indicateurs monétaires sont donc "
      "insuffisants, mais ils restent utiles.",
  diss="Cette conclusion nuancée est la bonne manière de traiter un sujet sur "
       "la mesure du développement : ni rejet du PIB, ni foi dans un "
       "indicateur unique."),

f(id='q7-n20', sp='c7-05', niv='raisonner', type='courte', b=875,
  q="Quel compromis le cours identifie-t-il dans la mesure du développement ?",
  ans={'modele': "Les nouveaux indicateurs permettent de mieux restituer la "
       "complexité du développement : revenu, santé, éducation, inégalités, "
       "rapports de genre, privations concrètes, accès réel aux opportunités. "
       "On ne réduit plus le développement à la croissance et l’on reconnaît "
       "ses dimensions sociale, humaine, distributive et qualitative. Mais "
       "plus un indicateur est composite, plus son interprétation devient "
       "difficile. L’enjeu n’est donc pas de multiplier indéfiniment les "
       "indicateurs mais de trouver un compromis entre richesse analytique et "
       "lisibilité statistique ; le développement suppose une lecture croisée "
       "et nuancée, non un seul chiffre.",
       'cles': [{'f': ['richesse analytique', 'complexite', 'multidimension'],
                 'l': 'des indicateurs plus riches restituent mieux la complexité'},
                {'f': ['lisibilite', 'interpretation', 'difficile', 'illisible'],
                 'l': 'mais l’interprétation devient plus difficile'},
                {'f': ['compromis', 'croisee', 'un seul chiffre', 'unique'],
                 'l': 'd’où la recherche d’un compromis, et une lecture croisée'}]},
  exp="Cette tension est l’une des trois idées directrices du chapitre, et "
      "elle explique la coexistence durable des indicateurs monétaires et des "
      "indicateurs composites."),

f(id='q7-n21', sp='c7-05', niv='appliquer', type='vf', b=748,
  q="Un pays dont l’IDHI est très inférieur à son IDH connaît de fortes "
    "inégalités internes.",
  ans=True,
  exp="L’IDHI reprend les trois dimensions de l’IDH mais applique un malus "
      "lorsque les inégalités y sont importantes. Plus les inégalités sont "
      "fortes, plus l’écart entre IDH et IDHI est grand et plus le classement "
      "du pays recule. Le cours cite l’Afrique du Sud et le Brésil : un "
      "niveau de développement humain non négligeable, mais de fortes "
      "inégalités internes.",
  diss="Savoir lire un écart entre deux indicateurs — IDH / IDHI, IDH / IDHP, "
       "durée attendue / durée moyenne — est la compétence la plus rentable "
       "de ce chapitre."),

# ----------------------------------- c7-06 démographie et développement
f(id='q7-n22', sp='c7-06', niv='connaitre', type='qcm', b=905,
  q="Quelle formule résume la position populationniste de Jean Bodin, et dans "
    "quel ouvrage l’exprime-t-il ?",
  opts=["« Il n’est richesse ni force que d’hommes », dans La République "
        "(1576)",
        "« La population croît géométriquement », dans l’Essai sur le "
        "principe de population (1798)",
        "« L’offre crée sa propre demande », dans le Traité d’économie "
        "politique (1803)",
        "« Les hommes font la richesse des nations », dans la Richesse des "
        "nations (1776)"],
  ans=0,
  why=["Cette formule est de Malthus, qui soutient la thèse inverse.",
       "C’est la loi de Say, étrangère à la question démographique.",
       "Ni la formule ni l’ouvrage ne correspondent."],
  exp="Pour Bodin, une population nombreuse signifie plus de production, donc "
      "plus de richesse, mais aussi plus de soldats, donc plus de puissance "
      "politique et militaire. La population est pensée comme un facteur de "
      "puissance économique et étatique.",
  diss="Bodin ouvre le débat que Malthus, Marx, Boserup et Hansen vont "
       "prolonger : la population est-elle une richesse ou une charge ?"),

f(id='q7-n23', sp='c7-06', niv='comprendre', type='qcm', b=926,
  q="Quelle est, selon le cours, la véritable question posée par une forte "
    "croissance démographique ?",
  opts=["Le nombre total d’habitants que la planète peut nourrir",
        "La capacité d’absorption : l’économie peut-elle créer assez "
        "d’emplois, scolariser la jeunesse, financer santé et "
        "infrastructures ?",
        "Le niveau du taux de fécondité souhaitable",
        "Le rythme des migrations internationales"],
  ans=1,
  why=["La capacité nourricière globale est l’angle malthusien, que le cours "
       "dépasse.",
       "Le cours ne fixe aucun niveau souhaitable de fécondité.",
       "Les migrations sont une composante de la croissance démographique, "
       "non la question centrale."],
  exp="La vraie question n’est pas seulement combien d’habitants il y a, mais "
      "si l’économie est capable de transformer une population jeune en "
      "population productive. La démographie n’est favorable que si elle est "
      "accompagnée de capacités économiques et institutionnelles suffisantes.",
  diss="Formule à retenir : la démographie n’est ni une fatalité ni une "
       "garantie ; ses effets dépendent de la manière dont une société "
       "transforme sa population en capacité productive."),

f(id='q7-n24', sp='c7-06', niv='appliquer', type='qcm', b=966,
  q="Quels repères historiques le cours retient-il pour la population "
    "mondiale ?",
  opts=["1 milliard vers 1800, 2,5 milliards vers 1950, 8,1 à 8,2 milliards "
        "vers 2024",
        "500 millions vers 1800, 2 milliards vers 1950, 7 milliards vers 2024",
        "1 milliard vers 1800, 4 milliards vers 1950, 9 milliards vers 2024",
        "2 milliards vers 1800, 5 milliards vers 1950, 8 milliards vers 2024"],
  ans=0,
  why=["Les trois ordres de grandeur sont sous-estimés.",
       "Le chiffre de 1950 est très surestimé.",
       "Le point de départ de 1800 est doublé à tort."],
  exp="Entre 1800 et 1950, la population mondiale augmente fortement, mais "
      "c’est surtout après 1950 que l’impression d’explosion démographique "
      "devient marquante — d’où l’inquiétude des années 1960-1970. Le cours "
      "précise aussitôt la nuance fondamentale : la population continue "
      "d’augmenter, mais son taux de croissance ralentit, du fait de la baisse "
      "de la fécondité, de la diffusion de l’éducation, de l’urbanisation et "
      "de l’accès à la contraception."),

f(id='q7-n25', sp='c7-06', niv='connaitre', type='assoc', b=1013,
  q="Associez chaque auteur à son analyse de la relation entre démographie et "
    "développement.",
  ans=[["Malthus", "La population croît géométriquement, la production arithmétiquement : risque de famine et de misère"],
       ["Marx", "La pauvreté ne vient pas d’un excès de population mais du capitalisme : armée industrielle de réserve"],
       ["Boserup", "La pression démographique est une pression créatrice : elle pousse à innover et à intensifier l’agriculture"],
       ["Hansen", "Un ralentissement démographique réduit la demande et l’investissement : risque de stagnation"]],
  exp="Les quatre positions ne sont pas symétriques. Malthus voit un risque "
      "dans l’excès, Hansen un risque dans l’insuffisance ; Marx déplace "
      "l’analyse vers les rapports sociaux, Boserup inverse directement la "
      "logique malthusienne. L’ensemble montre qu’il n’existe pas de relation "
      "mécanique entre population et développement.",
  diss="Pouvoir opposer Malthus et Boserup d’un côté, Malthus et Hansen de "
       "l’autre, permet de montrer que le même phénomène démographique peut "
       "être lu comme menace ou comme moteur."),

f(id='q7-n26', sp='c7-06', niv='comprendre', type='qcm', b=1026,
  q="Que distingue Malthus entre freins préventifs et freins positifs ?",
  opts=["Les freins préventifs sont les politiques publiques, les freins "
        "positifs les comportements individuels",
        "Les freins préventifs limitent les naissances — retard du mariage, "
        "limitation volontaire ; les freins positifs réduisent la population "
        "par les famines, les guerres et les maladies",
        "Les freins préventifs relèvent de l’agriculture, les freins positifs "
        "de l’industrie",
        "Les freins préventifs sont souhaitables, les freins positifs "
        "efficaces"],
  ans=1,
  why=["La distinction ne porte pas sur l’acteur mais sur le moment et le "
       "mécanisme.",
       "Aucun lien sectoriel n’est en cause.",
       "Le qualificatif « positif » ne porte aucun jugement de valeur : il "
       "désigne une action effective sur la mortalité."],
  exp="Malthus raisonne à partir des rendements décroissants en agriculture : "
      "il serait impossible de nourrir durablement une population en forte "
      "expansion. Les freins préventifs agissent sur la natalité, les freins "
      "positifs sur la mortalité. Attention au vocabulaire : « positif » ne "
      "signifie pas « souhaitable »."),

f(id='q7-n27', sp='c7-06', niv='raisonner', type='ordre', b=1094,
  q="Remettez dans l’ordre les trois effets successifs d’une forte fécondité, "
    "tels que le cours les décrit.",
  ans=["Une jeunesse nombreuse pèse sur le revenu par tête : dépenses "
       "scolaires et de santé, forte dépendance démographique",
       "Ces générations arrivent à l’âge actif : plus de main-d’œuvre, de "
       "production, de revenus, d’épargne et d’investissement",
       "C’est le moment du dividende démographique, à condition que "
       "l’économie absorbe cette main-d’œuvre",
       "Puis la population vieillit : hausse des retraités, dépenses de santé "
       "et de dépendance",
       "Une nouvelle charge pèse alors sur les systèmes sociaux"],
  exp="L’intérêt de cette séquence est de montrer qu’une même dynamique "
      "démographique produit successivement une charge, un soutien à la "
      "croissance, puis de nouveau une charge. Le rapport actifs / inactifs "
      "est donc une clé de lecture dynamique, et non un état.",
  diss="Enchaînement très efficace pour traiter un sujet sur le vieillissement "
       "sans tomber dans le catastrophisme : la charge actuelle est le revers "
       "d’un dividende passé."),

f(id='q7-n28', sp='c7-06', niv='raisonner', type='qcmm', b=1134,
  q="À quelles conditions le dividende démographique se réalise-t-il, selon "
    "Bloom et Canning ? (plusieurs réponses)",
  opts=["Des emplois en nombre suffisant",
        "Un système éducatif et sanitaire capable d’accompagner les "
        "générations nombreuses",
        "Des infrastructures et des institutions efficaces",
        "Une stabilité politique",
        "Un taux de fécondité maintenu élevé"],
  ans=[0, 1, 2, 3],
  why=["Exacte : sans emplois, le dividende se transforme en chômage massif.",
       "Exacte : éducation et santé conditionnent la productivité de ces "
       "actifs.",
       "Exacte : le cours les cite explicitement.",
       "Exacte : elle conditionne l’investissement et l’absorption de la "
       "main-d’œuvre.",
       "C’est l’inverse : le dividende apparaît précisément quand la "
       "fécondité baisse et que la part des enfants diminue relativement."],
  exp="Sans ces conditions, la fenêtre démographique se referme sur du "
      "chômage massif, de l’informalité, du sous-emploi et des tensions "
      "sociales. Le dividende est une opportunité, non un automatisme."),

f(id='q7-n29', sp='c7-07', niv='comprendre', type='qcm', b=1217,
  q="Quelle critique majeure le cours adresse-t-il au modèle de la transition "
    "démographique ?",
  opts=["Il surestime le rôle de la mortalité infantile",
        "Il est eurocentrique : construit à partir de l’expérience "
        "européenne, surtout occidentale, il ne peut pas être érigé en loi "
        "universelle",
        "Il néglige l’effet des migrations",
        "Il repose sur des données non vérifiables"],
  ans=1,
  why=["La mortalité infantile est au contraire un canal essentiel du "
       "modèle.",
       "Les migrations sont traitées séparément, comme composante de la "
       "croissance démographique.",
       "Le cours ne met pas en cause la qualité des données."],
  exp="Le modèle est éclairant mais ne s’applique pas partout au même rythme, "
      "avec les mêmes institutions, ni selon la même chronologie. Le cours "
      "illustre par le cas français : l’égalité successorale a pu inciter "
      "certaines familles à limiter les naissances pour éviter la "
      "fragmentation du patrimoine. Les comportements démographiques sont donc "
      "aussi économiques, sociaux et institutionnels.",
  diss="Le cas français est précieux : il montre qu’une baisse précoce de la "
       "fécondité peut relever des institutions, et non du seul niveau de "
       "développement."),

f(id='q7-n30', sp='c7-07', niv='raisonner', type='qcm', b=1271,
  q="Pourquoi les projections démographiques doivent-elles être maniées avec "
    "prudence ?",
  opts=["Parce qu’elles sont rarement publiées",
        "Parce qu’elles dépendent de comportements humains et de "
        "transformations économiques, sociales, culturelles et politiques qui "
        "peuvent évoluer rapidement",
        "Parce qu’elles ne portent que sur le court terme",
        "Parce qu’elles négligent la mortalité"],
  ans=1,
  why=["Elles sont au contraire indispensables et régulièrement produites.",
       "Elles portent justement sur le long terme.",
       "La mortalité est l’une de leurs variables centrales."],
  exp="Les trajectoires dépendent du niveau de vie, de l’urbanisation, de la "
      "scolarisation des filles, de l’accès à la contraception, du recul de "
      "la mortalité infantile, de l’emploi des femmes, des normes familiales, "
      "des politiques natalistes ou antinatalistes et des migrations. Une "
      "baisse de la mortalité n’entraîne donc pas mécaniquement une hausse "
      "durable de la natalité : elle peut même accélérer la transition.",
  diss="Les comportements démographiques ne relèvent pas d’un déterminisme "
       "biologique simple : c’est la formule à retenir pour nuancer tout "
       "raisonnement sur la population."),

# ------------------------------------- c7-07 / c7-08 endettement et dette
f(id='q7-n31', sp='c7-07', niv='comprendre', type='qcm', b=1328,
  q="Pourquoi l’endettement constitue-t-il un mode normal de financement du "
    "développement ?",
  opts=["Parce qu’il permet d’éviter l’impôt",
        "Parce qu’un pays en développement n’a pas toujours une épargne "
        "intérieure suffisante, un système fiscal performant ni un revenu "
        "national permettant d’autofinancer ses investissements",
        "Parce que les taux d’intérêt internationaux sont toujours plus bas "
        "que la croissance",
        "Parce que les créanciers imposent des investissements productifs"],
  ans=1,
  why=["L’endettement n’est pas une alternative à l’impôt mais un complément "
       "de financement.",
       "Rien ne garantit cette inégalité : la crise des années 1980 en est "
       "la démonstration inverse.",
       "Le cours relève au contraire qu’une partie des emprunts a financé des "
       "dépenses improductives."],
  exp="Le mécanisme attendu est une chaîne : emprunt aujourd’hui, "
      "investissement public ou productif, hausse future de la productivité "
      "et de la croissance, hausse des recettes publiques, remboursement rendu "
      "possible. L’endettement permet donc de mobiliser immédiatement des "
      "ressources pour des investissements dont les effets se manifesteront "
      "plus tard.",
  diss="La question du chapitre est bien posée : faut-il s’endetter pour se "
       "développer, ou se développer pour se désendetter ?"),

f(id='q7-n32', sp='c7-07', niv='connaitre', type='qcm', b=1363,
  q="Quel contexte international a favorisé l’endettement des pays du Sud "
    "dans les années 1960-1970 ?",
  opts=["La hausse des taux d’intérêt américains",
        "L’abondance de liquidités internationales et le recyclage des "
        "pétrodollars après 1973, avec l’impression que la croissance future "
        "permettrait de rembourser facilement",
        "La création du Consensus de Washington",
        "L’appréciation du dollar"],
  ans=1,
  why=["La hausse des taux américains est au contraire le déclencheur de la "
       "crise, en 1979.",
       "Le Consensus de Washington date de 1989 : il est la réponse à la "
       "crise, non sa cause.",
       "L’appréciation du dollar fait partie des chocs qui aggravent la "
       "crise des années 1980."],
  exp="Deux logiques se conjuguaient : une insuffisance de l’épargne "
      "intérieure dans les pays en développement, et une offre abondante de "
      "capitaux internationaux à coût relativement faible. Les prêts aux pays "
      "du Sud se multiplient, dans l’anticipation d’une croissance qui "
      "faciliterait le remboursement."),

f(id='q7-n33', sp='c7-08', niv='raisonner', type='ordre', b=1413,
  q="Remettez dans l’ordre la chaîne qui transforme l’endettement en crise au "
    "début des années 1980.",
  ans=["En 1979, Paul Volcker mène à la Fed une politique monétaire "
       "restrictive pour lutter contre l’inflation",
       "Les taux d’intérêt s’envolent, or environ 70 % de la dette du Tiers "
       "Monde est à taux variable auprès de banques privées",
       "Le dollar s’apprécie, et comme la dette est largement libellée en "
       "dollars, son poids réel augmente",
       "Les cours des matières premières reculent, réduisant les recettes "
       "d’exportation",
       "Dette plus chère, plus lourde en monnaie nationale, recettes en "
       "baisse : la soutenabilité s’effondre"],
  exp="Les trois chocs sont indépendants mais convergents, et c’est leur "
      "combinaison qui fait basculer la situation. Le cours insiste sur un "
      "point : la crise ne vient pas du fait d’emprunter, mais du fait de ne "
      "plus pouvoir rembourser — ou de ne pouvoir le faire qu’au prix d’une "
      "récession majeure, voire de perdre l’accès au financement.",
  diss="Enchaînement très rentable : il montre qu’une crise de la dette peut "
       "venir entièrement de l’extérieur, sans changement de comportement du "
       "pays débiteur."),

f(id='q7-n34', sp='c7-08', niv='connaitre', type='assoc', b=1448,
  q="Associez chaque solution de gestion de la dette à son contenu et à son "
    "exemple institutionnel.",
  ans=[["Le rééchelonnement", "Reporter les échéances et allonger la durée sans réduire la dette : Club de Paris (1956), Club de Londres"],
       ["L’allègement ou la restructuration", "Réduire une partie de la dette contre des engagements : Plan Brady (1989)"],
       ["L’annulation partielle", "Effacer une partie de la dette : les PPTE depuis les années 1990"]],
  exp="Chaque solution a sa limite. Le rééchelonnement soulage la contrainte "
      "de liquidité mais ne règle pas la solvabilité : il déplace le problème "
      "dans le temps. L’allègement laisse une dette qui peut rester lourde si "
      "la croissance ne repart pas. L’annulation risque une perte de confiance "
      "des créanciers, un « mauvais signal », une difficulté d’accès futur aux "
      "marchés et une fragilisation du système bancaire créancier.",
  diss="Le Club de Paris réunit les créanciers publics, le Club de Londres "
       "constitue un cadre plus informel pour les créanciers privés : la "
       "distinction est souvent demandée."),

f(id='q7-n35', sp='c7-08', niv='comprendre', type='qcm', b=1493,
  q="Que sont les PAS, et dans quelle logique s’inscrivent-ils ?",
  opts=["Des prêts à taux bonifiés accordés par le Club de Paris",
        "Des plans d’ajustement structurel imposés ou fortement encouragés "
        "par le FMI et la Banque mondiale en échange d’une aide financière, "
        "inscrits dans le Consensus de Washington",
        "Des programmes d’aide alimentaire d’urgence",
        "Des accords commerciaux préférentiels négociés à l’OMC"],
  ans=1,
  why=["Le Club de Paris restructure des dettes publiques, il n’impose pas de "
       "programme de réformes.",
       "Les PAS ne sont pas des programmes humanitaires.",
       "Ils ne relèvent pas du droit commercial international."],
  exp="Les PAS sont la contrepartie politique et économique du traitement de "
      "la dette : en échange d’une aide, d’un rééchelonnement ou d’un soutien "
      "à la solvabilité, les pays s’engagent à stabiliser leur monnaie, "
      "réduire les déficits, libéraliser, ouvrir, privatiser et déréglementer.",
  diss="Le mot de John Williamson, en 1989, donne son nom à l’ensemble : "
       "Consensus de Washington. La trilogie à citer est déréglementation, "
       "libéralisation, privatisation."),

f(id='q7-n36', sp='c7-08', niv='raisonner', type='qcmm', b=1522,
  q="Quels effets pervers le cours attribue-t-il aux PAS ? (plusieurs "
    "réponses)",
  opts=["Une contraction de la demande intérieure : baisse des dépenses "
        "publiques, réduction des salaires publics, recul de la consommation",
        "Une aggravation de la pauvreté : baisse des dépenses sociales, recul "
        "de l’accès à la santé et à l’éducation",
        "Une accentuation des inégalités et une marginalisation des secteurs "
        "fragiles",
        "Une fragilisation des économies nationales : industries locales "
        "exposées trop vite à la concurrence internationale",
        "Une hausse durable de l’inflation"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est le premier canal, par l’austérité budgétaire.",
       "Exacte : le recul de l’accès aux services essentiels est relevé "
       "explicitement.",
       "Exacte : protection sociale réduite et concentration des gains.",
       "Exacte : désindustrialisation ou affaiblissement des secteurs "
       "naissants, dépendance accrue aux marchés mondiaux.",
       "La stabilisation monétaire est au contraire l’un des objectifs "
       "affichés des PAS."],
  exp="Le cours résume : les PAS ont souvent restauré des équilibres "
      "financiers de court terme au prix d’un coût social élevé. C’est "
      "exactement la tension à exposer dans une copie : efficacité financière "
      "contre soutenabilité sociale."),

# ------------------------------- c7-09 dette souveraine, cas argentin
f(id='q7-n37', sp='c7-09', niv='connaitre', type='qcm', b=1551,
  q="Qu’est-ce qu’un fonds vautour ?",
  opts=["Un fonds souverain investissant dans les matières premières",
        "Un fonds d’investissement privé qui rachète à bas prix la dette d’un "
        "État en difficulté puis réclame devant les tribunaux le remboursement "
        "intégral à la valeur nominale",
        "Un fonds de garantie créé par le FMI pour les pays surendettés",
        "Un fonds spéculatif pariant sur la faillite des banques"],
  ans=1,
  why=["Un fonds souverain appartient à un État : ce n’est pas la même "
       "catégorie d’acteur.",
       "Le FMI n’a pas créé de fonds de ce type.",
       "La spéculation visée porte sur des titres de dette souveraine, non "
       "sur des banques."],
  exp="Benjamin Lemoine, dans « Chasseurs d’États » (2024), montre comment "
      "certains acteurs financiers privés transforment la dette souveraine en "
      "terrain de chasse spéculatif, révélant l’emprise croissante de la "
      "finance sur les États.",
  diss="Le vocabulaire est important : ces fonds ne spéculent pas sur un "
       "défaut à venir, ils achètent après le défaut et misent sur la justice "
       "pour obtenir le nominal."),

f(id='q7-n38', sp='c7-09', niv='appliquer', type='ordre', b=1554,
  q="Remettez dans l’ordre la chronologie du contentieux argentin.",
  ans=["En 2001, l’Argentine fait défaut partiellement sur sa dette "
       "souveraine, pour environ 100 milliards de dollars",
       "De 2005 à 2010, environ 93 % des créanciers acceptent une "
       "restructuration réduisant d’environ 70 % la valeur de la dette",
       "Une minorité d’environ 7 % refuse, dont le fonds NML, et réclame le "
       "remboursement intégral à la valeur nominale",
       "De 2012 à 2014, un juge américain bloque certains paiements puis la "
       "justice américaine donne raison aux fonds",
       "En 2016, l’Argentine met fin au contentieux, verse environ "
       "4,65 milliards de dollars et émet de nouvelles dettes pour revenir sur "
       "les marchés"],
  exp="Le fonds NML, lié à Paul Singer, réalise un gain considérable : des "
      "obligations achetées à très bas prix, remboursées à un niveau très "
      "supérieur. L’épisode illustre l’asymétrie de pouvoir entre un État "
      "souverain et des créanciers privés capables de l’isoler des marchés.",
  diss="Chronologie précieuse : elle permet de montrer concrètement comment "
       "une restructuration acceptée par la quasi-totalité des créanciers peut "
       "être défaite par une minorité."),

f(id='q7-n39', sp='c7-09', niv='raisonner', type='qcm', b=1577,
  q="Quels phénomènes majeurs le cas argentin révèle-t-il ?",
  opts=["La financiarisation et la judiciarisation de la dette souveraine, "
        "ainsi que l’asymétrie de pouvoir entre débiteurs et créanciers",
        "L’inefficacité des rééchelonnements du Club de Paris",
        "L’impossibilité pour un État de faire défaut",
        "La supériorité des créanciers publics sur les créanciers privés"],
  ans=0,
  why=["Le Club de Paris n’intervient pas dans cet épisode, qui oppose "
       "l’Argentine à des créanciers privés.",
       "L’Argentine fait précisément défaut en 2001 : c’est le point de "
       "départ.",
       "Le cas montre l’inverse : ce sont les créanciers privés qui imposent "
       "leur solution par la voie judiciaire."],
  exp="Trois phénomènes se combinent. La dette publique devient un actif "
      "financier négociable et spéculatif. Le règlement ne passe plus "
      "seulement par la négociation politique et les institutions "
      "internationales, mais par les tribunaux, le droit des contrats et "
      "l’arbitrage judiciaire. Et un État souverain peut se retrouver "
      "contraint juridiquement, isolé des marchés, soumis à des logiques "
      "financières privées.",
  diss="À relier à la judiciarisation croissante des enjeux économiques et "
       "écologiques, que le cours évoque en fin de chapitre : le droit devient "
       "un instrument de valorisation économique."),

f(id='q7-n40', sp='c7-09', niv='comprendre', type='assoc', b=4042,
  q="Associez chaque notion de dette à sa définition.",
  ans=[["Le service de la dette", "Le paiement des intérêts et le remboursement du capital sur une année"],
       ["La dette publique", "Celle contractée par les administrations publiques, par opposition à la dette privée"],
       ["La dette extérieure", "Celle contractée auprès de créanciers étrangers, par opposition à la dette domestique"],
       ["La dette souveraine", "Celle émise ou garantie par un État"],
       ["La dette soutenable", "Pour un PED, un service de la dette publique extérieure n’excédant pas 15 % des exportations"]],
  exp="Ces distinctions ne sont pas purement formelles : une dette publique "
      "domestique n’expose pas aux mêmes risques qu’une dette extérieure "
      "libellée en devises, dont le poids augmente avec l’appréciation de la "
      "monnaie d’emprunt. C’est précisément ce qui s’est produit dans les "
      "années 1980.",
  diss="Le repère des 15 % des exportations est un critère concret, très "
       "utile pour qualifier une situation d’endettement sans rester dans le "
       "vague."),

f(id='q7-n41', sp='c7-09', niv='raisonner', type='courte', b=1599,
  q="L’endettement des pays en développement est-il un atout ou un obstacle ?",
  ans={'modele': "Il est d’abord un outil normal et parfois nécessaire du "
       "financement du développement, lorsque l’épargne intérieure est "
       "insuffisante et que des investissements productifs doivent être "
       "engagés : il permet d’accélérer le rattrapage et d’accroître le stock "
       "de capital. Mais il devient un obstacle majeur dès qu’il est "
       "insoutenable : hausse du service de la dette, spirale "
       "d’auto-entretien, dépendance aux créanciers, vulnérabilité aux chocs "
       "extérieurs, ajustements récessifs, aggravation de la pauvreté et des "
       "inégalités. La crise des années 1980 montre qu’un même instrument peut "
       "faire basculer un pays d’une logique de rattrapage à une logique de "
       "contrainte permanente.",
       'cles': [{'f': ['epargne', 'investissement', 'financement', 'rattrapage'],
                 'l': 'un mode normal de financement quand l’épargne manque'},
                {'f': ['soutenable', 'service', 'insoutenable'],
                 'l': 'à condition que la dette reste soutenable'},
                {'f': ['spirale', 'dependance', 'creancier', 'choc'],
                 'l': 'sinon spirale, dépendance et vulnérabilité'},
                {'f': ['1980', 'pas', 'social', 'pauvrete'],
                 'l': 'la crise des années 1980 et le coût social des PAS'}]},
  exp="La réponse attendue n’est donc ni oui ni non : c’est la soutenabilité "
      "qui fait la différence, et elle dépend autant de l’usage des fonds "
      "empruntés que de l’environnement financier international."),

# ------------------------- c7-10 mondialisation asymétrique : l’Inde (Allen)
f(id='q7-n42', sp='c7-10', niv='comprendre', type='qcm', b=1649,
  q="Quels facteurs intègrent l’économie mondiale au XIXᵉ siècle, selon "
    "Robert C. Allen ?",
  opts=["La création d’institutions internationales de régulation",
        "La baisse des coûts de transport, le navire à vapeur, le chemin de "
        "fer, le télégraphe et l’ouverture des marchés",
        "La libéralisation financière et la convertibilité des monnaies",
        "La fin des empires coloniaux"],
  ans=1,
  why=["Les institutions internationales de régulation n’apparaissent qu’au "
       "XXᵉ siècle.",
       "La finance n’est pas le canal retenu ici.",
       "La période étudiée est au contraire celle de l’apogée coloniale."],
  exp="Cette intégration croissante intensifie la concurrence entre "
      "producteurs à l’échelle mondiale. L’idée essentielle du cours est que "
      "la mondialisation ne crée pas spontanément une convergence entre "
      "pays : elle peut au contraire accentuer les écarts de développement.",
  diss="La référence est « Introduction à l’histoire économique mondiale » "
       "(2014) : à citer pour montrer que la question du rattrapage se pose "
       "dès le XIXᵉ siècle."),

f(id='q7-n43', sp='c7-10', niv='raisonner', type='ordre', b=1679,
  q="Remettez dans l’ordre le mécanisme de la désindustrialisation indienne "
    "au XIXᵉ siècle.",
  ans=["L’Inde dispose au départ d’une tradition textile reconnue, de "
       "cotonnades compétitives et de coûts salariaux faibles",
       "La révolution industrielle britannique crée un écart massif de "
       "productivité dans la filière coton",
       "L’intégration des marchés transmet la baisse des prix anglais à "
       "l’échelle mondiale",
       "L’Inde perd son avantage dans les textiles manufacturés mais le "
       "conserve dans le coton brut",
       "Elle devient exportatrice de matière première et importatrice de "
       "textiles britanniques, et la main-d’œuvre se replie vers "
       "l’agriculture"],
  exp="Le chiffre à retenir est la chute de la part de l’emploi industriel : "
      "22 % en 1810, 9 % en 1901. Le renversement est fondamental : avant, "
      "exportation de produits transformés ; après, exportation de matière "
      "première et importation de biens manufacturés.",
  diss="C’est la meilleure démonstration que ce qui est « efficace » selon la "
       "logique des avantages comparatifs peut être défavorable au "
       "développement de long terme."),

f(id='q7-n44', sp='c7-10', niv='raisonner', type='qcm', b=1695,
  q="Quelle tension fondamentale le cas indien met-il en évidence ?",
  opts=["Entre croissance démographique et ressources disponibles",
        "Entre l’efficacité immédiate de la spécialisation internationale et "
        "le blocage de la montée en gamme productive à long terme",
        "Entre épargne intérieure et investissement étranger",
        "Entre industrie légère et industrie lourde"],
  ans=1,
  why=["La démographie n’est pas en cause dans ce passage.",
       "Le financement n’est pas l’angle retenu par Allen.",
       "L’arbitrage sectoriel est une autre question, celle des stratégies "
       "d’industrialisation."],
  exp="Se spécialiser dans le coton brut était conforme aux avantages "
      "comparatifs de l’Inde après la montée en productivité britannique : "
      "l’allocation immédiate des ressources s’en trouvait améliorée. Mais "
      "cette spécialisation a détruit la base manufacturière et fermé la voie "
      "à l’industrialisation.",
  diss="Argument central contre une lecture purement ricardienne du "
       "développement : l’avantage comparatif peut enfermer un pays dans une "
       "spécialisation dominée."),

f(id='q7-n45', sp='c7-10', niv='comprendre', type='qcmm', b=1749,
  q="Quel rôle les institutions coloniales jouent-elles dans la trajectoire "
    "indienne ? (plusieurs réponses)",
  opts=["Une ouverture forcée ou asymétrique",
        "De faibles protections douanières, empêchant le protectionnisme "
        "éducateur",
        "Une orientation de l’économie vers les besoins de la métropole",
        "L’absence de contrôle indien sur sa propre politique économique",
        "Une interdiction formelle de toute industrie en Inde"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’insertion dans l’Empire suit des règles favorables à la "
       "métropole.",
       "Exacte : c’est l’instrument qui manque le plus à l’Inde.",
       "Exacte : la production est réorientée selon les besoins "
       "britanniques.",
       "Exacte : d’où l’impossibilité d’une stratégie nationale de "
       "rattrapage.",
       "Le cours ne mentionne aucune interdiction formelle : le mécanisme est "
       "économique et institutionnel, non juridiquement prohibitif."],
  exp="Pour développer une industrie moderne, il aurait fallu des droits de "
      "douane protecteurs, des banques d’investissement, des infrastructures "
      "orientées vers le marché intérieur, une éducation plus large et une "
      "politique industrielle cohérente. Dans le cadre colonial, le "
      "libre-échange n’est donc pas neutre : il organise une insertion "
      "subordonnée au profit de la métropole."),

f(id='q7-n46', sp='c7-10', niv='raisonner', type='qcm', b=1771,
  q="Pourquoi le chemin de fer indien est-il qualifié d’« occasion "
    "partiellement manquée » ?",
  opts=["Parce que le réseau était trop réduit pour être utile",
        "Parce que, malgré 61 000 km de voies avant 1914, les intrants "
        "modernes étaient importés, les commandes profitaient aux entreprises "
        "britanniques et il n’y eut pas de transfert de compétences",
        "Parce qu’il a été construit après l’indépendance",
        "Parce qu’il ne servait qu’aux transports militaires"],
  ans=1,
  why=["Le réseau était au contraire important : environ 61 000 km avant "
       "1914.",
       "Il est construit en pleine période coloniale.",
       "Il servait aussi aux besoins militaires, mais pas uniquement : il "
       "contribuait à créer un marché national."],
  exp="Les atouts étaient réels : intégration du territoire, baisse des coûts "
      "de transport, développement des échanges internes, facilitation des "
      "exportations. Mais rails, locomotives et acier étaient largement "
      "importés, les commandes bénéficiaient aux entreprises britanniques, et "
      "la pose des voies était confiée aux Anglais, sans transfert de "
      "connaissances ni de compétences. L’infrastructure existe, les "
      "retombées industrielles internes restent limitées.",
  diss="Exemple parfait pour montrer qu’une infrastructure n’est un facteur "
       "de développement que si elle engendre des effets d’entraînement "
       "locaux."),

f(id='q7-n47', sp='c7-10', niv='raisonner', type='courte', b=1800,
  q="En quoi le cas indien conduit-il à nuancer les théories linéaires du "
    "développement ?",
  ans={'modele': "Il montre qu’il n’existe pas de passage automatique du "
       "commerce à l’industrialisation, de l’ouverture à la modernisation, ni "
       "de l’intégration au rattrapage. L’insertion dans le marché mondial "
       "peut moderniser certains segments — le chemin de fer, les cultures "
       "d’exportation — tout en détruisant la base industrielle locale. Le "
       "sous-développement ne résulte donc pas d’un simple retard interne : il "
       "peut être produit ou aggravé par les formes concrètes de la "
       "mondialisation et par des rapports de domination politique et "
       "économique. Cela relativise directement les théories du développement "
       "par étapes, et notamment Rostow, qui suppose qu’un pays suivra "
       "naturellement la trajectoire occidentale.",
       'cles': [{'f': ['pas automatique', 'ouverture', 'integration', 'rattrapage'],
                 'l': 'aucun passage automatique de l’ouverture au rattrapage'},
                {'f': ['modernise', 'detruit', 'base industrielle'],
                 'l': 'la mondialisation peut moderniser et détruire à la fois'},
                {'f': ['domination', 'colonial', 'subordonnee'],
                 'l': 'des rapports de domination produisent le sous-développement'},
                {'f': ['rostow', 'etape', 'lineaire'],
                 'l': 'ce qui nuance Rostow et les théories par étapes'}]},
  exp="Le cas indien fait donc charnière dans le chapitre : il clôt la partie "
      "sur la mondialisation asymétrique et introduit la discussion des trois "
      "lectures du sous-développement — retard, spécificités structurelles, "
      "blocage."),

# ------------------------ c7-11 / c7-12 les trois lectures du sous-développement
f(id='q7-n48', sp='c7-11', niv='comprendre', type='assoc', b=2304,
  q="Associez chaque lecture du sous-développement à sa thèse et à ses "
    "auteurs.",
  ans=[["Lecture libérale : le sous-développement comme retard", "Rostow et les étapes de la croissance ; ouverture, marché et avantages comparatifs (HOS)"],
       ["Lecture structuraliste : des spécificités structurelles", "Gerschenkron, Perroux, Lewis et Nurkse : dualisme, désarticulation, nécessité de l’État"],
       ["Lecture tiers-mondiste : un blocage externe", "Prebisch, Emmanuel et Samir Amin : échange inégal, centre / périphérie, captation des surplus"]],
  exp="Le passage d’une lecture à l’autre déplace la cause du "
      "sous-développement : le temps pour les libéraux — il suffit d’attendre "
      "et d’ouvrir ; les structures internes pour les structuralistes — il "
      "faut transformer ; le système international pour les tiers-mondistes — "
      "il faut rompre ou renégocier.",
  diss="Cette grille à trois entrées est le plan le plus solide pour un sujet "
       "sur les causes du sous-développement."),

f(id='q7-n49', sp='c7-11', niv='comprendre', type='qcmm', b=1905,
  q="Quelles critiques le cours adresse-t-il à la lecture libérale du "
    "sous-développement ? (plusieurs réponses)",
  opts=["Une vision trop linéaire, supposant que tous les pays suivent la "
        "même trajectoire",
        "Une approche ethnocentrique, faisant du modèle occidental la norme "
        "universelle",
        "Une sous-estimation des héritages coloniaux et des asymétries de "
        "puissance",
        "Une négligence des effets parfois destructeurs de l’ouverture",
        "Un refus de prendre en compte le rôle du capital"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la première critique énoncée.",
       "Exacte : elle universalise la trajectoire occidentale.",
       "Exacte : spécialisations imposées et rapports de force sont ignorés.",
       "Exacte : le cas indien en est la démonstration historique.",
       "Le rôle du capital n’est nullement nié par l’approche libérale."],
  exp="La lecture libérale des années 1950-1960 voyait dans le "
      "sous-développement une étape inachevée : les pays pauvres suivraient la "
      "même trajectoire que les pays développés, avec un décalage temporel. À "
      "partir de 1989, cette logique inspire le FMI et la Banque mondiale dans "
      "le cadre du Consensus de Washington."),

f(id='q7-n50', sp='c7-11', niv='comprendre', type='qcm', b=1956,
  q="Quel diagnostic les structuralistes portent-ils sur les structures "
    "productives des pays en développement ?",
  opts=["Elles sont diversifiées mais mal financées",
        "Elles sont fragiles, peu diversifiées et désarticulées : les secteurs "
        "sont mal reliés, les gains de productivité restent localisés et ne se "
        "diffusent pas",
        "Elles sont trop industrialisées par rapport à la demande",
        "Elles sont identiques à celles des pays développés, à une échelle "
        "plus petite"],
  ans=1,
  why=["Le défaut de diversification est précisément l’un des constats "
       "centraux.",
       "C’est l’inverse : la faible industrialisation et la dépendance au "
       "secteur primaire sont relevées.",
       "La spécificité structurelle est au contraire ce que les "
       "structuralistes veulent établir."],
  exp="Les traits retenus sont : faible industrialisation, forte dépendance "
      "au secteur primaire, spécialisation dans des activités peu "
      "productives, faible diversification, marché intérieur limité, faible "
      "diffusion du progrès technique. Le problème central est la "
      "désarticulation : la croissance d’un secteur ne se diffuse pas à "
      "l’ensemble de l’économie.",
  diss="C’est ce diagnostic qui justifie l’intervention de l’État : "
       "protectionnisme éducateur, politique industrielle, planification, "
       "soutien aux industries naissantes, diversification productive."),

f(id='q7-n51', sp='c7-11', niv='raisonner', type='qcm', b=2044,
  q="Qu’est-ce qui distingue Lewis de Nurkse dans l’analyse du dualisme ?",
  opts=["Lewis nie l’existence du dualisme, Nurkse l’affirme",
        "Pour Lewis le dualisme peut être surmonté si le secteur moderne "
        "absorbe la main-d’œuvre et réinvestit ses profits ; pour Nurkse il "
        "peut devenir durable car il entretient un cercle vicieux",
        "Lewis raisonne sur les pays développés, Nurkse sur les pays pauvres",
        "Lewis privilégie le marché, Nurkse l’aide internationale"],
  ans=1,
  why=["Lewis est précisément celui qui théorise le dualisme.",
       "Les deux raisonnent sur les économies en développement.",
       "Nurkse ne fait pas de l’aide internationale sa réponse : il décrit un "
       "mécanisme."],
  exp="Pour Lewis, cette économie duale n’est que passagère : si le secteur "
      "moderne se développe, absorbe progressivement la main-d’œuvre "
      "excédentaire et réinvestit ses profits, il entraîne l’ensemble de "
      "l’économie. Pour Nurkse, la pauvreté produit elle-même les conditions "
      "de sa reproduction : faibles revenus, faible épargne, faible "
      "investissement, faible productivité, faibles revenus.",
  diss="Vision relativement optimiste contre lecture plus pessimiste : "
       "l’opposition est très rentable, d’autant qu’elle commande la réponse "
       "en termes de politique économique."),

f(id='q7-n52', sp='c7-12', niv='comprendre', type='qcm', b=2127,
  q="Comment Prebisch décrit-il l’organisation de l’économie mondiale ?",
  opts=["En trois ensembles : Nord, Sud et pays émergents",
        "Entre un centre industrialisé, technologiquement avancé et dominant, "
        "et une périphérie spécialisée dans les produits primaires, dépendante "
        "et dominée",
        "Entre pays créanciers et pays débiteurs",
        "Entre économies de marché et économies planifiées"],
  ans=1,
  why=["La tripartition n’est pas celle de Prebisch.",
       "L’opposition créanciers / débiteurs appartient à l’analyse de la "
       "dette.",
       "Le clivage entre systèmes économiques n’est pas son objet."],
  exp="La périphérie exporte surtout des matières premières et des produits "
      "agricoles, et importe des biens manufacturés, industriels et "
      "d’équipement. Prebisch, premier secrétaire exécutif de la CEPAL créée "
      "en 1948, en conclut que cette division internationale du travail "
      "enferme les pays en développement dans une position de dépendance.",
  diss="Attention à la nuance : le cours précise que la thèse est discutée, "
       "sur la solidité empirique des séries de prix comme sur la faisabilité "
       "d’un développement autocentré pour tous les pays."),

f(id='q7-n53', sp='c7-12', niv='connaitre', type='qcm', b=2148,
  q="Que mesurent respectivement le degré d’ouverture et le taux de "
    "couverture ?",
  opts=["Le degré d’ouverture mesure la part des exportations dans le PIB, le "
        "taux de couverture la part des importations",
        "Le degré d’ouverture mesure l’importance des échanges extérieurs "
        "dans l’économie, le taux de couverture la capacité des exportations à "
        "financer les importations",
        "Les deux mesurent la même chose, sous deux formes différentes",
        "Le degré d’ouverture mesure les droits de douane, le taux de "
        "couverture les quotas"],
  ans=1,
  why=["Le taux de couverture est un rapport entre exportations et "
       "importations, pas une simple part dans le PIB.",
       "Les deux indicateurs sont distincts : l’un porte sur l’intensité des "
       "échanges, l’autre sur leur solde relatif.",
       "Aucun des deux ne mesure les instruments de protection."],
  exp="Un taux de couverture supérieur à 1 signifie que les exportations "
      "financent plus que les importations. Mais le cours prévient contre une "
      "lecture mécanique : un taux inférieur à 1 ne signifie pas "
      "automatiquement un échec, car il peut refléter des importations de "
      "biens d’équipement, une forte demande intérieure ou une phase "
      "d’investissement. De même, un degré d’ouverture élevé n’implique pas "
      "que l’insertion soit bénéfique.",
  diss="Savoir relativiser un indicateur commercial évite les conclusions "
       "hâtives : c’est exactement ce que le cours demande à propos de "
       "Prebisch."),

f(id='q7-n54', sp='c7-12', niv='raisonner', type='assoc', b=2245,
  q="Associez chaque auteur de la radicalisation dépendantiste à sa thèse.",
  ans=[["Arghiri Emmanuel", "L’échange inégal (1969) : les écarts internationaux de salaires rendent le libre-échange structurellement inégal"],
       ["Samir Amin", "Captation des surplus : la périphérie participe au système mondial dans une position dominée, une partie de sa richesse étant captée par le centre"],
       ["Paul Bairoch", "Nuance historique : le libre-échange pur n’a pas été la voie suivie par les pays aujourd’hui développés"]],
  exp="Emmanuel et Amin vont plus loin que Prebisch : pour eux le "
      "sous-développement n’est pas un effet secondaire d’une mauvaise "
      "spécialisation mais le produit d’une logique structurelle de "
      "domination ; le sous-développement n’est donc pas une étape "
      "transitoire mais une relation de dépendance durable. Bairoch rappelle "
      "à l’inverse que beaucoup de pays développés se sont industrialisés "
      "grâce au protectionnisme et à la construction d’un marché intérieur.",
  diss="Bairoch est l’auteur à citer pour éviter l’opposition trop rigide "
       "entre ouverture bénéfique et fermeture protectrice."),

f(id='q7-n55', sp='c7-12', niv='raisonner', type='qcmm', b=2287,
  q="Quelles limites le cours oppose-t-il à l’approche tiers-mondiste ? "
    "(plusieurs réponses)",
  opts=["Tous les pays en développement ne sont pas dans la même situation de "
        "dépendance",
        "La réalité de la détérioration des termes de l’échange a été débattue",
        "Si une volonté délibérée d’exploitation existait, comment expliquer "
        "que certains pays aient échappé à cette domination ?",
        "L’approche nie l’existence des rapports de force internationaux",
        "L’approche ignore le rôle du progrès technique dans le centre"],
  ans=[0, 1, 2],
  why=["Exacte : l’hétérogénéité des PED est l’un des constats majeurs du "
       "chapitre.",
       "Exacte : le cours relève que les séries de prix et leur "
       "interprétation sont contestées.",
       "Exacte : c’est l’objection la plus forte, que les rattrapages "
       "asiatiques illustrent.",
       "C’est au contraire le cœur de son analyse.",
       "Le progrès technique du centre est au contraire au fondement de "
       "l’écart de productivité décrit."],
  exp="L’approche tiers-mondiste a une forte puissance critique, mais les "
      "trajectoires des NPI asiatiques montrent qu’une insertion dans "
      "l’économie mondiale peut aussi servir le rattrapage. C’est précisément "
      "ce que le modèle du vol d’oies sauvages permettra d’expliquer."),

# ---------------------------------------- c7-13 stratégies d’industrialisation
f(id='q7-n56', sp='c7-13', niv='connaitre', type='assoc', b=2423,
  q="Associez chaque type d’industrie à son contenu.",
  ans=[["L’industrie légère", "Biens de consommation finale : textile, habillement, agroalimentaire"],
       ["Les industries de biens intermédiaires", "Consommations intermédiaires : acier transformé, tissus, composants, produits chimiques intermédiaires"],
       ["L’industrie lourde", "Énergie, métaux, sidérurgie, chimie lourde, biens d’équipement, machines-outils"]],
  exp="Cette typologie commande les stratégies. L’industrie légère est la "
      "plus simple à développer au départ : coûts fixes plus faibles, "
      "investissements moins lourds, mise en place plus rapide. L’industrie "
      "lourde exige au contraire des coûts fixes très élevés, de lourdes "
      "infrastructures, des investissements massifs et souvent un rôle "
      "important de l’État.",
  diss="L’enjeu majeur du développement est de passer de l’exportation de "
       "produits primaires à celle de produits manufacturés : c’est le fil "
       "directeur de toute cette partie."),

f(id='q7-n57', sp='c7-13', niv='comprendre', type='qcm', b=2463,
  q="Quels sont les deux grands dilemmes des stratégies de développement des "
    "années 1950-1980 ?",
  opts=["Protectionnisme ou libre-échange ; planification ou marché",
        "Commencer par l’industrie lourde ou par l’industrie légère ; "
        "développement autocentré ou ouverture extérieure",
        "Agriculture ou industrie ; épargne intérieure ou endettement",
        "Capital étranger ou capital national ; emploi ou productivité"],
  ans=1,
  why=["Ces oppositions recoupent partiellement le second dilemme, mais ne "
       "sont pas la formulation du cours.",
       "L’arbitrage agriculture / industrie est une conséquence des choix, "
       "non le dilemme initial.",
       "Ces questions sont secondaires dans la présentation du cours."],
  exp="Les pays qui veulent s’industrialiser ne peuvent pas tout développer "
      "en même temps : d’où l’arbitrage sectoriel. Et ils doivent décider du "
      "rapport qu’ils entretiennent avec le commerce extérieur : s’en "
      "protéger pour rompre avec une dépendance héritée, ou s’appuyer sur lui "
      "comme levier de développement.",
  diss="C’est à partir du croisement de ces deux dilemmes que se déploient "
       "les trois grandes stratégies historiques : industries "
       "industrialisantes, ISI, promotion des exportations."),

f(id='q7-n58', sp='c7-13', niv='comprendre', type='qcm', b=2524,
  q="En quoi consiste la stratégie des industries industrialisantes, et de "
    "qui vient l’expression ?",
  opts=["Une logique extravertie donnant la priorité au textile exportateur, "
        "formulée par Akamatsu",
        "Une logique autocentrée donnant la priorité à l’industrie lourde, "
        "avec un État qui administre les prix, planifie et nationalise : "
        "l’expression vient de Perroux",
        "Une logique de spécialisation par avantages comparatifs, formulée "
        "par Ricardo",
        "Une logique de substitution aux importations partant de l’industrie "
        "légère, formulée par Prebisch"],
  ans=1,
  why=["Akamatsu formule le modèle du vol d’oies sauvages, qui est séquencé "
       "et non centré sur l’industrie lourde.",
       "Les avantages comparatifs justifient au contraire l’ouverture.",
       "La substitution aux importations part de l’industrie légère : c’est "
       "une stratégie distincte."],
  exp="L’idée est que certaines industries, en particulier l’industrie "
      "lourde, auraient un effet d’entraînement sur l’ensemble de l’économie : "
      "on commence par la sidérurgie, l’énergie, la chimie et les biens "
      "d’équipement, puis viennent les biens intermédiaires, puis les biens de "
      "consommation. Le développement est censé se faire hors du marché, dans "
      "une recherche d’autarcie. Les exemples cités sont l’Inde (1951-1979) "
      "et l’Algérie des années 1960.",
  diss="Limites à citer : coûts fixes très élevés, faible intensité en "
       "travail alors que la main-d’œuvre est abondante, renforcement du "
       "dualisme, et agriculture parfois négligée — la critique classique "
       "adressée à l’Algérie."),

f(id='q7-n59', sp='c7-13', niv='raisonner', type='qcm', b=2596,
  q="Quelle difficulté majeure le cours identifie-t-il dans les trois "
    "stratégies d’industrialisation ?",
  opts=["Elles échouent toutes à produire de la croissance",
        "En voulant échapper à une dépendance, beaucoup de pays tombent dans "
        "d’autres formes de dépendance : technologique, financière ou "
        "commerciale",
        "Elles supposent toutes un régime autoritaire",
        "Elles nécessitent toutes une adhésion à l’OMC"],
  ans=1,
  why=["Plusieurs de ces stratégies ont au contraire produit des rattrapages "
       "spectaculaires, notamment en Asie.",
       "Le régime politique n’est pas la variable retenue.",
       "L’adhésion à l’OMC n’est pas une condition de ces stratégies, dont "
       "la plupart sont antérieures."],
  exp="Trois déplacements sont décrits. Dépendance technologique : "
      "industrialiser exige d’importer machines, biens d’équipement et "
      "savoir-faire. Dépendance financière : les investissements massifs "
      "excèdent l’épargne disponible, d’où l’endettement — fragilité qui "
      "éclate dans les années 1980. Dépendance commerciale : les stratégies "
      "autocentrées continuent d’importer des intrants, les stratégies "
      "extraverties dépendent de la demande mondiale.",
  diss="Formule à retenir : l’industrialisation ne supprime pas la "
       "dépendance, elle la transforme."),

f(id='q7-n60', sp='c7-13', niv='raisonner', type='assoc', b=2689,
  q="Associez chaque stratégie à sa limite propre.",
  ans=[["Les industries industrialisantes", "Coûts fixes très élevés, faible intensité en travail, renforcement du dualisme, agriculture négligée"],
       ["L’ISI", "Marché intérieur souvent trop étroit pour les économies d’échelle, dépendance persistante aux biens d’équipement importés"],
       ["La promotion des exportations", "Forte dépendance à la demande mondiale, coûts sociaux élevés, spécialisation contrainte par le marché mondial"]],
  exp="Chaque limite découle logiquement de la logique de la stratégie : "
      "l’industrie lourde est capitalistique dans une économie à main-d’œuvre "
      "abondante ; l’ISI produit pour un marché national étroit ; "
      "l’exportation suppose de produire ce que demande le marché mondial "
      "plutôt que ce dont la population a besoin.",
  diss="Pouvoir énoncer une limite propre à chaque stratégie, et non une "
       "critique générale, est ce qui distingue une analyse d’un catalogue."),

# ------------------------- c7-14 / c7-15 vol d’oies sauvages et Japon
f(id='q7-n61', sp='c7-14', niv='comprendre', type='ordre', b=2757,
  q="Remettez dans l’ordre la séquence du modèle du vol d’oies sauvages.",
  ans=["Le pays importe un produit étranger : l’importation révèle le retard "
       "mais fournit un modèle à imiter",
       "Il le produit sur son territoire, derrière une protection : logique "
       "de substitution aux importations",
       "Il l’exporte quand il devient compétitif : logique de promotion des "
       "exportations",
       "Il monte en gamme vers des productions plus sophistiquées",
       "Il transfère les productions les plus simples à des pays suiveurs, "
       "créant une division régionale du travail"],
  exp="L’intérêt majeur du modèle est de montrer que l’ISI et la promotion "
      "des exportations ne sont pas contradictoires mais successives : le "
      "développement peut être d’abord protégé, puis ouvert. Le cours "
      "illustre par le Japon : importation de textiles occidentaux, puis "
      "production nationale dépassant les importations dès 1885, puis "
      "exportation de vêtements à partir des années 1920.",
  diss="C’est l’argument le plus fort contre l’opposition rigide entre "
       "autocentrage et ouverture : la séquence compte plus que le choix."),

f(id='q7-n62', sp='c7-14', niv='comprendre', type='qcm', b=2839,
  q="Quelle trajectoire sectorielle le Japon suit-il, selon le modèle ?",
  opts=["De l’agriculture vers les services, sans phase industrielle",
        "Du textile vers l’acier, puis vers des biens comme les téléviseurs, "
        "la vidéo et la HDTV",
        "De l’industrie lourde vers l’industrie légère",
        "Du charbon vers le pétrole puis vers le nucléaire"],
  ans=1,
  why=["Le Japon passe au contraire par une industrialisation complète.",
       "La progression va de l’industrie légère vers des productions plus "
       "sophistiquées, non l’inverse.",
       "Le cours ne décrit pas de trajectoire énergétique pour le Japon."],
  exp="Le pays ne reste pas spécialisé dans le même type de biens : il quitte "
      "les secteurs simples pour des secteurs plus technologiques. Le "
      "développement s’accompagne donc d’une remontée de filière et d’une "
      "montée en gamme productive, à l’échelle intra-industrielle comme "
      "interindustrielle."),

f(id='q7-n63', sp='c7-14', niv='comprendre', type='qcm', b=2896,
  q="Dans la hiérarchie régionale décrite par le modèle, quel ordre de "
    "spécialisation observe-t-on ?",
  opts=["Le Japon sur les productions standardisées, les NPI sur les "
        "productions sophistiquées",
        "Le Japon sur les productions les plus sophistiquées, les NPI sur des "
        "productions intermédiaires, l’ASEAN sur des productions plus "
        "standardisées, les latecomers sur les activités les plus simples",
        "Tous les pays asiatiques sur les mêmes produits, en concurrence "
        "directe",
        "Les latecomers sur les productions sophistiquées, grâce aux "
        "transferts de technologie"],
  ans=1,
  why=["La hiérarchie est exactement inverse.",
       "Le modèle explique précisément pourquoi les pays ne se spécialisent "
       "pas tous dans les mêmes produits au même moment.",
       "Les latecomers récupèrent les activités les plus simples, au bas de "
       "la hiérarchie."],
  exp="Les NPI sont la Corée du Sud, Taïwan, Hong Kong et Singapour ; "
      "viennent ensuite les pays de l’ASEAN, puis les entrants plus tardifs "
      "comme le Vietnam. Le Japon joue le rôle d’« oie de tête » : il "
      "industrialise d’abord certains secteurs puis, en montant en gamme, "
      "laisse les activités les plus simples aux suiveurs.",
  diss="Le modèle a donc trois dimensions : historique — le rattrapage "
       "japonais ; économique — comment on s’industrialise ; géographique — la "
       "répartition spatiale des spécialisations."),

f(id='q7-n64', sp='c7-15', niv='comprendre', type='qcm', b=2978,
  q="Quel rôle l’État japonais joue-t-il pendant l’ère Meiji (1867-1912) ?",
  opts=["Il se retire de l’économie pour laisser agir le marché",
        "Il fonde les premiers arsenaux, développe les chemins de fer, crée "
        "des usines de soieries et de lainages, investit dans les "
        "infrastructures et organise le démarrage industriel",
        "Il nationalise l’ensemble de l’industrie et interdit "
        "l’investissement privé",
        "Il se limite à protéger les droits de propriété"],
  ans=1,
  why=["C’est l’inverse : l’industrialisation japonaise n’est pas un simple "
       "processus spontané de marché.",
       "Le cours décrit au contraire un transfert d’actifs vers le privé à "
       "partir des années 1880.",
       "Le rôle de l’État est bien plus large qu’une mission de garantie "
       "juridique."],
  exp="Le Japon décolle grâce à un État stratège, très actif dans la phase "
      "initiale du rattrapage. Il investit aussi massivement dans le capital "
      "humain : accueil d’experts étrangers, importation de savoirs "
      "techniques, envoi d’étudiants japonais à l’étranger. Puis, à partir des "
      "années 1880, il privatise une partie des activités, ce qui permet la "
      "montée de groupes privés puissants.",
  diss="La séquence est remarquable : impulsion publique d’abord, relais du "
       "privé ensuite. C’est un argument fort pour discuter le rôle de l’État "
       "dans le rattrapage."),

f(id='q7-n65', sp='c7-15', niv='raisonner', type='qcmm', b=3013,
  q="Quels angles morts le cours relève-t-il dans le modèle du vol d’oies "
    "sauvages ? (plusieurs réponses)",
  opts=["Le rôle décisif de l’État japonais — protectionnisme, contrôle du "
        "système financier, encadrement du crédit",
        "Le rôle des conglomérats, les zaibatsu, qui concentrent les capitaux "
        "et coordonnent les investissements",
        "La dimension coloniale et impériale : Corée, Taïwan, puis Mandchourie",
        "Les transferts technologiques américains et l’ouverture du marché "
        "américain à partir des années 1950",
        "L’absence totale de montée en gamme dans les faits"],
  ans=[0, 1, 2, 3],
  why=["Exacte : le marché seul n’explique pas la trajectoire japonaise.",
       "Exacte : un conglomérat réunit banque, industrie, commerce, "
       "transport au sein d’un même groupe.",
       "Exacte : certains débouchés et ressources ont été obtenus dans un "
       "cadre de domination impériale.",
       "Exacte : le soutien extérieur est trop peu internalisé par le modèle.",
       "La montée en gamme est au contraire parfaitement documentée : c’est "
       "le cœur du modèle."],
  exp="Le modèle peut donner l’image d’un développement presque naturel, "
      "fluide et harmonieux. Le cours corrige : il reste à nuancer par les "
      "rapports de puissance. Deux enseignements théoriques subsistent "
      "néanmoins — le développement peut être séquencé et non linéaire, et "
      "l’on peut combiner protection initiale et ouverture ultérieure.",
  diss="Signaler ces angles morts, c’est montrer qu’on ne confond pas un "
       "modèle avec une histoire : exactement ce qu’attend un correcteur d’un "
       "usage critique des références."),

# ----------------------------------------- c7-16 la stratégie chinoise
f(id='q7-n66', sp='c7-16', niv='comprendre', type='qcm', b=3128,
  q="Qu’appelle-t-on, à partir du tournant de Deng Xiaoping, l’« économie "
    "socialiste de marché » ?",
  opts=["Un modèle purement libéral, assorti d’un régime démocratique",
        "Une ouverture économique qui conserve la planification, une forte "
        "intervention de l’État et le contrôle politique du PCC",
        "Une économie planifiée intégralement, fermée au commerce mondial",
        "Un système de cogestion entre entreprises publiques et syndicats"],
  ans=1,
  why=["La Chine ne choisit pas un modèle libéral et le régime reste "
       "autoritaire.",
       "La Chine s’ouvre au contraire au commerce mondial, de façon "
       "progressive et encadrée.",
       "Aucun mécanisme de cogestion n’est décrit."],
  exp="La formule à retenir est : ouverture économique n’est pas retrait "
      "politique de l’État. Les premières réformes portent sur l’agriculture, "
      "la gestion des entreprises publiques et la création des zones "
      "économiques spéciales, qui permettent d’attirer les capitaux, de "
      "favoriser les investissements étrangers, d’organiser des transferts de "
      "technologie et de lancer une remontée de filière.",
  diss="Les ZES sont le symbole de la méthode chinoise : s’ouvrir par "
       "morceaux, dans des espaces ciblés, pour apprendre et monter "
       "progressivement en gamme."),

f(id='q7-n67', sp='c7-16', niv='connaitre', type='qcm', b=3170,
  q="Quels repères le cours retient-il pour la phase de croissance "
    "extravertie chinoise ?",
  opts=["Entrée à l’OMC en 2001, exportations principal moteur jusqu’en 2009, "
        "croissance d’environ 10 % par an entre 1980 et 2010",
        "Entrée à l’OMC en 1995, croissance de 6 % par an depuis 1990",
        "Entrée à l’OMC en 2001, croissance de 5 % par an depuis 1980",
        "Entrée à l’OMC en 2008, exportations principal moteur depuis"],
  ans=0,
  why=["L’OMC est créée en 1995 mais la Chine y entre en 2001, et le rythme "
       "retenu est bien plus élevé.",
       "Le rythme de croissance est très sous-estimé.",
       "La date d’adhésion est inexacte."],
  exp="L’entrée à l’OMC en 2001 accélère l’intégration de la Chine aux "
      "chaînes de valeur mondiales, sa spécialisation manufacturière et son "
      "rôle d’« atelier du monde ». Les exportations sont le principal moteur "
      "de la croissance jusqu’en 2009.",
  diss="Attention à la chronologie des dirigeants : Deng pour le tournant, "
       "Jiang Zemin (1989-2002) et Hu Jintao (2002-2012) pour l’insertion "
       "mondiale."),

f(id='q7-n68', sp='c7-16', niv='raisonner', type='qcm', b=3180,
  q="Que révèle la crise de 2008 sur le modèle de croissance chinois ?",
  opts=["Que la Chine n’était pas intégrée aux chaînes de valeur mondiales",
        "Un essoufflement du modèle exportateur, avec un capital par "
        "travailleur encore faible et une productivité du travail inférieure "
        "à celle des États-Unis, d’où un recentrage sur la demande intérieure",
        "Que la planification avait disparu",
        "Que la Chine devait abandonner l’industrie au profit des services"],
  ans=1,
  why=["Son intégration était au contraire très forte, ce qui explique "
       "l’exposition au choc.",
       "La planification n’a jamais vraiment disparu en Chine : elle "
       "redevient simplement plus visible après 2013.",
       "Le cours décrit une montée en gamme industrielle, non un abandon de "
       "l’industrie."],
  exp="La Chine a beaucoup accumulé, mais elle doit encore monter en "
      "productivité et en sophistication technologique. Le modèle purement "
      "tiré par les exportations devient insuffisant : il faut rééquilibrer la "
      "croissance vers le marché intérieur.",
  diss="À relier au 15ᵉ plan (2025-2030), qui vise une hausse de la "
       "consommation des ménages jusqu’à 45 % du PIB."),

f(id='q7-n69', sp='c7-16', niv='connaitre', type='assoc', b=3206,
  q="Associez chaque plan quinquennal chinois à sa priorité.",
  ans=[["13ᵉ plan (2016-2020)", "Mise en place de la BRI et poursuite de la stratégie d’industrialisation"],
       ["14ᵉ plan (2020-2025)", "Croissance tirée vers une innovation verte et inclusive, intégration internationale renforcée"],
       ["15ᵉ plan (2025-2030)", "Autosuffisance technologique, priorité aux semi-conducteurs et à l’IA, consommation des ménages portée vers 45 % du PIB"]],
  exp="À partir de 2013, la planification redevient plus visible : non pas "
      "comme administration de l’économie, mais comme feuille de route "
      "stratégique, organisation de long terme et priorisation des secteurs "
      "clés. La Chine ne vise plus seulement la croissance quantitative, mais "
      "la souveraineté technologique.",
  diss="Cette évolution est l’illustration parfaite d’un passage d’une "
       "logique de rattrapage à une logique de leadership."),

f(id='q7-n70', sp='c7-16', niv='comprendre', type='qcm', b=3220,
  q="Que recouvre la Belt and Road Initiative, lancée en 2013 ?",
  opts=["Un programme d’aide au développement de l’ONU",
        "Un projet d’infrastructures maritimes, terrestres, digitales et "
        "parfois aériennes, assorti d’une coordination des politiques de "
        "développement et d’une intégration financière autour du renminbi",
        "Un accord commercial régional signé avec l’ASEAN",
        "Un plan de relance intérieure après la crise de 2008"],
  ans=1,
  why=["Il s’agit d’une initiative chinoise, non onusienne.",
       "La BRI n’est pas un accord commercial mais un projet "
       "d’infrastructures et de coordination.",
       "Elle est tournée vers l’extérieur, non vers la relance intérieure."],
  exp="Annoncée officiellement à Pékin en 2017, la BRI a pour horizon "
      "symbolique 2049, centenaire de la République populaire : les autorités "
      "se donnent environ trente-cinq ans. Elle réactive une référence "
      "historique pour légitimer un projet contemporain de projection de "
      "puissance, et sert aussi à diffuser l’usage du renminbi pour réduire à "
      "long terme la dépendance au dollar.",
  diss="La BRI est l’exemple le plus net d’une stratégie où développement, "
       "commerce, monnaie et géopolitique sont indissociables."),

f(id='q7-n71', sp='c7-16', niv='appliquer', type='qcmm', b=3271,
  q="Quelles positions la Chine occupe-t-elle dans les industries de la "
    "transition énergétique, selon Guillaume Pitron ? (plusieurs réponses)",
  opts=["Premier producteur de 33 des 51 ressources minérales indispensables "
        "aux économies",
        "Premier fabricant de produits photovoltaïques",
        "Premier investisseur dans l’éolien onshore et offshore",
        "Premier producteur de voitures électriques",
        "Premier producteur de semi-conducteurs les plus avancés"],
  ans=[0, 1, 2, 3],
  why=["Exacte : métaux critiques et terres rares, utiles aux téléphones, à "
       "l’automobile, aux batteries, au numérique et à la défense.",
       "Exacte : avec une place très forte dans la capacité solaire "
       "installée.",
       "Exacte : le cours le précise explicitement.",
       "Exacte : avec des constructeurs comme BYD, Chery et Geely.",
       "C’est précisément la faiblesse chinoise : les puces inférieures à "
       "7 nanomètres, d’où la priorité récente à l’autosuffisance "
       "technologique."],
  exp="L’ouvrage de référence est « La guerre des métaux rares » (2023). Le "
      "cours ajoute une nuance importante sur le solaire : les renouvelables "
      "s’ajoutent au charbon, elles ne le remplacent pas totalement.",
  diss="La maîtrise quasi complète des chaînes de valeur, batteries incluses, "
       "avec un point de vulnérabilité sur les semi-conducteurs avancés : "
       "c’est ce qui explique l’enjeu taïwanais."),

f(id='q7-n72', sp='c7-16', niv='raisonner', type='qcmm', b=3340,
  q="Quelles fragilités le cours relève-t-il dans la puissance chinoise ? "
    "(plusieurs réponses)",
  opts=["Le vieillissement de la population et la contrainte sur la "
        "main-d’œuvre",
        "Un endettement élevé et des vulnérabilités financières",
        "Des surcapacités de production supérieures à la demande solvable",
        "Un coût environnemental très élevé : 19 % du PIB mondial en PPA mais "
        "31 % des émissions mondiales de GES",
        "L’absence de planification stratégique"],
  ans=[0, 1, 2, 3],
  why=["Exacte : le ralentissement démographique pèsera sur la croissance "
       "future.",
       "Exacte : le poids de la dette est explicitement cité.",
       "Exacte : d’où un risque de déséquilibres internes.",
       "Exacte : c’est le décalage le plus frappant entre puissance "
       "économique et coût écologique.",
       "La planification est au contraire renforcée depuis 2013."],
  exp="Deux autres limites sont citées : l’opacité financière, qui rend les "
      "risques difficiles à évaluer, et la limite monétaire — le renminbi "
      "progresse mais reste loin derrière le dollar dans les réserves de "
      "change. Le cours ajoute une interrogation institutionnelle, en "
      "mobilisant Acemoglu : des institutions extractives peuvent-elles, à "
      "terme, freiner le développement ?",
  diss="Conclusion attendue : la puissance chinoise est réelle mais "
       "ambivalente — performances industrielles et géopolitiques d’un côté, "
       "fragilités structurelles de l’autre."),

f(id='q7-n73', sp='c7-16', niv='raisonner', type='courte', b=3377,
  q="Résumez en trois étapes la logique d’ensemble de la stratégie chinoise.",
  ans={'modele': "D’abord une modernisation planifiée et encadrée : à partir "
       "de la fin des années 1970, Deng Xiaoping instaure une « économie "
       "socialiste de marché », réforme l’agriculture et les entreprises "
       "publiques, et ouvre sélectivement par les zones économiques spéciales, "
       "organisant transferts de technologie et remontée de filière. Ensuite "
       "une croissance extravertie : dans les années 1990-2000, les "
       "exportations deviennent le moteur, l’entrée à l’OMC en 2001 fait de la "
       "Chine l’« atelier du monde ». Enfin, après la crise de 2008 et surtout "
       "depuis 2013, un recentrage stratégique : demande intérieure, "
       "innovation, souveraineté technologique, planification de long terme et "
       "projection de puissance par la BRI.",
       'cles': [{'f': ['deng', 'socialiste de marche', 'zes', 'planifi'],
                 'l': 'une modernisation planifiée et une ouverture encadrée'},
                {'f': ['export', 'omc', '2001', 'atelier du monde', 'extravert'],
                 'l': 'une croissance extravertie, tirée par les exportations'},
                {'f': ['2008', 'demande interieure', 'innovation', 'souverainete', 'bri'],
                 'l': 'puis un recentrage sur l’innovation et la souveraineté'}]},
  exp="Le modèle chinois est donc hybride : il ne relève ni de l’ISI pure ni "
      "de la promotion des exportations pure, mais combine les deux dans une "
      "séquence pilotée par l’État — ce qui le rapproche, en le modifiant, du "
      "modèle du vol d’oies sauvages."),

# -------------------------------- c7-17 soutenabilité, climat, finance
f(id='q7-n74', sp='c7-17', niv='comprendre', type='qcm', b=3442,
  q="Pourquoi l’IDH classique surestime-t-il parfois la performance des pays "
    "développés ?",
  opts=["Parce qu’il surpondère le revenu par rapport à la santé",
        "Parce qu’il ne mesure ni les émissions de GES, ni la pression sur "
        "les ressources, ni l’empreinte écologique incorporée dans les "
        "importations",
        "Parce qu’il ignore les inégalités internes",
        "Parce qu’il repose sur des données déclaratives"],
  ans=1,
  why=["La pondération des dimensions n’est pas l’argument retenu ici.",
       "L’omission des inégalités internes est bien une limite de l’IDH, mais "
       "c’est celle que corrige l’IDHI, non l’IDHP.",
       "La qualité des données n’est pas mise en cause."],
  exp="Un pays peut apparaître performant en développement humain tout en "
      "produisant à l’étranger, en important des biens fortement polluants et "
      "en affichant une production nationale apparemment propre : une partie "
      "de la pollution est externalisée. C’est précisément cette limite que "
      "l’IDHP, créé en 2020, vient corriger.",
  diss="Lecture de l’indicateur : si l’IDHP est proche de l’IDH, la pression "
       "écologique est faible ; plus l’écart est grand, plus le développement "
       "repose sur un mode de croissance coûteux pour la planète."),

f(id='q7-n75', sp='c7-17', niv='raisonner', type='qcm', b=3471,
  q="Quelle double asymétrie le changement climatique révèle-t-il ?",
  opts=["Les pays riches polluent peu et subissent beaucoup ; les pays "
        "pauvres polluent beaucoup et subissent peu",
        "Les pays développés sont historiquement les plus responsables des "
        "dégradations, mais les pays les moins développés en subissent les "
        "effets les plus violents avec une plus faible capacité d’adaptation",
        "Les deux groupes de pays sont également responsables et également "
        "exposés",
        "Les pays émergents sont les plus responsables et les plus exposés"],
  ans=1,
  why=["Les deux termes sont inversés.",
       "C’est précisément ce que le cours récuse : responsabilités et "
       "vulnérabilités sont inégales.",
       "Le cours n’attribue pas cette double position aux pays émergents."],
  exp="Les pays à faible empreinte écologique sont souvent ceux qui subissent "
      "le plus fortement canicules, inondations et chocs climatiques. Ce "
      "paradoxe fonde l’idée de justice climatique, de responsabilité "
      "historique et de financement climatique par les pays développés.",
  diss="C’est le fondement du principe de responsabilités communes mais "
       "différenciées, par lequel le chapitre s’ouvre à propos de la Chine : "
       "la boucle se referme."),

f(id='q7-n76', sp='c7-17', niv='comprendre', type='qcm', b=3494,
  q="Comment le cours applique-t-il la tragédie des communs de Hardin (1968) "
    "au climat ?",
  opts=["Le climat est un bien privé dont il faut définir le propriétaire",
        "Le climat est un bien commun mondial : sans coordination "
        "internationale apparaissent des comportements de passager "
        "clandestin, un sous-investissement collectif et une surexploitation "
        "des ressources planétaires",
        "Le climat est un bien public local, géré par les États",
        "Le climat échappe à toute analyse économique"],
  ans=1,
  why=["Le climat n’est précisément pas appropriable : c’est ce qui fait le "
       "problème.",
       "Sa dimension est mondiale, non locale : aucun État ne peut le gérer "
       "seul.",
       "Le cours en fait au contraire un objet central de l’analyse "
       "économique."],
  exp="C’est la première étape de la montée en puissance de la question "
      "écologique dans le chapitre : Hardin (1968), puis le rapport Meadows "
      "(1972), le rapport Brundtland (1987) et la création du GIEC (1988). "
      "L’analyse en termes de bien commun explique pourquoi la gouvernance "
      "mondiale devient nécessaire — et pourquoi elle est si difficile.",
  diss="Le cours note aussi, en fin de chapitre, qu’Ostrom est précieuse pour "
       "penser la gouvernance des communs, mais que ses mécanismes sont plus "
       "difficiles à appliquer aux biens communs mondiaux."),

f(id='q7-n77', sp='c7-17', niv='appliquer', type='qcm', b=3575,
  q="L’intensité carbone de l’énergie diminue et l’efficacité énergétique "
    "s’améliore, mais les émissions continuent d’augmenter. Comment "
    "l’identité de Kaya explique-t-elle ce paradoxe ?",
  opts=["Les mesures d’émissions sont biaisées",
        "Les progrès sur les deux premiers facteurs sont compensés par la "
        "hausse du niveau de vie et celle de la population",
        "L’intensité carbone n’a en réalité pas diminué",
        "Les émissions sont désormais toutes externalisées"],
  ans=1,
  why=["Le cours ne met pas en cause la mesure des émissions.",
       "La baisse de l’intensité carbone est au contraire le point de départ "
       "du paradoxe.",
       "L’externalisation est une autre critique, adressée aux comparaisons "
       "nationales."],
  exp="Les quatre facteurs de Kaya sont l’intensité carbone de l’énergie, "
      "l’intensité énergétique de la production, le PIB par habitant et la "
      "population. On produit parfois plus efficacement, avec des énergies un "
      "peu moins carbonées, mais on produit et on consomme beaucoup plus. Le "
      "GIEC a utilisé cette logique pour montrer que les gains techniques ne "
      "suffisent pas.",
  diss="C’est le meilleur argument pour montrer que l’efficacité technique "
       "seule ne résout pas le problème climatique : il faut aussi agir sur "
       "les volumes."),

f(id='q7-n78', sp='c7-17', niv='comprendre', type='assoc', b=3604,
  q="Associez chacun des trois risques climatiques de Mark Carney à son "
    "contenu.",
  ans=[["Les risques physiques", "Dommages directs — inondations, incendies, canicules, tempêtes — destruction ou dévalorisation d’actifs, hausse des coûts d’assurance"],
       ["Les risques de responsabilité", "Mises en cause juridiques d’entreprises, banques, investisseurs ou assureurs pour avoir financé des activités polluantes ou tardé à agir"],
       ["Les risques de transition", "Dévalorisation des activités fossiles sous l’effet des normes, taxes et innovations : les actifs échoués"]],
  exp="Le cours souligne un point souvent manqué : un actif peut perdre de la "
      "valeur sans être détruit, simplement parce qu’il devient risqué ou "
      "invendable — un bien immobilier en zone inondable par exemple — ce qui "
      "réduit aussi la capacité d’endettement des ménages et des entreprises. "
      "Les actifs échoués sont des actifs encore existants mais devenus "
      "économiquement obsolètes.",
  diss="Avec Carney, le climat devient un enjeu de stabilité financière : "
       "c’est la référence qui permet de relier environnement et finance dans "
       "une copie."),

# -------------------- c7-18 gouvernance, instruments, échelles d’action
f(id='q7-n79', sp='c7-18', niv='connaitre', type='qcm', b=3725,
  q="Quel est l’objet du traité sur la haute mer ?",
  opts=["Fixer les limites des zones économiques exclusives",
        "Protéger les espaces marins situés au-delà des ZEE : protéger la "
        "biodiversité marine, créer des aires marines protégées, mieux "
        "encadrer l’exploitation des ressources océaniques",
        "Interdire la pêche industrielle dans les eaux territoriales",
        "Organiser le partage des ressources minières sous-marines entre "
        "États côtiers"],
  ans=1,
  why=["Les ZEE préexistent au traité : elles vont jusqu’à environ "
       "200 milles nautiques, soit à peu près 370 km des côtes.",
       "Le traité ne porte pas sur les eaux territoriales mais sur la haute "
       "mer.",
       "Il ne s’agit pas d’un partage entre États côtiers mais de la "
       "protection d’un espace commun."],
  exp="La haute mer représentait en grande partie un espace peu régulé, un "
      "quasi espace de non-droit. Signé en 2023, le traité est un exemple "
      "concret de protection d’un bien commun mondial — son entrée en vigueur "
      "dépendant d’un nombre suffisant de ratifications.",
  diss="Exemple à mobiliser pour illustrer la gouvernance mondiale du climat "
       "et de l’environnement, à côté de Kyoto et de Paris."),

f(id='q7-n80', sp='c7-18', niv='raisonner', type='qcm', b=3755,
  q="Quelle limite majeure le cours assigne-t-il au marché du carbone ?",
  opts=["Il n’existe pas encore à l’échelle européenne",
        "Le prix du carbone est souvent trop faible et trop volatil : autour "
        "de 80 € la tonne, jugé insuffisant, quand certains économistes "
        "estiment qu’il faudrait plutôt 140 €",
        "Il taxe deux fois les mêmes émissions",
        "Il ne concerne que les ménages"],
  ans=1,
  why=["Le marché existe et fonctionne : c’est son niveau de prix qui est en "
       "cause.",
       "Il n’y a pas de double imposition dans ce dispositif.",
       "Il porte au contraire sur les émetteurs industriels."],
  exp="Le marché du carbone doit donner un signal-prix, faire payer la "
      "pollution et inciter à réduire les émissions. Mais il n’est efficace "
      "que si le prix est assez élevé et stable. Le cours conclut : "
      "l’instrument est pertinent, son calibrage insuffisant.",
  diss="Ce constat prépare la question de l’instrument : marché ou règle ? "
       "Et il rejoint le débat Pigou — taxer les externalités — dont le cours "
       "souligne qu’une taxe peut être socialement régressive."),

f(id='q7-n81', sp='c7-18', niv='raisonner', type='assoc', b=3763,
  q="Associez chaque logique de gouvernance climatique à ses avantages et à "
    "ses limites.",
  ans=[["Top-down : avantages", "Plus de contrainte, meilleure coordination, plus de cohérence collective"],
       ["Top-down : limites", "Refus d’obéissance, faible adhésion, contournements"],
       ["Bottom-up : avantages", "Meilleure appropriation, engagement plus acceptable, logique plus souple"],
       ["Bottom-up : limites", "Efforts insuffisants, passager clandestin, manque de contrainte, coordination difficile"]],
  exp="Le cours conclut que ni Kyoto ni Paris n’ont totalement résolu le "
      "problème de l’action collective mondiale : la contrainte sans adhésion "
      "échoue, l’adhésion sans contrainte ne suffit pas. C’est précisément ce "
      "qui justifie de compléter la gouvernance mondiale par des initiatives "
      "locales et microéconomiques.",
  diss="Opposition très rentable : elle permet de traiter la gouvernance "
       "climatique comme un problème d’action collective, et non comme une "
       "question de volonté politique."),

f(id='q7-n82', sp='c7-18', niv='appliquer', type='qcmm', b=3792,
  q="En quoi la démarche de Veja illustre-t-elle une action microéconomique "
    "pour le développement durable ? (plusieurs réponses)",
  opts=["Un approvisionnement au Brésil auprès de petits producteurs, payés "
        "au-dessus du prix de marché, avec des revenus garantis",
        "Le respect des conditions de travail et un paiement anticipé d’une "
        "partie de la production",
        "Une logique environnementale sur toute la chaîne de valeur : "
        "transport par porte-conteneurs plutôt que par avion, ateliers "
        "d’insertion",
        "Des ateliers de réparation allongeant la durée de vie des produits, "
        "dans une logique d’économie circulaire",
        "Un modèle désormais dominant dans l’industrie de la chaussure"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est une logique de commerce équitable.",
       "Exacte : le paiement anticipé sécurise le revenu des producteurs.",
       "Exacte : l’entreprise agit sur matières premières, production, "
       "transport, distribution et financement.",
       "Exacte : réparation, réemploi, recyclage, allongement de la durée de "
       "vie.",
       "Le cours relève l’inverse : la démarche reste marginale à l’échelle "
       "macroéconomique, initiative vertueuse mais impact global limité."],
  exp="Le cours relie explicitement cette démarche aux théories de la "
      "dépendance : Prebisch, la CEPAL, les échanges inégaux d’Arghiri "
      "Emmanuel et de Samir Amin. Veja apparaît comme une tentative de "
      "corriger, à l’échelle d’une entreprise, les asymétries que ces auteurs "
      "dénonçaient.",
  diss="Ce lien théorie-pratique est précieux : il permet de mobiliser une "
       "référence contemporaine concrète sans quitter le cadre analytique du "
       "chapitre."),

f(id='q7-n83', sp='c7-18', niv='raisonner', type='qcm', b=3940,
  q="Que montre l’épisode des Gilets jaunes (2018-2019) sur les politiques "
    "climatiques ?",
  opts=["Que la taxation du carbone est économiquement inefficace",
        "Que l’efficacité écologique d’un instrument ne garantit pas son "
        "acceptabilité sociale : une taxe peut être régressive",
        "Que les ménages ne sont pas sensibles aux prix de l’énergie",
        "Que la transition écologique est impossible en démocratie"],
  ans=1,
  why=["L’instrument est au contraire fondé théoriquement, par Pigou : son "
       "problème est social, non analytique.",
       "C’est l’inverse : la contestation est née précisément de la "
       "sensibilité des ménages dépendants de la voiture.",
       "Le cours ne tire pas cette conclusion : il appelle à concilier les "
       "objectifs."],
  exp="La hausse de la fiscalité carbone sur les carburants a été contestée "
      "par des ménages dépendants de la voiture, avec le slogan « fin du mois "
      "ou fin du monde ». La référence théorique est Pigou — taxer les "
      "externalités négatives — mais socialement, la taxe peut peser "
      "davantage sur les bas revenus.",
  diss="Le cours cite aussi Pierre Charbonnier : les impératifs économiques "
       "et écologiques entrent souvent en collision. C’est l’argument central "
       "d’une troisième partie sur les tensions entre objectifs."),

f(id='q7-n84', sp='c7-18', niv='comprendre', type='qcm', b=3969,
  q="Qu’est-ce que le mécanisme d’ajustement carbone aux frontières (CBAM / "
    "MACF) et à quoi répond-il ?",
  opts=["Une taxe sur les exportations européennes vers les pays émergents",
        "Une taxation des importations venant de pays moins exigeants "
        "écologiquement, afin d’éviter les distorsions de concurrence, de "
        "protéger les producteurs européens et de limiter le dumping "
        "environnemental",
        "Une subvention aux industries européennes décarbonées",
        "Un quota d’importation de produits fortement carbonés"],
  ans=1,
  why=["Le mécanisme porte sur les importations, non sur les exportations.",
       "Il ne s’agit pas d’une subvention mais d’un ajustement à la "
       "frontière.",
       "Ce n’est pas un quota quantitatif mais un dispositif de prix."],
  exp="La « compétitivité écologique » paraît d’abord un oxymore : le "
      "commerce cherche des débouchés, de la compétitivité et des coûts bas, "
      "tandis que les politiques climatiques cherchent à réduire l’empreinte "
      "carbone, relocaliser et limiter les transports longs. Le CBAM tente de "
      "réconcilier les deux en neutralisant l’avantage des producteurs "
      "moins-disants.",
  diss="À relier au devoir de vigilance : les deux dispositifs posent la même "
       "question — l’Europe doit-elle montrer l’exemple au risque de pénaliser "
       "ses producteurs ?"),

f(id='q7-n85', sp='c7-18', niv='raisonner', type='qcm', b=3990,
  q="Quel exemple le cours donne-t-il du contournement d’une règle "
    "environnementale, et quelle leçon en tire-t-il ?",
  opts=["La taxe carbone européenne, contournée par les entreprises "
        "américaines",
        "La taxe sur les colis aériens en France : les entreprises livrent "
        "dans un autre pays européen puis transportent par la route, ce qui "
        "fait baisser le fret aérien direct sans réduire les flux réels",
        "L’interdiction des sacs plastiques, contournée par les importations",
        "Le marché des quotas, contourné par les achats de crédits étrangers"],
  ans=1,
  why=["Le cours ne donne pas cet exemple.",
       "Les sacs plastiques ne sont pas mentionnés.",
       "Les crédits internationaux sont un débat distinct."],
  exp="La leçon est générale : une règle isolée à petite échelle peut être "
      "inefficace si les acteurs disposent d’arbitrages spatiaux et "
      "logistiques pour la contourner. D’où la question de l’échelle "
      "pertinente de la régulation — plus l’échelle est étroite, plus le "
      "risque de contournement est élevé ; plus elle est large, plus la "
      "coordination politique devient difficile.",
  diss="Ce dilemme d’échelle est la conclusion la plus solide d’un sujet sur "
       "les instruments de la transition écologique."),

f(id='q7-n86', sp='c7-18', niv='comprendre', type='qcmm', b=3918,
  q="À quelles échelles l’action en faveur du développement durable se "
    "déploie-t-elle, selon le cours ? (plusieurs réponses)",
  opts=["International : ONU, COP, accords climatiques",
        "Régional : Union européenne, Green Deal",
        "National et local",
        "Microéconomique : entreprises, et individuel : comportements, "
        "sobriété",
        "Exclusivement international, les autres échelles étant inefficaces"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est l’échelle de la gouvernance mondiale.",
       "Exacte : l’Union européenne est l’échelon régional cité.",
       "Exacte : les deux figurent dans l’énumération du cours.",
       "Exacte : Veja pour le microéconomique, la sobriété pour "
       "l’individuel.",
       "Le cours affirme l’inverse : aucune échelle ne suffit à elle seule."],
  exp="Le cours nuance l’échelle individuelle : ne pas laisser couler l’eau, "
      "raccourcir les douches, adopter des comportements plus sobres sont des "
      "gestes utiles pour sensibiliser, mais ils représentent une part "
      "limitée des grands déséquilibres. La responsabilisation individuelle "
      "est nécessaire, mais elle ne peut masquer le poids décisif des "
      "infrastructures, des modes de production et des politiques publiques.",
  diss="La sobriété est définie comme la réduction volontaire de certaines "
       "consommations afin de limiter les pressions environnementales sans "
       "diminuer le bien-être essentiel."),

f(id='q7-n87', sp='c7-18', niv='raisonner', type='qcm', b=4021,
  q="Quelle extension du droit le cours évoque-t-il à propos des biens "
    "communs naturels ?",
  opts=["La création d’un tribunal international du climat",
        "La reconnaissance d’une personnalité juridique à certains biens "
        "communs naturels, qui permettrait à des associations d’agir en "
        "justice au nom de la nature",
        "L’interdiction constitutionnelle de toute activité polluante",
        "L’obligation pour les États de racheter les actifs échoués"],
  ans=1,
  why=["Aucune juridiction climatique internationale n’est évoquée.",
       "Le cours ne mentionne aucune interdiction constitutionnelle "
       "générale.",
       "Le rachat des actifs échoués n’est pas discuté."],
  exp="La référence citée est Juliette Rochefeld, « Justice pour le climat » "
      "(2020). Le cours relie cette question à la judiciarisation croissante "
      "de l’économie : avec le devoir de vigilance, les grandes entreprises "
      "doivent surveiller leurs chaînes de valeur, anticiper les atteintes "
      "aux droits humains et à l’environnement, et rendre des comptes.",
  diss="Le débat est explicitement ambivalent : responsabiliser les firmes, "
       "ou pénaliser surtout les entreprises européennes ? Le cours laisse la "
       "question ouverte, et c’est ainsi qu’il faut la traiter."),

f(id='q7-n88', sp='c7-18', niv='connaitre', type='qcm', b=4040,
  q="Que désigne l’anthropocène ?",
  opts=["La période de forte croissance démographique après 1950",
        "Une ère où l’influence de l’être humain sur la biosphère devient une "
        "force géologique majeure, provoquant changement climatique, perte de "
        "biodiversité et dégradation des écosystèmes",
        "L’étude de l’empreinte écologique par habitant",
        "La phase de transition énergétique vers les renouvelables"],
  ans=1,
  why=["L’explosion démographique est un phénomène distinct, même s’il "
       "contribue à la pression écologique.",
       "L’empreinte écologique est un indicateur, non une ère géologique.",
       "La transition énergétique est une politique, non une périodisation "
       "géologique."],
  exp="Le terme désigne une ère où les activités humaines menacent la survie "
      "de la planète à long terme et celle de l’espèce humaine. Il prend tout "
      "son sens à côté des chiffres de l’empreinte écologique : environ "
      "2,5 hectares par personne aujourd’hui contre 0,6 en 1960, pour une "
      "biocapacité de 1,6 hectare.",
  diss="Notion utile en ouverture ou en conclusion : elle donne une échelle "
       "géologique à un raisonnement économique."),
]

from qz07n1 import L as _M1

NEW = NEW + _M1
