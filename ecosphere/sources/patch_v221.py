# -*- coding: utf-8 -*-
"""Integration des chapitres 5 et 6 de deuxieme annee (cles 25 et 26).

Couches ajoutees, strictement additives :
  1. eco-chapitre-25 / eco-chapitre-26 : cours, notions et fiches, quiz,
     cartes, auteurs, sujets, complements aux sujets des autres chapitres.
  2. eco-ch25-correctifs / eco-ch26-correctifs : tags des questions, onglet
     et carte dans la section Sujets.
  3. eco-cours-cartes-a2b : cartes des chapitres 5 et 6 dans la grille Cours.

Retouches de source : libelles des chapitres 25 et 26 partout ou les
chapitres de deuxieme annee sont nommes, et items de la frise.
"""

import io
import json
import re

import don25_auteurs
import don25_frise
import don25_maps
import don25_notions
import don25_quiz
import don25_suj1
import don25_suj2
import don25_suj3
import don26_auteurs
import don26_frise
import don26_maps
import don26_notions
import don26_quiz
import don26_suj1
import don26_suj2
import don26_suj3
import don2526_enrich

SRC = 'app_in.html'
DST = 'app_v221.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-chapitre-25' not in s
assert 'eco-chapitre-26' not in s

# ----------------------------------------------------------------- données
S25 = don25_suj1.S1 + don25_suj2.S2 + don25_suj3.S3
for i, su in enumerate(S25, 1):
    su['id'], su['num'], su['chapter'] = 'ch25-%d' % i, i, 25
S26 = don26_suj1.S1 + don26_suj2.S2 + don26_suj3.S3
for i, su in enumerate(S26, 1):
    su['id'], su['num'], su['chapter'] = 'ch26-%d' % i, i, 26

COURS25 = io.open('cours_ch25.html', encoding='utf-8').read()
COURS26 = io.open('cours_ch26.html', encoding='utf-8').read()

# L'enrichissement des sujets existants est unique : il est porte par la
# couche du chapitre 25, qui le pose une seule fois.
D25 = {
    'title': 'L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG',
    'sub': 'Demande effective et équilibre de sous-emploi · multiplicateur et '
           'fuites · préférence pour la liquidité et courbe LM · effet '
           'd’éviction et trappe à liquidité · critiques monétaristes et modèle '
           'OG-DG · policy mix · courbe BP, Mundell-Fleming et triangle des '
           'incompatibilités · dilemmes interne-externe.',
    'cours': COURS25,
    'notions': [{'term': t, 'def': d, 'type': 'definition'}
                for (t, d) in don25_notions.NOTIONS],
    'methode': don25_maps.METHODE,
    'quiz': don25_quiz.QUIZ,
    'subjects': S25,
    'auteurs': don25_auteurs.AUTEURS,
    'map': don25_maps.MAP,
    'vmap': don25_maps.VMAP,
    'enrich': don2526_enrich.ENRICH,
    'args': don2526_enrich.ARGS,
    'ajout': [],
}

D26 = {
    'title': 'Taux de change et systèmes de change',
    'sub': 'Monnaie, devise et mesure du change · marché des changes et '
           'financiarisation · parité des pouvoirs d’achat et effet '
           'Balassa-Samuelson · typologie des régimes et peur du flottement · '
           'triangle de Mundell et histoire du SMI · politique de change · '
           'dévaluation compétitive, Marshall-Lerner et courbe en J · '
           'désinflation compétitive et théorème de Schmidt.',
    'cours': COURS26,
    'notions': [{'term': t, 'def': d, 'type': 'definition'}
                for (t, d) in don26_notions.NOTIONS],
    'methode': don26_maps.METHODE,
    'quiz': don26_quiz.QUIZ,
    'subjects': S26,
    'auteurs': don26_auteurs.AUTEURS,
    'map': don26_maps.MAP,
    'vmap': don26_maps.VMAP,
    'enrich': {},
    'args': [],
    'ajout': [],
}

