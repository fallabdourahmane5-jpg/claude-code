# -*- coding: utf-8 -*-
"""Ensemble 12 — Le financement de l’économie et la finance (3/4)."""

from doss_base import d

d('n12-diversification', 12, "Diversification du risque",
  "Répartir pour réduire, disperser pour propager",
  "La diversification du risque consiste à répartir les placements entre "
  "plusieurs actifs afin que la défaillance de l’un ne compromette pas "
  "l’ensemble. Le cours la présente comme un avantage des organismes de "
  "placement collectif en valeurs mobilières, qui permettent de diversifier "
  "les placements, actions, obligations et autres, et de réunir l’argent de "
  "plusieurs épargnants dans un portefeuille diversifié.",
  "Le cours traite la diversification à trois niveaux, et c’est le passage du "
  "troisième qui en fait un dossier critique. Au niveau de l’épargnant "
  "d’abord. Les organismes de placement collectif en valeurs mobilières "
  "réunissent l’argent de plusieurs épargnants pour l’investir dans un "
  "portefeuille diversifié de titres financiers, actions et obligations. Le "
  "cours en distingue deux formes : le fonds commun de placement, créé en "
  "1979, où l’investisseur est porteur de parts et copropriétaire du "
  "portefeuille, le fonds n’ayant pas de personnalité morale ; et la société "
  "d’investissement à capital variable, où l’investisseur est actionnaire. "
  "Leurs avantages sont explicitement la gestion professionnelle par des "
  "experts, la diversification du risque et un accès facile à différents "
  "marchés. Au niveau du marché ensuite : le marché à terme permet une "
  "couverture contre le risque, en fixant à l’avance le prix d’une "
  "transaction future, et les produits dérivés de crédit fonctionnent comme "
  "une assurance sur une dette, l’acheteur payant une prime et étant indemnisé "
  "en cas de défaut de l’emprunteur. Au niveau du système enfin, et c’est là "
  "que le cours renverse l’argument. La titrisation transforme des créances en "
  "titres négociables et a notamment pour objectif de transférer le risque ; "
  "les produits structurés regroupent plusieurs dettes en titres vendus à "
  "travers le monde. Mais le cours montre que la dispersion n’est pas une "
  "réduction : comme ces produits sont vendus à travers le monde, le risque "
  "est dispersé internationalement, de sorte que lorsque les défauts "
  "augmentent, la crise se propage très vite. Il ajoute que le même mécanisme "
  "dilue la responsabilité et rend les risques moins lisibles.",
  [("La mutualisation par le portefeuille",
    "Réunir l’argent de plusieurs épargnants dans un portefeuille diversifié "
    "permet d’acquérir de nombreux titres : la perte sur l’un est compensée "
    "par les autres, ce qui réduit la variabilité du rendement d’ensemble."),
   ("La gestion professionnelle",
    "La diversification exige une sélection et un suivi : les organismes de "
    "placement collectif les confient à des experts, ce qui donne à "
    "l’épargnant individuel un accès à des marchés qu’il ne pourrait pas "
    "suivre seul."),
   ("La couverture par les marchés à terme",
    "Fixer aujourd’hui le prix d’une transaction future supprime le risque de "
    "sa variation : la couverture ne répartit pas le risque, elle le "
    "transfère à une contrepartie qui l’accepte."),
   ("Le transfert par la titrisation",
    "En cédant ses créances à un véhicule qui émet des titres, la banque sort "
    "le risque de son bilan : elle transfère son exposition à des "
    "investisseurs dispersés, et récupère des liquidités pour financer de "
    "nouveaux crédits."),
   ("Le retournement de la dispersion en contagion",
    "Lorsque les titres issus de créances sont vendus à travers le monde, le "
    "risque est dispersé internationalement : une hausse des défauts atteint "
    "simultanément de nombreux détenteurs et la crise se propage très vite.")],
  [{'a': "La diversification réduit effectivement le risque supporté par "
         "l’épargnant individuel, en répartissant son épargne entre de "
         "nombreux titres.",
    'cond': "La réduction suppose que les rendements des titres détenus ne "
            "varient pas tous dans le même sens au même moment.",
    'lim': "Cette condition disparaît en crise : lorsque les défauts "
           "augmentent simultanément, la diversification ne protège plus et "
           "la perte frappe l’ensemble du portefeuille."},
   {'a': "Les organismes de placement collectif donnent à de petits "
         "épargnants un accès à une diversification et à une gestion "
         "professionnelle qu’ils ne pourraient pas obtenir seuls.",
    'cond': "L’avantage suppose que la gestion par des experts soit "
            "effectivement meilleure que la sélection individuelle, après "
            "frais.",
    'lim': "Le cours relève que le rendement dépend de la performance des "
           "placements réalisés par la société de gestion, ce qui remplace un "
           "risque de marché par un risque de gestion."},
   {'a': "La titrisation accroît la liquidité et la capacité de financement "
         "du système, en permettant aux banques de recycler leurs créances.",
    'cond': "Le gain suppose que les acquéreurs des titres puissent évaluer "
            "correctement la qualité des créances qu’ils achètent.",
    'lim': "Le cours relève que le produit devient très complexe et que "
           "l’investisseur ne voit plus toujours clairement la qualité réelle "
           "des créances contenues dans le panier."},
   {'a': "La dispersion internationale du risque évite qu’une perte "
         "n’écrase un seul acteur ni un seul système bancaire.",
    'cond': "Elle suppose que les détenteurs finaux soient suffisamment "
            "nombreux et solides pour absorber chacun une petite part.",
    'lim': "Le cours montre l’effet inverse : parce que ces produits sont "
           "vendus à travers le monde, la crise se propage très vite dès que "
           "les défauts augmentent."}],
  [{'t': "La diversification du risque est l’un des principaux avantages des "
         "organismes de placement collectif en valeurs mobilières.",
    'qui': "Le cours, dans sa présentation des fonds communs de placement et "
           "des sociétés d’investissement à capital variable.",
    'rep': "Le cours relève que le rendement dépend de la performance des "
           "placements réalisés par la société de gestion : la "
           "diversification réduit le risque spécifique mais n’élimine ni le "
           "risque de marché ni celui de la gestion."},
   {'t': "La titrisation améliore le système financier puisqu’elle accroît la "
         "liquidité et la capacité de financement en transférant le risque.",
    'qui': "La logique de la titrisation que le cours expose avant d’en "
           "montrer les limites.",
    'rep': "Le cours objecte qu’elle peut diluer la responsabilité, rendre "
           "les risques moins lisibles et favoriser des bulles, comme en 2007 "
           "et 2008."},
   {'t': "Disperser un risque entre de nombreux détenteurs le rend "
         "inoffensif pour le système financier dans son ensemble.",
    'qui': "La lecture de la dispersion comme réduction du risque "
           "systémique.",
    'rep': "Le cours montre le contraire avec les produits structurés : "
           "vendus à travers le monde, ils dispersent le risque "
           "internationalement, de sorte que la hausse des défauts propage la "
           "crise très vite."}],
  [{'n': "Henri Bourguinat",
    'i': "Le décloisonnement et la déréglementation ont multiplié les "
         "instruments de transfert du risque.",
    'p': "Le cours rattache à sa règle des trois D la globalisation "
         "financière, marquée par l’innovation financière et la montée de "
         "nouveaux acteurs : c’est elle qui rend possible la diffusion "
         "mondiale des produits issus de la titrisation."},
   {'n': "John Hicks",
    'i': "Le passage à une économie de marchés financiers modifie la manière "
         "de porter les risques.",
    'p': "Le cours reprend son opposition pour situer la diversification : "
         "dans l’économie d’endettement, le risque reste au bilan de la "
         "banque qui l’a sélectionné ; dans l’économie de marchés, il est "
         "réparti entre les porteurs de titres."},
   {'n': "Esther Duflo",
    'i': "Une mauvaise structure financière prive les projets innovants des "
         "financements dont ils ont besoin.",
    'p': "Le cours relève que là où les banques concentrent le financement et "
         "les marchés sont peu développés, il y a peu de diversification du "
         "risque et peu de capital-risque, d’où des projets innovants "
         "sous-financés et une productivité stagnante."}],
  [{'f': "Le cours décrit deux formes d’organismes de placement collectif : "
         "le fonds commun de placement, créé en 1979, où l’investisseur est "
         "porteur de parts sans personnalité morale du fonds, et la société "
         "d’investissement à capital variable, où il est actionnaire.",
    'p': "La distinction montre que la diversification est organisée par des "
         "structures juridiques précises, dont le statut détermine les droits "
         "de l’épargnant."},
   {'f': "Le cours attribue aux organismes de placement collectif trois "
         "avantages : gestion professionnelle par des experts, "
         "diversification du risque et accès facile à différents marchés.",
    'p': "L’énumération établit que la diversification est vendue comme un "
         "service, ce qui en fait un argument commercial autant qu’une "
         "propriété statistique."},
   {'f': "Le cours explique que les produits structurés étant vendus à "
         "travers le monde, le risque est dispersé internationalement, et "
         "que lorsque les défauts augmentent la crise se propage très vite.",
    'p': "Le mécanisme démontre que la dispersion transforme un risque "
         "concentré en risque systémique, au lieu de l’éteindre."}],
  [{'q': "La diversification réduit-elle le risque ?",
    'f': "Pour l’épargnant individuel, oui : répartir son épargne entre de "
         "nombreux titres fait que la perte sur l’un est compensée par les "
         "autres, et le cours en fait l’un des trois avantages des organismes "
         "de placement collectif. Pour le système, la réponse est inverse : "
         "disperser le risque internationalement fait que la hausse des "
         "défauts se propage très vite.",
    'r': "Le raisonnement change d’échelle, de l’individu au système, et "
         "montre qu’une propriété vraie au premier niveau devient fausse au "
         "second.",
    'ex': "Le cours relève la diffusion mondiale du risque par les produits "
          "structurés vendus à travers le monde."},
   {'q': "Transférer un risque, est-ce le supprimer ?",
    'f': "Non : le transfert déplace l’exposition sans la détruire. La "
         "titrisation permet à la banque de sortir une partie des créances de "
         "son bilan, de récupérer des liquidités et de transférer le risque, "
         "mais le risque est désormais porté par les acquéreurs des titres, "
         "souvent moins bien informés sur la qualité réelle des créances.",
    'r': "Le raisonnement suit le risque dans le bilan de chaque acteur, ce "
         "qui montre qu’il reste dans le système tout en devenant moins "
         "visible.",
    'ex': "Le cours relève que l’investisseur ne voit plus toujours "
          "clairement la qualité réelle des créances du panier."},
   {'q': "Pourquoi la diversification peut-elle aggraver une crise ?",
    'f': "Parce qu’elle multiplie les connexions. Si chaque détenteur ne "
         "porte qu’une petite part du risque, la perte est supportable "
         "individuellement ; mais tous les détenteurs sont exposés au même "
         "événement, de sorte qu’une hausse des défauts les atteint "
         "simultanément. Le cours ajoute que la complexité du produit empêche "
         "de savoir qui porte quoi.",
    'r': "On montre que la diversification réduit la perte individuelle mais "
         "augmente le nombre d’acteurs touchés, ce qui transforme la nature "
         "du risque plus qu’elle ne le diminue.",
    'ex': "Le cours relève que les mêmes mécanismes ont pu favoriser des "
          "bulles, comme en 2007 et 2008."}],
  voisins=['n13-contagion-financiere', 'n12-marches-financiers',
           'n13-risque-systemique', 'n12-allocation-epargne'])


