"""Matière : Marketing (7 documents : cours partie 1, chap. 1 suite, chap. 2, marketing stratégique suite, dernière partie, TD, cas L&L + corrigé)."""
from lib import Cours, table, ul, ol, P, H3, H4, NOTE, WARN, FORM, fr
from svg import Plot, boxes, matrix, COL

SRC1 = ['Cours du Marketing — Partie 1 (K. Samhale, 2020/21, 53 diapos)', 'Chap 1 suite — L\'environnement, évolution du marketing (24 diapos)']
SRC2 = ['Marketing Chap 2 — marketing stratégique, diagnostic (35 diapos)', 'Marketing stratégique suite — ADL, BCG, McKinsey, domination par les coûts (23 diapos)', 'Cours Marketing dernière partie — spécialisation, différenciation, innovation, croissance externe (38 diapos)']
SRC_TD = ['Série TD Marketing (6 exercices)', 'Étude de cas L&L + réponse']
DOCS = SRC1 + SRC2 + SRC_TD


def ch1():
    c = Cours()
    c.sec('I. Définitions du marketing')
    c.p('Les résultats financiers des entreprises dépendent souvent de leurs capacités en marketing : la finance, la comptabilité ou la production ont peu d\'utilité si la <b>demande</b> pour les produits est insuffisante.')
    c.ul(['Fonction qui relie une entreprise aux besoins et désirs de ses clients pour obtenir le bon produit, au bon endroit, au bon moment.', 'Accomplissement des objectifs de l\'entreprise par une meilleure réponse aux besoins du client que celle de la concurrence.', 'Processus de gestion qui identifie, anticipe et satisfait efficacement et de façon rentable les exigences du client.'])
    c.df('Marketing (définition de l\'AMA)', 'Fonction de l\'organisation et ensemble de processus visant à créer, communiquer et délivrer de la valeur aux clients et à gérer la relation client d\'une manière qui bénéficie à l\'organisation et à ses parties prenantes (American Marketing Association).')
    c.df('Marketing (définition du Mercator)', '« Effort d\'adaptation des organisations à des marchés concurrentiels, pour influencer en leur faveur le comportement des publics dont elles dépendent, par une offre dont la valeur perçue est durablement supérieure à celle des concurrents. »')
    c.p('Ces définitions ne s\'opposent pas : elles se complètent. Trois idées structurent le cours :')
    c.h3('1. Un effort constant d\'adaptation')
    c.p('Les organisations dépendent de leurs publics et n\'ont pas de pouvoir de contrainte : elles doivent comprendre les attentes des clients et leur évolution, la politique de la concurrence, la réglementation, les évolutions technologiques et le contexte économique. La tendance naturelle est pourtant de rester dans sa « zone de confort ».')
    c.ex('Exemple : l\'industrie de la musique', '<p>Âge d\'or avec les médias de masse, le vinyle et les cassettes ; la révolution numérique (copies sans perte, téléchargement illégal) fait passer les ventes mondiales de 28,6 milliards de dollars en 1999 à moins de 15 milliards en 2010 (source IFPI). Elles repartent depuis 2015 grâce aux concerts, au téléchargement légal et au streaming.</p>')
    c.h3('2. Créer une valeur perçue supérieure à celle des concurrents')
    c.p('Sur des marchés concurrentiels, il faut proposer une offre perçue comme <b>différente et supérieure</b>. La valeur d\'une offre n\'existe pas en soi : elle est toujours <b>relative</b> aux offres concurrentes, et la meilleure offre d\'aujourd\'hui peut cesser de l\'être demain.')
    c.ex('Exemple : Nokia', '<p>Leader incontesté du téléphone portable jusque dans les années 2000, Nokia perd le haut de gamme face à l\'iPhone et à Samsung et le bas de gamme face aux fabricants chinois. Sa division mobile est vendue à Microsoft fin 2013, qui s\'en débarrasse trois ans plus tard.</p>')
    c.h3('3. Une politique qui s\'inscrit dans la durée')
    c.p('Longtemps centré sur l\'offre, le marketing adopte une perspective durable et <b>relationnelle</b> : il faut conquérir les clients et aussi les <b>fidéliser</b>. Exemple : Free et son forfait à 2 € pour recruter, puis faire monter en gamme (augmentation du panier moyen).')

    c.sec('II. La valeur perçue')
    c.df('Valeur perçue', 'Perception par les clients de ce qu\'ils obtiennent (bénéfices perçus : le produit) pour ce qu\'ils donnent (coûts perçus : le prix, mais aussi les efforts, le temps, le risque).')
    c.tab(['Bénéfices perçus', 'Coûts perçus'], [['Produit principal, qualité, performances', 'Prix'], ['Services associés (information, conseil, SAV…)', 'Efforts (pour s\'informer, acheter…)'], ['Éléments intangibles portés par la marque', 'Coût de changement, temps, risque perçu']])
    c.p('La valeur perçue peut dépendre d\'éléments objectifs (une voiture bien conçue est perçue fiable), mais des éléments objectifs qui n\'influencent pas la perception peuvent être inutiles ou à mieux valoriser. Exemple : l\'eau Cristaline à 0,15 €/l, Evian à 0,39 €/l (promesse de jeunesse), San Pellegrino à 0,75 €/l, Iceberg Water à 16 €/l.')
    c.p('Question essentielle : la perception qu\'a l\'entreprise de la valeur de son offre correspond-elle à celle des clients ? Chez un constructeur automobile, l\'effort porte sur l\'ingénierie et la fabrication, mais la valeur perçue dépend du design, de la marque et de la relation avec les concessionnaires.')
    c.h3('Deux compléments essentiels')
    c.ul(['La valeur perçue est toujours <b>relative</b> à la valeur perçue des offres concurrentes.', 'La valeur perçue <b>avant achat</b> explique la décision d\'achat ; la valeur perçue <b>après achat</b> (expérience) explique le rachat, c\'est-à-dire la fidélité.'])
    c.df('Satisfaction', 'Résultat de la comparaison entre les attentes (valeur perçue avant achat) et l\'expérience (après achat) ; elle entraîne en principe la fidélité.')
    c.df('Attrition', 'Défection ou abandon des clients, favorisés par l\'insatisfaction.')
    c.p('Conséquences : la valeur perçue n\'est pas la somme des bénéfices perçus, ni réductible à la seule qualité perçue ; et tous les clients n\'ont pas les mêmes attentes ni la même perception des coûts et des bénéfices.')
    c.h3('Accroître les bénéfices perçus')
    c.ul(['Créer un nouveau type de produit (innovation de concept).', 'Renforcer les performances du produit.', 'Améliorer l\'identité sensorielle (design, toucher, odeur, goût) ou le packaging.', 'Développer des services associés (accueil, information, conseil, paiement, maintenance, réclamation).', 'Accroître la qualité perçue (durabilité, moins de pannes).', 'Valoriser la marque (style, style de vie, prestige).'])
    c.h3('Réduire les coûts perçus')
    c.ul(['Baisser le prix, avec un risque sur la rentabilité.', 'Modifier la perception du prix : faire participer le client (libre-service, meubles Ikea à monter), baisser le prix de l\'équipement et se rattraper sur le consommable (imprimantes et cartouches), promotions ciblées.', 'Réduire les autres coûts : temps et efforts (accès à l\'information), coûts de fonctionnement et de maintenance, risque perçu (certifications).'])
    c.ex('Exemples du cours', '<p><b>Drive</b> : même prix qu\'en hypermarché, mais réduction du temps et de l\'effort. <b>Airbus A320neo</b> (lancé en décembre 2010, plus de 4 800 exemplaires vendus en 6 ans) : plus de bénéfices (+950 km d\'autonomie, +2 t de charge utile, nouvelle cabine) et moins de coûts (−15 % de carburant, −10 % d\'émissions).</p>')

    c.sec('III. Les deux facettes du marketing')
    c.tab(['Marketing codifié', 'Marketing intuitif'], [['Grandes entreprises, groupes internationaux (EDF, Procter & Gamble)', 'Entrepreneurs, jeunes entreprises'], ['Processus, outils et postes identifiés, écrits, partagés', 'Créativité et vision'],
                                                        ['Importance des panels et des études ; contexte compris par de nombreuses données', 'Peu d\'études, veille informelle ; contexte compris par l\'intuition et les contacts'], ['Peu de place à la créativité', 'La vision doit être validée par un minimum de données factuelles']])
    c.p('Organisation de la démarche : l\'orientation marketing s\'appuie sur l\'<b>audit</b> (analyse de la situation : marché, stratégie, segmentation), les <b>études de marché</b> (qualitatives, quantitatives, tests consommateurs) et le <b>marketing mix</b> (les 4P : produit, prix, place, promotion).')

    c.sec('IV. Les concepts clés')
    c.df('Produit', 'Tout ce qui peut être offert sur un marché de façon à satisfaire un besoin.')
    c.df('Besoin', 'Sentiment de manque ou de privation portant sur des éléments nécessaires (nourriture, air, eau, vêtements, abri…) ; les besoins préexistent, ils sont innés.')
    c.df('Désir', 'Matérialisation du besoin : il porte sur un objet spécifique ; le marketing, avec d\'autres forces sociales, influence les désirs mais ne crée pas les besoins.')
    c.df('Demande', 'Désir d\'acheter certains produits soutenu par un pouvoir et un vouloir d\'achat.')
    c.p('<b>Pyramide de Maslow</b> (hiérarchie des besoins, de la base au sommet) : physiologiques → sécurité → amour et appartenance → estime → accomplissement de soi.')
    c.p('Les besoins sont difficiles à cerner : besoins <b>exprimés</b> (ce que le client dit), <b>réels</b> (ce qu\'il veut dire), <b>latents</b> (ce à quoi il ne pense pas), <b>rêvés</b>, <b>profonds</b> (ce qui le motive secrètement). Il serait réducteur de s\'en tenir aux besoins exprimés.')
    c.tab(['Type de demande', 'Exemple'], [['Négative', 'Soins dentaires, assurance décès'], ['Absente ou latente', 'Produit ignoré ou qui n\'existe pas encore'], ['Irrégulière', 'Consommation irrégulière dans le temps'], ['Déclinante', 'Fax'], ['Soutenue', 'Nourriture'], ['Excessive', 'Circulation'], ['Indésirable', 'Drogue']])
    c.df('Échange', 'Situation qui suppose cinq conditions : deux parties, chacune possède quelque chose qui a de la valeur pour l\'autre, chacune peut communiquer et livrer, chacune est libre d\'accepter ou de refuser, et chacune juge l\'échange adapté à son problème.')

    c.sec('V. Le marché')
    c.df('Marché (en marketing)', 'Couple produit/client, c\'est-à-dire l\'ensemble de l\'offre et de la demande et de leurs acteurs (concurrents, distributeurs, consommateurs actuels et potentiels) ; il se définit toujours géographiquement.')
    c.p('Acteurs du marché : les <b>clients</b>, les <b>producteurs</b>, les <b>distributeurs</b>, les <b>influenceurs</b> (prescripteurs) et les <b>institutions</b> qui le régulent (exemple du cours : le médicament sur ordonnance, où le médecin prescrit, le pharmacien distribue et la sécurité sociale rembourse).')
    c.tab(['Type de marché', 'Définition', 'Exemples'], [['Principal', 'Produits directement concurrents (même technologie, même fonction)', 'L\'automobile'], ['Indirect', 'Produits de nature différente satisfaisant le même besoin (même fonction, marché élargi)', 'Compagnies aériennes, train'],
                                                          ['Générique', 'Tous les produits liés au besoin satisfait (autre circuit, autre marché)', 'La visioconférence'], ['Support', 'Produits dont la présence est nécessaire ou complémentaire à la vente ou à l\'usage', 'Le circuit routier, l\'essence']])
    c.df('Niche', 'Marché étroit protégé par des barrières à l\'entrée, sur lequel les entreprises sont relativement à l\'abri de la concurrence ; un petit marché n\'est une niche que s\'il est défendable.')
    c.ex('Cas GoPro', '<p>Caméra miniature, étanche et antichoc lancée en 2005 ; 6,6 millions d\'unités vendues en 2015. Le segment devient alors attractif pour les géants de l\'électronique, qui lancent des modèles concurrents : en 2016, chute des ventes, pertes et licenciements. Un marché devenu trop grand n\'est plus une niche défendable.</p>')
    c.df('Marché induit', 'Marché qui dépend directement d\'un autre marché (ventes liées) : les applications dépendent du marché des smartphones.')
    c.df('Marché captif', 'Marché où les clients sont contraints d\'acheter une marque ou un produit donné : l\'App Store pour les utilisateurs d\'iPhone.')
    c.p('On distingue les marchés <b>B to C</b> (particuliers) et <b>B to B</b> (professionnels) : un véhicule neuf sur deux est vendu à une entreprise en France, et on ne vend pas une voiture à Hertz comme à un particulier.')

    c.sec('VI. L\'environnement')
    c.df('Environnement', 'Ensemble des acteurs et domaines qui influencent, de près ou de loin, le marché sur lequel l\'entreprise agit.')
    c.tab(['Environnement', 'Questions à se poser'], [['Technologique', 'Quelles innovations peuvent modifier nos processus, nos offres, nos coûts, nos prix ?'], ['Écologique', 'Quels risques anticiper ? Quelles normes anti-pollution ? Quelle rareté des ressources ?'],
                                                      ['Démographique', 'Les tendances démographiques obligent-elles à revoir nos cibles ?'], ['Économique', 'Croissance, prix, effet de la conjoncture sur nos clients et nos concurrents ?'], ['Légal', 'Quelles réglementations à venir touchent nos clients, notre distribution, notre communication, nos prix ?']])

    c.sec('VII. L\'évolution du marketing et les optiques')
    c.tab(['Économie', 'Rapport offre/demande', 'Qui domine', 'Rôle du marketing'], [
        ['De production', 'Offre < demande', 'L\'entreprise productrice', 'Produire suffit ; entreprise introvertie, dominée par les ingénieurs et le contrôle des coûts'],
        ['De distribution', 'Offre = demande', 'Le vendeur', 'Savoir vendre : promotion, publicité ; naissance des études de marché'],
        ['De marché', 'Offre > demande', 'Le consommateur', 'S\'adapter, segmenter ; entreprise extravertie'],
        ['D\'environnement', 'Offre > demande', 'Le milieu', 'Dépendance à l\'environnement technologique, économique, écologique, sociologique, légal']])
    c.p('Années 1970 : densité du tissu industriel, cycles de vie plus courts, consommateurs plus instruits, le prix n\'est plus la variable fondamentale de la demande. Aujourd\'hui : rendements croissants, délocalisation et dématérialisation, économie de l\'information ; société <b>postmoderne</b> (individualisme, recours à l\'éthique et à l\'écologie). Réponses : compétitivité, <b>veille</b> (technologique, concurrentielle, commerciale, environnementale), <b>micro-marketing</b> et marketing direct.')
    c.h3('Les quatre optiques de l\'activité marketing')
    c.df('Optique production', 'Quand la demande excède l\'offre : le consommateur choisit selon le prix et la disponibilité ; priorité à la capacité de production et à la distribution.')
    c.df('Optique produit', 'Domaine où la technologie domine : le consommateur préfère le produit le plus performant ; priorité à la qualité du produit.')
    c.df('Optique vente', 'Le consommateur n\'achète pas assez de lui-même : l\'entreprise doit stimuler l\'intérêt (partis politiques, vendeurs de meubles, promoteurs immobiliers, certaines assurances).')
    c.df('Optique marketing', 'Quatre idées : un choix de marché (ciblage), une orientation centrée sur le client, un marketing coordonné diffusé à tout le personnel et la rentabilité (profit, intérêt général ou service public selon l\'organisation).')
    return c


