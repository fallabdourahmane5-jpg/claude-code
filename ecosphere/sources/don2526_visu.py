# -*- coding: utf-8 -*-
"""« Visualisations stratégiques » : mise a jour des themes existants par les
chapitres 5 et 6 de deuxieme annee.

Aucune visualisation nouvelle n'est creee. Seuls les themes auxquels l'un des
deux chapitres apporte reellement un mecanisme, un auteur ou une donnee sont
completes, et toujours sur des noeuds existants : la structure graphique des
visualisations reste inchangee.

Format :
  'cle-visualisation': {
     'ch':      [25] / [26] / [25, 26],
     'lecture': [(titre, texte), ...],          # cles de lecture ajoutees
     'noeuds':  {'id-noeud': {'mec': [...], 'aut': [...], 'faits': [...],
                              'dos': [...]}, ...}
  }
"""

MAJ = {}


def v(cle, ch, lecture=None, noeuds=None):
    MAJ[cle] = {'ch': ch,
                'lecture': [[t, e] for (t, e) in (lecture or [])],
                'noeuds': noeuds or {}}


def n(mec=None, aut=None, faits=None, dos=None):
    return {'mec': [{'t': t, 'e': e} for (t, e) in (mec or [])],
            'aut': [{'n': a, 'i': i} for (a, i) in (aut or [])],
            'faits': [{'f': f, 'p': p} for (f, p) in (faits or [])],
            'dos': list(dos or [])}


