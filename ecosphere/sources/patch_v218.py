#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplace entièrement la section « Recherche » d'ÉcoSphère.

L'ancienne page et son moteur sont retirés : le balisage de #pg-search est
remplacé, et les fonctions de l'ancien index (doSearch, setF,
rebuildSearchIndex) sont neutralisées. Le nouveau moteur n'exploite plus
l'ancien tableau SEARCH_INDEX.

La nouvelle recherche travaille sur deux ensembles :
  — une charge de données embarquée, montée par rech_payload.py : définitions
    moissonnées dans les cours ou rédigées, sections des chapitres, formules,
    faits datés, dossiers d'« Autour d'une notion », idées de l'Atlas,
    chiffres et résumés ;
  — les contenus déjà présents en mémoire : notions de chapitre, fiches,
    auteurs, sujets, visualisations, page Formules, et surtout le texte même
    des cours, découpé en blocs au premier usage pour permettre la recherche
    de passages et l'ouverture du paragraphe exact.
"""
import io
import json
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v217.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v218.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-recherche-v218' not in s

DATA = json.load(open('recherche_payload.json'))

# --------------------------------------------------------------------- balisage
# l'ancienne page est retirée et remplacée
DEBUT = '<!-- SEARCH -->\n<div class="pg" id="pg-search">'
i = s.index(DEBUT)
j = s.index('<!-- AUTHORS -->', i)
ANCIEN = s[i:j]
assert 'doSearch()' in ANCIEN and len(ANCIEN) < 4000, len(ANCIEN)

NOUVEAU = '''<!-- RECHERCHE (v218) -->
<div class="pg" id="pg-search">
<div class="rq-wrap">
  <h1 class="rq-h1">Recherche</h1>
  <p class="rq-sub">Une notion, une définition, un passage de cours, un auteur,
    une formule, un chiffre, un fait daté, un sujet, un dossier.
    La définition arrive d’abord, puis les passages qui l’expliquent.</p>
  <div class="rq-bar">
    <span class="rq-ic">🔍</span>
    <input class="rq-in" id="rq-in" type="text" autocomplete="off"
      placeholder="Ex. position extérieure nette, avantage comparatif, Bairoch, multiplicateur…">
    <button class="rq-x" id="rq-x" title="Effacer">✕</button>
  </div>
  <div class="rq-chips" id="rq-chips"></div>
  <div class="rq-etat" id="rq-etat"></div>
  <div id="rq-res"></div>
</div>
</div>

'''
s = s[:i] + NOUVEAU + s[j:]

STYLE = r"""
<style id="eco-recherche-style-v218">
#pg-search{--rq-f:#f6f8fb;--rq-b:#dbe4ea;--rq-t:#0f172a;--rq-t2:#475569;
  --rq-t3:#94a3b8;--rq-a:#1d4ed8;--rq-a2:#0e7490;--rq-ok:#047857;
  --rq-at:#b45309;--rq-vi:#6d28d9}
#pg-search .rq-wrap{max-width:1120px;margin:0 auto;padding:24px 18px 80px}
#pg-search .rq-h1{font-family:'Playfair Display',serif;font-size:2rem;
  font-weight:900;margin:0 0 8px;color:var(--rq-t)}
#pg-search .rq-sub{color:var(--rq-t2);font-size:.9rem;line-height:1.6;
  margin:0 0 16px;max-width:820px}
#pg-search .rq-bar{display:flex;align-items:center;gap:8px;background:#fff;
  border:1px solid var(--rq-b);border-radius:14px;padding:4px 10px;
  box-shadow:0 8px 26px rgba(15,23,42,.06)}
#pg-search .rq-ic{font-size:1rem;opacity:.7}
#pg-search .rq-in{flex:1;border:0;outline:0;background:transparent;
  font-family:inherit;font-size:1rem;color:var(--rq-t);padding:11px 2px}
#pg-search .rq-x{border:0;background:transparent;color:var(--rq-t3);
  font-size:.9rem;cursor:pointer;padding:6px 8px;display:none}
#pg-search .rq-x.on{display:block}
#pg-search .rq-chips{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0 6px}
#pg-search .rq-c{border:1px solid var(--rq-b);background:#fff;border-radius:999px;
  padding:6px 12px;font-size:.78rem;font-family:inherit;color:var(--rq-t2);
  cursor:pointer;white-space:nowrap}
#pg-search .rq-c:hover{background:#f1f5f9}
#pg-search .rq-c.on{background:var(--rq-t);color:#fff;border-color:var(--rq-t)}
#pg-search .rq-c i{font-style:normal;opacity:.55;margin-left:5px;font-size:.72rem}
#pg-search .rq-etat{font-size:.8rem;color:var(--rq-t2);margin:10px 0 14px;
  line-height:1.55}
#pg-search .rq-etat b{color:var(--rq-t)}
#pg-search .rq-corr{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;
  border-radius:9px;padding:8px 11px;display:inline-block}
#pg-search .rq-corr b{color:#7c2d12}
#pg-search .rq-g{border:1px solid var(--rq-b);border-radius:16px;background:#fff;
  margin-bottom:14px;overflow:hidden;box-shadow:0 4px 16px rgba(15,23,42,.04)}
#pg-search .rq-prim{padding:15px 17px 14px;cursor:pointer;
  background:linear-gradient(180deg,#fff,#fbfdff)}
#pg-search .rq-prim:hover{background:#f6faff}
#pg-search .rq-hd{display:flex;align-items:center;gap:8px;flex-wrap:wrap;
  margin-bottom:7px}
#pg-search .rq-ty{font-size:.68rem;font-weight:800;letter-spacing:.04em;
  text-transform:uppercase;padding:3px 8px;border-radius:6px;
  background:#eef2ff;color:var(--rq-a)}
#pg-search .rq-ty.d{background:#ecfdf5;color:var(--rq-ok)}
#pg-search .rq-ty.p{background:#eff6ff;color:#1d4ed8}
#pg-search .rq-ty.a{background:#fef2f2;color:#b91c1c}
#pg-search .rq-ty.c{background:#fffbeb;color:var(--rq-at)}
#pg-search .rq-ty.v{background:#f5f3ff;color:var(--rq-vi)}
#pg-search .rq-ty.r{background:#f1f5f9;color:#475569}
#pg-search .rq-loc{font-size:.72rem;color:var(--rq-t3)}
#pg-search .rq-ti{font-size:1.04rem;font-weight:800;color:var(--rq-t);
  line-height:1.35;margin-bottom:6px}
#pg-search .rq-tx{font-size:.88rem;color:var(--rq-t2);line-height:1.62}
#pg-search .rq-path{font-size:.73rem;color:var(--rq-t3);margin-top:7px;
  font-style:italic}
#pg-search mark{background:#fde68a;color:#78350f;border-radius:3px;
  padding:0 2px;font-weight:700}
#pg-search .rq-ou{border-top:1px solid #eef2f6;padding:10px 14px 12px;
  background:#fbfdff}
#pg-search .rq-ou-t{font-size:.7rem;text-transform:uppercase;
  letter-spacing:.05em;color:var(--rq-t3);font-weight:800;margin-bottom:7px}
#pg-search .rq-ou-l{display:flex;flex-wrap:wrap;gap:6px}
#pg-search .rq-o{border:1px solid var(--rq-b);background:#fff;border-radius:8px;
  padding:5px 9px;font-size:.76rem;font-family:inherit;color:var(--rq-t2);
  cursor:pointer;text-align:left;max-width:100%}
#pg-search .rq-o:hover{background:#eef2ff;border-color:#c7d2fe;color:var(--rq-a)}
#pg-search .rq-o b{color:var(--rq-t);font-weight:700}
#pg-search .rq-sec{border-top:1px dashed #e2e8f0;padding:11px 15px;
  cursor:pointer}
