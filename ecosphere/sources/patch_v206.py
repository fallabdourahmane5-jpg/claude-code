#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute à ÉcoSphère la section « Autour d'une notion ».

Couche unique et additive : une page, un onglet, un index de 507 dossiers
répartis en 28 ensembles, une recherche, des filtres, et pour chaque dossier
rédigé la définition, l'explication, les mécanismes, les arguments et leurs
conditions, les critiques, les auteurs, les faits et chiffres, les liens vers
les autres sections et les formulations pour la dissertation.
"""
import io
import json

import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v205.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v206.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-autour-notion' not in s

DATA = json.load(open('autour_payload.json'))
assert len(DATA['dossiers']) == 507
assert len(DATA['ensembles']) == 28

STYLE = r"""
<style id="eco-autour-style">
#pg-autour{--an-fond:#f6f8fb;--an-bord:#dbe4ea;--an-txt:#0f172a;--an-txt2:#475569;
  --an-acc:#1d4ed8;--an-acc2:#0e7490;--an-ok:#047857;--an-att:#b45309;--an-gris:#94a3b8}
#pg-autour .an-wrap{max-width:1180px;margin:0 auto;padding:26px 20px 70px}
#pg-autour .an-h1{font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;
  margin:0 0 8px;color:var(--an-txt)}
#pg-autour .an-sub{color:var(--an-txt2);font-size:.92rem;line-height:1.62;margin:0 0 18px;max-width:900px}
#pg-autour .an-bar{display:flex;flex-wrap:wrap;gap:9px;align-items:center;
  background:#fff;border:1px solid var(--an-bord);border-radius:14px;padding:11px 12px;
  margin-bottom:16px;box-shadow:0 6px 22px rgba(15,23,42,.05)}
#pg-autour .an-bar input[type=text]{flex:1 1 300px;min-width:200px;border:1px solid var(--an-bord);
  border-radius:9px;padding:9px 12px;font-size:.9rem;font-family:inherit;color:var(--an-txt);background:#fff}
#pg-autour .an-bar select{border:1px solid var(--an-bord);border-radius:9px;padding:9px 10px;
  font-size:.84rem;font-family:inherit;background:#fff;color:var(--an-txt);
  max-width:300px;min-width:0;text-overflow:ellipsis}
#pg-autour .an-btn{border:1px solid var(--an-bord);background:#fff;border-radius:9px;
  padding:9px 13px;font-size:.82rem;font-family:inherit;cursor:pointer;color:var(--an-txt2)}
#pg-autour .an-btn:hover{background:#f1f5f9}
#pg-autour .an-nb{margin-left:auto;font-size:.8rem;color:var(--an-txt2);white-space:nowrap}
#pg-autour .an-ens{border:1px solid var(--an-bord);border-radius:14px;background:#fff;
  margin-bottom:12px;overflow:hidden}
#pg-autour .an-ensh{display:flex;align-items:center;gap:11px;padding:13px 15px;cursor:pointer;
  background:linear-gradient(180deg,#fff,#f8fafc)}
#pg-autour .an-ensh:hover{background:#f1f5f9}
#pg-autour .an-car{color:var(--an-gris);font-size:.7rem;transition:transform .18s}
#pg-autour .an-ens.open .an-car{transform:rotate(90deg)}
#pg-autour .an-ensn{font-weight:800;font-size:.95rem;color:var(--an-txt)}
#pg-autour .an-ensc{margin-left:auto;font-size:.75rem;color:var(--an-txt2);white-space:nowrap}
#pg-autour .an-ensb{display:none;padding:4px 14px 15px}
#pg-autour .an-ens.open .an-ensb{display:block}
#pg-autour .an-liste{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:9px}
#pg-autour .an-it{border:1px solid var(--an-bord);border-radius:11px;padding:10px 12px;
  cursor:pointer;background:#fff;transition:border-color .15s,box-shadow .15s}
#pg-autour .an-it:hover{border-color:var(--an-acc);box-shadow:0 5px 16px rgba(29,78,216,.1)}
#pg-autour .an-it b{display:block;font-size:.86rem;font-weight:700;color:var(--an-txt);line-height:1.38}
#pg-autour .an-it span{display:block;margin-top:5px;font-size:.73rem;color:var(--an-txt2)}
#pg-autour .an-et{display:inline-block;font-size:.65rem;font-weight:700;letter-spacing:.04em;
  text-transform:uppercase;padding:2px 7px;border-radius:7px;margin-top:6px}
#pg-autour .an-et.redige{background:rgba(4,120,87,.1);color:var(--an-ok)}
#pg-autour .an-et.a-venir{background:rgba(180,83,9,.1);color:var(--an-att)}
#pg-autour .an-et.hors-cours{background:rgba(148,163,184,.17);color:#64748b}
#pg-autour .an-et.renvoi{background:rgba(14,116,144,.1);color:var(--an-acc2)}
#pg-autour .an-qs{margin:9px 0 13px;padding:11px 13px;border-left:3px solid var(--an-acc2);
  background:#f0f9ff;border-radius:0 9px 9px 0}