d('n12-efficience', 12, "Efficience des marchés",
  "Les prix disent-ils la vérité sur les actifs ?",
  "L’efficience d’un marché financier désigne sa capacité à produire des prix "
  "qui reflètent correctement la valeur des actifs et à diriger les capitaux "
  "vers les emplois les plus productifs. Le cours l’énonce comme une "
  "hypothèse à tester : si le marché était parfaitement efficace, le capital "
  "irait naturellement vers les projets les plus productifs.",
  "Le cours aborde l’efficience par deux voies, l’une allocative et l’autre "
  "informationnelle, qui échouent toutes deux au test des faits. La voie "
  "allocative d’abord. Le raisonnement est posé comme une hypothèse : si le "
  "marché était parfaitement efficace, le capital irait naturellement vers les "
  "projets les plus productifs. Or le cours constate l’inverse dans de "
  "nombreux pays : le capital est mal distribué, l’innovation est freinée, les "
  "élites captent les rentes et les droits de propriété sont fragiles. Il en "
  "tire que le problème dépasse le marché lui-même et qu’il faut s’interroger "
  "sur les règles du jeu, ce qui conduit à l’analyse institutionnelle de "
  "Douglass North. La voie informationnelle ensuite. Le cours attribue à la "
  "Bourse la fonction de fournir une information de prix, ce qui suppose que "
  "les cotations renseignent effectivement sur la valeur des actifs. Mais il "
  "énumère les obstacles. Les marchés de gré à gré ne sont pas centralisés, "
  "sans place boursière organisée, avec une négociation bilatérale et moins de "
  "transparence. Les produits structurés de titrisation introduisent une "
  "opacité explicite : le produit devient très complexe et l’investisseur ne "
  "voit plus toujours clairement la qualité réelle des créances contenues dans "
  "le panier, puisqu’il s’agit d’un mélange de créances peu risquées et de "
  "créances très risquées. Le système bancaire parallèle est enfin décrit "
  "comme une finance de l’ombre, moins visible et parfois moins régulée. Le "
  "cours ajoute un contre-exemple décisif avec le Bitcoin, actif financier "
  "sans valeur sous-jacente, sans État ni garantie, sans intérêt ni dividende, "
  "dont la valeur dépend uniquement de l’offre et de la demande et qu’on "
  "achète surtout dans l’espoir de le revendre plus cher.",
  [("Le prix comme information",
    "La confrontation des ordres produit une cotation publique : la Bourse "
    "fournit ainsi une information de prix dont l’utilité dépend entièrement "
    "de la qualité des données que les émetteurs publient."),
   ("La condition de transparence",
    "Pour être coté, un émetteur doit publier une information financière "
    "transparente et accepter une surveillance : l’efficience "
    "informationnelle est donc une construction réglementaire et non une "
    "propriété spontanée."),
   ("L’opacité des produits complexes",
    "Un produit construit à partir d’un panier mêlant créances peu risquées "
    "et très risquées devient trop complexe pour que l’investisseur voie la "
    "qualité réelle de ce qu’il achète : le prix cesse de renseigner."),
   ("L’absence de centralisation",
    "Sur un marché de gré à gré, les transactions sont bilatérales et non "
    "centralisées : aucun prix public ne se forme, ce qui prive le reste du "
    "marché de l’information."),
   ("La valorisation sans sous-jacent",
    "Un actif sans valeur réelle, sans revenu ni garantie, ne peut être "
    "valorisé que par l’anticipation du prix de revente : le prix ne reflète "
    "alors rien d’autre que l’opinion du marché sur lui-même.")],
  [{'a': "L’hypothèse d’efficience fournit un étalon utile, puisqu’elle "
         "permet de mesurer l’écart entre l’allocation observée et "
         "l’allocation souhaitable.",
    'cond': "L’usage comme étalon suppose que l’on puisse estimer la "
            "productivité des emplois alternatifs du capital.",
    'lim': "Le cours constate que le capital est mal distribué dans de "
           "nombreux pays, de sorte que l’étalon ne décrit pas la réalité "
           "mais la met en accusation."},
   {'a': "La cotation en Bourse produit une information de prix publique, "
         "utile bien au-delà des parties à la transaction.",
    'cond': "Elle exige des émetteurs une information financière "
            "transparente et le respect d’obligations de publication.",
    'lim': "Les marchés de gré à gré et le système bancaire parallèle "
           "échappent à ces obligations, de sorte qu’une part croissante de "
           "la finance ne produit pas cette information."},
   {'a': "L’échec de l’efficience allocative justifie de porter l’analyse sur "
         "les institutions plutôt que sur les seuls mécanismes de marché.",
    'cond': "Le déplacement suppose que les règles du jeu, droits de "
            "propriété et sécurité juridique, influencent effectivement "
            "l’investissement.",
    'lim': "Douglass North rappelle que les institutions changent lentement, "
           "de sorte que le diagnostic ne fournit pas de remède rapide."},
   {'a': "L’opacité des produits complexes explique pourquoi les prix ont "
         "cessé de signaler le risque avant la crise de 2008.",
    'cond': "L’explication suppose que les investisseurs se soient fiés aux "
            "prix et aux notations plutôt qu’à l’examen des créances "
            "sous-jacentes.",
    'lim': "Elle n’explique pas à elle seule l’ampleur de la crise, à "
           "laquelle ont contribué l’effet de levier, la dispersion "
           "internationale et la concentration des acteurs systémiques."}],
  [{'t': "Si le marché était parfaitement efficace, le capital irait "
         "naturellement vers les projets les plus productifs.",
    'qui': "L’hypothèse d’efficience allocative que le cours énonce pour la "
           "soumettre aux faits.",
    'rep': "Le cours constate l’inverse : le capital est mal distribué, "
           "l’innovation est freinée, les élites captent les rentes et les "
           "droits de propriété sont fragiles, ce qui montre que le problème "
           "dépasse le marché lui-même."},
   {'t': "La Bourse fournit une information de prix fiable, qui permet aux "
         "agents de décider en connaissance de cause.",
    'qui': "La fonction que le cours attribue à la Bourse comme institution "
           "centrale des marchés financiers.",
    'rep': "Le cours relève que les produits structurés rendent les risques "
           "opaques, l’investisseur ne voyant plus clairement la qualité "
           "réelle des créances, et que les marchés de gré à gré offrent "
           "moins de transparence."},
   {'t': "Le prix d’un actif financier reflète la valeur de ce qu’il "
         "représente économiquement.",
    'qui': "La logique d’une valorisation par les revenus futurs.",
    'rep': "Le cours cite le Bitcoin comme contre-exemple : sans valeur "
           "sous-jacente, sans État, sans garantie, sans intérêt ni "
           "dividende, sa valeur dépend uniquement de l’offre et de la "
           "demande, donc hautement spéculative."}],
  [{'n': "Douglass North",
    'i': "Les institutions sont les règles formelles et informelles qui "
         "structurent les interactions humaines et réduisent l’incertitude.",
    'p': "Le cours le mobilise précisément là où l’efficience échoue : si le "
         "capital est mal alloué, c’est que le problème dépasse le marché et "
         "concerne les règles du jeu, droits de propriété, sécurité juridique "
         "et crédibilité des règles."},
   {'n': "Satoshi Nakamoto",
    'i': "Le Bitcoin repose sur un registre décentralisé où les transactions "
         "sont vérifiées par les utilisateurs eux-mêmes.",
    'p': "Le cours en tire un contre-exemple pour l’efficience : le Bitcoin "
         "ne repose sur aucune valeur réelle, ni État ni garantie ni revenu, "
         "de sorte que son prix ne reflète que l’offre et la demande, d’où "
         "une très forte volatilité."},
   {'n': "Henri Bourguinat",
    'i': "L’innovation financière et la déréglementation ont transformé les "
         "marchés depuis les années 1980.",
    'p': "Le cours rattache à sa règle des trois D le développement des "
         "marchés de gré à gré, du système bancaire parallèle et des produits "
         "structurés, c’est-à-dire précisément des segments les moins "
         "transparents de la finance."}],
  [{'f': "Le cours relève que dans de nombreux pays le capital est mal "
         "distribué, l’innovation est freinée, les élites captent les rentes "
         "et les droits de propriété sont fragiles.",
    'p': "Ce constat réfute directement l’hypothèse d’efficience allocative "
         "et oblige à chercher l’explication dans les institutions."},
   {'f': "Les produits structurés sont construits à partir d’un panier "
         "mêlant des créances peu risquées et des créances très risquées, de "
         "sorte que l’investisseur ne voit plus la qualité réelle de ce qu’il "
         "achète.",
    'p': "L’opacité démontre que l’innovation financière peut détruire "
         "l’information que les marchés sont censés produire."},
   {'f': "Le cours caractérise le système bancaire parallèle comme une "
         "finance de l’ombre, moins visible et parfois moins régulée.",
    'p': "L’expression montre qu’une part de la finance échappe par "
         "construction à la production d’information publique, ce qui borne "
         "l’efficience informationnelle de l’ensemble."}],
  [{'q': "Les marchés financiers allouent-ils efficacement le capital ?",
    'f': "Le cours soumet l’hypothèse à l’épreuve des faits et la réfute : si "
         "le marché était parfaitement efficace, le capital irait "
         "naturellement vers les projets les plus productifs, or il est mal "
         "distribué dans de nombreux pays, l’innovation est freinée et les "
         "élites captent les rentes. Le problème dépasse donc le marché "
         "lui-même et concerne les règles du jeu.",
    'r': "Le raisonnement traite l’efficience comme une proposition "
         "testable, puis conclut au déplacement de l’analyse vers les "
         "institutions.",
    'ex': "Le cours renvoie à Douglass North pour expliquer la mauvaise "
          "allocation."},
   {'q': "Les prix de marché sont-ils une bonne information ?",
    'f': "Ils peuvent l’être, puisque le cours attribue à la Bourse la "
         "fonction de fournir une information de prix, assortie de conditions "
         "exigeantes de transparence et de surveillance. Mais ils cessent de "
         "l’être dès que les produits deviennent trop complexes ou les "
         "marchés non centralisés : l’investisseur ne voit plus la qualité "
         "réelle des créances d’un panier structuré.",
    'r': "Le raisonnement conditionne la qualité de l’information à "
         "l’architecture du marché, ce qui explique que l’efficience varie "
         "selon les segments.",
    'ex': "Le cours relève que les marchés de gré à gré offrent moins de "
          "transparence et parfois plus de risques systémiques."},
   {'q': "Un actif peut-il valoir sans rien représenter ?",
    'f': "Le Bitcoin en fournit le cas limite. Le cours le présente comme un "
         "actif financier sans valeur sous-jacente, sans État, sans "
         "garantie, sans intérêt ni dividende, dont la valeur dépend "
         "uniquement de l’offre et de la demande, et qu’on achète surtout "
         "dans l’espoir de le revendre plus cher. Son prix ne reflète donc "
         "aucune information sur une réalité productive.",
    'r': "Le raisonnement isole un actif dépourvu de sous-jacent pour montrer "
         "que le prix peut être entièrement autoréférentiel, ce qui est la "
         "négation de l’efficience informationnelle.",
    'ex': "Le cours souligne la grande volatilité du cours du Bitcoin, dont la "
          "masse est pourtant fixe."}],
  voisins=['n12-allocation-epargne', 'n12-bulles', 'n12-speculation',
           'n12-marches-financiers'])