#pg-search .rq-sec:hover{background:#f8fafc}
#pg-search .rq-sec .rq-ti{font-size:.92rem;margin-bottom:4px}
#pg-search .rq-sec .rq-tx{font-size:.84rem}
#pg-search .rq-vide{border:1px dashed var(--rq-b);border-radius:14px;
  padding:26px 20px;color:var(--rq-t2);font-size:.9rem;line-height:1.65;
  background:#fff}
#pg-search .rq-vide b{color:var(--rq-t)}
#pg-search .rq-sugg{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
#pg-search .rq-sugg button{border:1px solid var(--rq-b);background:#fff;
  border-radius:8px;padding:6px 11px;font-size:.8rem;font-family:inherit;
  color:var(--rq-a);cursor:pointer}
.rq-flash{animation:rqflash 2.4s ease-out 1}
@keyframes rqflash{0%{background:#fde68a}60%{background:#fef3c7}
  100%{background:transparent}}
@media(max-width:700px){
  #pg-search .rq-wrap{padding:16px 13px 70px}
  #pg-search .rq-h1{font-size:1.5rem}
  #pg-search .rq-in{font-size:.95rem}
  #pg-search .rq-ti{font-size:.98rem}
}
@media(prefers-color-scheme:dark){
  #pg-search:not([data-th="light"]){--rq-f:#0b1220;--rq-b:#1e293b;
    --rq-t:#e2e8f0;--rq-t2:#94a3b8;--rq-t3:#64748b}
  #pg-search:not([data-th="light"]) .rq-bar,
  #pg-search:not([data-th="light"]) .rq-g,
  #pg-search:not([data-th="light"]) .rq-o,
  #pg-search:not([data-th="light"]) .rq-vide{background:#111a2b}
  #pg-search:not([data-th="light"]) .rq-prim{background:#111a2b}
  #pg-search:not([data-th="light"]) .rq-ou{background:#0d1626}
}
</style>
"""

MOTEUR = r"""
<script id="eco-recherche-v218">
(function(){
'use strict';
if(window.__ECO_RECH_V218) return;
window.__ECO_RECH_V218 = true;

var D = __PAYLOAD__;

/* Les grands tableaux de l'application sont déclarés avec const au premier
   niveau d'un script : ils sont dans la portée lexicale globale mais ne sont
   pas des propriétés de window. On les lit donc par leur nom. */
function G(nom){
  try { return (new Function('try{return ' + nom + '}catch(e){return undefined}'))(); }
  catch(e){ return undefined; }
}
var _cache = {};
function g(nom){
  if(!(nom in _cache)) _cache[nom] = G(nom);
  return _cache[nom];
}
function oublier(){ _cache = {}; }

/* ====================================================== normalisation */
function nz(s){
  return (s==null?'':String(s)).toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g,'')
    .replace(/[’‘ʼ]/g,"'")
    .replace(/œ/g,'oe').replace(/æ/g,'ae')
    .replace(/\s+/g,' ').trim();
}
function sing(w){
  /* on ne retire jamais le « x » final : taux, prix, flux ne sont pas des
     pluriels */
  if(w.length>5 && /eaux$/.test(w)) return w.slice(0,-1);
  if(w.length>5 && /aux$/.test(w)) return w.slice(0,-3)+'al';
  if(w.length>5 && /ail$/.test(w)) return w.slice(0,-3)+'al';
  if(w.length>3 && /s$/.test(w) && !/ss$/.test(w)) return w.slice(0,-1);
  return w;
}
var PETITS = {de:1,du:1,des:1,la:1,le:1,les:1,un:1,une:1,et:1,ou:1,au:1,aux:1,
  en:1,dans:1,par:1,pour:1,sur:1,ce:1,ces:1,sa:1,se:1,son:1,ses:1,qui:1,que:1,
  est:1,sont:1,aux:1,ne:1,pas:1,plus:1,avec:1,sans:1,sous:1,leur:1,leurs:1};
function toks(s){
  var t = nz(s).replace(/[^a-z0-9' ]+/g,' ').replace(/'/g,' ');
  var o = [], a = t.split(' '), i;
  for(i=0;i<a.length;i++){ if(a[i].length>1) o.push(sing(a[i])); }
  return o;
}
function motsUtiles(s){
  var a = toks(s), o = [], i;
  for(i=0;i<a.length;i++) if(!PETITS[a[i]]) o.push(a[i]);
  return o.length ? o : a;
}
var RE_ART = /^(le|la|les|l|un|une|des|du|de|d|au|aux|ce|cet|cette|ces|son|sa|ses|leur|leurs|mon|notre)\s+/;
function cle(s){
  var t = toks(s).join(' '), p;
  do { p = t; t = t.replace(RE_ART,''); } while(t !== p && t);
  return t || toks(s).join(' ');
}

/* ====================================================== blocs des cours */
var RE_MARQ = /^\s*(?:[IVXLC]{1,6}\.|[A-Z]{1,2}\.|\d{1,2}\s*[-.)])\s*/;
function R_TITRE(t){ return String(t||'').replace(RE_MARQ,'').trim(); }

var SEL = 'h2,h3,h4,h5,p,li,.db,table,blockquote';
var BL = {}, NX = {}, OFF = {}, PRET = {}, VOC = null, VOCB = null;

function blocsChapitre(k){
  if(PRET[k]) return BL[k];
  var CC = g('CH_CONTENT');
  var h = (CC && CC[k] && CC[k].cours) || '';
  var d = document.createElement('div');
  d.innerHTML = h;
  var out = [], h2='', h3='', h4='', n = 0;
  d.querySelectorAll(SEL).forEach(function(el){
    if(el.closest('.db') && !el.classList.contains('db')) return;
    if(el.tagName === 'TABLE' && el.closest('.db')) return;
    var tag = el.classList.contains('db') ? 'db' : el.tagName.toLowerCase();
    var txt = (el.innerText||'').replace(/\s+/g,' ').trim(), dt='', dd='';
    if(tag === 'db'){
      var a = el.querySelector('.dt'), b = el.querySelector('.dd');
      dt = a ? (a.innerText||'').replace(/\s+/g,' ').trim() : '';
      dd = b ? (b.innerText||'').replace(/\s+/g,' ').trim() : '';
      txt = (dt + ' : ' + dd).trim();
    }
    if(tag === 'h2'){ h2 = txt; h3=''; h4=''; }
    else if(tag === 'h3'){ h3 = txt; h4=''; }
    else if(tag === 'h4' || tag === 'h5'){ h4 = txt; }
    el.setAttribute('data-rb', String(n));
    out.push({g:tag, x:txt, dt:dt, dd:dd, p:[h2,h3,h4]});
    n++;
  });
  /* on réinjecte le balisage marqué : les liens profonds pourront viser
     le bloc exact, y compris si le chapitre est rouvert plus tard */
  try{ if(CC && CC[k]) CC[k].cours = d.innerHTML; }catch(e){}
  /* le texte indexé est une suite de jetons au singulier séparés par des
     espaces : la recherche d'une expression y respecte les frontières de
     mots et ignore les différences de pluriel */
  var txts = [], offs = [], pos = 0, i;
  for(i=0;i<out.length;i++){
    var t = ' ' + toks(out[i].x).join(' ') + ' ';
    offs.push(pos); txts.push(t); pos += t.length + 1;
  }
  BL[k] = out; NX[k] = txts.join('\n'); OFF[k] = offs; PRET[k] = true;
  return out;
}

function tousLesBlocs(){
  Object.keys(D.ch).forEach(function(k){ blocsChapitre(k); });
}

function blocAt(k, off){
  var a = OFF[k], lo = 0, hi = a.length - 1, r = 0;
  while(lo <= hi){ var m = (lo+hi)>>1;
    if(a[m] <= off){ r = m; lo = m+1; } else hi = m-1; }
  return r;
}

/* ====================================================== vocabulaire */
function vocabulaire(){
  if(VOC) return VOC;
  var S = Object.create(null);
  function av(s){ var a = toks(s), i; for(i=0;i<a.length;i++) S[a[i]] = 1; }
  Object.keys(D.def).forEach(function(c){ av(D.def[c].t); });
  D.sec.forEach(function(x){ av(x.t); });
  D.dos.forEach(function(x){ av(x.t); });
  D.atl.forEach(function(x){ av(x.t); av(x.n); });
  try{ (g('AUTHORS')||[]).forEach(function(a){ av(a.name); av(a.idea); }); }catch(e){}
  try{ var CC = g('CH_CONTENT')||{}; Object.keys(CC).forEach(function(k){
    (CC[k].notions||[]).forEach(function(n){ av(n.term); }); }); }catch(e){}
  Object.keys(NX).forEach(function(k){
    var a = NX[k].replace(/[^a-z0-9 ]+/g,' ').split(' '), i;
    for(i=0;i<a.length;i++) if(a[i].length>2) S[sing(a[i])] = 1;
  });
  VOC = S;
  VOCB = Object.create(null);
  Object.keys(S).forEach(function(w){
    var b = w.charAt(0) + w.length;
    (VOCB[b] = VOCB[b] || []).push(w);
  });
  return VOC;
}
function dist1(a,b,max){
  if(Math.abs(a.length-b.length) > max) return max+1;
  var i=0, j=0, d=0;
  while(i<a.length && j<b.length){
    if(a[i]===b[j]){ i++; j++; continue; }
    d++; if(d>max) return d;
    if(a.length>b.length) i++;
    else if(a.length<b.length) j++;
    else { i++; j++; }
  }
  return d + (a.length-i) + (b.length-j);
}
function corriger(w){
  vocabulaire();
  if(VOC[w]) return w;
  var max = w.length >= 8 ? 2 : (w.length >= 5 ? 1 : 0);
  if(!max) return w;
  var best = null, bd = max + 1, l = w.charAt(0), i, dl, b, arr, k;
  for(dl = -max; dl <= max; dl++){
    for(i = 0; i < 2; i++){
      b = (i ? l : '') + (w.length + dl);
      arr = VOCB[(i ? l : '') + (w.length + dl)];
      if(i === 0) arr = null;
      if(!arr) continue;
      for(k = 0; k < arr.length; k++){
        var d = dist1(w, arr[k], bd - 1);
        if(d < bd){ bd = d; best = arr[k]; if(!d) return best; }
      }
    }
  }
  /* seconde passe : première lettre différente (faute de frappe initiale) */
  if(!best && w.length >= 6){
    var cles = Object.keys(VOCB), z;
    for(z = 0; z < cles.length; z++){
      if(Math.abs(parseInt(cles[z].slice(1),10) - w.length) > 1) continue;
      arr = VOCB[cles[z]];
      for(k = 0; k < arr.length; k++){
        var dd = dist1(w, arr[k], 1);
        if(dd < bd){ bd = dd; best = arr[k]; }
      }
    }
  }
  return best || w;
}

/* ====================================================== entrées */
var E = null;

function act(a){ return a; }

function ajouterEntrees(){
  if(E) return E;
  var L = [];
  function add(o){
    o.g = o.g || cle(o.t);
    o.nt = cle(o.t);
    o.nd = toks((o.d||'') + ' ' + (o.kw||'')).join(' ');
    L.push(o);
  }
  /* 1. définitions (cours moissonnés + rédigées) */
  Object.keys(D.def).forEach(function(c){
    var v = D.def[c];
    var ou = (v.ou||[]).filter(function(z){ return D.ch[z[0]]; });
    add({y:'def', t:v.t, d:v.d, c:ou.length?ou[0][0]:'', b:ou.length?ou[0][1]:-1,
         al:v.al||[], o:v.o, ou:ou, g:c,
         k:ou.length?['ch',ou[0][0],ou[0][1]]:null});
  });
  /* 2. notions des chapitres (déjà en mémoire) */
  try{
    var CC = g('CH_CONTENT')||{};
    Object.keys(CC).forEach(function(k){
      if(!D.ch[k]) return;
      (CC[k].notions||[]).forEach(function(n){
        if(!n.term || !n.def) return;
        add({y:(n.type==='formule'?'formule':'notion'), t:n.term, d:n.def,
             c:k, b:-1, k:['nt',k,n.term]});
      });
    });
  }catch(e){}
  /* 3. sections des chapitres */
  D.sec.forEach(function(x){
    add({y:'sect', t:x.t, d:'', kw:x.p, c:x.c, b:x.b, path:x.p,
         k:['ch',x.c,x.b]});
  });
  /* 4. auteurs */
  try{
    (g('AUTHORS')||[]).forEach(function(a){
      add({y:'auteur', t:a.name, d:(a.idea||''),
           kw:[a.courant,a.detail,a.phrase,(a.oeuvres||[]).join(' ')].join(' '),
           c:String(a.ch||''), b:-1, k:['au',a.name]});
    });
  }catch(e){}
  /* 5. formules : page Formules + blocs de cours */
  try{
    document.querySelectorAll('#pg-formulas .cardx').forEach(function(el,i){
      var b = el.querySelector('b'), n = el.querySelector('.s-note');
      if(!b) return;
      el.setAttribute('data-rf', String(i));
      add({y:'formule', t:(b.innerText||'').trim(),
           d:(n?(n.innerText||'').trim():''), c:'', b:i, k:['fo',i]});
    });
  }catch(e){}
  D.fml.forEach(function(x){
    add({y:'formule', t:x.t, d:x.d, c:x.c, b:x.b, k:['ch',x.c,x.b]});
  });
  /* 6. faits datés */
  D.fai.forEach(function(x){
    add({y:'fait', t:String(x.an), d:x.d, kw:x.p, c:x.c, b:x.b,
         an:x.an, g:'fait-'+x.c+'-'+x.b, k:['ch',x.c,x.b]});
  });
  /* 7. dossiers d'« Autour d'une notion » */
  D.dos.forEach(function(x){
    add({y:'dossier', t:x.t, d:x.d, c:(x.ch&&x.ch.length?String(x.ch[0]):''),
         b:-1, etat:x.et, k:['do',x.cle]});
  });
  /* 8. idées de l'Atlas */
  D.atl.forEach(function(x){
    add({y:'atlas', t:x.t, d:x.d, kw:(x.no||[]).join(' ')+' '+x.n, c:x.c,
         b:-1, aut:x.n, g:'atlas-'+nz(x.n)+'-'+cle(x.t), k:['at',x.c]});
  });
  /* 9. chiffres */
  D.chf.forEach(function(x){
    add({y:'chiffre', t:(x.v+' — '+(x.u||'')).replace(/ — $/,''), d:x.d,
         kw:[x.z,x.p,(x.k||[]).join(' ')].join(' '), c:x.c, b:-1,
         g:'chf-'+x.c+'-'+nz(x.v), k:['ci',x.c]});
  });
  /* 10. résumés */
  D.res.forEach(function(x){
    add({y:'resume', t:'Résumé — '+(D.ch[x.c]?D.ch[x.c].t:('chapitre '+x.c)),
         d:x.d, kw:x.q+' '+(x.i||[]).join(' '), c:x.c, b:-1,
         g:'res-'+x.c, k:['re',x.c]});
  });
  /* 11. sujets */
  try{
    (g('SUBJECTS_BANK_PREMIUM')||[]).forEach(function(z){
      add({y:'sujet', t:z.title, d:'', c:String(z.chapter||''), b:-1,
           g:'suj-'+z.id, k:['su',String(z.chapter||'')]});
    });
  }catch(e){}
  /* 12. fiches — l'habillage de révision est retiré pour que la fiche
         rejoigne la notion au lieu de faire doublon */
  var FICHE_OK = {definition:1, 'définition':1, 'notion-clé':1, notion:1,
    formule:1, auteur:1, ouvrage:1, courant:1, tableau:1};
  var RE_HABIT = /^\s*(?:d[ée]finis|que faut-il retenir de|quel concept correspond [àa] cette (?:d[ée]finition|id[ée]e)|quel auteur associer [àa] l['’]id[ée]e suivante|rappelle|explique|cite)\s*:?\s*/i;
  try{
    (g('FC_DATA')||[]).forEach(function(f){
      if(!f.term || !f.def) return;
      if(!FICHE_OK[f.type]) return;
      var t = String(f.term).replace(RE_HABIT, '').replace(/\s*\?\s*$/, '').trim();
      if(t.length < 2) return;
      add({y:'fiche', t:t, d:f.def, c:String(f.ch||''), b:-1,
           g:'fc-'+cle(t)+'-'+(f.ch||''), k:['fc',f.ch]});
    });
  }catch(e){}
  /* 13. visualisations */
  try{
    (g('visualisationsStrategiques')||g('VZ')||[]).forEach(function(v){
      add({y:'visu', t:v.titre, d:v.resume||'', kw:v.fam||'', c:'', b:-1,
           g:'vz-'+v.cle, k:['vz',v.cle]});
      (v.noeuds||[]).forEach(function(n){
        add({y:'visu', t:n.t, d:n.r||n.defi||'', kw:v.titre, c:'', b:-1,
             g:'vz-'+v.cle+'-'+n.id, k:['vz',v.cle]});
      });
    });
  }catch(e){}
  E = L;
  return E;
}

/* ====================================================== score */
var PRIO = {def:460, notion:330, sect:150, dossier:250, atlas:160, auteur:200,
  formule:180, chiffre:130, fait:95, sujet:80, fiche:70, visu:110, resume:-320,
  passage:0};
var TYPE_LIB = {def:'définition', notion:'notion', sect:'section de cours',
  passage:'passage du cours', auteur:'auteur', formule:'formule',
  chiffre:'chiffre', fait:'fait daté', dossier:'dossier', atlas:'idée (Atlas)',
  chiffre_:'chiffre', sujet:'sujet', fiche:'fiche', resume:'résumé',
  visu:'visualisation'};
var TYPE_CL = {def:'d', notion:'d', sect:'p', passage:'p', auteur:'a',
  formule:'', chiffre:'c', fait:'c', dossier:'', atlas:'v', sujet:'',
  fiche:'', resume:'r', visu:'v'};

function noter(e, Q){
  var s = 0, i, n = 0;
  var nt = e.nt, nd = e.nd, ntp = ' ' + nt + ' ', ndp = ' ' + nd + ' ';
  var expr = Q.mots.length ? Q.mots.join(' ') : '';
  var court = Q.cle.length <= 3;
  if(nt === Q.cle) s += 1000;
  else if((e.al||[]).indexOf(Q.cle) >= 0) s += 940;
  else if(court){
    /* sigle ou mot très court : on exige un jeton entier, jamais un morceau */
    if(ntp.indexOf(' ' + Q.cle + ' ') >= 0) s += 620;
  }
  else if(nt.indexOf(Q.cle + ' ') === 0)
    s += 700 - Math.min(140, (nt.length - Q.cle.length) * 4);
  else if(Q.cle && ntp.indexOf(' ' + Q.cle + ' ') >= 0) s += 560;
  else if(Q.cle && nt.indexOf(Q.cle) >= 0) s += 420;
  else if(Q.cle && Q.cle.indexOf(nt + ' ') === 0 && nt.length >= 4) s += 300;
  for(i=0;i<Q.mots.length;i++) if(ntp.indexOf(' '+Q.mots[i]+' ') >= 0) n++;
  if(Q.mots.length) s += Math.round(230 * n / Q.mots.length);
  var dansD = expr && ndp.indexOf(' ' + expr + ' ') >= 0;
  if(dansD) s += 180;
  var nd2 = 0;
  for(i=0;i<Q.mots.length;i++) if(ndp.indexOf(' '+Q.mots[i]+' ') >= 0) nd2++;
  if(Q.mots.length) s += Math.round(70 * nd2 / Q.mots.length);
  /* un résultat n'est retenu que s'il correspond vraiment : expression
     présente, ou tous les mots de la requête présents */
  var couvre = (n === Q.mots.length && Q.mots.length > 0) || dansD ||
               (nd2 === Q.mots.length && Q.mots.length > 0) ||
               (!court && Q.cle && nt.indexOf(Q.cle) >= 0);
  if(!couvre) return 0;
  s += (PRIO[e.y] || 0);
  if(e.y === 'resume'){
    /* un résumé ne remonte que si la requête y figure littéralement */
    if(!dansD && n < Q.mots.length) return 0;
  }
  if(e.y === 'auteur'){
    if(nt === Q.cle) s += 700;
    else if(Q.mots.length <= 2){
      /* le nom de famille seul doit suffire à faire remonter l'auteur */
      var np = nt.split(' ');
      if(np.length && Q.mots.indexOf(np[np.length-1]) >= 0) s += 640;
    }
  }
  if(e.y === 'dossier' && e.etat === 'hors-cours') s -= 260;
  if(e.y === 'sect' && !e.d) s -= 40;
  if(e.c && Q.ch && String(e.c) === Q.ch) s += 120;
  return s;
}

/* ====================================================== passages */
function chercherPassages(Q, lim){
  var out = [], ks = Object.keys(D.ch), i, k;
  for(i=0;i<ks.length;i++){
    k = ks[i];
    if(!PRET[k]) blocsChapitre(k);
    var t = NX[k], trouve = {};
    var expr = Q.mots.length ? (' ' + Q.mots.join(' ') + ' ') : '';
    if(expr && Q.mots.length > 1){
      var p = t.indexOf(expr), garde = 0;
      while(p >= 0 && garde < 400){
        var b = blocAt(k, p);
        if(!trouve[b]) trouve[b] = {b:b, exact:1, n:0};
        trouve[b].n++;
        p = t.indexOf(expr, p + expr.length - 1); garde++;
      }
    }
    if(Q.mots.length){
      /* tous les jetons de la requête dans le même bloc */
      var m0 = ' ' + Q.mots[0] + ' ', q = t.indexOf(m0), g2 = 0;
      while(q >= 0 && g2 < 2500){
        var bb = blocAt(k, q);
        if(!trouve[bb]){
          var xb = ' ' + toks((BL[k][bb]||{}).x || '').join(' ') + ' ';
          var tous = 1, j;
          for(j=0;j<Q.mots.length;j++)
            if(xb.indexOf(' ' + Q.mots[j] + ' ') < 0){ tous = 0; break; }
          if(tous) trouve[bb] = {b:bb, exact:(Q.mots.length === 1 ? 1 : 0), n:1};
        }
        q = t.indexOf(m0, q + m0.length - 1); g2++;
      }
    }
    Object.keys(trouve).forEach(function(bk){
      var z = trouve[bk], bl = BL[k][z.b];
      if(!bl || bl.x.length < 24) return;
      if(bl.g === 'h2' || bl.g === 'h3') return;  /* les titres : type « sect » */
      if(!z.exact && Q.mots.length > 1){
        /* mots dispersés : on exige que la section parle du sujet, sinon le
           rapprochement est fortuit */
        var ts = ' ' + toks((bl.p[1] || bl.p[0] || '') + ' ' + (bl.p[2] || '')).join(' ') + ' ';
        var un = 0;
        for(var w = 0; w < Q.mots.length; w++)
          if(ts.indexOf(' ' + Q.mots[w] + ' ') >= 0){ un = 1; break; }
        if(!un) return;
      }
      var etiq = bl.p[2] || '';
      var GEN_ET = /^(idee|idee cle|idee centrale|idee generale|idee essentielle|schema|formule|exemple|mecanisme|etape|pourquoi|remarque|attention|consequence|definition|synthese|resume|rappel|document|lecture|cas|mot cle a retenir|a retenir|conclusion|objectif|constat|limite|critique|principe|logique|precision|nuance|application|illustration|comparaison|tableau)\b/;
      if(etiq && GEN_ET.test(nz(R_TITRE(etiq)))) etiq = '';
      var sect = bl.p[1] || bl.p[0] || '';
      var titrePass = (sect ? R_TITRE(sect) : D.ch[k].t)
        + (etiq ? ' — ' + R_TITRE(etiq) : '');
      out.push({y:'passage',
        nt:cle(titrePass), nd:toks(bl.x).join(' '),
        t:(sect ? R_TITRE(sect) : D.ch[k].t) + (etiq ? ' — ' + R_TITRE(etiq) : ''),
        d:bl.x, c:k, b:z.b,
        path:[bl.p[0], bl.p[2]].filter(Boolean).map(R_TITRE).join(' › '),
        sect:sect,
        sc: (z.exact ? 620 : 300) + Math.min(60, z.n*12)
            + (bl.g === 'db' ? 240 : 0) + (bl.g === 'li' ? -25 : 0)
            + (Q.mots.length && (' ' + toks(sect).join(' ') + ' ')
                 .indexOf(' ' + Q.mots.join(' ') + ' ') >= 0 ? 190 : -110),
        k:['ch',k,z.b]});
    });
  }
  out.sort(function(a,b){ return b.sc - a.sc; });
  return out.slice(0, lim || 400);
}

/* ====================================================== recherche */
var FILTRE = 'tout';
var FAM = {
  tout:null,
  definitions:['def','notion'],
  cours:['passage','sect'],
  auteurs:['auteur'],
  formules:['formule'],
  chiffres:['chiffre'],
  faits:['fait'],
  dossiers:['dossier'],
  atlas:['atlas'],
  sujets:['sujet'],
  fiches:['fiche'],
  resumes:['resume'],
  visu:['visu']
};
var FAM_LIB = {tout:'Tout', definitions:'Définitions', cours:'Cours',
  auteurs:'Auteurs', formules:'Formules', chiffres:'Chiffres',
  faits:'Faits & dates', dossiers:'Dossiers', atlas:'Atlas', sujets:'Sujets',
  fiches:'Fiches', resumes:'Résumés', visu:'Visualisations'};

function analyser(q){
  var brut = nz(q);
  var ch = null;
  var m = brut.match(/\bchapitre\s+(\d{1,2})\b/);
  if(m) ch = m[1];
  var sansch = brut.replace(/\bchapitre\s+\d{1,2}\b/g,' ').trim();
  var mots = motsUtiles(sansch);
  /* correction des fautes de frappe */
  var corr = [], change = 0, i;
  for(i=0;i<mots.length;i++){
    var c = corriger(mots[i]);
    if(c !== mots[i]) change = 1;
    corr.push(c);
  }
  var nq = cle(sansch);
  var syn = [];
  var k = nq;
  if(D.syn[k]) syn = D.syn[k].slice(0);
  return {brut:brut, nq:nz(sansch), cle:nq, mots:corr, mots0:mots,
          corrige:change, ch:ch, syn:syn};
}

function texteSection(c, b){
  /* le contenu d'une section : les premiers blocs qui la suivent */
  var v = BL[c];
  if(!v) { blocsChapitre(c); v = BL[c]; }
  if(!v) return '';
  var out = [], i;
  for(i = b + 1; i < v.length && out.length < 4; i++){
    if(v[i].g === 'h2' || v[i].g === 'h3') break;
    if(v[i].x.length > 18) out.push(v[i].x);
  }
  return out.join(' ');
}

/* types qui nomment une notion : deux clés différentes = deux notions */
var NOMME = {def:1, notion:1, dossier:1, auteur:1, fiche:1, atlas:1, visu:1};
/* types qui situent une notion : ils rejoignent la carte de la notion */
var SITUE = {sect:1, passage:1, chiffre:1, fait:1, resume:1, formule:1,
  sujet:1, atlas:1, visu:1, fiche:1};

function fusionner(res, Q){
  var PR = {def:9, notion:8, auteur:9, dossier:7, atlas:6, formule:6,
    passage:5, sect:4, chiffre:4, fait:3, visu:3, sujet:2, fiche:2, resume:1};
  var syn = {};
  (Q.syn || []).forEach(function(z){ syn[cle(z)] = 1; });
  Object.keys(D.syn).forEach(function(k){
    if((D.syn[k] || []).map(cle).indexOf(Q.cle) >= 0) syn[cle(k)] = 1;
  });

  /* toutes les façons d'écrire la notion cherchée */
  var VAR = [Q.mots.join(' ')];
  Object.keys(syn).forEach(function(z){ if(z) VAR.push(z); });
  VAR = VAR.filter(function(z, i){ return z && VAR.indexOf(z) === i; });

  /* la notion cherchée : d'abord le libellé exact, ensuite un synonyme */
  var principal = null, rangPrin = -1;
  res.forEach(function(r){
    if(!NOMME[r.y]) return;
    var rang = r.nt === Q.cle ? 2 : (syn[r.nt] ? 1 : 0);
    if(!rang) return;
    var pr = PR[r.y] || 0;
    if(!principal || rang > rangPrin
       || (rang === rangPrin && pr > (PR[principal.y] || 0))
       || (rang === rangPrin && pr === (PR[principal.y] || 0) && r.sc > principal.sc)){
      principal = r; rangPrin = rang;
    }
  });

  var par = Object.create(null), ordre = [];
  function groupe(cl){
    if(!par[cl]){ par[cl] = {cle:cl, items:[], sc:0}; ordre.push(par[cl]); }
    return par[cl];
  }
  var tete = null;
  if(principal){
    tete = groupe('@' + Q.cle);
    tete.items.push(principal);
    tete.sc = principal.sc + 60;
  }

  res.forEach(function(r){
    if(r === principal) return;
    var memeNotion = (r.nt === Q.cle) || !!syn[r.nt];
    /* une occurrence qui porte la notion, sous l'une de ses écritures,
       rejoint sa carte au lieu de former un résultat de plus */
    var porte = memeNotion;
    if(!porte && tete){
      var champ = ' ' + r.nt + ' ' + r.nd + ' ', z;
      if(SITUE[r.y]){
        for(z = 0; z < VAR.length && !porte; z++)
          if(champ.indexOf(' ' + VAR[z] + ' ') >= 0) porte = true;
      }
      /* un dossier ou une idée dont le titre développe la notion */
      if(!porte && (r.y === 'dossier' || r.y === 'atlas' || r.y === 'visu')){
        for(z = 0; z < VAR.length && !porte; z++)
          if(r.nt.indexOf(VAR[z] + ' ') === 0) porte = true;
      }
    }
    if(tete && porte){
      tete.items.push(r);
      return;
    }
    var cl = NOMME[r.y] ? cle(r.t) : (r.g || cle(r.t));
    var gr = groupe(cl);
    gr.items.push(r);
    if(r.sc > gr.sc) gr.sc = r.sc;
  });

  ordre.forEach(function(g){
    g.items.sort(function(a,b){
      var d = (PR[b.y] || 0) - (PR[a.y] || 0);
      return d || (b.sc - a.sc);
    });
    g.prim = g.items[0];
    /* dans la carte de la notion, on ne garde qu'un endroit par section */
    if(g === tete){
      var vus = Object.create(null), gardes = [g.prim];
      g.items.slice(1).forEach(function(r){
        var sig = r.y === 'passage' || r.y === 'sect'
          ? 'l-' + r.c + '-' + cle(r.sect || r.t)
          : r.y + '-' + (r.g || cle(r.t));
        if(vus[sig]) return;
        vus[sig] = 1;
        gardes.push(r);
      });
      g.items = gardes.slice(0, 26);
    }
  });
  ordre.sort(function(a,b){ return b.sc - a.sc; });
  return ordre;
}

function chercher(q){
  var Q = analyser(q);
  if(!Q.mots.length && !Q.ch) return {Q:Q, groupes:[], n:0};
  ajouterEntrees();
  var res = [], i, e;
  var cibles = FAM[FILTRE];
  for(i=0;i<E.length;i++){
    e = E[i];
    if(cibles && cibles.indexOf(e.y) < 0) continue;
    var sc = noter(e, Q);
    if(Q.syn.length && !sc){
      for(var z=0; z<Q.syn.length; z++){
        var Q2 = {nq:Q.syn[z], cle:cle(Q.syn[z]), mots:motsUtiles(Q.syn[z]), ch:Q.ch};
        var s2 = noter(e, Q2);
        if(s2){ sc = Math.round(s2 * 0.92); break; }
      }
    }
    if(sc > 0){ res.push(Object.assign({}, e, {sc:sc})); }
  }
  if(!cibles || cibles.indexOf('passage') >= 0){
    var pas = chercherPassages(Q, 260);
    if(!pas.length && Q.syn.length){
      for(var y=0; y<Q.syn.length && !pas.length; y++){
        pas = chercherPassages({nq:Q.syn[y], cle:cle(Q.syn[y]),
          mots:motsUtiles(Q.syn[y])}, 260);
      }
    }
    if(Q.ch) pas = pas.filter(function(p){ return p.c === Q.ch; });
    res = res.concat(pas);
  }
  if(Q.ch) res = res.filter(function(r){ return !r.c || String(r.c) === Q.ch; });
  var groupes = fusionner(res, Q);
  return {Q:Q, groupes:groupes, n:res.length};
}

/* ====================================================== rendu */
function esc(s){ return (s==null?'':String(s))
  .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
  .replace(/"/g,'&quot;'); }

function surligner(txt, Q, al){
  var t = esc(txt), zones = [], i;
  var cibles = [];
  if(Q.nq && Q.nq.length >= 3) cibles.push(Q.nq);
  for(i=0;i<Q.mots.length;i++) if(Q.mots[i].length > 2) cibles.push(Q.mots[i]);
  (Q.syn||[]).forEach(function(z){ if(z && z.length > 2) cibles.push(nz(z)); });
  (al||[]).forEach(function(z){
    if(!z || z.length < 3) return;
    /* un alias n'est surligné que s'il est bien ce que l'on a cherché */
    if(Q.cle === z || (Q.syn||[]).indexOf(z) >= 0 || cle(z) === Q.cle)
      cibles.push(nz(z));
  });
  var nt = nz(t);
  cibles.forEach(function(c){
    var p = nt.indexOf(c), garde = 0;
    while(p >= 0 && garde < 60){
      /* on étend jusqu'à la fin du mot pour ne pas couper un pluriel */
      var fin = p + c.length;
      while(fin < nt.length && /[a-z0-9]/.test(nt.charAt(fin))) fin++;
      zones.push([p, fin]);
      p = nt.indexOf(c, p + c.length); garde++;
    }
  });
  if(!zones.length) return t;
  zones.sort(function(a,b){ return a[0]-b[0]; });
  var f = [], cur = zones[0].slice();
  for(i=1;i<zones.length;i++){
    if(zones[i][0] <= cur[1]) cur[1] = Math.max(cur[1], zones[i][1]);
    else { f.push(cur); cur = zones[i].slice(); }
  }
  f.push(cur);
  var out = '', pos = 0;
  f.forEach(function(z){
    out += t.slice(pos, z[0]) + '<mark>' + t.slice(z[0], z[1]) + '</mark>';
    pos = z[1];
  });
  return out + t.slice(pos);
}

function extrait(txt, Q, long){
  var t = ' ' + (txt||'').replace(/\s+/g,' ').trim() + ' ';
  var n = nz(t), lim = long || 300;
  var p = Q.nq && Q.nq.length >= 3 ? n.indexOf(Q.nq) : -1;
  if(p < 0){ for(var i=0;i<Q.mots.length;i++){ p = n.indexOf(Q.mots[i]); if(p>=0) break; } }
  if(p < 0) return t.trim().slice(0, lim) + (t.length > lim ? '…' : '');
  if(t.length <= lim) return t.trim();
  var a = Math.max(0, p - Math.round(lim*0.38));
  /* on démarre sur un début de phrase ou de mot */
  var pt = t.lastIndexOf('. ', p);
  if(pt > a - 60 && pt > 0 && pt < p) a = pt + 2;
  else { var sp = t.indexOf(' ', a); if(sp > 0 && sp < p) a = sp + 1; }
  var b = Math.min(t.length, a + lim);
  var sp2 = t.lastIndexOf(' ', b);
  if(sp2 > a + 60) b = sp2;
  return (a > 1 ? '…' : '') + t.slice(a, b).trim() + (b < t.length - 1 ? '…' : '');
}

function lieu(r){
  if(r.y === 'auteur') return r.c && D.ch[r.c] ? D.ch[r.c].l : 'base des auteurs';
  if(r.y === 'visu') return 'visualisations stratégiques';
  if(r.y === 'dossier') return 'Autour d’une notion' + (r.etat === 'hors-cours' ? ' · hors programme traité' : '');
  if(r.y === 'atlas') return 'Atlas des idées' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(!r.c || !D.ch[r.c]) return '';
  return D.ch[r.c].l;
}

function bouton(r, lib){
  return '<button class="rq-o" data-k="' + esc(JSON.stringify(r.k)) + '">'
    + lib + '</button>';
}

function carteOu(g, Q){
  /* « où le retrouver » : un bouton par endroit distinct */
  var vus = Object.create(null), bts = [], i;
  function pose(r, lib){
    var sig = JSON.stringify(r.k);
    if(vus[sig]) return;
    vus[sig] = 1;
    bts.push(bouton(r, lib));
  }
  var prim = g.prim;
  if(prim.y === 'def' && prim.ou && prim.ou.length){
    prim.ou.forEach(function(z){
      if(!D.ch[z[0]]) return;
      pose({k:['ch',z[0],z[1]]}, '<b>' + esc(D.ch[z[0]].l) + '</b> · '
        + (z[1] >= 0 ? 'le passage du cours' : 'le chapitre'));
    });
  }
  var parCh = Object.create(null);
  g.items.forEach(function(r){
    if(r === prim) return;
    if(r.y === 'passage'){
      var c = r.c + '|' + (r.sect || '');
      if(parCh[c]) return;
      parCh[c] = 1;
      pose(r, '<b>' + esc(D.ch[r.c] ? D.ch[r.c].l : r.c) + '</b> · '
        + esc((r.sect || '').slice(0, 64) || 'passage'));
    } else if(r.y === 'sect'){
      pose(r, '<b>' + esc(D.ch[r.c] ? D.ch[r.c].l : r.c) + '</b> · section « '
        + esc(r.t.slice(0, 54)) + ' »');
    } else if(r.y === 'dossier'){
      pose(r, 'dossier « ' + esc(r.t.slice(0, 54)) + ' »');
    } else if(r.y === 'atlas'){
      pose(r, 'Atlas · ' + esc(r.aut || '') + ' — ' + esc(r.t.slice(0, 46)));
    } else if(r.y === 'chiffre'){
      pose(r, 'chiffre · ' + esc(r.t.slice(0, 56)));
    } else if(r.y === 'fait'){
      pose(r, 'fait daté · ' + esc(r.an));
    } else if(r.y === 'auteur'){
      pose(r, 'auteur · ' + esc(r.t));
    } else if(r.y === 'formule'){
      pose(r, 'formule · ' + esc(r.t.slice(0, 54)));
    } else if(r.y === 'sujet'){
      pose(r, 'sujet · ' + esc(r.t.slice(0, 70)));
    } else if(r.y === 'fiche'){
      pose(r, 'fiche · ' + esc(D.ch[r.c] ? D.ch[r.c].l : ''));
    } else if(r.y === 'resume'){
      pose(r, 'résumé du chapitre · ' + esc(D.ch[r.c] ? D.ch[r.c].l : ''));
    } else if(r.y === 'visu'){
      pose(r, 'visualisation · ' + esc(r.t.slice(0, 54)));
    } else if(r.y === 'notion'){
      pose(r, '<b>' + esc(D.ch[r.c] ? D.ch[r.c].l : '') + '</b> · fiche de notion');
    }
  });
  if(!bts.length) return '';
  return '<div class="rq-ou"><div class="rq-ou-t">Où le retrouver — '
    + bts.length + (bts.length > 1 ? ' endroits' : ' endroit')
    + '</div><div class="rq-ou-l">' + bts.join('') + '</div></div>';
}

function rendre(R) {
  var box = document.getElementById('rq-res');
  var etat = document.getElementById('rq-etat');
  var Q = R.Q;
  if(!R.groupes.length){
    etat.innerHTML = '';
    var sug = ['position extérieure nette','avantage comparatif',
      'multiplicateur keynésien','anomie','Bairoch','chaînes de valeur mondiales'];
    box.innerHTML = '<div class="rq-vide"><b>Aucun contenu d’ÉcoSphère ne '
      + 'porte cette expression.</b><br>La recherche ne balaie que les cours, '
      + 'les fiches, les auteurs, les sujets, les dossiers, l’Atlas, les '
      + 'chiffres et les résumés : si l’expression n’y figure pas, c’est '
      + 'qu’elle n’est pas traitée dans tes chapitres.'
      + '<div class="rq-sugg">' + sug.map(function(x){
          return '<button data-q="' + esc(x) + '">' + esc(x) + '</button>';
        }).join('') + '</div></div>';
    return;
  }
  var n = R.groupes.length;
  var msg = '<b>' + n + (n > 1 ? ' entrées' : ' entrée') + '</b> pour « '
    + esc(Q.brut) + ' »';
  if(Q.ch) msg += ', limitées au chapitre ' + esc(Q.ch);
  if(Q.corrige) msg = '<span class="rq-corr">Recherche élargie à <b>'
    + esc(Q.mots.join(' ')) + '</b></span><br>' + msg;
  etat.innerHTML = msg;

  var h = R.groupes.slice(0, 40).map(function(g){
    var p = g.prim;
    var cl = TYPE_CL[p.y] || '';
    var txt = p.d || '';
    if(p.y === 'sect' && !txt){
      try{ txt = texteSection(p.c, p.b); }catch(e){}
    }
    var corps = surligner(extrait(txt, Q, p.y === 'sect' ? 340 : 300), Q)
      || esc('Section du cours' + (p.path ? ' — ' + p.path : ''));
    var sup = [];
    if((p.al||[]).length){
      var vus2 = (p.al||[]).filter(function(z){
        return z && z !== p.nt && (z === Q.cle || (Q.syn||[]).indexOf(z) >= 0);
      });
      if(vus2.length) sup.push('aussi écrit ' + vus2.join(', ').toUpperCase());
    }
    if(p.y === 'def' && p.o && p.o.indexOf('redigee') >= 0)
      sup.push('définition rédigée à partir du cours');
    if(p.y === 'def' && p.o && p.o.indexOf('cours-encadre') >= 0)
      sup.push('définition du cours');
    var autres = g.items.length - 1;
    return '<div class="rq-g">'
      + '<div class="rq-prim" data-k="' + esc(JSON.stringify(p.k)) + '">'
      + '<div class="rq-hd"><span class="rq-ty ' + cl + '">'
      + esc(TYPE_LIB[p.y] || p.y) + '</span>'
      + (lieu(p) ? '<span class="rq-loc">' + esc(lieu(p)) + '</span>' : '')
      + (sup.length ? '<span class="rq-loc">· ' + esc(sup.join(' · ')) + '</span>' : '')
      + '</div>'
      + '<div class="rq-ti">' + surligner(p.t, Q, p.al) + '</div>'
      + '<div class="rq-tx">' + corps + '</div>'
      + (p.path && p.y === 'passage' ? '<div class="rq-path">'
          + esc(p.path) + '</div>' : '')
      + '</div>'
      + (autres > 0 ? carteOu(g, Q) : '')
      + '</div>';
  }).join('');
  box.innerHTML = h;
}

/* ====================================================== ouverture */
function ouvrir(k){
  if(!k) return;
  var t = k[0];
  try{
    if(t === 'ch'){
      var ch = k[1], b = k[2];
      if(typeof openCh === 'function') openCh(Number(ch) || ch);
      if(typeof showSect === 'function') { try{ showSect('cours'); }catch(e){} }
      if(b != null && b >= 0) viserBloc(ch, b);
    } else if(t === 'nt'){
      if(typeof openCh === 'function') openCh(Number(k[1]) || k[1]);
      if(typeof showSect === 'function') { try{ showSect('notions'); }catch(e){} }
      viserTexte('sect-notions', k[2]);
    } else if(t === 'au'){
      if(typeof openAuthorByName === 'function') openAuthorByName(k[1]);
      else if(typeof allerAuteur === 'function') allerAuteur(k[1]);
    } else if(t === 'do'){
      if(typeof window.ouvrirNotion === 'function') window.ouvrirNotion(k[1]);
      else if(typeof allerDossier === 'function') allerDossier(k[1]);
    } else if(t === 'at'){
      if(typeof allerAtlas === 'function') allerAtlas(k[1]);
      else showPg('atlas');
    } else if(t === 'ci'){
      if(typeof window.ouvrirChiffres === 'function') window.ouvrirChiffres(k[1]);
      else showPg('chiffres');
    } else if(t === 're'){
      if(typeof window.ouvrirResume === 'function') window.ouvrirResume(k[1]);
      else showPg('resumes');
    } else if(t === 'su'){
      if(typeof ouvrirSujets === 'function') ouvrirSujets(Number(k[1]) || k[1]);
      else showPg('subjects');
    } else if(t === 'fc'){
      showPg('fc');
      if(typeof filterFC === 'function') setTimeout(function(){
        filterFC(Number(k[1]) || 0); }, 60);
    } else if(t === 'vz'){
      if(typeof window.VZ_OUVRIR === 'function') window.VZ_OUVRIR(k[1]);
      else showPg('visualisations');
    } else if(t === 'fo'){
      showPg('formulas');
      viser('[data-rf="' + k[1] + '"]', 'pg-formulas');
    }
  }catch(e){ try{ console.warn('[recherche]', e); }catch(_){} }
}
function viserBloc(c, b){
  /* d'abord le marquage posé au découpage ; s'il a été effacé par un
     réaffichage du chapitre, on retrouve le bloc par son texte */
  var bl = (BL[c] || [])[b];
  var cible = bl ? nz(bl.x).slice(0, 80) : '';
  var essais = 0;
  (function boucle(){
    essais++;
    var p = document.getElementById('sect-cours');
    var el = p ? p.querySelector('[data-rb="' + b + '"]') : null;
    if(!el && p && cible){
      var cands = p.querySelectorAll(SEL), i;
      for(i = 0; i < cands.length; i++){
        var z = nz(cands[i].innerText || '');
        if(z.length > 10 && (z.indexOf(cible) === 0 || cible.indexOf(z.slice(0, 60)) === 0)){
          el = cands[i]; break;
        }
      }
      if(!el){
        for(i = 0; i < cands.length; i++){
          if(nz(cands[i].innerText || '').indexOf(cible.slice(0, 50)) >= 0){
            el = cands[i]; break;
          }
        }
      }
    }
    if(el){ flasher(el); return; }
    if(essais < 16) setTimeout(boucle, 120);
  })();
}
function flasher(el){
  try{ el.scrollIntoView({behavior:'smooth', block:'center'}); }
  catch(e){ try{ el.scrollIntoView(); }catch(_){} }
  el.classList.remove('rq-flash');
  void el.offsetWidth;
  el.classList.add('rq-flash');
}
function viser(sel, dans){
  var essais = 0;
  (function boucle(){
    essais++;
    var p = document.getElementById(dans);
    var el = p ? p.querySelector(sel) : document.querySelector(sel);
    if(el){
      try{ el.scrollIntoView({behavior:'smooth', block:'center'}); }
      catch(e){ el.scrollIntoView(); }
      el.classList.remove('rq-flash');
      void el.offsetWidth;
      el.classList.add('rq-flash');
      return;
    }
    if(essais < 14) setTimeout(boucle, 110);
  })();
}
function viserTexte(dans, texte){
  var essais = 0, cible = nz(texte);
  (function boucle(){
    essais++;
    var p = document.getElementById(dans);
    if(p){
      var els = p.querySelectorAll('.dt'), i;
      for(i=0;i<els.length;i++){
        if(nz(els[i].textContent).indexOf(cible) === 0){
          var bl = els[i].closest('.db') || els[i];
          try{ bl.scrollIntoView({behavior:'smooth', block:'center'}); }
          catch(e){ bl.scrollIntoView(); }
          bl.classList.remove('rq-flash'); void bl.offsetWidth;
          bl.classList.add('rq-flash');
          return;
        }
      }
    }
    if(essais < 14) setTimeout(boucle, 110);
  })();
}

/* ====================================================== interface */
var DERNIER = null, MINUT = null;

function compter(){
  ajouterEntrees();
  var c = Object.create(null), i;
  for(i=0;i<E.length;i++) c[E[i].y] = (c[E[i].y]||0) + 1;
  var tot = 0;
  Object.keys(D.ch).forEach(function(k){ tot += D.ch[k].n; });
  c.passage = tot;
  return c;
}

function poserChips(){
  var z = document.getElementById('rq-chips');
  if(!z) return;
  var c = compter();
  var ordre = ['tout','definitions','cours','auteurs','formules','chiffres',
    'faits','dossiers','atlas','sujets','fiches','resumes','visu'];
  z.innerHTML = ordre.map(function(f){
    var n = 0;
    if(f === 'tout') n = Object.keys(c).reduce(function(a,k){ return a + c[k]; }, 0);
    else (FAM[f]||[]).forEach(function(y){ n += (c[y]||0); });
    return '<button class="rq-c' + (f === FILTRE ? ' on' : '') + '" data-f="'
      + f + '">' + FAM_LIB[f] + '<i>' + n.toLocaleString('fr-FR') + '</i></button>';
  }).join('');
}

function lancer(){
  var v = (document.getElementById('rq-in').value || '').trim();
  document.getElementById('rq-x').classList.toggle('on', !!v);
  if(!v){
    document.getElementById('rq-etat').innerHTML = '';
    document.getElementById('rq-res').innerHTML =
      '<div class="rq-vide">Tape une notion, une définition, un auteur, une '
      + 'formule, un chiffre ou une date.<br>La recherche couvre les '
      + '<b>14 chapitres</b> au paragraphe près, et toutes les autres '
      + 'sections d’ÉcoSphère.</div>';
    return;
  }
  DERNIER = chercher(v);
  rendre(DERNIER);
}

function brancher(){
  var inp = document.getElementById('rq-in');
  if(!inp || inp.__rq) return;
  inp.__rq = 1;
  inp.addEventListener('input', function(){
    clearTimeout(MINUT);
    MINUT = setTimeout(lancer, 130);
  });
  document.getElementById('rq-x').addEventListener('click', function(){
    inp.value = ''; inp.focus(); lancer();
  });
  document.getElementById('rq-chips').addEventListener('click', function(e){
    var b = e.target.closest('[data-f]');
    if(!b) return;
    FILTRE = b.getAttribute('data-f');
    poserChips();
    lancer();
  });
  document.getElementById('rq-res').addEventListener('click', function(e){
    var q = e.target.closest('[data-q]');
    if(q){ inp.value = q.getAttribute('data-q'); lancer(); return; }
    var b = e.target.closest('[data-k]');
    if(!b) return;
    var k = null;
    try{ k = JSON.parse(b.getAttribute('data-k')); }catch(err){}
    ouvrir(k);
  });
  poserChips();
  lancer();
}

/* l'ancien moteur est désactivé : plus rien ne le lit ni ne le reconstruit */
function neutraliser(){
  try{
    window.doSearch = function(){ try{ lancer(); }catch(e){} };
    window.setF = function(){};
    window.rebuildSearchIndex = function(){};
  }catch(e){}
}

function preparer(){
  /* découpage des cours en blocs, un chapitre à la fois pour ne pas figer
     l'interface ; la recherche reste utilisable pendant ce temps */
  var ks = Object.keys(D.ch), i = 0;
  (function suite(){
    if(i >= ks.length){ vocabulaire(); return; }
    try{ blocsChapitre(ks[i]); }catch(e){}
    i++;
    setTimeout(suite, 0);
  })();
}

function demarrer(){
  neutraliser();
  brancher();
  preparer();
}

if(typeof window.showPg === 'function'){
  var vieux = window.showPg;
  window.showPg = function(id){
    var r = vieux.apply(this, arguments);
    if(id === 'search'){
      setTimeout(function(){
        brancher();
        var i = document.getElementById('rq-in');
        if(i && !i.value) { try{ i.focus(); }catch(e){} }
      }, 40);
    }
    return r;
  };
}

if(document.readyState === 'loading')
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(demarrer, 600); });
else setTimeout(demarrer, 600);
[1200, 3000, 6000].forEach(function(t){ setTimeout(function(){
  try{ neutraliser(); brancher(); }catch(e){} }, t); });

setTimeout(function(){
  try{
    var c = compter();
    console.log('[ÉcoSphère v218] Recherche reconstruite — '
      + Object.keys(D.ch).length + ' chapitres découpés en ' + c.passage
      + ' blocs, ' + Object.keys(D.def).length + ' définitions embarquées, '
      + (c.def+c.notion) + ' entrées de définition, ' + c.auteur + ' auteurs, '
      + c.dossier + ' dossiers, ' + c.atlas + ' idées, ' + c.chiffre
      + ' chiffres, ' + c.fait + ' faits datés');
  }catch(e){}
}, 8000);

window.__ECO_RECHERCHE = {debug:function(q){
    var R = chercher(q);
    return {n:R.n, groupes:R.groupes.length, Q:{cle:R.Q.cle, mots:R.Q.mots,
      corrige:R.Q.corrige, ch:R.Q.ch},
      liste:R.groupes.slice(0,14).map(function(g){ return {
        cle:g.cle, sc:g.sc, n:g.items.length,
        prim:{y:g.prim.y, t:g.prim.t, c:g.prim.c, b:g.prim.b, sc:g.prim.sc},
        types:g.items.map(function(x){ return x.y; })};})};
  },
  chercher:chercher, analyser:analyser,
  blocs:function(k){ return blocsChapitre(k); }, entrees:ajouterEntrees,
  compter:compter, filtre:function(f){ FILTRE = f; poserChips(); lancer(); },
  ouvrir:ouvrir, lancer:lancer, cle:cle, nz:nz};
})();
</script>
"""

MOTEUR = MOTEUR.replace('__PAYLOAD__', json.dumps(
    DATA, ensure_ascii=False, separators=(',', ':')))

s = s.rstrip() + '\n' + STYLE.strip() + '\n\n' + MOTEUR.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('ancien balisage retiré : %d octets' % len(ANCIEN))
print('définitions embarquées : %d' % len(DATA['def']))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
