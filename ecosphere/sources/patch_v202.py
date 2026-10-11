#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Section « Résumés des chapitres », version approfondie (v202).

Les résumés de la v201 survolaient les chapitres. Ceux-ci suivent l'ordre réel
des parties et des sous-parties de la section « Cours » : pour chaque idée, ce
qu'elle démontre, le mécanisme, les conditions et limites, puis la transition
vers l'idée suivante. Auteurs, théories, exemples, débats et chiffres sont
intégrés à l'endroit où ils servent le raisonnement. La longueur suit la
richesse du chapitre.

Le format reste constant, dans cet ordre :
  1. La question centrale                              champ q
  2. L'essentiel                                       champ ess
  3. Le chapitre partie par partie                     champ parties (t / sp / v)
         sous-partie : t, d (paragraphes), mec, lim
  4. Auteurs et exemples incontournables               champ ae (n / k / i)
  5. Ce qu'il faut mobiliser en dissertation           champs arg, deb, lien
  6. À retenir en une minute                           champ min

POUR UN FUTUR CHAPITRE : créer res2_<n>.py avec exactement ces champs, l'ajouter
à ORDRE et TITRES, puis relancer ce script. Les contrôles ci-dessous refusent un
résumé incomplet, et la couverture est vérifiée contre la liste des chapitres
réellement intégrés à ÉcoSphère.
"""
import io, json, re, importlib

SRC = 'app_v200.html'
DST = 'app_v202.html'

ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '21', '22', '23']
LIB = {'21': '2ᵉ année — Chapitre 1', '22': '2ᵉ année — Chapitre 2', '23': '2ᵉ année — Chapitre 3'}
TITRES = {
 '1': "Pauvreté, capitalisme et rôle de l’État",
 '2': "Monnaie et financement de l’économie",
 '3': "Les grands courants de la pensée économique",
 '4': "Analyse microéconomique : consommateur et producteur",
 '5': "Défaillances du marché et régulation",
 '6': "Croissance économique",
 '7': "Développement et soutenabilité",
 '8': "Révolutions industrielles, entreprise, travail et IA",
 '9': "Taille et stratégies des entreprises",
 '10': "Sociologie des organisations et du travail",
 '21': "Mondialisation et déséquilibres extérieurs",
 '22': "FMN, États et politique industrielle",
 '23': "L’analyse économique du commerce international",
}

R = {}
for c in ORDRE:
    mod = importlib.import_module('res2_' + c)
    for k, v in mod.R.items():
        assert k not in R, ('résumé en double', k)
        R[k] = v

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-resumes' not in s, 'la base contient déjà une section Résumés'

# ------------------------------------------------- couverture des chapitres
# Les chapitres réellement intégrés à ÉcoSphère, lus dans CH_CONTENT.
cles = set()
for m in re.finditer(r'CH_CONTENT\s*\[\s*(\d+)\s*\]', s):
    cles.add(m.group(1))
bloc = re.search(r'const\s+CH_CONTENT\s*=\s*\{', s)
if bloc:
    fin = s.find('\n};', bloc.end())
    for m in re.finditer(r'^\s*(\d+)\s*:', s[bloc.end():fin if fin > 0 else bloc.end() + 400000],
                         re.M):
        cles.add(m.group(1))
manquants = sorted(cles - set(ORDRE), key=int)
assert not manquants, ('chapitres intégrés sans résumé', manquants)

# ------------------------------------------------------------- contrôles
RE_MOT = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ]{3,}')


def mots(txt):
    return set(m.group(0).lower() for m in RE_MOT.finditer(txt))


def texte(r):
    """Tout le texte d'un résumé, pour les contrôles et la recherche."""
    b = [r['q'], r['ess']]
    for p in r['parties']:
        b.append(p['t'])
        b.append(p['v'])
        for sp in p['sp']:
            b.append(sp['t'])
            b += sp['d']
            if sp.get('mec'):
                b.append(sp['mec'])
            if sp.get('lim'):
                b.append(sp['lim'])
    for a in r['ae']:
        b += [a['n'], a['i']]
    b += r['arg'] + r['deb'] + r['min']
    b += [l['p'] for l in r['lien']]
    return ' '.join(b)


assert set(R) == set(ORDRE), (sorted(set(ORDRE) - set(R)), sorted(set(R) - set(ORDRE)))

