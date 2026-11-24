# -*- coding: utf-8 -*-
"""Chapitre 1 — complément de questions « Appliquer » et « Raisonner ».

L'audit a montré que le chapitre était solide sur « Connaître » et
« Comprendre » mais pauvre sur les deux niveaux hauts. Ces questions
reprennent donc les calculs et les enchaînements du cours : multiplicateur
et accélérateur, salaire brut et net, pouvoir d'achat, actualisation,
quotient familial, mécanique du déficit. Chaque renvoi a été vérifié dans
le texte du chapitre.
"""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------- c1-01 · circuit
f(id='q1-m01', sp='c1-01', niv='raisonner', type='qcm', b=47,
  q="La comptabilité nationale fige ses normes et conventions pendant cinq "
    "ans et demande au moins trois années pour publier des données "
    "définitives. Quelle exigence ce double délai sert-il ?",
  opts=["La comparabilité : des séries ne sont comparables dans le temps que "
        "si la règle de mesure ne change pas en cours de route",
        "La confidentialité des données des entreprises",
        "L’équilibre du budget de l’État, qui dépend de ces publications",
        "La rapidité de la décision politique"],
  ans=0,
  why=["Les données individuelles sont agrégées : la confidentialité tient à "
       "l’agrégation, pas au calendrier des normes.",
       "Le budget s’appuie sur ces chiffres, mais ce n’est pas la raison du "
       "délai : une norme stable sert d’abord la mesure.",
       "Le délai va au contraire contre la rapidité : il l’accepte comme prix "
       "de la fiabilité."],
  exp="Une statistique n’a de sens que rapportée à une convention. Si la "
      "définition du périmètre changeait chaque année, une hausse mesurée "
      "pourrait venir de la règle et non du phénomène. Le cours insiste donc "
      "sur deux garanties : des normes adoptées pour cinq ans sous l’égide de "
      "l’ONU, et un délai de trois ans avant la donnée définitive, le temps "
      "que les déclarations soient recoupées.",
  diss="Argument précieux dès qu’un sujet demande de « mesurer » : avant de "
       "commenter une série, on rappelle que l’indicateur est une convention, "
       "ce qui ouvre la critique du PIB ou du chômage sans tomber dans le "
       "relativisme."),

f(id='q1-m02', sp='c1-01', niv='appliquer', type='qcm', b=42,
  q="Un boulanger exerce en entreprise individuelle. Dans quel secteur "
    "institutionnel la comptabilité nationale le range-t-elle ?",
  opts=["Les ménages", "Les sociétés non financières",
        "Les administrations publiques",
        "Les institutions sans but lucratif au service des ménages"],
  ans=0,
  why=["Les sociétés non financières supposent une personnalité juridique "
       "distincte de celle de leur propriétaire : ce n’est pas le cas d’une "
       "entreprise individuelle.",
       "Les administrations publiques produisent des services non marchands "
       "et redistribuent ; un boulanger vend une production marchande.",
       "Les ISBLSM offrent des services non marchands aux ménages sans but "
       "lucratif."],
  exp="Le critère est juridique : l’entreprise individuelle n’a pas de "
      "patrimoine séparé de celui de la personne qui la possède, donc la "
      "comptabilité nationale ne peut pas la distinguer du ménage. C’est le "
      "piège classique du classement par secteurs : on range selon la "
      "fonction principale et la ressource principale, mais la personnalité "
      "juridique tranche les cas limites.",
  diss="Sert à montrer qu’une catégorie statistique n’épouse jamais "
       "exactement la réalité économique : les micro-entrepreneurs "
       "« produisent » comme des entreprises mais sont comptés avec les "
       "ménages."),