d('n12-speculation', 12, "Spéculation",
  "Parier sur le prix futur, à la hausse ou à la baisse",
  "Spéculer consiste à prendre une position sur l’évolution future du prix "
  "d’un actif. Le cours distingue deux formes : spéculer à la hausse, en "
  "achetant aujourd’hui pour revendre plus cher demain, et spéculer à la "
  "baisse, en pariant sur la baisse future d’un actif, par vente à découvert, "
  "marchés à terme ou produits dérivés.",
  "Le cours traite la spéculation sans la condamner d’emblée, en l’inscrivant "
  "parmi les raisons de détenir un titre, puis en montrant où elle devient "
  "destructrice. Les raisons de détenir un titre sont au nombre de trois : "
  "obtenir un revenu, coupons pour les obligations ou dividendes pour les "
  "actions ; réaliser une plus-value, en achetant dans l’espoir de revendre "
  "plus cher ; spéculer, à la hausse ou à la baisse. Le cours en tire la "
  "conclusion que le marché ne sert pas seulement à financer, il sert aussi à "
  "arbitrer, à couvrir des risques et à spéculer. Les instruments ensuite. Le "
  "marché à terme permet une transaction conclue aujourd’hui mais exécutée à "
  "une date future, ce qui sert à la couverture contre le risque, à "
  "l’anticipation sur l’évolution des prix et à la spéculation. Le service de "
  "règlement différé permet de différer le règlement d’une opération "
  "boursière, avec pour intérêt l’effet de levier, la spéculation et la prise "
  "de position sans paiement immédiat intégral. Le cours montre alors le point "
  "de bascule avec les produits dérivés de crédit, qui fonctionnent comme une "
  "assurance sur une dette : l’investisseur détient une créance, paie une "
  "prime et est indemnisé si l’emprunteur fait défaut. Le problème est qu’on "
  "peut acheter une telle protection même sans posséder la créance : on peut "
  "donc parier sur la faillite d’un acteur, ce qui crée trois risques, la "
  "spéculation sur la faillite, puisque des acteurs peuvent gagner de l’argent "
  "si une entreprise ou un État va mal, l’effet de contagion, puisque la "
  "défaillance d’un gros débiteur peut provoquer une chaîne de pertes, et le "
  "risque systémique, le vendeur de la protection pouvant lui-même être "
  "incapable d’indemniser. Le cours cite enfin le cas historique de la bulle "
  "du Mississippi et le Bitcoin, hautement spéculatif.",
  [("L’anticipation du prix futur",
    "Le spéculateur achète ou vend non pour le revenu de l’actif mais pour "
    "l’écart de prix qu’il anticipe : sa décision porte sur une variation "
    "future et non sur un rendement contractuel."),
   ("La vente à découvert",
    "Parier sur la baisse suppose de vendre un actif qu’on ne détient pas "
    "encore, pour le racheter moins cher : la position se construit donc sans "
    "avance de capital proportionnelle."),
   ("L’effet de levier",
    "Le règlement différé permet d’engager des montants supérieurs aux fonds "
    "disponibles : le gain comme la perte sont démultipliés par rapport au "
    "capital effectivement immobilisé."),
   ("Le détournement de l’assurance en pari",
    "Un produit dérivé de crédit protège le détenteur d’une créance, mais on "
    "peut l’acheter sans posséder cette créance : l’instrument de couverture "
    "devient alors un pari sur la défaillance d’autrui."),
   ("La chaîne de pertes",
    "Si de nombreux acteurs sont liés par ces contrats, la défaillance d’un "
    "gros débiteur provoque une chaîne de pertes, et le vendeur de la "
    "protection peut lui-même se révéler incapable d’indemniser.")],
  [{'a': "La spéculation apporte de la liquidité aux marchés, puisque les "
         "spéculateurs acceptent de prendre les positions dont d’autres "
         "veulent se défaire.",
    'cond': "L’argument suppose que les spéculateurs soient effectivement en "
            "face de ceux qui cherchent à se couvrir.",
    'lim': "Le cours montre que les mêmes instruments servent à parier sans "
           "aucune exposition à couvrir, ce qui déconnecte la position du "
           "besoin économique qui la justifiait."},
   {'a': "L’anticipation des prix futurs est une fonction utile du marché à "
         "terme, puisqu’elle informe sur les évolutions attendues.",
    'cond': "L’information n’est fiable que si les anticipations reposent sur "
            "des éléments objectifs et non sur l’imitation des autres "
            "intervenants.",
    'lim': "Le cours rappelle que le cours d’un actif sans sous-jacent, comme "
           "le Bitcoin, dépend uniquement de l’offre et de la demande, "
           "l’anticipation n’informant alors que sur elle-même."},
   {'a': "La couverture des risques est une fonction légitime que seuls des "
         "instruments spéculatifs permettent d’organiser.",
    'cond': "Elle exige que l’acheteur de protection détienne effectivement "
            "l’exposition qu’il prétend couvrir.",
    'lim': "Le cours relève qu’on peut acheter une protection sans posséder "
           "la créance, ce qui transforme l’assurance en spéculation sur la "
           "faillite."},
   {'a': "L’effet de levier permet d’engager des positions sans immobiliser "
         "l’intégralité des fonds, ce qui augmente l’efficacité du capital.",
    'cond': "Le mécanisme suppose que l’intervenant puisse honorer ses "
            "engagements en cas d’évolution défavorable.",
    'lim': "Il démultiplie les pertes autant que les gains, et le cours "
           "range le levier parmi les intérêts du règlement différé "
           "précisément à côté de la spéculation."}],
  [{'t': "La spéculation est une fonction normale des marchés, aux côtés de "
         "l’arbitrage et de la couverture des risques.",
    'qui': "Le cours, qui conclut que le marché ne sert pas seulement à "
           "financer mais aussi à arbitrer, couvrir et spéculer.",
    'rep': "Le cours montre où elle devient destructrice : on peut parier sur "
           "la faillite d’un acteur, ce qui crée une spéculation sur la "
           "faillite, un effet de contagion et un risque systémique."},
   {'t': "Les produits dérivés de crédit sont des instruments d’assurance "
         "contre le risque de défaut d’un emprunteur.",
    'qui': "La définition que le cours donne de ces produits dérivés.",
    'rep': "Le cours relève qu’ils ont aussi servi à spéculer sur les "
           "faillites, puisqu’on peut en acheter sans posséder la créance, ce "
           "qui a renforcé le risque systémique."},
   {'t': "La spéculation sur un actif finit toujours par être corrigée par "
         "le retour aux fondamentaux.",
    'qui': "La confiance dans l’autocorrection des marchés spéculatifs.",
    'rep': "Le cours montre avec le système de John Law que la correction "
           "peut prendre la forme d’un effondrement brutal : les actions "
           "passent de cent cinquante à quatre mille cent livres avant la "
           "panique de 1720 et la ruine des épargnants."}],
  [{'n': "John Law",
    'i': "La spéculation sur les actions de la Compagnie du Mississippi "
         "produit la première grande bulle financière.",
    'p': "Le cours chiffre l’épisode : les actions passent de cent cinquante "
         "à quatre mille cent livres, soutenues par l’émission de billets de "
         "la Banque Royale, avant que la demande de conversion en or ne "
         "provoque la panique et l’effondrement de 1720."},
   {'n': "Satoshi Nakamoto",
    'i': "Le Bitcoin repose sur une masse fixe et une valeur déterminée par "
         "la seule offre et la seule demande.",
    'p': "Le cours en tire son caractère hautement spéculatif : sans valeur "
         "sous-jacente, sans garantie et sans revenu, le Bitcoin s’achète "
         "surtout dans l’espoir d’être revendu plus cher, ce qui en fait un "
         "actif à très forte volatilité."},
   {'n': "Henri Bourguinat",
    'i': "La déréglementation et l’innovation financière ont multiplié les "
         "instruments spéculatifs.",
    'p': "Le cours rattache à sa règle des trois D le développement des "
         "marchés de gré à gré et des produits dérivés, qui permettent des "
         "positions sur mesure, rapides et partiellement soustraites aux "
         "contraintes des marchés organisés."}],
  [{'f': "Le cours énumère les moyens de spéculer à la baisse : vente à "
         "découvert, marchés à terme, produits dérivés.",
    'p': "L’existence de ces instruments établit que la spéculation ne "
         "suppose pas de détenir l’actif, ce qui la détache de toute "
         "fonction de financement."},
   {'f': "Le cours relève qu’on peut acheter un produit dérivé de crédit même "
         "sans posséder l’obligation, et donc parier sur la faillite d’un "
         "acteur.",
    'p': "Ce détail technique démontre comment un instrument d’assurance se "
         "transforme en pari, en rompant le lien entre la protection et "
         "l’exposition réelle."},
   {'f': "Les actions de la Compagnie du Mississippi passent de cent "
         "cinquante à quatre mille cent livres avant l’effondrement de 1720.",
    'p': "L’ampleur de la hausse et la brutalité de la chute montrent qu’une "
         "dynamique spéculative peut s’auto-entretenir très loin de toute "
         "valeur économique."}],
  [{'q': "La spéculation est-elle utile ?",
    'f': "Le cours ne la condamne pas : il la range parmi les trois raisons "
         "de détenir un titre et conclut que le marché sert aussi à arbitrer, "
         "à couvrir des risques et à spéculer, la contrepartie spéculative "
         "étant nécessaire à celui qui veut se couvrir. Mais il montre où "
         "elle devient nuisible : lorsqu’on peut parier sur la faillite d’un "
         "acteur sans y être exposé.",
    'r': "Le raisonnement distingue la spéculation comme contrepartie d’une "
         "couverture de la spéculation pure, ce qui permet de juger non "
         "l’activité mais la rupture du lien avec une exposition réelle.",
    'ex': "Le cours relève qu’on peut acheter un produit dérivé de crédit "
          "sans posséder l’obligation correspondante."},
   {'q': "Pourquoi la spéculation peut-elle devenir systémique ?",
    'f': "Le cours identifie trois enchaînements. La spéculation sur la "
         "faillite donne à certains acteurs intérêt à ce qu’une entreprise ou "
         "un État aille mal. L’effet de contagion fait que la défaillance d’un "
         "gros débiteur provoque une chaîne de pertes entre tous ceux qui "
         "sont liés par ces contrats. Le risque systémique vient de ce que le "
         "vendeur de la protection peut lui-même ne pas pouvoir indemniser.",
    'r': "Le raisonnement suit la propagation du défaut de contrat en "
         "contrat, ce qui montre comment un pari bilatéral devient un risque "
         "collectif.",
    'ex': "Le cours relève que c’est exactement ce qui a rendu certains "
          "acteurs ultra fragiles en 2008."},
   {'q': "Une bulle spéculative est-elle prévisible ?",
    'f': "Son éclatement l’est difficilement, mais son mécanisme est "
         "identifiable. Le cours décrit celui de John Law : la banque émet "
         "des billets, l’État rembourse ses dettes, les individus achètent des "
         "actions, l’argent revient à la banque, de nouveaux billets sont "
         "fabriqués. Le circuit alimente lui-même la hausse, de cent "
         "cinquante à quatre mille cent livres, jusqu’à la demande de "
         "conversion.",
    'r': "On met au jour le caractère circulaire du financement de la hausse, "
         "ce qui permet d’identifier le mécanisme sans prétendre dater le "
         "retournement.",
    'ex': "En 1720, la Banque n’a plus de réserves lorsque les détenteurs "
          "veulent échanger leurs billets contre de l’or."}],
  voisins=['n12-bulles', 'n12-actions-obligations', 'n12-efficience',
           'n13-instabilite-financiere'])


