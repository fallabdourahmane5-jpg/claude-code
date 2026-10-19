# -*- coding: utf-8 -*-
"""Ensemble 6 — Les défaillances du marché et les limites de l’intervention
publique (2/4)."""

from doss_base import d

d('n6-selection-adverse', 6, "Sélection adverse",
  "Avant le contrat : les mauvais produits chassent les bons",
  "La sélection adverse, aussi appelée antisélection, apparaît lorsque, à "
  "cause d’une asymétrie d’information avant l’échange, les produits de "
  "mauvaise qualité restent sur le marché tandis que les bons produits en "
  "sortent. Elle se produit avant la signature du contrat et porte sur des "
  "caractéristiques cachées que la partie mal informée ne peut pas observer.",
  "La sélection adverse est le premier des deux effets de l’asymétrie "
  "d’information, et sa place dans le temps — avant le contrat — est ce qui la "
  "distingue de l’aléa moral. Le mécanisme est celui qu’Akerlof expose en "
  "1970 sur le marché des voitures d’occasion, et le cours le décompose en "
  "six temps qu’il faut savoir restituer. Le vendeur sait si la voiture est "
  "bonne ou mauvaise ; l’acheteur ne le sait pas ; l’acheteur devient méfiant "
  "et baisse son consentement à payer ; le prix moyen baisse ; les vendeurs de "
  "bonnes voitures renoncent à vendre ; il ne reste que des mauvaises "
  "voitures. Le résultat se résume en une formule que le cours donne telle "
  "quelle : les mauvaises voitures chassent les bonnes. Le cours y voit une "
  "application de la loi de Gresham, selon laquelle la mauvaise monnaie chasse "
  "la bonne monnaie. La conséquence est grave : le marché se dégrade et peut "
  "même disparaître, alors qu’il existait des échanges mutuellement "
  "avantageux à réaliser entre vendeurs de bonnes voitures et acheteurs "
  "prêts à les payer. Le cours donne un second exemple, essentiel parce qu’il "
  "sort du marché des biens : le crédit bancaire. La banque ne sait pas si "
  "l’emprunteur est prudent ou risqué ; elle augmente les taux d’intérêt pour "
  "se protéger ; les emprunteurs prudents renoncent ; les emprunteurs risqués "
  "acceptent. La banque attire donc surtout les mauvais profils, et la hausse "
  "du taux destinée à la protéger dégrade la qualité de son portefeuille. "
  "C’est le point le plus contre-intuitif du dossier et le plus utile en "
  "dissertation : la réaction défensive de la partie mal informée aggrave le "
  "problème qu’elle entendait résoudre. Les remèdes consistent à révéler "
  "l’information cachée — garanties, étiquetage, obligation d’information, "
  "certification — ou à rationner la quantité plutôt qu’à ajuster le prix.",
  [("L’existence d’une caractéristique cachée",
    "La qualité du bien ou le profil de risque de l’agent sont connus d’une "
    "partie seulement : l’information est détenue avant tout échange, ce qui "
    "distingue la sélection adverse de l’aléa moral."),
   ("La réaction défensive par le prix moyen",
    "Ne pouvant distinguer les qualités, la partie mal informée applique un "
    "traitement uniforme : elle baisse son consentement à payer, ou relève le "
    "taux qu’elle exige, pour se protéger du risque moyen."),
   ("L’éviction de la qualité haute",
    "Ce traitement moyen est trop défavorable pour les meilleurs : les "
    "vendeurs de bonnes voitures renoncent à vendre, les emprunteurs prudents "
    "renoncent à emprunter, et ils quittent le marché."),
   ("La dégradation cumulative",
    "Le départ des meilleurs abaisse la qualité moyenne restante, ce qui "
    "justifie un traitement encore plus défavorable : le mécanisme se nourrit "
    "de lui-même jusqu’à l’effondrement possible du marché."),
   ("L’aggravation par la protection",
    "La mesure destinée à protéger la partie mal informée produit l’effet "
    "inverse : en relevant son taux, la banque attire surtout les mauvais "
    "profils, ce qui détériore son portefeuille.")],
  [{'a': "Le mécanisme explique la disparition de marchés pourtant "
         "socialement utiles, sans supposer ni fraude ni irrationalité.",
    'cond': "Il suppose que la qualité soit invérifiable avant l’échange et "
            "que les détenteurs de qualité haute disposent d’une alternative "
            "à la vente.",
    'lim': "Si la qualité peut être certifiée à faible coût, le mécanisme "
           "disparaît : la défaillance dépend donc du coût de révélation de "
           "l’information."},
   {'a': "Il s’applique bien au-delà du marché des biens, notamment au crédit "
         "bancaire et à l’assurance.",
    'cond': "La transposition suppose que le prix ou le taux soit l’unique "
            "instrument d’ajustement dont dispose la partie mal informée.",
    'lim': "Dès que le rationnement quantitatif est possible, le prêteur peut "
           "limiter le volume plutôt que relever le taux, ce qui atténue "
           "l’antisélection."},
   {'a': "Il montre qu’une réaction défensive rationnelle peut aggraver le "
         "problème, ce qui est un résultat théorique fort.",
    'cond': "Le paradoxe suppose que la hausse du prix exigé modifie la "
            "composition de la demande et non seulement son volume.",
    'lim': "Il faut donc que les profils soient hétérogènes dans leur "
           "sensibilité au prix, ce qui n’est pas vrai sur tous les marchés."},
   {'a': "Il justifie des remèdes réglementaires ciblés et peu coûteux, qui "
         "portent sur l’information et non sur le prix.",
    'cond': "Les remèdes supposent que l’information révélée soit vérifiable "
            "et que la fausse déclaration soit sanctionnable.",
    'lim': "Ils relèvent de l’action par les règles, dont le cours rappelle "
           "les défauts : effet de seuil, rigidité, risque de contournement."}],
  [{'t': "La sélection adverse se résout par le marché lui-même, grâce à la "
         "réputation et aux garanties commerciales.",
    'qui': "La lecture par les dispositifs privés de révélation de "
           "l’information.",
    'rep': "Ces dispositifs limitent le mécanisme, mais le cours montre que la "
           "protection du consommateur relève aussi de la règle : garanties "
           "légales, étiquetage et obligation d’information."},
   {'t': "Le problème n’est pas l’information mais le prix : il suffirait de "
         "laisser les prix se différencier par qualité.",
    'qui': "Une lecture strictement concurrentielle du marché.",
    'rep': "L’objection manque le cœur du mécanisme : c’est précisément parce "
           "que l’acheteur ne peut pas observer la qualité qu’il ne peut pas "
           "payer un prix différencié, d’où le prix moyen."},
   {'t': "L’antisélection affecte aussi le marché du travail, et pas seulement "
         "les biens et le crédit.",
    'qui': "La nouvelle économie keynésienne, qui insiste sur l’asymétrie "
           "d’information et sur les salaires d’efficience.",
    'rep': "L’extension est cohérente avec le cours, qui note que "
           "l’information est imparfaite, que certains agents savent plus que "
           "d’autres et que le marché du travail est particulièrement "
           "concerné."},
   {'t': "Le mécanisme est une application d’une loi monétaire ancienne, et "
         "non une découverte des années 1970.",
    'qui': "Le rapprochement que le cours opère avec la loi de Gresham.",
    'rep': "Le rapprochement est éclairant mais l’apport d’Akerlof demeure : "
           "il fournit le mécanisme général, applicable à tout marché où la "
           "qualité est cachée, et non seulement à la circulation monétaire."}],
  [{'n': "George Akerlof",
    'i': "À cause de l’asymétrie avant l’échange, les produits de mauvaise "
         "qualité restent sur le marché tandis que les bons en sortent.",
    'p': "Son article The Market for Lemons (1970) décompose le mécanisme : le "
         "vendeur connaît la qualité, l’acheteur non, celui-ci baisse son "
         "consentement à payer, le prix moyen baisse, les vendeurs de bonnes "
         "voitures renoncent, et il ne reste que des mauvaises voitures."},
   {'n': "George Akerlof",
    'i': "L’asymétrie d’information est la situation normale des marchés, non "
         "une exception.",
    'p': "C’est un second apport, de portée méthodologique : il déplace la "
         "transparence de l’information du statut d’hypothèse simplificatrice "
         "à celui d’hypothèse fausse, ce qui engage toute la théorie de "
         "l’équilibre concurrentiel."},
   {'n': "Joseph Stiglitz",
    'i': "L’information imparfaite empêche les marchés de s’ajuster "
         "correctement.",
    'p': "Le cours le compte parmi les auteurs de la nouvelle économie "
         "keynésienne, pour laquelle les marchés réels sont imparfaits et "
         "l’asymétrie d’information explique, avec les rigidités de prix et la "
         "concurrence imparfaite, la persistance d’un chômage involontaire."}],
  [{'f': "Le cours résume la sélection adverse par une formule : les mauvaises "
         "voitures chassent les bonnes.",
    'p': "La formule est directement citable et condense le mécanisme en "
         "montrant que l’éviction porte sur la qualité et non sur les "
         "quantités."},
   {'f': "Le cours y voit une application de la loi de Gresham, selon laquelle "
         "la mauvaise monnaie chasse la bonne monnaie.",
    'p': "Le rapprochement montre la généralité du mécanisme et permet de le "
         "relier au chapitre sur la monnaie."},
   {'f': "Dans le cas du crédit bancaire, la banque augmente les taux pour se "
         "protéger, les emprunteurs prudents renoncent et les emprunteurs "
         "risqués acceptent.",
    'p': "L’exemple est le plus fort du dossier car il montre que la mesure de "
         "protection dégrade la qualité du portefeuille au lieu de "
         "l’améliorer."},
   {'f': "Le cours situe la sélection adverse avant la signature du contrat et "
         "l’aléa moral après.",
    'p': "Le repère temporel est le critère de classement le plus sûr et évite "
         "la confusion la plus fréquente entre les deux notions."}],
  [{'q': "Sujet du type « L’information imparfaite empêche-t-elle le marché de "
         "fonctionner ? »",
    'f': "La sélection adverse montre qu’elle peut le détruire. Sur le marché "
         "des voitures d’occasion, le vendeur sait si la voiture est bonne, "
         "l’acheteur ne le sait pas : celui-ci devient méfiant et baisse son "
         "consentement à payer, le prix moyen baisse, les vendeurs de bonnes "
         "voitures renoncent à vendre et il ne reste que des mauvaises "
         "voitures. Les mauvaises voitures chassent les bonnes, le marché se "
         "dégrade et peut même disparaître.",
    'r': "Le raisonnement montre que la défaillance est cumulative et non "
         "ponctuelle : chaque tour du mécanisme aggrave la situation, ce qui "
         "explique qu’il puisse aboutir à la disparition du marché.",
    'ex': "La loi de Gresham, selon laquelle la mauvaise monnaie chasse la "
          "bonne monnaie."},
   {'q': "Sujet du type « Le prix suffit-il à équilibrer un marché ? »",
    'f': "Le cas du crédit bancaire montre que non, et même que l’ajustement "
         "par le prix peut être contre-productif. La banque ne sait pas si "
         "l’emprunteur est prudent ou risqué ; elle augmente donc les taux "
         "d’intérêt pour se protéger ; mais les emprunteurs prudents "
         "renoncent tandis que les emprunteurs risqués acceptent, de sorte "
         "qu’elle attire surtout les mauvais profils.",
    'r': "Le raisonnement établit que le prix ne sélectionne pas seulement un "
         "volume mais aussi une composition : relever le prix peut dégrader la "
         "qualité de ce que l’on achète, ce qui invalide l’ajustement "
         "classique.",
    'ex': "Le rationnement du crédit, où la banque limite le volume prêté "
          "plutôt que de relever indéfiniment son taux."}],
  voisins=['n6-asymetries', 'n6-alea-moral', 'n6-reglementation',
           'n5-cpp'])


