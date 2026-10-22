# -*- coding: utf-8 -*-
"""Ensemble 8 — L’entreprise, l’entrepreneur et la gouvernance (1/4)."""

from doss_base import d

d('n8-entreprise', 8, "Entreprise",
  "Pourquoi des organisations hiérarchiques existent-elles à côté du marché ?",
  "L’entreprise est une organisation qui combine des facteurs de production "
  "pour produire des biens et des services vendus sur un marché. Mais le cours "
  "insiste sur une question plus profonde : si le marché coordonnait "
  "parfaitement les échanges, pourquoi créer de grandes organisations "
  "hiérarchiques, salarier durablement des travailleurs et intégrer des "
  "activités, alors que tout pourrait être acheté directement sur le marché ?",
  "L’entreprise est l’objet où la théorie économique découvre qu’elle avait "
  "oublié l’organisation, et le cours reconstitue cette découverte en trois "
  "temps. Premier temps, la vision néoclassique traditionnelle : l’entreprise "
  "n’y est pas étudiée comme organisation, seul compte le producteur, qui "
  "combine le capital et le travail selon une fonction de production, loue les "
  "services du travail et rémunère les détenteurs du capital. Sous les "
  "hypothèses de rationalité, de productivités marginales décroissantes, de "
  "concurrence pure et parfaite et d’atomicité, la firme est price taker : "
  "elle réagit mécaniquement aux signaux de prix, ce que le cours appelle "
  "l’entreprise comme automate. Deuxième temps, le problème : dans la réalité, "
  "les grandes firmes existent, les multinationales dominent des pans entiers "
  "de l’économie, alors que l’atomicité supposait qu’aucune entreprise ne "
  "puisse peser. Il faut donc expliquer pourquoi les entreprises grandissent. "
  "Troisième temps, les deux réponses rivales que le cours met face à face. "
  "L’approche contractuelle, qui domine les années 1970 avec Alchian, Demsetz, "
  "Jensen et Meckling, soutient que la firme n’est pas différente du marché : "
  "le marché fonctionne grâce à des contrats, la firme aussi, elle est un nœud "
  "de contrats reliant salariés, dirigeants, actionnaires, fournisseurs et "
  "créanciers ; la seule différence est que le marché mobilise des contrats "
  "commerciaux et la firme y ajoute des contrats de travail. L’approche "
  "transactionnelle, avec Coase puis Oliver Williamson, soutient l’inverse : "
  "la firme existe justement pour échapper au marché, parce que recourir au "
  "marché coûte cher, crée de l’incertitude et favorise les conflits. Le cours "
  "ajoute enfin que l’entreprise n’a pas qu’un seul objectif : elle est aussi "
  "un lieu de coopération, de conflit, de pouvoir et d’identité.",
  [("La combinaison des facteurs",
    "L’entreprise réunit le capital et le travail selon une fonction de "
    "production : elle loue les services du travail, rémunère les détenteurs "
    "du capital et combine les facteurs, sans être nécessairement propriétaire "
    "de tous les moyens de production."),
   ("La coordination par l’autorité plutôt que par les prix",
    "Dans la firme, l’entrepreneur agit par autorité, alors que le marché "
    "fonctionne par les prix : c’est cette substitution d’un commandement "
    "hiérarchique au signal de prix qui distingue, chez Coase, la firme du "
    "marché."),
   ("L’arbitrage faire ou faire faire",
    "La taille de l’entreprise résulte de la comparaison entre les coûts de "
    "transaction du recours au marché et les coûts d’internalisation : la "
    "firme internalise tant que produire soi-même coûte moins cher que "
    "d’acheter."),
   ("La stabilisation des équipes",
    "Certaines activités exigent une coordination permanente, de la confiance "
    "et des habitudes communes : le travail collectif pousse à constituer des "
    "équipes stables, donc à développer des entreprises plutôt qu’à "
    "recontracter en permanence."),
   ("La production des routines",
    "Le fonctionnement réel de l’entreprise ne repose pas seulement sur des "
    "contrats formels mais sur la confiance, les habitudes et les routines : "
    "une firme garde un fournisseur fiable même s’il n’est pas le moins cher.")],
  [{'a': "L’entreprise permet une coordination que le marché assure mal, "
         "parce qu’elle remplace la négociation répétée par une relation "
         "d’autorité durable.",
    'cond': "L’argument vaut lorsque les transactions sont fréquentes et "
            "portent sur des actifs spécifiques, cas où la renégociation "
            "permanente serait coûteuse.",
    'lim': "Il perd de sa force pour les transactions ponctuelles et "
           "standardisées, que le marché traite parfaitement bien et qu’il "
           "serait absurde d’internaliser."},
   {'a': "Lire la firme comme un nœud de contrats a l’avantage de ramener "
         "l’entreprise dans le cadre analytique général des relations "
         "économiques volontaires.",
    'cond': "Cela suppose des agents rationnels, calculateurs et guidés par "
            "leur intérêt personnel, auxquels on ajoute seulement "
            "l’asymétrie d’information.",
    'lim': "Le cours relève que cette réduction oublie les relations "
           "humaines, la culture d’entreprise, les rapports de pouvoir et les "
           "dimensions sociales et politiques de l’organisation."},
   {'a': "L’approche transactionnelle explique la taille et les frontières "
         "des firmes, que la théorie standard laissait entièrement "
         "indéterminées.",
    'cond': "Elle exige que l’on puisse comparer les coûts de transaction aux "
            "coûts d’internalisation, donc que ces coûts soient au moins "
            "approximativement évaluables.",
    'lim': "Elle fait de l’entreprise un lieu de défiance et de triche, alors "
           "que le cours objecte qu’elle est aussi un lieu de coopération, et "
           "qu’elle ne vise pas que l’efficience."},
   {'a': "Considérer l’entreprise comme une organisation sociale et non comme "
         "un automate permet d’intégrer ses objectifs multiples.",
    'cond': "Il faut accepter que les acteurs recherchent aussi de la "
            "reconnaissance, de l’appartenance, du pouvoir et du sens, et pas "
            "seulement un gain monétaire.",
    'lim': "Cet élargissement rend l’analyse moins prédictive : plus on "
           "multiplie les objectifs poursuivis, moins le comportement de la "
           "firme est déductible d’un principe simple."}],
  [{'t': "La firme n’est pas de nature différente du marché : elle n’est "
         "qu’un ensemble de relations contractuelles entre agents rationnels.",
    'qui': "Armen Alchian et Harold Demsetz, puis Michael Jensen et William "
           "Meckling, dans l’approche contractuelle.",
    'rep': "Le cours répond que cette lecture réduit la firme à des contrats "
           "et à des calculs, et laisse de côté les relations humaines, la "
           "culture d’entreprise et les rapports de pouvoir qui la "
           "structurent réellement."},
   {'t': "La firme existe parce que le marché est coûteux, incertain et "
         "propice à l’opportunisme : elle est une alternative au marché.",
    'qui': "Ronald Coase dès 1937, prolongé par Oliver Williamson.",
    'rep': "Le cours objecte que le comportement opportuniste fait de "
           "l’entreprise un lieu de triche, alors qu’elle est aussi un lieu "
           "de coopération, et que son enjeu ne se limite pas à "
           "l’efficience."},
   {'t': "La firme est entièrement soumise au marché : elle réagit "
         "mécaniquement aux prix et aux quantités, comme un automate.",
    'qui': "La théorie néoclassique traditionnelle, qui ne raisonne que sur "
           "le producteur.",
    'rep': "Cette vision est contredite par les faits : les multinationales "
           "et les concentrations existent, alors que l’hypothèse "
           "d’atomicité supposait qu’aucune entreprise ne puisse exercer un "
           "pouvoir important."}],
  [{'n': "Ronald Coase",
    'i': "La firme existe parce qu’il y a un coût à recourir au marché, "
         "c’est-à-dire des coûts de transaction.",
    'p': "Le cours rappelle qu’il l’explique dès 1937 et en tire une règle de "
         "taille : la comparaison entre les coûts de transaction et les coûts "
         "d’internalisation détermine la taille de l’entreprise, qui cherche à "
         "minimiser ses coûts de transaction."},
   {'n': "Ronald Coase",
    'i': "La firme est un mode de coordination centralisé, par nature "
         "différent du marché.",
    'p': "Le cours insiste sur le critère : dans la firme l’entrepreneur agit "
         "par autorité, alors que le marché fonctionne avec des prix. C’est "
         "cette substitution du commandement au prix qui définit la frontière "
         "entre les deux modes de coordination."},
   {'n': "Armen Alchian",
    'i': "La firme est un nœud de contrats entre des acteurs aux intérêts "
         "divers tenus de travailler ensemble.",
    'p': "Avec Harold Demsetz, il ajoute que le manager assigne les tâches et "
         "qu’il est le créancier résiduel : il perçoit le revenu qui reste "
         "quand tous les autres apporteurs de facteurs sont rémunérés, et il a "
         "donc intérêt à ce que l’entreprise soit efficace."},
   {'n': "Oliver Williamson",
    'i': "La firme existe pour échapper aux limites du marché, qui coûte "
         "cher et génère des conflits.",
    'p': "Le cours précise qu’il prolonge Coase et Herbert Simon en ajoutant "
         "trois hypothèses : la rationalité limitée, l’avenir incertain et "
         "l’opportunisme. Les contrats sont donc nécessairement incomplets et "
         "exigent des dispositifs de surveillance."},
   {'n': "Alfred Marshall",
    'i': "La proximité géographique des entreprises engendre des effets "
         "d’agglomération.",
    'p': "Le cours le mobilise à propos des districts industriels pour "
         "montrer que la coordination productive ne se joue pas seulement "
         "entre la firme et le marché, mais aussi dans des réseaux "
         "territorialisés d’entreprises spécialisées."}],
  [{'f': "Les entreprises organisent aujourd’hui des réseaux complexes de "
         "sous-traitance et de coopération le long de chaînes de production "
         "mondialisées.",
    'p': "Cela montre que la frontière entre la firme et le marché n’est pas "
         "une ligne nette mais un continuum de formes hybrides, exactement ce "
         "que l’approche transactionnelle permet de penser."},
   {'f': "Le capitalisme contemporain fait coexister des grandes entreprises "
         "intégrées, des petites et moyennes entreprises, des firmes-réseaux, "
         "des districts industriels et des plateformes numériques.",
    'p': "La coexistence de ces formes interdit de conclure qu’un seul mode "
         "d’organisation serait optimal : la taille efficace dépend des "
         "activités, des actifs et de la fréquence des transactions."},
   {'f': "Le cours prend l’exemple d’une entreprise de déménagement, où le "
         "travail exige coordination, confiance et habitudes communes.",
    'p': "L’exemple établit que certaines activités ne peuvent pas être "
         "recomposées à chaque fois sur le marché et justifient des équipes "
         "stables, donc une entreprise."}],
  [{'q': "Pourquoi les entreprises existent-elles ?",
    'f': "Si le marché coordonnait parfaitement les échanges, l’entreprise "
         "serait superflue : il suffirait d’acheter chaque prestation au "
         "moment voulu. L’existence de firmes durables signale donc une "
         "défaillance du marché comme mode de coordination, et c’est ce que "
         "Coase établit dès 1937 en faisant des coûts de transaction la raison "
         "d’être de la firme.",
    'r': "Le raisonnement part de l’énigme que la théorie standard laisse "
         "ouverte, puis la résout par un coût oublié : celui du recours au "
         "marché lui-même, qui rend l’internalisation parfois moins chère.",
    'ex': "Le cours chiffre ce coût en nature : recherche d’informations, "
          "négociation, rédaction des contrats, surveillance, conflits "
          "juridiques."},
   {'q': "La firme fonctionne-t-elle comme un marché ?",
    'f': "Deux lectures s’opposent terme à terme. Pour l’approche "
         "contractuelle, la firme n’est qu’un nœud de contrats, donc une autre "
         "modalité de coordination marchande. Pour l’approche "
         "transactionnelle, elle est au contraire une organisation "
         "hiérarchique qui existe pour échapper au marché. L’opposition porte "
         "donc sur la nature même de l’entreprise.",
    'r': "On montre que le désaccord vient d’une hypothèse : selon que l’on "
         "suppose des contrats complets ou incomplets, la firme apparaît comme "
         "un marché déguisé ou comme son substitut.",
    'ex': "Chez Alchian et Demsetz, le manager est créancier résiduel d’un "
          "faisceau de contrats ; chez Williamson, il est le garant d’une "
          "surveillance rendue nécessaire par l’opportunisme."},
   {'q': "L’entreprise poursuit-elle un seul objectif ?",
    'f': "Réduire l’entreprise à la maximisation du profit a l’avantage de la "
         "simplicité analytique, mais le cours montre que cette finalité "
         "unique ne décrit plus les organisations réelles : l’entreprise est "
         "aussi un lieu de coopération et de conflit, un espace de pouvoir et "
         "un support d’identité pour ceux qui y travaillent.",
    'r': "Le raisonnement oppose la finalité postulée par la théorie aux "
         "objectifs effectivement poursuivis par les acteurs, puis conclut "
         "que l’élargissement des buts rend l’analyse plus réaliste mais "
         "moins prédictive.",
    'ex': "Le cours cite l’élargissement des objectifs aux dimensions "
          "sociales, environnementales et sociétales."}],
  voisins=['n8-entrepreneur', 'n8-frontieres-firme', 'n8-profit',
           'n6-couts-transaction'])


