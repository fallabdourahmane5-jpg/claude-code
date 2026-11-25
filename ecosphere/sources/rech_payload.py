# -*- coding: utf-8 -*-
"""Monte la charge de données de la nouvelle recherche.

Ne sont embarquées que les sources inaccessibles au moteur à l'exécution :
les définitions moissonnées dans les cours, celles qui ont été rédigées, les
sections des chapitres, les formules, les faits datés, les dossiers
d'« Autour d'une notion », les idées de l'Atlas, les chiffres et les résumés.
Les notions de chapitre, les fiches, les auteurs, les sujets et les
visualisations sont déjà présents en mémoire dans l'application : le moteur
les lit directement, ce qui évite de les dupliquer.
"""
import json
import re
from collections import Counter

import rech_base as R
import rech_defs
import rech_defs2
import rech_defs3
import rech_defs4
import rech_defs5
import rech_defs6
import rech_defs7
import rech_defs8
import rech_defs9
import rech_fml2526
import rech_moisson

MAX_DEF = 520
MAX_TXT = 420


ART_TETE = re.compile(r"(?i)^(le|la|les|l['\u2019]|un|une)\s+")


def sans_article(t):
    """« Les externalités » devient « Externalité » : le titre doit nommer la
    notion, pas la phrase du cours. On ne retire l'article que si la forme
    obtenue désigne la même notion."""
    t = str(t or '').strip()
    n = ART_TETE.sub('', t).strip()
    if not n or len(n) < 3:
        return t
    if R.cle(n) != R.cle(t):
        return t
    return n[0].upper() + n[1:]


def majuscule(t):
    t = str(t or '').strip()
    return (t[0].upper() + t[1:]) if t else t


def court(s, n=MAX_TXT):
    s = ' '.join(str(s or '').split())
    return s if len(s) <= n else s[:n - 1].rsplit(' ', 1)[0] + '…'


# ----------------------------------------------------------------- définitions

REJET_DEF = {
    'armen alchian et harold demsetz', 'fiscalite', 'institutionnelle converge',
    'a retenir', 'simple', 'union europeenne', 'transparence de l information',
    'barriere a l entree generale', 'generale', 'biens', 'nomade',
}

# noms de lieux et de personnes : ils relèvent des faits et des auteurs,
# pas de la rubrique « Définitions »
LIEUX = {R.cle(x) for x in """europe chine france allemagne japon inde
bresil russie russe royaume-uni etats-unis afrique asie amerique oceanie
coree vietnam mexique canada italie espagne portugal pologne grece turquie
iran irak israel egypte nigeria kenya maroc algerie tunisie senegal
bangladesh pakistan indonesie thailande malaisie singapour taiwan australie
paris londres berlin pekin shanghai tokyo bruxelles washington californie
bavicre occident orient""".split()}
LIEUX |= {R.cle(x) for x in ['royaume uni', 'etats unis', 'coree du sud',
                             'amerique latine', 'union europeenne',
                             'hong kong', 'new york', 'moyen orient']}


def _noms_auteurs():
    C = R.corpus()
    s = set()
    for a in C['auteurs']:
        n = R.nz(a['name'])
        s.add(n)
        s.add(R.cle(n))
        p = n.split()
        if p:
            s.add(p[-1])
        if len(p) > 1:
            s.add(p[0] + ' ' + p[-1])
    return s


def _poids_chapitre(terme):
    """Nombre d'occurrences de l'expression dans chaque chapitre."""
    import socle
    global _TXT
    try:
        _TXT
    except NameError:
        _TXT = {k: R.nz(socle.TXT[k]) for k in R.ORDRE}
    # comptage sur les mots entiers : « PEN » ne doit pas être trouvé dans
    # « dépend » ni dans « pénétration »
    rx = re.compile(r'(?<![a-z0-9])' + re.escape(R.nz(terme)) + r'(?![a-z0-9])')
    return {k: len(rx.findall(_TXT[k])) for k in R.ORDRE}