d('n6-alea-moral', 6, "Aléa moral",
  "Après le contrat : être protégé change le comportement",
  "L’aléa moral, ou risque moral, apparaît lorsqu’un agent, une fois protégé, "
  "adopte un comportement plus risqué qu’avant. Il se produit après la "
  "signature du contrat et porte sur un comportement non observable par la "
  "partie qui supporte le risque. Le cours en tire une ambiguïté "
  "fondamentale : les dispositifs de protection sont nécessaires pour "
  "stabiliser l’économie, mais ils créent aussi de l’aléa moral.",
  "L’aléa moral est le second effet de l’asymétrie d’information, et sa "
  "position temporelle — après la signature — commande toute son analyse. "
  "Puisque le contrat est conclu, le problème ne porte plus sur une "
  "caractéristique cachée mais sur un comportement : l’agent protégé sait que "
  "les conséquences de ses actes seront supportées par un autre, et modifie "
  "donc son comportement. Le cours donne trois exemples qu’il faut maîtriser "
  "car ils couvrent trois domaines différents. Premier exemple, la banque "
  "centrale prêteur en dernier ressort : elle protège le système bancaire, "
  "mais les banques savent qu’elles seront sauvées et prennent plus de "
  "risques — c’est la logique du too big to fail. Deuxième exemple, "
  "l’assurance : elle protège contre les accidents mais peut encourager "
  "l’imprudence, par une conduite plus risquée et une moindre vigilance, "
  "l’assuré se disant que ce n’est pas grave puisque l’assurance paiera. "
  "Troisième exemple, l’annulation des dettes : si les agents savent que leurs "
  "dettes peuvent être annulées, ils prennent plus de risques "
  "d’endettement — le cours parle d’aléa moral public à propos de la "
  "monétisation de la dette, puisque si l’État sait que la banque centrale "
  "peut financer les dépenses, il n’a plus d’incitation à maîtriser le déficit "
  "et la dette. L’ambiguïté fondamentale est le point le plus important : la "
  "solution est en même temps une partie du problème, car les dispositifs de "
  "protection sont nécessaires pour stabiliser l’économie tout en créant de "
  "l’aléa moral. Enfin, le cours insiste sur la nature de cette défaillance : "
  "même avec des agents rationnels, même sans monopole ni externalité, le "
  "marché n’alloue pas efficacement les ressources, et le problème vient "
  "uniquement de l’information imparfaite.",
  [("La protection accordée par le contrat",
    "L’agent cesse de supporter tout ou partie des conséquences de ses actes : "
    "le coût de son imprudence est transféré à l’assureur, au prêteur en "
    "dernier ressort ou au créancier."),
   ("La non-observabilité du comportement",
    "La partie qui supporte le risque ne peut pas vérifier la prudence "
    "effective de l’agent : faute de pouvoir conditionner la protection au "
    "comportement, elle ne peut pas corriger l’incitation."),
   ("La modification de l’incitation",
    "Puisque l’imprudence n’est plus coûteuse, l’agent arbitre différemment : "
    "il prend des risques qu’il aurait évités s’il en avait supporté les "
    "conséquences."),
   ("L’anticipation du sauvetage",
    "Lorsque la protection est attendue plutôt que contractuelle, l’effet est "
    "identique : les banques prennent plus de risques parce qu’elles savent "
    "qu’elles seront sauvées, selon la logique du too big to fail."),
   ("L’ambiguïté du dispositif de protection",
    "Le mécanisme de stabilisation produit lui-même l’instabilité qu’il doit "
    "prévenir : la solution est en même temps une partie du problème, ce qui "
    "interdit de la supprimer comme de la laisser sans contrepartie.")],
  [{'a': "La notion explique pourquoi un dispositif de protection peut "
         "augmenter le risque global au lieu de le réduire.",
    'cond': "L’effet suppose que la protection soit perçue comme acquise et "
            "que le comportement prudent soit coûteux pour l’agent.",
    'lim': "Si la protection est partielle — franchise, participation aux "
           "pertes — l’agent continue de supporter une part du coût et "
           "l’incitation est préservée."},
   {'a': "Elle fournit un argument pour conditionner et calibrer la "
         "protection plutôt que pour la supprimer purement et simplement.",
    'cond': "La conditionnalité suppose que l’on puisse observer, même "
            "imparfaitement, le comportement de l’agent protégé.",
    'lim': "Or c’est précisément l’inobservabilité qui définit le problème : "
           "le remède suppose de lever la difficulté qui le rend nécessaire."},
   {'a': "Elle s’applique aussi bien aux relations privées qu’aux finances "
         "publiques, ce qui en fait un outil d’analyse très général.",
    'cond': "La transposition au secteur public suppose que l’État anticipe "
            "effectivement le soutien de la banque centrale.",
    'lim': "C’est précisément pour éviter cette dérive que, dans les "
           "économies modernes et notamment dans l’Union européenne, la banque "
           "centrale n’a pas le droit de financer directement l’État."},
   {'a': "Elle établit qu’une défaillance peut être purement "
         "informationnelle, indépendamment de la structure du marché.",
    'cond': "L’argument suppose des agents rationnels, ce qui renforce la "
            "démonstration plutôt qu’il ne l’affaiblit.",
    'lim': "Il reste à mesurer l’ampleur du phénomène, qui dépend du degré "
           "réel de protection et de la culture du risque dans le secteur "
           "concerné."}],
  [{'t': "Les dispositifs de protection doivent être réduits, puisqu’ils "
         "engendrent eux-mêmes la prise de risque.",
    'qui': "La lecture par l’aléa moral poussée jusqu’à sa conclusion "
           "logique.",
    'rep': "Le cours écarte cette conclusion : les dispositifs de protection "
           "sont nécessaires pour stabiliser l’économie, et la question est "
           "donc leur calibrage et non leur suppression."},
   {'t': "L’aléa moral public justifie à lui seul l’interdiction faite à la "
         "banque centrale de financer directement l’État.",
    'qui': "La règle que le cours rappelle pour les économies modernes et "
           "l’Union européenne.",
    'rep': "La justification est explicite et triple : perte d’indépendance de "
           "la banque centrale, risque de dérive permanente du déficit, et "
           "risque inflationniste à long terme."},
   {'t': "Le prêteur en dernier ressort reste indispensable malgré l’aléa "
         "moral que sa seule existence engendre.",
    'qui': "L’analyse de la stabilité financière que le cours développe depuis "
           "la crise de 2008.",
    'rep': "L’argument est solide : la banque centrale doit éviter les crises "
           "bancaires, les paniques de liquidité, le blocage du crédit et les "
           "faillites systémiques, ce qui suppose d’accepter un aléa moral "
           "résiduel."},
   {'t': "L’aléa moral concerne aussi le marché du travail, où il se "
         "manifeste par les salaires d’efficience.",
    'qui': "La nouvelle économie keynésienne, que le cours mobilise.",
    'rep': "L’extension est cohérente : elle montre que l’employeur ne peut "
           "pas observer parfaitement l’effort du salarié, ce qui le conduit à "
           "payer au-dessus du salaire de marché pour obtenir un comportement "
           "qu’il ne peut pas contrôler."}],
  [{'n': "George Akerlof",
    'i': "L’asymétrie d’information produit deux effets distincts selon le "
         "moment où elle joue.",
    'p': "Le cours construit à partir de son analyse la distinction qui fonde "
         "ce dossier : avant la signature du contrat, sélection adverse ; "
         "après la signature, aléa moral. L’aléa moral porte donc sur un "
         "comportement et non sur une caractéristique."},
   {'n': "Éric Monnet",
    'i': "La banque centrale contemporaine tend à devenir un acteur plus large "
         "de la gouvernance économique.",
    'p': "Dans La Banque Providence (2021), que le cours mobilise, il propose "
         "d’élargir ses missions au-delà de la stabilité des prix, de la "
         "croissance et de la stabilité financière. L’extension des fonctions "
         "élargit du même coup le périmètre de l’aléa moral public."},
   {'n': "Joseph Stiglitz",
    'i': "Les marchés réels sont imparfaits, notamment parce que l’information "
         "est asymétrique.",
    'p': "Le cours le rattache à la nouvelle économie keynésienne, qui cite "
         "explicitement l’aléa moral et les salaires d’efficience comme "
         "exemples d’imperfections informationnelles sur le marché du travail, "
         "expliquant un chômage involontaire et durable."}],
  [{'f': "Le cours définit l’aléa moral comme la situation où un agent, une "
         "fois protégé, adopte un comportement plus risqué qu’avant, après la "
         "signature du contrat.",
    'p': "La définition associe l’effet et le moment, ce qui permet de "
         "distinguer immédiatement l’aléa moral de la sélection adverse."},
   {'f': "La banque centrale prêteur en dernier ressort protège le système "
         "bancaire, mais les banques savent qu’elles seront sauvées et "
         "prennent plus de risques : c’est la logique du too big to fail.",
    'p': "L’exemple est le plus important parce qu’il porte sur un dispositif "
         "jugé indispensable, ce qui rend l’arbitrage inévitable."},
   {'f': "L’assurance protège contre les accidents mais peut encourager "
         "l’imprudence : conduite plus risquée, moindre vigilance, "
         "raisonnement selon lequel l’assurance paiera.",
    'p': "L’exemple montre que l’aléa moral ne suppose aucune malveillance : "
         "il résulte d’un simple déplacement du coût du risque."},
   {'f': "Si l’État sait que la banque centrale peut financer les dépenses, il "
         "n’a plus d’incitation à maîtriser le déficit et la dette : le cours "
         "parle d’aléa moral public.",
    'p': "Le fait justifie l’interdiction du financement monétaire direct dans "
         "les économies modernes, ce qui relie la notion à l’architecture "
         "institutionnelle de la zone euro."}],
  [{'q': "Sujet du type « Faut-il protéger les agents contre le risque ? »",
    'f': "La protection est nécessaire mais jamais neutre, et le cours "
         "formule l’arbitrage avec netteté : les dispositifs de protection "
         "sont nécessaires pour stabiliser l’économie, mais ils créent aussi "
         "de l’aléa moral, de sorte que la solution est en même temps une "
         "partie du problème. La banque centrale prêteur en dernier ressort en "
         "est l’illustration : elle protège le système bancaire, mais les "
         "banques savent qu’elles seront sauvées et prennent plus de risques.",
    'r': "Le raisonnement montre que l’arbitrage ne porte pas sur l’existence "
         "de la protection mais sur son calibrage, ce qui déplace la "
         "discussion vers les contreparties exigées des agents protégés.",
    'ex': "La logique du too big to fail, qui transforme une garantie "
          "implicite en incitation à la prise de risque."},
   {'q': "Sujet du type « La banque centrale doit-elle pouvoir financer "
         "l’État ? »",
    'f': "Le cours répond par trois objections, dont l’une est un aléa moral "
         "public. La monétisation de la dette ferait perdre à la banque "
         "centrale son indépendance et sa crédibilité dans la lutte contre "
         "l’inflation ; elle créerait un risque de dérive permanente, puisque "
         "si l’État sait que la banque centrale peut financer les dépenses, il "
         "n’a plus d’incitation à maîtriser le déficit et la dette ; elle "
         "engendrerait enfin un risque inflationniste, les dépenses étant "
         "financées par création monétaire sans contrepartie productive "
         "immédiate.",
    'r': "Le raisonnement montre que l’interdiction institutionnelle est une "
         "réponse à un problème d’incitation et non un dogme, ce qui permet "
         "d’en discuter les exceptions.",
    'ex': "L’interdiction faite à la banque centrale, dans l’Union européenne, "
          "de financer directement l’État."}],
  voisins=['n6-asymetries', 'n6-selection-adverse', 'n6-defaillances-etat',
           'n6-reglementation'])


