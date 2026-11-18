# -*- coding: utf-8 -*-
"""Conversion en cours HTML des documents de deuxième année (chapitres 5 et 6).

Les deux documents sont des transcriptions de cours oral : aucun style de titre
n'est porté par le fichier Word, la hiérarchie est donc reconstruite à partir du
contenu. Trois particularités de ces documents sont traitées ici :

  * les lignes « 👉 » prolongent la ligne précédente qui se termine par deux
    points ; une seule ligne de prolongement est recollée à la précédente, un
    groupe de plusieurs devient une liste ;
  * les enchaînements de mécanismes sont écrits sur plusieurs lignes
    (« Taux d'intérêt ↓ » puis « → investissement ↑ ») : ils sont réunis en un
    seul encadré ;
  * les repères de montage du document (⸻, « 📌 IMAGE », « Insérer ici… ») et
    les images sont retirés, conformément à la demande : la partie Cours ne
    reprend que le texte. Les paragraphes « Lecture : » sont conservés, car ils
    décrivent le contenu des graphiques.
"""
import html
import re

LABELS = {
    'idée', 'idée générale', 'idée clé', 'idée importante', 'idée essentielle',
    'idée fondamentale à retenir', 'mécanisme', 'mécanisme complet',
    'exemple', 'exemples', 'rappel', 'conclusion', 'problématique', 'cl',
    'le principe', 'lecture', 'définition', 'transition', 'pourquoi ?',
    'attention', 'autre exemple', 'exemple historique', 'exemple majeur',
    'premier cas', 'deuxième cas', 'troisième cas', 'quatrième cas',
    'cas 1', 'cas 2', 'phrase parfaite', 'nuance', 'nuance importante',
    'nuance essentielle', 'précision', 'précision importante',
    'remarque', 'à retenir', 'conséquence', 'conséquence économique',
    'conséquences', 'objectif', 'exemple simplifié', 'exemple chiffré',
    'bilan', 'limite fondamentale', 'résultat',
    'première distinction', 'deuxième distinction', 'origine du raisonnement',
    'points de vigilance', 'point de vigilance',
    'enchaînement général', 'synthèse',
}

# amorces de titres de rang 4
RE_H4 = re.compile(
    r'^(Premi[eè]re?|Deuxi[eè]me|Troisi[eè]me|Quatri[eè]me|Cinqui[eè]me|Sixi[eè]me|'
    r'Septi[eè]me|Huiti[eè]me|Premier|Second|Un premier|Une premi[eè]re|Cas \d|'
    r'Exemple|D[ée]finition|Th[ée]or[eè]me|[ÉE]tape \d|Phase \d|'
    r'Premi[eè]re valeur|Deuxi[eè]me valeur)\b')

# lignes de montage du document : retirées
RE_MONTAGE = re.compile(
    r'^(⸻|📌|IMAGE|Insérer ici|Je reprends exactement|Point de vigilance|'
    r'J’ai également placé|Début de la première grande partie|'
    r'La prof emploie cette expression|IMAGE À COLLER)')

RE_FORMULE = re.compile(
    r'[↑↓→↔⬇≠≈≥≤×÷]|^[\d\s,.%+−-]+$|^[A-Za-zΔ][\w₀-₉’\'()*]*\s*=|'
    r'^\|ε|^e = |^k[A-Z] = |^\d+\s*%$|^r [<>] r')
RE_REF = re.compile(r'(?:,|»|\)|\d)\s*(?:1[6-9]|20)\d\d\s*\.?$')
RE_PUCE = re.compile(r'^👉\s*')
# numérotation déjà présente dans le document (« A. », « 1- », « 2. »)
RE_NUM = re.compile(r'^(?:[A-Z]\.\s+|\d\s*[-–.]\s*)')


# tournures orales de la transcription, ramenées à la langue du cours
ORAL = [
    ('Exemple évoqué par la prof', 'Exemple du cours'),
    ('La prof emploie cette expression', 'Le cours emploie cette expression'),
    ('La prof prend l’exemple', 'Le cours prend l’exemple'),
    ('La prof souligne', 'Le cours souligne'),
    ('La prof évoque', 'Le cours évoque'),
    ('La prof insiste', 'Le cours insiste'),
    ('la prof insiste', 'le cours insiste'),
    ('la prof évoque', 'le cours évoque'),
    ('la prof souligne', 'le cours souligne'),
    # lapsus de transcription : l'économiste des dilemmes de politique
    # économique est Jacques Généreux
    ('Jacques Généreux', 'Jacques Généreux'),
]


