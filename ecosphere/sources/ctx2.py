# -*- coding: utf-8 -*-
"""Pour chaque expression, les passages du cours les plus informatifs."""
import re, sys, rech_base as R
B = R.blocs()
def ctx(e, n=4):
    rx = re.compile(r'(?<![a-z0-9])' + re.escape(R.nz(e)) + r'(?![a-z0-9])')
    pris, vus = [], set()
    for prio in ('db', 'h', 'p'):
        for k in R.ORDRE:
            for i, x in enumerate(B[k]):
                g = x['g']
                if prio == 'db' and g != 'db': continue
                if prio == 'h' and g not in ('h2','h3','h4'): continue
                if prio == 'p' and g not in ('p','li'): continue
                t = ' '.join(x['x'].split())
                if not rx.search(R.nz(t)): continue
                if len(t) < 30 or t[:60] in vus: continue
                vus.add(t[:60])
                if prio == 'h':
                    suite = []
                    for y in B[k][i+1:i+5]:
                        if y['g'] in ('h2','h3'): break
                        if len(y['x']) > 25: suite.append(' '.join(y['x'].split()))
                    t = R.titre_propre(t) + ' → ' + ' | '.join(suite)[:300]
                pris.append('ch%s [%s] %s' % (k, g, t[:330]))
                if len(pris) >= n: return pris
    return pris
if __name__ == '__main__':
    for e in [x.strip() for x in open(sys.argv[1]) if x.strip() and not x.startswith('#')]:
        print('### ' + e)
        for l in ctx(e, int(sys.argv[2]) if len(sys.argv) > 2 else 3):
            print('   ' + l)
