# -*- coding: utf-8 -*-
import json, sys, xml.etree.ElementTree as ET
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
A='http://schemas.openxmlformats.org/drawingml/2006/main'
n=sys.argv[1]
root=ET.parse(f'ch{n}x/word/document.xml').getroot(); body=root.find(f'{{{W}}}body')
def runs(p):
    out=[]
    for r in p.iter(f'{{{W}}}r'):
        t=''.join(x.text or '' for x in r.findall(f'{{{W}}}t'))
        if not t: continue
        rPr=r.find(f'{{{W}}}rPr')
        out.append({'t':t,'b': rPr is not None and rPr.find(f'{{{W}}}b') is not None})
    return out
def numinfo(p):
    pPr=p.find(f'{{{W}}}pPr')
    if pPr is None: return None
    x=pPr.find(f'{{{W}}}numPr')
    if x is None: return None
    il=x.find(f'{{{W}}}ilvl')
    return int(il.get(f'{{{W}}}val')) if il is not None else 0
blocks=[]
for el in body:
    tag=el.tag.split('}')[1]
    if tag=='p':
        rs=runs(el); t=''.join(r['t'] for r in rs).strip()
        img = el.find(f'.//{{{A}}}blip') is not None
        if not t and not img: continue
        blocks.append({'k':'P','txt':t,'runs':rs,'bold':bool(rs) and all(r['b'] for r in rs),
                       'num':numinfo(el),'img':img})
    elif tag=='tbl':
        rows=[]
        for tr in el.findall(f'{{{W}}}tr'):
            rows.append([' '.join(''.join(x.text or '' for x in pp.findall(f'{{{W}}}t')) for pp in tc.iter(f'{{{W}}}p')).strip()
                         for tc in tr.findall(f'{{{W}}}tc')])
        if rows: blocks.append({'k':'TBL','rows':rows})
json.dump(blocks, open(f'ch{n}_blocks.json','w'), ensure_ascii=False)
P=[x for x in blocks if x['k']=='P' and x['txt'].strip()]
print(f"blocs {len(blocks)} | paragraphes {len(P)} | tableaux {sum(1 for b in blocks if b['k']=='TBL')} "
      f"| gras {sum(1 for x in P if x['bold'])/max(1,len(P)):.0%} | puces numPr {sum(1 for x in P if x['num'] is not None)}")
