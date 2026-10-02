#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Second passage : repère les noms propres introduits par une formule d'attribution
(« selon X », « X montre », « le modèle de X », « d'après X »…) et absents de l'app."""
import io, json, re, unicodedata, collections

cours = json.load(io.open('cours.json', encoding='utf-8'))
data = json.load(io.open('data.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


connus = set()
for a in data['AUTHORS']:
    for p in a['name'].split():
        if len(p) > 2:
            connus.add(nz(p))
for ch in atlas['chapitres']:
    for e in ch['e']:
        for p in e['n'].split():
            if len(p) > 2:
                connus.add(nz(p))

STOP = set(nz(x) for x in """
France Allemagne Chine Japon Inde Russie Italie Espagne Angleterre Royaume Uni Etats
Bresil Coree Suede Norvege Danemark Finlande Pologne Grece Portugal Turquie Suisse
Mexique Argentine Afrique Asie Europe Amerique Oceanie Nord Sud Est Ouest Taiwan
Paris Londres Berlin Tokyo Pekin Shanghai Washington York Bruxelles Francfort Chicago
Etat Union Europeenne Banque Centrale Commission Conseil Parlement Vienne Cambridge
Tresor Fonds Monetaire International Mondial Organisation Mondiale Commerce Cour
Nations Unies PNUD OCDE INSEE BCE FED OMC FMI ONU IDH RNB GIEC Club Rome Davos
Grande Depression Guerre Mondiale Revolution Industrielle Trente Glorieuses Crise
Nouveau Monde Ancien Regime Moyen Age Renaissance Lumieres Occident Orient Meiji
Janvier Fevrier Mars Avril Juin Juillet Aout Septembre Octobre Novembre Decembre
Chapitre Partie Section Introduction Conclusion Exemple Remarque Attention Idee
Definition These Limite Limites Apport Apports Mecanisme Consequence Conclusion
Cependant Toutefois Ainsi Donc Enfin Ensuite Cela Cette Ces Les Des Une Autrement
Pour Dans Par Sur Avec Sans Mais Car Il Elle Nous Vous Ils Elles Lui Leur Leurs
Pourquoi Comment Quand Lorsque Puisque Alors Aussi Encore Deja Chaque Tout Tous
Premier Premiere Second Seconde Troisieme Deuxieme Grand Grande Petit Petite Autre
Loi Theorie Modele Courbe Effet Principe Systeme Analyse Approche Courant Ecole
Capital Travail Monnaie Marche Marches Entreprise Entreprises Firme Firmes Pays
Source Sources Document Documents Cours Schema Tableau Graphique Figure Rapport
Toyota General Electric Standard Oil Amazon Google Apple Microsoft Meta Netflix
Boeing Airbus Renault Peugeot Nokia Samsung Intel Nvidia Tesla Huawei Alibaba
GAFAM BATX New Deal Bretton Woods Maastricht Rome Lisbonne Doha Kyoto Accord
Wall Street City Silicon Valley Manchester Birmingham Liverpool Detroit Bangalore
Monsieur Madame Saint Sainte Nobel Prix Traite Sommet Protocole Pacte Plan
Afrique Nigeria Vietnam Indonesie Thailande Malaisie Singapour Hong Kong Macao
Produit Revenu Salaire Profit Interet Credit Dette Deficit Budget Impot Taxe
Consommation Epargne Investissement Production Echange Croissance Developpement
Inegalites Pauvrete Chomage Inflation Deflation Recession Expansion Cycle
""".split())

MOT = r"[A-ZÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ][a-zàâäéèêëîïôöùûüç'’\-]{2,}"
NOM = r'(?:%s)(?:\s+(?:de|du|des|van|von|der|le|la)\s+%s|[\s-]+%s){0,2}' % (MOT, MOT, MOT)
FORMULES = [
    r'(?:[Ss]elon|[Pp]our|[Cc]hez|[Dd]\'après|[Dd]e l\'avis de)\s+(%s)' % NOM,
    r'\b(%s)\s+(?:montre|affirme|explique|souligne|propose|distingue|défend|estime|observe|développe|formalise|introduit|analyse|critique|conteste|rappelle|parle de|insiste|note|considère|constate|publie|écrit|utilise|reprend|qualifie|appelle|définit)' % NOM,
    r"(?:le |la |les |l')(?:modèle|théorie|analyse|loi|courbe|approche|thèse|idée|notion|concept|paradoxe|théorème|effet|indice|coefficient|équation|fonction|multiplicateur|triangle|dilemme|règle|critique|typologie)\s+(?:de |d'|du )(%s)" % NOM,
    r'\b(%s)\s*\((?:19|18|20)\d\d\)' % NOM,
]

compte = collections.defaultdict(lambda: collections.Counter())
exemples = {}
for ch, txt in cours.items():
    for rx in FORMULES:
        for m in re.finditer(rx, txt):
            plein = re.sub(r'\s+', ' ', m.group(1)).strip()
            mots = plein.split()
            if any(nz(w) in STOP for w in mots):
                continue
            d = nz(mots[-1])
            if d in connus or len(d) < 4:
                continue
            compte[d][ch] += 1
            exemples.setdefault(d, (plein, ch, re.sub(r'\s+', ' ', txt[max(0, m.start() - 130):m.start() + 230])))

lignes = sorted(((sum(v.values()), d, dict(v)) for d, v in compte.items()), reverse=True)
print('%d candidats signalés par une formule d\'attribution\n' % len(lignes))
for tot, d, parch in lignes:
    plein, ch, ctx = exemples[d]
    chs = ' '.join('ch%s:%d' % (k, v) for k, v in sorted(parch.items(), key=lambda x: -x[1]))
    print('%3d  %-26s %s' % (tot, plein, chs))
    print('     …%s…' % ctx[:215])
