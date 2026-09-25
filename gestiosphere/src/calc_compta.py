"""Calculs comptables utilisés pour les corrigés (vérifiés par tests_calc.py).

Convention de prorata : année commerciale de 360 jours, mois de 30 jours,
jours comptés du jour de mise en service (exclu) à la fin du mois, puis mois
entiers. C'est la convention qui reproduit les cumuls donnés par l'énoncé de
l'exercice 2 du poly (ex. 20/08/2012 → 130 jours).
"""
from lib import r2

COEF_DEG = [(4, 1.25), (6, 1.75), (99, 2.25)]  # (durée max, coefficient)


def jours_restants(j, m):
    """Jours de l'exercice (clôture 31/12) à partir d'une mise en service le j/m.
    Le 1er du mois compte le mois entier."""
    if j == 1:
        return (12 - m + 1) * 30
    return (30 - min(j, 30)) + (12 - m) * 30


def jours_ecoules(j, m):
    """Jours du 01/01 jusqu'à une date de sortie j/m (cession)."""
    return (m - 1) * 30 + (min(j, 30) - 1 if j > 1 else 0)


def coef_degressif(duree):
    for dmax, c in COEF_DEG:
        if duree <= dmax:
            return c


def plan_lineaire(base, duree, j, m, annee):
    """Plan linéaire au prorata temporis. Renvoie une liste de lignes
    (année, base, taux, annuité, cumul, VNC)."""
    taux = 1 / duree
    annuite = base * taux
    rows = []
    cumul = 0.0
    first = r2(annuite * jours_restants(j, m) / 360)
    a = annee
    rest = base
    k = 0
    while rest > 0.005:
        if k == 0:
            dot = first
        else:
            dot = r2(min(annuite, base - cumul))
        cumul = r2(cumul + dot)
        rest = r2(base - cumul)
        rows.append((a, base, taux, dot, cumul, rest))
        a += 1
        k += 1
    return rows


def plan_degressif(base, duree, mois_acq, annee):
    """Plan dégressif fiscal : prorata en mois depuis le 1er jour du mois
    d'acquisition ; passage au linéaire quand le taux linéaire sur la durée
    restante dépasse le taux dégressif. Lignes :
    (année, VNC début, taux lin. restant, taux dégressif, annuité, cumul, VNC fin)."""
    coef = coef_degressif(duree)
    td = (1 / duree) * coef
    mois = 12 - mois_acq + 1
    restant = duree * 12  # en mois
    vnc = base
    cumul = 0.0
    rows = []
    a = annee
    lineaire = None
    first = True
    while vnc > 0.005:
        m_ex = mois if first else min(12, restant)
        tl = 12 / restant if restant else 1  # taux linéaire annuel sur la durée restante
        if lineaire is None and not first and tl > td:
            lineaire = vnc / (restant / 12)
        if lineaire is not None:
            dot = r2(min(vnc, lineaire * m_ex / 12))
            if restant - m_ex <= 0:
                dot = r2(vnc)
            taux_aff = tl
        else:
            dot = r2(vnc * td * m_ex / 12)
            taux_aff = tl
        cumul = r2(cumul + dot)
        rows.append((a, vnc, taux_aff, td, dot, cumul, r2(vnc - dot)))
        vnc = r2(vnc - dot)
        restant -= m_ex
        a += 1
        first = False
    return rows, coef, td
