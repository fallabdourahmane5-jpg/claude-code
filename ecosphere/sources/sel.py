# -*- coding: utf-8 -*-
"""Vérifie, pour une liste d'expressions, si une définition existe déjà."""
import sys, socle, rech_base as R
from audit_familles import defs_existantes
D = defs_existantes()
TXT = {k: R.nz(socle.TXT[k]) for k in R.ORDRE}
def etat(e):
    c = R.cle(e)
    occ = {k: TXT[k].count(R.nz(e)) for k in R.ORDRE}
    occ = {k: v for k, v in occ.items() if v}
    v = D.get(c)
    return c, occ, v
if __name__ == '__main__':
    for e in [x.strip() for x in open(sys.argv[1]) if x.strip() and not x.startswith('#')]:
        c, occ, v = etat(e)
        print('%-40s %-34s %s' % (e[:40],
              ','.join('%s:%d' % (k, n) for k, n in occ.items())[:34],
              ('DÉJÀ [' + ','.join(sorted(v['src'])) + '] ' + v['t'][:34]) if v else '—'))