#pg-autour .an-qs h4{margin:0 0 7px;font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;
  color:var(--an-acc2);font-weight:800}
#pg-autour .an-qs ul{margin:0;padding-left:18px}
#pg-autour .an-qs li{font-size:.83rem;color:var(--an-txt2);line-height:1.6;margin-bottom:3px}
#pg-autour .an-vide{padding:34px;text-align:center;color:var(--an-txt2);font-size:.9rem}
/* --------- dossier --------- */
#pg-autour .an-dos{background:#fff;border:1px solid var(--an-bord);border-radius:16px;
  padding:0;overflow:hidden;box-shadow:0 10px 36px rgba(15,23,42,.07)}
#pg-autour .an-dh{padding:19px 22px;background:linear-gradient(180deg,#f8fafc,#fff);
  border-bottom:1px solid var(--an-bord)}
#pg-autour .an-dret{border:1px solid var(--an-bord);background:#fff;border-radius:9px;
  padding:6px 12px;font-size:.8rem;cursor:pointer;color:var(--an-txt2);margin-bottom:11px;font-family:inherit}
#pg-autour .an-dret:hover{background:#f1f5f9}
#pg-autour .an-dt{font-family:'Playfair Display',serif;font-size:1.55rem;font-weight:900;
  margin:0 0 6px;color:var(--an-txt);line-height:1.22}
#pg-autour .an-dc{font-size:.9rem;color:var(--an-txt2);line-height:1.55;margin:0}
#pg-autour .an-dens{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;
  color:var(--an-acc2);font-weight:800;margin-bottom:5px}
#pg-autour .an-som{display:flex;flex-wrap:wrap;gap:6px;padding:12px 22px;border-bottom:1px solid var(--an-bord);
  background:#fcfdfe;position:sticky;top:0;z-index:4}
#pg-autour .an-som a{font-size:.76rem;padding:5px 11px;border-radius:999px;border:1px solid var(--an-bord);
  color:var(--an-txt2);cursor:pointer;background:#fff;text-decoration:none}
#pg-autour .an-som a:hover{background:var(--an-acc);color:#fff;border-color:var(--an-acc)}
#pg-autour .an-db{padding:6px 22px 24px}
#pg-autour .an-s{padding:17px 0;border-bottom:1px dashed #e8eef4}
#pg-autour .an-s:last-child{border-bottom:none}
#pg-autour .an-st{display:flex;align-items:center;gap:8px;font-size:.78rem;font-weight:800;
  text-transform:uppercase;letter-spacing:.06em;color:var(--an-acc);margin-bottom:9px}
#pg-autour .an-p{font-size:.93rem;line-height:1.72;color:#1e293b;margin:0 0 10px;text-align:justify}
#pg-autour .an-def{background:#eff6ff;border-left:3px solid var(--an-acc);border-radius:0 10px 10px 0;
  padding:13px 15px;font-size:.94rem;line-height:1.7;color:#1e293b}
#pg-autour .an-etape{display:flex;gap:11px;margin-bottom:11px}
#pg-autour .an-num{flex:0 0 25px;height:25px;border-radius:50%;background:var(--an-acc);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:.77rem;font-weight:800}
#pg-autour .an-etape div b{display:block;font-size:.88rem;color:var(--an-txt);margin-bottom:2px}
#pg-autour .an-etape div p{margin:0;font-size:.89rem;line-height:1.65;color:var(--an-txt2)}
#pg-autour .an-blo{border:1px solid var(--an-bord);border-radius:11px;padding:12px 14px;margin-bottom:10px}
#pg-autour .an-blo .an-a{font-size:.92rem;line-height:1.68;color:#1e293b;margin:0 0 9px;font-weight:600}
#pg-autour .an-sl{font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;
  display:block;margin-bottom:3px}
#pg-autour .an-cond .an-sl{color:var(--an-ok)}
#pg-autour .an-lim .an-sl{color:var(--an-att)}
#pg-autour .an-cond,#pg-autour .an-lim{font-size:.87rem;line-height:1.62;color:var(--an-txt2);margin-bottom:7px}
#pg-autour .an-crit{border-left:3px solid #b45309;background:#fffbeb;border-radius:0 10px 10px 0;
  padding:12px 14px;margin-bottom:10px}
#pg-autour .an-crit .t{font-size:.91rem;line-height:1.66;color:#1e293b;font-weight:600;margin:0 0 6px}
#pg-autour .an-crit .q{font-size:.8rem;color:var(--an-txt2);font-style:italic;margin:0 0 6px}
#pg-autour .an-crit .r{font-size:.88rem;line-height:1.64;color:var(--an-txt2);margin:0}
#pg-autour .an-aut{border:1px solid var(--an-bord);border-radius:11px;padding:11px 14px;margin-bottom:9px}
#pg-autour .an-aut .n{font-weight:800;font-size:.9rem;color:var(--an-txt);cursor:pointer}
#pg-autour .an-aut .n:hover{color:var(--an-acc);text-decoration:underline}
#pg-autour .an-aut .i{font-size:.89rem;color:#1e293b;line-height:1.6;margin:4px 0 5px}
#pg-autour .an-aut .pz{font-size:.87rem;color:var(--an-txt2);line-height:1.62;margin:0}
#pg-autour .an-fait{border-left:3px solid var(--an-acc2);background:#f0fdfa;border-radius:0 10px 10px 0;
  padding:11px 14px;margin-bottom:9px}
