# -*- coding: utf-8 -*-
"""Formules des chapitres 5 et 6 de deuxième année, pour la rubrique
« Formules » de la recherche.

Dans ces deux chapitres, les formules sont portées par des blocs
`<div class="formula">`, que l'énumération des blocs du cours ne retient pas :
elles échapperaient donc à l'index. Chaque entrée reprend le texte exact de la
formule et le numéro du bloc qui la précède immédiatement, ce qui permet
d'ouvrir le passage. Le montage vérifie, pour chaque entrée, que la formule se
trouve bien à cet endroit du cours.
"""

# (chapitre, bloc, intitulé, formule)
FML = [
 # ------------------------------------------------- chapitre 5 : agrégats
 ('25', 171, 'Produit intérieur brut — approche par la production',
  'PIB = somme des valeurs ajoutées brutes + impôts sur les produits '
  '− subventions sur les produits.'),
 ('25', 176, 'Produit intérieur brut — approche par la demande',
  'PIB = C + I + G + X − M.'),
 ('25', 186, 'Produit intérieur brut — approche par les revenus',
  'PIB = rémunération des salariés + excédent brut d’exploitation + revenu '
  'mixte brut + impôts sur la production et les importations − subventions.'),

 # ----------------------------------- chapitre 5 : consommation et équilibre
 ('25', 470, 'Fonction de consommation keynésienne', 'C = C₀ + cY'),
 ('25', 479, 'Propension marginale à consommer', 'c = ΔC / ΔY'),
 ('25', 512, 'Revenu d’équilibre en économie fermée sans État',
  'Yₑ = (C₀ + I₀) / (1 − c)'),

 # --------------------------------------- chapitre 5 : les multiplicateurs
 ('25', 753, 'Principe du multiplicateur',
  'Multiplicateur = ΔY / ΔDépense initiale'),
 ('25', 779, 'Propension marginale à épargner', 's = 1 − c = 0,2'),
 ('25', 787, 'Épargne engendrée par le multiplicateur', 'ΔS = s × ΔY'),
 ('25', 791, 'L’épargne supplémentaire égale l’investissement initial',
  'ΔS = ΔI = 100'),
 ('25', 818, 'Revenu d’équilibre, forme résolue', 'Y = (C₀ + I) / (1 − c)'),
 ('25', 826, 'Multiplicateur d’investissement', 'kI = 1 / (1 − c)'),
 ('25', 849, 'Revenu d’équilibre avec État',
  'Y = (C₀ − cT + cF + I + G) / (1 − c)'),
 ('25', 861, 'Multiplicateur des dépenses publiques',
  'kG = ΔY / ΔG = 1 / (1 − c)'),
 ('25', 893, 'Multiplicateur des prestations sociales',
  'kF = ΔY / ΔF = c / (1 − c)'),
 ('25', 934, 'Multiplicateur fiscal', 'kT = ΔY / ΔT = −c / (1 − c)'),

 # ------------------------------------------ chapitre 5 : économie ouverte
 ('25', 1022, 'Équilibre macroéconomique en économie ouverte',
  'Y = C + I + G + X − M'),
 ('25', 1043, 'Propension marginale à importer', 'm = ΔM / ΔY'),
 ('25', 1061, 'Revenu d’équilibre en économie ouverte',
  'Y = (C₀ + I + G + X) / (1 − c + m)'),
 ('25', 1062, 'Multiplicateur des dépenses autonomes en économie ouverte',
  'k = 1 / (1 − c + m)'),
 ('25', 3070, 'Fonction d’importation', 'M = M₀ + mY.'),

 # ------------------------------------------- chapitre 5 : IS, LM et BP
 ('25', 341, 'Courbe IS : équilibre du marché des biens et services',
  'I = S.'),
 ('25', 345, 'Mécanisme de la courbe IS',
  'Taux d’intérêt ↓ → investissement ↑ → demande globale ↑ → production et '
  'revenu ↑.'),
 ('25', 351, 'Courbe LM : équilibre du marché de la monnaie', 'M = L.'),
 ('25', 357, 'Mécanisme de la courbe LM',
  'Revenu ↑ → demande de monnaie pour transactions ↑ → taux d’intérêt ↑.'),
 ('25', 2652, 'Triple équilibre en économie ouverte',
  'IS = LM = BP → triple équilibre macroéconomique.'),
 ('25', 2772, 'Diagnostic de l’équilibre interne',
  'Y < Ype → sous-emploi → politique de relance.'),

 # ---------------------------------------- chapitre 6 : taux de change
 ('26', 700, 'Parité des pouvoirs d’achat absolue, cotation au certain',
  'e = P* / P.'),
 ('26', 751, 'Mécanisme de la parité des pouvoirs d’achat relative',
  'inflation domestique > inflation étrangère → prix domestiques relatifs ↑ '
  '→ compétitivité-prix ↓ → pression à la dépréciation de la monnaie '
  'domestique.'),
 ('26', 2117, 'Condition de Marshall-Lerner', '|εX| + |εM| > 1'),

 # ------------------------------- chapitre 6 : marges et taux réels
 ('26', 2519, 'Taux de marge des entreprises', 'Taux de marge = EBE / VA × 100'),
 ('26', 2545, 'Taux d’intérêt réel',
  'Taux d’intérêt réel ≈ taux d’intérêt nominal − taux d’inflation.'),
 ('26', 2553, 'Effet de la désinflation sur les taux réels',
  'inflation ↓ + taux nominaux maintenus relativement élevés → taux d’intérêt '
  'réel ↑.'),
 ('26', 2575, 'Désinflation et priorité au désendettement',
  'inflation ↓ → taux d’intérêt réels ↑ → poids réel de l’endettement ↑ → '
  'priorité au désendettement.'),
]