d('n6-marches-incomplets', 6, "Marchés incomplets",
  "Tous les échanges imaginables n’ont pas de marché pour les porter",
  "L’hypothèse de marchés complets, que le cours range parmi les sept "
  "conditions d’Arrow-Debreu, suppose qu’il existe un marché pour chaque bien "
  "présent, pour chaque bien futur, pour chaque service et pour chaque facteur "
  "de production, de sorte qu’on puisse échanger aujourd’hui ce qui sera livré "
  "demain. Des marchés incomplets signifient que certains échanges "
  "souhaitables n’ont aucun marché pour se réaliser.",
  "L’incomplétude des marchés est une défaillance d’un type particulier, car "
  "elle ne porte pas sur le fonctionnement d’un marché mais sur son absence. "
  "Le cours l’introduit par la théorie de l’équilibre général. Arrow et Debreu "
  "cherchent à établir sous quelles conditions les courbes d’offre et de "
  "demande se croisent nécessairement sur tous les marchés en même temps, "
  "puisque, comme le rappelle le cours, avoir autant d’équations que "
  "d’inconnues ne garantit pas qu’une solution existe : deux droites peuvent "
  "ne jamais se croiser. Ils identifient sept conditions, dont la complétude "
  "des marchés. Celle-ci est très exigeante : il faut un marché pour chaque "
  "bien présent, chaque bien futur, chaque service et chaque facteur de "
  "production. Autrement dit, tout échange concevable, y compris sur une date "
  "future ou un état du monde incertain, doit pouvoir être contracté "
  "aujourd’hui. Si cette condition n’est pas remplie, l’équilibre général "
  "n’est plus garanti et l’optimalité qu’on lui attache disparaît avec lui. Le "
  "cours souligne par ailleurs que les autres conditions sont tout aussi "
  "problématiques, et notamment la dotation de survie : chaque agent doit "
  "posséder un minimum de ressources au départ, faute de quoi aucun échange "
  "n’est possible — or cette dotation suppose une intervention extérieure au "
  "marché, État, Église ou institutions, ce qui contredit l’idée "
  "néoclassique que le marché se suffit à lui-même. L’incomplétude éclaire "
  "ainsi une famille entière de difficultés concrètes : l’absence de marché "
  "pour certains risques, qui renvoie à l’assurance et à l’aléa moral ; "
  "l’absence de prix pour les effets externes, qui renvoie aux externalités ; "
  "l’absence de marché pour les biens non excluables, qui renvoie aux biens "
  "collectifs. Dans tous ces cas, le problème n’est pas qu’un prix soit faux, "
  "mais qu’aucun prix n’existe.",
  [("L’exigence d’un marché pour chaque échange concevable",
    "La complétude suppose un marché pour chaque bien présent, chaque bien "
    "futur, chaque service et chaque facteur : la coordination par les prix ne "
    "peut porter que sur ce qui a un marché."),
   ("L’échange intertemporel",
    "Il faut pouvoir échanger aujourd’hui ce qui sera livré demain : sans "
    "marché à terme, les décisions présentes ne peuvent pas intégrer les prix "
    "futurs, et la coordination perd sa dimension temporelle."),
   ("L’absence de prix comme cause d’inefficacité",
    "Là où aucun marché n’existe, aucun prix ne transmet l’information : le "
    "problème n’est pas un prix faux mais l’absence de signal, ce qui rend "
    "l’arbitrage impossible pour les agents."),
   ("La fragilisation de l’équilibre général",
    "La complétude figure parmi les conditions d’existence de l’équilibre : "
    "son absence suffit à priver le modèle de sa conclusion, puisque rien ne "
    "garantit plus que tous les marchés s’équilibrent simultanément."),
   ("Le recours nécessaire à des institutions extérieures",
    "Quand le marché manque, la coordination doit venir d’ailleurs : la "
    "dotation de survie supposée par Arrow et Debreu désigne précisément une "
    "intervention extérieure au marché.")],
  [{'a': "La notion identifie une défaillance par absence et non par "
         "dysfonctionnement, ce qui élargit utilement l’analyse.",
    'cond': "L’argument suppose que l’échange manquant soit effectivement "
            "souhaité par les deux parties.",
    'lim': "L’absence de marché peut résulter d’un coût de transaction "
           "prohibitif plutôt que d’une impossibilité, auquel cas elle est "
           "efficiente au sens de Coase."},
   {'a': "Elle met en évidence le caractère extrêmement exigeant des "
         "conditions d’existence de l’équilibre général.",
    'cond': "L’argument n’a de force que si l’on admet le cadre d’Arrow et "
            "Debreu, puisque c’est à l’intérieur de ce cadre que la condition "
            "est posée.",
    'lim': "La critique est donc interne : elle ne conteste pas le théorème "
           "mais la vraisemblance de ses hypothèses."},
   {'a': "Elle unifie plusieurs défaillances apparemment distinctes, toutes "
         "liées à l’absence de prix.",
    'cond': "L’unification suppose de distinguer l’absence de marché de la "
            "simple imperfection du prix existant.",
    'lim': "Elle risque de diluer des mécanismes très différents : "
           "externalité, non-excluabilité et absence de marché à terme "
           "n’appellent pas les mêmes remèdes."},
   {'a': "Elle justifie la création institutionnelle de marchés là où ils "
         "manquent, comme les marchés de quotas d’émission.",
    'cond': "La création suppose de pouvoir définir des droits de propriété "
            "clairs, condition du théorème de Coase.",
    'lim': "Cette condition fait défaut pour les biens diffus ou "
           "transfrontaliers, tels que l’air, les océans ou le climat."}],
  [{'t': "L’équilibre général existe, mais sous des hypothèses dont la "
         "complétude des marchés fait partie et qui sont irréalistes.",
    'qui': "Kenneth Arrow et Gérard Debreu, dont le cours détaille les sept "
           "conditions.",
    'rep': "La critique est constructive : elle convertit une intuition en "
           "théorème conditionnel, et l’examen de chaque condition devient "
           "alors un programme de recherche."},
   {'t': "La condition la plus contradictoire du modèle n’est pas la "
         "complétude des marchés mais la dotation de survie.",
    'qui': "Le constat du cours sur les conditions d’Arrow-Debreu.",
    'rep': "L’argument est le plus fort du dossier : cette dotation suppose "
           "une intervention extérieure — État, Église, institutions — ce qui "
           "contredit frontalement l’idée que le marché se suffit à lui-même."},
   {'t': "Même avec des marchés parfaitement complets, rien ne garantirait "
         "la convergence du système vers l’équilibre.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "L’objection s’ajoute à la précédente : une fonction de demande "
           "globale peut avoir n’importe quelle forme, être croissante ou "
           "chaotique, de sorte que l’existence ne suffit pas."},
   {'t': "L’absence de certains marchés peut être efficiente, si les coûts de "
         "les organiser excèdent les gains attendus.",
    'qui': "Ronald Coase, pour qui le recours au marché n’est pas gratuit.",
    'rep': "L’argument nuance la notion d’incomplétude : tout marché manquant "
           "n’est pas une défaillance, puisque sa création a un coût qu’il "
           "faut comparer au bénéfice de l’échange rendu possible."}],
  [{'n': "Kenneth Arrow",
    'i': "L’existence de l’équilibre général suppose des marchés complets, "
         "pour chaque bien présent, futur, service et facteur.",
    'p': "Avec Debreu, il établit que les fonctions doivent être continues et "
         "bornées et énonce sept conditions. La complétude permet d’échanger "
         "aujourd’hui ce qui sera livré demain, hypothèse que l’existence même "
         "de l’incertitude rend très exigeante."},
   {'n': "Gérard Debreu",
    'i': "La formalisation de l’équilibre général rend explicites les "
         "hypothèses que l’analyse économique mobilisait implicitement.",
    'p': "Le cours lui attribue un second résultat, avec Sonnenschein et "
         "Mantel : l’existence de l’équilibre ne garantit ni sa stabilité ni "
         "la convergence du système vers lui, ce qui affaiblit la portée "
         "pratique du premier."},
   {'n': "Ronald Coase",
    'i': "Le recours au marché n’est jamais gratuit : il engendre toute une "
         "série de coûts de transaction.",
    'p': "Il les énumère : recherche d’information, négociation, rédaction des "
         "contrats, contrôle et surveillance. Ces coûts expliquent pourquoi "
         "certains marchés n’existent pas : les organiser coûterait plus que "
         "l’échange ne rapporterait."}],
  [{'f': "La condition de marchés complets exige un marché pour chaque bien "
         "présent, chaque bien futur, chaque service et chaque facteur de "
         "production.",
    'p': "L’énoncé montre l’ampleur de l’exigence : elle couvre non seulement "
         "les biens existants mais aussi les livraisons futures."},
   {'f': "Le cours rappelle qu’avoir autant d’équations que d’inconnues ne "
         "garantit pas qu’une solution existe, puisque deux droites peuvent ne "
         "jamais se croiser.",
    'p': "L’argument mathématique justifie l’existence même du problème traité "
         "par Arrow et Debreu et montre qu’il ne s’agit pas d’un raffinement "
         "formel."},
   {'f': "La dotation de survie suppose que chaque agent possède un minimum de "
         "ressources au départ, ce qui exige une intervention extérieure au "
         "marché : État, Église, institutions.",
    'p': "Le fait fournit la critique la plus citable du modèle : l’une de ses "
         "propres conditions contredit l’autosuffisance du marché."},
   {'f': "Les fonctions doivent être continues, sans trou ni saut brutal dans "
         "l’offre ou la demande, et bornées, c’est-à-dire encadrées entre un "
         "minimum et un maximum.",
    'p': "Les deux propriétés se traduisent économiquement par l’absence de "
         "comportements extrêmes, de coûts ou de demandes infinies, et de "
         "marchés qui disparaissent."}],
  [{'q': "Sujet du type « À quelles conditions le marché conduit-il à "
         "l’optimum ? »",
    'f': "Arrow et Debreu répondent en énonçant sept conditions, dont la "
         "complétude des marchés : il doit exister un marché pour chaque bien "
         "présent, chaque bien futur, chaque service et chaque facteur de "
         "production, de sorte qu’on puisse échanger aujourd’hui ce qui sera "
         "livré demain. Le cours souligne la contradiction la plus forte, "
         "celle de la dotation de survie, qui suppose une intervention "
         "extérieure au marché et contredit donc l’idée néoclassique que le "
         "marché se suffit à lui-même.",
    'r': "Le raisonnement procède condition par condition, ce qui transforme "
         "une affirmation générale sur l’efficacité du marché en une liste "
         "d’hypothèses discutables une à une.",
    'ex': "L’absence de marché pour certains risques futurs, qui prive les "
          "agents d’un prix sur lequel fonder leurs décisions présentes."},
   {'q': "Sujet du type « Pourquoi certains échanges n’ont-ils pas lieu ? »",
    'f': "Deux explications se superposent. L’une est l’incomplétude : il "
         "n’existe pas de marché pour l’échange envisagé, de sorte qu’aucun "
         "prix ne permet aux parties de se coordonner. L’autre est celle de "
         "Coase : le recours au marché n’est pas gratuit, puisqu’il engendre "
         "des coûts de recherche d’information, de négociation, de rédaction "
         "des contrats et de contrôle, et l’échange peut ne pas valoir ce "
         "coût.",
    'r': "Le raisonnement distingue l’absence de marché par impossibilité de "
         "l’absence par non-rentabilité, distinction décisive puisque la "
         "première appelle une création institutionnelle et la seconde non.",
    'ex': "Les marchés de quotas d’émission, créés institutionnellement pour "
          "faire exister un prix qui n’existait pas."}],
  voisins=['n5-equilibre', 'n6-couts-transaction', 'n6-externalites',
           'n5-pareto'])


