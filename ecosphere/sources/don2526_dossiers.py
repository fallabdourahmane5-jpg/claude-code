# -*- coding: utf-8 -*-
"""« Autour d'une notion » : mise a jour des dossiers existants par les
chapitres 5 et 6 de deuxieme annee.

Aucun dossier nouveau n'est cree : seuls les dossiers dont l'analyse mobilise
reellement l'un des deux chapitres sont completes. Pour chacun : les chapitres
a ajouter dans les liens, et les idees que le document de cours justifie.

Format d'une entree :
  'cle-du-dossier': {
     'ch':    [25] ou [26] ou [25, 26],
     'mec':   [(titre, explication), ...],
     'aut':   [(nom, idee, portee), ...],
     'args':  [(argument, condition, limite), ...],
     'faits': [(fait, portee), ...],
     'diss':  [(question, formulation), ...],
  }
"""

MAJ = {}


def d(cle, ch, mec=None, aut=None, args=None, faits=None, diss=None):
    MAJ[cle] = {
        'ch': ch,
        'mec': [{'t': t, 'e': e} for (t, e) in (mec or [])],
        'aut': [{'n': n, 'i': i, 'p': p} for (n, i, p) in (aut or [])],
        'args': [{'a': a, 'cond': c, 'lim': l} for (a, c, l) in (args or [])],
        'faits': [{'f': f, 'p': p} for (f, p) in (faits or [])],
        'diss': [{'q': q, 'f': f} for (q, f) in (diss or [])],
    }


# ===================================================== ensemble 1 et 5
d('n1-potentielle', [25],
  mec=[("L’écart de production comme instrument de diagnostic",
        "La production potentielle n’est pas observable : elle est estimée, et ces estimations sont révisées. L’écart de production, ou output gap, mesure la différence avec la production effective. Un écart négatif signale une sous-utilisation des ressources et donne un objet à la politique de demande ; un écart nul ou positif signifie qu’une relance se traduira davantage par des tensions sur les prix.")],
  aut=[("Arthur Okun",
        "La loi d’Okun (1962) relie l’écart de production au chômage : produire sous son potentiel va de pair avec un chômage plus élevé.",
        "Le cours nuance : la loi porte sur la relation entre production et chômage, et l’interprétation inflationniste d’un output gap positif relève plus largement de l’analyse des capacités et de la demande.")],
  faits=[("Le modèle OG-DG permet d’analyser la stagflation de 1975, où la croissance est de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec des inflations de 11,7 %, 5,9 % et 9,1 %.",
          "Cette configuration montre qu’un écart de production négatif peut coexister avec une inflation élevée : le diagnostic conjoncturel ne se réduit donc jamais à une seule grandeur.")])

d('n1-investissement', [25],
  mec=[("Les débouchés anticipés plutôt que le seul taux d’intérêt",
        "L’investissement dépend des débouchés futurs anticipés, du coût du financement, du rendement attendu du capital et de l’incertitude. Une baisse des taux peut donc rester sans effet si les anticipations sont très pessimistes — ce qui explique qu’une politique monétaire accommodante puisse ne pas relancer l’investissement.")],
  args=[("Dans une trappe à liquidité, l’investissement cesse de réagir au canal monétaire conventionnel : les taux étant très bas, leur baisse supplémentaire ne modifie plus les décisions.",
         "Il faut que les anticipations de demande soient effectivement dégradées, et non seulement que les taux soient bas.",
         "Le canal budgétaire reste alors efficace, l’effet d’éviction devenant nul : c’est la configuration qui a réhabilité le modèle IS-LM après 2008.")])

d('n5-equilibre', [25],
  mec=[("L’ajustement par les quantités plutôt que par les prix",
        "Le tâtonnement walrasien suppose un commissaire-priseur annonçant des prix successifs sans qu’aucun échange ait lieu hors équilibre. Faute d’un tel dispositif, les déséquilibres réels se résorbent par les variations de stocks, du revenu et de l’emploi : c’est l’espace qu’occupe l’analyse keynésienne de l’équilibre de sous-emploi.")],
  aut=[("John Maynard Keynes",
        "Un équilibre macroéconomique n’est pas nécessairement un équilibre de plein emploi.",
        "La production peut être égale à la demande globale tout en demeurant insuffisante pour employer l’ensemble de la main-d’œuvre : le chômage devient involontaire, et la flexibilité des prix ne le corrige pas.")])

# ===================================================== ensemble 10 : chômage
d('n10-chomage-classique-keynesien', [25],
  mec=[("L’objection keynésienne à la flexibilité salariale",
        "Les salaires sont à la fois un coût pour l’entreprise et un revenu pour les ménages. Leur baisse générale réduit donc la consommation, donc la demande globale, donc les débouchés anticipés et la production : le remède risque d’aggraver le mal, ce qui retire à la flexibilité salariale son statut de solution universelle.")],
  aut=[("Arthur Pigou",
        "Dans The Theory of Unemployment (1933), le chômage résulte d’un salaire réel supérieur à son niveau d’équilibre.",
        "L’offre de travail croît avec le salaire réel, la demande décroît : un salaire maintenu au-dessus du niveau d’équilibre engendre un excès d’offre, et l’explication est entièrement interne au marché du travail."),
       ("John Maynard Keynes",
        "Le chômage peut résulter d’une insuffisance de la demande globale, sans qu’aucun salaire ne soit en cause.",
        "C’est la demande effective — anticipée par les entrepreneurs — qui détermine la production et l’emploi : si elle est insuffisante, aucune entreprise n’a intérêt à produire davantage, quel que soit le salaire.")])

d('n10-chomage-conj-struct', [25],
  mec=[("Deux diagnostics, deux instruments",
        "Un chômage conjoncturel accompagne un écart de production négatif : une politique de demande peut le réduire, puisque des capacités sont inemployées. Un chômage structurel dépend des frictions, de l’adéquation des qualifications et des institutions : aucune relance ne l’abaisse durablement, elle n’obtient qu’une accélération de l’inflation.")],
  aut=[("Milton Friedman",
        "Le taux de chômage naturel (1968) dépend des frictions, de l’adéquation entre qualifications et emplois, des institutions et de la formation des salaires.",
        "Il n’est pas immuable, mais il borne ce qu’une politique de demande peut obtenir : c’est ce résultat qui a déplacé la politique économique vers les politiques structurelles.")],
  diss=[("Sujet du type « Le chômage résulte-t-il d’un dysfonctionnement du marché du travail ? »",
         "La réponse exige de séparer les deux diagnostics : l’analyse de Pigou décrit un déséquilibre interne au marché du travail, celle de Keynes une insuffisance de la demande sur le marché des biens. L’erreur la plus coûteuse est l’erreur de diagnostic, puisqu’elle conduit à mobiliser un instrument inopérant.")])

