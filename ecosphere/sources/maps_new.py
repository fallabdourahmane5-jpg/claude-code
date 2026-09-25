# -*- coding: utf-8 -*-
import json

def B(titre, *enfants):
    return {"title": titre, "children": list(enfants)}
def S(titre, *feuilles):
    return {"title": titre, "children": list(feuilles)}

MAPS = {}

# ---------------- CHAPITRE 9 ----------------
MAPS["9"] = {
 "title": "Chapitre 9 — Taille et stratégies des entreprises en concurrence imparfaite",
 "core": "Taille et stratégies des entreprises en concurrence imparfaite",
 "branches": [
  B("Croissance et Concentration",
    S("Mouvement historique", "Révolution industrielle", "Gains de productivité", "Mondialisation"),
    S("Formes de concentration", "Horizontale (éliminer concurrents)", "Verticale (amont/aval)", "Conglomérale (diversification)"),
    S("Exemples et Logiques", "Standard Oil (Rockefeller)", "General Electric (Conglomérat)", "Économies d’échelle")),
  B("Stratégies en Concurrence Imparfaite",
    S("Pouvoir de marché", "Price maker", "Indice de Lerner", "Barrières à l’entrée"),
    S("Différenciation des produits", "Verticale (qualité/gamme)", "Horizontale (style/lieu)", "Concurrence monopolistique (Chamberlin)"),
    S("Pratiques anticoncurrentielles", "Cartels et ententes", "Ventes liées", "Prix prédateurs", "Dénigrement"),
    S("Modèles d’analyse", "Dilemme du prisonnier (instabilité)", "Théorie des marchés contestables", "Modèle SCP (Structure-Comportement-Performance)")),
  B("Théories de la Firme",
    S("Approche néoclassique", "Firme automate", "Combinaison K et L"),
    S("Approche contractuelle", "Nœud de contrats (Alchian/Demsetz)", "Théorie de l’agence (Jensen/Meckling)", "Relation Principal/Agent"),
    S("Approche transactionnelle", "Coûts de transaction (Coase)", "Rationalité limitée (Simon)", "Opportunisme (Williamson)")),
  B("Diversité et Organisation des Formes",
    S("PME et ETI", "Souplesse et réactivité", "Fragilité financière", "Dépendance bancaire"),
    S("Nouveaux modèles", "Firmes-réseaux (Apple)", "Districts industriels (Marshall)", "Effets d’agglomération (Silicon Valley)"),
    S("Évolution du travail", "Taylorisme (standardisation)", "Toyotisme (flexibilité)", "Formes U et M (Chandler)")),
  B("Politiques de Concurrence",
    S("Cadre institutionnel", "Lois Antitrust (USA)", "Droit européen (TFUE 101/102)", "Autorité de la concurrence (FR)"),
    S("Domaines d’intervention", "Surveillance des aides d’État", "Contrôle des concentrations", "Sanction des abus de position dominante", "Procédure de clémence"),
    S("Défis contemporains", "Souveraineté numérique", "Digital Markets Act (DMA)", "Régulation des GAFAM", "Marché pertinent (Local vs Mondial)")),
 ]}

# ---------------- CHAPITRE 10 (carte fournie en anglais, traduite) ----------------
MAPS["10"] = {
 "title": "Chapitre 10 — Sociologie des organisations et du travail",
 "core": "Sociologie des organisations et du travail",
 "branches": [
  B("Rationalité et bureaucratie",
    S("Max Weber",
      "4 types d’action : finalité, valeur, tradition, affect",
      "Bureaucratie : spécialisation, hiérarchie, règles, impersonnalité",
      "3 types de domination : traditionnelle, charismatique, légale-rationnelle",
      "Concepts : rationalisation, cage d’acier, désenchantement"),
    S("Christian Morel",
      "Décisions absurdes : erreurs collectives de groupes rationnels",
      "Causes : biais cognitifs, conformisme, pensée de groupe (Janis)",
      "Cas : échec du lancement de la navette Challenger",
      "Métarègles : check-lists, avocat du diable, consensus"),
    S("Gérald Bronner",
      "Marché cognitif : dérégulation de l’information sur Internet",
      "Invariants mentaux : avarice cognitive, visibilité, peurs",
      "Dangers : chambres d’écho, biais de confirmation, fausses informations",
      "Solutions : esprit critique, vérification des sources")),
  B("Relations humaines et analyse stratégique",
    S("Elton Mayo",
      "École des relations humaines : une motivation au-delà du salaire",
      "Effet Hawthorne : être observé accroît la productivité",
      "Facteurs : cohésion du groupe, reconnaissance, écoute"),
    S("Michel Crozier",
      "Deux mondes : formel (organigramme) vs informel (sociogramme)",
      "Zone d’incertitude : le contrôle d’une ressource rare comme pouvoir",
      "Stratégie : des acteurs usant de leurs marges de manœuvre",
      "Cercle vicieux bureaucratique : rigidité et nouvelles règles")),
  B("Travail et intégration sociale",
    S("Émile Durkheim",
      "Solidarité : mécanique (ressemblance) vs organique (différence)",
      "Intégration vs régulation : groupes et normes sociales",
      "Pathologies : anomie (absence de normes), égoïsme (isolement)"),
    S("Robert Castel",
      "Société salariale : l’emploi comme statut et protection",
      "Désaffiliation : vulnérabilité et perte des liens sociaux"),
    S("Florence Aubenas",
      "Le Quai de Ouistreham : la vie des travailleurs précaires",
      "Enjeux : bas salaires, transport, isolement social")),
  B("Réalités de l’emploi et action collective",
    S("Mutations structurelles",
      "Salarisation : domination du travail salarié",
      "Tertiarisation : essor du secteur des services",
      "Désindustrialisation : transformation du monde ouvrier"),
    S("Dynamiques du marché",
      "Flexibilité : ajuster la main-d’œuvre à l’activité",
      "Précarité : CDI vs CDD, temps partiel, contrats temporaires",
      "Chômage : définition du BIT vs catégories de France Travail",
      "Halo du chômage : frontière entre activité et inactivité"),
    S("Inégalités",
      "Écarts femmes-hommes : salaires et statut professionnel",
      "Pauvreté laborieuse : le phénomène des travailleurs pauvres"),
    S("Syndicats et conflit",
      "Crise syndicale : recul lié à l’individualisme et à la mondialisation",
      "Institutionnalisation des conflits : négociation organisée vs grèves")),
 ]}

