#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Section « Chiffres à retenir » : les données chiffrées utiles en dissertation,
classées par année, par chapitre et par degré de priorité.

v200 : le titre de chaque carte énonce ce que mesure le chiffre, la zone, la
période puis la valeur avec son unité — la donnée doit se comprendre à la seule
lecture du titre.
v203 : ajout du chapitre 4 de deuxième année (dix chiffres prioritaires et dix
chiffres complémentaires).
"""
import io, json, re

import chif_a, chif_b, chif_c, chif_d, titres_chif, titres_ch24

SRC = 'app_v198.html'
DST = 'app_v203.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-chiffres' not in s

ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '21', '22', '23', '24']
LIB = {'21': '2ᵉ année — Chapitre 1', '22': '2ᵉ année — Chapitre 2',
       '23': '2ᵉ année — Chapitre 3', '24': '2ᵉ année — Chapitre 4'}
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
 '24': "Régionalisation, gouvernance et régulations internationales",
}

D = {}
for src in (chif_a.CH, chif_b.CH, chif_c.CH, chif_d.CH):
    D.update(src)

# ------------------------------------- titre explicite de chaque carte
# Mesure + zone + periode + valeur : le titre doit se lire seul.
T = dict(titres_chif.T)
T.update(titres_ch24.T)
# Les regles, modeles, typologies et seuils institutionnels ne portent pas
# d'annee : c'est le cas de l'exemple donne par l'utilisateur (Maastricht).
SANS_ANNEE = frozenset((
    'seuils institutionnels', 'objectif institutionnel', 'marge institutionnelle',
    'règle institutionnelle', 'seuil', 'seuils', 'coefficient', 'maturités',
    'modèle', 'typologie', 'conditions du modèle', 'hypothèses du modèle',
    'seuils analytiques', 'propriété analytique', 'seuil analytique',
    'durée institutionnelle', 'règle de calcul', 'indice', 'matrice de gains',
    'base juridique', 'seuils conventionnels', 'durée', 'taux',
))
RE_PERIODE = re.compile(
    r'\b(1[5-9]\d\d|20\d\d)\b|XV|XVI|XVII|XVIII|XIX|XX|'
    r'années \d{4}|non datée|non précisé|tendance récente|ordre de grandeur|'
    r'aujourd’hui|modèle|théorie|typologie|exemple|règle|convention|'
    r'protocole|mandat|cours pivot|période|horizon|estimation du cours|'
    r'étudié par le cours|récente du cours|cas étudié|projet|travaux|'
    r'ordres de grandeur|année non|sans année précisée|rapport Draghi|'
    r'études citées|avant 1914')

# ------------------------------------------------------------- contrôles
SUIVI = {'datés': 0, 'règles': 0}
total = 0
for c in ORDRE:
    assert c in D, c
    for rang, x in enumerate(D[c]['prio'] + D[c]['comp'], 1):
        imp = 'p' if rang <= len(D[c]['prio']) else 'c'
        cle = '%s%s%d' % (c, imp, rang if imp == 'p' else rang - len(D[c]['prio']))
        titre = T.get(cle)
        assert titre, ('titre manquant', cle)
        assert ' : ' in titre, ('titre sans valeur annoncée', cle)
        assert 40 < len(titre) < 280, ('titre hors gabarit', cle, len(titre))
        # la periode doit figurer dans le titre lui-meme, pas seulement
        # dans l'etiquette ou le texte explicatif ; seules les regles, modeles
        # et seuils institutionnels en sont dispenses, comme les criteres de
        # Maastricht donnes en exemple par l'utilisateur.
        if x['nat'] not in SANS_ANNEE:
            assert RE_PERIODE.search(titre), ('période absente du titre', cle, titre)
            SUIVI['datés'] += 1
        else:
            SUIVI['règles'] += 1
        x['t'] = titre
        for k in ('v', 'u', 'nat', 'z', 'p', 's', 'd', 'q', 'k'):
            assert x.get(k), (c, k)
        assert len(x['d']) > 80 and len(x['q']) > 120, (c, x['v'])
        assert isinstance(x['k'], list) and len(x['k']) >= 3
    assert len(D[c]['prio']) <= 10 and len(D[c]['comp']) <= 10, c
    total += len(D[c]['prio']) + len(D[c]['comp'])
assert total > 210, total
assert len(T) == total, (len(T), total)

# Les notions proches doivent etre nommees dans le titre : dette ou deficit,
# stock ou flux, montant en euros ou pourcentage du PIB.
PAIRES = [
 ('1p1', ('dette', 'stock', '% du PIB', 'milliards')),
 ('1p2', ('éficit', 'annuel', '2024', 'milliards')),
 ('1p3', ('déficit public annuel', 'stock de dette', '3 %', '60 %')),
 ('1p4', ('harge d’intérêts', '2019', '% du PIB')),
 ('7p6', ('stock',)),
 ('7p7', ('% du PIB',)),
 ('21p6', ('% du PIB',)),
 ('22c4', ('stock d’IDE', '2024')),
]
for cle, mots in PAIRES:
    for m in mots:
        assert m.lower() in T[cle].lower(), ('distinction absente', cle, m)
# aucun titre ne doit se reduire a un nombre
for cle, titre in T.items():
    av = titre.split(' : ')[0]
    assert len(av) > 18 and not av.strip().rstrip('%').replace(' ', '').isdigit(), (cle, av)

PAYLOAD = {'ordre': ORDRE, 'lib': LIB, 'titres': TITRES,
           'ch': {c: {'p': D[c]['prio'], 'c': D[c]['comp']} for c in ORDRE}}

CSS = """
<style id="eco-chiffres-css">
#pg-chiffres .cf-wrap{max-width:1180px;margin:0 auto;padding:26px 18px 70px}
#pg-chiffres .cf-h1{font-size:2rem;font-weight:800;margin:0 0 6px}
#pg-chiffres .cf-sub{color:var(--txt2);margin:0 0 20px;line-height:1.55;max-width:820px}
#pg-chiffres .cf-bar{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
#pg-chiffres .cf-in{flex:1 1 280px;min-width:220px;padding:11px 14px;border-radius:10px;
  border:1px solid var(--bdr);background:var(--s2);color:var(--txt);font-family:inherit;font-size:.9rem}