def ch2():
    c = Cours()
    c.sec('I. Le vocabulaire de la stratégie')
    c.tab(['Terme', 'Définition'], [['Mission', 'Propos fondamental de l\'organisation, en rapport avec les valeurs et les attentes des parties prenantes'], ['Vision (intention stratégique)', 'État futur souhaité : l\'aspiration de l\'organisation'], ['But', 'Déclaration générale d\'intention'],
                                     ['Objectif', 'Quantification (si possible) ou intention plus précise'], ['Compétences fondamentales', 'Ressources, procédés et aptitudes qui permettent d\'obtenir un avantage concurrentiel'], ['Stratégie', 'Orientation à long terme'], ['Contrôle', 'Évaluation de l\'efficacité de la stratégie et des réalisations, modification si nécessaire']])
    for t, d in (('Mission', 'Propos fondamental de l\'organisation, en rapport avec les valeurs et les attentes des parties prenantes.'), ('Compétences fondamentales', 'Ressources, procédés et aptitudes qui permettent d\'obtenir un avantage concurrentiel.'), ('Stratégie', 'Orientation à long terme de l\'organisation.')):
        c.df(t, d, show=False)
    c.ex('Exemple : British Airways', '<p><b>Mission</b> : être la meilleure et la plus prospère des compagnies, construire la première alliance globale. <b>Vision</b> : une qualité inégalée pour être toujours le premier choix des clients. <b>Compétence fondamentale</b> : « n\'importe qui peut faire voler un avion, mais peu d\'organisations excellent dans le service aux clients » (difficile à copier). <b>Stratégie</b> : rester à l\'avant-garde de la globalisation (Asie-Pacifique, Europe, Amérique du Nord concentrent plus de 80 % du trafic) et garder la priorité à la qualité de service.</p>')
    c.sec('II. Marketing stratégique et marketing opérationnel')
    c.df('Marketing stratégique', 'Orientations générales de l\'entreprise : positionner l\'entreprise, ses marques et ses gammes, fixer à moyen et long terme ses orientations de développement et énoncer un plan stratégique clair ; il relève de la direction.')
    c.df('Marketing opérationnel', 'Ensemble des tactiques au service de la stratégie : communication clients et prospects, appui à la force de vente, lancement de produits, suivi du marché (CA, volumes, PdM), actions avec fournisseurs et distributeurs.')
    c.h3('La démarche marketing : le modèle SOSTAC (Paul Smith)')
    c.tab(['Étape', 'Contenu'], [['<b>S</b>ituation analysis', 'Comprendre le contexte : macro-environnement (PESTEL), micro-environnement (fournisseurs, clients, distributeurs, concurrents, actionnaires), opportunités, menaces, forces, faiblesses'],
                                 ['<b>O</b>bjectives', 'Objectifs <b>SMART</b> : spécifiques, mesurables, ambitieux, réalistes, inscrits dans le temps'], ['<b>S</b>trategy', 'Segmentation, ciblage, positionnement'], ['<b>T</b>actics', 'Marketing mix : produit, prix, distribution, communication'],
                                 ['<b>A</b>ctions', 'Passage à l\'action : former et informer la force de vente'], ['<b>C</b>ontrol', 'Confronter prévisions et réalité, contrôler le retour sur investissement des dépenses marketing']])
    c.df('Segmentation', 'Division d\'un marché hétérogène en sous-groupes homogènes selon des critères propres au secteur.')
    c.df('Ciblage', 'Choix d\'un ou plusieurs segments (cibles) sur lesquels l\'entreprise concentre ses efforts et adapte son marketing opérationnel.')
    c.df('Positionnement', 'Image que l\'entreprise veut donner au marché et à ses partenaires.')
    c.df('Objectif SMART', 'Objectif spécifique au contexte, mesurable (chiffré), ambitieux, réaliste et inscrit dans le temps.')

    c.sec('III. Le diagnostic stratégique')
    c.p('Préalable indispensable : une <b>étude du marché</b> (et de la concurrence) et une <b>étude des ressources internes</b>, pour assurer la cohérence entre le marché, l\'environnement concurrentiel et les aspirations et ressources de l\'entreprise. Analyse externe (état des lieux, scénarios) + analyse interne (capacité stratégique) → diagnostic et position stratégique.')
    c.p('Nature de l\'environnement : simple et statique → analyse historique, prévision ; dynamique → planification par scénarios ; complexe → décentralisation, expérience et apprentissage.')
    c.h3('L\'analyse PESTEL (macro-environnement)')
    c.df('PESTEL', 'Grille d\'analyse du macro-environnement : facteurs politiques, économiques, socioculturels, technologiques, écologiques et légaux.')
    c.tab(['Facteur', 'Exemples du cours'], [['Politique / légal', 'Lois sur les monopoles, protection de l\'environnement, politique fiscale, commerce extérieur, droit du travail, stabilité gouvernementale'], ['Économique', 'Cycles, revenu disponible, PNB, politique monétaire, inflation, taux d\'intérêt, chômage, coût de l\'énergie'],
                                             ['Socioculturel', 'Démographie, distribution des revenus, mobilité sociale, modes de vie, rapport aux loisirs et au travail, éducation'], ['Technologique', 'R&D publique, investissements, découvertes, vitesse des transferts, taux d\'obsolescence']])
    c.h3('Le SWOT')
    c.df('SWOT', 'Diagnostic stratégique croisant l\'analyse interne (forces, faiblesses) et l\'analyse externe (opportunités, menaces), développé en 1965 par Learned, Christensen, Andrews et Guth (Harvard Business School).')
    c.p('Raisonnement en 5 phases : (1) évaluation externe (menaces, opportunités, facteurs clés de succès) ; (2) évaluation interne (forces, faiblesses, compétences distinctives) ; (3) recensement des possibilités d\'action ; (4) valeurs de l\'environnement (RSE) et valeurs managériales ; (5) formulation de la stratégie.')
    c.tab(['', 'Opportunités', 'Menaces'], [['<b>Forces</b>', 'Stratégie d\'<b>attaque</b> (en retirer le maximum)', 'Stratégie d\'<b>ajustement</b> (rétablir les points forts)'], ['<b>Faiblesses</b>', 'Stratégie de <b>défense</b> (contourner les difficultés)', 'Stratégie de <b>survie</b> (surveiller étroitement la concurrence)']])
    c.h3('Les 5 + 1 forces concurrentielles de Porter')
    c.df('Modèle des 5 (+1) forces de Porter', 'Outil qui analyse l\'intensité concurrentielle d\'un secteur ou d\'un domaine d\'activité stratégique (DAS) : nouveaux entrants, produits de substitution, pouvoir des clients, pouvoir des fournisseurs, rivalité entre concurrents, plus les contraintes réglementaires des pouvoirs publics.')
    c.df('Domaine d\'activité stratégique (DAS)', 'Sous-ensemble homogène de l\'activité de l\'entreprise (couple produit/marché) sur lequel on analyse la concurrence et on définit une stratégie.')
    c.tab(['Force', 'Elle dépend de…'], [['Nouveaux entrants', 'Économies d\'échelle, besoins en capitaux, coûts de changement pour le client, accès à la distribution et à la technologie, fidélité à la marque, riposte des acteurs en place, réglementation'],
                                         ['Produits de substitution', 'Qualité, volonté des acheteurs de substituer, prix et performances relatifs, coûts de changement'], ['Pouvoir des fournisseurs', 'Concentration, force de la marque, rentabilité, menace d\'intégration en aval, rôle de la qualité, coûts de remplacement'],
                                         ['Pouvoir des clients', 'Concentration des acheteurs, différenciation des produits, rentabilité des acheteurs, menace d\'intégration, coûts de changement'], ['Rivalité', 'Structure des coûts (coûts fixes élevés → guerre des prix), nombre et taille des concurrents, différenciation, coûts de changement, objectifs agressifs, barrières à la sortie'],
                                         ['Pouvoirs publics (+1)', 'Agrément ou licence (téléphonie mobile), subventions, contraintes de sécurité (alimentation), interdictions']])
    c.p('Exemple du cours : l\'<b>hexagone sectoriel</b> de l\'industrie du livre en 2015 note chaque force de 0 à 10 : rivalité (Hachette, Bertelsmann…), nouveaux entrants (Google Books, Amazon), fournisseurs (imprimeurs, auteurs), acheteurs (librairies, grande distribution, sites en ligne), substituts (livre électronique, liseuses), État (ministère de la Culture, Commission européenne).')

    c.sec('IV. La maturité du marché : la matrice d\'ADL')
    c.df('Matrice ADL (Arthur D. Little)', 'Matrice qui croise la maturité de l\'activité (démarrage, croissance, maturité, déclin) et la position concurrentielle (marginale à dominante) pour apprécier rentabilité, besoins de financement et risques.')
    c.tab(['Position concurrentielle', 'Démarrage / croissance', 'Maturité / déclin'], [['Forte / dominante', 'Bonne rentabilité, fort besoin de cash', 'Bonne rentabilité, faible besoin de cash'], ['Faible / marginale', 'Faible rentabilité, fort besoin de cash', 'Faible rentabilité, faible besoin de cash']])
    c.p('Lecture : les besoins financiers et le risque sectoriel diminuent avec la maturité ; la rentabilité et la baisse du risque concurrentiel augmentent avec la position. Deux idées : (1) une <b>PdM élevée</b> donne un avantage concurrentiel et amplifie les effets d\'expérience et d\'échelle ; (2) un <b>marché en croissance</b> demande des liquidités pour financer la croissance.')

    c.sec('V. Le portefeuille de produits : BCG et McKinsey')
    c.df('Matrice BCG', 'Matrice du Boston Consulting Group qui classe les produits selon la croissance du marché et la part de marché : dilemmes, stars, vaches à lait, poids morts.')
    c.tab(['Case', 'Croissance / PdM', 'Caractéristiques', 'Objectif'], [
        ['Dilemmes', 'Forte croissance, PdM faible', 'Rentabilité faible, besoins financiers +++, support marketing +++ ; peuvent devenir des stars ou des poids morts', 'Investir et relancer (ou laisser aller)'],
        ['Stars', 'Forte croissance, PdM forte', 'Leaders ; rentabilité forte, besoins financiers ++ ; vaches à lait de demain', 'Soutenir'],
        ['Vaches à lait', 'Faible croissance, PdM forte', 'Rentabilité très forte, besoins faibles ; financent la R&D et les autres produits', 'Rentabiliser (récolte optimum)'],
        ['Poids morts', 'Faible croissance, PdM faible', 'Produits en déclin, risque d\'hémorragie financière', 'Abandon']])
    c.df('Vache à lait', 'Produit à forte part de marché sur un marché à faible croissance : il fournit des liquidités et consomme peu de capitaux.')
    c.df('Dilemme', 'Produit à faible part de marché sur un marché en forte croissance : il demande des capitaux pour devenir une star, sinon il deviendra un poids mort.')
    c.df('Matrice McKinsey', 'Matrice qui croise l\'intérêt stratégique (attrait) du marché et la position concurrentielle en 3 × 3 cases, de « maintenir sa position de leader » à « abandon ».')
    c.tab(['Position ↓ / intérêt →', 'Fort', 'Moyen', 'Faible'], [['Forte', 'Maintenir sa position de leader', '« Surfer » sur la vague', 'Rentabiliser'], ['Moyenne', 'Améliorer sa position', 'Rentabiliser, optimiser', 'Abandon sélectif'], ['Faible', 'R&D… ou abandon ?', 'Abandon sélectif / progressif', 'Abandon']])
    c.p('Finalités de l\'analyse du portefeuille : exploitation optimum des produits, définition rationnelle des stratégies, appréciation des besoins financiers et de la rentabilité, équilibre entre les activités.')
    c.warn('Ces matrices sont des <b>outils d\'aide à la décision</b>, pas des recettes : elles ont des faiblesses, le discernement reste de rigueur.')

    c.sec('VI. Les stratégies de développement : croissance interne')
    c.p('Quatre stratégies de croissance interne : domination par les coûts, spécialisation, différenciation, innovation.')
    c.h3('1. La domination par les coûts')
    c.df('Domination par les coûts', 'Stratégie fondée sur la maîtrise absolue des coûts de production et de la logistique (effet d\'expérience et économies d\'échelle) pour être le producteur le moins cher.')
    c.df('Effet d\'expérience', 'Le coût unitaire décroît d\'un pourcentage constant chaque fois que la production cumulée double ; causes : apprentissage, modifications des produits ou de la fabrication, économies d\'échelle.')
    c.df('Économie d\'échelle', 'Baisse du coût unitaire quand le nombre d\'unités par série augmente, par dilution des frais fixes.')
    c.p('Enchaînement : effet d\'expérience → baisse des coûts → avantage concurrentiel → prise de parts de marché → effet de volume et économies d\'échelle (cercle vertueux).')
    c.ul(['<b>Trois avantages</b> : mieux placée en cas de guerre des prix ; dissuade les concurrents moins performants ; souplesse de négociation en amont et en aval.', '<b>Flexibilité prix</b> : prix de pénétration au lancement, prix réactifs en croissance, pression sur les prix mais profitabilité en maturité, flexibilité en déclin.',
          '<b>Facteurs limitants</b> : connaître parfaitement les facteurs clés de succès, capacité d\'investissement, capitaliser l\'effet d\'expérience.', '<b>Risques</b> : changement technologique qui annule l\'avantage, concurrent plus performant, sur-standardisation, myopie sur les évolutions du marché.',
          '<b>Facteurs clés de réussite</b> : extrême rigueur financière, forte organisation technique, maîtrise de la production.'])
    c.df('Délocalisation', 'Faire produire au moins cher dans des pays à faibles coûts pour vendre dans les pays à fort pouvoir d\'achat ; une des solutions de la domination par les coûts, qui suppose une main-d\'œuvre compétente et une faisabilité logistique.')
    c.p('Inconvénients de la délocalisation : chômage en Occident (et baisse du pouvoir d\'achat), cantonnement des pays à bas coûts dans des tâches à faible valeur ajoutée.')
    c.h3('2. La spécialisation (stratégie de niche)')
    c.df('Spécialisation (niche)', 'Stratégie par laquelle l\'entreprise s\'assigne une cible restreinte et adapte son offre pour satisfaire mieux que les autres certaines exigences de ces clients.')
    c.ul(['Exigences spécifiques : qualité du service, de la formation, normalisation, adaptation du matériel.', '<b>Avantages</b> : prix plus élevés, fidélisation, limitation des nouveaux entrants, développement des compétences.', '<b>Facteurs clés</b> : structure légère, marketing et R&D performants, capacité à employer des ressources extérieures.',
          '<b>Risques</b> : différentiel de prix trop important, obsolescence, dépendance au segment, érosion des différences avec les autres segments ; difficulté à financer les investissements structurels.'])
    c.h3('3. La différenciation')
    c.df('Différenciation', 'Stratégie qui distingue l\'offre par une ou plusieurs variables du marketing mix ; la différence doit être perçue et valorisée par le marché.')
    c.ul(['<b>Avantages</b> : prix plus élevé, fidélisation, entrée plus difficile pour un nouvel entrant.', '<b>Limites</b> : maîtrise marketing (et parfois technologique), anticipation des besoins, coordination R&D-production-marketing.',
          '<b>Modes</b> : le <b>produit</b> (fonctionnalité, fiabilité, performance, réparabilité, conformité, style, durabilité, design) ; le <b>service</b> avant la vente (aide à la définition des besoins, conseils, démonstrations, ateliers) et après la vente (installation, formation, maintenance, télédépannage, pièces) ; le <b>personnel</b> (compétence, fiabilité, courtoisie, serviabilité, crédibilité, écoute) ; l\'<b>accès au produit</b> (couverture du territoire, expertise du réseau) ; l\'<b>image</b> (identité voulue vs perception du marché).',
          '<b>Facteurs clés</b> : excellente organisation, marketing et R&D très performants, créativité supérieure.', '<b>Risques</b> : banalisation du marché, imitations, différentiel de prix trop élevé.'])
    c.h3('4. L\'innovation')
    c.df('Innovation (stratégie)', 'Développement et exploitation des ressources internes et de la R&D : amélioration de l\'existant ou innovation pure (nouveaux produits).')
    c.p('<b>Conclusion</b> : ces stratégies érigent des barrières à l\'entrée, mais restent liées à la dynamique du marché, d\'où la nécessité éventuelle d\'une croissance externe.')

    c.sec('VII. Croissance externe, impartition et alliances')
    c.df('Croissance externe', 'Ensemble des opérations d\'acquisition d\'une autre entreprise (rachat) ou de fusion pour accélérer son développement.')
    c.ul(['<b>Motifs</b> : s\'implanter à l\'étranger, éliminer un concurrent, acquérir des compétences (gagner du temps), sécuriser les débouchés (<b>intégration en aval</b>) ou les approvisionnements (<b>intégration en amont</b>).', '<b>Avantages</b> : leadership et CA rapides, portefeuille de compétences élargi, structure du marché recomposée, taille critique et économies d\'échelle, pouvoir de négociation accru.',
          '<b>Inconvénients</b> : engagement difficilement réversible, capitaux considérables, risques d\'inadaptation des équipes, inquiétudes des collaborateurs, montage complexe et coûteux.'])
    c.df('Intégration verticale', 'Rachat d\'un fournisseur (intégration en amont) ou d\'un client ou distributeur (intégration en aval) pour maîtriser la filière.')
    c.df('Impartition', 'Manœuvre entre partenaires aux potentiels complémentaires (« faire ou faire faire ? ») : sous-traitance, franchise, concession ; on conserve les activités créatrices de valeur.')
    c.tab(['Technique', 'Principe'], [['Sous-traitance', 'Une entreprise demande à une autre de réaliser tout ou partie de ce qu\'elle devait fournir à ses clients'], ['Franchise', 'Le franchiseur accorde une licence (enseigne, marque, notoriété) et une assistance au franchisé, contre des droits'], ['Concession', 'Le concédant (fabricant) accorde au concessionnaire (commerçant indépendant) une exclusivité de revente sur une zone']])
    c.p('Motivations de l\'impartition : réduction des coûts fixes, concentration des investissements, flexibilité, réduction de la complexité, nécessité pour certaines opérations.')
    c.df('Alliance', 'Association entre entreprises concurrentes ou non pour obtenir des effets d\'échelle, une position internationale, l\'accès à une zone, un savoir-faire ou promouvoir un standard.')
    c.df('Avantage concurrentiel', 'Avantage temporaire, sorte de monopole de situation : performance supérieure due à la position de l\'entreprise face à la concurrence (définition du corrigé du cas L&L).')
    c.df('Facteur clé de succès', 'Élément de l\'offre ou de l\'organisation qu\'il faut maîtriser pour réussir dans un secteur.')
    return c