def _premier_bloc(B, k, terme):
    """Premier bloc du chapitre qui porte l'expression, un encadré de
    définition ou un intitulé de section de préférence."""
    rx = re.compile(r'(?<![a-z0-9])' + re.escape(R.nz(terme)) + r'(?![a-z0-9])')
    sec, autre = -1, -1
    for i, x in enumerate(B[k]):
        if not rx.search(R.nz(x['x'])):
            continue
        if x['g'] == 'db':
            return i
        if x['g'] in ('h2', 'h3') and sec < 0:
            sec = i
        elif autre < 0 and len(x['x']) > 60:
            autre = i
    return sec if sec >= 0 else autre


def definitions(B, NC):
    M = rech_moisson.moisson(B, NC)
    out = {}
    for c, v in M.items():
        if c in REJET_DEF or ' s ' in c:
            continue
        pds = _poids_chapitre(v['t'])
        # tous les chapitres qui emploient l'expression, avec le premier bloc
        # qui la porte : le lien profond fonctionne partout, pas seulement là
        # où la définition a été trouvée
        lieux = dict(v['ch'])
        for k, n in pds.items():
            if n and k not in lieux:
                b0 = _premier_bloc(B, k, v['t'])
                if b0 >= 0:
                    lieux[k] = b0
        ou = sorted(lieux.items(), key=lambda z: (-pds.get(z[0], 0),
                                                  R.ORDRE.index(z[0])))[:6]
        out[c] = {'t': sans_article(majuscule(v['t'])),
                  'd': court(v['d'], MAX_DEF),
                  'o': v['o'], 'ou': [[k, b] for k, b in ou], 'al': []}
    # « Productivité globale des facteurs (PGF) » : la parenthèse devient
    # un alias et sort du titre
    for c in list(out):
        m = re.match(r'^(.{4,70}?)\s*\(([^)]{2,12})\)\s*$', out[c]['t'])
        if not m:
            continue
        base, sig = m.group(1).strip(), m.group(2).strip()
        cb = R.cle(base)
        if not cb or cb in out:
            continue
        v = out.pop(c)
        v['t'] = base
        v['al'] = sorted(set(v.get('al') or []) | {R.cle(sig), c})
        out[cb] = v

    # un sigle défini par le cours prend le libellé développé comme titre,
    # le sigle devenant un alias : « PEN » se trouve aussi bien sous
    # « position extérieure nette »
    for sig, dev in SYN.items():
        if sig not in out or not dev:
            continue
        plein = R.cle(dev[0])
        if plein in out:
            continue
        lib = LIBELLE.get(sig) or NC.get(plein)
        if not lib or len(lib) < len(out[sig]['t']):
            continue
        v = out.pop(sig)
        v['al'] = sorted(set(v.get('al') or []) | {sig} | {R.cle(x) for x in dev})
        v['t'] = lib
        out[plein] = v

    # les sigles et leurs développements se trouvent l'un par l'autre
    INV = {}
    for sig, dev in SYN.items():
        for x in dev:
            INV.setdefault(R.cle(x), set()).add(R.cle(sig))
    for c in out:
        sup = set(SYN.get(c, []) and [R.cle(x) for x in SYN[c]]) | INV.get(c, set())
        if sup:
            out[c]['al'] = sorted((set(out[c].get('al') or []) | sup) - {c})

    # définitions rédigées : elles prennent le pas sur la moisson
    SEC = sections_par_titre(B)
    REDIGEES = ([tuple(x) + ('',) for x in rech_defs.DEFS]
                + [tuple(x) for x in rech_defs2.DEFS]
                + [tuple(x) for x in rech_defs3.DEFS]
                + [tuple(x) for x in rech_defs4.DEFS]
                + [tuple(x) for x in rech_defs5.DEFS]
                + [tuple(x) for x in rech_defs6.DEFS]
                + [tuple(x) for x in rech_defs7.DEFS]
                + [tuple(x) for x in rech_defs8.DEFS]
                + [tuple(x) for x in rech_defs9.DEFS]
                + [tuple(x) for x in rech_defs9.REECRITES])
    for ligne in REDIGEES:
        terme, chs, anc, defi, al = ligne[0], ligne[1], ligne[2], ligne[3], ligne[4]
        dist = ligne[5] if len(ligne) > 5 else ''
        c = R.cle(terme)
        pds = _poids_chapitre(terme)
        lieux = {}
        for k in chs:
            b = SEC.get((k, R.cle(anc)), -1)
            if b < 0:
                b = _premier_bloc(B, k, terme)
            # un chapitre secondaire emploie souvent une autre formulation :
            # on cherche alors les alias avant de renoncer au renvoi
            if b < 0:
                for a in al:
                    b = _premier_bloc(B, k, a)
                    if b >= 0:
                        break
            lieux[k] = b
        # les autres chapitres où l'expression est employée
        for k, n in sorted(pds.items(), key=lambda z: -z[1]):
            if n and k not in lieux and len(lieux) < 7:
                b0 = _premier_bloc(B, k, terme)
                if b0 >= 0:
                    lieux[k] = b0
        # le chapitre qui traite le plus la notion arrive en tête : c'est lui
        # que le lien principal doit ouvrir
        # un chapitre dont le passage n'a pas été localisé ne donnerait
        # qu'un renvoi vide : on ne le garde pas, sauf s'il ne reste rien,
        # auquel cas le renvoi ouvre le chapitre à son début.
        lieux = {k: b for k, b in lieux.items() if b >= 0} or \
            {k: 0 for k in list(lieux)[:1]}
        ou = [[k, v] for k, v in sorted(
            lieux.items(), key=lambda z: (-pds.get(z[0], 0),
                                          R.ORDRE.index(z[0])))]
        out[c] = {'t': terme, 'd': court(defi, 1100), 'o': ['redigee'],
                  'ou': ou, 'al': sorted({R.cle(a) for a in al} - {c})}
        if dist:
            out[c]['x'] = court(dist, 480)

    # faux termes : la moisson a parfois pris pour une notion un intitulé de
    # lecture de graphique ou un fragment de phrase
    for c in rech_defs9.REJET:
        out.pop(c, None)

    # renvois manquants : une définition déjà écrite ailleurs s'applique à
    # l'un des deux derniers chapitres sans y conduire. On ajoute le renvoi
    # vers le passage pertinent plutôt que de créer un doublon.
    for c, k, anc in rech_defs9.RENVOIS:
        v = out.get(c)
        if not v or any(str(o[0]) == k for o in v['ou']):
            continue
        b = SEC.get((k, R.cle(anc)), -1)
        if b < 0:
            b = _premier_bloc(B, k, v['t'])
        if b >= 0:
            v['ou'].append([k, b])

    # formulations équivalentes : elles doivent conduire à l'entrée qui
    # existe déjà, et non à une entrée nouvelle
    for c, al in rech_defs9.ALIAS:
        v = out.get(c)
        if not v:
            continue
        v['al'] = sorted((set(v.get('al') or []) | {R.cle(a) for a in al}) - {c})

    # dernier filtrage : ni nom d'auteur, ni nom de lieu
    AUT = _noms_auteurs()
    for c in list(out):
        if 'redigee' in out[c]['o']:
            continue
        n = R.nz(out[c]['t'])
        if n in AUT or c in AUT or c in LIEUX or n in LIEUX:
            del out[c]
    return out


