# -*- coding: utf-8 -*-
"""Chapitre 2 — complément de questions « Appliquer » et « Raisonner ».

Le chapitre était fourni sur les définitions mais pauvre sur les deux
niveaux hauts. Ces questions reprennent donc les mécanismes chiffrés et les
enchaînements : fonctions de Krugman, création monétaire, multiplicateur et
diviseur, équation de Fisher, corridor des taux, canaux de transmission,
3D de Bourguinat, titrisation. Chaque renvoi a été vérifié dans le cours.
"""


def f(**kw):
    return kw


L = [

# ----------------------------------- c2-01 · formes et fonctions, change
f(id='q2-m01', sp='c2-01', niv='appliquer', type='assoc', b=90,
  q="Associez chaque usage international du dollar à la fonction de Krugman "
    "qu’il illustre.",
  ans=[["Le prix du pétrole est affiché en dollars, même entre un pays "
        "européen et un pays asiatique", "Monnaie de libellé"],
       ["Une entreprise française règle ses achats chinois en dollars",
        "Monnaie véhiculaire"],
       ["Des investisseurs du monde entier achètent des obligations "
        "américaines", "Monnaie d’investissement"],
       ["Le franc CFA est ancré à l’euro, le dollar de Hong Kong au dollar",
        "Monnaie d’ancrage"],
       ["Les banques centrales détiennent leurs réserves officielles en "
        "dollars", "Monnaie de réserve"]],
  exp="Krugman répartit six fonctions selon deux points de vue. Côté privé : "
      "libellé — on affiche les prix dans cette monnaie —, véhiculaire — on "
      "règle les transactions —, investissement — on y place son épargne. "
      "Côté banques centrales : ancrage — on y rattache son taux de change —, "
      "intervention — on l’achète ou on la vend pour défendre sa monnaie —, "
      "réserve — on la conserve. Une monnaie n’est pleinement internationale "
      "que si elle remplit les deux séries.",
  diss="La grille de Krugman permet de répondre précisément à « le dollar "
       "est-il menacé ? » : il faut regarder fonction par fonction, car "
       "l’euro progresse sur certaines et stagne sur d’autres."),

f(id='q2-m02', sp='c2-01', niv='appliquer', type='qcm', b=141,
  q="Le taux de change passe de 1 € = 1,10 $ à 1 € = 1,17 $. Qui est "
    "avantagé ?",
  opts=["Les importateurs européens et les exportateurs américains",
        "Les exportateurs européens et les importateurs américains",
        "Tous les agents européens, puisque l’euro est plus fort",
        "Personne : un taux de change nominal n’a pas d’effet réel"],
  ans=0,
  why=["C’est l’inverse : un euro plus cher renchérit les produits européens "
       "à l’étranger et pénalise donc les exportateurs européens.",
       "Une appréciation ne profite pas à tous : le cours insiste sur le fait "
       "que les intérêts des agents sont contradictoires.",
       "Le taux de change modifie les prix relatifs des produits nationaux et "
       "étrangers : il a bien des effets réels."],
  exp="L’euro s’apprécie, le dollar se déprécie. Un importateur européen paie "
      "ses achats en dollars moins cher en euros : il gagne. Un exportateur "
      "américain voit ses produits devenir moins chers pour les Européens : "
      "il gagne aussi. Symétriquement, l’exportateur européen et "
      "l’importateur américain perdent. Le cours en tire une leçon de "
      "méthode : en économie, les intérêts des agents sont contradictoires, "
      "et une même variation n’est ni bonne ni mauvaise en soi.",
  diss="Ce tableau à quatre cases évite la copie qui affirme qu’un euro fort "
       "est « bon » ou « mauvais » : il oblige à préciser pour qui."),

f(id='q2-m03', sp='c2-01', niv='raisonner', type='courte', b=156,
  q="L’euro a-t-il supprimé le risque de change pour la France ? Nuancez.",
  ans={'modele':
       "À l’intérieur de la zone, oui : les pays partagent la même monnaie, "
       "donc les échanges intra-zone ne subissent plus de variation de "
       "change, et le dumping monétaire — dévaluer pour gagner en "
       "compétitivité — n’est plus possible entre membres. Mais le risque "
       "n’a pas disparu : il s’est déplacé vers la relation entre l’euro et "
       "les autres monnaies, dollar en tête. S’y ajoute un coût nouveau : "
       "les taux étant décidés par la BCE pour l’ensemble de la zone, un choc "
       "asymétrique — qui ne frappe qu’un pays ou qu’un secteur — ne peut "
       "plus être amorti par une dépréciation nationale.",
       'cles': [{'f': ['intra', 'interieur', 'entre les pays', 'zone euro'],
                 'l': 'le risque disparaît à l’intérieur de la zone'},
                {'f': ['deplac', 'autres monnaies', 'dollar'],
                 'l': 'il s’est déplacé vers les monnaies tierces'},
                {'f': ['asymetrique'], 'l': 'le problème des chocs asymétriques'},
                {'f': ['devalu', 'depreciation', 'dumping'],
                 'l': 'la perte de l’arme de la dépréciation'}]},
  exp="Le cours est explicite : « avec l’euro ce risque n’a pas complètement "
      "disparu mais il s’est déplacé entre l’euro et les autres monnaies ». "
      "Il ajoute deux conséquences institutionnelles : l’impossibilité du "
      "dumping monétaire entre membres, et la vulnérabilité aux chocs "
      "asymétriques puisque la politique monétaire est unique. Une réponse "
      "qui se contente du premier point manque la moitié de la question.",
  diss="Le couple « disparition interne / déplacement externe » est "
       "transposable à toute union monétaire, et prépare la discussion des "
       "zones monétaires optimales."),

# --------------------------------- c2-02 · création monétaire et théories
f(id='q2-m04', sp='c2-02', niv='appliquer', type='qcm', b=241,
  q="Une banque accorde un crédit de 50 000 € à un ménage. Que se passe-t-il "
    "dans son bilan ?",
  opts=["Elle inscrit une créance à l’actif et crédite le compte du client au "
        "passif : la monnaie est créée au moment du prêt",
        "Elle transfère 50 000 € prélevés sur les dépôts d’autres clients",
        "Elle emprunte d’abord 50 000 € à la Banque centrale, puis prête",
        "Elle vend pour 50 000 € d’obligations d’État"],
  ans=0,
  why=["C’est l’idée intuitive que le cours réfute : « les crédits font les "
       "dépôts », la banque n’a pas besoin de dépôts préalables.",
       "Le refinancement auprès de la Banque centrale vient après, et "
       "seulement si nécessaire : il ne conditionne pas l’octroi du crédit.",
       "L’achat d’obligations d’État est une autre source de création "
       "monétaire, pas la contrepartie d’un crédit aux ménages."],
  exp="La création monétaire est la monétisation d’une créance : la banque "
      "transforme une promesse de remboursement en moyen de paiement "
      "immédiatement utilisable. L’opération est simultanée — elle crée la "
      "monnaie et sa contrepartie au même instant — et ne suppose aucune "
      "encaisse préalable. D’où la formule du cours : « les crédits font les "
      "dépôts ». Le remboursement détruit symétriquement la monnaie.",
  diss="Cette mécanique est le socle de tout développement sur l’endogénéité "
       "de la monnaie : elle montre que la quantité de monnaie dépend d’abord "
       "de la demande de crédit."),

f(id='q2-m05', sp='c2-02', niv='appliquer', type='qcm', b=264,
  q="Dans l’exemple du multiplicateur de crédit du cours, 100 de base "
    "monétaire circulent avec un taux de retrait en billets de 20 %. Quel "
    "montant de monnaie est finalement créé ?",
  opts=["500", "200", "120", "80"],
  ans=0,
  why=["200 correspondrait à un multiplicateur de 2, donc à un taux de "
       "retrait de 50 %.",
       "120 revient à ne compter qu’une seule vague supplémentaire.",
       "80 est le montant disponible après le premier retrait, pas le total "
       "créé."],
  exp="Les vagues successives forment une suite géométrique : 100, puis 80, "
      "puis 64, puis 51,2… de raison 0,8. La somme converge vers 100 / 0,2, "
      "soit 500 — c’est l’exemple exact du cours. Le modèle suppose que la "
      "Banque centrale contrôle la base monétaire M0 et donc, par le "
      "multiplicateur et les réserves obligatoires, la masse monétaire : "
      "dans cette optique la monnaie est exogène.",
  diss="Le chiffre importe moins que l’hypothèse : le multiplicateur ne vaut "
       "que si la contrainte vient de la base monétaire, ce que le diviseur "
       "de crédit conteste."),

f(id='q2-m06', sp='c2-02', niv='raisonner', type='vf', b=272,
  q="Vrai ou faux : multiplicateur de crédit et diviseur de crédit décrivent "
    "le même mécanisme, dans deux vocabulaires différents. Justifiez.",
  ans=False,
  exp="Ils décrivent le même circuit, mais en inversant le sens de la "
      "causalité, et donc la conclusion de politique économique. Dans le "
      "multiplicateur, la Banque centrale fixe la base monétaire et les "
      "banques en déduisent le volume de crédit : MC → M, la monnaie est "
      "exogène. Dans le diviseur, d’inspiration keynésienne, les banques "
      "prêtent d’abord en réponse à la demande de crédit, puis se "
      "refinancent auprès de la Banque centrale : M → MC, la monnaie est "
      "endogène. Dans le premier cas la Banque centrale pilote la quantité "
      "de monnaie ; dans le second, elle n’en pilote que le prix, le taux.",
  diss="L’opposition exogène / endogène commande tout le jugement porté sur "
       "le monétarisme : si la monnaie est endogène, cibler un agrégat "
       "monétaire n’a guère de sens."),

f(id='q2-m07', sp='c2-02', niv='appliquer', type='qcm', b=306,
  q="Dans l’équation de Fisher MV = PT, la quantité de monnaie augmente de "
    "10 %. Que prévoit la théorie quantitative, et sous quelles hypothèses ?",
  opts=["Les prix augmentent d’environ 10 %, si V et T sont stables",
        "La production augmente de 10 %, si les prix sont rigides",
        "Les prix et la production augmentent chacun de 5 %",
        "Rien : l’équation est une identité comptable sans contenu prédictif"],
  ans=0,
  why=["La théorie quantitative suppose précisément que la production ne "
       "réagit pas : c’est le sens de la neutralité de la monnaie.",
       "Un partage entre prix et volumes supposerait que T varie, ce que "
       "l’hypothèse de stabilité exclut.",
       "MV = PT est bien une identité, mais la théorie quantitative y ajoute "
       "deux hypothèses — V et T stables — qui la rendent prédictive."],
  exp="Tout tient aux hypothèses ajoutées à l’identité : si la vitesse de "
      "circulation V et le volume des transactions T sont stables, alors "
      "toute variation de M se reporte intégralement sur P. D’où la formule "
      "de Fisher reprise par le cours : « l’inflation est un phénomène "
      "monétaire ». C’est la version formalisée de l’idée, plus ancienne, "
      "que la monnaie n’est qu’un voile — Bodin, Say, Ricardo.",
  diss="Savoir énoncer les hypothèses, et non seulement l’équation, permet de "
       "critiquer la théorie quantitative au bon endroit : c’est la stabilité "
       "de V qui est contestée."),

f(id='q2-m08', sp='c2-02', niv='raisonner', type='ordre', b=322,
  q="Remettez dans l’ordre le raisonnement de Friedman sur l’effet d’une "
    "politique monétaire expansionniste.",
  ans=["La Banque centrale augmente la quantité de monnaie : les taux "
       "baissent et le crédit devient plus facile",
       "À court terme, l’investissement et la consommation augmentent : la "
       "production progresse et le chômage recule",
       "Les prix montent et les agents, dotés d’anticipations adaptatives, "
       "apprennent de l’inflation passée",
       "Les salariés réclament des hausses de salaires et les entreprises "
       "relèvent leurs prix",
       "La production revient à son niveau initial : seule l’inflation "
       "subsiste"],
  exp="Friedman ne nie pas l’effet réel à court terme — le cours le souligne "
      "explicitement. Il affirme qu’il est instable et non durable, parce que "
      "les agents ajustent leurs anticipations à partir de l’inflation "
      "observée. La conclusion est forte : la relation entre monnaie et "
      "variables réelles est imprévisible, alors que la relation entre "
      "monnaie et prix est stable à long terme. C’est le pas qui mène à la "
      "nouvelle économie classique.",
  diss="Dérouler ces cinq temps vaut mieux que citer « la monnaie est "
       "neutre » : la neutralité est une conclusion de long terme, pas un "
       "postulat de départ."),

# ------------------------------ c2-03 · taux directeurs et canaux
f(id='q2-m09', sp='c2-03', niv='appliquer', type='ordre', b=542,
  q="Classez les trois taux directeurs de la BCE du plus bas au plus haut, "
    "tels que le corridor les ordonne.",
  ans=["Le taux de facilité de dépôt, taux plancher",
       "Le taux de refinancement, au centre du corridor",
       "Le taux de facilité de prêt, taux plafond"],
  exp="Le corridor encadre le taux du marché interbancaire. Une banque ne "
      "prêtera jamais durablement à une autre en dessous de ce qu’elle "
      "obtient sans risque en déposant à la Banque centrale : la facilité de "
      "dépôt fait plancher. Elle n’empruntera jamais au-dessus du taux auquel "
      "la Banque centrale lui prête : la facilité de prêt fait plafond. Le "
      "taux de refinancement, sur des opérations à une semaine, se situe "
      "entre les deux et constitue le taux directeur de référence.",
  diss="Le corridor montre concrètement comment une banque centrale pilote "
       "un prix — le taux — et non une quantité, ce qui rejoint la thèse de "
       "l’endogénéité de la monnaie."),

f(id='q2-m10', sp='c2-03', niv='raisonner', type='qcm', b=539,
  q="La BCE relève fortement son taux de facilité de dépôt. Quel effet le "
    "cours attend-il sur le crédit ?",
  opts=["Les banques peuvent préférer placer leurs liquidités auprès de la "
        "Banque centrale plutôt que de prêter : le crédit se restreint",
        "Les banques prêtent davantage, pour compenser la rémunération de "
        "leurs dépôts",
        "Rien : ce taux ne concerne que les relations entre banques "
        "commerciales",
        "Le crédit se restreint parce que les réserves obligatoires "
        "augmentent mécaniquement"],
  ans=0,
  why=["Un placement mieux rémunéré et sans risque rend le crédit "
       "relativement moins attractif, pas davantage.",
       "Ce taux lie chaque banque à la Banque centrale et fixe le plancher "
       "du marché interbancaire : son effet est général.",
       "Les réserves obligatoires sont un autre instrument : elles ne varient "
       "pas avec le taux de dépôt."],
  exp="Le raisonnement est un arbitrage de rendement. Prêter à l’économie "
      "rapporte un intérêt mais comporte un risque de défaut ; déposer à la "
      "Banque centrale rapporte le taux de facilité de dépôt sans risque. "
      "Relever ce taux élève donc le rendement minimal exigé de tout crédit, "
      "et en restreint le volume. C’est le premier maillon du canal des taux "
      "d’intérêt : taux ↓ → crédit ↑ → monnaie ↑ → demande ↑, et "
      "réciproquement.",
  diss="Permet d’expliquer en une phrase pourquoi la remontée des taux de "
       "2022-2023 a freiné le crédit avant même de freiner les prix."),

f(id='q2-m11', sp='c2-03', niv='appliquer', type='assoc', b=575,
  q="Associez chaque mécanisme au canal de transmission de la politique "
    "monétaire qu’il décrit.",
  ans=[["Taux ↓ → crédit ↑ → monnaie ↑ → demande ↑",
        "Le canal des taux d’intérêt"],
       ["La hausse de la valeur des actifs rend leurs détenteurs plus riches "
        "et soutient la demande", "Le canal du prix des actifs"],
       ["La banque centrale annonce l’orientation future probable de ses taux",
        "Le canal des anticipations (forward guidance)"],
       ["La variation des taux modifie la valeur externe de la monnaie et "
        "donc la compétitivité", "Le canal du taux de change"]],
  exp="Les quatre canaux ne s’excluent pas : ils agissent ensemble et "
      "expliquent pourquoi une même décision a des effets diffus. Le cours "
      "rattache l’effet richesse du canal des actifs à la logique "
      "patrimoniale de l’effet Pigou, et souligne que la forward guidance "
      "agit sans qu’aucun taux ne bouge, par la seule annonce.",
  diss="Énumérer les canaux permet de montrer qu’une politique monétaire "
       "n’agit pas seulement par le coût du crédit, et donc d’expliquer son "
       "efficacité variable selon les économies."),

# ------------------------- c2-04 · 2008, PMNC, modes de financement
f(id='q2-m12', sp='c2-04', niv='raisonner', type='qcm', b=638,
  q="Pourquoi les banques centrales ont-elles dû recourir à des politiques "
    "non conventionnelles après 2008 ?",
  opts=["Parce que les taux, ramenés près de zéro, ne pouvaient plus guère "
        "baisser : la trappe à liquidité privait l’outil conventionnel de sa "
        "marge d’action",
        "Parce que les traités européens leur interdisaient de modifier les "
        "taux directeurs",
        "Parce que l’inflation était trop élevée pour baisser les taux",
        "Parce que les banques commerciales avaient cessé d’exister"],
  ans=0,
  why=["Aucune interdiction de ce type : la contrainte est économique, c’est "
       "le plancher des taux nominaux.",
       "La période est au contraire marquée par un risque déflationniste, ce "
       "qui justifiait de soutenir la demande.",
       "Les banques ont été fragilisées, non supprimées ; la difficulté "
       "portait sur la transmission de la politique monétaire."],
  exp="Le cadre conventionnel fonctionne tant que les taux peuvent être "
      "librement ajustés. Proches de zéro, ils ne peuvent plus guère baisser, "
      "et la demande de monnaie devient très sensible : c’est la trappe à "
      "liquidité. La Banque centrale change alors de registre — elle "
      "n’agit plus seulement sur le prix de la monnaie, mais sur les bilans, "
      "les titres et les anticipations : assouplissement quantitatif, "
      "qualitatif, taux négatifs, forward guidance.",
  diss="La trappe à liquidité est l’argument keynésien classique de "
       "l’inefficacité de la politique monétaire : elle justifie le relais "
       "budgétaire."),

f(id='q2-m13', sp='c2-04', niv='appliquer', type='qcm', b=669,
  q="Une banque centrale achète des titres risqués et revend des titres sûrs, "
    "sans modifier la taille de son bilan. De quelle politique s’agit-il ?",
  opts=["D’un assouplissement qualitatif (qualitative easing)",
        "D’un assouplissement quantitatif (quantitative easing)",
        "D’une opération de refinancement classique",
        "D’une politique de réserves obligatoires"],
  ans=0,
  why=["L’assouplissement quantitatif gonfle la taille du bilan par des "
       "achats nets de titres : ici le total reste constant.",
       "Le refinancement classique passe par des prêts à court terme aux "
       "banques, contre garanties.",
       "Les réserves obligatoires portent sur ce que les banques doivent "
       "déposer, non sur la composition du bilan de la Banque centrale."],
  exp="La distinction tient en un mot : la taille ou la composition. Le "
      "quantitative easing augmente la taille du bilan en achetant des "
      "titres, le qualitative easing en modifie la composition, en prenant à "
      "son bilan des actifs plus risqués contre des actifs plus sûrs qu’elle "
      "revend. Le second transfère du risque vers la Banque centrale sans "
      "créer de monnaie supplémentaire, ce qui nourrit la critique de l’aléa "
      "moral.",
  diss="Opposer taille et composition du bilan évite la confusion entre « la "
       "BCE fait marcher la planche à billets » et « la BCE assume le "
       "risque »."),

f(id='q2-m14', sp='c2-04', niv='raisonner', type='courte', b=695,
  q="Le passage à une économie de marchés financiers signifie-t-il le recul "
    "des banques ? Argumentez.",
  ans={'modele':
       "Non, et le cours le dit expressément : l’opposition doit être "
       "nuancée. Le basculement décrit par Hicks oppose un financement "
       "indirect, où la banque s’interpose entre prêteur et emprunteur, à un "
       "financement direct par émission de titres sur les marchés. Mais les "
       "banques restent centrales : elles interviennent désormais elles-mêmes "
       "largement sur les marchés, comme émettrices, investisseuses et "
       "intermédiaires. Le passage à une économie de marchés financiers n’est "
       "donc pas la disparition du système bancaire, mais une transformation "
       "profonde des modalités de financement — la financiarisation.",
       'cles': [{'f': ['indirect'], 'l': 'financement indirect, intermédié'},
                {'f': ['direct', 'titre', 'marche'],
                 'l': 'financement direct par les titres'},
                {'f': ['banque reste', 'restent centrales', 'pas la disparition',
                       'ne disparai', 'interviennent'],
                 'l': 'les banques restent centrales et interviennent sur les marchés'},
                {'f': ['hicks'], 'l': 'le basculement décrit par Hicks'}]},
  exp="Le cours construit l’opposition — économie d’endettement contre "
      "économie de marchés financiers — puis la relativise aussitôt. C’est "
      "cette nuance qui est attendue : les deux circuits coexistent, et les "
      "banques sont devenues des acteurs de marché. Une réponse qui se "
      "contente d’opposer les deux modèles reste en deçà du texte.",
  diss="Le schéma « opposition posée puis nuancée » est exactement ce qu’on "
       "attend d’une troisième partie : on ne choisit pas un modèle contre "
       "l’autre, on montre leur articulation."),

# ------------------- c2-05 · marchés de capitaux et risque systémique
f(id='q2-m15', sp='c2-05', niv='appliquer', type='qcmm', b=812,
  q="Par quels traits le cours caractérise-t-il la globalisation financière ? "
    "(plusieurs réponses)",
  opts=["L’ouverture internationale des capitaux",
        "La déréglementation",
        "L’innovation financière",
        "La montée de nouveaux acteurs",
        "Le retour au contrôle des changes dans les pays développés"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la libre circulation des capitaux est le premier trait cité.",
       "Exacte : la levée des encadrements accompagne cette ouverture.",
       "Exacte : nouveaux produits et nouveaux montages financiers.",
       "Exacte : fonds, véhicules et intermédiaires non bancaires.",
       "Le mouvement va exactement en sens inverse : le contrôle des changes "
       "recule."],
  exp="Le cours énumère cinq traits : ouverture internationale des capitaux, "
      "déréglementation, innovation financière, montée de nouveaux acteurs, "
      "et une instabilité accrue — cette dernière étant la conséquence des "
      "quatre premières plutôt qu’un trait de même nature. Il rattache cette "
      "transformation à la « règle des 3D » par laquelle Henri Bourguinat la "
      "résume dans Les vertiges de la finance internationale (1987), puis "
      "note qu’elle s’est prolongée depuis les années 2000 par une finance "
      "plus complexe, plus globale et plus risquée.",
  diss="Énumérer ces traits permet de rattacher la crise de 2008 à un "
       "mouvement de long terme plutôt qu’à un accident, et d’éviter la "
       "copie qui fait commencer la finance mondiale en 2007."),

f(id='q2-m16', sp='c2-05', niv='raisonner', type='qcm', b=833,
  q="Pourquoi le cours parle-t-il de « finance de l’ombre » à propos du "
    "shadow banking ?",
  opts=["Parce que ces activités de financement se déroulent en dehors du "
        "système bancaire traditionnel ou à sa périphérie, donc moins "
        "visibles et parfois moins régulées",
        "Parce qu’elles sont illégales",
        "Parce qu’elles ne concernent que les paradis fiscaux",
        "Parce qu’elles portent uniquement sur des espèces"],
  ans=0,
  why=["Le shadow banking n’est pas clandestin : il est légal, mais soumis à "
       "des règles moins strictes que l’activité bancaire.",
       "La localisation offshore est une question distincte : le shadow "
       "banking se développe aussi dans les grandes places financières.",
       "Il s’agit au contraire de financements par titres et véhicules "
       "financiers, pas d’espèces."],
  exp="Le qualificatif porte sur la visibilité et la régulation, non sur la "
      "légalité. Des activités de financement équivalentes à celles des "
      "banques — transformation d’échéances, octroi de liquidité — sont "
      "exercées par des entités qui ne sont pas des banques et échappent donc "
      "aux ratios prudentiels. C’est ce qui rend la mesure du risque "
      "difficile, et nourrit l’opacité que le cours relie à la contagion de "
      "2008.",
  diss="Permet de montrer qu’une régulation produit ses propres angles "
       "morts : plus on encadre les banques, plus l’activité migre vers ce "
       "qui n’est pas une banque."),

f(id='q2-m17', sp='c2-05', niv='raisonner', type='ordre', b=861,
  q="Remettez dans l’ordre l’enchaînement qui transforme un défaut localisé "
    "en risque systémique, tel que le cours le décrit.",
  ans=["Des crédits de qualité inégale sont regroupés et découpés en titres "
       "complexes, vendus à des investisseurs du monde entier",
       "L’opacité empêche d’identifier qui détient réellement le risque",
       "Les premiers défauts dévalorisent ces titres et fragilisent leurs "
       "détenteurs",
       "La défiance se propage : chacun doute de la solidité de ses "
       "contreparties et le crédit se bloque",
       "L’effondrement d’un acteur menace l’ensemble du système : le risque "
       "devient systémique"],
  exp="Le point décisif est le deuxième : ce n’est pas le volume des pertes "
      "initiales qui crée le risque systémique, c’est l’impossibilité de "
      "savoir où elles se logent. La diffusion mondiale du risque, présentée "
      "comme un facteur de dilution, devient un facteur de contagion dès lors "
      "que l’information manque. D’où l’enchaînement : opacité, défiance, "
      "gel du crédit, contagion.",
  diss="Cet enchaînement est l’argument central contre l’idée que la "
       "dispersion du risque le réduit : elle le réduit individuellement et "
       "l’augmente collectivement."),

f(id='q2-m18', sp='c2-05', niv='appliquer', type='vf', b=749,
  q="Vrai ou faux : le service de règlement différé (SRD) permet d’acheter "
    "des titres sans disposer immédiatement des fonds, ce qui en fait un "
    "instrument de spéculation. Justifiez.",
  ans=True,
  exp="Le SRD permet de différer le règlement d’une opération boursière : "
      "l’acheteur prend position aujourd’hui et paie plus tard. Il peut donc "
      "engager des montants supérieurs à sa trésorerie, ce qui amplifie "
      "gains et pertes — c’est l’effet de levier. Le cours en fait un "
      "« outil révélateur d’une logique de marché davantage tournée vers "
      "l’anticipation et la spéculation » : la détention d’un titre n’a plus "
      "pour fin son rendement, mais la plus-value attendue à la revente.",
  diss="Le SRD, le marché à terme et la vente à découvert forment un trio "
       "utile pour montrer que les marchés financiers ne servent pas "
       "seulement à financer : ils organisent aussi le pari sur les prix."),

f(id='q2-m19', sp='c2-05', niv='raisonner', type='courte', b=720,
  q="Pour quelles raisons un agent détient-il un titre financier ? "
    "Distinguez-les et dites ce qui change selon le motif.",
  ans={'modele':
       "Le cours en distingue trois. Le rendement : on détient le titre pour "
       "le revenu qu’il procure — intérêts et coupons pour une obligation, "
       "dividendes variables selon les résultats pour une action. La "
       "plus-value : on achète dans l’espoir de revendre plus cher. La "
       "logique spéculative : l’achat n’est motivé que par l’anticipation du "
       "prix futur, à la hausse comme à la baisse. Ce qui change, c’est "
       "l’horizon et le lien au financement de l’économie : la détention "
       "pour rendement finance durablement l’émetteur, la spéculation peut "
       "au contraire accroître la volatilité sans apporter de ressources "
       "nouvelles.",
       'cles': [{'f': ['rendement', 'revenu', 'coupon', 'dividende'],
                 'l': 'le rendement : intérêts ou dividendes'},
                {'f': ['plus value', 'revendre plus cher'],
                 'l': 'la plus-value à la revente'},
                {'f': ['specul'], 'l': 'la logique spéculative'},
                {'f': ['obligation'], 'l': 'obligation : revenu fixe'},
                {'f': ['action'], 'l': 'action : revenu variable'}]},
  exp="Le cours ordonne la matière ainsi : obligations à revenus fixes "
      "contre actions à revenus variables, puis trois motifs de détention — "
      "rendement, plus-value, spéculation. La conclusion qu’il en tire est "
      "importante : l’existence de ces motifs appelle des marchés organisés, "
      "au comptant, à terme ou de gré à gré, dont la fonction excède le seul "
      "financement de l’économie.",
  diss="Hiérarchiser les motifs de détention permet de répondre à « les "
       "marchés financiers financent-ils l’économie ? » sans caricature : "
       "tout dépend de la part respective de chaque motif."),
]