# ------------------------------------------------------- contrôles de forme
for D, n, mini in ((D25, 25, 300000), (D26, 26, 230000)):
    assert len(D['cours']) > mini, (n, len(D['cours']))
    assert len(D['notions']) > 90, (n, len(D['notions']))
    assert len(D['quiz']) > 90, (n, len(D['quiz']))
    assert len(D['subjects']) == 14, (n, len(D['subjects']))
    assert len(D['auteurs']) >= 14, (n, len(D['auteurs']))
    for su in D['subjects']:
        assert len(su['plan']) >= 30, (su['id'], len(su['plan']))
    assert D['map'] and D['vmap'] and D['methode']

for terme in ['multiplicateur', 'demande effective', 'trappe à liquidité',
              'effet d’éviction', 'Mundell', 'policy mix', 'Bourguinat',
              'OG-DG', 'Phillips', 'Okun']:
    assert terme in D25['cours'], 'absent du cours 25 : ' + terme
for terme in ['Cassel', 'Balassa', 'Marshall', 'courbe en J', 'Plaza',
              'Louvre', 'Volcker', 'Schmidt', 'Miran', 'franc fort']:
    assert terme in D26['cours'], 'absent du cours 26 : ' + terme

# ================================================================ couche 1
SCRIPT1 = r"""
<script id="eco-chapitre-__N__">
/* =====================================================================
   ÉcoSphère Pro — Deuxième année, chapitre __NUM__ (v221)
   Couche purement additive : cours, notions et fiches, quiz, cartes,
   auteurs, sujets et compléments aux sujets des autres chapitres.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_CH__N__) return;
window.__ECO_CH__N__ = true;

var D = __PAYLOAD__;
var N = __N__;
var LIB = 'Deuxième année — Chapitre __NUM__';
var bilan = {fiches:0, quiz:0, sujets:0, args:0, auteurs:0, mobiliser:0};

function norm(s){ return String(s == null ? '' : s).toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim(); }

/* ------------------------------------------------------------ 1. cours */
function poserCours(){
  if(typeof CH_CONTENT === 'undefined' || CH_CONTENT[N]) return;
  CH_CONTENT[N] = {title:D.title, sub:D.sub, cours:D.cours, notions:D.notions,
                   methode:D.methode, annee:2, numAnnee:__NUM__};
}

/* ----------------------------------------------------------- 2. fiches */
function poserFiches(){
  if(typeof FC_DATA === 'undefined') return;
  var vus = {};
  FC_DATA.forEach(function(c){ vus[norm(c.term)+'|'+c.ch+'|'+c.type] = 1; });
  function add(type, term, def){
    if(!term || !def) return;
    var k = norm(term)+'|'+N+'|'+type;
    if(vus[k]) return;
    vus[k] = 1;
    FC_DATA.push({term:String(term), def:String(def), type:type, ch:N, eco2526:1});
    bilan.fiches++;
  }
  D.notions.forEach(function(n){
    add('definition', n.term, n.def);
    add('definition-révision', 'Que faut-il retenir de ' + n.term + ' ?', n.def);
    add('identification', 'Quel concept correspond à cette définition : ' + n.def.slice(0,110), n.term);
    add('notion-clé', n.term, n.def);
    add('définition', 'Définis : ' + n.term, n.def);
  });
  D.auteurs.forEach(function(a){
    var oe = [].concat(a.oeuvres || []).filter(Boolean);
    var ref = oe.length ? ' — ' + oe[0] : (a.dates ? ' (' + a.dates + ')' : '');
    add('auteur', a.name, a.detail || a.idea);
    add('auteur-révision', 'Que faut-il retenir de ' + a.name + ' ?', a.detail);
    if(a.idea) add('auteur-idée', 'Quel auteur associer à l’idée suivante : ' + a.idea,
      a.name + (a.dates ? ' (' + a.dates + ')' : '') + (a.courant ? ' — ' + a.courant : ''));
    if(a.courant) add('courant', a.name + ' — courant de pensée',
      a.name + ' appartient au courant ' + a.courant + '.' + (a.idea ? ' ' + a.idea : ''));
    if(a.phrase) add('mobilisation-auteur', 'Comment mobiliser ' + a.name + ' dans une copie ?', a.phrase);
    if(oe.length) add('ouvrage', a.name + ' — ouvrage(s) à retenir', oe.join(' · '));
    if(a.detail){
      add('auteur-repère', 'Quel auteur ou quelle référence associer à cette idée : ' + a.detail.slice(0,110), a.name + ref);
      add('mobilisation', 'Quelle idée de cours mobiliser à partir de ' + a.name + ref + ' ?', a.detail);
    }
  });
}

/* ------------------------------------------------------------- 3. quiz */
function poserQuiz(){
  try{
    if(window.ECOSPHERE_QUESTION_BANK && !window.ECOSPHERE_QUESTION_BANK[N]){
      window.ECOSPHERE_QUESTION_BANK[N] = D.quiz.map(function(q){ return Object.assign({}, q); });
    }
  }catch(e){}
  try{
    var A = window.__ECO_ADV_ALL_BANK;
    if(A && !A.some(function(q){ return Number(q.ch) === N; })){
      D.quiz.forEach(function(q){
        A.push({type:q.type, q:q.q, opts:q.opts, ans:q.ans, exp:q.exp, ch:N,
                id:q.id, source:'chapitre__N__', tags:['deuxième année','chapitre __N__']});
        bilan.quiz++;
      });
    }
  }catch(e){}
}

/* ----------------------------------------------------------- 4. cartes */
function poserCartes(){
  try{ if(typeof MAP_DATA !== 'undefined' && !MAP_DATA[N]) MAP_DATA[N] = D.map; }catch(e){}
  try{ if(typeof VISUAL_MAPS_V83 !== 'undefined' && !VISUAL_MAPS_V83[N]) VISUAL_MAPS_V83[N] = D.vmap; }catch(e){}
}

/* ---------------------------------------------------------- 5. auteurs */
function poserAuteurs(){
  if(typeof AUTHORS === 'undefined') return;
  var vus = {}; AUTHORS.forEach(function(a){ vus[norm(a.name)] = a; });
  D.auteurs.forEach(function(a){
    var ex = vus[norm(a.name)];
    if(ex){
      ex.chapters = [].concat(ex.chapters || (ex.ch != null ? [ex.ch] : []));
      if(ex.chapters.map(String).indexOf(String(N)) < 0){ ex.chapters.push(N); bilan.auteurs++; }
      var oe = [].concat(a.oeuvres || []).filter(Boolean);
      if(oe.length){
        ex.oeuvres = [].concat(ex.oeuvres || []);
        oe.forEach(function(o){
          if(ex.oeuvres.map(norm).indexOf(norm(o)) < 0) ex.oeuvres.push(o);
        });
      }
      return;
    }
    var neuf = Object.assign({}, a);
    AUTHORS.push(neuf);
    vus[norm(a.name)] = neuf;
    bilan.auteurs++;
  });
  (D.ajout || []).forEach(function(nom){
    AUTHORS.forEach(function(a){
      if(norm(a.name) !== norm(nom)) return;
      a.chapters = [].concat(a.chapters || (a.ch != null ? [a.ch] : []));
      if(a.chapters.map(String).indexOf(String(N)) < 0){ a.chapters.push(N); bilan.auteurs++; }
    });
  });
}

/* ----------------------------------------------------------- 6. sujets */
var estPartie = function(t){ return /^\s*[IVX]+\.\s/.test(t); };
var estSousPartie = function(t){ return /^\s*[A-Z]\.\s/.test(t); };
var estArg = function(t){ return /^\s*\d+\)/.test(t); };
var argsFaits = {};

function poserSujets(){
  if(typeof SUBJECTS_BANK_PREMIUM === 'undefined') return false;
  var S = SUBJECTS_BANK_PREMIUM;
  if(!S.some(function(x){ return String(x.chapter) === String(N); })){
    D.subjects.forEach(function(x){ S.push(Object.assign({}, x)); bilan.sujets++; });
  }
  S.forEach(function(x){
    var add = D.enrich[x.id];
    if(!add) return;
    var base = String(x.mobiliser || '').trim();
    if(base.indexOf('2ᵉ année ch. 5') >= 0 || base.indexOf('2ᵉ année ch. 6') >= 0) return;
    x.mobiliser = base ? (base + ' · ' + add) : add;
    bilan.mobiliser++;
  });
  var parId = {};
  S.forEach(function(x){ if(x && x.id) parId[x.id] = x; });
  (D.args || []).forEach(function(ins, idx){
    if(argsFaits[idx]) return;
    var suj = parId[ins.id];
    if(!suj || !Array.isArray(suj.plan) || !suj.plan.length) return;
    var vu = 0, debut = -1, fin = suj.plan.length, i;
    for(i = 0; i < suj.plan.length; i++){
      if(estPartie(String(suj.plan[i]))){
        vu++;
        if(vu === ins.part) debut = i;
        else if(vu === ins.part + 1){ fin = i; break; }
      }
    }
    if(debut < 0){
      for(var k = suj.plan.length - 1; k >= 0; k--){
        if(estPartie(String(suj.plan[k]))){ debut = k; fin = suj.plan.length; break; }
      }
    }
    if(debut < 0){ debut = 0; fin = suj.plan.length; }
    var num = 0;
    for(var j = fin - 1; j > debut; j--){
      if(estSousPartie(String(suj.plan[j]))) break;
      if(estArg(String(suj.plan[j]))) num++;
    }
    var ajouts = ins.args.map(function(txt, q){ return (num + q + 1) + ') ' + txt; });
    ajouts = ajouts.filter(function(a){
      var corps = norm(a.replace(/^\s*\d+\)\s*/, '')).slice(0, 70);
      return corps && !suj.plan.some(function(pl){ return norm(pl).indexOf(corps) >= 0; });
    });
    argsFaits[idx] = 1;
    if(!ajouts.length) return;
    suj.plan = suj.plan.slice(0, fin).concat(ajouts, suj.plan.slice(fin));
    bilan.args += ajouts.length;
  });
  return true;
}

/* ----------------------------------- 7. « Chapitre __N__ » -> libellé lisible */
var occupe = false;
function relibeller(racine){
  if(occupe || !racine) return;
  occupe = true;
  try{
    var it = document.createTreeWalker(racine, NodeFilter.SHOW_TEXT, null), n, cibles = [];
    while((n = it.nextNode())){
      if(/chapitre\s*__N__(?![0-9])/i.test(n.nodeValue) || /\bCH\.?\s*__N__(?![0-9])/i.test(n.nodeValue)) cibles.push(n);
    }
    cibles.forEach(function(t){
      t.nodeValue = t.nodeValue
        .replace(/CHAPITRE\s*__N__(?![0-9])/g, 'DEUXIÈME ANNÉE — CHAPITRE __NUM__')
        .replace(/Chapitre\s*__N__(?![0-9])/g, LIB)
        .replace(/chapitre\s*__N__(?![0-9])/g, 'deuxième année — chapitre __NUM__')
        .replace(/\bCH\.?\s*__N__(?![0-9])/g, '2ᵉ ANNÉE · CH.__NUM__')
        .replace(/\bCh\.?\s*__N__(?![0-9])/g, '2ᵉ année ch.__NUM__')
        .replace(/\bch\.?\s*__N__(?![0-9])/g, '2ᵉ année ch.__NUM__');
    });
  }catch(e){}
  occupe = false;
}

function tout(){
  try{
    poserCours(); poserFiches(); poserQuiz(); poserCartes(); poserAuteurs(); poserSujets();
    if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex();
  }catch(e){ try{ console.warn('[ch__N__]', e); }catch(_){} }
}
function fait(){ try{ return typeof CH_CONTENT !== 'undefined' && !!CH_CONTENT[N]; }catch(e){ return false; } }
function assurer(){ if(!fait()) tout(); else { try{ poserQuiz(); poserCartes(); poserSujets(); }catch(e){} } }

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tout);
else tout();
[400, 1200, 2600, 4200, 6500, 9000].forEach(function(t){ setTimeout(assurer, t); });

try{
  ['pg-chapter','pg-quiz','pg-search','pg-subjects','pg-maps','pg-fc','pg-authors','pg-frise','pg-home','pg-atlas']
   .forEach(function(id){
    var el = document.getElementById(id);
    if(!el) return;
    var cb = function(){ relibeller(el); };
    new MutationObserver(window.__ecoGroupe ? window.__ecoGroupe(id + '-__N__', cb) : cb).observe(el, {childList:true, subtree:true});
  });
}catch(e){}

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    assurer();
    var r = old.apply(this, arguments);
    if(pg === 'subjects'){
      try{ poserSujets(); }catch(e){}
      setTimeout(function(){ try{ poserSujets(); if(typeof renderSubjectsPremium === 'function') renderSubjectsPremium(); }catch(e){} }, 70);
    }
    setTimeout(function(){ relibeller(document.getElementById('pg-' + pg)); }, 40);
    setTimeout(function(){ relibeller(document.getElementById('pg-' + pg)); }, 280);
    return r;
  };
}
if(typeof window.openCh === 'function'){
  var oldC = window.openCh;
  window.openCh = function(n){
    assurer();
    var r = oldC.apply(this, arguments);
    setTimeout(function(){ relibeller(document.getElementById('pg-chapter')); }, 60);
    return r;
  };
}
setTimeout(function(){ relibeller(document.body); }, 3000);

window.__ECO_CH__N___BILAN = bilan;
setTimeout(function(){
  console.log('[ÉcoSphère v221] 2e année ch.__NUM__ — ' + bilan.fiches + ' fiches, ' + bilan.quiz
    + ' questions, ' + bilan.auteurs + ' auteurs, ' + bilan.mobiliser + ' rubriques « mobiliser », '
    + bilan.args + ' arguments ajoutés aux corrigés');
}, 7000);
})();
</script>
"""

