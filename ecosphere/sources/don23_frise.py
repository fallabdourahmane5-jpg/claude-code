# -*- coding: utf-8 -*-
"""Frise chronologique : items du chapitre 3 de deuxieme annee.

NOUVEAUX : items ajoutes. Aucun auteur n'est date lorsque le document de cours
ne fournit qu'une initiale et que la date de naissance n'est pas etablie : dans
ce cas seule la publication, dont l'annee est certaine, est portee sur la frise.
MAJ : items deja presents auxquels le chapitre 23 est ajoute.
"""

MAJ = {
 # auteurs
 'a195': "Adam Smith", 'a196': "David Ricardo", 'a358': "Friedrich List",
 'a199': "Karl Marx", 'a255': "Ernst Engel", 'a344': "Alfred Marshall",
 'a333': "Vilfredo Pareto", 'a209': "John Maynard Keynes",
 'a345': "Edward Chamberlin", 'a277': "Raúl Prebisch", 'a233': "Nicholas Kaldor",
 'a280': "Arghiri Emmanuel", 'a211': "Paul Samuelson", 'a281': "Paul Bairoch",
 'a279': "Samir Amin", 'a243': "Branko Milanovic", 'a323': "Paul Krugman",
 'a244': "Dani Rodrik",
 # ouvrages
 'o065': "Richesse des nations", 'o066': "Principes de Ricardo",
 'o183': "Principes de Marshall", 'o174': "Manuel de Pareto",
 'o143': "L’échange inégal", 'o144': "Mythes et paradoxes de l’histoire économique",
 # theories, periodes, evenements
 'f053': "Protectionnisme éducateur", 'f055': "Concurrence monopolistique",
 'f062': "Courbe environnementale de Kuznets", 'f001': "Première mondialisation",
 'f003': "Entre-deux-guerres et démondialisation", 'f006': "Hypermondialisation",
 'f020': "Tarif Hawley-Smoot",
}

M = "Mondialisation"
NOUVEAUX = []


def it(idn, type_, an, titre, resume, portee, fam, courant=M,
       auteur=None, fin=None, vivant=None, oeuvres=None):
    d = {'id': 'c23_' + idn, 'type': type_, 'an': an, 'titre': titre,
         'resume': resume, 'portee': portee, 'courant': courant,
         'ch': [23], 'fam': fam}
    if auteur:
        d['auteur'] = auteur
    if fin is not None:
        d['fin'] = fin
    if vivant is not None:
        d['vivant'] = vivant
    if oeuvres:
        d['oeuvres'] = oeuvres
    NOUVEAUX.append(d)


# ------------------------------------------------------------------ auteurs
it('a01', 'auteur', 1755, "Alexander Hamilton",
   "Formule avant List l’argument des industries naissantes dans une économie en rattrapage.",
   "Hamilton établit qu’une manufacture nouvelle ne peut affronter d’emblée des concurrents déjà établis.",
   'classique', "Protectionnisme éducateur", auteur="Alexander Hamilton",
   fin=1804, vivant=False, oeuvres=["Rapport sur les manufactures (fin du XVIIIe siècle)"])
it('a02', 'auteur', 1806, "John Stuart Mill",
   "Détermine les bornes du prix international entre lesquelles l’échange reste accepté par les deux pays.",
   "Mill complète Ricardo sur le partage du gain : c’est la position du prix international qui décide qui gagne le plus.",
   'classique', "Classique", auteur="John Stuart Mill", fin=1873, vivant=False,
   oeuvres=["Principes d’économie politique (1848)"])
it('a03', 'auteur', 1870, "Lénine",
   "Analyse l’impérialisme comme stade du capitalisme : monopoles, exportations de capitaux, partage du monde.",
   "Chez Lénine, l’internationalisation est d’abord financière et territoriale avant d’être commerciale.",
   'marxiste', "Marxiste", auteur="Lénine", fin=1924, vivant=False,
   oeuvres=["L’Impérialisme, stade suprême du capitalisme (1916)"])