f(id='q1-m03', sp='c1-01', niv='raisonner', type='courte', b=67,
  q="Pourquoi un circuit économique a-t-il besoin d’un système de "
    "financement ? Répondez en quelques phrases.",
  ans={'modele':
       "Les revenus distribués ne coïncident jamais, agent par agent, avec "
       "les dépenses souhaitées : certains agents ont un revenu supérieur à "
       "leurs dépenses — ils dégagent une capacité de financement, c’est-à-"
       "dire une épargne —, d’autres veulent dépenser plus qu’ils ne "
       "reçoivent et sont en besoin de financement. Sans mécanisme de "
       "transfert, l’épargne des premiers resterait inemployée et "
       "l’investissement des seconds n’aurait pas lieu : le circuit se "
       "contracterait. Le financement — crédit bancaire ou marché — assure la "
       "jonction entre capacités et besoins, et permet que la dépense totale "
       "reste au niveau de la production.",
       'cles': [{'f': ['capacite'], 'l': 'des agents en capacité de financement'},
                {'f': ['besoin'], 'l': 'des agents en besoin de financement'},
                {'f': ['epargne'], 'l': 'l’épargne des uns finance les autres'},
                {'f': ['credit', 'emprunt', 'marche', 'banque'],
                 'l': 'crédit, emprunt ou marché comme intermédiaire'}]},
  exp="Le cours pose que les revenus ne suffisent pas toujours à couvrir "
      "consommation et investissement : il faut alors du financement. La "
      "symétrie est essentielle — à tout besoin de financement répond, "
      "quelque part, une capacité. Le circuit n’est donc pas seulement un "
      "flux de biens et de revenus : il comporte un étage financier, sans "
      "lequel l’épargne serait une fuite définitive.",
  diss="Cette symétrie capacité / besoin est la charnière entre le chapitre "
       "sur le circuit et celui sur la monnaie et le financement : elle "
       "permet d’enchaîner sans rupture sur le rôle des banques."),

# --------------------------------------- c1-02 · investissement et revenus
f(id='q1-m04', sp='c1-02', niv='appliquer', type='qcm', b=156,
  q="Une entreprise achète un logiciel de gestion qu’elle utilisera pendant "
    "quatre ans. Comment la comptabilité nationale enregistre-t-elle cette "
    "dépense ?",
  opts=["Un investissement, parce que le bien sert plus d’un an",
        "Une consommation intermédiaire, parce qu’un logiciel est immatériel",
        "Un placement, parce qu’il s’agit d’un actif",
        "Une consommation finale, parce que l’entreprise est l’utilisatrice"],
  ans=0,
  why=["Le caractère immatériel ne change rien : le cours classe brevets, "
       "licences et logiciels dans l’investissement immatériel.",
       "Un placement est l’achat d’un actif financier — action ou "
       "obligation —, pas d’un outil de production.",
       "La consommation finale est le fait des ménages ; une entreprise qui "
       "achète un outil de production investit."],
  exp="Le critère retenu par le cours est la durée : au-delà d’un an, on "
      "parle d’investissement ; en deçà, de consommation intermédiaire, "
      "c’est-à-dire de biens transformés ou entièrement consommés dans le "
      "processus de production. La nature matérielle ou immatérielle du bien "
      "n’intervient pas dans ce classement : elle sépare seulement "
      "l’investissement corporel de l’investissement incorporel.",
  diss="Le critère de durée explique pourquoi la R&D et les logiciels pèsent "
       "de plus en plus dans l’investissement mesuré : utile pour nuancer "
       "l’idée d’un recul de l’investissement dans les économies de "
       "services."),

f(id='q1-m05', sp='c1-02', niv='appliquer', type='vf', b=164,
  q="Vrai ou faux : lorsqu’une entreprise achète des obligations d’État avec "
    "sa trésorerie, elle réalise un investissement au sens de la "
    "comptabilité nationale. Justifiez.",
  ans=False,
  exp="C’est un placement, non un investissement. Le cours distingue "
      "nettement les deux : le placement est l’achat d’un actif financier "
      "— action ou obligation — qui augmente le patrimoine financier de "
      "l’entreprise ; l’investissement est un achat qui augmente "
      "physiquement son stock de capital. Acheter une obligation, c’est "
      "prêter à l’émetteur, pas accroître la capacité de production. "
      "L’arbitrage entre les deux dépend de la situation de l’entreprise : "
      "en capacité ou en besoin de financement.",
  diss="Cette frontière sert à comprendre la critique de la "
       "« financiarisation » : des profits élevés peuvent nourrir des "
       "placements plutôt que de l’investissement productif."),

