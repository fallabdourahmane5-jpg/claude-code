#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit : confronte une liste de patronymes d'économistes et de sociologues au
texte des cours, et signale ceux qui y figurent sans être dans l'application."""
import io, json, re, unicodedata, collections, sys

cours = json.load(io.open('cours.json', encoding='utf-8'))
data = json.load(io.open('data.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


CANDIDATS = """
Bhagwati Debreu Phillips Aghion Juglar Kitchin Kondratiev Palma Nakamoto
Krueger Tullock Niskanen Downs Olson Buchanan Becker Mincer Schultz Nelson Winter
Veblen Commons Mitchell Galbraith Myrdal Hirschman Prebisch Singer Furtado
Lewis Nurkse Rosenstein Leibenstein Hirschman Perroux Bairoch Maddison Landes
Mokyr Crafts Clark Wrigley Braudel Polanyi Weber Sombart Schumpeter Hayek
Mises Rothbard Kirzner Lachmann Menger Bohm Wieser Robbins Pigou Marshall
Edgeworth Bowley Hicks Allen Slutsky Samuelson Solow Swan Ramsey Cass Koopmans
Diamond Phelps Sidrauski Lucas Sargent Barro Kydland Prescott Mankiw Romer
Stiglitz Akerlof Spence Vickrey Mirrlees Laffont Tirole Holmstrom Milgrom
Hart Moore Grossman Williamson Coase Alchian Demsetz Jensen Meckling Fama
Modigliani Miller Markowitz Sharpe Tobin Minsky Kindleberger Fisher Wicksell
Hawtrey Robertson Kalecki Kaldor Pasinetti Robinson Sraffa Harcourt Garegnani
Boyer Aglietta Lipietz Orlean Favereau Thevenot Boltanski Chiapello Bourdieu
Durkheim Mauss Halbwachs Simiand Elias Goffman Merton Parsons Becker Crozier
Friedberg March Simon Cyert Mintzberg Chandler Penrose Nelson Teece Porter
Rodrik Krugman Melitz Helpman Grossman Baldwin Venables Fujita Ottaviano
Dixit Stiglitz Lancaster Linder Vernon Hymer Dunning Caves Markusen
Ricardo Torrens Mill Senior Bastiat Cournot Dupuit Walras Pareto Barone
Wieser Clark Knight Schumpeter Shackle Keynes Kahn Meade Harrod Domar
Hansen Hicks Patinkin Clower Leijonhufvud Malinvaud Benassy Drèze
Friedman Phelps Brunner Meltzer Laidler Cagan Lucas Barro Fischer Taylor
Blanchard Krugman Obstfeld Rogoff Reinhart Eichengreen Bordo Triffin Mundell
Fleming Dornbusch Calvo Rey Gourinchas Caballero Farhi Werning Gopinath
Piketty Saez Zucman Atkinson Milanovic Bourguignon Deaton Banerjee Duflo
Kremer Sen Nussbaum Anand Ravallion Chen Alkire Foster
Nordhaus Stern Weitzman Dasgupta Heal Hotelling Hartwick Daly Georgescu
Meadows Jackson Raworth Fressoz Jarrige Bonneuil Charbonnier Pisani
Veltz Askenazy Cahuc Zylberberg Cette Artus Betbeze Plihon Chavagneux
Jorion Giraud Lordon Orlean Boyer Coriat Petit Amable Hall Soskice
Streeck Esping Andersen Castel Paugam Maurin Dubet Lahire Beaud Pialoux
Mayo Taylor Fayol Ford Ohno Lewin Likert Herzberg Maslow McGregor Argyris
Asch Milgram Janis Festinger Tversky Kahneman Thaler Sunstein Ariely
Bronner Morel Boudon Coleman Granovetter Burt Uzzi White Zelizer Callon
Latour Dodier Thevenot Olson Ostrom Hardin Heller Buchanan Stigler Posner
Aubenas Weil Linhart Terssac Reynaud Segrestin Supiot Gollac Clot Dejours
List Hamilton Carey Prebisch Chang Wade Amsden Johnson Evans Mazzucato
Rockefeller Carnegie Morgan Welch Sloan Drucker Mintzberg Hamel Prahalad
Shih Reich Malgouyres Fontagné Mouhoud Cohen Fourastié Sauvy Clark
Michalet Bairoch Beraud Volcker Greenspan Bernanke Yellen Powell Lagarde
Draghi Trichet Monnet Villeroy Kelton Lerner Wray Mosler Godley
Bodin Colbert Mun Serra Montchrestien Cantillon Quesnay Turgot Gournay
Mandeville Petty Boisguilbert Vauban Law Palmstruch Smith Malthus Marx
Engels Proudhon Saint Fourier Owen Lassalle Bernstein Luxemburg Lenin
Hilferding Bukharin Baran Sweezy Amin Emmanuel Frank Wallerstein Arrighi
Gerschenkron Rostow Hoselitz Myrdal Kuznets Chenery Syrquin Hirschman
Acemoglu Robinson North Weingast Greif Putnam Fukuyama Landes Diamond
Pomeranz Allen Wrigley Mokyr Crafts Bairoch Maddison OBrien Parthasarathi
Chamberlin Robinson Bain Mason Stigler Baumol Panzar Willig Combe Jenny
Arkwright Crompton Cartwright Hargreaves Watt Jenner Darby Bessemer
Edison Tesla Bell Marconi Turing Shannon Berners Gates Jobs Musk Bezos
Gossen Jevons Bentham Mill Sidgwick Rawls Nozick Dworkin Roemer Fleurbaey
Easterlin Layard Frey Stutzer Kahneman Deaton Stiglitz Fitoussi
Boserup Landry Notestein Bloom Canning Chesnais Vallin Pison Toulemon
Brundtland Meadows Rockstrom Steffen Latouche Gorz Illich Schumacher
Duesenberry Engel Modigliani Brumberg Ando Friedman Hall Flavin Deaton
Musgrave Samuelson Tiebout Oates Olson Wagner Peacock Baumol Wiseman
Rosanvallon Spire Jaravel Bozio Garbinti Goupille Landais Dubet
Keen Raworth Mazzucato Chang Reinert Reinhart Rogoff Blyth Streeck
Wolf Rajan Shiller Akerlof Minsky Kindleberger Galbraith Bourguinat
Sombart Elias Veblen Simmel Tonnies Tarde LePlay Comte Spencer
Mill Say Sismondi Malthus Ricardo Senior Torrens McCulloch
"""

patro = sorted({x for x in CANDIDATS.split() if len(x) > 3})

# patronymes déjà présents dans l'application
dans_app = set()
for a in data['AUTHORS']:
    for p in a['name'].split():
        if len(p) > 2:
            dans_app.add(nz(p))
for ch in atlas['chapitres']:
    for e in ch['e']:
        for p in e['n'].split():
            if len(p) > 2:
                dans_app.add(nz(p))

# faux amis : patronymes dont la forme normalisée se confond avec un mot courant
AMBIGUS = {nz(x) for x in ('March', 'List', 'Clark', 'Allen', 'Ford', 'Mill', 'Bell',
                           'Hall', 'Hart', 'Moore', 'White', 'Chen', 'Gates', 'Jobs',
                           'Wolf', 'Say', 'Miller', 'Porter', 'Shannon', 'Bain',
                           'Means', 'Jenny', 'Simon', 'Sen', 'Rey', 'Law', 'Watt',
                           'Monnet', 'Cohen', 'Robinson', 'Evans', 'Johnson', 'Wade')}

res = collections.defaultdict(lambda: collections.Counter())
ctxs = {}
for nom in patro:
    n = nz(nom)
    if n in dans_app:
        continue
    pat = re.compile(r'\b' + re.escape(nom) + r'\b')
    for ch, txt in cours.items():
        for m in pat.finditer(txt):
            res[nom][ch] += 1
            ctxs.setdefault((nom, ch), txt[max(0, m.start() - 150):m.start() + 320])

lignes = sorted(((sum(v.values()), nom, dict(v)) for nom, v in res.items()), reverse=True)
print('%d patronymes présents dans les cours et absents de l\'application\n' % len(lignes))
for tot, nom, parch in lignes:
    marque = ' (ambigu)' if nz(nom) in AMBIGUS else ''
    chs = ' '.join('ch%s:%d' % (k, v) for k, v in sorted(parch.items(), key=lambda x: -x[1]))
    print('%4d  %-16s %s%s' % (tot, nom, chs, marque))
    pch = max(parch, key=parch.get)
    print('      …%s…\n' % re.sub(r'\s+', ' ', ctxs[(nom, pch)])[:300])