#pg-autour .an-fait .f{font-size:.9rem;color:#1e293b;line-height:1.62;margin:0 0 5px;font-weight:600}
#pg-autour .an-fait .pz{font-size:.87rem;color:var(--an-txt2);line-height:1.6;margin:0}
#pg-autour .an-tab{width:100%;border-collapse:collapse;font-size:.85rem;margin-top:4px}
#pg-autour .an-tab th,#pg-autour .an-tab td{border:1px solid var(--an-bord);padding:9px 11px;
  text-align:left;vertical-align:top;line-height:1.55}
#pg-autour .an-tab th{background:#f1f5f9;font-weight:800;font-size:.8rem;color:var(--an-txt)}
#pg-autour .an-tab td:first-child{font-weight:700;color:var(--an-txt);width:17%;background:#fafcfe}
#pg-autour .an-diss{border:1px solid #c7d2fe;background:#eef2ff;border-radius:11px;
  padding:13px 15px;margin-bottom:10px}
#pg-autour .an-diss .q{font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em;
  color:#4338ca;margin:0 0 7px}
#pg-autour .an-diss .ph{font-size:.93rem;line-height:1.7;color:#1e1b4b;margin:0 0 8px;text-align:justify}
#pg-autour .an-diss .rz{font-size:.87rem;line-height:1.62;color:#3730a3;margin:0 0 5px}
#pg-autour .an-diss .ez{font-size:.86rem;line-height:1.6;color:#4c1d95;margin:0}
#pg-autour .an-cop{float:right;border:1px solid #c7d2fe;background:#fff;border-radius:7px;
  padding:3px 9px;font-size:.72rem;cursor:pointer;color:#4338ca;font-family:inherit}
#pg-autour .an-lk{display:flex;flex-wrap:wrap;gap:6px}
#pg-autour .an-lk button{border:1px solid var(--an-bord);background:#fff;border-radius:999px;
  padding:6px 12px;font-size:.78rem;cursor:pointer;color:var(--an-txt2);font-family:inherit}
#pg-autour .an-lk button:hover{background:var(--an-acc);color:#fff;border-color:var(--an-acc)}
#pg-autour .an-grp{margin-bottom:11px}
#pg-autour .an-grp>b{display:block;font-size:.73rem;text-transform:uppercase;letter-spacing:.05em;
  color:var(--an-gris);font-weight:800;margin-bottom:5px}
#pg-autour .an-att{background:#fffbeb;border:1px solid #fde68a;border-radius:11px;padding:14px 16px;
  font-size:.89rem;line-height:1.65;color:#92400e}
#pg-autour mark{background:#fef08a;padding:0 2px;border-radius:3px}
@media(max-width:760px){
  #pg-autour .an-wrap{padding:18px 14px 56px}
  #pg-autour .an-h1{font-size:1.5rem}
  #pg-autour .an-dt{font-size:1.2rem}
  #pg-autour .an-liste{grid-template-columns:1fr}
  #pg-autour .an-bar{flex-direction:column;align-items:stretch}
  #pg-autour .an-bar input[type=text],#pg-autour .an-bar select{width:100%;max-width:100%;flex:0 0 auto}
  #pg-autour .an-nb{margin-left:0;width:100%}
  #pg-autour .an-dh,#pg-autour .an-som,#pg-autour .an-db{padding-left:14px;padding-right:14px}
  #pg-autour .an-tab,#pg-autour .an-tab tbody,#pg-autour .an-tab tr,#pg-autour .an-tab td{display:block;width:100%}
  #pg-autour .an-tab thead{display:none}
  #pg-autour .an-tab td:first-child{width:auto}
  #pg-autour .an-p{text-align:left}
}
</style>
"""

SCRIPT = r"""
<script id="eco-autour-notion">
/* =====================================================================
   ÉcoSphère — « Autour d'une notion » (v206)
   Un dossier par notion : définition, raisonnement, mécanismes, arguments
   et conditions, critiques, auteurs, faits et chiffres, liens vers les
   autres sections, formulations pour la dissertation.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_AUTOUR) return;
window.__ECO_AUTOUR = true;

var D = __PAYLOAD__;
var PAR_CLE = {};
D.dossiers.forEach(function(x){ PAR_CLE[x.cle] = x; });
var ENS = {};
D.ensembles.forEach(function(e){ ENS[e.num] = e; });

function nz(s){
  return String(s == null ? '' : s).normalize('NFD').replace(/[̀-ͯ]/g,'')
    .toLowerCase().replace(/’/g,"'").replace(/[^a-z0-9' ]+/g,' ').replace(/\s+/g,' ').trim();
}
function esc(s){
  return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/* texte de recherche de chaque dossier */
