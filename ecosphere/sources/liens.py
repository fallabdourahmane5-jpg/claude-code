# -*- coding: utf-8 -*-
"""Calcule, pour chaque dossier, les liens vers les contenus réellement présents.

Rien n'est inventé : un lien n'existe que si l'expression du dossier apparaît
dans le chapitre, la fiche, l'idée de l'Atlas ou le sujet visé.
"""
import json, re, unicodedata
import notions_liste, alias24

C = json.load(open('corpus.json'))
A = json.load(open('corpus_atlas.json'))

def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'"))

ORDRE = ['1','2','3','4','5','6','7','8','9','10','21','22','23','24']
CH = {k: nz(C['chapitres'][k]['texte']) for k in ORDRE}
TITRES = {k: C['chapitres'][k]['title'] for k in ORDRE}
NOTIONS = {k: [n['t'] for n in C['chapitres'][k]['notions']] for k in ORDRE}
SUJ = C['sujets']
AUT = C['auteurs']

LIB = {'21': '2ᵉ année — ch.1', '22': '2ᵉ année — ch.2',
       '23': '2ᵉ année — ch.3', '24': '2ᵉ année — ch.4'}
def lib(k): return LIB.get(str(k), 'Chapitre ' + str(k))

def expressions(libelle):
    if libelle in alias24.ALIAS:
        return [nz(x) for x in alias24.ALIAS[libelle]]
    l = re.sub(r'\s*:\s*', ' | ', libelle)
    out = []
    for p in re.split(r'\s+\|\s+|,\s*', l):
        p = p.strip(' .')
        if not p:
            continue
        m = re.match(r'^(.{4,45}?) et (.{4,60})$', p)
        if m:
            out += [m.group(1), m.group(2)]
        else:
            out.append(p)
    fin = []
    for o in out:
        o = re.sub(r"^(les|le|la|l'|des|du|de la|de l')\s+", '', o.strip(' .'), flags=re.I)
        if len(o) >= 5:
            fin.append(nz(o))
    return fin or [nz(libelle)]


def liens_de(libelle, ex=None):
    ex = ex or expressions(libelle)
    chap = sorted(([k, sum(CH[k].count(x) for x in ex)] for k in ORDRE),
                  key=lambda t: -t[1])
    chap = [{'k': k, 'n': n, 'lib': lib(k), 'titre': TITRES[k]}
            for k, n in chap if n]
    fiches = [{'k': k, 't': t} for k in ORDRE for t in NOTIONS[k]
              if any(x in nz(t) for x in ex)][:14]
    idees = [{'k': c['k'], 'n': x['n'], 'ti': x['ti']}
             for c in A['atlas'] for x in c['e']
             if any(x2 in nz(x['ti'] + ' ' + ' '.join(x['no'])) for x2 in ex)][:14]
    sujets = [{'id': s['id'], 'ch': s['ch'], 't': s['title']} for s in SUJ
              if any(x in nz(s['title']) for x in ex)][:14]
    auteurs = [a['name'] for a in AUT
               if any(x in nz((a.get('idea') or '') + ' ' + (a.get('detail') or ''))
                      for x in ex)][:20]
    return {'ch': chap, 'fi': fiches, 'at': idees, 'su': sujets, 'au': auteurs}


if __name__ == '__main__':
    for e in notions_liste.ENSEMBLES:
        if e['num'] != 28:
            continue
        for d in e['dossiers']:
            L = liens_de(d)
            print('— %s' % d)
            print('   chapitres :', ', '.join('%s(%d)' % (x['lib'], x['n']) for x in L['ch'][:6]))
            print('   fiches %d · atlas %d · sujets %d · auteurs %s'
                  % (len(L['fi']), len(L['at']), len(L['su']), L['au'][:6]))
