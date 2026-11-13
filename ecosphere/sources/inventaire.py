# -*- coding: utf-8 -*-
"""Inventaire chapitre par chapitre de tout ce que les cours contiennent.

Pour chacun des quatorze chapitres, on relève :
  plan        la hiérarchie réelle des intitulés (I. / A. / 1- …)
  definitions les phrases qui définissent une expression
  idees       les encadrés « Idée », « Idée clé », « À retenir »
  mecanismes  les enchaînements écrits avec des flèches
  auteurs     les mentions d'auteurs et ce que le cours leur attribue
  formules    les égalités et les expressions de calcul
  chiffres    les valeurs numériques et leur contexte
  faits       les mentions datées

Chaque élément garde sa position exacte dans le texte du chapitre : c'est
cette position qui permettra plus tard d'ouvrir le bon passage.
"""
import json
import re
import unicodedata

import socle

ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
         '21', '22', '23', '24']

# ------------------------------------------------------------------ outillage


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'"))


# un intitulé : « I. », « II. », « A. », « AB. », « 1- », « 1. »
RE_TITRE = re.compile(
    r'(?m)^[ \t]*((?:[IVXLC]{1,6})\.|(?:[A-Z]{1,2})\.|\d{1,2}[-.)])[ \t]*(\S.{2,140})$')

# une définition : « X désigne … », « X correspond à … », « Un X est … »
VERBES = (r"designe|desigent|correspond a|correspondent a|est defini|sont definis|"
          r"se definit|se definissent|consiste a|consistent a|renvoie a|renvoient a|"
          r"s'entend comme|appelle|nomme|mesure|exprime|traduit")
RE_DEF = re.compile(
    r'(?m)^[^\n]{0,400}?(?:'
    r'(?P<t1>[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÆŒ][^\n.;:!?]{2,70})\s+(?:' + VERBES + r')\b'
    r'|(?:Un|Une|Le|La|L[’\']|Les)\s+(?P<t2>[^\n.;:!?]{2,70})\s+(?:est|sont)\s+'
    r')[^\n]{10,500}', re.I)

RE_FLECHE = re.compile(r'(?m)^[^\n]*(?:→|->|⇒)[^\n]*$')
RE_IDEE = re.compile(r'(?m)^[ \t]*(Idée clé|Idée|À retenir|A retenir|Définition|'
                     r'Remarque|Attention|Conclusion)\b[ \t:]*(.*)$')
RE_FORMULE = re.compile(
    r'(?m)^[^\n]{0,120}?[A-Za-zÀ-ÿ\)\]][ \t]*=[ \t]*[^\n=]{3,150}$')
RE_CHIFFRE = re.compile(
    r'(?:\d[\d   .,]*\s?(?:%|‰|milliards?|millions?|milliers?|'
    r'points? de (?:PIB|pourcentage)|€|\$|dollars?|euros?|ans?|habitants?|'
    r'fois|heures?)|\b(?:1[6-9]\d\d|20[0-4]\d)\b)')
RE_ANNEE = re.compile(r'\b(1[5-9]\d\d|20[0-5]\d)\b')
RE_REF = re.compile(r'(?m)^[ \t]*(?:Référence|Document|Lecture|Source)\b[ \t:]*(.*)$')

VIDE = set("""de du des la le les un une et ou au aux en dans par pour sur ce
cette ces son sa ses leur leurs il elle on qui que est sont etre avoir plus
moins tres tout tous toute toutes non pas ne comme donc alors meme autre
autres entre vers chez sans sous apres avant lorsque puisque parce ainsi
aussi mais car si selon peut peuvent doit doivent fait faire cours notion
document lecture graphique schema exemple idee cle retenir remarque""".split())


def phrase_autour(t, i, avant=160, apres=320):
    """La phrase complète qui entoure la position i."""
    a = max(0, i - avant)
    b = min(len(t), i + apres)
    g = t.rfind('\n', a, i)
    if g < 0:
        g = a
    d = t.find('\n', i, b)
    if d < 0:
        d = b
    return t[g:d].strip()


# ------------------------------------------------------------------ extraction


def plan(t):
    """Hiérarchie des intitulés, avec la position de chacun."""
    out = []
    for m in RE_TITRE.finditer(t):
        marque, titre = m.group(1), m.group(2).strip()
        if len(nz(titre).split()) < 2 and not titre.endswith('?'):
            continue
        if re.fullmatch(r'[IVXLC]{1,6}\.', marque):
            niv = 1
        elif re.fullmatch(r'[A-Z]{1,2}\.', marque):
            niv = 2
        else:
            niv = 3
        out.append({'niv': niv, 'marque': marque, 't': titre, 'i': m.start()})
    return out