D.dossiers.forEach(function(x){
  var b = [x.titre, ENS[x.ens] ? ENS[x.ens].titre : '', x.court || '', x.defi || '', x.expl || ''];
  (x.mec || []).forEach(function(m){ b.push(m.t, m.e); });
  (x.args || []).forEach(function(a){ b.push(a.a, a.cond, a.lim); });
  (x.crit || []).forEach(function(c){ b.push(c.t, c.qui || '', c.rep); });
  (x.aut || []).forEach(function(a){ b.push(a.n, a.i, a.p); });
  (x.faits || []).forEach(function(f){ b.push(f.f, f.p); });
  (x.diss || []).forEach(function(s){ b.push(s.q, s.f, s.r, s.ex); });
  (x.liens.au || []).forEach(function(a){ b.push(a); });
  x.__r = nz(b.join(' '));
});

var S = {q:'', ens:'', etat:'', ouvert:null};
var deplies = {};

var LIBCH = {21:'2ᵉ année — ch.1', 22:'2ᵉ année — ch.2',
             23:'2ᵉ année — ch.3', 24:'2ᵉ année — ch.4'};
function libCh(k){ return LIBCH[k] || ('Chapitre ' + k); }

/* ------------------------------------------------- navigation inter-sections */
function allerCours(k){
  try{ if(typeof openCh === 'function'){ openCh(Number(k)); return; } }catch(e){}
  try{ showPg('chapter'); }catch(e){}
}
function allerFiches(k){
  try{ showPg('fc'); }catch(e){}
  setTimeout(function(){ try{ if(typeof filterFC === 'function') filterFC(Number(k)); }catch(e){} }, 60);
}
function allerSujets(k){
  try{ showPg('subjects'); }catch(e){}
  setTimeout(function(){
    try{ if(typeof setSubjectChapterPremium === 'function') setSubjectChapterPremium(Number(k)); }catch(e){}
  }, 110);
}
function allerAtlas(k){
  try{ showPg('atlas'); }catch(e){}
  setTimeout(function(){
    try{
      var sel = document.getElementById('at-ch');
      if(sel){ sel.value = String(k); sel.dispatchEvent(new Event('change')); }
    }catch(e){}
  }, 110);
}
function allerAuteur(nom){
  try{ if(typeof openAuthorByName === 'function'){ openAuthorByName(nom); return; } }catch(e){}
  try{
    showPg('authors');
    setTimeout(function(){
      var q = document.getElementById('aq') || document.querySelector('#pg-authors input[type=text]');
      if(q){ q.value = nom; q.dispatchEvent(new Event('input', {bubbles:true})); }
    }, 80);
  }catch(e){}
}
function allerChiffres(k){
  try{ if(typeof ouvrirChiffres === 'function'){ ouvrirChiffres(String(k)); return; } }catch(e){}
  try{ showPg('chiffres'); }catch(e){}
}

/* ------------------------------------------------------------- construction */
function construire(){
  if(document.getElementById('pg-autour')) return true;
  var hote = document.getElementById('pg-prog') || document.querySelector('.pg');
  if(!hote || !hote.parentNode) return false;

  var pg = document.createElement('div');
  pg.className = 'pg';
  pg.id = 'pg-autour';
  var opts = D.ensembles.map(function(e){
    return '<option value="' + e.num + '">' + e.num + '. ' + esc(e.titre) + '</option>';
  }).join('');

  pg.innerHTML =
    '<div class="an-wrap">' +
      '<h1 class="an-h1">🧩 Autour d’une notion</h1>' +
      '<p class="an-sub">Choisis une notion du programme et retrouve au même endroit tout ce qui ' +
        'permet de la comprendre et de la mobiliser : la définition, le raisonnement détaillé, ' +
        'les mécanismes étape par étape, les arguments avec leurs conditions de validité et ' +
        'leurs limites, les critiques et les débats, les auteurs et leurs idées précises, les faits ' +
        'et les chiffres, les liens vers les chapitres, fiches, sujets et idées de l’Atlas, et ' +
        'plusieurs formulations rédigées pour la dissertation.</p>' +
      '<div class="an-bar">' +
        '<input type="text" id="an-q" placeholder="Rechercher une notion, un mécanisme, un auteur, un argument…">' +
        '<select id="an-ens"><option value="">Tous les ensembles</option>' + opts + '</select>' +
        '<select id="an-etat"><option value="">Tous les dossiers</option>' +
          '<option value="redige">Dossiers rédigés</option>' +
          '<option value="a-venir">Dossiers à venir</option>' +
          '<option value="hors-cours">Hors du champ des cours chargés</option></select>' +
        '<button class="an-btn" id="an-rz">Réinitialiser</button>' +
        '<button class="an-btn" id="an-tt">Tout déplier</button>' +
        '<span class="an-nb" id="an-nb"></span>' +
      '</div>' +
      '<div id="an-corps"></div>' +
    '</div>';
  hote.parentNode.insertBefore(pg, hote);

  document.getElementById('an-q').addEventListener('input', function(){ S.q = this.value; rendre(); });
  document.getElementById('an-ens').addEventListener('change', function(){ S.ens = this.value; rendre(); });
  document.getElementById('an-etat').addEventListener('change', function(){ S.etat = this.value; rendre(); });
  document.getElementById('an-rz').addEventListener('click', function(){
    S = {q:'', ens:'', etat:'', ouvert:null};
    deplies = {};
    ['an-q','an-ens','an-etat'].forEach(function(i){ var el = document.getElementById(i); if(el) el.value = ''; });
    rendre();
  });
  document.getElementById('an-tt').addEventListener('click', function(){
    var on = this.getAttribute('data-on') === '1';
    this.setAttribute('data-on', on ? '0' : '1');
    this.textContent = on ? 'Tout déplier' : 'Tout replier';
    D.ensembles.forEach(function(e){ deplies[e.num] = !on; });
    rendre();
  });
  document.getElementById('an-corps').addEventListener('click', clic);
  return true;
}

