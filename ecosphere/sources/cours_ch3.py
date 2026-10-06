# -*- coding: utf-8 -*-
"""Conversion du document du chapitre 3 (2e annee) en cours HTML.

Le document transmis ne porte aucun style de titre : la hierarchie est donc
reconstruite a partir du contenu, comme pour le chapitre 2 de deuxieme annee.
"""
import json, re, html, os

ICI = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(ICI, 'ch3_paras.json'), encoding='utf-8'))

# --- niveaux h2 : les grandes parties du document -------------------------
H2 = {
    1:    "I. Introduction générale : comment l’analyse du commerce international a-t-elle évolué ?",
    322:  "II. Les théories traditionnelles de l’échange international",
    2224: "III. Les théories contemporaines de l’échange international",
    3106: "IV. Les enjeux du débat libre-échange / protectionnisme",
}

LABELS = {
    'idée', 'idée générale', 'idée clé', 'idée importante', 'mécanisme',
    'mécanisme complet', 'exemple', 'exemples', 'rappel', 'conclusion',
    'problématique', 'cl', 'le principe', 'lecture', 'définition',
    'théorème h-o', 'théorème stolper-samuelson', 'efficacité ≠ efficience',
    'exemple très simple', 'avant', 'désormais', 'pourquoi ?',
}

# fragments de raisonnement que la detection prendrait pour des titres
DENY = {
    2234, 939, 1816, 3777, 3781, 3937, 4071, 4807, 4847, 517, 518, 519, 520,
    523, 1912, 2605, 1534, 1536, 1730, 1731, 1732, 2681, 2683, 3226, 3227,
    1809, 1810, 1817, 2098, 2099, 2862, 3430, 4223, 4253, 4902, 5195, 5200,
    3501, 3503, 4795,
}

# tableau Ricardo : coûts de production en hommes-années
TABLEAU = {517: ('Coût de production en hommes-années',
                 ['', 'Portugal', 'Angleterre'],
                 [['Drap', '90', '100'], ['Vin', '80', '120']],
                 525)}

RE_FORMULE = re.compile(r'[↑↓→]|^[\d\s,.%]+$|^\(?K/L\)?|^[\d,]+\s*<|^r/w$|=\s*[-−]?\d|\s\+\s')
RE_REF = re.compile(r'(?:,|»|\))\s*(?:1[6-9]|20)\d\d\s*\.?$')
RE_EMOJI = re.compile(r'^[\U0001F300-\U0001FAFF←-⇿⬀-⯿📌🖼⬇✏️]')
RE_IMG = re.compile(r'^(📌\s*IMAGE|🖼️|🖼)')


def est_formule(t):
    return bool(RE_FORMULE.search(t))


def mots(t):
    return len([w for w in re.split(r'\s+', t) if w])


def classe(i, t):
    if i in H2:
        return 'h2'
    b = t.lower().strip().rstrip('.')
    if b in LABELS:
        return 'h4'
    if i in DENY:
        return None
    if t.startswith('👉') or RE_EMOJI.match(t):
        return None
    if re.search(r'[.;:?!»,]$', t):
        return None
    if RE_REF.search(t):
        return None
    if est_formule(t):
        return None
    if not re.match(r'^[A-ZÀÂÉÈÊÎÔÛÇ«\d]', t):
        return None
    if mots(t) < 3 or len(t) < 18:
        return None
    if re.match(r'^\d\s*-\s*', t):
        return 'h4'
    if re.match(r'^(Premi[eè]re?|Deuxi[eè]me|Troisi[eè]me|Quatri[eè]me|Cinqui[eè]me|'
                r'Premier|Second|Un premier|Une premi[eè]re|Cas \d|Exemple|Section \d+|'
                r'Définition|Théorème)\b', t):
        return 'h4'
    return 'h3'


