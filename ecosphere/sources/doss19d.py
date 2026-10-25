# -*- coding: utf-8 -*-
"""Ensemble 19 — La compétitivité, l’industrie et la souveraineté (4/4)."""

from doss_base import d

d('n19-subventions-production', 19, "Subventions à la production",
  "Modifier artificiellement les coûts relatifs — et déclencher la surenchère",
  "Une subvention à la production est un transfert public qui abaisse le "
  "coût d’une entreprise nationale. Le cours en donne l’enchaînement : "
  "subvention publique, donc coût de l’entreprise nationale en baisse, donc "
  "compétitivité en hausse, donc concurrence internationale modifiée. Elle "
  "constitue à la fois un instrument de politique industrielle et une forme "
  "de protectionnisme non tarifaire.",
  "Le cours traite les subventions à trois niveaux, qu’il faut distinguer. "
  "Au niveau de la justification économique d’abord : une subvention permet "
  "de corriger une externalité positive, selon le schéma externalité "
  "positive, investissement privé insuffisant, intervention publique, "
  "recherche en hausse, innovation en hausse, gains de productivité en "
  "hausse ; le soutien public à la recherche vise ainsi à rapprocher le "
  "niveau d’investissement privé du niveau socialement optimal en "
  "internalisant une partie des externalités positives produites par "
  "l’innovation. Au niveau de l’effet sur la concurrence internationale "
  "ensuite : une politique industrielle peut passer par des subventions, "
  "lesquelles peuvent modifier artificiellement les coûts relatifs entre "
  "entreprises, selon l’enchaînement subvention à une entreprise nationale, "
  "coûts relatifs en baisse, compétitivité en hausse, concurrence "
  "internationale modifiée. Le cours range d’ailleurs les subventions parmi "
  "les instruments du protectionnisme non tarifaire, aux côtés des quotas, "
  "des normes et des exigences de contenu local, et il précise que les "
  "subventions directement liées aux exportations sont notamment interdites "
  "dans le cadre de l’Organisation mondiale du commerce. Au niveau des "
  "réponses enfin : si une entreprise étrangère bénéficie de subventions "
  "publiques, elle peut disposer d’un avantage de coût artificiel, et un "
  "droit compensateur vise alors à neutraliser cet avantage, selon "
  "l’enchaînement subvention étrangère, prix artificiellement faible, droit "
  "compensateur, prix réajusté. Le cours relie également les subventions "
  "au dumping, puisqu’au sens strict il y a dumping lorsqu’un même produit "
  "est vendu moins cher à l’exportation que sur le marché intérieur du pays "
  "producteur et que cette différence résulte notamment d’un soutien "
  "destiné à favoriser artificiellement l’exportation. Mais la "
  "difficulté majeure que le cours identifie est la surenchère : Antoine "
  "Bouët montre à propos de l’Inflation Reduction Act que lorsqu’une grande "
  "puissance subventionne, ses partenaires sont incités à l’imiter, de "
  "sorte qu’une réaction en chaîne s’enclenche. Le cours confirme cette "
  "crainte au niveau général : les politiques industrielles peuvent "
  "déclencher des réactions des autres pays, provoquer une course aux "
  "subventions et accentuer la fragmentation de l’économie mondiale.",
  [("La correction d’une externalité positive",
    "Lorsqu’une activité produit des effets bénéfiques que l’investisseur ne "
    "capte pas, l’investissement privé est insuffisant : la subvention "
    "rapproche le niveau d’investissement privé du niveau socialement "
    "optimal."),
   ("La baisse du coût de l’entreprise nationale",
    "Le mécanisme direct est explicite : subvention publique, donc coût de "
    "l’entreprise nationale en baisse, donc compétitivité en hausse, donc "
    "concurrence internationale modifiée."),
   ("La modification des coûts relatifs",
    "Les subventions peuvent modifier artificiellement les coûts relatifs "
    "entre entreprises : l’avantage obtenu n’est donc pas un avantage de "
    "productivité mais un avantage de transfert, ce qui le rend contestable "
    "internationalement."),
   ("L’usage comme instrument protectionniste non tarifaire",
    "Le cours range les subventions parmi les instruments du protectionnisme "
    "non tarifaire, aux côtés des quotas, des normes et des exigences de "
    "contenu local : elles protègent sans fermer formellement la frontière."),
   ("L’interdiction des subventions à l’exportation",
    "Les subventions directement liées aux exportations sont notamment "
    "interdites dans le cadre de l’Organisation mondiale du commerce, parce "
    "qu’elles se rapprochent du dumping au sens strict."),
   ("La riposte par les droits compensateurs",
    "Si une entreprise étrangère bénéficie de subventions publiques, elle "
    "dispose d’un avantage de coût artificiel : le droit compensateur vise à "
    "le neutraliser, selon l’enchaînement subvention étrangère, prix "
    "artificiellement faible, droit compensateur, prix réajusté."),
   ("La réaction en chaîne entre puissances",
    "Lorsqu’une grande puissance subventionne, ses partenaires sont incités "
    "à l’imiter : la politique industrielle peut déclencher des réactions "
    "des autres pays, provoquer une course aux subventions et accentuer la "
    "fragmentation de l’économie mondiale.")],
  [{'a': "La subvention dispose d’une justification théorique solide "
         "lorsqu’elle corrige une externalité positive.",
    'cond': "La justification suppose le schéma du cours : externalité "
            "positive, investissement privé insuffisant, intervention "
            "publique, recherche et innovation en hausse.",
    'lim': "L’existence d’une externalité ne dit pas quel montant de "
           "subvention est optimal : le cours relève que les aides "
           "importantes produisent des effets parfois difficiles à "
           "identifier."},
   {'a': "Elle peut renverser l’issue d’un marché oligopolistique au profit d’un champion national, comme le montrent Brander et Spencer.",
    'cond': "Le renversement suppose le cadre de Brander et Spencer : marché "
            "trop étroit pour deux producteurs, coûts fixes élevés, "
            "anticipations du concurrent.",
    'lim': "Barbara Spencer insiste sur la fragilité informationnelle : "
           "l’État doit anticiper correctement les coûts, la demande et les "
           "réactions du concurrent, faute de quoi la subvention est versée "
           "sans produire le renversement attendu."},
   {'a': "Elle agit sans fermer formellement la frontière, ce qui la rend "
         "politiquement plus acceptable qu’un droit de douane.",
    'cond': "L’argument suppose que la subvention relève du protectionnisme "
            "non tarifaire, aux côtés des quotas, des normes et des "
            "exigences de contenu local.",
    'lim': "Cette discrétion a un coût budgétaire direct, là où le droit de "
           "douane procure au contraire des recettes douanières."},
   {'a': "Elle peut servir la transition écologique, en finançant les "
         "technologies encore non rentables.",
    'cond': "L’argument suppose la logique de la politique industrielle "
            "verte que le cours illustre par l’Inflation Reduction Act.",
    'lim': "Le cours relève que le verdissement ne supprime pas la logique "
           "de puissance, et que la transition peut créer une greenflation, "
           "hausse des prix liée à la transition écologique."},
   {'a': "Elle met au jour un problème de coordination internationale, par "
         "la surenchère qu’elle déclenche.",
    'cond': "Le problème suppose l’analyse d’Antoine Bouët : lorsqu’une "
            "grande puissance subventionne, ses partenaires sont incités à "
            "l’imiter.",
    'lim': "Le cours souligne que l’ampleur du déplacement des "
           "investissements reste incertaine et que l’Europe conserve des "
           "atouts propres : la surenchère n’est donc pas toujours "
           "efficace."}],
  [{'t': "Une subvention est un gaspillage d’argent public qui fausse la "
         "concurrence sans créer de valeur.",
    'qui': "La lecture libérale que le cours équilibre par la théorie des "
           "externalités.",
    'rep': "Le cours objecte qu’une externalité positive conduit à un "
           "investissement privé insuffisant, et que l’intervention publique "
           "vise à rapprocher le niveau d’investissement privé du niveau "
           "socialement optimal, ce que Arthur Pigou justifie par l’écart "
           "entre coûts privés et coûts sociaux."},
   {'t': "Puisque les subventions à l’exportation sont interdites, les États "
         "ne peuvent plus soutenir leurs producteurs.",
    'qui': "La lecture que l’étendue des instruments du cours démentit.",
    'rep': "Le cours objecte que seules les subventions directement liées "
           "aux exportations sont notamment interdites par l’Organisation "
           "mondiale du commerce, et que subsistent les subventions aux "
           "producteurs, les crédits d’impôt, les exigences de contenu "
           "local, les aides à l’investissement et à la recherche."},
   {'t': "Subventionner un champion national est une stratégie gagnante "
         "puisque la rente captée excède la subvention versée.",
    'qui': "La lecture que Barbara Spencer nuance par un argument "
           "informationnel.",
    'rep': "Le cours souligne la fragilité informationnelle du dispositif : "
           "l’État doit anticiper correctement les coûts, la demande et les "
           "réactions du concurrent ; s’il se trompe, la subvention est "
           "versée sans produire le renversement attendu et le coût reste à "
           "la charge du contribuable."},
   {'t': "Un État qui subventionne obtient durablement un avantage sur ses "
         "partenaires commerciaux.",
    'qui': "La lecture qu’Antoine Bouët corrige par la réaction en chaîne.",
    'rep': "Le cours objecte que lorsqu’une grande puissance subventionne, "
           "ses partenaires sont incités à l’imiter : il s’ensuit une "
           "surenchère, une course aux subventions et une fragmentation "
           "accrue de l’économie mondiale, de sorte que l’avantage relatif "
           "s’érode."}],
  [{'n': "Antoine Bouët",
    'i': "L’Inflation Reduction Act déclenche une réaction en chaîne de "
         "subventions industrielles.",
    'p': "Le cours en précise la portée : l’Europe conserve des atouts "
         "propres et l’ampleur du déplacement des investissements reste "
         "incertaine, mais l’épisode illustre surtout une surenchère, car "
         "lorsqu’une grande puissance subventionne, ses partenaires sont "
         "incités à l’imiter."},
   {'n': "James Brander",
    'i': "Une subvention peut déplacer la rente d’un oligopole international "
         "vers l’économie nationale.",
    'p': "Le cours en détaille le mécanisme : sur un marché mondial trop "
         "étroit pour deux producteurs à coûts fixes élevés, l’avantage du "
         "premier entrant décide de l’issue sans intervention ; une "
         "subvention publique renverse l’équilibre en rendant la production "
         "profitable quelle que soit la décision du concurrent."},
   {'n': "Barbara Spencer",
    'i': "La politique commerciale stratégique repose sur un problème "
         "d’information.",
    'p': "Le cours insiste sur cette fragilité : l’État doit anticiper "
         "correctement les coûts, la demande et les réactions du concurrent ; "
         "s’il se trompe, la subvention est versée sans produire le "
         "renversement attendu et son coût demeure."},
   {'n': "Arthur Pigou",
    'i': "L’intervention publique est légitime lorsque le marché est "
         "défaillant, notamment en présence d’externalités.",
    'p': "Le cours en tire la justification des subventions : elles "
         "corrigent, comme les taxes et la réglementation, les écarts entre "
         "coûts privés et coûts sociaux, ce qui fonde le soutien public à la "
         "recherche et à l’innovation."},
   {'n': "Philippe Aghion",
    'i': "La croissance par destruction créatrice dépend de la recherche et "
         "de la concurrence.",
    'p': "Le cours en tire des rôles précis pour l’État : le soutien à la "
         "recherche se justifie parce que le taux de croissance dépend "
         "d’innovations successives qui rendent obsolètes les technologies "
         "antérieures, ce qui fait de la subvention à la recherche un "
         "instrument de croissance et non seulement de compétitivité."}],
  [{'f': "Le schéma du cours est explicite : externalité positive, "
         "investissement privé insuffisant, intervention publique, recherche "
         "en hausse, innovation en hausse, gains de productivité en hausse.",
    'p': "Le fait établit la justification théorique de la subvention et la "
         "distingue d’un simple transfert en faveur d’une entreprise."},
   {'f': "Les subventions directement liées aux exportations sont notamment "
         "interdites dans le cadre de l’Organisation mondiale du commerce.",
    'p': "Le fait montre que le cadre multilatéral distingue les formes de "
         "soutien selon leur effet direct sur la concurrence à "
         "l’exportation."},
   {'f': "Un droit compensateur vise à neutraliser l’avantage procuré par "
         "une subvention étrangère : subvention étrangère, prix "
         "artificiellement faible, droit compensateur, prix réajusté.",
    'p': "Le fait montre que la riposte est prévue par les règles, ce qui "
         "fait de la subvention un instrument immédiatement contestable."},
   {'f': "L’État peut soutenir la recherche en finançant la recherche "
         "fondamentale, en subventionnant la recherche privée, en accordant "
         "des crédits d’impôt, en finançant des universités, en créant des "
         "centres de recherche, en développant des clusters et en protégeant "
         "temporairement les innovations par les brevets.",
    'p': "L’énumération démontre la variété des formes de soutien, et montre "
         "que la subvention directe n’en est qu’une parmi plusieurs."},
   {'f': "Les politiques industrielles peuvent déclencher des réactions des "
         "autres pays, provoquer une course aux subventions et accentuer la "
         "fragmentation de l’économie mondiale.",
    'p': "Le fait établit le coût collectif de l’instrument et explique "
         "pourquoi il nourrit la fragmentation géoéconomique."},
   {'f': "Au sens strict, il y a dumping lorsqu’un même produit est vendu "
         "moins cher à l’exportation que sur le marché intérieur du pays "
         "producteur, par exemple 22 000 euros à l’export contre 30 000 "
         "euros sur le marché national, notamment du fait d’un soutien "
         "public.",
    'p': "Le chiffrage montre le lien entre subvention et dumping, et donc "
         "pourquoi les soutiens à l’exportation sont les plus strictement "
         "encadrés."}],
  [{'q': "Sujet sur la légitimité des subventions publiques aux entreprises",
    'f': "Le cours fournit une justification précise. Lorsqu’une activité "
         "produit des effets bénéfiques que l’investisseur ne capte pas, "
         "l’investissement privé est insuffisant au regard de l’optimum "
         "social : le schéma est externalité positive, investissement privé "
         "insuffisant, intervention publique, recherche en hausse, "
         "innovation en hausse, gains de productivité en hausse. Arthur "
         "Pigou fonde cette logique en justifiant taxes, subventions ou "
         "réglementation pour corriger les écarts entre coûts privés et "
         "coûts sociaux.",
    'r': "On montre que la subvention n’est pas un transfert arbitraire mais "
         "la correction d’un écart mesurable entre rendement privé et "
         "rendement social, ce qui en fixe aussi la limite.",
    'ex': "Le crédit d’impôt recherche, qui abaisse le coût privé de la "
          "recherche et développement."},
   {'q': "Sujet sur les subventions comme instrument de concurrence "
         "internationale",
    'f': "Le cours montre que la subvention modifie artificiellement les "
         "coûts relatifs entre entreprises, selon l’enchaînement subvention "
         "à une entreprise nationale, coûts relatifs en baisse, "
         "compétitivité en hausse, concurrence internationale modifiée. Il "
         "la range donc parmi les instruments du protectionnisme non "
         "tarifaire, aux côtés des quotas, des normes et des exigences de "
         "contenu local, et il rappelle que les subventions directement "
         "liées aux exportations sont interdites par l’Organisation mondiale "
         "du commerce.",
    'r': "On montre que l’avantage obtenu est un avantage de transfert et "
         "non de productivité, ce qui le rend contestable et explique "
         "l’existence des droits compensateurs.",
    'ex': "Le droit compensateur : subvention étrangère, prix "
          "artificiellement faible, droit compensateur, prix réajusté."},
   {'q': "Sujet sur la course aux subventions entre grandes puissances",
    'f': "Le cours mobilise l’analyse d’Antoine Bouët sur l’Inflation "
         "Reduction Act. L’Europe conserve des atouts propres et l’ampleur "
         "du déplacement des investissements reste incertaine, mais "
         "l’épisode illustre surtout une surenchère : lorsqu’une grande "
         "puissance subventionne, ses partenaires sont incités à l’imiter. "
         "Le cours généralise : les politiques industrielles peuvent "
         "déclencher des réactions des autres pays, provoquer une course aux "
         "subventions et accentuer la fragmentation de l’économie mondiale.",
    'r': "On montre que l’efficacité d’une subvention s’érode lorsqu’elle "
         "est imitée, ce qui transforme un avantage individuel en coût "
         "collectif, comme dans la concurrence fiscale.",
    'ex': "Le CHIPS Act et l’Inflation Reduction Act de 2022, suivis du plan "
          "européen Made in Europe."},
   {'q': "Sujet sur les limites informationnelles de l’intervention publique",
    'f': "Le cours insiste, avec Barbara Spencer, sur la fragilité "
         "informationnelle de la politique commerciale stratégique : l’État "
         "doit anticiper correctement les coûts, la demande et les réactions "
         "du concurrent. S’il se trompe, la subvention est versée sans "
         "produire le renversement attendu et son coût reste à la charge du "
         "contribuable. Le cours relève par ailleurs le risque d’entretenir "
         "des « canards boiteux » lorsque la protection maintient "
         "artificiellement une activité non rentable.",
    'r': "On montre que la justification théorique de la subvention ne dit "
         "rien de la capacité pratique de l’État à l’appliquer, ce qui "
         "déplace le débat de la légitimité vers la compétence.",
    'ex': "Le risque des « canards boiteux » : subventions répétées, "
          "captation de rente, activité non rentable maintenue."}],
  voisins=['n19-politique-commerciale-strategique', 'n19-politique-industrielle',
           'n19-champions-nationaux', 'n18-concurrence-fiscale'])