/* ----------------------------------------------------------------- filtrage */
function filtrer(){
  var mots = nz(S.q).split(' ').filter(Boolean);
  return D.dossiers.filter(function(x){
    if(S.ens && String(x.ens) !== S.ens) return false;
    if(S.etat && x.etat === 'renvoi'){
      var o = PAR_CLE[x.vers];
      if(!o || o.etat !== S.etat) return false;
      for(var j = 0; j < mots.length; j++) if(o.__r.indexOf(mots[j]) < 0) return false;
      return true;
    }
    if(x.etat === 'renvoi'){
      var o2 = PAR_CLE[x.vers];
      for(var k = 0; k < mots.length; k++){
        if((o2 ? o2.__r : x.__r).indexOf(mots[k]) < 0) return false;
      }
      return true;
    }
    if(S.etat && x.etat !== S.etat) return false;
    for(var i = 0; i < mots.length; i++) if(x.__r.indexOf(mots[i]) < 0) return false;
    return true;
  });
}
function surligner(t, mots){
  var o = esc(t);
  mots.forEach(function(m){
    if(m.length < 3) return;
    try{ o = o.replace(new RegExp('(' + m.replace(/[.*+?^${}()|[\]\\]/g,'\\$&') + ')','gi'), '<mark>$1</mark>'); }catch(e){}
  });
  return o;
}

var ETIQ = {redige:'dossier complet', 'a-venir':'à venir',
            'hors-cours':'hors des cours chargés', renvoi:'renvoi'};

/* ------------------------------------------------------------------- index */
function rendre(){
  var box = document.getElementById('an-corps');
  if(!box) return;
  if(S.ouvert){ rendreDossier(S.ouvert); return; }
  var mots = nz(S.q).split(' ').filter(Boolean);
  var res = filtrer();
  var cpt = document.getElementById('an-nb');
  var nr = res.filter(function(x){
    return x.etat === 'redige' ||
      (x.etat === 'renvoi' && PAR_CLE[x.vers] && PAR_CLE[x.vers].etat === 'redige');
  }).length;
  if(cpt) cpt.textContent = res.length + ' dossier' + (res.length > 1 ? 's' : '') +
    ' · ' + nr + ' rédigé' + (nr > 1 ? 's' : '');
  if(!res.length){
    box.innerHTML = '<div class="an-vide">Aucun dossier ne correspond à ces critères.</div>';
    return;
  }
  var parEns = {};
  res.forEach(function(x){ (parEns[x.ens] = parEns[x.ens] || []).push(x); });
  var filtre = !!(mots.length || S.etat);
  var h = '';
  D.ensembles.forEach(function(e){
    var l = parEns[e.num];
    if(!l) return;
    var ouvert = filtre || !!S.ens || deplies[e.num];
    var nr2 = l.filter(function(x){
      return x.etat === 'redige' ||
        (x.etat === 'renvoi' && PAR_CLE[x.vers] && PAR_CLE[x.vers].etat === 'redige');
    }).length;
    h += '<div class="an-ens' + (ouvert ? ' open' : '') + '" data-e="' + e.num + '">' +
      '<div class="an-ensh" data-pli="' + e.num + '">' +
        '<span class="an-car">▶</span>' +
        '<span class="an-ensn">' + e.num + '. ' + esc(e.titre) + '</span>' +
        '<span class="an-ensc">' + l.length + ' dossier' + (l.length > 1 ? 's' : '') +
          (nr2 ? ' · ' + nr2 + ' rédigé' + (nr2 > 1 ? 's' : '') : '') + '</span>' +
      '</div><div class="an-ensb">' +
        (e.questions && e.questions.length ?
          '<div class="an-qs"><h4>Questions à explorer</h4><ul>' +
          e.questions.map(function(q){ return '<li>' + esc(q) + '</li>'; }).join('') +
          '</ul></div>' : '') +
        '<div class="an-liste">' + l.map(function(x){
          var n = x.liens.ch.length;
          return '<div class="an-it" data-go="' + esc(x.cle) + '">' +
            '<b>' + surligner(x.titre, mots) + '</b>' +
            (x.court ? '<span>' + esc(x.court) + '</span>' :
              (n ? '<span>' + n + ' chapitre' + (n > 1 ? 's' : '') + ' concerné' +
                   (n > 1 ? 's' : '') + '</span>' : '')) +
            '<span class="an-et ' + x.etat + '">' + ETIQ[x.etat] + '</span></div>';
        }).join('') + '</div>' +
      '</div></div>';
  });
  box.innerHTML = h;
}

