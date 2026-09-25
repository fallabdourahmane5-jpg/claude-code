"""Outils de rédaction du contenu de Gestiosphère.

Chaque matière est un module Python qui construit un dictionnaire (voir build.py).
Les helpers ci-dessous produisent le HTML du cours avec les mêmes classes que
l'application, enregistrent les définitions au passage et vérifient les
écritures comptables (débit = crédit).
"""
from decimal import Decimal, ROUND_HALF_UP
import html as _html

E = _html.escape


def r2(x):
    """Arrondi comptable au centime (demi à l'écart de zéro)."""
    return float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def fr(x, dec=None):
    """Format français : 12 345,67 (décimales supprimées si entier)."""
    x = r2(x)
    neg = x < 0
    x = abs(x)
    if dec is None:
        dec = 0 if x == int(x) else 2
    s = f"{x:,.{dec}f}".replace(',', ' ').replace('.', ',')
    return ('−' if neg else '') + s


def eur(x, dec=None):
    return fr(x, dec) + ' €'


class Cours:
    """Accumule le HTML d'un chapitre et ses définitions."""

    def __init__(self):
        self.parts = []
        self.notions = []
        self._open = False

    # -- structure
    def sec(self, titre):
        self._close()
        self.parts.append(f'<div class="nb"><h2>{titre}</h2>')
        self._open = True
        return self

    def _close(self):
        if self._open:
            self.parts.append('</div>')
            self._open = False

    def h3(self, t):
        self.parts.append(f'<h3>{t}</h3>')
        return self

    def h4(self, t):
        self.parts.append(f'<h4>{t}</h4>')
        return self

    def p(self, t):
        self.parts.append(f'<p>{t}</p>')
        return self

    def ul(self, items, ordered=False):
        tag = 'ol' if ordered else 'ul'
        self.parts.append(f'<{tag}>' + ''.join(f'<li>{i}</li>' for i in items) + f'</{tag}>')
        return self

    def df(self, term, definition, show=True):
        """Définition : affichée dans le cours et ajoutée aux notions."""
        self.notions.append({'term': term, 'def': _plain(definition)})
        if show:
            self.parts.append(f'<div class="db"><div class="dt">{E(term)}</div><div class="dd">{definition}</div></div>')
        return self

    def note(self, t):
        self.parts.append(f'<div class="alertb"><p>💡 {t}</p></div>')
        return self

    def warn(self, t):
        self.parts.append(f'<div class="warn-box">⚠️ {t}</div>')
        return self

    def f(self, t):
        self.parts.append(f'<div class="formula">{t}</div>')
        return self

    def ex(self, titre, html):
        self.parts.append(f'<div class="ex-box"><div class="exh">{titre}</div>{html}</div>')
        return self

    # ---- blocs pédagogiques (style Écosphère) ----
    def intro(self, titre, texte, questions=()):
        """Ouverture du chapitre : de quoi on parle et les questions auxquelles il répond."""
        self._close()
        q = ''.join(f'<li>{x}</li>' for x in questions)
        self.parts.append(f'<div class="nb intro-ch"><h2>{titre}</h2><p>{texte}</p>' + (f'<div class="q-box"><div class="qh">Les questions du chapitre</div><ul>{q}</ul></div>' if q else '') + '</div>')
        return self

    def idee(self, t):
        self.parts.append(f'<div class="idee"><span class="ih">L\'idée</span>{t}</div>')
        return self

    def autrement(self, t):
        self.parts.append(f'<p class="adit"><b>Autrement dit :</b> {t}</p>')
        return self

    def pourquoi(self, q, r):
        self.parts.append(f'<div class="why"><div class="wq">❓ {q}</div><div class="wr">{r}</div></div>')
        return self

    def pas(self, titre, etapes, conclusion=''):
        li = ''.join(f'<li>{e}</li>' for e in etapes)
        self.parts.append(f'<div class="step-box"><div class="sh">🧮 {titre}</div><ol>{li}</ol>' + (f'<p class="sc">{conclusion}</p>' if conclusion else '') + '</div>')
        return self

    def retenir(self, items, titre='Ce qu\'il faut retenir'):
        li = ''.join(f'<li>{i}</li>' for i in items)
        self.parts.append(f'<div class="retenir"><div class="rh">✅ {titre}</div><ul>{li}</ul></div>')
        return self

    def transition(self, t):
        self.parts.append(f'<p class="trans">➜ {t}</p>')
        return self

    def synthese(self, items, titre='Ce qu\'il faut absolument retenir'):
        self._close()
        li = ''.join(f'<li>{i}</li>' for i in items)
        self.parts.append(f'<div class="nb synth"><h2>🎯 {titre}</h2><ul>{li}</ul></div>')
        return self

    def raw(self, h):
        self.parts.append(h)
        return self

    def tab(self, head, rows, num_cols=(), tot=False):
        self.parts.append(table(head, rows, num_cols, tot))
        return self

    def ecr(self, *entries):
        self.parts.append(journal(*entries))
        return self

    @property
    def html(self):
        self._close()
        return ''.join(self.parts)