# ================================================================ couche 2
SCRIPT2 = r"""
<script id="eco-ch__N__-correctifs">
(function(){
'use strict';
if(window.__ECO_CH__N___FIX) return;
window.__ECO_CH__N___FIX = true;

var TAGS = __TAGS__;
var N = __N__;

function poserTags(){
  var A = window.__ECO_ADV_ALL_BANK;
  if(!A) return false;
  var n = 0;
  A.forEach(function(q){
    if(Number(q.ch) !== N) return;
    var t = TAGS[q.id];
    if(!t) return;
    var voulu = ['deuxième année', 'chapitre __N__'].concat(t);
    if((q.tags || []).length === voulu.length) return;
    q.tags = voulu;
    n++;
  });
  return n > 0;
}

function nbSujets(){
  try{
    return (SUBJECTS_BANK_PREMIUM || []).filter(function(s){ return Number(s.chapter) === N; }).length;
  }catch(e){ return 0; }
}
function poserSujets(){
  var n = nbSujets();
  if(!n) return;
  var tabs = document.getElementById('subjTabsPremium');
  if(tabs && !tabs.querySelector('[data-ch__N__]')){
    tabs.insertAdjacentHTML('beforeend',
      '<button class="subj-tab" data-ch__N__="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '2ᵉ année — Ch. __NUM__</button>');
  }
  var grid = document.getElementById('subjChaptersPremium');
  if(grid && grid.children.length && !grid.querySelector('[data-ch__N__]')){
    grid.insertAdjacentHTML('beforeend',
      '<div class="subj-ch-card" data-ch__N__="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '<div class="subj-ch-num">2ᵉ année — Chapitre __NUM__</div>' +
      '<div class="subj-ch-title">Sujets corrigés</div>' +
      '<div class="subj-ch-count">' + n + ' dissertations corrigées</div></div>');
  }
  try{
    var b = tabs && tabs.querySelector('[data-ch__N__]');
    if(b) b.classList.toggle('on', window.currentSubjChapter === N);
  }catch(e){}
}

function tout(){ try{ poserTags(); poserSujets(); }catch(e){} }

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tout);
else tout();
[300, 900, 2000, 3500, 6000, 9500].forEach(function(t){ setTimeout(tout, t); });

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    if(pg === 'subjects' || pg === 'quiz'){ setTimeout(tout, 50); setTimeout(tout, 300); }
    return r;
  };
}
if(typeof window.setSubjectChapterPremium === 'function'){
  var oldS = window.setSubjectChapterPremium;
  window.setSubjectChapterPremium = function(){
    var r = oldS.apply(this, arguments);
    setTimeout(tout, 40);
    return r;
  };
}
try{
  var z = document.getElementById('pg-subjects');
  if(z) new MutationObserver(function(){ poserSujets(); }).observe(z, {childList:true, subtree:true});
}catch(e){}
})();
</script>
"""

