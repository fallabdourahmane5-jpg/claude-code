#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Intègre le chapitre 4 de deuxième année (clé 24) dans ÉcoSphère.

Couches ajoutées :
  * eco-chapitre-24      : cours, notions et fiches, quiz, cartes, auteurs, sujets
  * eco-ch24-correctifs  : tags du quiz, onglet et carte du chapitre dans Sujets
  * eco-cours-cartes-a2  : cartes manquantes de la grille « Cours » pour les
                           chapitres 2, 3 et 4 de deuxième année

Retouches de source :
  * libellés « 24 » -> « 2ᵉ année ch.4 » dans les fonctions concernées
  * recalcul du compteur des cartes de la section Sujets pour le chapitre 24
  * items de la frise chronologique (nouveaux + chapitre ajouté aux existants)
"""
import io
import json
import re

import cours_ch4
import don24_auteurs
import don24_enrich
import don24_frise
import don24_maps
import don24_notions
import don24_quiz
import don24_suj1
import don24_suj2
import don24_suj3

SRC = 'app_v205_atlas.html'
DST = 'app_v205.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-chapitre-24' not in s

N = 24

# ----------------------------------------------------------------- données
SUJETS = don24_suj1.S1 + don24_suj2.S2 + don24_suj3.S3
for i, su in enumerate(SUJETS, 1):
    su['id'] = 'ch24-%d' % i
    su['num'] = i
    su['chapter'] = N

D = {
    'title': 'Régionalisation, gouvernance et régulations internationales',
    'sub': 'Doux commerce et interdépendances asymétriques · biens publics mondiaux '
           'et stabilité hégémonique · GATT, OMC et cycles de négociation · création '
           'et détournement de trafic · intégration profonde et bol de spaghettis · '
           'trilemme de Rodrik, capitalisme de la finitude et mondialisation fragmentée.',
    'cours': cours_ch4.construire(),
    'notions': [{'term': t, 'def': d, 'type': 'definition'}
                for (t, d) in don24_notions.NOTIONS],
    'methode': don24_maps.METHODE,
    'quiz': don24_quiz.QUIZ,
    'subjects': SUJETS,
    'auteurs': don24_auteurs.AUTEURS,
    'map': don24_maps.MAP,
    'vmap': don24_maps.VMAP,
    'enrich': don24_enrich.ENRICH,
    'args': don24_enrich.ARGS,
    # fiches déjà présentes auxquelles le chapitre 4 doit être rattaché : le
    # chapitre cite le modèle HOS, dont les trois auteurs ont leur propre fiche.
    'ajout': ['Eli Heckscher', 'Bertil Ohlin', 'Paul Samuelson'],
}

# ------------------------------------------------------- contrôles de forme
assert len(D['cours']) > 200000, len(D['cours'])
assert len(D['notions']) > 100, len(D['notions'])
assert len(D['quiz']) > 130, len(D['quiz'])
assert len(D['subjects']) == 14, len(D['subjects'])
assert len(D['auteurs']) > 20, len(D['auteurs'])
for su in D['subjects']:
    assert len(su['plan']) >= 30, (su['id'], len(su['plan']))
for terme in ['GATT', 'Seattle', 'arachide', 'multifibres', 'Cairns',
              'O’Rourke', 'nation la plus favorisée']:
    assert terme in D['cours'], 'absent du cours : ' + terme

# =============================================================== couche 1
SCRIPT1 = r"""
<script id="eco-chapitre-24">
/* =====================================================================
   ÉcoSphère Pro — Deuxième année, chapitre 4 (v205)
   Régionalisation, gouvernance et régulations internationales.
   Couche purement additive : cours, notions et fiches, quiz, cartes,
   auteurs, sujets et compléments aux sujets des autres chapitres.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_CH24) return;
window.__ECO_CH24 = true;

var D = __PAYLOAD__;
var N = 24;
var LIB = 'Deuxième année — Chapitre 4';
var bilan = {fiches:0, quiz:0, sujets:0, args:0, auteurs:0, mobiliser:0};

function norm(s){ return String(s == null ? '' : s).toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim(); }

/* ------------------------------------------------------------ 1. cours */
function poserCours(){
  if(typeof CH_CONTENT === 'undefined' || CH_CONTENT[N]) return;
  CH_CONTENT[N] = {title:D.title, sub:D.sub, cours:D.cours, notions:D.notions,
                   methode:D.methode, annee:2, numAnnee:4};
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
    FC_DATA.push({term:String(term), def:String(def), type:type, ch:N, eco24:1});
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
                id:q.id, source:'chapitre24', tags:['deuxième année','chapitre 24']});
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
      /* certaines fiches ne portent qu'un « ch » unique : on le conserve */
      ex.chapters = [].concat(ex.chapters || (ex.ch != null ? [ex.ch] : []));
      if(ex.chapters.map(String).indexOf(String(N)) < 0){ ex.chapters.push(N); bilan.auteurs++; }
      /* une œuvre citée par le chapitre 4 et absente de la fiche est ajoutée */
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
  /* fiches existantes que le chapitre 4 mobilise sans les redéfinir */
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
  /* « Chapitres à mobiliser » des autres chapitres */
  S.forEach(function(x){
    var add = D.enrich[x.id];
    if(!add) return;
    var base = String(x.mobiliser || '').trim();
    if(base.indexOf('2ᵉ année ch. 4') >= 0) return;
    x.mobiliser = base ? (base + ' · ' + add) : add;
    bilan.mobiliser++;
  });
  /* arguments ajoutés aux corrigés concernés */
  var parId = {};
  S.forEach(function(x){ if(x && x.id) parId[x.id] = x; });
  D.args.forEach(function(ins, idx){
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
    suj.__ch24 = (suj.__ch24 || 0) + ajouts.length;
    bilan.args += ajouts.length;
  });
  return true;
}