def cycle_svg():
    data = {'A': [2000, 3000, 3800, 4300, 4500], 'B': [200, 360, 540, 960, 1570], 'C': [None, None, None, 250, 350], 'D': [1540, 1600, 1480, 1250, 1150]}
    lab = ['N-4', 'N-3', 'N-2', 'N-1', 'N']
    p = Plot(4.4, 5000, 'Année', 'Ventes', xmin=-0.3).axes(xticks=range(5), yticks=range(0, 5001, 1000), fmt=lambda v: str(int(v)), xfmt=lambda v: lab[int(v)])
    cols = {'A': COL[0], 'B': COL[2], 'C': COL[3], 'D': COL[1]}
    names = {'A': 'A — maturité', 'B': 'B — croissance', 'C': 'C — lancement', 'D': 'D — déclin'}
    for k, v in data.items():
        pts = [(i, y) for i, y in enumerate(v) if y is not None]
        p.curve(pts, cols[k], label=names[k], lpos=(pts[-1][0] - 0.1, pts[-1][1] + 180), anchor='end')
        for x, y in pts:
            p.point(x, y, cols[k], r=3)
    return p.svg()


def cycle_theorique():
    import math
    p = Plot(10, 10, 'Temps', 'Ventes', w=520, h=300).axes()
    f = lambda t: 8.5 * math.exp(-((t - 5.2) ** 2) / 6)
    p.fn(f, 0.3, 9.8, color=COL[0], width=2.4)
    for x, t in ((1, 'Lancement'), (3.2, 'Croissance'), (5.4, 'Maturité'), (8, 'Déclin')):
        p.text(x, 9.4, t, '#f7a26a', 11, 'middle', 700)
    for x in (2.1, 4.2, 6.6):
        p.curve([(x, 0), (x, 9)], '#4d5874', 1, dash='4 4')
    return p.svg()