# ================================================================ couche 3
SCRIPT3 = r"""
<script id="eco-cours-cartes-a2b">
/* La grille de la section « Cours » recevait les cartes des chapitres 2, 3 et 4
   de deuxième année. On ajoute celles des chapitres 5 et 6, en reprenant le
   titre et le descriptif de CH_CONTENT afin de ne jamais réécrire le contenu
   du chapitre, et on regroupe les six cartes de deuxième année à la fin. */
(function(){
'use strict';
if(window.__ECO_CG_A2B) return;
window.__ECO_CG_A2B = true;

var CFG = [
  {k:25, num:'05', tags:['IS-LM', 'Multiplicateur', 'Policy mix']},
  {k:26, num:'06', tags:['Taux de change', 'Régimes de change', 'Dévaluation']}
];

function esc(s){
  return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function poser(){
  var grid = document.querySelector('.cg');
  if(!grid || typeof CH_CONTENT === 'undefined') return;
  CFG.forEach(function(c){
    var v = CH_CONTENT[c.k];
    if(!v || grid.querySelector('[data-c="' + c.k + '"]')) return;
    var tags = '<span class="tag tag-a2">2ᵉ année</span>' +
      c.tags.map(function(t){ return '<span class="tag">' + esc(t) + '</span>'; }).join('');
    grid.insertAdjacentHTML('beforeend',
      '<div class="cc cc-annee2" data-c="' + c.k + '" onclick="openCh(' + c.k + ')">' +
      '<div class="cc-num">// DEUXIÈME ANNÉE · CHAPITRE ' + c.num + '</div>' +
      '<div class="cc-title">' + esc(v.title) + '</div>' +
      '<div class="cc-desc">' + esc(v.sub) + '</div>' +
      '<div class="cc-tags">' + tags + '</div>' +
      '<div class="cc-btns">' +
        '<button class="btn btn-p" onclick="event.stopPropagation();openCh(' + c.k + ')">📖 Cours</button>' +
        '<button class="btn btn-g" onclick="event.stopPropagation();startQuiz(' + c.k + ')">🎯 Quiz IA</button>' +
      '</div></div>');
  });
  try{
    [21, 22, 23, 24, 25, 26].forEach(function(k){
      var el = grid.querySelector('[data-c="' + k + '"]');
      if(el) grid.appendChild(el);
    });
  }catch(e){}
}

/* Le bandeau du quiz annonce les numéros internes : le relibellage existant ne
   couvrait que 21 à 24. On ajoute 25 et 26. */
function libellesQuiz(){
  var zone = document.getElementById('pg-quiz');
  if(!zone) return;
  try{
    var it = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT, null), n, cibles = [];
    while((n = it.nextNode())){
      if(/Chapitres\s/.test(n.nodeValue) && /\b(25|26)\b/.test(n.nodeValue)) cibles.push(n);
    }
    cibles.forEach(function(t){
      t.nodeValue = t.nodeValue.replace(/\b(25|26)\b/g, function(m){
        return '2ᵉ année ch.' + (Number(m) - 20);
      });
    });
  }catch(e){}
}

function tout(){ poser(); libellesQuiz(); }

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tout);
else tout();
[500, 1400, 2800, 4500, 7000, 9800].forEach(function(t){ setTimeout(tout, t); });

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    setTimeout(tout, 60);
    return r;
  };
}
try{
  var zq = document.getElementById('pg-quiz');
  if(zq) new MutationObserver(window.__ecoGroupe ? window.__ecoGroupe('pg-quiz-a2b', libellesQuiz) : libellesQuiz)
    .observe(zq, {childList:true, subtree:true});
}catch(e){}
})();
</script>
"""

