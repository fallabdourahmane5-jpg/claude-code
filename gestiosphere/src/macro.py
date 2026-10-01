"""Matière : Macroéconomie (économie ouverte) — 5 documents de notes de cours (MACRO_R, R2, 3-1, R4, R5)."""
from lib import table, ul, ol, P, H3, H4, NOTE, WARN, FORM, fr
from svg import Plot, COL, boxes, E
from macro_cours import ch1, ch2, ch3, ch4, ch5

SRC = ['MACRO_R — Balance des paiements, PEN, balance globale, absorption et épargne',
       'MACRO_R2 — Taux de change, marché des changes, régimes de change fixe et flexible',
       'MACRO_3-1 — Taux de change réel, élasticités, Marshall-Lerner, courbe en J, PTINC',
       'MACRO_R4 — Marché du travail, IS, LM, PTINC, équilibre général',
       'MACRO_R5 — Politiques monétaire et budgétaire, triangle d\'incompatibilité, hausse de i*']
DOCS = SRC

RED = '#f76a6a'
BLUE = '#6aa8f7'


def duo(a, b):
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">{a}{b}</div>'


# ---------------------------------------------------------------- IS-LM-PTINC
def _is(c):
    return lambda y: c - 0.8 * y


def _lm(d):
    return lambda y: 0.8 * y - d


def panel(titre, IS=(), LM=(), PT=(), pts=(), arrows=(), dash=()):
    """IS : i = c − 0,8Y ; LM : i = 0,8Y − d ; PT : niveau de la PTINC. Chaque élément : (paramètre, couleur, étiquette)."""
    p = Plot(10, 10, 'Y', 'i', w=260, h=250, pad=(30, 12, 26, 34)).axes()
    for lev, col, lab in PT:
        p.curve([(0, lev), (10, lev)], col, 2, label=lab, lpos=(0.1, lev + 0.15))
    for cc, col, lab in IS:
        yl = min(9.7, (cc - 0.4) / 0.8)
        p.fn(_is(cc), 0, 10, color=col, width=2, label=lab, lpos=(yl, cc - 0.8 * yl), anchor='end')
    for d, col, lab in LM:
        yl = min(9.7, (9.6 + d) / 0.8)
        p.fn(_lm(d), 0, 10, color=col, width=2, label=lab, lpos=(yl - 0.25, 0.8 * yl - d), anchor='end')
    for x, y in dash:
        p.dashes(x, y)
    for x, y, lab, col in pts:
        p.point(x, y, col, lab, dx=5, dy=-6, r=3.5)
    for a in arrows:
        p.arrow(*a)
    p.text(5, 9.6, titre, '#e8eaf2', 11, 'middle', 700)
    return p.svg()


def plot_islm_base():
    a = panel('Courbe IS', IS=((9, COL[1], 'IS'), (11, RED, 'IS1')), arrows=((5.2, 4.6, 6.6, 4.8),), pts=((5, 5, 'G ↑, T ↓, Y* ↑…', '#f7e66a'),))
    b = panel('Courbe LM', LM=((1, COL[0], 'LM'), (3, BLUE, 'LM1')), arrows=((5.6, 3.9, 6.9, 3.2),), pts=((4.6, 4.2, 'Ms ↑', '#f7e66a'),))
    return duo(a, b)


def plot_equilibre():
    p = Plot(10, 10, 'Y', 'i', pad=(56, 20, 24, 44)).axes()
    p.curve([(0, 4), (10, 4)], COL[2], 2.2, label='PTINC : i = i* + êᵃ', lpos=(6.6, 4.2))
    p.fn(_is(9), 0, 10, color=COL[1], label='IS (marché des biens)', lpos=(1.4, 8.2))
    p.fn(_lm(1), 0, 10, color=COL[0], label='LM (marché de la monnaie)', lpos=(9.6, 6.6), anchor='end')
    p.point(6.25, 4, '#e8eaf2', 'E (Yé ; ié)', dx=6, dy=16)
    p.dashes(6.25, 4, xl='Yé', yl='ié')
    p.text(1.2, 6.4, 'BG > 0 : entrées de capitaux', '#f7e66a', 10)
    p.text(1.2, 2.2, 'BG < 0 : sorties de capitaux', '#f76ab4', 10)
    return p.svg()


def plot_retour_haut():
    a = panel('Change flexible', IS=((9, COL[1], 'IS'), (7, RED, 'IS1')), LM=((1, COL[0], 'LM'),), PT=((3, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'A', '#e8eaf2'), (5, 3, 'E', '#f7e66a')), arrows=((7.4, 2.6, 6.6, 1.9),))
    b = panel('Change fixe', IS=((9, COL[1], 'IS'),), LM=((1, COL[0], 'LM'), (3, BLUE, 'LM1')), PT=((3, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'A', '#e8eaf2'), (7.5, 3, 'E', '#f7e66a')), arrows=((5.2, 2.6, 6.4, 1.6),))
    return duo(a, b)


def plot_retour_bas():
    a = panel('Change flexible', IS=((9, COL[1], 'IS'), (11, RED, 'IS1')), LM=((1, COL[0], 'LM'),), PT=((5, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'A', '#e8eaf2'), (7.5, 5, 'E', '#f7e66a')), arrows=((7.6, 2.4, 8.6, 2.4),))
    b = panel('Change fixe', IS=((9, COL[1], 'IS'),), LM=((1, COL[0], 'LM'), (-1, BLUE, 'LM1')), PT=((5, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'A', '#e8eaf2'), (5, 5, 'E', '#f7e66a')), arrows=((6.6, 3.0, 5.4, 3.0),))
    return duo(a, b)


def plot_pol_mon():
    a = panel('Change flexible', IS=((9, COL[1], 'IS'), (11, RED, 'IS1')), LM=((1, COL[0], 'LM'), (3, BLUE, 'LM1')), PT=((4, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'E', '#e8eaf2'), (7.5, 3, 'A', '#f7e66a'), (8.75, 4, "E'", '#6af7a2')), arrows=((7.9, 2.0, 8.9, 2.0),))
    b = panel('Change fixe', IS=((9, COL[1], 'IS'),), LM=((1, COL[0], 'LM'), (3, BLUE, 'LM1 (prov.)')), PT=((4, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'E', '#6af7a2'), (7.5, 3, 'A', '#f7e66a')), arrows=((7.2, 2.6, 6.3, 3.4),))
    return duo(a, b)


def plot_pol_bud():
    a = panel('Change flexible', IS=((9, COL[1], 'IS'), (11, RED, 'IS1 (prov.)')), LM=((1, COL[0], 'LM'),), PT=((4, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'E', '#6af7a2'), (7.5, 5, 'A', '#f7e66a')), arrows=((7.4, 5.6, 6.5, 5.6),))
    b = panel('Change fixe', IS=((9, COL[1], 'IS'), (11, RED, 'IS1')), LM=((1, COL[0], 'LM'), (3, BLUE, 'LM1')), PT=((4, COL[2], 'PTINC'),),
              pts=((6.25, 4, 'E', '#e8eaf2'), (7.5, 5, 'A', '#f7e66a'), (8.75, 4, "E'", '#6af7a2')), arrows=((7.0, 2.2, 8.2, 2.2),))
    return duo(a, b)


def plot_istar():
    a = panel('Change flexible', IS=((9, COL[1], 'IS'), (11, RED, 'IS1')), LM=((1, COL[0], 'LM'),), PT=((4, '#4d5874', 'PTINC'), (5, COL[2], 'PTINC1')),
              pts=((6.25, 4, 'E', '#e8eaf2'), (7.5, 5, "E'", '#6af7a2')), arrows=((7.6, 2.4, 8.6, 2.4),))
    b = panel('Change fixe', IS=((9, COL[1], 'IS'),), LM=((1, COL[0], 'LM'), (-1, BLUE, 'LM1')), PT=((4, '#4d5874', 'PTINC'), (5, COL[2], 'PTINC1')),
              pts=((6.25, 4, 'E', '#e8eaf2'), (5, 5, "E'", RED)), arrows=((6.6, 3.0, 5.4, 3.0),))
    return duo(a, b)


# ---------------------------------------------------------------- change, J, élasticités, travail
def plot_changes():
    a = Plot(10, 10, 'Quantité de $', 'e (prix du $ en €)', w=260, h=250, pad=(30, 12, 26, 34)).axes()
    a.fn(lambda q: 9 - 0.8 * q, 0, 10, color=COL[0], width=2, label='D$', lpos=(8.6, 2.6))
    a.fn(lambda q: 1 + 0.8 * q, 0, 10, color=COL[1], width=2, label='O$', lpos=(8.0, 7.6))
    a.fn(lambda q: 0.8 * q - 1, 1.25, 10, color=RED, width=2, label="O$'", lpos=(9.0, 6.0))
    a.point(5, 5, '#e8eaf2', 'E0', dx=-20, dy=-6, r=3.5).point(6.25, 4, '#f7e66a', 'E1', dx=6, dy=14, r=3.5)
    a.arrow(6.2, 6.0, 7.4, 6.0)
    a.text(5, 9.6, 'Change flexible', '#e8eaf2', 11, 'middle', 700)
    a.text(0.4, 0.6, '$ se déprécie, € s\'apprécie', '#f7e66a', 9.5)
    b = Plot(10, 10, 'Quantité de $', 'e (prix du $ en €)', w=260, h=250, pad=(30, 12, 26, 34)).axes()
    b.fn(lambda q: 9 - 0.8 * q, 0, 10, color=COL[0], width=2, label='D$', lpos=(8.6, 2.6))
    b.fn(lambda q: 1 + 0.8 * q, 0, 10, color=COL[1], width=2, label='O$', lpos=(8.0, 7.6))
    b.fn(lambda q: 0.8 * q - 1, 1.25, 10, color=RED, width=2, label="O$'", lpos=(9.0, 6.0))
    b.curve([(0, 5), (10, 5)], COL[2], 1.6, dash='5 4', label='Parité', lpos=(0.2, 5.2))
    b.curve([(5, 5), (7.5, 5)], '#f7e66a', 4)
    b.text(4.2, 3.6, 'Achat de $ par la BC', '#f7e66a', 9.5)
    b.text(4.2, 2.8, '(réserves ↑, Ms ↑)', '#f7e66a', 9.5)
    b.text(5, 9.6, 'Change fixe', '#e8eaf2', 11, 'middle', 700)
    return duo(a.svg(), b.svg())


def plot_j():
    p = Plot(10, 4, 'Temps', 'Balance commerciale', ymin=-3.5, pad=(56, 20, 24, 44)).axes(yticks=[-3, 0, 3])
    p.curve([(0, 0), (10, 0)], '#4d5874', 1, dash='4 4')
    pts = [(0, 0), (1, 0), (1.5, -1.2), (2, -2.1), (2.6, -2.5), (3.2, -2.2), (4, -1.2), (4.8, 0), (6, 1.4), (7.5, 2.4), (9.5, 3.1)]
    p.curve(pts, COL[1], 2.6, label='Balance des biens et services', lpos=(5.6, 2.9))
    p.point(1, 0, '#f7e66a', 'Dépréciation', dx=-10, dy=-10)
    p.text(1.6, -3.2, 'Effet prix d\'abord (Z plus chères)', '#f76ab4', 10)
    p.text(5.6, -0.9, 'Puis effet volume (X ↑, Z ↓)', '#6af7a2', 10)
    return p.svg()


def plot_ml():
    p = Plot(4.6, 4, '', 'Variation (% des exportations)', ymin=-2, pad=(56, 20, 24, 44)).axes(yticks=[-1, 0, 1, 2, 3])
    data = [(0.7, 2, COL[0], 'X : +2 %'), (1.7, 1.5, COL[2], 'Z : −1,5 %'), (2.7, -1, RED, 'Effet prix'), (3.8, 2.5, '#f7e66a', 'Effet net')]
    for x, v, col, lab in data:
        p.area([(x - 0.3, 0), (x - 0.3, v), (x + 0.3, v), (x + 0.3, 0)], col, 0.85)
        p.text(x, v + (0.18 if v > 0 else -0.4), ('+' if v > 0 else '−') + fr(abs(v)), col, 11, 'middle', 700)
        p.text(x, -1.75, lab, '#c4c9d8', 10, 'middle')
    p.curve([(0, 0), (4.6, 0)], '#8890a8', 1)
    p.text(2.3, 3.75, 'Dépréciation réelle de 1 % (εX = −2 ; εZ = 1,5)', '#e8eaf2', 11, 'middle', 600)
    return p.svg()