stats = {}
for c in ORDRE:
    r = R[c]
    for k in ('q', 'ess', 'parties', 'ae', 'arg', 'deb', 'lien', 'min'):
        assert r.get(k), (c, 'champ manquant', k)
    assert 80 < len(r['q']) < 320, (c, 'question centrale', len(r['q']))
    assert r['q'].rstrip().endswith('?'), (c, 'la question centrale doit être une question')
    # L'essentiel s'adapte à la richesse du chapitre, sans jamais devenir une fiche.
    assert 1000 < len(r['ess']) < 4000, (c, 'essentiel', len(r['ess']))
    assert 4 <= len(r['parties']) <= 24, (c, 'parties', len(r['parties']))
    nsp = 0
    for p in r['parties']:
        for k in ('t', 'sp', 'v'):
            assert p.get(k), (c, 'partie incomplète', p.get('t'), k)
        assert 20 < len(p['t']) < 180, (c, 'titre de partie', p['t'])
        assert 40 < len(p['v']) < 420, (c, p['t'], 'transition', len(p['v']))
        assert 1 <= len(p['sp']) <= 24, (c, p['t'], 'sous-parties', len(p['sp']))
        for sp in p['sp']:
            assert sp.get('t') and sp.get('d'), (c, p['t'], 'sous-partie incomplète')
            assert isinstance(sp['d'], list) and 1 <= len(sp['d']) <= 8, (c, sp['t'])
            for para in sp['d']:
                assert 100 < len(para) < 1500, (c, sp['t'], 'paragraphe', len(para))
            if sp.get('mec'):
                assert 40 < len(sp['mec']) < 1100, (c, sp['t'], 'mécanisme')
            if sp.get('lim'):
                assert 40 < len(sp['lim']) < 1100, (c, sp['t'], 'limites')
            nsp += 1
    # Le chapitre doit être couvert : au moins deux sous-parties par partie en moyenne.
    assert nsp >= 2 * len(r['parties']), (c, 'couverture trop faible', nsp, len(r['parties']))
    # Au moins un mécanisme et une limite explicités par résumé.
    assert sum(1 for p in r['parties'] for sp in p['sp'] if sp.get('mec')) >= 3, (c, 'mécanismes')
    assert sum(1 for p in r['parties'] for sp in p['sp'] if sp.get('lim')) >= 3, (c, 'limites')
    assert 12 <= len(r['ae']) <= 70, (c, 'auteurs et exemples', len(r['ae']))
    for a in r['ae']:
        assert a['k'] in ('a', 'e'), (c, a['n'])
        assert 50 < len(a['i']) < 600, (c, a['n'], len(a['i']))
    assert sum(1 for a in r['ae'] if a['k'] == 'a') >= 8, (c, 'trop peu d’auteurs')
    assert sum(1 for a in r['ae'] if a['k'] == 'e') >= 3, (c, 'trop peu d’exemples')
    assert 5 <= len(r['arg']) <= 20 and 4 <= len(r['deb']) <= 18, c
    assert 3 <= len(r['lien']) <= 10, c
    for l in r['lien']:
        assert str(l['c']) in ORDRE and str(l['c']) != c, (c, 'lien invalide', l['c'])
        assert len(l['p']) > 60, (c, l['c'])
    assert 8 <= len(r['min']) <= 26, (c, 'à retenir en une minute', len(r['min']))
    for m in r['min']:
        assert 25 < len(m) < 900, (c, 'point trop long ou trop court', m[:60])
    stats[c] = {'signes': len(texte(r)), 'parties': len(r['parties']), 'sp': nsp}

# Aucun résumé générique : chaque chapitre garde un vocabulaire propre.
SACS = {c: mots(texte(R[c])) for c in ORDRE}
for c in ORDRE:
    propre = SACS[c] - set().union(*[SACS[d] for d in ORDRE if d != c])
    assert len(propre) >= 60, (c, 'résumé trop générique', len(propre))
    for d in ORDRE:
        if d <= c:
            continue
        j = len(SACS[c] & SACS[d]) / float(len(SACS[c] | SACS[d]))
        assert j < 0.42, ('deux résumés trop proches', c, d, round(j, 3))

# Les notions, auteurs et chiffres clés doivent figurer dans le résumé du chapitre.
EXIGE = {
 '1': ['circuit', 'comptabilité nationale', 'dette publique'],
 '2': ['monnaie', 'banque centrale', 'inflation'],
 '3': ['Keynes', 'néoclassique', 'Marx'],
 '4': ['utilité', 'coût marginal', 'rendements décroissants'],
 '5': ['externalité', 'bien collectif', 'asymétrie'],
 '6': ['Solow', 'productivité', 'Schumpeter'],
 '7': ['soutenabilité', 'Sen', 'climat'],
 '8': ['révolution industrielle', 'Taylor', 'intelligence artificielle'],
 '9': ['Coase', 'concentration', 'barrière'],
 '10': ['Weber', 'organisation', 'travail'],
 '21': ['Michalet', 'balance des paiements', 'chaîne'],
 '22': ['Coase', 'désindustrialisation', 'politique industrielle'],
 '23': ['Ricardo', 'Heckscher', 'Krugman', 'List', 'Stolper'],
}
for c, termes in EXIGE.items():
    t = texte(R[c]).lower()
    for mot in termes:
        assert mot.lower() in t, (c, 'notion attendue absente du résumé', mot)

PAYLOAD = {'ordre': ORDRE, 'lib': LIB, 'titres': TITRES,
           'ch': {c: R[c] for c in ORDRE}}