# ===================================================== retouches de source
remp = 0


def remplacer(old, new):
    global s, remp
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)
    remp += 1


# (a) relibellerResume : libellé court
remplacer(
    "(v === '24' ? '2\\u1D49 ann\\u00e9e ch.4' : v)));",
    "(v === '24' ? '2\\u1D49 ann\\u00e9e ch.4' : "
    "(v === '25' ? '2\\u1D49 ann\\u00e9e ch.5' : "
    "(v === '26' ? '2\\u1D49 ann\\u00e9e ch.6' : v)))));")

# (b) « Qui suis-je ? » : libelleCh
remplacer(
    "  if(String(n) === '24') return 'Deuxième année — Chapitre 4';\n  return 'Chapitre ' + n;",
    "  if(String(n) === '24') return 'Deuxième année — Chapitre 4';\n"
    "  if(String(n) === '25') return 'Deuxième année — Chapitre 5';\n"
    "  if(String(n) === '26') return 'Deuxième année — Chapitre 6';\n  return 'Chapitre ' + n;")

# (c) frise : chLabel
remplacer(
    "  if(String(n) === '24') return '2ᵉ année — ch.4';\n  return 'Ch. ' + n;",
    "  if(String(n) === '24') return '2ᵉ année — ch.4';\n"
    "  if(String(n) === '25') return '2ᵉ année — ch.5';\n"
    "  if(String(n) === '26') return '2ᵉ année — ch.6';\n  return 'Ch. ' + n;")

