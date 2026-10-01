"""Macroéconomie (économie ouverte) — cours rédigés pour être compris (style Écosphère), d'après les
5 documents de notes : MACRO_R (balance des paiements), MACRO_R2 (marché des changes, régimes de change),
MACRO_3-1 (taux de change réel, Marshall-Lerner, PTINC), MACRO_R4 (modèle IS-LM-PTINC) et
MACRO_R5 (politiques économiques, triangle d'incompatibilité)."""
from lib import Cours


def ch1():
    c = Cours()
    c.intro("De quoi parle ce chapitre ?",
            "Un pays n'est pas une île : il vend et achète des biens à l'étranger, y place son épargne, y emprunte. "
            "La <b>balance des paiements</b> est le tableau qui enregistre tous ces échanges sur une année. Elle sert de point de départ à tout le cours : "
            "les chapitres suivants expliquent ce qui fait bouger ses soldes (le taux de change, les taux d'intérêt, la politique économique).",
            ["Qu'enregistre la balance des paiements, et comment ?", "Pourquoi est-elle toujours équilibrée ?",
             "Que signifie un déficit ou un excédent courant ?", "Qu'est-ce que la position extérieure nette d'un pays ?",
             "Comment relier le compte courant à l'épargne et à la dépense nationale ?"])

    c.sec("I. Définition et grands comptes")
    c.idee("La balance des paiements est la <b>comptabilité d'un pays face au reste du monde (RDM)</b>. Chaque opération entre un résident et un non-résident y est inscrite.")
    c.df("Balance des paiements", "Document comptable qui enregistre toutes les opérations effectuées entre les résidents d'un pays et les non-résidents au cours d'une année donnée ; elle est toujours exprimée en monnaie nationale.")
    c.df("Résident", "Agent (ménage, entreprise, administration) installé sur le territoire depuis plus d'un an, quelle que soit sa nationalité.")
    c.df("Non-résident (RDM)", "Agent installé hors du territoire ; l'ensemble des non-résidents forme le reste du monde (RDM).")
    c.autrement("ce n'est pas la nationalité qui compte mais le lieu de vie. Un Américain qui vit à Paris depuis trois ans est un résident français ; ses achats en France ne passent pas par la balance des paiements.")
    c.p("La balance des paiements comporte <b>quatre grands comptes</b> :")
    c.tab(["Compte", "Ce qu'il enregistre", "Exemples"], [
        ["<b>Compte courant (CC)</b>", "Les échanges de biens et services et les revenus", "Exportations d'Airbus, tourisme, dividendes, contribution au budget européen"],
        ["<b>Compte de capital (CK)</b>", "Les transferts de capital sans contrepartie", "Remise ou annulation de dette, achat ou vente de brevets"],
        ["<b>Compte financier (CF)</b>", "Les variations d'avoirs et d'engagements financiers sur l'étranger", "IDE, achats d'actions et d'obligations, prêts bancaires, réserves de change"],
        ["<b>Erreurs et omissions (EO)</b>", "Le solde de ce qui n'a pas pu être enregistré correctement", "Opérations oubliées ou connues seulement après le 31/12"]])

    c.h3("1. Le compte courant : quatre postes")
    c.df("Poste des biens", "Exportations et importations de marchandises ; son solde est la balance commerciale.")
    c.df("Poste des services", "Exportations et importations de services : tourisme, transport, conseil, assurance… ; son solde est la balance des services.")
    c.df("Revenus primaires", "Revenus des facteurs de production reçus du RDM ou versés au RDM : salaires des travailleurs frontaliers, dividendes, intérêts sur prêts ou obligations.")
    c.df("Revenus secondaires", "Transferts courants sans contrepartie : contribution au budget européen ou au FMI, dons publics aux pays en développement, envois de fonds des travailleurs émigrés et immigrés.")
    c.f("Balance commerciale = X biens − M biens · Balance des services = X services − M services")
    c.f("Compte courant (balance des opérations courantes) = biens + services + revenus primaires + revenus secondaires")
    c.pourquoi("Pourquoi les dividendes reçus de l'étranger sont-ils dans le compte courant et pas dans le compte financier ?",
               "Parce que ce sont des <b>revenus</b> : la rémunération d'un placement passé, comme un salaire rémunère un travail. "
               "L'achat de l'action, lui, est une opération financière (compte financier) ; le dividende qu'elle rapporte chaque année est un revenu primaire (compte courant).")

    c.h3("2. Le compte de capital")
    c.p("Il est en général petit. Il enregistre les <b>transferts en capital</b> (remises de dette) et l'achat ou la vente d'actifs non financiers non produits, comme les brevets.")

    c.h3("3. Le compte financier : avoirs et engagements")
    c.idee("Le compte financier dit <b>sous quelle forme</b> le pays a fait varier sa richesse sur l'étranger : comptes bancaires, actions, obligations, prêts, réserves de la banque centrale.")
    c.df("Avoirs", "Créances des résidents sur le RDM : ce que nous possédons à l'étranger (comptes bancaires, actions, obligations, prêts accordés).")
    c.df("Engagements", "Dettes des résidents envers le RDM : ce que les non-résidents possèdent chez nous.")
    c.p("Cinq postes :")
    c.df("Investissements directs étrangers (IDE)", "Achats d'actions donnant au moins 10 % du capital d'une entreprise, dans un but durable (moyen-long terme) et non spéculatif ; IDE entrant quand un non-résident investit chez nous, sortant quand un résident investit à l'étranger.")
    c.df("Investissements de portefeuille", "Achats ou ventes d'actions (moins de 10 % du capital), d'obligations ou de bons du Trésor dans un but de placement ; les obligations sont toujours des investissements de portefeuille.")
    c.df("Produits financiers dérivés", "Opérations sur options, contrats à terme, stock-options ; elles concernent surtout les économies développées.")
    c.df("Autres investissements", "Prêts et emprunts bancaires avec le RDM et tout ce qui n'entre pas dans les autres postes.")
    c.df("Avoirs de réserve", "Actifs extérieurs détenus par la banque centrale (or, devises, titres étrangers) ; ils varient quand elle achète ou vend des devises.")
    c.pas("Les prêts bancaires, côté avoirs et côté engagements", [
        "Une banque française prête à un non-résident : la dette du RDM envers nous augmente, nos <b>avoirs</b> augmentent.",
        "Une banque française emprunte à une banque étrangère : notre dette envers le RDM augmente, nos <b>engagements</b> augmentent.",
        "Au 31/12, on calcule la variation des avoirs nets = variation des avoirs − variation des engagements."],
        "Si la variation des avoirs nets est négative, le pays a plus emprunté à l'étranger qu'il n'a prêté.")
    c.f("Solde du compte financier : CF = Δ avoirs − Δ engagements")

    c.h3("4. L'équation fondamentale")
    c.f("CC + CK − CF + EO = 0")
    c.autrement("ce que le pays gagne (ou perd) avec le reste du monde sur ses opérations courantes et en capital se retrouve forcément dans la variation de sa richesse financière sur l'étranger. "
                "Si CK et EO sont nuls : <b>CC = CF</b>.")
    c.retenir(["Quatre comptes : CC, CK, CF, EO.", "CC = biens + services + revenus primaires + revenus secondaires.", "CF = Δ avoirs − Δ engagements.", "CC + CK − CF + EO = 0 ; si CK = EO = 0, CC = CF."])
    c.transition("Pourquoi cette égalité est-elle toujours vraie ? À cause de la comptabilité en partie double.")

    c.sec("II. Le double enregistrement : chaque opération apparaît deux fois")
    c.idee("Comme en comptabilité d'entreprise, chaque transaction avec le RDM est inscrite <b>deux fois</b> : une fois au compte courant (l'échange), une fois au compte financier (le paiement).")
    c.df("Partie double (balance des paiements)", "Principe selon lequel chaque transaction courante est enregistrée une fois dans le compte courant et une fois, en contrepartie, dans le compte financier ; la balance des paiements est donc toujours équilibrée.")
    c.pas("Une exportation de X € vers les États-Unis", [
        "Compte courant : +X au <b>crédit</b> du poste des biens.",
        "L'exportateur est payé en dollars : il détient un dépôt bancaire aux États-Unis. Les <b>avoirs</b> de la France à l'étranger augmentent de X.",
        "Il peut garder ces dollars, les vendre à sa banque contre des euros (la banque détient alors l'avoir, il reste en France), ou les placer aux États-Unis en actions ou obligations (l'avoir change de forme)."],
        "Dans tous les cas, la richesse de la France sur l'étranger a augmenté : c'est une <b>sortie de capitaux</b> (la France prête au RDM).")
    c.pas("Une importation de X €", [
        "Compte courant : X au <b>débit</b> du poste des biens.",
        "Pour payer, l'importateur utilise un compte en dollars s'il en a un : ses avoirs baissent.",
        "Sinon, il achète des dollars à sa banque. Si la banque a des dollars aux États-Unis, elle les prélève (avoirs ↓). Si elle n'en a pas assez, elle se tourne vers la banque centrale, qui puise dans ses réserves (avoirs de réserve ↓). Si la banque centrale refuse, la banque doit vendre des titres (avoirs ↓) ou emprunter aux États-Unis (engagements ↑)."],
        "Dans tous les cas, la richesse nette de la France sur l'étranger diminue : c'est une <b>entrée de capitaux</b> qui finance l'importation.")
    c.pourquoi("Pourquoi un excédent courant correspond-il à une « sortie » de capitaux ?",
               "Le mot surprend, mais il faut le lire du point de vue du financement : le pays exportateur a été payé en avoirs sur l'étranger. "
               "Il a donc <b>prêté</b> au reste du monde, puisqu'il détient des créances sur lui. Les capitaux sortent du pays vers l'étranger sous forme de placements. "
               "À l'inverse, un déficit courant doit être financé par l'étranger : des capitaux entrent.")
    c.tab(["Situation", "Compte courant", "Compte financier", "Richesse nette sur l'étranger", "Capitaux"], [
        ["X > M", "Excédent", "Δ avoirs > Δ engagements : CF > 0", "↑", "Sortie"],
        ["X < M", "Déficit", "Δ avoirs < Δ engagements : CF < 0", "↓", "Entrée"]])
    c.h3("Que faire d'un excédent ? Comment financer un déficit ?")
    c.ul(["<b>Excédent</b> : le pays détient des avoirs bancaires à l'étranger. Il peut les <b>conserver</b> ou les <b>placer</b> (actions, obligations), ce qui rapportera plus tard des revenus primaires.",
          "<b>Déficit</b> : le pays manque de devises. Il peut <b>vendre des actifs</b> étrangers (avoirs ↓), <b>emprunter</b> à des banques étrangères (engagements ↑) ou <b>vendre des entreprises</b> à des non-résidents (IDE entrant : engagements ↑)."])
    c.retenir(["Chaque opération est enregistrée deux fois : CC et CF.", "Excédent courant ⇒ avoirs nets ↑ ⇒ sortie de capitaux.", "Déficit courant ⇒ avoirs nets ↓ ou engagements ↑ ⇒ entrée de capitaux."])
    c.transition("Le compte financier dit comment la richesse extérieure a varié pendant l'année. Mais quel est son niveau ? C'est la position extérieure nette.")

    c.sec("III. La position extérieure nette (PEN)")
    c.df("Position extérieure nette (PEN)", "À une date donnée, différence entre les avoirs des résidents sur le RDM et leurs engagements envers lui ; c'est le stock de richesse nette du pays sur l'étranger, cumul de toutes les variations passées.")
    c.autrement("le compte financier est un <b>flux</b> (ce qui a changé pendant l'année), la PEN est un <b>stock</b> (ce que le pays possède net à une date). C'est la différence entre un salaire du mois et le solde du compte en banque.")
    c.f("PEN(t) = PEN(t − 1) + CF(t) + effets de valorisation (prix des titres, taux de change)")
    c.ul(["<b>PEN négative</b> : dettes > avoirs. Le pays est en <b>endettement extérieur net</b> ; il a plus emprunté qu'investi (États-Unis, Royaume-Uni).",
          "<b>PEN positive</b> : avoirs > dettes. Le pays a une <b>richesse extérieure nette</b> ; il a plus prêté qu'emprunté (pays pétroliers, Chine, Allemagne)."])
    c.h3("De quoi dépend la PEN ?")
    c.ul(["Du <b>cumul des comptes courants et financiers passés</b> : vingt ans d'excédents courants donnent une PEN positive.", "De l'<b>évolution du prix des titres</b> détenus ou émis.", "De l'<b>évolution du taux de change</b>, qui modifie la valeur en monnaie nationale des avoirs et des engagements."])
    c.pas("L'exemple des États-Unis", [
        "Début des années 1980 : la PEN est positive, mais le compte courant devient déficitaire.",
        "Pour financer ce déficit, le pays « puise » dans sa PEN : elle baisse chaque année.",
        "Le déficit persiste : la PEN finit par devenir négative."],
        "Les États-Unis passent d'une richesse extérieure nette à une situation d'endettement extérieur net.")
    c.retenir(["PEN = avoirs − engagements à une date (stock).", "Elle varie avec le CF, le prix des titres et le change.", "PEN < 0 : endettement extérieur net ; PEN > 0 : richesse extérieure nette."])

    c.sec("IV. La balance globale (BG)")
    c.idee("On sépare dans le compte financier ce que font les agents privés (CFHAR) et ce que fait la <b>banque centrale</b> (variation des avoirs de réserve). La balance globale mesure ce qui reste à la charge de la banque centrale.")
    c.df("CFHAR", "Compte financier hors avoirs de réserve : opérations des ménages, des entreprises, des banques commerciales et des autres résidents.")
    c.df("Balance globale (BG)", "BG = CC + CK − CFHAR ; solde des opérations des agents privés, qui doit être compensé par la variation des avoirs de réserve de la banque centrale.")
    c.f("CF = CFHAR + Δ avoirs de réserve")
    c.pas("De l'équation fondamentale à la balance globale", [
        "On part de CC + CK − CF + EO = 0.",
        "On remplace CF : CC + CK − CFHAR − Δ AR + EO = 0.",
        "On pose BG = CC + CK − CFHAR : BG − Δ AR + EO = 0.",
        "Si EO = 0 : <b>BG = Δ AR</b>."])
    c.tab(["BG", "Avoirs de réserve", "Interprétation"], [
        ["BG = +X (excédent)", "Δ AR = +X", "Les réserves officielles augmentent de X : la banque centrale a accumulé des devises."],
        ["BG = −Y (déficit)", "Δ AR = −Y", "La banque centrale a dû puiser dans ses réserves pour financer le déficit."],
        ["BG = 0", "Δ AR = 0", "Aucun changement des réserves."]])
    c.pourquoi("Pourquoi peut-on déduire le signe de la BG en regardant seulement les réserves de change ?",
               "Parce que les deux se compensent exactement (aux erreurs et omissions près). Si les agents privés ont, au total, fait entrer plus de devises qu'ils n'en ont fait sortir, "
               "ces devises finissent à la banque centrale : ses réserves augmentent. Une hausse des réserves signale donc une BG excédentaire.")
    c.retenir(["BG = CC + CK − CFHAR.", "BG = Δ avoirs de réserve (si EO = 0).", "BG > 0 ⇒ réserves ↑ ; BG < 0 ⇒ réserves ↓."])
    c.transition("Reste à comprendre ce que révèle un déficit courant sur l'économie nationale. Deux lectures sont possibles : par la dépense (absorption) et par l'épargne.")

    c.sec("V. Interpréter le compte courant : absorption et épargne")
    c.h3("1. Première lecture : l'absorption")
    c.p("En économie fermée, PIB = C + I + G. En économie ouverte, les ressources (PIB + importations) égalent les emplois (C + I + G + exportations) :")
    c.f("PIB + M = C + I + G + X ⇒ PIB = C + I + G + (X − M)")
    c.p("On ajoute les revenus primaires et secondaires nets des deux côtés pour faire apparaître le revenu national (le PNB du cours) et le compte courant :")
    c.f("PNB = PIB + revenus primaires nets + revenus secondaires nets ⇒ PNB = C + I + G + CC")
    c.df("Absorption (A)", "Demande intérieure globale : A = C + I + G ; c'est ce que les résidents dépensent en biens et services.")
    c.f("PNB = A + CC ⇔ CC = PNB − A")
    c.idee("Un pays en <b>déficit courant</b> dépense plus qu'il ne gagne (A > PNB). Un pays en <b>excédent</b> dépense moins qu'il ne gagne (A < PNB).")
    c.ul(["PNB > PIB : le pays reçoit plus de revenus du RDM qu'il n'en verse ; en général sa PEN est positive (il a beaucoup investi à l'étranger).",
          "PNB < PIB : le pays verse plus de revenus qu'il n'en reçoit ; en général sa PEN est négative et il est très endetté.",
          "Exception : les États-Unis ont une PEN négative mais PNB > PIB. Ils empruntent à taux faible (leur dette est jugée sûre) et placent à l'étranger dans des actifs risqués qui rapportent plus."])
    c.pourquoi("Pourquoi réduire un déficit courant coûte-t-il en croissance et en emploi ?",
               "Puisque CC = PNB − A, pour revenir à l'équilibre il faut baisser l'absorption : moins de consommation, d'investissement ou de dépenses publiques. "
               "Moins de demande, c'est moins de production et d'emplois. C'est pourquoi on souligne aussi la responsabilité des pays en excédent durable : si certains sont en déficit, c'est que d'autres sont en excédent.")
    c.h3("2. Deuxième lecture : l'épargne")
    c.p("Le revenu national sert à consommer, épargner et payer les impôts : PNB = C + S + T. On l'égalise avec PNB = C + I + G + CC :")
    c.f("C + S + T = C + I + G + CC ⇒ CC = (S − I) + (T − G)")
    c.df("Épargne privée nette (S − I)", "Excédent de l'épargne des ménages et des entreprises sur l'investissement.")
    c.df("Épargne publique (T − G)", "Excédent budgétaire ; positive quand T > G, elle sert à l'État à se désendetter ; négative, c'est un déficit public.")
    c.df("Épargne nationale", "Somme de l'épargne privée et de l'épargne publique ; quand elle dépasse l'investissement, le surplus est placé à l'étranger (excédent courant, sortie de capitaux, PEN ↑).")
    c.autrement("un déficit courant signifie que le pays n'épargne pas assez pour financer son propre investissement : il emprunte l'épargne du reste du monde. Ce manque d'épargne peut venir du privé (S < I) ou de l'État (déficit public).")
    c.warn("Avec un déficit public (T − G < 0), le compte courant se dégrade sauf si l'épargne privée augmente d'autant : c'est l'idée des « déficits jumeaux » (budget et compte courant).")
    c.retenir(["Absorption : CC = PNB − A. Déficit courant = le pays dépense plus qu'il ne gagne.", "Épargne : CC = (S − I) + (T − G). Déficit courant = épargne nationale insuffisante.", "Les deux lectures disent la même chose sous deux angles."])
    c.synthese(["La balance des paiements enregistre en partie double les opérations avec le RDM : CC + CK − CF + EO = 0.",
                "Excédent courant = sortie de capitaux = hausse de la richesse sur l'étranger (et inversement).",
                "La PEN est le stock de richesse nette sur l'étranger ; le CF en est le flux annuel.",
                "BG = CC + CK − CFHAR = Δ avoirs de réserve : la banque centrale absorbe le solde des opérations privées.",
                "CC = PNB − A = (S − I) + (T − G)."])
    return c


