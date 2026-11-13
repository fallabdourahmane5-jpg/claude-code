# -*- coding: utf-8 -*-
"""Moissonne dans les cours toutes les phrases qui définissent une notion.

Trois gisements, par ordre de fiabilité décroissante :
  1. les blocs de définition du cours (terme / définition encadrés) ;
  2. le paragraphe qui suit un intitulé « Définition … » ;
  3. les phrases de forme « X désigne … », « Un X est … », lorsque X nomme
     une notion du chapitre ou l'intitulé d'une section.

Rien n'est reformulé : la définition retenue est le texte du cours. Chaque
définition garde le numéro du bloc dont elle provient, ce qui permet d'ouvrir
le passage exact.
"""
import re

import rech_base as R

VERBE = (r"designe|designent|correspond a|correspondent a|est defini|"
         r"sont definis|se definit|se definissent|consiste a|consistent a|"
         r"renvoie a|renvoient a|mesure|mesurent|exprime|expriment|"
         r"regroupe|regroupent|est|sont")

RE_DEF_TITRE = re.compile(r'(?i)\bd[eé]finition')

# mots qui désignent le discours du cours, non une notion du programme
GENERIQUE = set("""demande offre production structure role fonction rapport
question relation sens flux stock solution mesure difference paradoxe
probleme enjeu consequence caractere caracteristique explication idee
essentielle fondamentale auteur exemple travail travailleur revenu service
bien marche concurrence pays etat entreprise population principe logique
objectif constat limite critique terme nature type forme niveau cas effet
politique analyse approche point element condition resultat situation
comportement performance intitule generale precise majeur pente plus
chronologique interet problematique avoir engagement capital commun
introduction conclusion transition remarque attention source reference
document lecture graphique tableau schema plan sommaire bilan synthese
rappel""".split())

MAUVAIS_DEBUT = re.compile(
    r'^(?:et|ou|de|du|des|en|sur|par|pour|avec|sans|dans|donc|or|mais|ainsi|'
    r'plus|moins|puis|alors|ensuite|enfin|cette|ce|ces|il|elle|on|nous|'
    r'd ou|ou la|ou le|ou les|si|quand|lorsque|comme|chez|tandis|alors que|'
    r'exemple|autrement|c est|il s agit|voici|soit)\b')

SUSPECT = re.compile(r'[0-9\\«»~^{}|<>]|\u00ab|\u00bb')

# un libellé de notion n'est pas une phrase conjuguée
CONJUGUE = re.compile(
    r'\b(est|sont|peut|peuvent|doit|doivent|permet|permettent|montre|montrent|'
    r'explique|expliquent|conduit|conduisent|depend|dependent|implique|'
    r'impliquent|suppose|supposent|devient|deviennent|reste|restent|faut|'
    r'il y a|on peut|illustre|illustrent|constitue|constituent|repose|'
    r'reposent|traduit|traduisent|revient|reviennent|donne|donnent|apparait|'
    r'apparaissent|cherche|cherchent|parlent|parle|pensent|pense|vit|vient|'
    r'a ete|ont|avait|etait|sera|va|vont|n est|s agit|existe|augmente|'
    r'diminue|correspond|designe|consiste|renvoie|regroupe|definit|'
    r'exercent|creent|offre|suffit|reconnait)\b')

# amorces de discours : ce n'est pas un nom de notion
DISCOURS = re.compile(
    r'(?i)^(autre|autres|certain|certains|certaines|cependant|ainsi|donc|or|'
    r'mais|cela|c est|il|elle|on|ce|cette|ces|par exemple|autrement dit|'
    r'en effet|premier|premiere|deuxieme|troisieme|quatrieme|dernier|'
    r'derniere|conclusion|consequence|hypothese|idee|point|exemple|remarque|'
    r'critique|comparaison|face|depasser|ils|elles|nous|vous|imais|'
    r'innovation majeure|freins|dernier point)\b')


def _auteurs_connus():
    import json
    try:
        C = json.load(open('corpus.json'))
    except Exception:
        return set()
    s = set()
    for a in C['auteurs']:
        n = R.nz(a['name'])
        s.add(n)
        p = n.split()
        if p:
            s.add(p[-1])
        if len(p) > 1:
            s.add(p[0] + ' ' + p[-1])
    return s


AUTEURS = None
NOTIONS_SURES = None