def _plain(h):
    import re
    t = re.sub(r'<[^>]+>', '', h)
    return _html.unescape(re.sub(r'\s+', ' ', t)).strip()


def table(head, rows, num_cols=(), tot=False):
    """Tableau HTML. num_cols : index des colonnes numériques (alignées à droite).
    Les nombres (int/float) sont formatés automatiquement. tot=True : dernière ligne en gras."""
    def cell(v, i, tag):
        cls = ' class="n"' if i in num_cols else ''
        if isinstance(v, int) and not isinstance(v, bool) and 1900 <= v <= 2100:
            v = str(v)
        elif isinstance(v, (int, float)) and not isinstance(v, bool):
            v = fr(v)
        return f'<{tag}{cls}>{v}</{tag}>'
    h = '<tr>' + ''.join(cell(x, i, 'th') for i, x in enumerate(head)) + '</tr>'
    body = ''
    for k, r in enumerate(rows):
        cls = ' class="tot"' if tot and k == len(rows) - 1 else ''
        body += f'<tr{cls}>' + ''.join(cell(x, i, 'td') for i, x in enumerate(r)) + '</tr>'
    return f'<div class="table-wrap"><table class="dt">{h}{body}</table></div>'


class Ecriture:
    """Une écriture au journal. lignes : (sens 'D'/'C', compte, libellé, montant)."""

    def __init__(self, date, lignes, libelle=''):
        self.date = date
        self.lignes = [(s, str(c), l, r2(m)) for s, c, l, m in lignes]
        self.libelle = libelle
        d = r2(sum(m for s, _, _, m in self.lignes if s == 'D'))
        c = r2(sum(m for s, _, _, m in self.lignes if s == 'C'))
        if abs(d - c) > 0.005:
            raise ValueError(f'Écriture déséquilibrée ({date} {libelle}) : D={d} C={c}')
        for s, _, _, m in self.lignes:
            if s not in 'DC' or m <= 0:
                raise ValueError(f'Ligne invalide dans {date} {libelle}')
        self.total = d


def journal(*entries):
    rows = ''
    for e in entries:
        rows += f'<tr class="dt2"><td colspan="5">— {E(e.date)} —</td></tr>'
        for s, cpt, lib, m in sorted(e.lignes, key=lambda x: x[0] != 'D'):
            if s == 'D':
                rows += f'<tr><td class="cd">{cpt}</td><td class="cc2"></td><td class="lib">{lib}</td><td class="m">{fr(m, 2)}</td><td class="m"></td></tr>'
            else:
                rows += f'<tr><td class="cd"></td><td class="cc2">{cpt}</td><td class="lib cr">{lib}</td><td class="m"></td><td class="m">{fr(m, 2)}</td></tr>'
        if e.libelle:
            rows += f'<tr class="lbl"><td></td><td></td><td colspan="3">{E(e.libelle)}</td></tr>'
    return ('<div class="jrw"><table class="jr"><tr class="dt2"><td>Débit</td><td>Crédit</td><td>Libellé</td>'
            '<td>Montant débit</td><td>Montant crédit</td></tr>' + rows + '</table></div>')


def E_(date, lignes, libelle=''):
    return Ecriture(date, lignes, libelle)


def ol(items):
    return '<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def P(t):
    return f'<p>{t}</p>'


def H3(t):
    return f'<h3>{t}</h3>'


def H4(t):
    return f'<h4>{t}</h4>'


def NOTE(t):
    return f'<div class="alertb"><p>💡 {t}</p></div>'


def WARN(t):
    return f'<div class="warn-box">⚠️ {t}</div>'


def FORM(t):
    return f'<div class="formula">{t}</div>'