def _bisect(f, a, b):
    for _ in range(60):
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


def plot_travail():
    ld = lambda L: 12 / (L + 1)
    ls = lambda L: 0.5 + 0.08 * L * L
    L0 = _bisect(lambda L: ld(L) - ls(L), 0.1, 9)
    w0 = ld(L0)

    def base(titre):
        p = Plot(10, 9, 'L', 'w/P', w=260, h=250, pad=(34, 12, 26, 34)).axes()
        p.fn(ld, 0.4, 9.6, color=COL[0], width=2, label='Ld', lpos=(8.8, ld(9.6) + 0.3))
        p.fn(ls, 0, 9.4, color=COL[1], width=2, label='Ls', lpos=(7.8, 7.0))
        p.curve([(9.6, 0), (9.6, 8.6)], '#8890a8', 1.4, label='PAT', lpos=(8.6, 8.4))
        p.text(5, 8.9, titre, '#e8eaf2', 11, 'middle', 700)
        return p
    a = base('Chômage classique')
    w1 = w0 + 1.6
    C = 12 / w1 - 1
    A = ((w1 - 0.5) / 0.08) ** 0.5
    a.curve([(0, w1), (A, w1)], '#4d5874', 1, dash='4 4')
    a.text(0.1, w1 + 0.2, 'w/P1', '#c4c9d8', 9.5)
    a.curve([(C, w1), (A, w1)], RED, 4)
    a.text((C + A) / 2, w1 - 0.6, 'chômage', RED, 10, 'middle')
    a.point(L0, w0, '#e8eaf2', 'E0', dx=6, dy=12, r=3)
    a.text(C, 0.3, 'C', '#c4c9d8', 10, 'middle').text(A, 0.3, 'A', '#c4c9d8', 10, 'middle')
    b = base('Chômage keynésien')
    Ck = L0 * 0.55
    b.curve([(Ck, 0), (Ck, 8.4)], '#f7e66a', 2, label='Demande effective', lpos=(Ck, 6.8))
    b.curve([(Ck, w0), (L0, w0)], RED, 4)
    b.text((Ck + L0) / 2, w0 - 0.6, 'chômage', RED, 10, 'middle')
    b.point(L0, w0, '#e8eaf2', 'L0', dx=6, dy=12, r=3)
    b.text(Ck, 0.3, 'C', '#c4c9d8', 10, 'middle')
    return duo(a.svg(), b.svg())


def plot_triangle():
    W, H = 520, 330
    A, B, C = (260, 40), (80, 270), (440, 270)
    el = [f'<path d="M{A[0]},{A[1]} L{B[0]},{B[1]} L{C[0]},{C[1]} Z" fill="#7c6af7" fill-opacity=".14" stroke="#7c6af7" stroke-width="2"/>']
    for (x, y), t, anc, dy in ((A, 'Change fixe', 'middle', -12), (B, 'Mobilité parfaite des capitaux', 'start', 26), (C, 'Politique monétaire autonome', 'end', 26)):
        el.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#f7e66a"/>')
        el.append(f'<text x="{x + (-60 if anc == "start" else 60 if anc == "end" else 0)}" y="{y + dy}" fill="#f7e66a" font-size="12.5" font-weight="700" text-anchor="{anc}">{E(t)}</text>')
    sides = [((A[0] + B[0]) / 2 - 12, (A[1] + B[1]) / 2, 'end', ['Union monétaire,', 'caisse d\'émission']), ((A[0] + C[0]) / 2 + 12, (A[1] + C[1]) / 2, 'start', ['Contrôle des capitaux', '(Bretton Woods)']),
             ((B[0] + C[0]) / 2, B[1] - 16, 'middle', ['Change flexible (dollar, livre, euro face au $)'])]
    for x, y, anc, lines in sides:
        for k, l in enumerate(lines):
            el.append(f'<text x="{x}" y="{y + k * 14}" fill="#c4c9d8" font-size="10.5" text-anchor="{anc}">{E(l)}</text>')
    el.append('<text x="260" y="168" fill="#e8eaf2" font-size="12" font-weight="700" text-anchor="middle">On ne peut avoir</text><text x="260" y="184" fill="#e8eaf2" font-size="12" font-weight="700" text-anchor="middle">que deux sommets</text>')
    return f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans, sans-serif">{"".join(el)}</svg>'


def plot_bp():
    return boxes(520, 330, [
        (10, 10, 240, 150, 'Compte courant (CC)', ['Biens : balance commerciale', 'Services : tourisme, transport…', 'Revenus primaires : dividendes, intérêts', 'Revenus secondaires : transferts', 'sans contrepartie'], COL[1]),
        (270, 10, 240, 70, 'Compte de capital (CK)', ['Remises de dette, brevets'], COL[4]),
        (270, 95, 240, 150, 'Compte financier (CF)', ['IDE (≥ 10 %)', 'Investissements de portefeuille', 'Produits dérivés', 'Autres investissements (prêts)', 'Avoirs de réserve (BC)'], COL[0]),
        (10, 180, 240, 65, 'Erreurs et omissions (EO)', ['Solde de ce qui manque'], '#8890a8'),
        (60, 262, 400, 58, 'CC + CK − CF + EO = 0', ['CF = Δ avoirs − Δ engagements · BG = CC + CK − CFHAR = Δ AR'], COL[2])],
        [(250, 85, 268, 150, 'contrepartie'), (130, 245, 160, 262, ''), (390, 245, 360, 262, '')])


def plot_absorption():
    return boxes(520, 300, [
        (10, 10, 240, 120, 'Lecture par la dépense', ['PIB = C + I + G + (X − M)', 'PNB = PIB + revenus nets du RDM', 'PNB = A + CC', 'avec A = C + I + G (absorption)'], COL[1]),
        (270, 10, 240, 120, 'Lecture par l\'épargne', ['PNB = C + S + T', 'C + S + T = C + I + G + CC', 'CC = (S − I) + (T − G)', 'épargne privée + épargne publique'], COL[0]),
        (60, 175, 400, 110, 'Déficit courant (CC < 0)', ['Le pays dépense plus qu\'il ne gagne (A > PNB)', 'Son épargne nationale ne couvre pas son investissement', 'Il emprunte l\'épargne du RDM : entrée de capitaux, PEN ↓'], RED)],
        [(130, 130, 200, 175, ''), (390, 130, 320, 175, '')])