# (d) frise : optionsCh
remplacer(
    "String(c) === '24' ? 'Deuxième année — Chapitre 4' : 'Chapitre ' + c",
    "String(c) === '24' ? 'Deuxième année — Chapitre 4' : "
    "String(c) === '25' ? 'Deuxième année — Chapitre 5' : "
    "String(c) === '26' ? 'Deuxième année — Chapitre 6' : 'Chapitre ' + c")

# (e) page Quiz : liste de sélection des chapitres
remplacer(
    "lab:'R\\u00e9gionalisation, gouvernance et r\\u00e9gulations internationales'}\n];",
    "lab:'R\\u00e9gionalisation, gouvernance et r\\u00e9gulations internationales'},\n"
    "  {n:25, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.5', "
    "lab:'\\u00c9quilibre macro\\u00e9conomique et politiques conjoncturelles'},\n"
    "  {n:26, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.6', "
    "lab:'Taux de change et syst\\u00e8mes de change'}\n];")

# (f) page Quiz : libellé des cases à cocher
remplacer(
    "c.n === 24 ? '2ᵉ année — Ch.4' : 'Ch.' + c.n;",
    "c.n === 24 ? '2ᵉ année — Ch.4' : c.n === 25 ? '2ᵉ année — Ch.5' "
    ": c.n === 26 ? '2ᵉ année — Ch.6' : 'Ch.' + c.n;")

