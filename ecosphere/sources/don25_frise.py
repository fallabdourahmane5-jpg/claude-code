# -*- coding: utf-8 -*-
"""Frise chronologique : items du chapitre 5 de deuxieme annee.

MAJ : items deja presents auxquels le chapitre 25 est ajoute.
NOUVEAUX : items ajoutes. Aucune date de naissance n'est portee lorsque le
document de cours ne la fournit pas de facon certaine : dans ce cas seule la
publication est datee.
"""

MAJ = {
 # auteurs déjà présents
 'a209': "John Maynard Keynes", 'a210': "John Hicks",
 'a236': "Alvin Hansen", 'a290': "Alvin Hansen",
 'a211': "Paul Samuelson", 'a226': "Robert Solow",
 'a231': "Robert Barro", 'a229': "Paul Romer",
 'a252': "Milton Friedman", 'a318': "Milton Friedman",
 'a216': "Arthur Pigou", 'a206': "Léon Walras", 'a333': "Vilfredo Pareto",
 'a310': "Max Weber", 'a227': "Roy Harrod", 'a228': "Evsey Domar",
 'a198': "Jean-Baptiste Say", 'a344': "Alfred Marshall",
 'a242': "Simon Kuznets", 'a201': "François Quesnay",
 'a322': "Robert Mundell", 'a321': "Henri Bourguinat",
 # ouvrages déjà présents
 'o078': "Théorie générale de l'emploi, de l'intérêt et de la monnaie",
 'o079': "Mr. Keynes and the 'Classics'",
 'o125': "A Theory of the Consumption Function",
 'o104': "Government Spending in a Simple Model of Endogenous Growth",
 'o102': "Increasing Returns and Long-Run Growth",
 'o086': "The Economics of Welfare",
 # théories déjà présentes
 'f056': "Modèle de croissance Harrod-Domar",
 # événements déjà présents
 'f023': "Accords de Bretton Woods",
 'f028': "Microprocesseur et fin de la convertibilité dollar-or",
 'f030': "Premier choc pétrolier",
 'f032': "Second choc pétrolier et choc Volcker",
}

C = "Macroéconomie des politiques conjoncturelles"
NOUVEAUX = []


def it(idn, type_, an, titre, resume, portee, fam, courant=C,
       auteur=None, fin=None, vivant=None, oeuvres=None):
    d = {'id': 'c25_' + idn, 'type': type_, 'an': an, 'titre': titre,
         'resume': resume, 'portee': portee, 'courant': courant,
         'ch': [25], 'fam': fam}
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
it('a01', 'auteur', 1905, "Richard Kahn",
   "Développe en 1931 le principe du multiplicateur d’emploi, que Keynes généralisera en multiplicateur de revenu.",
   "Kahn fournit le mécanisme central de l’analyse keynésienne : une dépense initiale engendre, par la circulation des revenus, un supplément d’activité démultiplié.",
   'keynesien', courant="Keynésien", auteur="Richard Kahn", fin=1989, vivant=False,
   oeuvres=["Travaux de 1931 sur le multiplicateur d’emploi"])
it('a02', 'auteur', 1914, "Alban William Phillips",
   "Établit en 1958 une relation inverse entre le taux de chômage et la variation des salaires nominaux au Royaume-Uni.",
   "La relation originelle porte sur les salaires nominaux, non sur l’inflation : c’est la reformulation ultérieure qui a créé l’arbitrage inflation-chômage.",
   'keynesien', courant="Économétrie appliquée", auteur="Alban William Phillips",
   fin=1975, vivant=False, oeuvres=["Article de 1958 sur chômage et salaires nominaux"])
it('a03', 'auteur', 1928, "Richard Lipsey",
   "Approfondit en 1960 l’analyse théorique de la courbe de Phillips.",
   "Lipsey est le maillon souvent oublié entre Phillips et la lecture en termes d’inflation : il théorise ce que Phillips avait seulement mesuré.",
   'keynesien', courant="Keynésien", auteur="Richard Lipsey", vivant=True,
   oeuvres=["Travaux de 1960 sur la courbe de Phillips"])
