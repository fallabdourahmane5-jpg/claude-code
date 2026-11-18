# -*- coding: utf-8 -*-
"""Carte mentale et fiche méthode du chapitre 5 de deuxième année (clé 25).

La structure reprend exactement celle de la carte mentale transmise : neuf
branches et leurs sous-branches. Les feuilles sont détaillées à partir du
document de cours.
"""

VMAP = {
 'title': "Deuxième année, chapitre 5 — L’équilibre macroéconomique : IS-LM, "
          "IS-LM-BP et OG-DG",
 'core': "L’équilibre macroéconomique",
 'branches': [

  {'title': "Introduction et modélisation économique", 'children': [
    {'title': "Représentation simplifiée du réel", 'children': [
      "Un modèle est une représentation abstraite construite sur des hypothèses",
      "Sa pertinence dépend des hypothèses retenues, pas de son réalisme descriptif",
      "Les hypothèses fixent les comportements, la coordination et les conditions d’équilibre",
      "Max Weber : l’idéal-type accentue certains traits du réel pour l’analyser",
      "Concurrence pure et parfaite et monopole pur sont deux idéaux-types"]},
    {'title': "Diversité des modèles de croissance", 'children': [
      "Harrod-Domar : l’investissement stimule la demande et accroît les capacités",
      "Rien ne garantit que demande et capacités progressent au même rythme",
      "Croissance potentiellement instable, avec déséquilibres cumulatifs",
      "Solow (1956) : les rendements décroissants font converger vers un état stationnaire",
      "Deux modèles du même objet concluent différemment : les hypothèses décident"]},
    {'title': "Coordination par les marchés", 'children': [
      "Révolution marginaliste dès les années 1870 : choix rationnels sous contrainte",
      "Alfred Marshall, Principles of Economics (1890) : équilibre partiel",
      "Marshall : districts industriels et économies externes, prolongés par Krugman",
      "Arthur Pigou, The Economics of Welfare (1920) : externalités et taxe pigouvienne",
      "Pigou, The Theory of Unemployment (1933) : chômage par rigidité du salaire réel",
      "Léon Walras (1874) : équilibre général, commissaire-priseur et tâtonnement",
      "Vilfredo Pareto : optimum et efficacité allocative, muets sur la répartition"]}]},

  {'title': "Révolution keynésienne et circuit économique", 'children': [
    {'title': "Loi des débouchés de Say", 'children': [
      "Jean-Baptiste Say, Traité d’économie politique (1803)",
      "« Toute offre crée sa propre demande » : la production distribue les revenus",
      "La monnaie est un intermédiaire des échanges, non une richesse recherchée",
      "Une insuffisance durable de la demande devient difficile à expliquer"]},
    {'title': "Rupture de Keynes (1936)", 'children': [
      "Théorie générale de l’emploi, de l’intérêt et de la monnaie",
      "Demande effective : les débouchés anticipés commandent production et emploi",
      "Préférence pour la liquidité : la monnaie peut être demandée pour elle-même",
      "Équilibre durable de sous-emploi et chômage involontaire",
      "Ajustement par les quantités lorsque prix et salaires sont rigides"]},
    {'title': "Représentation sous forme de circuit", 'children': [
      "François Quesnay, Tableau économique (1758) : flux entre classes sociales",
      "Flux réels : biens, services et facteurs de production",
      "Flux monétaires : paiements et revenus associés",
      "Production → revenus → dépenses → demande → production"]}]},

  {'title': "Comptabilité nationale et agrégats", 'children': [
    {'title': "Mesure de l’activité économique", 'children': [
      "Simon Kuznets et le revenu national américain dans les années 1930",
      "La crise de 1929 impose de mesurer l’activité globale",
      "PIB réel américain : − 25 à − 30 % entre 1929 et 1933 selon les séries"]},
    {'title': "Trois approches du PIB", 'children': [
      "Production : somme des valeurs ajoutées + impôts − subventions sur les produits",
      "Valeur ajoutée = production − consommations intermédiaires",
      "Demande : PIB = C + I + G + X − M",
      "Revenus : rémunérations + EBE + revenu mixte + impôts nets de subventions",
      "Les trois approches donnent le même PIB, aux ajustements statistiques près"]},
    {'title': "Équilibre emplois-ressources", 'children': [
      "Économie ouverte : PIB + M = C + I + G + X",
      "Économie fermée sans État : Y = C + I et Y = C + S, donc I = S",
      "Distinguer l’égalité comptable ex post et l’égalité des grandeurs désirées"]}]},

  {'title': "Équilibre en économie fermée (modèle simple)", 'children': [
    {'title': "Diagramme à 45° de Samuelson (1949)", 'children': [
      "La bissectrice rassemble les points où le revenu égale la demande",
      "Fonction de consommation C = C₀ + cY",
      "Propension marginale à consommer c = ΔC / ΔY, comprise entre 0 et 1",
      "Loi psychologique fondamentale : la consommation croît moins vite que le revenu",
      "Investissement autonome I = I₀ dans la version simplifiée",
      "Revenu d’équilibre Yₑ = (C₀ + I₀) / (1 − c)"]},
    {'title': "Dysfonctionnements macroéconomiques", 'children': [
      "Équilibre de sous-emploi : Y’ < Yₑ alors que production = demande",
      "Écart inflationniste : Y’’ > Yₑ et tensions sur les capacités",
      "Surchauffe : rareté de la main-d’œuvre, salaires puis prix en hausse",
      "Écart de production : output gap négatif ou positif",
      "Arthur Okun (1962) : produire sous son potentiel élève le chômage"]},
    {'title': "Comportements et anticipations", 'children': [
      "L’investissement dépend des débouchés anticipés, pas de la situation présente",
      "Récession → anticipations pessimistes → investissement ↓ → revenus ↓ → demande ↓",
      "Prophétie autoréalisatrice : l’anticipation produit la situation anticipée",
      "D’où la nécessité d’une impulsion publique pour sortir du cercle vicieux"]},
    {'title': "Marché du travail néoclassique", 'children': [
      "Offre de travail croissante avec le salaire réel",
      "Demande de travail décroissante avec le salaire réel",
      "Chômage = excès d’offre lorsque le salaire réel est trop élevé",
      "Remède supposé : la flexibilité du salaire réel (Pigou)",
      "Keynes inverse le raisonnement : c’est la demande globale qui manque"]}]},

  {'title': "Multiplicateurs en économie fermée", 'children': [
    {'title': "Principe du multiplicateur", 'children': [
      "Richard Kahn (1931) puis Keynes (1936)",
      "Diffusion par vagues successives de revenus : 100, puis 80, 64, 51,2…",
      "L’épargne est la fuite qui atténue le processus : s = 1 − c",
      "Avec c = 0,8, une dépense de 100 produit 500 de revenu : k = 5",
      "L’investissement engendre lui-même l’épargne correspondante : ΔS = ΔI = 100"]},
    {'title': "Multiplicateurs budgétaires", 'children': [
      "Multiplicateur d’investissement kI = 1 / (1 − c)",
      "Multiplicateur de dépenses publiques kG = 1 / (1 − c) = 5",
      "Multiplicateur des prestations sociales kF = c / (1 − c) = 4",
      "Multiplicateur fiscal kT = − c / (1 − c) = − 4",
      "Les transferts transitent par le revenu disponible : première vague de 80 seulement"]},
    {'title': "Efficacité et redistribution", 'children': [
      "Supériorité des dépenses publiques directes dans le modèle simple",
      "Le choix dépend aussi de la situation et des objectifs sociaux poursuivis",
      "Redistribution verticale vers les ménages à forte propension à consommer",
      "Keynes privilégie l’investissement public, qui accroît aussi les capacités"]},
    {'title': "Ouverture internationale", 'children': [
      "Propension marginale à importer m = ΔM / ΔY",
      "Multiplicateur en économie ouverte k = 1 / (1 − c + m)",
      "L’ouverture fait passer le multiplicateur de 5 à 2 dans l’exemple du cours",
      "Deuxième fuite : les importations profitent aux producteurs étrangers",
      "Argument protectionniste conjoncturel, à confronter à ses coûts",
      "Passager clandestin et intérêt d’une coordination des relances"]}]},

  {'title': "Le modèle IS-LM", 'children': [
    {'title': "Construction historique", 'children': [
      "John Hicks (1937), Econometrica : formalisation de l’équilibre simultané",
      "Alvin Hansen (1941), Fiscal Policy and Business Cycles",
      "Tradition Hicks-Hansen et synthèse néoclassique",
      "Trois hypothèses : monnaie active, court terme, niveau général des prix fixe"]},
    {'title': "La courbe IS", 'children': [
      "Investment-Saving : couples (Y, r) équilibrant le marché des biens",
      "Pente décroissante : r ↓ → investissement ↑ → demande ↑ → revenu ↑"]},
    {'title': "La courbe LM", 'children': [
      "Liquidity preference-Money supply : couples (Y, r) équilibrant la monnaie",
      "Motif de transaction et motif de précaution : fonction croissante du revenu",
      "Motif de spéculation : fonction décroissante du taux d’intérêt",
      "Effet balançoire entre taux d’intérêt et cours des obligations",
      "Trappe à liquidité : phase horizontale, politique monétaire inefficace",
      "Zone classique : phase verticale, demande spéculative négligeable"]},
    {'title': "Équilibre simultané", 'children': [
      "L’intersection détermine le revenu Y* et le taux d’intérêt r*",
      "Compatibilité de la sphère réelle et de la sphère monétaire",
      "Le taux d’intérêt assure la transmission entre les deux sphères",
      "Cet équilibre ne garantit pas le plein emploi"]}]},

  {'title': "Politiques économiques et policy mix", 'children': [
    {'title': "Politique budgétaire", 'children': [
      "Expansionniste : IS se déplace vers la droite",
      "Restrictive : IS se déplace vers la gauche",
      "Déplacement parallèle, la pente dépendant de comportements inchangés",
      "Effet d’éviction : revenu ↑ → demande de monnaie ↑ → r ↑ → investissement privé ↓",
      "Éviction nulle en trappe à liquidité, totale en zone classique"]},
    {'title': "Politique monétaire", 'children': [
      "Expansionniste : LM se déplace vers la droite, r baisse, investissement ↑",
      "Restrictive : LM se déplace vers la gauche, r monte, investissement ↓",
      "Le modèle à prix fixes ne représente pas directement la désinflation"]},
    {'title': "Exemples historiques de policy mix", 'children': [
      "Clinton-Greenspan : consolidation budgétaire et monnaie accommodante",
      "Solde américain : − 4,5 % du PIB en 1992, + 0,8 % en 1998",
      "Réunification allemande (1990) : relance budgétaire et Bundesbank restrictive",
      "Taux courts allemands : 4,3 % en 1988, 9,2 % en 1991",
      "Zone euro : politique monétaire unique et budgets nationaux encadrés"]}]},

  {'title': "Critiques du modèle IS-LM et modèles alternatifs", 'children': [
    {'title': "Critiques post-keynésiennes", 'children': [
      "Hicks et Hansen auraient privilégié l’équilibre sur le processus",
      "Distinguer l’équilibre ex ante, décisions séparées, et ex post, grandeurs réalisées",
      "Rôle dynamique du multiplicateur : l’investissement engendre son épargne"]},
    {'title': "Critiques monétaristes et nouveaux classiques", 'children': [
      "Milton Friedman (1957) : hypothèse du revenu permanent",
      "Un transfert perçu comme temporaire est principalement épargné",
      "Robert Barro (1974) : équivalence ricardienne ou effet Ricardo-Barro",
      "Taux de chômage naturel : la demande ne l’abaisse pas durablement",
      "Relance au plein emploi : prix ↑ → offre réelle de monnaie ↓ → LM gauche → éviction"]},
    {'title': "Le modèle OG-DG", 'children': [
      "Offre globale et demande globale déterminent production et niveau des prix",
      "Courbe de Phillips (1958), Lipsey (1960), Samuelson et Solow (1960)",
      "Stagflation des années 1970 après les chocs pétroliers",
      "Choc d’offre négatif : OG vers la gauche, prix ↑ et production ↓",
      "OCDE 1975 : croissance − 1,0 % en France, inflation 11,7 %",
      "Retour des politiques d’offre et de la croissance potentielle (Romer, 1986)"]}]},

  {'title': "Le modèle IS-LM-BP (Mundell-Fleming)", 'children': [
    {'title': "Équilibre extérieur et courbe BP", 'children': [
      "J. Marcus Fleming (1962) et Robert Mundell (1963)",
      "Balance globale = solde courant + mouvements autonomes de capitaux",
      "Pente croissante : Y ↑ → importations ↑ → besoin de capitaux → r ↑",
      "Au-dessus de BP : excédent ; en dessous : déficit",
      "Mobilité parfaite des capitaux : BP horizontale, r = r*",
      "Globalisation financière et trois D d’Henri Bourguinat"]},
    {'title': "Politiques économiques en économie ouverte", 'children': [
      "Changes fixes : l’ajustement passe par LM, interventions de la banque centrale",
      "Changes fixes et mobilité parfaite : budgétaire très efficace, monétaire inefficace",
      "Changes flexibles : l’ajustement passe par IS, via les exportations nettes",
      "Changes flexibles et mobilité parfaite : monétaire très efficace, budgétaire inefficace",
      "Effet d’éviction par le taux de change",
      "Triangle des incompatibilités de Mundell et règle d’affectation",
      "Dilemmes interne/externe, contrainte extérieure et tournant de la rigueur de 1983"]}]},
 ],
}