d('n19-politique-commerciale-strategique', 19,
  "Politique commerciale stratégique",
  "Subventionner pour dissuader un concurrent d’entrer",
  "La politique commerciale stratégique, théorisée par James Brander et "
  "Barbara Spencer en 1983, consiste à utiliser l’intervention publique "
  "pour modifier stratégiquement la concurrence entre quelques grandes "
  "firmes internationales. Le cours précise que l’instrument relève en "
  "pratique largement de la politique industrielle, puisqu’il s’agit de "
  "subventionner un champion national sur un marché oligopolistique.",
  "Le cours introduit cette théorie en la distinguant des justifications "
  "précédentes du protectionnisme : Friedrich List et Nicholas Kaldor "
  "justifient la protection par la nécessité de transformer dans le temps "
  "la compétitivité d’une branche, tandis que Brander et Spencer proposent "
  "un raisonnement différent, puisqu’il ne s’agit plus seulement de "
  "protéger une industrie mais d’utiliser l’intervention publique pour "
  "modifier stratégiquement la concurrence entre quelques grandes firmes "
  "internationales. La référence est International R&D Rivalry and "
  "Industrial Strategy, de 1983, et le cours avertit que l’instrument "
  "étudié relève en pratique largement de la politique industrielle, "
  "puisqu’il s’agit de subventionner un champion national. Le raisonnement "
  "s’applique aux marchés oligopolistiques, l’exemple retenu étant Airbus "
  "contre Boeing : les deux entreprises disposent d’un pouvoir de marché et "
  "se partagent une grande partie du marché mondial. Le premier cas est "
  "celui d’un marché sans subvention. Supposons un nouveau très gros "
  "porteur, sur un marché trop petit pour permettre aux deux entreprises de "
  "produire rentablement : si les deux produisent, chacune enregistre une "
  "perte de 5 ; si aucune ne produit, les gains sont nuls ; si une seule "
  "produit, elle obtient 100 et l’autre 0. Si Boeing dispose d’une avance "
  "et entre avant Airbus, Airbus sait qu’une entrée simultanée ferait "
  "perdre les deux entreprises et préfère donc ne pas produire : Boeing "
  "obtient 100 et Airbus 0, l’avantage initial déterminant l’issue du "
  "marché. Dans un marché oligopolistique où les coûts fixes sont très "
  "élevés, l’avantage du premier entrant peut donc suffire à évincer son "
  "concurrent. Le second cas introduit la subvention. Avec une subvention "
  "de 25 accordée à Airbus, si les deux produisent Airbus obtient −5 + 25 = "
  "20 tandis que Boeing perd 5 ; si Airbus produit seule elle obtient 100 + "
  "25 = 125. Quelle que soit la décision de Boeing, Airbus a donc intérêt à "
  "produire ; anticipant une perte en cas d’entrée simultanée, Boeing peut "
  "renoncer au marché, ce qui permet à Airbus de capter la rente. La "
  "subvention transforme ainsi les décisions stratégiques des deux "
  "entreprises. Mais Barbara Spencer insiste sur la fragilité "
  "informationnelle du dispositif : l’État doit anticiper correctement les "
  "coûts, la demande et les réactions du concurrent, faute de quoi la "
  "subvention est versée sans produire le renversement attendu.",
  [("Le cadre du marché oligopolistique",
    "Le raisonnement suppose quelques grandes firmes disposant d’un pouvoir "
    "de marché et se partageant une grande partie du marché mondial, "
    "l’exemple du cours étant Airbus et Boeing dans l’aéronautique civile."),
   ("L’étroitesse du marché au regard des coûts fixes",
    "Le marché est trop petit pour permettre aux deux entreprises de "
    "produire rentablement : si les deux produisent, chacune perd 5 ; si une "
    "seule produit, elle gagne 100. C’est cette structure qui rend "
    "l’intervention efficace."),
   ("La décision par l’avantage du premier entrant",
    "Si Boeing entre avant Airbus, Airbus sait qu’une entrée simultanée "
    "ferait perdre les deux et renonce : Boeing obtient 100 et Airbus 0. "
    "L’avantage initial détermine alors l’issue du marché."),
   ("Le renversement des gains par la subvention",
    "Avec une subvention de 25, Airbus obtient 20 même si Boeing produit, et "
    "125 si elle produit seule : produire devient une stratégie dominante, "
    "indépendamment de la décision du concurrent."),
   ("La dissuasion du concurrent par anticipation",
    "Boeing, anticipant une perte de 5 en cas d’entrée simultanée face à un "
    "Airbus désormais déterminé à produire, peut renoncer au marché : la "
    "subvention agit par les anticipations plus que par le transfert."),
   ("La captation de la rente par le champion national",
    "Le résultat est qu’Airbus capte seule la rente de 125 subvention "
    "comprise, de sorte que le gain national excède le montant public "
    "engagé : c’est le ressort de l’argument."),
   ("La fragilité informationnelle du dispositif",
    "L’État doit anticiper correctement les coûts, la demande et les "
    "réactions du concurrent ; s’il se trompe, la subvention est versée sans "
    "produire le renversement attendu et son coût reste à la charge du "
    "contribuable.")],
  [{'a': "La théorie fournit un argument rigoureux en faveur de "
         "l’intervention, fondé sur la structure du marché et non sur une "
         "préférence nationale.",
    'cond': "L’argument suppose le cadre du cours : marché oligopolistique, "
            "coûts fixes très élevés, marché trop étroit pour deux "
            "producteurs rentables.",
    'lim': "Hors de ce cadre, l’argument ne vaut pas : sur un marché "
           "concurrentiel, la subvention transfère une rente sans dissuader "
           "aucun concurrent."},
   {'a': "Elle montre que la subvention agit par les anticipations du "
         "concurrent, et non seulement par la baisse du coût.",
    'cond': "L’argument suppose que le concurrent raisonne stratégiquement, "
            "anticipant une perte en cas d’entrée simultanée face à un "
            "rival déterminé à produire.",
    'lim': "Cette efficacité dépend de la crédibilité de l’engagement "
           "public : si la subvention peut être retirée, la dissuasion "
           "disparaît."},
   {'a': "Elle fait apparaître un gain national supérieur au coût public "
         "engagé, ce qui en fait un argument budgétairement défendable.",
    'cond': "Le calcul suppose les grandeurs du cours : une subvention de 25 "
            "pour une rente de 125 captée par le champion national.",
    'lim': "Ces grandeurs sont celles d’un exemple pédagogique : le cours ne "
           "prétend pas qu’elles décrivent un cas réel."},
   {'a': "Elle éclaire des épisodes industriels concrets, notamment "
         "l’existence d’un duopole aéronautique mondial.",
    'cond': "L’argument suppose que l’intervention publique ait "
            "effectivement permis l’entrée d’un second producteur sur un "
            "marché que les coûts fixes réservaient au premier.",
    'lim': "Le cours construit l’exemple pour expliquer la théorie et ne "
           "prétend pas que l’histoire d’Airbus s’y réduise."},
   {'a': "Elle est explicitement rattachée à la politique industrielle, ce "
         "qui en clarifie la nature.",
    'cond': "Le rattachement suppose l’avertissement du cours : l’instrument "
            "étudié relève en pratique largement de la politique "
            "industrielle, puisqu’il s’agit de subventionner un champion "
            "national.",
    'lim': "Cette assimilation l’expose à toutes les limites de la politique "
           "industrielle : contradictions avec les autres politiques, course "
           "aux subventions, fragmentation de l’économie mondiale."}],
  [{'t': "Une subvention à une entreprise nationale est toujours un "
         "transfert sans contrepartie pour la collectivité.",
    'qui': "La lecture que le raisonnement de Brander et Spencer conteste.",
    'rep': "Le cours montre qu’avec une subvention de 25, Airbus obtient 20 "
           "même si Boeing produit et 125 si elle produit seule : la "
           "subvention rend la production profitable quelle que soit la "
           "décision du concurrent, et la rente captée excède le transfert "
           "consenti."},
   {'t': "La politique commerciale stratégique est un argument "
         "protectionniste comme un autre, visant à protéger une industrie "
         "existante.",
    'qui': "La lecture que le cours distingue de List et Kaldor.",
    'rep': "Le cours souligne que le raisonnement est différent : il ne "
           "s’agit plus seulement de protéger une industrie mais d’utiliser "
           "l’intervention publique pour modifier stratégiquement la "
           "concurrence entre quelques grandes firmes internationales, par "
           "la subvention plutôt que par la barrière."},
   {'t': "L’avantage du premier entrant est un simple avantage de coût, qui "
         "peut être compensé par une baisse de prix.",
    'qui': "La lecture que la matrice du cours contredit.",
    'rep': "Le cours montre que l’avantage du premier entrant opère par "
           "dissuasion et non par le prix : dans un marché trop étroit pour "
           "deux producteurs, le second renonce parce qu’une entrée "
           "simultanée ferait perdre les deux, indépendamment du niveau des "
           "prix pratiqués."},
   {'t': "Si la théorie est juste, les États devraient subventionner "
         "systématiquement leurs champions sur les marchés "
         "oligopolistiques.",
    'qui': "La lecture que Barbara Spencer limite par un argument "
           "informationnel.",
    'rep': "Le cours insiste sur la fragilité informationnelle du "
           "dispositif : l’État doit anticiper correctement les coûts, la "
           "demande et les réactions du concurrent ; s’il se trompe, la "
           "subvention est versée sans produire le renversement attendu et "
           "son coût demeure."}],
  [{'n': "James Brander",
    'i': "Une subvention peut déplacer la rente d’un oligopole international "
         "vers l’économie nationale.",
    'p': "Le cours situe la référence en 1983, avec International R&D "
         "Rivalry and Industrial Strategy, et en détaille le mécanisme : sur "
         "un marché mondial trop étroit pour deux producteurs à coûts fixes "
         "élevés, l’avantage du premier entrant décide de l’issue sans "
         "intervention, et une subvention publique renverse cet équilibre."},
   {'n': "Barbara Spencer",
    'i': "La politique commerciale stratégique repose sur un problème "
         "d’information.",
    'p': "Le cours insiste sur cette fragilité informationnelle : l’État "
         "doit anticiper correctement les coûts, la demande et les réactions "
         "du concurrent ; s’il se trompe, la subvention est versée sans "
         "produire le renversement attendu et le coût reste supporté par la "
         "collectivité."},
   {'n': "Friedrich List",
    'i': "Une industrie naissante peut justifier une protection temporaire, "
         "le temps d’atteindre la compétitivité.",
    'p': "Le cours en fait l’une des justifications théoriques les plus "
         "solides du protectionnisme, le protectionnisme éducateur, et il la "
         "distingue de Brander et Spencer : List justifie la protection par "
         "la transformation de la compétitivité dans le temps, non par la "
         "modification d’un jeu stratégique."},
   {'n': "Nicholas Kaldor",
    'i': "La protection peut servir à transformer la compétitivité d’une "
         "branche dans le temps.",
    'p': "Le cours l’associe à List dans la justification temporelle de la "
         "protection : la protection temporaire peut permettre d’investir, "
         "d’innover, d’améliorer la qualité et de retrouver une "
         "compétitivité hors-prix, au risque d’entretenir des « canards "
         "boiteux » si la branche ne peut redevenir compétitive."},
   {'n': "Antoine Bouët",
    'i': "Une subvention d’une grande puissance incite ses partenaires à "
         "l’imiter.",
    'p': "Le cours en tire la limite collective de la politique commerciale "
         "stratégique : l’épisode de l’Inflation Reduction Act illustre une "
         "surenchère, et les politiques industrielles peuvent provoquer une "
         "course aux subventions qui accentue la fragmentation de "
         "l’économie mondiale."}],
  [{'f': "La référence est James Brander et Barbara Spencer, International "
         "R&D Rivalry and Industrial Strategy, 1983, et le raisonnement "
         "s’applique notamment aux marchés oligopolistiques.",
    'p': "Le fait situe précisément la théorie et en délimite le champ "
         "d’application, qui exclut les marchés concurrentiels."},
   {'f': "Dans l’exemple du cours, lorsque les deux constructeurs produisent "
         "simultanément ils enregistrent chacun une perte de 5, lorsqu’un "
         "seul produit il obtient un gain de 100, et si aucun ne produit les "
         "gains sont nuls.",
    'p': "La matrice démontre que le marché ne peut rentabiliser deux "
         "producteurs, condition sans laquelle l’argument ne tient pas."},
   {'f': "Si Boeing dispose d’une avance et entre avant Airbus, Airbus "
         "renonce et le résultat est Boeing 100, Airbus 0 : l’avantage "
         "initial détermine l’issue du marché.",
    'p': "Le fait démontre que l’avantage du premier entrant peut suffire à "
         "évincer un concurrent, ce qui justifie une intervention pour "
         "corriger l’asymétrie."},
   {'f': "Avec une subvention de 25, Airbus obtient 20 lorsque les deux "
         "produisent et 125 lorsqu’elle produit seule, tandis que Boeing "
         "perd 5 en cas d’entrée simultanée.",
    'p': "Le calcul démontre que la subvention fait de la production une "
         "stratégie dominante pour Airbus et une perspective perdante pour "
         "Boeing, qui peut donc renoncer."},
   {'f': "Le cours précise que l’instrument étudié relève en pratique "
         "largement de la politique industrielle, puisqu’il s’agit de "
         "subventionner un champion national.",
    'p': "Le fait rattache la théorie à son instrument réel et explique "
         "pourquoi elle est mobilisée dans le débat sur la politique "
         "industrielle autant que sur le commerce."},
   {'f': "Le cours range la politique commerciale stratégique parmi les "
         "arguments théoriques en faveur du protectionnisme, aux côtés des "
         "recettes fiscales, du soutien keynésien de la demande, de la "
         "réduction des dépendances, de la lutte contre la concurrence "
         "déloyale et de la protection des industries naissantes et "
         "vieillissantes.",
    'p': "Le fait situe l’argument dans une liste limitée, le cours "
         "rappelant que les arguments favorables au protectionnisme sont "
         "moins nombreux que ceux favorables au libre-échange."}],
  [{'q': "Sujet sur les arguments théoriques en faveur du protectionnisme",
    'f': "Le cours énumère les arguments possibles : recettes fiscales, "
         "soutien de la demande dans une logique keynésienne, réduction de "
         "certaines dépendances, lutte contre une concurrence jugée "
         "déloyale, protection des industries naissantes, protection "
         "temporaire d’industries vieillissantes, et politique commerciale "
         "stratégique. Il précise que ces arguments sont moins nombreux que "
         "ceux favorables au libre-échange, et que le protectionnisme "
         "éducateur constitue l’une des justifications les plus solides.",
    'r': "On montre que la politique commerciale stratégique occupe une "
         "place particulière, puisqu’elle ne protège pas une industrie mais "
         "modifie un jeu stratégique entre firmes.",
    'ex': "La distinction du cours entre List et Kaldor d’un côté, Brander "
          "et Spencer de l’autre."},
   {'q': "Sujet sur le duopole et l’intervention publique",
    'f': "Le cours construit l’exemple en deux cas. Sans subvention, sur un "
         "marché trop petit pour deux producteurs, si les deux produisent "
         "chacune perd 5 et si une seule produit elle gagne 100 : le premier "
         "entrant évince le second, qui renonce. Avec une subvention de 25 à "
         "Airbus, celle-ci obtient 20 même si Boeing produit et 125 si elle "
         "produit seule : produire devient une stratégie dominante, et "
         "Boeing, anticipant une perte, peut renoncer au marché.",
    'r': "On montre que la subvention agit en modifiant les anticipations du "
         "concurrent plutôt qu’en comblant un écart de coût, ce qui en fait "
         "un instrument de dissuasion.",
    'ex': "Le très gros porteur, marché trop étroit pour deux producteurs "
          "rentables."},
   {'q': "Sujet sur les limites de la politique commerciale stratégique",
    'f': "Le cours en identifie deux. La première est informationnelle : "
         "Barbara Spencer insiste sur le fait que l’État doit anticiper "
         "correctement les coûts, la demande et les réactions du concurrent, "
         "faute de quoi la subvention est versée sans produire le "
         "renversement attendu. La seconde est collective : Antoine Bouët "
         "montre qu’une subvention d’une grande puissance incite ses "
         "partenaires à l’imiter, d’où une course aux subventions et une "
         "fragmentation accrue de l’économie mondiale.",
    'r': "On montre que l’argument est théoriquement solide mais "
         "pratiquement fragile, ce qui invite à réserver l’instrument aux "
         "cas où la structure du marché est clairement identifiée.",
    'ex': "La réaction en chaîne déclenchée par l’Inflation Reduction Act."},
   {'q': "Sujet sur le retour des politiques industrielles",
    'f': "Le cours relie la politique commerciale stratégique au retour "
         "contemporain de la politique industrielle. Le protectionnisme "
         "contemporain ne se limite plus aux barrières douanières : avec "
         "l’Inflation Reduction Act et le CHIPS Act, les États-Unis "
         "utilisent la politique industrielle et les exigences de contenu "
         "local afin de relocaliser les productions stratégiques et de "
         "renforcer leur autonomie technologique. Le raisonnement de "
         "Brander et Spencer en fournit la justification théorique.",
    'r': "On montre que la subvention est devenue l’instrument principal du "
         "protectionnisme contemporain, ce qui transforme la concurrence "
         "commerciale en concurrence budgétaire entre États.",
    'ex': "Les exigences de contenu local de l’Inflation Reduction Act et du "
          "CHIPS Act."}],
  voisins=['n19-subventions-production', 'n19-champions-nationaux',
           'n19-politique-industrielle', 'n16-economies-echelle'])

