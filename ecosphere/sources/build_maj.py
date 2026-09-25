# -*- coding: utf-8 -*-
import json
D=json.load(open('auteurs_data.json'))
js = """
<script id="eco-maj-fiches-recherche-auteurs">
(function(){
'use strict';
if(window.__ECO_MAJ_FRA) return;
window.__ECO_MAJ_FRA = true;
var NOUVEAUX = %s;
var LIENS = %s;

function norm(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').trim();}

/* ---------- 1. AUTEURS ---------- */
function poserAuteurs(){
  if(typeof AUTHORS === 'undefined') return false;
  NOUVEAUX.forEach(function(a){
    var f = AUTHORS.find(function(x){ return norm(x.name) === norm(a.name); });
    if(f){
      f.chapters = Array.from(new Set([].concat(f.chapters || [f.ch], a.ch)));
      if(!f.oeuvres || !f.oeuvres.length) f.oeuvres = a.oeuvres;
      return;
    }
    AUTHORS.push(a);
  });
  LIENS.forEach(function(p){
    var f = AUTHORS.find(function(x){ return norm(x.name) === norm(p[0]); });
    if(f) f.chapters = Array.from(new Set([].concat(f.chapters || [f.ch], p[1])));
  });
  return true;
}

/* ---------- 2. FICHES : puces de filtre manquantes ---------- */
var CHIPS = [[9,'Ch.9'],[10,'Ch.10'],[21,'2ᵉ année — Ch.1']];
function poserChips(){
  var bar = document.querySelector('#pg-fc .fc-controls');
  if(!bar) return;
  CHIPS.forEach(function(c){
    var deja = [].slice.call(bar.querySelectorAll('button')).some(function(b){
      return b.textContent.trim() === c[1];
    });
    if(deja) return;
    var btn = document.createElement('button');
    btn.className = 'btn btn-g btn-sm';
    btn.textContent = c[1];
    btn.setAttribute('onclick', 'filterFC(' + c[0] + ')');
    bar.appendChild(btn);
  });
}

/* ---------- 2 bis. FICHES : badge « CH.21 » -> libelle d'annee ---------- */
function relabelBadges(racine){
  var zone = racine || document;
  var badges = zone.querySelectorAll('.fc-badge');
  for(var i=0;i<badges.length;i++){
    var t = badges[i].textContent;
    if(t.indexOf('21') === -1) continue;
    var nt = t.replace(/CH[.\\s]*21(?![0-9])/i, '2ᵉ ANNÉE · CH.1');
    if(nt !== t) badges[i].textContent = nt;
  }
}
function surveillerFiches(){ relabelBadges(document.querySelector('#pg-fc .fc-grid')); }
/* le rendu des fiches recree les badges : on relabellise apres chaque rendu */
['renderFC','filterFC','flipFC'].forEach(function(fn){
  if(typeof window[fn] !== 'function' || window[fn].__a2wrapped) return;
  var old = window[fn];
  var w = function(){
    var r = old.apply(this, arguments);
    try{ setTimeout(surveillerFiches, 0); }catch(e){}
    return r;
  };
  w.__a2wrapped = true;
  window[fn] = w;
});

/* ---------- 3. RECHERCHE : reconstruire les index ---------- */
function rafraichirIndex(){
  try{ if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex(); }catch(e){}
  try{ if(typeof renderAuthors === 'function' && document.getElementById('ag')) renderAuthors(); }catch(e){}
}

function boot(){
  poserAuteurs();
  poserChips();
  surveillerFiches();
  rafraichirIndex();
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
setTimeout(boot, 900);
setTimeout(boot, 2200);
setTimeout(boot, 4200);

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    try{
      if(pg === 'fc'){ setTimeout(function(){ poserChips(); surveillerFiches(); }, 60);
                       setTimeout(surveillerFiches, 400); setTimeout(surveillerFiches, 1000); }
      if(pg === 'authors') setTimeout(function(){ poserAuteurs(); rafraichirIndex(); }, 60);
    }catch(e){}
    return r;
  };
}
})();
</script>
""" % (json.dumps(D['nouveaux'], ensure_ascii=False), json.dumps(D['liens'], ensure_ascii=False))
open('maj_patch.html','w').write(js)
print('bloc :', f"{len(js):,}".replace(',',' '), 'caractères')
