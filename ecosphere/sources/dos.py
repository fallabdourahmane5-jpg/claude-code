# -*- coding: utf-8 -*-
"""Recherche de clés de dossiers « Autour d'une notion » par titre."""
import json, sys, unicodedata, re
D=json.load(open('autour_payload.json',encoding='utf-8'))
R=[(x['cle'],x['titre'],x['ens']) for x in D['dossiers'] if x['etat']=='redige']
def nz(s):
    s=unicodedata.normalize('NFD',str(s)).lower()
    s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9 ]+',' ',s)
if __name__=='__main__':
    q=nz(' '.join(sys.argv[1:]))
    mots=[m for m in q.split() if m]
    out=[(c,t,e) for c,t,e in R if all(m in nz(t) for m in mots)]
    for c,t,e in out[:40]: print('%-36s ens%-3s %s'%(c,e,t))
    print('(%d résultats)'%len(out))