#pg-chiffres .cf-sel{padding:11px 12px;border-radius:10px;border:1px solid var(--bdr);
  background:var(--s2);color:var(--txt);font-family:inherit;font-size:.85rem;cursor:pointer}
#pg-chiffres .cf-count{color:var(--txt3);font-size:.82rem;margin-left:auto}
#pg-chiffres .cf-chips{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:22px}
#pg-chiffres .cf-chip{padding:7px 13px;border-radius:999px;border:1px solid var(--bdr);
  background:var(--s2);color:var(--txt2);font-size:.78rem;cursor:pointer;font-family:inherit;transition:all .15s}
#pg-chiffres .cf-chip:hover{color:var(--txt);border-color:var(--acc)}
#pg-chiffres .cf-chip.on{background:var(--acc);border-color:var(--acc);color:#fff;font-weight:600}
#pg-chiffres .cf-grp{margin:0 0 34px}
#pg-chiffres .cf-grp-h{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;
  padding:0 0 10px;border-bottom:1px solid var(--bdr);margin-bottom:16px}
#pg-chiffres .cf-grp-n{font-size:.72rem;font-weight:900;letter-spacing:.11em;text-transform:uppercase;color:var(--acc2)}
#pg-chiffres .cf-grp-t{font-size:1.1rem;font-weight:700}
#pg-chiffres .cf-grp-a{margin-left:auto;display:flex;gap:7px}
#pg-chiffres .cf-lk{padding:5px 11px;border-radius:8px;border:1px solid var(--bdr);background:var(--s2);
  color:var(--txt2);font-size:.75rem;cursor:pointer;font-family:inherit}
