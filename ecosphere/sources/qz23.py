# -*- coding: utf-8 -*-
"""Chapitre 23 — Les théories du commerce international et la politique commerciale.

Audit : 95 questions héritées, 18 sous-parties. Les corrigés étaient déjà
développés mais aucune question ne comportait la réfutation des distracteurs,
aucune réponse rédigée n'avait de grille d'évaluation, et la quasi-totalité
des questions étaient étiquetées « comprendre ». Sept questions vrai/faux
reformulant un QCM voisin sont écartées, trois questions mal rattachées sont
replacées dans leur sous-partie, 88 questions sont corrigées et une banque
nouvelle est ajoutée.
"""

SP = {
 'c23-01': "Analyse positive, analyse normative et coûts politiques de l'ouverture",
 'c23-02': "Smith, Ricardo et la rupture avec le mercantilisme",
 'c23-03': "L'avantage comparatif et le coût d'opportunité",
 'c23-04': "Mill et le partage du gain, Marx et les débouchés extérieurs",
 'c23-05': "Les analyses critiques : Lénine, Prebisch, Emmanuel, Bhagwati",
 'c23-06': "Le modèle HOS : dotations factorielles et hypothèses",
 'c23-07': "Stolper-Samuelson, Rybczynski et les vérifications empiriques",
 'c23-08': "Spécialisations révélées, reprimarisation et commerce intra-branche",
 'c23-09': "Approches néo-factorielles et néo-technologiques",
 'c23-10': "Cycle du produit, différenciation et demande de différence",
 'c23-11': "Krugman : rendements croissants, variété et districts industriels",
 'c23-12': "Agglomération, dépendance au sentier et avantages acquis",
 'c23-13': "Faits et doctrines : libre-échange, protectionnisme, mercantilisme",
 'c23-14': "Les instruments de la protection et leur coût",
 'c23-15': "Dilemme du prisonnier, GATT, contournements et guerres commerciales",
 'c23-16': "Protectionnisme éducateur et protection des industries vieillissantes",
 'c23-17': "La politique commerciale stratégique et ses limites",
 'c23-18': "Protectionnisme contemporain, environnement et fragmentation géo-économique",
}

# Questions supprimées : chacune reformulait en vrai/faux un QCM de la même
# sous-partie, sans apporter de contenu nouveau.
DROP = [
 'ch23-vraifa-59',   # doublon de ch23-qcm-16 (Stolper-Samuelson)
 'ch23-vraifa-61',   # doublon de ch23-qcm-19 et -20 (paradoxe de Leontief)
 'ch23-vraifa-62',   # doublon de ch23-qcm-21 (avantages comparatifs révélés)
 'ch23-vraifa-63',   # doublon de ch23-qcm-23 (commerce intra-branche)
 'ch23-vraifa-65',   # doublon de ch23-qcm-32 (économies d'échelle externes)
 'ch23-vraifa-66',   # doublon de ch23-qcm-38 et -39 (droit de douane)
 'ch23-vraifa-70',   # doublon de ch23-questi-91 (asymétrie politique, Pareto)
]

from qz23f1 import FIX as _F1
from qz23f2 import FIX as _F2
from qz23f3 import FIX as _F3

FIX = dict(_F1)
FIX.update(_F2)
FIX.update(_F3)


# Éléments attendus pour les réponses rédigées héritées.
def k(f, l):
    return {'f': f, 'l': l}