MAP = {
 'title': "Deuxième année, chapitre 5 — L’équilibre macroéconomique : IS-LM, "
          "IS-LM-BP et OG-DG",
 'sub': "Modèles et hypothèses · circuit et comptabilité nationale · diagramme à "
        "45° et multiplicateurs · courbes IS et LM · politiques conjoncturelles et "
        "policy mix · critiques monétaristes et modèle OG-DG · Mundell-Fleming et "
        "contrainte extérieure.",
 'core': "L’équilibre macroéconomique",
 'branches': [],
 'legend': [
  {'k': "Auteurs",
   'v': "Weber, Harrod, Domar, Solow, Marshall, Pigou, Walras, Pareto, Say, "
        "Quesnay, Keynes, Kuznets, Delas, Hicks, Hansen, Fleming, Mundell, Kahn, "
        "Samuelson, Okun, Phillips, Lipsey, Friedman, Barro, Romer, Bourguinat, "
        "Jacques Généreux."},
  {'k': "Pièges",
   'v': "Consommation autonome ≠ consommation incompressible ; propension marginale "
        "à importer ≠ ratio importations / PIB ; égalité ex post entre épargne et "
        "investissement ≠ égalité des grandeurs désirées ex ante ; le multiplicateur "
        "fiscal est négatif, mais une baisse d’impôts augmente le revenu ; la courbe "
        "de Phillips originelle relie chômage et salaires nominaux, pas directement "
        "l’inflation ; équilibre macroéconomique ≠ plein emploi ; trappe à liquidité "
        "(LM horizontale) ≠ zone classique (LM verticale) ; balance des paiements "
        "comptablement équilibrée ≠ équilibre de chacun de ses soldes ; un excédent "
        "courant peut coexister avec une balance globale déficitaire."},
  {'k': "Chiffres",
   'v': "c = 0,8 → kG = 5, kF = 4, kT = − 4 ; ouverture : multiplicateur de 5 à 2 ; "
        "PIB américain − 25 à − 30 % entre 1929 et 1933 ; OCDE 1975 : croissance "
        "− 1,0 % en France et inflation 11,7 % ; États-Unis − 4,5 % du PIB en 1992 et "
        "+ 0,8 % en 1998 ; taux courts allemands 4,3 % en 1988 et 9,2 % en 1991 ; "
        "inflation française 13 % en 1981 ; critères de Maastricht 3 % et 60 % ; "
        "budget européen un peu plus de 1 % du RNB."},
 ],
}