def _notions_sures():
    """Libellés que l'application tient explicitement pour des notions :
    notions de chapitre, libellés du programme, titres de dossiers et idées de
    l'Atlas. Sert à filtrer les définitions dont le titre est un mot isolé."""
    import notions_liste
    s = set()
    try:
        C = R.corpus()
        for k in R.ORDRE:
            for n in C['chapitres'][k]['notions']:
                if n['t']:
                    s.add(R.cle(n['t']))
        for e in notions_liste.ENSEMBLES:
            for lb in e['dossiers']:
                s.add(R.cle(lb))
        for x in R.autour()['dossiers']:
            s.add(R.cle(x['titre']))
        for c in R.atlas()['atlas']:
            for e in c['e']:
                s.add(R.cle(e['ti']))
                for no in (e.get('no') or []):
                    s.add(R.cle(no))
    except Exception:
        pass
    return s

# un libellé de notion ne se termine pas par le verbe qui introduit sa
# définition : « l'utilité marginale mesure » n'est pas un nom de notion
FIN_VERBE = set("""mesure mesurent designe designent correspond correspondent
est sont consiste consistent renvoie renvoient exprime expriment regroupe
regroupent definit definissent appelle nomme traduit indique signifie
permet permettent devient deviennent reste restent""".split())
ARTICLE_TETE = re.compile(r"(?i)^(?:le|la|les|l['’]|un|une|des|du)\s+")


def _phrase(t):
    """Première phrase utile d'un bloc."""
    t = ' '.join(str(t or '').split())
    m = re.search(r'(.{40,600}?[.!])(?:\s|$)', t)
    return (m.group(1) if m else t)[:600]


def _propre(t):
    return str(t or '').strip(' :·—–-’\'"«»')


def etoffer(B, k, i, defi, cible=190, plafond=560):
    """Complète une définition trop brève par les blocs qui la suivent."""
    if len(defi) >= cible:
        return defi
    bouts = [defi]
    n = len(defi)
    for y in B[k][i + 1:i + 7]:
        if y['g'] in ('h2', 'h3'):
            break
        t = ' '.join(str(y['x']).split())
        if len(t) < 18 or R.BRUIT.match(R.nz(t)):
            continue
        if t in bouts:
            continue
        bouts.append(t)
        n += len(t) + 2
        if n >= cible:
            break
    out = ' '.join(bouts)
    return out[:plafond].rstrip(' ,;:·—–-')