it('a04', 'auteur', 1928, "Arthur Okun",
   "Établit en 1962 la relation entre l’écart de production et le chômage : produire sous son potentiel va de pair avec un chômage plus élevé.",
   "Okun fournit l’instrument de diagnostic conjoncturel : c’est par l’output gap que l’on juge si une politique de demande a un objet.",
   'keynesien', courant="Keynésien", auteur="Arthur Okun", fin=1980, vivant=False,
   oeuvres=["Travaux de 1962 sur l’écart de production"])
it('a05', 'auteur', 1911, "Marcus Fleming",
   "Prolonge en 1962 l’analyse keynésienne à l’économie ouverte : l’efficacité des politiques dépend du régime de change et de la mobilité des capitaux.",
   "Avec Mundell, Fleming déplace la question de l’efficacité des politiques : elle ne dépend plus seulement du modèle, mais du cadre monétaire international.",
   'keynesien', courant="Macroéconomie internationale", auteur="Marcus Fleming",
   fin=1976, vivant=False, oeuvres=["Travaux de 1962 sur l’équilibre en économie ouverte"])
it('a06', 'auteur', 1956, "Jacques Généreux",
   "Propose en 2016 une représentation simplifiée des dilemmes de politique économique par l’écart entre le revenu de plein emploi et le revenu équilibrant les transactions courantes.",
   "Généreux offre l’outil le plus économique pour poser un dilemme interne-externe : la position relative de Ype et de YBTC suffit à l’identifier.",
   'keynesien', courant="Keynésien", auteur="Jacques Généreux", vivant=True,
   oeuvres=["Travaux de 2016 sur les dilemmes de politique économique"])

# ----------------------------------------------------------------- ouvrages
it('o01', 'ouvrage', 1931, "Travaux de Kahn sur le multiplicateur d’emploi",
   "Kahn montre qu’une dépense initiale engendre un supplément d’emploi démultiplié par la circulation des revenus.",
   "Point de départ du multiplicateur keynésien, repris et généralisé par Keynes cinq ans plus tard.",
   'keynesien', courant="Keynésien", auteur="Richard Kahn")
it('o02', 'ouvrage', 1933, "The Theory of Unemployment",
   "Pigou développe l’analyse néoclassique du chômage : un salaire réel supérieur au niveau d’équilibre engendre un excès d’offre de travail.",
   "C’est la cible explicite de Keynes : si le chômage vient du salaire réel, la flexibilité suffit ; s’il vient de la demande, elle ne suffit pas.",
   'neoclassique', courant="Néoclassique", auteur="Arthur Pigou")
it('o03', 'ouvrage', 1941, "Fiscal Policy and Business Cycles",
   "Hansen prolonge le modèle de Hicks et contribue à diffuser l’analyse keynésienne aux États-Unis.",
   "Fonde la tradition Hicks-Hansen, qui fait d’IS-LM l’instrument majeur d’analyse des politiques économiques — en économie fermée.",
   'keynesien', courant="Keynésien", auteur="Alvin Hansen")
it('o04', 'ouvrage', 1949, "Economics (édition de 1949)",
   "Samuelson y présente le diagramme à 45° : la bissectrice rassemble les points où le revenu est égal à la demande globale.",
   "Représentation graphique canonique du modèle keynésien simple, où l’équilibre ne correspond pas nécessairement au plein emploi.",
   'keynesien', courant="Synthèse néoclassique", auteur="Paul Samuelson")
it('o05', 'ouvrage', 1958, "Article de Phillips sur chômage et salaires nominaux",
   "Phillips met en évidence une relation inverse entre le taux de chômage et la variation des salaires nominaux au Royaume-Uni.",
   "Attention à l’attribution : la relation porte sur les salaires nominaux. La lecture en termes d’inflation vient de Lipsey, Samuelson et Solow.",
   'keynesien', courant="Économétrie appliquée", auteur="Alban William Phillips")
it('o06', 'ouvrage', 1962, "Travaux de Fleming sur l’équilibre en économie ouverte",
   "Fleming montre que l’efficacité des politiques budgétaire et monétaire dépend du régime de change et de la mobilité des capitaux.",
   "Première moitié du modèle Mundell-Fleming, qui établit la symétrie inversée de l’efficacité des deux instruments.",
   'keynesien', courant="Macroéconomie internationale", auteur="Marcus Fleming")
