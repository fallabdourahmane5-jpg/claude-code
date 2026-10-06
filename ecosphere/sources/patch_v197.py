#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integre le chapitre 3 de deuxieme annee (cle 23) dans ÉcoSphère.

Couches ajoutees :
  * eco-chapitre-23      : cours, notions et fiches, quiz, cartes, auteurs, sujets
  * eco-ch23-correctifs  : tags du quiz, onglet et carte du chapitre dans Sujets

Retouches de source :
  * libelles « 23 » -> « 2e annee ch.3 » dans les quatre fonctions concernees
  * items de la frise chronologique (nouveaux + chapitre ajoute aux existants)
"""
import io, json, re

import cours_ch3
import don23_notions, don23_auteurs, don23_quiz, don23_maps, don23_enrich
import don23_suj1, don23_suj2, don23_suj3
import don23_frise

SRC = 'app_v196.html'
DST = 'app_v197.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-chapitre-23' not in s

N = 23

# ----------------------------------------------------------------- donnees
SUJETS = don23_suj1.S1 + don23_suj2.S2 + don23_suj3.S3
for i, su in enumerate(SUJETS, 1):
    su['id'] = 'ch23-%d' % i
    su['num'] = i
    su['chapter'] = N

D = {
 'title': "L’analyse économique du commerce international",
 'sub': "Théories traditionnelles et contemporaines de l’échange · gains et perdants du libre-échange · "
        "instruments et évaluation des politiques commerciales · retour du protectionnisme et fragmentation géo-économique.",
 'cours': cours_ch3.construire(),
 'notions': [{'term': t, 'def': d, 'type': 'definition'} for (t, d) in don23_notions.NOTIONS],
 'methode': don23_maps.METHODE,
 'quiz': don23_quiz.QUIZ,
 'subjects': SUJETS,
 'auteurs': don23_auteurs.AUTEURS,
 'map': don23_maps.MAP,
 'vmap': don23_maps.VMAP,
 'enrich': don23_enrich.ENRICH,
 'args': don23_enrich.ARGS,
}

# ------------------------------------------------------- controles de forme
assert len(D['cours']) > 200000, len(D['cours'])
assert len(D['notions']) > 100
assert len(D['quiz']) > 80
assert len(D['subjects']) == 14
assert len(D['auteurs']) > 40
for su in D['subjects']:
    assert len(su['plan']) >= 30

# =============================================================== couche 1
SCRIPT1 = r"""
<script id="eco-chapitre-23">
/* =====================================================================
   ÉcoSphère Pro — Deuxième année, chapitre 3 (v197)
   L'analyse économique du commerce international.
   Couche purement additive : cours, notions et fiches, quiz, cartes,
   auteurs, sujets et compléments aux sujets des autres chapitres.
   ===================================================================== */
(function(){
'use strict';
if(window.__ECO_CH23) return;
window.__ECO_CH23 = true;

var D = __PAYLOAD__;
var N = 23;
var LIB = 'Deuxième année — Chapitre 3';
var bilan = {fiches:0, quiz:0, sujets:0, args:0, auteurs:0, mobiliser:0};

function norm(s){ return String(s == null ? '' : s).toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim(); }

/* ------------------------------------------------------------ 1. cours */
function poserCours(){
  if(typeof CH_CONTENT === 'undefined' || CH_CONTENT[N]) return;
  CH_CONTENT[N] = {title:D.title, sub:D.sub, cours:D.cours, notions:D.notions,
                   methode:D.methode, annee:2, numAnnee:3};
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
    FC_DATA.push({term:String(term), def:String(def), type:type, ch:N, eco23:1});
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
                id:q.id, source:'chapitre23', tags:['deuxième année','chapitre 23']});
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
      ex.chapters = [].concat(ex.chapters || []);
      if(ex.chapters.map(String).indexOf(String(N)) < 0){ ex.chapters.push(N); bilan.auteurs++; }
      return;
    }
    var neuf = Object.assign({}, a);
    AUTHORS.push(neuf);
    vus[norm(a.name)] = neuf;
    bilan.auteurs++;
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
    D.subjects.forEach(function(x){ S.push(Object.assign({}, x)); });
  }
  /* « Chapitres a mobiliser » des autres chapitres */
  S.forEach(function(x){
    var add = D.enrich[x.id];
    if(!add) return;
    var base = String(x.mobiliser || '').trim();
    if(base.indexOf('2ᵉ année ch. 3') >= 0) return;
    x.mobiliser = base ? (base + ' · ' + add) : add;
    bilan.mobiliser++;
  });
  /* arguments ajoutes aux corriges concernes */
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
    var ajouts = ins.args.map(function(txt, q){ return (num + q + 1) + ') ' + txt; });
    ajouts = ajouts.filter(function(a){
      var corps = norm(a.replace(/^\s*\d+\)\s*/, '')).slice(0, 70);
      return corps && !suj.plan.some(function(pl){ return norm(pl).indexOf(corps) >= 0; });
    });
    argsFaits[idx] = 1;
    if(!ajouts.length) return;
    suj.plan = suj.plan.slice(0, fin).concat(ajouts, suj.plan.slice(fin));
    suj.__ch23 = (suj.__ch23 || 0) + ajouts.length;
    bilan.args += ajouts.length;
  });
  return true;
}

