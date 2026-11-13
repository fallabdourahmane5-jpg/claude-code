# -*- coding: utf-8 -*-
"""Audit des notions par familles, chapitre par chapitre.

Le principe : une notion du programme se présente presque toujours comme un
nom suivi d'un qualificatif — « capital humain », « capital naturel », « taux
de change réel », « protectionnisme éducateur ». On relève donc dans le texte
des cours, pour chaque mot-tête déjà connu comme notion, toutes les
expressions de cette forme, puis on confronte la liste à ce qui possède
réellement une définition autonome dans ÉcoSphère.

Sortie : audit_familles.json — pour chaque famille, les expressions trouvées
dans les cours, leur nombre d'occurrences, les chapitres concernés, et
l'existence ou non d'une définition.
"""
import json
import re
import unicodedata
from collections import Counter, defaultdict

import rech_base as R
import socle

# ------------------------------------------------------------------- outillage

VIDE = set("""de du des la le les l un une et ou a au aux en dans par pour sur
ce cette ces son sa ses leur leurs il elle on qui que quoi dont est sont etre
avoir plus moins tres tout tous toute toutes non pas ne comme donc alors meme
autre autres entre vers chez sans sous apres avant lorsque puisque parce ainsi
aussi mais car si selon peut peuvent doit doivent fait faire cours notion
document lecture graphique schema exemple idee cle retenir remarque donc or
cela elles ils tant plutot y a ont eu ete soit ni"""
            .split())

# qualificatifs vides : « capital de ce type » n'est pas une notion
QUAL_VIDE = set("""ce cette ces cet celui celle ceux celles il elle on nous
vous ils elles le la les un une des du de leur leurs son sa ses mon ma mes
notre nos votre vos tout toute tous toutes meme memes autre autres tel telle
plus moins tres bien mal donc ainsi alors aussi encore deja ici la lorsque
quand si que qui dont ou et mais car or ne pas point jamais toujours souvent
parfois peut peuvent doit doivent est sont etait etaient sera seront a ont eu
ete etre avoir fait faire dit dire va vont par pour dans sur sous avec sans
chez vers entre apres avant depuis pendant au aux en y il ya"""
             .split())

RE_MOT = re.compile(r"[a-z0-9àâçéèêëîïôûùüÿ']+")


def mots_nz(t):
    return RE_MOT.findall(R.nz(t))


def defs_existantes():
    """Toutes les clés qui possèdent déjà une définition autonome."""
    P = json.load(open('recherche_payload.json'))
    C = R.corpus()
    d = {}

    def pose(t, src, defi=''):
        c = R.cle(t)
        if not c or len(c) < 3:
            return
        x = d.setdefault(c, {'t': t, 'src': set(), 'd': defi})
        x['src'].add(src)
        if len(defi) > len(x['d']):
            x['d'] = defi
        if len(t) < len(x['t']):
            x['t'] = t

    for c, v in P['def'].items():
        pose(v['t'], 'definition', v['d'])
        for a in (v.get('al') or []):
            pose(a, 'alias', v['d'])
    for k in R.ORDRE:
        for n in C['chapitres'][k]['notions']:
            if n['t'] and n['d']:
                pose(n['t'], 'notion-chapitre', n['d'])
    for f in R.fiches():
        if f.get('term') and f.get('def') and f.get('type') in (
                'definition', 'définition', 'notion-clé', 'notion', 'formule'):
            t = re.sub(r"(?i)^(?:définis|definis|que faut-il retenir de|"
                       r"quel concept correspond à cette (?:définition|idée)|"
                       r"quel auteur associer à l['’]idée suivante)\s*:?\s*",
                       '', f['term']).strip(' ?')
            if len(t) > 2:
                pose(t, 'fiche', f['def'])
    for x in R.autour()['dossiers']:
        if x['etat'] == 'redige':
            pose(x['titre'], 'dossier', x.get('defi') or '')
    return d


def tetes(D):
    """Mots-têtes des notions connues : le vocabulaire des familles."""
    c = Counter()
    for v in D.values():
        m = mots_nz(v['t'])
        if m and m[0] not in VIDE and len(m[0]) > 3:
            c[R.sing(m[0])] += 1
    return c


# expressions de la forme « tête + qualificatif(s) »
def expressions(tete, txt):
    """Toutes les suites « tête (de|d'|du|des|à|en)? mot(s) » du chapitre."""
    out = Counter()
    for m in re.finditer(r'(?<![a-zàâçéèêëîïôûùüÿ])' + re.escape(tete)
                         + r"(?:s|x)?\s+((?:(?:de|du|des|d'|a|au|aux|en|par|"
                         r"sur)\s+)?[a-zàâçéèêëîïôûùüÿ'-]{3,22}"
                         r"(?:\s+[a-zàâçéèêëîïôûùüÿ'-]{3,22})?)", txt):
        suite = m.group(1).strip()
        jet = RE_MOT.findall(suite)
        if not jet:
            continue
        # on retire les mots outils de fin
        while jet and jet[-1] in QUAL_VIDE:
            jet.pop()
        if not jet:
            continue
        # au moins un mot plein
        plein = [w for w in jet if w not in QUAL_VIDE and len(w) > 3]
        if not plein:
            continue
        if jet[0] in ('de', 'du', 'des', "d'", 'a', 'au', 'aux', 'en', 'par',
                      'sur') and len(jet) == 1:
            continue
        for n in (1, 2, 3):
            if len(jet) < n:
                continue
            bout = jet[:n]
            while bout and bout[-1] in QUAL_VIDE:
                bout.pop()
            if not bout or not any(w not in QUAL_VIDE and len(w) > 3
                                   for w in bout):
                continue
            out[' '.join([tete] + bout)] += 1
    return out