def experience_svg():
    import math
    p = Plot(64, 105, 'Production cumulée', 'Coût unitaire', w=520, h=300).axes(xticks=[1, 2, 4, 8, 16, 32, 64], yticks=[0, 20, 40, 60, 80, 100], fmt=lambda v: str(int(v)))
    b = math.log(0.8, 2)
    p.fn(lambda q: 100 * q ** b, 1, 64, color=COL[2], label='Courbe d\'expérience à 80 % (illustration)', lpos=(20, 60))
    for q in (1, 2, 4, 8, 16, 32, 64):
        p.point(q, 100 * q ** b, '#e8eaf2', fr(100 * q ** b, 1) if q < 16 else None, dx=4, dy=-8, r=3)
    return p.svg()


def porter_svg():
    return boxes(520, 360, [
        (185, 140, 150, 80, 'Rivalité', ['entre concurrents', 'existants'], COL[4]), (185, 10, 150, 70, 'Substituts', ['nouveaux usages,', 'nouvelle technologie'], COL[3]),
        (185, 280, 150, 70, 'Nouveaux entrants', ['barrières à l\'entrée'], COL[2]), (10, 140, 140, 80, 'Clients', ['pouvoir de', 'négociation'], COL[0]),
        (370, 140, 140, 80, 'Fournisseurs', ['pouvoir de', 'négociation'], COL[1]), (10, 280, 140, 70, '+1 Pouvoirs publics', ['lois, licences, normes'], COL[5])],
        arrows=[(260, 82, 260, 138, ''), (260, 278, 260, 222, ''), (152, 180, 183, 180, ''), (368, 180, 337, 180, ''), (150, 290, 200, 222, '')])


def valeur_svg():
    return boxes(520, 300, [
        (10, 10, 170, 115, 'Bénéfices perçus', ['produit principal', 'performances, qualité', 'services associés', 'marque'], COL[2]),
        (10, 170, 170, 115, 'Coûts perçus', ['prix, efforts', 'temps, coût de changement', 'risque perçu'], COL[1]),
        (205, 110, 120, 70, 'VALEUR PERÇUE', ['(avant achat)', 'vs offres concurrentes'], COL[0]),
        (350, 10, 160, 70, 'Satisfaction', ['→ intention de rachat', 'fidélité'], COL[2]), (350, 110, 160, 70, 'Expérience', ['valeur perçue', 'après achat'], COL[3]),
        (350, 210, 160, 75, 'Insatisfaction', ['→ probabilité de', 'défection (attrition)'], COL[4])],
        arrows=[(180, 70, 205, 120, ''), (180, 225, 205, 170, ''), (325, 145, 348, 145, ''), (430, 108, 430, 82, ''), (430, 182, 430, 208, '')])


def sostac_svg():
    items = []
    arr = []
    labels = [('S', 'Situation', 'analyse'), ('O', 'Objectifs', 'SMART'), ('S', 'Stratégie', 'segm. · cible · posit.'), ('T', 'Tactiques', 'marketing mix 4P'), ('A', 'Actions', 'force de vente'), ('C', 'Contrôle', 'ROI, écarts')]
    for i, (l, t, s) in enumerate(labels):
        x = 10 + i * 85
        items.append((x, 40, 75, 90, l, [t, s], COL[i % len(COL)]))
        if i:
            arr.append((x - 10, 85, x, 85, ''))
    return boxes(520, 170, items, arr)