d('n10-hysterese-du-chomage', [25],
  mec=[("De la conjoncture à la structure",
        "Un chômage conjoncturel prolongé dégrade les compétences et l’employabilité : le chômage devient structurel, et la frontière entre les deux diagnostics cesse d’être étanche. La rapidité de la réaction conjoncturelle importe donc autant que la nature de l’instrument employé, ce qui plaide pour les stabilisateurs automatiques.")],
  args=[("L’hystérèse justifie une intervention rapide même en cas d’incertitude sur le diagnostic : attendre la confirmation d’un écart de production négatif peut coûter plus cher que d’agir à tort.",
         "Il faut que l’instrument mobilisé agisse sans délai excessif, ce que les stabilisateurs automatiques permettent mieux que les décisions discrétionnaires.",
         "Mais une politique mal calibrée devient procyclique : la production potentielle n’étant qu’estimée, le risque d’amplifier le cycle demeure.")])

# ===================================================== ensemble 11 : monnaie
d('n11-monnaie-activite', [25],
  mec=[("La transmission par le taux d’intérêt",
        "Une hausse de l’offre de monnaie conduit les agents à détenir plus de monnaie qu’ils ne le souhaitent : ils achètent des titres, le prix des obligations monte et le taux d’intérêt baisse. La baisse du taux réduit le coût du financement et stimule l’investissement, qui se diffuse ensuite par le multiplicateur.")],
  faits=[("Dans la trappe à liquidité, LM devient horizontale et le canal conventionnel est bloqué ; dans la zone classique, LM est verticale et l’effet d’éviction d’une relance budgétaire devient total.",
          "Les deux configurations extrêmes montrent que l’effet de la monnaie sur l’activité n’est pas une propriété fixe : il dépend de la pente de LM, donc de la sensibilité de la demande de monnaie au taux et au revenu.")])

d('n11-neutralite-monnaie', [25, 26],
  mec=[("La neutralité comme résultat de long terme",
        "Au plein emploi, une relance provoque des tensions sur les prix ; la hausse des prix réduit l’offre réelle de monnaie, déplace LM vers la gauche, élève le taux d’intérêt et évince l’investissement privé. L’économie retrouve exactement son niveau potentiel YPE avec un taux plus élevé : la production réelle est inchangée.")],
  args=[("La monnaie n’est pas neutre à court terme en situation de sous-emploi : la préférence pour la liquidité fait du taux d’intérêt un phénomène monétaire, et une variation de l’offre de monnaie agit sur l’investissement.",
         "Il faut que l’économie dispose de capacités inemployées et que les anticipations de débouchés ne soient pas dégradées au point d’annuler l’effet du taux.",
         "Dans une trappe à liquidité, le canal conventionnel est bloqué ; en économie très ouverte, une politique accommodante prolongée déprécie la monnaie et alimente l’inflation importée."),
        ("En économie ouverte, la monnaie agit aussi par le taux de change : une politique expansionniste en changes flottants déprécie la monnaie, améliore la compétitivité-prix et déplace IS vers la droite.",
         "Il faut une mobilité élevée des capitaux et des élasticités suffisantes pour que les volumes exportés réagissent.",
         "En changes fixes avec mobilité parfaite, l’expansion monétaire est au contraire intégralement neutralisée par la défense de la parité.")])

d('n11-preference-liquidite', [25],
  mec=[("Trois motifs et l’effet balançoire",
        "Les motifs de transaction et de précaution dépendent positivement du revenu ; le motif de spéculation dépend négativement du taux d’intérêt. L’effet balançoire le fonde : une hausse du taux fait baisser le prix des obligations existantes, de sorte qu’un taux jugé anormalement bas fait anticiper une perte en capital et pousse à détenir de la monnaie.")],
  faits=[("Il faut distinguer trois grandeurs : le coupon, fixe ; le prix de marché de l’obligation, variable ; et le rendement de marché, qui varie en sens inverse du prix.",
          "Cette distinction est la clé de l’effet balançoire, donc du motif de spéculation, donc de la pente de la courbe LM et de l’existence d’une trappe à liquidité.")])

d('n11-liquidite', [25],
  aut=[("John Maynard Keynes",
        "Le taux d’intérêt est le prix de la renonciation à la liquidité, non le prix du capital prêtable.",
        "C’est la rupture avec l’analyse classique : le taux d’intérêt se détermine sur le marché monétaire et non sur un marché des fonds prêtables où l’épargne rencontrerait l’investissement.")],
  args=[("Dans une trappe à liquidité, la préférence pour la liquidité devient si forte que toute monnaie supplémentaire est thésaurisée : le taux ne baisse plus.",
         "Il faut que les agents anticipent une remontée des taux, donc une baisse du prix des obligations, ce qui rend leur détention risquée.",
         "Le cours précise que c’est le canal conventionnel qui est bloqué, et non nécessairement toute action monétaire.")])

d('n11-taux-d-interet-nominal-et-reel', [26],
  mec=[("De l’effet de levier à l’effet de massue",
        "Le taux réel vaut approximativement le taux nominal moins l’inflation. Avec un taux nominal de 10 %, il s’établit à − 4 % pour une inflation de 14 % mais à + 8 % pour une inflation de 2 %. L’effet de levier — rentabilité économique de 10 % contre un coût réel de 4 % — bascule alors en effet de massue — coût réel de 8 % contre une rentabilité de 5 %.")],
  faits=[("La désinflation française, en portant le taux d’intérêt réel de − 4 % à + 8 %, a conduit les entreprises à privilégier le désendettement plutôt que l’investissement, malgré un taux de marge passé de 25 % en 1985 à 32 % en 1989.",
          "C’est la première limite du théorème de Schmidt : la restauration des profits est une condition favorable à l’investissement, mais non une condition suffisante.")])