d('n19-souverainete-economique', 19, "Souveraineté économique",
  "Conserver une capacité de décision sans dépendance excessive",
  "La souveraineté économique consiste, selon le cours, à conserver une "
  "capacité de décision et d’action sans dépendance extérieure excessive. "
  "Elle se distingue du protectionnisme, qui protège le marché intérieur, et "
  "de l’autarcie : un pays peut maintenir des importations tout en restant "
  "relativement souverain s’il dispose de plusieurs fournisseurs.",
  "Le cours construit la souveraineté économique par une double "
  "distinction. La première l’oppose au protectionnisme : celui-ci a pour "
  "objectif de protéger la production et les emplois domestiques contre la "
  "concurrence étrangère, par des droits de douane, des quotas, des normes "
  "et des restrictions commerciales, tandis que la souveraineté a pour "
  "objectif de conserver une capacité de décision et d’action sans "
  "dépendance extérieure excessive. Autrement dit, protectionnisme égale "
  "protéger le marché intérieur, souveraineté égale éviter une dépendance "
  "jugée dangereuse. La seconde distinction l’oppose à l’autarcie : un pays "
  "peut maintenir des importations tout en étant relativement souverain s’il "
  "dispose de plusieurs fournisseurs, de sorte que souveraineté n’égale pas "
  "autarcie. Le cours formule l’idée avec précision : la souveraineté ne "
  "signifie pas l’autosuffisance, elle consiste à empêcher qu’une "
  "dépendance particulière devienne suffisamment forte pour qu’un "
  "fournisseur étranger puisse contraindre les choix économiques ou "
  "politiques d’un pays. Un pays totalement souverain serait capable de "
  "prendre ses décisions sans contrainte extérieure, mais dans une économie "
  "mondialisée l’indépendance absolue est irréaliste, d’où le recours à une "
  "notion plus nuancée, celle d’autonomie stratégique. Le cours écarte "
  "ensuite une fausse solution : vouloir produire absolument tout soi-même "
  "serait une erreur, car une souveraineté absolue conduirait à l’autarcie "
  "et ferait perdre les gains de spécialisation, les économies d’échelle, "
  "la diversité des fournisseurs et les avantages comparatifs. Emmanuel "
  "Combe et Sarah Guillou dénoncent sur ce point le « mythe du potager », "
  "la croyance qu’un pays serait plus sûr simplement parce qu’il produit "
  "tout lui-même : un choc domestique peut lui aussi détruire la "
  "production, qu’il s’agisse d’une catastrophe naturelle, d’une grève, "
  "d’une crise énergétique ou d’un problème sanitaire, de sorte qu’un seul "
  "fournisseur national constitue un risque autant qu’un seul fournisseur "
  "étranger ; la diversification géographique des fournisseurs peut donc "
  "offrir davantage de résilience que la concentration de toute la "
  "production sur le territoire national. Le cours en déduit une pluralité "
  "d’instruments : produire davantage sur le territoire, diversifier les "
  "fournisseurs, constituer des stocks, recycler, développer des substituts "
  "technologiques, organiser des approvisionnements avec des pays alliés. "
  "La relocalisation n’est donc qu’un instrument parmi plusieurs.",
  [("La distinction d’avec le protectionnisme",
    "Le protectionnisme vise à protéger la production et les emplois "
    "domestiques contre la concurrence étrangère ; la souveraineté vise à "
    "conserver une capacité de décision et d’action sans dépendance "
    "extérieure excessive. Les objectifs diffèrent."),
   ("La distinction d’avec l’autarcie",
    "Un pays peut maintenir des importations tout en étant relativement "
    "souverain s’il dispose de plusieurs fournisseurs : ce qui compte est la "
    "structure de l’approvisionnement et non son volume."),
   ("Le critère de la contrainte possible",
    "La souveraineté consiste à empêcher qu’une dépendance particulière "
    "devienne suffisamment forte pour qu’un fournisseur étranger puisse "
    "contraindre les choix économiques ou politiques d’un pays."),
   ("Le passage à l’autonomie stratégique",
    "Un pays totalement souverain prendrait ses décisions sans contrainte "
    "extérieure, mais l’indépendance absolue est irréaliste dans une "
    "économie mondialisée, d’où une notion plus relative, l’autonomie "
    "stratégique."),
   ("L’écartement de l’autosuffisance",
    "Une souveraineté absolue conduirait à l’autarcie et ferait perdre les "
    "gains de spécialisation, les économies d’échelle, la diversité des "
    "fournisseurs et les avantages comparatifs : l’autosuffisance est donc "
    "contre-productive."),
   ("La réfutation du « mythe du potager »",
    "Un choc domestique peut aussi détruire la production — catastrophe "
    "naturelle, grève, crise énergétique, problème sanitaire — de sorte qu’un "
    "seul fournisseur national constitue un risque au même titre qu’un seul "
    "fournisseur étranger."),
   ("La combinaison des leviers",
    "Pour réduire une dépendance, le cours énumère six stratégies : "
    "réindustrialiser, diversifier les fournisseurs, constituer des stocks, "
    "recycler, développer des substituts technologiques, s’approvisionner "
    "auprès de pays alliés.")],
  [{'a': "La notion se distingue nettement du protectionnisme, ce qui évite "
         "de confondre deux objectifs poursuivis avec des instruments "
         "voisins.",
    'cond': "La distinction suppose la définition du cours : le "
            "protectionnisme protège le marché intérieur, la souveraineté "
            "évite une dépendance jugée dangereuse.",
    'lim': "Les instruments étant souvent identiques, la souveraineté peut "
           "servir de justification commode à un protectionnisme ordinaire."},
   {'a': "Elle se mesure à la structure de l’approvisionnement et non à son "
         "volume, ce qui en fait un critère opératoire.",
    'cond': "Le critère suppose l’exemple du cours : un pays peut maintenir "
            "des importations tout en restant relativement souverain s’il "
            "dispose de plusieurs fournisseurs.",
    'lim': "Pour les matières premières critiques, la concentration mondiale "
           "du traitement rend la diversification difficile à court terme : "
           "il n’existe pas toujours de second fournisseur."},
   {'a': "Elle écarte explicitement l’autarcie comme solution, ce qui préserve les gains que procure l’ouverture internationale.",
    'cond': "L’argument suppose la réfutation du cours : une souveraineté "
            "absolue ferait perdre les gains de spécialisation, les "
            "économies d’échelle, la diversité des fournisseurs et les "
            "avantages comparatifs.",
    'lim': "Le cours ne fixe pas le seuil au-delà duquel une dépendance "
           "devient dangereuse, ce qui laisse la frontière entre ouverture "
           "et vulnérabilité à l’appréciation politique."},
   {'a': "Elle débouche sur une pluralité d’instruments, ce qui élargit la "
         "politique de souveraineté bien au-delà de la relocalisation.",
    'cond': "La pluralité suppose les six leviers du cours : production "
            "nationale, diversification, stocks, recyclage, substituts "
            "technologiques, approvisionnements auprès d’alliés.",
    'lim': "Le cours ne hiérarchise pas ces leviers ni n’en précise les "
           "coûts respectifs, ce qui rend l’arbitrage entre eux "
           "indéterminé."},
   {'a': "Elle intègre la critique du « mythe du potager », ce qui la "
         "protège d’une dérive autarcique.",
    'cond': "L’argument suppose la démonstration d’Emmanuel Combe et Sarah "
            "Guillou : un choc domestique peut aussi détruire la production.",
    'lim': "Cette critique vaut pour la production mais pas pour la "
           "coercition : un fournisseur national ne peut pas, lui, imposer "
           "des choix politiques au pays."}],
  [{'t': "La souveraineté économique suppose de produire sur le territoire "
         "national l’essentiel de ce que l’on consomme.",
    'qui': "La lecture que le cours écarte en distinguant souveraineté et "
           "autarcie.",
    'rep': "Le cours répond que la souveraineté ne signifie pas "
           "l’autosuffisance : elle consiste à empêcher qu’une dépendance "
           "particulière devienne suffisamment forte pour qu’un fournisseur "
           "étranger puisse contraindre les choix économiques ou politiques "
           "d’un pays, un pays pouvant maintenir des importations s’il "
           "dispose de plusieurs fournisseurs."},
   {'t': "Produire soi-même est toujours plus sûr que de dépendre d’un fournisseur étranger, quel que soit le secteur concerné.",
    'qui': "Le « mythe du potager » dénoncé par Emmanuel Combe et Sarah "
           "Guillou.",
    'rep': "Le cours objecte qu’un choc domestique peut lui aussi détruire "
           "la production — catastrophe naturelle, grève, crise énergétique, "
           "problème sanitaire — et que la diversification géographique des "
           "fournisseurs peut offrir davantage de résilience que la "
           "concentration de toute la production sur le territoire national."},
   {'t': "Souveraineté et protectionnisme sont une seule et même chose, "
         "puisqu’ils recourent aux mêmes instruments.",
    'qui': "La confusion que le cours corrige par la distinction des "
           "objectifs.",
    'rep': "Le cours distingue les finalités : le protectionnisme protège la "
           "production et les emplois domestiques contre la concurrence "
           "étrangère, la souveraineté évite une dépendance jugée "
           "dangereuse. Un pays peut être souverain tout en important "
           "largement, et protectionniste sans être souverain."},
   {'t': "Puisque l’indépendance absolue est irréaliste, la souveraineté "
         "économique est une notion vide dans une économie mondialisée.",
    'qui': "La lecture que le cours écarte en introduisant l’autonomie "
           "stratégique.",
    'rep': "Le cours répond en substituant à l’indépendance totale une "
           "notion plus relative : l’autonomie stratégique, qui consiste à "
           "poursuivre ses intérêts sans être isolé, sans chercher "
           "l’autarcie, mais sans dépendances indésirables ni contraintes "
           "excessives."}],
  [{'n': "Emmanuel Combe",
    'i': "Croire qu’un pays est plus sûr parce qu’il produit tout lui-même "
         "relève du « mythe du potager ».",
    'p': "Le cours en détaille la réfutation : une souveraineté absolue "
         "conduirait à l’autarcie et ferait perdre les gains de "
         "spécialisation, les économies d’échelle, la diversité des "
         "fournisseurs et les avantages comparatifs, alors qu’un choc "
         "domestique peut lui aussi détruire la production."},
   {'n': "Sarah Guillou",
    'i': "La localisation d’une production est désormais évaluée non "
         "seulement par son coût mais par le risque géopolitique de la "
         "dépendance.",
    'p': "Le cours parle à ce propos d’une « nouvelle obsession » de la "
         "souveraineté industrielle, apparue depuis 2020, et il en tire la "
         "conséquence pour les politiques publiques : la diversification "
         "géographique des fournisseurs peut offrir davantage de résilience "
         "que la concentration nationale."},
   {'n': "John Maynard Keynes",
    'i': "L’interdépendance n’est pas toujours synonyme de sécurité "
         "lorsqu’elle porte sur des activités essentielles.",
    'p': "Le cours situe cette intuition dès 1933 et la présente comme "
         "annonçant les débats contemporains sur la souveraineté, "
         "l’autonomie stratégique, la sécurité économique et les secteurs "
         "stratégiques, selon la chaîne ouverture, interdépendance, "
         "dépendance potentielle, vulnérabilité."},
   {'n': "Dani Rodrik",
    'i': "Hypermondialisation, souveraineté nationale et démocratie ne "
         "peuvent être poursuivies simultanément.",
    'p': "Le cours en donne l’application économique : la mobilité du "
         "capital accroît la concurrence fiscale et réduit la capacité de "
         "taxation nationale, de sorte que préserver souveraineté et "
         "démocratie suppose de limiter l’hypermondialisation, solution que "
         "Rodrik rapproche du compromis de Bretton Woods."}],
  [{'f': "Le cours oppose les deux objectifs : protectionnisme égale "
         "protéger le marché intérieur, souveraineté égale éviter une "
         "dépendance jugée dangereuse.",
    'p': "La formule établit la distinction conceptuelle sur laquelle repose "
         "tout le raisonnement, et évite de confondre deux politiques aux "
         "instruments voisins."},
   {'f': "Un pays peut maintenir des importations tout en étant relativement "
         "souverain s’il dispose de plusieurs fournisseurs : souveraineté "
         "n’égale donc pas autarcie.",
    'p': "Le fait démontre que la souveraineté se mesure à la structure de "
         "l’approvisionnement et non à son volume, ce qui déplace la "
         "question de la fermeture vers la diversification."},
   {'f': "Emmanuel Combe et Sarah Guillou dénoncent le « mythe du potager » : "
         "un choc domestique peut aussi détruire la production, qu’il "
         "s’agisse d’une catastrophe naturelle, d’une grève, d’une crise "
         "énergétique ou d’un problème sanitaire.",
    'p': "Le fait démontre qu’un seul fournisseur national constitue un "
         "risque au même titre qu’un seul fournisseur étranger, ce qui "
         "disqualifie l’autosuffisance comme solution de sécurité."},
   {'f': "Pour réduire une dépendance, le cours énumère six stratégies : "
         "produire davantage sur le territoire, diversifier les "
         "fournisseurs, constituer des stocks, recycler, développer des "
         "substituts technologiques, organiser des approvisionnements avec "
         "des pays alliés.",
    'p': "L’énumération démontre que la relocalisation n’est qu’un "
         "instrument parmi plusieurs, ce qui élargit considérablement la "
         "politique de souveraineté."},
   {'f': "Le cours relie la souveraineté à l’économie numérique : la "
         "maîtrise des infrastructures, semi-conducteurs, énergie et métaux "
         "rares conditionne la souveraineté économique, la compétitivité et "
         "la puissance géopolitique.",
    'p': "Le fait montre que la souveraineté économique concerne aussi les "
         "secteurs réputés immatériels, puisque l’économie numérique "
         "renforce les dépendances matérielles."},
   {'f': "Le cours formule la problématique du chapitre sur les firmes et "
         "les États : comment concilier efficacité économique et "
         "souveraineté, quitte parfois à accepter des coûts plus élevés ?",
    'p': "La formulation montre que la souveraineté économique est posée "
         "comme un arbitrage et non comme un objectif gratuit."}],
  [{'q': "Sujet sur la souveraineté économique dans une économie ouverte",
    'f': "Le cours impose deux distinctions. La souveraineté n’est pas le "
         "protectionnisme : celui-ci protège la production et les emplois "
         "domestiques contre la concurrence étrangère, celle-là conserve une "
         "capacité de décision et d’action sans dépendance extérieure "
         "excessive. Et la souveraineté n’est pas l’autarcie : un pays peut "
         "maintenir des importations tout en restant relativement souverain "
         "s’il dispose de plusieurs fournisseurs, puisque l’enjeu est "
         "d’empêcher qu’une dépendance devienne un instrument de contrainte.",
    'r': "On montre que la souveraineté se mesure à la structure de "
         "l’approvisionnement et non à son volume, ce qui déplace la "
         "question de la fermeture vers la diversification.",
    'ex': "L’autonomie stratégique européenne : ni isolement, ni autarcie, "
          "mais pas de dépendances indésirables ni de contraintes "
          "excessives."},
   {'q': "Sujet sur les limites de l’autosuffisance comme stratégie de "
         "sécurité",
    'f': "Le cours écarte explicitement cette voie. Vouloir produire "
         "absolument tout soi-même serait une erreur, car une souveraineté "
         "absolue conduirait à l’autarcie et ferait perdre les gains de "
         "spécialisation, les économies d’échelle, la diversité des "
         "fournisseurs et les avantages comparatifs. Emmanuel Combe et Sarah "
         "Guillou dénoncent le « mythe du potager » : un choc domestique "
         "peut lui aussi détruire la production, de sorte qu’un seul "
         "fournisseur national est un risque autant qu’un seul fournisseur "
         "étranger.",
    'r': "On montre que la sécurité d’approvisionnement est un problème de "
         "diversification du risque et non de localisation, ce qui "
         "disqualifie la réponse par la production nationale généralisée.",
    'ex': "Les chocs domestiques cités : catastrophe naturelle, grève, crise "
          "énergétique, problème sanitaire."},
   {'q': "Sujet sur l’arbitrage entre efficacité et souveraineté",
    'f': "Le cours en fait la problématique de son chapitre sur les firmes "
         "et les États : le défi contemporain consiste à concilier "
         "l’efficacité recherchée par les firmes à travers "
         "l’internationalisation de la production avec la volonté des États "
         "de préserver leur souveraineté économique et industrielle, quitte "
         "parfois à accepter des coûts plus élevés. La fragmentation produit "
         "l’efficacité ; la souveraineté exige une maîtrise que cette "
         "fragmentation défait.",
    'r': "On montre que la souveraineté se paie en efficacité, ce qui "
         "transforme la question en arbitrage explicite et impose de limiter "
         "la protection aux dépendances réellement dangereuses.",
    'ex': "La logique de résilience : accepter parfois un coût économique "
          "supérieur pour réduire une dépendance risquée."},
   {'q': "Sujet sur la souveraineté et la mondialisation financière",
    'f': "Le cours mobilise Dani Rodrik. On ne peut pas poursuivre "
         "simultanément hypermondialisation, souveraineté nationale et "
         "démocratie, parce que la mobilité du capital accroît la "
         "concurrence fiscale et réduit la capacité de taxation nationale. "
         "Préserver souveraineté et démocratie suppose donc de limiter "
         "l’hypermondialisation, solution que Rodrik rapproche du compromis "
         "de Bretton Woods, où l’ouverture reste importante mais où les "
         "États conservent des marges de manœuvre.",
    'r': "On montre que la souveraineté économique est entamée par la "
         "mobilité du capital autant que par la dépendance productive, ce "
         "qui en élargit la portée au-delà des seules chaînes "
         "d’approvisionnement.",
    'ex': "L’enchaînement du cours : mobilité du capital en hausse, "
          "concurrence fiscale en hausse, capacité de taxation nationale en "
          "baisse."}],
  voisins=['n19-autonomie-strategique', 'n17-dependances-strategiques',
           'n19-industries-strategiques', 'n18-rapports-firmes-etats'])

