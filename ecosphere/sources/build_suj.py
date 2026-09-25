# -*- coding: utf-8 -*-
import json
NEW9  = json.load(open('ch9_new_subjects.json'))   # id -> sujet complet
MOB   = json.load(open('mob_1021.json'))           # "10"/"21" -> {num: mobiliser}
ADD18 = json.load(open('enrich_1_8.json'))         # id -> complément

js = """
<script id="eco-maj-sujets">
(function(){
'use strict';
if(window.__ECO_MAJ_SUJ) return;
window.__ECO_MAJ_SUJ = true;
var NEW9 = %s, MOB = %s, ADD18 = %s;

function appliquer(){
  if(typeof SUBJECTS_BANK_PREMIUM === 'undefined') return false;
  var n9 = 0, nm = 0, na = 0;
  SUBJECTS_BANK_PREMIUM.forEach(function(s){
    /* 1. chapitre 9 : corrigés entièrement refondus */
    var r = NEW9[s.id];
    if(r){
      s.mobiliser    = r.mobiliser;
      s.commentaire  = r.commentaire;
      s.intro        = r.intro;
      s.problematique= r.problematique;
      s.plan         = r.plan;
      s.conclusion   = r.conclusion;
      n9++;
      return;
    }
    /* 2. chapitres 10 et 2e année : « chapitres à mobiliser » analysés */
    var cle = String(s.chapter);
    if(MOB[cle] && MOB[cle][String(s.num)]){
      s.mobiliser = MOB[cle][String(s.num)];
      nm++;
      return;
    }
    /* 3. chapitres 1 à 8 : ajout transversal ciblé */
    var base = String(s.mobiliser || '').trim();
    if(base && /^[0-9,\\s]+$/.test(base)){ base = 'Ch. ' + base.replace(/\\s+/g,' '); s.mobiliser = base; }
    var add = ADD18[s.id];
    if(add && s.mobiliser.indexOf(add) === -1){
      s.mobiliser = base ? (base + ' · ' + add) : add;
      na++;
    }
  });
  window.__ECO_MAJ_SUJ_STATS = {ch9:n9, mobiliser:nm, enrichis:na};
  return true;
}
function rafraichir(){
  try{ if(typeof window.renderSubjectsPremium === 'function') window.renderSubjectsPremium(); }catch(e){}
}
function boot(){ if(appliquer()) rafraichir(); }
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
setTimeout(boot, 900);
setTimeout(boot, 2400);
if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    if(pg === 'subjects'){ try{ appliquer(); setTimeout(rafraichir, 40); }catch(e){} }
    return r;
  };
}
})();
</script>
""" % (json.dumps(NEW9, ensure_ascii=False), json.dumps(MOB, ensure_ascii=False), json.dumps(ADD18, ensure_ascii=False))
open('suj_patch.html','w').write(js)
print('bloc sujets :', f"{len(js):,}".replace(',',' '), 'caractères')