# ============================================================ vz-crises
v('vz-crises', [25, 26],
  lecture=[("Le régime de change décide de l’instrument",
            "Les chapitres 5 et 6 de deuxième année ajoutent une condition que le cycle seul ne révèle pas : en changes fixes avec mobilité parfaite des capitaux, la relance budgétaire est amplifiée et la politique monétaire neutralisée ; en changes flexibles, exactement l’inverse. Avant de choisir un instrument, il faut donc avoir identifié non seulement le choc, mais le cadre monétaire international.")],
  noeuds={
   'multiplicateur': n(
     mec=[("Les trois multiplicateurs budgétaires",
           "Avec c = 0,8 : kG = 1 / (1 − c) = 5 pour une dépense publique, kF = c / (1 − c) = 4 pour une prestation sociale, kT = − c / (1 − c) = − 4 pour un impôt. La hiérarchie vient du point d’entrée dans le circuit : une dépense publique est immédiatement une demande, un transfert passe d’abord par le revenu disponible."),
          ("La fuite par les importations",
           "En économie ouverte, M = M₀ + mY et le multiplicateur devient 1 / (1 − c + m) : il passe de 5 à 2 dans l’exemple du cours. Une dépense de 100 ne produit alors plus que 200 de revenu national, le reste profitant aux producteurs étrangers.")],
     aut=[("Richard Kahn",
           "Développe en 1931 le multiplicateur d’emploi, que Keynes généralise en 1936 : l’investissement engendre l’épargne qui lui correspond.")],
     faits=[("Avec s = 0,2 et un revenu supplémentaire de 500, l’épargne engendrée atteint exactement les 100 d’investissement initial.",
             "La causalité keynésienne va donc de l’investissement au revenu puis à l’épargne : l’investissement n’exige pas une épargne préalable équivalente.")],
     dos=['n15-multiplicateur-budgetaire', 'n20-epargne-investissement-ouverte']),
   'budget': n(
     mec=[("L’effet d’éviction limite la relance",
           "Dépenses publiques ↑ → revenu ↑ → demande de monnaie ↑ → taux d’intérêt ↑ → investissement privé ↓. Le revenu atteint Y1 et non Y3 : son intensité dépend de la pente de LM et de la sensibilité de l’investissement au taux.")],
     faits=[("L’effet d’éviction est nul dans une trappe à liquidité, où LM est horizontale, et total dans la zone classique, où LM est verticale.",
             "C’est pourquoi la crise de 2008 a réhabilité le modèle IS-LM : près du plancher des taux, la relance budgétaire retrouve une efficacité élevée.")],
     dos=['n15-effet-eviction', 'n15-trappe-liquidite']),
   'monetaire': n(
     mec=[("Un canal indirect dont chaque maillon peut céder",
           "La politique monétaire modifie un prix, le taux d’intérêt, en espérant que des agents privés en tireront des décisions d’investissement. Le premier maillon cède dans une trappe à liquidité, le deuxième lorsque les anticipations de débouchés sont dégradées, le troisième lorsque le régime de change contraint la banque centrale à défendre une parité.")],
     dos=['n15-politique-monetaire', 'n11-preference-liquidite']),
   'limites': n(
     mec=[("Trois critiques, trois canaux distincts",
           "L’effet d’éviction porte sur l’investissement, par le marché monétaire. Le revenu permanent de Friedman (1957) porte sur la consommation : un transfert jugé temporaire est largement épargné. L’équivalence ricardienne de Barro (1974) porte sur le financement : l’épargne privée compense la désépargne publique.")],
     aut=[("Milton Friedman",
           "Le taux de chômage naturel (1968) borne ce qu’une politique de demande peut obtenir sur l’emploi : elle n’obtient au-delà qu’une accélération de l’inflation."),
          ("Robert Barro",
           "Formule l’équivalence ricardienne en 1974, mais montre en 1990 que les infrastructures publiques productives soutiennent la croissance de long terme.")],
     faits=[("Au plein emploi, la hausse des prix réduit l’offre réelle de monnaie, déplace LM vers la gauche et ramène l’économie à son potentiel avec un taux d’intérêt plus élevé.",
             "C’est la démonstration monétariste : la relance n’a produit qu’une recomposition de la demande au détriment du secteur privé et une hausse des prix.")],
     dos=['n15-politique-relance', 'n11-neutralite-monnaie']),
   'choc': n(
     faits=[("En 1975, la croissance est de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec des inflations de 11,7 %, 5,9 % et 9,1 % (OCDE).",
             "Le choc d’offre déplace l’offre globale de court terme vers la gauche : la production baisse et les prix montent, configuration que l’arbitrage inflation-chômage ne permettait pas d’expliquer.")],
     dos=['n14-courbe-phillips']),
   'regime': n(
     mec=[("La symétrie inversée de Mundell-Fleming",
           "En changes fixes avec mobilité parfaite, une relance budgétaire est amplifiée par l’accompagnement monétaire qu’exige la défense de la parité, tandis que l’expansion monétaire est intégralement neutralisée. En changes flexibles, le budget est neutralisé par l’appréciation et la monnaie amplifiée par la dépréciation.")],
     aut=[("Robert Mundell",
           "Le triangle des incompatibilités : changes fixes, mobilité des capitaux et autonomie monétaire ne peuvent être pleinement conciliés."),
          ("Jacques Généreux",
           "Les dilemmes se lisent par l’écart entre le revenu de plein emploi Ype et le revenu équilibrant les transactions courantes YBTC.")],
     faits=[("La France de 1981-1983 : inflation d’environ 14 % au début de 1982, trois dévaluations subies en octobre 1981, juin 1982 et mars 1983, puis tournant de la rigueur.",
             "L’épisode illustre la contrainte extérieure : l’objectif externe finit par l’emporter sur l’objectif interne.")],
     dos=['n15-contrainte-exterieure', 'n20-changes-fixes-flottants']),
  })