# ---------------------------------------------------------------- sujets
def sujets():
    S = []
    # Exercice 1 : enregistrement et soldes
    bien, serv = 500 - 560, 120 - 80
    rp, rs = 60 - 40, 5 - 30
    cc = bien + serv + rp + rs
    ck = -10
    dav, deng = 70 + 20 + 25, 90 + 40
    cf = dav - deng
    eo = -(cc + ck - cf)
    cfhar = cf - 25
    bg = cc + ck - cfhar
    assert (cc, cf, eo, bg) == (-25, -15, 20, 5) and bg - 25 + eo == 0
    S.append(dict(id='mac-s1', num='Exercice 1', ch='macro-1', mobiliser=['compta-0'], type='Exercice d\'application', source='D\'après MACRO_R (postes, partie double, BG)',
                  titre='Construire la balance des paiements d\'un pays et calculer ses soldes',
                  enonce=P('Opérations de la France avec le RDM sur une année (en millions d\'euros) :') + ol([
                      'Exportations de biens : 500 ; importations de biens : 560.', 'Tourisme : dépenses des étrangers en France 120 ; dépenses des Français à l\'étranger 80.',
                      'Dividendes et intérêts reçus du RDM : 60 ; versés au RDM : 40.', 'Contribution au budget européen : 30 ; envois de fonds reçus de travailleurs émigrés : 5.',
                      'La France annule une dette de 10 d\'un pays en développement.', 'Une entreprise française rachète 30 % d\'une société américaine : 70.',
                      'Des non-résidents achètent des obligations du Trésor français : 90.', 'Les banques françaises empruntent 40 à l\'étranger et prêtent 20 à des non-résidents.',
                      'La Banque de France achète 25 de devises.']) +
                         P('Questions :') + ol(['Classer chaque opération dans son compte et son poste.', 'Calculer la balance commerciale, la balance des services, le compte courant et le compte de capital.', 'Calculer le solde du compte financier, puis les erreurs et omissions.', 'Calculer le CFHAR et la balance globale ; vérifier BG = Δ AR − EO.', 'Interpréter.']),
                  pourquoi='Chapitre 1, sections I (postes), II (partie double) et IV (balance globale).',
                  commentaire=ul(['Bien séparer <b>revenus</b> (compte courant) et <b>achats d\'actifs</b> (compte financier).', 'Compte financier : on calcule Δ avoirs − Δ engagements, pas « crédit − débit ».', 'Les erreurs et omissions se calculent en dernier, par l\'équation CC + CK − CF + EO = 0.']),
                  corrige=H3('1. Classement') + table(['Opération', 'Compte · poste'], [
                      ['1', 'CC · biens'], ['2', 'CC · services'], ['3', 'CC · revenus primaires'], ['4', 'CC · revenus secondaires'], ['5', 'Compte de capital'], ['6', 'CF · IDE sortant (≥ 10 %) : avoirs ↑'],
                      ['7', 'CF · investissement de portefeuille : engagements ↑'], ['8', 'CF · autres investissements : engagements ↑ 40, avoirs ↑ 20'], ['9', 'CF · avoirs de réserve ↑']]) +
                          H3('2. Soldes du compte courant') + table(['Solde', 'Calcul', 'Montant'], [
                              ['Balance commerciale', '500 − 560', bien], ['Balance des services', '120 − 80', serv], ['Revenus primaires', '60 − 40', rp], ['Revenus secondaires', '5 − 30', rs],
                              ['<b>Compte courant</b>', '−60 + 40 + 20 − 25', cc], ['<b>Compte de capital</b>', 'remise de dette accordée', ck]], num_cols=(2,)) +
                          H3('3. Compte financier et erreurs et omissions') + FORM(f'Δ avoirs = 70 + 20 + 25 = {dav} · Δ engagements = 90 + 40 = {deng} · CF = {dav} − {deng} = {fr(cf)}') +
                          FORM(f'CC + CK − CF + EO = 0 ⇒ {fr(cc)} {fr(ck)} + 15 + EO = 0 ⇒ EO = {fr(eo)}') +
                          H3('4. Balance globale') + FORM(f'CFHAR = CF − Δ AR = {fr(cf)} − 25 = {fr(cfhar)} · BG = CC + CK − CFHAR = {fr(cc)} {fr(ck)} + 40 = {fr(bg)}') +
                          P(f'Vérification : BG − Δ AR + EO = {bg} − 25 + {eo} = 0. ✔') +
                          H3('5. Interprétation') + ul(['Le pays est en <b>déficit courant</b> (−25) : il dépense plus qu\'il ne gagne avec le RDM, surtout à cause des biens.',
                                                         'Ce déficit est financé par des <b>entrées de capitaux</b> : les engagements (+130) augmentent plus que les avoirs (+115), CF < 0. La richesse nette sur l\'étranger baisse.',
                                                         'Les agents privés ont fait entrer plus de devises qu\'il n\'en fallait (CFHAR = −40) : la BG est excédentaire et la banque centrale a accumulé 25 de réserves (aux erreurs et omissions près).'])))
    # Exercice 2 : absorption, épargne, PEN
    S.append(dict(id='mac-s2', num='Exercice 2', ch='macro-1', mobiliser=['macro-3'], type='Exercice d\'application', source='D\'après MACRO_R (absorption, épargne, PEN)',
                  titre='Compte courant, absorption et épargne : deux lectures d\'un même déficit',
                  enonce=P('Données (en milliards d\'euros) : PIB = 2 000 ; revenus primaires nets reçus du RDM = +20 ; revenus secondaires nets = −25 ; C = 1 300 ; I = 450 ; G = 400 ; T = 380. PEN en début d\'année : +300.') +
                         ol(['Calculer le solde des biens et services (X − M).', 'Calculer le PNB et le compte courant.', 'Calculer l\'absorption et vérifier CC = PNB − A.', 'Calculer l\'épargne privée S, l\'épargne privée nette et l\'épargne publique ; vérifier CC = (S − I) + (T − G).', 'En supposant CK = EO = 0 et aucun effet de valorisation, que devient la PEN ?', 'Quelles politiques pourraient réduire ce déficit ? Quel en serait le coût ?']),
                  pourquoi='Chapitre 1, sections III (PEN) et V (absorption et épargne). La question 6 annonce les chapitres 3 et 5.',
                  commentaire=ul(['PNB = C + S + T sert à trouver S.', 'Ne pas oublier que la PEN varie du solde du compte financier (= CC si CK = EO = 0).']),
                  corrige=ol(['X − M = PIB − (C + I + G) = 2 000 − 2 150 = <b>−150</b>.', 'PNB = 2 000 + 20 − 25 = <b>1 995</b> ; CC = −150 + 20 − 25 = <b>−155</b>.',
                              'A = C + I + G = <b>2 150</b> ; PNB − A = 1 995 − 2 150 = −155 = CC. ✔ Le pays dépense plus qu\'il ne gagne.',
                              'S = PNB − C − T = 1 995 − 1 300 − 380 = <b>315</b>. Épargne privée nette S − I = 315 − 450 = <b>−135</b>. Épargne publique T − G = 380 − 400 = <b>−20</b> (déficit public). Somme : −155 = CC. ✔ Le déficit vient surtout du privé.',
                              'CF = CC = −155 : la PEN passe de +300 à <b>+145</b>. Le pays reste créancier net mais sa richesse extérieure fond ; au même rythme, elle deviendrait négative en un an de plus (comme les États-Unis dans les années 1980).',
                              'Réduire l\'absorption (moins de C, I ou G) : coûteux en croissance et en emploi. Augmenter l\'épargne (privée ou publique). Gagner en compétitivité-prix (dépréciation réelle, désinflation compétitive) si la condition de Marshall-Lerner est vérifiée (chapitre 3).'])))
    # Exercice 3 : cotations
    S.append(dict(id='mac-s3', num='Exercice 3', ch='macro-2', mobiliser=[], type='Exercice d\'application', source='D\'après MACRO_R2 (cotations, PIP, spread)',
                  titre='Cotation au certain et à l\'incertain, PIP et spread',
                  enonce=ol(['L\'euro est coté 1 EUR = 1,1250 USD. Donner la cotation à l\'incertain.', 'Le lendemain, 1 EUR = 1,1300 USD. L\'euro s\'est-il apprécié ou déprécié ? De combien de PIP et de combien de % ?',
                             'Une banque affiche EUR/USD 1,1248 / 1,1252. Lequel est le cours d\'achat, lequel le cours de vente ? Quel est le spread ?', 'Tu vends 10 000 € à cette banque, puis tu rachètes immédiatement des euros avec les dollars obtenus. Combien d\'euros récupères-tu ? Commente.']),
                  pourquoi='Chapitre 2, section I.',
                  commentaire=ul(['Le cours d\'achat est toujours le plus faible : la banque achète bas et vend haut.', 'Un PIP = 0,0001.']),
                  corrige=ol(['1 USD = 1/1,1250 = <b>0,8889 EUR</b>.', 'Avec 1 € on obtient plus de dollars : l\'euro s\'est <b>apprécié</b> de 50 PIP (1,1300 − 1,1250 = 0,0050), soit (1,1300/1,1250 − 1) ≈ <b>+0,44 %</b>.',
                              'Cours d\'achat (bid) = 1,1248, cours de vente (offer) = 1,1252 ; spread = <b>4 PIP</b>.', 'Vente de 10 000 € au cours d\'achat : 11 248 $. Rachat d\'euros au cours de vente : 11 248/1,1252 ≈ <b>9 996,44 €</b>. La perte de 3,56 € est le coût du spread, la marge de la banque.'])))
    # Exercice 4 : BG et régimes
    S.append(dict(id='mac-s4', num='Question de cours', ch='macro-2', mobiliser=['macro-1'], type='Question de réflexion', source='D\'après MACRO_R2 (interprétation de la balance des paiements)',
                  titre='Une balance globale excédentaire : que se passe-t-il en change flexible et en change fixe ?',
                  enonce=P('La zone euro a un compte courant excédentaire, mais les placements à l\'étranger de ses résidents (CFHAR) sont inférieurs à cet excédent.') + ol(['Que vaut le signe de la BG ? Que détiennent les résidents en trop ?', 'Quelle est la situation du marché des changes ?', 'Décrire l\'ajustement en change flexible.', 'Décrire l\'ajustement en change fixe ; pourquoi l\'équilibre n\'est-il d\'abord que temporaire ?', 'Quel est le risque dans la situation inverse (BG déficitaire) en change fixe ?']),
                  pourquoi='Chapitre 2, sections II à IV, et chapitre 1, section IV (BG).',
                  commentaire=ul(['Toujours partir de : qui offre quelle monnaie, qui en demande ?', 'En change fixe, ne pas oublier l\'effet sur la masse monétaire.']),
                  corrige=ol(['BG = CC + CK − CFHAR > 0 : les résidents détiennent un <b>excès d\'avoirs en dollars</b> qu\'ils n\'ont pas placés.', 'Ils rapatrient ces dollars : <b>offre excédentaire de dollars, demande excédentaire d\'euros</b>. Ni le marché des changes ni la BG ne sont à l\'équilibre.',
                              'Le dollar se déprécie, l\'euro s\'apprécie, sans intervention de la BCE. Le marché des changes et la BG reviennent à l\'équilibre : équilibre <b>stationnaire</b> obtenu par le taux de change.',
                              'La BCE achète les dollars en trop contre des euros qu\'elle crée : réserves en dollars ↑, masse monétaire ↑. Le marché des changes est équilibré, mais la BG reste excédentaire : équilibre <b>temporaire</b>, qui ne peut durer (les réserves exploseraient). Ensuite, Ms ↑ ⇒ i ↓ ⇒ sorties de capitaux ⇒ la BG se rééquilibre : équilibre stationnaire.',
                              'La BCE doit vendre des dollars : ses réserves baissent et peuvent s\'épuiser. Elle ne peut plus défendre la parité : <b>dévaluation</b>. En attendant, la baisse de la masse monétaire fait monter les taux et peut provoquer une récession.'])))
    # Exercice 5 : TCR et ML
    S.append(dict(id='mac-s5', num='Exercice 5', ch='macro-3', mobiliser=['micro-1'], type='Exercice d\'application', source='D\'après MACRO_3-1 (TCR, élasticités, Marshall-Lerner)',
                  titre='Calculer un taux de change réel et l\'effet d\'une dépréciation sur la balance commerciale',
                  enonce=P('Indice des prix français P = 105, indice des prix américains P* = 100, e = 0,90 € pour 1 $.') + ol(['Calculer le TCR et l\'interpréter.', 'L\'année suivante : inflation française 2 %, américaine 3 %, et e passe à 0,92. Calculer le nouveau TCR et son taux de variation (exact et approché).', 'ε X/TCR = −0,8 et ε Z/TCR = 0,6. Calculer les variations des exportations et des importations en volume.', 'La condition de Marshall-Lerner est-elle vérifiée ? De combien la balance s\'améliore-t-elle (en % des exportations, en partant d\'une balance équilibrée) ?', 'Pourquoi l\'amélioration risque-t-elle de ne pas apparaître tout de suite ?']),
                  pourquoi='Chapitre 3, sections I à IV. L\'élasticité est la même notion qu\'en micro (chapitre 1).',
                  commentaire=ul(['TCR = P/(e·P*) avec e le prix du dollar en euros.', 'Approximation : TCR^ ≈ π − π* − ê.', 'Effet net ≈ (|εX| + εZ − 1) × |TCR^|.']),
                  corrige=ol(['TCR = 105/(0,90 × 100) ≈ <b>1,167</b> > 1 : les produits français sont plus chers que les produits américains convertis en euros ; la France est moins compétitive.',
                              'TCR = 107,1/(0,92 × 103) ≈ <b>1,130</b>. Variation exacte : 1,130/1,167 − 1 ≈ <b>−3,12 %</b>. Approximation : 2 − 3 − 2,22 ≈ −3,22 %. Dépréciation réelle : gain de compétitivité.',
                              'X^ = −0,8 × (−3,12) ≈ <b>+2,5 %</b> ; Z^ = 0,6 × (−3,12) ≈ <b>−1,87 %</b>.',
                              '|−0,8| + 0,6 = 1,4 > 1 : <b>vérifiée</b>. Effet net ≈ (1,4 − 1) × 3,12 ≈ <b>+1,25 %</b> des exportations : l\'effet volume (4,37 %) dépasse l\'effet prix (3,12 %).',
                              'Courbe en J : l\'effet prix (importations plus chères) est immédiat, l\'effet volume demande du temps (contrats, habitudes). La balance commence par se dégrader.'])))
    S.append(dict(id='mac-s6', num='QCM raisonné', ch='macro-3', mobiliser=[], type='Exercice d\'application', source='D\'après MACRO_3-1 (exemples du cours)',
                  titre='Marshall-Lerner : trois pays, trois diagnostics',
                  enonce=P('Pour chaque pays, dire si une dépréciation réelle de 1 % améliore la balance des biens et services, et de combien (balance initialement équilibrée).') + table(['Pays', 'ε X/TCR', 'ε Z/TCR'], [['A', '−2', '1,5'], ['B', '−0,7', '0,5'], ['C', '−0,3', '0,4']]) + P('Puis : que se passe-t-il pour le pays A en cas d\'appréciation réelle de 1 % ?'),
                  pourquoi='Chapitre 3, section III.',
                  commentaire=ul(['Somme des valeurs absolues comparée à 1.', 'L\'amélioration est l\'écart à 1, pas la somme.']),
                  corrige=table(['Pays', '|εX| + εZ', 'Diagnostic', 'Effet net'], [['A', '3,5', 'M-L vérifiée', '+2,5 %'], ['B', '1,2', 'M-L vérifiée', '+0,2 %'], ['C', '0,7', 'M-L <b>non</b> vérifiée', '−0,3 % : la dépréciation dégrade la balance']]) +
                          P('Pays A, appréciation de 1 % : effet prix favorable (+1 %), effet volume défavorable (−3,5 %) : la balance se dégrade de 2,5 % des exportations.')))
    S.append(dict(id='mac-s7', num='Exercice 7', ch='macro-3', mobiliser=['macro-2'], type='Exercice d\'application', source='D\'après MACRO_3-1 (PTINC)',
                  titre='Parité des taux d\'intérêt non couverte : où vont les capitaux ?',
                  enonce=P('Taux d\'intérêt en zone euro : i = 3 %. Taux américain : i* = 5 %. Taux de change aujourd\'hui : e = 0,90 € pour 1 $ ; taux anticipé dans un an : eᵃ = 0,882.') + ol(['Calculer le taux de dépréciation anticipé de l\'euro.', 'La PTINC est-elle vérifiée ? Y a-t-il des mouvements de capitaux ?', 'i* passe à 6 %. Que se passe-t-il pour les capitaux, la BG et le marché des changes ?', 'Quelles conséquences en change flexible ? En change fixe ?']),
                  pourquoi='Chapitre 3, section V. Les conséquences sont développées au chapitre 5.',
                  commentaire=ul(['êᵃ = (eᵃ − e)/e ; négatif = appréciation anticipée de l\'euro.', 'Comparer i à i* + êᵃ.']),
                  corrige=ol(['êᵃ = (0,882 − 0,90)/0,90 = <b>−2 %</b> : le marché anticipe une appréciation de l\'euro de 2 %.', 'i* + êᵃ = 5 − 2 = 3 % = i : la PTINC est <b>vérifiée</b>. Un placement aux États-Unis rapporte plus d\'intérêts mais fait perdre 2 % sur le change : aucun intérêt à bouger.',
                              'i* + êᵃ = 4 % > 3 % : <b>sorties de capitaux</b>, CFHAR > 0, BG < 0. Offre excédentaire d\'euros, demande excédentaire de dollars.',
                              'Change flexible : l\'euro se déprécie, TCR ↓, compétitivité ↑, CC ↑ (si M-L) : la production augmente. Change fixe : la BCE vend des dollars, ses réserves et la masse monétaire baissent, le taux d\'intérêt monte : récession.'])))
    # Modèle chiffré
    S.append(dict(id='mac-s8', num='Exercice 8', ch='macro-4', mobiliser=['macro-3', 'micro-0'], type='Exercice d\'application', source='Exercice construit sur le modèle de MACRO_R4',
                  titre='Un modèle IS-LM-PTINC chiffré : équilibre interne, BG et retour à l\'équilibre',
                  enonce=P('Petite économie ouverte, prix fixes (P = 1), chômage keynésien. C = 100 + 0,8(Y − T) ; I = 300 − 20i ; G = 200 ; T = 200 ; CC = 150 − 0,1Y (pour un TCR donné). Offre de monnaie M = 400 ; demande de monnaie L = 0,25Y − 50i. i et i* en %. i* = 2 %, êᵃ = 0.') +
                         ol(['Établir l\'équation d\'IS.', 'Établir l\'équation de LM.', 'Calculer l\'équilibre interne (Y, i). L\'économie est-elle sur la PTINC ? Signe de la BG ?', 'Change fixe : quelle masse monétaire la BCE laisse-t-elle finalement en circulation ? Quel est le nouveau Y ?', 'Change flexible : de combien la composante autonome du CC doit-elle augmenter (dépréciation) pour rejoindre la PTINC ? Quel est le nouveau Y ?']),
                  pourquoi='Chapitre 4 (IS, LM, PTINC, retour à l\'équilibre).',
                  commentaire=ul(['IS : écrire Y = C + I + G + CC et isoler Y.', 'LM : M = L(Y, i).', 'En change fixe, c\'est M qui s\'ajuste ; en change flexible, c\'est le CC (via le TCR) : IS bouge.']),
                  corrige=ol(['Y = 100 + 0,8Y − 160 + 300 − 20i + 200 + 150 − 0,1Y ⇒ 0,3Y = 590 − 20i ⇒ <b>Y = (590 − 20i)/0,3</b>.', '400 = 0,25Y − 50i ⇒ <b>i = 0,005Y − 8</b>.',
                              'On remplace : 0,3Y = 590 − 0,1Y + 160 ⇒ 0,4Y = 750 ⇒ <b>Y = 1 875</b> et i = 9,375 − 8 = <b>1,375 %</b>. i < i* = 2 % : l\'équilibre interne est <b>sous</b> la PTINC. Sorties de capitaux, <b>BG < 0</b>.',
                              'La BCE vend des devises et rachète des euros : M baisse jusqu\'à ce que i = 2 %. Sur IS : Y = (590 − 40)/0,3 ≈ <b>1 833,3</b>. Sur LM : M = 0,25 × 1 833,3 − 100 ≈ <b>358,3</b> (perte de réserves d\'environ 41,7). La production baisse : LM s\'est déplacée vers le haut.',
                              'L\'euro se déprécie : la composante autonome du CC augmente et IS se déplace à droite. Sur LM à i = 2 % : 2 = 0,005Y − 8 ⇒ <b>Y = 2 000</b>. Sur IS : 0,3 × 2 000 = 600 = A − 40 ⇒ A = 640, soit <b>+50</b> pour le CC autonome (de 150 à 200). La production augmente.'])))
    S.append(dict(id='mac-s9', num='Exercice 9', ch='macro-5', mobiliser=['macro-4'], type='Exercice d\'application', source='Exercice construit sur le modèle de MACRO_R5',
                  titre='Comparer les politiques dans le modèle chiffré (suite de l\'exercice 8)',
                  enonce=P('On part de l\'équilibre général E : Y = 2 000, i = i* = 2 %, avec IS : 0,3Y = 640 − 20i et LM : M = 0,25Y − 50i avec M = 400.') + ol(['L\'État augmente G de 30. Nouvel équilibre en change fixe ? Variation des réserves ?', 'Même politique en change flexible : nouvel équilibre ? Que devient le CC ?', 'La BCE augmente M de 20 par open market. Nouvel équilibre en change flexible ?', 'Même politique en change fixe ?', 'Conclure.']),
                  pourquoi='Chapitre 5, sections II et III.',
                  commentaire=ul(['Parfaite mobilité : à l\'équilibre final, i revient toujours à 2 %.', 'Change fixe : Y se lit sur IS ; change flexible : Y se lit sur LM.']),
                  corrige=ol(['IS : 0,3Y = 670 − 20i. À i = 2 % : Y = 630/0,3 = <b>2 100</b> (+100, le multiplicateur 1/0,3 joue en plein). M doit valoir 0,25 × 2 100 − 100 = 425 : la BCE a acheté des devises, <b>réserves +25</b>. Très efficace.',
                              'LM inchangée et i = 2 % ⇒ Y = (2 + 8)/0,005 = <b>2 000</b> : aucun effet. L\'euro s\'apprécie et la composante autonome du CC baisse de <b>30</b> : éviction totale par le taux de change.',
                              'LM : 420 = 0,25Y − 50i. À i = 2 % : Y = 520/0,25 = <b>2 080</b> (+80). Sur IS : 0,3 × 2 080 + 40 = 664 ⇒ le CC autonome augmente de 24 (dépréciation). Efficace.',
                              'i baisse, les capitaux sortent, la BCE vend 20 de devises et M revient à 400 : <b>Y = 2 000</b>, réserves −20. Inefficace.',
                              'Change fixe : seule la politique budgétaire marche. Change flexible : seule la politique monétaire marche. C\'est le résultat de Mundell-Fleming.'])))
    S.append(dict(id='mac-d1', num='Dissertation', ch='macro-5', mobiliser=['macro-2', 'macro-3', 'macro-4'], type='Sujet de dissertation', source='Sujet type construit sur MACRO_R5',
                  titre='« Dans une petite économie ouverte, le choix du régime de change détermine l\'efficacité des politiques économiques. » Discutez.',
                  enonce=P('Vous vous placerez dans le cadre d\'une petite économie ouverte à parfaite mobilité des capitaux, à court terme, en situation de chômage keynésien.'),
                  pourquoi='Chapitre 5 (résultats), chapitre 4 (outil IS-LM-PTINC), chapitres 2 et 3 (mécanismes du change, Marshall-Lerner).',
                  commentaire=ul(['Définir : régime de change, politique monétaire et budgétaire, parfaite mobilité des capitaux.', 'Chaque mécanisme doit être déroulé pas à pas et illustré par un graphique IS-LM-PTINC.', 'Ne pas oublier les limites : hypothèses du modèle, condition de Marshall-Lerner, courbe en J.']),
                  corrige=H3('Introduction') + P('Accroche : la crise du SME de 1992-1993. Définitions. Problématique : <i>pourquoi un même instrument peut-il être très efficace ou totalement inutile selon le régime de change ?</i>') +
                          H3('I. Avec des capitaux parfaitement mobiles, le régime de change décide de l\'instrument efficace') +
                          H4('A. En change flexible, la politique monétaire est très efficace et la politique budgétaire inefficace') + ul(['Ms ↑ ⇒ i < i* ⇒ sorties de capitaux ⇒ dépréciation ⇒ CC ↑ (si M-L) ⇒ IS → droite : double effet.', 'G ↑ ⇒ i > i* ⇒ entrées ⇒ appréciation ⇒ CC ↓ ⇒ IS revient : éviction par le change.']) +
                          H4('B. En change fixe, c\'est l\'inverse') + ul(['Ms ↑ ⇒ sorties ⇒ la BC vend des devises ⇒ Ms revient : inefficace et coûteux en réserves.', 'G ↑ ⇒ entrées ⇒ la BC achète des devises ⇒ Ms ↑ ⇒ LM → droite : très efficace.']) +
                          H3('II. Mais ce résultat dépend d\'hypothèses fortes et de contraintes') +
                          H4('A. Le triangle d\'incompatibilité et le risque de crise de change') + ul(['On ne peut avoir que deux sommets sur trois.', 'Un change fixe défendu contre les marchés épuise les réserves : dévaluation.', 'La hausse de i* est importée en change fixe (récession), amortie en change flexible.']) +
                          H4('B. Les limites du modèle') + ul(['Marshall-Lerner pas toujours vérifiée ; effet en J à court terme.', 'Prix fixes : à plus long terme, l\'inflation modifie le TCR (π − π*).', 'Mobilité imparfaite des capitaux, aversion au risque, grands pays qui influencent i*.']) +
                          H3('Conclusion') + P('Le régime de change fixe le « canal » par lequel les flux de capitaux neutralisent ou amplifient une politique. Ouverture : la zone euro, où la politique monétaire est commune et la politique budgétaire reste nationale.')))
    S.append(dict(id='mac-d2', num='Question de synthèse', ch='macro-1', mobiliser=['macro-3', 'macro-5'], type='Question de synthèse', source='Sujet type construit sur MACRO_R et MACRO_3-1',
                  titre='Un déficit courant persistant est-il un problème ?',
                  enonce=P('Vous mobiliserez les deux lectures du compte courant et la notion de position extérieure nette.'),
                  pourquoi='Chapitre 1 (CC = PNB − A = (S − I) + (T − G), PEN) ; chapitre 3 (compétitivité, Marshall-Lerner) ; chapitre 5 (politiques).',
                  commentaire=ul(['Un déficit courant n\'est pas forcément mauvais : tout dépend de ce qu\'il finance.', 'Pense à l\'exemple des États-Unis.']),
                  corrige=ul(['<b>Ce que dit un déficit</b> : le pays dépense plus qu\'il ne gagne (A > PNB) et son épargne nationale ne couvre pas son investissement. Il emprunte au RDM : entrées de capitaux, PEN en baisse.',
                              '<b>Pas forcément grave</b> : s\'il finance de l\'investissement productif (S − I < 0 parce que I est élevé), il prépare des revenus futurs. Les États-Unis gardent PNB > PIB malgré une PEN négative, car ils empruntent à bas taux et placent dans des actifs plus rentables.',
                              '<b>Problématique</b> s\'il finance la consommation ou un déficit public durable (déficits jumeaux) : la PEN devient de plus en plus négative, les revenus versés au RDM augmentent et le pays dépend de la confiance des prêteurs.',
                              '<b>Corriger le déficit</b> : baisser l\'absorption (coûteux en croissance et en emploi), regagner en compétitivité (dépréciation réelle efficace seulement si Marshall-Lerner est vérifiée, après une courbe en J ; désinflation compétitive).',
                              '<b>Responsabilité partagée</b> : si certains pays sont durablement en déficit, d\'autres sont durablement en excédent ; l\'ajustement ne devrait pas peser que sur les premiers.'])))
    return S


