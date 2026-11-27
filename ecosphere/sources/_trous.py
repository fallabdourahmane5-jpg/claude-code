import sys, bisect
sys.path.insert(0,'.')
import importlib
import fc_base as F
ch=sys.argv[1]; mod=importlib.import_module(sys.argv[2])
B=F.blocs(ch); anc=sorted({k['b'] for k in mod.L})
subst=[i for i,b in enumerate(B) if b.get('g') in ('p','li','db','table') and len(b.get('x') or '')>40]
trous=[]; cur=[]
for i in subst:
    j=bisect.bisect_left(anc,i)
    d=min([abs(i-anc[k]) for k in (j-1,j) if 0<=k<len(anc)] or [999])
    if d>20: cur.append(i)
    else:
        if cur: trous.append((cur[0],cur[-1],len(cur))); cur=[]
if cur: trous.append((cur[0],cur[-1],len(cur)))
trous.sort(key=lambda t:-t[2])
for a,b,n in trous[:int(sys.argv[3]) if len(sys.argv)>3 else 10]:
    print(f"{a}-{b} ({n}) :", (B[a].get('p') or [''])[0][:70], '|', (B[a].get('p') or ['',''])[1][:50])