# ===================================================== ensemble 12 et 14
d('n12-speculation', [26],
  mec=[("Spéculation stabilisatrice ou déstabilisatrice selon le régime d’anticipations",
        "En période calme, les opérateurs forment des anticipations de retour à la moyenne : ils achètent une monnaie sous-évaluée et vendent une monnaie surévaluée, ce qui ramène le cours vers sa référence. En période de crise, les anticipations portent sur la poursuite de la tendance et les ventes alimentent la baisse qu’elles anticipaient.")],
  aut=[("Milton Friedman",
        "Dans The Case for Flexible Exchange Rates (1953), la spéculation est présentée comme stabilisatrice.",
        "Le cours nuance fortement : le marché des changes peut être simultanément stabilisateur et déstabilisateur, ce qui rend l’argument conditionnel au régime d’anticipations plutôt que faux.")])

d('n14-courbe-phillips', [25],
  mec=[("La chaîne d’attribution, à ne pas confondre",
        "Phillips établit en 1958 une relation entre le chômage et la variation des salaires nominaux au Royaume-Uni. Lipsey en approfondit l’analyse théorique en 1960, et Samuelson et Solow contribuent la même année à populariser sa reformulation en termes de relation entre inflation et chômage. C’est cette reformulation, non la relation originelle, que la stagflation a invalidée.")],
  faits=[("En 1975, la croissance est de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec des inflations de 11,7 %, 5,9 % et 9,1 % (OCDE).",
          "La coexistence d’un chômage élevé et d’une inflation élevée ruine l’idée d’un arbitrage stable exploitable par la politique économique, et impose le modèle OG-DG.")],
  aut=[("Milton Friedman",
        "Le taux de chômage naturel (1968) interdit d’exploiter durablement un arbitrage entre inflation et chômage.",
        "Une relance peut réduire le chômage tant que les anticipations de prix ne sont pas révisées ; dès qu’elles le sont, le chômage revient à son niveau naturel avec une inflation plus élevée.")])

d('n14-inflation-demande', [25],
  mec=[("Du modèle IS-LM au modèle OG-DG",
        "Le modèle IS-LM raisonne à prix fixes : il explique les variations du revenu et du taux d’intérêt mais ne peut pas représenter l’inflation. Le modèle OG-DG réintroduit le niveau général des prix, de sorte qu’une hausse de la demande globale se répartit entre production et prix selon la position de l’économie par rapport à son potentiel.")],
  args=[("Au voisinage du potentiel, une hausse de la demande se traduit principalement par de l’inflation : la hausse des prix réduit l’offre réelle de monnaie, déplace LM vers la gauche et ramène la production à YPE.",
         "Il faut que les capacités productives soient effectivement saturées, ce que l’écart de production permet d’apprécier — mais la production potentielle n’est qu’estimée.",
         "En situation de sous-emploi, la même hausse de la demande agit au contraire principalement sur la production et l’emploi.")])

d('n14-inflation-importee', [26],
  mec=[("L’érosion du gain de compétitivité et les effets de second tour",
        "Une dépréciation renchérit les biens de consommation finale importés et les intrants utilisés par les entreprises nationales. L’inflation réduit le pouvoir d’achat, les salariés formulent des revendications salariales, les coûts de production augmentent — mécanisme renforcé lorsque les salaires sont indexés — et les prix domestiques s’élèvent : l’avantage initial de la dévaluation est réduit.")],
  faits=[("L’inflation importée est l’un des deux mécanismes de la peur du flottement établie par Calvo et Reinhart en 2002, avec l’endettement en devises.",
          "Dans une économie très dépendante de ses importations, elle peut contraindre la banque centrale à relever ses taux et freiner l’activité : la dépréciation cesse alors d’être un instrument neutre.")],
  diss=[("Sujet du type « La dévaluation permet-elle de restaurer la compétitivité ? »",
         "L’inflation importée fournit la limite temporelle : même si la condition de Marshall-Lerner est vérifiée et si la courbe en J a été franchie, la troisième phase peut voir les gains s’éroder si l’inflation importée renchérit durablement les coûts nationaux.")])

d('n14-desinflation', [26],
  mec=[("La désinflation compétitive : agir sur les prix plutôt que sur la parité",
        "À parité stable, obtenir une inflation inférieure à celle des partenaires améliore progressivement le taux de change réel, donc la compétitivité-prix, sans recourir à la dévaluation. La stratégie mobilise des politiques structurelles — déréglementations, flexibilisation du marché du travail — une politique budgétaire de maîtrise de la demande et, surtout, une politique monétaire restrictive.")],
  faits=[("L’inflation française passe d’environ 14 % au début des années 1980 à environ 2 % au début des années 1990, le taux de marge des entreprises remontant de 25 % en 1985 à 32 % en 1989.",
          "Le cours précise que la référence à 2 % mesure l’ampleur de la désinflation et ne doit pas être confondue avec la cible institutionnelle de la BCE, créée ultérieurement."),
         ("Mais la croissance française reste proche de 2 % par an contre environ 3 % dans l’OCDE, et le chômage passe d’environ 8 % de la population active en 1982 à environ 12 % en 1998, contre un ordre de grandeur de 7 % ailleurs.",
          "La désinflation a donc atteint son objectif monétaire sans produire les effets réels attendus : c’est l’échec relatif du théorème de Schmidt.")])

# ===================================================== ensemble 15 : politiques
d('n15-multiplicateur-budgetaire', [25],
  mec=[("Les trois multiplicateurs et la hiérarchie par le point d’entrée",
        "De Y(1 − c) = C₀ − cT + cF + I + G on tire kG = 1 / (1 − c) = 5, kF = c / (1 − c) = 4 et kT = − c / (1 − c) = − 4 avec c = 0,8. La hiérarchie s’explique par le point d’entrée dans le circuit : une dépense publique de 100 est immédiatement une demande, un transfert de 100 passe d’abord par le revenu disponible dont 80 seulement sont consommés.")],
  faits=[("En économie ouverte, les importations constituent une seconde fuite et le multiplicateur devient 1 / (1 − c + m) : il passe de 5 à 2 dans l’exemple du cours.",
          "Une dépense de 100 ne produit alors plus que 200 de revenu national, le reste profitant aux producteurs étrangers — ce qui justifie la coordination des relances."),
         ("Cibler une relance sur les ménages à forte propension marginale à consommer porte la première vague de dépense de 60 à 95 pour 100 distribués.",
          "La redistribution verticale devient ainsi un instrument d’efficacité macroéconomique, et non seulement de justice sociale.")],
  args=[("À montant initial égal, le multiplicateur est le même pour une dépense publique de consommation et une dépense d’investissement.",
         "Le cours formule explicitement cette nuance : c’est le montant injecté dans le circuit qui détermine l’effet de court terme.",
         "L’intérêt propre de l’investissement public est d’accroître en outre les capacités productives futures, donc d’agir sur la croissance potentielle.")])