def sections_par_titre(B):
    d = {}
    for k in R.ORDRE:
        for i, x in enumerate(B[k]):
            if x['g'] in ('h2', 'h3', 'h4'):
                t = R.cle(R.titre_propre(x['x']))
                d.setdefault((k, t), i)
    return d


# -------------------------------------------------------------------- sections

def sections(B):
    out = []
    for k in R.ORDRE:
        for i, x in enumerate(B[k]):
            if x['g'] not in ('h2', 'h3'):
                continue
            t = R.titre_propre(x['x'])
            if len(t) < 4 or R.BRUIT.match(R.nz(t)):
                continue
            out.append({'c': k, 'b': i, 'n': 1 if x['g'] == 'h2' else 2,
                        't': court(t, 120),
                        'p': court(' › '.join(y for y in x['p'][:2] if y), 150)})
    return out


# -------------------------------------------------------------------- formules

RE_EGAL = re.compile(r'^[^=]{2,90}=[^=]{2,120}$')


def formules(B):
    out, vus = [], set()
    for k in R.ORDRE:
        v = B[k]
        for i, x in enumerate(v):
            txt = ' '.join(x['x'].split())
            est = False
            titre = ''
            if x['g'] == 'db' and x['dd'] and RE_EGAL.match(x['dd']):
                est, titre = True, x['dt']
            elif x['g'] in ('p', 'li', 'db') and RE_EGAL.match(txt):
                if re.search(r'[A-Za-zÀ-ÿ]{2,}', txt.split('=')[0]):
                    # un intitulé « Formule » juste au-dessus confirme
                    amont = [y for y in v[max(0, i - 3):i]
                             if y['g'] in ('h3', 'h4', 'h5')]
                    est = bool(amont and re.search(
                        r'(?i)formule|calcul|equation|taux|indice|mesure',
                        amont[-1]['x']))
                    titre = R.titre_propre(amont[-1]['x']) if amont else ''
            if not est or not (6 <= len(txt) <= 220):
                continue
            cl = R.nz(txt)
            if cl in vus:
                continue
            vus.add(cl)
            out.append({'c': k, 'b': i, 't': court(titre or txt, 90),
                        'd': court(txt, 220)})
    # chapitres 25 et 26 : les formules sont portées par des blocs
    # « formula » que l'énumération ne retient pas ; on les ajoute en
    # vérifiant que chacune se trouve bien au bloc indiqué.
    import json as _json
    _fml = _json.load(open('fml2526.json', encoding='utf-8'))
    _idx = {}
    for _k in _fml:
        for _x in _fml[_k]:
            _idx.setdefault((_k, _x['b']), []).append(R.nz(_x['f']))
    for k, b, t, f in rech_fml2526.FML:
        assert 0 <= b < len(B[k]), ('bloc hors bornes', k, b)
        n = R.nz(f)
        assert n in _idx.get((k, b), []) or n in R.nz(B[k][b]['x']), \
            ('formule absente du cours', k, b, f)
        if n in vus:
            continue
        vus.add(n)
        out.append({'c': k, 'b': b, 't': court(t, 90), 'd': court(f, 220)})
    return out