METHODE = (
 '<div class="nb"><h2>✏️ Méthode — Deuxième année, chapitre 5</h2>'
 '<h3>Réflexes de copie</h3><ul>'
 '<li><strong>Toujours nommer le modèle avant de l’utiliser</strong> : IS-LM '
 'détermine Y et r à prix fixes en économie fermée, OG-DG détermine Y et P, '
 'IS-LM-BP ajoute l’équilibre extérieur. Un correcteur sanctionne moins une '
 'démonstration incomplète qu’un modèle mobilisé hors de son domaine.</li>'
 '<li><strong>Deux courbes, deux politiques</strong> : la politique budgétaire '
 'déplace IS, la politique monétaire déplace LM. Dire dans quel sens, et '
 'pourquoi, suffit à structurer un paragraphe entier.</li>'
 '<li><strong>Distinguer l’équilibre et le plein emploi</strong> : l’apport de '
 'Keynes n’est pas que le marché ne s’équilibre pas, c’est qu’il s’équilibre à '
 'un niveau d’activité insuffisant. La phrase « équilibre de sous-emploi » doit '
 'être justifiée, jamais posée.</li>'
 '<li><strong>Ex ante / ex post</strong> : l’égalité comptable entre épargne et '
 'investissement réalisés est toujours vraie ; l’égalité entre grandeurs '
 'désirées est une condition d’équilibre. Confondre les deux ruine le '
 'raisonnement sur le multiplicateur.</li>'
 '<li><strong>Chiffrer le multiplicateur</strong> : avec c = 0,8, kG = 5, '
 'kF = 4, kT = − 4, et l’ouverture ramène le multiplicateur à 2. Trois nombres '
 'suffisent à montrer que l’on maîtrise le mécanisme et sa limite.</li>'
 '<li><strong>En économie ouverte, annoncer le régime de change et la mobilité '
 'des capitaux avant de conclure</strong> : en mobilité parfaite, changes fixes '
 'favorisent le budgétaire, changes flexibles le monétaire. Conclure sans poser '
 'ces deux hypothèses est la faute la plus fréquente.</li></ul>'
 '<h3>Trois plans types</h3><ul>'
 '<li><strong>« Les politiques conjoncturelles sont-elles encore efficaces ? »</strong> '
 'I. Le modèle IS-LM fonde leur efficacité (multiplicateur, policy mix, trappe à '
 'liquidité) — II. Les critiques en montrent les limites (éviction, revenu '
 'permanent, équivalence ricardienne, chômage naturel) — III. Leur efficacité est '
 'conditionnelle : configuration des courbes, régime de change, coordination '
 'internationale.</li>'
 '<li><strong>« L’ouverture prive-t-elle les États de leurs instruments ? »</strong> '
 'I. L’ouverture affaiblit le multiplicateur et impose une contrainte extérieure '
 '(1981-1983) — II. Elle redistribue l’efficacité des instruments selon le régime '
 'de change (Mundell-Fleming, triangle des incompatibilités) — III. Elle déplace '
 'l’enjeu vers la coordination et les politiques structurelles.</li>'
 '<li><strong>« Faut-il préférer les politiques d’offre aux politiques de '
 'demande ? »</strong> I. La demande commande l’activité à court terme (Keynes, '
 'multiplicateur, 2008) — II. La stagflation et le niveau potentiel limitent les '
 'politiques de demande (OG-DG, chômage naturel) — III. L’articulation dépend de '
 'l’écart de production : soutenir la demande quand l’output gap est négatif, agir '
 'sur l’offre quand la contrainte est structurelle.</li></ul>'
 '<h3>Phrases à réutiliser</h3><ul>'
 '<li>« L’équilibre macroéconomique n’est pas l’équilibre de plein emploi : '
 'l’économie peut se stabiliser à un niveau d’activité qui laisse une partie de '
 'la main-d’œuvre inemployée. »</li>'
 '<li>« Le multiplicateur ne mesure pas la générosité d’une relance mais la '
 'longueur du circuit qu’elle parcourt avant de fuir par l’épargne et les '
 'importations. »</li>'
 '<li>« En mobilité parfaite des capitaux, le régime de change ne change pas '
 'seulement l’intensité des politiques conjoncturelles : il en inverse '
 'l’efficacité relative. »</li></ul></div>')