d('n15-effet-eviction', [25],
  mec=[("L’enchaînement complet et ses trois déterminants",
        "Dépenses publiques ↑ → demande globale ↑ → revenu ↑ → demande de monnaie pour transactions ↑ → à offre inchangée, taux d’intérêt ↑ → coût du financement ↑ → investissement privé ↓. Son intensité dépend de la pente de LM, de la sensibilité de l’investissement au taux et de la configuration monétaire : nulle dans une trappe à liquidité, totale dans la zone classique.")],
  faits=[("Dans le modèle IS-LM, une relance budgétaire porte le revenu à Y1 et non à Y3 : la différence mesure l’investissement privé évincé.",
          "L’effet d’éviction n’annule donc pas la relance, il en réduit l’ampleur — et une politique monétaire accommodante, en déplaçant LM vers la droite, permet de la restaurer.")],
  diss=[("Sujet du type « Les politiques de relance sont-elles encore efficaces ? »",
         "L’effet d’éviction doit être distingué des deux autres critiques : il porte sur l’investissement et sur le marché monétaire, tandis que le revenu permanent de Friedman porte sur la consommation et l’équivalence ricardienne de Barro sur le financement. Confondre ces trois canaux est la faute majeure du chapitre.")])

d('n15-policy-mix', [25],
  mec=[("Deux combinaisons symétriques",
        "Policy mix Clinton-Greenspan : la consolidation budgétaire déplace IS vers la gauche, l’assouplissement monétaire LM vers la droite — le revenu est préservé et le taux d’intérêt baisse. Réunification allemande : les dépenses déplacent IS vers la droite, la Bundesbank déplace LM vers la gauche — l’activité est soutenue au prix de taux d’intérêt élevés.")],
  faits=[("Le solde budgétaire américain passe de − 4,5 % à + 0,8 % du PIB entre 1992 et 1998, avec une croissance de 3,7 % en 1998 et des taux à un an reculant de 5,5 % à 4,8 %.",
          "Le cours formule une nuance explicite : les taux américains ont connu plusieurs phases et la croissance dépend aussi d’autres facteurs — c’est une illustration du policy mix, non une démonstration causale."),
         ("En Allemagne, les taux courts passent de 4,3 % en 1988 à 9,2 % en 1991, tandis que le solde budgétaire se dégrade de + 0,2 % du PIB en 1989 à − 2,9 % en 1991.",
          "Le cas montre qu’un policy mix peut être non coopératif : la banque centrale contre l’expansion budgétaire qu’elle juge inflationniste.")],
  aut=[("Robert Mundell",
        "La règle d’affectation attribue chaque instrument à l’objectif pour lequel son efficacité relative est la plus grande : le budget à l’équilibre interne, la monnaie à l’équilibre externe.",
        "Elle suppose cependant que les deux instruments soient disponibles, ce que le triangle des incompatibilités peut interdire selon le régime de change retenu.")])

d('n15-politique-budgetaire', [25],
  args=[("L’efficacité de la politique budgétaire dépend du régime de change : en changes fixes avec mobilité parfaite des capitaux, elle est amplifiée par l’accompagnement monétaire qu’exige la défense de la parité.",
         "Il faut une mobilité élevée des capitaux et un engagement crédible sur la parité.",
         "En changes flexibles avec mobilité parfaite, elle est au contraire neutralisée : la hausse du taux attire les capitaux, apprécie la monnaie et réduit les exportations nettes — c’est l’éviction par le taux de change.")],
  faits=[("Dans la zone euro, l’instrument budgétaire reste national mais encadré — 3 % de déficit et 60 % de dette depuis Maastricht, Pacte de stabilité de 1997 — tandis que la politique monétaire est unique.",
          "Le budget commun représentant un peu plus de 1 % du revenu national brut de l’Union, aucune stabilisation centralisée n’est possible : la coordination relève de la construction politique.")])

d('n15-politique-monetaire', [25, 26],
  mec=[("Un canal indirect, dont chaque maillon peut céder",
        "La politique monétaire ne dépense pas : elle modifie un prix, le taux d’intérêt, en espérant que des agents privés en tireront des décisions d’investissement. Le premier maillon cède dans une trappe à liquidité, le deuxième lorsque les anticipations de débouchés sont trop dégradées, le troisième lorsque le régime de change contraint la banque centrale à défendre une parité.")],
  args=[("En changes flexibles avec mobilité parfaite des capitaux, la politique monétaire dispose d’un double canal : la baisse du taux provoque des sorties de capitaux, donc une dépréciation qui stimule les exportations nettes et déplace IS vers la droite.",
         "Il faut des élasticités suffisantes pour que les volumes exportés réagissent, et une économie peu exposée à l’inflation importée.",
         "En changes fixes avec mobilité parfaite, elle est intégralement neutralisée ; et dans une union monétaire, l’instrument est transféré à une institution commune.")])