# ---------------------------------------------------------------- quiz
def Q(q, opts, ans=0, exp='', tag=None):
    d = dict(type='qcm', q=q, opts=opts, ans=ans, exp=exp)
    if tag:
        d['tag'] = tag
    return d


def VF(q, ans, exp):
    return dict(type='vf', q=q, ans=ans, exp=exp)


def quiz1():
    return [Q('Un étudiant chinois vit à Lyon depuis deux ans. Pour la balance des paiements française, il est…', ['résident', 'non-résident', 'résident seulement s\'il travaille', 'non pris en compte'], 0, 'Est résident celui qui vit sur le territoire depuis plus d\'un an.'),
            Q('Dans quel compte enregistre-t-on des dividendes reçus d\'une filiale américaine ?', ['Compte courant (revenus primaires)', 'Compte financier (IDE)', 'Compte de capital', 'Revenus secondaires'], 0, 'C\'est un revenu du capital.'),
            Q('La contribution de la France au budget européen est un…', ['revenu secondaire versé', 'revenu primaire versé', 'transfert en capital', 'investissement de portefeuille'], 0, 'Transfert courant sans contrepartie.'),
            Q('Un fonds américain achète 15 % du capital d\'une entreprise française pour la diriger durablement. C\'est…', ['un IDE entrant', 'un IDE sortant', 'un investissement de portefeuille', 'une variation des avoirs de réserve'], 0, 'Au moins 10 % et un but durable.'),
            Q('L\'achat d\'obligations françaises par des non-résidents est…', ['un investissement de portefeuille (engagements ↑)', 'un IDE', 'une exportation de services', 'un transfert en capital'], 0, 'Les obligations sont toujours des investissements de portefeuille.'),
            Q('Quelle est l\'équation fondamentale de la balance des paiements ?', ['CC + CK − CF + EO = 0', 'CC − CK + CF = 0', 'CC = CK + CF', 'BG = CC + CF'], 0, 'Avec CF = Δ avoirs − Δ engagements.', 'mécanisme'),
            Q('CC = −40, CK = 0, EO = 0. Que vaut CF ?', ['−40', '+40', '0', 'On ne peut pas savoir'], 0, 'CC + CK − CF + EO = 0 ⇒ CF = CC.', 'calcul'),
            Q('Un excédent courant correspond à…', ['une sortie de capitaux et une hausse de la richesse sur l\'étranger', 'une entrée de capitaux', 'une baisse des avoirs', 'une baisse de la PEN'], 0, 'Le pays prête au RDM : ses avoirs nets augmentent.', 'mécanisme'),
            VF('La balance des paiements est toujours équilibrée en raison de la partie double.', True, 'Chaque opération est enregistrée au CC et en contrepartie au CF.'),
            Q('La PEN d\'un pays est…', ['la différence entre ses avoirs et ses engagements envers le RDM à une date', 'le solde du compte courant d\'une année', 'le solde de la balance commerciale', 'le montant des réserves de change'], 0, 'C\'est un stock, le CF en est le flux.'),
            Q('Une PEN négative signifie que le pays…', ['est en endettement extérieur net', 'a une richesse extérieure nette', 'a un excédent courant', 'n\'a aucune réserve'], 0, 'Dettes > avoirs.'),
            Q('BG = CC + CK − CFHAR. Si EO = 0, la BG est égale à…', ['la variation des avoirs de réserve', 'la variation de la PEN', 'le compte financier', 'zéro'], 0, 'BG − Δ AR + EO = 0.', 'mécanisme'),
            Q('Les réserves de change de la banque centrale augmentent de 30 (EO = 0). La BG est…', ['excédentaire de 30', 'déficitaire de 30', 'nulle', 'indéterminée'], 0, 'BG = Δ AR.', 'calcul'),
            Q('PNB = 1 000 ; C + I + G = 1 050. Que vaut le compte courant ?', ['−50', '+50', '1 050', '0'], 0, 'CC = PNB − A.', 'calcul'),
            Q('CC = (S − I) + (T − G). Un déficit public non compensé par l\'épargne privée…', ['dégrade le compte courant', 'améliore le compte courant', 'n\'a aucun effet', 'augmente la PEN'], 0, 'Déficits jumeaux.', 'mécanisme'),
            VF('Un pays dont le PNB est supérieur au PIB reçoit plus de revenus du RDM qu\'il n\'en verse.', True, 'PNB = PIB + revenus nets du RDM.')]