def moisson(blocs=None, notions_connues=None):
    """cle -> {'t','d','ch','b','o'} pour chaque définition trouvée."""
    B = blocs or R.blocs()
    connues = notions_connues or {}
    out = {}

    def pose(terme, defi, ch, b, origine):
        terme = _propre(terme)
        defi = ' '.join(str(defi or '').split())
        c = R.cle(terme)
        if not c or len(c) < 3 or len(terme) > 80:
            return
        if len(defi) < 25 or len(defi) > 900:
            return
        if R.BRUIT.match(R.nz(terme)):
            return
        n = R.nz(terme)
        if SUSPECT.search(terme) or MAUVAIS_DEBUT.match(n):
            return
        if ':' in terme or terme.count(' ') > 7:
            return
        jetons = R.mots(terme)
        if not jetons or all(w in GENERIQUE for w in jetons):
            return
        if len(c.split()) == 1 and c in GENERIQUE:
            return
        if jetons[-1] in FIN_VERBE:
            return
        global AUTEURS
        if AUTEURS is None:
            AUTEURS = _auteurs_connus()
        # un nom d'auteur relève de la rubrique « auteurs », pas des définitions
        if n in AUTEURS or R.cle(terme) in AUTEURS:
            return
        if CONJUGUE.search(n) or DISCOURS.match(n):
            return
        if len(jetons) > 6:
            return
        if terme.isupper() and len(jetons) > 2:
            return
        # un titre d'un seul mot n'est retenu que s'il s'agit d'un sigle ou
        # d'une notion reconnue ailleurs dans l'application
        if len(jetons) == 1 and not (terme.isupper() and len(terme) <= 6):
            global NOTIONS_SURES
            if NOTIONS_SURES is None:
                NOTIONS_SURES = _notions_sures()
            if c not in NOTIONS_SURES:
                return
        x = out.setdefault(c, {'t': terme, 'd': defi, 'ch': {}, 'o': set()})
        x['o'].add(origine)
        x['ch'].setdefault(str(ch), b)
        # on garde la formulation la plus complète, et le libellé le plus court
        if len(defi) > len(x['d']):
            x['d'] = defi
        if len(terme) < len(x['t']):
            x['t'] = terme

    for k in R.ORDRE:
        v = B[k]
        for i, x in enumerate(v):
            # ---- 1. blocs de définition du cours
            if x['g'] == 'db' and x['dt'] and x['dd']:
                pose(x['dt'], etoffer(B, k, i, x['dd']), k, i, 'cours-encadre')
                continue
            # ---- 2. paragraphe suivant un intitulé « Définition … »
            if x['g'] in ('h3', 'h4', 'h5') and RE_DEF_TITRE.search(x['x']):
                # le terme est soit nommé dans l'intitulé, soit celui de la
                # section qui précède
                nom = _propre(RE_DEF_TITRE.sub('', R.titre_propre(x['x'])))
                nom = re.sub(r"(?i)^(?:generale?|precise|du|de la|de l['’]|"
                             r"des|d['’]|:)\s*", '', nom).strip()
                if len(R.cle(nom)) < 3:
                    for y in reversed(v[max(0, i - 10):i]):
                        if y['g'] in ('h2', 'h3'):
                            cand = R.titre_propre(y['x'])
                            if R.est_notion(cand):
                                nom = cand
                            break
                for y in v[i + 1:i + 4]:
                    if y['g'] in ('h2', 'h3', 'h4'):
                        break
                    if len(y['x']) >= 40:
                        pose(nom, etoffer(B, k, i + 1, _phrase(y['x'])), k, i,
                             'cours-intitule')
                        break
                continue
            # ---- 3. phrases définitoires explicites
            if x['g'] not in ('p', 'li'):
                continue
            txt = ' '.join(x['x'].split())
            if not (45 <= len(txt) <= 900):
                continue
            m = re.match(r'(?i)^(?:le|la|les|l[’\']|un|une)\s+'
                         r'([^.;:!?]{3,60}?)\s+(?:' + VERBE + r')\b(.{20,})$',
                         R.nz(txt))
            if not m:
                m = re.match(r'(?i)^([A-ZÀ-Ý][^.;:!?]{3,60}?)\s+(?:'
                             + VERBE + r')\b(.{20,})$', R.nz(txt))
            if not m:
                continue
            brut = m.group(1)
            c = R.cle(brut)
            if not c or len(c) < 3:
                continue
            # on n'accepte que si l'expression est déjà reconnue comme notion
            # du chapitre, intitulé de section ou notion du programme
            if c not in connues:
                continue
            pose(connues[c], etoffer(B, k, i, _phrase(txt)), k, i,
                 'cours-phrase')
    for v in out.values():
        v['o'] = sorted(v['o'])
    return out


def notions_connues(blocs=None):
    """cle -> libellé, pour tout ce que les cours nomment comme notion."""
    import notions_liste
    B = blocs or R.blocs()
    C = R.corpus()
    d = {}

    def pose(t):
        c = R.cle(t)
        if c and len(c) >= 3 and (c not in d or len(t) < len(d[c])):
            d[c] = _propre(t)

    for k in R.ORDRE:
        for n in C['chapitres'][k]['notions']:
            if n['t']:
                pose(n['t'])
        for x in B[k]:
            if x['g'] == 'db' and x['dt']:
                pose(x['dt'])
            elif x['g'] in ('h2', 'h3', 'h4'):
                t = R.titre_propre(x['x'])
                if R.est_notion(t):
                    pose(t)
    for e in notions_liste.ENSEMBLES:
        for lb in e['dossiers']:
            pose(lb)
    for x in R.autour()['dossiers']:
        pose(x['titre'])
    return d


if __name__ == '__main__':
    B = R.blocs()
    NC = notions_connues(B)
    M = moisson(B, NC)
    from collections import Counter
    print('notions nommées par les cours : %d' % len(NC))
    print('définitions moissonnées       : %d' % len(M))
    print('  par gisement :', Counter(o for v in M.values()
                                      for o in v['o']).most_common())
    from manques import definitions_existantes
    DEF = definitions_existantes()
    neuves = {c: v for c, v in M.items() if c not in DEF}
    print('  dont absentes d’ÉcoSphère   : %d' % len(neuves))
    for c, v in sorted(neuves.items())[:40]:
        print('    %-44s %s' % (v['t'][:44], v['d'][:90]))