# ----------------------------------------------------------------------- faits

RE_AN = re.compile(r'\b(1[5-9]\d\d|20[0-5]\d)\b')


def faits(B):
    out, vus = [], set()
    for k in R.ORDRE:
        for i, x in enumerate(B[k]):
            if x['g'] not in ('p', 'li', 'db'):
                continue
            txt = ' '.join(x['x'].split())
            if not (55 <= len(txt) <= 500):
                continue
            ans = RE_AN.findall(txt)
            if not ans:
                continue
            cl = R.nz(txt)[:70]
            if cl in vus:
                continue
            vus.add(cl)
            out.append({'c': k, 'b': i, 'an': int(ans[0]),
                        'd': court(txt, 380),
                        'p': court(' › '.join(y for y in x['p'][:2] if y), 120)})
    return out


# ------------------------------------------------- dossiers, atlas, chiffres…

def dossiers():
    out = []
    for x in R.autour()['dossiers']:
        if x['etat'] == 'renvoi':
            continue
        out.append({'cle': x['cle'], 't': x['titre'], 'e': x['ens'],
                    'et': x['etat'],
                    'd': court(x.get('defi') or x.get('court') or '', MAX_DEF),
                    'ch': [c['k'] for c in (x['liens']['ch'] or [])[:4]]})
    return out


def atlas():
    out = []
    for c in R.atlas()['atlas']:
        for e in c['e']:
            out.append({'c': str(c['k']), 'n': e['n'], 't': e['ti'],
                        'd': court(e.get('af') or e.get('po') or '', MAX_DEF),
                        'no': [court(z, 60) for z in (e.get('no') or [])[:8]]})
    return out


def chiffres():
    out = []
    for k, v in R.chiffres().items():
        for x in v:
            out.append({'c': k, 'r': x.get('rang', 'prio'),
                        'v': court(x.get('v'), 90), 'u': court(x.get('u'), 110),
                        'z': court(x.get('z'), 60), 'p': court(x.get('p'), 60),
                        'd': court(x.get('d'), MAX_DEF),
                        'k': [court(z, 50) for z in (x.get('k') or [])[:8]]})
    return out


def resumes():
    out = []
    for k, v in R.resumes().items():
        idees = [court(i.get('t'), 120) for i in (v.get('idees') or [])]
        out.append({'c': k, 'q': court(v.get('q'), 320),
                    'd': court(v.get('ess') or v.get('min') or '', 700),
                    'i': idees[:14]})
    return out