# ========================================================= vz-financement
v('vz-financement', [25, 26],
  lecture=[("La monnaie comme actif, et non seulement comme instrument",
            "Le chapitre 5 de deuxième année ajoute la préférence pour la liquidité : trois motifs de détention — transaction et précaution, croissants avec le revenu, spéculation, décroissante avec le taux d’intérêt — font du taux d’intérêt le prix de la renonciation à la liquidité. Le chapitre 6 ajoute la dimension externe : le marché des changes, marché-réseau mondial et quasi continu, est devenu le lieu où le prix des monnaies se forme, largement déconnecté des échanges réels.")],
  noeuds={
   'monnaie': n(
     mec=[("La préférence pour la liquidité et l’effet balançoire",
           "Une hausse du taux d’intérêt fait baisser le prix des obligations existantes. Un taux jugé anormalement bas fait donc anticiper sa remontée, donc une perte en capital, ce qui pousse à détenir de la monnaie plutôt que des titres : c’est le fondement du motif de spéculation.")],
     dos=['n11-preference-liquidite', 'n11-liquidite']),
   'bc': n(
     mec=[("L’asymétrie des interventions de change",
           "Pour freiner une appréciation, la banque centrale vend sa monnaie et achète des devises : l’opération est relativement facile, puisqu’elle peut créer sa propre monnaie. Pour contrer une dépréciation, elle doit vendre des devises prélevées sur des réserves nécessairement limitées — c’est cette asymétrie que les attaques spéculatives exploitent.")],
     faits=[("Les lignes de swap entre banques centrales — fourniture temporaire de liquidités — doivent être distinguées des interventions de change, qui sont des achats ou ventes de devises.",
             "Elles élargissent la capacité de défense au-delà des réserves propres, et constituent l’une des formes durables de coopération monétaire.")],
     dos=['n20-crise-change', 'n15-politique-monetaire']),
   'canaux': n(
     mec=[("Le canal du taux de change",
           "En changes flottants avec forte mobilité des capitaux, une politique monétaire expansionniste abaisse le taux d’intérêt, provoque des sorties de capitaux et déprécie la monnaie, ce qui améliore la compétitivité-prix. Dans le modèle IS-LM-BP, la hausse des exportations nettes déplace IS vers la droite : la dépréciation amplifie l’effet de relance.")],
     dos=['n20-changes-fixes-flottants']),
   'instabilite': n(
     faits=[("Le choc Volcker transforme l’endettement des pays en développement en crise : la dette extérieure de l’Amérique latine passe d’environ 75 milliards de dollars en 1975 à 315 milliards en 1983, son service de 12 à 66 milliards.",
             "La crise mexicaine de 1982 démontre que la flexibilité des changes ne supprime pas l’interdépendance monétaire internationale.")],
     aut=[("Guillermo Calvo",
           "La peur du flottement (2002) : l’endettement en devises et le risque d’inflation importée rendent les dépréciations potentiellement déstabilisatrices.")],
     dos=['n20-crise-change', 'n20-position-exterieure-nette']),
  })