/* ------------------------------------- 7. « Chapitre 23 » -> libelle lisible */
var occupe = false;
function relibeller(racine){
  if(occupe || !racine) return;
  occupe = true;
  try{
    var it = document.createTreeWalker(racine, NodeFilter.SHOW_TEXT, null), n, cibles = [];
    while((n = it.nextNode())){
      if(/chapitre\s*23(?![0-9])/i.test(n.nodeValue) || /\bCH\.?\s*23(?![0-9])/i.test(n.nodeValue)) cibles.push(n);
    }
    cibles.forEach(function(t){
      t.nodeValue = t.nodeValue
        .replace(/CHAPITRE\s*23(?![0-9])/g, 'DEUXIÈME ANNÉE — CHAPITRE 3')
        .replace(/Chapitre\s*23(?![0-9])/g, LIB)
        .replace(/chapitre\s*23(?![0-9])/g, 'deuxième année — chapitre 3')
        .replace(/\bCH\.?\s*23(?![0-9])/g, '2ᵉ ANNÉE · CH.3')
        .replace(/\bCh\.?\s*23(?![0-9])/g, '2ᵉ année ch.3')
        .replace(/\bch\.?\s*23(?![0-9])/g, '2ᵉ année ch.3');
    });
  }catch(e){}
  occupe = false;
}