it('o07', 'ouvrage', 1963, "Travaux de Mundell sur la mobilité des capitaux et les régimes de change",
   "Mundell établit qu’en changes fixes avec mobilité parfaite la politique monétaire est neutralisée, et qu’en changes flexibles c’est la politique budgétaire qui l’est.",
   "Seconde moitié du modèle Mundell-Fleming : l’instrument efficace dépend du régime de change, non de la doctrine.",
   'keynesien', courant="Macroéconomie internationale", auteur="Robert Mundell")
it('o08', 'ouvrage', 1974, "« Are Government Bonds Net Wealth? »",
   "Barro soutient qu’une baisse d’impôts financée par la dette est anticipée comme un prélèvement futur : l’épargne privée compense la désépargne publique.",
   "Formulation de l’équivalence ricardienne, troisième grande critique de la relance budgétaire — qui porte sur le financement, non sur l’investissement.",
   'monetaire', courant="Nouvelle économie classique", auteur="Robert Barro")
it('o09', 'ouvrage', 2016, "Travaux de Généreux sur les dilemmes de politique économique",
   "Généreux formalise les dilemmes par l’écart entre le revenu de plein emploi Ype et le revenu équilibrant les transactions courantes YBTC.",
   "Outil de diagnostic : l’ordre relatif des deux revenus détermine le dilemme auquel une économie ouverte est exposée.",
   'keynesien', courant="Keynésien", auteur="Jacques Généreux")

# ----------------------------------------------------------------- théories
it('t01', 'theorie', 1931, "Principe du multiplicateur",
   "Une dépense initiale engendre, par la circulation des revenus, un supplément d’activité démultiplié : k = 1 / (1 − c), soit 5 pour c = 0,8.",
   "Avec s = 0,2 et ΔY = 500, l’épargne engendrée atteint exactement l’investissement initial : la causalité va de l’investissement à l’épargne.",
   'keynesien', courant="Keynésien", auteur="Richard Kahn")
it('t02', 'theorie', 1936, "Demande effective et équilibre de sous-emploi",
   "La demande anticipée par les entrepreneurs détermine la production et l’emploi : si elle est insuffisante, l’économie s’équilibre durablement sous le plein emploi.",
   "Le chômage devient involontaire, et une baisse des salaires ne garantit pas le retour au plein emploi puisqu’elle réduit aussi les revenus.",
   'keynesien', courant="Keynésien", auteur="John Maynard Keynes")
it('t03', 'theorie', 1936, "Préférence pour la liquidité",
   "Trois motifs de détention de monnaie : transaction et précaution, croissants avec le revenu ; spéculation, décroissante avec le taux d’intérêt.",
   "Le taux d’intérêt cesse d’équilibrer épargne et investissement : il devient le prix de la renonciation à la liquidité, déterminé sur le marché monétaire.",
   'monetaire', courant="Keynésien", auteur="John Maynard Keynes")
it('t04', 'theorie', 1937, "Modèle IS-LM",
   "Hicks articule l’équilibre du marché des biens (IS) et celui du marché de la monnaie (LM) dans un plan revenu-taux d’intérêt.",
   "Hypothèses : monnaie active, court terme, prix fixes. C’est cette dernière qui interdit d’analyser l’inflation et appellera le modèle OG-DG.",
   'keynesien', courant="Keynésien", auteur="John Hicks")
it('t05', 'theorie', 1937, "Effet d’éviction",
   "Dépenses publiques ↑ → revenu ↑ → demande de monnaie ↑ → taux d’intérêt ↑ → investissement privé ↓.",
   "Son intensité dépend de la pente de LM : nulle dans une trappe à liquidité, totale dans la zone classique. C’est la première critique de la relance.",
   'keynesien', courant="Keynésien")
