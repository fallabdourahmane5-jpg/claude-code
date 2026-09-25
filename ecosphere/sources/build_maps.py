# -*- coding: utf-8 -*-
import json
MAPS = json.load(open('maps_v83_new.json'))
js = """
<script id="eco-cartes-v83-ajout">
(function(){
'use strict';
if(window.__ECO_MAPS_ADD) return;
window.__ECO_MAPS_ADD = true;
var NOUVELLES = %s;
function poser(){
  var T = window.VISUAL_MAPS_V83;
  if(!T) return false;
  Object.keys(NOUVELLES).forEach(function(k){ T[k] = NOUVELLES[k]; });
  return true;
}
if(!poser()){
  var n = 0;
  var it = setInterval(function(){ if(poser() || ++n > 40) clearInterval(it); }, 100);
}
document.addEventListener('DOMContentLoaded', poser);
/* si une carte concernee est deja affichee, on la redessine */
function rafraichir(){
  try{
    var ch = window.currentMapCh;
    if(ch && NOUVELLES[String(ch)] && typeof window.renderVisualMap === 'function'){
      window.renderVisualMap(ch);
    }
  }catch(e){}
}
setTimeout(function(){ poser(); rafraichir(); }, 900);
setTimeout(function(){ poser(); rafraichir(); }, 2200);
})();
</script>
""" % json.dumps(MAPS, ensure_ascii=False)
open('maps_patch.html','w').write(js)
print('bloc cartes :', f"{len(js):,}".replace(',',' '), 'caractères')
