"""Construit gestiosphere/gestiosphere.html à partir du modèle et des modules de contenu.

Usage : python3 build.py
Contrôles : identifiants uniques, chapitres « à mobiliser » existants, réponses de quiz valides,
écritures équilibrées (vérifiées à la création), aucune clé de sauvegarde Écosphère.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import compta  # noqa: E402

MODULES = [compta]
try:
    import micro  # noqa: E402
    MODULES.append(micro)
except ImportError:
    pass
try:
    import marketing  # noqa: E402
    MODULES.append(marketing)
except ImportError:
    pass
try:
    import macro  # noqa: E402
    MODULES.append(macro)
except ImportError:
    pass

ORDER = ['compta', 'micro', 'macro', 'marketing']
PLACEHOLDERS = {
    'micro': dict(id='micro', nom='Microéconomie', court='Micro', couleur='#7c6af7'),
    'macro': dict(id='macro', nom='Macroéconomie', court='Macro', couleur='#f7a26a',
                  attente='Les documents de macroéconomie n\'ont pas encore été transmis. La matière sera construite sur le même modèle dès leur réception.'),
    'marketing': dict(id='marketing', nom='Marketing', court='Marketing', couleur='#f76ab4'),
}


def validate(mats):
    errs = []
    ch_ids = {c['id'] for m in mats for c in m.get('chapitres', [])}
    seen = set()

    def uniq(kind, i):
        if i in seen:
            errs.append(f'identifiant en double : {kind} {i}')
        seen.add(i)
    for m in mats:
        for c in m.get('chapitres', []):
            uniq('chapitre', c['id'])
            for k in ('titre', 'cours', 'notions'):
                if not c.get(k):
                    errs.append(f'{c["id"]} : champ {k} vide')
            for q in c.get('quiz', []):
                if q.get('type', 'qcm') == 'qcm':
                    if not (isinstance(q.get('ans'), int) and 0 <= q['ans'] < len(q.get('opts', []))):
                        errs.append(f'{c["id"]} quiz : réponse invalide « {q["q"][:50]} »')
                    if len(set(q['opts'])) != len(q['opts']):
                        errs.append(f'{c["id"]} quiz : options en double « {q["q"][:50]} »')
                elif q['type'] == 'vf':
                    if not isinstance(q.get('ans'), bool):
                        errs.append(f'{c["id"]} vf : réponse non booléenne « {q["q"][:50]} »')
            for l in c.get('liens', []):
                if l['ch'] not in ch_ids:
                    errs.append(f'{c["id"]} : lien vers chapitre inconnu {l["ch"]}')
            if c.get('carte'):
                if not c['carte'].get('branches'):
                    errs.append(f'{c["id"]} : carte sans branches')
        for s in m.get('sujets', []):
            uniq('sujet', s['id'])
            if s['ch'] not in ch_ids:
                errs.append(f'sujet {s["id"]} : chapitre principal inconnu {s["ch"]}')
            for x in s.get('mobiliser', []):
                if x not in ch_ids:
                    errs.append(f'sujet {s["id"]} : chapitre à mobiliser inconnu {x}')
            for k in ('titre', 'enonce', 'corrige', 'type'):
                if not s.get(k):
                    errs.append(f'sujet {s["id"]} : champ {k} vide')
        for g in m.get('courbes', []):
            uniq('courbe', g['id'])
            if g['ch'] not in ch_ids:
                errs.append(f'courbe {g["id"]} : chapitre inconnu')
        for a in m.get('auteurs', []):
            for x in a.get('chapitres', []):
                if x not in ch_ids:
                    errs.append(f'auteur {a["nom"]} : chapitre inconnu {x}')
            if a.get('source') not in ('cours', 'compl'):
                errs.append(f'auteur {a["nom"]} : source manquante')
        for f in m.get('formules', []):
            if f.get('ch') and f['ch'] not in ch_ids:
                errs.append(f'formule {f["titre"]} : chapitre inconnu')
        for c in m.get('comptes', []):
            if c['ch'] not in ch_ids:
                errs.append(f'compte {c["num"]} : chapitre inconnu')
    return errs


def main():
    mats = {m.matiere()['id']: m.matiere() for m in MODULES}
    out = [mats[k] if k in mats else PLACEHOLDERS[k] for k in ORDER]
    import graph_exp
    miss = graph_exp.apply(out)
    errs = validate(out) + [f'courbe {g} : explication détaillée manquante' for g in miss]
    if errs:
        print('\n'.join('ERREUR : ' + e for e in errs))
        sys.exit(1)
    data = {'app': 'gestiosphere', 'niveau': 'Licence 3', 'matieres': out}
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    html = tpl.replace('/*__GS_DATA__*/null', js)
    if re.search(r"eco_(state|failed)", html):
        print('ERREUR : clé de sauvegarde Écosphère détectée')
        sys.exit(1)
    dst = os.path.join(os.path.dirname(HERE), 'gestiosphere.html')
    open(dst, 'w', encoding='utf-8').write(html)
    for m in out:
        chs = m.get('chapitres', [])
        print(f"{m['nom']:<28} chapitres={len(chs):>2}  notions={sum(len(c.get('notions', [])) for c in chs):>3}  quiz={sum(len(c.get('quiz', [])) for c in chs):>3}  "
              f"sujets={len(m.get('sujets', [])):>2}  auteurs={len(m.get('auteurs', [])):>2}  courbes={len(m.get('courbes', [])):>2}")
    print(f'→ {dst} ({len(html) / 1024:.0f} Ko)')


if __name__ == '__main__':
    main()
