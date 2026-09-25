def S(t,m,c,i,p,pl,cc): return dict(title=t,mobiliser=m,commentaire=c,intro=i,problematique=p,plan=pl,conclusion=cc)
def P(*parts):
    out=[]
    for titre, subs in parts:
        out.append(titre)
        for st, args in subs:
            out.append(st); out.extend(args)
    return out