f(id='q1-m06', sp='c1-02', niv='appliquer', type='qcm', b=205,
  q="Le PIB d’un pays progresse de 2 % et l’investissement des entreprises "
    "de 6 % la même année. Quel mécanisme du cours cette observation "
    "illustre-t-elle ?",
  opts=["L’accélérateur d’Aftalion et Clark : une variation de la demande "
        "entraîne une variation plus que proportionnelle de l’investissement",
        "Le multiplicateur keynésien : une dépense initiale accroît le revenu "
        "d’un montant supérieur",
        "La loi d’Engel : la structure de la consommation se déforme avec le "
        "revenu",
        "L’effet de cliquet : la dépense résiste à la baisse"],
  ans=0,
  why=["Le multiplicateur part de l’investissement pour aboutir au revenu ; "
       "ici c’est la demande qui précède et l’investissement qui suit.",
       "La loi d’Engel porte sur la déformation de la structure de "
       "consommation, pas sur l’investissement.",
       "L’effet de cliquet est un mécanisme de consommation, avancé par "
       "Duesenberry."],
  exp="Le sens de la causalité est le seul moyen de ne pas confondre les deux "
      "mécanismes. Accélérateur : variation de la demande → variation de "
      "l’investissement, plus forte en proportion. Multiplicateur : variation "
      "de l’investissement → variation du revenu. Samuelson les combine en "
      "1939 dans l’oscillateur, où l’enchaînement investissement → revenu → "
      "demande → investissement engendre des fluctuations.",
  diss="Le couple multiplicateur / accélérateur est le cœur de toute "
       "dissertation sur l’instabilité de la croissance : il explique "
       "pourquoi un choc modéré de demande produit des variations amples de "
       "l’investissement."),

f(id='q1-m07', sp='c1-02', niv='raisonner', type='vf', b=207,
  q="Vrai ou faux : l’ouverture aux échanges réduit la valeur du "
    "multiplicateur des dépenses. Justifiez.",
  ans=True,
  exp="Le multiplicateur mesure la somme des vagues de dépenses engendrées "
      "par une dépense initiale ; son ampleur dépend de ce qui sort du "
      "circuit à chaque tour. En économie fermée, la seule fuite est "
      "l’épargne : avec une propension à consommer de 0,8, le cours retient "
      "ΔY = 5ΔI. En économie ouverte, une partie de la dépense s’adresse à "
      "des producteurs étrangers : les importations constituent une seconde "
      "fuite, et le cours ramène le coefficient à 2,5. Plus une économie est "
      "ouverte, plus une relance par la demande profite à ses partenaires.",
  diss="Argument décisif contre une relance isolée : c’est exactement ce qui "
       "est reproché à la relance française de 1981, et ce qui justifie la "
       "recherche d’une relance coordonnée."),

f(id='q1-m08', sp='c1-02', niv='appliquer', type='ordre', b=217,
  q="Remettez dans l’ordre décroissant les trois niveaux de salaire du cours, "
    "du plus coûteux pour l’employeur au plus faible pour le salarié.",
  ans=["Le salaire super brut : le coût total du travail pour l’employeur",
       "Le salaire brut : le super brut moins les cotisations patronales",
       "Le salaire net : le brut moins les cotisations salariales"],
  exp="La cascade se lit toujours dans ce sens : on part du coût total du "
      "travail, on retire les cotisations patronales pour obtenir le brut, "
      "puis les cotisations salariales pour obtenir le net. Le cours en tire "
      "une conséquence de politique économique : les cotisations étant "
      "proportionnelles, les allègements ciblés sur les bas salaires "
      "réduisent fortement le coût du travail peu qualifié, mais comportent "
      "un effet pervers — ils peuvent dissuader d’augmenter les salaires, "
      "puisque l’allègement disparaît à mesure que la rémunération monte.",
  diss="La cascade super brut / brut / net permet de montrer qu’une même "
       "mesure — baisser « le coût du travail » — se juge différemment selon "
       "qu’on regarde l’emploi ou le pouvoir d’achat."),