def ch2():
    c = Cours()
    c.intro("De quoi parle ce chapitre ?",
            "Pour payer une importation américaine, il faut des dollars. Les monnaies s'échangent donc entre elles sur un marché, à un prix : le <b>taux de change</b>. "
            "Ce chapitre explique comment ce prix se fixe, et ce qui change selon que l'État laisse faire le marché (<b>change flexible</b>) ou défend une parité (<b>change fixe</b>).",
            ["Qu'est-ce qu'un taux de change et comment le lire ?", "Comment fonctionne le marché des changes ?",
             "Que se passe-t-il en change flexible quand l'offre ou la demande d'une monnaie change ?", "Comment la banque centrale défend-elle une parité fixe, et jusqu'où peut-elle le faire ?",
             "Comment un déséquilibre de la balance globale se corrige-t-il selon le régime de change ?"])

    c.sec("I. Le taux de change et le marché des changes")
    c.df("Taux de change", "Prix d'une monnaie exprimé en une autre monnaie ; 1 € = 1,5 $ signifie qu'un euro vaut 1,5 dollar.")
    c.df("Marché des changes", "Marché mondial où l'on échange une monnaie contre une autre ; il fixe les taux de change.")
    c.df("Taux de change nominal", "Nombre d'unités de monnaie étrangère obtenues avec une unité de monnaie nationale (ou l'inverse) : « avec 1 €, combien de dollars ? ».")
    c.df("Appréciation", "Hausse du prix d'une monnaie en termes d'une autre ; elle résulte d'une demande excédentaire de cette monnaie.")
    c.df("Dépréciation", "Baisse du prix d'une monnaie en termes d'une autre ; elle résulte d'une offre excédentaire de cette monnaie.")
    c.p("Le taux de change dépend de l'offre et de la demande de monnaie (et de titres) dans les pays concernés, et de l'offre et de la demande de ces monnaies dans le monde entier.")
    c.h3("Deux façons de coter")
    c.df("Cotation au certain", "Une unité de monnaie nationale exprimée en monnaie étrangère : 1 € = 0,8 $ (notation officielle ISO : 1 EUR = 0,8000 USD).")
    c.df("Cotation à l'incertain", "Une unité de monnaie étrangère exprimée en monnaie nationale : 1 $ = 1/0,8 = 1,25 €.")
    c.f("Cotation à l'incertain = 1 / cotation au certain")
    c.df("PIP", "Quatrième décimale d'un taux de change (les taux sont cotés à 4 décimales) ; « l'euro s'est déprécié de 5 PIP » signifie que la 4ᵉ décimale a baissé de 5.")
    c.warn("Dans la suite du cours, <b>e</b> désigne le prix d'une unité de monnaie étrangère en monnaie nationale (cotation à l'incertain : 1 $ = e €). Une <b>hausse de e</b> est donc une <b>dépréciation</b> de la monnaie nationale. Vérifie toujours la convention au début d'un sujet.")
    c.h3("Cours acheteur, cours vendeur, spread")
    c.df("Cours d'achat (bid)", "Prix auquel le marché (banques, agents de change) achète 1 €, donc prix auquel le public vend 1 €.")
    c.df("Cours de vente (offer)", "Prix auquel le marché vend 1 €, donc prix auquel le public achète 1 €.")
    c.df("Spread", "Écart entre le cours de vente et le cours d'achat ; c'est la marge bénéficiaire des intermédiaires.")
    c.pas("Exemple : EUR/USD coté 1,1248 / 1,1252", [
        "Tu vends 10 000 € à la banque : elle te les achète au cours d'achat, 1,1248 → 11 248 $.",
        "Tu rachètes aussitôt des euros avec ces 11 248 $ : la banque te vend l'euro au cours de vente, 1,1252 → 11 248 / 1,1252 ≈ 9 996,44 €."],
        "Tu as perdu environ 3,56 € : c'est le spread de 4 PIP, la rémunération de la banque.")
    c.h3("Un marché géant et concentré")
    c.ul(["Volume quotidien d'environ <b>18 fois le PIB mondial quotidien</b> et 72 fois le commerce mondial quotidien.", "Ouvert 24 h/24 (sauf jours fériés) grâce au décalage horaire.",
          "Très concentré : environ 40 % des transactions à Londres et 20 % à New York, avec un petit nombre de grandes banques."])
    c.h3("Pourquoi échange-t-on des devises ?")
    c.ul(["Pour régler des <b>exportations et importations</b>, des revenus et des transferts (opérations du compte courant).", "Pour <b>spéculer</b> : parier sur l'évolution d'un taux (toujours risqué).",
          "Pour se <b>couvrir</b> contre le risque de change.", "Pour faire de l'<b>arbitrage</b> : profiter d'écarts de prix entre places."])
    c.retenir(["Taux de change = prix d'une monnaie dans une autre.", "Certain : 1 € = x $ ; incertain : 1 $ = 1/x €.", "Bid < offer ; l'écart est le spread.", "Demande excédentaire → appréciation ; offre excédentaire → dépréciation."])
    c.transition("Comment ce prix évolue-t-il ? Tout dépend du régime de change.")

    c.sec("II. Le change flexible : le marché fixe le prix")
    c.df("Régime de change flexible", "Régime où le taux de change est déterminé librement par l'offre et la demande sur le marché des changes, sans intervention de la banque centrale.")
    c.idee("Le marché des changes fonctionne comme n'importe quel marché du chapitre 0 de micro : un excès d'offre d'une monnaie fait baisser son prix, un excès de demande le fait monter.")
    c.pas("Les exportations françaises vers les États-Unis augmentent", [
        "Les importateurs américains doivent payer en euros : ils vendent des dollars contre des euros.",
        "Offre excédentaire de dollars et demande excédentaire d'euros.",
        "Le prix du dollar en euros baisse (le dollar se déprécie) et le prix de l'euro en dollars monte (l'euro s'apprécie)."])
    c.pourquoi("Pourquoi le marché finit-il par revenir à l'équilibre ?",
               "Quand le dollar baisse, les biens américains deviennent moins chers en euros : on en importe plus, on emprunte, investit ou spécule davantage en dollars. La demande de dollars (et l'offre d'euros) augmente. "
               "De plus, les détenteurs de dollars préfèrent les garder en attendant une remontée : l'offre de dollars ralentit. Ces deux forces stoppent la baisse : on revient à l'équilibre.")
    c.p("Comme en micro, il faut distinguer :")
    c.ul(["<b>Déplacement des courbes</b> : il est provoqué par un changement autre que le taux de change (hausse des exportations françaises, qui déplace l'offre de dollars et la demande d'euros).",
          "<b>Déplacement le long des courbes</b> : il est provoqué par la variation du taux de change lui-même."])
    c.retenir(["Change flexible : pas d'intervention de la banque centrale.", "Le taux de change s'ajuste et ramène le marché à l'équilibre."])

    c.sec("III. Le change fixe : la banque centrale défend une parité")
    c.df("Régime de change fixe", "Régime où des pays se mettent d'accord sur une parité (taux de change officiel) que les banques centrales défendent en achetant ou vendant des devises avec leurs réserves officielles.")
    c.df("Réserves officielles (de change)", "Actifs que la banque centrale détient à l'étranger (devises, or, titres) et qu'elle utilise pour intervenir sur le marché des changes.")
    c.pas("Exemple du cours : parité entre l'euro et le mark (DM), les exportations françaises vers l'Allemagne augmentent", [
        "Les Allemands échangent des DM contre des euros : offre excédentaire de DM, demande excédentaire d'euros. L'euro devrait s'apprécier.",
        "Pour l'en empêcher, la banque centrale <b>achète les DM</b> en trop et <b>vend des euros</b>, qu'elle crée.",
        "Ces euros répondent à la demande excédentaire : le marché revient à l'équilibre à la parité."],
        "Résultat : les réserves de la banque centrale en DM augmentent et la masse monétaire en euros augmente (seule la banque centrale peut créer ou détruire des euros).")
    c.h3("Deux limites à la défense d'une parité")
    c.ul(["<b>L'épuisement des réserves</b> (dans le cas inverse, quand il faut vendre des devises pour soutenir sa monnaie) : au bout d'un moment, la banque centrale n'a plus de DM. Elle ne peut plus défendre la parité. Si la Bundesbank refuse de lui en prêter, une nouvelle parité s'impose : <b>dévaluation</b> de l'euro et <b>réévaluation</b> du DM.",
          "<b>L'effet sur la masse monétaire</b> : quand la banque centrale rachète sa propre monnaie, la masse monétaire baisse, les taux d'intérêt montent, l'investissement et la consommation reculent. En chômage keynésien, la production baisse et le chômage augmente : <b>récession</b>."])
    c.df("Dévaluation", "Baisse officielle de la parité d'une monnaie dans un régime de change fixe (à distinguer de la dépréciation, qui se fait par le marché).")
    c.df("Réévaluation", "Hausse officielle de la parité d'une monnaie dans un régime de change fixe.")
    c.retenir(["Change fixe : la banque centrale achète ou vend des devises pour tenir la parité.", "Elle fait varier ses réserves et sa masse monétaire.", "Limites : épuisement des réserves (dévaluation) et effets récessifs de la baisse de la masse monétaire."])

    c.sec("IV. Interpréter un déséquilibre de la balance globale selon le régime")
    c.h3("Cas 1 : BG excédentaire (CC excédentaire et CFHAR < CC)")
    c.p("Le pays n'a pas réinvesti à l'étranger tous ses gains : il a un excès d'avoirs en dollars. Les agents rapatrient ces dollars et les échangent contre des euros : <b>offre excédentaire de dollars, demande excédentaire d'euros</b>. Ni le marché des changes ni la BG ne sont à l'équilibre.")
    c.tab(["", "Change flexible", "Change fixe"], [
        ["Réaction", "Le dollar se déprécie, l'euro s'apprécie, sans intervention", "La BCE achète les dollars en trop contre des euros qu'elle crée"],
        ["Conséquences", "Retour à l'équilibre du marché des changes et de la BG", "Réserves en dollars ↑, masse monétaire en euros ↑ ; le marché des changes est équilibré, mais pas encore la BG"],
        ["Type d'équilibre", "Stationnaire (grâce au taux de change)", "Temporaire, puis stationnaire : Ms ↑ ⇒ i ↓ ⇒ sorties de capitaux ⇒ la BG se rééquilibre"]])
    c.h3("Cas 2 : BG déficitaire (CC déficitaire et CFHAR > CC)")
    c.p("Le pays n'a pas réussi à financer tout son déficit : il manque de dollars pour payer ses achats. <b>Offre excédentaire d'euros, demande excédentaire de dollars.</b>")
    c.tab(["", "Change flexible", "Change fixe"], [
        ["Réaction", "L'euro se déprécie, le dollar s'apprécie", "La BCE vend des dollars de ses réserves et rachète des euros"],
        ["Conséquences", "Retour à l'équilibre sur les deux marchés", "Réserves en dollars ↓, masse monétaire ↓ ; si elle intervient trop, ses réserves s'épuisent"],
        ["Type d'équilibre", "Stationnaire", "Temporaire, puis stationnaire : Ms ↓ ⇒ i ↑ ⇒ entrées de capitaux ⇒ la BG se rééquilibre"]])
    c.pourquoi("Pourquoi, en change fixe, la variation de la masse monétaire finit-elle par rééquilibrer la BG ?",
               "Parce qu'elle change les taux d'intérêt. Quand la BCE crée des euros (BG excédentaire), les taux baissent : placer en euros devient moins intéressant, les capitaux sortent (CFHAR ↑) et la BG revient vers zéro. "
               "Quand elle détruit des euros (BG déficitaire), les taux montent, les capitaux entrent (CFHAR ↓) et la BG se rééquilibre aussi.")
    c.h3("Les autres régimes de change")
    c.ul(["<b>Ancrage fixe dur</b> : il n'y a plus de taux de change du tout (union économique et monétaire, comme la zone euro).", "<b>Ancrage glissant</b> : change fixe, mais la banque centrale programme à l'avance des dévaluations régulières.",
          "<b>Change fixe avec bande de fluctuation</b> : le taux peut bouger librement à l'intérieur d'une bande autour de la parité ; la banque centrale n'intervient qu'aux bords.", "<b>Change libre</b> (flottement pur)."])
    c.synthese(["Le taux de change est le prix d'une monnaie ; il se lit au certain ou à l'incertain.",
                "Change flexible : le prix s'ajuste seul ; une monnaie en offre excédentaire se déprécie.",
                "Change fixe : la banque centrale défend la parité avec ses réserves ; sa masse monétaire varie avec la BG.",
                "BG ≠ 0 : en flexible, correction par le change ; en fixe, par les réserves puis par les taux d'intérêt.",
                "Limite du change fixe : réserves épuisées ⇒ dévaluation."])
    return c