def nettoyer(t):
    for a, b in ORAL:
        if a in t:
            t = t.replace(a, b)
    return t


def mots(t):
    return len([w for w in re.split(r'\s+', t) if w])


def esc(s):
    return html.escape(s, quote=False)


def est_formule(t):
    if RE_FORMULE.search(t):
        return True
    # « Y(1 − c) = C₀ − cT + cF + I + G » : égalité courte sans ponctuation finale
    return ('=' in t and len(t) < 70 and not re.search(r'[.?!;:]$', t)
            and mots(t) < 20)


def est_mecanisme(t):
    """Ligne de départ ou de poursuite d'un enchaînement de mécanisme."""
    return t.startswith('→') or t.startswith('⬇')


ROM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lettre(n):
    if n < 26:
        return ROM[n]
    return ROM[n // 26 - 1] + ROM[n % 26]


class Cours(object):
    def __init__(self, paras, h2, titre, chapeau, classe_css,
                 skip=(), h3=(), h4=None, formules=(), tableaux=None,
                 numerotation='lettres'):
        self.P = paras
        self.H2 = h2
        self.titre = titre
        self.chapeau = chapeau
        self.css = classe_css
        self.SKIP = set(skip)
        self.H3 = set(h3)
        self.H4 = dict(h4 or {})
        self.FORMULES = set(formules)
        self.TAB = dict(tableaux or {})
        self.num = numerotation

    # ------------------------------------------------------------- découpage
    def classe(self, i, t):
        if i in self.H2:
            return 'h2'
        if i in self.H4:
            return 'h4'
        if i in self.H3:
            return 'h3'
        if i in self.FORMULES:
            return 'formule'
        b = t.lower().strip().rstrip('.').rstrip(' :').rstrip(' ?')
        if b in LABELS:
            return 'h4'
        if t.endswith('?'):
            return 'pb' if len(t) > 95 else None
        if est_mecanisme(t):
            return 'mec'
        if re.search(r'[.;,»!]$', t):
            return None
        if t.endswith(':'):
            return None
        if RE_REF.search(t) and not re.match(r'^(Le|La|Les|L’|Un|Une)\b', t):
            return None
        if est_formule(t):
            return None
        if not re.match(r'^[A-ZÀÂÉÈÊÎÔÛÇ«]', t):
            return None
        if mots(t) < 4 or len(t) < 22 or len(t) > 112:
            return None
        if RE_H4.match(t):
            return 'h4'
        if self.ouvre_mecanisme(i):
            return 'mec0'
        return 'h3'

    def ouvre_mecanisme(self, i):
        """Vrai si la ligne suivante prolonge la ligne i par une flèche."""
        for j in range(i + 1, min(i + 3, len(self.P))):
            u = self.P[j]['txt'].strip()
            if not u:
                continue
            return u.startswith('→')
        return False

    # ------------------------------------------------------------ assemblage
    def construire(self):
        P = self.P
        out = ['<div class="nb %s">' % self.css]
        out.append('  <h2>%s</h2>' % esc(self.titre))
        out.append('  <p>%s</p>' % esc(self.chapeau))
        puces = []
        mec = []
        nlettre = 0
        saut = -1

        def vider():
            if puces:
                out.append('  <ul>' + ''.join(
                    '<li>' + esc(x) + '</li>' for x in puces) + '</ul>')
                del puces[:]

        def vider_mec():
            if mec:
                out.append('  <div class="formula">' + esc(' '.join(mec))
                           + '</div>')
                del mec[:]

        def vider_tout():
            vider_mec()
            vider()

        for i, p in enumerate(P):
            if i <= saut or i in self.SKIP:
                continue
            t = nettoyer(re.sub(r'(\S)\((1[5-9]\d\d|20\d\d)\)', r'\1 (\2)',
                                p['txt'].strip()))
            if not t:
                continue
            if RE_MONTAGE.match(t):
                continue

            # --- tableaux reconstitués
            if i in self.TAB:
                titre, entetes, corps, fin = self.TAB[i]
                vider_tout()
                saut = fin
                th = ''.join('<th>' + esc(x) + '</th>' for x in entetes)
                tr = ''.join('<tr>' + ''.join('<td>' + esc(c) + '</td>'
                                              for c in l) + '</tr>'
                             for l in corps)
                out.append('  <div class="table-wrap"><div class="dt">'
                           + esc(titre) + '</div><table class="dt"><tr>' + th
                           + '</tr>' + tr + '</table></div>')
                continue

            # --- regroupement « ligne : » + « 👉 … »
            if t.endswith(':') and i + 1 < len(P):
                suite = []
                j = i + 1
                while j < len(P):
                    u = P[j]['txt'].strip()
                    if not u or RE_MONTAGE.match(u):
                        break
                    if not u.startswith('👉'):
                        break
                    suite.append(RE_PUCE.sub('', u).strip())
                    j += 1
                if len(suite) == 1 and not est_formule(suite[0]):
                    corps = suite[0]
                    if corps:
                        # le prolongement commence en minuscule : la phrase se
                        # recolle sans les deux points ; s'il commence par une
                        # majuscule (nom propre, sigle, variable), on les garde
                        if corps[:1].islower():
                            t = t[:-1].rstrip() + ' ' + corps
                        else:
                            t = t + ' ' + corps
                        saut = j - 1
                elif len(suite) >= 2:
                    vider_mec()
                    out.append('  <p>' + esc(t) + '</p>')
                    for x in suite:
                        puces.append(x)
                    vider()
                    saut = j - 1
                    continue

            c = self.classe(i, t)

            if c == 'mec0':
                vider()
                mec.append(t)
                continue
            if c == 'mec':
                vider()
                if mec:
                    mec.append(t)
                else:
                    # la ligne précédente a ouvert le mécanisme
                    if out and out[-1].startswith('  <p>'):
                        ouvre = out.pop()[5:-4]
                        mec.append(ouvre)
                    mec.append(t)
                continue
            vider_mec()

            if c == 'h2':
                vider()
                nlettre = 0
                out.append('  <h2>' + esc(self.H2[i]) + '</h2>')
                continue
            if c == 'h3':
                vider()
                t = RE_NUM.sub('', t).strip()
                rang = (str(nlettre + 1) if self.num == 'chiffres'
                        else lettre(nlettre))
                out.append('  <h3>' + rang + '. ' + esc(t) + '</h3>')
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
                lib = RE_NUM.sub('', self.H4.get(i) or t).strip()
                base = lib.strip().lower().rstrip('.')
                if base == 'cl':
                    lib = 'Idée clé'
                elif base == 'phrase parfaite':
                    lib = 'Phrase à retenir'
                elif base.endswith(' :') or base.endswith(':'):
                    lib = lib.strip().rstrip(':').rstrip()
                out.append('  <h4>' + esc(lib) + '</h4>')
                continue

            # --- corps de texte
            if t.startswith('Lecture :') or t.startswith('Lecture du graphique')\
                    or t.startswith('Lecture du tableau'):
                vider()
                lab, _, reste = t.partition(':')
                out.append('  <div class="db"><div class="dt">' + esc(lab.strip())
                           + '</div><div class="dd">' + esc(reste.strip())
                           + '</div></div>')
                continue
            if t.startswith('👉'):
                t = RE_PUCE.sub('', t).strip()
                if not t:
                    continue
            if self.ouvre_mecanisme(i) and not puces:
                vider()
                mec.append(t)
                continue
            if est_formule(t) and len(t) < 260:
                vider()
                out.append('  <div class="formula">' + esc(t) + '</div>')
                continue
            if RE_REF.search(t) and mots(t) >= 3 and len(t) < 240 \
                    and re.search(r'[«»,]|\bdans\b', t):
                vider()
                out.append('  <div class="db"><div class="dt">Référence</div>'
                           '<div class="dd">' + esc(t) + '</div></div>')
                continue
            if t.endswith(';') or (len(t) < 110 and not re.search(r'[.?!:]$', t)
                                   and mots(t) >= 2) \
                    or (puces and len(t) < 110 and t[:1].islower()
                        and t.endswith('.')):
                puces.append(t)
                continue
            vider()
            out.append('  <p>' + esc(t) + '</p>')

        vider_tout()
        out.append('</div>')
        return '\n'.join(out)