d('n8-entrepreneur', 8, "Entrepreneur",
  "Une fonction économique réelle, et un récit qui la dépasse",
  "L’entrepreneur est, dans le capitalisme entrepreneurial, celui qui réunit "
  "toutes les fonctions de l’entreprise : apporteur de capital, organisateur "
  "de la production, décideur, parfois travailleur lui-même. Il n’est pas "
  "salarié, il est son propre patron. Le cours en fait une figure totale, "
  "doublée d’une construction idéologique qu’il appelle le mythe du "
  "fondateur.",
  "Le cours traite l’entrepreneur en deux mouvements inverses, et c’est cette "
  "tension qui en fait un sujet de dissertation. Premier mouvement, la "
  "construction de la figure. Au dix-neuvième siècle, l’entreprise est de "
  "petite taille, peu complexe, et repose sur une personne centrale qui cumule "
  "la propriété du capital, la direction et souvent l’activité productive "
  "elle-même : propriété et contrôle sont confondus. Cette centralité est "
  "renforcée par la responsabilité illimitée, puisque l’entrepreneur "
  "individuel ne séparait pas son patrimoine personnel de celui de "
  "l’entreprise et engageait donc ses biens propres : le risque maximal "
  "légitime le pouvoir maximal. À cette fonction économique le cours ajoute "
  "deux lectures savantes. Celle de Max Weber d’abord : parmi les trois formes "
  "de domination, l’entrepreneur peut incarner la domination charismatique, "
  "car le pouvoir ne repose pas seulement sur la richesse ou la position "
  "hiérarchique mais aussi sur une qualité personnelle, le charisme, qui fait "
  "que les individus le suivent parce qu’il inspire et fédère. Celle de Joseph "
  "Schumpeter ensuite : l’entrepreneur est un innovateur, un preneur de "
  "risque, un agent de transformation, qui introduit de nouveaux produits, de "
  "nouvelles techniques et de nouveaux marchés ; l’économie ne progresse pas "
  "toute seule, elle avance grâce à des individus qui cassent les routines. "
  "Second mouvement, la déconstruction. Le récit dominant présente un individu "
  "seul, parti de rien, réussissant par son seul mérite. Anthony Galluzzo "
  "soutient dans Le mythe de l’entrepreneur, en 2023, que le capitalisme "
  "moderne construit cette image héroïque pour légitimer l’ordre économique "
  "et social, alors que l’innovation est collective, que l’État finance "
  "souvent une partie essentielle des innovations et que beaucoup "
  "d’entrepreneurs viennent déjà de milieux favorisés. Le cours conclut que "
  "cette organisation devient de toute façon insuffisante : avec les "
  "révolutions industrielles, une seule personne ne peut plus tout contrôler.",
  [("Le cumul des fonctions",
    "L’entrepreneur réunit l’apport de capital, l’organisation de la "
    "production et la décision, parfois le travail lui-même : il n’est pas "
    "salarié, ce qui concentre dans une seule personne ce que les grandes "
    "firmes répartiront ensuite entre plusieurs acteurs."),
   ("Le risque comme source du pouvoir",
    "La responsabilité illimitée fait que l’entrepreneur engage ses biens "
    "professionnels mais aussi ses biens personnels : supportant "
    "personnellement les risques, il tire de cette exposition la légitimité de "
    "sa position centrale."),
   ("L’innovation comme rupture des routines",
    "Chez Schumpeter, l’entrepreneur prend des risques, change les façons de "
    "produire et crée du nouveau : il introduit de nouveaux produits, de "
    "nouvelles techniques et de nouveaux marchés, ce qui met l’économie en "
    "mouvement."),
   ("L’adhésion charismatique",
    "Chez Weber, l’autorité de l’entrepreneur ne découle pas seulement de sa "
    "propriété : sa capacité à entraîner, à convaincre et à susciter "
    "l’adhésion relève de la domination charismatique, fondée sur une qualité "
    "personnelle."),
   ("La production du mythe",
    "Le récit du fondateur génial et solitaire remplit une fonction de "
    "légitimation : en attribuant la réussite au seul mérite individuel, il "
    "masque la dimension collective de l’innovation et le poids des réseaux, "
    "du capital et du contexte historique.")],
  [{'a': "La figure de l’entrepreneur explique réellement la gouvernance des "
         "entreprises aux origines du capitalisme, où propriété et contrôle "
         "sont effectivement confondus.",
    'cond': "L’argument ne vaut que pour des entreprises de petite taille et "
            "peu complexes, où une seule personne peut maîtriser l’ensemble "
            "de l’activité.",
    'lim': "Avec les révolutions industrielles, la complexité technique et la "
           "taille rendent cette direction impossible, ce qui fait apparaître "
           "la séparation entre propriété et direction."},
   {'a': "L’analyse schumpétérienne confère à l’entrepreneur un rôle "
         "macroéconomique précis : il est le moteur du capitalisme et de la "
         "croissance.",
    'cond': "Elle suppose que l’innovation provienne d’initiatives "
            "individuelles capables de rompre avec les routines établies.",
    'lim': "Le cours objecte que l’innovation est en réalité collective et "
           "que les salariés, ingénieurs, chercheurs et managers y jouent un "
           "rôle majeur."},
   {'a': "Mobiliser Weber permet de comprendre une autorité qui ne se déduit "
         "ni de la richesse ni de la hiérarchie.",
    'cond': "Il faut que l’entrepreneur suscite effectivement l’adhésion, "
            "faute de quoi le charisme reste une ressource potentielle "
            "inemployée.",
    'lim': "Le cours rappelle que les trois formes de domination se "
           "combinent dans la réalité, de sorte que le charisme n’explique "
           "jamais seul l’autorité d’un dirigeant."},
   {'a': "La critique sociologique du mythe apporte une information "
         "vérifiable sur l’origine sociale et le financement des "
         "innovations.",
    'cond': "Elle suppose que l’on dispose de données sur les trajectoires "
            "des entrepreneurs et sur la part publique du financement de "
            "l’innovation.",
    'lim': "Elle ne supprime pas la fonction économique de l’entrepreneur : "
           "montrer qu’il n’est jamais seul n’établit pas que son initiative "
           "soit sans effet."}],
  [{'t': "L’entrepreneur est un héros individuel, parti de rien, dont la "
         "réussite résulte du seul mérite personnel.",
    'qui': "Le récit dominant du fondateur, que le cours présente comme une "
           "construction idéologique.",
    'rep': "Anthony Galluzzo montre que l’innovation est collective, que "
           "l’État finance souvent une part essentielle des innovations et "
           "que le succès dépend aussi des réseaux, du capital et du contexte "
           "historique."},
   {'t': "L’entrepreneur est l’aventurier de l’économie, à l’origine des "
         "innovations qui dynamisent le capitalisme.",
    'qui': "Joseph Schumpeter, dans son analyse de l’entrepreneur "
           "innovateur.",
    'rep': "L’analyse garde sa force pour expliquer la dynamique du "
           "capitalisme, mais le cours la nuance en rappelant que "
           "l’entreprise est une production collective et que l’entrepreneur "
           "n’est jamais seul."},
   {'t': "Le pouvoir dans l’entreprise repose sur une aura personnelle autant "
         "que sur la propriété du capital.",
    'qui': "Max Weber, avec la domination charismatique.",
    'rep': "La proposition éclaire l’adhésion suscitée par certains "
           "dirigeants, mais le cours souligne que la domination "
           "légale-rationnelle devient dominante dans les organisations "
           "modernes, où l’on obéit à la fonction plus qu’à la personne."}],
  [{'n': "Joseph Schumpeter",
    'i': "L’entrepreneur est un innovateur et un preneur de risque, agent de "
         "transformation de l’économie.",
    'p': "Le cours précise ce qu’il introduit : de nouveaux produits, de "
         "nouvelles techniques, de nouveaux marchés. L’économie n’avance pas "
         "toute seule, elle progresse grâce à des individus qui cassent les "
         "routines, ce qui fait de l’entrepreneur le moteur du capitalisme."},
   {'n': "Max Weber",
    'i': "Le pouvoir peut reposer sur le charisme, c’est-à-dire sur une "
         "qualité personnelle et non sur la position occupée.",
    'p': "Le cours rattache cette idée à la distinction entre trois formes de "
         "domination, rationnelle-légale, traditionnelle et charismatique, et "
         "en tire que si les individus suivent l’entrepreneur, ce n’est pas "
         "seulement parce qu’il est propriétaire."},
   {'n': "Anthony Galluzzo",
    'i': "Le capitalisme moderne construit une image héroïque de "
         "l’entrepreneur pour légitimer l’ordre économique et social.",
    'p': "Le cours rattache cette thèse à Le mythe de l’entrepreneur, en "
         "2023, et détaille ce que le récit dissimule : le caractère "
         "collectif de l’innovation, le rôle des salariés et des chercheurs, "
         "le financement public et l’origine sociale souvent favorisée des "
         "fondateurs."},
   {'n': "Henri Fayol",
    'i': "La direction d’une entreprise peut être organisée rationnellement "
         "autour de fonctions précises.",
    'p': "Dans Administration industrielle et générale, en 1916, il énonce "
         "cinq fonctions : prévoir, organiser, commander, coordonner, "
         "contrôler. Le cours en tire que diriger devient une compétence "
         "enseignable, ce qui ouvre la voie au remplacement de l’entrepreneur "
         "par le manager."}],
  [{'f': "Les entreprises du capitalisme entrepreneurial sont souvent "
         "familiales et transmises de génération en génération, au point que "
         "le nom de l’entreprise reflète celui de la famille.",
    'p': "Les cas de Peugeot et d’Hermès que cite le cours montrent que la "
         "confusion entre propriété et pouvoir s’appuie sur une continuité "
         "dynastique, et non seulement sur la petite taille des firmes."},
   {'f': "Le récit héroïque s’appuie sur des figures contemporaines "
         "présentées comme des fondateurs géniaux et solitaires, que le cours "
         "cite comme exemples du mythe.",
    'p': "Le fait que les mêmes noms reviennent systématiquement indique que "
         "l’on a affaire à un récit construit et non à une description "
         "statistique des entrepreneurs réels."},
   {'f': "Avec les révolutions industrielles, les entreprises grandissent, "
         "les techniques se complexifient et la gestion devient plus "
         "difficile, notamment dans la sidérurgie et les chemins de fer.",
    'p': "Cette évolution démontre que la figure de l’entrepreneur-"
         "propriétaire est historiquement datée : une seule personne ne peut "
         "plus planifier la production, coordonner des milliers de salariés et "
         "gérer les finances."}],
  [{'q': "La figure de l’entrepreneur est-elle un mythe ?",
    'f': "La réponse ne peut être ni oui ni non. L’entrepreneur correspond "
         "d’abord à une réalité économique précise, celle du propriétaire-"
         "dirigeant qui supporte le risque et innove, mais il est aussi "
         "l’objet d’un récit qui lui attribue seul le résultat d’un processus "
         "collectif ; la fonction est réelle, c’est son attribution exclusive "
         "qui relève du mythe.",
    'r': "Le raisonnement dissocie deux niveaux : la fonction économique "
         "d’innovation et de prise de risque, qui résiste à la critique, et "
         "le récit de la réussite individuelle, que la sociologie "
         "démonte.",
    'ex': "Galluzzo rappelle en 2023 que l’État finance souvent une partie "
          "essentielle des innovations attribuées aux fondateurs."},
   {'q': "Qui dirige l’entreprise au commencement du capitalisme ?",
    'f': "Dans le capitalisme entrepreneurial, la question ne se pose presque "
         "pas : celui qui possède l’entreprise est aussi celui qui la dirige, "
         "et souvent celui qui produit. Cette confusion de la propriété et du "
         "contrôle n’est pourtant pas un état naturel du capitalisme, mais le "
         "produit d’une taille et d’une complexité limitées.",
    'r': "On montre que la concentration du pouvoir s’explique par les "
         "caractéristiques objectives des entreprises de l’époque, et non par "
         "une qualité intrinsèque de l’entrepreneur.",
    'ex': "La responsabilité illimitée, qui engage les biens personnels du "
          "propriétaire, est le signe juridique de cette confusion."},
   {'q': "L’entrepreneur est-il le moteur de la croissance ?",
    'f': "Chez Schumpeter, la réponse est affirmative : la croissance naît "
         "d’innovations portées par des individus qui rompent les routines. "
         "Mais le cours oppose à cette lecture une innovation collective, "
         "financée en partie par l’État et produite par des salariés, des "
         "ingénieurs et des chercheurs, ce qui déplace le moteur de "
         "l’individu vers l’organisation.",
    'r': "Le raisonnement conserve le mécanisme schumpétérien mais en change "
         "le sujet : ce n’est plus l’entrepreneur isolé, c’est le dispositif "
         "collectif de production des innovations.",
    'ex': "Le cours souligne le rôle majeur des salariés, ingénieurs, "
          "chercheurs et managers dans l’innovation."}],
  voisins=['n8-entreprise', 'n8-capitalisme-entrepreneurial',
           'n8-risque-incertitude', 'n8-profit'])