d('n15-politique-relance', [25],
  mec=[("Trois critiques, trois canaux distincts",
        "L’effet d’éviction porte sur l’investissement, par le marché monétaire. L’hypothèse du revenu permanent de Friedman (1957) porte sur la consommation : un transfert jugé temporaire est largement épargné. L’équivalence ricardienne de Barro (1974) porte sur le financement : l’épargne privée compense la désépargne publique. Ces trois canaux convergent vers un multiplicateur plus faible, mais par des mécanismes séparés.")],
  faits=[("La relance française de mai 1981 intervient dans un contexte d’inflation d’environ 13 % et de croissance faible des partenaires : une part de la demande se porte sur les importations, les comptes extérieurs se dégradent et trois dévaluations interviennent avant le tournant de mars 1983.",
          "L’épisode illustre la contrainte extérieure : l’efficacité d’une relance ne se juge jamais indépendamment du cadre monétaire international.")],
  args=[("La crise de 2008 a réhabilité la relance budgétaire dans une configuration précise : près du plancher des taux, l’effet d’éviction devient très limité et la politique budgétaire retrouve une efficacité élevée.",
         "Il faut que l’économie dispose de capacités inemployées et que les taux soient effectivement proches de leur plancher.",
         "Le cours conclut que les politiques de demande ne sont ni systématiquement efficaces ni systématiquement inefficaces : leur pertinence dépend du contexte macroéconomique.")])

d('n15-trappe-liquidite', [25],
  mec=[("Pourquoi LM devient horizontale",
        "Lorsque les taux sont très bas, les agents anticipent leur remontée, donc une baisse du prix des obligations, donc une perte en capital : la demande spéculative de monnaie devient extrêmement sensible au taux, et toute monnaie supplémentaire est thésaurisée. Le cours précise que c’est le canal conventionnel de baisse du taux qui est bloqué, et non nécessairement toute action monétaire.")],
  args=[("La trappe à liquidité inverse la hiérarchie des instruments : l’effet d’éviction devenant nul, la politique budgétaire est particulièrement efficace.",
         "Il faut que l’économie dispose de capacités inemployées pour que la hausse de la demande se traduise en production.",
         "C’est précisément cette configuration qui a réhabilité le modèle IS-LM après 2008, après que les critiques monétaristes avaient semblé le congédier.")])

d('n15-contrainte-exterieure', [25, 26],
  mec=[("Quatre configurations, deux dilemmes seulement",
        "On croise sous-emploi ou tensions inflationnistes, et déficit ou excédent extérieur. Sous-emploi avec excédent, et inflation avec déficit : une même orientation corrige les deux déséquilibres. Sous-emploi avec déficit, et inflation avec excédent : l’instrument qui corrige l’un aggrave l’autre — ce sont les deux véritables dilemmes.")],
  aut=[("Jacques Généreux",
        "Les dilemmes se lisent par l’écart entre le revenu de plein emploi Ype et le revenu équilibrant les transactions courantes YBTC.",
        "L’ordre relatif des deux revenus suffit à identifier le dilemme : si YBTC est inférieur à Ype, atteindre le plein emploi implique un déficit courant, et seule une politique agissant sur YBTC desserre durablement la contrainte."),
       ("Robert Mundell",
        "La règle d’affectation résout le problème logique : il faut autant d’instruments que d’objectifs.",
        "Le budget est affecté à l’équilibre interne, la monnaie à l’équilibre externe — mais le triangle des incompatibilités peut rendre l’un des deux indisponible.")],
  faits=[("Le cours corrige explicitement l’idée reçue selon laquelle les changes flexibles supprimeraient la contrainte extérieure : l’exemple japonais montre qu’une politique accommodante accentue les pressions à la dépréciation, qui renchérissent les importations.",
          "La contrainte change de forme — d’une contrainte de parité à une contrainte d’inflation importée — mais elle ne disparaît pas.")])

d('n15-fonctions-musgrave', [25],
  mec=[("Stabilisateurs automatiques et politiques discrétionnaires",
        "La fonction de stabilisation peut s’exercer par des décisions discrétionnaires, exposées aux délais de diagnostic, de décision, de mise en œuvre et de transmission, ou par des stabilisateurs automatiques — progressivité de l’impôt, indemnisation du chômage — qui agissent sans délai et se retournent spontanément avec le cycle.")],
  args=[("Une politique procyclique amplifie les fluctuations au lieu de les amortir : relancer une économie déjà repartie ou freiner une économie qui ralentit déjà accentue le cycle.",
         "Le risque vient du caractère non observable de la production potentielle, estimée et révisée.",
         "Le cours nuance : une politique procyclique n’est pas nécessairement inefficace pour tous les objectifs possibles, mais elle contredit l’objectif de stabilisation.")])

d('n15-deficit-public', [25],
  args=[("L’équivalence ricardienne de Barro (1974) soutient qu’un déficit financé par la dette est anticipé comme un prélèvement futur, l’épargne privée compensant la désépargne publique.",
         "Elle suppose des agents informés, capables d’épargner, raisonnant sur un horizon long et peu contraints par leur revenu courant.",
         "Le cours la présente comme une critique théorique importante mais non universellement vérifiée ; et Barro lui-même montre en 1990 que les infrastructures publiques productives soutiennent la croissance de long terme.")])

d('n15-dette-publique', [25],
  faits=[("Les critères de Maastricht retiennent 3 % de déficit public et 60 % de dette publique ; le traité est signé en 1992 et entré en vigueur en 1993, et le Pacte de stabilité et de croissance de 1997 complète cet encadrement.",
          "Le cours rappelle que ces seuils ne sont ni des interdictions absolues ni inconditionnelles : ils encadrent un instrument resté national face à une politique monétaire devenue unique.")])

# ===================================================== ensemble 19 : compétitivité
d('n19-competitivite-prix', [26],
  mec=[("Le taux de change réel comme mesure, et ses deux leviers",
        "Le taux de change réel corrige le taux nominal par les niveaux de prix : il mesure le prix relatif des produits nationaux et étrangers. On peut donc l’améliorer par la parité — dévaluation compétitive — ou par les prix internes — désinflation compétitive. Le taux effectif réel, pondéré par le poids commercial des partenaires, en est la forme pertinente.")],
  faits=[("Une dévaluation de 10 % porte le solde commercial à + 4,6 avec des élasticités-prix de 0,8 et 0,6, mais le dégrade à − 4,8 avec des élasticités de 0,3 et 0,2.",
          "Ce n’est donc pas la baisse du taux de change qui garantit l’amélioration du solde, mais la réaction des volumes échangés — c’est-à-dire la structure productive.")])

