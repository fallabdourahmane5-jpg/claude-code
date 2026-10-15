# -*- coding: utf-8 -*-
"""Atlas des idées — chapitre 4 de deuxième année : entrées complètes."""

import at24a
import at24b

ENTREES = list(at24a.E) + list(at24b.E)

# Correction d'une entrée existante : l'Atlas du chapitre 1 mentionnait
# « Orain » sans prénom et un titre d'ouvrage incomplet.
CORRECTIONS = [{
    'ch': 1,
    'cible': 'Le capitalisme de la finitude',
    'n_ancien': 'Orain',
    'n': 'Arnaud Orain',
    'ou': 'Le Monde confisqué. Essai sur le capitalisme de la finitude '
          '(XVIe-XXIe siècle) (2025)',
    'li_ajout': [{
        'a': 'Arnaud Orain',
        'r': 'prolonge',
        't': 'Le troisième âge du capitalisme de la finitude explique le retour '
             'des stratégies mercantilistes étudiées au chapitre 4 de deuxième '
             'année.'}],
}]