f(id='q1-m09', sp='c1-02', niv='appliquer', type='courte', b=243,
  q="Un salarié gagne 1 000 € par mois. L’indice des prix passe de 100 à 110. "
    "Que devient son revenu réel, et que faut-il en conclure si son salaire "
    "nominal a augmenté de 5 % sur la même période ?",
  ans={'modele':
       "Le revenu réel se calcule en déflatant : 1 000 / 110 × 100 = 909 €. À "
       "salaire nominal inchangé, le pouvoir d’achat recule donc d’environ "
       "9 %. Si le salaire nominal a augmenté de 5 %, le revenu réel vaut "
       "1 050 / 110 × 100 = 954 € : la hausse nominale ne compense pas "
       "l’inflation de 10 %, le pouvoir d’achat baisse encore d’environ 4,5 %. "
       "Conclusion : seule la comparaison entre la hausse des prix et celle du "
       "revenu nominal renseigne sur le pouvoir d’achat.",
       'cles': [{'f': ['909'], 'l': 'revenu réel de 909 € (1 000/110 × 100)'},
                {'f': ['deflat', 'indice', 'prix constant'],
                 'l': 'le calcul consiste à déflater par l’indice des prix'},
                {'f': ['954', '1050', '1 050'],
                 'l': 'avec +5 % de salaire, environ 954 €'},
                {'f': ['baisse', 'recul', 'diminue', 'perd'],
                 'l': 'le pouvoir d’achat baisse malgré la hausse nominale'}]},
  exp="Le cours donne la formule — pouvoir d’achat du revenu = revenu "
      "nominal / indice des prix × 100 — et l’exemple exact : 1 000 pour un "
      "indice de 110 donnent 909. L’intérêt pédagogique est le second temps : "
      "une hausse nominale inférieure à l’inflation est une baisse réelle. "
      "C’est la distinction entre valeur courante et volume, qui vaut pour "
      "toutes les grandeurs — PIB, consommation, investissement.",
  diss="Le réflexe « en valeur ou en volume ? » doit être posé dès qu’un "
       "sujet mobilise une série longue : sans déflation, toute comparaison "
       "dans le temps confond prix et quantités."),

# ----------------------------------------------- c1-03 · la consommation
f(id='q1-m10', sp='c1-03', niv='raisonner', type='ordre', b=328,
  q="Remettez dans l’ordre le raisonnement de Friedman sur le revenu "
    "permanent.",
  ans=["Le revenu courant se décompose en un revenu permanent, stable et "
       "anticipé, et un revenu transitoire, temporaire",
       "Les ménages estiment leur revenu permanent en actualisant les revenus "
       "qu’ils pensent percevoir dans l’avenir",
       "Ils calent leur consommation sur ce revenu permanent et cherchent à "
       "la lisser dans le temps",
       "Une hausse de revenu perçue comme transitoire est donc largement "
       "épargnée",
       "Une prime ponctuelle ou une baisse temporaire d’impôts a par "
       "conséquent peu d’effet sur la consommation"],
  exp="L’ordre compte : Friedman part d’un constat — la consommation est plus "
      "stable que le revenu —, le explique par une décomposition du revenu, "
      "puis en tire une conclusion de politique économique. C’est cette "
      "dernière qui vise Keynes : si la consommation dépend du revenu "
      "permanent, la relance budgétaire ponctuelle perd son efficacité, et "
      "avec elle la justification de l’intervention publique que le cours "
      "rattache à la loi psychologique fondamentale.",
  diss="Dérouler cette chaîne vaut mieux que citer « revenu permanent » : "
       "elle montre que le désaccord entre Keynes et Friedman porte moins sur "
       "les faits que sur l’horizon retenu par les ménages."),

f(id='q1-m11', sp='c1-03', niv='appliquer', type='qcm', b=332,
  q="Un placement doit rapporter 1 000 € dans un an et le taux d’intérêt est "
    "de 10 %. Quelle est sa valeur actualisée aujourd’hui ?",
  opts=["Environ 909 €", "1 100 €", "1 000 €", "Environ 990 €"],
  ans=0,
  why=["1 100 € est la valeur future de 1 000 € placés un an à 10 %, soit "
       "l’opération inverse.",
       "1 000 € serait la réponse si le taux était nul : actualiser, c’est "
       "précisément tenir compte du taux.",
       "990 € correspondrait à un taux d’environ 1 %, pas de 10 %."],
  exp="La valeur actualisée se calcule K / (1 + r), soit 1 000 / 1,1 = 909 €. "
      "L’intuition : disposer de 909 € aujourd’hui équivaut à disposer de "
      "1 000 € dans un an, puisque 909 € placés à 10 % donnent 1 000 €. "
      "Ce calcul n’est pas un détail technique : il est le support du "
      "raisonnement de Friedman, pour qui le revenu permanent est la valeur "
      "actualisée des revenus futurs anticipés.",
  diss="L’actualisation permet de relier, dans une même copie, la décision "
       "d’investir — comparer un coût immédiat à des recettes futures — et la "
       "décision de consommer selon Friedman."),