def ch3():
    c = Cours()
    c.intro("De quoi parle ce chapitre ?",
            "Le taux de change nominal ne suffit pas à savoir si un pays est compétitif : il faut aussi comparer les <b>prix</b>. C'est le rôle du <b>taux de change réel</b>. "
            "On verra ensuite à quelle condition une dépréciation améliore vraiment le commerce extérieur (la condition de Marshall-Lerner), "
            "puis ce qui guide les mouvements de capitaux entre pays : la comparaison des rendements (la PTINC).",
            ["De quoi dépendent les exportations et les importations ?", "Qu'est-ce que le taux de change réel et comment l'interpréter ?",
             "Une dépréciation améliore-t-elle toujours la balance commerciale ?", "Pourquoi l'effet d'une dépréciation suit-il une courbe en J ?",
             "Qu'est-ce qui fait entrer ou sortir les capitaux ?"])

    c.sec("I. Compétitivité et taux de change réel")
    c.p("La demande d'exportations dépend :")
    c.ul(["<b>négativement</b> de nos prix relatifs, donc du TCR (plus nos produits sont chers, moins on exporte) : c'est la compétitivité-prix ;", "<b>positivement</b> de la compétitivité hors prix (qualité, innovation, image) ;", "<b>positivement</b> du revenu réel du RDM."])
    c.p("La demande d'importations dépend positivement de nos prix relatifs (plus nos produits sont chers, plus on importe), de la compétitivité hors prix des produits étrangers et du revenu réel national.")
    c.df("Compétitivité-prix", "Capacité à vendre grâce à des prix inférieurs à ceux des concurrents étrangers, une fois les prix convertis dans la même monnaie.")
    c.df("Compétitivité hors prix", "Capacité à vendre grâce à des éléments autres que le prix : qualité, innovation, image, service après-vente.")
    c.h3("Le taux de change réel (TCR)")
    c.p("Pour comparer les prix, il faut les exprimer dans la même monnaie : le prix étranger P* (en dollars) multiplié par e (prix du dollar en euros) donne le prix étranger en euros.")
    c.f("TCR = P / (e × P*)")
    c.df("Taux de change réel (TCR)", "Rapport entre les prix nationaux et les prix étrangers exprimés dans la même monnaie : TCR = P/(e·P*) ; il mesure la compétitivité-prix d'un pays.")
    c.ul(["<b>TCR > 1</b> : les produits français sont plus chers que ceux du RDM ; la France est moins compétitive.", "<b>TCR < 1</b> : les produits français sont moins chers ; la France est plus compétitive."])
    c.df("Appréciation réelle", "Hausse du TCR : les prix français augmentent par rapport aux prix étrangers convertis en euros ; perte de compétitivité-prix.")
    c.df("Dépréciation réelle", "Baisse du TCR : les prix français baissent par rapport aux prix étrangers convertis en euros ; gain de compétitivité-prix.")
    c.df("Taux de change effectif réel (TCER)", "Moyenne pondérée des taux de change réels d'un pays vis-à-vis de ses principaux partenaires ; on l'utilise pour comparer un pays à un ensemble de pays.")
    c.warn("Ne confonds pas le taux de change <b>nominal</b> (prix d'une monnaie) et le taux de change <b>réel</b> (rapport de prix). Et certaines organisations définissent le TCR à l'envers (e·P*/P) : une hausse signifie alors un gain de compétitivité. Vérifie la définition en début d'examen.")
    c.pourquoi("Pourquoi une hausse du TCR fait-elle baisser les exportations ?",
               "Un TCR qui monte veut dire que nos produits deviennent plus chers que les produits étrangers pour un même acheteur. Les clients étrangers se tournent vers d'autres fournisseurs (X ↓) et les Français achètent davantage de produits étrangers (Z ↑). "
               "Il reste à savoir <b>de combien</b> : c'est le rôle des élasticités.")
    c.retenir(["TCR = P/(e·P*).", "TCR ↑ = appréciation réelle = perte de compétitivité-prix ⇒ X ↓, Z ↑.", "TCR ↓ = dépréciation réelle = gain de compétitivité ⇒ X ↑, Z ↓."])

    c.sec("II. Mesurer la réaction : les élasticités")
    c.df("Taux de croissance", "Variation relative d'une grandeur : (valeur d'arrivée − valeur de départ)/valeur de départ, en %.")
    c.f("ε X/TCR = (ΔX/ΔTCR) × (TCR/X) < 0 · ε Z/TCR = (ΔZ/ΔTCR) × (TCR/Z) > 0")
    c.df("Élasticité des exportations au TCR", "Variation en % des exportations quand le TCR augmente de 1 % ; elle est négative.")
    c.df("Élasticité des importations au TCR", "Variation en % des importations (en volume) quand le TCR augmente de 1 % ; elle est positive.")
    c.f("X^ = ε X/TCR × TCR^ · Z^ = ε Z/TCR × TCR^ (le chapeau ^ désigne un taux de croissance)")
    c.ex("Interpréter", "<p>ε X/TCR = −2 : si le TCR s'apprécie de 1 % (les prix français montent de 1 % par rapport aux prix étrangers), les exportations baissent de 2 %.</p><p>ε Z/TCR = 2,5 : dans la même situation, les importations augmentent de 2,5 %.</p>")
    c.p("C'est exactement la logique de l'élasticité vue en microéconomie (chapitre 1), appliquée au commerce extérieur.")

    c.sec("III. Taux de change et balance des biens et services")
    c.p("On suppose ici les revenus primaires et secondaires nuls : le compte courant se réduit à X − M.")
    c.h3("1. Tout exprimer dans la même unité")
    c.p("Les exportations X sont mesurées en euros constants (en paniers de biens français) ; les importations Z en dollars constants (en paniers de biens américains). Pour les soustraire, il faut convertir les importations :")
    c.pas("Convertir les importations en paniers de biens français", [
        "Dollars constants → dollars courants : Z × P*.", "Dollars courants → euros courants : Z × P* × e.", "Euros courants → euros constants : Z × P* × e / P = Z / TCR."],
        "Un panier américain vaut e·P*/P = 1/TCR panier français.")
    c.f("Balance des biens et services (en euros constants) : BBS = X − Z / TCR")
    c.h3("2. Une dépréciation réelle a deux effets opposés")
    c.df("Effet volume (effet de compétitivité)", "Après une dépréciation réelle, les produits nationaux deviennent plus compétitifs : les exportations augmentent et les importations diminuent en volume ; effet favorable à la balance commerciale.")
    c.df("Effet prix (effet termes de l'échange)", "Après une dépréciation réelle, chaque unité importée coûte plus cher en monnaie nationale (1/TCR augmente) : la facture des importations s'alourdit ; effet défavorable à la balance commerciale.")
    c.pas("Exemple du cours : ε X/TCR = −2, ε Z/TCR = 1,5, le TCR se déprécie de 1 %", [
        "Exportations : X^ = −2 × (−1) = <b>+2 %</b>.", "Importations en volume : Z^ = 1,5 × (−1) = <b>−1,5 %</b>.",
        "Effet volume total : 2 + 1,5 = 3,5 % (somme des valeurs absolues des élasticités).", "Effet prix : chaque panier importé coûte 1 % plus cher en paniers français, soit −1 %."],
        "Effet net ≈ 3,5 − 1 = <b>+2,5 %</b> des exportations (en partant d'une balance équilibrée) : la balance s'améliore.")
    c.h3("3. La condition de Marshall-Lerner")
    c.df("Condition de Marshall-Lerner", "Une dépréciation réelle améliore la balance des biens et services si la somme des valeurs absolues des élasticités-prix des exportations et des importations est supérieure à 1 : |ε X/TCR| + ε Z/TCR > 1.")
    c.f("|ε X/TCR| + ε Z/TCR > 1 ⇒ effet volume > effet prix ⇒ dépréciation favorable")
    c.autrement("une dépréciation n'est utile que si les volumes réagissent assez fort pour compenser le fait que les importations coûtent plus cher. L'amélioration est égale à « l'écart par rapport à 1 ».")
    c.ex("Exemple du cours", "<p>ε X = −0,7 et ε Z = 0,5 : 0,7 + 0,5 = 1,2 > 1. L'effet compétitivité l'emporte ; pour une dépréciation réelle de 1 %, la balance s'améliore d'environ 0,2 % des exportations (1,2 − 1).</p>")
    c.p("Une <b>appréciation</b> réelle produit l'inverse : l'effet prix est favorable (les importations coûtent moins cher), l'effet compétitivité défavorable. Si Marshall-Lerner est vérifiée, la balance se détériore.")
    c.h3("4. La courbe en J")
    c.df("Courbe en J", "Évolution de la balance commerciale après une dépréciation : elle se dégrade d'abord (l'effet prix est immédiat), puis s'améliore quand l'effet volume se manifeste ; son tracé rappelle la lettre J.")
    c.pourquoi("Pourquoi l'effet prix arrive-t-il avant l'effet volume ?",
               "Le jour de la dépréciation, les importations déjà commandées coûtent immédiatement plus cher : l'effet prix est instantané. "
               "L'effet volume demande du temps : les producteurs doivent appliquer les nouveaux prix, les consommateurs doivent s'en apercevoir et changer leurs habitudes, les contrats doivent être renégociés. "
               "La balance commence donc par se dégrader avant de s'améliorer, si Marshall-Lerner est vérifiée.")
    c.retenir(["BBS = X − Z/TCR.", "Dépréciation réelle : effet volume (+) et effet prix (−).", "Marshall-Lerner : |εX| + εZ > 1.", "À court terme, l'effet prix domine : courbe en J."])

    c.sec("IV. Qu'est-ce qui fait varier le TCR ?")
    c.f("TCR^ ≈ π − π* − ê (π : inflation nationale ; π* : inflation étrangère ; ê : taux de variation de e)")
    c.h3("1. À taux de change nominal constant : l'inflation")
    c.df("Inflation", "Hausse du niveau général des prix ; son taux est π = (P(t) − P(t−1))/P(t−1) ; π* désigne l'inflation étrangère.")
    c.ul(["Si les prix nationaux montent plus vite que les prix étrangers (π > π*) : TCR ↑, perte de compétitivité, la balance se dégrade (si M-L).", "Si π < π* : TCR ↓, gain de compétitivité, la balance s'améliore (si M-L)."])
    c.df("Désinflation compétitive", "Stratégie qui consiste à maintenir une inflation plus faible que celle des partenaires (π < π*) pour faire baisser le TCR et gagner en compétitivité sans dévaluer.")
    c.p("Moyens : ralentir la croissance de la masse monétaire, modérer les salaires (souvent via la hausse du chômage), donc baisser les coûts des entreprises et l'inflation. Le coût social est élevé.")
    c.h3("2. À prix constants : le taux de change nominal")
    c.pas("Exemple du cours : en T0, 1 $ = 1 € ; en T1, 1 $ = 2 € (soit 1 € = 0,5 $)", [
        "L'euro s'est déprécié : avec la même somme on obtient moins de dollars. e ↑ donc TCR ↓.",
        "Effet volume : la France est plus compétitive, X ↑ et Z ↓ (le compte courant s'améliore si M-L est vérifiée).",
        "Effet prix : il faut maintenant 2 € pour importer ce qui coûtait 1 $ : la facture des importations augmente."],
        "Le résultat net dépend de Marshall-Lerner : la balance s'améliore si |εX| + εZ > 1.")
    c.retenir(["TCR^ ≈ π − π* − ê.", "Inflation plus forte que chez les partenaires ⇒ perte de compétitivité.", "Dépréciation nominale (e ↑) ⇒ TCR ↓."])
    c.transition("Le commerce n'est qu'une partie de la balance des paiements. Pour les économies développées, les postes les plus importants sont les IDE et les autres investissements : que guide ces flux de capitaux ?")

    c.sec("V. Taux de change, taux d'intérêt et marché des actifs : la PTINC")
    c.idee("Les capitaux vont là où ils <b>rapportent le plus</b>. Un placement à l'étranger rapporte le taux d'intérêt étranger, plus (ou moins) ce que l'on gagne (ou perd) sur le change.")
    c.p("Hypothèses : parfaite mobilité des capitaux, absence d'aversion au risque, titres de même risque dans les deux pays.")
    c.pas("Comparer deux placements d'un euro pendant un an", [
        "En France : 1 € devient <b>1 + i</b>.",
        "Aux États-Unis : on convertit l'euro en dollars au taux e, on place au taux i*, puis on reconvertit au taux de change anticipé e<sup>a</sup>. On obtient (1 + i*) × e<sup>a</sup>/e.",
        "Avec ê<sup>a</sup> = (e<sup>a</sup> − e)/e, le taux de dépréciation anticipé de l'euro : (1 + i*)(1 + ê<sup>a</sup>) ≈ 1 + i* + ê<sup>a</sup>."],
        "Il faut donc comparer i et <b>i* + ê<sup>a</sup></b>.")
    c.df("Parité des taux d'intérêt non couverte (PTINC)", "Condition d'équilibre des marchés d'actifs en parfaite mobilité des capitaux : i = i* + ê^a, le rendement national égale le rendement étranger augmenté de la dépréciation anticipée de la monnaie nationale ; il n'y a alors pas de mouvement de capitaux.")
    c.f("PTINC : i = i* + ê<sup>a</sup> · forme exacte : 1 + i = (1 + i*)(e<sup>a</sup>/e)")
    c.tab(["Situation", "Capitaux", "CFHAR", "BG", "Marché des changes", "Change flexible", "Change fixe"], [
        ["i > i* + ê<sup>a</sup>", "Entrées (rendement meilleur chez nous)", "< 0 (engagements ↑ ou avoirs ↓)", "> 0", "Offre excédentaire de $, demande excédentaire d'€", "€ s'apprécie, TCR ↑, perte de compétitivité", "Réserves en $ ↑, masse monétaire en € ↑"],
        ["i < i* + ê<sup>a</sup>", "Sorties (rendement meilleur chez eux)", "> 0 (avoirs ↑ ou engagements ↓)", "< 0", "Offre excédentaire d'€, demande excédentaire de $", "€ se déprécie, TCR ↓, gain de compétitivité", "Réserves ↓, masse monétaire ↓"],
        ["i = i* + ê<sup>a</sup>", "Aucun mouvement", "0", "0", "Équilibre", "—", "—"]])
    c.p("Le compte courant dépend du revenu étranger (Y* ↑ ⇒ X ↑), du revenu national (Y ↑ ⇒ Z ↑) et du TCR (TCR ↑ ⇒ CC ↓ si M-L). La balance globale dépend en plus, et surtout, de l'<b>écart de rendement anticipé</b> i − (i* + ê<sup>a</sup>), car les flux financiers dépassent de loin les flux commerciaux.")
    c.synthese(["TCR = P/(e·P*) ; TCR ↑ = perte de compétitivité-prix.",
                "Une dépréciation réelle améliore la balance si |εX| + εZ > 1 (Marshall-Lerner), après une phase de dégradation (courbe en J).",
                "TCR^ ≈ π − π* − ê : l'inflation relative et le change nominal font bouger le TCR.",
                "PTINC : i = i* + ê^a ; si i est plus élevé, les capitaux entrent (BG > 0), sinon ils sortent (BG < 0)."])
    return c