it('a04', 'auteur', 1879, "Eli Heckscher",
   "Fonde l’avantage comparatif sur les dotations factorielles plutôt que sur la productivité du travail.",
   "Heckscher déplace la cause du commerce des écarts de productivité vers la structure des dotations.",
   'neoclassique', "Néoclassique", auteur="Eli Heckscher", fin=1952, vivant=False,
   oeuvres=["« The Effects of Foreign Trade on the Distribution of Income » (1919)"])
it('a05', 'auteur', 1899, "Bertil Ohlin",
   "Établit que c’est l’abondance relative des facteurs, et non absolue, qui détermine la spécialisation.",
   "Ohlin transforme l’intuition de Heckscher en théorème en passant par le prix relatif des facteurs.",
   'neoclassique', "Néoclassique", auteur="Bertil Ohlin", fin=1979, vivant=False,
   oeuvres=["Interregional and International Trade (1933)"])
it('a06', 'auteur', 1906, "Wassily Leontief",
   "Confronte le modèle HOS aux données américaines et met au jour le paradoxe qui porte son nom.",
   "Le paradoxe de Leontief oblige à redéfinir les facteurs plutôt qu’à rejeter le raisonnement.",
   'neoclassique', "Analyse input-output", auteur="Wassily Leontief", fin=1999, vivant=False,
   oeuvres=["« Domestic Production and Foreign Trade : The American Capital Position Re-examined » (1953)"])
it('a07', 'auteur', 1912, "Wolfgang Stolper",
   "Montre avec Samuelson que le commerce modifie la rémunération des facteurs et crée des perdants internes.",
   "Le théorème Stolper-Samuelson interdit de conclure du gain agrégé de l’ouverture à son caractère souhaitable.",
   'neoclassique', "Néoclassique", auteur="Wolfgang Stolper", fin=2002, vivant=False,
   oeuvres=["« Protection and Real Wages », avec P. Samuelson (1941)"])
it('a08', 'auteur', 1913, "Raymond Vernon",
   "Décrit le cycle de vie international du produit, de l’innovation à la délocalisation puis à l’importation.",
   "Chez Vernon, ce n’est pas le pays qui perd son avantage : c’est le produit qui change de nature en se banalisant.",
   'mondialisation', "Approche néo-technologique", auteur="Raymond Vernon", fin=1999, vivant=False,
   oeuvres=["« International Investment and International Trade in the Product Cycle », QJE (1966)"])
it('a09', 'auteur', 1934, "Jagdish Bhagwati",
   "Construit le cas de la croissance appauvrissante, où produire plus réduit le bien-être national.",
   "Bhagwati fournit le cas limite le plus net contre une lecture purement optimiste de la spécialisation.",
   'developpement', "Économie internationale", auteur="Jagdish Bhagwati",
   vivant=True, oeuvres=["« Immiserizing Growth: A Geometrical Note », RES (1958)"])
it('a10', 'auteur', 1960, "Alan Krueger",
   "Établit avec Grossman la relation en cloche entre revenu par habitant et pollution.",
   "Le retournement de la courbe environnementale ne se produit pas spontanément : il suppose des institutions.",
   'croissance', "Économie appliquée", auteur="Alan Krueger", fin=2019, vivant=False,
   oeuvres=["Travaux de 1995 avec G. Grossman sur croissance et environnement"])

# ------------------------------------------------------------------ ouvrages
it('o01', 'ouvrage', 1841, "Système national d’économie politique",
   "List systématise le protectionnisme éducateur en trois phases, de l’économie agricole à la maturité industrielle.",
   "La protection n’y est pas une doctrine mais un instrument daté, dont la levée fait partie du dispositif.",
   'mondialisation', "Protectionnisme éducateur", auteur="Friedrich List")
