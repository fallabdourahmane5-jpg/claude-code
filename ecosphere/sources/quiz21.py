# -*- coding: utf-8 -*-
import json
L='ABCD'
QCM=[
("L’ouverture commerciale désigne les échanges :",["De capitaux financiers","De biens et de services","De devises","De main-d’œuvre"],1),
("Un IDE se distingue d’un investissement de portefeuille parce qu’il :",["Est toujours plus petit","Relève d’une logique productive et de contrôle","Ne traverse pas les frontières","Concerne uniquement l’État"],1),
("L’investissement de portefeuille correspond à :",["Une prise de contrôle d’entreprise","L’achat d’actifs financiers étrangers dans une logique de placement","Un prêt bancaire national","Une exportation de services"],1),
("Le passage par le marché des changes est nécessaire parce que :",["Les prix sont fixes","Les opérations internationales impliquent des devises différentes","L’État l’impose","Les banques l’exigent"],1),
("Les trois dimensions de l’ouverture internationale sont :",["Agricole, industrielle, tertiaire","Commerciale, productive, financière et monétaire","Publique, privée, mixte","Locale, nationale, mondiale"],1),
("Pour Michalet, la mondialisation est :",["Un phénomène purement commercial","Un processus multidimensionnel","Une politique publique","Un régime monétaire"],1),
("La configuration multinationale de Michalet met au centre :",["Le commerce de biens","L’investissement direct et l’implantation des firmes","Les migrations","L’étalon-or"],1),
("La configuration globale se caractérise par :",["Le repli national","La fragmentation de la production et l’unification financière","La fin des échanges","Le troc"],1),
("L’hypermondialisation correspond :",["Au remplacement du commerce par la finance","Au cumul des dimensions commerciale, productive et financière","À la démondialisation","Au protectionnisme"],1),
("Pierre-Noël Giraud analyse les globalisations comme :",["Une harmonisation des économies","Une généralisation des compétitions entre territoires","Une baisse des échanges","Un phénomène purement monétaire"],1),
("Le « privilège exorbitant » désigne l’avantage tiré par les États-Unis :",["De leur agriculture","Du statut international du dollar","De leur démographie","De leurs matières premières"],1),
("Les BRICS regroupent :",["Brésil, Russie, Inde, Chine, Afrique du Sud","Belgique, Roumanie, Irlande, Chypre, Suède","Brésil, Rwanda, Inde, Canada, Serbie","Bolivie, Russie, Iran, Chine, Soudan"],0),
("Selon Prebisch, la spécialisation primaire conduit à :",["Une amélioration des termes de l’échange","Une détérioration des termes de l’échange","Une industrialisation rapide","Une hausse des salaires"],1),
("Les termes de l’échange rapportent :",["Le PIB aux exportations","Le prix des exportations au prix des importations","L’épargne à l’investissement","Les impôts aux dépenses"],1),
("La DIT traditionnelle repose sur :",["Une spécialisation verticale centre / périphérie","Une fragmentation des processus productifs","L’autarcie","Le libre-échange intégral"],0),
("La DIPP signifie :",["Division internationale des prix de production","Décomposition internationale des processus productifs","Dette interne des pays pauvres","Demande intérieure par produit"],1),
("Une chaîne de valeur mondiale correspond à :",["Une entreprise unique","La fragmentation des étapes de production entre plusieurs pays","Un accord douanier","Un indice boursier"],1),
("Acemoglu et Robinson mettent en avant le rôle :",["Du climat","Des institutions extractives","De la démographie","Des transports"],1),
("La malédiction des ressources désigne :",["L’épuisement des matières premières","Le fait que l’abondance de ressources peut freiner le développement","Une taxe sur les exportations","Une crise monétaire"],1),
("La courbe de l’éléphant a été popularisée par :",["Branko Milanovic","Raúl Prebisch","Charles-Albert Michalet","Pierre-Noël Giraud"],0),
("La courbe de l’éléphant montre que la mondialisation :",["Réduit toutes les inégalités","Réduit les inégalités entre pays mais renforce certaines inégalités internes","Augmente toutes les inégalités","N’a aucun effet"],1),
("La balance des paiements enregistre :",["Le budget de l’État","Les opérations entre résidents et non-résidents","Les prix à la consommation","La masse monétaire"],1),
("Le compte courant comprend notamment :",["Uniquement les biens","Les biens, les services, les revenus et les transferts courants","Uniquement les capitaux","Uniquement l’or"],1),
("Le compte financier enregistre :",["Les échanges de biens","Les mouvements de capitaux entre résidents et non-résidents","Les impôts","Les salaires"],1),
("L’identité macroéconomique du solde extérieur s’écrit :",["X − M = (S − I) + (T − G)","X + M = C + I","Y = C + S","M = X + G"],0),
("Un déficit courant traduit :",["Une capacité de financement","Un besoin de financement vis-à-vis du reste du monde","Un excédent d’épargne","Une baisse des importations"],1),
("Les « déficits jumeaux » associent :",["Déficit public et déficit extérieur","Déficit commercial et excédent courant","Inflation et chômage","Dette privée et dette publique"],0),
("La balance des paiements est :",["Toujours déficitaire","Équilibrée par construction","Toujours excédentaire","Indépendante des capitaux"],1),
("Le taux d’ouverture mesure :",["Le poids du commerce extérieur dans le PIB","Le taux de chômage","Le taux d’épargne","L’inflation importée"],0),
("Le commerce en valeur ajoutée corrige :",["Les variations de change","Le double comptage des biens intermédiaires","Les erreurs statistiques","L’inflation"],1),
("Le double comptage provient :",["Des services financiers","Du passage répété des biens intermédiaires aux frontières","Des migrations","Des transferts publics"],1),
("La première mondialisation s’achève :",["En 1870","En 1914","En 1945","En 1971"],1),
("Le régime monétaire de la première mondialisation était :",["Le flottement généralisé","L’étalon-or","Le bimétallisme régional","L’euro"],1),
("Les migrations de la première mondialisation se dirigeaient surtout :",["De l’Asie vers l’Europe","de l’Europe vers les Amériques","De l’Afrique vers l’Asie","Des Amériques vers l’Europe"],1),
("L’entre-deux-guerres se caractérise par :",["Une ouverture record","Le protectionnisme et l’effondrement des flux","La fin des États-nations","La création de l’OMC"],1),
("Le basculement de puissance de l’entre-deux-guerres profite :",["À l’Empire britannique","Aux États-Unis","À la Chine","À la Russie"],1),
("La mondialisation contemporaine est, par rapport à la première :",["Plus migratoire","Moins migratoire et beaucoup plus financière","Identique","Uniquement commerciale"],1),
("La slowbalization désigne :",["Un recul massif des échanges","Un ralentissement de la progression de l’ouverture","Une accélération du commerce","Une crise monétaire"],1),
("Depuis 2008, le commerce mondial :",["Progresse plus vite qu’avant","Voit sa progression ralentir","S’est effondré","A disparu"],1),
("La stagnation du taux d’ouverture signifie :",["Une démondialisation certaine","Pas nécessairement une véritable démondialisation","Une hausse des droits de douane","La fin des chaînes de valeur"],1),
("L’arsenalisation de la politique économique désigne :",["La hausse des dépenses militaires","L’usage des instruments économiques comme moyens de rapport de force","La privatisation de l’armée","Une politique budgétaire expansive"],1),
("Le décrochage européen se mesure notamment par :",["La hausse du PIB européen","La baisse du poids de l’Europe dans le PIB mondial et de ses parts de marché","La hausse des exportations","La baisse du chômage"],1),
]
VF=[
("L’ouverture internationale se limite aux échanges de biens et de services.",False,"Faux : elle comporte aussi une dimension productive, financière et monétaire."),
("Un IDE relève d’une logique productive, contrairement à l’investissement de portefeuille.",True,"Exact : l’IDE vise un contrôle durable de l’activité, le portefeuille un simple placement."),
("Pour Michalet, la mondialisation se réduit au commerce international.",False,"Non : il montre au contraire qu’elle est un processus multidimensionnel."),
("L’hypermondialisation remplace les formes antérieures d’internationalisation.",False,"Faux : elle correspond à leur cumul, pas à leur remplacement."),
("Le statut international du dollar procure aux États-Unis un avantage de financement.",True,"Exact : c’est le « privilège exorbitant »."),
("Selon Prebisch, la spécialisation primaire améliore les termes de l’échange des périphéries.",False,"Non : elle les détériore, obligeant à exporter davantage pour importer autant."),
("La DIT traditionnelle et la DIPP désignent la même chose.",False,"Faux : la DIT traditionnelle est une spécialisation verticale par produits, la DIPP une fragmentation des étapes de production."),
("La malédiction des ressources signifie que l’abondance de matières premières garantit le développement.",False,"C’est l’inverse : elle peut freiner la diversification et le développement."),
("La courbe de l’éléphant permet de concilier réduction des inégalités entre pays et hausse de certaines inégalités internes.",True,"Exact : c’est précisément le paradoxe qu’elle résout."),
("La balance des paiements peut être durablement déséquilibrée sur son total.",False,"Faux : elle est équilibrée par construction ; ce sont ses soldes internes qui peuvent l’être."),
("Le solde commercial et le solde courant sont équivalents.",False,"Non : le compte courant intègre aussi les services, les revenus et les transferts."),
("Un déficit courant traduit un besoin de financement vis-à-vis du reste du monde.",True,"Exact : il doit trouver une contrepartie dans le compte financier."),
("Un déficit extérieur est toujours le signe d’un problème économique.",False,"Non : il peut financer un investissement productif ; tout dépend de son origine et de sa soutenabilité."),
("L’identité X − M = (S − I) + (T − G) relie le solde extérieur à l’épargne et au solde public.",True,"Exact : c’est l’identité macroéconomique centrale du chapitre."),
("Le taux d’ouverture mesure le poids du commerce extérieur dans le PIB.",True,"Exact : c’est l’indicateur traditionnel principal."),
("Le commerce en valeur ajoutée donne les mêmes résultats que les statistiques brutes.",False,"Non : il corrige le double comptage des biens intermédiaires et modifie les classements."),
("La première mondialisation était plus migratoire que la mondialisation actuelle.",True,"Exact : les mouvements de population d’avant 1914 étaient proportionnellement bien plus massifs."),
("L’entre-deux-guerres est une période d’approfondissement de la mondialisation.",False,"Faux : c’est une période de repli, de protectionnisme et d’effondrement des flux."),
("La slowbalization équivaut à une démondialisation avérée.",False,"Non : la progression ralentit, mais l’ouverture ne recule pas massivement."),
("La montée des BRICS peut se lire comme un rééquilibrage après deux siècles de domination occidentale.",True,"Exact : c’est la lecture historique proposée dans le chapitre."),
]
OPEN=[
("Distinguez les trois dimensions de l’ouverture internationale.","L’ouverture commerciale porte sur les échanges de biens et de services entre résidents et non-résidents. L’ouverture productive concerne la circulation des facteurs de production, notamment à travers les investissements directs à l’étranger. L’ouverture financière et monétaire recouvre la circulation des capitaux de placement et les mouvements de devises qui les accompagnent. La mondialisation ne se réduit donc pas au commerce."),
("Distinguez IDE et investissement de portefeuille.","L’investissement direct à l’étranger est réalisé dans une logique productive : il vise un contrôle durable de l’activité implantée à l’étranger. L’investissement de portefeuille est un achat d’actifs financiers étrangers dans une logique de placement, sans prise de contrôle. Le premier relève de l’ouverture productive, le second de l’ouverture financière, et leur mobilité diffère fortement."),
("Présentez les trois configurations de la mondialisation chez Michalet.","La configuration internationale repose essentiellement sur les échanges commerciaux entre nations. La configuration multinationale met au centre l’implantation des firmes à l’étranger et l’investissement direct. La configuration globale se caractérise par la fragmentation de la production et l’unification des marchés financiers. Michalet montre ainsi que la mondialisation est un processus multidimensionnel."),
("Qu’est-ce que l’hypermondialisation ?","L’hypermondialisation désigne une ouverture quantitativement sans précédent, née du cumul des trois dimensions : échanges commerciaux, fragmentation productive et circulation massive des capitaux. Elle ne remplace pas les formes antérieures d’internationalisation mais les additionne, ce qui explique l’intensité des interdépendances contemporaines."),
("Expliquez l’analyse de Prebisch sur les termes de l’échange.","Prebisch montre que les pays spécialisés dans les produits primaires subissent une détérioration tendancielle de leurs termes de l’échange : le prix de leurs exportations progresse moins vite que celui de leurs importations manufacturées. Ils doivent donc exporter toujours davantage pour financer un même volume d’importations, ce qui enferme les périphéries dans leur spécialisation."),
("Qu’est-ce que la malédiction des ressources ?","La malédiction des ressources désigne le paradoxe selon lequel l’abondance de matières premières peut ralentir la diversification et le développement au lieu de les favoriser. La rente tirée des ressources décourage l’investissement dans d’autres secteurs, peut nourrir des institutions extractives et expose l’économie à la volatilité des cours mondiaux."),
("Que montre la courbe de l’éléphant ?","Elle représente les gains de revenu par percentile mondial entre 1988 et 2008. Elle met en évidence un double mouvement : de forts gains pour les classes moyennes des pays émergents et pour les très hauts revenus mondiaux, mais une quasi-stagnation pour les classes populaires des pays développés. Elle permet ainsi de concilier réduction des inégalités entre pays et renforcement de certaines inégalités internes."),
("Comment lit-on une balance des paiements ?","La balance des paiements enregistre toutes les opérations entre résidents et non-résidents. Le compte courant regroupe les biens, les services, les revenus et les transferts courants ; le compte financier enregistre les mouvements de capitaux. L’ensemble est équilibré par construction : un déficit courant a nécessairement une contrepartie dans le compte financier."),
("Expliquez l’identité X − M = (S − I) + (T − G).","Le solde extérieur est égal à la somme du solde d’épargne privée et du solde public. Un déficit extérieur traduit donc soit une épargne privée insuffisante au regard de l’investissement, soit un déficit public, soit les deux. Cette identité déplace l’analyse : le déficit commercial n’est pas seulement un problème de compétitivité, il renvoie aux comportements d’épargne et de finances publiques."),
("Un déficit extérieur est-il nécessairement un problème ?","Non. Un déficit courant traduit un besoin de financement, mais sa portée dépend de son origine : s’il finance un investissement productif, il peut préparer une croissance future et se résorber. Il devient préoccupant lorsqu’il finance de la consommation, qu’il repose sur des capitaux volatils ou qu’il devient insoutenable au regard des engagements extérieurs accumulés."),
("Pourquoi le commerce en valeur ajoutée modifie-t-il la mesure de la mondialisation ?","Les statistiques traditionnelles comptent la valeur totale d’un bien à chaque passage de frontière. Avec la fragmentation des chaînes de valeur, les biens intermédiaires traversent plusieurs fois les frontières, ce qui produit un double comptage et surestime les flux. Le commerce en valeur ajoutée ne retient que la valeur créée dans chaque pays et modifie sensiblement les soldes bilatéraux."),
("Qu’est-ce qu’une chaîne de valeur mondiale et quelles vulnérabilités crée-t-elle ?","Une chaîne de valeur mondiale correspond à la fragmentation des étapes de production entre plusieurs pays, chacune localisée selon les conditions de coût, de compétence ou d’accès au marché. Elle procure des gains d’efficacité, mais crée des dépendances sur des intrants critiques et expose les économies aux ruptures d’approvisionnement, ce qui nourrit aujourd’hui les débats sur la relocalisation."),
("Comparez la première mondialisation et la mondialisation contemporaine.","La première mondialisation, jusqu’en 1914, reposait sur la révolution des transports, l’étalon-or et des migrations massives, notamment européennes vers les Amériques. La mondialisation contemporaine est nettement moins migratoire, mais beaucoup plus financière et surtout productive, avec la fragmentation internationale des processus de production que la première ne connaissait pas."),
("Quelles leçons tirer du repli de l’entre-deux-guerres ?","La montée du protectionnisme et l’effondrement des flux montrent que l’ouverture internationale n’est jamais irréversible : elle dépend de choix politiques et d’un cadre institutionnel. Cette période s’accompagne aussi d’un basculement de puissance vers les États-Unis, ce qui rappelle que les phases de repli redistribuent les positions dominantes."),
("Assistons-nous à une démondialisation depuis 2008 ?","Le commerce mondial progresse moins vite depuis la crise et le taux d’ouverture stagne : on parle de slowbalization. Mais l’ouverture ne recule pas massivement et les chaînes de valeur demeurent. Il s’agit donc moins d’une démondialisation que d’un ralentissement accompagné d’une fragmentation : les échanges se recomposent en blocs régionaux et affinitaires."),
]
out=[]
for i,(q,opts,ans) in enumerate(QCM,1):
    out.append({"type":"qcm","q":q,"opts":opts,"ans":ans,"exp":f"Bonne réponse : {L[ans]}) {opts[ans]}","ch":21,"id":f"ch21-qcm-{i}"})
for i,(q,a,e) in enumerate(VF,1):
    out.append({"type":"vf","q":q,"ans":a,"exp":e,"ch":21,"id":f"ch21-vf-{i}"})
for i,(q,s) in enumerate(OPEN,1):
    out.append({"type":"open","q":q,"sample":s,"exp":s,"ch":21,"id":f"ch21-open-{i}"})
json.dump(out, open('ch21_quiz.json','w'), ensure_ascii=False)
from collections import Counter
print('total:',len(out), dict(Counter(x['type'] for x in out)))
assert len({x['id'] for x in out})==len(out)
for x in out:
    if x['type']=='qcm': assert len(x['opts'])==4 and 0<=x['ans']<4, x['id']
print('validation format : OK')
