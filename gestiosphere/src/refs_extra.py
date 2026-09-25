"""Compléments pour l'onglet « Auteurs & références » (fusionnés au build).

Pour chaque référence :
- famille : auteur | ouvrage | texte | organisme (sert aux filtres) ;
- apport : ce que la référence apporte concrètement à ton cours ;
- quand : dans quel type de question ou d'exercice la mobiliser ;
- phrase : formule prête à réutiliser en copie (complète les phrases vides) ;
- cles : mots cherchés dans le cours, les définitions et les sujets pour trouver
  les passages et les notions liés.
"""

REFS = {
    # ---------------- Comptabilité ----------------
    'Plan comptable général (PCG)': dict(
        famille='texte',
        apport="C'est la « grammaire » de tout le cours : numéros de comptes, sens des soldes, règle du 8 (amortissements) et du 9 (dépréciations) en deuxième position, postes du bilan et du compte de résultat.",
        quand="Dans chaque écriture : choisir le bon compte, justifier une présentation au bilan, expliquer pourquoi une dépréciation est en 29, 39, 49 ou 59.",
        cles=['PCG', 'plan comptable', 'plan de comptes']),
    'Code de commerce': dict(
        famille='texte',
        apport="Fonde l'obligation d'inventaire annuel et les principes d'image fidèle, de régularité et de sincérité : c'est la raison d'être des travaux de clôture.",
        quand="En introduction d'une question sur l'inventaire ou les comptes annuels, ou pour justifier qu'une perte probable doit être constatée (prudence).",
        cles=['Code de commerce', 'image fidèle', 'sincères', 'inventaire']),
    'Code général des impôts': dict(
        famille='texte',
        apport="Fixe les coefficients du dégressif (1,25 / 1,75 / 2,25) et les règles de déduction : c'est l'écart entre fiscal et comptable qui crée les amortissements dérogatoires.",
        quand="Dès qu'un exercice parle de dégressif, de dérogatoire (145, 6872, 7872) ou de provision déductible.",
        cles=['fiscal', 'dégressif', 'dérogatoire', 'coefficient']),
    'Luca Pacioli': dict(
        famille='auteur',
        apport="Explique d'où vient la règle débit = crédit que tu appliques à chaque écriture : elle n'est pas arbitraire, elle garantit l'équilibre de la balance.",
        quand="Pour une introduction historique ou pour justifier l'égalité débit / crédit et le contrôle par la balance.",
        cles=['partie double', 'débit', 'crédit']),
    'Ordonnance du commerce (Colbert)': dict(
        famille='texte',
        apport="Montre que l'inventaire est une obligation ancienne, reprise aujourd'hui par le Code de commerce.",
        quand="En accroche historique d'une question sur l'inventaire ou la clôture.",
        cles=['inventaire', 'livres']),
    'Autorité des normes comptables (ANC)': dict(
        famille='organisme',
        apport="C'est l'auteur du PCG que tu utilises (règlement ANC 2014-03) : quand on dit « le PCG impose », c'est l'ANC qui l'a écrit.",
        quand="Pour citer précisément la source d'une règle comptable.",
        phrase="« Le règlement ANC n° 2014-03 relatif au PCG fixe les règles de comptabilisation et de présentation des comptes annuels. »",
        cles=['ANC', 'règlement', 'normalisation']),
    # ---------------- Microéconomie ----------------
    'Robert Pindyck et Daniel Rubinfeld': dict(
        famille='ouvrage',
        apport="Le manuel de référence du cours : mêmes notions, mêmes graphiques (contrainte budgétaire, courbes d'indifférence, isoquantes, coûts), avec beaucoup d'exemples chiffrés.",
        quand="Pour relire une notion mal comprise avec d'autres exemples, ou pour vérifier une représentation graphique.",
        phrase="« Comme le montrent Pindyck et Rubinfeld, le consommateur choisit le panier qui maximise sa satisfaction compte tenu de sa contrainte budgétaire. »",
        cles=['Pindyck', 'Rubinfeld']),
    'Pierre Picard': dict(
        famille='ouvrage',
        apport="Plus formalisé que Pindyck : utile pour la résolution par le Lagrangien, les conditions du premier ordre et les démonstrations.",
        quand="Quand un exercice demande une résolution mathématique complète (Lagrangien, dérivées partielles).",
        phrase="« La résolution par le Lagrangien (Picard) conduit à l'égalité entre le TMS et le rapport des prix. »",
        cles=['Picard', 'Lagrangien']),
    'Pierre Picard et Bruno Jullien': dict(
        famille='ouvrage',
        apport="Le recueil d'exercices corrigés associé : même type de questions que tes TD (optimum, demande, coûts), avec corrections détaillées.",
        quand="Pour s'entraîner avant un partiel, après avoir fait les sujets de l'onglet Sujets corrigés.",
        phrase="« On retrouve ici le raisonnement type des exercices de Picard et Jullien : conditions du premier ordre, puis contrainte saturée. »",
        cles=['Jullien', 'exercices']),
    'John Hicks': dict(
        famille='auteur',
        apport="Donne la méthode de décomposition utilisée dans le cours : effet de substitution à utilité constante, puis effet de revenu. ES + ER = ET.",
        quand="Dans toute question « décomposez l'effet d'une variation de prix », et pour expliquer les biens de Giffen.",
        cles=['Hicks', 'effet de substitution', 'effet de revenu', 'effet total']),
    'Robert Giffen': dict(
        famille='auteur',
        apport="Cas limite de la théorie : un bien inférieur dont l'effet revenu l'emporte sur l'effet de substitution, si bien que la demande monte avec le prix.",
        quand="Pour classer un bien selon son élasticité-prix, ou commenter une demande croissante avec le prix.",
        phrase="« Un bien de Giffen est un bien inférieur dont l'effet revenu, positif, domine l'effet de substitution : sa demande augmente quand son prix augmente. »",
        cles=['Giffen', 'bien inférieur']),
    'Thorstein Veblen': dict(
        famille='auteur',
        apport="Autre cas de demande croissante avec le prix, mais pour une raison différente de Giffen : le prix élevé signale un statut.",
        quand="Pour distinguer Veblen de Giffen dans une question de cours ou un QCM.",
        phrase="« Avec l'effet Veblen, le prix élevé fait partie de ce qui est acheté : il signale un statut social. »",
        cles=['Veblen', 'ostentatoire']),
    'Ernst Engel': dict(
        famille='auteur',
        apport="Relie consommation et revenu : la courbe d'Engel se lit sur le chemin d'expansion du revenu et permet de classer bien normal, inférieur, de luxe.",
        quand="Dans une question sur l'élasticité-revenu ou la courbe consommation-revenu.",
        phrase="« Selon la loi d'Engel, la part du budget consacrée à l'alimentation diminue quand le revenu augmente : son élasticité-revenu est inférieure à 1. »",
        cles=['Engel', 'élasticité-revenu', 'consommation-revenu']),
    'Joseph-Louis Lagrange': dict(
        famille='auteur',
        apport="L'outil mathématique des deux grands programmes du cours : maximiser l'utilité sous contrainte de budget, minimiser le coût sous contrainte de production.",
        quand="Dès qu'on te demande de résoudre un programme d'optimisation « sous contrainte ».",
        phrase="« On forme le Lagrangien L = U(x1, x2) + λ(R − p1x1 − p2x2) ; les conditions du premier ordre donnent TMS = p1/p2. »",
        cles=['Lagrange', 'Lagrangien', 'multiplicateur']),
    'Charles Cobb et Paul Douglas': dict(
        famille='auteur',
        apport="La forme fonctionnelle de presque tous tes exercices. Ses propriétés (TMS simple, rendements d'échelle lus sur α + β) rendent les calculs rapides.",
        quand="Pour reconnaître les rendements d'échelle (α + β > 1, = 1, < 1) ou utiliser les parts de budget fixes (x1 = αR/p1 quand α + β = 1).",
        phrase="« Avec une fonction de Cobb-Douglas y = K^α·L^β, les rendements d'échelle sont croissants si α + β > 1. »",
        cles=['Cobb', 'Douglas', 'Cobb-Douglas']),
    'Léon Walras': dict(
        famille='auteur',
        apport="Donne l'idée d'ajustement par les prix : un excès d'offre fait baisser le prix, un excès de demande le fait monter, jusqu'à l'équilibre.",
        quand="Pour expliquer le retour à l'équilibre d'un marché ou introduire l'interdépendance des marchés.",
        phrase="« Dans la logique walrasienne, le prix s'ajuste jusqu'à égaliser l'offre et la demande. »",
        cles=['Walras', 'équilibre', 'excès d']),
    'Alfred Marshall': dict(
        famille='auteur',
        apport="Le cadre du « marché » du chapitre 0 : offre, demande, équilibre partiel (un seul marché, le reste inchangé) et élasticité.",
        quand="Pour définir l'équilibre partiel, raisonner « toutes choses égales par ailleurs » ou introduire l'élasticité.",
        phrase="« Dans l'analyse d'équilibre partiel de Marshall, on étudie un marché isolé, toutes choses égales par ailleurs. »",
        cles=['Marshall', 'équilibre partiel', 'élasticité']),
    'Vilfredo Pareto': dict(
        famille='auteur',
        apport="Justifie l'approche ordinale du cours : on n'a pas besoin de mesurer l'utilité, seulement de classer les paniers avec des courbes d'indifférence.",
        quand="Dans une question « utilité cardinale ou ordinale ? » ou pour introduire les courbes d'indifférence.",
        phrase="« Depuis Pareto, l'utilité est ordinale : seules comptent les préférences entre paniers, représentées par des courbes d'indifférence. »",
        cles=['Pareto', 'ordinale', 'indifférence']),
    # ---------------- Marketing ----------------
    'American Marketing Association (AMA)': dict(
        famille='organisme',
        apport="Fournit la définition « officielle » du marketing, centrée sur la création et l'échange de valeur pour le client.",
        quand="En introduction de toute copie de marketing : définir le terme avant de raisonner.",
        phrase="« Selon l'AMA, le marketing est l'ensemble des activités et processus qui créent, communiquent et délivrent de la valeur aux clients. »",
        cles=['AMA', 'valeur']),
    'Mercator (J. Lendrevie, J. Lévy, D. Lindon)': dict(
        famille='ouvrage',
        apport="La définition de référence en France : le marketing comme effort d'adaptation aux marchés concurrentiels par une valeur perçue supérieure.",
        quand="Pour définir le marketing ou la valeur perçue ; utile aussi pour structurer une réponse autour de l'offre et de la concurrence.",
        cles=['Mercator', 'valeur perçue', 'adaptation']),
    'Abraham Maslow': dict(
        famille='auteur',
        apport="Aide à analyser les besoins et les motivations du consommateur : à quel niveau de besoin répond le produit ?",
        quand="Dans une question sur les besoins, les motivations d'achat ou le positionnement d'une offre.",
        phrase="« Selon Maslow, les besoins sont hiérarchisés : un besoin supérieur (estime, accomplissement) ne motive que si les besoins de base sont satisfaits. »",
        cles=['Maslow', 'besoin', 'pyramide']),
    'Michael Porter': dict(
        famille='auteur',
        apport="Deux outils majeurs du chapitre 2 : les 5 (+1) forces pour mesurer l'attractivité d'un secteur, et les stratégies génériques pour construire un avantage concurrentiel.",
        quand="Dans l'analyse externe (environnement concurrentiel) d'une étude de cas, ou pour qualifier la stratégie d'une entreprise.",
        cles=['Porter', 'cinq forces', '5 forces', 'domination par les coûts', 'différenciation', 'focalisation']),
    'Learned, Christensen, Andrews et Guth': dict(
        famille='auteur',
        apport="Le modèle SWOT, qui sert de synthèse au diagnostic : il croise l'analyse interne (forces, faiblesses) et externe (opportunités, menaces).",
        quand="En conclusion du diagnostic d'une étude de cas, avant les recommandations.",
        phrase="« Le modèle LCAG (SWOT) croise les forces et faiblesses de l'entreprise avec les opportunités et menaces de son environnement. »",
        cles=['SWOT', 'LCAG', 'forces', 'faiblesses', 'opportunités', 'menaces']),
    'Boston Consulting Group (BCG)': dict(
        famille='organisme',
        apport="La matrice BCG classe les activités (vedettes, vaches à lait, dilemmes, poids morts) ; l'effet d'expérience explique pourquoi la part de marché compte.",
        quand="Pour analyser un portefeuille d'activités et proposer une allocation des ressources.",
        phrase="« Selon la matrice BCG, les vaches à lait financent les dilemmes et les vedettes de demain. »",
        cles=['BCG', 'vache', 'vedette', 'dilemme', 'poids mort', "effet d'expérience"]),
    'Arthur D. Little (ADL)': dict(
        famille='organisme',
        apport="Matrice qui tient compte du cycle de vie de l'activité (démarrage, croissance, maturité, déclin) et de la position concurrentielle.",
        quand="Quand le cas insiste sur la maturité du marché, ou pour nuancer la matrice BCG.",
        phrase="« La matrice ADL croise la maturité du secteur et la position concurrentielle pour apprécier le risque de chaque activité. »",
        cles=['ADL', 'Arthur D. Little', 'maturité']),
    'McKinsey': dict(
        famille='organisme',
        apport="Matrice plus fine que BCG (3 × 3, critères multiples) : elle débouche directement sur des recommandations (investir, maintenir, se retirer).",
        quand="Pour recommander une stratégie par activité à partir de l'attrait du marché et des atouts de l'entreprise.",
        phrase="« La matrice McKinsey combine plusieurs critères d'attrait et d'atouts, ce qui la rend plus nuancée que la matrice BCG. »",
        cles=['McKinsey', 'attrait', 'atouts']),
    'Paul R. Smith': dict(
        famille='auteur',
        apport="Le modèle SOSTAC donne un plan type pour une recommandation marketing : de l'analyse de situation au contrôle.",
        quand="Pour structurer un plan marketing ou la partie « recommandations » d'une étude de cas.",
        phrase="« Selon le modèle SOSTAC de P. R. Smith, un plan marketing part de l'analyse de la situation et se termine par le contrôle des résultats. »",
        cles=['SOSTAC', 'Smith']),
    'N. Van Laethem et L. Body': dict(
        famille='ouvrage',
        apport="Source de la typologie des marchés (principal, indirect, générique, support) : elle aide à délimiter le marché d'une entreprise.",
        quand="Quand on te demande de définir le marché d'un produit ou d'identifier les concurrents indirects.",
        phrase="« Selon Van Laethem et Body, le marché d'un produit ne se limite pas au marché principal : il inclut les marchés indirect, générique et support. »",
        cles=['marché principal', 'indirect', 'Van Laethem']),
    'G. Johnson, K. Scholes et al.': dict(
        famille='ouvrage',
        apport="Source de la grille PESTEL et de la démarche de diagnostic (analyse externe + analyse interne → choix stratégiques).",
        quand="Pour structurer l'analyse du macro-environnement d'une étude de cas.",
        phrase="« La grille PESTEL (Johnson, Scholes) passe en revue les facteurs politiques, économiques, socioculturels, technologiques, écologiques et légaux. »",
        cles=['PESTEL', 'Johnson', 'Scholes']),
    'Philip Kotler': dict(
        famille='auteur',
        apport="Situe le marketing dans son histoire (des optiques production et vente à l'optique marketing) et classe les rôles concurrentiels.",
        quand="En introduction (évolution du marketing) ou pour qualifier la position d'une entreprise face à ses concurrents.",
        phrase="« Selon Kotler, l'optique marketing part des besoins du client, là où l'optique vente part du produit à écouler. »",
        cles=['Kotler', 'optique', 'leader', 'challenger']),
    'H. Igor Ansoff': dict(
        famille='auteur',
        apport="La matrice produits / marchés sert à formuler les options de croissance d'une entreprise, de la moins risquée (pénétration) à la plus risquée (diversification).",
        quand="Dans les recommandations : proposer une voie de croissance et en évaluer le risque.",
        phrase="« D'après la matrice d'Ansoff, la diversification, qui combine nouveaux produits et nouveaux marchés, est l'option de croissance la plus risquée. »",
        cles=['Ansoff', 'diversification', 'pénétration']),
}

KIND_FAMILLE = {'auteur': 'Auteurs', 'ouvrage': 'Manuels & ouvrages', 'texte': 'Textes de référence', 'organisme': 'Institutions & cabinets'}


def apply(mats):
    """Fusionne les compléments dans les auteurs ; renvoie les références sans complément."""
    missing = []
    for m in mats:
        for i, a in enumerate(m.get('auteurs', [])):
            a.setdefault('id', f"{m['id']}-a{i}")
            x = REFS.get(a['nom'])
            if not x:
                missing.append(a['nom'])
                continue
            a['famille'] = x['famille']
            a['apport'] = x['apport']
            a['quand'] = x['quand']
            a['cles'] = x['cles']
            if not a.get('phrase') and x.get('phrase'):
                a['phrase'] = x['phrase']
            if not a.get('phrase'):
                missing.append(a['nom'] + ' (phrase)')
    return missing
