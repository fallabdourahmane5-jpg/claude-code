# -*- coding: utf-8 -*-
import json
MAP={
"title":"Deuxième année — Chapitre 1 : Mondialisation, ouverture internationale et déséquilibres",
"sub":"Dimensions de l’ouverture, définitions et configurations, asymétries et inégalités, balance des paiements, mesure du commerce, chaînes de valeur, histoire des mondialisations.",
"core":"Mondialisation",
"branches":[
 {"title":"Dimensions de l’ouverture","items":["Commerciale : biens et services","Productive : IDE, facteurs","Financière et monétaire : capitaux, devises"]},
 {"title":"Définir la mondialisation","items":["Interdépendance et intégration","Michalet : internationale → multinationale → globale","Hypermondialisation = cumul des trois"]},
 {"title":"Asymétries","items":["Prebisch : centre / périphérie, termes de l’échange","Échange inégal, DIT traditionnelle","Acemoglu & Robinson : institutions extractives"]},
 {"title":"Gagnants et perdants","items":["Consommateur gagnant, travailleur exposé","Milanovic : courbe de l’éléphant","Inégalités entre pays vs internes"]},
 {"title":"Balance des paiements","items":["Compte courant / compte financier","X − M = (S − I) + (T − G)","Déficits jumeaux, soutenabilité"]},
 {"title":"Mesurer la mondialisation","items":["Taux d’ouverture, taux d’exportation","Double comptage des biens intermédiaires","Commerce en valeur ajoutée"]},
 {"title":"Chaînes de valeur","items":["DIPP et fragmentation","Dépendances et vulnérabilités","Relocalisation, souveraineté"]},
 {"title":"Histoire des mondialisations","items":["Première mondialisation : étalon-or, migrations","Entre-deux-guerres : protectionnisme, repli","Depuis 1945 : remondialisation, slowbalization"]},
],
"legend":[
 {"k":"Auteurs","v":"Michalet, Giraud, Prebisch, Acemoglu & Robinson, Milanovic."},
 {"k":"Pièges","v":"Mondialisation ≠ commerce seul ; solde commercial ≠ solde courant ; balance des paiements équilibrée par construction ; déficit extérieur ≠ problème automatique ; DIT traditionnelle ≠ DIPP ; slowbalization ≠ démondialisation ; décrochage européen relatif, non absolu."},
 {"k":"Repères","v":"Première mondialisation jusqu’en 1914 · étalon-or · entre-deux-guerres : protectionnisme et basculement vers les États-Unis · après 1945 : remondialisation · courbe de l’éléphant 1988-2008 · ralentissement depuis 2008."},
],
"schemas":[
 {"title":"Les trois dimensions de l’ouverture","tag":"Mécanisme",
  "flow":["Ouverture commerciale","Ouverture productive (IDE, DIPP)","Ouverture financière","Ouverture monétaire","Cumul des trois","Hypermondialisation"],
  "note":"L’hypermondialisation additionne les dimensions, elle ne les remplace pas."},
 {"title":"Du solde extérieur à ses causes","tag":"Balance des paiements",
  "flow":["Solde courant","X − M","(S − I) épargne privée","(T − G) solde public","Besoin de financement","Contrepartie au compte financier"],
  "note":"Le déficit extérieur renvoie aux comportements d’épargne, pas seulement à la compétitivité."},
 {"title":"Le biais du double comptage","tag":"Mesure",
  "flow":["Fragmentation des chaînes","Biens intermédiaires","Passages répétés aux frontières","Flux bruts gonflés","Commerce en valeur ajoutée","Soldes bilatéraux corrigés"],
  "note":"Les statistiques traditionnelles surestiment l’ouverture réelle."},
 {"title":"Les phases historiques","tag":"Histoire",
  "flow":["Première mondialisation (→1914)","Repli de l’entre-deux-guerres","Remondialisation après 1945","Hypermondialisation","Ralentissement depuis 2008","Slowbalization / fragmentation"],
  "note":"L’ouverture n’est pas irréversible : elle dépend de choix politiques."},
]}

