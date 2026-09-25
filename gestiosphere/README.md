# Gestiosphère — Licence 2

Application de révision **indépendante d'Écosphère**. Elle reprend la structure, la navigation et les fonctionnalités d'Écosphère v181, avec d'autres cours.

- **Fichier à ouvrir :** `gestiosphere.html`. C'est un fichier autonome, qui marche hors ligne ; seules les polices viennent de Google Fonts.
- **Matières :** comptabilité des sociétés (6 documents), microéconomie (13), marketing (7). La macroéconomie apparaît « à venir » en attendant ses documents.
- **Sauvegardes :** clés `gs_state` et `gs_failed_questions` du navigateur, avec export et import depuis l'onglet Progrès. Aucune clé `eco_` n'est lue ni écrite, et le build refuse d'en produire.

## Onglets

Accueil par matière · Cours (cours complet, définitions, auteurs et ouvrages, méthode, sujets du chapitre, liens entre chapitres) · Quiz (générateur multi-chapitres, questions ratées) · Fiches · Recherche · Auteurs & ouvrages · Sujets corrigés (chapitres à mobiliser, méthode et pièges, corrigé) · Méthode · Courbes & schémas · Cartes mentales · Formules · Repères · Progrès.

## Reconstruire

```bash
cd gestiosphere/src
python3 build.py
```

`build.py` injecte le contenu de `compta.py`, `micro.py` et `marketing.py` (plus `macro.py` s'il existe) dans `template.html`. Il vérifie aussi :

- que les identifiants sont uniques ;
- que chaque chapitre « à mobiliser » et chaque lien existe ;
- que les réponses des quiz sont valides ;
- qu'il n'y a aucune clé Écosphère.

Les écritures comptables sont contrôlées dès leur création (débit = crédit). Les montants des corrigés sont calculés, pas saisis à la main (`calc_compta.py`, balance de l'exercice 11).

## Ajouter la macroéconomie

Créer `src/macro.py` avec une fonction `matiere()` qui renvoie `id='macro'`, sur le modèle de `micro.py`. Le build la prend en compte automatiquement.
