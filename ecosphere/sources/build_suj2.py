# -*- coding: utf-8 -*-
import json
NEW = {}
NEW.update(json.load(open('ch9_new_subjects.json')))
NEW.update(json.load(open('ch10_new_subjects.json')))
NEW.update(json.load(open('ch21_new_subjects.json')))
MOB   = json.load(open('mob_1021.json'))
ADD18 = json.load(open('enrich_1_8.json'))

js = """
<script id="eco-maj-sujets-2">
(function(){
'use strict';
if(window.__ECO_MAJ_SUJ2) return;
window.__ECO_MAJ_SUJ2 = true;
var NEW = %s, MOB = %s, ADD18 = %s;

function appliquer(){
  if(typeof SUBJECTS_BANK_PREMIUM === 'undefined') return false;
  var nc = 0, nm = 0, na = 0;
  SUBJECTS_BANK_PREMIUM.forEach(function(s){
    var cle = String(s.chapter);
    /* 1. chapitres 9, 10 et 2e annee ch.1 : corriges entierement refondus */
    var r = NEW[s.id];
    if(r){
      if(MOB[cle] && MOB[cle][String(s.num)]) s.mobiliser = MOB[cle][String(s.num)];
      else if(r.mobiliser) s.mobiliser = r.mobiliser;
      s.commentaire  = r.commentaire;
      s.intro        = r.intro;
      s.problematique= r.problematique;
      s.plan         = r.plan;
      s.conclusion   = r.conclusion;
      nc++;
      return;
    }
    /* 2. filet de securite : chapitres a mobiliser analyses */
    if(MOB[cle] && MOB[cle][String(s.num)]){
      s.mobiliser = MOB[cle][String(s.num)];
      nm++;
      return;
    }
    /* 3. chapitres 1 a 8 : ajout transversal cible */
    var base = String(s.mobiliser || '').trim();
    if(base && /^[0-9,\\s]+$/.test(base)){ base = 'Ch. ' + base.replace(/\\s+/g,' '); s.mobiliser = base; }
    var add = ADD18[s.id];
    if(add && s.mobiliser.indexOf(add) === -1){
      s.mobiliser = base ? (base + ' \\u00b7 ' + add) : add;
      na++;
    }
  });
  window.__ECO_MAJ_SUJ2_STATS = {corriges:nc, mobiliser:nm, enrichis:na};
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
""" % (json.dumps(NEW, ensure_ascii=False), json.dumps(MOB, ensure_ascii=False), json.dumps(ADD18, ensure_ascii=False))
open('suj_patch2.html','w').write(js)
print('bloc sujets 2 :', f"{len(js):,}".replace(',',' '), 'caracteres ; corriges refondus :', len(NEW))