def rattacher(plan_ch, i):
    """Chemin d'intitulés (niveau 1 puis 2) au-dessus de la position i."""
    h1 = h2 = None
    for x in plan_ch:
        if x['i'] > i:
            break
        if x['niv'] == 1:
            h1, h2 = x, None
        elif x['niv'] == 2:
            h2 = x
    return [y['t'] for y in (h1, h2) if y]


def definitions(t):
    out = []
    for m in RE_DEF.finditer(t):
        terme = (m.group('t1') or m.group('t2') or '').strip(' ,;:·—-’\'')
        if not terme:
            continue
        mots = [w for w in nz(terme).split() if w not in VIDE]
        if not mots or len(nz(terme)) < 4 or len(nz(terme)) > 70:
            continue
        txt = ' '.join(m.group(0).split())
        if len(txt) < 60:
            continue
        out.append({'t': terme, 'txt': txt, 'i': m.start()})
    return out


def idees(t):
    out = []
    for m in RE_IDEE.finditer(t):
        suite = m.group(2).strip()
        if len(suite) < 40:
            j = m.end()
            suite = ' '.join(t[j:j + 600].split('\n')[0:3]).strip()
        if len(suite) < 40:
            continue
        out.append({'k': m.group(1), 'txt': ' '.join(suite.split())[:700],
                    'i': m.start()})
    return out


def mecanismes(t):
    out = []
    for m in RE_FLECHE.finditer(t):
        txt = ' '.join(m.group(0).split())
        if txt.count('→') + txt.count('->') + txt.count('⇒') < 1:
            continue
        if len(txt) < 18 or len(txt) > 420:
            continue
        out.append({'txt': txt, 'i': m.start()})
    return out


def formules(t):
    out = []
    for m in RE_FORMULE.finditer(t):
        txt = ' '.join(m.group(0).split())
        if len(txt) < 10 or len(txt) > 180:
            continue
        if not re.search(r'[A-Za-zÀ-ÿ]', txt.split('=')[0]):
            continue
        out.append({'txt': txt, 'i': m.start()})
    return out


def chiffres(t):
    out = []
    for m in RE_CHIFFRE.finditer(t):
        ph = phrase_autour(t, m.start())
        if len(ph) < 30:
            continue
        out.append({'v': m.group(0), 'txt': ' '.join(ph.split())[:420],
                    'i': m.start()})
    return out


def faits(t):
    out = []
    for m in RE_ANNEE.finditer(t):
        ph = phrase_autour(t, m.start(), 200, 360)
        if len(ph) < 45:
            continue
        out.append({'an': int(m.group(1)), 'txt': ' '.join(ph.split())[:460],
                    'i': m.start()})
    return out


def auteurs_cites(t, noms):
    """Mentions des auteurs de la base, avec le passage qui les porte."""
    out = []
    for nom in noms:
        fam = nom.split()[-1]
        if len(fam) < 4:
            continue
        for m in re.finditer(r'\b' + re.escape(fam) + r'\b', t):
            ph = phrase_autour(t, m.start(), 150, 420)
            if len(ph) < 40:
                continue
            out.append({'n': nom, 'txt': ' '.join(ph.split())[:520],
                        'i': m.start()})
    return out


# ------------------------------------------------------------------ programme

if __name__ == '__main__':
    C = json.load(open('corpus.json'))
    NOMS = sorted({a['name'] for a in C['auteurs']})
    inv = {}
    for k in ORDRE:
        t = socle.TXT[k]
        p = plan(t)
        inv[k] = {
            'titre': C['chapitres'][k]['title'],
            'signes': len(t),
            'plan': p,
            'notions_fiche': C['chapitres'][k]['notions'],
            'definitions': definitions(t),
            'idees': idees(t),
            'mecanismes': mecanismes(t),
            'formules': formules(t),
            'chiffres': chiffres(t),
            'faits': faits(t),
            'auteurs': auteurs_cites(t, NOMS),
        }
    json.dump(inv, open('inventaire.json', 'w'), ensure_ascii=False)

    cols = ['plan', 'notions_fiche', 'definitions', 'idees', 'mecanismes',
            'formules', 'chiffres', 'faits', 'auteurs']
    print('%-4s %-46s %8s %s' % ('ch', 'titre', 'signes',
                                 ' '.join('%7s' % c[:7] for c in cols)))
    tot = {c: 0 for c in cols}
    for k in ORDRE:
        x = inv[k]
        print('%-4s %-46s %8d %s'
              % (k, x['titre'][:46], x['signes'],
                 ' '.join('%7d' % len(x[c]) for c in cols)))
        for c in cols:
            tot[c] += len(x[c])
    print('%-4s %-46s %8d %s'
          % ('', 'TOTAL', sum(inv[k]['signes'] for k in ORDRE),
             ' '.join('%7d' % tot[c] for c in cols)))