/* ----------------------------------------------------------------- dossier */
function bloc(id, titre, icone, corps){
  return '<div class="an-s" id="' + id + '"><div class="an-st"><span>' + icone +
         '</span>' + titre + '</div>' + corps + '</div>';
}

function rendreDossier(cle){
  var x = PAR_CLE[cle];
  var box = document.getElementById('an-corps');
  if(!x || !box) return;
  if(x.etat === 'renvoi'){ S.ouvert = x.vers; rendreDossier(x.vers); return; }
  var e = ENS[x.ens] || {titre:''};
  var h = '<div class="an-dos"><div class="an-dh">' +
    '<button class="an-dret" data-retour="1">← Retour à la liste</button>' +
    '<div class="an-dens">Ensemble ' + x.ens + ' · ' + esc(e.titre) + '</div>' +
    '<h2 class="an-dt">' + esc(x.titre) + '</h2>' +
    (x.court ? '<p class="an-dc">' + esc(x.court) + '</p>' : '') + '</div>';

  var som = [];
  if(x.etat === 'redige'){
    som.push(['an-x-def','Définition']);
    som.push(['an-x-exp','Le raisonnement']);
    som.push(['an-x-mec','Mécanismes']);
    som.push(['an-x-arg','Arguments et conditions']);
    som.push(['an-x-cri','Critiques et débats']);
    if(x.comp) som.push(['an-x-cmp','Comparaison']);
    som.push(['an-x-aut','Auteurs']);
    som.push(['an-x-fai','Faits et chiffres']);
    som.push(['an-x-dis','En dissertation']);
  }
  som.push(['an-x-lie','Liens dans ÉcoSphère']);
  h += '<div class="an-som">' + som.map(function(a){
    return '<a data-anc="' + a[0] + '">' + a[1] + '</a>';
  }).join('') + '</div><div class="an-db">';

  if(x.etat === 'redige'){
    h += bloc('an-x-def', 'Définition', '📌',
      '<div class="an-def">' + esc(x.defi) + '</div>');
    h += bloc('an-x-exp', 'Le raisonnement en détail', '🧠',
      '<p class="an-p">' + esc(x.expl) + '</p>');
    h += bloc('an-x-mec', 'Les mécanismes, étape par étape', '⚙️',
      x.mec.map(function(m, i){
        return '<div class="an-etape"><div class="an-num">' + (i + 1) + '</div>' +
          '<div><b>' + esc(m.t) + '</b><p>' + esc(m.e) + '</p></div></div>';
      }).join(''));
    h += bloc('an-x-arg', 'Arguments, conditions de validité et limites', '⚖️',
      x.args.map(function(a){
        return '<div class="an-blo"><p class="an-a">' + esc(a.a) + '</p>' +
          '<div class="an-cond"><span class="an-sl">Conditions de validité</span>' + esc(a.cond) + '</div>' +
          '<div class="an-lim"><span class="an-sl">Limites</span>' + esc(a.lim) + '</div></div>';
      }).join(''));
    h += bloc('an-x-cri', 'Critiques, oppositions et débats', '🗣️',
      x.crit.map(function(c){
        return '<div class="an-crit"><p class="t">' + esc(c.t) + '</p>' +
          (c.qui ? '<p class="q">' + esc(c.qui) + '</p>' : '') +
          '<p class="r"><b>Ce qu’on peut répondre —</b> ' + esc(c.rep) + '</p></div>';
      }).join(''));
    if(x.comp){
      h += bloc('an-x-cmp', esc(x.comp.titre), '🔍',
        '<table class="an-tab"><thead><tr><th>Critère</th><th>' + esc(x.comp.a) +
        '</th><th>' + esc(x.comp.b) + '</th></tr></thead><tbody>' +
        x.comp.lignes.map(function(l){
          return '<tr><td>' + esc(l[0]) + '</td><td>' + esc(l[1]) + '</td><td>' + esc(l[2]) + '</td></tr>';
        }).join('') + '</tbody></table>');
    }
    h += bloc('an-x-aut', 'Les auteurs et leurs idées sur cette notion', '👤',
      x.aut.map(function(a){
        return '<div class="an-aut"><div class="n" data-aut="' + esc(a.n) + '">' + esc(a.n) + '</div>' +
          '<p class="i">' + esc(a.i) + '</p><p class="pz">' + esc(a.p) + '</p></div>';
      }).join(''));
    h += bloc('an-x-fai', 'Faits, exemples et chiffres', '📊',
      x.faits.map(function(f){
        return '<div class="an-fait"><p class="f">' + esc(f.f) + '</p>' +
          '<p class="pz"><b>Ce que cela montre —</b> ' + esc(f.p) + '</p></div>';
      }).join(''));
    h += bloc('an-x-dis', 'Mobiliser la notion en dissertation', '✍️',
      x.diss.map(function(s, i){
        return '<div class="an-diss"><p class="q">' + esc(s.q) +
          '<button class="an-cop" data-cop="cop-' + esc(x.cle) + '-' + i + '">copier</button></p>' +
          '<p class="ph" id="cop-' + esc(x.cle) + '-' + i + '">' + esc(s.f) + '</p>' +
          '<p class="rz"><b>Le raisonnement —</b> ' + esc(s.r) + '</p>' +
          '<p class="ez"><b>L’exemple —</b> ' + esc(s.ex) + '</p></div>';
      }).join(''));
  } else if(x.etat === 'hors-cours'){
    h += '<div class="an-s"><div class="an-att">Cette notion ne figure pas dans les ' +
      'chapitres actuellement chargés dans ÉcoSphère. Aucun dossier n’a donc été ' +
      'rédigé : il le sera dès que le chapitre correspondant sera ajouté, afin de ne ' +
      'produire aucune définition ni aucune attribution d’auteur qui ne soit justifiée ' +
      'par les cours.</div></div>';
  } else {
    h += '<div class="an-s"><div class="an-att">Ce dossier est prévu et sa matière est ' +
      'déjà présente dans les cours : les liens ci-dessous indiquent où la notion ' +
      'intervient. La rédaction complète — mécanismes, arguments, critiques, auteurs, ' +
      'chiffres et formulations — sera ajoutée lors d’une prochaine vague.</div></div>';
  }

  /* --------- liens --------- */
  var L = x.liens, lk = '';
  if(L.ch.length){
    lk += '<div class="an-grp"><b>Chapitres où la notion intervient</b><div class="an-lk">' +
      L.ch.map(function(c){
        return '<button data-ch="' + c.k + '">📖 ' + esc(c.lib) + ' · ' + c.n + '</button>';
      }).join('') + '</div></div>';
    lk += '<div class="an-grp"><b>Autres sections, par chapitre</b><div class="an-lk">' +
      L.ch.slice(0, 5).map(function(c){
        return '<button data-fc="' + c.k + '">🃏 Fiches ' + esc(c.lib) + '</button>' +
               '<button data-at="' + c.k + '">🗺️ Atlas ' + esc(c.lib) + '</button>' +
               '<button data-cf="' + c.k + '">🔢 Chiffres ' + esc(c.lib) + '</button>' +
               '<button data-su="' + c.k + '">📝 Sujets ' + esc(c.lib) + '</button>';
      }).join('') + '</div></div>';
  }
  if(L.fi.length){
    lk += '<div class="an-grp"><b>Fiches portant ce nom</b><div class="an-lk">' +
      L.fi.map(function(f){
        return '<button data-fc="' + f.k + '">🃏 ' + esc(f.t) + '</button>';
      }).join('') + '</div></div>';
  }
  if(L.at.length){
    lk += '<div class="an-grp"><b>Idées de l’Atlas sur cette notion</b><div class="an-lk">' +
      L.at.map(function(a){
        return '<button data-at="' + a.k + '">🗺️ ' + esc(a.n) + ' — ' +
          esc(a.ti.slice(0, 60)) + '</button>';
      }).join('') + '</div></div>';
  }
  if(L.su.length){
    lk += '<div class="an-grp"><b>Sujets où la notion est centrale</b><div class="an-lk">' +
      L.su.map(function(u){
        return '<button data-su="' + u.ch + '">📝 ' + esc(u.t.slice(0, 70)) + '</button>';
      }).join('') + '</div></div>';
  }
  if(L.au && L.au.length){
    lk += '<div class="an-grp"><b>Auteurs dont une idée porte sur cette notion</b><div class="an-lk">' +
      L.au.map(function(a){ return '<button data-aut="' + esc(a) + '">👤 ' + esc(a) + '</button>'; })
      .join('') + '</div></div>';
  }
  if(x.voisins && x.voisins.length){
    lk += '<div class="an-grp"><b>Notions liées</b><div class="an-lk">' +
      x.voisins.map(function(v){
        var o = PAR_CLE[v];
        return o ? '<button data-go="' + esc(v) + '">🧩 ' + esc(o.titre) + '</button>' : '';
      }).join('') + '</div></div>';
  }
  var e2 = ENS[x.ens];
  if(e2 && e2.questions && e2.questions.length){
    lk += '<div class="an-grp"><b>Questions de dissertation de cet ensemble</b>' +
      '<ul style="margin:0;padding-left:18px">' + e2.questions.map(function(q){
        return '<li style="font-size:.85rem;color:#475569;line-height:1.6">' + esc(q) + '</li>';
      }).join('') + '</ul></div>';
  }
  h += bloc('an-x-lie', 'Liens dans ÉcoSphère', '🔗',
            lk || '<p class="an-p">Aucun lien automatique n’a pu être établi.</p>');

  h += '</div></div>';
  box.innerHTML = h;
  try{ window.scrollTo(0, 0); }catch(err){}
}

