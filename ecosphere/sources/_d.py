import json,sys
d=json.load(open('blocs_bruts.json',encoding='utf-8'))
ch=sys.argv[1]; a=int(sys.argv[2]); z=int(sys.argv[3]) if len(sys.argv)>3 else a+60
MAX=int(sys.argv[4]) if len(sys.argv)>4 else 420
b=d[ch]; prev=None
for i in range(a,min(z,len(b))):
    o=b[i]; p=' › '.join([t for t in (o.get('p') or []) if t])
    if p!=prev: print('\n--- %s'%p[:150]); prev=p
    t=o.get('x') or ' '.join(x for x in (o.get('dt'),o.get('dd')) if x)
    t=' '.join(t.split())
    if len(t)>MAX: t=t[:MAX]+'…'
    if o.get('g') in ('h2','h3','h4','h5') and t and p.endswith(t[:60]): continue
    print('%4d %s'%(i,t))
