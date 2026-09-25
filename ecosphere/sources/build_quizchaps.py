# -*- coding: utf-8 -*-
js = r"""
<script id="eco-quiz-chapitres-manquants">
(function(){
'use strict';
if(window.__ECO_QUIZ_CHAPS) return;
window.__ECO_QUIZ_CHAPS = true;

/* Chapitres presents dans les banques de questions mais absents des deux
   listes de la page Quiz (CHAPTER_LABELS s'arrete au chapitre 8).
   Le moteur (startQuiz, selectedChapters, availableQuestions) les gere deja :
   seule l'interface de selection etait incomplete. */
var SUP = [
  {n:9,  court:'Chapitre 9',          lab:'Taille & stratégies des entreprises'},
  {n:10, court:'Chapitre 10',         lab:'Sociologie des organisations & du travail'},
  {n:21, court:'2ᵉ année — Ch.1', lab:'Mondialisation & déséquilibres extérieurs'}
];

var occupe = false;

function libelleCase(c){
  return (c.n === 21 ? '2ᵉ année — Ch.1' : 'Ch.' + c.n) + ' · ' + c.lab;
}

/* 1. Cases a cocher du generateur intelligent */
function poserCases(){
  var grid = document.getElementById('adv-chapters');
  if(!grid) return;
  SUP.forEach(function(c){
    if(grid.querySelector('.adv-ch[value="' + c.n + '"]')) return;
    var l = document.createElement('label');
    l.className = 'smart-check';
    var inp = document.createElement('input');
    inp.className = 'adv-ch';
    inp.type = 'checkbox';
    inp.value = String(c.n);
    l.appendChild(inp);
    l.appendChild(document.createTextNode(' ' + libelleCase(c)));
    inp.addEventListener('change', function(){
      l.classList.toggle('on', inp.checked);
      /* refreshTags() est lexical : on le declenche via une case deja liee,
         sans modifier son etat (le handler d'origine est idempotent). */
      var ref = grid.querySelector('.adv-ch[value="1"]');
      if(ref){ try{ ref.dispatchEvent(new Event('change')); }catch(e){} }
    });
    grid.appendChild(l);
  });
}

/* 2. Boutons de l'acces rapide classique */
function poserBoutons(){
  var grid = document.querySelector('#pg-quiz .quiz-options-grid');
  if(!grid) return;
  var dernier = null;
  var btns = grid.querySelectorAll('.qo-btn');
  for(var i = 0; i < btns.length; i++){
    var oc = btns[i].getAttribute('onclick') || '';
    if(/startFailedQuiz/.test(oc)){ dernier = btns[i]; break; }
  }
  SUP.forEach(function(c){
    var deja = false;
    grid.querySelectorAll('.qo-btn').forEach(function(b){
      var oc = b.getAttribute('onclick') || '';
      if(oc.replace(/\s/g,'') === 'startQuiz(' + c.n + ')') deja = true;
    });
    if(deja) return;
    var b = document.createElement('button');
    b.className = 'qo-btn';
    b.setAttribute('onclick', 'startQuiz(' + c.n + ')');
    var sp = document.createElement('span');
    sp.textContent = c.lab;
    b.appendChild(document.createTextNode(c.court));
    b.appendChild(sp);
    if(dernier) grid.insertBefore(b, dernier); else grid.appendChild(b);
  });
}

/* 3. Resume « Chapitres 9, 10, 21 » : le 21 doit se lire « 2e annee ch.1 ».
   Le relabellage existant ne traite que la forme au singulier. */
function relibellerResume(){
  var zone = document.getElementById('pg-quiz');
  if(!zone) return;
  var it = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT, null);
  var n, cibles = [];
  while((n = it.nextNode())){
    if(/Chapitres\s+\d/.test(n.nodeValue) && /(^|[\s,])21([\s,]|$)/.test(n.nodeValue)) cibles.push(n);
  }
  cibles.forEach(function(t){
    t.nodeValue = t.nodeValue.replace(/Chapitres\s+([0-9]+(?:\s*,\s*[0-9]+)*)/g, function(tout, liste){
      var parts = liste.split(/\s*,\s*/).map(function(v){
        return v === '21' ? '2\u1D49 ann\u00e9e ch.1' : v;
      });
      return 'Chapitres ' + parts.join(', ');
    });
  });
}

function appliquer(){
  if(occupe) return;
  occupe = true;
  try{ poserCases(); poserBoutons(); relibellerResume(); }catch(e){}
  occupe = false;
}

/* La page Quiz est re-rendue par renderAdvancedSelector (fonction lexicale,
   non enveloppable) : on observe le conteneur pour reinjecter a chaque rendu. */
function observer(){
  var cible = document.getElementById('pg-quiz');
  if(!cible) return;
  try{
    new MutationObserver(function(){ appliquer(); })
      .observe(cible, {childList:true, subtree:true});
  }catch(e){}
}

function boot(){ appliquer(); observer(); }
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
setTimeout(boot, 800);
setTimeout(appliquer, 2200);

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    if(pg === 'quiz'){ setTimeout(appliquer, 30); setTimeout(appliquer, 260); }
    return r;
  };
}
})();
</script>
"""
open('quizchaps_patch.html','w',encoding='utf-8').write(js)
src = open('app_v179.html', encoding='utf-8').read()
i = src.rfind('</body>')
assert i > 0
open('app_v180.html','w',encoding='utf-8').write(src[:i] + js + src[i:])
print('patch :', len(js), 'caracteres | app_v180.html :', f"{len(src)+len(js):,}".replace(',',' '))
