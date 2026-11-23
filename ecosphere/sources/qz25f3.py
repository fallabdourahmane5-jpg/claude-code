# -*- coding: utf-8 -*-
"""Chapitre 25 — corrections des questions héritées, sous-parties c25-13 à c25-18."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c25-13
'ch25-qcm-64': f(niv='connaitre', sp='c25-13', b=2891,
 why=["Y et r sont les variables du modèle IS-LM, non les deux revenus de "
      "référence de cette analyse.",
      "IS et LM sont les courbes du modèle, non des niveaux de revenu.",
      "C et S désignent consommation et épargne."],
 diss="Outil d’analyse à retenir : comparer le revenu de plein emploi Ype et "
      "le revenu équilibrant les transactions courantes YBTC permet "
      "d’identifier le dilemme auquel un pays est exposé."),
'ch25-qcm-75': f(niv='appliquer', sp='c25-13', b=2726,
 why=["Vendre sa monnaie contre des devises accentuerait la pression à la "
      "dépréciation.",
      "Laisser la monnaie se déprécier correspond au régime de changes "
      "flexibles, non à la défense d’une parité.",
      "L’augmentation des dépenses publiques est un instrument budgétaire, "
      "étranger à la défense du change."],
 diss="Conséquence monétaire essentielle : la base monétaire diminue, LM se "
      "déplace vers la gauche — la politique monétaire est donc endogène en "
      "changes fixes."),
'ch25-vraifa-98': f(niv='raisonner', sp='c25-13', b=2891),

# =============================================================== c25-14
'ch25-qcm-36': f(niv='connaitre', sp='c25-14', b=2964,
 why=["Mai 1981 est le moment du lancement de la relance, non de son "
      "abandon.",
      "Juin 1982 correspond à une première inflexion, mais le tournant est "
      "postérieur.",
      "Janvier 1986 est bien plus tardif que le choix décisif."],
 diss="Enjeu du choix de mars 1983 : maintenir le franc dans le Système "
      "monétaire européen implique l’abandon de la stratégie de relance."),
'ch25-qcm-37': f(niv='raisonner', sp='c25-14', b=3085,
 why=["Une propension à consommer trop faible n’est pas l’explication "
      "retenue : la demande a bien augmenté.",
      "Les taux d’intérêt bas ne sont pas la cause de l’échec.",
      "Les dépenses publiques ont effectivement augmenté : c’est leur "
      "destination, et non leur montant, qui pose problème."],
 diss="Deux conditions défavorables à citer ensemble : la faiblesse de la "
      "croissance des partenaires et une inflation française déjà élevée, "
      "autour de 13 % en 1981."),
'ch25-qcm-65': f(niv='raisonner', sp='c25-14', b=3051,
 why=["La suppression de la contrainte extérieure est précisément ce que "
      "l’exemple dément.",
      "La trappe à liquidité est au contraire très présente dans l’analyse "
      "du cas japonais.",
      "Le caractère monétaire de l’inflation est une thèse monétariste, "
      "étrangère à cet exemple."],
 diss="Mécanisme à expliciter : monnaie accommodante → attractivité des "
      "placements en yens ↓ → pression à la dépréciation → importations plus "
      "chères."),
'ch25-questi-107': f(niv='raisonner', sp='c25-14', b=2912),

# =============================================================== c25-15
'ch25-qcm-27': f(niv='appliquer', sp='c25-15', b=3159,
 why=["Une grande efficacité de la politique monétaire caractérise au "
      "contraire le régime de changes flexibles.",
      "Une politique monétaire ne déplace pas BP, qui dépend du taux mondial "
      "et de la propension à importer.",
      "La pression est à la dépréciation, non à l’appréciation, puisque le "
      "taux domestique devient inférieur au taux mondial."],
 diss="Enchaînement complet à restituer : LM droite → r < r* → sorties de "
      "capitaux → la banque centrale achète sa monnaie → masse monétaire ↓ → "
      "LM revient à sa position initiale."),
'ch25-qcm-28': f(niv='appliquer', sp='c25-15', b=3212,
 why=["L’inefficacité de la relance budgétaire caractérise le régime de "
      "changes flexibles.",
      "La pression est à l’appréciation, puisque r devient supérieur à r*.",
      "LM se déplace au contraire vers la droite, du fait des achats de "
      "devises de la banque centrale."],
 diss="Résultat central à mémoriser : en changes fixes avec mobilité "
      "parfaite, la politique budgétaire est amplifiée par un accompagnement "
      "monétaire automatique."),
'ch25-qcm-32': f(niv='comprendre', sp='c25-15', b=3224,
 why=["Associer changes fixes et mobilité des capitaux priverait les États "
      "de toute autonomie monétaire, ce que Bretton Woods voulait éviter.",
      "Les changes flexibles sont postérieurs : ils caractérisent le système "
      "d’après 1973.",
      "L’union monétaire avec mobilité des capitaux décrit la zone euro, non "
      "Bretton Woods."],
 diss="Lecture par le triangle : c’est la libre circulation des capitaux qui "
      "est sacrifiée, ce qui permet de concilier les deux autres objectifs."),
'ch25-vraifa-97': f(niv='raisonner', sp='c25-15', b=3224),
'ch25-questi-106': f(niv='raisonner', sp='c25-15', b=3224),

# =============================================================== c25-16
'ch25-qcm-31': f(niv='connaitre', sp='c25-16', b=3327,
 why=["Inflation, chômage et dette sont des objectifs de politique "
      "économique, mais ne constituent pas ce triangle.",
      "Exporter, importer et investir ne sont pas des objectifs "
      "incompatibles.",
      "Taxer, dépenser et emprunter sont des instruments budgétaires."],
 diss="Autre nom à connaître : la trinité impossible — deux objectifs au "
      "maximum peuvent être pleinement conciliés."),

# =============================================================== c25-17
'ch25-qcm-58': f(niv='connaitre', sp='c25-17', b=3597,
 why=["5 % et 90 % ne correspondent à aucun seuil du traité.",
      "1 % et 40 % sous-estiment les deux critères.",
      "Inverser les deux chiffres attribuerait à la dette un seuil de 3 %, "
      "ce qui serait absurde."],
 diss="Repères institutionnels à joindre : traité signé en 1992, entré en "
      "vigueur en 1993, complété par le Pacte de stabilité et de croissance "
      "en 1997 — et ces seuils ne sont pas des interdictions absolues."),
'ch25-qcm-59': f(niv='connaitre', sp='c25-17', b=3630,
 why=["5 % du RNB surestime très largement le budget européen.",
      "10 % correspondrait à un budget de type fédéral.",
      "20 % dépasse même le poids des budgets fédéraux existants."],
 diss="Conséquence analytique majeure : cette faiblesse relative interdit une "
      "stabilisation centralisée comparable à celle d’un État fédéral, ce qui "
      "reporte la charge sur les budgets nationaux."),
'ch25-qcm-60': f(niv='comprendre', sp='c25-17', b=3565,
 why=["Les changes flexibles décrivent la relation de la zone euro avec le "
      "reste du monde, non celle de ses membres entre eux.",
      "L’autarcie supposerait l’absence d’échanges, ce qui est "
      "manifestement faux.",
      "Le flottement administré suppose des interventions sur un taux de "
      "change qui n’existe plus entre membres."],
 diss="Double lecture indispensable : changes fixes à l’intérieur, changes "
      "flexibles à l’extérieur — les deux conclusions de Mundell-Fleming "
      "s’appliquent donc simultanément."),
'ch25-vraifa-94': f(niv='raisonner', sp='c25-17', b=3565),

# =============================================================== c25-18
'ch25-qcm-29': f(niv='appliquer', sp='c25-18', b=3917,
 why=["Une grande efficacité budgétaire caractérise au contraire le régime "
      "de changes fixes.",
      "La politique budgétaire déplace IS, non LM.",
      "La monnaie s’apprécie et ne se déprécie pas, puisque r devient "
      "supérieur à r*."],
 diss="Nom du mécanisme à employer : l’effet d’éviction par le taux de "
      "change, distinct de l’éviction par le taux d’intérêt."),
'ch25-qcm-30': f(niv='appliquer', sp='c25-18', b=3917,
 why=["L’inefficacité monétaire caractérise le régime de changes fixes.",
      "Un effet limité aux prix supposerait une économie au plein emploi, "
      "hypothèse étrangère au modèle.",
      "La politique monétaire ne déplace pas BP, qui dépend du taux mondial."],
 diss="Point remarquable : la politique monétaire agit par deux canaux "
      "cumulatifs, le taux d’intérêt puis le taux de change."),
'ch25-qcm-33': f(niv='comprendre', sp='c25-18', b=3811,
 why=["Inverser l’affectation attribuerait chaque instrument à l’objectif "
      "pour lequel il est le moins efficace.",
      "Utiliser les deux instruments dans le même sens revient à renoncer à "
      "l’idée d’affectation.",
      "Confier les deux instruments à la banque centrale contredit la "
      "séparation institutionnelle des politiques."],
 diss="Principe à énoncer : chaque instrument est affecté à l’objectif pour "
      "lequel il possède l’efficacité relative la plus grande."),
'ch25-qcm-34': f(niv='raisonner', sp='c25-18', b=3809,
 why=["Sous-emploi avec excédent et inflation avec déficit sont précisément "
      "les deux configurations sans dilemme.",
      "Associer deux fois le déficit omet la configuration inflation et "
      "excédent.",
      "Associer deux fois l’inflation omet la configuration sous-emploi et "
      "déficit."],
 diss="Critère de reconnaissance : il y a dilemme lorsque la politique qui "
      "corrige le déséquilibre interne aggrave le déséquilibre externe."),
'ch25-qcm-61': f(niv='appliquer', sp='c25-18', b=3917,
 why=["Affirmer que c’est impossible contredit la définition de la balance "
      "globale.",
      "Le régime de change ne conditionne pas cette possibilité "
      "comptable.",
      "Le niveau de l’inflation n’intervient pas dans ce calcul."],
 diss="Exemple numérique à reproduire : excédent courant de 100 et sorties "
      "de capitaux de 140 donnent une balance globale déficitaire de 40."),
'ch25-qcm-76': f(niv='comprendre', sp='c25-18', b=3917,
 why=["Le multiplicateur décrit la propagation d’une dépense, non "
      "l’ajustement du solde commercial à une dépréciation.",
      "La trappe à liquidité concerne le marché monétaire.",
      "La courbe de Phillips relie chômage et salaires nominaux."],
 diss="Trois déterminants de l’ajustement à citer : les élasticités-prix, les "
      "délais de réaction et le contenu importé des exportations."),
'ch25-questi-104': f(niv='raisonner', sp='c25-18', b=3917),
'ch25-questi-105': f(niv='raisonner', sp='c25-18', b=3917),
'ch25-questi-112': f(niv='raisonner', sp='c25-18', b=3809),
'ch25-questi-120': f(niv='raisonner', sp='c25-18', b=3893),

}