# ========================================================== vz-court-long
v('vz-court-long', [25],
  lecture=[("Les prix fixes ne sont pas une erreur, c’est une hypothèse",
            "Le chapitre 5 de deuxième année met en lumière une règle méthodologique : le modèle IS-LM suppose la monnaie active, un raisonnement de court terme et un niveau général des prix fixe. C’est cette dernière hypothèse qui l’a rendu inopérant face à la stagflation et qui a imposé le modèle OG-DG. Un modèle n’est donc pas vrai ou faux : il est valide dans le cadre de ses hypothèses, et le choix du modèle pertinent constitue le premier acte d’analyse.")],
  noeuds={
   'horizon': n(
     mec=[("Conjoncturel et structurel : deux objets, deux instruments",
           "Une politique conjoncturelle agit à court terme sur la demande globale ; une politique structurelle modifie durablement l’offre et les capacités de production. Si la production est bornée par le potentiel, seule la seconde peut desserrer la contrainte : investissement productif ↑ → capacités ↑ → productivité ↑ → croissance potentielle ↑.")],
     aut=[("Paul Romer",
           "Les externalités de connaissance peuvent soutenir une croissance durable (1986) : fondement théorique des politiques d’offre.")],
     dos=['n1-potentielle']),
   'capacites': n(
     faits=[("La loi d’Okun (1962) relie l’écart de production au chômage, mais la production potentielle n’est pas observable : elle est estimée, et ces estimations sont révisées.",
             "D’où le risque de politique procyclique : relancer une économie déjà repartie, ou freiner une économie qui ralentit déjà, amplifie le cycle au lieu de l’amortir.")],
     dos=['n1-potentielle', 'n10-chomage-conj-struct']),
   'demande': n(
     mec=[("La demande effective et la prophétie autoréalisatrice",
           "C’est la demande anticipée par les entrepreneurs qui détermine la production et l’emploi. L’enchaînement peut devenir cumulatif : récession → anticipations pessimistes → investissement ↓ → revenus distribués ↓ → consommation ↓ → récession aggravée. L’anticipation contribue alors à faire advenir la situation anticipée.")],
     dos=['n5-equilibre', 'n26-equilibre-desequilibre']),
   'rigidites': n(
     mec=[("Pourquoi la flexibilité des salaires ne suffit pas",
           "Les salaires sont à la fois un coût pour l’entreprise et un revenu pour les ménages : leur baisse générale réduit la consommation, donc la demande globale, donc les débouchés anticipés. C’est l’objection décisive de Keynes à l’analyse de Pigou, et elle ne porte pas sur la rigidité mais sur le circuit.")],
     dos=['n10-chomage-classique-keynesien']),
  })

# ========================================================= vz-etat-marche
v('vz-etat-marche', [25],
  lecture=[("La stabilisation suppose un diagnostic, pas une doctrine",
            "Le chapitre 5 de deuxième année montre que l’efficacité d’une intervention conjoncturelle dépend de la configuration : position par rapport au potentiel, pente de LM, régime de change, mobilité des capitaux. Les politiques de demande ne sont ni systématiquement efficaces ni systématiquement inefficaces, ce qui déplace le débat de la doctrine vers le diagnostic.")],
  noeuds={
   'relance': n(
     mec=[("Le choix de l’instrument n’est pas neutre",
           "Avec c = 0,8, une relance de 100 millions produit + 500 millions de revenu national par la dépense publique, + 400 par les prestations sociales et + 400 par une baisse d’impôts. Cibler les ménages à forte propension marginale à consommer porte en outre la première vague de 60 à 95 pour 100 distribués.")],
     faits=[("La relance française de mai 1981 intervient dans un contexte d’inflation d’environ 13 % et de croissance faible des partenaires : les comptes extérieurs se dégradent et le tournant de la rigueur survient en mars 1983.",
             "Une relance isolée en économie ouverte voit une partie de ses effets s’exporter : le multiplicateur passe de 5 à 2 dans l’exemple du cours.")],
     dos=['n15-politique-relance', 'n15-multiplicateur-budgetaire']),
   'mix': n(
     faits=[("Policy mix Clinton-Greenspan : le solde budgétaire américain passe de − 4,5 % à + 0,8 % du PIB entre 1992 et 1998, avec une croissance de 3,7 % en 1998 et des taux à un an reculant de 5,5 % à 4,8 %.",
             "Une consolidation budgétaire accompagnée d’un assouplissement monétaire préserve le revenu et abaisse le taux — mais le cours rappelle qu’il s’agit d’une illustration, non d’une démonstration causale."),
            ("Réunification allemande : les taux courts passent de 4,3 % en 1988 à 9,2 % en 1991, le solde budgétaire se dégradant de + 0,2 % du PIB en 1989 à − 2,9 % en 1991.",
             "Le cas symétrique montre qu’un policy mix peut être non coopératif, la banque centrale contrant l’expansion budgétaire qu’elle juge inflationniste.")],
     aut=[("Robert Mundell",
           "La règle d’affectation : le budget à l’équilibre interne, la monnaie à l’équilibre externe — chaque instrument à l’objectif où son efficacité relative est la plus grande.")],
     dos=['n15-policy-mix']),
   'musgrave': n(
     mec=[("Stabilisateurs automatiques contre politiques discrétionnaires",
           "Les stabilisateurs automatiques agissent sans délai de diagnostic ni de décision et se retournent spontanément avec le cycle. Les politiques discrétionnaires cumulent au contraire quatre délais — diagnostic, décision, mise en œuvre, transmission — ce qui expose au risque de politique procyclique.")],
     dos=['n15-fonctions-musgrave']),
   'anticipations': n(
     mec=[("Deux canaux par les anticipations",
           "Friedman (1957) : les ménages règlent leur consommation sur le revenu permanent anticipé, de sorte qu’un transfert jugé temporaire est largement épargné. Barro (1974) : une baisse d’impôts financée par la dette fait anticiper des prélèvements futurs, l’épargne privée compensant la désépargne publique. Les deux supposent des agents informés et non contraints financièrement.")],
     dos=['n15-deficit-public']),
  })

