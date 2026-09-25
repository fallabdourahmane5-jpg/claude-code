"""Petites fonctions de dessin SVG (thème sombre de l'application)."""
from lib import E

W, H = 520, 360
AX = '#8890a8'
TXT = '#c4c9d8'
COL = ['#7c6af7', '#f7a26a', '#6af7c4', '#f7e66a', '#f76ab4', '#6aa8f7']


class Plot:
    """Repère cartésien : coordonnées « métier » (x, y) → pixels."""

    def __init__(self, xmax, ymax, xlabel='', ylabel='', w=W, h=H, xmin=0, ymin=0, pad=(50, 20, 24, 44)):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.w, self.h = w, h
        self.l, self.r, self.t, self.b = pad
        self.el = []
        self.xlabel, self.ylabel = xlabel, ylabel

    def X(self, x):
        return self.l + (x - self.xmin) / (self.xmax - self.xmin) * (self.w - self.l - self.r)

    def Y(self, y):
        return self.h - self.b - (y - self.ymin) / (self.ymax - self.ymin) * (self.h - self.t - self.b)

    def axes(self, xticks=(), yticks=(), fmt=lambda v: str(v), xfmt=None):
        xfmt = xfmt or fmt
        x0, y0 = self.X(self.xmin), self.Y(self.ymin)
        self.el.append(f'<line x1="{x0}" y1="{y0}" x2="{self.w - self.r + 6}" y2="{y0}" stroke="{AX}" stroke-width="1.4" marker-end="url(#ar)"/>')
        self.el.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{self.t - 6}" stroke="{AX}" stroke-width="1.4" marker-end="url(#ar)"/>')
        for v in xticks:
            self.el.append(f'<text x="{self.X(v):.1f}" y="{y0 + 16}" fill="{AX}" font-size="10" text-anchor="middle">{E(xfmt(v))}</text>')
        for v in yticks:
            self.el.append(f'<text x="{x0 - 6}" y="{self.Y(v) + 3:.1f}" fill="{AX}" font-size="10" text-anchor="end">{E(fmt(v))}</text>')
            self.el.append(f'<line x1="{x0}" y1="{self.Y(v):.1f}" x2="{self.w - self.r}" y2="{self.Y(v):.1f}" stroke="#242d42" stroke-width="0.6"/>')
        if self.xlabel:
            self.el.append(f'<text x="{self.w - self.r}" y="{y0 + 32}" fill="{TXT}" font-size="11" text-anchor="end">{E(self.xlabel)}</text>')
        if self.ylabel:
            self.el.append(f'<text x="{x0 + 6}" y="{self.t - 8}" fill="{TXT}" font-size="11">{E(self.ylabel)}</text>')
        return self

    def curve(self, pts, color=COL[0], width=2.2, dash=None, label=None, lpos=None, anchor='start'):
        d = ' '.join(f'{"M" if i == 0 else "L"}{self.X(x):.1f},{self.Y(y):.1f}' for i, (x, y) in enumerate(pts))
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} stroke-linejoin="round" stroke-linecap="round"/>')
        if label:
            x, y = lpos if lpos else pts[-1]
            self.el.append(f'<text x="{self.X(x) + 4:.1f}" y="{self.Y(y) - 4:.1f}" fill="{color}" font-size="11" font-weight="700" text-anchor="{anchor}">{E(label)}</text>')
        return self

    def fn(self, f, x0, x1, n=120, **kw):
        pts = []
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n
            try:
                y = f(x)
            except ZeroDivisionError:
                continue
            if y is None or y != y:
                continue
            if self.ymin - (self.ymax - self.ymin) * 0.02 <= y <= self.ymax * 1.02:
                pts.append((x, y))
        return self.curve(pts, **kw)

    def point(self, x, y, color='#e8eaf2', label=None, dx=6, dy=-6, r=4, anchor='start'):
        self.el.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" fill="{color}"/>')
        if label:
            self.el.append(f'<text x="{self.X(x) + dx:.1f}" y="{self.Y(y) + dy:.1f}" fill="{color}" font-size="11" font-weight="600" text-anchor="{anchor}">{E(label)}</text>')
        return self

    def dashes(self, x, y, color='#4d5874', xl=None, yl=None):
        self.el.append(f'<path d="M{self.X(x):.1f},{self.Y(self.ymin):.1f} L{self.X(x):.1f},{self.Y(y):.1f} L{self.X(self.xmin):.1f},{self.Y(y):.1f}" fill="none" stroke="{color}" stroke-dasharray="4 4"/>')
        if xl:
            self.el.append(f'<text x="{self.X(x):.1f}" y="{self.Y(self.ymin) + 16:.1f}" fill="{TXT}" font-size="10.5" text-anchor="middle">{E(xl)}</text>')
        if yl:
            self.el.append(f'<text x="{self.X(self.xmin) - 6:.1f}" y="{self.Y(y) + 3:.1f}" fill="{TXT}" font-size="10.5" text-anchor="end">{E(yl)}</text>')
        return self

    def text(self, x, y, t, color=TXT, size=11, anchor='start', weight=400):
        self.el.append(f'<text x="{self.X(x):.1f}" y="{self.Y(y):.1f}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{E(t)}</text>')
        return self

    def arrow(self, x1, y1, x2, y2, color='#f7e66a'):
        self.el.append(f'<line x1="{self.X(x1):.1f}" y1="{self.Y(y1):.1f}" x2="{self.X(x2):.1f}" y2="{self.Y(y2):.1f}" stroke="{color}" stroke-width="1.6" marker-end="url(#ar2)"/>')
        return self

    def area(self, pts, color='#7c6af7', op=0.15):
        d = ' '.join(f'{"M" if i == 0 else "L"}{self.X(x):.1f},{self.Y(y):.1f}' for i, (x, y) in enumerate(pts)) + ' Z'
        self.el.append(f'<path d="{d}" fill="{color}" fill-opacity="{op}" stroke="none"/>')
        return self

    def bars(self, data, color=COL[0], width=0.35, offset=0.0, labels=True, fmt=lambda v: str(v)):
        for x, v in data:
            x0 = self.X(x - width / 2 + offset)
            x1 = self.X(x + width / 2 + offset)
            y0, y1 = self.Y(0), self.Y(v)
            self.el.append(f'<rect x="{x0:.1f}" y="{y1:.1f}" width="{x1 - x0:.1f}" height="{y0 - y1:.1f}" fill="{color}" rx="2"/>')
            if labels:
                self.el.append(f'<text x="{(x0 + x1) / 2:.1f}" y="{y1 - 4:.1f}" fill="{color}" font-size="9" text-anchor="middle">{E(fmt(v))}</text>')
        return self

    def legend(self, items, x=None, y=None):
        x = x if x is not None else self.l + 14
        y = y if y is not None else self.t + 8
        for i, (c, t) in enumerate(items):
            self.el.append(f'<rect x="{x}" y="{y + i * 17}" width="12" height="4" fill="{c}" rx="1"/>')
            self.el.append(f'<text x="{x + 18}" y="{y + i * 17 + 6}" fill="{TXT}" font-size="10.5">{E(t)}</text>')
        return self

    def svg(self):
        defs = ('<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="#8890a8"/></marker>'
                '<marker id="ar2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f7e66a"/></marker></defs>')
        return f'<svg viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans, sans-serif">{defs}{"".join(self.el)}</svg>'


