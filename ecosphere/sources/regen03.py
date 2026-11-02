# -*- coding: utf-8 -*-
"""Régénère doss03a.py / doss03b.py à partir du payload embarqué dans app_v215."""
import io, json, textwrap

KEYS = ['n3-developpement', 'n3-sous-developpement', 'n3-humain',
        'n3-capabilites', 'n3-ipm', 'n3-emergence', 'n3-pma',
        'n3-cercle-vicieux', 'n3-trappe-pauvrete', 'n3-trappe-intermediaire']

P = json.load(open('recup_autour.json'))
D = {x['cle']: x for x in P['dossiers']}


def q(s, ind):
    """Chaîne découpée en littéraux concaténés, indentés de `ind`."""
    lines = textwrap.wrap(s, width=74 - ind, break_long_words=False, break_on_hyphens=False)
    pad = ' ' * ind
    out = []
    for i, L in enumerate(lines):
        t = L.replace('\\', '\\\\').replace('"', '\\"')
        out.append(('' if i == 0 else pad) + '"' + t + (' "' if i < len(lines) - 1 else '"'))
    return ('\n').join(out)


def emit(cle):
    x = D[cle]
    b = []
    b.append("d('%s', %d, %s,\n  %s,\n  %s,\n  %s"
             % (x['cle'], x['ens'], q(x['titre'], 2), q(x['court'], 2),
                q(x['defi'], 2), q(x['expl'], 2)))
    b.append('  [' + ',\n   '.join(
        '(%s,\n    %s)' % (q(m['t'], 5), q(m['e'], 4)) for m in x['mec']) + ']')
    b.append('  [' + ',\n   '.join(
        "{'a': %s,\n    'cond': %s,\n    'lim': %s}"
        % (q(a['a'], 9), q(a['cond'], 12), q(a['lim'], 11)) for a in x['args']) + ']')
    b.append('  [' + ',\n   '.join(
        "{'t': %s,\n    'qui': %s,\n    'rep': %s}"
        % (q(c['t'], 9), q(c.get('qui', ''), 11), q(c['rep'], 11)) for c in x['crit']) + ']')
    b.append('  [' + ',\n   '.join(
        "{'n': %s,\n    'i': %s,\n    'p': %s}"
        % (q(a['n'], 9), q(a['i'], 9), q(a['p'], 9)) for a in x['aut']) + ']')
    b.append('  [' + ',\n   '.join(
        "{'f': %s,\n    'p': %s}" % (q(f['f'], 9), q(f['p'], 9)) for f in x['faits']) + ']')
    b.append('  [' + ',\n   '.join(
        "{'q': %s,\n    'f': %s,\n    'r': %s,\n    'ex': %s}"
        % (q(s['q'], 9), q(s['f'], 9), q(s['r'], 9), q(s['ex'], 10))
        for s in x['diss']) + ']')
    if x.get('voisins'):
        b.append('  voisins=%r' % (x['voisins'],))
    if x.get('comp'):
        c = x['comp']
        lg = ',\n              '.join('(%r, %r, %r)' % tuple(l) for l in c['lignes'])
        b.append("  comp={'titre': %r,\n        'a': %r, 'b': %r,\n        'lignes': [%s]}"
                 % (c['titre'], c['a'], c['b'], lg))
    return ',\n'.join(b) + ')\n'


for nom, ks, num in (('doss03a.py', KEYS[:5], '1/4'), ('doss03b.py', KEYS[5:], '2/4')):
    out = ['# -*- coding: utf-8 -*-',
           '"""Ensemble 3 — Le développement et les stratégies de rattrapage (%s)."""' % num,
           '', 'from doss_base import d', '']
    for k in ks:
        out.append('')
        out.append(emit(k))
    io.open(nom, 'w', encoding='utf-8').write('\n'.join(out))
    print('écrit', nom)