CTX = """DEUXIÈME ANNÉE — CHAPITRE 1 : Mondialisation, ouverture internationale et déséquilibres extérieurs.
L'ouverture internationale a trois dimensions : commerciale (échanges de biens et services entre résidents et non-résidents), productive (circulation des facteurs, IDE), financière et monétaire (capitaux de placement, devises, marché des changes).
IDE = investissement réalisé dans un autre pays dans une logique productive et de contrôle durable. Investissement de portefeuille = achat d'actifs financiers étrangers dans une logique de placement. Distinguer capital productif et capital financier.
Mondialisation = processus d'interdépendance et d'intégration croissantes. Charles-Albert Michalet : processus multidimensionnel, trois configurations — internationale (commerce), multinationale (IDE, implantation des firmes), globale (fragmentation productive et unification financière). Hypermondialisation = cumul des trois dimensions, ouverture quantitativement sans précédent.
Pierre-Noël Giraud : les globalisations comme généralisation des compétitions entre territoires. Compétition pour attirer les capitaux. Privilège exorbitant américain lié au statut international du dollar.
Déplacement du centre de gravité : domination européenne lors de la première mondialisation, leadership américain après 1945, déplacement vers l'Asie émergente avec l'hypermondialisation. BRICS : rééquilibrage après deux siècles de domination occidentale. Chine : d'acteur secondaire à géant économique ; rivalité économique et technologique avec les États-Unis ; arsenalisation de la politique économique. Décrochage relatif de l'Europe : baisse du poids dans le PIB mondial et des parts de marché. Divergence croissante entre pays en développement.
Asymétries : Prebisch et la logique centre / périphérie, détérioration des termes de l'échange, DIT traditionnelle (spécialisation verticale). Acemoglu et Robinson : institutions extractives. Théories de l'échange inégal. Économie du développement. Limites des stratégies trop fermées. Malédiction des ressources = l'abondance de matières premières peut freiner la diversification et le développement.
Firmes multinationales : d'abord recherche de ressources et de marchés, puis firme globale et DIPP (décomposition internationale des processus productifs). Qui fixe les règles, l'État ou la firme ? Stratégies offensives (Chine), défensives (États-Unis), indécises (Union européenne).
Gagnants et perdants : le ménage consommateur est généralement gagnant, le ménage travailleur gagnant ou perdant selon son exposition, le ménage épargnant peut bénéficier de la globalisation financière. Milanovic : big bang des inégalités avec la révolution industrielle ; courbe de l'éléphant 1988-2008 ; la mondialisation réduit les inégalités entre pays tout en renforçant certaines inégalités internes.
Balance des paiements : enregistre les opérations entre résidents et non-résidents ; compte courant (biens, services, revenus, transferts), compte de capital, compte financier (mouvements de capitaux). Équilibrée par construction. Solde commercial ≠ solde courant. Identité : Y = C + I + G + X − M et Y = C + S + T, d'où X − M = (S − I) + (T − G). Déficits jumeaux sous Reagan. Un déficit extérieur traduit un besoin de financement ; il n'est pas toujours un problème : tout dépend de son origine et de sa soutenabilité. Déséquilibres extérieurs mondiaux et inquiétudes sur la stabilité financière internationale.
Mesure : taux d'ouverture = [(X + M) / 2] / PIB × 100 ; taux d'exportation = X / PIB × 100. Problème du double comptage des biens intermédiaires dans les chaînes de valeur. Commerce en valeur ajoutée : ne retient que la valeur créée dans chaque pays, corrige les soldes bilatéraux.
Chaînes de valeur mondiales = fragmentation des étapes de production entre plusieurs pays. Contenu en importations des exportations. Dépendances et vulnérabilités, ruptures d'approvisionnement, relocalisation, souveraineté économique.
Histoire : première mondialisation jusqu'en 1914 (révolution des transports, étalon-or, migrations massives de l'Europe vers les Amériques, première mondialisation financière). Repli de l'entre-deux-guerres : protectionnisme, effondrement des flux, basculement de puissance vers les États-Unis. Après 1945 : remondialisation, hypermondialisation, nouvelle géographie des échanges vers l'Asie. Mondialisation contemporaine : moins migratoire, beaucoup plus financière et productive. Depuis 2008 : ralentissement du commerce mondial, slowbalization, question de la démondialisation et de la fragmentation ; la stagnation du taux d'ouverture ne signifie pas nécessairement une démondialisation."""