f(id='q1-m12', sp='c1-03', niv='raisonner', type='assoc', b=372,
  q="Associez chaque auteur à la variable par laquelle il explique la "
    "consommation.",
  ans=[["Keynes", "Le revenu courant, par la loi psychologique fondamentale"],
       ["Friedman", "Le revenu permanent, valeur actualisée des revenus futurs"],
       ["Duesenberry", "Le revenu relatif et le revenu le plus élevé atteint "
                       "dans le passé"],
       ["Modigliani", "Le patrimoine et l’âge, dans un cycle de vie"]],
  exp="Les trois critiques de Keynes ne se contredisent pas : elles ajoutent "
      "chacune une dimension absente de la fonction de consommation "
      "keynésienne. Friedman ajoute l’avenir anticipé, Duesenberry le "
      "regard des autres — effet de démonstration — et le passé — effet de "
      "cliquet, Modigliani la durée de la vie. Toutes trois expliquent le "
      "même fait : la consommation est plus stable que le revenu, et la "
      "propension moyenne à consommer ne baisse pas autant que Keynes "
      "l’anticipait.",
  diss="Cette grille à quatre entrées structure à elle seule une partie de "
       "dissertation sur les déterminants de la consommation : une variable "
       "explicative par auteur, et un même fait à expliquer."),

f(id='q1-m13', sp='c1-03', niv='raisonner', type='courte', b=311,
  q="Les études menées après 1945 ont-elles invalidé la loi psychologique "
    "fondamentale de Keynes ? Répondez de façon argumentée.",
  ans={'modele':
       "Elles l’ont nuancée plutôt que balayée. Keynes énonce que la part du "
       "revenu consacrée à la consommation décroît quand le revenu augmente. "
       "À court terme et en coupe instantanée, le fait se vérifie : les "
       "ménages aisés épargnent une part plus grande de leur revenu. Mais les "
       "séries longues montrent que le rapport C/Y reste assez stable à long "
       "terme. La loi d’Engel donne la clé : les ménages riches consacrent "
       "proportionnellement moins à l’alimentation, mais compensent par "
       "d’autres postes — loisirs, culture. La structure de la consommation "
       "se déforme donc, sans que la proportion globale baisse autant que "
       "Keynes le pensait.",
       'cles': [{'f': ['court terme', 'instantan', 'coupe'],
                 'l': 'la loi se vérifie à court terme ou en coupe'},
                {'f': ['stable', 'stabilit'],
                 'l': 'le rapport C/Y reste stable à long terme'},
                {'f': ['engel'], 'l': 'la loi d’Engel'},
                {'f': ['structure', 'poste', 'deform'],
                 'l': 'c’est la structure de la consommation qui change'}]},
  exp="Le cours présente la loi psychologique fondamentale, puis les travaux "
      "d’après 1945 qui montrent la stabilité de C/Y, puis la loi d’Engel "
      "comme explication de ce qui change réellement : la composition du "
      "panier, non sa part dans le revenu. Répondre « c’est faux » serait "
      "aussi excessif que répondre « c’est vrai » : la bonne réponse "
      "distingue les horizons et le niveau d’observation.",
  diss="Modèle de nuance attendu en dissertation : on oppose court terme et "
       "long terme, puis niveau et structure, avant de conclure que la loi "
       "garde sa portée là où Keynes l’utilise — l’analyse de la demande "
       "effective à court terme."),

f(id='q1-m14', sp='c1-03', niv='appliquer', type='qcm', b=378,
  q="Un étudiant de 22 ans s’endette pour financer ses études ; un cadre de "
    "50 ans épargne ; un retraité de 75 ans puise dans son épargne. Quel "
    "modèle rend compte de ces trois comportements ?",
  opts=["Le cycle de vie de Modigliani",
        "L’effet de cliquet de Duesenberry",
        "La loi psychologique fondamentale de Keynes",
        "La courbe de Laffer"],
  ans=0,
  why=["L’effet de cliquet décrit la résistance de la consommation à une "
       "baisse du revenu, pas la succession des âges.",
       "La loi de Keynes relie la consommation au seul revenu courant : elle "
       "ne dit rien de l’âge ni du patrimoine.",
       "La courbe de Laffer porte sur le rendement de l’impôt."],
  exp="Modigliani part du constat que le revenu est inégalement réparti sur "
      "la durée de la vie : faible chez les jeunes, maximal en milieu de "
      "carrière, déclinant à la retraite. Les ménages épargnent pendant la "
      "période d’activité pour ne pas voir leur consommation chuter une fois "
      "retraités ; les jeunes s’endettent, leur patrimoine est négatif. La "
      "consommation dépend donc du revenu courant, mais aussi du patrimoine "
      "et de l’âge.",
  diss="Le cycle de vie éclaire les débats sur les retraites et sur "
       "l’épargne des ménages : l’épargne n’est pas seulement une "
       "renonciation, c’est un transfert de pouvoir d’achat entre âges."),