def quiz2():
    return [Q('1 EUR = 0,8000 USD. Quelle est la cotation à l\'incertain ?', ['1 USD = 1,25 EUR', '1 USD = 0,80 EUR', '1 EUR = 1,25 USD', '1 USD = 0,20 EUR'], 0, '1/0,8 = 1,25.', 'calcul'),
            Q('L\'EUR/USD passe de 1,1250 à 1,1245. L\'euro…', ['s\'est déprécié de 5 PIP', 's\'est apprécié de 5 PIP', 's\'est déprécié de 0,5 PIP', 'est stable'], 0, 'La 4ᵉ décimale a baissé de 5.', 'calcul'),
            Q('Le cours auquel le public achète des euros à la banque est…', ['le cours de vente (offer)', 'le cours d\'achat (bid)', 'le cours moyen', 'la parité'], 0, 'La banque vend au cours le plus élevé.'),
            Q('Le spread est…', ['l\'écart entre cours de vente et cours d\'achat', 'l\'écart entre deux parités', 'la variation journalière du change', 'la quatrième décimale'], 0, 'C\'est la marge de l\'intermédiaire.'),
            Q('Une demande excédentaire d\'euros provoque, en change flexible…', ['une appréciation de l\'euro', 'une dépréciation de l\'euro', 'une dévaluation', 'une intervention de la BCE'], 0, 'Le prix monte quand la demande dépasse l\'offre.', 'mécanisme'),
            Q('Les exportations françaises vers les États-Unis augmentent (change flexible). Le dollar…', ['se déprécie face à l\'euro', 's\'apprécie face à l\'euro', 'ne bouge pas', 'est dévalué'], 0, 'Les Américains offrent des dollars pour obtenir des euros.', 'mécanisme'),
            Q('En change fixe, pour empêcher l\'appréciation de sa monnaie, la banque centrale…', ['achète des devises et crée de la monnaie nationale', 'vend des devises', 'relève ses taux', 'réduit la masse monétaire'], 0, 'Ses réserves et sa masse monétaire augmentent.', 'mécanisme'),
            Q('Quand ses réserves s\'épuisent en défendant sa monnaie, une banque centrale en change fixe doit…', ['dévaluer', 'réévaluer', 'créer des devises', 'augmenter sa masse monétaire'], 0, 'Elle ne peut plus soutenir la parité.'),
            VF('Une dépréciation et une dévaluation sont deux mots pour le même phénomène.', False, 'Dépréciation : par le marché (flexible) ; dévaluation : décision officielle (fixe).'),
            Q('En change fixe, une BG déficitaire entraîne…', ['une baisse des réserves et de la masse monétaire', 'une hausse des réserves', 'une appréciation de la monnaie', 'une baisse des taux d\'intérêt'], 0, 'La BC vend des devises et rachète sa monnaie.', 'mécanisme'),
            Q('En change fixe, pourquoi la baisse de la masse monétaire peut-elle provoquer une récession ?', ['Les taux montent, l\'investissement et la consommation baissent', 'Les prix augmentent', 'Les exportations explosent', 'Le taux de change se déprécie'], 0, 'En chômage keynésien, moins de demande = moins de production.', 'mécanisme'),
            Q('Quel régime correspond à la zone euro entre ses pays membres ?', ['Ancrage fixe dur (union monétaire)', 'Ancrage glissant', 'Change flexible', 'Change fixe avec bande'], 0, 'Il n\'y a plus de taux de change entre eux.'),
            VF('Le marché des changes est très concentré, avec environ 40 % des transactions à Londres.', True, 'Et environ 20 % à New York.')]


def quiz3():
    return [Q('Le taux de change réel (convention du cours) s\'écrit…', ['TCR = P/(e·P*)', 'TCR = e·P*/P', 'TCR = P*/P', 'TCR = e'], 0, 'Avec e le prix d\'une unité de devise en euros.'),
            Q('TCR = 1,2. La France est…', ['moins compétitive que le RDM', 'plus compétitive que le RDM', 'aussi compétitive', 'en excédent courant'], 0, 'Ses prix sont 20 % plus élevés une fois convertis.'),
            Q('Une hausse du TCR (convention du cours) est…', ['une appréciation réelle : perte de compétitivité', 'une dépréciation réelle', 'un gain de compétitivité', 'une dévaluation'], 0, 'Nos prix montent par rapport aux prix étrangers.'),
            Q('P = 110, P* = 100, e = 1. TCR ?', ['1,1', '0,91', '110', '1'], 0, '110/(1 × 100).', 'calcul'),
            Q('ε X/TCR = −1,5 et le TCR augmente de 2 %. Les exportations…', ['baissent de 3 %', 'augmentent de 3 %', 'baissent de 1,5 %', 'baissent de 0,75 %'], 0, 'X^ = −1,5 × 2.', 'calcul'),
            Q('La condition de Marshall-Lerner s\'écrit…', ['|εX| + εZ > 1', '|εX| + εZ < 1', 'εX = εZ', '|εX| − εZ > 0'], 0, 'Effet volume > effet prix.'),
            Q('εX = −0,4 et εZ = 0,3. Une dépréciation réelle…', ['dégrade la balance commerciale', 'l\'améliore', 'n\'a aucun effet', 'améliore les seules exportations nettes à long terme'], 0, '0,7 < 1 : l\'effet prix l\'emporte.', 'calcul'),
            Q('Lors d\'une dépréciation réelle, l\'effet prix…', ['renchérit les importations et dégrade la balance', 'augmente les exportations', 'réduit les importations en volume', 'améliore la balance'], 0, 'Chaque unité importée coûte plus cher.', 'mécanisme'),
            Q('Pourquoi la courbe en J ?', ['L\'effet prix est immédiat, l\'effet volume prend du temps', 'L\'effet volume est immédiat', 'Les prix sont flexibles', 'La banque centrale intervient'], 0, 'Contrats et habitudes changent lentement.', 'mécanisme'),
            Q('π = 4 %, π* = 2 %, e constant. Le TCR…', ['augmente d\'environ 2 % : perte de compétitivité', 'baisse de 2 %', 'est constant', 'augmente de 6 %'], 0, 'TCR^ ≈ π − π* − ê.', 'calcul'),
            Q('La désinflation compétitive consiste à…', ['avoir moins d\'inflation que ses partenaires pour faire baisser le TCR', 'dévaluer sa monnaie', 'augmenter les salaires', 'augmenter la masse monétaire'], 0, 'Gain de compétitivité sans dévaluation.'),
            Q('PTINC : i = 2 %, i* = 4 %, êᵃ = −2 %. Que se passe-t-il ?', ['Rien : la PTINC est vérifiée', 'Entrées de capitaux', 'Sorties de capitaux', 'Dévaluation'], 0, 'i* + êᵃ = 2 % = i.', 'calcul'),
            Q('i > i* + êᵃ entraîne…', ['des entrées de capitaux, CFHAR < 0, BG > 0', 'des sorties de capitaux, BG < 0', 'une dépréciation de la monnaie', 'une baisse des réserves en change fixe'], 0, 'Le rendement est meilleur chez nous.', 'mécanisme'),
            VF('Le taux de change effectif réel compare un pays à un ensemble de partenaires, avec une moyenne pondérée.', True, 'À la différence du TCR bilatéral.')]