#pg-chiffres .cf-lk:hover{color:var(--txt);border-color:var(--acc)}
#pg-chiffres .cf-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}
#pg-chiffres .cf-card{border:1px solid var(--bdr);border-radius:13px;background:var(--s2);
  padding:16px 17px;display:flex;flex-direction:column;gap:9px}
#pg-chiffres .cf-card.prio{border-left:3px solid var(--acc)}
#pg-chiffres .cf-card.comp{border-left:3px solid var(--bdr)}
#pg-chiffres .cf-top{display:flex;align-items:flex-start;gap:10px}
#pg-chiffres .cf-rk{flex:0 0 auto;min-width:26px;height:26px;border-radius:7px;display:flex;
  align-items:center;justify-content:center;font-size:.72rem;font-weight:800;
  background:rgba(124,106,247,.14);color:var(--acc2);padding:0 6px}
#pg-chiffres .cf-card.comp .cf-rk{background:rgba(148,163,184,.14);color:var(--txt3)}
#pg-chiffres .cf-t{font-size:.97rem;font-weight:800;line-height:1.38}
#pg-chiffres .cf-u{color:var(--txt2);font-size:.78rem;line-height:1.45;margin-top:4px}
#pg-chiffres .cf-u b{color:var(--txt3);font-weight:700;font-size:.68rem;
  text-transform:uppercase;letter-spacing:.07em}
#pg-chiffres .cf-meta{display:flex;gap:6px;flex-wrap:wrap}
#pg-chiffres .cf-b{font-size:.68rem;padding:3px 8px;border-radius:999px;border:1px solid var(--bdr);color:var(--txt3)}
#pg-chiffres .cf-b.nat{color:var(--acc3);border-color:rgba(106,247,196,.3)}
#pg-chiffres .cf-b.z{color:#f7a26a;border-color:rgba(247,162,106,.3)}
#pg-chiffres .cf-b.p{color:#6ab8f7;border-color:rgba(106,184,247,.3)}
#pg-chiffres .cf-src{font-size:.74rem;color:var(--txt3);font-style:italic;line-height:1.45}
#pg-chiffres .cf-sec{font-size:.83rem;line-height:1.55;color:var(--txt2)}
#pg-chiffres .cf-sec b{color:var(--txt);font-weight:700;display:block;font-size:.7rem;
  text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px;color:var(--txt3)}
#pg-chiffres .cf-q{font-size:.83rem;line-height:1.55;color:var(--txt);
  border-left:2px solid var(--acc);padding-left:11px}
#pg-chiffres .cf-tags{display:flex;gap:5px;flex-wrap:wrap;margin-top:1px}
#pg-chiffres .cf-tag{font-size:.66rem;color:var(--txt3);background:rgba(148,163,184,.1);
  padding:2px 7px;border-radius:5px;cursor:pointer}