/* ------------------------------------- 7. « Chapitre 24 » -> libellé lisible */
var occupe = false;
function relibeller(racine){
  if(occupe || !racine) return;
  occupe = true;
  try{
    var it = document.createTreeWalker(racine, NodeFilter.SHOW_TEXT, null), n, cibles = [];
    while((n = it.nextNode())){
      if(/chapitre\s*24(?![0-9])/i.test(n.nodeValue) || /\bCH\.?\s*24(?![0-9])/i.test(n.nodeValue)) cibles.push(n);
    }
    cibles.forEach(function(t){
      t.nodeValue = t.nodeValue
        .replace(/CHAPITRE\s*24(?![0-9])/g, 'DEUXIÈME ANNÉE — CHAPITRE 4')
        .replace(/Chapitre\s*24(?![0-9])/g, LIB)
        .replace(/chapitre\s*24(?![0-9])/g, 'deuxième année — chapitre 4')
        .replace(/\bCH\.?\s*24(?![0-9])/g, '2ᵉ ANNÉE · CH.4')
        .replace(/\bCh\.?\s*24(?![0-9])/g, '2ᵉ année ch.4')
        .replace(/\bch\.?\s*24(?![0-9])/g, '2ᵉ année ch.4');
    });
  }catch(e){}
  occupe = false;
}