# ============================================================ vz-travail
v('vz-travail', [25],
  lecture=[("Deux diagnostics du chômage, deux familles d’instruments",
            "Le chapitre 5 de deuxième année oppose explicitement le chômage comme excès d’offre sur le marché du travail, chez Pigou, et le chômage comme conséquence d’une insuffisance de la demande sur le marché des biens, chez Keynes. La distinction entre chômage conjoncturel et chômage structurel en découle, et avec elle le choix de l’instrument : politique de demande pour le premier, politiques structurelles pour le second.")],
  noeuds={
   'marche': n(
     mec=[("L’objection keynésienne à la flexibilité salariale",
           "Les salaires étant à la fois un coût et un revenu, leur baisse générale réduit la consommation et donc les débouchés anticipés : le remède peut aggraver le mal. La solution se déplace alors du marché du travail vers la demande globale.")],
     aut=[("Arthur Pigou",
           "Dans The Theory of Unemployment (1933), un salaire réel supérieur au niveau d’équilibre engendre un excès d’offre de travail, c’est-à-dire du chômage.")],
     dos=['n10-chomage-classique-keynesien']),
   'politiques': n(
     mec=[("Ce qu’une politique de demande peut et ne peut pas",
           "Si l’écart de production est négatif, une politique de demande réduit le chômage conjoncturel. Mais le taux de chômage naturel, qui dépend des frictions, de l’adéquation des qualifications et des institutions, borne ce qu’elle peut obtenir : au-delà, elle n’obtient qu’une accélération de l’inflation.")],
     aut=[("Milton Friedman",
           "Formule en 1968 l’hypothèse du taux de chômage naturel, que les politiques de demande ne peuvent pas durablement abaisser.")],
     faits=[("La stagflation des années 1970 invalide la lecture de la courbe de Phillips en termes d’arbitrage inflation-chômage, reformulation due à Lipsey puis à Samuelson et Solow en 1960.",
             "Phillips avait établi en 1958 une relation entre chômage et variation des salaires nominaux : l’attribution exacte est un point sur lequel les copies se distinguent.")],
     dos=['n10-chomage-conj-struct', 'n14-courbe-phillips']),
   'flexibilite': n(
     mec=[("L’hystérèse brouille la frontière",
           "Un chômage conjoncturel prolongé dégrade les compétences et l’employabilité : il devient structurel. La rapidité de la réaction conjoncturelle importe donc autant que la nature de l’instrument, ce qui plaide pour les stabilisateurs automatiques.")],
     dos=['n10-hysterese-du-chomage']),
  })