#pg-chiffres .cf-tag:hover{color:var(--acc2)}
#pg-chiffres .cf-vide{color:var(--txt3);padding:40px 0;text-align:center}
#pg-chiffres .cf-note{color:var(--txt3);font-size:.78rem;margin:-6px 0 18px;line-height:1.5}
@media(max-width:640px){#pg-chiffres .cf-cards{grid-template-columns:1fr}
 #pg-chiffres .cf-count{margin-left:0;width:100%}}
/* quinze sections ne tiennent plus sur une seule ligne : la barre passe
   à la ligne et le décalage du contenu suit sa hauteur réelle. */
nav{height:auto;min-height:58px;flex-wrap:wrap;row-gap:5px;padding-top:7px;padding-bottom:7px}
main{padding-top:var(--eco-nav-h,58px)}
</style>
"""

SCRIPT = r"""
<script id="eco-chiffres">
/* =====================================================================
   ÉcoSphère Pro — section « Chiffres à retenir » (v199)
   Les données chiffrées des documents de cours, classées par année, par
   chapitre et par priorité, avec recherche, filtres et liens vers le
   cours et les fiches.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_CHIFFRES) return;
window.__ECO_CHIFFRES = true;

var D = __PAYLOAD__;
var S = {q:'', annee:'0', ch:'0', imp:'0'};

function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(m){
  return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]; }); }
function nz(s){ return String(s == null ? '' : s).normalize('NFD')
  .replace(/[̀-ͯ]/g,'').toLowerCase(); }
function libCh(c){ return D.lib[c] || ('Chapitre ' + c); }
function courtCh(c){ return D.lib[c] ? ('2ᵉ année — Ch. ' + (Number(c) - 20)) : ('Ch. ' + c); }
function annee(c){ return Number(c) >= 21 ? '2' : '1'; }

/* ------------------------------------------------- collecte et filtrage */
function tous(){
  var out = [];
  D.ordre.forEach(function(c){
    (D.ch[c].p || []).forEach(function(x, i){ out.push({ch:c, imp:'p', rang:i + 1, x:x}); });
    (D.ch[c].c || []).forEach(function(x, i){ out.push({ch:c, imp:'c', rang:i + 1, x:x}); });
  });
  return out;
}
function correspond(it){
  if(S.annee !== '0' && annee(it.ch) !== S.annee) return false;
  if(S.ch !== '0' && it.ch !== S.ch) return false;
  if(S.imp !== '0' && it.imp !== S.imp) return false;
  if(!S.q) return true;
  var q = nz(S.q);
  var x = it.x;
  var bloc = nz([x.t || '', x.v, x.u, x.nat, x.z, x.p, x.s, x.d, x.q, (x.k || []).join(' '),
                 libCh(it.ch), D.titres[it.ch] || ''].join(' '));
  return q.split(/\s+/).every(function(m){ return !m || bloc.indexOf(m) >= 0; });
}

/* ------------------------------------------------------------- rendu */
function carte(it){
  var x = it.x;
  return '<div class="cf-card ' + (it.imp === 'p' ? 'prio' : 'comp') + '">'
   + '<div class="cf-top"><span class="cf-rk">' + (it.imp === 'p' ? '' : 'c') + it.rang + '</span>'
   + '<div><div class="cf-t">' + esc(x.t || x.v) + '</div>'
   + '<div class="cf-u"><b>Précision</b> ' + esc(x.u) + '</div></div></div>'
   + '<div class="cf-meta"><span class="cf-b nat">' + esc(x.nat) + '</span>'
   + '<span class="cf-b z">' + esc(x.z) + '</span>'
   + '<span class="cf-b p">' + esc(x.p) + '</span></div>'
   + '<div class="cf-src">Source : ' + esc(x.s) + '</div>'
   + '<div class="cf-sec"><b>Ce que la donnée démontre</b>' + esc(x.d) + '</div>'
   + '<div class="cf-q">' + esc(x.q) + '</div>'
   + '<div class="cf-tags">' + (x.k || []).map(function(t){
       return '<span class="cf-tag" data-t="' + esc(t) + '">' + esc(t) + '</span>'; }).join('')
   + '</div></div>';
}

function rendre(){
  var zone = document.getElementById('cf-liste');
  if(!zone) return;
  var liste = tous().filter(correspond);
  var cpt = document.getElementById('cf-count');
  if(cpt) cpt.textContent = liste.length + ' chiffre' + (liste.length > 1 ? 's' : '')
    + ' sur ' + tous().length;
  if(!liste.length){
    zone.innerHTML = '<div class="cf-vide">Aucun chiffre ne correspond à cette recherche.</div>';
    return;
  }
  var par = {};
  liste.forEach(function(it){ (par[it.ch] = par[it.ch] || []).push(it); });
  zone.innerHTML = D.ordre.filter(function(c){ return par[c]; }).map(function(c){
    var np = par[c].filter(function(i){ return i.imp === 'p'; }).length;
    var nc = par[c].length - np;
    return '<div class="cf-grp"><div class="cf-grp-h">'
      + '<span class="cf-grp-n">' + esc(libCh(c)) + '</span>'
      + '<span class="cf-grp-t">' + esc(D.titres[c] || '') + '</span>'
      + '<span class="cf-grp-a">'
      + '<button class="cf-lk" data-cours="' + c + '">📖 Cours</button>'
      + '<button class="cf-lk" data-fiches="' + c + '">🃏 Fiches</button>'
      + '</span></div>'
      + '<div class="cf-note">' + np + ' prioritaire' + (np > 1 ? 's' : '')
      + (nc ? ' · ' + nc + ' complémentaire' + (nc > 1 ? 's' : '') : '') + '</div>'
      + '<div class="cf-cards">' + par[c].map(carte).join('') + '</div></div>';
  }).join('');
}

/* ------------------------------------------------------- page et nav */
function optionsCh(){
  return '<option value="0">Tous les chapitres</option>'
    + D.ordre.map(function(c){
        return '<option value="' + c + '">' + esc(libCh(c)) + '</option>'; }).join('');
}

function construire(){
  if(document.getElementById('pg-chiffres')) return true;
  var main = document.querySelector('main');
  if(!main) return false;
  var n = tous().length;
  var pg = document.createElement('div');
  pg.className = 'pg'; pg.id = 'pg-chiffres';
  pg.innerHTML =
   '<div class="cf-wrap">'
   + '<h1 class="cf-h1">🔢 Chiffres à retenir</h1>'
   + '<p class="cf-sub">' + n + ' données chiffrées tirées des documents de cours, classées par année '
   + 'puis par chapitre. Dix chiffres prioritaires par chapitre, puis des chiffres complémentaires. '
   + 'Chaque donnée précise son unité, sa nature — stock, flux annuel, taux, part —, la zone concernée, '
   + 'la période, la source du document, ce qu’elle démontre et une phrase directement mobilisable en copie.</p>'
   + '<div class="cf-bar">'
   + '<input class="cf-in" id="cf-q" type="text" placeholder="Rechercher un chiffre, une notion, une zone, une source…">'
   + '<select class="cf-sel" id="cf-an"><option value="0">Les deux années</option>'
   + '<option value="1">Première année</option><option value="2">Deuxième année</option></select>'
   + '<select class="cf-sel" id="cf-ch">' + optionsCh() + '</select>'
   + '<select class="cf-sel" id="cf-imp"><option value="0">Tous les chiffres</option>'
   + '<option value="p">Prioritaires seulement</option><option value="c">Complémentaires seulement</option></select>'
   + '<span class="cf-count" id="cf-count"></span>'
   + '</div>'
   + '<div class="cf-chips" id="cf-chips">'
   + '<button class="cf-chip on" data-ch="0">Tous</button>'
   + D.ordre.map(function(c){
       return '<button class="cf-chip" data-ch="' + c + '">' + esc(courtCh(c)) + '</button>'; }).join('')
   + '</div>'
   + '<div id="cf-liste"></div>'
   + '</div>';
  main.appendChild(pg);
  brancher();
  rendre();
  return true;
}

function majChips(){
  var b = document.getElementById('cf-chips');
  if(!b) return;
  b.querySelectorAll('.cf-chip').forEach(function(x){
    x.classList.toggle('on', x.getAttribute('data-ch') === S.ch);
  });
  var sel = document.getElementById('cf-ch');
  if(sel && sel.value !== S.ch) sel.value = S.ch;
}

function brancher(){
  var q = document.getElementById('cf-q');
  if(q) q.addEventListener('input', function(){ S.q = this.value; rendre(); });
  var an = document.getElementById('cf-an');
  if(an) an.addEventListener('change', function(){ S.annee = this.value; rendre(); });
  var ch = document.getElementById('cf-ch');
  if(ch) ch.addEventListener('change', function(){ S.ch = this.value; majChips(); rendre(); });
  var im = document.getElementById('cf-imp');
  if(im) im.addEventListener('change', function(){ S.imp = this.value; rendre(); });
  var chips = document.getElementById('cf-chips');
  if(chips) chips.addEventListener('click', function(ev){
    var b = ev.target.closest('.cf-chip');
    if(!b) return;
    S.ch = b.getAttribute('data-ch');
    if(S.ch !== '0') S.annee = '0';
    var sa = document.getElementById('cf-an'); if(sa) sa.value = S.annee;
    majChips(); rendre();
  });
  var liste = document.getElementById('cf-liste');
  if(liste) liste.addEventListener('click', function(ev){
    var t = ev.target.closest('.cf-tag');
    if(t){ S.q = t.getAttribute('data-t');
      var i = document.getElementById('cf-q'); if(i) i.value = S.q;
      rendre(); window.scrollTo({top:0, behavior:'smooth'}); return; }
    var c = ev.target.closest('[data-cours]');
    if(c){ try{ openCh(Number(c.getAttribute('data-cours'))); }catch(e){} return; }
    var f = ev.target.closest('[data-fiches]');
    if(f){
      var n = Number(f.getAttribute('data-fiches'));
      try{ showPg('fc'); }catch(e){}
      setTimeout(function(){ try{ if(typeof filterFC === 'function') filterFC(n); }catch(e){} }, 220);
      return;
    }
  });
}

function poserNav(){
  if(document.getElementById('cf-nav')) return;
  var nav = document.querySelector('nav');
  if(!nav) return;
  var ref = null;
  nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'frise'") >= 0) ref = b;
  });
  if(!ref) nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'formulas'") >= 0) ref = b;
  });
  var b = document.createElement('button');
  b.className = 'nt'; b.id = 'cf-nav';
  b.setAttribute('onclick', "showPg('chiffres')");
  b.textContent = '🔢 Chiffres';
  if(ref && ref.nextSibling) nav.insertBefore(b, ref.nextSibling);
  else nav.appendChild(b);
}

