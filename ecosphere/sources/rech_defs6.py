# -*- coding: utf-8 -*-
"""Définitions rédigées pour les notions du chapitre 6 de deuxième année
(« Taux de change et systèmes de change »).

Chaque entrée est rédigée à partir du passage du cours désigné par `anc`
(l'intitulé de la section) et n'ajoute rien qui ne s'y trouve. Aucune
attribution d'auteur n'est faite au-delà de ce que le chapitre établit.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias, distinction)
DEFS = [

 ("Devise", ['26'],
  "La devise : une monnaie étrangère",
  "Une devise est une monnaie étrangère, c’est-à-dire une monnaie considérée "
  "du point de vue d’un autre espace monétaire que celui où elle a cours "
  "légal. La distinction avec la monnaie est essentielle : la monnaie est une "
  "créance dotée d’un pouvoir libératoire général sur son territoire "
  "d’émission, tandis que la devise n’est utilisable à l’extérieur qu’à la "
  "mesure de sa convertibilité et de l’acceptation qu’elle rencontre.",
  ["monnaie etrangere"],
  "Une même unité est monnaie chez elle et devise ailleurs : la qualité "
  "dépend du point de vue, non de la monnaie."),

 ("Convertibilité", ['26'],
  "La convertibilité permet l’utilisation internationale d’une monnaie",
  "La convertibilité est la possibilité d’échanger librement une monnaie "
  "contre une autre. Elle conditionne l’utilisation internationale d’une "
  "monnaie : sans elle, une monnaie ne peut servir ni aux règlements "
  "internationaux, ni de réserve, ni d’unité de compte. C’est elle qui rend "
  "possible l’existence d’un marché des changes et qui permet à une monnaie "
  "d’exercer les fonctions internationales que le dollar remplit "
  "aujourd’hui.",
  ["convertibilite d une monnaie", "monnaie convertible"],
  "La convertibilité est une condition de l’usage international, non une "
  "garantie de stabilité du change."),

 ("Monnaie véhiculaire", ['26'],
  "Le dollar comme monnaie véhiculaire",
  "Une monnaie véhiculaire est une monnaie utilisée comme intermédiaire dans "
  "des transactions qui ne concernent pas directement son pays d’émission : "
  "plutôt que d’échanger directement deux monnaies peu traitées, les "
  "opérateurs passent par elle. Le dollar occupe cette position centrale sur "
  "le marché des changes, ce qui se cumule avec ses fonctions d’unité de "
  "compte et de réserve de valeur internationale et explique sa place dans le "
  "système monétaire international.",
  ["monnaie vehiculaire internationale", "role vehiculaire du dollar"],
  "À distinguer des deux autres fonctions internationales d’une monnaie, "
  "l’unité de compte et la réserve de valeur."),

 ("Taux de change nominal bilatéral", ['26'],
  "Le taux de change nominal bilatéral",
  "Le taux de change nominal bilatéral est le prix d’une monnaie exprimé dans "
  "une autre : il mesure la valeur relative de deux monnaies à un moment "
  "donné. Il se lit de deux manières, selon la convention de cotation "
  "retenue, et son évolution décrit l’appréciation ou la dépréciation de la "
  "monnaie considérée.",
  ["taux de change bilateral", "taux de change nominal"],
  "Nominal et non réel : il ne tient pas compte des écarts de prix entre les "
  "deux économies."),

 ("Cotation au certain", ['26'],
  "La cotation au certain",
  "La cotation au certain exprime le prix d’une unité de monnaie nationale en "
  "monnaie étrangère : c’est la convention retenue pour l’euro, coté en "
  "dollars. Dans cette convention, une hausse du taux signifie une "
  "appréciation de la monnaie nationale. La cotation à l’incertain fait "
  "l’inverse : elle exprime le prix d’une unité de monnaie étrangère en "
  "monnaie nationale, et une hausse du taux y signifie alors une "
  "dépréciation.",
  ["cotation a l incertain", "convention de cotation"],
  "Confondre les deux conventions inverse le sens de l’appréciation et de la "
  "dépréciation : c’est l’erreur la plus fréquente du chapitre."),

 ("Taux de change effectif", ['26'],
  "Le taux de change effectif nominal",
  "Le taux de change effectif est une moyenne des taux de change bilatéraux "
  "d’une monnaie, pondérée par le poids des partenaires commerciaux : il donne "
  "une approche multilatérale de sa valeur externe, là où un taux bilatéral ne "
  "renseigne que sur une relation. Une monnaie peut ainsi se déprécier face à "
  "une devise tout en s’appréciant en termes effectifs.",
  ["taux de change effectif nominal", "taux de change multilateral"],
  "À distinguer du taux de change réel, qui corrige des écarts de prix ; "
  "l’effectif corrige de la structure des échanges."),

 ("Taux de change réel", ['26'],
  "Le taux de change réel mesure la compétitivité-prix relative",
  "Le taux de change réel corrige le taux de change nominal des niveaux de "
  "prix des deux économies : il mesure donc la compétitivité-prix relative. "
  "Une monnaie peut rester stable nominalement et perdre en compétitivité si "
  "son inflation est plus forte que celle de ses partenaires ; inversement, "
  "une inflation plus faible agit comme une appréciation réelle évitée. C’est "
  "pourquoi la désinflation compétitive cherche un gain de compétitivité par "
  "les prix et non par la parité.",
  ["competitivite prix relative", "taux de change reel effectif"],
  "Un change nominal stable ne garantit pas un change réel stable : tout "
  "dépend du différentiel d’inflation."),

 ("Marché des changes", ['26'],
  "Le Forex est un marché international dématérialisé",
  "Le marché des changes, ou Forex, est le marché sur lequel se confrontent "
  "l’offre et la demande de devises et où se forme le prix des monnaies. "
  "International et dématérialisé, il fonctionne presque en permanence, est "
  "dominé par le dollar et constitue principalement un marché de gros où "
  "interviennent les banques et les investisseurs institutionnels. Son "
  "développement spectaculaire — essor du commerce international, "
  "multiplication des produits dérivés, montée des investisseurs "
  "institutionnels — révèle la financiarisation de l’économie mondiale et une "
  "déconnexion croissante entre transactions financières et échanges réels.",
  ["forex", "marche des devises"],
  "La formation du taux de change y dépend du régime de change : en change "
  "fixe ou administré, la banque centrale intervient pour tenir la parité."),

 ("Arbitrage sur le marché des changes", ['26'],
  "L’arbitrage tend à unifier les cotations",
  "L’arbitrage consiste à tirer parti, sans risque, d’un écart de cotation "
  "entre deux places ou deux séquences d’opérations : en achetant là où la "
  "monnaie est moins chère pour revendre là où elle l’est davantage, les "
  "opérateurs font disparaître l’écart. L’arbitrage tend donc à unifier les "
  "cotations sur l’ensemble du marché des changes.",
  ["arbitrage de change", "unification des cotations"],
  "À distinguer de la spéculation, qui prend un risque sur l’évolution "
  "future, et de la couverture, qui le réduit."),

 ("Couverture du risque de change", ['26'],
  "La couverture : réduire l’exposition au risque de change",
  "La couverture consiste à réduire son exposition au risque de change en "
  "fixant à l’avance les conditions d’une opération future, notamment par des "
  "opérations à terme, des options ou des swaps. Elle répond à une attitude "
  "d’aversion au risque : l’agent accepte de renoncer à un gain éventuel pour "
  "s’assurer contre une variation défavorable de la parité.",
  ["hedging", "couverture de change", "operation a terme"],
  "Oppose à la spéculation la même technique employée dans un but inverse : "
  "réduire l’exposition au lieu de l’accepter."),

 ("Spéculation sur le marché des changes", ['26'],
  "La spéculation : accepter une exposition dans l’espoir d’un gain",
  "La spéculation consiste à accepter volontairement une exposition au risque "
  "de change dans l’espoir d’un gain tiré de l’évolution anticipée de la "
  "parité. Le chapitre en montre l’ambivalence : en période calme, des "
  "anticipations de retour à la moyenne conduisent les spéculateurs à acheter "
  "une monnaie sous-évaluée et à vendre une monnaie surévaluée, ce qui "
  "stabilise le change ; en période de crise, des anticipations de poursuite "
  "de la tendance amplifient au contraire les déséquilibres. Le marché des "
  "changes peut donc être simultanément stabilisateur et déstabilisateur.",
  ["speculation de change", "anticipations mimetiques de change"],
  "Ni stabilisatrice ni déstabilisatrice par nature : tout dépend du type "
  "d’anticipations qui domine."),

 ("Parité des pouvoirs d’achat", ['26'],
  "Gustav Cassel en 1918 développe la théorie de la parité des pouvoirs d’achat",
  "La théorie de la parité des pouvoirs d’achat, développée par Gustav Cassel "
  "en 1918, explique le taux de change par les différences de niveaux de prix "
  "entre les économies. Sous sa forme absolue, elle détermine un taux "
  "d’équilibre à partir des niveaux de prix, ce qui permet de repérer les "
  "monnaies surévaluées ou sous-évaluées en comparant le change observé au "
  "change de PPA. Sous sa forme relative, elle explique les variations du "
  "change par les écarts d’inflation : avec 6 % d’inflation dans la zone euro "
  "contre 2 % aux États-Unis, l’euro devrait se déprécier d’environ 4 %. Ses "
  "limites empiriques sont importantes : coûts de transaction, biens non "
  "échangeables, effet Balassa-Samuelson et mouvements de capitaux éloignent "
  "durablement le change de la PPA.",
  ["ppa", "parite de pouvoir d achat", "cassel 1918"],
  "La PPA absolue détermine un niveau, la PPA relative une variation : seule "
  "la seconde résiste partiellement à l’épreuve des faits."),

 ("Loi du prix unique", ['26'],
  "La loi du prix unique constitue le fondement de la PPA",
  "La loi du prix unique énonce qu’en l’absence d’obstacle aux échanges, un "
  "même bien doit se vendre au même prix partout une fois converti dans une "
  "monnaie commune, l’arbitrage éliminant les écarts. Elle constitue le "
  "fondement de la parité des pouvoirs d’achat, et c’est son démenti partiel "
  "— coûts de transaction, biens non échangeables — qui explique les limites "
  "de la PPA.",
  ["loi du prix unique internationale"],
  "Vaut pour un bien échangeable : les services et les biens non échangeables "
  "y échappent largement."),

 ("Effet Balassa-Samuelson", ['26'],
  "L’effet Balassa-Samuelson explique les différences durables de niveaux de "
  "prix",
  "L’effet Balassa-Samuelson, formulé en 1964, explique que les pays les plus "
  "productifs connaissent un niveau général des prix plus élevé : les gains de "
  "productivité portent surtout sur les biens échangeables, les salaires "
  "s’alignent dans l’ensemble de l’économie et renchérissent donc les services "
  "non échangeables. Il en résulte des écarts durables de niveaux de prix "
  "entre pays riches et pays pauvres, qui expliquent pourquoi le taux de "
  "change observé s’écarte systématiquement du taux de parité des pouvoirs "
  "d’achat.",
  ["balassa samuelson", "effet balassa samuelson 1964"],
  "Explique un écart durable à la PPA, non un déséquilibre à corriger."),

 ("Régime de change", ['26'],
  "Un régime de change est un ensemble de règles encadrant la détermination du "
  "taux de change",
  "Un régime de change est l’ensemble des règles qui encadrent la "
  "détermination du taux de change d’une monnaie. Son choix relève de la "
  "souveraineté monétaire et engage l’autonomie de la politique économique. "
  "Les régimes forment un continuum entre ancrage strict et flottement libre : "
  "dollarisation et union monétaire à une extrémité, caisse d’émission et "
  "changes fixes conventionnels ensuite, puis bandes de fluctuation, enfin "
  "flottement. En 2025, 29 pays pratiquent un arrimage ferme (13 %), 88 un "
  "arrimage souple (46 %), 66 un flottement (34 %) et 13 ne sont pas classés "
  "(7 %), ce qui confirme la diversité des choix monétaires.",
  ["regimes de change", "typologie des regimes de change"],
  "Même en changes flottants, les banques centrales peuvent intervenir : la "
  "frontière entre régimes est graduelle."),

 ("Dollarisation", ['26'],
  "La dollarisation et l’euroïsation : l’abandon de la monnaie nationale",
  "La dollarisation est l’abandon de la monnaie nationale au profit du dollar, "
  "l’euroïsation étant son équivalent avec l’euro. C’est la forme la plus "
  "stricte d’ancrage : le pays renonce à toute politique monétaire autonome et "
  "importe celle du pays émetteur, en échange d’une crédibilité monétaire "
  "immédiate. Elle se distingue de l’union monétaire, où les pays partagent "
  "une monnaie et participent à la décision monétaire commune.",
  ["euroisation", "abandon de la monnaie nationale"],
  "Dans la dollarisation le pays subit la politique monétaire d’un autre ; "
  "dans l’union monétaire il contribue à la définir."),

 ("Caisse d’émission", ['26'],
  "La caisse d’émission ou currency board",
  "La caisse d’émission, ou currency board, est un régime dans lequel "
  "l’émission de monnaie nationale est strictement gagée sur des réserves en "
  "devises, à une parité fixe garantie par la règle. Elle procure une "
  "crédibilité forte au prix d’un abandon presque complet de l’autonomie "
  "monétaire, la banque centrale ne pouvant plus créer de monnaie "
  "discrétionnairement. L’Argentine en a pratiqué une forme, sous le régime de "
  "convertibilité de 1991 à 2002.",
  ["currency board", "caisse d emission monetaire"],
  "Plus contraignante qu’un change fixe conventionnel, moins radicale que la "
  "dollarisation : la monnaie nationale subsiste."),

 ("Bandes de fluctuation", ['26'],
  "Les bandes de fluctuation",
  "Les bandes de fluctuation sont les marges à l’intérieur desquelles le taux "
  "de change est autorisé à varier autour de sa parité centrale, la banque "
  "centrale s’engageant à intervenir aux bornes. Le Système monétaire "
  "européen, de 1979 à 1993, retenait des marges de ± 2 % autour de la parité "
  "centrale, élargies à ± 15 % en août 1993 après les crises de 1992-1993. Il "
  "faut donc distinguer la parité centrale, qui est l’engagement, des bandes, "
  "qui en mesurent la souplesse.",
  ["parite centrale", "marges de fluctuation", "bande de fluctuation du sme"],
  "Un élargissement des bandes n’est pas une dévaluation : la parité centrale "
  "peut rester inchangée."),

 ("Peur du flottement", ['26'],
  "Calvo et Reinhart (2002) : la peur du flottement explique le maintien de "
  "nombreux régimes d’ancrage",
  "La peur du flottement, mise en évidence par Calvo et Reinhart en 2002, "
  "désigne la réticence de nombreux pays émergents à laisser réellement "
  "flotter leur monnaie, même lorsqu’ils déclarent un régime flottant. Deux "
  "raisons l’expliquent : l’endettement libellé en devises, qu’une dépréciation "
  "alourdit mécaniquement, et l’inflation importée qu’elle alimente. Elle "
  "explique le maintien d’interventions fréquentes et le décalage entre "
  "régimes déclarés et régimes effectivement pratiqués.",
  ["fear of floating", "calvo et reinhart 2002"],
  "Ce n’est pas un régime mais un comportement : un pays peut annoncer le "
  "flottement et le limiter en pratique."),

 ("Politique de change", ['26'],
  "La politique de change : agir sur la valeur externe de la monnaie",
  "La politique de change est l’action des autorités sur la valeur externe de "
  "la monnaie. Elle est particulièrement importante en changes fixes, où il "
  "faut défendre une parité, et repose sur trois instruments : les "
  "interventions sur le marché des changes au moyen des réserves, les taux "
  "d’intérêt, et le contrôle des mouvements de capitaux. Les politiques "
  "conjoncturelles l’influencent indirectement, puisqu’elles agissent sur les "
  "taux et sur l’activité.",
  ["instruments de la politique de change", "valeur externe de la monnaie"],
  "À distinguer de la politique monétaire interne, dont elle utilise pourtant "
  "les instruments : l’objectif est externe."),

 ("Guerre des monnaies", ['26'],
  "La guerre des monnaies",
  "La guerre des monnaies désigne l’enchaînement par lequel des États "
  "cherchent à déprécier leur monnaie pour gagner en compétitivité, chaque "
  "dépréciation appelant une riposte : l’avantage obtenu par l’un est pris aux "
  "autres, et le jeu est globalement perdant. C’est pourquoi les dévaluations "
  "font l’objet d’un encadrement international. Le chapitre identifie une "
  "forme nouvelle de ce conflit, lorsque les politiques conjoncturelles — "
  "notamment monétaires — produisent indirectement une dépréciation sans être "
  "présentées comme une politique de change.",
  ["guerre des changes", "devaluations competitives en chaine"],
  "À distinguer d’une dévaluation isolée : la guerre des monnaies est le jeu "
  "non coopératif qu’elle déclenche."),

 ("Dévaluation compétitive", ['26'],
  "Dévaluation subie et dévaluation compétitive",
  "Une dévaluation compétitive est une baisse volontaire de la parité destinée "
  "à améliorer la compétitivité-prix et le solde extérieur. Elle se distingue "
  "de la dévaluation subie, imposée par les marchés lorsqu’une parité n’est "
  "plus défendable : les trois dévaluations du franc d’octobre 1981, juin 1982 "
  "et mars 1983 relèvent principalement de ce second cas. Son efficacité est "
  "conditionnelle : la courbe en J retarde ses effets, la condition de "
  "Marshall-Lerner exige des élasticités suffisantes, et une spécialisation en "
  "compétitivité hors prix comme un comportement de marge des entreprises "
  "peuvent en annuler le bénéfice.",
  ["devaluation subie", "devaluation volontaire"],
  "Une dévaluation subie signale un échec de la politique de change ; une "
  "dévaluation compétitive prétend être un instrument."),

 ("Courbe en J", ['26'],
  "La courbe en J : les effets bénéfiques ne sont pas immédiats",
  "La courbe en J décrit le profil temporel des effets d’une dévaluation sur "
  "le solde commercial : dans un premier temps le solde se dégrade, les "
  "volumes n’ayant pas eu le temps de réagir alors que les importations "
  "coûtent déjà plus cher ; dans un second temps, l’ajustement des volumes "
  "l’améliore. Les effets bénéfiques ne sont donc pas immédiats, ce qui expose "
  "la politique de dévaluation à une mise en cause prématurée.",
  ["effet courbe en j", "profil en j du solde commercial"],
  "Décrit un délai d’ajustement, non une condition : même vérifiée, la "
  "condition de Marshall-Lerner laisse subsister la phase défavorable."),

 ("Condition de Marshall-Lerner", ['26'],
  "La condition de Marshall-Lerner : les élasticités critiques",
  "La condition de Marshall-Lerner énonce qu’une dévaluation n’améliore le "
  "solde commercial que si la somme des élasticités-prix des exportations et "
  "des importations, en valeur absolue, est supérieure à 1 : il faut que les "
  "volumes réagissent assez fortement pour compenser la dégradation des termes "
  "de l’échange. Le chapitre l’illustre : après une dévaluation de 10 %, le "
  "solde s’améliore de 4,6 avec des élasticités de 0,8 et 0,6, mais se dégrade "
  "de 4,8 avec des élasticités de 0,3 et 0,2.",
  ["elasticites critiques", "marshall lerner", "theoreme des elasticites critiques"],
  "Condition nécessaire portant sur les élasticités ; la courbe en J porte "
  "sur le délai, le comportement de marge sur la répercussion des prix."),

 ("Comportement de marge", ['26'],
  "Le comportement de marge peut limiter les gains de compétitivité",
  "Le comportement de marge désigne le choix des entreprises exportatrices de "
  "ne pas répercuter intégralement une dévaluation sur leurs prix en devises : "
  "elles préfèrent reconstituer leurs marges plutôt que gagner des parts de "
  "marché. Le gain de compétitivité-prix attendu de la dévaluation est alors "
  "en partie absorbé, et l’amélioration des volumes exportés s’en trouve "
  "réduite. Le degré de concurrence sur le marché conditionne ce choix.",
  ["marge a l exportation", "repercussion de la devaluation sur les prix"],
  "Explique qu’une dévaluation puisse rester sans effet sur les volumes alors "
  "même que la condition de Marshall-Lerner est vérifiée."),

 ("Cercle vicieux de la monnaie faible", ['26'],
  "Le cercle vicieux d’une monnaie faible",
  "Le cercle vicieux de la monnaie faible enchaîne l’érosion du gain de "
  "compétitivité par l’inflation importée, la persistance du déficit "
  "extérieur, l’anticipation d’une nouvelle dévaluation et la pression des "
  "marchés sur la monnaie, qui rend cette dévaluation inévitable. Les "
  "anticipations y sont autoréalisatrices, et le mécanisme peut se prolonger en "
  "crise de dette souveraine. Il constitue l’argument central en faveur de la "
  "stratégie inverse, celle de la monnaie forte.",
  ["cercle vicieux de la devaluation", "spirale de la monnaie faible"],
  "Symétrique du cercle vertueux de la monnaie forte : les deux "
  "enchaînements s’autoalimentent, en sens inverse."),

 ("Désinflation compétitive", ['26'],
  "L’objectif de la désinflation compétitive",
  "La désinflation compétitive est la stratégie qui consiste à rechercher la "
  "compétitivité non par la dévaluation mais par une inflation durablement "
  "inférieure à celle des partenaires, de façon à gagner en compétitivité "
  "réelle à parité stable. Engagée en France au tournant de la rigueur de mars "
  "1983, elle combine des politiques conjoncturelles — monnaie restrictive, "
  "maîtrise budgétaire — et des politiques structurelles de déréglementation, "
  "d’ouverture à la concurrence et de flexibilisation du marché du travail. "
  "L’inflation française passe ainsi d’environ 14 % au début des années 1980 à "
  "environ 2 % au début des années 1990.",
  ["politique de desinflation competitive", "tournant de la rigueur"],
  "Cherche le même objectif qu’une dévaluation compétitive — la "
  "compétitivité-prix — par le moyen exactement inverse."),

 ("Stratégie de monnaie forte", ['26'],
  "Le cercle vertueux d’une monnaie forte",
  "La stratégie de monnaie forte parie sur un enchaînement vertueux : une "
  "monnaie forte et stable abaisse les prix à l’importation, accroît la "
  "pression concurrentielle sur les entreprises, les oblige à des efforts de "
  "productivité et de compétitivité hors prix, améliore le solde extérieur et "
  "renforce la confiance dans la monnaie, ce qui soutient le change et permet "
  "de maintenir la monnaie forte. Le chapitre en reconnaît trois succès pour "
  "le franc fort — une désinflation importante, un redressement des "
  "transactions courantes et une restauration du taux de marge des entreprises, "
  "de 25 % en 1985 à 32 % en 1989 — mais aussi des effets pervers : croissance "
  "d’environ 2 % par an contre 3 % dans l’OCDE, et chômage passé d’environ 8 % "
  "en 1982 à environ 12 % en 1998.",
  ["franc fort", "monnaie forte", "cercle vertueux de la monnaie forte"],
  "Le bilan est contrasté, non négatif : des succès monétaires au prix de "
  "coûts économiques et sociaux durables."),

 ("Théorème de Schmidt", ['26'],
  "Le théorème de Schmidt",
  "Le théorème de Schmidt énonce que les profits d’aujourd’hui font les "
  "investissements de demain et les emplois d’après-demain : la restauration "
  "des marges doit donc se transmettre à l’investissement puis à l’emploi. Le "
  "chapitre l’utilise pour éclairer le paradoxe du franc fort : le taux de "
  "marge est bien restauré, de 25 % en 1985 à 32 % en 1989, mais la "
  "transmission ne se produit pas. Deux raisons l’expliquent : la "
  "globalisation financière multiplie les placements alternatifs à "
  "l’investissement productif, et l’investissement dépend avant tout des "
  "débouchés anticipés, que les politiques de rigueur affaiblissent sans que "
  "la demande extérieure compense.",
  ["profits investissements emplois", "theoreme de schmidt"],
  "Le chapitre ne le réfute pas : il montre que ses conditions de "
  "transmission ne sont pas réunies."),

 ("Taux d’intérêt réel", ['26'],
  "La distinction entre taux d’intérêt nominal et taux d’intérêt réel",
  "Le taux d’intérêt réel est le taux nominal corrigé de l’inflation : c’est "
  "lui qui mesure le coût véritable d’un emprunt et le rendement véritable "
  "d’un placement. La désinflation l’élève mécaniquement à taux nominal "
  "inchangé : pour un taux nominal de 10 %, il est de − 4 % avec 14 % "
  "d’inflation et de + 8 % avec 2 %. C’est ce basculement qui explique que la "
  "désinflation compétitive ait favorisé le désendettement des entreprises "
  "plutôt que l’investissement.",
  ["taux reel", "taux nominal et taux reel"],
  "Un taux nominal stable peut cacher un renversement complet du coût réel de "
  "la dette."),

 ("Effet de levier", ['26'],
  "L’effet de levier : lorsque l’endettement améliore la rentabilité financière",
  "L’effet de levier est le mécanisme par lequel l’endettement améliore la "
  "rentabilité financière de l’entreprise : il opère lorsque la rentabilité "
  "économique des projets dépasse le coût réel de la dette, l’écart "
  "bénéficiant aux fonds propres. Dans l’illustration du chapitre, une "
  "rentabilité économique de 10 % face à un coût réel de la dette de 4 % joue "
  "en faveur de l’emprunt.",
  ["levier d endettement", "rentabilite financiere et endettement"],
  "Se renverse en effet de massue dès que le coût réel de la dette dépasse la "
  "rentabilité économique."),

 ("Effet de massue", ['26'],
  "L’effet de massue : lorsque l’endettement devient pénalisant",
  "L’effet de massue est le renversement de l’effet de levier : lorsque le "
  "coût réel de la dette dépasse la rentabilité économique, l’endettement "
  "dégrade la rentabilité financière. L’illustration du chapitre oppose une "
  "rentabilité économique de 5 % à un coût réel de la dette de 8 %. C’est ce "
  "basculement, provoqué par la hausse des taux d’intérêt réels liée à la "
  "désinflation, qui conduit les entreprises à privilégier le désendettement "
  "plutôt que l’investissement.",
  ["effet de massue de la dette", "levier inverse"],
  "Même mécanisme que l’effet de levier, de signe opposé : c’est la "
  "comparaison des deux taux qui décide."),

 ("Inflation importée", ['26'],
  "La dépréciation peut alimenter l’inflation importée",
  "L’inflation importée est la hausse des prix intérieurs provoquée par le "
  "renchérissement des produits achetés à l’étranger. Une dépréciation de la "
  "monnaie en est la cause directe : elle augmente le prix en monnaie "
  "nationale des importations, matières premières et énergie comprises. C’est "
  "l’une des deux raisons de la peur du flottement des pays émergents, et "
  "c’est elle qui érode le gain de compétitivité attendu d’une dévaluation, "
  "enclenchant le cercle vicieux de la monnaie faible. Lutter contre elle est "
  "un des motifs d’une politique de monnaie forte.",
  ["inflation par les prix importes", "inflation importee par la depreciation"],
  "À distinguer d’une inflation d’origine interne : son déclencheur est la "
  "parité, non la demande intérieure."),

 ("Réserves de change", ['26'],
  "Les réserves de change et les risques liés aux ventes d’obligations",
  "Les réserves de change sont les avoirs en devises détenus par la banque "
  "centrale, qui lui permettent d’intervenir sur le marché des changes pour "
  "soutenir sa monnaie. Leur usage est contraint : soutenir une parité les "
  "épuise, et les vendre peut exiger de céder des obligations étrangères, ce "
  "qui comporte ses propres risques. Préserver les réserves est donc un objectif "
  "de la politique de change, et les lignes de swap entre banques centrales "
  "offrent une alternative en fournissant des devises sans ponction sur les "
  "réserves.",
  ["reserves de change de la banque centrale", "ligne de swap"],
  "Permettent de soutenir une monnaie, non de l’apprécier durablement : elles "
  "sont par nature limitées."),

 ("Recyclage des pétrodollars", ['26'],
  "Le recyclage des pétrodollars finance l’endettement des pays en "
  "développement",
  "Le recyclage des pétrodollars désigne le circuit par lequel les excédents "
  "accumulés par les pays exportateurs de pétrole après les chocs de 1973 et "
  "1979 — environ 450 milliards de dollars entre 1974 et 1981 — sont déposés "
  "dans les banques occidentales et prêtés aux pays en développement. La dette "
  "extérieure de l’Amérique latine passe ainsi d’environ 75 à 315 milliards de "
  "dollars entre 1975 et 1983. Le choc Volcker transforme cet endettement en "
  "crise de la dette : la hausse des taux américains renchérit le service de "
  "la dette, l’appréciation du dollar en alourdit le poids, et la crise "
  "mexicaine de 1982 en marque le déclenchement.",
  ["petrodollars", "endettement des pays en developpement"],
  "Montre que le flottement n’a pas garanti l’autonomie monétaire promise : "
  "la contrainte est passée par les taux et le dollar."),

 ("Stablecoin", ['26'],
  "Les stablecoins : une nouvelle source de demande privée de dollars",
  "Un stablecoin est un cryptoactif adossé à une monnaie officielle, dont il "
  "vise à reproduire la valeur — environ un dollar pour un stablecoin indexé "
  "sur le dollar, parité qui peut toutefois être perdue. Le chapitre y voit "
  "une nouvelle source de demande privée de dollars, puisque les réserves qui "
  "gagent ces jetons sont placées en actifs américains, et rattache cet enjeu "
  "à la réglementation américaine de 2025 encadrant les stablecoins.",
  ["stablecoins", "cryptoactif adosse a une monnaie"],
  "À distinguer des cryptoactifs non adossés, dont la valeur est libre, et "
  "des monnaies numériques de banque centrale, qui sont publiques."),

 ("Monnaie numérique de banque centrale", ['26'],
  "Les monnaies numériques de banque centrale (MNBC)",
  "Une monnaie numérique de banque centrale est une forme numérique de la "
  "monnaie officielle, émise et garantie par la banque centrale elle-même. "
  "Elle se distingue des cryptoactifs non adossés, dont la valeur n’est garantie "
  "par aucune institution, et des stablecoins, émis par des acteurs privés sur "
  "la foi de réserves.",
  ["mnbc", "monnaie digitale de banque centrale"],
  "Publique et garantie, là où le stablecoin est privé et adossé : la nature "
  "de l’émetteur fait la différence."),

 ("Doctrine Miran", ['26'],
  "La doctrine Miran : le dollar fort comme handicap pour l’économie américaine",
  "La doctrine Miran, exposée dans un rapport de novembre 2024, soutient que "
  "le dollar fort constitue un handicap pour l’économie américaine en "
  "pénalisant ses exportateurs, et envisage une dépréciation coordonnée du "
  "dollar sur le modèle des accords du Plaza de 1985 — le projet désigné comme "
  "« accords de Mar-a-Lago ». Le chapitre en souligne les nuances et les "
  "contradictions : les droits de douane renchérissent les importations et "
  "peuvent alimenter l’inflation, une coordination est difficile à obtenir, et "
  "déprécier la monnaie de réserve mondiale risque d’entamer la confiance dans "
  "les actifs américains qui fait précisément la force du dollar.",
  ["accords de mar a lago", "rapport miran"],
  "Projet discuté, non politique appliquée : le chapitre l’analyse comme une "
  "doctrine et en expose les contradictions."),

 ("Risque de change", ['26'],
  "Les options et les swaps permettent de gérer le risque de change",
  "Le risque de change est le risque de perte lié à une variation de la parité "
  "entre le moment où un engagement est pris et celui où il est dénoué. Les "
  "opérations à terme, les options et les swaps permettent de le gérer : ils "
  "fixent ou bornent à l’avance les conditions de l’échange de devises. Le "
  "même instrument sert à la couverture, pour réduire l’exposition, et à la "
  "spéculation, pour l’accepter volontairement.",
  ["risque de change pour l entreprise", "produits derives de change"],
  "La technique ne dit pas l’intention : c’est l’exposition recherchée qui "
  "distingue couverture et spéculation."),
]