CSS = """
<style id="eco-resumes-css">
#pg-resumes .rs-wrap{max-width:1100px;margin:0 auto;padding:26px 18px 80px}
#pg-resumes .rs-h1{font-size:2rem;font-weight:800;margin:0 0 6px}
#pg-resumes .rs-sub{color:var(--txt2);margin:0 0 20px;line-height:1.55;max-width:800px}
#pg-resumes .rs-bar{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
#pg-resumes .rs-in{flex:1 1 280px;min-width:200px;padding:11px 14px;border-radius:10px;
  border:1px solid var(--bdr);background:var(--s2);color:var(--txt);font-family:inherit;font-size:.9rem}
#pg-resumes .rs-sel{padding:11px 12px;border-radius:10px;border:1px solid var(--bdr);
  background:var(--s2);color:var(--txt);font-family:inherit;font-size:.85rem;cursor:pointer;
  max-width:100%;min-width:0}
#pg-resumes .rs-count{color:var(--txt3);font-size:.82rem;margin-left:auto}
#pg-resumes .rs-year{font-size:.72rem;font-weight:900;letter-spacing:.11em;text-transform:uppercase;
  color:var(--acc2);margin:22px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--bdr)}
#pg-resumes .rs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px}
#pg-resumes .rs-card{border:1px solid var(--bdr);border-left:3px solid var(--acc);border-radius:13px;
  background:var(--s2);padding:16px 17px;cursor:pointer;transition:border-color .15s,transform .12s}
#pg-resumes .rs-card:hover{border-color:var(--acc);transform:translateY(-2px)}
#pg-resumes .rs-card-n{font-size:.68rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--txt3);margin-bottom:5px}
#pg-resumes .rs-card-t{font-size:1rem;font-weight:800;line-height:1.35;margin-bottom:7px}
#pg-resumes .rs-card-q{font-size:.83rem;line-height:1.5;color:var(--txt2)}
#pg-resumes .rs-card-m{margin-top:9px;font-size:.72rem;color:var(--txt3)}
#pg-resumes .rs-card-go{margin-top:8px;font-size:.75rem;color:var(--acc2);font-weight:700}
#pg-resumes .rs-back{display:inline-block;margin-bottom:14px;padding:7px 13px;border-radius:9px;
  border:1px solid var(--bdr);background:var(--s2);color:var(--txt2);font-size:.8rem;cursor:pointer;
  font-family:inherit}
#pg-resumes .rs-back:hover{color:var(--txt);border-color:var(--acc)}
#pg-resumes .rs-det-n{font-size:.72rem;font-weight:900;letter-spacing:.11em;text-transform:uppercase;
  color:var(--acc2);margin-bottom:5px}
#pg-resumes .rs-det-t{font-size:1.55rem;font-weight:800;line-height:1.25;margin:0 0 14px}
#pg-resumes .rs-links{display:flex;gap:7px;flex-wrap:wrap;margin:0 0 24px}
#pg-resumes .rs-lk{padding:7px 13px;border-radius:9px;border:1px solid var(--bdr);background:var(--s2);
  color:var(--txt2);font-size:.78rem;cursor:pointer;font-family:inherit;white-space:nowrap}
#pg-resumes .rs-lk:hover{color:var(--txt);border-color:var(--acc)}
#pg-resumes .rs-sec{margin:0 0 26px}
#pg-resumes .rs-sec-h{display:flex;align-items:baseline;gap:9px;margin:0 0 11px}
#pg-resumes .rs-sec-i{flex:0 0 auto;width:22px;height:22px;border-radius:6px;display:inline-flex;
  align-items:center;justify-content:center;font-size:.7rem;font-weight:900;
  background:rgba(124,106,247,.14);color:var(--acc2)}
#pg-resumes .rs-sec-t{font-size:.74rem;font-weight:900;letter-spacing:.09em;text-transform:uppercase;
  color:var(--txt3)}
#pg-resumes .rs-q{font-size:1.02rem;line-height:1.55;font-weight:700;
  border-left:3px solid var(--acc);padding:2px 0 2px 14px}
#pg-resumes .rs-p{font-size:.9rem;line-height:1.68;color:var(--txt2);margin:0 0 10px}
#pg-resumes .rs-tools{display:flex;gap:7px;flex-wrap:wrap;margin:0 0 12px}
#pg-resumes .rs-tool{padding:6px 11px;border-radius:8px;border:1px solid var(--bdr);background:var(--s2);
  color:var(--txt2);font-size:.75rem;cursor:pointer;font-family:inherit}
#pg-resumes .rs-tool:hover{color:var(--txt);border-color:var(--acc)}
#pg-resumes .rs-plan{border:1px solid var(--bdr);border-radius:12px;background:var(--s2);
  padding:12px 15px;margin:0 0 16px}
#pg-resumes .rs-plan-t{font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  color:var(--txt3);margin:0 0 8px}
#pg-resumes .rs-plan ol{margin:0;padding-left:19px}
#pg-resumes .rs-plan li{font-size:.84rem;line-height:1.5;color:var(--txt2);margin:0 0 5px;
  cursor:pointer}
#pg-resumes .rs-plan li:hover{color:var(--acc2)}
#pg-resumes .rs-part{border:1px solid var(--bdr);border-radius:13px;background:var(--s2);
  margin:0 0 13px;overflow:hidden}
#pg-resumes .rs-part-h{display:flex;align-items:flex-start;gap:9px;padding:13px 15px;cursor:pointer;
  border-left:3px solid var(--acc)}
#pg-resumes .rs-part-h:hover{background:rgba(124,106,247,.06)}
#pg-resumes .rs-part-t{flex:1 1 auto;font-size:.98rem;font-weight:800;line-height:1.38}
#pg-resumes .rs-part-c{flex:0 0 auto;font-size:.68rem;color:var(--txt3);padding-top:3px}
#pg-resumes .rs-part-x{flex:0 0 auto;font-size:.8rem;color:var(--txt3);padding-top:2px}
#pg-resumes .rs-part-b{padding:0 15px 13px}
#pg-resumes .rs-sp{border-top:1px solid var(--bdr);padding:12px 0 2px}
#pg-resumes .rs-sp:first-child{border-top:0;padding-top:4px}
#pg-resumes .rs-sp-t{font-size:.88rem;font-weight:800;line-height:1.4;margin:0 0 7px;color:var(--txt)}
#pg-resumes .rs-sp-d{font-size:.87rem;line-height:1.68;color:var(--txt2);margin:0 0 9px}
#pg-resumes .rs-sp-d b{color:var(--txt);font-weight:700}
#pg-resumes .rs-box{border-radius:9px;padding:9px 12px;margin:0 0 9px;font-size:.82rem;
  line-height:1.58}
#pg-resumes .rs-box b{display:block;font-size:.65rem;font-weight:900;letter-spacing:.08em;
  text-transform:uppercase;margin-bottom:3px}
#pg-resumes .rs-mec{background:rgba(106,247,196,.07);border:1px solid rgba(106,247,196,.25);
  color:var(--txt2)}
#pg-resumes .rs-mec b{color:var(--acc3)}
#pg-resumes .rs-lim{background:rgba(247,162,106,.07);border:1px solid rgba(247,162,106,.25);
  color:var(--txt2)}
#pg-resumes .rs-lim b{color:#f7a26a}
#pg-resumes .rs-part-v{margin:11px 0 0;padding:10px 12px;border-radius:9px;
  background:rgba(124,106,247,.07);border:1px solid rgba(124,106,247,.22);
  font-size:.82rem;line-height:1.58;color:var(--txt2)}
#pg-resumes .rs-part-v b{display:block;font-size:.65rem;font-weight:900;letter-spacing:.08em;
  text-transform:uppercase;color:var(--acc2);margin-bottom:3px}
#pg-resumes .rs-ae{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:10px}
#pg-resumes .rs-ae-c{border:1px solid var(--bdr);border-radius:11px;background:var(--s2);padding:12px 14px}
#pg-resumes .rs-ae-n{font-size:.87rem;font-weight:800;line-height:1.35;margin-bottom:5px}
#pg-resumes .rs-ae-b{font-size:.63rem;padding:2px 7px;border-radius:999px;border:1px solid var(--bdr);
  color:var(--txt3);margin-right:6px;vertical-align:middle;text-transform:uppercase;letter-spacing:.06em}
#pg-resumes .rs-ae-c.ex .rs-ae-b{color:#f7a26a;border-color:rgba(247,162,106,.3)}
#pg-resumes .rs-ae-c.au .rs-ae-b{color:var(--acc3);border-color:rgba(106,247,196,.3)}
#pg-resumes .rs-ae-i{font-size:.82rem;line-height:1.55;color:var(--txt2)}
#pg-resumes .rs-ul{list-style:none;padding:0;margin:0 0 14px}
#pg-resumes .rs-ul li{font-size:.87rem;line-height:1.62;color:var(--txt2);padding:0 0 0 18px;
  margin:0 0 8px;position:relative}
#pg-resumes .rs-ul li:before{content:"";position:absolute;left:0;top:.62em;width:7px;height:7px;
  border-radius:2px;background:var(--acc)}
#pg-resumes .rs-ul.deb li:before{background:#f7a26a;border-radius:50%}
#pg-resumes .rs-sub-t{font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  color:var(--txt3);margin:0 0 7px}
#pg-resumes .rs-lien{border:1px solid var(--bdr);border-radius:10px;background:var(--s2);
  padding:10px 13px;margin:0 0 8px;cursor:pointer}
#pg-resumes .rs-lien:hover{border-color:var(--acc)}
#pg-resumes .rs-lien-n{font-size:.72rem;font-weight:800;color:var(--acc2);margin-bottom:3px}
#pg-resumes .rs-lien-p{font-size:.82rem;line-height:1.55;color:var(--txt2)}
#pg-resumes .rs-min{border:1px solid var(--bdr);border-left:3px solid var(--acc3);border-radius:12px;
  background:var(--s2);padding:15px 17px}
#pg-resumes .rs-min ol{margin:0;padding-left:20px}
#pg-resumes .rs-min li{font-size:.87rem;line-height:1.6;color:var(--txt);margin:0 0 7px}
#pg-resumes .rs-vide{color:var(--txt3);padding:40px 0;text-align:center}
@media(max-width:640px){
 #pg-resumes .rs-wrap{padding:20px 14px 70px}
 #pg-resumes .rs-h1{font-size:1.55rem}
 #pg-resumes .rs-det-t{font-size:1.25rem}
 #pg-resumes .rs-grid,#pg-resumes .rs-ae{grid-template-columns:1fr}
 #pg-resumes .rs-count{margin-left:0;width:100%}
 #pg-resumes .rs-bar{flex-direction:column;align-items:stretch}
 #pg-resumes .rs-sel,#pg-resumes .rs-in{width:100%;max-width:100%;min-width:0;flex:0 0 auto}
 #pg-resumes .rs-links{gap:6px}
 #pg-resumes .rs-lk{font-size:.74rem;padding:7px 10px}
 #pg-resumes .rs-part-h{padding:11px 12px}
 #pg-resumes .rs-part-b{padding:0 12px 11px}
 #pg-resumes .rs-part-t{font-size:.92rem}
 #pg-resumes .rs-part-c{display:none}
 #pg-resumes .rs-p,#pg-resumes .rs-sp-d{font-size:.88rem}
}
</style>
"""

