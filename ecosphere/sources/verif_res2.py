# -*- coding: utf-8 -*-
import importlib, glob, os, re, sys
ORD = ['1','2','3','4','5','6','7','8','9','10','21','22','23']
R = {}
for f in sorted(glob.glob('res2_*.py')):
    m = importlib.import_module(os.path.basename(f)[:-3])
    R.update(m.R)
tot = 0
for c in ORD:
    if c not in R:
        continue
    r = R[c]
    for k in ('q','ess','parties','ae','arg','deb','lien','min'):
        assert r.get(k), (c, k)
    assert r['q'].rstrip().endswith('?'), c
    n = len(r['ess'])
    nsp = sum(len(p['sp']) for p in r['parties'])
    txt = r['q'] + r['ess']
    for p in r['parties']:
        txt += p['t'] + p['v']
        assert p['sp'], (c, p['t'])
        assert len(p['v']) > 40, (c, p['t'])
        for s in p['sp']:
            assert s.get('t') and s.get('d'), (c, p['t'], s.get('t'))
            assert isinstance(s['d'], list), (c, s['t'])
            for para in s['d']:
                assert 100 < len(para) < 1500, (c, s['t'], len(para))
            txt += s['t'] + ' '.join(s['d']) + s.get('mec','') + s.get('lim','')
    for a in r['ae']:
        assert a['k'] in ('a','e'), (c, a['n']); txt += a['n'] + a['i']
    txt += ' '.join(r['arg'] + r['deb'] + r['min'] + [l['p'] for l in r['lien']])
    tot += len(txt)
    print('ch%-3s %d parties · %2d sous-parties · %2d auteurs/ex · %5d signes (ess %d)'
          % (c, len(r['parties']), nsp, len(r['ae']), len(txt), n))
print('%d chapitres, %d signes au total' % (len([c for c in ORD if c in R]), tot))