/* ----------------------------------------- indexation dans la recherche */
function indexer(){
  try{
    if(typeof SEARCH_INDEX === 'undefined') return;
    if(SEARCH_INDEX.some(function(x){ return x.type === 'chiffre'; })) return;
    tous().forEach(function(it){
      var x = it.x;
      SEARCH_INDEX.push({
        type: 'chiffre',
        term: x.t || x.v,
        def: x.u + ' · ' + x.z + ' · ' + x.p + '. ' + x.d,
        ch: Number(it.ch),
        action: "ouvrirChiffres('" + String(it.ch) + "')",
        explain: x.q,
        source: x.s
      });
    });
  }catch(e){}
}
/* la recherche globale est servie par buildSearch48, qui relit ses propres
   sources : on injecte donc nos résultats après coup, en tête de liste. */
function scoreCf(it, q, mots){
  var x = it.x;
  var t = nz(x.v);
  var hay = nz([x.t || '', x.v, x.u, x.nat, x.z, x.p, x.s, x.d, x.q,
                (x.k || []).join(' ')].join(' '));
  var sc = 0;
  if(t === q) sc += 300;
  if(t.indexOf(q) >= 0) sc += 180;
  if(hay.indexOf(q) >= 0) sc += 90;
  mots.forEach(function(m){
    if(!m) return;
    if(t.split(' ').indexOf(m) >= 0) sc += 35;
    else if(hay.indexOf(m) >= 0) sc += 10;
  });
  if(it.imp === 'p') sc += 8;
  return sc;
}
function injecter(){
  try{
    var input = document.getElementById('si');
    var box = document.getElementById('search-res');
    if(!input || !box) return;
    var raw = (input.value || '').trim();
    if(!raw) return;
    if(box.querySelector('[data-cf]')) return;
    if(typeof SEARCH_FILTER !== 'undefined' && SEARCH_FILTER !== 'all') return;
    var q = nz(raw), mots = q.split(/\s+/).filter(Boolean);
    var res = tous().map(function(it){ return {it:it, sc:scoreCf(it, q, mots)}; })
      .filter(function(r){ return r.sc >= 40; })
      .sort(function(a, b){ return b.sc - a.sc; })
      .slice(0, 10);
    if(!res.length) return;
    box.insertAdjacentHTML('afterbegin', res.map(function(r){
      var x = r.it.x;
      return '<div class="ri" data-cf="1" onclick="ouvrirChiffres(\'' + r.it.ch + '\')">'
        + '<div class="ri-type">chiffre · ' + esc(libCh(r.it.ch))
        + (r.it.imp === 'p' ? ' · prioritaire' : ' · complémentaire') + '</div>'
        + '<div class="ri-term">' + esc(x.t || x.v) + '</div>'
        + '<div class="ri-def">' + esc(x.u + ' · ' + x.z + ' · ' + x.p + ' — ' + x.d) + '</div>'
        + '<div class="ri-src">Source : ' + esc(x.s) + '</div></div>';
    }).join(''));
  }catch(e){}
}
if(typeof window.doSearch === 'function' && !window.doSearch.__cf){
  var vieuxS = window.doSearch;
  window.doSearch = function(){
    var r = vieuxS.apply(this, arguments);
    try{ injecter(); }catch(e){}
    return r;
  };
  window.doSearch.__cf = 1;
}