it('o02', 'ouvrage', 1848, "Principes d’économie politique (Mill)",
   "Mill y établit que le prix international doit rester entre les prix relatifs internes des deux pays.",
   "Dans l’exemple ricardien, l’échange n’est accepté que si le prix du vin en drap reste entre 0,88 et 1,2.",
   'classique', "Classique", auteur="John Stuart Mill")
it('o03', 'ouvrage', 1848, "Discours sur le libre-échange",
   "Marx y présente l’ouverture comme la résolution provisoire d’une insuffisance de demande intérieure.",
   "Le libre-échange y devient une nécessité du capital plutôt qu’un bienfait réciproque.",
   'marxiste', "Marxiste", auteur="Karl Marx")
it('o04', 'ouvrage', 1916, "L’Impérialisme, stade suprême du capitalisme",
   "Lénine y énumère cinq caractéristiques : monopoles, fusion banque-industrie, exportations de capitaux, partage des marchés et des territoires.",
   "Le commerce international y devient inséparable des rapports de puissance politique.",
   'marxiste', "Marxiste", auteur="Lénine")
it('o05', 'ouvrage', 1919, "The Effects of Foreign Trade on the Distribution of Income",
   "Heckscher y introduit l’idée que les pays diffèrent par les quantités de facteurs dont ils disposent.",
   "Point de départ du modèle HOS : l’échange naît des dotations, à technologies identiques.",
   'neoclassique', "Néoclassique", auteur="Eli Heckscher")
it('o06', 'ouvrage', 1933, "Interregional and International Trade",
   "Ohlin y montre que l’abondance relative d’un facteur le rend relativement moins cher, donc avantage les productions qui l’utilisent intensivement.",
   "Énoncé achevé du théorème Heckscher-Ohlin et de son mécanisme par les prix relatifs des facteurs.",
   'neoclassique', "Néoclassique", auteur="Bertil Ohlin")
it('o07', 'ouvrage', 1933, "De l’autosuffisance nationale",
   "Keynes y soutient qu’une économie trop dépendante de l’extérieur perd la maîtrise de sa politique économique.",
   "Argument non conjoncturel en faveur d’une limitation de certaines dépendances, distinct de l’argument du multiplicateur.",
   'keynesien', "Keynésien", auteur="John Maynard Keynes")
it('o08', 'ouvrage', 1941, "Protection and Real Wages",
   "Stolper et Samuelson y montrent que l’ouverture augmente la rémunération du facteur abondant et réduit celle du facteur rare.",
   "Référence centrale de toute analyse distributive du libre-échange.",
   'neoclassique', "Néoclassique", auteur="W. Stolper et P. Samuelson")
it('o09', 'ouvrage', 1950, "Le développement économique de l’Amérique latine et ses principaux problèmes",
   "Prebisch y établit la dégradation tendancielle des termes de l’échange des produits primaires sur 1875-1938.",
   "Une spécialisation conforme aux avantages comparatifs peut appauvrir relativement le pays qui s’y conforme.",
   'developpement', "Structuraliste", auteur="Raúl Prebisch")
it('o10', 'ouvrage', 1953, "Domestic Production and Foreign Trade : The American Capital Position Re-examined",
   "Leontief y constate que les exportations américaines sont moins intensives en capital que les biens substituables aux importations.",
   "Origine du paradoxe de Leontief et de l’ouverture du modèle HOS à l’hétérogénéité du travail.",
   'neoclassique', "Analyse input-output", auteur="Wassily Leontief")
it('o11', 'ouvrage', 1955, "Factor Endowment and Relative Commodity Prices",
   "Rybczynski y établit qu’un accroissement de dotation augmente plus que proportionnellement la production du bien intensif en ce facteur.",
   "Les dotations deviennent endogènes : l’avantage comparatif peut être construit par l’accumulation.",
   'neoclassique', "Commerce international", auteur="T. Rybczynski")
