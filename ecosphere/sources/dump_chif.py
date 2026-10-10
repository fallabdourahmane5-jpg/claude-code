# -*- coding: utf-8 -*-
import io, importlib
CH = {}
for m in ('chif_a','chif_b','chif_c'):
    mod = importlib.import_module(m)
    for k,v in mod.CH.items():
        CH[k]=v
ORD=['1','2','3','4','5','6','7','8','9','10','21','22','23']
out=[]
n=0
for c in ORD:
    d=CH[c]
    for imp,key in (('p','prio'),('c','comp')):
        for i,x in enumerate(d.get(key,[]),1):
            n+=1
            out.append('%s|%s%d| v=%s | u=%s | nat=%s | z=%s | p=%s | s=%s'%(c,imp,i,x['v'],x['u'],x['nat'],x['z'],x['p'],x['s']))
io.open('dump_chif.txt','w',encoding='utf-8').write('\n'.join(out))
print(n)