SCRIPT = r"""
<script id="eco-resumes">
/* =====================================================================
   ÉcoSphère Pro — section « Résumés des chapitres » (v202, approfondie)
   Chaque résumé suit l'ordre des parties et des sous-parties du cours :
   ce que l'idée démontre, le mécanisme, les conditions et limites, puis
   la transition vers l'idée suivante. Auteurs, théories, exemples et
   chiffres sont placés là où ils servent le raisonnement, de façon à
   pouvoir reconstituer la logique du chapitre sans ouvrir le cours.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_RESUMES) return;
window.__ECO_RESUMES = true;

var D = __PAYLOAD__;
var S = {q:'', annee:'0', ch:''};
var PLIE = {};   /* chapitre -> { index de partie : true si repliée } */

function esc(t){
  return String(t == null ? '' : t).replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
/* **gras** : seule mise en forme admise dans les textes, échappés d'abord. */
function rich(t){
  return esc(t).replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
}
function nz(t){
  return String(t == null ? '' : t).toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g,'')
    .replace(/[’']/g,"'").replace(/\s+/g,' ').trim();
}
function annee(c){ return Number(c) >= 21 ? '2' : '1'; }
function libCh(c){ return D.lib[c] || ('Chapitre ' + c); }
function courtCh(c){ return Number(c) >= 21 ? '2ᵉ année — Ch. ' + (Number(c) - 20) : 'Ch. ' + c; }

function nbSp(c){
  var n = 0;
  D.ch[c].parties.forEach(function(p){ n += p.sp.length; });
  return n;
}

function blocTexte(c){
  var r = D.ch[c], b = [r.q, r.ess, libCh(c), D.titres[c] || ''];
  r.parties.forEach(function(p){
    b.push(p.t, p.v);
    p.sp.forEach(function(sp){
      b.push(sp.t);
      b = b.concat(sp.d);
      if(sp.mec) b.push(sp.mec);
      if(sp.lim) b.push(sp.lim);
    });
  });
  r.ae.forEach(function(a){ b.push(a.n, a.i); });
  b = b.concat(r.arg, r.deb, r.min);
  r.lien.forEach(function(l){ b.push(l.p); });
  return nz(b.join(' '));
}
var INDEX = {};
D.ordre.forEach(function(c){ INDEX[c] = blocTexte(c); });

function correspond(c){
  if(S.annee !== '0' && annee(c) !== S.annee) return false;
  if(!S.q) return true;
  var q = nz(S.q);
  return q.split(/\s+/).every(function(m){ return !m || INDEX[c].indexOf(m) >= 0; });
}

/* ------------------------------------------------------------ liste */
function optionsCh(){
  /* titre tronqué : le select se dimensionne sur sa plus longue option, ce qui
     ferait déborder la page sur téléphone. */
  function court(t){
    t = String(t || '');
    return t.length > 26 ? t.slice(0, 25).replace(/[\s,;:]+$/, '') + '…' : t;
  }
  return '<option value="0">Tous les chapitres</option>'
    + D.ordre.map(function(c){
        return '<option value="' + c + '">' + esc(courtCh(c)) + ' — ' + esc(court(D.titres[c]))
          + '</option>'; }).join('');
}

function carte(c){
  var r = D.ch[c];
  return '<div class="rs-card" data-ouvre="' + c + '">'
   + '<div class="rs-card-n">' + esc(libCh(c)) + '</div>'
   + '<div class="rs-card-t">' + esc(D.titres[c] || '') + '</div>'
   + '<div class="rs-card-q">' + esc(r.q) + '</div>'
   + '<div class="rs-card-m">' + r.parties.length + ' parties · ' + nbSp(c)
   + ' sous-parties · ' + r.ae.length + ' auteurs et exemples</div>'
   + '<div class="rs-card-go">Lire le résumé →</div>'
   + '</div>';
}

function rendreListe(){
  var zone = document.getElementById('rs-corps');
  if(!zone) return;
  var liste = D.ordre.filter(correspond);
  var cpt = document.getElementById('rs-count');
  if(cpt) cpt.textContent = liste.length + ' chapitre' + (liste.length > 1 ? 's' : '')
    + ' sur ' + D.ordre.length;
  if(!liste.length){
    zone.innerHTML = '<div class="rs-vide">Aucun résumé ne correspond à cette recherche.</div>';
    return;
  }
  var html = '';
  [['1', 'Première année'], ['2', 'Deuxième année']].forEach(function(an){
    var sous = liste.filter(function(c){ return annee(c) === an[0]; });
    if(!sous.length) return;
    html += '<div class="rs-year">' + esc(an[1]) + '</div><div class="rs-grid">'
         + sous.map(carte).join('') + '</div>';
  });
  zone.innerHTML = html;
}

/* ------------------------------------------------------------ détail */
function section(num, titre, corps){
  return '<div class="rs-sec"><div class="rs-sec-h"><span class="rs-sec-i">' + num + '</span>'
   + '<span class="rs-sec-t">' + esc(titre) + '</span></div>' + corps + '</div>';
}

function liens(c){
  return '<div class="rs-links">'
   + '<button class="rs-lk" data-cours="' + c + '">📖 Cours complet</button>'
   + '<button class="rs-lk" data-fiches="' + c + '">🃏 Fiches</button>'
   + '<button class="rs-lk" data-carte="' + c + '">🧠 Carte mentale</button>'
   + '<button class="rs-lk" data-atlas="' + c + '">🗺️ Atlas des idées</button>'
   + '<button class="rs-lk" data-chiffres="' + c + '">🔢 Chiffres à retenir</button>'
   + '<button class="rs-lk" data-sujets="' + c + '">📝 Sujets</button>'
   + '</div>';
}

function sousPartie(sp){
  var h = '<div class="rs-sp"><div class="rs-sp-t">' + esc(sp.t) + '</div>';
  sp.d.forEach(function(p){ h += '<p class="rs-sp-d">' + rich(p) + '</p>'; });
  if(sp.mec) h += '<div class="rs-box rs-mec"><b>Mécanisme</b>' + rich(sp.mec) + '</div>';
  if(sp.lim) h += '<div class="rs-box rs-lim"><b>Conditions et limites</b>' + rich(sp.lim)
    + '</div>';
  return h + '</div>';
}

function partie(c, p, k){
  var replie = !!(PLIE[c] && PLIE[c][k]);
  return '<div class="rs-part" id="rs-p-' + c + '-' + k + '">'
   + '<div class="rs-part-h" data-plie="' + k + '">'
   + '<span class="rs-part-x">' + (replie ? '▸' : '▾') + '</span>'
   + '<span class="rs-part-t">' + esc(p.t) + '</span>'
   + '<span class="rs-part-c">' + p.sp.length + ' point' + (p.sp.length > 1 ? 's' : '')
   + '</span></div>'
   + '<div class="rs-part-b" data-corps="' + k + '"'
   + (replie ? ' style="display:none"' : '') + '>'
   + p.sp.map(sousPartie).join('')
   + '<div class="rs-part-v"><b>Ce que cela ouvre</b>' + rich(p.v) + '</div>'
   + '</div></div>';
}

function rendreDetail(c){
  var zone = document.getElementById('rs-corps');
  var r = D.ch[c];
  if(!zone || !r) return;
  var h = '<button class="rs-back" id="rs-back">← Tous les résumés</button>'
   + '<div class="rs-det-n">' + esc(libCh(c)) + '</div>'
   + '<h2 class="rs-det-t">' + esc(D.titres[c] || '') + '</h2>'
   + liens(c);

  h += section('1', 'La question centrale', '<div class="rs-q">' + esc(r.q) + '</div>');
  h += section('2', 'L’essentiel', '<p class="rs-p">' + rich(r.ess) + '</p>');

  var plan = '<div class="rs-plan"><div class="rs-plan-t">Plan du chapitre — '
   + r.parties.length + ' parties, ' + nbSp(c) + ' sous-parties</div><ol>'
   + r.parties.map(function(p, k){
       return '<li data-va="' + k + '">' + esc(p.t) + '</li>'; }).join('')
   + '</ol></div>'
   + '<div class="rs-tools">'
   + '<button class="rs-tool" id="rs-ouvrir">Tout déplier</button>'
   + '<button class="rs-tool" id="rs-fermer">Tout replier</button>'
   + '</div>';

  h += section('3', 'Le chapitre partie par partie, dans l’ordre du cours',
    plan + r.parties.map(function(p, k){ return partie(c, p, k); }).join(''));

  h += section('4', 'Auteurs et exemples incontournables',
    '<div class="rs-ae">' + r.ae.map(function(a){
      return '<div class="rs-ae-c ' + (a.k === 'a' ? 'au' : 'ex') + '">'
        + '<div class="rs-ae-n"><span class="rs-ae-b">' + (a.k === 'a' ? 'auteur' : 'exemple')
        + '</span>' + esc(a.n) + '</div>'
        + '<div class="rs-ae-i">' + rich(a.i) + '</div></div>';
    }).join('') + '</div>');

  h += section('5', 'À mobiliser en dissertation',
    '<div class="rs-sub-t">Arguments</div><ul class="rs-ul">'
    + r.arg.map(function(x){ return '<li>' + rich(x) + '</li>'; }).join('') + '</ul>'
    + '<div class="rs-sub-t">Débats</div><ul class="rs-ul deb">'
    + r.deb.map(function(x){ return '<li>' + rich(x) + '</li>'; }).join('') + '</ul>'
    + '<div class="rs-sub-t">Liens avec les autres chapitres</div>'
    + r.lien.map(function(l){
        return '<div class="rs-lien" data-ouvre="' + l.c + '">'
          + '<div class="rs-lien-n">' + esc(courtCh(String(l.c))) + ' — '
          + esc(D.titres[String(l.c)] || '') + '</div>'
          + '<div class="rs-lien-p">' + esc(l.p) + '</div></div>'; }).join(''));

  h += section('6', 'À retenir en une minute',
    '<div class="rs-min"><ol>'
    + r.min.map(function(x){ return '<li>' + rich(x) + '</li>'; }).join('') + '</ol></div>');

  zone.innerHTML = h;
  var cpt = document.getElementById('rs-count');
  if(cpt) cpt.textContent = libCh(c) + ' · ' + r.parties.length + ' parties';
  var sel = document.getElementById('rs-ch');
  if(sel) sel.value = c;
  try{ window.scrollTo({top:0, behavior:'smooth'}); }catch(e){ window.scrollTo(0, 0); }
}

function rendre(){
  if(S.ch) rendreDetail(S.ch);
  else rendreListe();
}

function basculer(c, k, force){
  PLIE[c] = PLIE[c] || {};
  var replie = (force === undefined) ? !PLIE[c][k] : !!force;
  PLIE[c][k] = replie;
  var bloc = document.querySelector('#pg-resumes [data-corps="' + k + '"]');
  var fl = document.querySelector('#pg-resumes [data-plie="' + k + '"] .rs-part-x');
  if(bloc) bloc.style.display = replie ? 'none' : '';
  if(fl) fl.textContent = replie ? '▸' : '▾';
}

function toutes(c, replie){
  var n = D.ch[c] ? D.ch[c].parties.length : 0;
  for(var k = 0; k < n; k++) basculer(c, k, replie);
}

/* ------------------------------------------------------- construction */
function construire(){
  if(document.getElementById('pg-resumes')) return true;
  var main = document.querySelector('main');
  if(!main) return false;
  var pg = document.createElement('div');
  pg.className = 'pg'; pg.id = 'pg-resumes';
  pg.innerHTML =
   '<div class="rs-wrap">'
   + '<h1 class="rs-h1">📄 Résumés des chapitres</h1>'
   + '<p class="rs-sub">L’essentiel de chaque chapitre, organisé par année puis par chapitre, '
   + 'à relire avant un cours, un DS ou une dissertation. Chaque résumé suit l’ordre des parties '
   + 'et des sous-parties du cours : ce que l’idée démontre, son mécanisme, ses conditions et '
   + 'limites, puis la transition vers l’idée suivante, avec les auteurs, théories, exemples et '
   + 'chiffres placés là où ils servent le raisonnement. On peut ainsi reconstituer la logique du '
   + 'chapitre sans ouvrir le cours. Chaque résumé renvoie au cours complet, aux fiches, à la '
   + 'carte mentale, à l’Atlas des idées, aux chiffres et aux sujets du chapitre.</p>'
   + '<div class="rs-bar">'
   + '<input class="rs-in" id="rs-q" type="text" placeholder="Rechercher une notion, un auteur, un débat…">'
   + '<select class="rs-sel" id="rs-an"><option value="0">Les deux années</option>'
   + '<option value="1">Première année</option><option value="2">Deuxième année</option></select>'
   + '<select class="rs-sel" id="rs-ch">' + optionsCh() + '</select>'
   + '<span class="rs-count" id="rs-count"></span>'
   + '</div>'
   + '<div id="rs-corps"></div>'
   + '</div>';
  main.appendChild(pg);
  brancher();
  rendre();
  return true;
}

function ajusterBarre(){
  try{
    var etroit = window.innerWidth <= 640;
    ['rs-q', 'rs-an', 'rs-ch'].forEach(function(id){
      var e = document.getElementById(id);
      if(!e) return;
      if(etroit){
        /* en colonne, « flex: 1 1 280px » s'applique à la hauteur : il faut le
           neutraliser, sinon le champ de recherche occupe tout l'écran. */
        e.style.setProperty('width', '100%', 'important');
        e.style.setProperty('max-width', '100%', 'important');
        e.style.setProperty('min-width', '0', 'important');
        e.style.setProperty('flex', '0 0 auto', 'important');
        e.style.setProperty('height', 'auto', 'important');
      }else{
        e.style.removeProperty('width');
        e.style.removeProperty('max-width');
        e.style.removeProperty('min-width');
        e.style.removeProperty('flex');
        e.style.removeProperty('height');
      }
    });
    var bar = document.querySelector('#pg-resumes .rs-bar');
    if(bar){
      if(etroit){
        bar.style.setProperty('flex-direction', 'column', 'important');
        bar.style.setProperty('align-items', 'stretch', 'important');
      }else{
        bar.style.removeProperty('flex-direction');
        bar.style.removeProperty('align-items');
      }
    }
  }catch(e){}
}
window.addEventListener('resize', ajusterBarre);

function brancher(){
  ajusterBarre();
  var q = document.getElementById('rs-q');
  if(q) q.addEventListener('input', function(){
    S.q = this.value; S.ch = ''; rendre();
  });
  var an = document.getElementById('rs-an');
  if(an) an.addEventListener('change', function(){
    S.annee = this.value; S.ch = ''; rendre();
  });
  var ch = document.getElementById('rs-ch');
  if(ch) ch.addEventListener('change', function(){
    S.ch = this.value === '0' ? '' : this.value;
    rendre();
  });
  var corps = document.getElementById('rs-corps');
  if(corps) corps.addEventListener('click', function(ev){
    var n;
    if(ev.target.closest('#rs-ouvrir')){ toutes(S.ch, false); return; }
    if(ev.target.closest('#rs-fermer')){ toutes(S.ch, true); return; }
    if((n = ev.target.closest('[data-va]'))){
      var k = n.getAttribute('data-va');
      basculer(S.ch, Number(k), false);
      var cible = document.getElementById('rs-p-' + S.ch + '-' + k);
      if(cible){
        try{ cible.scrollIntoView({behavior:'smooth', block:'start'}); }
        catch(e){ cible.scrollIntoView(); }
      }
      return;
    }
    if((n = ev.target.closest('[data-plie]'))){
      basculer(S.ch, Number(n.getAttribute('data-plie')));
      return;
    }
    var o = ev.target.closest('[data-ouvre]');
    if(o){ S.ch = o.getAttribute('data-ouvre'); S.q = '';
      var i = document.getElementById('rs-q'); if(i) i.value = '';
      rendre(); return; }
    if(ev.target.closest('#rs-back')){
      S.ch = '';
      var sel = document.getElementById('rs-ch'); if(sel) sel.value = '0';
      rendre(); return;
    }
    if((n = ev.target.closest('[data-cours]'))){
      try{ openCh(Number(n.getAttribute('data-cours'))); }catch(e){}
      return;
    }
    if((n = ev.target.closest('[data-fiches]'))){
      var nf = Number(n.getAttribute('data-fiches'));
      try{ showPg('fc'); }catch(e){}
      setTimeout(function(){ try{ if(typeof filterFC === 'function') filterFC(nf); }catch(e){} }, 220);
      return;
    }
    if((n = ev.target.closest('[data-carte]'))){
      var nc = Number(n.getAttribute('data-carte'));
      try{ showPg('maps'); }catch(e){}
      setTimeout(function(){
        try{ if(typeof renderVisualMap === 'function') renderVisualMap(nc); }catch(e){}
      }, 240);
      return;
    }
    if((n = ev.target.closest('[data-atlas]'))){
      var na = n.getAttribute('data-atlas');
      try{ showPg('atlas'); }catch(e){}
      setTimeout(function(){
        try{
          var s = document.getElementById('at-ch');
          if(s){
            var ok = false;
            for(var k2 = 0; k2 < s.options.length; k2++){
              if(String(s.options[k2].value) === String(na)){ s.value = na; ok = true; break; }
            }
            if(ok) s.dispatchEvent(new Event('change', {bubbles:true}));
          }
        }catch(e){}
      }, 260);
      return;
    }
    if((n = ev.target.closest('[data-chiffres]'))){
      try{ ouvrirChiffres(String(n.getAttribute('data-chiffres'))); }catch(e){}
      return;
    }
    if((n = ev.target.closest('[data-sujets]'))){
      var ns = Number(n.getAttribute('data-sujets'));
      try{ showPg('subjects'); }catch(e){}
      setTimeout(function(){
        try{
          if(typeof setSubjectChapterPremium === 'function') setSubjectChapterPremium(ns);
        }catch(e){}
      }, 240);
      return;
    }
  });
}

function poserNav(){
  if(document.getElementById('rs-nav')) return;
  var nav = document.querySelector('nav');
  if(!nav) return;
  var ref = null;
  nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'chiffres'") >= 0) ref = b;
  });
  if(!ref) nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'frise'") >= 0) ref = b;
  });
  var b = document.createElement('button');
  b.className = 'nt'; b.id = 'rs-nav';
  b.setAttribute('onclick', "showPg('resumes')");
  b.textContent = '📄 Résumés';
  if(ref && ref.nextSibling) nav.insertBefore(b, ref.nextSibling);
  else nav.appendChild(b);
}

/* --------------------------------------- indexation dans la recherche */
function indexer(){
  try{
    if(typeof SEARCH_INDEX === 'undefined') return;
    if(SEARCH_INDEX.some(function(x){ return x.type === 'résumé'; })) return;
    D.ordre.forEach(function(c){
      var r = D.ch[c];
      SEARCH_INDEX.push({
        type: 'résumé',
        term: 'Résumé — ' + (D.titres[c] || libCh(c)),
        def: r.q,
        ch: Number(c),
        action: "ouvrirResume('" + c + "')",
        explain: r.ess.slice(0, 400),
        source: libCh(c)
      });
    });
  }catch(e){}
}

/* la recherche globale est servie par buildSearch48 : on injecte après coup */
function scoreRs(c, q, mots){
  var r = D.ch[c];
  var t = nz((D.titres[c] || '') + ' ' + libCh(c));
  var hay = INDEX[c];
  var sc = 0;
  if(t.indexOf(q) >= 0) sc += 160;
  if(nz(r.q).indexOf(q) >= 0) sc += 120;
  mots.forEach(function(m){
    if(!m) return;
    if(t.indexOf(m) >= 0) sc += 40;
    if(hay.indexOf(m) >= 0) sc += 22;
  });
  return sc;
}

function injecter(){
  try{
    var box = document.getElementById('search-res');
    if(!box) return;
    if(box.querySelector('[data-rs]')) return;
    var si = document.getElementById('si');
    var raw = si ? si.value : '';
    if(!raw || raw.trim().length < 2) return;
    if(typeof SEARCH_FILTER !== 'undefined' && SEARCH_FILTER !== 'all') return;
    var q = nz(raw), mots = q.split(/\s+/).filter(Boolean);
    var res = D.ordre.map(function(c){ return {c:c, sc:scoreRs(c, q, mots)}; })
      .filter(function(r){ return r.sc >= 44; })
      .sort(function(a, b){ return b.sc - a.sc; })
      .slice(0, 5);
    if(!res.length) return;
    box.insertAdjacentHTML('afterbegin', res.map(function(r){
      var x = D.ch[r.c];
      return '<div class="ri" data-rs="1" onclick="ouvrirResume(\'' + r.c + '\')">'
        + '<div class="ri-type">résumé · ' + esc(libCh(r.c)) + '</div>'
        + '<div class="ri-term">Résumé — ' + esc(D.titres[r.c] || '') + '</div>'
        + '<div class="ri-def">' + esc(x.q) + '</div>'
        + '<div class="ri-src">' + esc(x.parties.length + ' parties · ' + nbSp(r.c)
        + ' sous-parties') + '</div></div>';
    }).join(''));
  }catch(e){}
}
if(typeof window.doSearch === 'function' && !window.doSearch.__rs){
  var vieuxS = window.doSearch;
  window.doSearch = function(){
    var r = vieuxS.apply(this, arguments);
    try{ injecter(); }catch(e){}
    return r;
  };
  window.doSearch.__rs = 1;
}

window.ouvrirResume = function(c){
  S.q = ''; S.annee = '0'; S.ch = c ? String(c) : '';
  try{ showPg('resumes'); }catch(e){}
  setTimeout(function(){
    var i = document.getElementById('rs-q'); if(i) i.value = '';
    rendre();
  }, 120);
};

function majHauteurNav(){
  try{
    var nav = document.querySelector('nav');
    if(!nav) return;
    /* seize onglets : la barre passe à la ligne, et le décalage du contenu
       suit sa hauteur réelle (l'application est en quirks mode, d'où les
       styles en ligne marqués important). */
    nav.style.setProperty('flex-wrap', 'wrap', 'important');
    nav.style.setProperty('height', 'auto', 'important');
    nav.style.setProperty('row-gap', '5px', 'important');
    nav.style.setProperty('padding-top', '7px', 'important');
    nav.style.setProperty('padding-bottom', '7px', 'important');
    nav.style.setProperty('overflow-x', 'visible', 'important');
    var h = Math.round(nav.getBoundingClientRect().height);
    if(h > 0){
      document.documentElement.style.setProperty('--eco-nav-h', h + 'px');
      var m = document.querySelector('main');
      if(m) m.style.setProperty('padding-top', h + 'px', 'important');
    }
  }catch(e){}
}
try{
  majHauteurNav();
  window.addEventListener('resize', majHauteurNav);
  var navEl = document.querySelector('nav');
  if(navEl && window.ResizeObserver) new ResizeObserver(majHauteurNav).observe(navEl);
}catch(e){}

function boot(){
  try{
    if(construire()){ poserNav(); indexer(); majHauteurNav(); ajusterBarre(); }
  }catch(e){ try{ console.warn('[résumés]', e); }catch(_){} }
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
[300, 900, 2000, 3500, 6000, 9500].forEach(function(t){ setTimeout(boot, t); });
[300, 1200, 3000, 7000, 11000].forEach(function(t){ setTimeout(majHauteurNav, t); });

if(typeof window.rebuildSearchIndex === 'function' && !window.rebuildSearchIndex.__rs){
  var vieux = window.rebuildSearchIndex;
  window.rebuildSearchIndex = function(){
    var r = vieux.apply(this, arguments);
    try{ indexer(); }catch(e){}
    return r;
  };
  window.rebuildSearchIndex.__rs = 1;
}

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    if(pg === 'resumes'){
      boot();
      document.querySelectorAll('.pg').forEach(function(p){ p.classList.remove('on'); });
      document.querySelectorAll('.nt').forEach(function(t){ t.classList.remove('on'); });
      var el = document.getElementById('pg-resumes');
      if(el) el.classList.add('on');
      var nb = document.getElementById('rs-nav');
      if(nb) nb.classList.add('on');
      setTimeout(rendre, 30);
      return;
    }
    return old.apply(this, arguments);
  };
}

window.__ECO_RESUMES_N = D.ordre.length;
setTimeout(function(){
  var np = 0, ns = 0;
  D.ordre.forEach(function(c){ np += D.ch[c].parties.length; ns += nbSp(c); });
  console.log('[ÉcoSphère v202] Résumés approfondis — ' + D.ordre.length + ' chapitres, '
    + np + ' parties, ' + ns + ' sous-parties');
}, 7000);
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', json.dumps(PAYLOAD, ensure_ascii=False, separators=(',', ':')))
s = s.rstrip() + '\n' + CSS.strip() + '\n\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)

print('  %d résumés approfondis, un par chapitre intégré' % len(ORDRE))
tp = ts = 0
for c in ORDRE:
    r = R[c]
    st = stats[c]
    tp += st['parties']
    ts += st['sp']
    print('    %-22s %2d parties · %3d sous-parties · %2d auteurs et exemples · '
          '%2d arguments · %2d débats · %d liens · %2d points · %6d signes'
          % (LIB.get(c, 'Chapitre ' + c), st['parties'], st['sp'], len(r['ae']), len(r['arg']),
             len(r['deb']), len(r['lien']), len(r['min']), st['signes']))
print('  total : %d parties, %d sous-parties, %d signes' % (tp, ts, sum(x['signes'] for x in stats.values())))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