it('o12', 'ouvrage', 1958, "« Immiserizing Growth: A Geometrical Note »",
   "Bhagwati y montre qu’une hausse de production peut dégrader le prix mondial au point de réduire le bien-être national.",
   "Cas limite décisif : lorsqu’un pays pèse sur le prix mondial, produire plus peut revenir à gagner moins.",
   'developpement', "Économie internationale", auteur="Jagdish Bhagwati")
it('o13', 'ouvrage', 1961, "« International Trade and Technical Change »",
   "Posner y explique les écarts de productivité par l’innovation, dont l’avantage est temporaire du fait de l’imitation.",
   "L’avantage comparatif dépend du flux d’innovations, et non d’un stock acquis.",
   'mondialisation', "Approche néo-technologique", auteur="M. Posner")
it('o14', 'ouvrage', 1966, "« Labor Skills and Comparative Advantage »",
   "Keesing y fait de la qualification du travail une dotation factorielle à part entière.",
   "Cœur de l’approche néo-factorielle : le modèle HOS est conservé, sa liste de facteurs est enrichie.",
   'neoclassique', "Approche néo-factorielle", auteur="D. Keesing")
it('o15', 'ouvrage', 1966, "« International Investment and International Trade in the Product Cycle »",
   "Vernon y décrit les quatre phases du cycle de vie du produit, de la naissance à l’importation par le pays innovateur.",
   "Articule innovation et délocalisation sans invoquer de perte d’avantage du pays d’origine.",
   'mondialisation', "Approche néo-technologique", auteur="Raymond Vernon")
it('o16', 'ouvrage', 1971, "Travaux sur la structure du commerce extérieur des États-Unis",
   "Baldwin y montre que les exportations américaines sont intensives en travail qualifié et en savoir technologique.",
   "Résout le paradoxe de Leontief en abandonnant l’hypothèse d’un travail homogène.",
   'neoclassique', "Économie internationale empirique", auteur="Robert Baldwin")
it('o17', 'ouvrage', 1979, "« Increasing Returns, Monopolistic Competition, and International Trade »",
   "Krugman y associe concurrence monopolistique et rendements croissants : l’ouverture est profitable même entre pays identiques.",
   "Trois gains en découlent : sélection par la concurrence, variété disponible, effet de dimension.",
   'mondialisation', "Nouvelle économie géographique", auteur="Paul Krugman")
it('o18', 'ouvrage', 1983, "« International R&D Rivalry and Industrial Strategy »",
   "Brander et Spencer y montrent qu’une subvention peut renverser l’équilibre d’un oligopole international et capter une rente étrangère.",
   "Fondement de la politique commerciale stratégique, et de sa fragilité informationnelle.",
   'mondialisation', "Politique commerciale stratégique", auteur="James Brander et Barbara Spencer")
it('o19', 'ouvrage', 1991, "Geography and Trade",
   "Krugman y montre que la localisation initiale engendre l’avantage par les rendements croissants et les effets d’agglomération.",
   "Inversion de la causalité des théories traditionnelles : l’avantage comparatif peut être acquis.",
   'mondialisation', "Nouvelle économie géographique", auteur="Paul Krugman")
it('o20', 'ouvrage', 1996, "La mondialisation n’est pas coupable",
   "Krugman y attribue les difficultés de l’emploi industriel au progrès technique plutôt qu’à la concurrence des pays à bas salaires.",
   "À confronter à son réexamen de 2019, qui reconnaît la sous-estimation des effets locaux et distributifs.",
   'mondialisation', "Nouvelle économie géographique", auteur="Paul Krugman")
it('o21', 'ouvrage', 2022, "Le temps de la démondialisation",
   "Vuillemey y soutient que l’ouverture conduit les États à renoncer à des exigences sociales et environnementales.",
   "Déplace la justification de la protection des intérêts sectoriels vers la capacité d’action collective.",
   'mondialisation', "Critique de la mondialisation", auteur="Guillaume Vuillemey")
