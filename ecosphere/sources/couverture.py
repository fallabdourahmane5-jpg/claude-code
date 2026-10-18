# -*- coding: utf-8 -*-
"""Mesure la couverture de chaque dossier par le contenu réel des cours."""
import json, re, unicodedata, collections
import notions_liste

C = json.load(open('corpus.json'))
A = json.load(open('corpus_atlas.json'))

def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s)

CH = {k: nz(v['texte']) for k, v in C['chapitres'].items()}
NOTIONS = {k: [(n['t'], n['d']) for n in v['notions']] for k, v in C['chapitres'].items()}
ORDRE = ['1','2','3','4','5','6','7','8','9','10','21','22','23','24']

def mots_cles(libelle):
    """Transforme un libellé de dossier en expressions à chercher."""
    l = libelle
    # « A et B » / « A : B » / « A, B » : on garde les segments porteurs
    l = re.sub(r'\s*:\s*', ' | ', l)
    parts = re.split(r'\s+\|\s+', l)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # « X et Y » -> deux expressions quand les deux côtés sont courts
        m = re.match(r'^(.{3,40}?) et (.{3,60})$', p)
        if m:
            out += [m.group(1), m.group(2)]
        else:
            out.append(p)
    # réduction : « croissance extensive et croissance intensive » etc.
    fin = []
    for o in out:
        o = o.strip(" .")
        o = re.sub(r'^(les|le|la|l\'|des|du|de la|de l\')\s+', '', o, flags=re.I)
        if len(o) >= 4:
            fin.append(o)
    return fin or [libelle]

lignes = []
for e in notions_liste.ENSEMBLES:
    for d in e['dossiers']:
        cles = [nz(c) for c in mots_cles(d)]
        chaps = []
        for k in ORDRE:
            t = CH[k]
            n = sum(t.count(c) for c in cles)
            if n:
                chaps.append((k, n))
        # notions de fiche exactes
        fiches = []
        for k in ORDRE:
            for (t, _) in NOTIONS[k]:
                if any(c in nz(t) or nz(t) in c for c in cles):
                    fiches.append((k, t))
        # idées de l'Atlas
        idees = []
        for c24 in A['atlas']:
            for x in c24['e']:
                blob = nz(x['ti'] + ' ' + ' '.join(x['no']))
                if any(c in blob for c in cles):
                    idees.append((c24['k'], x['n'], x['ti']))
        total = sum(n for _, n in chaps)
        lignes.append({'ens': e['num'], 'dossier': d, 'cles': cles,
                       'chapitres': chaps, 'total': total,
                       'fiches': fiches[:8], 'idees': idees[:8]})

json.dump(lignes, open('couverture.json', 'w'), ensure_ascii=False)

print('dossiers       :', len(lignes))
print('questions      :', notions_liste.TOTAL_QUESTIONS)
seuils = collections.Counter()
for x in lignes:
    t = x['total']
    seuils['0 occurrence' if t == 0 else
           '1-4' if t < 5 else
           '5-19' if t < 20 else
           '20-99' if t < 100 else '100+'] += 1
for k in ['0 occurrence', '1-4', '5-19', '20-99', '100+']:
    print('%-14s : %3d' % (k, seuils[k]))
print()
print('--- dossiers sans aucune occurrence dans les cours :')
for x in lignes:
    if x['total'] == 0:
        print('  ens %-2d | %s' % (x['ens'], x['dossier']))