/* ------------------------------------------------------------ interactions */
function clic(ev){
  var t = ev.target;
  var r = t.closest('[data-retour]');
  if(r){ S.ouvert = null; rendre(); return; }
  var g = t.closest('[data-go]');
  if(g){ S.ouvert = g.getAttribute('data-go'); rendreDossier(S.ouvert); return; }
  var p = t.closest('[data-pli]');
  if(p){
    var n = p.getAttribute('data-pli');
    deplies[n] = !p.parentNode.classList.contains('open');
    p.parentNode.classList.toggle('open');
    return;
  }
  var a = t.closest('[data-anc]');
  if(a){
    var el = document.getElementById(a.getAttribute('data-anc'));
    if(el) try{ el.scrollIntoView({behavior:'smooth', block:'start'}); }catch(e){ el.scrollIntoView(); }
    return;
  }
  var c = t.closest('[data-cop]');
  if(c){
    var src = document.getElementById(c.getAttribute('data-cop'));
    if(src){
      var fini = function(){ c.textContent = 'copié'; setTimeout(function(){ c.textContent = 'copier'; }, 1300); };
      try{
        if(navigator.clipboard && navigator.clipboard.writeText){
          navigator.clipboard.writeText(src.textContent).then(fini, fini);
        } else {
          var ta = document.createElement('textarea'); ta.value = src.textContent;
          document.body.appendChild(ta); ta.select();
          try{ document.execCommand('copy'); }catch(e){}
          document.body.removeChild(ta); fini();
        }
      }catch(e){ fini(); }
    }
    return;
  }
  var b;
  if((b = t.closest('[data-ch]'))){ allerCours(b.getAttribute('data-ch')); return; }
  if((b = t.closest('[data-fc]'))){ allerFiches(b.getAttribute('data-fc')); return; }
  if((b = t.closest('[data-at]'))){ allerAtlas(b.getAttribute('data-at')); return; }
  if((b = t.closest('[data-cf]'))){ allerChiffres(b.getAttribute('data-cf')); return; }
  if((b = t.closest('[data-su]'))){ allerSujets(b.getAttribute('data-su')); return; }
  if((b = t.closest('[data-aut]'))){ allerAuteur(b.getAttribute('data-aut')); return; }
}