# ------------------------------------------------------- indice de « termhood »

QUAL_PAUVRE = set("""pays partie annees grandes trois quatre cinq deux
secteurs entreprises certain certains certaines nombreux nombreuses
exemple exemples cas type types forme formes niveau niveaux point points
element elements chose choses facon maniere sorte ensemble groupe groupes
monde moment periode temps fois siecle siecles jours jour annee mois
nouveau nouvelle nouveaux nouvelles ancien ancienne meme memes propre
propres general generale generaux autre autres premier premiere dernier
derniere force cherchent cherche doivent peuvent veulent vont font ont
sont etre avoir suivant suivante suivants suivantes present presente""".split())


def reperes():
    """Tout ce qui, dans ÉcoSphère, atteste qu'une expression est une notion :
    un intitulé de section, un encadré de définition, une notion de chapitre,
    un libellé de fiche, un titre de dossier, d'idée de l'Atlas ou de sujet."""
    B = R.blocs()
    C = R.corpus()
    titres, encadres = [], []
    for k in R.ORDRE:
        for x in B[k]:
            if x['g'] in ('h2', 'h3', 'h4', 'h5'):
                titres.append((k, R.nz(x['x'])))
            elif x['g'] == 'db':
                encadres.append((k, R.nz(x['x'])))
    autres = []
    for k in R.ORDRE:
        for n in C['chapitres'][k]['notions']:
            autres.append((k, R.nz(n['t'])))
    for f in R.fiches():
        autres.append((str(f.get('ch') or ''), R.nz(f.get('term') or '')))
    for x in R.autour()['dossiers']:
        autres.append(('', R.nz(x['titre'])))
    for c in R.atlas()['atlas']:
        for e in c['e']:
            autres.append((str(c['k']), R.nz(e['ti']) + ' ' + R.nz(
                ' '.join(e.get('no') or []))))
    for s in C['sujets']:
        autres.append((str(s['ch']), R.nz(s['title'])))
    for k, v in R.chiffres().items():
        for x in v:
            autres.append((k, R.nz(' '.join(x.get('k') or []))))
    return titres, encadres, autres


def atteste(e, TIT, ENC, AUT):
    """Les indices de termhood pour une expression donnée."""
    rx = re.compile(r'(?<![a-z0-9])' + re.escape(e) + r'(?![a-z0-9])')
    s = set()
    for k, t in ENC:
        if rx.search(t):
            s.add('encadre'); break
    for k, t in TIT:
        if rx.search(t):
            s.add('intitule'); break
    for k, t in AUT:
        if rx.search(t):
            s.add('libelle'); break
    return s


def defini_par_le_cours(e, TXT):
    """L'expression est-elle suivie d'un verbe de définition ?"""
    rx = re.compile(r'(?<![a-z0-9])' + re.escape(e)
                    + r"s?\s+(?:designe|designent|correspond|correspondent|"
                      r"est|sont|mesure|mesurent|renvoie|renvoient|regroupe|"
                      r"regroupent|consiste|consistent)\b")
    return any(rx.search(TXT[k]) for k in R.ORDRE)


if __name__ == '__main__':
    D = defs_existantes()
    T = tetes(D)
    print('définitions autonomes recensées : %d' % len(D))
    print('  par source :',
          Counter(s for v in D.values() for s in v['src']).most_common())
    print('mots-têtes de notions           : %d' % len(T))

    TXT = {k: R.nz(socle.TXT[k]) for k in R.ORDRE}
    # on ne garde que les têtes qui structurent vraiment des familles
    cibles = [h for h, n in T.most_common() if n >= 2 and len(h) > 3]
    print('familles examinées              : %d' % len(cibles))

    TIT, ENC, AUT = reperes()
    print('intitulés relevés               : %d' % len(TIT))
    print('encadrés de définition          : %d' % len(ENC))
    print('libellés de contenus            : %d' % len(AUT))

    fam = {}
    for h in cibles:
        trouve = Counter()
        parch = defaultdict(Counter)
        for k in R.ORDRE:
            e = expressions(h, TXT[k])
            for x, n in e.items():
                trouve[x] += n
                parch[x][k] += n
        membres = []
        for x, n in trouve.items():
            c = R.cle(x)
            if n < 3:
                continue
            jet = mots_nz(x)[1:]
            if not jet or all(w in QUAL_PAUVRE for w in jet):
                continue
            att = atteste(x, TIT, ENC, AUT)
            if defini_par_le_cours(x, TXT):
                att.add('phrase')
            if not att:
                continue
            membres.append({
                'att': sorted(att),
                'e': x, 'n': n, 'cle': c,
                'ch': sorted(parch[x], key=R.ORDRE.index),
                'def': c in D,
                'libelle': D[c]['t'] if c in D else '',
                'src': sorted(D[c]['src']) if c in D else [],
            })
        membres.sort(key=lambda z: -z['n'])
        if membres:
            fam[h] = membres
    json.dump(fam, open('audit_familles.json', 'w'), ensure_ascii=False)

    manquants = [(h, m) for h, ms in fam.items() for m in ms if not m['def']]
    print('expressions relevées            : %d'
          % sum(len(v) for v in fam.values()))
    print('  avec définition               : %d'
          % sum(1 for v in fam.values() for m in v if m['def']))
    print('  sans définition               : %d' % len(manquants))
    print()
    manquants.sort(key=lambda z: -z[1]['n'])
    for h, m in manquants[:160]:
        print('  %-40s %4d occ.  ch %-22s [%s]'
              % (m['e'][:40], m['n'], ','.join(m['ch'])[:22],
                 ','.join(m['att'])))