d('n19-competitivite-hors-prix', [26],
  mec=[("Pourquoi la monnaie ne l’atteint pas",
        "Une politique de change agit exclusivement sur le prix. Lorsque les acheteurs privilégient la qualité, l’innovation, la marque ou la technologie, les volumes réagissent plus faiblement aux variations de prix : la dévaluation masque un déficit de gamme sans le corriger, et une sous-évaluation durable peut même réduire l’incitation à la montée en gamme.")],
  args=[("Le cercle vertueux de la monnaie forte repose précisément sur cette logique : en abaissant les prix à l’importation et en accroissant la pression concurrentielle, elle contraint les entreprises aux gains de productivité et à la compétitivité hors prix.",
         "Il faut que les entreprises disposent des moyens d’investir, c’est-à-dire de marges et de débouchés anticipés suffisants.",
         "Le cours nuance : une faible sensibilité des exportations aux prix peut traduire un fort pouvoir de marché plutôt qu’un manque de compétitivité.")])

d('n19-competitivite-cout', [26],
  faits=[("Le cours compare l’Allemagne et la France au début des années 2000 : deux stratégies de compétitivité distinctes.",
          "La comparaison montre que la compétitivité-coût et la compétitivité hors prix ne sont pas substituables : une économie peut conserver des positions commerciales avec une monnaie forte si sa spécialisation la rend peu sensible aux prix.")],
  mec=[("Le comportement de marge comme variable intermédiaire",
        "Pour gagner des volumes après une dévaluation, les exportateurs doivent répercuter la baisse sur leurs prix en devises. Ils peuvent au contraire maintenir leurs prix et reconstituer leurs marges : les volumes ne progressent alors pas. Le rôle de la concurrence détermine cet arbitrage.")])

# ===================================================== ensemble 20 : extérieur
d('n20-balance-paiements', [25],
  mec=[("La balance globale, et non le seul solde courant",
        "La courbe BP rassemble les couples de revenu et de taux d’intérêt compatibles avec l’équilibre de la balance globale, somme du solde courant et des mouvements autonomes de capitaux. Elle est croissante : une hausse du revenu accroît les importations, dégrade le solde courant et exige d’attirer des capitaux, donc d’élever le taux d’intérêt.")],
  faits=[("Un excédent courant de 100 accompagné de sorties de capitaux de 140 donne une balance globale déficitaire de 40.",
          "Le solde courant seul ne permet donc jamais de conclure sur l’équilibre extérieur : c’est la balance globale qui détermine la position par rapport à la courbe BP.")])

d('n20-balance-commerciale', [26],
  mec=[("Effet-prix contre effet-volume",
        "Une dévaluation combine un effet-volume favorable — exportations moins chères en devises, importations plus chères — et un effet-prix défavorable, puisque chaque unité importée coûte davantage. Le solde ne s’améliore que si la somme des élasticités-prix, en valeur absolue, dépasse l’unité : c’est la condition de Marshall-Lerner.")],
  faits=[("La courbe en J décrit trois phases : domination des effets-prix à court terme et dégradation du solde, apparition des effets-volume à moyen terme, puis amélioration ou érosion des gains selon l’inflation importée.",
          "Les effets bénéfiques d’une dévaluation ne sont donc jamais immédiats, et leur persistance n’est pas garantie.")])

d('n20-taux-change-nominal-reel', [26],
  mec=[("Nominal, effectif, réel : trois mesures et trois usages",
        "Le taux nominal bilatéral mesure la valeur relative de deux monnaies, à la cotation au certain ou à l’incertain. Le taux effectif nominal est une moyenne pondérée des taux bilatéraux selon le poids des partenaires. Le taux réel corrige par les niveaux de prix et mesure la compétitivité-prix relative : c’est lui qui compte pour l’analyse économique.")],
  faits=[("Dans l’exemple simplifié du cours, les pondérations du taux effectif sont de 40 % pour les États-Unis, 35 % pour la Chine et 25 % pour le Royaume-Uni.",
          "Une monnaie peut donc se déprécier face à une devise tout en s’appréciant en termes effectifs : raisonner sur un seul taux bilatéral conduit à des conclusions fausses.")])

d('n20-changes-fixes-flottants', [25, 26],
  mec=[("Le régime détermine quel instrument reste efficace",
        "En changes fixes avec mobilité parfaite des capitaux, une relance budgétaire est amplifiée par l’accompagnement monétaire qu’exige la défense de la parité, tandis que l’expansion monétaire est intégralement neutralisée. En changes flexibles, la hiérarchie s’inverse exactement : le budget est neutralisé par l’appréciation, la monnaie amplifiée par la dépréciation.")],
  faits=[("D’après les données de 2025, 29 pays pratiquent un arrimage ferme (13 %), 88 un arrimage souple (46 %), 66 un flottement (34 %) et 13 ne sont pas classés (7 %).",
          "Une majorité de pays ne pratiquent donc pas un flottement totalement libre : les régimes forment un continuum, et non une alternative entre deux options.")],
  aut=[("Guillermo Calvo",
        "La peur du flottement (2002) explique le maintien de nombreux régimes d’ancrage.",
        "L’endettement en devises, par effet de bilan, et le risque d’inflation importée rendent les dépréciations potentiellement déstabilisatrices : le flottement n’est pas une option neutre.")])

d('n20-crise-change', [26],
  mec=[("Le mécanisme autoréalisateur et l’asymétrie des interventions",
        "Un investisseur qui anticipe une dévaluation vend la monnaie avant sa baisse pour la racheter plus bas. Si de nombreux opérateurs agissent ainsi, la banque centrale doit mobiliser des réserves nécessairement limitées, et la défense devient impossible : l’anticipation produit la dévaluation qu’elle prévoyait. Freiner une appréciation est au contraire relativement facile, puisque la banque centrale peut créer sa propre monnaie.")],
  faits=[("Les crises du SME de 1992-1993 conduisent à élargir les marges de fluctuation à ± 15 % en août 1993 ; le cours cite également l’exemple du peso argentin et le régime de convertibilité argentin de 1991 à 2002.",
          "Dans un monde de capitaux mobiles, une parité fixe mais défendable devient intenable : l’échec de la voie intermédiaire prépare le passage à la monnaie unique.")],
  diss=[("Sujet du type « Les crises de change sont-elles inévitables ? »",
         "Il faut distinguer les crises qui sanctionnent une incohérence des fondamentaux, évitables par une politique alignée sur le pays d’ancrage, et les crises autoréalisatrices, contre lesquelles aucune rigueur ne protège puisque c’est le coût politique de la défense que les marchés évaluent.")])