# ---------------- DEUXIÈME ANNÉE — CHAPITRE 1 ----------------
MAPS["21"] = {
 "title": "Deuxième année, chapitre 1 — L’ouverture internationale et la mondialisation",
 "core": "L’ouverture internationale et la mondialisation",
 "branches": [
  B("Dimensions de l’Ouverture",
    S("Ouverture commerciale", "Échanges de biens et services", "Commerce international"),
    S("Ouverture productive", "Mobilité des facteurs de production", "IDE (Capital productif)", "Migrations internationales (Travail)"),
    S("Ouverture financière et monétaire", "Investissements de portefeuille", "Marché des changes et devises", "Taux de change")),
  B("Processus de Mondialisation",
    S("Définition et Dynamique", "Interdépendance et intégration", "Processus dynamique et réversible", "Fragmentation et régionalisation"),
    S("Configurations Historiques (Michalet)", "Dimension internationale (Commerce)", "Dimension multinationale (Production/FMN)", "Dimension globale (Finance)", "Logique cumulative"),
    S("Vagues Historiques", "1870-1913 : Première mondialisation", "Post-1945 : Remondialisation", "1990-2008 : Hypermondialisation")),
  B("Asymétries et Inégalités",
    S("Rapports de Force", "Centre vs Périphérie (Prebisch)", "Institutions extractives (Acemoglu)", "DIT traditionnelle"),
    S("Gagnants et Perdants", "Stratégies de montée en gamme", "Malédiction des ressources", "Maladie hollandaise", "Privilège exorbitant du dollar"),
    S("Inégalités (Milanovic)", "Courbe de l’éléphant", "Rattrapage des émergents (Chine)", "Stagnation des classes populaires du Nord", "Théorème Stolper-Samuelson")),
  B("Analyse Macroéconomique",
    S("Balance des Paiements", "Compte courant (Flux réels)", "Compte financier (Mouvements de capitaux)", "Déficit courant = Besoin de financement"),
    S("Équilibres Fondamentaux", "Identité X-M = (S-I) + (T-G)", "Déficits jumeaux (États-Unis)", "Surépargne et sous-investissement"),
    S("Position Extérieure Nette (PEN)", "Stock d’actifs vs engagements", "Créancier vs Débiteur net", "Risque de Sudden Stop")),
  B("Mesures et Indicateurs",
    S("Indicateurs Traditionnels", "Taux d’ouverture", "Taux de couverture", "Taux de pénétration", "Élasticité-prix"),
    S("Commerce en Valeur Ajoutée", "Chaînes de Valeur Mondiales (CVM)", "Fragmentation productive (DIPP)", "Biais des statistiques brutes (iPhone)", "Dépendance aux intrants critiques")),
 ]}

json.dump(MAPS, open('maps_v83_new.json','w'), ensure_ascii=False)
for k,v in MAPS.items():
    nb_sub=sum(len(b['children']) for b in v['branches'])
    nb_leaf=sum(len(s['children']) for b in v['branches'] for s in b['children'])
    print(f"  carte {k:>3} : {len(v['branches'])} branches · {nb_sub} sous-branches · {nb_leaf} feuilles")
