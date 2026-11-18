# -*- coding: utf-8 -*-
"""Atlas des idées : entrée manquante de Richard Lipsey (chapitre 5 de
deuxième année).

Deux idées du chapitre renvoyaient à Richard Lipsey sans qu'il dispose d'une
entrée dans l'Atlas : le renvoi s'affichait alors en texte simple au lieu
d'être cliquable. L'entrée est rédigée à partir du seul passage que le
document consacre à Lipsey — l'approfondissement théorique de la courbe de
Phillips en 1960 et sa reformulation en arbitrage inflation-chômage.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_lib.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_atl2.html'

E = {
 'n': 'Richard Lipsey',
 'd': '1928',
 'c': 'Keynésien',
 'ti': 'L’approfondissement théorique de la courbe de Phillips et le passage à '
       'l’arbitrage inflation-chômage',
 'af': "Lipsey approfondit en 1960 l’analyse théorique de la relation que "
       "Phillips avait établie en 1958 entre le chômage et la variation des "
       "salaires nominaux. L’apport est de nature théorique et non empirique : "
       "il ne s’agit pas de confirmer la corrélation observée au Royaume-Uni, "
       "mais de lui donner un fondement explicite du côté du marché du "
       "travail. C’est ce travail, puis la contribution de Paul Samuelson et "
       "de Robert Solow la même année, qui font passer la relation de son "
       "énoncé originel — chômage et salaires nominaux — à la forme sous "
       "laquelle elle est devenue célèbre : un arbitrage entre inflation et "
       "chômage. Le chapitre insiste sur cette chaîne d’attribution, parce "
       "qu’elle commande la portée de la critique ultérieure : ce que la "
       "stagflation des années 1970 a invalidé est la reformulation, non la "
       "relation que Phillips avait mesurée.",
 'me': "Le raisonnement se déroule en trois temps. Un : un chômage faible "
       "rend la main-d’œuvre rare, les entreprises qui veulent embaucher se "
       "la disputent et les salaires nominaux progressent vite ; un chômage "
       "élevé affaiblit le pouvoir de négociation des salariés et ralentit "
       "cette progression. Deux : la progression des salaires nominaux se "
       "répercute, par les coûts de production, sur le niveau général des "
       "prix — c’est le maillon qui transforme la relation salariale en "
       "relation inflationniste. Trois : il en résulte, pour les pouvoirs "
       "publics, l’apparence d’un menu stable, où réduire le chômage se paie "
       "d’une accélération de l’inflation et où désinflater se paie d’un "
       "chômage plus élevé. Le deuxième temps est celui qui fragilise "
       "l’ensemble : la répercussion dépend des gains de productivité, du "
       "comportement de marge des entreprises et du degré de concurrence, et "
       "rien ne garantit sa stabilité dans le temps.",
 'ex': "L’illustration du chapitre : un taux de chômage de 2,25 % correspond "
       "à une progression des salaires nominaux de 2 % ; si cette progression "
       "égale exactement les gains de productivité, l’inflation peut être "
       "nulle sous les hypothèses retenues.",
 'po': "La portée est double. D’abord, elle explique comment une régularité "
       "empirique limitée à un pays et à une période a pu devenir, pendant une "
       "décennie, l’instrument de réglage de la politique économique : c’est "
       "la reformulation théorique qui lui a donné cette autorité. Ensuite, "
       "elle permet de situer exactement la critique monétariste : Friedman "
       "ne conteste pas en 1968 la mesure de Phillips, il conteste la "
       "stabilité de l’arbitrage que la reformulation avait installée, en "
       "opposant l’ajustement des anticipations et l’existence d’un taux de "
       "chômage naturel. Savoir qui a écrit quoi est donc la condition pour "
       "formuler correctement la controverse.",
 'di': "À mobiliser dès qu’un sujet porte sur l’inflation, le chômage ou les "
       "limites des politiques de demande : citer « Lipsey, Samuelson et "
       "Solow (1960) » pour la reformulation, et réserver 1958 à Phillips, "
       "montre une maîtrise de la filiation que la seule mention de « la "
       "courbe de Phillips » ne donne pas.",
 'co': "Lipsey approfondit en 1960 l’analyse théorique de la courbe de "
       "Phillips : avec Samuelson et Solow, il fait passer la relation "
       "chômage-salaires nominaux à un arbitrage inflation-chômage, c’est-à-"
       "dire à la forme que la stagflation des années 1970 invalidera.",
 'ou': "Travaux de 1960 sur la courbe de Phillips",
 'no': ['courbe de Phillips', 'arbitrage inflation-chômage',
        'salaires nominaux', 'stagflation'],
 'li': [
   {'a': 'Alban William Phillips', 'r': 'prolonge',
    't': "Lipsey prolonge la relation que Phillips avait mesurée en 1958 "
         "entre chômage et variation des salaires nominaux."},
   {'a': 'Paul Samuelson', 'r': 'complement',
    't': "Samuelson et Solow contribuent la même année à populariser la "
         "lecture en termes d’inflation et de chômage."},
   {'a': 'Milton Friedman', 'r': 'opposition',
    't': "Friedman oppose en 1968 l’ajustement des anticipations et le taux "
         "de chômage naturel à l’idée d’un arbitrage durable."},
 ],
 'ch': [25],
}

s = open(SRC, encoding='utf-8').read()
i = s.find('id="eco-atlas-idees"')
assert i > 0
j = s.find('var DATA = ', i)
k = s.find('\n', j)
brut = s[j + len('var DATA = '):k].rstrip()
assert brut.endswith(';')
A = json.loads(brut[:-1])
assert json.dumps(A, ensure_ascii=False, separators=(',', ':')) == brut[:-1]

ch = [c for c in A['chapitres'] if c['k'] == 25]
assert len(ch) == 1
ch = ch[0]
modele = ch['e'][0]
assert set(E) == set(modele), set(E) ^ set(modele)
assert not any(x['n'] == E['n'] for x in ch['e']), 'entrée déjà présente'

# le modèle fixe l'ordre des champs
ordre = list(modele)
ch['e'].append({c: E[c] for c in ordre})

noms = {x['n'] for c in A['chapitres'] for x in c['e']}
for l in E['li']:
    assert l['a'] in noms, ('cible de lien absente de l’Atlas', l['a'])
    assert l['r'] in ('complement', 'opposition', 'prolonge'), l['r']

manquants = [(c['k'], l['a']) for c in A['chapitres'] for x in c['e']
             for l in (x.get('li') or []) if l['a'] not in noms]
print('idées : %d · liens non cliquables restants : %d'
      % (sum(len(c['e']) for c in A['chapitres']), len(manquants)))
for m in sorted(set(manquants)):
    print('   ch%-3s %s' % m)

neuf = 'var DATA = ' + json.dumps(A, ensure_ascii=False,
                                  separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]
open(DST, 'w', encoding='utf-8').write(s)
print('chapitre 25 : %d idées' % len(ch['e']))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
