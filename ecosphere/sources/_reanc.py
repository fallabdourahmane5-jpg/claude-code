"""Réancre les cartes dont le bloc n'a pas de texte exploitable.

On ne change que l'ancre, jamais le contenu de la carte : on cherche le
bloc substantiel le plus proche, en privilégiant celui qui suit.
"""
import re
import sys
import fc_base as F

ch = sys.argv[1]
mod = sys.argv[2]
B = F.blocs(ch)


def bon(i):
    return (0 <= i < len(B)
            and B[i].get('g') not in ('h2', 'h3', 'h4', 'h5', 'table')
            and len(F.nz(F.texte_bloc(ch, i))) >= 25)


s = open(mod, encoding='utf-8').read()
chg = 0
for m in sorted(set(int(x) for x in re.findall(r'b=(\d+)\)', s))):
    if bon(m):
        continue
    for d in (1, 2, 3, 4, 5):
        if bon(m + d):
            s = s.replace('b=%d)' % m, 'b=%d)' % (m + d))
            print('  %d → %d  %s' % (m, m + d, F.texte_bloc(ch, m + d)[:60]))
            chg += 1
            break
    else:
        print('  %d : aucun bloc proche exploitable' % m)
open(mod, 'w', encoding='utf-8').write(s)
print('%d ancres corrigées' % chg)