def matiere():
    c1, c2 = ch1(), ch2()
    bcg = matrix(520, 330, [[('Dilemmes', 'rentabilité faible\nbesoins +++ · investir ou relancer', COL[3]), ('Stars', 'rentabilité forte\nbesoins ++ · soutenir', COL[0])],
                            [('Poids morts', 'rentabilité faible\nbesoins faibles · abandon', COL[4]), ('Vaches à lait', 'rentabilité très forte\nbesoins faibles · rentabiliser', COL[2])]],
                 'Part de marché (croissante vers la droite, comme dans ton cours)', 'Croissance du marché', xl=('faible', 'forte'), yl=('faible', 'forte'))
    adl = matrix(520, 330, [[('Forte position', 'bonne rentabilité\nfort besoin de cash', COL[0]), ('Forte position', 'bonne rentabilité\nfaible besoin de cash', COL[2])],
                            [('Faible position', 'faible rentabilité\nfort besoin de cash', COL[3]), ('Faible position', 'faible rentabilité\nfaible besoin de cash', COL[4])]],
                 'Maturité de l\'activité (démarrage, croissance → maturité, déclin)', 'Position concurrentielle', xl=('démarrage / croissance', 'maturité / déclin'), yl=('marginale', 'dominante'))
    mck = matrix(520, 330, [[('Maintenir', 'position de leader', COL[2]), ('« Surfer »', 'sur la vague', COL[2]), ('Rentabiliser', '', COL[3])],
                            [('Améliorer', 'sa position', COL[2]), ('Rentabiliser', 'optimiser', COL[3]), ('Abandon', 'sélectif', COL[4])],
                            [('R&D', 'ou abandon ?', COL[3]), ('Abandon', 'sélectif / progressif', COL[4]), ('Abandon', '', COL[4])]],
                 'Intérêt stratégique (fort → faible)', 'Position concurrentielle', xl=('fort', 'faible'), yl=('faible', 'forte'))
    swot = matrix(520, 300, [[('Attaque', 'forces × opportunités\nen retirer le maximum', COL[2]), ('Ajustement', 'forces × menaces\nrétablir les points forts', COL[3])],
                             [('Défense', 'faiblesses × opportunités\ncontourner les difficultés', COL[0]), ('Survie', 'faiblesses × menaces\nsurveiller la concurrence', COL[4])]],
                  'Diagnostic externe : opportunités | menaces', 'Diagnostic interne', xl=('opportunités', 'menaces'), yl=('faiblesses', 'forces'))
    chs = [
        dict(id='marketing-1', num=1, titre='Le marketing : définitions, valeur perçue, marché et environnement', sous='Définitions (AMA, Mercator) · valeur perçue · besoins, désirs, demande · marchés · environnement · optiques',
             desc='Ce qu\'est le marketing, comment se crée la valeur perçue, les concepts clés (besoin, désir, demande, échange), les types de marchés, l\'environnement et l\'évolution vers l\'optique marketing.',
             tags=['Valeur perçue', 'Maslow', 'Marché', 'Optiques'], sources=SRC1, cours=c1.html, notions=c1.notions,
             quiz=[dict(type='qcm', q='Selon le Mercator, le marketing vise une offre dont la valeur perçue est…', opts=['durablement supérieure à celle des concurrents', 'la moins chère du marché', 'égale à celle des concurrents', 'fixée par l\'État'], ans=0, exp='Définition du Mercator citée dans le cours.'),
                   dict(type='qcm', q='La valeur perçue est le rapport entre…', opts=['bénéfices perçus et coûts perçus', 'prix et coût de revient', 'qualité et quantité', 'ventes et parts de marché'], ans=0, exp='Ce que j\'obtiens (produit) pour ce que je donne (prix, efforts, temps, risque).'),
                   dict(type='vf', q='Le marketing crée les besoins.', ans=False, exp='Les besoins préexistent ; le marketing influence les désirs.'),
                   dict(type='qcm', q='Qu\'est-ce que l\'attrition ?', opts=['La défection des clients insatisfaits', 'La baisse des prix', 'La hausse des coûts', 'La fidélisation'], ans=0, exp='Terme du jargon marketing pour l\'abandon.'),
                   dict(type='qcm', q='Le succès du drive vient surtout…', opts=['de la réduction du temps et de l\'effort', 'de prix plus bas qu\'en hypermarché', 'de nouveaux produits', 'de la publicité'], ans=0, exp='Prix identiques, mais moins de temps et d\'effort pour le client.'),
                   dict(type='qcm', q='Les compagnies aériennes par rapport au train : quel type de marché ?', opts=['Marché indirect', 'Marché principal', 'Marché support', 'Marché captif'], ans=0, exp='Produits de nature différente, même fonction.'),
                   dict(type='qcm', q='L\'App Store pour les utilisateurs d\'iPhone illustre un marché…', opts=['induit et captif', 'générique', 'de niche', 'support'], ans=0, exp='Il dépend du marché des smartphones et les clients sont contraints.'),
                   dict(type='qcm', q='Une niche suppose…', opts=['des barrières à l\'entrée qui la rendent défendable', 'un marché de masse', 'un produit bon marché', 'l\'absence de clients'], ans=0, exp='Un petit marché n\'est pas forcément une niche.'),
                   dict(type='qcm', q='Économie où l\'offre est inférieure à la demande :', opts=['économie de production', 'économie de marché', 'économie d\'environnement', 'économie de distribution'], ans=0, exp='Il suffit de produire, l\'entreprise domine le client.'),
                   dict(type='qcm', q='Quelle optique convient aux partis politiques ou aux assurances décès selon le cours ?', opts=['Optique vente', 'Optique produit', 'Optique production', 'Optique marketing'], ans=0, exp='Le consommateur n\'achète pas spontanément : il faut stimuler l\'intérêt.'),
                   dict(type='qcm', q='Les soins dentaires relèvent d\'une demande…', opts=['négative', 'soutenue', 'excessive', 'irrégulière'], ans=0, exp='Exemple du cours.'),
                   dict(type='vf', q='La valeur perçue après achat explique surtout la décision de rachat.', ans=True, exp='L\'avant-achat explique l\'achat ; l\'après-achat la fidélité.'),
                   dict(type='qcm', q='Au sommet de la pyramide de Maslow :', opts=['L\'accomplissement de soi', 'Les besoins physiologiques', 'La sécurité', 'L\'appartenance'], ans=0, exp='Physiologie → sécurité → appartenance → estime → accomplissement.'),
                   dict(type='qcm', q='Laquelle n\'est PAS une des quatre idées de l\'optique marketing ?', opts=['Maximiser la capacité de production', 'Choix de marché', 'Orientation client', 'Marketing coordonné'], ans=0, exp='La 4ᵉ idée est la rentabilité.')],
             methode=ul(['Toujours raisonner en <b>valeur perçue</b> : que gagne le client, que lui coûte-t-il, par rapport aux concurrents ?', 'Pour un cas : identifier le marché (principal, indirect, générique, support), les acteurs et l\'environnement (grille PESTEL).', 'Illustrer chaque notion par un exemple (Evian, Nespresso, drive, GoPro…).']),
             fiches=[dict(q='Cinq niveaux de besoins à explorer ?', a='Exprimés, réels, latents, rêvés, profonds.'), dict(q='Cinq conditions de l\'échange ?', a='Deux parties ; chacune a quelque chose de valeur pour l\'autre ; chacune peut communiquer et livrer ; chacune est libre d\'accepter ou de refuser ; chacune juge l\'échange adapté à son problème.'),
                     dict(q='Cinq acteurs du marché ?', a='Clients, producteurs, distributeurs, influenceurs, institutions de régulation.'), dict(q='Comment réduire les coûts perçus ?', a='Baisser le prix, modifier la perception du prix (libre-service, consommables, promotions), réduire temps, efforts, maintenance et risque.')],
             carte=dict(core='Le marketing', branches=[dict(t='Définitions', items=['AMA : créer, communiquer, délivrer de la valeur', 'Mercator : adaptation, valeur perçue supérieure', 'Adaptation, valeur, durée']),
                                                        dict(t='Valeur perçue', items=['Bénéfices / coûts perçus', 'Relative aux concurrents', 'Avant achat → achat', 'Après achat → fidélité / attrition']),
                                                        dict(t='Concepts clés', items=['Besoin → désir → demande', 'Maslow', 'Types de demande', 'Échange (5 conditions)']),
                                                        dict(t='Marché', items=['Principal, indirect, générique, support', 'Niche défendable', 'Induit, captif', 'B to C / B to B']),
                                                        dict(t='Environnement', items=['Technologique, écologique', 'Démographique, économique, légal']), dict(t='Optiques', items=['Production', 'Produit', 'Vente', 'Marketing'])],
                        schemas=[dict(t='De la valeur à la fidélité', steps=['Bénéfices − coûts perçus', 'Valeur perçue avant achat', 'Achat', 'Expérience', 'Satisfaction → rachat']), dict(t='Évolution du marketing', steps=['Production (O < D)', 'Distribution (O = D)', 'Marché (O > D)', 'Environnement'])]),
             liens=[dict(ch='marketing-2', pourquoi='L\'analyse de l\'environnement et du marché alimente le diagnostic stratégique (PESTEL, Porter, SWOT).'),
                    dict(ch='micro-0', pourquoi='Le marché comme confrontation de l\'offre et de la demande ; en marketing, le marché est un couple produit/client défini géographiquement.'),
                    dict(ch='micro-1', pourquoi='Demande = désir + pouvoir d\'achat : le revenu et les prix (contrainte budgétaire, élasticités) déterminent la demande solvable.')]),
        dict(id='marketing-2', num=2, titre='Le marketing stratégique : diagnostic, portefeuille et stratégies de développement', sous='SOSTAC · PESTEL · SWOT · Porter 5+1 · ADL · BCG · McKinsey · coûts, spécialisation, différenciation, innovation · croissance externe',
             desc='De la démarche SOSTAC au diagnostic (PESTEL, SWOT, 5+1 forces), l\'analyse du portefeuille (ADL, BCG, McKinsey) et les stratégies de développement internes et externes.',
             tags=['SWOT', 'Porter', 'BCG', 'Différenciation'], sources=SRC2, cours=c2.html, notions=c2.notions,
             quiz=[dict(type='qcm', q='Dans la matrice BCG, un produit à forte PdM sur un marché à faible croissance est…', opts=['une vache à lait', 'une star', 'un dilemme', 'un poids mort'], ans=0, exp='Il génère des liquidités et consomme peu de capitaux.'),
                   dict(type='qcm', q='Objectif associé aux stars :', opts=['les soutenir', 'les abandonner', 'les récolter immédiatement', 'les vendre'], ans=0, exp='Elles seront les vaches à lait de demain.'),
                   dict(type='qcm', q='Que signifie le « O » de SOSTAC ?', opts=['Objectives (objectifs SMART)', 'Opportunities', 'Organisation', 'Offre'], ans=0, exp='Situation, Objectives, Strategy, Tactics, Actions, Control.'),
                   dict(type='qcm', q='La « +1 » force de Porter du cours est…', opts=['les contraintes réglementaires des pouvoirs publics', 'la force de vente', 'les actionnaires', 'la R&D'], ans=0, exp='Lois, licences, normes, subventions.'),
                   dict(type='qcm', q='Forces × menaces dans la matrice SWOT du cours :', opts=['stratégie d\'ajustement', 'stratégie d\'attaque', 'stratégie de survie', 'stratégie de défense'], ans=0, exp='Rétablir les points forts.'),
                   dict(type='qcm', q='L\'effet d\'expérience : le coût unitaire baisse d\'un % constant chaque fois que…', opts=['la production cumulée double', 'le prix double', 'la taille d\'une série augmente', 'les salaires baissent'], ans=0, exp='L\'effet d\'échelle, lui, porte sur la taille des séries.'),
                   dict(type='qcm', q='Quel est un risque de la domination par les coûts ?', opts=['Un changement technologique qui annule l\'avantage', 'Des prix trop élevés', 'Une dépendance à un petit segment', 'La banalisation de l\'image'], ans=0, exp='Autres risques : concurrent plus performant, sur-standardisation, myopie.'),
                   dict(type='qcm', q='Une stratégie qui vise une cible restreinte est une stratégie…', opts=['de spécialisation (niche)', 'de domination par les coûts', 'de croissance externe', 'de diversification'], ans=0, exp='Satisfaire mieux que les autres les exigences d\'un type de client.'),
                   dict(type='vf', q='En différenciation, la différence doit être perçue et valorisée par le marché.', ans=True, exp='Sinon, pas de prix plus élevé ni de fidélisation.'),
                   dict(type='qcm', q='Racheter son fournisseur est une…', opts=['intégration en amont', 'intégration en aval', 'franchise', 'sous-traitance'], ans=0, exp='En aval : racheter un client ou un distributeur.'),
                   dict(type='qcm', q='Contrat où un fabricant accorde à un commerçant une exclusivité de revente sur une zone :', opts=['concession', 'franchise', 'sous-traitance', 'alliance'], ans=0, exp='Le concédant et le concessionnaire.'),
                   dict(type='qcm', q='Dans la matrice ADL, une forte position en phase de démarrage ou de croissance donne…', opts=['bonne rentabilité, fort besoin de cash', 'faible rentabilité, faible besoin de cash', 'bonne rentabilité, faible besoin de cash', 'faible rentabilité, fort besoin de cash'], ans=0, exp='Le marché en croissance demande des liquidités.'),
                   dict(type='qcm', q='Qui a développé le SWOT selon le cours ?', opts=['Learned, Christensen, Andrews et Guth (Harvard, 1965)', 'Michael Porter', 'Le Boston Consulting Group', 'Paul Smith'], ans=0, exp='Professeurs de la Harvard Business School.'),
                   dict(type='vf', q='Les matrices de portefeuille sont des recettes à appliquer telles quelles.', ans=False, exp='Ce sont des outils d\'aide à la décision ; le discernement reste de rigueur.'),
                   dict(type='qcm', q='Mission, vision, but, objectif : lequel est une quantification ?', opts=['L\'objectif', 'La mission', 'La vision', 'Le but'], ans=0, exp='Le but est une déclaration générale ; l\'objectif est chiffré si possible.'),
                   dict(type='qcm', q='Le « S » de SMART signifie…', opts=['Spécifique', 'Simple', 'Stratégique', 'Stable'], ans=0, exp='Spécifique, Mesurable, Ambitieux, Réaliste, Temporel.')],
             methode=ul(['Diagnostic : externe (PESTEL, Porter) puis interne (forces, faiblesses), synthèse SWOT.', 'Portefeuille : placer chaque produit (BCG/ADL) et en déduire investissement, maintien ou abandon.', 'Stratégie : nommer la stratégie (coûts, spécialisation, différenciation, innovation, croissance externe…) et la justifier par des indices du texte.', 'Vérifier la cohérence stratégie ↔ ressources ↔ marché.']),
             fiches=[dict(q='Les 4 cases du BCG et leurs objectifs ?', a='Dilemmes (investir ou relancer), stars (soutenir), vaches à lait (rentabiliser), poids morts (abandonner).'), dict(q='Les 4 stratégies du SWOT ?', a='Attaque (F×O), ajustement (F×M), défense (Fa×O), survie (Fa×M).'),
                     dict(q='Modes de différenciation ?', a='Produit, service (avant/après vente), personnel, accès au produit, image.'), dict(q='Les 3 avantages de la domination par les coûts ?', a='Mieux placée en guerre des prix, dissuade les concurrents moins performants, souplesse de négociation amont et aval.'),
                     dict(q='Techniques d\'impartition ?', a='Sous-traitance, franchise, concession.')],
             carte=dict(core='Le marketing stratégique', branches=[dict(t='Cadre', items=['Mission, vision, objectifs', 'Stratégique ≠ opérationnel', 'SOSTAC, objectifs SMART', 'Segmentation, ciblage, positionnement']),
                                                                    dict(t='Diagnostic', items=['PESTEL', 'Porter 5+1', 'SWOT → attaque, ajustement, défense, survie']), dict(t='Portefeuille', items=['ADL : maturité × position', 'BCG : croissance × PdM', 'McKinsey : intérêt × position']),
                                                                    dict(t='Croissance interne', items=['Domination par les coûts', 'Spécialisation / niche', 'Différenciation', 'Innovation']), dict(t='Croissance externe', items=['Acquisition, fusion', 'Intégration amont / aval', 'Impartition, alliances'])],
                        schemas=[dict(t='Cercle vertueux des coûts', steps=['Effet d\'expérience', 'Baisse des coûts', 'Avantage concurrentiel', 'Gain de PdM', 'Volume et économies d\'échelle']), dict(t='Démarche SOSTAC', steps=['Situation', 'Objectifs', 'Stratégie', 'Tactiques', 'Actions', 'Contrôle'])]),
             liens=[dict(ch='marketing-1', pourquoi='Le diagnostic prolonge l\'analyse du marché et de l\'environnement ; la différenciation crée de la valeur perçue.'),
                    dict(ch='micro-2', pourquoi='Économies d\'échelle, rendements croissants et coûts moyens décroissants fondent la domination par les coûts.'),
                    dict(ch='micro-0', pourquoi='Barrières à l\'entrée et atomicité : Porter décrit l\'écart au modèle de concurrence pure et parfaite.'),
                    dict(ch='compta-4', pourquoi='Le chiffre d\'affaires, le résultat et la taille (bilan) servent à caractériser une entreprise dans une étude de cas (ex. L&L).')]),
    ]
    sujets = [
        dict(id='mkt-td1', num='TD 1', ch='marketing-2', mobiliser=['marketing-1'], type='Exercice de TD', source='Série TD — Exercice 1',
             titre='Cycle de vie de quatre produits et équilibre du portefeuille',
             enonce=P('Entreprise de produits pour le bâtiment. Ventes :') + table(['Produit', 'N-4', 'N-3', 'N-2', 'N-1', 'N'], [['A', 2000, 3000, 3800, 4300, 4500], ['B', 200, 360, 540, 960, 1570], ['C', '', '', '', 250, 350], ['D', 1540, 1600, 1480, 1250, 1150]], num_cols=(1, 2, 3, 4, 5)) + ol(['Dans quelle phase de son cycle de vie se situe chaque produit ?', 'Le portefeuille est-il équilibré ?']),
             pourquoi='Le cycle de vie (maturité de l\'activité) est au cœur de la matrice ADL et de l\'analyse de portefeuille (chapitre 2) ; la flexibilité des prix selon les phases est traitée avec la domination par les coûts.',
             commentaire=ul(['Calculer les taux de croissance d\'une année sur l\'autre : c\'est leur évolution qui révèle la phase.']),
             corrige=table(['Produit', 'Taux de croissance annuels', 'Phase'], [['A', '+50 % ; +27 % ; +13 % ; +5 %', '<b>Maturité</b> : ventes élevées, croissance qui s\'essouffle'], ['B', '+80 % ; +50 % ; +78 % ; +64 %', '<b>Croissance</b> : ventes en forte hausse'], ['C', '+40 % (apparu en N-1)', '<b>Lancement</b> (démarrage)'], ['D', '+4 % ; −8 % ; −16 % ; −8 %', '<b>Déclin</b> depuis N-2']]) +
             P('<b>Portefeuille</b> : il est plutôt équilibré, avec un produit à chaque phase : C prépare l\'avenir, B prend le relais, A finance (vache à lait si sa part de marché est forte), D est à gérer ou abandonner. Mais la dépendance à A est forte (4 500 sur 7 570 unités en N, soit environ 59 %) alors qu\'A arrive en fin de croissance. L\'entreprise doit soutenir B et réussir le lancement de C (investissements), en utilisant les liquidités d\'A, et programmer le retrait de D. Le cours rappelle d\'adapter la politique de prix à chaque phase : pénétration au lancement, prix réactifs en croissance, pression en maturité, flexibilité en déclin.')),
        dict(id='mkt-td2', num='TD 2', ch='marketing-2', mobiliser=[], type='Exercice de TD', source='Série TD — Exercice 2',
             titre='Belle Pomme, Pomme industrielle, Bio Pomme, Pomme Poirée : identifier les stratégies',
             enonce=P('Belle Pomme (13 % de PdM) vend un jus haut de gamme grâce à un producteur exclusif dont elle rachète l\'exploitation, et vise les États-Unis et le Japon. Pomme industrielle (leader, 22 %) produit dix fois plus avec une usine dernier cri, veut convertir les non-consommateurs, lance une gamme plus sucrée, se diversifie dans les filets de pêche et rachète un transporteur. Bio Pomme (PdM confidentielle, clients fidèles) élargit aux poires, pêches, abricots et lance une nouvelle variété bio. Pomme Poirée détient un brevet de fruit croisé, évite le leader, veut faire connaître son produit et proposera des fraises à cueillir.') + P('Quelles sont les stratégies suivies par les différents acteurs ?'),
             pourquoi='Stratégies de développement du chapitre 2 : domination par les coûts, différenciation, spécialisation, innovation, croissance externe et intégration.',
             commentaire=ul(['Relier chaque indice du texte à une stratégie du cours.', 'Un même acteur peut combiner plusieurs stratégies.']),
             corrige=table(['Acteur', 'Indices', 'Stratégies'], [
                 ['Belle Pomme', 'Qualité exceptionnelle perçue, producteur exclusif puis racheté, international', '<b>Différenciation</b> par la qualité (produit, image) ; <b>croissance externe par intégration en amont</b> (rachat du producteur, sécurisation des approvisionnements et du savoir-faire) ; développement géographique'],
                 ['Pomme industrielle', 'Leader, usine dernier cri, volumes ×10, gros moyens marketing, conquête des non-consommateurs, gamme plus sucrée, filets de pêche, rachat d\'un transporteur', '<b>Domination par les coûts</b> (effet d\'expérience, économies d\'échelle) ; développement de la demande par conquête de nouveaux consommateurs et extension de gamme ; <b>diversification</b> (filets de pêche) ; <b>intégration</b> du transport par croissance externe'],
                 ['Bio Pomme', 'Cible bio, clients fidèles, gamme élargie, nouvelle variété', '<b>Spécialisation (niche)</b> sur le bio, avec des prix plus élevés et une clientèle fidèle ; élargissement de gamme et <b>innovation</b>'],
                 ['Pomme Poirée', 'Brevet, très faible PdM, évite l\'affrontement', '<b>Innovation</b> protégée par un brevet (barrière à l\'entrée) sur une <b>niche</b>, en évitant le leader ; diversification (fraises à cueillir)']]) +
             NOTE('Vocabulaire complémentaire, hors diapos : Pomme industrielle est le <b>leader</b>, Belle Pomme un <b>challenger</b>, Bio Pomme et Pomme Poirée des <b>spécialistes</b>. Ce sont les rôles concurrentiels de Kotler.')),
        dict(id='mkt-td3', num='TD 3', ch='marketing-1', mobiliser=['marketing-2'], type='Exercice de TD', source='Série TD — Exercice 3',
             titre='Marché des dosettes de café : micro et macro-environnement',
             enonce=P('Vous êtes n° 3 (16 % de PdM) du concept cafetière/dosettes. Le leader (55 %) couvre tous les segments depuis 6 ans ; le second (23 %) propose une offre haute qualité avec un programme de fidélisation, cible les segments les plus rentables et maîtrise la distribution de ses dosettes. Votre partenaire fabricant de cafetières est mal distribué et met peu en avant l\'offre commune.') + P('Décrivez le micro-environnement puis le macro-environnement de l\'entreprise.'),
             pourquoi='Le chapitre 1 fournit l\'environnement et les acteurs du marché ; le chapitre 2 fournit le PESTEL et les forces de Porter.',
             commentaire=ul(['Micro-environnement : les acteurs proches (concurrents, fournisseurs/partenaires, distributeurs, clients).', 'Macro-environnement : grille PESTEL.']),
             corrige=H3('Micro-environnement') + ul(['<b>Concurrents</b> : un leader dominant (55 %) présent sur tous les segments ; un second (23 %) différencié par la qualité, la fidélisation et la maîtrise de la distribution.', '<b>Partenaire / fournisseur</b> : le fabricant de cafetières, maillon faible (mauvais circuits, peu de mise en avant).',
                                                        '<b>Distributeurs</b> : circuits de vente des machines et des dosettes (grande distribution, boutiques, en ligne), stratégiques puisque le second les contrôle.', '<b>Clients</b> : consommateurs segmentés (des plus rentables, recherchant la qualité, aux plus sensibles au prix).', 'Position : offre « coincée » entre les deux concurrents, positionnement flou.']) +
             H3('Macro-environnement (PESTEL)') + table(['Facteur', 'Exemples'], [['Politique / légal', 'Normes alimentaires et de sécurité des appareils, brevets sur les systèmes de dosettes, règles de concurrence'], ['Économique', 'Pouvoir d\'achat, prix des matières premières (café), conjoncture'], ['Socioculturel', 'Goût pour le café portionné, praticité, montée du haut de gamme et de la dégustation'],
                                                                                                    ['Technologique', 'Innovation sur les machines et les capsules, compatibilités'], ['Écologique', 'Déchets des dosettes, recyclage, attentes environnementales']]) + NOTE('Les exemples du PESTEL sont des pistes à adapter : l\'énoncé ne donne que le micro-environnement.')),
        dict(id='mkt-td4', num='TD 4', ch='marketing-2', mobiliser=['marketing-1'], type='Exercice de TD', source='Série TD — Exercice 4',
             titre='Cycle de vie raccourci : comment relancer un produit ?',
             enonce=P('Il y a dix ans, un produit électroménager vivait cinq ans ; aujourd\'hui, dès trois ans, les tests révèlent un vieillissement confirmé par la stagnation des ventes. Les industriels modifient régulièrement leurs produits pour attirer de nouveaux clients sans perdre les anciens.') + P('Quels moyens industriels l\'entreprise peut-elle mettre en œuvre pour relancer ses produits ?'),
             pourquoi='Innovation et différenciation par le produit (chapitre 2), valeur perçue (chapitre 1).',
             commentaire=ul(['S\'appuyer sur les déterminants produit du cours (fonctionnalité, fiabilité, performance, réparabilité, conformité, style, durabilité, design).']),
             corrige=ul(['<b>Améliorer le produit existant</b> (innovation incrémentale) : performances, nouvelles fonctionnalités, fiabilité, consommation d\'énergie.', '<b>Renouveler le design et le style</b> (relooking), les matériaux, le packaging : l\'identité sensorielle renforce les bénéfices perçus.',
                         '<b>Décliner la gamme</b> : nouvelles versions, tailles, options, séries limitées, pour de nouveaux segments sans perdre les anciens.', '<b>Réduire les coûts de production</b> (effet d\'expérience, standardisation des composants) pour baisser le prix ou financer les améliorations.',
                         '<b>Enrichir le service associé</b> : garantie étendue, réparabilité, pièces détachées (différenciation par le service).', '<b>Chercher de nouveaux usages</b> ou applications.']) + P('L\'objectif est d\'<b>allonger la phase de maturité</b> et de repousser le déclin, en accroissant la valeur perçue par rapport aux concurrents.')),
        dict(id='mkt-td5', num='TD 5', ch='marketing-2', mobiliser=['marketing-1', 'micro-0'], type='Exercice de TD', source='Série TD — Exercice 5',
             titre='Smartphones : cinq forces de Porter et SWOT de Samsung et d\'Apple',
             enonce=P('Le marché mondial du téléphone mobile décline alors que celui du smartphone est en pleine croissance. En 2011, 1,6 milliard de mobiles vendus ; Nokia leader malgré une forte baisse (417,1 millions), Samsung 2ᵉ (327,4 millions), Apple 3ᵉ (93 millions). En France, Samsung et Apple dominent et rivalisent d\'innovations, avec l\'émergence de nouveaux acteurs.') + ol(['Analysez l\'attractivité du marché avec les cinq forces de Porter.', 'Établissez le SWOT de Samsung et d\'Apple.']),
             pourquoi='Outils du chapitre 2 (Porter, SWOT). Le chapitre 1 fournit le cas Nokia et les marchés induits et captifs (App Store). L\'introduction de micro fournit les barrières à l\'entrée, qui contredisent l\'hypothèse de CPP.',
             commentaire=ul(['Pour chaque force, dire si elle est forte ou faible et conclure sur l\'attractivité.', 'Dans le SWOT, les forces et faiblesses sont internes, les opportunités et menaces externes.']),
             corrige=H3('1. Cinq (+1) forces') + table(['Force', 'Analyse', 'Intensité'], [['Rivalité', 'Course à l\'innovation entre Samsung et Apple, lancements annuels, guerre des brevets', 'Très forte'], ['Nouveaux entrants', 'Barrières élevées (R&D, brevets, marque, distribution) mais arrivée de nouveaux acteurs, notamment asiatiques à prix agressifs', 'Moyenne'],
                                                                       ['Substituts', 'Tablettes, ordinateurs portables, mobiles classiques (en déclin)', 'Faible à moyenne'], ['Clients', 'Consommateurs dispersés (pouvoir faible), mais opérateurs et distributeurs qui négocient les volumes', 'Moyenne'],
                                                                       ['Fournisseurs', 'Composants clés (processeurs, écrans) concentrés ; système d\'exploitation (Android de Google pour Samsung)', 'Moyenne à forte'], ['+1 Pouvoirs publics', 'Brevets, normes, régulation des télécoms', 'Moyenne']]) +
             P('Marché <b>attractif</b> par sa croissance, mais très concurrentiel : l\'avantage va aux acteurs qui combinent innovation, marque et maîtrise des coûts. Nokia montre qu\'une position de leader se perd vite (chapitre 1).') +
             H3('2. SWOT') + table(['', 'Samsung', 'Apple'], [['Forces', 'Gamme très large (tous les prix), volumes (327 M), maîtrise de composants, rapidité d\'innovation', 'Marque et image premium, écosystème iOS et App Store (marché captif), design, fidélité, marges'], ['Faiblesses', 'Dépendance au système d\'exploitation d\'un tiers, image moins premium', 'Gamme étroite et prix élevés, volumes plus faibles (93 M)'],
                                                        ['Opportunités', 'Croissance du smartphone, pays émergents, déclin de Nokia', 'Croissance du marché, services et contenus (marchés induits)'], ['Menaces', 'Nouveaux entrants à bas prix, litiges de brevets', 'Concurrence d\'Android, banalisation, saturation du haut de gamme']]) +
             NOTE('Les éléments qualitatifs du SWOT relèvent de ta connaissance du marché, comme le demande l\'énoncé : justifie-les avec les données chiffrées fournies.')),
        dict(id='mkt-td6', num='TD 6', ch='marketing-2', mobiliser=['marketing-1'], type='Exercice de TD', source='Série TD — Exercice 6',
             titre='L\'arrivée de Free Mobile : réactions et stratégies d\'Orange, SFR et Bouygues',
             enonce=P('Free arrive sur le mobile. Orange lance une marque low-cost, Sosh (35 000 clients fin 2011), en « contre-feu », s\'appuie sur son réseau de boutiques et sur l\'accord d\'itinérance qui permet à Free de lancer son offre. SFR communique sur la qualité (98 % de la population couverte en 3G+ selon l\'Arcep) et la sécurité de son réseau, et lance Red (à partir de 12 €). Bouygues, le plus petit et le plus menacé, offre un iPhone 4 avec ses abonnements et lance B&You, avec de l\'illimité en voix et en data. Free entretient la rumeur en gardant ses tarifs secrets.') +
             ol(['Rappelez ce qu\'est un marché potentiel et les principales stratégies fondées sur la demande.', 'Comment les concurrents réagissent-ils ?', 'Qualifiez leurs stratégies.']),
             pourquoi='Stratégies du chapitre 2 (domination par les coûts, différenciation par la qualité et le service, barrières à l\'entrée) ; marché et valeur perçue au chapitre 1.',
             commentaire=ul(['Distinguer les réactions défensives (protéger sa base) des réactions offensives (conquérir).']),
             corrige=H3('1. Marché potentiel et stratégies fondées sur la demande') +
             P('Le <b>marché potentiel</b> est l\'estimation de la demande maximale : le marché actuel plus les non-consommateurs relatifs (ceux qui pourraient consommer). Stratégies fondées sur la demande : <b>extensive</b> (conquérir de nouveaux consommateurs, ce qui développe le marché), <b>intensive</b> (faire consommer davantage les clients actuels, montée en gamme, panier moyen), <b>concurrentielle ou sélective</b> (prendre des clients aux concurrents).') +
             NOTE('Ces définitions sont des repères complémentaires : elles ne figurent pas telles quelles dans tes diapos, mais le cours évoque le recrutement puis la montée en gamme chez Free (forfait à 2 €).') +
             H3('2. Réactions') + table(['Opérateur', 'Réaction'], [['Orange (leader historique)', 'Marque de combat low-cost Sosh ciblant les jeunes ; « arsenal de ripostes » prêtes ; réseau de boutiques pour rassurer ; accord d\'itinérance qui rend Free dépendant de son réseau'], ['SFR', 'Communication sur la qualité (couverture 3G+) et la sécurité du réseau ; offre low-cost Red aux services limités'], ['Bouygues (le plus petit, le plus menacé)', 'Offre agressive (iPhone offert) ; B&You avec de l\'illimité voix et data, exactement le terrain de Free']]) +
             H3('3. Stratégies') + ul(['<b>Orange</b> : stratégie défensive de leader, avec une double marque (Sosh pour contrer le low-cost, Orange pour la qualité et le service : différenciation par l\'accès au produit, les boutiques).', '<b>SFR</b> : <b>différenciation</b> par la qualité et la sécurité du réseau, doublée d\'une marque low-cost.', '<b>Bouygues</b> : riposte frontale par les prix et l\'illimité, alignement sur le positionnement de Free.', '<b>Free</b> : nouvel entrant low-cost (domination par les coûts et les prix), marketing de la rumeur, au risque de décevoir.'])),
        dict(id='mkt-ll', num='Cas', ch='marketing-2', mobiliser=['marketing-1', 'compta-4'], type='Étude de cas (avec corrigé)', source='Étude de cas L&L + réponse',
             titre='Cas L&L : diagnostic stratégique externe, stratégie et avantages concurrentiels d\'un distributeur de biens culturels',
             enonce=P('L&L, SA au capital de 3 M€, distribue des biens culturels et de loisirs (livres, disques, micro-informatique, son, vidéo, photo) : 450 salariés, 700 000 clients par an, 45 magasins dans 18 villes, 75 000 m², CA 2015 de 25 M€, résultat net 2,4 M€. Longtemps seule à proposer une gamme large dans un même espace, elle affronte des franchises spécialisées, puis les hypermarchés (prix bas) et les marchands en ligne (prix attractifs, livraison rapide). Le PDG attribue les difficultés à l\'agressivité de la concurrence et à l\'évolution des modes de distribution ; il veut se différencier par la qualité des prestations, ouvrir des magasins près des cités étudiantes et améliorer le conseil des vendeurs.') +
             ol(['Caractériser l\'organisation : type, taille, statut juridique, secteur, métier.', 'Établir le diagnostic stratégique externe.', 'Identifier (a) la stratégie adoptée, (b) les axes stratégiques choisis.', 'Définir la notion d\'avantage concurrentiel.', 'Identifier les avantages concurrentiels de chaque nouvelle concurrence.']),
             pourquoi='Le chapitre 2 est central (diagnostic externe, stratégies, avantage concurrentiel). Le chapitre 1 éclaire le marché et l\'environnement technologique de la distribution. Les données du compte de résultat (CA, résultat) renvoient aux documents de synthèse en compta.',
             commentaire=ul(['Le corrigé ci-dessous reprend <b>le corrigé fourni avec le cas</b>, complété par des liens vers le cours.', 'Diagnostic externe = opportunités et menaces seulement (pas les forces et faiblesses).']),
             corrige=H3('1. Caractérisation (corrigé fourni)') + table(['Critère', 'Réponse'], [['Type', 'Entreprise privée'], ['Taille', 'Grande entreprise (CA 25 M€, 450 salariés, 75 000 m², 45 magasins)'], ['Statut juridique', 'SA'], ['Secteur', 'Tertiaire (services)'], ['Métier', 'Distribution de biens culturels et de loisirs']]) +
             H3('2. Diagnostic stratégique externe') + table(['Opportunités', 'Menaces'], [['Forte demande ; position géographique propice (implantation dans les grandes villes universitaires)', 'Structures concurrentielles hostiles (hypermarchés et vendeurs en ligne) ; entrée de nouveaux concurrents (franchises) ; évolution des modes de distribution']]) +
             H3('3. Stratégie') + P('<b>(a)</b> Selon le corrigé fourni, L&L adopte une <b>stratégie de spécialisation</b>. <b>(b)</b> Elle se caractérise par une <b>extension géographique</b> de ses activités (nouveaux magasins près des cités étudiantes) et l\'<b>adaptation de ses produits aux besoins spécifiques</b> des consommateurs.') +
             NOTE('Lien avec le cours : L&L cible un type de clients (étudiants) et veut « satisfaire mieux que les autres » leurs exigences (qualité du service, conseil), ce qui définit la spécialisation. Les leviers annoncés par le PDG sont ceux de la <b>différenciation par le service et par le personnel</b> (compétence, écoute, conseil), à l\'opposé de la domination par les coûts des concurrents.') +
             H3('4. Avantage concurrentiel') + P('Avantage temporaire, sorte de <b>monopole de situation</b> : une performance provoquée par la position de l\'entreprise face à la concurrence.') +
             H3('5. Avantages des nouveaux concurrents') + table(['Concurrent', 'Avantage concurrentiel'], [['Hypermarchés', 'Politique agressive de prix bas (domination par les coûts)'], ['Marchands culturels en ligne', 'Le prix, la rapidité de livraison, la disponibilité des produits']]) +
             P('Pour aller plus loin : rentabilité nette de L&L = 2,4 / 25 ≈ 9,6 % du CA.')),
        dict(id='mkt-nes', num='Cas', ch='marketing-1', mobiliser=['marketing-2'], type='Étude de cas du cours', source='Cours Partie 1 — Étude de cas Nespresso',
             titre='Le succès de Nespresso : éléments de force, bénéfices perçus et coûts perçus',
             enonce=ol(['Quels sont les éléments de force de Nespresso ?', 'Comment peut-on accroître les bénéfices perçus ?', 'Comment peut-on réduire les coûts perçus ?']),
             pourquoi='Le chapitre 1 est central (valeur perçue). Le chapitre 2 intervient car Nespresso illustre la différenciation (produit, service, accès, image) et l\'innovation de concept.',
             commentaire=ul(['Répondre avec la grille bénéfices / coûts perçus du cours.']),
             corrige=H3('Éléments de force (cours)') + ul(['Une innovation de concept : les capsules.', 'Une qualité perçue renforcée (appellations de « grands crus »).', 'Une très forte identité sensorielle : goûts marqués, packaging haut de gamme, design des machines.', 'Des services associés intégrés dans une relation forte (boutiques, club).', 'Un approvisionnement facile (commande en ligne, livraison rapide).', 'Une marque servie par des campagnes exceptionnelles (« What else ? » avec George Clooney).']) +
             H3('Accroître les bénéfices perçus') + P('Innovation de concept, performances, identité sensorielle et packaging, services associés, qualité perçue, valorisation de la marque.') +
             H3('Réduire les coûts perçus') + P('Baisser le prix (avec prudence pour la rentabilité), modifier la perception du prix (machine abordable et marge sur le consommable, promotions ciblées), réduire le temps, l\'effort et le risque (commande en ligne, livraison rapide, service client).') +
             P('Lien avec le chapitre 2 : c\'est une <b>différenciation</b> multiple (produit, service, accès, image) protégée par l\'<b>innovation</b>.')),
    ]
    return dict(id='marketing', nom='Marketing', court='Marketing', couleur='#f76ab4', sourcesResume='7 documents · 5 fichiers de cours + série de TD + cas L&L et sa réponse', documents=DOCS, chapitres=chs,
                formules=[dict(titre='Grilles et outils à connaître', ch='marketing-2', items=[dict(t='Valeur perçue', f='Bénéfices perçus / coûts perçus', note='Relative aux offres concurrentes'), dict(t='SOSTAC', f='Situation → Objectifs → Stratégie → Tactiques → Actions → Contrôle'),
                                                                                                dict(t='Objectif SMART', f='Spécifique · Mesurable · Ambitieux · Réaliste · Temporel'), dict(t='PESTEL', f='Politique · Économique · Socioculturel · Technologique · Écologique · Légal'),
                                                                                                dict(t='SWOT → stratégies', f='F×O attaque · F×M ajustement · Fa×O défense · Fa×M survie'), dict(t='Porter 5 + 1', f='Entrants · substituts · clients · fournisseurs · rivalité + pouvoirs publics'),
                                                                                                dict(t='BCG', f='Croissance du marché × part de marché → dilemmes, stars, vaches à lait, poids morts'), dict(t='Effet d\'expérience', f='Coût unitaire × (1 − x %) à chaque doublement de la production cumulée'),
                                                                                                dict(t='Part de marché', f='PdM = ventes de l\'entreprise / ventes totales du marché', note='Ex. TD 3 : 55 % + 23 % + 16 %'), dict(t='Taux de croissance des ventes', f='(Vn − Vn-1) / Vn-1', note='Sert à situer un produit dans son cycle de vie (TD 1)')])],
                auteurs=[dict(nom='American Marketing Association (AMA)', kind='Institution', dates='Définition du marketing', courant='Définitions', source='cours', chapitres=['marketing-1'], idee='Marketing : fonction et processus qui créent, communiquent et délivrent de la valeur aux clients et gèrent la relation client au bénéfice de l\'organisation et de ses parties prenantes.', phrase=''),
                         dict(nom='Mercator (J. Lendrevie, J. Lévy, D. Lindon)', kind='Manuel', dates='Dalloz / Dunod, éditions successives', courant='Marketing', source='cours', chapitres=['marketing-1'], oeuvres=['Mercator'], idee='Définition citée par ton cours : effort d\'adaptation aux marchés concurrentiels par une offre à la valeur perçue durablement supérieure.', phrase='« Selon le Mercator, le marketing est l\'effort d\'adaptation des organisations à des marchés concurrentiels… »'),
                         dict(nom='Abraham Maslow', kind='Auteur', dates='1908 – 1970', courant='Psychologie', source='cours', chapitres=['marketing-1'], oeuvres=['A Theory of Human Motivation (1943)', 'Motivation and Personality (1954)'], idee='Pyramide des besoins : physiologiques, sécurité, appartenance, estime, accomplissement de soi.', phrase=''),
                         dict(nom='Michael Porter', kind='Auteur', dates='né en 1947', courant='Stratégie (Harvard)', source='cours', chapitres=['marketing-2'], oeuvres=['Competitive Strategy (1980)', 'Competitive Advantage (1985)'], idee='Les cinq forces concurrentielles (et la « +1 » des pouvoirs publics dans ton cours) ; stratégies génériques de coût, de différenciation et de focalisation.', phrase='« Selon Porter, l\'intensité concurrentielle d\'un secteur dépend de cinq forces. »'),
                         dict(nom='Learned, Christensen, Andrews et Guth', kind='Auteurs', dates='1965', courant='Harvard Business School', source='cours', chapitres=['marketing-2'], idee='Modèle SWOT (LCAG) : croiser forces et faiblesses internes avec opportunités et menaces externes.', phrase=''),
                         dict(nom='Boston Consulting Group (BCG)', kind='Cabinet', dates='fondé en 1963 par Bruce Henderson', courant='Conseil en stratégie', source='cours', chapitres=['marketing-2'], idee='Matrice croissance / part de marché et effet d\'expérience.', phrase=''),
                         dict(nom='Arthur D. Little (ADL)', kind='Cabinet', dates='Matrice ADL', courant='Conseil en stratégie', source='cours', chapitres=['marketing-2'], idee='Matrice maturité de l\'activité × position concurrentielle.', phrase=''),
                         dict(nom='McKinsey', kind='Cabinet', dates='Matrice attrait / position', courant='Conseil en stratégie', source='cours', chapitres=['marketing-2'], idee='Matrice 3 × 3 intérêt stratégique × position concurrentielle, avec les recommandations associées.', phrase=''),
                         dict(nom='Paul R. Smith', kind='Auteur', dates='Modèle SOSTAC', courant='Planification marketing', source='cours', chapitres=['marketing-2'], idee='Démarche de planification : Situation, Objectives, Strategy, Tactics, Actions, Control.', phrase=''),
                         dict(nom='N. Van Laethem et L. Body', kind='Auteurs', dates='2004', courant='Marketing', source='cours', chapitres=['marketing-1'], oeuvres=['Le Plan marketing, Dunod, 2004'], idee='Source du tableau des types de marchés (principal, indirect, générique, support) de ton cours.', phrase=''),
                         dict(nom='G. Johnson, K. Scholes et al.', kind='Manuel', dates='cité « Stratégique, 2002 »', courant='Stratégie', source='cours', chapitres=['marketing-2'], oeuvres=['Stratégique (Pearson)'], idee='Source de la grille PESTEL de ton cours et du schéma analyse interne / externe → diagnostic.', phrase=''),
                         dict(nom='Philip Kotler', kind='Auteur', dates='né en 1931', courant='Marketing management', source='compl', chapitres=['marketing-1', 'marketing-2'], oeuvres=['Marketing Management (1ʳᵉ éd. 1967)'], idee='Les optiques (production, produit, vente, marketing) et les rôles concurrentiels (leader, challenger, suiveur, spécialiste).', phrase=''),
                         dict(nom='H. Igor Ansoff', kind='Auteur', dates='1918 – 2002', courant='Stratégie', source='compl', chapitres=['marketing-2'], oeuvres=['Corporate Strategy (1965)'], idee='Matrice produits / marchés : pénétration, développement de marché, développement de produit, diversification.', phrase='')],
                reperes=[dict(date='1943', t='Maslow, A Theory of Human Motivation (pyramide des besoins).'), dict(date='1963', t='Création du Boston Consulting Group (Bruce Henderson).'), dict(date='1965', t='Modèle SWOT (Learned, Christensen, Andrews, Guth).', src='cours'),
                         dict(date='1967', t='Kotler, Marketing Management.'), dict(date='1980', t='Porter, Competitive Strategy (cinq forces).'), dict(date='1999', t='Pic du marché mondial de la musique : 28,6 Md$ (IFPI).', src='cours'),
                         dict(date='2005', t='Lancement de la première GoPro.', src='cours'), dict(date='2010', t='Musique : moins de 15 Md$ ; lancement de l\'A320neo en décembre.', src='cours'), dict(date='2011', t='Smartphones : Nokia 417,1 M, Samsung 327,4 M, Apple 93 M d\'unités ; arrivée annoncée de Free Mobile.', src='cours'),
                         dict(date='2013', t='Nokia vend sa division mobile à Microsoft.', src='cours'), dict(date='2015', t='Reprise des ventes de musique (streaming) ; GoPro vend 6,6 millions de caméras ; L&L réalise 25 M€ de CA.', src='cours')],
                methode=[dict(titre='Traiter une étude de cas marketing', html=ol(['Caractériser l\'entreprise (type, taille, statut, secteur, métier).', 'Diagnostic externe : opportunités et menaces (PESTEL, Porter).', 'Diagnostic interne : forces et faiblesses.', 'Nommer la stratégie avec le vocabulaire du cours et la justifier par le texte.', 'Proposer ou évaluer des actions cohérentes (marketing mix).']), piege='Mélanger interne et externe dans le diagnostic, ou recopier le texte sans le qualifier avec les notions du cours.'),
                         dict(titre='Construire un SWOT utile', html=ul(['Quatre cases, 3 à 5 éléments par case, formulés de façon précise.', 'Forces et faiblesses : internes, comparées aux concurrents.', 'Opportunités et menaces : externes, issues du PESTEL et des forces de Porter.', 'Conclure par la stratégie : attaque, ajustement, défense ou survie.'])),
                         dict(titre='Analyser un portefeuille (BCG, ADL, cycle de vie)', html=ol(['Calculer les taux de croissance et situer chaque produit dans son cycle de vie.', 'Placer les produits dans la matrice.', 'Associer à chaque case un objectif (soutenir, rentabiliser, relancer, abandonner).', 'Juger l\'équilibre : les vaches à lait financent-elles les stars et les dilemmes ?'])),
                         dict(titre='Identifier une stratégie de développement', html=table(['Indice dans le texte', 'Stratégie'], [['Volumes, usine, prix bas, économies d\'échelle', 'Domination par les coûts'], ['Qualité, service, image, design', 'Différenciation'], ['Cible restreinte, clients fidèles, exigences spécifiques', 'Spécialisation / niche'], ['Brevet, nouveau produit, R&D', 'Innovation'], ['Rachat, fusion, intégration amont/aval', 'Croissance externe'], ['Franchise, concession, sous-traitance', 'Impartition']]))],
                courbes=[dict(id='mkt-g1', ch='marketing-2', titre='Matrice BCG (orientation de ton cours)', svg=bcg, tags=['BCG', 'portefeuille'], exp=ul(['Axe vertical : croissance du marché ; axe horizontal : part de marché (croissante vers la droite dans tes diapos).', 'Les vaches à lait financent les stars et les dilemmes prometteurs ; les poids morts sont à abandonner.'])),
                         dict(id='mkt-g2', ch='marketing-2', titre='Matrice ADL : maturité × position concurrentielle', svg=adl, tags=['ADL', 'maturité'], exp=ul(['Une position forte donne une bonne rentabilité.', 'Démarrage et croissance demandent du cash ; maturité et déclin en demandent peu.'])),
                         dict(id='mkt-g3', ch='marketing-2', titre='Matrice McKinsey : recommandations stratégiques', svg=mck, tags=['McKinsey'], exp=ul(['Vert : investir ou maintenir ; jaune : rentabiliser ou sélectionner ; rose : abandonner.'])),
                         dict(id='mkt-g4', ch='marketing-2', titre='SWOT : les quatre stratégies', svg=swot, tags=['SWOT'], exp=ul(['Attaque quand forces et opportunités se rencontrent ; survie quand faiblesses et menaces se cumulent.'])),
                         dict(id='mkt-g5', ch='marketing-2', titre='Les 5 + 1 forces de Porter', svg=porter_svg(), tags=['Porter', 'concurrence'], exp=ul(['Quatre forces pèsent sur la rivalité centrale, plus les pouvoirs publics (« +1 » de ton cours).', 'Plus les forces sont fortes, moins le secteur est attractif.'])),
                         dict(id='mkt-g6', ch='marketing-2', titre='TD 1 : ventes des produits A, B, C, D et phases du cycle de vie', svg=cycle_svg(), tags=['cycle de vie', 'TD'], exp=ul(['A plafonne (maturité), B accélère (croissance), C démarre (lancement), D recule (déclin).', 'Tracé à partir des données de l\'exercice 1 du TD.'])),
                         dict(id='mkt-g7', ch='marketing-2', titre='Cycle de vie théorique d\'un produit', svg=cycle_theorique(), tags=['cycle de vie'], exp=ul(['Lancement, croissance, maturité, déclin.', 'Politique de prix (cours) : pénétration → prix réactifs → pression en maturité → flexibilité en déclin.'])),
                         dict(id='mkt-g8', ch='marketing-2', titre='Effet d\'expérience (illustration à 80 %)', svg=experience_svg(), tags=['effet d\'expérience', 'coûts'], exp=ul(['Le coût unitaire baisse d\'un pourcentage constant (ici 20 %) à chaque doublement de la production cumulée : 100 → 80 → 64 → 51,2…', 'Le taux de 80 % est une illustration : ton cours donne le principe, pas de taux.'])),
                         dict(id='mkt-g9', ch='marketing-1', titre='Les mécanismes de perception de la valeur', svg=valeur_svg(), tags=['valeur perçue', 'fidélité'], exp=ul(['Avant achat : bénéfices et coûts perçus, comparés aux offres concurrentes.', 'Après achat : l\'expérience conduit à la satisfaction (rachat) ou à l\'insatisfaction (défection).'])),
                         dict(id='mkt-g10', ch='marketing-2', titre='La démarche SOSTAC', svg=sostac_svg(), tags=['SOSTAC', 'démarche'], exp=ul(['De l\'analyse de la situation au contrôle, en passant par des objectifs SMART, la stratégie (segmentation, ciblage, positionnement) et les tactiques (4P).']))],
                sujets=sujets)
