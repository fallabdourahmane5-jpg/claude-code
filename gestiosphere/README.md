# Gestiosphère — Licence 2

Application de révision **indépendante d'Écosphère**. Elle reprend la structure, la navigation et les fonctionnalités d'Écosphère v181, avec d'autres cours.

- **Fichier à ouvrir :** `gestiosphere.html`. C'est un fichier autonome, qui marche hors ligne ; seules les polices viennent de Google Fonts.
- **Matières :** comptabilité des sociétés (6 documents), microéconomie (13), macroéconomie (5 documents de notes : économie ouverte) et marketing (7).
- **Sauvegardes :** clés `gs_state` et `gs_failed_questions` du navigateur, avec export et import depuis l'onglet Progrès. Aucune clé `eco_` n'est lue ni écrite, et le build refuse d'en produire.

## Onglets

Accueil par matière · Cours (cours complet, définitions, auteurs et références, méthode, sujets du chapitre, liens entre chapitres) · Quiz (générateur multi-chapitres, questions ratées) · Fiches · Recherche (lexique A–Z, mécanismes, fiche complète par notion) · Auteurs & références (apport au cours, quand le citer, phrase de copie, jeu « Qui suis-je ? ») · Sujets corrigés (chapitres à mobiliser, méthode et pièges, corrigé) · Méthode · Courbes & schémas · Cartes mentales · Formules · Repères · Progrès.

## Reconstruire

```bash
cd gestiosphere/src
python3 build.py
```

`build.py` injecte le contenu de `compta.py`, `micro.py`, `macro.py` et `marketing.py` dans `template.html`. Il vérifie aussi :

- que les identifiants sont uniques ;
- que chaque chapitre « à mobiliser » et chaque lien existe ;
- que les réponses des quiz sont valides ;
- qu'il n'y a aucune clé Écosphère.

Les écritures comptables sont contrôlées dès leur création (débit = crédit). Les montants des corrigés sont calculés, pas saisis à la main (`calc_compta.py`, balance de l'exercice 11).

## Macroéconomie

`src/macro_cours.py` contient les 5 chapitres : balance des paiements, change, TCR et Marshall-Lerner, IS-LM-PTINC, politiques économiques. `src/macro.py` contient les graphiques, les quiz, les sujets corrigés (calculs vérifiés par `assert`) et le reste de la matière. `src/macro_exp.py` contient les explications détaillées des courbes.
