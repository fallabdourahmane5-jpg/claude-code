# -*- coding: utf-8 -*-
"""Assemble la banque de questions du quiz.

Trois sources :
  - les questions déjà présentes dans l'application, normalisées et rattachées
    à leur sous-partie et au bloc de cours qui les justifie ;
  - les modules de chapitre `qz01.py` … `qz26.py`, qui portent les libellés des
    sous-parties, les corrigés réécrits et les questions nouvelles ;
  - l'audit, qui fournit le rattachement automatique.

Le montage contrôle chaque question et dresse la liste de ce qui reste à
reprendre, chapitre par chapitre.
"""

import glob
import importlib
import json
import re
import sys
from collections import Counter, defaultdict

import qz_base as Z

# « Bonne réponse : B) … » : l'ancienne banque répétait la lettre et le texte de
# la proposition en tête du corrigé, ce que la nouvelle présentation affiche
# déjà. On retire cette amorce pour ne garder que l'explication.
AMORCE = re.compile(r'^\s*Bonne r[ée]ponse\s*:?\s*[A-F]?\s*[\).:–-]*\s*')


def nettoyer(exp, opts, ans):
    t = AMORCE.sub('', str(exp or '')).strip()
    if opts and isinstance(ans, int) and 0 <= ans < len(opts):
        bonne = str(opts[ans]).strip().rstrip('.')
        if t[:len(bonne)].strip().rstrip('.').lower() == bonne.lower():
            t = t[len(bonne):].lstrip(' .–—:')
    return t.strip()

NORM_TYPE = {'qcm': 'qcm', 'vf': 'vf', 'vrai/faux': 'vf', 'open': 'courte',
             'question ouverte': 'courte', 'qcmm': 'qcmm', 'assoc': 'assoc',
             'ordre': 'ordre', 'courte': 'courte'}


def charger_modules():
    """Modules de chapitre : SP (libellés), FIX (corrigés), NEW (questions),
    DROP (questions écartées)."""
    mods = {}
    for f in sorted(glob.glob('qz[0-9][0-9].py')):
        m = importlib.import_module(f[:-3])
        mods[str(int(f[2:4]))] = m
    return mods


def main():
    B = json.load(open('blocs_bruts.json', encoding='utf-8'))
    SP = json.load(open('sousparties.json', encoding='utf-8'))
    AU = json.load(open('audit_quiz.json', encoding='utf-8'))
    QA = json.load(open('quiz_actuel.json', encoding='utf-8'))['bank']
    MODS = charger_modules()

    # --- libellés des sous-parties, repris des modules quand ils existent
    sousp = {}
    for k, liste in SP.items():
        m = MODS.get(k)
        libs = getattr(m, 'SP', {}) if m else {}
        sousp[k] = []
        for s in liste:
            lib = libs.get(s['cle']) or s['lib']
            sousp[k].append({'cle': s['cle'], 'lib': lib, 'a': s['a'],
                             'b': s['b'], 'partie': s['partie']})

    banque = []
    restant = defaultdict(list)
    vus = {}
    for k in sorted(QA, key=lambda x: int(x)):
        m = MODS.get(k)
        FIX = getattr(m, 'FIX', {}) if m else {}
        DROP = set(getattr(m, 'DROP', []) if m else [])
        NEW = getattr(m, 'NEW', []) if m else []
        pos = {d['id']: d for d in AU[k]['detail']}
        titres = {s['cle']: s['lib'] for s in sousp[k]}

        for q0 in QA[k]:
            if q0['id'] in DROP:
                continue
            f = FIX.get(q0['id'], {})
            t = NORM_TYPE.get(f.get('type') or q0.get('type'), 'qcm')
            d = pos.get(q0['id'], {})
            q = {
                'id': f.get('id') or q0['id'],
                'ch': int(k),
                'sp': f.get('sp') or d.get('sp') or sousp[k][0]['cle'],
                'niv': f.get('niv') or Z.niveau(q0.get('q'), t),
                'type': t,
                'q': f.get('q') or q0.get('q'),
                'exp': f.get('exp') or nettoyer(q0.get('exp'),
                                               q0.get('opts'), q0.get('ans')),
                'b': f.get('b', d.get('b', -1)),
            }
            if t in ('qcm', 'qcmm'):
                q['opts'] = f.get('opts') or q0.get('opts') or []
                q['ans'] = f.get('ans', q0.get('ans'))
            elif t == 'vf':
                # deux conventions coexistaient : un booléen pour les chapitres
                # de première année (True = l'affirmation est vraie), un indice
                # dans ['Vrai', 'Faux'] pour les chapitres de deuxième année.
                if 'ans' in f:
                    q['ans'] = bool(f['ans'])
                elif q0.get('type') == 'vf':
                    q['ans'] = bool(q0.get('ans'))
                else:
                    q['ans'] = (q0.get('ans') == 0)
            elif t == 'courte':
                a = f.get('ans')
                if not a:
                    modele = q0.get('sample') or q0.get('exp') or ''
                    a = {'modele': modele, 'cles': []}
                q['ans'] = a
            else:
                q['ans'] = f.get('ans')
            for champ in ('why', 'diss', 'src', 'tags'):
                if f.get(champ):
                    q[champ] = f[champ]
            banque.append(q)

        for q in NEW:
            q = dict(q)
            q['ch'] = int(k)
            banque.append(q)

    # --- renvoi au cours : intitulé du passage
    for q in banque:
        k = str(q['ch'])
        b = q.get('b', -1)
        if b is not None and b >= 0 and b < len(B[k]):
            p = B[k][b].get('p') or []
            q['src'] = q.get('src') or (p[1] or p[0] or '')[:110]

    # --- contrôles
    for q in banque:
        n = Z.nz(q['q'])
        if n in vus:
            restant['doublon'].append('%s ≡ %s' % (q['id'], vus[n]))
        vus[n] = q['id']
        for e in Z.verifier(q):
            restant[str(q['ch'])].append('%s : %s' % (q['id'], e))

    parch = Counter(q['ch'] for q in banque)
    print('%-5s %6s %6s %-34s %s' % ('ch', 'quest', 'à faire', 'niveaux', 'types'))
    for k in sorted(parch, key=int):
        qs = [q for q in banque if q['ch'] == k]
        niv = Counter(q['niv'] for q in qs)
        typ = Counter(q['type'] for q in qs)
        print('%-5s %6d %6d  %-34s %s'
              % (k, len(qs), len(restant.get(str(k), [])),
                 ' '.join('%s:%d' % (n[:4], niv[n]) for n in Z.NIVEAUX),
                 ' '.join('%s:%d' % (t, typ[t]) for t in Z.TYPES if typ[t])))
    print('total : %d questions, %d points à reprendre, %d doublons'
          % (len(banque), sum(len(v) for k, v in restant.items() if k != 'doublon'),
             len(restant.get('doublon', []))))

    json.dump({'v': 223, 'sp': sousp, 'q': banque},
              open('banque.json', 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(restant, open('restant.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        for k in sorted(restant, key=lambda x: (x == 'doublon', x)):
            print('\n=== %s' % k)
            for ligne in restant[k][:40]:
                print('   ', ligne)


if __name__ == '__main__':
    main()
