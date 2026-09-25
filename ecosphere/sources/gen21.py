# -*- coding: utf-8 -*-
import json, re, html
b=json.load(open('ch21_blocks.json'))
PARTS=[0,190,748,1166,1617,1731,2419,2923,3385,3812,4053,4257,4371,4486,4662,5108,5351,5822,6255]
END=('.',',',':',';','!','…')

def roman(k):
    v=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    s=''
    for n_,sym in v:
        while k>=n_: s+=sym; k-=n_
    return s

def clean(t):
    t=t.replace(' ',' ').replace(' ',' ')
    t=re.sub(r'([.!?;,:])([A-ZÀÂÉÈÊÎÔÛÇ«“])', r'\1 \2', t)
    t=re.sub(r'([A-ZÀ-Ý]{2,})([A-ZÀ-Ý][a-zà-ÿ])', r'\1 \2', t)
    t=re.sub(r'\s*(➡️?|->|→)\s*', ' → ', t)
    t=re.sub(r'\s+([,.])', r'\1', t)
    t=re.sub(r'([,;])([A-Za-zÀ-ÿ])', r'\1 \2', t)
    t=re.sub(r'\s*([;:!?])\s*', r' \1 ', t)
    t=re.sub(r'(\w)\(', r'\1 (', t); t=re.sub(r'\)(\w)', r') \1', t)
    t=re.sub(r'\(\s+','(',t); t=re.sub(r'\s+\)',')',t)
    return re.sub(r'\s+',' ',t).strip()

def esc(t): return html.escape(clean(t), quote=False)
def rich(x):
    rs=x.get('runs') or []
    if not rs: return esc(x['txt'])
    tot=sum(len(r['t']) for r in rs) or 1
    g=sum(len(r['t']) for r in rs if r['b'])/tot
    if g>0.85 or g<0.15: return esc(x['txt'])
    m=[]
    for r in rs:
        if m and m[-1]['b']==r['b']: m[-1]['t']+=r['t']
        else: m.append({'t':r['t'],'b':r['b']})
    return clean(''.join((f"<strong>{html.escape(k['t'],quote=False)}</strong>" if k['b'] else html.escape(k['t'],quote=False)) for k in m))
def letter(n):
    s=''
    while True:
        s=chr(65+n%26)+s; n=n//26-1
        if n<0: break
    return s

BAD={'intro','introduction','conclusion','exemple','remarque','note','plan','problématique','objectif',
     'idée','idée générale','mot-clé','attention','bilan','question','questions','rappel','définition',
     'transition','exemples','application','synthèse','en résumé'}
def is_def(t):
    if t.startswith('→'): return None
    t2=t.lstrip('👉 ').strip()
    m=re.match(r'^([A-ZÀ-Ý][^:=]{2,58}?)\s*[:=]\s+(\S.{20,})$', t2)
    if not m: return None
    term=m.group(1).strip()
    if len(term.split())>7 or term.lower() in BAD: return None
    if re.search(r'\b(est|sont|il y a|on |nous |peut|doit|faut|donc|ainsi|mais|car|parce)\b', term, re.I): return None
    return (term, m.group(2).strip())
def is_h4(x):
    if x['k']!='P' or x['num'] is not None or not x.get('bold'): return False
    t=clean(x['txt'])
    return 3<len(t)<=70 and not t.endswith(END) and not re.search(r'[=→<>]',t) and not t.startswith(('→','👉','•'))
def is_head(x):
    if x['k']!='P' or x['num'] is not None or x.get('bold'): return False
    t=x['txt'].strip()
    if not t or len(t)>95: return False
    if t.rstrip().endswith(END): return False
    if t.startswith(('→','➡','👉','•','↓')) or re.search(r'[=<>]',t): return False
    return True
def arrow(t): return t.lstrip().startswith(('➡','→','👉'))
def item_like(x):
    if x['k']!='P' or x['num'] is not None or arrow(x['txt']): return False
    t=clean(x['txt'])
    return len(t)<=130 and t.endswith((',',';'))

# pre-passe : qualifier les candidats-titres
cand=[i for i,x in enumerate(b) if is_head(x)]
candset=set(cand); prev={}; last=None
for i,x in enumerate(b):
    prev[i]=last
    if x['k']=='P' and x['txt'].strip(): last=x['txt'].strip()
    elif x['k']=='TBL': last='[tableau]'