def ch4():
    c = Cours()
    c.intro("De quoi parle ce chapitre ?",
            "On rassemble tout ce qui précède dans un modèle : comment se déterminent ensemble la production, le taux d'intérêt et la balance globale d'une petite économie ouverte à court terme ? "
            "C'est le modèle <b>IS-LM-PTINC</b> (modèle de Mundell-Fleming). Il servira au chapitre suivant à évaluer les politiques économiques.",
            ["Sur quelles hypothèses repose le modèle ?", "Pourquoi le chômage est-il keynésien à court terme ?", "Que représentent les courbes IS, LM et la droite PTINC ?",
             "Qu'est-ce que l'équilibre général ?", "Comment l'économie revient-elle à l'équilibre selon le régime de change ?"])

    c.sec("I. Le cadre d'analyse")
    c.p("Quatre marchés sont étudiés, avec leur prix :")
    c.tab(["Marché", "Prix national", "Prix étranger"], [["Biens et services", "P", "P*"], ["Travail", "w/P (salaire réel)", "w*/P*"], ["Monnaie (change)", "1 € ou e €", ""], ["Titres", "i (taux d'intérêt)", "i*"]])
    c.df("Salaire réel", "Salaire nominal divisé par le niveau des prix (w/P) : nombre de paniers de biens qu'une heure de travail permet d'acheter.")
    c.note("Le taux d'intérêt évolue en sens inverse du prix des titres : quand le cours des titres monte, i baisse ; quand il baisse, i monte.")
    c.h3("Les hypothèses")
    c.ul(["<b>Petit pays</b> : il n'influence ni les prix, ni les taux d'intérêt, ni les revenus étrangers (P*, i*, Y* sont donnés).",
          "<b>Court terme</b> : le stock de capital est fixe et le progrès technique donné ; Y = f(K, L), où Y est le PIB.",
          "<b>Prix et salaires rigides</b> (fixes) à court terme : aucune entreprise ne veut monter ses prix la première, de peur de perdre ses clients.",
          "<b>Parfaite mobilité des capitaux</b> (d'où la droite PTINC horizontale)."])
    c.df("Hypothèse du petit pays", "Le pays étudié est trop petit pour influencer les variables étrangères (prix, taux d'intérêt, revenu du RDM), qu'il prend comme données.")

    c.sec("II. Le marché du travail : chômage classique et chômage keynésien")
    c.df("Offre de travail (Ls)", "Nombre d'heures que les ménages souhaitent travailler pour chaque salaire réel ; elle croît avec w/P jusqu'à la population active totale (PAT).")
    c.df("Demande de travail (Ld)", "Nombre d'heures que les entreprises souhaitent employer ; elle décroît avec le coût réel du travail et, à court terme, dépend aussi de la demande de biens et services.")
    c.df("Population active totale (PAT)", "Ensemble des personnes en âge et en capacité de travailler ; au-delà de l'offre de travail, le reste est inactif.")
    c.p("À l'équilibre Ls = Ld = L0 : il n'y a pas de chômage involontaire. Le chômage apparaît quand l'équilibre n'est pas atteint.")
    c.df("Chômage classique", "Chômage dû à un coût réel du travail trop élevé : au salaire w/P1 > w/P0, l'offre de travail (0A) dépasse la demande (0C) ; le chômage est CA ; il ne se résorbe pas tant que les salaires restent rigides.")
    c.df("Chômage keynésien", "Chômage dû à une demande de biens et services insuffisante : les entreprises subissent une contrainte de débouchés, produisent moins que leur optimum et n'emploient que ce dont elles ont besoin, même au salaire d'équilibre.")
    c.pas("Si prix et salaires étaient flexibles (chômage classique)", [
        "Les entreprises, en position de force, obtiennent une baisse des salaires.",
        "Certaines personnes cessent de chercher un emploi (Ls ↓, elles deviennent inactives) ; d'autres acceptent un salaire plus bas.",
        "Les entreprises embauchent davantage (Ld ↑) : le chômage se résorbe jusqu'au plein emploi."])
    c.pas("Pour réduire le chômage keynésien", [
        "Agir sur la demande : politique budgétaire ou monétaire.", "Yd ↑ ⇒ production ↑ ⇒ profits ↑ ⇒ embauches ↑ ⇒ chômage ↓."],
        "La demande de biens et services gouverne la production, et donc l'emploi.")
    c.idee("Dans tout le modèle, on se place en <b>chômage keynésien à court terme</b> : Y = Yd < Y optimal. Le marché du travail n'a donc pas besoin d'être étudié à part : l'emploi suit la production, qui suit la demande.")
    c.retenir(["Chômage classique : salaire réel trop élevé (problème d'offre).", "Chômage keynésien : demande insuffisante (problème de débouchés).", "À court terme, on raisonne en chômage keynésien."])

    c.sec("III. Équilibres partiels et loi de Walras")
    c.df("Loi de Walras", "Quand une économie comporte n marchés et que n − 1 d'entre eux sont à l'équilibre, le dernier l'est aussi.")
    c.p("Le marché du travail dépend du marché des biens ; avec la loi de Walras, il reste <b>trois marchés</b> à étudier : biens et services (IS), monnaie et titres (LM), monnaie étrangère (PTINC).")
    c.df("Équilibre partiel", "Équilibre d'un marché étudié isolément, toutes choses égales par ailleurs.")
    c.df("Équilibre général", "Équilibre simultané de tous les marchés étudiés : intersection d'IS, de LM et de la PTINC.")

    c.sec("IV. Le marché des biens et services : la courbe IS")
    c.p("On a Y = Yd < Y optimal : les firmes ne produisent que ce qui est demandé.")
    c.ul(["Si Y < Yd, les firmes ont sous-estimé la demande : ventes manquées.", "Si Y > Yd, elles l'ont surestimée : invendus.", "L'équilibre (Y = Yd) n'est pas walrasien : les firmes subissent une contrainte de débouchés, leurs souhaits ne sont pas réalisés."])
    c.f("Yd = C + I + G + (X − M) = C + I + G + CC")
    c.ul(["La consommation dépend du revenu disponible (Y − T) et de l'optimisme des ménages.", "L'investissement dépend du taux d'intérêt réel r et de l'optimisme des firmes.",
          "Les dépenses publiques G et les impôts T sont décidés par l'État (politique budgétaire) ; la banque centrale décide de la politique monétaire.", "CC dépend du revenu national, du revenu étranger Y* et du TCR."])
    c.f("Y = Yd = f(Y ; T ; G ; r ; Y* ; TCR ; DOF ; DOM) ⇒ courbe IS")
    c.df("Courbe IS", "Ensemble des couples (Y, i) qui assurent l'équilibre du marché des biens et services (Y = Yd) ; elle est décroissante, car une hausse du taux d'intérêt réduit l'investissement donc la production.")
    c.df("Multiplicateur keynésien", "Mécanisme par lequel une hausse initiale de la demande entraîne une hausse plus que proportionnelle de la production : la production supplémentaire distribue des revenus, qui sont en partie dépensés, ce qui relance encore la production.")
    c.pas("Effet d'une hausse de G (financée par l'emprunt)", ["La demande augmente.", "Les entreprises produisent plus et embauchent.", "Les salariés embauchés consomment : les entreprises de biens de consommation embauchent à leur tour…"],
          "C'est l'effet multiplicateur : la production d'équilibre augmente plus que G.")
    c.tab(["Variable", "Effet sur la demande", "Effet sur IS"], [
        ["G ↑", "Demande publique ↑", "IS se déplace à droite"], ["T ↓", "C ↑ (revenu disponible ↑)", "IS se déplace à droite"], ["Y* ↑", "X ↑", "IS se déplace à droite"],
        ["DOF ↑ (optimisme des firmes)", "I ↑", "IS se déplace à droite"], ["DOM ↑ (optimisme des ménages)", "C ↑", "IS se déplace à droite"],
        ["TCR ↑ (appréciation réelle)", "CC ↓ si M-L (demande extérieure nette ↓)", "IS se déplace à gauche"], ["r (ou i) ↑", "I ↓", "Déplacement <b>le long</b> d'IS"]])
    c.retenir(["IS : équilibre des biens, décroissante.", "Une variation de r ⇒ déplacement le long d'IS.", "G, T, Y*, DOF, DOM, TCR ⇒ déplacement d'IS.", "CC est la demande extérieure nette."])

    c.sec("V. Le marché de la monnaie : la courbe LM")
    c.df("Demande de monnaie", "Quantité de monnaie que les agents souhaitent détenir ; la demande réelle Md/P dépend positivement du revenu (transactions) et négativement du taux d'intérêt nominal (coût d'opportunité de détenir de la monnaie).")
    c.df("Open market expansionniste", "La banque centrale achète des titres publics et paie en monnaie qu'elle crée : la masse monétaire augmente, le cours des titres monte et le taux d'intérêt baisse.")
    c.df("Open market restrictif", "La banque centrale vend des titres publics et détruit la monnaie reçue : la masse monétaire baisse, le cours des titres baisse et le taux d'intérêt monte.")
    c.idee("En économie ouverte, la masse monétaire varie de <b>deux façons</b> en change fixe (open market <b>et</b> interventions sur le marché des changes, liées à la BG), mais d'<b>une seule</b> en change flexible (open market).")
    c.f("Ms/P = Md/P = L(Y ; i) ⇒ i = g(Ms/P ; Y) : courbe LM")
    c.df("Courbe LM", "Ensemble des couples (Y, i) qui assurent l'équilibre du marché de la monnaie (offre = demande de monnaie) ; elle est croissante.")
    c.pas("Pourquoi LM est croissante : Y ↑", ["Les firmes produisent plus et embauchent.", "Elles ont besoin de monnaie pour verser les salaires.", "Elles vendent des titres pour obtenir cette monnaie : l'offre de titres augmente.", "Le cours des titres baisse."], "Le taux d'intérêt monte : à l'équilibre monétaire, plus de production va avec un taux plus élevé.")
    c.ul(["Une variation de Y : déplacement <b>le long</b> de LM.", "Une variation de Ms : déplacement <b>de</b> LM (Ms ↑ : LM vers le bas, ou vers la droite)."])

    c.sec("VI. La balance des paiements : la droite PTINC")
    c.p("En économie ouverte, les flux financiers dépassent largement le compte courant ; ils dépendent de l'écart i − (i* + ê<sup>a</sup>). Avec une parfaite mobilité des capitaux, la BG n'est équilibrée que si i = i* + ê<sup>a</sup>.")
    c.df("Droite PTINC (droite d'intégration financière)", "Droite horizontale au niveau i = i* + ê^a dans le plan (Y, i) : ensemble des points où la balance globale et le marché des changes sont équilibrés en parfaite mobilité des capitaux.")
    c.ul(["Au-dessus de la PTINC (i > i* + ê<sup>a</sup>) : entrées de capitaux, CFHAR < 0, BG > 0, offre excédentaire de devises.", "En dessous : sorties de capitaux, CFHAR > 0, BG < 0, offre excédentaire de monnaie nationale."])
    c.h3("L'équation de Fisher")
    c.df("Équation de Fisher", "Relation entre taux d'intérêt nominal et réel : i = r + π^a (taux réel plus inflation anticipée), soit r = i − π^a.")
    c.p("Dans IS apparaît r (l'investissement dépend du taux réel) ; dans LM apparaît i (la demande de monnaie dépend du taux nominal). On suppose une inflation anticipée nulle : <b>r = i</b>, et on peut tracer IS et LM sur le même graphique.")

    c.sec("VII. L'équilibre général et le retour à l'équilibre")
    c.f("Équilibre général E (Yé ; ié) : IS ∩ LM ∩ PTINC")
    c.p("Supposons que l'équilibre interne soit atteint (IS et LM se coupent en A) mais que A ne soit pas sur la PTINC. La BG n'est pas équilibrée : l'ajustement dépend du régime de change.")
    c.h3("Cas 1 : iA > i* + ê<sup>a</sup> (A au-dessus de la PTINC)")
    c.p("Entrées de capitaux, BG > 0 : offre excédentaire de devises et demande excédentaire de monnaie nationale.")
    c.pas("Change flexible", ["La monnaie nationale s'apprécie : TCR ↑, perte de compétitivité.", "X ↓ et Z ↑ : le CC se dégrade (si M-L), la demande extérieure nette baisse.", "En chômage keynésien, la production baisse et le chômage augmente.", "IS se déplace vers la <b>gauche</b> jusqu'à couper LM sur la PTINC."],
          "Retour à l'équilibre en E, mais avec une production plus faible qu'en A.")
    c.pas("Change fixe", ["La banque centrale achète les devises : réserves ↑, masse monétaire ↑.", "Le taux d'intérêt baisse : l'investissement augmente.", "La production augmente et le chômage baisse.", "LM se déplace vers le <b>bas</b> (la droite) jusqu'à la PTINC."],
          "Retour à l'équilibre général en E, avec une production plus forte qu'en A.")
    c.h3("Cas 2 : iA < i* + ê<sup>a</sup> (A en dessous de la PTINC)")
    c.p("Sorties de capitaux, BG < 0 : offre excédentaire de monnaie nationale et demande excédentaire de devises.")
    c.pas("Change flexible", ["La monnaie nationale se déprécie : TCR ↓, gain de compétitivité.", "X ↑ et Z ↓ : le CC s'améliore (si M-L), la demande extérieure nette augmente.", "La production augmente et le chômage baisse.", "IS se déplace vers la <b>droite</b>."], "Retour en E, avec une production plus forte qu'en A.")
    c.pas("Change fixe", ["La banque centrale vend des devises : réserves ↓, masse monétaire ↓.", "Le taux d'intérêt monte : l'investissement baisse.", "La production baisse et le chômage augmente.", "LM se déplace vers le <b>haut</b> (la gauche)."], "Retour en E, avec une production plus faible qu'en A.")
    c.pourquoi("Pourquoi, en change flexible, est-ce IS qui bouge, et en change fixe, LM ?",
               "En change flexible, la variable qui s'ajuste est le <b>taux de change</b>. Or le taux de change agit sur le TCR, donc sur le compte courant, qui est une composante de la demande : c'est IS qui se déplace. "
               "En change fixe, le taux de change ne bouge pas ; c'est la <b>masse monétaire</b> qui s'ajuste à travers les interventions de la banque centrale : c'est LM qui se déplace.")
    c.retenir(["Équilibre général : IS ∩ LM ∩ PTINC.", "Au-dessus de la PTINC : BG > 0 ; en dessous : BG < 0.", "Change flexible : IS s'ajuste (via le TCR) ; change fixe : LM s'ajuste (via Ms)."])
    c.synthese(["Petit pays, court terme, prix rigides, chômage keynésien : la demande gouverne la production.",
                "IS (biens, décroissante), LM (monnaie, croissante), PTINC (BG, horizontale en parfaite mobilité).",
                "Loi de Walras : 3 marchés suffisent.", "Le retour à l'équilibre passe par le change (flexible, IS bouge) ou par la masse monétaire (fixe, LM bouge)."])
    return c


