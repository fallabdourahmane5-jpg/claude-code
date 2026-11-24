/* ÉcoSphère — garde-fou sur le texte des cours (v223).

   Plusieurs couches anciennes (v89 pour le chapitre 8, v90, v91, v98 et
   v124 pour les chapitres 1 à 7) embarquent des tables de cours vides et
   réécrivent CH_CONTENT[k].cours = "" à chaque appel de openCh. L'affichage
   n'en souffre pas — le cours visible est posé par une couche plus récente —
   mais le modèle de données est vidé dès la première ouverture d'un
   chapitre. Conséquence : la recherche ne peut plus indexer ces chapitres et
   les liens « Ouvrir le passage du cours » des corrections du quiz ne
   trouvent plus leur cible.

   Correction additive : on prend une empreinte du cours de chaque chapitre
   une fois toutes les couches de chargement passées, puis on remplace la
   propriété « cours » par un accesseur qui refuse les écritures
   destructrices. Une couche qui enrichit le cours (balisage des blocs,
   compléments) écrit une chaîne au moins aussi longue : elle passe. Une
   couche qui l'efface écrit une chaîne vide : elle est ignorée. */
(function(){
'use strict';
if(window.__ECO_GARDE_COURS) return;

function contenu(){
  try{ if(typeof CH_CONTENT !== 'undefined' && CH_CONTENT) return CH_CONTENT; }catch(e){}
  try{ if(window.CH_CONTENT) return window.CH_CONTENT; }catch(e){}
  return null;
}

var SNAP = {}, POSE = {}, SEUIL = 0.6;

function garder(C, k){
  if(POSE[k]) return false;
  var o = C[k];
  if(!o || typeof o !== 'object') return false;
  var val = typeof o.cours === 'string' ? o.cours : '';
  if(val.length < 200) return false;          /* rien de solide à protéger */
  var d = Object.getOwnPropertyDescriptor(o, 'cours');
  if(d && !d.configurable) return false;
  SNAP[k] = val;
  try{
    Object.defineProperty(o, 'cours', {
      configurable: true,
      enumerable: true,
      get: function(){ return val; },
      set: function(v){
        v = (v == null) ? '' : String(v);
        /* on accepte l'enrichissement, on refuse l'effacement */
        if(v.length >= val.length * SEUIL){ val = v; SNAP[k] = v; }
      }
    });
  }catch(e){ return false; }
  POSE[k] = true;
  return true;
}

function poser(){
  var C = contenu();
  if(!C) return 0;
  var n = 0;
  Object.keys(C).forEach(function(k){ if(garder(C, k)) n++; });
  return n;
}

/* En cas de besoin : réécrit le cours d'origine là où une couche aurait
   réussi à le vider avant la pose du garde-fou. */
function restaurer(){
  var C = contenu();
  if(!C) return 0;
  var n = 0;
  Object.keys(SNAP).forEach(function(k){
    if(!C[k]) return;
    var v = C[k].cours || '';
    if(v.length < SNAP[k].length * SEUIL){ C[k].cours = SNAP[k]; n++; }
  });
  return n;
}

window.__ECO_GARDE_COURS = {
  poser: poser, restaurer: restaurer,
  etat: function(){
    var C = contenu(), o = {};
    Object.keys(SNAP).forEach(function(k){
      o[k] = {empreinte: SNAP[k].length,
              courant: (C && C[k] && C[k].cours || '').length,
              garde: !!POSE[k]};
    });
    return o;
  }
};

function demarrer(){
  var n = poser();
  if(!n){ setTimeout(demarrer, 400); return; }
  /* une dernière passe après les minuteries des couches anciennes */
  setTimeout(poser, 1200);
}
if(document.readyState === 'loading'){
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(demarrer, 120); });
} else {
  setTimeout(demarrer, 120);
}
})();