d('n6-couts-transaction', 6, "Coûts de transaction",
  "Le marché n’est pas gratuit, et c’est pourquoi les entreprises existent",
  "Les coûts de transaction sont les coûts liés au fonctionnement du marché : "
  "coûts de recherche d’information, de négociation, de rédaction des "
  "contrats, de contrôle et de surveillance. Leur existence explique à la fois "
  "les limites du théorème de Coase et la raison d’être de l’entreprise, "
  "puisque certaines activités sont internalisées afin de les réduire.",
  "La notion de coûts de transaction est l’une des plus fécondes du "
  "programme, car elle sert successivement de limite et d’explication. Comme "
  "limite d’abord : Coase montre que les externalités peuvent être résolues "
  "par le marché si des droits de propriété clairement définis sont attribués, "
  "mais il insiste sur un point crucial — le marché n’est pas gratuit. La "
  "condition de validité de son théorème est donc triple : les coûts de "
  "transaction doivent être faibles, les acteurs ne doivent pas être trop "
  "nombreux, et les droits de propriété doivent être faciles à définir. Le "
  "cours en tire une liste de cas favorables — ressources facilement "
  "identifiables, acteurs peu nombreux, droits clairs, coûts faibles, avec "
  "pour exemples les terres agricoles et les enclosures, les quotas "
  "d’émission, les concessions et les ressources naturelles localisées — et "
  "une liste de cas défavorables : biens difficiles à délimiter, acteurs trop "
  "nombreux, coûts de transaction élevés, propriété difficile à attribuer, "
  "avec pour exemples l’air, les océans, le climat et certaines espèces "
  "animales très mobiles. Comme explication ensuite, et c’est l’apport de "
  "Williamson : certaines entreprises internalisent des activités afin de "
  "réduire les coûts de transaction. L’entreprise n’est alors plus une simple "
  "fonction de production mais un mode de coordination alternatif au marché, "
  "choisi lorsque le recours au marché coûte plus cher que l’organisation "
  "interne. Le cours en tire deux prolongements. Premier prolongement, la "
  "concentration verticale s’explique économiquement : réunir fournisseurs, "
  "producteurs et distributeurs permet de contrôler la chaîne productive en "
  "économisant les coûts de contractualisation. Second prolongement, les "
  "contrats ne sont pas tous formels : certaines relations reposent sur la "
  "confiance, une entreprise gardant un fournisseur non parce qu’il est le "
  "moins cher mais parce qu’il est fiable, connu, jugé honnête ; apparaissent "
  "alors des routines et des relations informelles, que le cours relie aux "
  "institutions formelles et informelles de North.",
  [("Le coût d’usage du marché",
    "Échanger exige de rechercher l’information, de négocier, de rédiger un "
    "contrat puis d’en contrôler l’exécution : ces opérations consomment des "
    "ressources, de sorte que le marché n’est jamais gratuit."),
   ("La condition de validité de la solution marchande",
    "Le théorème de Coase ne fonctionne que si ces coûts restent faibles, si "
    "les acteurs sont peu nombreux et si les droits sont faciles à définir : "
    "trois conditions qui délimitent le domaine de la solution privée."),
   ("L’arbitrage entre marché et organisation",
    "L’entreprise compare le coût du recours au marché au coût de "
    "l’organisation interne : elle internalise l’activité lorsque le premier "
    "excède le second, ce qui fixe la frontière de la firme."),
   ("La protection des actifs stratégiques",
    "La firme garde le contrôle lorsqu’elle détient une technologie "
    "stratégique ou un savoir-faire particulier, qu’il existe un risque de "
    "copie ou que la qualité doit être strictement contrôlée."),
   ("Le rôle des relations informelles",
    "Toutes les relations ne passent pas par un contrat : la confiance, la "
    "réputation et les routines réduisent les coûts de transaction sans "
    "formalisation, ce qui rapproche l’analyse économique des institutions.")],
  [{'a': "La notion explique l’existence de l’entreprise, que la théorie du "
         "marché ne peut pas déduire de ses propres hypothèses.",
    'cond': "L’explication suppose que l’organisation interne ait elle aussi "
            "un coût, faute de quoi tout serait internalisé.",
    'lim': "Le cours souligne cet arbitrage : le choix dépend des coûts "
            "d’organisation et de contrôle autant que des coûts de "
            "transaction."},
   {'a': "Elle borne précisément la portée du théorème de Coase, ce qui évite "
         "d’en faire un argument universel pour la solution marchande.",
    'cond': "La délimitation suppose d’examiner la délimitabilité du bien et "
            "le nombre d’acteurs concernés.",
    'lim': "Les cas où la solution échoue sont précisément les plus "
           "importants : l’air, les océans, le climat et les espèces très "
           "mobiles."},
   {'a': "Elle fournit une explication économique de la concentration "
         "verticale, au-delà de la recherche de pouvoir de marché.",
    'cond': "L’argument suppose un risque réel de dépendance ou de perte "
            "technologique justifiant le contrôle direct.",
    'lim': "L’intégration peut aussi fermer l’accès des concurrents aux "
           "intrants ou à la distribution, et devenir une barrière à "
           "l’entrée."},
   {'a': "Elle intègre les relations informelles et la confiance dans "
         "l’analyse économique, ce qui en augmente le réalisme.",
    'cond': "L’intégration suppose d’admettre que des déterminants non "
            "marchands pèsent sur des décisions économiques.",
    'lim': "Elle rend les prédictions moins précises, puisque la confiance et "
           "la réputation sont difficiles à mesurer."}],
  [{'t': "Si les coûts de transaction sont faibles, le marché règle lui-même "
         "les externalités et l’intervention publique est superflue.",
    'qui': "Ronald Coase, avec son théorème.",
    'rep': "La conclusion est exacte sous ses conditions, mais celles-ci "
           "excluent les problèmes les plus graves : le cours cite l’air, les "
           "océans, le climat et les espèces animales très mobiles."},
   {'t': "L’internalisation des activités répond à une logique d’efficacité et "
         "non de domination.",
    'qui': "Oliver Williamson, pour qui les entreprises internalisent afin de "
           "réduire les coûts de transaction.",
    'rep': "L’argument est valide mais ne vaut pas exclusion : la même "
           "intégration peut simultanément économiser des coûts et verrouiller "
           "l’accès d’un concurrent à un intrant."},
   {'t': "L’extension des droits de propriété destinée à réduire les coûts de "
         "transaction peut créer de nouveaux blocages.",
    'qui': "Michael Heller, avec la tragédie des anti-communs.",
    'rep': "L’exemple pharmaceutique le démontre : à force de multiplier les "
           "brevets, chaque innovation exige royalties et autorisations "
           "multiples, et la recherche devient plus lente, plus coûteuse, "
           "parfois bloquée."},
   {'t': "Les coûts de transaction ne sont pas seulement un obstacle : ils "
         "sont une ressource stratégique pour les acteurs.",
    'qui': "Michel Crozier, pour qui les acteurs utilisent les zones "
           "d’incertitude à leur avantage.",
    'rep': "L’objection déplace l’analyse : réduire les coûts de transaction "
           "suppose de réduire l’incertitude, ce que certains acteurs ont "
           "précisément intérêt à empêcher."}],
  [{'n': "Ronald Coase",
    'i': "Le marché n’est pas gratuit : son fonctionnement engendre des coûts "
         "de transaction.",
    'p': "Il les énumère précisément : coûts de recherche d’information, de "
         "négociation, de rédaction des contrats, de contrôle et de "
         "surveillance. Leur niveau conditionne la validité de son théorème "
         "sur la résolution marchande des externalités."},
   {'n': "Oliver Williamson",
    'i': "Certaines entreprises internalisent des activités afin de réduire "
         "les coûts de transaction.",
    'p': "Le cours fait de cette thèse l’explication théorique de la "
         "concentration verticale, et la rattache aux néo-institutionnalistes. "
         "La frontière de l’entreprise devient alors une variable économique "
         "et non une donnée."},
   {'n': "Douglass North",
    'i': "Les institutions reposent à la fois sur des règles formelles et sur "
         "des règles informelles.",
    'p': "Le cours le mobilise en prolongement de Williamson : les contrats ne "
         "sont pas tous formels, certaines relations reposant sur la confiance, "
         "les habitudes et les routines, ce qui élargit l’analyse des coûts de "
         "transaction aux normes sociales."},
   {'n': "Michel Crozier",
    'i': "Les acteurs d’une organisation utilisent les zones d’incertitude à "
         "leur avantage.",
    'p': "Le cours l’oppose à Williamson et Akerlof : là où ceux-ci "
         "cherchent à réduire les asymétries et les coûts de transaction, "
         "Crozier montre que les acteurs peuvent au contraire entretenir "
         "l’incertitude parce qu’elle leur confère du pouvoir."}],
  [{'f': "Le cours définit les coûts de transaction comme les coûts liés au "
         "fonctionnement du marché : recherche d’information, négociation, "
         "rédaction des contrats, contrôle et surveillance.",
    'p': "L’énumération donne le contenu concret de la notion et permet de "
         "l’appliquer à n’importe quel échange examiné."},
   {'f': "La solution de Coase fonctionne pour les terres agricoles et les "
         "enclosures, les quotas d’émission, les concessions et les ressources "
         "naturelles localisées.",
    'p': "La liste fournit un critère opérationnel : la solution marchande "
         "vaut là où la ressource est délimitable et les acteurs identifiables."},
   {'f': "Elle pose problème pour l’air, les océans, le climat et certaines "
         "espèces animales très mobiles.",
    'p': "La liste symétrique montre que les défaillances les plus graves sont "
         "précisément celles que la solution marchande ne peut pas traiter."},
   {'f': "Le cours note qu’une entreprise garde parfois un fournisseur non "
         "parce qu’il est le moins cher mais parce qu’il est fiable, connu, "
         "jugé honnête.",
    'p': "L’exemple montre que la confiance fonctionne comme un substitut "
         "économique au contrat formel, en réduisant les coûts de contrôle."}],
  [{'q': "Sujet du type « Pourquoi existe-t-il des entreprises ? »",
    'f': "Parce que le recours au marché a un coût. Coase montre que le marché "
         "n’est pas gratuit : échanger suppose de rechercher l’information, de "
         "négocier, de rédiger des contrats et de contrôler leur exécution. "
         "Williamson en tire la conséquence : certaines entreprises "
         "internalisent des activités afin de réduire les coûts de "
         "transaction. L’entreprise apparaît ainsi comme un mode de "
         "coordination alternatif au marché, retenu lorsqu’il est moins "
         "coûteux que lui.",
    'r': "Le raisonnement fait de la frontière entre marché et organisation "
         "une variable économique déterminée par un arbitrage de coûts, ce qui "
         "est l’apport décisif de l’économie des coûts de transaction.",
    'ex': "L’internalisation d’une activité lorsque l’entreprise détient une "
          "technologie stratégique et qu’il existe un risque de copie."},
   {'q': "Sujet du type « Le marché peut-il corriger lui-même ses "
         "défaillances ? »",
    'f': "Coase répond oui, mais à trois conditions strictes que les coûts de "
         "transaction commandent : ces coûts doivent être faibles, les acteurs "
         "ne doivent pas être trop nombreux et les droits de propriété doivent "
         "être faciles à définir. Le cours en tire la délimitation exacte du "
         "domaine de validité : la solution fonctionne pour les terres "
         "agricoles, les quotas d’émission, les concessions et les ressources "
         "localisées, mais échoue pour l’air, les océans, le climat et les "
         "espèces très mobiles.",
    'r': "Le raisonnement montre que la capacité autocorrectrice du marché est "
         "inversement proportionnelle à l’importance du problème, les "
         "défaillances globales étant précisément les moins traitables par la "
         "propriété.",
    'ex': "Le climat, bien diffus et transfrontalier pour lequel dire à qui il "
          "appartient est économiquement complexe et politiquement "
          "contestable."}],
  voisins=['n6-externalites', 'n5-coordination', 'n6-marches-incomplets',
           'n5-concentration'])