d('n12-bulles', 12, "Bulles financières",
  "Quand le prix monte parce qu’il monte",
  "Une bulle financière est une hausse du prix d’un actif qui s’éloigne "
  "durablement de sa valeur économique, alimentée par l’anticipation de "
  "nouvelles hausses, et qui s’achève par un effondrement. Le cours en donne "
  "le cas fondateur avec la bulle du Mississippi, dont les actions passent de "
  "cent cinquante à quatre mille cent livres avant l’éclatement de 1720.",
  "Le cours analyse les bulles par un cas historique détaillé, puis par leurs "
  "formes contemporaines. Le cas fondateur est le système de John Law. En "
  "1716, la France est ruinée après les guerres de Louis quatorze et manque de "
  "monnaie métallique ; Law crée la Banque Générale, émettant des billets "
  "convertibles en or, puis la Banque Royale en 1718, garantie par l’État. Il "
  "fonde la Compagnie du Mississippi pour exploiter les colonies d’Amérique, "
  "et les gens achètent des actions de la Compagnie avec les billets de la "
  "Banque Royale : le cours parle d’une hausse spectaculaire du cours des "
  "actions, c’est-à-dire d’une bulle spéculative, qui passe de cent cinquante "
  "à quatre mille cent livres. Le mécanisme est circulaire : la banque émet "
  "des billets, l’État rembourse ses dettes, les individus achètent des "
  "actions, l’argent revient à la Banque, de nouveaux billets sont fabriqués, "
  "ce qui constitue une création monétaire sans limite. En 1720 le système "
  "éclate : les gens veulent échanger leurs billets contre de l’or, la Banque "
  "n’a plus de réserves, c’est la panique et l’effondrement, avec une crise "
  "financière, la ruine des épargnants et une hostilité durable des Français "
  "envers les banques et la monnaie papier. Le cours en fait la première "
  "grande bulle financière. Les formes contemporaines ensuite. La titrisation "
  "peut diluer la responsabilité, rendre les risques moins lisibles et "
  "favoriser des bulles, comme en 2007 et 2008. Le Bitcoin, dont la valeur "
  "dépend uniquement de l’offre et de la demande et qui ne repose sur aucune "
  "valeur réelle, est qualifié d’actif hautement spéculatif. Le cours relève "
  "enfin que la banque centrale doit éviter les emballements spéculatifs, "
  "qu’il range parmi les cinq risques menaçant la stabilité financière.",
  [("Le financement de la hausse par le crédit",
    "Les acheteurs paient avec une monnaie nouvellement créée : la hausse du "
    "prix est financée par l’expansion du crédit, ce qui lui permet de se "
    "poursuivre bien au-delà de l’épargne disponible."),
   ("Le caractère circulaire du mécanisme",
    "L’émission de monnaie finance l’achat d’actions, dont le produit revient "
    "à l’émetteur, qui émet de nouveau : le circuit s’auto-alimente, ce que "
    "le cours décrit comme une création monétaire sans limite."),
   ("L’anticipation auto-réalisatrice",
    "On achète parce que le prix monte, et le prix monte parce qu’on achète : "
    "la hausse se justifie elle-même tant que de nouveaux acheteurs entrent, "
    "sans référence à un revenu attendu."),
   ("Le déclenchement par la demande de conversion",
    "L’éclatement survient lorsque les détenteurs veulent récupérer un actif "
    "sûr : la demande simultanée de conversion révèle que les engagements "
    "excèdent les réserves, et la hausse se retourne en panique."),
   ("Le coût durable de l’éclatement",
    "Au-delà de la crise financière et de la ruine des épargnants, "
    "l’éclatement laisse une défiance durable : le cours relève une hostilité "
    "prolongée des Français envers les banques et la monnaie papier.")],
  [{'a': "L’étude des bulles historiques fournit un modèle du mécanisme "
         "spéculatif, reconnaissable dans des contextes très différents.",
    'cond': "La transposition suppose que l’on retrouve les éléments "
            "constitutifs, financement par le crédit et anticipation de "
            "hausse.",
    'lim': "Les formes changent : les monnaies contemporaines n’étant plus "
           "convertibles en or, le déclencheur de 1720 ne peut pas se "
           "reproduire à l’identique."},
   {'a': "Le rôle du crédit explique l’ampleur des bulles mieux que ne le "
         "ferait la seule irrationalité des acheteurs.",
    'cond': "L’argument suppose que l’expansion du crédit accompagne "
            "effectivement la hausse des prix d’actifs.",
    'lim': "Il n’explique pas pourquoi la hausse se concentre sur un actif "
           "particulier, ce qui renvoie aux récits et aux anticipations des "
           "intervenants."},
   {'a': "La titrisation a pu favoriser des bulles, en rendant les risques "
         "moins lisibles et en diluant la responsabilité.",
    'cond': "Le mécanisme suppose que les acquéreurs se fient au produit sans "
            "examiner la qualité des créances sous-jacentes.",
    'lim': "La titrisation accroît aussi la liquidité et la capacité de "
           "financement : le cours lui reconnaît explicitement cet avantage "
           "avant d’en relever le risque."},
   {'a': "Faire des emballements spéculatifs un objet de la politique de "
         "stabilité financière donne une responsabilité claire à la banque "
         "centrale.",
    'cond': "Elle suppose que la banque centrale puisse identifier une bulle "
            "avant son éclatement, ce qui est précisément difficile.",
    'lim': "Le cours relève que son intervention crée un risque d’aléa moral, "
           "en encourageant les comportements imprudents de ceux qui "
           "anticipent d’être secourus."}],
  [{'t': "Le système de John Law était un moyen légitime de relancer "
         "l’économie par les billets et le crédit.",
    'qui': "John Law, auquel Schumpeter rend hommage comme monétariste et "
           "pré-keynésien.",
    'rep': "Le cours montre l’issue : le mécanisme circulaire aboutit à une "
           "création monétaire sans limite, puis à l’effondrement de 1720, à "
           "la ruine des épargnants et à une hostilité durable envers la "
           "monnaie papier."},
   {'t': "La titrisation améliore le financement de l’économie en accroissant "
         "la liquidité et la capacité de financement.",
    'qui': "La logique de la titrisation que le cours expose.",
    'rep': "Le cours relève qu’elle peut diluer la responsabilité, rendre les "
           "risques moins lisibles et favoriser des bulles, comme en 2007 et "
           "2008."},
   {'t': "Le Bitcoin est un actif d’investissement comme un autre, dont la "
         "hausse traduit l’adoption croissante d’une technologie nouvelle.",
    'qui': "L’argument des promoteurs des crypto-actifs.",
    'rep': "Le cours objecte qu’il ne repose sur aucune valeur réelle, ni "
           "État, ni garantie, ni revenu, et que sa valeur dépend uniquement "
           "de l’offre et de la demande, ce qui la rend hautement "
           "spéculative."}],
  [{'n': "John Law",
    'i': "Son système associe émission de billets et spéculation sur les "
         "actions de la Compagnie du Mississippi.",
    'p': "Le cours décrit le circuit complet : la banque émet des billets, "
         "l’État rembourse ses dettes, les individus achètent des actions, "
         "l’argent revient à la Banque, de nouveaux billets sont fabriqués, "
         "d’où une création monétaire sans limite jusqu’à l’effondrement de "
         "1720."},
   {'n': "Joseph Schumpeter",
    'i': "Il rend hommage à John Law en le qualifiant de monétariste et de "
         "pré-keynésien.",
    'p': "Le cours mentionne ce jugement pour montrer que l’épisode n’est pas "
         "seulement une erreur : Law a saisi avant d’autres le rôle actif de "
         "la monnaie et du crédit, mais son dispositif en a révélé le danger "
         "en l’absence de limite."},
   {'n': "Satoshi Nakamoto",
    'i': "Le Bitcoin repose sur une masse limitée à vingt-et-un millions "
         "d’unités et sur une valeur fixée par l’offre et la demande.",
    'p': "Le cours en tire sa grande volatilité : sans valeur sous-jacente ni "
         "revenu, son prix ne dépend que des anticipations des acheteurs, ce "
         "qui en fait un actif hautement spéculatif."},
   {'n': "Christine Lagarde",
    'i': "Les économies contemporaines traversent une succession constante de "
         "crises inédites majeures.",
    'p': "Le cours ouvre sur ce diagnostic de permacrises, qui explique "
         "pourquoi la prévention des emballements spéculatifs figure "
         "désormais parmi les missions explicites de la banque centrale au "
         "titre de la stabilité financière."}],
  [{'f': "Les actions de la Compagnie du Mississippi passent de cent "
         "cinquante à quatre mille cent livres avant l’éclatement de 1720.",
    'p': "Le chiffre donne l’ordre de grandeur d’une bulle : une "
         "multiplication par plus de vingt-cinq sans transformation "
         "équivalente de la valeur productive sous-jacente."},
   {'f': "En 1720, les détenteurs veulent échanger leurs billets contre de "
         "l’or, la Banque n’a plus de réserves, et c’est la panique et "
         "l’effondrement.",
    'p': "Le déclencheur montre que l’éclatement vient d’une demande de "
         "conversion vers un actif sûr, et non d’une révision du jugement sur "
         "la Compagnie."},
   {'f': "Le cours relève que la titrisation peut diluer la responsabilité, "
         "rendre les risques moins lisibles et favoriser des bulles, comme en "
         "2007 et 2008.",
    'p': "Le rapprochement entre 1720 et 2008 montre la permanence du "
         "mécanisme sous des formes techniques entièrement différentes."}],
  [{'q': "Comment se forme une bulle financière ?",
    'f': "Le cours en donne le mécanisme avec John Law : la banque émet des "
         "billets, l’État rembourse ses dettes, les individus achètent des "
         "actions, l’argent revient à la Banque, de nouveaux billets sont "
         "fabriqués. Le crédit finance la hausse et la hausse justifie de "
         "nouveaux achats, ce qui permet au cours des actions de passer de "
         "cent cinquante à quatre mille cent livres.",
    'r': "Le raisonnement met au jour la circularité du financement, ce qui "
         "explique pourquoi la hausse peut se poursuivre bien au-delà de "
         "toute valeur économique.",
    'ex': "Le cours qualifie cet épisode de première grande bulle "
          "financière."},
   {'q': "Pourquoi une bulle éclate-t-elle ?",
    'f': "Parce que les détenteurs finissent par vouloir un actif sûr. En "
         "1720, les gens veulent échanger leurs billets contre de l’or, la "
         "Banque n’a plus de réserves, et la panique provoque "
         "l’effondrement. L’éclatement ne vient donc pas d’une révision du "
         "jugement sur la Compagnie, mais de la découverte que les "
         "engagements excèdent les réserves.",
    'r': "On identifie le déclencheur dans la demande simultanée de "
         "conversion, ce qui relie l’éclatement d’une bulle au mécanisme de "
         "la panique bancaire.",
    'ex': "La crise de 1720 entraîne la ruine des épargnants et une "
          "hostilité durable envers la monnaie papier."},
   {'q': "Les bulles sont-elles un phénomène du passé ?",
    'f': "Non, et le cours le montre par deux cas contemporains. La "
         "titrisation peut diluer la responsabilité, rendre les risques moins "
         "lisibles et favoriser des bulles, comme en 2007 et 2008. Le "
         "Bitcoin, sans valeur sous-jacente ni revenu, voit son cours "
         "déterminé par la seule offre et la seule demande, ce qui le rend "
         "hautement spéculatif.",
    'r': "Le raisonnement identifie le mécanisme commun, une valorisation "
         "sans ancrage dans un revenu attendu, sous des formes techniques "
         "entièrement renouvelées.",
    'ex': "Le cours range les emballements spéculatifs parmi les risques que "
          "la banque centrale doit éviter."}],
  voisins=['n12-speculation', 'n12-efficience',
           'n13-instabilite-financiere', 'n11-confiance'])
