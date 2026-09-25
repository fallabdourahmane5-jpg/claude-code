# -*- coding: utf-8 -*-
import json
D = json.load(open('ch6_maps.json'))
js = """
<script id="eco-carte-chapitre-6">
(function(){
'use strict';
if(window.__ECO_MAP6) return;
window.__ECO_MAP6 = true;
var V83 = %s;
var MD  = %s;
function poser(){
  var ok = false;
  try{ if(window.VISUAL_MAPS_V83){ window.VISUAL_MAPS_V83['6'] = V83; ok = true; } }catch(e){}
  try{ if(typeof MAP_DATA !== 'undefined' && !MAP_DATA[6]) MAP_DATA[6] = MD; }catch(e){}
  return ok;
}
if(!poser()){
  var n=0, it=setInterval(function(){ if(poser() || ++n>40) clearInterval(it); }, 100);
}
document.addEventListener('DOMContentLoaded', poser);
function rafraichir(){
  try{
    /* redessiner le selecteur pour faire apparaitre l'onglet du chapitre 6 */
    var sw = document.getElementById('map-switch');
    if(sw && sw.innerHTML && sw.innerHTML.indexOf('renderMaps(6)') === -1 && typeof window.renderMaps === 'function'){
      window.renderMaps(window.currentMapCh || 1);
    }
    if(window.currentMapCh === 6 && typeof window.renderVisualMap === 'function') window.renderVisualMap(6);
  }catch(e){}
}
setTimeout(function(){ poser(); rafraichir(); }, 1000);
setTimeout(function(){ poser(); rafraichir(); }, 2400);
if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    if(pg === 'maps'){ try{ poser(); setTimeout(rafraichir, 60); }catch(e){} }
    return r;
  };
}
})();
</script>
""" % (json.dumps(D['v83'], ensure_ascii=False), json.dumps(D['map'], ensure_ascii=False))
open('map6_patch.html','w').write(js)
print('bloc chapitre 6 :', f"{len(js):,}".replace(',',' '), 'caractères')
