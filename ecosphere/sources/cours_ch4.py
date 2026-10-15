# -*- coding: utf-8 -*-
"""Conversion du document du chapitre 4 (2e annee) en cours HTML.

Comme pour les chapitres 2 et 3 de deuxieme annee, le document transmis ne
porte aucun style de titre : la hierarchie est reconstruite a partir du
contenu. Les tableaux du document (matrice de Kindleberger, cycles de
negociation, droits de douane agricoles, decomposition de Findlay et
O'Rourke) sont reconstitues explicitement.
"""
import json, re, html, os

ICI = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(ICI, 'ch24_paras.json'), encoding='utf-8'))

# --- niveaux h2 : les grandes parties du document -------------------------
H2 = {
    1:    "Introduction — De la « mondialisation heureuse » à la « mondialisation dangereuse »",
    353:  "I. Les institutions d’après-guerre instaurent un multilatéralisme",
    1775: "II. La régionalisation des échanges : une autre voie de régulation",
    2518: "III. Quelle régulation de l’hypermondialisation ? Une gouvernance hybride",
}

LABELS = {
    'idée', 'idée générale', 'idée clé', 'idée importante', 'mécanisme',
    'mécanisme complet', 'exemple', 'exemples', 'rappel', 'conclusion',
    'problématique', 'cl', 'le principe', 'lecture', 'définition',
    'transition', 'pourquoi ?', 'attention', 'autre exemple',
    'exemple historique', 'exemple majeur', 'la portée de cette analyse',
    'premier cas', 'deuxième cas', 'troisième cas', 'quatrième cas',
    'cas 1', 'cas 2', 'idée essentielle',
    'problématique générale du chapitre', 'exemple simplifié',
}

# paragraphes a ignorer : repetition du document
SKIP = {85, 1384}

# titres de rang inferieur imposes (listes du document que la detection
# prendrait pour des sections)
H4 = {
    239: None, 243: None, 247: None,          # les trois contestations de l'OMC
    1448: None, 1450: None, 1452: None,       # les thèmes du cycle de Doha
    1454: None, 1456: None, 1458: None,
    1178: None,                               # question interne au cas senegalais
    1385: '2005 — fin du régime de quotas',
    3390: None,                               # question interne au retour sur Kindleberger
}

# titres de section que la ponctuation finale masquerait
H3 = {3274}

# lignes de comparaison a composer comme des formules
FORMULES = {2069, 2077, 3039, 3314, 3365}

# --- tableaux du document -------------------------------------------------
# cle = index du premier paragraphe remplace ; valeur = (titre, entetes,
# lignes, index du dernier paragraphe absorbe)
TABLEAUX = {
 488: ("Gains de la coopération internationale — joueur A : le leader, joueur B : le suiveur",
       ['Joueur A / Joueur B', 'B coopère', 'B fait défection'],
       [['A coopère', '(4 ; 4)', '(3 ; 5)'],
        ['A fait défection', '(3 ; 5)', '(2 ; 3)']], 496),
 1056: ("Droit de douane moyen par secteur en 2019",
        ['Secteur', 'Droit de douane moyen'],
        [['Agriculture mondiale', '15,9 %'],
         ['Industrie mondiale', '3 %']], 1059),
 1244: ("Les quatre premiers cycles de négociation du GATT",
        ['Année', 'Round', 'Participants'],
        [['1947', 'Genève', '23'], ['1949', 'Annecy', '33'],
         ['1951', 'Torquay', '34'], ['1955-1956', 'Genève', '34']], 1258),
 1576: ("Findlay et O’Rourke (2002) — décomposition de la croissance du commerce mondial, "
        "des années 1950 aux années 1980",
        ['Facteur explicatif', 'Part de la croissance'],
        [['Hausse des revenus', '67 %'],
         ['Réduction des droits de douane', '25 %'],
         ['Baisse des coûts de transport', '8 %']], 1582),
}