d('n20-devaluation-reevaluation', [26],
  mec=[("Dévaluation subie et dévaluation compétitive",
        "Une dévaluation subie est imposée par les déséquilibres et les pressions des marchés ; une dévaluation compétitive est une stratégie délibérée de conquête de parts de marché. La distinction est décisive : les trois dévaluations françaises d’octobre 1981, juin 1982 et mars 1983 sont principalement subies, les autorités cherchant initialement à maintenir le franc dans le SME.")],
  faits=[("Les dévaluations font l’objet d’un encadrement international : dans le dispositif initial de Bretton Woods, les changements cumulés de parité dépassant 10 % relevaient d’une procédure de consultation et d’examen par le FMI.",
          "Le cours précise qu’un seuil de 15 % est également évoqué et qu’il ne faut pas présenter ces chiffres comme une règle générale et permanente d’autorisation automatique.")],
  args=[("Le cercle vicieux de la monnaie faible montre qu’une dévaluation peut appeler la suivante : inflation importée, effets de second tour, érosion du gain, déficit persistant, anticipations de dévaluation, épuisement des réserves.",
         "Il faut que l’économie soit suffisamment ouverte pour que l’inflation importée neutralise rapidement l’avantage initial.",
         "La stratégie inverse — maintenir la parité et comprimer l’inflation interne — a ses propres coûts : croissance faible et chômage durablement élevé.")])

d('n20-parite-des-taux-d-interet', [26],
  mec=[("Les déterminants de court terme dominent",
        "À court terme, ce sont les écarts de taux d’intérêt, les mouvements de capitaux et les anticipations qui commandent le taux de change, non les écarts d’inflation. Le développement du marché des changes révèle une déconnexion croissante entre transactions financières et échanges réels, ce qui explique que le change puisse s’écarter durablement de la parité des pouvoirs d’achat.")],
  faits=[("L’appréciation du dollar au début des années 1980 illustre ce mécanisme : la hausse des taux américains attire les capitaux, et les anticipations d’appréciation la renforcent de façon autoréalisatrice.",
          "La séquence conduit au creusement du déficit commercial américain, dans un contexte de déficits jumeaux, puis aux accords du Plaza de septembre 1985.")])

d('n20-epargne-investissement-ouverte', [25],
  mec=[("Le multiplicateur ouvert et la fuite par les importations",
        "Les importations dépendent positivement du revenu : M = M₀ + mY, où m est la propension marginale à importer — à ne pas confondre avec le ratio importations / PIB, qui mesure un poids et non une variation. Le multiplicateur devient 1 / (1 − c + m) et passe de 5 à 2 dans l’exemple du cours.")],
  args=[("L’interdépendance engendre des effets de débordement : la relance d’un pays stimule les exportations de ses partenaires, dont la production et les revenus augmentent.",
         "Il faut une intégration commerciale suffisante pour que les effets de retour soient significatifs.",
         "D’où la tentation du passager clandestin : si chacun attend que l’autre relance, aucune relance suffisante n’est engagée — ce qui justifie la coordination.")])

d('n20-desequilibres-mondiaux', [26],
  faits=[("Les excédents courants cumulés des pays de l’OPEP atteignent environ 450 milliards de dollars entre 1974 et 1981, recyclés par le système financier international vers les pays en développement.",
          "Le choc Volcker transforme cet endettement en crise : la dette extérieure de l’Amérique latine passe d’environ 75 milliards de dollars en 1975 à 315 milliards en 1983, son service de 12 à 66 milliards, et la crise mexicaine de 1982 en marque le déclenchement.")],
  args=[("Les déséquilibres extérieurs persistent en changes flottants : c’est la troisième limite des arguments flexibilistes, l’ajustement automatique promis par la dépréciation ne s’observant pas.",
         "Il faudrait que les élasticités-prix soient suffisantes et que les capitaux ne financent pas durablement les déficits.",
         "La doctrine Miran, dans un rapport de novembre 2024, soutient inversement que la demande internationale d’actifs sûrs en dollars entretient une surévaluation américaine.")])

d('n20-position-exterieure-nette', [26],
  mec=[("L’effet de bilan",
        "Lorsque la dette est libellée en devises, une dépréciation alourdit mécaniquement sa charge en monnaie nationale, alors que les revenus qui doivent la servir restent en monnaie locale. Le flottement cesse alors d’être une option neutre pour devenir un risque de solvabilité : c’est l’un des deux mécanismes de la peur du flottement.")])

# ===================================================== ensemble 21 : SMI
d('n21-bretton-woods', [25, 26],
  mec=[("La combinaison du triangle de Mundell que Bretton Woods retient",
        "Le système associe des changes fixes mais ajustables et une autonomie monétaire relative, grâce au contrôle des mouvements de capitaux — ce que le cours nomme la fermeture du bas de la balance des paiements. Le sommet sacrifié est donc la mobilité des capitaux, et c’est la montée de cette mobilité qui rendra la combinaison intenable.")],
  faits=[("Dans le dispositif initial, les changements cumulés de parité dépassant 10 % relevaient d’une procédure de consultation et d’examen par le FMI.",
          "La fixité était donc encadrée et non absolue : l’ajustement restait possible, mais soumis à une discipline collective."),
         ("La convertibilité du dollar en or est suspendue le 15 août 1971 ; en 1973, les principales monnaies passent à un flottement généralisé.",
          "Le triangle de Mundell permet de lire cet effondrement : la libéralisation financière rendait l’arbitrage initial de plus en plus coûteux à maintenir.")],
  aut=[("Jean-Marc Daniel",
        "« Le monde a accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle des incompatibilités de Robert Mundell. »",
        "La formule interdit la lecture téléologique : Bretton Woods n’était pas un système archaïque remplacé par un système moderne, mais un arbitrage différent entre trois objectifs également souhaitables.")])