METHODE = """<div class="nb"><h2>✏️ Méthode — Deuxième année, chapitre 1</h2><h3>Copies types</h3><ul><li><strong>Mondialisation</strong> : ne jamais la réduire au commerce. Poser d’emblée les trois dimensions et mobiliser les configurations de Michalet.</li><li><strong>Solde commercial / solde courant</strong> : confusion la plus fréquente. Le compte courant intègre aussi services, revenus et transferts.</li><li><strong>Balance des paiements</strong> : elle est équilibrée <em>par construction</em>. Ce sont ses soldes internes qui informent, jamais son total.</li><li><strong>Déficit extérieur</strong> : jamais « bon » ou « mauvais » en soi. Passer par X − M = (S − I) + (T − G) pour en identifier l’origine.</li><li><strong>DIT traditionnelle ≠ DIPP</strong> : la première est une spécialisation verticale par produits, la seconde une fragmentation des étapes de production.</li><li><strong>Inégalités</strong> : toujours préciser l’échelle. Entre pays elles se réduisent, à l’intérieur elles peuvent croître — c’est tout le sens de la courbe de l’éléphant.</li><li><strong>Slowbalization</strong> : ralentissement de la progression, pas recul des flux. Ne pas conclure trop vite à la démondialisation.</li><li><strong>Décrochage européen</strong> : relatif, largement mécanique du fait du rattrapage des émergents.</li></ul>
<h3>Références à mobiliser</h3><ul><li><strong>Michalet</strong> : mondialisation multidimensionnelle, trois configurations.</li><li><strong>Giraud</strong> : globalisations comme généralisation des compétitions.</li><li><strong>Prebisch</strong> : centre / périphérie, détérioration des termes de l’échange.</li><li><strong>Acemoglu &amp; Robinson</strong> : institutions extractives.</li><li><strong>Milanovic</strong> : big bang des inégalités, courbe de l’éléphant.</li></ul>
<h3>Formules à savoir écrire</h3><ul><li>Y = C + I + G + X − M &nbsp;et&nbsp; Y = C + S + T</li><li><strong>X − M = (S − I) + (T − G)</strong></li><li>Taux d’ouverture = [(X + M) / 2] / PIB × 100</li><li>Taux d’exportation = X / PIB × 100</li></ul>
<h3>Repères chronologiques</h3><ul><li>Première mondialisation : jusqu’en 1914, sous étalon-or.</li><li>Entre-deux-guerres : protectionnisme et effondrement des flux.</li><li>Après 1945 : remondialisation puis hypermondialisation.</li><li>Courbe de l’éléphant : 1988-2008.</li><li>Ralentissement du commerce mondial : depuis 2008.</li></ul>
<div class="alertb"><p><strong>Réflexe de dissertation :</strong> presque tous les sujets du chapitre se règlent en opposant <em>les gains globaux de l’ouverture</em> et <em>leur répartition inégale</em>, ou <em>ce que mesurent les indicateurs</em> et <em>ce qui se passe réellement</em>. Poser l’une de ces deux tensions sécurise le plan.</p></div></div>"""

json.dump({"map":MAP,"ctx":CTX,"methode":METHODE}, open('ch21_extras.json','w'), ensure_ascii=False)
print('branches:',len(MAP['branches']),'| schémas:',len(MAP['schemas']),'| légende:',len(MAP['legend']))
print('contexte:',len(CTX),'car. | méthode:',len(METHODE),'car.')