runs_=[]; cur=[]
for i in cand:
    if cur and i==cur[-1]+1: cur.append(i)
    else:
        if cur: runs_.append(cur)
        cur=[i]
if cur: runs_.append(cur)
real=set()
for r in runs_:
    if len(r)>=3: continue
    for i in r:
        if (prev.get(i) or '').rstrip().endswith(':'): continue
        real.add(i)
for p in PARTS: real.discard(p)

out=[]
for pi,start in enumerate(PARTS):
    end = PARTS[pi+1] if pi+1<len(PARTS) else len(b)
    title=clean(b[start]['txt'])
    if title.isupper():
        ACR={'DIT','PIB','IDE','DIPP','BRICS','OMC','FMI','ONU','UE','PME','FMN','CVM','RNB','TVA','OCDE'}
        mots=title.split(' ')
        title=' '.join(w if w.strip('.,:;()') in ACR else (w.lower()) for w in mots)
        title=title[0].upper()+title[1:]
    out.append('\n<div class="nb ch21-premium-course">')
    out.append(f'  <h2>{roman(pi+1)}. {html.escape(title,quote=False)}</h2>')
    sub=0; i=start+1; buf=[]; colon=False
    def flush():
        global buf
        if buf:
            out.append('  <ul>'+''.join(f'<li>{v}</li>' for v in buf)+'</ul>'); buf=[]
    while i<end:
        x=b[i]
        if x['k']=='TBL':
            flush(); colon=False; rows=x['rows']
            t=['  <div class="table-wrap"><table class="dt">']
            for ri,r in enumerate(rows):
                tg='th' if ri==0 else 'td'
                t.append('<tr>'+''.join(f'<{tg}>{esc(c)}</{tg}>' for c in r)+'</tr>')
            out.append(''.join(t)+'</table></div>'); i+=1; continue
        raw=x['txt'].strip()
        if not raw or raw in ('↓','↑'): i+=1; continue
        if i in real:
            flush(); colon=False
            out.append(f'  <h3>{letter(sub)}. {esc(raw)}</h3>'); sub+=1; i+=1; continue
        c=clean(raw)
        if is_h4(x) and not colon:
            flush(); out.append(f'  <h4>{esc(raw)}</h4>'); i+=1; continue
        d=is_def(c)
        if d:
            flush(); colon=False
            out.append(f'  <div class="db"><div class="dt">{html.escape(d[0],quote=False)}</div>'
                       f'<div class="dd">{html.escape(d[1],quote=False)}</div></div>'); i+=1; continue
        explicite = (x['num'] is not None) or item_like(x) or (i in candset)
        if explicite or (colon and len(c)<=150 and not arrow(c)):
            buf.append(rich(x))
            if explicite: colon=False
            elif c.rstrip().endswith(('.','!','?')): colon=False
            i+=1
            if not (i<end and (b[i].get('num') is not None or item_like(b[i]))):
                if i<end and b[i]['k']=='P' and i not in real and not is_h4(b[i]) and not arrow(b[i]['txt']):
                    t2=clean(b[i]['txt'])
                    suite = t2[:1].islower() or len(t2)<=60
                    if len(t2)<=140 and t2.endswith('.') and suite:
                        buf.append(rich(b[i])); i+=1; colon=False
            continue
        flush()
        if arrow(c):
            if len(c)>90: out.append(f'  <div class="alertb"><p>{rich(x)}</p></div>')
            else: out.append(f'  <p>{rich(x)}</p>')
            colon=False
        elif re.search(r'[=<>]', c) and len(c)<=110 and c.count(' ')<16:
            out.append(f'  <div class="formula">{esc(c)}</div>'); colon=False
        else:
            out.append(f'  <p>{rich(x)}</p>')
            colon = c.rstrip().endswith(':')
        i+=1
    flush()
    out.append('</div>')
h='\n'.join(out)
open('ch21_cours.html','w').write(h)
DB=h.count('class="db"'); FO=h.count('class="formula"'); AL=h.count('class="alertb"')
print(f"cours : {len(h):,} caractères".replace(',',' '))
print(f"  h2={h.count('<h2>')} h3={h.count('<h3>')} h4={h.count('<h4>')} p={h.count('<p>')} li={h.count('<li>')} db={DB} formule={FO} alerte={AL}")