d('n21-monnaie-internationale', [26],
  mec=[("Les trois fonctions internationales du dollar",
        "Monnaie véhiculaire, il sert d’intermédiaire dans des transactions qui ne concernent pas directement les États-Unis. Unité de compte, il libelle de nombreux contrats et matières premières. Réserve de valeur internationale, il constitue une part importante des réserves des banques centrales. Le marché des changes lui-même est dominé par le dollar.")],
  faits=[("Le cours relève quatre-vingts ans de domination du dollar, mais aussi l’appréciation de l’euro face au dollar depuis son point bas de 2022 et la dépréciation de plusieurs monnaies émergentes.",
          "La position reste dominante, mais la doctrine Miran de novembre 2024 la réévalue de l’intérieur en soutenant que la surévaluation qui en résulte pénalise l’industrie manufacturière américaine.")],
  args=[("Le paradoxe du dollar : déprécier la monnaie de réserve mondiale réduit la valeur externe des placements qui y sont libellés et risque de miner la confiance dans les actifs américains.",
         "Il faudrait que la demande internationale d’actifs sûrs se maintienne malgré la perte de valeur externe — dans l’exemple du cours, un patrimoine perd 20 %.",
         "D’où la recherche de nouvelles sources de demande privée, notamment par les stablecoins adossés au dollar, encadrés depuis juillet 2025 par le GENIUS Act.")])

d('n21-convergence-europeenne', [26],
  mec=[("Du SME à l’euro : une réponse institutionnelle au triangle",
        "Le SME, de 1979 à 1993, limite les fluctuations bilatérales par des parités centrales assorties de bandes de ± 2 %, élargies à ± 15 % en août 1993 après les crises de 1992-1993. L’euro, en 1999, préserve la stabilité monétaire interne et la libre circulation des capitaux en transférant la souveraineté monétaire à la BCE : le sommet sacrifié devient l’autonomie monétaire nationale.")],
  faits=[("Les différentiels de taux d’intérêt jouent un rôle central dans les tensions du SME : c’est par eux que la mobilité croissante des capitaux met en échec une parité fixe mais défendable.",
          "L’échec de la voie intermédiaire explique le passage à la monnaie unique : il ne restait, dans un monde de capitaux mobiles, que les deux solutions extrêmes.")])

# ===================================================== ensembles 26 et 28
d('n26-epargne-investissement', [25],
  mec=[("Le renversement de la causalité par le multiplicateur",
        "De Y = C + I et Y = C + S on tire I = S : c’est une identité comptable ex post. Mais avec c = 0,8, un investissement de 100 engendre 500 de revenu, dont 20 % sont épargnés, soit exactement 100. L’épargne n’a donc pas précédé l’investissement : elle en est le produit. La causalité keynésienne va de l’investissement au revenu puis à l’épargne.")],
  args=[("L’égalité ex post n’implique aucune coordination ex ante : l’épargne désirée et l’investissement désiré sont décidés par des agents différents et peuvent parfaitement différer.",
         "C’est la critique post-keynésienne, que le cours formule explicitement.",
         "L’écart se résorbe alors par les variations de stocks, du revenu et de l’emploi — c’est-à-dire par un ajustement coûteux, et non par un mécanisme de prix.")])

d('n26-equilibre-desequilibre', [25],
  mec=[("Trois modèles, trois dimensions de l’équilibre",
        "IS-LM analyse les politiques de demande en économie fermée à prix fixes. OG-DG réintroduit le niveau général des prix et permet d’analyser inflation, déflation et chocs d’offre. IS-LM-BP ajoute l’équilibre extérieur et montre que l’efficacité des politiques dépend du régime de change et de la mobilité des capitaux.")],
  args=[("Le cours en tire une conclusion méthodologique : aucun modèle macroéconomique ne permet à lui seul d’analyser toutes les situations.",
         "Le premier acte d’analyse consiste donc à identifier la configuration — position par rapport au potentiel, pente de LM, régime de change, mobilité des capitaux — avant de choisir l’outil.",
         "Appliquer IS-LM à une économie au plein emploi conduit à une conclusion fausse non parce que le modèle est mauvais, mais parce qu’il est hors de son domaine de validité.")])

d('n26-monnaie-neutre-active', [25],
  faits=[("Le modèle IS-LM repose sur trois hypothèses : la monnaie est active, le raisonnement est de court terme, le niveau général des prix est fixe.",
          "C’est cette dernière hypothèse qui interdit d’analyser l’inflation et qui a rendu le modèle inopérant face à la stagflation des années 1970, imposant le recours au modèle OG-DG.")],
  mec=[("La démonstration monétariste de la neutralité de long terme",
        "Au plein emploi, la relance déplace IS vers la droite ; la hausse des prix réduit l’offre réelle de monnaie et déplace LM vers la gauche ; le taux d’intérêt monte et évince l’investissement privé. L’économie retrouve exactement YPE avec un taux plus élevé : la relance n’a produit qu’une recomposition de la demande et une hausse des prix.")])

d('le28-efficacite-protectionnisme', [25],
  args=[("L’analyse du multiplicateur fournit un argument protectionniste : limiter les importations réduirait la fuite et adresserait une part plus importante de la demande aux producteurs nationaux, le multiplicateur passant de 1 / (1 − c + m) vers 1 / (1 − c).",
         "Il faudrait que les importations soient effectivement substituables par une production nationale, ce que la désindustrialisation compromet.",
         "Le cours confronte immédiatement cet argument aux coûts des restrictions et à l’intérêt d’une coordination des relances : les importations des uns étant les exportations des autres, la coopération obtient collectivement ce que la protection cherche individuellement.")])

d('le28-tentation-protectionnisme', [25, 26],
  args=[("La coordination des relances est collectivement supérieure à la protection : elle internalise les effets de débordement, puisque les importations des uns deviennent les exportations des autres.",
         "Il faut que les positions dans le cycle et les préférences collectives soient suffisamment proches pour qu’une orientation commune convienne à tous.",
         "La tentation du passager clandestin la rend difficile à obtenir, et aucune autorité ne peut contraindre un État à tenir un engagement conjoncturel.")],
  faits=[("La guerre des monnaies obéit à la même logique que la guerre commerciale, avec une limite que le cours qualifie de fondamentale : les taux de change étant relatifs, tous les pays ne peuvent pas déprécier simultanément les uns par rapport aux autres.",
          "Une politique de change est donc intrinsèquement conflictuelle, ce qui explique l’encadrement international des dévaluations et les tentatives de coopération comme les accords du Plaza de 1985.")])