def ch5():
    c = Cours()
    c.intro("De quoi parle ce chapitre ?",
            "Une économie en chômage keynésien peut-elle être relancée ? Avec quel instrument ? On applique le modèle IS-LM-PTINC du chapitre 4 aux deux grandes politiques (monétaire et budgétaire), dans les deux régimes de change. "
            "Le résultat est spectaculaire : <b>l'efficacité d'une politique dépend entièrement du régime de change</b>.",
            ["Une politique monétaire de relance est-elle efficace en change flexible ? En change fixe ?", "Et une politique budgétaire ?", "Qu'est-ce que le triangle d'incompatibilité ?",
             "Que se passe-t-il quand les taux d'intérêt étrangers augmentent ?"])

    c.sec("I. Objectif et cadre")
    c.idee("Le but des politiques macroéconomiques est de passer d'un équilibre général à un <b>équilibre meilleur</b>, avec plus de production et moins de chômage, en relançant la demande de biens et services.")
    c.p("Cadre : petite économie ouverte, parfaite mobilité des capitaux, chômage keynésien. On part d'un équilibre général E sur la PTINC.")
    c.df("Politique monétaire", "Action de la banque centrale sur la masse monétaire et les taux d'intérêt, ici par l'open market.")
    c.df("Politique budgétaire", "Action de l'État sur la demande par les dépenses publiques (G) et les impôts (T).")

    c.sec("II. En change flexible")
    c.h3("1. Politique monétaire expansive : très efficace")
    c.pas("Le mécanisme", [
        "Open market expansionniste : Ms ↑, i ↓. La consommation et l'investissement augmentent ; LM se déplace vers le bas. On arrive en A, sous la PTINC.",
        "i < i* : il est plus intéressant de placer à l'étranger ; les capitaux sortent (avoirs ↑, CFHAR > 0, BG < 0).",
        "Offre excédentaire de monnaie nationale : elle se déprécie, TCR ↓, l'économie devient plus compétitive.",
        "Le CC s'améliore (si M-L) : la demande extérieure nette augmente, la production augmente et le chômage baisse ; IS se déplace vers la droite jusqu'à la PTINC."],
        "La production augmente deux fois : par la baisse du taux, puis par la dépréciation. Politique <b>très efficace</b>.")
    c.h3("2. Politique budgétaire expansive : inefficace")
    c.pas("Le mécanisme", [
        "G ↑ : la demande augmente, la production aussi ; IS se déplace vers la droite. Les besoins de monnaie font monter i : on arrive en A, au-dessus de la PTINC.",
        "i > i* : les capitaux entrent (engagements ↑, CFHAR < 0, BG > 0).",
        "Demande excédentaire de monnaie nationale : elle s'apprécie, TCR ↑, perte de compétitivité.",
        "Le CC se dégrade (si M-L) : la demande extérieure nette baisse, IS revient vers la gauche jusqu'à la PTINC, au point de départ."],
        "La hausse de G est entièrement compensée par la baisse du solde extérieur : <b>effet d'éviction par le taux de change</b>. Politique <b>inefficace</b> sur la production.")
    c.df("Éviction par le taux de change", "En change flexible et parfaite mobilité des capitaux, la hausse des dépenses publiques provoque une appréciation de la monnaie qui réduit le solde extérieur d'autant : la demande totale, donc la production, ne change pas.")
    c.retenir(["Change flexible : politique monétaire très efficace, politique budgétaire inefficace.", "Le taux de change amplifie la politique monétaire et neutralise la politique budgétaire."])

    c.sec("III. En change fixe")
    c.h3("1. Politique monétaire expansive : inefficace")
    c.pas("Le mécanisme", [
        "Ms ↑, i ↓ : LM se déplace vers le bas ; on arrive en A, sous la PTINC.",
        "i < i* : sorties de capitaux, CFHAR > 0, BG < 0 ; offre excédentaire de monnaie nationale, qui devrait se déprécier.",
        "Pour tenir la parité, la banque centrale rachète sa monnaie et vend des devises : masse monétaire ↓, réserves ↓.",
        "La baisse de la masse monétaire (vente de titres, cours ↓) fait remonter i : LM revient à sa position initiale."],
        "Retour à l'équilibre initial : la politique monétaire est <b>inefficace</b>, et elle a coûté des réserves. Trop risqué.")
    c.h3("2. Politique budgétaire expansive : très efficace")
    c.pas("Le mécanisme", [
        "G ↑ : la production augmente, les firmes embauchent et ont besoin de monnaie ; la banque centrale ne bouge pas la masse monétaire, donc les firmes vendent des titres : cours ↓, i ↑. IS se déplace vers la droite ; on arrive en A, au-dessus de la PTINC.",
        "i > i* : entrées de capitaux, CFHAR < 0, BG > 0 ; demande excédentaire de monnaie nationale.",
        "Pour tenir la parité, la banque centrale achète les devises et crée de la monnaie : réserves ↑, masse monétaire ↑.",
        "Ms ↑ (achat de titres, cours ↑) fait baisser i : l'investissement et la consommation augmentent ; LM se déplace vers le bas jusqu'à la PTINC."],
        "La production augmente deux fois (par G, puis par la création monétaire) : politique <b>très efficace</b>, avec un excédent de BG.")
    c.tab(["", "Change flexible", "Change fixe"], [
        ["Politique monétaire expansive", "<b>Très efficace</b> (dépréciation ⇒ IS → droite)", "<b>Inefficace</b> (perte de réserves ⇒ LM revient)"],
        ["Politique budgétaire expansive", "<b>Inefficace</b> (appréciation ⇒ IS revient)", "<b>Très efficace</b> (création monétaire ⇒ LM → droite)"]])
    c.pourquoi("Pourquoi la même politique peut-elle être très efficace dans un régime et inutile dans l'autre ?",
               "Parce que, avec des capitaux parfaitement mobiles, le taux d'intérêt est bloqué au niveau mondial (i = i*). Toute politique qui l'écarte de ce niveau déclenche des flux de capitaux. "
               "En change flexible, ces flux font bouger le taux de change, qui agit sur IS : il renforce la politique monétaire et annule la politique budgétaire. "
               "En change fixe, ils font bouger la masse monétaire, qui agit sur LM : il annule la politique monétaire et renforce la politique budgétaire.")
    c.retenir(["Change fixe : politique monétaire inefficace, politique budgétaire très efficace.", "En change fixe, la masse monétaire n'est plus un instrument : elle dépend de la BG."])

    c.sec("IV. Le triangle d'incompatibilité")
    c.df("Triangle d'incompatibilité", "Un pays ne peut pas avoir en même temps un change fixe, une parfaite mobilité internationale des capitaux et une politique monétaire indépendante ; il doit renoncer à l'un des trois.")
    c.autrement("c'est exactement le résultat précédent : avec des capitaux mobiles et un change fixe, la politique monétaire ne sert à rien, la banque centrale doit consacrer la masse monétaire à défendre la parité.")
    c.tab(["On garde…", "On renonce à…", "Exemple"], [
        ["Change fixe + mobilité des capitaux", "La politique monétaire indépendante", "Zone euro entre ses membres, caisses d'émission"],
        ["Mobilité des capitaux + politique monétaire autonome", "Le change fixe (on laisse flotter)", "États-Unis, Royaume-Uni, zone euro face au dollar"],
        ["Change fixe + politique monétaire autonome", "La mobilité des capitaux (contrôles des capitaux)", "Système de Bretton Woods, Chine longtemps"]])
    c.h3("Le lien avec les crises de change")
    c.p("Un pays qui veut garder un change fixe et la libre circulation des capitaux, tout en menant une politique monétaire différente de celle de ses partenaires, s'expose à des sorties de capitaux. "
        "La banque centrale perd ses réserves en défendant la parité ; quand les marchés anticipent qu'elle ne tiendra plus, la spéculation s'accélère et la parité finit par céder : c'est une <b>crise de change</b>, qui se termine par une dévaluation (voir le chapitre 2).")
    c.df("Crise de change", "Attaque spéculative contre une monnaie en change fixe : les sorties de capitaux épuisent les réserves de la banque centrale, qui doit abandonner la parité ou dévaluer.")

    c.sec("V. Un choc extérieur : la hausse des taux d'intérêt étrangers")
    c.p("Le taux étranger i* augmente : la droite PTINC monte. L'ancien équilibre E se retrouve <b>sous</b> la nouvelle PTINC : i < i*.")
    c.p("Placer à l'étranger devient plus intéressant : sorties de capitaux, avoirs ↑, CFHAR > 0, BG < 0 ; offre excédentaire de monnaie nationale et demande excédentaire de devises.")
    c.pas("En change flexible", ["La monnaie nationale se déprécie : TCR ↓, l'économie est plus compétitive.", "X ↑ et Z ↓ : le CC s'améliore (si M-L), la demande extérieure nette augmente.", "La production augmente et le chômage baisse ; IS se déplace vers la droite jusqu'à la nouvelle PTINC."],
          "Paradoxe : la hausse des taux étrangers <b>stimule</b> l'économie (croissance, chômage ↓).")
    c.pas("En change fixe", ["La banque centrale vend des devises et rachète sa monnaie : masse monétaire ↓, réserves ↓.", "Le taux d'intérêt monte : C et I baissent.", "La production baisse et le chômage augmente ; LM se déplace vers le haut jusqu'à la nouvelle PTINC."],
          "La hausse des taux étrangers est <b>importée</b> : récession.")
    c.p("C'est ce qu'ont vécu les pays du Système monétaire européen au début des années 1990, quand la Bundesbank a relevé ses taux après la réunification allemande.")
    c.synthese(["Change flexible : monétaire très efficace, budgétaire inefficace (éviction par le change).",
                "Change fixe : monétaire inefficace (perte de réserves), budgétaire très efficace (création monétaire induite).",
                "Triangle d'incompatibilité : change fixe, mobilité des capitaux, politique monétaire autonome ; deux sur trois seulement.",
                "Hausse de i* : expansion en change flexible (dépréciation), récession en change fixe (Ms ↓)."])
    return c