d('n19-autonomie-strategique', 19, "Autonomie stratégique",
  "La version relative de la souveraineté retenue au niveau européen",
  "L’autonomie stratégique est la conception relative de la souveraineté "
  "que le cours attribue à l’Union européenne : poursuivre ses intérêts "
  "sans être isolée, sans chercher l’autarcie, mais sans « dépendances "
  "indésirables » ni « contraintes excessives ». Elle remplace l’objectif "
  "d’indépendance totale par celui de réduction des dépendances "
  "dangereuses.",
  "Le cours introduit l’autonomie stratégique comme la réponse à une "
  "impossibilité. Un pays totalement souverain serait capable de prendre "
  "ses décisions sans contrainte extérieure, mais dans une économie "
  "mondialisée l’indépendance absolue est irréaliste : d’où une notion plus "
  "nuancée, l’autonomie stratégique, et c’est précisément cette conception "
  "plus relative de la souveraineté qui est privilégiée au niveau européen. "
  "L’Union européenne défend l’idée de pouvoir poursuivre ses intérêts sans "
  "être isolée, sans chercher l’autarcie, mais sans « dépendances "
  "indésirables » ni « contraintes excessives ». Le cours insiste sur le "
  "caractère essentiel de cette définition : elle remplace l’indépendance "
  "totale par la réduction des dépendances dangereuses. L’autonomie "
  "stratégique européenne ne vise donc pas l’autarcie mais la maîtrise des "
  "interdépendances, l’objectif étant de rester ouvert au commerce tout en "
  "évitant qu’une dépendance trop concentrée devienne un instrument de "
  "coercition. Le vocabulaire de la politique industrielle a d’ailleurs "
  "changé depuis 2020 : on parle de plus en plus de souveraineté, "
  "d’autonomie stratégique, de sécurité économique, de résilience, de "
  "relocalisation, de nearshoring et de friendshoring, et cette nouvelle "
  "logique rompt avec l’hypermondialisation. Pendant plusieurs décennies "
  "l’objectif était de localiser chaque étape de production là où elle "
  "était la plus efficace ; désormais une autre question apparaît : "
  "peut-on accepter qu’un bien essentiel soit produit presque exclusivement "
  "dans un pays avec lequel une crise est possible ? Le cours décline "
  "ensuite l’autonomie stratégique en objectifs industriels concrets. Le "
  "premier objectif de la réindustrialisation est de retrouver l’autonomie "
  "stratégique, c’est-à-dire de produire sur le territoire européen des "
  "biens critiques en santé, défense, numérique, énergie, batteries et "
  "semi-conducteurs, l’exemple typique étant les batteries de véhicules "
  "électriques, puisque si l’Europe dépend de la Chine et que celle-ci "
  "bloque, l’Europe est coincée ; Mario Draghi s’inscrit dans cette "
  "logique, en identifiant la compétitivité européenne à la capacité de "
  "produire les biens stratégiques. Le cours observe enfin que la "
  "dépendance européenne ne concerne pas seulement la Chine, puisqu’il "
  "relève aussi la domination américaine dans l’intelligence artificielle "
  "et le caractère stratégique de ce retard, et il conclut que la "
  "souveraineté est nécessairement relative.",
  [("Le constat d’irréalisme de l’indépendance absolue",
    "Un pays totalement souverain prendrait ses décisions sans contrainte "
    "extérieure, mais dans une économie mondialisée l’indépendance absolue "
    "est irréaliste : il faut donc une notion plus relative."),
   ("La formule européenne en quatre termes",
    "L’Union européenne défend l’idée de poursuivre ses intérêts sans être "
    "isolée, sans chercher l’autarcie, mais sans « dépendances "
    "indésirables » ni « contraintes excessives »."),
   ("Le remplacement de l’objectif",
    "La définition remplace l’indépendance totale par la réduction des "
    "dépendances dangereuses : le critère n’est plus l’absence de "
    "dépendance mais son caractère maîtrisé."),
   ("La maîtrise des interdépendances",
    "L’objectif est de rester ouvert au commerce tout en évitant qu’une "
    "dépendance trop concentrée devienne un instrument de coercition : "
    "l’ouverture est maintenue, la concentration est combattue."),
   ("Le changement de vocabulaire depuis 2020",
    "On parle de plus en plus de souveraineté, d’autonomie stratégique, de "
    "sécurité économique, de résilience, de relocalisation, de nearshoring "
    "et de friendshoring : cette logique rompt avec l’hypermondialisation."),
   ("Le renversement du critère de localisation",
    "Pendant des décennies l’objectif était de localiser chaque étape là où "
    "elle était la plus efficace ; désormais la question est de savoir si "
    "l’on peut accepter qu’un bien essentiel soit produit presque "
    "exclusivement dans un pays avec lequel une crise est possible."),
   ("La déclinaison industrielle",
    "Le premier objectif de la réindustrialisation est de retrouver "
    "l’autonomie stratégique, en produisant sur le territoire européen des "
    "biens critiques en santé, défense, numérique, énergie, batteries et "
    "semi-conducteurs.")],
  [{'a': "La notion résout l’impasse de l’indépendance absolue en proposant "
         "un objectif atteignable.",
    'cond': "L’argument suppose le constat du cours : dans une économie "
            "mondialisée, l’indépendance absolue est irréaliste.",
    'lim': "Le caractère relatif rend l’objectif difficile à évaluer : le "
           "cours ne dit pas à partir de quand une dépendance devient "
           "« indésirable »."},
   {'a': "Elle maintient l’ouverture commerciale, ce qui préserve les gains de spécialisation et les économies d’échelle.",
    'cond': "La préservation suppose la formule européenne : poursuivre ses "
            "intérêts sans être isolée et sans chercher l’autarcie.",
    'lim': "Rester ouvert tout en évitant la coercition exige une capacité "
           "de filtrage et de contrôle dont le coût administratif et "
           "diplomatique n’est pas chiffré."},
   {'a': "Elle vise la concentration plutôt que le volume des importations, "
         "ce qui en fait un critère précis.",
    'cond': "Le critère suppose l’objectif du cours : éviter qu’une "
            "dépendance trop concentrée devienne un instrument de "
            "coercition.",
    'lim': "Pour les matières premières critiques, la concentration mondiale "
           "du traitement rend la diversification difficile, ce qui limite "
           "l’applicabilité du critère."},
   {'a': "Elle se décline en objectifs industriels identifiables et sectoriels, ce qui la rend réellement opérationnelle.",
    'cond': "La déclinaison suppose la liste des biens critiques du cours : "
            "santé, défense, numérique, énergie, batteries, "
            "semi-conducteurs.",
    'lim': "Le cours relève un décalage de temps : la politique "
           "industrielle européenne se heurte à l’écart entre le temps long "
           "de l’investissement et la rapidité de l’expansion des "
           "concurrents."},
   {'a': "Elle oblige à considérer toutes les dépendances, et pas seulement "
         "celles envers un adversaire désigné.",
    'cond': "L’argument suppose le constat du cours : la dépendance "
            "européenne ne concerne pas seulement la Chine, le retard dans "
            "l’intelligence artificielle étant également stratégique.",
    'lim': "Multiplier les fronts dilue les moyens : le cours souligne par "
           "ailleurs qu’une politique industrielle doit rester sélective."}],
  [{'t': "L’autonomie stratégique est une autarcie déguisée, puisqu’elle "
         "vise à produire sur place.",
    'qui': "La lecture que la définition européenne du cours réfute.",
    'rep': "Le cours objecte que l’Union européenne défend l’idée de "
           "poursuivre ses intérêts sans être isolée et sans chercher "
           "l’autarcie, et que l’autonomie stratégique ne vise pas "
           "l’autarcie mais la maîtrise des interdépendances, l’objectif "
           "étant de rester ouvert au commerce."},
   {'t': "Puisque la souveraineté absolue est impossible, la notion "
         "d’autonomie stratégique n’a pas de contenu opérationnel.",
    'qui': "La lecture que le cours écarte en détaillant les biens "
           "critiques.",
    'rep': "Le cours lui donne un contenu précis : produire sur le "
           "territoire européen des biens critiques en santé, défense, "
           "numérique, énergie, batteries et semi-conducteurs, avec des "
           "critères de sélection par l’importance du produit et la "
           "vulnérabilité de l’approvisionnement."},
   {'t': "L’enjeu de l’autonomie stratégique européenne se réduit à la dépendance envers la Chine et ses exportations.",
    'qui': "La lecture que le cours élargit.",
    'rep': "Le cours observe que la dépendance européenne ne concerne pas "
           "seulement la Chine, et il relève la domination américaine dans "
           "l’intelligence artificielle ainsi que le caractère stratégique "
           "de ce retard : l’autonomie stratégique se joue sur plusieurs "
           "fronts simultanément."},
   {'t': "Rechercher l’autonomie stratégique est sans risque, puisqu’il "
         "s’agit seulement de se protéger.",
    'qui': "La lecture que le paradoxe de la fragmentation contredit.",
    'rep': "Le cours montre qu’en cherchant à réduire leurs interdépendances "
           "pour diminuer leurs vulnérabilités, les États réduisent "
           "simultanément le coût économique d’un éventuel conflit : la "
           "recherche individuelle de sécurité économique peut donc "
           "contribuer collectivement à accroître l’insécurité "
           "géopolitique."}],
  [{'n': "Mario Draghi",
    'i': "La compétitivité européenne se confond avec la capacité à produire "
         "les biens stratégiques.",
    'p': "Le cours l’inscrit dans le premier objectif de la "
         "réindustrialisation, retrouver l’autonomie stratégique, et "
         "l’illustre par les batteries de véhicules électriques : si "
         "l’Europe dépend de la Chine pour ces composants et que celle-ci "
         "bloque les livraisons, l’Europe se retrouve coincée."},
   {'n': "Sarah Guillou",
    'i': "Depuis 2020, la localisation d’une production est évaluée non "
         "seulement par son coût mais par le risque géopolitique de la "
         "dépendance.",
    'p': "Le cours parle d’une « nouvelle obsession » de la souveraineté "
         "industrielle et en donne le symptôme lexical : on parle désormais "
         "de souveraineté, d’autonomie stratégique, de sécurité économique, "
         "de résilience, de relocalisation, de nearshoring et de "
         "friendshoring."},
   {'n': "Emmanuel Combe",
    'i': "Le « mythe du potager » consiste à croire qu’un pays est plus sûr "
         "parce qu’il produit tout lui-même.",
    'p': "Le cours en tire la justification du caractère relatif de "
         "l’autonomie stratégique : la diversification géographique des "
         "fournisseurs peut offrir davantage de résilience que la "
         "concentration de toute la production sur le territoire national."},
   {'n': "Janet Yellen",
    'i': "Le friendshoring consiste à privilégier les pays considérés comme "
         "politiquement fiables.",
    'p': "Le cours en fait l’un des instruments de l’autonomie stratégique, "
         "aux côtés de la relocalisation et du nearshoring, tout en "
         "soulignant la fragilité de son hypothèse : les alliances peuvent "
         "changer, et un pays fiable aujourd’hui ne l’est pas "
         "nécessairement demain."}],
  [{'f': "L’Union européenne défend l’idée de pouvoir poursuivre ses "
         "intérêts sans être isolée, sans chercher l’autarcie, mais sans "
         "« dépendances indésirables » ni « contraintes excessives ».",
    'p': "La formule constitue la définition de référence et montre que "
         "l’objectif retenu est la maîtrise des dépendances et non leur "
         "suppression."},
   {'f': "Depuis 2020, le vocabulaire de la politique industrielle change : "
         "on parle de souveraineté, d’autonomie stratégique, de sécurité "
         "économique, de résilience, de relocalisation, de nearshoring et de "
         "friendshoring.",
    'p': "Le fait date le basculement doctrinal et montre que la rupture "
         "avec l’hypermondialisation s’exprime d’abord dans les mots."},
   {'f': "Pendant plusieurs décennies, l’objectif était de localiser chaque "
         "étape de production là où elle était la plus efficace ; désormais "
         "la question est de savoir si l’on peut accepter qu’un bien "
         "essentiel soit produit presque exclusivement dans un pays avec "
         "lequel une crise est possible.",
    'p': "Le fait démontre le renversement du critère de localisation, de "
         "l’efficacité vers la sécurité d’approvisionnement."},
   {'f': "Le premier objectif de la réindustrialisation est de produire sur "
         "le territoire européen des biens critiques en santé, défense, "
         "numérique, énergie, batteries et semi-conducteurs.",
    'p': "L’énumération donne le contenu industriel concret de l’autonomie "
         "stratégique et montre qu’elle est sélective par construction."},
   {'f': "La dépendance européenne ne concerne pas seulement la Chine : le "
         "cours relève la domination américaine dans l’intelligence "
         "artificielle et le caractère stratégique de ce retard.",
    'p': "Le fait élargit la notion : l’autonomie stratégique se joue sur "
         "plusieurs fronts simultanément, y compris envers des alliés."},
   {'f': "La politique industrielle européenne cherche à reconstruire une "
         "chaîne de valeur autonome de la batterie, mais elle se heurte au "
         "décalage entre le temps long de l’investissement industriel et la "
         "rapidité de l’expansion concurrente, la mine de lithium de "
         "l’Allier n’atteignant son plein fonctionnement que vers 2030.",
    'p': "Le fait montre la principale contrainte de l’autonomie "
         "stratégique : le temps, pendant lequel l’avance du concurrent se "
         "maintient."}],
  [{'q': "Sujet sur l’autonomie stratégique européenne",
    'f': "Le cours en donne la définition de référence. Un pays totalement "
         "souverain prendrait ses décisions sans contrainte extérieure, mais "
         "l’indépendance absolue est irréaliste dans une économie "
         "mondialisée, d’où une notion plus nuancée. L’Union européenne "
         "défend l’idée de poursuivre ses intérêts sans être isolée, sans "
         "chercher l’autarcie, mais sans « dépendances indésirables » ni "
         "« contraintes excessives » : la définition remplace "
         "l’indépendance totale par la réduction des dépendances "
         "dangereuses.",
    'r': "On montre que l’objectif retenu est la maîtrise des "
         "interdépendances et non leur suppression, ce qui permet de "
         "concilier ouverture commerciale et sécurité d’approvisionnement.",
    'ex': "La formule du cours : rester ouvert au commerce tout en évitant "
          "qu’une dépendance trop concentrée devienne un instrument de "
          "coercition."},
   {'q': "Sujet sur le changement de doctrine de la politique industrielle",
    'f': "Le cours date le basculement de 2020. Le vocabulaire change : on "
         "parle de plus en plus de souveraineté, d’autonomie stratégique, de "
         "sécurité économique, de résilience, de relocalisation, de "
         "nearshoring et de friendshoring, et cette logique rompt avec "
         "l’hypermondialisation. Pendant plusieurs décennies l’objectif "
         "était de localiser chaque étape là où elle était la plus "
         "efficace ; désormais la question devient celle du risque attaché à "
         "une production presque exclusivement étrangère.",
    'r': "On montre que le critère de localisation s’est déplacé de "
         "l’efficacité vers la sécurité, ce qui redéfinit la rationalité des "
         "choix productifs.",
    'ex': "La question du cours : peut-on accepter qu’un bien essentiel soit "
          "produit presque exclusivement dans un pays avec lequel une crise "
          "est possible ?"},
   {'q': "Sujet sur les instruments de l’autonomie stratégique",
    'f': "Le cours en énumère six : produire davantage sur le territoire, "
         "diversifier les fournisseurs, constituer des stocks, recycler, "
         "développer des substituts technologiques, organiser des "
         "approvisionnements avec des pays alliés. La relocalisation n’est "
         "donc qu’un instrument parmi plusieurs, et le friendshoring, "
         "expression popularisée par Janet Yellen, repose sur une hypothèse "
         "fragile, puisque les alliances peuvent changer et qu’un pays "
         "fiable aujourd’hui ne l’est pas nécessairement demain.",
    'r': "On montre que l’autonomie stratégique est un problème de "
         "diversification du risque, ce qui en élargit la palette bien "
         "au-delà du retour de la production nationale.",
    'ex': "La fragilité du friendshoring : identifier durablement les "
          "partenaires sur lesquels compter."},
   {'q': "Sujet sur les limites de la recherche d’autonomie",
    'f': "Le cours en identifie deux. La contrainte de temps d’abord : la "
         "politique industrielle européenne cherche à reconstruire une "
         "chaîne de valeur autonome de la batterie mais se heurte au "
         "décalage entre le temps long de l’investissement industriel et la "
         "rapidité de l’expansion concurrente, la mine de lithium de "
         "l’Allier n’atteignant son plein fonctionnement que vers 2030. Le "
         "paradoxe de la fragmentation ensuite : en réduisant leurs "
         "interdépendances, les États diminuent le coût économique d’un "
         "conflit.",
    'r': "On montre que la recherche d’autonomie est à la fois lente et "
         "potentiellement déstabilisatrice, ce qui impose de la limiter aux "
         "dépendances réellement dangereuses.",
    'ex': "La recherche individuelle de sécurité économique contribuant "
          "collectivement à accroître l’insécurité géopolitique."}],
  voisins=['n19-souverainete-economique', 'n17-dependances-strategiques',
           'n19-reindustrialisation', 'n17-fragmentation-geoeconomique'])
