# -*- coding: utf-8 -*-
"""Extrait les paragraphes du document du chapitre 4 (2e annee).

Les sauts de ligne internes (<w:br>) separent de vrais paragraphes logiques :
ils sont donc traites comme des fins de paragraphe, comme dans le document du
chapitre 3.
"""
import io, json, zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
Z = zipfile.ZipFile('ch24_src/2b925508-chap_4_deuxie_me_anne_e.docx')
root = ET.fromstring(Z.read('word/document.xml'))

out = []
for para in root.iter(W + 'p'):
    style = ''
    ppr = para.find(W + 'pPr')
    if ppr is not None:
        ps = ppr.find(W + 'pStyle')
        if ps is not None:
            style = ps.get(W + 'val') or ''
    img = para.find('.//' + W + 'drawing') is not None
    morceaux = ['']
    for el in para.iter():
        tag = el.tag
        if tag == W + 't':
            morceaux[-1] += (el.text or '')
        elif tag in (W + 'br', W + 'cr'):
            morceaux.append('')
    for k, m in enumerate(morceaux):
        t = m.strip()
        if t:
            out.append({'style': style, 'txt': t, 'img': img and k == 0})
            img = False
    if img:
        out.append({'style': style, 'txt': '', 'img': True})

io.open('ch24_paras.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, separators=(',', ':')))
print('paragraphes :', len(out), '· images :', sum(1 for x in out if x['img']))
