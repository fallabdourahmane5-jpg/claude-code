# -*- coding: utf-8 -*-
import json

def S(t,*f): return {"title":t,"children":list(f)}

# ---- carte visuelle (moteur v83, arborescence de ton image) ----
V83_6 = {
 "title": "Chapitre 6 — La croissance économique",
 "core": "Croissance économique",
 "branches": [
  S("Définitions et Mesures",
    "PIB en volume (croissance réelle)", "Augmentation durable de la production",
    "Caractère cumulatif et exponentiel", "Croissance vs Développement"),
  S("Faits Stylisés et Histoire",
    "Stagnation pré-industrielle (Malthus)", "Rupture de la Révolution industrielle",
    "Inégalités temporelles et géographiques", "Rattrapage économique"),
  S("Modèles Classiques de Croissance",
    S("Rostow : Vision Linéaire", "5 étapes du développement", "Rôle central du Take-off", "Société de consommation de masse"),
    S("Gerschenkron : Vision Différenciée", "Avantage du retard initial", "Sauts technologiques", "Rôle des banques et de l’État")),
  S("Théories de la Croissance",
    S("Harrod-Domar (Post-keynésien)", "Instabilité fondamentale", "Équilibre sur le fil du rasoir", "Déséquilibre épargne/investissement"),
    S("Solow (Néoclassique)", "Rendements marginaux décroissants", "Convergence vers l’état stationnaire", "Progrès technique exogène (résidu)"),
    S("Croissance Endogène", "Romer : R&D et idées", "Lucas : Capital humain", "Barro : Capital public", "Aghion : Destruction créatrice")),
  S("Productivité et Progrès Technique",
    "Productivité Globale des Facteurs (PGF)", "Croissance extensive vs intensive",
    "Loi du déversement (Sauvy)", "Société hyper-industrielle (Veltz)"),
  S("Défis Contemporains",
    S("Stagnation Séculaire", "Hansen et Summers", "Affaissement de la demande globale", "Ralentissement de l’innovation (Gordon)"),
    S("Inégalités", "Courbe de Kuznets", "Courbe de l’éléphant (Milanovic)", "Rente de citoyenneté"),
    S("Soutenabilité", "Développement durable (Brundtland)", "Croissance verte et inclusive", "Réindustrialisation stratégique")),
 ]}

# ---- panneau texte + schémas (MAP_DATA, même format que les autres chapitres) ----
MAP_6 = {
 "title":"Chapitre 6 — La croissance économique",
 "sub":"Définitions et mesure · faits stylisés · Rostow et Gerschenkron · Harrod-Domar, Solow et croissance endogène · productivité · défis contemporains.",
 "core":"Croissance économique",
 "branches":[
  {"title":"Définitions et mesures","items":["PIB en volume (croissance réelle)","Augmentation durable de la production","Caractère cumulatif et exponentiel","Croissance ≠ développement"]},
  {"title":"Faits stylisés et histoire","items":["Stagnation pré-industrielle (Malthus)","Rupture de la révolution industrielle","Inégalités temporelles et géographiques","Rattrapage économique"]},
  {"title":"Modèles classiques","items":["Rostow : 5 étapes, take-off, consommation de masse","Gerschenkron : avantage du retard, sauts technologiques","Rôle des banques et de l’État"]},
  {"title":"Harrod-Domar","items":["Instabilité fondamentale","Équilibre sur le fil du rasoir","Déséquilibre épargne / investissement"]},
  {"title":"Solow","items":["Rendements marginaux décroissants","Convergence vers l’état stationnaire","Progrès technique exogène (résidu)"]},
  {"title":"Croissance endogène","items":["Romer : R&D et idées","Lucas : capital humain","Barro : capital public","Aghion : destruction créatrice"]},
  {"title":"Productivité et progrès technique","items":["Productivité globale des facteurs (PGF)","Croissance extensive vs intensive","Loi du déversement (Sauvy)","Société hyper-industrielle (Veltz)"]},
  {"title":"Défis contemporains","items":["Stagnation séculaire (Hansen, Summers, Gordon)","Inégalités : Kuznets, éléphant, rente de citoyenneté","Soutenabilité : Brundtland, croissance verte, réindustrialisation"]},
 ],
 "legend":[
  {"k":"Auteurs","v":"Malthus, Rostow, Gerschenkron, Harrod, Domar, Solow, Romer, Lucas, Barro, Aghion, Sauvy, Veltz, Hansen, Summers, Gordon, Kuznets, Milanovic, Brundtland."},
  {"k":"Pièges","v":"Croissance ≠ développement ; Solow explique la convergence mais laisse le progrès technique exogène ; la croissance endogène l’internalise ; la loi du déversement n’est pas automatique ; stagnation séculaire ≠ crise conjoncturelle."},
  {"k":"Repères","v":"Take-off de Rostow · résidu de Solow · rapport Brundtland 1987 · courbe de Kuznets · courbe de l’éléphant 1988-2008."},
 ],
 "schemas":[
  {"title":"Du modèle de Solow à la croissance endogène","tag":"Théorie",
   "flow":["Accumulation du capital","Rendements décroissants","État stationnaire","Progrès technique exogène","Internalisation : R&D, capital humain","Croissance auto-entretenue"],
   "note":"La croissance endogène répond à la limite majeure de Solow : le résidu inexpliqué."},
  {"title":"Deux lectures du rattrapage","tag":"Histoire",
   "flow":["Rostow : étapes universelles","Take-off","Consommation de masse","Gerschenkron : avantage du retard","Sauts technologiques","Rôle des banques et de l’État"],
   "note":"Trajectoire unique chez Rostow, trajectoires différenciées chez Gerschenkron."},
  {"title":"Croissance et emploi","tag":"Productivité",
   "flow":["Gains de productivité","Destruction d’emplois dans le secteur","Baisse des prix","Hausse du pouvoir d’achat","Demande nouvelle","Créations d’emplois ailleurs"],
   "note":"La loi du déversement de Sauvy décrit un mécanisme, pas une garantie."},
  {"title":"Les défis contemporains","tag":"Enjeux",
   "flow":["Ralentissement de la productivité","Affaissement de la demande","Stagnation séculaire","Montée des inégalités","Contrainte écologique","Croissance verte et inclusive"],
   "note":"La question n’est plus seulement le rythme, mais la nature de la croissance."},
 ]}

json.dump({"v83":V83_6,"map":MAP_6}, open('ch6_maps.json','w'), ensure_ascii=False)
nb_sub=sum(len(b['children']) for b in V83_6['branches'])
nb_leaf=sum(len(c.get('children',[])) if isinstance(c,dict) else 0 for b in V83_6['branches'] for c in b['children'])
print(f"carte visuelle : {len(V83_6['branches'])} branches · {nb_sub} nœuds de niveau 2 · {nb_leaf} feuilles")
print(f"panneau texte  : {len(MAP_6['branches'])} branches · {len(MAP_6['schemas'])} schémas · {len(MAP_6['legend'])} entrées de légende")
