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
                pose(x['dt'], x['dd'], k, i, 'cours-encadre')
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
                        pose(nom, _phrase(y['x']), k, i, 'cours-intitule')
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
            pose(connues[c], _phrase(txt), k, i, 'cours-phrase')
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