d('n8-profit', 8, "Profit",
  "Un revenu résiduel, une incitation, et une finalité contestée",
  "Le profit est le revenu qui reste à l’entreprise lorsque tous les autres "
  "apporteurs de facteurs ont été rémunérés. Le cours lui donne trois statuts "
  "successifs : une grandeur comptable mesurée par le taux de marge, une "
  "incitation qui explique les comportements, et une finalité normative "
  "lorsque Milton Friedman affirme que la seule responsabilité de l’entreprise "
  "est de maximiser le profit.",
  "Le profit est la notion où se joue la question de la finalité de "
  "l’entreprise, et le cours l’aborde par étages. Premier étage, comptable : "
  "le taux de marge indique la part de la valeur ajoutée qui reste à "
  "l’entreprise, un taux élevé traduisant la capacité à dégager un résultat "
  "d’exploitation important par rapport aux coûts de production, un taux faible "
  "signalant une fragilité financière associée à un manque de rentabilité. "
  "Deuxième étage, incitatif : chez Alchian et Demsetz, le manager est "
  "créancier résiduel, il perçoit le revenu qui reste quand tous les autres "
  "apporteurs de facteurs sont rémunérés, et il a donc intérêt à ce que "
  "l’entreprise soit efficace ; le profit n’est pas seulement un gain, il "
  "aligne les comportements. Troisième étage, dynamique : chez Schumpeter, "
  "l’innovateur bénéficie d’un avantage technologique, d’un brevet ou d’une "
  "position de quasi-monopole temporaire qui lui procure un surprofit, la rente "
  "d’innovation, laquelle n’est pas un privilège mais une incitation à innover. "
  "Quatrième étage, normatif : dans The Social Responsibility of Business is to "
  "Increase its Profits, en 1970, Milton Friedman soutient que la seule "
  "responsabilité de l’entreprise est de maximiser le profit pour les "
  "actionnaires, les dimensions sociales et environnementales étant "
  "secondaires. Cinquième étage, critique : le cours souligne que l’entreprise "
  "n’a pas qu’un seul objectif et que ses finalités se sont élargies aux "
  "dimensions sociales, environnementales et sociétales. Il distingue enfin le "
  "profit légitime du profit de rente : la rente de monopole est un profit "
  "élevé obtenu uniquement grâce à une position dominante, qui ne récompense ni "
  "l’innovation ni la productivité mais le pouvoir de marché.",
  [("Le profit comme revenu résiduel",
    "Le profit est ce qui reste une fois rémunérés tous les autres apporteurs "
    "de facteurs : il n’est pas garanti par contrat, ce qui en fait à la fois "
    "une prise de risque et une incitation à l’efficacité pour celui qui le "
    "perçoit."),
   ("Le taux de marge comme mesure",
    "Le taux de marge rapporte la marge dégagée au prix d’achat et indique la "
    "part de la valeur ajoutée conservée : il permet de lire la santé "
    "financière de l’entreprise et sa capacité à autofinancer son "
    "investissement."),
   ("La rente d’innovation",
    "L’innovateur protégé par un brevet ou par une avance technologique "
    "obtient un surprofit temporaire : la rente d’innovation récompense la "
    "prise de risque et constitue l’incitation même à innover, avant d’être "
    "erodée par l’imitation."),
   ("Le profit de position",
    "La rente de monopole est un profit élevé obtenu uniquement grâce à la "
    "position dominante : elle ne récompense ni l’innovation ni la "
    "productivité, et prive l’entreprise de toute pression à réduire ses "
    "coûts."),
   ("La discipline actionnariale",
    "Lorsque la rentabilité financière devient l’objectif assigné aux "
    "dirigeants, le profit cesse d’être un résultat pour devenir une "
    "contrainte imposée de l’extérieur, qui oriente les décisions vers les "
    "restructurations et la distribution de dividendes.")],
  [{'a': "Faire du profit l’objectif de l’entreprise fournit un critère de "
         "décision unique et donc un modèle de comportement prédictif.",
    'cond': "Le critère n’est opératoire que si les droits des autres parties "
            "sont déjà garantis par le droit et le contrat, faute de quoi la "
            "maximisation se fait à leurs dépens.",
    'lim': "Le cours relève que l’entreprise n’a pas qu’un seul objectif et "
           "que ses finalités se sont élargies aux dimensions sociales, "
           "environnementales et sociétales."},
   {'a': "Le profit résiduel aligne les intérêts : celui qui le perçoit a "
         "intérêt à ce que l’entreprise soit efficace.",
    'cond': "L’alignement suppose que le créancier résiduel dispose "
            "effectivement du pouvoir d’organiser la production et "
            "d’assigner les tâches.",
    'lim': "Lorsque la propriété et le contrôle sont séparés, le résidu va "
           "aux actionnaires mais les décisions appartiennent aux managers, "
           "et l’alignement disparaît."},
   {'a': "Le surprofit de l’innovateur est économiquement justifié parce "
         "qu’il rémunère une prise de risque et finance l’innovation "
         "suivante.",
    'cond': "Il faut que le surprofit reste temporaire et soit effectivement "
            "erodé par l’imitation et par l’entrée de concurrents.",
    'lim': "Si la position se verrouille, le surprofit d’innovation se "
           "transforme en rente de monopole, qui ne récompense plus que le "
           "pouvoir de marché."},
   {'a': "Mesurer le profit par le taux de marge permet un diagnostic "
         "financier simple et comparable entre entreprises.",
    'cond': "La comparaison n’a de sens qu’entre entreprises d’un même "
            "secteur, les structures de coûts et les intensités capitalistiques "
            "étant très différentes.",
    'lim': "Un taux de marge élevé peut traduire une position protégée autant "
           "qu’une efficacité productive : l’indicateur ne distingue pas le "
           "profit d’innovation du profit de rente."}],
  [{'t': "La seule responsabilité sociale de l’entreprise est d’augmenter ses "
         "profits ; les objectifs sociaux et environnementaux sont "
         "secondaires.",
    'qui': "Milton Friedman, dans The Social Responsibility of Business is to "
           "Increase its Profits, en 1970.",
    'rep': "Le cours oppose à cette thèse l’élargissement effectif des "
           "objectifs de l’entreprise et la montée des parties prenantes, qui "
           "conduit à une gouvernance hybride où la rentabilité n’est plus le "
           "seul critère."},
   {'t': "Le profit n’est pas une rémunération mais un prélèvement sur la "
         "valeur créée par le travailleur.",
    'qui': "Karl Marx, avec la plus-value comme source de l’exploitation "
           "capitaliste.",
    'rep': "L’analyse met en évidence un conflit de répartition que la "
           "lecture incitative ignore, mais elle explique mal la fonction "
           "d’incitation du résidu, que le cours documente avec le créancier "
           "résiduel."},
   {'t': "Le profit tend naturellement à décliner, parce que les rendements "
         "décroissants font monter les salaires et comprimer les marges.",
    'qui': "David Ricardo, avec la baisse tendancielle du taux de profit.",
    'rep': "La prévision d’un état stationnaire n’a pas été vérifiée, le "
           "progrès technique ayant repoussé les rendements décroissants, mais "
           "le mécanisme reste utile pour penser les contraintes de long terme "
           "sur la rentabilité."}],
  [{'n': "Milton Friedman",
    'i': "La seule responsabilité de l’entreprise est de maximiser le profit "
         "pour ses actionnaires.",
    'p': "Le cours rattache cette position à The Social Responsibility of "
         "Business is to Increase its Profits, en 1970, et en tire la "
         "légitimation du capitalisme actionnarial : l’entreprise devient un "
         "instrument au service des actionnaires, les autres dimensions étant "
         "jugées secondaires."},
   {'n': "Harold Demsetz",
    'i': "Le manager est le créancier résiduel de la firme, celui qui "
    "perçoit " "ce qui reste du revenu.",
    'p': "Avec Armen Alchian, il précise que ce créancier perçoit le revenu "
         "qui reste quand tous les autres apporteurs de facteurs sont "
         "rémunérés : il a donc intérêt à l’efficacité de l’entreprise et "
         "détient le pouvoir de vendre ses droits de propriété."},
   {'n': "Joseph Schumpeter",
    'i': "L’innovateur tire de son avance un surprofit temporaire, la rente "
         "d’innovation.",
    'p': "Le cours précise le rôle du brevet : il protège juridiquement "
         "l’innovation et empêche la copie immédiate, ce qui permet le "
         "surprofit. Cette rente n’est pas un privilège mais l’incitation "
         "même à innover."},
   {'n': "Karl Marx",
    'i': "Le profit provient de la plus-value, différence entre la valeur "
         "créée par le travailleur et son salaire.",
    'p': "Le cours en fait la source de l’exploitation capitaliste : le "
         "rapport salarial permet au détenteur du capital de s’approprier un "
         "surplus, ce qui fait du profit un enjeu de répartition et non "
         "seulement une incitation à produire efficacement."}],
  [{'f': "Le cours relève qu’en 2022 le taux de marge se situe autour de "
         "trente-deux pour cent, et rappelle qu’un taux d’autofinancement "
         "supérieur à cent signifie que l’entreprise peut financer seule son "
         "investissement.",
    'p': "Le chiffre montre que le profit n’est pas seulement un revenu "
         "distribué : il conditionne la capacité d’investissement et donc la "
         "croissance future de l’entreprise."},
   {'f': "Le cours distingue explicitement la rente de monopole, profit élevé "
         "obtenu grâce à la seule position dominante, du profit qui "
         "récompense l’innovation ou la productivité.",
    'p': "La distinction établit qu’un même niveau de profit peut avoir des "
         "significations économiques opposées, ce qui interdit de juger une "
         "entreprise sur son seul résultat."},
   {'f': "En situation de monopole, l’absence de concurrents supprime la "
         "pression à réduire les coûts, alors qu’en concurrence réduire ses "
         "coûts est une condition de survie.",
    'p': "Cela démontre que le profit n’a de vertu incitative que sous "
         "contrainte concurrentielle : protégé, il décourage l’effort "
         "productif au lieu de le stimuler."}],
  [{'q': "Le profit constitue-t-il le seul objectif de l’entreprise ?",
    'f': "La thèse de Friedman a le mérite de la clarté : en 1970, il "
         "soutient que la seule responsabilité de l’entreprise est "
         "d’augmenter ses profits. Mais le cours montre que cette finalité "
         "unique a été progressivement contestée, au point que l’entreprise "
         "poursuit aujourd’hui aussi des objectifs sociaux, environnementaux "
         "et sociétaux, dans une gouvernance devenue hybride.",
    'r': "On commence par reconnaître la cohérence de la position "
         "actionnariale, puis on montre que ses effets observés, "
         "court-termisme et inégalités, ont provoqué l’élargissement des "
         "objectifs assignés à la firme.",
    'ex': "La loi PACTE de 2019 introduit en France la raison d’être et le "
          "statut d’entreprise à mission."},
   {'q': "Tous les profits ont-ils la même signification ?",
    'f': "Un profit peut récompenser une innovation, et il est alors "
         "l’incitation même à innover ; il peut aussi résulter d’une position "
         "dominante, et il devient une rente qui ne récompense ni "
         "l’innovation ni la productivité, mais le seul pouvoir de marché. "
         "Juger une entreprise sur le niveau de son profit sans examiner son "
         "origine n’a donc guère de sens.",
    'r': "Le raisonnement sépare les sources du profit, puis en tire une "
         "conséquence normative : la politique de la concurrence doit "
         "s’attaquer à la rente sans décourager la rémunération de "
         "l’innovation.",
    'ex': "Le brevet illustre cette ambivalence : il crée un quasi-monopole "
          "temporaire tout en rémunérant l’innovateur."},
   {'q': "Le profit est-il une rémunération ou un prélèvement ?",
    'f': "Deux lectures du même flux s’opposent. Comme revenu résiduel, le "
         "profit rémunère un risque et une organisation, et il incite "
         "celui qui le perçoit à l’efficacité. Comme plus-value, il est chez "
         "Marx un prélèvement sur la valeur créée par le travailleur et donc "
         "le ressort de l’exploitation capitaliste.",
    'r': "On montre que les deux lectures ne portent pas sur la même "
         "question : l’une explique les comportements, l’autre la "
         "répartition, de sorte qu’elles ne se réfutent pas directement.",
    'ex': "Le créancier résiduel d’Alchian et Demsetz et la plus-value de "
          "Marx désignent le même montant avec deux significations opposées."}],
  voisins=['n8-entreprise', 'n8-valeur-actionnariale', 'n8-rse',
           'n8-entrepreneur'])


