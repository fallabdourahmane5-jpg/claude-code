import json,sys
d=json.load(open('blocs_bruts.json',encoding='utf-8'))
for ch in sys.argv[1:]:
    b=d[ch]; vus=[]; 
    for i,x in enumerate(b):
        p=[t for t in (x.get('p') or []) if t]
        k=' › '.join(p)
        if not vus or vus[-1][0]!=k: vus.append([k,i,i])
        else: vus[-1][2]=i
    # fusionner
    agg={}
    for k,a,z in vus: agg.setdefault(k,[0,a]); agg[k][0]+= z-a+1
    print('=== CH %s === %d blocs, %d sections'%(ch,len(b),len(agg)))
    for k,(n,a) in agg.items(): print('  %4d  [%4d]  %s'%(n,a,k))