# (g) page Fiches : puces de filtre des chapitres
remplacer(
    "[23,'2ᵉ année — Ch.3'],[24,'2ᵉ année — Ch.4']];",
    "[23,'2ᵉ année — Ch.3'],[24,'2ᵉ année — Ch.4'],"
    "[25,'2ᵉ année — Ch.5'],[26,'2ᵉ année — Ch.6']];")

# (h) Sujets : recalcul du compteur des cartes de chapitre
remplacer(
    "    [[24, '[data-ch24]'], [23, '[data-ch23]'], [22, '[data-ch22]']].forEach(function(p){",
    "    [[26, '[data-ch26]'], [25, '[data-ch25]'], [24, '[data-ch24]'], "
    "[23, '[data-ch23]'], [22, '[data-ch22]']].forEach(function(p){")

# ------------------------------------------------- frise : items 25 et 26
m = re.search(r'var ITEMS = (\[.*?\]);', s, re.S)
assert m, 'tableau ITEMS de la frise introuvable'
ITEMS = json.loads(m.group(1))
par_id = {x['id']: x for x in ITEMS}
FAMILLES = {x['fam'] for x in ITEMS}
TYPES = {x['type'] for x in ITEMS}
avant = len(ITEMS)
maj = 0
for N, mod in ((25, don25_frise), (26, don26_frise)):
    for idn, titre in mod.MAJ.items():
        x = par_id.get(idn)
        assert x is not None, 'item de frise absent : ' + idn
        assert x['titre'] == titre, (idn, x['titre'], titre)
        ch = [int(c) for c in (x.get('ch') or [])]
        if N not in ch:
            ch.append(N)
            x['ch'] = sorted(ch)
            maj += 1
    for x in mod.NOUVEAUX:
        assert x['id'] not in par_id, x['id']
        assert x['fam'] in FAMILLES, (x['id'], x['fam'])
        assert x['type'] in TYPES, (x['id'], x['type'])
        assert x['ch'] == [N], (x['id'], x['ch'])
        ITEMS.append(x)
        par_id[x['id']] = x