d('n8-risque-incertitude', 8, "Risque et incertitude",
  "Un avenir probabilisable, ou un avenir qui ne l’est pas",
  "Le risque désigne une situation dans laquelle les événements possibles et "
  "leurs probabilités peuvent être évalués ; l’incertitude désigne une "
  "situation où cette évaluation est hors d’atteinte. Le cours fait de cette "
  "distinction un point de rupture théorique : les néoclassiques considèrent "
  "que l’avenir est probabilisable, alors que l’approche transactionnelle "
  "postule au contraire un avenir incertain.",
  "La distinction entre risque et incertitude commande, dans le cours, le "
  "partage entre deux manières de faire de l’économie de l’entreprise. Du côté "
  "néoclassique, l’avenir est probabilisable : les agents peuvent prévoir, "
  "anticiper et calculer rationnellement, et le cours donne l’exemple du "
  "consommateur qui prépare sa retraite, anticipe ses revenus futurs et "
  "organise sa consommation, avec une référence implicite au modèle du cycle de "
  "vie. Dans ce cadre, l’incertitude n’est qu’un risque mal mesuré : elle se "
  "réduit par l’information et s’assure par le contrat. Du côté de "
  "Williamson, le constat est inverse et il en fait l’une de ses trois "
  "hypothèses majeures, aux côtés de la rationalité limitée et de "
  "l’opportunisme : l’avenir est incertain. La conséquence est immédiate et "
  "décisive : les contrats sont nécessairement incomplets, puisqu’aucune "
  "clause ne peut prévoir toutes les situations possibles ; il faut donc "
  "mettre en place des dispositifs de surveillance des agents, et "
  "l’organisation hiérarchique devient préférable au marché. L’incertitude "
  "n’est plus une imperfection à corriger, elle est la raison d’être de la "
  "firme. Le cours prolonge ce raisonnement en sociologie des organisations : "
  "chez Michel Crozier, aucune règle ne peut prévoir toutes les situations, de "
  "sorte que toute organisation comporte des zones d’incertitude ; ce qui "
  "constitue un problème pour l’organisation devient alors une ressource pour "
  "les acteurs capables de la maîtriser. Enfin, le cours associe le risque à "
  "l’entrepreneur : la responsabilité illimitée l’expose personnellement, et "
  "ce risque maximal fonde la centralité de sa position, tandis que la société "
  "anonyme et la responsabilité limitée transforment radicalement cette "
  "exposition.",
  [("L’avenir probabilisable",
    "Dans le cadre néoclassique, les états futurs et leurs probabilités sont "
    "connus : l’agent peut comparer des espérances, de sorte que les décisions "
    "intertemporelles se ramènent à un calcul et que le contrat peut tout "
    "prévoir."),
   ("L’incomplétude des contrats",
    "Si l’avenir n’est pas probabilisable et si la rationalité est limitée, "
    "aucun contrat ne peut énumérer les situations futures : les contrats sont "
    "nécessairement incomplets, ce qui laisse place à la renégociation et à "
    "l’opportunisme."),
   ("Le passage à la hiérarchie",
    "Parce que l’incertitude rend le marché risqué, instable et coûteux, la "
    "firme devient préférable : elle permet la surveillance, la hiérarchie, la "
    "coordination et le contrôle, là où le contrat marchand serait "
    "indéterminé."),
   ("L’incertitude comme ressource de pouvoir",
    "Dans une organisation, celui qui maîtrise une situation imprévisible "
    "rend les autres dépendants de lui : il augmente sa marge de liberté et "
    "réduit celle des autres, ce qui transforme l’incertitude en source de "
    "pouvoir."),
   ("L’exposition personnelle de l’entrepreneur",
    "Sans séparation entre patrimoine personnel et patrimoine professionnel, "
    "l’entrepreneur engage ses biens propres : ce risque maximal renforce son "
    "pouvoir, alors que la responsabilité limitée dissocie ensuite décision et "
    "exposition.")],
  [{'a': "Distinguer le risque de l’incertitude permet d’expliquer pourquoi "
         "les firmes existent, alors que le risque assurable n’exigerait "
         "aucune organisation.",
    'cond': "L’argument suppose que l’incertitude soit effectivement "
            "irréductible, et non une simple insuffisance d’information que "
            "l’on pourrait acheter.",
    'lim': "Pour les transactions standardisées et répétées, le marché assure "
           "très bien la coordination, ce qui montre que l’incertitude n’est "
           "pas partout du même ordre."},
   {'a': "L’incomplétude des contrats justifie des dispositifs de "
         "surveillance et explique les coûts d’organisation réellement "
         "observés dans les firmes.",
    'cond': "Elle suppose que la surveillance soit elle-même possible et "
            "moins coûteuse que la renégociation permanente des contrats.",
    'lim': "La surveillance a ses propres coûts, et le cours montre avec "
           "Crozier que les acteurs peuvent conserver des marges de manœuvre "
           "y compris sous contrôle étroit."},
   {'a': "Faire du risque la justification du pouvoir de l’entrepreneur donne "
         "un fondement clair à son autorité dans l’entreprise individuelle.",
    'cond': "Le raisonnement n’est valide que lorsque celui qui décide est "
            "aussi celui qui supporte les pertes, c’est-à-dire sous "
            "responsabilité illimitée.",
    'lim': "La séparation entre propriété et contrôle rompt ce lien : les "
           "managers décident sans supporter personnellement le risque, et le "
           "fondement de leur autorité doit être cherché ailleurs."},
   {'a': "Traiter l’incertitude comme une ressource éclaire des rapports de "
         "pouvoir que l’organigramme ne montre pas.",
    'cond': "Il faut que l’acteur maîtrise mieux que les autres la situation "
            "imprévisible, et que les autres en dépendent effectivement pour "
            "atteindre leurs objectifs.",
    'lim': "Cette lecture explique les blocages mais pas la performance "
           "d’ensemble : elle décrit la distribution du pouvoir plus que "
           "l’efficacité de l’organisation."}],
  [{'t': "L’avenir est probabilisable : les agents peuvent prévoir, anticiper "
         "et calculer rationnellement leurs décisions intertemporelles.",
    'qui': "Le cadre néoclassique, auquel le cours rattache le modèle du "
           "cycle de vie.",
    'rep': "Williamson objecte que les capacités cognitives sont limitées et "
           "que l’avenir est incertain, de sorte que les contrats sont "
           "nécessairement incomplets et exigent des dispositifs de "
           "surveillance."},
   {'t': "L’incertitude et l’opportunisme font de l’entreprise un lieu de "
         "défiance où il faut surveiller les agents.",
    'qui': "Oliver Williamson, dans l’approche transactionnelle.",
    'rep': "Le cours objecte que le comportement opportuniste fait de "
           "l’entreprise un lieu de triche, alors qu’elle est aussi un lieu "
           "de coopération, et que son enjeu ne se réduit pas à "
           "l’efficience."},
   {'t': "Les organisations doivent chercher à réduire leurs zones "
         "d’incertitude, qui rendent les comportements moins prévisibles.",
    'qui': "La logique gestionnaire que Crozier met en évidence pour la "
           "retourner.",
    'rep': "Crozier montre que ce qui constitue un problème pour "
           "l’organisation devient une ressource pour les acteurs : réduire "
           "les zones d’incertitude remet en cause des équilibres de pouvoir "
           "et provoque des résistances au changement."}],
  [{'n': "Oliver Williamson",
    'i': "L’avenir est incertain, ce qui rend les contrats nécessairement "
         "incomplets.",
    'p': "Le cours en fait l’une de ses trois hypothèses majeures, avec la "
         "rationalité limitée et l’opportunisme, et en tire la conséquence "
         "organisationnelle : les individus agissant dans un environnement "
         "incertain, il faut mettre en place des dispositifs de surveillance "
         "des agents."},
   {'n': "Herbert Simon",
    'i': "Les individus ne disposent pas d’une information parfaite et leurs "
         "capacités cognitives sont limitées.",
    'p': "Le cours fait de cette rationalité limitée la source de "
         "l’incomplétude contractuelle chez Williamson : ne sachant pas tout "
         "et ne pouvant pas tout prévoir, les agents ne peuvent pas écrire de "
         "contrats complets et se contentent de solutions satisfaisantes."},
   {'n': "Michel Crozier",
    'i': "Une zone d’incertitude est une situation que les règles ne "
         "prévoient pas entièrement, et toute organisation en comporte.",
    'p': "Le cours précise le retournement : l’incertitude est une contrainte "
         "pour l’organisation, qui cherche à la réduire, mais une ressource "
         "pour l’acteur qui la maîtrise, car il rend son comportement moins "
         "prévisible tout en influençant celui des autres."},
   {'n': "Franco Modigliani",
    'i': "Les ménages répartissent leur consommation sur l’ensemble de leur "
         "existence en anticipant leurs revenus futurs.",
    'p': "Le cours mobilise ce modèle du cycle de vie comme illustration de "
         "l’avenir probabilisable : il suppose des individus capables de "
         "prévoir leurs revenus et de préparer leur retraite, hypothèse que "
         "Williamson refuse explicitement."}],
  [{'f': "Le cours oppose deux exemples de contrat : celui de nettoyage "
         "prévoyant un passage par mois, qu’il faut renégocier si les vitres "
         "deviennent soudain très sales, et le contrat de travail, qui permet "
         "à l’employeur de modifier les tâches.",
    'p': "L’exemple montre concrètement comment l’incertitude sur les "
         "situations futures favorise l’internalisation : la subordination "
         "remplace une renégociation coûteuse et incertaine."},
   {'f': "À la SEITA, les ouvrières de production ne savent pas quand la "
         "machine sera réparée, avec quelle rapidité ni avec quelle qualité, "
         "alors que leurs primes en dépendent.",
    'p': "Le cas démontre que l’incertitude n’est pas seulement une donnée de "
         "l’environnement : elle se distribue à l’intérieur de "
         "l’organisation et redistribue le pouvoir indépendamment de la "
         "hiérarchie."},
   {'f': "L’entrepreneur individuel engage, en l’absence de séparation des "
         "patrimoines, ses biens professionnels mais aussi ses biens "
         "personnels dans l’activité.",
    'p': "Cette exposition maximale explique historiquement la centralité de "
         "sa position : le risque supporté personnellement fonde la "
         "légitimité du pouvoir de décision."}],
  [{'q': "L’incertitude explique-t-elle l’existence des firmes ?",
    'f': "Si l’avenir était probabilisable, tout pourrait être écrit dans un "
         "contrat et le marché suffirait. C’est précisément parce que "
         "l’avenir est incertain et la rationalité limitée que les contrats "
         "restent incomplets et que la firme, par la hiérarchie et la "
         "surveillance, devient un mode de coordination préférable au "
         "marché.",
    'r': "Le raisonnement part du cas limite, celui du contrat complet, pour "
         "montrer que la firme n’apparaît que lorsque ce cas limite est "
         "violé, ce qui fait de l’incertitude une condition de son "
         "existence.",
    'ex': "Williamson ajoute explicitement à Coase l’avenir incertain, la "
          "rationalité limitée et l’opportunisme."},
   {'q': "Faut-il réduire l’incertitude dans les organisations ?",
    'f': "La réponse gestionnaire est affirmative, puisque l’incertitude rend "
         "les comportements moins prévisibles et les décisions plus "
         "difficiles. Mais Crozier montre que les zones d’incertitude sont "
         "aussi les ressources sur lesquelles les acteurs ont bâti leurs "
         "stratégies, de sorte que les supprimer déplace l’équilibre des "
         "pouvoirs et suscite des résistances.",
    'r': "On oppose l’intérêt de l’organisation à celui des acteurs, puis on "
         "en tire une conséquence pratique : une réforme échoue moins par "
         "mauvaise conception que par redistribution du pouvoir.",
    'ex': "Les ouvriers d’entretien de la SEITA tirent leur pouvoir de la "
          "seule imprévisibilité des réparations."},
   {'q': "Le risque justifie-t-il le pouvoir dans l’entreprise ?",
    'f': "Dans le capitalisme entrepreneurial, le lien est direct : celui qui "
         "engage ses biens personnels décide, et le risque maximal fonde le "
         "pouvoir maximal. La séparation entre propriété et contrôle rompt ce "
         "lien, puisque les managers décident sans supporter personnellement "
         "les pertes, ce qui ouvre précisément le problème de la gouvernance.",
    'r': "Le raisonnement suit la dissociation historique entre celui qui "
         "supporte le risque et celui qui décide, et montre que la "
         "gouvernance d’entreprise naît de cette dissociation.",
    'ex': "La responsabilité illimitée de l’entrepreneur individuel contraste "
          "avec la situation du manager salarié d’une société anonyme."}],
  voisins=['n8-entrepreneur', 'n8-relation-agence', 'n9-zones-incertitude',
           'n8-frontieres-firme'])