# ------------------------------------------------ c1-04 · État et impôt
f(id='q1-m15', sp='c1-04', niv='appliquer', type='qcm', b=508,
  q="Un couple marié avec trois enfants déclare 40 000 € de revenu "
    "imposable. Combien de parts et quel quotient familial ?",
  opts=["4 parts, soit un quotient de 10 000 €",
        "5 parts, soit un quotient de 8 000 €",
        "3 parts, soit un quotient d’environ 13 300 €",
        "2 parts, soit un quotient de 20 000 €"],
  ans=0,
  why=["Compter une part entière par enfant est l’erreur la plus fréquente : "
       "les deux premiers comptent pour une demi-part chacun.",
       "Trois parts reviendrait à ignorer le troisième enfant.",
       "Deux parts correspondrait à un couple sans enfant."],
  exp="Le barème du cours est explicite : 1 + 1 pour les deux adultes, 0,5 "
      "pour chacun des deux premiers enfants, 1 pour le troisième, soit "
      "4 parts. Le quotient familial vaut alors 40 000 / 4 = 10 000 €, qui "
      "place le foyer dans la première tranche. L’impôt se calcule sur le "
      "quotient, puis se multiplie par le nombre de parts. Le mécanisme rend "
      "l’impôt à la fois progressif — le taux croît avec le revenu — et "
      "équitable — il tient compte de la taille du foyer.",
  diss="Le quotient familial est l’exemple à retenir pour distinguer "
       "progressivité et équité horizontale : deux foyers de même revenu mais "
       "de taille différente ne sont pas imposés pareillement."),

f(id='q1-m16', sp='c1-04', niv='raisonner', type='qcm', b=506,
  q="Pourquoi le cours qualifie-t-il la TVA d’impôt injuste, alors même que "
    "son taux est le même pour tous ?",
  opts=["Parce qu’un taux uniforme pèse proportionnellement plus sur les bas "
        "revenus, qui consomment la quasi-totalité de ce qu’ils gagnent",
        "Parce que son taux augmente avec le revenu du consommateur",
        "Parce qu’elle est payée par les entreprises et non par les ménages",
        "Parce qu’elle rapporte trop peu à l’État"],
  ans=0,
  why=["Le taux de TVA ne dépend pas du revenu de l’acheteur : il dépend du "
       "produit.",
       "La TVA est collectée par les entreprises mais supportée par le "
       "consommateur final : c’est la définition d’un impôt indirect.",
       "Elle rapporte au contraire environ 200 milliards d’euros, ce qui en "
       "fait la première recette fiscale."],
  exp="Un impôt est dit régressif lorsque son poids rapporté au revenu "
      "diminue à mesure que le revenu s’élève. Un ménage modeste consomme la "
      "quasi-totalité de son revenu, donc supporte la TVA sur presque tout ce "
      "qu’il gagne ; un ménage aisé en épargne une part, qui échappe à "
      "l’impôt sur la consommation. Même taux affiché, poids relatif "
      "différent : c’est pourquoi le cours oppose la TVA à l’impôt "
      "progressif sur le revenu.",
  diss="La distinction taux apparent / poids réel est l’outil central de "
       "toute dissertation sur la justice fiscale ; elle permet aussi "
       "d’expliquer les taux réduits sur les produits de première nécessité."),

