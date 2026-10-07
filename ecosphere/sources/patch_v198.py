#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete la banque de sujets : 20 dissertations corrigees par chapitre.

Chapitre 4 : 15 -> 20 · chapitre 8 : 10 -> 20 · 2e annee ch.3 : 14 -> 20.
Couche purement additive, re-entrante et idempotente (ajout par identifiant).
"""
import io, json, re

import suj198_ch4, suj198_ch8a, suj198_ch8b, suj198_ch23

SRC = 'app_v197.html'
DST = 'app_v198.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-sujets-v198' not in s

SUJETS = suj198_ch4.S4 + suj198_ch8a.S8A + suj198_ch8b.S8B + suj198_ch23.S23

# ------------------------------------------------------------- controles
assert len(SUJETS) == 21
vus = set()
for x in SUJETS:
    assert x['id'] not in vus, x['id']
    vus.add(x['id'])
    assert x['title'].endswith('?')
    for champ in ('mobiliser', 'commentaire', 'intro', 'problematique', 'conclusion'):
        assert len(x[champ]) > 130, (x['id'], champ)
    plan = x['plan']
    parties = [l for l in plan if re.match(r'^[IVX]+\. ', l)]
    sous = [l for l in plan if re.match(r'^[A-HJ-UW-Z]\. ', l)]
    args = [l for l in plan if re.match(r'^\d\) ', l)]
    assert (len(parties), len(sous), len(args)) == (3, 9, 27), (x['id'], len(parties), len(sous), len(args))
par_ch = {}
for x in SUJETS:
    par_ch[x['chapter']] = par_ch.get(x['chapter'], 0) + 1
assert par_ch == {4: 5, 8: 10, 23: 6}, par_ch

SCRIPT = r"""
<script id="eco-sujets-v198">
/* =====================================================================
   ÉcoSphère Pro — banque de sujets complétée (v198)
   Porte à vingt dissertations corrigées les chapitres 4, 8 et le
   chapitre 3 de deuxième année. Couche additive et idempotente.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_SUJ198) return;
window.__ECO_SUJ198 = true;

var D = __PAYLOAD__;
var bilan = {ajoutes:0, cartes:0};

function poser(){
  if(typeof SUBJECTS_BANK_PREMIUM === 'undefined') return false;
  var S = SUBJECTS_BANK_PREMIUM;
  if(!Array.isArray(S)) return false;
  var vus = {};
  S.forEach(function(x){ if(x && x.id) vus[x.id] = 1; });
  var n = 0;
  D.forEach(function(x){
    if(vus[x.id]) return;
    S.push(Object.assign({}, x));
    vus[x.id] = 1;
    n++;
  });
  if(n){ bilan.ajoutes += n; }
  return true;
}

/* le compteur de la carte « 2ᵉ année — Chapitre 3 » est figé a l'insertion :
   on le recalcule apres l'ajout des six sujets supplementaires. */
function majCartes(){
  try{
    var S = SUBJECTS_BANK_PREMIUM || [];
    [[23, '[data-ch23]'], [22, '[data-ch22]']].forEach(function(p){
      var n = S.filter(function(x){ return Number(x.chapter) === p[0]; }).length;
      if(!n) return;
      var carte = document.querySelector('#subjChaptersPremium ' + p[1] + ' .subj-ch-count');
      if(!carte) return;
      var voulu = n + ' dissertations corrigées';
      if(carte.textContent !== voulu){ carte.textContent = voulu; bilan.cartes++; }
    });
  }catch(e){}
}

function rendre(){
  try{ if(typeof renderSubjectsPremium === 'function') renderSubjectsPremium(); }catch(e){}
  majCartes();
}

function tout(){
  try{
    if(poser()){
      try{ if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex(); }catch(e){}
    }
  }catch(e){ try{ console.warn('[v198]', e); }catch(_){} }
  majCartes();
}

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tout);
else tout();
[400, 1200, 2600, 4200, 6500, 9500].forEach(function(t){ setTimeout(tout, t); });

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    tout();
    var r = old.apply(this, arguments);
    if(pg === 'subjects'){
      setTimeout(function(){ tout(); rendre(); }, 70);
      setTimeout(majCartes, 350);
    }
    return r;
  };
}
if(typeof window.setSubjectChapterPremium === 'function'){
  var oldS = window.setSubjectChapterPremium;
  window.setSubjectChapterPremium = function(){
    tout();
    var r = oldS.apply(this, arguments);
    setTimeout(majCartes, 40);
    return r;
  };
}
try{
  var z = document.getElementById('pg-subjects');
  if(z) new MutationObserver(function(){ majCartes(); }).observe(z, {childList:true, subtree:true});
}catch(e){}

window.__ECO_SUJ198_BILAN = bilan;
setTimeout(function(){
  console.log('[ÉcoSphère v198] banque de sujets — ' + bilan.ajoutes + ' dissertations ajoutées');
}, 7000);
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', json.dumps(SUJETS, ensure_ascii=False, separators=(',', ':')))
s = s.rstrip() + '\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('  sujets ajoutés : ch.4 +%d, ch.8 +%d, 2e année ch.3 +%d'
      % (par_ch[4], par_ch[8], par_ch[23]))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
