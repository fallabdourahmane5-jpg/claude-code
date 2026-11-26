# -*- coding: utf-8 -*-
"""La grille d'autoévaluation, reprise de la fiche distribuée en cours."""

from meth_base import crit, groupe

GRILLE = [
 groupe('Introduction', [
   crit('i1', 'Mon introduction comporte 3 ou 4 paragraphes ; accroche et annonce '
               'du plan sont isolées.', ex=('intro', None),
        aide='Isolées = chacune forme un paragraphe à elle seule, séparé du '
             'reste par un retour à la ligne. Le correcteur doit les repérer '
             'd’un coup d’œil.'),
   crit('i2', 'Mon accroche ne présente pas d’erreurs et fait apparaître un '
               'enjeu du sujet.', ex=('intro', 'i2'),
        aide='Une accroche juste mais décorative ne compte pas : elle doit '
             'déjà faire sentir pourquoi le sujet pose problème.'),
   crit('i3', 'Je définis et analyse chacun des termes du sujet.',
        ex=('intro', 'i3'),
        aide='Sur « Faut-il toujours défendre le libre-échange ? », les trois '
             'termes à traiter sont « toujours », « défendre » et '
             '« libre-échange ». Définir ne suffit pas : il faut montrer ce '
             'que chaque mot engage.'),
   crit('i4', 'Mes définitions et mon analyse ouvrent les pistes de réponse '
               'défendues dans le devoir.', ex=('intro', 'i4'),
        aide='L’analyse des termes doit déjà contenir en germe le plan : si '
             'l’on peut supprimer une définition sans rien changer à la '
             'suite, c’est qu’elle ne sert à rien.'),
   crit('i5', 'Mon cadrage est clairement établi et justifié.',
        ex=('intro', 'i5'),
        aide='Cadrer, c’est dire ce qu’on traite — champ, espace, période — '
             'et surtout pourquoi ce découpage sert le sujet.'),
   crit('i6', 'Ma problématique est formulée de manière claire et respecte le '
               'sens du sujet.', ex=('intro', 'i6'),
        aide='Elle doit se lire comme une vraie question, découler de '
             'l’analyse des termes, et ne pas déplacer le sujet.'),
   crit('i7', 'Mon annonce de plan indique I, II (III) ; elle n’est ni '
               'simpliste ni contradictoire.', ex=('intro', 'i7'),
        aide='Simpliste = « oui puis non ». Contradictoire = une partie qui '
             'détruit la précédente sans la dépasser.'),
   crit('i8', 'Les titres de mes parties répondent directement au sujet ou à '
               'la problématique.', ex=('plan', 'i8'),
        aide='Un titre qui pourrait coiffer un chapitre de cours n’est pas un '
             'titre de partie : il faut y retrouver les termes du sujet.'),
 ], intro='Quatre paragraphes au plus : accroche ; analyse des termes ; '
          'cadrage et problématique ; annonce du plan.'),

 groupe('Annonce des sous-parties', [
   crit('s1', 'J’annonce A, B (C) dans un paragraphe distinct, en montrant '
               'leur logique d’organisation.', ex=('annonce', 's1'),
        aide='Ce paragraphe ouvre chaque grande partie. Il ne se contente pas '
             'de lister A, B, C : il dit pourquoi elles se suivent dans cet '
             'ordre.'),
   crit('s2', 'Leurs titres répondent au sujet ou à la problématique.',
        ex=('plan', 's2'),
        aide='Même exigence que pour les grandes parties, à l’échelle de la '
             'sous-partie.'),
 ], intro='Au début de chaque grande partie, un paragraphe court annonce les '
          'sous-parties et la logique qui les relie.'),

 groupe('Développement', [
   crit('d1', 'Mes parties sont équilibrées = à peu près le même nombre de '
               'lignes.', ex=('plan', 'd1'),
        aide='Se vérifie sur la copie entière : une partie deux fois plus '
             'courte signale un déséquilibre de la démonstration, pas '
             'seulement de la rédaction.'),
   crit('d2', 'Mes sous-parties sont consistantes : 2 ou 3 arguments '
               'apparaissent.', ex=('souspartie', 'd2'),
        aide='Un argument = un paragraphe. Une sous-partie d’un seul '
             'paragraphe n’est pas une sous-partie.'),
   crit('d3', 'Chaque paragraphe débute par un argument répondant '
               'explicitement au sujet = je retrouve les termes du sujet.',
        ex=('souspartie', 'd3'),
        aide='Le correcteur doit pouvoir lire les seules premières phrases de '
             'vos paragraphes et y retrouver votre démonstration.'),
   crit('d4', 'Je commence par une affirmation en rapport avec le sujet ; '
               'l’auteur intervient ensuite pour l’étayer.',
        ex=('souspartie', 'd4'),
        aide='L’ordre compte : c’est votre idée qui commande, l’auteur la '
             'soutient. « Pour Ricardo… » en tête de paragraphe inverse ce '
             'rapport.'),
   crit('d5', 'Quand une référence théorique centrale structure le paragraphe, '
               'les mécanismes sont expliqués.', ex=('souspartie', 'd5'),
        aide='Nommer un théorème ne prouve rien : il faut dérouler la chaîne '
             'causale, étape par étape.'),
   crit('d6', 'Chaque référence mobilisée est datée et contextualisée.',
        ex=('souspartie', 'd6'),
        aide='Datée = l’année de l’ouvrage ou de l’article. Contextualisée = '
             'ce à quoi l’auteur répondait quand il écrivait.'),
   crit('d7', 'Je précise les titres des références majeures : ouvrages '
               'soulignés, articles entre « guillemets ».',
        ex=('souspartie', 'd7'),
        aide='Sur la copie manuscrite, les titres d’ouvrages se soulignent à '
             'la règle ; les titres d’articles se mettent entre guillemets.'),
   crit('d8', 'Chaque paragraphe revient aux faits : histoire économique '
               'et/ou données chiffrées.', ex=('souspartie', 'd8'),
        aide='Le fait n’illustre pas : il démontre. Il faut donc dire ce qu’il '
             'établit, pas seulement le citer.'),
   crit('d9', 'Si j’utilise un graphique : axes nommés, variables explicites, '
               'légende si besoin et lecture commentée.',
        ex=('souspartie', 'd9'), na=True,
        aide='Critère à ignorer si vous n’avez tracé aucun graphique. Un '
             'graphique sans phrase de lecture ne rapporte rien.'),
 ], intro='Le développement se juge paragraphe par paragraphe : un argument, '
          'un auteur daté, un mécanisme déroulé, un fait qui démontre.'),

 groupe('Transitions', [
   crit('t1', 'Mes transitions sont visuellement séparées des parties qui les '
               'encadrent.', ex=('transition', 't1'),
        aide='Un saut de ligne avant et après, éventuellement un léger '
             'retrait : la transition doit se voir sans être lue.'),
   crit('t2', 'Elles font le point sur le raisonnement en lien avec la '
               'problématique, au-delà d’un bilan ou d’une annonce.',
        ex=('transition', 't2'),
        aide='« Nous avons vu… nous verrons… » n’est pas une transition : il '
             'faut nommer la question que la partie précédente laisse '
             'ouverte.'),
 ], intro='Une transition par changement de grande partie, entre I et II puis '
          'entre II et III.'),

 groupe('Conclusion', [
   crit('c1', 'Je réponds clairement au sujet en résumant la progression du '
               'raisonnement, sans réciter le plan ; ma réponse apporte '
               'davantage que l’introduction.', ex=('conclusion', 'c1'),
        aide='Test simple : si l’on peut recopier la conclusion à la place de '
             'l’introduction sans que rien ne change, elle n’apporte rien.'),
   crit('c2', 'Mon ouverture prolonge réellement la réflexion ; elle ne '
               'remplace pas un argument du développement.',
        ex=('conclusion', 'c2'),
        aide='Une bonne ouverture déplace le critère de jugement. Une '
             'mauvaise ouverture est un argument qu’on a oublié de traiter.'),
 ], intro='La conclusion répond, puis ouvre — dans cet ordre, et jamais '
          'l’inverse.'),

 groupe('Forme', [
   crit('f1', 'Ma copie est lisible, propre, sans erreur de syntaxe ni fautes '
               'd’orthographe.', ex=('souspartie', 'f1'),
        aide='Se vérifie sur la copie entière. Relisez en fin d’épreuve en ne '
             'cherchant que les accords et la ponctuation : c’est le quart '
             'd’heure le mieux employé.'),
 ], intro='Le dernier critère de la grille, et le seul qui se gagne '
          'entièrement à la relecture.'),
]