def boxes(w, h, items, arrows=()):
    """Schéma de boîtes : items = [(x, y, w, h, titre, lignes, couleur)] ; arrows = [(x1,y1,x2,y2,label)]."""
    el = []
    for x, y, bw, bh, t, lines, c in items:
        el.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="#1a2033" stroke="{c}" stroke-width="1.5"/>')
        el.append(f'<text x="{x + bw / 2}" y="{y + 20}" fill="{c}" font-size="12.5" font-weight="700" text-anchor="middle">{E(t)}</text>')
        for i, l in enumerate(lines):
            el.append(f'<text x="{x + bw / 2}" y="{y + 38 + i * 15}" fill="{TXT}" font-size="10.5" text-anchor="middle">{E(l)}</text>')
    for x1, y1, x2, y2, lab in arrows:
        el.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#f7e66a" stroke-width="1.6" marker-end="url(#ar2)"/>')
        if lab:
            el.append(f'<text x="{(x1 + x2) / 2 + 4}" y="{(y1 + y2) / 2 - 4}" fill="#f7e66a" font-size="10">{E(lab)}</text>')
    defs = '<defs><marker id="ar2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f7e66a"/></marker></defs>'
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans, sans-serif">{defs}{"".join(el)}</svg>'


def matrix(w, h, cells, xlabel, ylabel, xl=('', ''), yl=('', ''), title_cols=None):
    """Matrice 2×2 (ou n×m) : cells = [[(titre, sous-titre, couleur)...] ligne du haut d'abord]."""
    rows, cols = len(cells), len(cells[0])
    L, T, R, B = 70, 20, 20, 50
    cw, chh = (w - L - R) / cols, (h - T - B) / rows
    el = []
    for i, row in enumerate(cells):
        for j, (t, s, c) in enumerate(row):
            x, y = L + j * cw, T + i * chh
            el.append(f'<rect x="{x + 3:.1f}" y="{y + 3:.1f}" width="{cw - 6:.1f}" height="{chh - 6:.1f}" rx="10" fill="{c}" fill-opacity=".14" stroke="{c}"/>')
            el.append(f'<text x="{x + cw / 2:.1f}" y="{y + chh / 2 - 4:.1f}" fill="{c}" font-size="14" font-weight="700" text-anchor="middle">{E(t)}</text>')
            for k, line in enumerate(s.split('\n')):
                el.append(f'<text x="{x + cw / 2:.1f}" y="{y + chh / 2 + 14 + k * 13:.1f}" fill="{TXT}" font-size="10" text-anchor="middle">{E(line)}</text>')
    el.append(f'<text x="{L + (w - L - R) / 2}" y="{h - 12}" fill="{TXT}" font-size="11.5" text-anchor="middle" font-weight="600">{E(xlabel)}</text>')
    el.append(f'<text x="{L - 14}" y="{T + (h - T - B) / 2}" fill="{TXT}" font-size="11.5" text-anchor="middle" font-weight="600" transform="rotate(-90 {L - 14} {T + (h - T - B) / 2})">{E(ylabel)}</text>')
    el.append(f'<text x="{L + 4}" y="{h - 30}" fill="{AX}" font-size="10">{E(xl[0])}</text><text x="{w - R - 4}" y="{h - 30}" fill="{AX}" font-size="10" text-anchor="end">{E(xl[1])}</text>')
    el.append(f'<text x="{L - 30}" y="{h - B - 4}" fill="{AX}" font-size="10" text-anchor="middle">{E(yl[0])}</text><text x="{L - 30}" y="{T + 12}" fill="{AX}" font-size="10" text-anchor="middle">{E(yl[1])}</text>')
    if title_cols:
        for j, t in enumerate(title_cols):
            el.append(f'<text x="{L + j * cw + cw / 2:.1f}" y="{h - 30}" fill="{AX}" font-size="10" text-anchor="middle">{E(t)}</text>')
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans, sans-serif">{"".join(el)}</svg>'
