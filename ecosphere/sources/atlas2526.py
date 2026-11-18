# -*- coding: utf-8 -*-
"""Atlas des idées — chapitres 5 et 6 de deuxième année : entrées complètes."""

import at25a
import at25b
import at25c
import at26a
import at26b

ENTREES = (list(at25a.E) + list(at25b.E) + list(at25c.E)
           + list(at26a.E) + list(at26b.E))

# Compléments de liens sur des entrées déjà présentes dans l'Atlas : ces
# auteurs y figurent pour d'autres chapitres, et le document de cours justifie
# d'y renvoyer explicitement vers les chapitres 5 et 6.
#   'ch' : chapitre de l'entrée à compléter · 'n' : nom exact de l'entrée
#   'li_ajout' : liens ajoutés s'ils sont absents
CORRECTIONS = [
    {'ch': 3, 'n': 'John Maynard Keynes',
     'li_ajout': [{
         'a': 'John Hicks', 'r': 'prolonge',
         't': "Le chapitre 5 de deuxième année formalise la demande effective "
              "et la préférence pour la liquidité dans le modèle IS-LM, "
              "construit par Hicks en 1937 et prolongé par Hansen en 1941."}]},
    {'ch': 2, 'n': 'Robert Mundell',
     'li_ajout': [{
         'a': 'Marcus Fleming', 'r': 'prolonge',
         't': "Les chapitres 5 et 6 de deuxième année mobilisent le modèle "
              "Mundell-Fleming et le triangle des incompatibilités pour juger "
              "de l'efficacité des politiques et du choix du régime de change."}]},
    {'ch': 8, 'n': 'Henri Bourguinat',
     'li_ajout': [{
         'a': 'Marcus Fleming', 'r': 'prolonge',
         't': "Le chapitre 5 de deuxième année relie les trois D à "
              "l'horizontalisation de la courbe BP, donc à la perte "
              "d'autonomie monétaire des États."}]},
    {'ch': 21, 'n': 'Paul Volcker',
     'li_ajout': [{
         'a': 'Guillermo Calvo', 'r': 'prolonge',
         't': "Le chapitre 6 de deuxième année fait du choc Volcker la "
              "contre-épreuve de l'insularisation, et la source de la peur du "
              "flottement établie par Calvo et Reinhart."}]},
]