it('t06', 'theorie', 1937, "Trappe à liquidité",
   "Lorsque les taux sont très bas, toute monnaie supplémentaire est thésaurisée : LM devient horizontale.",
   "Le canal monétaire conventionnel est bloqué, mais la politique budgétaire devient particulièrement efficace puisque l’effet d’éviction disparaît.",
   'monetaire', courant="Keynésien")
it('t07', 'theorie', 1957, "Hypothèse du revenu permanent",
   "Les ménages règlent leur consommation sur le revenu moyen de long terme qu’ils anticipent, non sur leur revenu courant.",
   "Un transfert perçu comme temporaire est donc largement épargné — sauf pour les ménages contraints financièrement, qui peuvent en consommer une large part.",
   'monetaire', courant="Monétariste", auteur="Milton Friedman")
it('t08', 'theorie', 1958, "Courbe de Phillips",
   "Relation inverse entre le taux de chômage et la variation des salaires nominaux, établie par Phillips sur le Royaume-Uni.",
   "Reformulée par Lipsey (1960) puis par Samuelson et Solow (1960) en arbitrage inflation-chômage : la stagflation des années 1970 invalidera cette lecture.",
   'keynesien', courant="Économétrie appliquée", auteur="Alban William Phillips")
it('t09', 'theorie', 1962, "Loi d’Okun et écart de production",
   "Relation entre l’écart de production et le chômage : produire sous son potentiel va de pair avec un chômage plus élevé.",
   "Fournit l’instrument de diagnostic : un output gap négatif justifie une politique de demande, un output gap positif signale des tensions.",
   'keynesien', courant="Keynésien", auteur="Arthur Okun")
it('t10', 'theorie', 1963, "Modèle Mundell-Fleming",
   "En changes fixes avec mobilité parfaite, la politique budgétaire est amplifiée et la monétaire neutralisée ; en changes flexibles, exactement l’inverse.",
   "L’instrument efficace dépend donc du régime de change. Limites : modèle statique, prix rigides, flux de capitaux réduits aux seuls différentiels de taux, petite économie ouverte.",
   'keynesien', courant="Macroéconomie internationale", auteur="Robert Mundell")
it('t11', 'theorie', 1963, "Courbe BP et balance globale",
   "BP rassemble les couples revenu-taux d’intérêt compatibles avec l’équilibre de la balance globale, somme du solde courant et des mouvements autonomes de capitaux.",
   "Sa pente diminue avec la mobilité des capitaux : horizontale en mobilité parfaite, verticale en son absence. Attention : il s’agit de la balance globale, non du solde courant.",
   'monetaire', courant="Macroéconomie internationale")
it('t12', 'theorie', 1963, "Triangle des incompatibilités de Mundell",
   "Changes fixes, libre circulation des capitaux et autonomie monétaire ne peuvent être pleinement conciliés : deux objectifs au maximum.",
   "Grille de lecture de la fin de Bretton Woods : la montée de la mobilité financière a rendu la combinaison fixité-autonomie intenable.",
   'monetaire', courant="Macroéconomie internationale", auteur="Robert Mundell")
it('t13', 'theorie', 1963, "Règle d’affectation de Mundell",
   "Chaque instrument doit être affecté à l’objectif pour lequel son efficacité relative est la plus grande : le budget à l’équilibre interne, la monnaie à l’équilibre externe.",
   "Réponse au problème des dilemmes : il faut autant d’instruments que d’objectifs, et les affecter correctement.",
   'monetaire', courant="Macroéconomie internationale", auteur="Robert Mundell")
it('t14', 'theorie', 1968, "Taux de chômage naturel",
   "Le chômage naturel dépend des frictions, de l’adéquation entre qualifications et emplois, des institutions et de la formation des salaires.",
   "Une politique de demande ne peut pas l’abaisser durablement : elle n’obtient qu’une accélération de l’inflation. D’où le basculement vers les politiques structurelles.",
   'monetaire', courant="Monétariste", auteur="Milton Friedman")
it('t15', 'theorie', 1974, "Équivalence ricardienne",
   "Une baisse d’impôts financée par la dette fait anticiper des prélèvements futurs : l’épargne privée compense la désépargne publique.",
   "Suppose des agents informés, capables d’épargner et à horizon long : le cours la présente comme une critique importante mais non universellement vérifiée.",
   'monetaire', courant="Nouvelle économie classique", auteur="Robert Barro")