CLES = {
 'ch23-questi-75': [
   k(['absolu', 'productivite', 'plus productif'],
     "l'avantage absolu compare les productivités entre pays"),
   k(['exclu', 'rien a proposer', 'moins productif partout'],
     "un pays moins productif partout n'aurait rien à proposer"),
   k(['cout d opportunite', 'opportunite', 'renonce'],
     "l'avantage comparatif compare les coûts d'opportunité internes"),
   k(['interieur', 'interne', 'relatif', 'chaque pays'],
     "une comparaison interne à chaque pays"),
   k(['portugal', 'ricardo', 'drap', 'vin'],
     "la démonstration ricardienne du Portugal")],
 'ch23-questi-76': [
   k(['production mondiale', 'production augmente', '4,325'],
     "à facteurs donnés, la production mondiale augmente"),
   k(['economie de facteur', 'moins de travail', '30'],
     "à production donnée, une économie de facteurs"),
   k(['reallocation', 'reaffect', 'affecter'],
     "la réallocation des facteurs"),
   k(['cout d opportunite', 'opportunite', 'plus faible'],
     "vers les emplois où le coût d'opportunité est le plus faible"),
   k(['efficacite', 'efficience', 'globale'],
     "une hausse de l'efficacité productive globale")],
 'ch23-questi-77': [
   k(['existence', 'gain', 'mutuellement avantageux'],
     "Ricardo établit l'existence du gain"),
   k(['indetermine', 'prix international', 'partage'],
     "mais laisse indéterminé le prix international, donc le partage"),
   k(['borne', 'intervalle', 'entre les rapports', '0,88', '1,2'],
     "Mill détermine les bornes du prix international"),
   k(['autarcie', 'refuse', 'prefere'],
     "hors de ces bornes, un pays préfère l'autarcie"),
   k(['proche', 'favorable', 'plus eleve', 'repartition'],
     "plus le prix est proche de la borne favorable, plus le gain est élevé")],
 'ch23-questi-78': [
   k(['accumulation', 'concurrence entre capitaliste'],
     "la concurrence entre capitalistes impose l'accumulation"),
   k(['plus-value', 'plus value', 'composition du capital', 'taux de profit'],
     "la baisse tendancielle du taux de profit"),
   k(['armee industrielle', 'reserve', 'salaire bas', 'compression'],
     "l'armée industrielle de réserve comprime les salaires"),
   k(['demande interieure', 'debouche', 'insuffisante', 'absorber'],
     "la demande intérieure devient insuffisante"),
   k(['contradiction', 'provisoire', 'necessite', 'pas un bienfait'],
     "l'exportation résout provisoirement une contradiction interne")],
 'ch23-questi-79': [
   k(['prebisch', 'terme de l echange', 'primaire'],
     "Prebisch : la dégradation des termes de l'échange"),
   k(['emmanuel', 'salaire', 'echange inegal'],
     "Emmanuel : l'échange inégal par les salaires"),
   k(['bhagwati', 'appauvrissante', 'prix mondial'],
     "Bhagwati : la croissance appauvrissante"),
   k(['conforme', 'defavorable', 'specialisation'],
     "une spécialisation conforme aux avantages comparatifs peut être défavorable"),
   k(['divergence', 'contextuelle', 'rattrapage', 'emergent'],
     "limite contextuelle : l'hypermondialisation s'accompagne d'un rattrapage")],
 'ch23-questi-80': [
   k(['intensivement', 'intensif', 'utilise'],
     "le pays se spécialise dans la production utilisant intensivement..."),
   k(['relativement abondant', 'abondance relative', 'mieux dote'],
     "...le facteur dont il est relativement le mieux doté"),
   k(['prix relatif', 'moins cher', 'moins couteu'],
     "l'abondance relative fait baisser le prix relatif du facteur"),
   k(['cout', 'baisse', 'relativement'],
     "le coût relatif de la production qui l'emploie baisse"),
   k(['rapport', 'relative', 'partenaire', 'comparer'],
     "comparer des rapports de dotations, et relativement aux partenaires")],
 'ch23-questi-81': [
   k(['repartition', 'distributif', 'redistribue'],
     "le débat se déplace du gain agrégé vers la répartition"),
   k(['abondant', 'augmente', 'rémunération', 'remuneration'],
     "la rémunération du facteur relativement abondant augmente"),
   k(['rare', 'diminue', 'reduit', 'baisse'],
     "celle du facteur relativement rare diminue"),
   k(['peu qualifie', 'qualifi', 'pays avance', 'expose'],
     "au Nord, les peu qualifiés des secteurs exposés perdent"),
   k(['normatif', 'perdant', 'gagne globalement', 'compens'],
     "un pays peut gagner globalement alors que certains perdent")],
 'ch23-questi-82': [
   k(['plus que proportionnel', 'accroissement', 'augmente la production'],
     "l'accroissement d'un facteur augmente plus que proportionnellement la production"),
   k(['endogene', 'evoluer', 'pas permanent', 'construit'],
     "les dotations deviennent endogènes"),
   k(['education', 'r&d', 'investissement', 'capital'],
     "l'État peut les construire par l'éducation, la R&D, le capital"),
   k(['coree', 'chine'],
     "les exemples coréen et chinois"),
   k(['politique industrielle', 'strategi', 'objet'],
     "la spécialisation devient objet de politique industrielle")],
 'ch23-questi-83': [
   k(['difference', 'productivite', 'dotation'],
     "les théories traditionnelles expliquent le commerce par des différences"),
   k(['inter-branche', 'inter branche', 'dissemblable'],
     "elles prévoient un commerce inter-branche entre pays dissemblables"),
   k(['comparable', 'semblable', 'meme branche', 'deux sens'],
     "or des pays comparables échangent dans la même branche, dans les deux sens"),
   k(['differenciation', 'variete', 'monopolistique'],
     "il faut mobiliser la différenciation et la concurrence monopolistique"),
   k(['demande de difference', 'lassudrie', 'demande'],
     "et la demande de différence")],
 'ch23-questi-84': [
   k(['neo-factoriel', 'neo factoriel', 'dotation', 'liste'],
     "les approches néo-factorielles enrichissent la liste des facteurs"),
   k(['keesing', 'qualification', '1966'],
     "Keesing (1966) fait de la qualification un facteur"),
   k(['capital humain'],
     "puis le capital humain élargit la nomenclature"),
   k(['neo-technologique', 'neo technologique', 'productivite', 'origine'],
     "les approches néo-technologiques expliquent l'origine des écarts de productivité"),
   k(['posner', 'avance technologique', 'temporaire'],
     "Posner (1961) : une avance technologique temporaire"),
   k(['vernon', 'cycle'],
     "Vernon (1966) : le cycle de vie du produit")],
 'ch23-questi-85': [
   k(['naissance', 'innovateur', 'technologie instable'],
     "naissance dans le pays innovateur"),
   k(['croissance', 'exportation', 'demande etrangere'],
     "croissance et premières exportations"),
   k(['maturite', 'standardis', 'banalis', 'delocalis'],
     "maturité, standardisation et délocalisation"),
   k(['importe', 'importation', 'inverse'],
     "le pays innovateur finit par importer"),
   k(['ecran', 'televiseur', 'japon', 'coree'],
     "l'exemple des téléviseurs à écran plat")],
 'ch23-questi-86': [
   k(['dotation determine', 'traditionnelle', 'specialisation puis localisation'],
     "dans les théories traditionnelles, la dotation détermine la localisation"),
   k(['implantation initiale', 'accident', 'histoire', 'premier'],
     "une implantation initiale, parfois accidentelle"),
   k(['volume', 'echelle', 'cout unitaire', 'rendements croissants'],
     "les volumes abaissent les coûts unitaires"),
   k(['attire', 'cumulatif', 'agglomeration', 'consolide'],
     "ce qui attire d'autres activités et consolide l'avantage"),
   k(['bangalore', 'toulouse', 'silicon valley'],
     "Bangalore, Toulouse ou la Silicon Valley")],
 'ch23-questi-87': [
   k(['cout unitaire', 'rendement croissant', 'echelle'],
     "les coûts unitaires baissent avec le volume"),
   k(['seuil', 'q0', 'exclu', 'volume suffisant'],
     "un producteur plus efficace peut rester exclu faute d'atteindre le seuil"),
   k(['anteriorite', 'deja installe', 'premier entrant'],
     "face à un concurrent déjà installé"),
   k(['protection temporaire', 'temporaire', 'franchir'],
     "une protection temporaire permet de franchir ce seuil"),
   k(['list', 'formalisation', 'educateur'],
     "l'argument de List reçoit une formalisation"),
   k(['marche domestique', 'demande domestique', 'condition'],
     "à condition d'un marché domestique suffisant")],
 'ch23-questi-88': [
   k(['prix interieur', 'prix augmente', 'montant du droit'],
     "le prix intérieur augmente du montant du droit"),
   k(['production nationale', 'production augmente'],
     "la production nationale s'accroît"),
   k(['importation', 'consommation', 'diminue'],
     "consommation et importations diminuent"),
   k(['recette', 'transfert', 'etat'],
     "l'État perçoit des recettes, qui sont un transfert"),
   k(['surplus', 'consommateur', 'producteur'],
     "le surplus des producteurs augmente, celui des consommateurs diminue davantage"),
   k(['perte seche', 'distorsion', 'deux perte'],
     "deux pertes sèches : distorsion à la production et à la consommation")],
 'ch23-questi-89': [
   k(['reduit sa demande', 'demande d importation', 'prix mondial'],
     "en réduisant sa demande, il fait baisser le prix mondial"),
   k(['terme de l echange', 'moins cher', 'gain'],
     "un gain de termes de l'échange"),
   k(['depasse', 'exceder', 'perte seche'],
     "qui peut excéder les deux pertes sèches"),
   k(['represaille', 'depens', 'partenaire'],
     "mais il s'obtient aux dépens des partenaires et appelle des représailles"),
   k(['elasticite', 'pouvoir de marche', 'hypothese', 'suppose'],
     "il suppose un pouvoir de marché et une élasticité favorable")],
 'ch23-questi-90': [
   k(['efficacite', 'objectif', 'atteint'],
     "l'efficacité : l'objectif est-il atteint ?"),
   k(['efficience', 'cout', 'rapport'],
     "l'efficience : à quel coût ?"),
   k(['200 000', '200 millions', '1 000 emploi', 'par emploi'],
     "l'exemple chiffré : 200 000 € par emploi sauvegardé"),
   k(['equite', 'repartition', 'qui paie'],
     "l'équité : qui paie, qui gagne ?"),
   k(['moyen', 'engagement', 'compatibilite', 'omc'],
     "la question des moyens et de la compatibilité avec les engagements")],
 'ch23-questi-91': [
   k(['pareto', 'asymetrie', 'organisation'],
     "l'asymétrie d'organisation mise en évidence par Pareto"),
   k(['concentre', 'petit nombre', 'producteur', 'identifiable'],
     "des gains concentrés sur des producteurs identifiables"),
   k(['diffus', 'disperse', 'faible', 'petite somme'],
     "des pertes diffuses sur des consommateurs dispersés"),
   k(['mobilis', 'organiser', 'lobby', 'groupe de pression'],
     "d'où une capacité de mobilisation asymétrique"),
   k(['charles', 'bloc social', 'cerealier'],
     "Léo Charles et la constitution d'un bloc social protectionniste")],
 'ch23-questi-92': [
   k(['ocean de protectionnisme', 'pas uniformement', 'xixe', '19e'],
     "le XIXᵉ siècle n'est pas uniformément libre-échangiste"),
   k(['royaume-uni', 'britannique', 'apres', 'consolide'],
     "le Royaume-Uni ne devient libre-échangiste qu'après s'être consolidé"),
   k(['etats-unis', 'allemagne', 'tarif eleve', 'protege'],
     "les États-Unis et l'Allemagne s'industrialisent derrière des tarifs élevés"),
   k(['daniel', 'pratique', 'tendanciellement'],
     "Jean-Marc Daniel : « les pratiques sont tendanciellement protectionnistes »"),
   k(['correlation', 'causalite', 'prudence', 'revolution industrielle'],
     "mais une corrélation n'établit pas une causalité")],
 'ch23-questi-93': [
   k(['oligopol', 'cout fixe', 'etroit', 'deux producteur'],
     "un marché trop étroit pour deux producteurs à coûts fixes élevés"),
   k(['premier entrant', 'anteriorite', 'boeing', 'dissuade'],
     "l'avantage du premier entrant décide de l'issue"),
   k(['subvention', 'renverse', 'profitable', 'airbus'],
     "une subvention peut renverser l'équilibre"),
   k(['rente', 'transfert', 'capter'],
     "et transférer la rente du concurrent"),
   k(['information', 'anticiper', 'erreur'],
     "limite : l'État doit anticiper correctement coûts, demande et réactions"),
   k(['guerre de subvention', 'somme nulle', 'represaille', 'escalade'],
     "limite : risque de guerre de subventions et de représailles")],
 'ch23-questi-94': [
   k(['bien commun', 'climat', 'sante', 'securite', 'cohesion'],
     "la protection est justifiée par des biens communs"),
   k(['vuillemey', 'action collective', 'cout cache'],
     "Vuillemey : préserver une capacité d'action collective"),
   k(['rodrik', 'productiviste', 'paradigme'],
     "Rodrik : l'émergence d'un paradigme productiviste"),
   k(['emlinger', 'guimbard', 'lefebvre', 'hierarchie'],
     "Emlinger, Guimbard et Lefebvre : une nouvelle hiérarchie des objectifs"),
   k(['difficile', 'contestable', 'pretexte', 'ambigu', 'legitim'],
     "ces justifications sont plus difficiles à contester, donc ambivalentes")],
 'ch23-questi-95': [
   k(['bloc', 'recomposition', 'reorient', 'alliance'],
     "une recomposition du commerce par blocs politiques"),
   k(['securite', 'alliance', 'friend-shoring', 'friend shoring'],
     "selon des critères de sécurité et d'alliance"),
   k(['approvisionnement', 'leadership', 'technologique', 'arsenalisation'],
     "sécurisation des approvisionnements et arsenalisation de l'interdépendance"),
   k(['negoci', 'bilateral', 'accord'],
     "stratégie 1 : négocier des accords bilatéraux"),
   k(['diversif', 'mercosur', 'inde', 'canada'],
     "stratégie 2 : diversifier ses partenaires"),
   k(['rapport de force', 'chine', 'terre rare', 'retorsion'],
     "stratégie 3 : le rapport de force, comme la Chine")],
}

# Les corrigés rédigés d'origine sont conservés comme réponses modèles : seule
# la grille d'évaluation est ajoutée (batir_banque complète alors « modele »).
for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'cles': _c}

from qz23n1 import L as _N1
from qz23n2 import L as _N2
from qz23n3 import L as _N3
from qz23n4 import L as _N4

NEW = _N1 + _N2 + _N3 + _N4