def quiz4():
    return [Q('Quelle hypothèse n\'est PAS celle du modèle du cours ?', ['Prix parfaitement flexibles', 'Petit pays', 'Court terme', 'Parfaite mobilité des capitaux'], 0, 'Les prix et salaires sont rigides à court terme.'),
            Q('Le chômage keynésien est dû à…', ['une demande de biens insuffisante', 'un salaire réel trop élevé', 'une offre de travail trop faible', 'des prix trop flexibles'], 0, 'Les firmes subissent une contrainte de débouchés.'),
            Q('Le chômage classique est dû à…', ['un coût réel du travail trop élevé', 'une demande insuffisante', 'une masse monétaire trop faible', 'un excédent courant'], 0, 'w/P1 > w/P0 : offre de travail > demande.'),
            Q('La loi de Walras permet de…', ['ne pas étudier un des n marchés', 'calculer le multiplicateur', 'tracer la PTINC', 'déterminer le TCR'], 0, 'Si n − 1 marchés sont équilibrés, le dernier aussi.'),
            Q('La courbe IS représente l\'équilibre…', ['du marché des biens et services', 'du marché de la monnaie', 'de la balance globale', 'du marché du travail'], 0, 'Y = Yd.'),
            Q('IS est décroissante car…', ['une hausse de i réduit l\'investissement, donc la production', 'une hausse de Y fait monter i', 'les prix sont fixes', 'la BG est équilibrée'], 0, 'I dépend négativement de r.', 'mécanisme'),
            Q('Une baisse des impôts…', ['déplace IS vers la droite', 'déplace IS vers la gauche', 'déplace LM vers le bas', 'provoque un déplacement le long d\'IS'], 0, 'C ↑ puis effet multiplicateur.'),
            Q('Une appréciation réelle (TCR ↑, M-L vérifiée)…', ['déplace IS vers la gauche', 'déplace IS vers la droite', 'déplace LM', 'n\'a pas d\'effet'], 0, 'CC ↓ : la demande extérieure nette baisse.', 'mécanisme'),
            Q('LM est croissante car…', ['quand Y augmente, la demande de monnaie augmente et fait monter i', 'quand i augmente, l\'investissement baisse', 'la BC fixe i', 'les prix montent avec Y'], 0, 'Les firmes vendent des titres pour obtenir de la monnaie : cours ↓, i ↑.', 'mécanisme'),
            Q('Un open market expansionniste…', ['déplace LM vers le bas (droite)', 'déplace LM vers le haut', 'déplace IS', 'déplace la PTINC'], 0, 'Ms ↑ ⇒ i ↓ pour chaque Y.'),
            Q('En parfaite mobilité des capitaux, la PTINC est…', ['horizontale au niveau i* + êᵃ', 'verticale', 'croissante', 'décroissante'], 0, 'La BG n\'est équilibrée qu\'à ce taux.'),
            Q('Équilibre interne en A, au-dessus de la PTINC, change flexible. Que se passe-t-il ?', ['Appréciation, IS se déplace à gauche', 'Dépréciation, IS à droite', 'Réserves ↑, LM à droite', 'Réserves ↓, LM à gauche'], 0, 'Entrées de capitaux ⇒ la monnaie s\'apprécie.', 'mécanisme'),
            Q('Même situation (A au-dessus de la PTINC) en change fixe :', ['Réserves ↑, Ms ↑, LM se déplace à droite', 'Appréciation, IS à gauche', 'Réserves ↓, LM à gauche', 'Rien ne bouge'], 0, 'La BC achète les devises et crée de la monnaie.', 'mécanisme'),
            Q('Équation de Fisher :', ['i = r + πᵃ', 'r = i + πᵃ', 'i = r × πᵃ', 'i = πᵃ − r'], 0, 'Taux nominal = taux réel + inflation anticipée.'),
            VF('En change fixe, la masse monétaire peut varier sans décision d\'open market.', True, 'Elle varie avec les interventions sur le marché des changes, donc avec la BG.')]


def quiz5():
    return [Q('Change flexible, parfaite mobilité : une politique monétaire expansive est…', ['très efficace', 'inefficace', 'efficace seulement à long terme', 'impossible'], 0, 'La dépréciation ajoute un effet sur le CC.'),
            Q('Change flexible : une hausse de G est inefficace à cause…', ['de l\'appréciation de la monnaie qui réduit le CC', 'de la baisse des réserves', 'de la hausse des prix', 'de la baisse de la masse monétaire'], 0, 'Éviction par le taux de change.', 'mécanisme'),
            Q('Change fixe : une politique monétaire expansive…', ['est annulée par la vente de devises de la BC', 'est très efficace', 'provoque une appréciation', 'augmente les réserves'], 0, 'Sorties de capitaux ⇒ Ms revient à son niveau.', 'mécanisme'),
            Q('Change fixe : une hausse de G est très efficace car…', ['les entrées de capitaux obligent la BC à créer de la monnaie', 'la monnaie se déprécie', 'les taux montent durablement', 'les réserves baissent'], 0, 'LM se déplace à droite.', 'mécanisme'),
            Q('Dans le graphique d\'une politique monétaire expansive en change flexible, quelle courbe bouge en second ?', ['IS (vers la droite)', 'LM (vers le haut)', 'PTINC', 'Aucune'], 0, 'La dépréciation améliore le CC.'),
            Q('Le triangle d\'incompatibilité associe…', ['change fixe, mobilité des capitaux, politique monétaire autonome', 'inflation, chômage, croissance', 'CC, CK, CF', 'IS, LM, PTINC'], 0, 'On ne peut en avoir que deux.'),
            Q('Un pays veut un change fixe et une politique monétaire autonome. Il doit…', ['contrôler les mouvements de capitaux', 'laisser flotter sa monnaie', 'adopter une monnaie unique', 'supprimer sa banque centrale'], 0, 'C\'était le cas sous Bretton Woods.'),
            Q('Hausse de i* en change flexible :', ['dépréciation, CC ↑, Y ↑', 'appréciation, Y ↓', 'Ms ↓, Y ↓', 'aucun effet'], 0, 'IS se déplace vers la droite.', 'mécanisme'),
            Q('Hausse de i* en change fixe :', ['Ms ↓, i ↑, récession', 'dépréciation, Y ↑', 'réserves ↑', 'IS à droite'], 0, 'La hausse des taux est importée.', 'mécanisme'),
            Q('Une crise de change survient quand…', ['les sorties de capitaux épuisent les réserves défendant une parité', 'la monnaie s\'apprécie trop', 'la BG est excédentaire', 'le CC est excédentaire'], 0, 'La parité finit par céder : dévaluation.'),
            Q('Dans le modèle, à l\'équilibre final avec parfaite mobilité, le taux d\'intérêt national…', ['revient à i* + êᵃ', 'est toujours supérieur à i*', 'est nul', 'dépend de G'], 0, 'Sinon les flux de capitaux continuent.'),
            VF('En change fixe, la politique budgétaire provoque un excédent de BG et une hausse des réserves.', True, 'Les entrées de capitaux sont achetées par la BC.')]