# ====================================================== vz-mondialisation
v('vz-mondialisation', [25, 26],
  lecture=[("L’ouverture déplace l’autonomie plutôt qu’elle ne l’abolit",
            "Les chapitres 5 et 6 de deuxième année ajoutent la dimension monétaire de la mondialisation : la fuite par les importations divise le multiplicateur national, les trois D de Bourguinat ont horizontalisé la courbe BP, et le triangle des incompatibilités de Mundell oblige chaque État à choisir entre stabilité du change et autonomie monétaire. L’autonomie n’est plus un attribut national : elle se décide par le choix d’un régime et se reconquiert par la coordination.")],
  noeuds={
   'finance': n(
     mec=[("Les trois D et l’horizontalisation de BP",
           "Déréglementation, décloisonnement et désintermédiation ont accru la sensibilité des capitaux aux différentiels internationaux de rendement. La courbe BP, qui mesure cette sensibilité par sa pente, est devenue de plus en plus plate : en mobilité parfaite, le taux domestique s’aligne sur le taux mondial.")],
     aut=[("Henri Bourguinat",
           "Résume la globalisation financière en trois D : déréglementation, décloisonnement, désintermédiation."),
          ("Dominique Plihon",
           "Le marché des changes est un marché-réseau : international, dématérialisé, quasi continu, unifié par l’arbitrage sans être centralisé.")],
     faits=[("Le développement du marché des changes révèle une déconnexion croissante entre transactions financières et échanges réels.",
             "C’est elle qui explique que le taux de change puisse s’écarter durablement de toute référence fondée sur les prix, comme la parité des pouvoirs d’achat de Cassel.")],
     dos=['n20-parite-des-taux-d-interet', 'n12-speculation']),
   'dependances': n(
     mec=[("La fuite par les importations et la tentation du passager clandestin",
           "Le multiplicateur devient 1 / (1 − c + m) et passe de 5 à 2 : une part de la relance profite aux producteurs étrangers. D’où une incitation à attendre que le partenaire relance — et, si tous attendent, l’absence de relance suffisante.")],
     dos=['n20-epargne-investissement-ouverte', 'le28-tentation-protectionnisme']),
   'rodrik': n(
     mec=[("Le triangle de Mundell comme second trilemme",
           "Changes fixes, mobilité des capitaux et autonomie monétaire ne peuvent être pleinement conciliés : chaque système monétaire se définit par l’objectif auquel il renonce. Bretton Woods sacrifie la mobilité, le flottement d’après 1971 la stabilité, l’euro de 1999 l’autonomie monétaire nationale.")],
     aut=[("Jean-Marc Daniel",
           "« Le monde a accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle des incompatibilités de Robert Mundell. »")],
     dos=['n21-bretton-woods', 'n20-changes-fixes-flottants']),
  })

# =========================================================== vz-courants
v('vz-courants', [25],
  lecture=[("La formalisation comme événement intellectuel",
            "Le chapitre 5 de deuxième année montre que la révolution keynésienne s’est imposée moins par le texte de 1936 que par sa formalisation : Hicks construit IS-LM en 1937, Hansen le diffuse en 1941, et c’est la tradition Hicks-Hansen qui fait du modèle l’instrument standard d’analyse des politiques économiques — au prix d’une simplification que certains keynésiens jugeront infidèle.")],
  noeuds={
   'keynes': n(
     mec=[("De la demande effective au modèle IS-LM",
           "La demande effective détermine la production et l’emploi, et la préférence pour la liquidité fait du taux d’intérêt le prix de la renonciation à la liquidité. Hicks articule ces deux propositions en 1937 dans un même plan : la courbe IS pour le marché des biens, la courbe LM pour le marché de la monnaie.")],
     aut=[("John Hicks",
           "Formalise en 1937, dans Econometrica, l’équilibre simultané du marché des biens et du marché de la monnaie."),
          ("Alvin Hansen",
           "Prolonge le modèle en 1941 et développe la notion de stagnation séculaire : l’insuffisance de demande peut être durable.")],
     dos=['n26-equilibre-desequilibre', 'n11-preference-liquidite']),
   'riposte': n(
     mec=[("Trois critiques et leur conclusion commune",
           "Effet d’éviction sur l’investissement, revenu permanent de Friedman (1957) sur la consommation, équivalence ricardienne de Barro (1974) sur le financement. Elles convergent vers un multiplicateur plus faible qu’annoncé, mais par des mécanismes distincts qu’il faut séparer."),
          ("La borne du potentiel",
           "Au plein emploi, la hausse des prix réduit l’offre réelle de monnaie, déplace LM vers la gauche et ramène l’économie à son potentiel avec un taux plus élevé. Avec le taux de chômage naturel, c’est le résultat qui a déplacé la politique économique vers l’offre.")],
     faits=[("La crise de 2008 a réhabilité le modèle IS-LM, pour analyser la trappe à liquidité et les limites de la politique monétaire conventionnelle.",
             "Le cours en tire une conclusion mesurée : les politiques de demande ne sont ni systématiquement efficaces ni systématiquement inefficaces.")],
     dos=['n15-politique-relance', 'n11-neutralite-monnaie']),
   'neoclassiques': n(
     mec=[("La dichotomie classique et ses deux piliers",
           "Les quantités et les prix relatifs se déterminent sur les marchés réels, la monnaie ne déterminant que le niveau général des prix. Le taux d’intérêt équilibre l’épargne et l’investissement sur le marché des fonds prêtables, et le chômage s’explique par un salaire réel trop élevé : c’est l’édifice que Keynes entreprend de défaire.")],
     dos=['n26-monnaie-neutre-active', 'n10-chomage-classique-keynesien']),
  })