RE_FORMULE = re.compile(
    r'[↑↓→↔⬇≠≈]|^[\d\s,.%]+$|^\(?\d\s*;\s*\d\)$|'
    r'^[A-Z]\s*=\s*\d|\+\s|^\d+\s*%$')
RE_REF = re.compile(r'(?:,|»|\)|\d)\s*(?:1[6-9]|20)\d\d\s*\.?$')
RE_EMOJI = re.compile(r'^[\U0001F300-\U0001FAFF←-⇿⬀-⯿📌🖼⬇✏️]')


def est_formule(t):
    return bool(RE_FORMULE.search(t))


def mots(t):
    return len([w for w in re.split(r'\s+', t) if w])


def classe(i, t):
    if i in H2:
        return 'h2'
    if i in H4:
        return 'h4'
    if i in H3:
        return 'h3'
    if i in FORMULES:
        return 'formule'
    b = t.lower().strip().rstrip('.').rstrip(' :')
    if b in LABELS:
        return 'h4'
    if t.endswith('?') and len(t) > 90:
        return 'pb'
    if t.startswith('👉') or RE_EMOJI.match(t):
        return None
    if re.search(r'[.;,»!]$', t):
        return None
    if t.endswith(':') and not re.match(r'^(Premi|Deuxi|Troisi|Quatri|Cinqui|Second|\d\s*-)', t):
        return None
    if RE_REF.search(t) and not re.match(r'^(Le|La|Les|L’|Un|Une)\b', t):
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
                r'Premier|Second|Un premier|Une premi[eè]re|Cas \d|Exemple|'
                r'Définition|Théorème|Étape \d)\b', t):
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
    out = ['<div class="nb ch24-premium-course">']
    out.append('  <h2>Deuxième année, chapitre 4 — Régionalisation, gouvernance '
               'et régulations internationales</h2>')
    out.append('  <p>Dans un contexte de fragmentation géoéconomique, de retour des '
               'souverainetés nationales et de crise du multilatéralisme, sous quelles '
               'formes peut-on encore réguler la mondialisation ?</p>')
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
        t = re.sub(r'(\S)\((1[5-9]\d\d|20\d\d)\)', r'\1 (\2)', p['txt'].strip())
        if i == 0 or i in SKIP:
            continue
        if i in TABLEAUX:
            titre, entetes, corps, fin = TABLEAUX[i]
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
        if p.get('img'):
            vider()
            out.append('  <div class="db"><div class="dt">Document</div>'
                       '<div class="dd">Graphique ou schéma du cours.</div></div>')
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
        if c == 'pb':
            vider()
            out.append('  <h4>Problématique</h4>')
            out.append('  <p>' + esc(t) + '</p>')
            continue
        if c == 'formule':
            vider()
            out.append('  <div class="formula">' + esc(t) + '</div>')
            continue
        if c == 'h4':
            vider()
            lib = H4.get(i) or t
            base = lib.strip().lower().rstrip('.')
            if base == 'cl':
                lib = 'Idée clé'
            elif base.endswith(' :'):
                lib = lib.strip()[:-1].rstrip()
            out.append('  <h4>' + esc(lib) + '</h4>')
            continue
        # --- corps ---
        if t.startswith('Lecture :') or t.startswith('Lecture:'):
            vider()
            out.append('  <div class="db"><div class="dt">Lecture</div><div class="dd">'
                       + esc(t.split(':', 1)[1].strip()) + '</div></div>')
            continue
        if RE_REF.search(t) and mots(t) >= 3 and not t.startswith('👉') and len(t) < 240 \
                and re.search(r'[«»,]|\bdans\b', t):
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
    open(os.path.join(ICI, 'cours_ch4.html'), 'w', encoding='utf-8').write(h)
    print('longueur', len(h))
    hs = re.findall(r'<(h[2-4])>(.*?)</\1>', h)
    print('titres', len(hs))
    for lvl, txt in hs:
        print(('' if lvl == 'h2' else '    ' if lvl == 'h3' else '        ') + lvl + ' ' + txt[:95])