it('o22', 'ouvrage', 2023, "L’économie mondiale 2024",
   "Emlinger, Guimbard et Lefebvre y documentent une nouvelle hiérarchie des objectifs des politiques commerciales.",
   "Sécurité des approvisionnements, transition écologique et capacités industrielles passent devant l’efficience allocative.",
   'mondialisation', "Économie internationale appliquée",
   auteur="C. Emlinger, H. Guimbard et K. Lefebvre")

# ------------------------------------------------------------------ théories
it('t01', 'theorie', 1776, "Avantage absolu",
   "Un pays se spécialise dans la production où il utilise moins de facteurs qu’un autre : l’échange devient un jeu à somme positive.",
   "Limite décisive : un pays sans aucun avantage absolu resterait exclu de l’échange.",
   'classique', "Classique", auteur="Adam Smith")
it('t02', 'theorie', 1817, "Avantage comparatif",
   "La spécialisation se détermine par comparaison des coûts d’opportunité internes, et non des productivités entre pays.",
   "Un pays absolument moins productif partout conserve un avantage comparatif : l’échange reste mutuellement avantageux.",
   'classique', "Classique", auteur="David Ricardo")
it('t03', 'theorie', 1848, "Bornes de Mill et partage du gain",
   "Le prix international doit rester entre les prix relatifs internes des deux pays, sous peine de refus de l’échange.",
   "Plus le prix est proche de la borne favorable à un pays, plus son gain est élevé : le partage dépend du rapport de force.",
   'classique', "Classique", auteur="John Stuart Mill")
it('t04', 'theorie', 1933, "Théorème Heckscher-Ohlin",
   "Un pays possède un avantage comparatif dans la production utilisant intensivement le facteur dont il est relativement le mieux doté.",
   "Mécanisme : abondance relative, baisse du prix relatif du facteur, baisse du coût relatif du bien, spécialisation.",
   'neoclassique', "Néoclassique", auteur="E. Heckscher et B. Ohlin")
it('t05', 'theorie', 1941, "Théorème Stolper-Samuelson",
   "L’ouverture augmente la rémunération réelle du facteur relativement abondant et réduit celle du facteur relativement rare.",
   "Le commerce redistribue à l’intérieur de chaque pays : les perdants se repèrent au facteur qu’ils détiennent.",
   'inegalites', "Néoclassique", auteur="W. Stolper et P. Samuelson")
it('t06', 'theorie', 1950, "Dégradation des termes de l’échange",
   "Les prix des produits primaires progressent moins vite que ceux des manufacturés : il faut exporter plus pour importer autant.",
   "Fondement de la critique structuraliste des spécialisations primaires.",
   'developpement', "Structuraliste", auteur="Raúl Prebisch")
it('t07', 'theorie', 1953, "Paradoxe de Leontief",
   "Les exportations du pays le plus abondant en capital apparaissent moins intensives en capital que les biens substituables aux importations.",
   "N’invalide pas le modèle HOS mais impose de redéfinir les facteurs : qualification, savoir technologique.",
   'neoclassique', "Analyse input-output", auteur="Wassily Leontief")
it('t08', 'theorie', 1955, "Théorème de Rybczynski",
   "L’accroissement de la dotation en un facteur augmente plus que proportionnellement la production du bien qui l’utilise intensivement.",
   "Rend les avantages comparatifs construits : l’investissement et l’éducation deviennent des instruments de spécialisation.",
   'neoclassique', "Commerce international", auteur="T. Rybczynski")
it('t09', 'theorie', 1958, "Croissance appauvrissante",
   "Lorsqu’un pays pèse sur le prix mondial, sa production supplémentaire dégrade le prix au point de réduire son bien-être.",
   "Cas limite où la croissance de la production diminue le revenu réel disponible.",
   'developpement', "Économie internationale", auteur="Jagdish Bhagwati")
it('t10', 'theorie', 1961, "Écart technologique",
   "L’innovation procure un avantage comparatif temporaire, érodé par le délai d’imitation des concurrents.",
   "L’avantage dépend du flux continu d’innovations : la spécialisation devient dynamique.",
   'mondialisation', "Approche néo-technologique", auteur="M. Posner")