f(id='q1-m17', sp='c1-04', niv='raisonner', type='courte', b=589,
  q="Quelle objection de liquidité est opposée à la taxe Zucman ? Expliquez "
    "le mécanisme.",
  ans={'modele':
       "La taxe porterait sur le patrimoine net, évalué pour les sociétés "
       "cotées à la capitalisation boursière et, pour les entreprises non "
       "cotées, à la valeur que les investisseurs leur attribuent. Or cette "
       "richesse peut être largement théorique : l’entrepreneur dont la "
       "start-up est valorisée 100 millions d’euros n’a encore rien vendu et "
       "ne perçoit aucun revenu correspondant. Une taxe de 2 % lui "
       "demanderait 2 millions d’euros qu’il ne détient pas sous forme "
       "liquide. Le même argument vaut pour des propriétaires riches en "
       "patrimoine et pauvres en revenu. S’y ajoute une limite juridique : le "
       "Conseil constitutionnel interdit l’impôt confiscatoire.",
       'cles': [{'f': ['liquid', 'liquidit'],
                 'l': 'le patrimoine taxé n’est pas liquide'},
                {'f': ['capitalisation', 'valoris', 'theorique', 'virtuel'],
                 'l': 'une valorisation théorique, non réalisée'},
                {'f': ['vendre', 'cede', 'revenu reel', 'aucun revenu'],
                 'l': 'il faudrait vendre pour payer'},
                {'f': ['confiscatoire', 'constitutionnel'],
                 'l': 'la limite de l’impôt confiscatoire'}]},
  exp="Le cours expose l’objection en trois temps : l’assiette repose sur une "
      "valorisation de marché, parfois purement virtuelle ; le contribuable "
      "peut ne disposer d’aucune liquidité pour s’acquitter de l’impôt ; et "
      "le droit français interdit un prélèvement confiscatoire. Il ajoute "
      "deux critiques économiques — un rendement estimé à 20 milliards jugé "
      "surévalué, et un risque de fuite des capitaux — que la réponse peut "
      "mentionner sans qu’elles répondent à la question posée, qui porte sur "
      "la liquidité.",
  diss="Exemple à garder pour montrer qu’un impôt ne se juge pas seulement à "
       "son rendement théorique : l’assiette, la liquidité et le droit "
       "constitutionnel en bornent la faisabilité."),

# --------------------------------------------- c1-05 · déficit et dette
f(id='q1-m18', sp='c1-05', niv='raisonner', type='ordre', b=464,
  q="Remettez dans l’ordre l’enchaînement qui conduit d’une récession à la "
    "hausse de la dette publique.",
  ans=["L’activité ralentit : la production et l’emploi reculent",
       "Les dépenses publiques augmentent mécaniquement — indemnisation du "
       "chômage, prestations sociales",
       "Les recettes publiques diminuent : moins de TVA, moins de cotisations "
       "sur les revenus du travail",
       "Les dépenses dépassent les recettes : un déficit public apparaît",
       "L’État émet des obligations pour le financer : la dette publique "
       "s’accroît"],
  exp="L’enchaînement est d’abord automatique : le cours insiste sur le fait "
      "qu’en récession les dépenses montent et les recettes baissent sans "
      "qu’aucune décision ne soit prise — ce sont les stabilisateurs "
      "automatiques. L’État peut ensuite y ajouter des mesures "
      "volontaristes. Le déficit est un flux annuel, la dette le stock des "
      "emprunts accumulés par l’ensemble des administrations publiques : "
      "confondre les deux est l’erreur la plus fréquente.",
  diss="Cette chaîne permet de répondre proprement à « faut-il réduire le "
       "déficit en période de crise ? » : une partie du déficit est l’effet "
       "de la crise, non sa cause."),

f(id='q1-m19', sp='c1-05', niv='raisonner', type='vf', b=652,
  q="Vrai ou faux : réduire la dette publique n’aurait aucun effet sur le "
    "budget courant de l’État. Justifiez.",
  ans=False,
  exp="La dette a un coût annuel : le service de la dette, c’est-à-dire les "
      "intérêts versés. Le cours en donne la trajectoire — environ "
      "39 milliards d’euros en 2019, 36,4 en 2021, 58 en 2024, et de l’ordre "
      "de 62 à 67 milliards attendus en 2025 — et rappelle que cette charge "
      "représente environ 2 % du PIB en 2024. Réduire la dette allégerait "
      "donc le budget de l’État autant que n’importe quelle économie de "
      "dépense. La difficulté est que la charge dépend aussi des taux : une "
      "remontée des taux alourdit le service même à dette constante, et "
      "oblige à « rouler » la dette dans des conditions moins favorables.",
  diss="Le service de la dette est le bon angle pour sortir du débat "
       "idéologique sur l’endettement : il transforme une question de stock "
       "en une question de flux budgétaire annuel et de taux d’intérêt."),
]