/* ------------------------------------------------------------- onglet, page */
function poserNav(){
  if(document.getElementById('an-nav')) return;
  var nav = document.querySelector('nav');
  if(!nav) return;
  var ref = null;
  nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'atlas'") >= 0) ref = b;
  });
  var b = document.createElement('button');
  b.className = 'nt';
  b.id = 'an-nav';
  b.setAttribute('onclick', "showPg('autour')");
  b.textContent = '🧩 Autour d’une notion';
  if(ref && ref.nextSibling) nav.insertBefore(b, ref.nextSibling);
  else nav.appendChild(b);
}
function marquer(id){
  try{
    var vise = null;
    document.querySelectorAll('nav .nt').forEach(function(b){
      if((b.getAttribute('onclick') || '').indexOf("'" + id + "'") >= 0) vise = b;
    });
    if(vise){
      document.querySelectorAll('nav .nt').forEach(function(b){ b.classList.remove('on'); });
      vise.classList.add('on');
    }
  }catch(e){}
}
function brancher(){
  if(typeof window.showPg !== 'function' || window.showPg.__autour) return;
  var old = window.showPg;
  var w = function(pg){
    if(pg === 'autour'){
      construire();
      document.querySelectorAll('.pg').forEach(function(p){ p.classList.remove('on'); });
      var el = document.getElementById('pg-autour');
      if(el) el.classList.add('on');
      var c = document.getElementById('an-corps');
      if(c && !c.innerHTML) rendre();
      marquer('autour');
      try{ window.scrollTo(0, 0); }catch(e){}
      return;
    }
    var r = old.apply(this, arguments);
    marquer(pg);
    return r;
  };
  w.__autour = true;
  window.showPg = w;
}

/* ouvrir un dossier depuis l'extérieur */
window.ouvrirNotion = function(cle){
  try{
    showPg('autour');
    setTimeout(function(){
      if(PAR_CLE[cle]){ S.ouvert = cle; rendreDossier(cle); }
    }, 60);
  }catch(e){}
};

function boot(){
  try{ if(construire()) poserNav(); brancher(); }
  catch(e){ try{ console.warn('[autour]', e); }catch(_){} }
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
[300, 900, 2000, 4000, 7000].forEach(function(t){ setTimeout(boot, t); });

setTimeout(function(){
  var n = D.dossiers.length;
  var r = D.dossiers.filter(function(x){ return x.etat === 'redige'; }).length;
  console.log('[ÉcoSphère v206] Autour d’une notion — ' + n + ' dossiers, ' +
    r + ' rédigés, ' + D.ensembles.length + ' ensembles');
}, 6000);
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', json.dumps(DATA, ensure_ascii=False,
                                                  separators=(',', ':')))

s = s.rstrip() + '\n' + STYLE.strip() + '\n\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)

etats = {}
for x in DATA['dossiers']:
    etats[x['etat']] = etats.get(x['etat'], 0) + 1
print('  dossiers : %d (%s)' % (len(DATA['dossiers']),
      ', '.join('%s %d' % (k, v) for k, v in sorted(etats.items()))))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