window.ouvrirChiffres = function(c){
  S.q = ''; S.imp = '0'; S.annee = '0'; S.ch = String(c || '0');
  try{ showPg('chiffres'); }catch(e){}
  setTimeout(function(){
    var i = document.getElementById('cf-q'); if(i) i.value = '';
    majChips(); rendre();
  }, 120);
};

function majHauteurNav(){
  try{
    var nav = document.querySelector('nav');
    if(!nav) return;
    /* quinze onglets ne tiennent plus sur une ligne : on force le retour à la
       ligne en style en ligne, seul moyen sûr face aux couches successives. */
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
    if(construire()){ poserNav(); indexer(); majHauteurNav(); }
  }catch(e){ try{ console.warn('[chiffres]', e); }catch(_){} }
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
[300, 900, 2000, 3500, 6000, 9500].forEach(function(t){ setTimeout(boot, t); });
[300, 1200, 3000, 7000, 11000].forEach(function(t){ setTimeout(majHauteurNav, t); });

/* la reconstruction de l'index vide le tableau : on réinjecte ensuite */
if(typeof window.rebuildSearchIndex === 'function' && !window.rebuildSearchIndex.__cf){
  var vieux = window.rebuildSearchIndex;
  window.rebuildSearchIndex = function(){
    var r = vieux.apply(this, arguments);
    try{ indexer(); }catch(e){}
    return r;
  };
  window.rebuildSearchIndex.__cf = 1;
}

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    if(pg === 'chiffres'){
      boot();
      document.querySelectorAll('.pg').forEach(function(p){ p.classList.remove('on'); });
      document.querySelectorAll('.nt').forEach(function(t){ t.classList.remove('on'); });
      var el = document.getElementById('pg-chiffres');
      if(el) el.classList.add('on');
      var nb = document.getElementById('cf-nav');
      if(nb) nb.classList.add('on');
      setTimeout(rendre, 30);
      return;
    }
    return old.apply(this, arguments);
  };
}

window.__ECO_CHIFFRES_N = tous().length;
setTimeout(function(){
  console.log('[ÉcoSphère v200] Chiffres à retenir — ' + tous().length + ' données indexées');
}, 7000);
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', json.dumps(PAYLOAD, ensure_ascii=False, separators=(',', ':')))
s = s.rstrip() + '\n' + CSS.strip() + '\n\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('  %d chiffres sur %d chapitres' % (total, len(ORDRE)))
print('  titres : %d datés (période dans le titre) + %d règles, modèles et seuils\n          institutionnels, qui ne portent pas d’année'
      % (SUIVI['datés'], SUIVI['règles']))
for c in ORDRE:
    print('    %-22s %2d prioritaires + %2d complémentaires'
          % (LIB.get(c, 'Chapitre ' + c), len(D[c]['prio']), len(D[c]['comp'])))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