d('n8-frontieres-firme', 8, "Frontières de la firme",
  "Faire ou faire faire : où s’arrête l’entreprise ?",
  "Les frontières de la firme désignent la limite entre les activités que "
  "l’entreprise réalise elle-même et celles qu’elle achète sur le marché. Le "
  "cours les fait dépendre d’une comparaison : la firme internalise tant que "
  "les coûts de transaction du recours au marché dépassent les coûts "
  "d’internalisation, et Williamson précise que ces frontières dépendent de la "
  "nature des actifs gérés et de la fréquence des transactions.",
  "La question des frontières de la firme est celle que le cours formule en "
  "quatre mots : faire ou faire faire. Elle suppose d’abord une rupture avec "
  "la théorie standard, où la taille de l’entreprise est indéterminée parce "
  "que la firme n’est qu’un producteur réagissant aux prix. Coase fournit le "
  "principe : la firme existe parce qu’il y a un coût à recourir au marché, et "
  "la comparaison entre les coûts de transaction et les coûts "
  "d’internalisation détermine la taille de l’entreprise, qui cherche à "
  "minimiser ses coûts de transaction. Williamson en tire une théorie plus "
  "fine : les frontières de la firme dépendent de la nature des actifs "
  "qu’elle gère et de la fréquence des transactions qu’elle réalise, ce qui "
  "explique pourquoi certaines firmes ont intérêt à l’intégration verticale, "
  "et pourquoi d’autres préfèrent des formes hybrides. Le cours illustre la "
  "comparaison des deux côtés. Du côté de l’externalisation, l’entreprise "
  "délègue le recrutement, la formation, le remplacement des salariés, la "
  "gestion des absences et des congés, donc allège sa charge administrative : "
  "si le salarié prestataire est malade, c’est la société prestataire qui doit "
  "le remplacer. Du côté des limites, le contrat ne peut pas tout prévoir : si "
  "les vitres deviennent soudain très sales alors que le contrat prévoyait un "
  "nettoyage mensuel, il faut renégocier et payer davantage, tandis que dans "
  "une entreprise intégrée le salarié étant subordonné, l’employeur peut "
  "modifier les tâches. Mais intégrer coûte aussi : salaires, cotisations "
  "sociales, retraite, congés payés, formation, recrutement. Le cours ajoute "
  "enfin que les frontières ne sont pas seulement contractuelles : les "
  "relations reposent aussi sur la confiance, les habitudes et les routines, "
  "une entreprise gardant un fournisseur fiable même s’il n’est pas le moins "
  "cher.",
  [("La comparaison des deux coûts",
    "La frontière se place là où les coûts de transaction du recours au "
    "marché égalent les coûts d’internalisation : au-delà, l’entreprise "
    "achète ; en deçà, elle produit elle-même, ce qui détermine sa taille."),
   ("La spécificité des actifs",
    "Plus un actif est spécifique à une relation, plus le recours au marché "
    "expose à la renégociation et à l’opportunisme : l’intégration verticale "
    "protège l’investissement spécifique, alors qu’un actif banal peut être "
    "acheté sans risque."),
   ("La fréquence des transactions",
    "Une transaction occasionnelle supporte mal les coûts fixes d’une "
    "organisation interne, alors qu’une transaction très fréquente les amortit "
    "et rend l’internalisation avantageuse, ce qui déplace la frontière vers "
    "l’intérieur."),
   ("L’incomplétude du contrat d’externalisation",
    "Le contrat de prestation ne peut pas prévoir tous les besoins futurs : "
    "tout imprévu suppose une renégociation et un paiement supplémentaire, "
    "alors que la subordination salariale permet de modifier les tâches sans "
    "renégocier."),
   ("Les coûts propres à l’internalisation",
    "Employer directement implique salaires, cotisations sociales, retraite, "
    "congés payés, formation et recrutement : ces coûts constituent la "
    "contrepartie de la souplesse hiérarchique et bornent l’extension de la "
    "firme.")],
  [{'a': "Le critère des coûts de transaction explique une grandeur que la "
         "théorie standard laissait indéterminée : la taille de l’entreprise.",
    'cond': "Il faut pouvoir comparer les deux types de coûts, donc disposer "
            "d’une évaluation au moins approximative des coûts de "
            "négociation, de surveillance et de conflit.",
    'lim': "Ces coûts sont largement inobservables, ce qui rend la théorie "
           "difficile à réfuter et la frontière prévue souvent indéterminée "
           "en pratique."},
   {'a': "Raisonner par la spécificité des actifs et la fréquence des "
         "transactions permet de prévoir des choix organisationnels "
         "différents selon les activités.",
    'cond': "Le raisonnement suppose que l’entreprise puisse réellement "
            "choisir, c’est-à-dire qu’il existe des prestataires disponibles "
            "sur le marché.",
    'lim': "Il laisse de côté les déterminants stratégiques du périmètre, "
           "comme la volonté de contrôler une technologie ou de préserver un "
           "pouvoir de marché."},
   {'a': "L’externalisation procure un gain administratif réel, puisqu’elle "
         "transfère au prestataire le recrutement, la formation et le "
         "remplacement des salariés.",
    'cond': "Le gain suppose que la prestation soit suffisamment "
            "standardisée pour être décrite dans un contrat et contrôlée sur "
            "un résultat.",
    'lim': "Dès que les besoins deviennent imprévisibles, la renégociation "
           "annule le gain : le cours montre qu’un simple changement de "
           "circonstances oblige à payer davantage."},
   {'a': "L’intégration apporte la souplesse de la subordination : "
         "l’employeur peut modifier les tâches sans renégocier le contrat.",
    'cond': "Cette souplesse suppose un rapport de subordination juridique, "
            "donc un contrat de travail et non une prestation de services.",
    'lim': "Elle se paie par l’ensemble des coûts attachés à l’emploi direct, "
           "des cotisations sociales à la formation, qui limitent "
           "l’internalisation."}],
  [{'t': "La taille de la firme résulte d’un calcul de minimisation des "
         "coûts de transaction, donc d’une recherche d’efficience.",
    'qui': "Ronald Coase, prolongé par Oliver Williamson.",
    'rep': "Le cours objecte que l’enjeu de l’entreprise ne se réduit pas à "
           "son efficience, et que ce raisonnement fait de la firme un lieu "
           "de défiance alors qu’elle est aussi un lieu de coopération."},
   {'t': "La frontière entre firme et marché n’a pas de signification "
         "profonde, puisque les deux reposent sur des contrats entre agents "
         "rationnels.",
    'qui': "L’approche contractuelle d’Alchian, Demsetz, Jensen et Meckling.",
    'rep': "Coase répond que la nature de la coordination diffère : dans la "
           "firme l’entrepreneur agit par autorité, alors que le marché "
           "fonctionne avec des prix, ce qui en fait deux modes distincts."},
   {'t': "Les frontières de la firme se déduisent de la nature des actifs et "
         "de la fréquence des transactions, indépendamment des relations "
         "sociales nouées entre les parties.",
    'qui': "La lecture transactionnelle stricte des choix d’intégration.",
    'rep': "Le cours objecte que les contrats ne sont pas tous formels et que "
           "la confiance, les habitudes et les routines expliquent qu’une "
           "entreprise conserve un fournisseur jugé fiable plutôt que le "
           "moins cher."}],
  [{'n': "Ronald Coase",
    'i': "La comparaison entre coûts de transaction et coûts "
         "d’internalisation détermine la taille de l’entreprise.",
    'p': "Le cours fait de cette comparaison la première théorie des "
         "frontières de la firme : l’entreprise s’étend tant que produire "
         "elle-même coûte moins cher que recourir au marché, et cherche donc "
         "à minimiser ses coûts de transaction."},
   {'n': "Oliver Williamson",
    'i': "Les frontières de la firme dépendent de la nature des actifs "
         "qu’elle gère et de la fréquence des transactions qu’elle réalise.",
    'p': "Le cours en tire une typologie de stratégies : cette approche "
         "explique pourquoi certaines firmes ont intérêt à l’intégration "
         "verticale et pourquoi d’autres préfèrent des formes hybrides, la "
         "concentration verticale devenant un moyen de réduire les coûts de "
         "transaction."},
   {'n': "Douglass North",
    'i': "Les institutions reposent à la fois sur des règles formelles et sur "
         "des règles informelles.",
    'p': "Le cours mobilise cette distinction comme prolongement moderne : "
         "les relations entre firmes ne se réduisent pas aux contrats écrits, "
         "mais s’appuient aussi sur la confiance, les habitudes et les "
         "routines qui stabilisent les échanges."}],
  [{'f': "Le cours oppose deux coûts concrets : déléguer le nettoyage évite "
         "de gérer recrutement, formation, absences et congés, mais employer "
         "directement implique salaires, cotisations sociales, retraite, "
         "congés payés et formation.",
    'p': "La mise en regard montre que l’arbitrage n’est pas idéologique mais "
         "comptable : chacune des deux solutions a un coût propre, et c’est "
         "leur comparaison qui fixe la frontière."},
   {'f': "L’exemple du contrat de nettoyage prévoyant un passage mensuel "
         "montre qu’un changement de circonstances oblige à renégocier et à "
         "payer davantage.",
    'p': "L’exemple établit que l’incomplétude du contrat est la vraie limite "
         "de l’externalisation : ce n’est pas le prix de la prestation qui "
         "pose problème, c’est l’imprévu."},
   {'f': "Le capitalisme contemporain combine grandes entreprises intégrées, "
         "petites et moyennes entreprises, plateformes, réseaux, "
         "sous-traitance et intégration verticale.",
    'p': "Cette diversité confirme qu’il n’existe pas de frontière optimale "
         "unique : la limite entre firme et marché varie selon les actifs, "
         "les fréquences et les secteurs."}],
  [{'q': "Faut-il faire ou faire faire ?",
    'f': "La question n’admet pas de réponse générale, car elle dépend de "
         "deux grandeurs. Si l’activité mobilise des actifs spécifiques et "
         "des transactions fréquentes, l’externalisation expose à la "
         "renégociation et l’intégration s’impose ; si la prestation est "
         "standardisée et occasionnelle, les coûts attachés à l’emploi direct "
         "rendent le recours au marché préférable.",
    'r': "Le raisonnement applique le critère de Williamson aux deux cas "
         "extrêmes, puis conclut que la frontière est contingente et non "
         "déductible d’un principe unique.",
    'ex': "Le cours montre qu’un contrat de nettoyage mensuel doit être "
          "renégocié dès que les besoins changent."},
   {'q': "La grande entreprise est-elle plus efficace ?",
    'f': "Chandler soutient qu’elle l’est, parce que la coordination interne "
         "des managers remplace avantageusement le marché et permet des "
         "économies d’échelle. Mais l’argument des coûts de transaction "
         "montre que cet avantage a une borne : au-delà d’un certain "
         "périmètre, les coûts d’internalisation dépassent ceux du marché, et "
         "la firme-réseau devient préférable à la firme intégrée.",
    'r': "On confronte l’avantage de coordination à son coût croissant, ce "
         "qui transforme la question de l’efficacité en question de taille "
         "optimale.",
    'ex': "La coexistence durable des petites et moyennes entreprises et des "
          "firmes-réseaux avec les grands groupes intégrés."},
   {'q': "Les frontières de la firme se réduisent-elles à un calcul ?",
    'f': "Le calcul des coûts de transaction donne le principe, mais le cours "
         "ajoute que les relations ne sont pas toutes contractuelles : une "
         "entreprise garde un fournisseur non parce qu’il est le moins cher, "
         "mais parce qu’il est fiable, connu et jugé honnête. La confiance et "
         "les routines déplacent donc une frontière que le calcul seul ne "
         "suffit pas à fixer.",
    'r': "Le raisonnement complète le critère économique par les "
         "déterminants institutionnels, en s’appuyant sur la distinction "
         "entre règles formelles et informelles.",
    'ex': "Le cours renvoie sur ce point à la distinction de Douglass North "
          "entre règles formelles et informelles."}],
  voisins=['n8-entreprise', 'n6-couts-transaction', 'n8-integration-verticale',
           'n8-externalisation'])