# ======================================================= vz-libre-echange
v('vz-libre-echange', [25, 26],
  lecture=[("L’argument macroéconomique de la protection, et sa réfutation",
            "Les chapitres 5 et 6 de deuxième année ajoutent deux arguments que l’analyse en termes d’allocation ne contient pas. Du côté de la protection : limiter les importations réduirait la fuite du multiplicateur, qui passe de 5 à 2 en économie ouverte. Du côté de la coopération : les importations des uns étant les exportations des autres, la coordination obtient collectivement ce que la protection cherche individuellement — et une guerre des monnaies, les taux de change étant relatifs, ne peut profiter à tous.")],
  noeuds={
   'couts': n(
     mec=[("Le multiplicateur ouvert comme argument, et sa contrepartie",
           "Avec M = M₀ + mY, le multiplicateur devient 1 / (1 − c + m) : limiter les importations adresserait une part plus importante de la demande aux producteurs nationaux. Mais la substituabilité est la condition décisive, et la désindustrialisation la détruit : sans appareil productif national, la facture augmente sans que les volumes diminuent.")],
     dos=['le28-efficacite-protectionnisme', 'n20-epargne-investissement-ouverte']),
   'representailles': n(
     mec=[("La guerre des monnaies et sa limite fondamentale",
           "Si plusieurs pays cherchent simultanément à dévaluer, la dévaluation de A fait perdre de la compétitivité à B, qui dévalue à son tour. Mais les taux de change étant relatifs, tous les pays ne peuvent pas simultanément déprécier leur monnaie les uns par rapport aux autres : l’impossibilité est logique, et non seulement coûteuse.")],
     faits=[("Les dévaluations font l’objet d’un encadrement international : dans le dispositif initial de Bretton Woods, les changements cumulés de parité dépassant 10 % relevaient d’une procédure de consultation du FMI.",
             "Les accords du Plaza de septembre 1985 et du Louvre de février 1987 montrent qu’une coordination monétaire est possible, mais qu’elle intervient en réaction à des désordres.")],
     dos=['n20-devaluation-reevaluation', 'le28-tentation-protectionnisme']),
  })