function tout(){
  try{
    poserCours(); poserFiches(); poserQuiz(); poserCartes(); poserAuteurs(); poserSujets();
    if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex();
  }catch(e){ try{ console.warn('[ch24]', e); }catch(_){} }
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
    new MutationObserver(window.__ecoGroupe ? window.__ecoGroupe(id + '-24', cb) : cb).observe(el, {childList:true, subtree:true});
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

window.__ECO_CH24_BILAN = bilan;
setTimeout(function(){
  console.log('[ÉcoSphère v205] 2e année ch.4 — ' + bilan.fiches + ' fiches, ' + bilan.quiz
    + ' questions, ' + bilan.auteurs + ' auteurs, ' + bilan.mobiliser + ' rubriques « mobiliser », '
    + bilan.args + ' arguments ajoutés aux corrigés');
}, 7000);
})();
</script>
"""

# =============================================================== couche 2
SCRIPT2 = r"""
<script id="eco-ch24-correctifs">
(function(){
'use strict';
if(window.__ECO_CH24_FIX) return;
window.__ECO_CH24_FIX = true;

var TAGS = __TAGS__;
var N = 24;

/* --- 1. tags thématiques des questions du chapitre 24 -------------------- */
function poserTags(){
  var A = window.__ECO_ADV_ALL_BANK;
  if(!A) return false;
  var n = 0;
  A.forEach(function(q){
    if(Number(q.ch) !== N) return;
    var t = TAGS[q.id];
    if(!t) return;
    var voulu = ['deuxième année', 'chapitre 24'].concat(t);
    if((q.tags || []).length === voulu.length) return;
    q.tags = voulu;
    n++;
  });
  return n > 0;
}

/* --- 2. onglet et carte du chapitre 24 dans la section Sujets ------------ */
function nbSujets(){
  try{
    return (SUBJECTS_BANK_PREMIUM || []).filter(function(s){ return Number(s.chapter) === N; }).length;
  }catch(e){ return 0; }
}
function poserSujets(){
  var n = nbSujets();
  if(!n) return;
  var tabs = document.getElementById('subjTabsPremium');
  if(tabs && !tabs.querySelector('[data-ch24]')){
    tabs.insertAdjacentHTML('beforeend',
      '<button class="subj-tab" data-ch24="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '2ᵉ année — Ch. 4</button>');
  }
  var grid = document.getElementById('subjChaptersPremium');
  if(grid && grid.children.length && !grid.querySelector('[data-ch24]')){
    grid.insertAdjacentHTML('beforeend',
      '<div class="subj-ch-card" data-ch24="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '<div class="subj-ch-num">2ᵉ année — Chapitre 4</div>' +
      '<div class="subj-ch-title">Sujets corrigés</div>' +
      '<div class="subj-ch-count">' + n + ' dissertations corrigées</div></div>');
  }
  try{
    var b = tabs && tabs.querySelector('[data-ch24]');
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

# =============================================================== couche 3
SCRIPT3 = r"""
<script id="eco-cours-cartes-a2">
/* La grille de la section « Cours » ne recevait une carte que pour le premier
   chapitre de deuxième année : les chapitres 2, 3 et 4 n'étaient accessibles
   que par la recherche ou par les autres sections. On ajoute les cartes
   manquantes, en reprenant le titre et le descriptif de CH_CONTENT afin de ne
   jamais réécrire le contenu du chapitre. */
(function(){
'use strict';
if(window.__ECO_CG_A2) return;
window.__ECO_CG_A2 = true;

var CFG = [
  {k:22, num:'02', tags:['FMN', 'IDE', 'Politique industrielle']},
  {k:23, num:'03', tags:['Avantage comparatif', 'Protectionnisme', 'Politique commerciale']},
  {k:24, num:'04', tags:['OMC', 'Régionalisation', 'Gouvernance mondiale']}
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
  /* les cartes de deuxième année restent groupées à la fin de la grille */
  try{
    [21, 22, 23, 24].forEach(function(k){
      var el = grid.querySelector('[data-c="' + k + '"]');
      if(el) grid.appendChild(el);
    });
  }catch(e){}
}

/* Le bandeau du quiz annonce « Chapitres 24 » : le numéro interne restait
   visible pour tous les chapitres de deuxième année, le relibellage ne portant
   que sur « Chapitre » au singulier. On corrige les quatre d'un coup. */
function libellesQuiz(){
  var zone = document.getElementById('pg-quiz');
  if(!zone) return;
  try{
    var it = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT, null), n, cibles = [];
    while((n = it.nextNode())){
      if(/Chapitres\s/.test(n.nodeValue) && /\b(21|22|23|24)\b/.test(n.nodeValue)) cibles.push(n);
    }
    cibles.forEach(function(t){
      t.nodeValue = t.nodeValue.replace(/\b(21|22|23|24)\b/g, function(m){
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
  if(zq) new MutationObserver(window.__ecoGroupe ? window.__ecoGroupe('pg-quiz-a2', libellesQuiz) : libellesQuiz)
    .observe(zq, {childList:true, subtree:true});
}catch(e){}
})();
</script>
"""

# ================================================= retouches de source
remp = 0


def remplacer(old, new):
    global s, remp
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)
    remp += 1


# (a) relibellerResume : libellé court des chapitres de deuxième année
remplacer(
    "(v === '23' ? '2\\u1D49 ann\\u00e9e ch.3' : v));",
    "(v === '23' ? '2\\u1D49 ann\\u00e9e ch.3' : (v === '24' ? '2\\u1D49 ann\\u00e9e ch.4' : v)));")

# (b) « Qui suis-je ? » : libelleCh
remplacer(
    "  if(String(n) === '23') return 'Deuxième année — Chapitre 3';\n  return 'Chapitre ' + n;",
    "  if(String(n) === '23') return 'Deuxième année — Chapitre 3';\n"
    "  if(String(n) === '24') return 'Deuxième année — Chapitre 4';\n  return 'Chapitre ' + n;")

# (c) frise : chLabel
remplacer(
    "  if(String(n) === '23') return '2ᵉ année — ch.3';\n  return 'Ch. ' + n;",
    "  if(String(n) === '23') return '2ᵉ année — ch.3';\n"
    "  if(String(n) === '24') return '2ᵉ année — ch.4';\n  return 'Ch. ' + n;")

# (d) frise : optionsCh
remplacer(
    "String(c) === '23' ? 'Deuxième année — Chapitre 3' : 'Chapitre ' + c",
    "String(c) === '23' ? 'Deuxième année — Chapitre 3' : "
    "String(c) === '24' ? 'Deuxième année — Chapitre 4' : 'Chapitre ' + c")

# (e) page Quiz : liste de sélection des chapitres
remplacer(
    "  {n:23, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.3', "
    "lab:'Analyse \\u00e9conomique du commerce international'}\n];",
    "  {n:23, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.3', "
    "lab:'Analyse \\u00e9conomique du commerce international'},\n"
    "  {n:24, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.4', "
    "lab:'R\\u00e9gionalisation, gouvernance et r\\u00e9gulations internationales'}\n];")

# (f) page Quiz : libellé des cases à cocher
remplacer(
    "          : c.n === 23 ? '2ᵉ année — Ch.3' : 'Ch.' + c.n;",
    "          : c.n === 23 ? '2ᵉ année — Ch.3' : c.n === 24 ? '2ᵉ année — Ch.4' : 'Ch.' + c.n;")

# (g) page Fiches : puces de filtre des chapitres
remplacer(
    "[22,'2ᵉ année — Ch.2'],[23,'2ᵉ année — Ch.3']];",
    "[22,'2ᵉ année — Ch.2'],[23,'2ᵉ année — Ch.3'],[24,'2ᵉ année — Ch.4']];")

# (h) Sujets : recalcul du compteur des cartes de chapitre
remplacer(
    "    [[23, '[data-ch23]'], [22, '[data-ch22]']].forEach(function(p){",
    "    [[24, '[data-ch24]'], [23, '[data-ch23]'], [22, '[data-ch22]']].forEach(function(p){")

# (i) fiche auteur « Orain » : prénom manquant et titre d'ouvrage incomplet.
# Sans cette correction, le chapitre 4 créerait une seconde fiche « Arnaud Orain »
# au lieu de compléter celle du chapitre 1.
remplacer(
    '{name:"Orain",dates:"Contemporain",courant:"Capitalisme contemporain",'
    'idea:"Le capitalisme est entré dans une phase de finitude",'
    'oeuvres:["Dans le monde confisqué"]',
    '{name:"Arnaud Orain",dates:"Contemporain",courant:"Capitalisme contemporain",'
    'idea:"Le capitalisme est entré dans une phase de finitude",'
    'oeuvres:["Le Monde confisqué. Essai sur le capitalisme de la finitude '
    '(XVIe-XXIe siècle) (2025)"]')

# ------------------------------------------------- frise : items ch24
m = re.search(r'var ITEMS = (\[.*?\]);', s, re.S)
assert m, 'tableau ITEMS de la frise introuvable'
ITEMS = json.loads(m.group(1))
par_id = {x['id']: x for x in ITEMS}
maj = 0
for idn in don24_frise.MAJ:
    x = par_id.get(idn)
    assert x is not None, 'item de frise absent : ' + idn
    ch = [int(c) for c in (x.get('ch') or [])]
    if N not in ch:
        ch.append(N)
        x['ch'] = sorted(ch)
        maj += 1
avant = len(ITEMS)
existants = set(par_id)
FAMILLES = {x['fam'] for x in ITEMS}
TYPES = {x['type'] for x in ITEMS}
for x in don24_frise.NOUVEAUX:
    assert x['id'] not in existants, x['id']
    assert x['fam'] in FAMILLES, (x['id'], x['fam'])
    assert x['type'] in TYPES, (x['id'], x['type'])
    assert x['ch'] == [N], (x['id'], x['ch'])
    ITEMS.append(x)
ITEMS.sort(key=lambda x: (x['an'], x['type'], x['titre']))
s = s[:m.start(1)] + json.dumps(ITEMS, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
print('  frise : %d items -> %d (%d mis à jour)' % (avant, len(ITEMS), maj))

# ------------------------------------------------- assemblage des couches
SCRIPT1 = SCRIPT1.replace('__PAYLOAD__', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
SCRIPT2 = SCRIPT2.replace('__TAGS__', json.dumps(don24_quiz.TAGS, ensure_ascii=False, separators=(',', ':')))

s = (s.rstrip() + '\n' + SCRIPT1.strip() + '\n\n' + SCRIPT2.strip()
     + '\n\n' + SCRIPT3.strip() + '\n')
io.open(DST, 'w', encoding='utf-8').write(s)
print('  retouches de libellés : %d' % remp)
print('  cours : %d caractères, %d notions, %d questions, %d sujets, %d auteurs'
      % (len(D['cours']), len(D['notions']), len(D['quiz']),
         len(D['subjects']), len(D['auteurs'])))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
