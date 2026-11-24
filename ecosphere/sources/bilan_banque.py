# -*- coding: utf-8 -*-
"""Bilan de la banque de questions, chapitre par chapitre."""
import json
import collections
import re
import unicodedata

B = json.load(open('banque.json', encoding='utf-8'))
Q, SP = B['q'], B['sp']
ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
         '21', '22', '23', '24', '25', '26']
LIBCH = {k: ('Chapitre ' + k if int(k) < 20 else '2e annee ch.' + str(int(k) - 20))
         for k in ORDRE}
NIV = ['connaitre', 'comprendre', 'appliquer', 'raisonner']
TYP = ['qcm', 'qcmm', 'vf', 'assoc', 'ordre', 'courte']


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '').lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


lignes = []
doublons = 0
vus = {}
for q in Q:
    c = nz(q['q'])[:90]
    if c in vus:
        doublons += 1
    vus[c] = 1

total_sp = 0
print('%-16s %6s %7s  %-42s  %s' % ('chapitre', 'quest', 's-parties', 'niveaux', 'formats'))
for k in ORDRE:
    qs = [q for q in Q if str(q['ch']) == k]
    sps = SP[k]
    parsp = collections.Counter(q['sp'] for q in qs)
    n = collections.Counter(q['niv'] for q in qs)
    t = collections.Counter(q['type'] for q in qs)
    couvertes = sum(1 for s in sps if parsp.get(s['cle']))
    total_sp += len(sps)
    mini = min((parsp.get(s['cle'], 0) for s in sps), default=0)
    maxi = max((parsp.get(s['cle'], 0) for s in sps), default=0)
    print('%-16s %6d %4d/%-4d  %-42s  %s'
          % (LIBCH[k], len(qs), couvertes, len(sps),
             ' '.join('%s:%d' % (x[:4], n.get(x, 0)) for x in NIV),
             ' '.join('%s:%d' % (x, t.get(x, 0)) for x in TYP)))
    creuses = [s['lib'] for s in sps if parsp.get(s['cle'], 0) < 4]
    lignes.append({
        'ch': k, 'lib': LIBCH[k], 'n': len(qs), 'sp': len(sps),
        'couvertes': couvertes, 'min': mini, 'max': maxi,
        'niv': {x: n.get(x, 0) for x in NIV},
        'typ': {x: t.get(x, 0) for x in TYP},
        'creuses': creuses,
        'parsp': [(s['lib'], parsp.get(s['cle'], 0)) for s in sps],
    })

print('\ntotal : %d questions, %d sous-parties, %d doublons d enonce'
      % (len(Q), total_sp, doublons))
print('questions avec « pourquoi les autres sont fausses » : %d'
      % sum(1 for q in Q if q.get('why')))
print('questions avec rubrique dissertation : %d' % sum(1 for q in Q if q.get('diss')))
print('questions avec lien vers le cours : %d' % sum(1 for q in Q if q.get('b') is not None))
print('longueur moyenne des corrections : %d signes'
      % (sum(len(q.get('exp') or '') for q in Q) / len(Q)))
json.dump(lignes, open('bilan_banque.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