it('t11', 'theorie', 1966, "Cycle de vie international du produit",
   "Quatre phases : naissance dans le pays innovateur, exportation, maturité et délocalisation, importation par le pays d’origine.",
   "Explique le déplacement des productions sans invoquer de perte d’avantage, mais une banalisation du procédé.",
   'mondialisation', "Approche néo-technologique", auteur="Raymond Vernon")
it('t13', 'theorie', 1979, "Rendements croissants et gains de variété",
   "L’ouverture procure trois gains même entre pays identiques : sélection par la concurrence, variété accrue, effet de dimension.",
   "Rompt avec la tradition en faisant de la taille du marché, et non des différences entre pays, la source du gain.",
   'mondialisation', "Nouvelle économie géographique", auteur="Paul Krugman")
it('t14', 'theorie', 1983, "Politique commerciale stratégique",
   "Dans un oligopole mondial à coûts fixes élevés, une subvention peut dissuader l’entrée du concurrent et transférer sa rente.",
   "Efficace sous condition d’information juste ; sa généralisation déclenche une guerre de subventions.",
   'mondialisation', "Politique commerciale stratégique", auteur="J. Brander et B. Spencer")
it('t15', 'theorie', 1991, "Nouvelle géographie économique",
   "La localisation initiale, par les rendements croissants et les externalités marshalliennes, engendre l’avantage au lieu d’en découler.",
   "Bangalore, Toulouse et la Silicon Valley illustrent des avantages acquis et difficilement réversibles.",
   'mondialisation', "Nouvelle économie géographique", auteur="Paul Krugman")
it('t16', 'theorie', 2022, "Paradigme productiviste",
   "La politique économique se recentre sur la qualité des emplois et les capacités productives localisées plutôt que sur l’efficience allocative.",
   "Cadre d’interprétation du retour de la politique industrielle et du protectionnisme contemporain.",
   'mondialisation', "Hétérodoxe", auteur="Dani Rodrik")

# ------------------------------------------------------------------ événements
it('e01', 'evenement', 1703, "Traité commercial anglo-portugais (traité de Methuen)",
   "L’accord échange l’ouverture du marché anglais aux vins portugais contre celle du marché portugais aux draps anglais.",
   "Le cours s’en sert pour montrer que les partenaires commerciaux n’ont pas le même pouvoir de négociation.",
   'histoire', "Histoire économique")
it('e02', 'evenement', 1834, "Entrée en vigueur du Zollverein",
   "L’union douanière allemande supprime les droits internes et établit un tarif commun face à l’extérieur.",
   "Cadre institutionnel du protectionnisme éducateur allemand analysé par List puis poursuivi sous Bismarck.",
   'histoire', "Protectionnisme éducateur")
it('e03', 'evenement', 1846, "Abrogation des Corn Laws",
   "Le Royaume-Uni supprime les droits protégeant les céréales nationales et s’engage dans le libre-échange.",
   "Marque la fin du protectionnisme britannique : avant cette date, le pays libre-échangiste était lui-même protégé.",
   'histoire', "Histoire économique")
it('e04', 'evenement', 1947, "Signature du GATT",
   "Vingt-trois pays signent l’Accord général sur les tarifs douaniers et le commerce, autour de la non-discrimination et de la réciprocité.",
   "Le droit de douane moyen mondial, d’environ 40 % en 1947, tombe à 20 % en 1960 puis 4 % en 2019.",
   'mondialisation', "Mondialisation")
it('e05', 'evenement', 1995, "Création de l’OMC (accords de Marrakech)",
   "L’Organisation mondiale du commerce succède au GATT, étend les règles aux services et se dote d’un organe de règlement des différends.",
   "Institutionnalisation du multilatéralisme commercial, dont la paralysie ultérieure prive le système de son mécanisme d’exécution.",
   'mondialisation', "Mondialisation")
