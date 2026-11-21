# -*- coding: utf-8 -*-
"""Feuille de travail d'un chapitre : tout ce qu'il faut pour reprendre ses
questions — le découpage en sous-parties, le plan du cours, et chaque question
existante avec son rattachement, son corrigé actuel et ce qui lui manque.

   python3 feuille.py 7            questions et sous-parties du chapitre 7
   python3 feuille.py 7 plan       plan détaillé du cours
   python3 feuille.py 7 texte 120 200   texte des blocs 120 à 200
"""

import json
import sys

import qz_base as Z

k = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'quest'

B = json.load(open('blocs_bruts.json', encoding='utf-8'))[k]
SP = json.load(open('sousparties.json', encoding='utf-8'))[k]
AU = json.load(open('audit_quiz.json', encoding='utf-8'))[k]
QA = json.load(open('quiz_actuel.json', encoding='utf-8'))['bank'][k]
POS = {d['id']: d for d in AU['detail']}

if mode == 'texte':
    a, b = int(sys.argv[3]), int(sys.argv[4])
    for i in range(a, min(b, len(B))):
        x = B[i]
        t = ' '.join(x['x'].split())
        if not t:
            continue
        print('%5d %-4s %s' % (i, x['g'], t[:400]))
    sys.exit()

if mode == 'plan':
    for i, x in enumerate(B):
        if x['g'] in ('h2', 'h3'):
            print('%5d %-3s %s%s' % (i, x['g'], '  ' if x['g'] == 'h3' else '',
                                     ' '.join(x['x'].split())[:120]))
    sys.exit()

print('=== CHAPITRE %s — %d blocs, %d questions' % (k, len(B), len(QA)))
print('\n--- SOUS-PARTIES')
for s in SP:
    n = len(AU['parsp'].get(s['cle']) or [])
    print('%-9s %4d-%4d  %2d question(s)  %s'
          % (s['cle'], s['a'], s['b'], n, s['lib'][:88]))
if AU['vides']:
    print('SANS QUESTION : %s' % ', '.join(AU['vides']))

print('\n--- QUESTIONS, par sous-partie')
parsp = {}
for q in QA:
    parsp.setdefault(POS[q['id']]['sp'], []).append(q)
for s in SP:
    liste = parsp.get(s['cle']) or []
    print('\n### %s — %s (%d)' % (s['cle'], s['lib'][:70], len(liste)))
    for q in liste:
        d = POS[q['id']]
        t = q.get('type')
        print('%-14s %-16s b%-5d niv=%s' % (q['id'], t, d['b'],
                                            Z.niveau(q.get('q'), t)))
        print('   Q  %s' % ' '.join(str(q.get('q')).split())[:300])
        for i, o in enumerate(q.get('opts') or []):
            m = '*' if i == q.get('ans') else ' '
            print('   %s%s %s' % (m, 'ABCDEF'[i], ' '.join(str(o).split())[:190]))
        if t in ('vf', 'vrai/faux'):
            vrai = bool(q.get('ans')) if t == 'vf' else (q.get('ans') == 0)
            print('    réponse : %s' % ('VRAI' if vrai else 'FAUX'))
        e = ' '.join(str(q.get('exp') or '').split())
        print('   EXP(%d) %s' % (len(e), e[:420]))