function tout(){
  try{
    poserCours(); poserFiches(); poserQuiz(); poserCartes(); poserAuteurs(); poserSujets();
    if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex();
  }catch(e){ try{ console.warn('[ch23]', e); }catch(_){} }
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
    new MutationObserver(window.__ecoGroupe ? window.__ecoGroupe(id + '-23', cb) : cb).observe(el, {childList:true, subtree:true});
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

window.__ECO_CH23_BILAN = bilan;
setTimeout(function(){
  console.log('[ÉcoSphère v197] 2e année ch.3 — ' + bilan.fiches + ' fiches, ' + bilan.quiz
    + ' questions, ' + bilan.auteurs + ' auteurs, ' + bilan.mobiliser + ' rubriques « mobiliser », '
    + bilan.args + ' arguments ajoutés aux corrigés');
}, 7000);
})();
</script>
"""

# =============================================================== couche 2
SCRIPT2 = r"""
<script id="eco-ch23-correctifs">
(function(){
'use strict';
if(window.__ECO_CH23_FIX) return;
window.__ECO_CH23_FIX = true;

var TAGS = __TAGS__;
var N = 23;

/* --- 1. tags thematiques des questions du chapitre 23 -------------------- */
function poserTags(){
  var A = window.__ECO_ADV_ALL_BANK;
  if(!A) return false;
  var n = 0;
  A.forEach(function(q){
    if(Number(q.ch) !== N) return;
    var t = TAGS[q.id];
    if(!t) return;
    var voulu = ['deuxième année', 'chapitre 23'].concat(t);
    if((q.tags || []).length === voulu.length) return;
    q.tags = voulu;
    n++;
  });
  return n > 0;
}

/* --- 2. onglet et carte du chapitre 23 dans la section Sujets ------------ */
function nbSujets(){
  try{
    return (SUBJECTS_BANK_PREMIUM || []).filter(function(s){ return Number(s.chapter) === N; }).length;
  }catch(e){ return 0; }
}
function poserSujets(){
  var n = nbSujets();
  if(!n) return;
  var tabs = document.getElementById('subjTabsPremium');
  if(tabs && !tabs.querySelector('[data-ch23]')){
    tabs.insertAdjacentHTML('beforeend',
      '<button class="subj-tab" data-ch23="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '2ᵉ année — Ch. 3</button>');
  }
  var grid = document.getElementById('subjChaptersPremium');
  if(grid && grid.children.length && !grid.querySelector('[data-ch23]')){
    grid.insertAdjacentHTML('beforeend',
      '<div class="subj-ch-card" data-ch23="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '<div class="subj-ch-num">2ᵉ année — Chapitre 3</div>' +
      '<div class="subj-ch-title">Sujets corrigés</div>' +
      '<div class="subj-ch-count">' + n + ' dissertations corrigées</div></div>');
  }
  try{
    var b = tabs && tabs.querySelector('[data-ch23]');
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

# ================================================= retouches de source
remp = 0

# (a) relibellerResume : liste « Chapitres 9, 10, 21, 22 »
old = "return v === '21' ? '2\\u1D49 ann\\u00e9e ch.1' : (v === '22' ? '2\\u1D49 ann\\u00e9e ch.2' : v);"
new = ("return v === '21' ? '2\\u1D49 ann\\u00e9e ch.1' : (v === '22' ? '2\\u1D49 ann\\u00e9e ch.2' "
       ": (v === '23' ? '2\\u1D49 ann\\u00e9e ch.3' : v));")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (b) « Qui suis-je ? » : libelleCh
old = "  if(String(n) === '22') return 'Deuxième année — Chapitre 2';\n  return 'Chapitre ' + n;"
new = ("  if(String(n) === '22') return 'Deuxième année — Chapitre 2';\n"
       "  if(String(n) === '23') return 'Deuxième année — Chapitre 3';\n  return 'Chapitre ' + n;")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (c) frise : chLabel
old = "  if(String(n) === '22') return '2ᵉ année — ch.2';\n  return 'Ch. ' + n;"
new = ("  if(String(n) === '22') return '2ᵉ année — ch.2';\n"
       "  if(String(n) === '23') return '2ᵉ année — ch.3';\n  return 'Ch. ' + n;")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (d) frise : optionsCh
old = ("String(c) === '22' ? 'Deuxième année — Chapitre 2' : 'Chapitre ' + c")
new = ("String(c) === '22' ? 'Deuxième année — Chapitre 2' : "
       "String(c) === '23' ? 'Deuxième année — Chapitre 3' : 'Chapitre ' + c")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (e) page Quiz : listes de selection des chapitres (couche « chapitres manquants »)
old = ("  {n:22, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.2', lab:'FMN, \\u00c9tats et politique industrielle'}\n];")
new = ("  {n:22, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.2', lab:'FMN, \\u00c9tats et politique industrielle'},\n"
       "  {n:23, court:'2\\u1D49 ann\\u00e9e \\u2014 Ch.3', lab:'Analyse \\u00e9conomique du commerce international'}\n];")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (f) page Quiz : libelle des cases a cocher pour les chapitres de deuxieme annee
old = "  return (c.n === 21 ? '2ᵉ année — Ch.1' : 'Ch.' + c.n) + ' · ' + c.lab;"
new = ("  var pre = c.n === 21 ? '2ᵉ année — Ch.1' : c.n === 22 ? '2ᵉ année — Ch.2'\n"
       "          : c.n === 23 ? '2ᵉ année — Ch.3' : 'Ch.' + c.n;\n  return pre + ' · ' + c.lab;")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# (g) page Fiches : puces de filtre des chapitres de deuxieme annee
old = "var CHIPS = [[9,'Ch.9'],[10,'Ch.10'],[21,'2ᵉ année — Ch.1']];"
new = ("var CHIPS = [[9,'Ch.9'],[10,'Ch.10'],[21,'2ᵉ année — Ch.1'],"
       "[22,'2ᵉ année — Ch.2'],[23,'2ᵉ année — Ch.3']];")
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); remp += 1

# ------------------------------------------------- frise : items ch23
m = re.search(r'var ITEMS = (\[.*?\]);', s, re.S)
assert m, 'tableau ITEMS de la frise introuvable'
ITEMS = json.loads(m.group(1))
par_id = {x['id']: x for x in ITEMS}
maj = 0
for idn in don23_frise.MAJ:
    x = par_id.get(idn)
    assert x is not None, 'item de frise absent : ' + idn
    ch = [int(c) for c in (x.get('ch') or [])]
    if N not in ch:
        ch.append(N)
        x['ch'] = sorted(ch)
        maj += 1
avant = len(ITEMS)
existants = set(par_id)
for x in don23_frise.NOUVEAUX:
    assert x['id'] not in existants, x['id']
    ITEMS.append(x)
ITEMS.sort(key=lambda x: (x['an'], x['type'], x['titre']))
s = s[:m.start(1)] + json.dumps(ITEMS, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
print('  frise : %d items -> %d (%d mis a jour)' % (avant, len(ITEMS), maj))

# ------------------------------------------------- assemblage des couches
SCRIPT1 = SCRIPT1.replace('__PAYLOAD__', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
SCRIPT2 = SCRIPT2.replace('__TAGS__', json.dumps(don23_quiz.TAGS, ensure_ascii=False, separators=(',', ':')))

s = s.rstrip() + '\n' + SCRIPT1.strip() + '\n\n' + SCRIPT2.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('  retouches de libelles : %d' % remp)
print('  cours : %d caracteres, %d notions, %d questions, %d sujets, %d auteurs'
      % (len(D['cours']), len(D['notions']), len(D['quiz']), len(D['subjects']), len(D['auteurs'])))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