it('e06', 'evenement', 2001, "Lancement du cycle de Doha",
   "Ouverture d’un cycle de négociations multilatérales qui ne sera jamais conclu.",
   "Son échec symbolise le blocage du multilatéralisme face à l’élargissement et à l’hétérogénéité des intérêts.",
   'mondialisation', "Mondialisation")
it('e07', 'evenement', 2008, "Engagement du G20 contre le protectionnisme",
   "Face à la crise, les membres du G20 s’engagent à ne pas recourir à de nouvelles mesures protectionnistes.",
   "L’épisode révèle la difficulté à tenir cet engagement en période de récession.",
   'mondialisation', "Mondialisation")
it('e08', 'evenement', 2018, "Guerre commerciale sino-américaine",
   "Les États-Unis instaurent des droits de 25 % sur l’acier et 10 % sur l’aluminium, puis relèvent par vagues les droits sur la Chine.",
   "Le droit moyen appliqué aux importations chinoises passe de 3,1 % à 12,4 %, puis 18,4 % et 21,5 %.",
   'mondialisation', "Mondialisation")
it('e09', 'evenement', 2019, "L’OMC autorise 7,5 milliards de dollars de rétorsion (Airbus-Boeing)",
   "L’organe de règlement des différends autorise les États-Unis à imposer des droits en réponse aux subventions européennes à Airbus.",
   "Illustration du risque d’un jeu à somme nulle dans la politique commerciale stratégique.",
   'mondialisation', "Politique commerciale stratégique")
it('e10', 'evenement', 2020, "Accord commercial dit de « phase one »",
   "Signé le 15 janvier 2020, il suspend l’escalade tarifaire sino-américaine sans traiter le conflit structurel.",
   "Montre la différence entre une trêve tarifaire et un règlement de la rivalité technologique et industrielle.",
   'mondialisation', "Mondialisation")
it('e11', 'evenement', 2021, "Suspension du conflit Airbus-Boeing",
   "Les parties suspendent leurs mesures de rétorsion réciproques après des années de contentieux.",
   "Clôt provisoirement l’illustration la plus documentée d’une guerre de subventions entre économies avancées.",
   'mondialisation', "Politique commerciale stratégique")
it('e12', 'evenement', 2022, "IRA et CHIPS Act",
   "Les États-Unis subordonnent des aides massives aux technologies vertes et aux semi-conducteurs à la production nationale.",
   "Clauses en tension avec le traitement national et la prohibition des subventions liées au contenu national.",
   'mondialisation', "Politique industrielle")
it('e13', 'evenement', 2024, "Relèvement des droits américains sur les véhicules électriques",
   "Les droits applicables aux véhicules électriques chinois sont portés de 25 % à 100 %.",
   "Transposition de la politique commerciale stratégique à une technologie jugée décisive pour la transition.",
   'mondialisation', "Politique industrielle")
it('e14', 'evenement', 2025, "« Liberation Day » du 2 avril",
   "Les États-Unis annoncent des droits dits réciproques sur un très grand nombre de partenaires.",
   "Le droit moyen américain passe d’environ 5 % à 23,7 %, avant un reflux partiel à 16,1 % fin mai.",
   'mondialisation', "Mondialisation")
it('e15', 'evenement', 2026, "Phase définitive du mécanisme d’ajustement carbone aux frontières",
   "Le dispositif européen taxe le contenu carbone de certaines importations pour l’aligner sur le prix du marché carbone européen.",
   "Premier instrument commercial dont l’assiette est le carbone et non l’origine : limiter les fuites de carbone.",
   'mondialisation', "Environnement")
it('e16', 'evenement', 1892, "Tournant protectionniste français (tarif Méline)",
   "La France relève ses droits de douane, notamment agricoles, à l’issue de la mobilisation des intérêts céréaliers.",
   "Léo Charles y voit la constitution d’un « bloc social » protectionniste : la politique commerciale traduit un rapport de forces interne.",
   'histoire', "Histoire économique", auteur="Léo Charles")