# ----------------------------------------------- libellés développés des sigles
LIBELLE = {
    'pen': 'Position extérieure nette',
    'tms': 'Taux marginal de substitution',
    'pgf': 'Productivité globale des facteurs',
    'fbcf': 'Formation brute de capital fixe',
    'idh': 'Indice de développement humain',
    'ide': 'Investissement direct à l’étranger',
    'fmn': 'Firme multinationale',
    'cvm': 'Chaîne de valeur mondiale',
    'zes': 'Zone économique spéciale',
    'csu': 'Coût salarial unitaire',
    'dit': 'Division internationale du travail',
    'dipp': 'Division internationale des processus productifs',
    'ppa': 'Parité de pouvoir d’achat',
    'macf': 'Mécanisme d’ajustement carbone aux frontières',
    'apd': 'Aide publique au développement',
    'rnb': 'Revenu national brut',
    'scp': 'Structure – Comportement – Performance',
    'qe': 'Quantitative easing',
}

# ------------------------------------------------------------------ synonymes

SYN = {
    'pen': ['position exterieure nette'],
    'position exterieure nette': ['pen'],
    'pib': ['produit interieur brut'],
    'produit interieur brut': ['pib'],
    'rnb': ['revenu national brut'],
    'idh': ['indice de developpement humain'],
    'ide': ['investissement direct a l etranger',
            'investissements directs etrangers'],
    'fmn': ['firme multinationale', 'firmes multinationales'],
    'fbcf': ['formation brute de capital fixe'],
    'pgf': ['productivite globale des facteurs'],
    'omc': ['organisation mondiale du commerce'],
    'gatt': ['accord general sur les tarifs douaniers et le commerce'],
    'fmi': ['fonds monetaire international'],
    'bce': ['banque centrale europeenne'],
    'ppa': ['parite de pouvoir d achat'],
    'cvm': ['chaine de valeur mondiale'],
    'zes': ['zone economique speciale'],
    'macf': ['mecanisme d ajustement carbone aux frontieres'],
    'qe': ['quantitative easing', 'assouplissement quantitatif'],
    'csu': ['cout salarial unitaire'],
    'dit': ['division internationale du travail'],
    'dipp': ['division internationale des processus productifs'],
    'ira': ['inflation reduction act'],
    'hos': ['heckscher ohlin samuelson'],
    'scp': ['structure comportement performance'],
    'apd': ['aide publique au developpement'],
    'zlecaf': ['zone de libre echange continentale africaine'],
    'apu': ['administrations publiques'],
    'snf': ['societes non financieres'],
    'rdm': ['reste du monde'],
    'ci': ['consommations intermediaires'],
    'va': ['valeur ajoutee'],
    'tms': ['taux marginal de substitution'],
    'tva': ['taxe sur la valeur ajoutee'],
    'bri': ['belt and road initiative', 'nouvelles routes de la soie'],
}


# ------------------------------------------------------------------ programme

def batir():
    B = R.blocs()
    NC = rech_moisson.notions_connues(B)
    C = R.corpus()
    data = {
        'v': 218,
        'ch': {k: {'t': C['chapitres'][k]['title'], 'l': R.lib(k),
                   'n': len(B[k]),
                   'a': 2 if k in ('21', '22', '23', '24', '25', '26') else 1}
               for k in R.ORDRE},
        'def': definitions(B, NC),
        'sec': sections(B),
        'fml': formules(B),
        'fai': faits(B),
        'dos': dossiers(),
        'atl': atlas(),
        'chf': chiffres(),
        'res': resumes(),
        'syn': SYN,
    }
    return data


if __name__ == '__main__':
    d = batir()
    json.dump(d, open('recherche_payload.json', 'w'), ensure_ascii=False)
    brut = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    print('définitions embarquées : %d' % len(d['def']))
    print('  par origine          :',
          Counter(o for v in d['def'].values() for o in v['o']).most_common())
    for n, k in (('sections', 'sec'), ('formules', 'fml'), ('faits', 'fai'),
                 ('dossiers', 'dos'), ('idées Atlas', 'atl'),
                 ('chiffres', 'chf'), ('résumés', 'res')):
        print('%-22s : %d' % (n, len(d[k])))
    print('synonymes              : %d' % len(d['syn']))
    print('taille de la charge    : %.2f Mo' % (len(brut.encode()) / 1048576.0))