# ========================================================= vz-gouvernance
v('vz-gouvernance', [26],
  lecture=[("La gouvernance monétaire : des règles explicites à la coordination intermittente",
            "Le chapitre 6 de deuxième année ajoute le versant monétaire de la gouvernance mondiale. Bretton Woods (1944-1971) organisait des règles explicites, encadrant jusqu’aux ajustements de parité. Depuis le flottement généralisé de 1973, chaque État choisit son régime, et la coordination n’intervient plus qu’en réaction : accords du Plaza en 1985, du Louvre en 1987, lignes de swap entre banques centrales.")],
  noeuds={
   'dollar': n(
     mec=[("Les trois fonctions internationales et le paradoxe qu’elles créent",
           "Monnaie véhiculaire, unité de compte et réserve de valeur internationale, le dollar bénéficie d’une demande structurelle. Mais la doctrine Miran, dans un rapport de novembre 2024, y voit un handicap : cette demande entretiendrait une surévaluation pénalisant l’industrie manufacturière américaine. Or déprécier la monnaie de réserve mondiale réduit la valeur externe des placements en dollars — 20 % dans l’exemple du cours — et risque de miner la confiance.")],
     aut=[("Stephen Miran",
           "Soutient dans un rapport de novembre 2024 que la demande internationale d’actifs sûrs en dollars entretient une surévaluation de la monnaie américaine.")],
     faits=[("Le projet dit d’« accords de Mar-a-Lago » viserait une dépréciation coordonnée du dollar, sur le modèle du Plaza de 1985, mais se heurte aux intérêts divergents des grandes puissances.",
             "Les stablecoins adossés au dollar, encadrés par le GENIUS Act de juillet 2025, cherchent à l’inverse à créer une demande privée supplémentaire de dollars et de bons du Trésor.")],
     dos=['n21-monnaie-internationale']),
   'institutions': n(
     faits=[("Le FMI est créé par les accords de Bretton Woods de 1944 pour surveiller un système de changes fixes mais ajustables, le contrôle des mouvements de capitaux permettant de préserver une autonomie monétaire relative.",
             "Après la suspension de la convertibilité du dollar en or le 15 août 1971 et le flottement de 1973, chaque pays choisit son régime : d’après les données de 2025, 29 pays pratiquent un arrimage ferme, 88 un arrimage souple, 66 un flottement et 13 ne sont pas classés.")],
     dos=['n21-bretton-woods', 'n20-changes-fixes-flottants']),
  })

# ======================================================== vz-marche-prix
v('vz-marche-prix', [25],
  lecture=[("Le tâtonnement suppose qu’aucun échange n’ait lieu hors équilibre",
            "Le chapitre 5 de deuxième année souligne l’hypothèse décisive du tâtonnement walrasien : le commissaire-priseur annonce des prix successifs et aucune transaction n’est conclue avant l’équilibre. Faute d’un tel dispositif, les déséquilibres réels se résorbent par les variations de stocks, du revenu et de l’emploi — c’est-à-dire par les quantités, et non par les prix.")],
  noeuds={
   'equilibre': n(
     mec=[("L’ajustement par les quantités",
           "Dans une économie réelle, les échanges se font en permanence à des prix qui ne sont pas d’équilibre. L’ajustement passe alors par les stocks, la production et l’emploi, ce qui rend possible un équilibre stable mais situé en dessous du plein emploi.")],
     aut=[("Vilfredo Pareto",
           "L’optimum de Pareto caractérise l’efficacité de l’équilibre général, mais ne dit rien de l’équité de la répartition.")],
     dos=['n5-equilibre', 'n26-equilibre-desequilibre']),
   'coordination': n(
     mec=[("Un modèle est un idéal-type",
           "La concurrence pure et parfaite — atomicité, homogénéité, libre entrée, transparence, mobilité des facteurs — est une construction qui accentue certains traits du réel pour les analyser, au sens de l’idéal-type wébérien. Sa pertinence ne se juge pas à son réalisme mais à sa capacité d’expliquer dans le cadre de ses hypothèses.")],
     aut=[("Max Weber",
           "L’idéal-type accentue certains traits du réel afin d’en faciliter l’analyse : la concurrence pure et parfaite en est un, le monopole pur un autre.")],
     dos=['n26-equilibre-desequilibre']),
  })
