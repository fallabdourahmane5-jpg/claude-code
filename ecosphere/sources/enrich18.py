# -*- coding: utf-8 -*-
import json
# id -> complément à ajouter au champ « Chapitres à mobiliser »
ADD={
# ---- chapitre 1 ----
"ch1-7":"Ch. 21 — 2ᵉ année ch. 1 (inégalités mondiales, courbe de l’éléphant de Milanovic)",
"ch1-8":"Ch. 10 (coopération et conflit dans l’organisation, interdépendance chez Crozier)",
"ch1-18":"Ch. 21 — 2ᵉ année ch. 1 (inégalités entre pays et inégalités internes) · Ch. 10 (précarisation, pauvreté laborieuse)",
"ch1-20":"Ch. 10 (société salariale et désaffiliation chez Robert Castel)",
# ---- chapitre 2 ----
"ch2-10":"Ch. 21 — 2ᵉ année ch. 1 (globalisation financière, capitaux de portefeuille) · Ch. 9 (financement des grandes firmes)",
"ch2-15":"Ch. 21 — 2ᵉ année ch. 1 (marché des changes, privilège exorbitant du dollar)",
"ch2-16":"Ch. 21 — 2ᵉ année ch. 1 (déséquilibres mondiaux, volatilité des capitaux, Hélène Rey)",
"ch2-18":"Ch. 21 — 2ᵉ année ch. 1 (ouverture financière, IDE et investissements de portefeuille)",
"ch2-19":"Ch. 21 — 2ᵉ année ch. 1 (globalisation financière et cercle vicieux de Nurkse)",
# ---- chapitre 3 ----
"ch3-5":"Ch. 10 (Crozier contre Marx : un pouvoir diffus et relationnel)",
"ch3-7":"Ch. 9 (théories concurrentes de la firme) · Ch. 10 (pluralité des approches en sciences sociales)",
"ch3-8":"Ch. 21 — 2ᵉ année ch. 1 (termes de l’échange chez Prebisch, protectionnisme éducateur de List, 1841)",
"ch3-11":"Ch. 9 (politiques de concurrence, marchés contestables) · Ch. 21 — 2ᵉ année ch. 1 (retour du protectionnisme)",
"ch3-12":"Ch. 21 — 2ᵉ année ch. 1 (List 1841, tarif Hawley-Smoot 1930, entre-deux-guerres)",
"ch3-13":"Ch. 21 — 2ᵉ année ch. 1 (Bairoch, Mythes et paradoxes de l’histoire économique, 1993)",
"ch3-15":"Ch. 9 (destruction créatrice, concentration et innovation)",
# ---- chapitre 4 ----
"ch4-1":"Ch. 10 (action sociale chez Weber, rationalité limitée chez Simon)",
"ch4-2":"Ch. 10 (avarice cognitive et marché cognitif chez Bronner, système 1 de Kahneman)",
"ch4-3":"Ch. 9 (concurrence imparfaite, concurrence monopolistique de Chamberlin, 1933)",
"ch4-11":"Ch. 10 (rationalité limitée de Simon, décisions absurdes de Morel)",
"ch4-12":"Ch. 10 (Bronner : marché cognitif, invariants mentaux, chambres d’écho)",
"ch4-14":"Ch. 10 (biais cognitifs, conformisme d’Asch, pensée de groupe de Janis)",
"ch4-15":"Ch. 9 (pouvoir de marché, barrières à l’entrée, indice de Lerner)",
"ch4-16":"Ch. 9 (contestabilité, brevets, stratégies d’exclusion)",
"ch4-17":"Ch. 9 (théorie de l’agence, opportunisme et coûts de transaction chez Williamson)",
"ch4-18":"Ch. 9 (effets de réseau, Digital Markets Act, contestabilité effondrée)",
"ch4-19":"Ch. 9 (monopole naturel, monopole contestable, démantèlement)",
# ---- chapitre 5 ----
"ch5-4":"Ch. 9 (monopole naturel, régulation plutôt que fragmentation)",
"ch5-5":"Ch. 9 (effets de réseau, avantage du premier entrant, Digital Markets Act)",
"ch5-10":"Ch. 9 (politiques de concurrence : aides d’État, concentrations, cartels, abus)",
"ch5-16":"Ch. 9 (monopole naturel, contrôle des prix et de l’accès)",
"ch5-17":"Ch. 9 (barrières réglementaires) · Ch. 21 — 2ᵉ année ch. 1 (compétition des territoires, Giraud)",
"ch5-18":"Ch. 9 (concentration, barrières à l’entrée, contestabilité)",
# ---- chapitre 6 ----
"ch6-1":"Ch. 21 — 2ᵉ année ch. 1 (ouverture, hypermondialisation, chaînes de valeur)",
"ch6-3":"Ch. 9 (concentration et innovation, rente et barrières à l’entrée)",
"ch6-8":"Ch. 9 (destruction créatrice freinée par les positions dominantes)",
"ch6-11":"Ch. 21 — 2ᵉ année ch. 1 (courbe de l’éléphant, inégalités entre et dans les pays)",
"ch6-14":"Ch. 21 — 2ᵉ année ch. 1 (DIPP, délocalisation) · Ch. 10 (transformation du monde ouvrier)",
"ch6-18":"Ch. 9 (financement de la R&D, contestabilité et incitation à innover)",
"ch6-19":"Ch. 9 (politique industrielle et concurrence) · Ch. 21 — 2ᵉ année ch. 1 (relocalisation, souveraineté)",
"ch6-20":"Ch. 10 (travail, précarisation, halo du chômage)",
# ---- chapitre 7 ----
"ch7-4":"Ch. 21 — 2ᵉ année ch. 1 (Milanovic, inégalités mondiales)",
"ch7-7":"Ch. 21 — 2ᵉ année ch. 1 (malédiction des ressources, termes de l’échange de Prebisch)",
"ch7-13":"Ch. 21 — 2ᵉ année ch. 1 (courbe de l’éléphant 1988-2008, rattrapage des émergents)",
"ch7-14":"Ch. 21 — 2ᵉ année ch. 1 (BRICS, déplacement du centre de gravité, rivalité Chine/États-Unis)",
"ch7-15":"Ch. 21 — 2ᵉ année ch. 1 (DIT traditionnelle, montée en gamme, protectionnisme éducateur de List)",
"ch7-17":"Ch. 21 — 2ᵉ année ch. 1 (malédiction des ressources, institutions extractives d’Acemoglu et Robinson)",
# ---- chapitre 8 ----
"ch8-1":"Ch. 9 (taille et innovation, contestabilité, brevets)",
"ch8-3":"Ch. 9 (théories de la firme : Coase, Williamson, Alchian et Demsetz) · Ch. 10 (Crozier, acteurs et marges de manœuvre)",
"ch8-4":"Ch. 9 (effets de réseau, Digital Markets Act) · Ch. 21 — 2ᵉ année ch. 1 (plateformes mondiales, souveraineté numérique)",
"ch8-5":"Ch. 9 (théorie de l’agence chez Jensen et Meckling, créancier résiduel)",
"ch8-11":"Ch. 10 (entreprise comme lieu de coopération et de conflit, parties prenantes)",
"ch8-12":"Ch. 9 (théorie de l’agence, nœud de contrats) · Ch. 10 (pouvoir informel chez Crozier)",
"ch8-13":"Ch. 9 (abus de position dominante, marché pertinent, DMA)",
"ch8-14":"Ch. 9 (gouvernance actionnariale, théorie de l’agence)",
}
json.dump(ADD, open('enrich_1_8.json','w'), ensure_ascii=False)
from collections import Counter
c=Counter(k.split('-')[0] for k in ADD)
print("sujets enrichis :", len(ADD))
print("répartition :", dict(sorted(c.items())))