# ---------------------------------------------------------------- matière
def matiere():
    c1, c2, c3, c4, c5 = ch1(), ch2(), ch3(), ch4(), ch5()
    chs = [
        dict(id='macro-1', num=1, titre='La balance des paiements', sous='Postes · partie double · PEN · balance globale · absorption et épargne',
             desc='Les quatre comptes, le double enregistrement, la position extérieure nette, la balance globale et les deux lectures du compte courant (PNB = A + CC ; CC = (S − I) + (T − G)).',
             tags=['Compte courant', 'Compte financier', 'PEN', 'BG', 'Absorption'], sources=[SRC[0]], cours=c1.html, notions=c1.notions, quiz=quiz1(),
             methode=ul(['Classer : échange de biens, services ou revenus → compte courant ; achat ou vente d\'actif → compte financier.', 'CF = Δ avoirs − Δ engagements ; EO se calcule en dernier.', 'BG = CC + CK − CFHAR = Δ AR (si EO = 0).', 'Interpréter un CC avec les deux lectures : absorption et épargne.']),
             fiches=[dict(q='Les 4 postes du compte courant ?', a='Biens, services, revenus primaires, revenus secondaires.'), dict(q='Équation fondamentale ?', a='CC + CK − CF + EO = 0 avec CF = Δ avoirs − Δ engagements.'),
                     dict(q='IDE ou portefeuille ?', a='IDE : au moins 10 % du capital, but durable. Portefeuille : moins de 10 %, obligations, placement.'), dict(q='BG = ?', a='CC + CK − CFHAR = Δ avoirs de réserve (si EO = 0).'),
                     dict(q='Deux lectures du CC ?', a='Absorption : CC = PNB − A. Épargne : CC = (S − I) + (T − G).'), dict(q='PEN ?', a='Avoirs − engagements envers le RDM à une date (stock).')],
             carte=dict(core='Balance des paiements', branches=[dict(t='Compte courant', items=['Biens (balance commerciale)', 'Services', 'Revenus primaires', 'Revenus secondaires']),
                                                                dict(t='Compte financier', items=['IDE (≥ 10 %)', 'Portefeuille', 'Dérivés', 'Autres investissements', 'Avoirs de réserve']),
                                                                dict(t='Équilibre', items=['CC + CK − CF + EO = 0', 'Partie double', 'CF = Δ avoirs − Δ engagements']), dict(t='PEN', items=['Avoirs − engagements', 'Stock ; CF = flux', 'Valorisation, change']),
                                                                dict(t='Balance globale', items=['BG = CC + CK − CFHAR', 'BG = Δ AR', 'Rôle de la banque centrale']), dict(t='Lectures du CC', items=['PNB = A + CC', 'CC = (S − I) + (T − G)', 'Déficits jumeaux'])],
                        schemas=[dict(t='Une exportation', steps=['X ↑ (crédit CC)', 'Paiement en devises', 'Avoirs ↑ (CF)', 'Sortie de capitaux', 'PEN ↑']),
                                 dict(t='Un déficit courant', steps=['A > PNB', 'Épargne nationale < I', 'Emprunt au RDM', 'Entrée de capitaux', 'PEN ↓'])]),
             liens=[dict(ch='compta-0', pourquoi='La balance des paiements applique la partie double de la comptabilité : chaque opération a une contrepartie, comme un débit a un crédit.'),
                    dict(ch='macro-2', pourquoi='Un déséquilibre de la BG se traduit par un déséquilibre du marché des changes.'), dict(ch='macro-3', pourquoi='Le compte courant dépend du TCR (compétitivité) ; les flux financiers dépendent de la PTINC.'),
                    dict(ch='macro-4', pourquoi='Le CC est la demande extérieure nette de la courbe IS ; la BG définit la droite PTINC.')]),
        dict(id='macro-2', num=2, titre='Le marché des changes et les régimes de change', sous='Taux de change · cotations · spread · change flexible · change fixe · réserves · dévaluation',
             desc='Le taux de change comme prix d\'une monnaie, le fonctionnement du marché des changes, l\'ajustement en change flexible et la défense d\'une parité en change fixe.',
             tags=['Change flexible', 'Change fixe', 'Cotation', 'Réserves', 'Dévaluation'], sources=[SRC[1]], cours=c2.html, notions=c2.notions, quiz=quiz2(),
             methode=ul(['Toujours écrire qui offre quelle monnaie et qui en demande.', 'Change flexible : en déduire l\'appréciation ou la dépréciation.', 'Change fixe : en déduire l\'intervention de la BC, la variation des réserves et de la masse monétaire.', 'Vérifier la convention de cotation (certain / incertain).']),
             fiches=[dict(q='Certain / incertain ?', a='Certain : 1 € = x $. Incertain : 1 $ = 1/x €.'), dict(q='Bid / offer ?', a='Bid : prix auquel la banque achète (le plus bas). Offer : prix auquel elle vend. Écart = spread.'),
                     dict(q='Change fixe et BG > 0 ?', a='La BC achète des devises : réserves ↑ et Ms ↑.'), dict(q='Dépréciation / dévaluation ?', a='Dépréciation par le marché (flexible) ; dévaluation par décision officielle (fixe).')],
             carte=dict(core='Marché des changes', branches=[dict(t='Taux de change', items=['Prix d\'une monnaie', 'Certain / incertain', '4 décimales, PIP', 'Bid, offer, spread']),
                                                              dict(t='Le marché', items=['18 × PIB mondial / jour', '24 h/24', 'Londres 40 %, New York 20 %', 'Commerce, spéculation, couverture, arbitrage']),
                                                              dict(t='Change flexible', items=['Pas d\'intervention', 'Offre excédentaire → dépréciation', 'Retour spontané à l\'équilibre']),
                                                              dict(t='Change fixe', items=['Parité officielle', 'Interventions avec les réserves', 'Ms varie avec la BG', 'Limites : réserves, récession']),
                                                              dict(t='Autres régimes', items=['Ancrage dur (UEM)', 'Ancrage glissant', 'Bande de fluctuation', 'Change libre'])],
                        schemas=[dict(t='BG > 0 en change fixe', steps=['Offre excédentaire de $', 'La BC achète les $', 'Réserves ↑, Ms ↑', 'i ↓', 'Sorties de capitaux', 'BG → 0']),
                                 dict(t='BG < 0 en change fixe', steps=['Offre excédentaire d\'€', 'La BC vend des $', 'Réserves ↓, Ms ↓', 'i ↑', 'Risque : réserves épuisées → dévaluation'])]),
             liens=[dict(ch='micro-0', pourquoi='Le marché des changes fonctionne comme le marché du chapitre 0 de micro : excès d\'offre → baisse du prix ; distinguer déplacement de la courbe et déplacement le long de la courbe.'),
                    dict(ch='macro-1', pourquoi='Les opérations de la balance des paiements créent l\'offre et la demande de devises ; les variations de réserves sont un poste du compte financier.'),
                    dict(ch='macro-3', pourquoi='Le taux de change nominal entre dans le TCR et dans la PTINC.'), dict(ch='macro-5', pourquoi='Le régime de change décide de l\'efficacité des politiques économiques.')]),
        dict(id='macro-3', num=3, titre='Taux de change réel, compétitivité et mouvements de capitaux', sous='TCR · élasticités · Marshall-Lerner · courbe en J · désinflation compétitive · PTINC',
             desc='La compétitivité-prix mesurée par le TCR, les effets volume et prix d\'une dépréciation, la condition de Marshall-Lerner, la courbe en J et la parité des taux d\'intérêt non couverte.',
             tags=['TCR', 'Marshall-Lerner', 'Courbe en J', 'PTINC'], sources=[SRC[2]], cours=c3.html, notions=c3.notions, quiz=quiz3(),
             methode=ul(['TCR = P/(e·P*) ; vérifier la convention.', 'Taux de croissance : X^ = εX × TCR^ ; Z^ = εZ × TCR^.', 'Marshall-Lerner : comparer |εX| + εZ à 1 ; effet net ≈ (somme − 1) × |TCR^|.', 'PTINC : comparer i et i* + êᵃ, en déduire le sens des capitaux puis la BG.']),
             fiches=[dict(q='TCR > 1 ?', a='Prix nationaux plus élevés que les prix étrangers convertis : moins compétitif.'), dict(q='Marshall-Lerner ?', a='|εX| + εZ > 1 : une dépréciation réelle améliore la balance.'),
                     dict(q='Courbe en J ?', a='Effet prix immédiat (dégradation), puis effet volume (amélioration).'), dict(q='PTINC ?', a='i = i* + êᵃ ; si i > i* + êᵃ, entrées de capitaux et BG > 0.'), dict(q='TCR^ ?', a='≈ π − π* − ê.')],
             carte=dict(core='Compétitivité et capitaux', branches=[dict(t='TCR', items=['P/(e·P*)', '> 1 : moins compétitif', 'TCER : moyenne pondérée']),
                                                                     dict(t='Élasticités', items=['εX < 0, εZ > 0', 'X^ = εX × TCR^']), dict(t='Dépréciation', items=['Effet volume (+)', 'Effet prix (−)', 'Marshall-Lerner : |εX| + εZ > 1', 'Courbe en J']),
                                                                     dict(t='Causes du TCR', items=['Inflation relative π − π*', 'Change nominal', 'Désinflation compétitive']), dict(t='PTINC', items=['i = i* + êᵃ', 'i > : entrées, BG > 0', 'i < : sorties, BG < 0'])],
                        schemas=[dict(t='Dépréciation réelle (M-L vérifiée)', steps=['TCR ↓', 'Effet prix : Z plus chères', 'Effet volume : X ↑, Z ↓', 'Balance ↓ puis ↑', 'Courbe en J']),
                                 dict(t='i > i* + êᵃ', steps=['Entrées de capitaux', 'CFHAR < 0', 'BG > 0', 'Demande excédentaire d\'€', 'Flexible : € ↑ ; fixe : réserves ↑'])]),
             liens=[dict(ch='micro-1', pourquoi='Les élasticités du commerce extérieur sont des élasticités-prix au sens du chapitre 1 de micro.'), dict(ch='macro-1', pourquoi='Le TCR agit sur le compte courant, la PTINC sur le compte financier.'),
                    dict(ch='macro-2', pourquoi='Le taux de change nominal e entre dans le TCR ; la PTINC explique les flux qui font bouger le marché des changes.'), dict(ch='macro-4', pourquoi='Le TCR déplace IS ; la PTINC devient la droite d\'équilibre de la BG.')]),
        dict(id='macro-4', num=4, titre='Le modèle IS-LM-PTINC (Mundell-Fleming) à court terme', sous='Hypothèses · chômage classique et keynésien · loi de Walras · IS · LM · PTINC · équilibre général',
             desc='Le modèle d\'une petite économie ouverte à prix fixes : marché du travail, courbes IS et LM, droite PTINC, équilibre général et retour à l\'équilibre selon le régime de change.',
             tags=['IS', 'LM', 'PTINC', 'Chômage keynésien', 'Équilibre général'], sources=[SRC[3]], cours=c4.html, notions=c4.notions, quiz=quiz4(),
             methode=ul(['Identifier ce qui déplace IS (G, T, Y*, optimisme, TCR) et ce qui déplace LM (Ms).', 'Repérer la position de A par rapport à la PTINC : au-dessus, BG > 0 ; en dessous, BG < 0.', 'Change flexible : le change bouge, donc IS ; change fixe : la masse monétaire bouge, donc LM.', 'Conclure sur Y et le chômage (chômage keynésien).']),
             fiches=[dict(q='Chômage keynésien ou classique ?', a='Keynésien : demande insuffisante. Classique : salaire réel trop élevé.'), dict(q='IS, LM, PTINC ?', a='IS : biens (décroissante). LM : monnaie (croissante). PTINC : BG (horizontale).'),
                     dict(q='Ce qui déplace IS ?', a='G, T, Y*, optimisme des firmes et des ménages, TCR. Une variation de i : mouvement le long.'), dict(q='Ce qui déplace LM ?', a='La masse monétaire (open market, ou BG en change fixe).'),
                     dict(q='A au-dessus de la PTINC ?', a='BG > 0. Flexible : appréciation, IS à gauche. Fixe : réserves ↑, Ms ↑, LM à droite.')],
             carte=dict(core='IS-LM-PTINC', branches=[dict(t='Hypothèses', items=['Petit pays', 'Court terme', 'Prix rigides', 'Mobilité parfaite']), dict(t='Travail', items=['Chômage classique', 'Chômage keynésien', 'L\'emploi suit la demande']),
                                                       dict(t='IS', items=['Y = C + I + G + CC', 'Décroissante', 'Multiplicateur']), dict(t='LM', items=['Ms/P = L(Y, i)', 'Croissante', 'Open market']),
                                                       dict(t='PTINC', items=['i = i* + êᵃ', 'Horizontale', 'Au-dessus : BG > 0']), dict(t='Équilibre', items=['Loi de Walras', 'IS ∩ LM ∩ PTINC', 'Flexible : IS bouge', 'Fixe : LM bouge'])],
                        schemas=[dict(t='G ↑ (multiplicateur)', steps=['Demande ↑', 'Production ↑', 'Embauches', 'Revenus ↑', 'Consommation ↑', 'Production ↑ encore']),
                                 dict(t='A sous la PTINC, change fixe', steps=['i < i*', 'Sorties de capitaux', 'BG < 0', 'La BC vend des devises', 'Ms ↓, i ↑', 'LM vers le haut'])]),
             liens=[dict(ch='micro-0', pourquoi='Loi de Walras, équilibre partiel et équilibre général prolongent l\'analyse des marchés de la micro.'), dict(ch='macro-1', pourquoi='Yd contient le CC ; la BG définit la PTINC.'),
                    dict(ch='macro-3', pourquoi='Le TCR déplace IS (si Marshall-Lerner) ; la PTINC vient de la comparaison des rendements.'), dict(ch='macro-5', pourquoi='Le modèle sert à analyser les politiques économiques.')]),
        dict(id='macro-5', num=5, titre='Politiques économiques en économie ouverte', sous='Politique monétaire · politique budgétaire · change fixe et flexible · triangle d\'incompatibilité · hausse de i*',
             desc='L\'efficacité comparée des politiques monétaire et budgétaire selon le régime de change, le triangle d\'incompatibilité, les crises de change et les effets d\'une hausse des taux étrangers.',
             tags=['Mundell-Fleming', 'Politique monétaire', 'Politique budgétaire', 'Triangle d\'incompatibilité'], sources=[SRC[4]], cours=c5.html, notions=c5.notions, quiz=quiz5(),
             methode=ul(['Partir de E sur la PTINC, déplacer la courbe touchée par la politique (LM pour la monétaire, IS pour la budgétaire).', 'Situer le nouveau point A par rapport à la PTINC : sens des capitaux et signe de la BG.', 'Appliquer la réaction du régime : change (IS bouge) ou masse monétaire (LM bouge).', 'Comparer Y final et Y initial : efficace ou non.']),
             fiches=[dict(q='Change flexible ?', a='Monétaire très efficace ; budgétaire inefficace (éviction par le change).'), dict(q='Change fixe ?', a='Monétaire inefficace (réserves) ; budgétaire très efficace (Ms ↑ induite).'),
                     dict(q='Triangle d\'incompatibilité ?', a='Change fixe, mobilité des capitaux, politique monétaire autonome : deux sur trois.'), dict(q='Hausse de i* ?', a='Flexible : dépréciation, Y ↑. Fixe : Ms ↓, récession.')],
             carte=dict(core='Politiques en économie ouverte', branches=[dict(t='Change flexible', items=['Monétaire : très efficace', 'Budgétaire : inefficace', 'Le change fait bouger IS']),
                                                                         dict(t='Change fixe', items=['Monétaire : inefficace', 'Budgétaire : très efficace', 'Ms fait bouger LM']),
                                                                         dict(t='Triangle', items=['Change fixe', 'Mobilité des capitaux', 'Politique monétaire autonome', '2 sur 3']),
                                                                         dict(t='Chocs', items=['i* ↑ : PTINC monte', 'Flexible : expansion', 'Fixe : récession importée']), dict(t='Crises de change', items=['Sorties de capitaux', 'Réserves épuisées', 'Dévaluation'])],
                        schemas=[dict(t='Politique monétaire, change flexible', steps=['Ms ↑', 'i < i*', 'Sorties de capitaux', 'Dépréciation', 'CC ↑ (M-L)', 'IS → droite', 'Y ↑↑']),
                                 dict(t='Politique budgétaire, change fixe', steps=['G ↑', 'i > i*', 'Entrées de capitaux', 'La BC achète des devises', 'Ms ↑', 'LM → droite', 'Y ↑↑']),
                                 dict(t='Politique budgétaire, change flexible', steps=['G ↑', 'i > i*', 'Entrées de capitaux', 'Appréciation', 'CC ↓', 'IS revient', 'Y inchangé'])]),
             liens=[dict(ch='macro-4', pourquoi='Le modèle IS-LM-PTINC est l\'outil d\'analyse.'), dict(ch='macro-2', pourquoi='Les interventions de la BC en change fixe et la dévaluation expliquent les crises de change.'),
                    dict(ch='macro-3', pourquoi='L\'effet de la dépréciation sur le CC suppose Marshall-Lerner.')]),
    ]
    G = [
        dict(id='mac-g1', ch='macro-1', titre='Les comptes de la balance des paiements', svg=plot_bp(), tags=['balance des paiements', 'compte courant', 'compte financier']),
        dict(id='mac-g2', ch='macro-1', titre='Deux lectures du compte courant : absorption et épargne', svg=plot_absorption(), tags=['absorption', 'épargne', 'compte courant']),
        dict(id='mac-g3', ch='macro-2', titre='Le marché des changes : hausse des exportations, change flexible et change fixe', svg=plot_changes(), tags=['change flexible', 'change fixe', 'réserves']),
        dict(id='mac-g4', ch='macro-3', titre='Effets d\'une dépréciation réelle de 1 % (exemple du cours)', svg=plot_ml(), tags=['Marshall-Lerner', 'effet prix', 'effet volume']),
        dict(id='mac-g5', ch='macro-3', titre='La courbe en J', svg=plot_j(), tags=['courbe en J', 'dépréciation']),
        dict(id='mac-g6', ch='macro-4', titre='Marché du travail : chômage classique et chômage keynésien', svg=plot_travail(), tags=['chômage', 'marché du travail']),
        dict(id='mac-g7', ch='macro-4', titre='Les courbes IS et LM et leurs déplacements', svg=plot_islm_base(), tags=['IS', 'LM']),
        dict(id='mac-g8', ch='macro-4', titre='L\'équilibre général IS-LM-PTINC', svg=plot_equilibre(), tags=['équilibre général', 'PTINC']),
        dict(id='mac-g9', ch='macro-4', titre='Retour à l\'équilibre quand A est au-dessus de la PTINC (BG > 0)', svg=plot_retour_haut(), tags=['retour à l\'équilibre', 'BG']),
        dict(id='mac-g10', ch='macro-4', titre='Retour à l\'équilibre quand A est en dessous de la PTINC (BG < 0)', svg=plot_retour_bas(), tags=['retour à l\'équilibre', 'BG']),
        dict(id='mac-g11', ch='macro-5', titre='Politique monétaire expansive : change flexible et change fixe', svg=plot_pol_mon(), tags=['politique monétaire', 'Mundell-Fleming']),
        dict(id='mac-g12', ch='macro-5', titre='Politique budgétaire expansive : change flexible et change fixe', svg=plot_pol_bud(), tags=['politique budgétaire', 'Mundell-Fleming']),
        dict(id='mac-g13', ch='macro-5', titre='Hausse du taux d\'intérêt étranger i*', svg=plot_istar(), tags=['taux étranger', 'choc extérieur']),
        dict(id='mac-g14', ch='macro-5', titre='Le triangle d\'incompatibilité', svg=plot_triangle(), tags=['triangle d\'incompatibilité', 'Mundell']),
    ]
    for g in G:
        g['exp'] = ''
    return dict(id='macro', nom='Macroéconomie', court='Macro', couleur='#f7a26a', sourcesResume='5 documents · notes de cours d\'économie ouverte (balance des paiements, change, Mundell-Fleming)', documents=DOCS, chapitres=chs,
                formules=[dict(titre='Balance des paiements', ch='macro-1', items=[dict(t='Équation fondamentale', f='CC + CK − CF + EO = 0'), dict(t='Compte financier', f='CF = Δ avoirs − Δ engagements'),
                                                                                 dict(t='Compte courant', f='CC = biens + services + revenus primaires + revenus secondaires'), dict(t='Balance globale', f='BG = CC + CK − CFHAR = Δ AR (si EO = 0)', note='CF = CFHAR + Δ AR'),
                                                                                 dict(t='PEN', f='PEN(t) = PEN(t−1) + CF + effets de valorisation'), dict(t='Absorption', f='PNB = A + CC ; A = C + I + G'), dict(t='Épargne', f='CC = (S − I) + (T − G)'),
                                                                                 dict(t='PNB', f='PNB = PIB + revenus primaires nets + revenus secondaires nets')]),
                          dict(titre='Change', ch='macro-2', items=[dict(t='Incertain', f='1 $ = 1/x € si 1 € = x $'), dict(t='Spread', f='Spread = cours de vente − cours d\'achat'), dict(t='PIP', f='1 PIP = 0,0001')]),
                          dict(titre='Compétitivité et capitaux', ch='macro-3', items=[dict(t='Taux de change réel', f='TCR = P/(e·P*)', note='e = prix d\'une unité de devise en euros'), dict(t='Variation du TCR', f='TCR^ ≈ π − π* − ê'),
                                                                                       dict(t='Élasticités', f='εX = (ΔX/ΔTCR)(TCR/X) < 0 ; εZ = (ΔZ/ΔTCR)(TCR/Z) > 0'), dict(t='Taux de croissance', f='X^ = εX × TCR^ ; Z^ = εZ × TCR^'),
                                                                                       dict(t='Balance en euros constants', f='BBS = X − Z/TCR'), dict(t='Marshall-Lerner', f='|εX| + εZ > 1', note='effet net ≈ (|εX| + εZ − 1) × |TCR^|'),
                                                                                       dict(t='PTINC', f='i = i* + êᵃ', note='exacte : 1 + i = (1 + i*)·eᵃ/e')]),
                          dict(titre='Modèle IS-LM-PTINC', ch='macro-4', items=[dict(t='Demande globale', f='Yd = C + I + G + CC'), dict(t='IS', f='Y = f(Y ; T ; G ; r ; Y* ; TCR ; DOF ; DOM)'), dict(t='LM', f='Ms/P = L(Y ; i)'),
                                                                                dict(t='Fisher', f='i = r + πᵃ'), dict(t='Équilibre général', f='IS ∩ LM ∩ PTINC'), dict(t='Salaire réel', f='w/P')])],
                auteurs=[dict(nom='Robert Mundell', kind='Auteur', dates='1932 – 2021', courant='Macroéconomie internationale (prix Nobel 1999)', source='compl', chapitres=['macro-4', 'macro-5'], oeuvres=['« Capital Mobility and Stabilization Policy under Fixed and Flexible Exchange Rates » (1963)', 'International Economics (1968)'],
                              idee='Modèle IS-LM-BP d\'une économie ouverte : avec des capitaux mobiles, l\'efficacité des politiques dépend du régime de change ; à l\'origine du triangle d\'incompatibilité et de la théorie des zones monétaires optimales.', phrase=''),
                         dict(nom='J. Marcus Fleming', kind='Auteur', dates='1911 – 1976', courant='Économiste du FMI', source='compl', chapitres=['macro-4', 'macro-5'], oeuvres=['« Domestic Financial Policies under Fixed and under Floating Exchange Rates » (1962)'],
                              idee='A établi, en même temps que Mundell, les résultats sur les politiques monétaire et budgétaire en change fixe et flexible : d\'où le nom de modèle de Mundell-Fleming.', phrase=''),
                         dict(nom='Alfred Marshall et Abba Lerner', kind='Auteurs', dates='1923 (Marshall) · 1944 (Lerner)', courant='Néoclassique', source='cours', chapitres=['macro-3'], oeuvres=['Money, Credit and Commerce (Marshall, 1923)', 'The Economics of Control (Lerner, 1944)'],
                              idee='Condition de Marshall-Lerner : une dépréciation réelle améliore la balance commerciale si la somme des valeurs absolues des élasticités-prix des exportations et des importations dépasse 1.', phrase=''),
                         dict(nom='John Maynard Keynes', kind='Auteur', dates='1883 – 1946', courant='Keynésianisme', source='cours', chapitres=['macro-4', 'macro-5'], oeuvres=['Théorie générale de l\'emploi, de l\'intérêt et de la monnaie (1936)'],
                              idee='La demande effective gouverne la production et l\'emploi : le chômage peut venir d\'une demande insuffisante (chômage keynésien) ; effet multiplicateur des dépenses.', phrase=''),
                         dict(nom='John Hicks (IS-LM)', kind='Auteur', dates='1904 – 1989', courant='Synthèse néoclassique', source='compl', chapitres=['macro-4'], oeuvres=['« Mr. Keynes and the "Classics" » (1937)'],
                              idee='A formalisé la pensée de Keynes dans le modèle IS-LM, que Mundell et Fleming ont ouvert sur l\'extérieur en ajoutant la balance des paiements.', phrase=''),
                         dict(nom='Léon Walras (loi de Walras)', kind='Auteur', dates='1834 – 1910', courant='Néoclassique (équilibre général)', source='cours', chapitres=['macro-4'], oeuvres=['Éléments d\'économie politique pure (1874)'],
                              idee='Loi de Walras : sur n marchés, si n − 1 sont à l\'équilibre, le dernier l\'est aussi ; elle permet de ne pas étudier le marché du travail à part.', phrase=''),
                         dict(nom='Irving Fisher', kind='Auteur', dates='1867 – 1947', courant='Néoclassique (monnaie)', source='cours', chapitres=['macro-4'], oeuvres=['The Theory of Interest (1930)'],
                              idee='Équation de Fisher : taux nominal = taux réel + inflation anticipée (i = r + πᵃ) ; avec πᵃ = 0, r = i.', phrase=''),
                         dict(nom='Fonds monétaire international (FMI)', kind='Institution', dates='Créé en 1944 (Bretton Woods)', courant='Coopération monétaire internationale', source='cours', chapitres=['macro-1', 'macro-2'], oeuvres=['Manuel de la balance des paiements et de la position extérieure globale (6ᵉ éd., BPM6)'],
                              idee='Fixe les normes internationales d\'établissement de la balance des paiements et de la position extérieure ; les contributions au FMI sont des revenus secondaires.', phrase=''),
                         dict(nom='Banque centrale européenne (BCE)', kind='Institution', dates='Créée en 1998', courant='Politique monétaire de la zone euro', source='cours', chapitres=['macro-2', 'macro-4', 'macro-5'],
                              idee='Seule à pouvoir créer ou détruire des euros ; conduit la politique monétaire (open market) et détient avec les banques centrales nationales les réserves de change de la zone euro.', phrase='')],
                reperes=[dict(date='1923-1944', t='Marshall puis Lerner formulent la condition sur les élasticités qui portera leurs noms.', src='cours'), dict(date='1936', t='Keynes, Théorie générale : la demande effective gouverne l\'emploi.', src='cours'),
                         dict(date='1937', t='Hicks formalise Keynes dans le modèle IS-LM.'), dict(date='1944', t='Accords de Bretton Woods : changes fixes autour du dollar, création du FMI.'),
                         dict(date='1962-1963', t='Fleming et Mundell ouvrent IS-LM sur l\'extérieur : modèle de Mundell-Fleming.'), dict(date='1971-1973', t='Fin de la convertibilité du dollar en or, passage aux changes flottants.'),
                         dict(date='1979', t='Création du Système monétaire européen (SME), changes fixes avec bandes de fluctuation.'), dict(date='1983', t='Tournant de la rigueur en France : stratégie de désinflation compétitive.'),
                         dict(date='1992-1993', t='Crise du SME : la livre et la lire quittent le système, les bandes sont élargies.'), dict(date='1999', t='Naissance de l\'euro et de la politique monétaire unique de la BCE.'),
                         dict(date='2009', t='6ᵉ édition du manuel de la balance des paiements du FMI (BPM6).')],
                methode=[dict(titre='Enregistrer une opération dans la balance des paiements', html=ol(['Identifier le résident et le non-résident.', 'Échange de biens, de services ou revenu ? → compte courant (crédit si on reçoit, débit si on paie).', 'Variation d\'un actif ou d\'une dette sur l\'étranger ? → compte financier (Δ avoirs ou Δ engagements).', 'Transfert en capital ? → compte de capital.', 'Contrôler : CC + CK − CF + EO = 0.']), piege='Mettre des dividendes dans le compte financier (ce sont des revenus) ou confondre IDE (≥ 10 %) et portefeuille.'),
                         dict(titre='Analyser un déséquilibre sur le marché des changes', html=ol(['Qui offre quelle monnaie ? Qui en demande ?', 'Change flexible : en déduire l\'appréciation ou la dépréciation et ses effets sur le TCR et le CC.', 'Change fixe : en déduire l\'intervention de la BC, la variation des réserves et de la masse monétaire, puis l\'effet sur les taux d\'intérêt.']), piege='Oublier la convention de cotation : e ↑ signifie une dépréciation de la monnaie nationale (incertain).'),
                         dict(titre='Calculer l\'effet d\'une dépréciation sur la balance', html=ol(['Calculer le TCR^ (exact ou π − π* − ê).', 'X^ = εX × TCR^ et Z^ = εZ × TCR^.', 'Vérifier Marshall-Lerner : |εX| + εZ > 1.', 'Effet net ≈ (|εX| + εZ − 1) × |TCR^| ; commenter la courbe en J.']), piege='Additionner les variations de X et Z sans retirer l\'effet prix.'),
                         dict(titre='Déroulé type d\'une analyse IS-LM-PTINC', html=ol(['Point de départ : E sur la PTINC.', 'Choc : quelle courbe se déplace ? (G, T, Y*, TCR → IS ; Ms → LM ; i* → PTINC)', 'Nouveau point A : au-dessus ou en dessous de la PTINC ? Sens des capitaux, signe de la BG.', 'Réaction du régime : change flexible → change → IS ; change fixe → réserves et Ms → LM.', 'Équilibre final : comparer Y et le chômage ; tracer le graphique.']), piege='Faire bouger LM en change flexible à cause de la BG : en flexible, la masse monétaire ne dépend pas de la BG.'),
                         dict(titre='Rédiger une dissertation de macro ouverte', html=ul(['Définir tous les termes (régime de change, mobilité des capitaux, politique monétaire, budgétaire).', 'Annoncer le cadre : petit pays, court terme, prix fixes, chômage keynésien.', 'Un mécanisme = une chaîne de flèches + un graphique.', 'Discuter les limites : Marshall-Lerner, courbe en J, mobilité imparfaite, prix flexibles à long terme.']), piege='Réciter les résultats (« la politique budgétaire est inefficace ») sans dérouler le mécanisme.')],
                courbes=G, sujets=sujets())