it('t16', 'theorie', 1975, "Modèle OG-DG et chocs d’offre",
   "En réintroduisant le niveau général des prix, le modèle offre globale-demande globale permet d’analyser inflation, déflation et chocs d’offre.",
   "Un choc d’offre négatif déplace l’offre globale de court terme vers la gauche : la production baisse et les prix montent. C’est la stagflation.",
   'monetaire', courant="Macroéconomie")

# --------------------------------------------------------------- événements
it('e01', 'evenement', 1975, "Stagflation : récession et inflation simultanées",
   "Croissance de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec des inflations de 11,7 %, 5,9 % et 9,1 % (OCDE).",
   "Configuration que l’arbitrage inflation-chômage ne permettait pas d’expliquer : elle impose le modèle OG-DG et l’analyse par les chocs d’offre.",
   'histoire', courant="Conjoncture")
it('e02', 'evenement', 1981, "Relance française et échec du multiplicateur en économie ouverte",
   "Relance de mai 1981 — hausse du SMIC, prestations sociales, emplois publics — dans un contexte d’inflation d’environ 13 % et de croissance faible des partenaires.",
   "Une part de la demande se porte sur les importations : les transactions courantes se dégradent et trois dévaluations interviennent entre 1981 et 1983.",
   'histoire', courant="Conjoncture")
it('e03', 'evenement', 1983, "Tournant de la rigueur",
   "En mars 1983, le gouvernement choisit de maintenir le franc dans le SME et abandonne la stratégie de relance au profit d’une politique restrictive.",
   "Illustration canonique de la contrainte extérieure : l’objectif externe l’emporte sur l’objectif interne.",
   'histoire', courant="Conjoncture")
it('e04', 'evenement', 1990, "Réunification allemande : un policy mix non coopératif",
   "Les dépenses de réunification déplacent IS vers la droite, tandis que la Bundesbank déplace LM vers la gauche pour contenir l’inflation.",
   "Taux courts de 4,3 % en 1988 à 9,2 % en 1991 ; solde budgétaire de + 0,2 % du PIB en 1989 à − 2,9 % en 1991 : l’activité est soutenue au prix de taux élevés.",
   'histoire', courant="Conjoncture")
it('e05', 'evenement', 1992, "Critères de Maastricht",
   "Traité signé en 1992 et entré en vigueur en 1993 : déficit public de référence de 3 % du PIB et dette publique de référence de 60 % du PIB.",
   "Le cours rappelle que ces seuils ne sont ni des interdictions absolues ni inconditionnelles, mais ils encadrent l’instrument budgétaire resté national.",
   'institutionnel', courant="Zone euro")
it('e06', 'evenement', 1997, "Pacte de stabilité et de croissance",
   "Adopté en 1997, il complète l’encadrement budgétaire des critères de Maastricht et sera plusieurs fois réformé.",
   "Avec une politique monétaire unique et des budgets nationaux encadrés, la zone euro présente une asymétrie institutionnelle qui rend la coordination difficile.",
   'institutionnel', courant="Zone euro")
it('e07', 'evenement', 1998, "Policy mix Clinton-Greenspan",
   "Le solde budgétaire américain passe de − 4,5 % à + 0,8 % du PIB entre 1992 et 1998, la croissance atteint 3,7 % en 1998 et les taux à un an reculent de 5,5 % à 4,8 %.",
   "Une consolidation budgétaire accompagnée d’un assouplissement monétaire préserve le revenu et abaisse le taux d’intérêt — illustration du policy mix, non démonstration causale.",
   'histoire', courant="Conjoncture")
it('e08', 'evenement', 2008, "Réhabilitation du modèle IS-LM",
   "La crise financière replace IS-LM au centre de l’analyse, pour comprendre la trappe à liquidité et les limites de la politique monétaire conventionnelle.",
   "Près du plancher des taux, l’expansion monétaire perd de son efficacité tandis que l’effet d’éviction d’une relance budgétaire devient très limité.",
   'keynesien', courant="Macroéconomie")