ITEMS.sort(key=lambda x: (x['an'], x['type'], x['titre']))
s = s[:m.start(1)] + json.dumps(ITEMS, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
print('  frise : %d items -> %d (%d mis à jour)' % (avant, len(ITEMS), maj))

# ----------------------------------------------- assemblage des couches
couches = []
for N, NUM, D, TAGS in ((25, 5, D25, don25_quiz.TAGS), (26, 6, D26, don26_quiz.TAGS)):
    c1 = (SCRIPT1
          .replace('__PAYLOAD__', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
          .replace('__NUM__', str(NUM)).replace('__N__', str(N)))
    c2 = (SCRIPT2
          .replace('__TAGS__', json.dumps(TAGS, ensure_ascii=False, separators=(',', ':')))
          .replace('__NUM__', str(NUM)).replace('__N__', str(N)))
    couches += [c1.strip(), c2.strip()]
couches.append(SCRIPT3.strip())

s = s.rstrip() + '\n' + '\n\n'.join(couches) + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('  retouches de libellés : %d' % remp)
for N, D in ((25, D25), (26, D26)):
    print('  ch.%d : cours %d car., %d notions, %d questions, %d sujets, %d auteurs'
          % (N, len(D['cours']), len(D['notions']), len(D['quiz']),
             len(D['subjects']), len(D['auteurs'])))
print('  sujets enrichis : %d · arguments ajoutés : %d'
      % (len(don2526_enrich.ENRICH), len(don2526_enrich.ARGS)))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