ROM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lettre(n):
    if n < 26:
        return ROM[n]
    return ROM[n // 26 - 1] + ROM[n % 26]


def esc(s):
    return html.escape(s, quote=False)


def construire():
    out = ['<div class="nb ch23-premium-course">']
    out.append('  <h2>Deuxième année, chapitre 3 — L’analyse économique du commerce international</h2>')
    out.append('  <p>Comment l’analyse économique du commerce international a-t-elle évolué, '
               'depuis des théories centrées sur les gains à l’échange jusqu’aux analyses '
               'contemporaines mettant davantage en évidence les coûts sociaux, industriels '
               'et distributifs de la mondialisation ?</p>')
    tampon = []
    nlettre = 0
    saut = -1

    def vider():
        if tampon:
            out.append('  <ul>' + ''.join('<li>' + esc(x) + '</li>' for x in tampon) + '</ul>')
            del tampon[:]

    for i, p in enumerate(P):
        if i <= saut:
            continue
        t = p['txt'].strip()
        if i == 0:
            continue
        if i in TABLEAU:
            titre, entetes, corps, fin = TABLEAU[i]
            vider()
            saut = fin
            th = ''.join('<th>' + esc(x) + '</th>' for x in entetes)
            tr = ''.join('<tr>' + ''.join('<td>' + esc(c) + '</td>' for c in l) + '</tr>'
                         for l in corps)
            out.append('  <div class="table-wrap"><div class="dt">' + esc(titre) + '</div>'
                       '<table class="dt"><tr>' + th + '</tr>' + tr + '</table></div>')
            continue
        if not t:
            if p.get('img'):
                vider()
                out.append('  <div class="db"><div class="dt">Document</div>'
                           '<div class="dd">Graphique ou schéma du cours.</div></div>')
            continue
        c = classe(i, t)
        if c == 'h2':
            vider()
            nlettre = 0
            out.append('  <h2>' + esc(H2[i]) + '</h2>')
            continue
        if c == 'h3':
            vider()
            out.append('  <h3>' + lettre(nlettre) + '. ' + esc(t) + '</h3>')
            nlettre += 1
            continue
        if c == 'h4':
            vider()
            lib = t
            if lib.strip().lower().rstrip('.') == 'cl':
                lib = 'Idée clé'
            out.append('  <h4>' + esc(lib) + '</h4>')
            continue
        # --- corps ---
        if RE_IMG.match(t):
            vider()
            lib = re.sub(r'^(📌\s*IMAGE\s*[—-]?\s*|🖼️\s*|🖼\s*)', '', t).strip() or 'Document du cours'
            out.append('  <div class="db"><div class="dt">Document</div><div class="dd">'
                       + esc(lib) + '</div></div>')
            continue
        if t.startswith('Lecture :') or t.startswith('Lecture:'):
            vider()
            out.append('  <div class="db"><div class="dt">Lecture</div><div class="dd">'
                       + esc(t.split(':', 1)[1].strip()) + '</div></div>')
            continue
        if RE_REF.search(t) and mots(t) >= 3 and not t.startswith('👉') and len(t) < 240:
            vider()
            out.append('  <div class="db"><div class="dt">Référence</div><div class="dd">'
                       + esc(t) + '</div></div>')
            continue
        if t.startswith('👉'):
            vider()
            out.append('  <p>' + esc(t) + '</p>')
            continue
        if est_formule(t) and len(t) < 400:
            vider()
            out.append('  <div class="formula">' + esc(t) + '</div>')
            continue
        if t.endswith(';') or (len(t) < 110 and not re.search(r'[.?!:]$', t) and mots(t) >= 2):
            tampon.append(t)
            continue
        vider()
        out.append('  <p>' + esc(t) + '</p>')
    vider()
    out.append('</div>')
    return '\n'.join(out)


if __name__ == '__main__':
    h = construire()
    open(os.path.join(ICI, 'cours_ch3.html'), 'w', encoding='utf-8').write(h)
    print('longueur', len(h))
    hs = re.findall(r'<(h[2-4])>(.*?)</\1>', h)
    print('titres', len(hs))
    for lvl, txt in hs:
        print(('' if lvl == 'h2' else '    ' if lvl == 'h3' else '        ') + lvl + ' ' + txt[:95])
