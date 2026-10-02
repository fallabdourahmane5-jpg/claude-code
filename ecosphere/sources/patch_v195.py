#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte dans l'application les auteurs relevés dans les documents et absents :
section « Auteurs », recherche, cours, fiches, quiz, sujets et cartes mentales.
La couche est purement additive : elle est ajoutée en fin de fichier."""
import io, json

import aut_v195

SRC = 'app_v192.html'
DST = 'app_v195.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>'), s.rstrip()[-200:]
assert 'eco-auteurs-v195' not in s

J = lambda o: json.dumps(o, ensure_ascii=False)

PAYLOAD = {
    'aut': aut_v195.AUTEURS,
    'notions': [{'ch': c, 'term': t, 'def': d} for (c, t, d) in aut_v195.NOTIONS],
    'quiz': {str(k): v for k, v in aut_v195.QUIZ.items()},
    'sujets': [{'id': i, 'part': n, 'args': list(a)} for (i, n, a) in aut_v195.SUJETS],
    'maps': {str(k): {'titre': v[0], 'enfants': v[1]} for k, v in aut_v195.MAPS.items()},
}

SCRIPT = """
<script id="eco-auteurs-v195">
/* =====================================================================
   ÉcoSphère Pro — audit des auteurs (v195)
   Auteurs relevés dans les documents de cours et absents de l'application.
   Couche additive : aucune donnée existante n'est supprimée ni réécrite.
   ===================================================================== */
(function(){
  'use strict';
  if (window.__ECO_AUT_V195) return;
  window.__ECO_AUT_V195 = true;

  var D = __PAYLOAD__;
  var bilan = { auteurs:0, notions:0, fiches:0, recherche:0, quiz:0, sujets:0, cartes:0 };

  function nz(x){
    return String(x == null ? '' : x)
      .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }

  /* ------------------------------------------------- 1. section Auteurs */
  try {
    if (typeof AUTHORS !== 'undefined' && Array.isArray(AUTHORS)) {
      var vus = {};
      AUTHORS.forEach(function(a){ vus[nz(a.name) + '|' + a.ch] = 1; });
      D.aut.forEach(function(a){
        var k = nz(a.name) + '|' + a.ch;
        if (vus[k]) return;
        vus[k] = 1;
        AUTHORS.push({
          name: a.name, dates: a.dates, courant: a.courant, idea: a.idea,
          oeuvres: a.oeuvres || [], detail: a.detail, phrase: a.phrase,
          ch: a.ch, chapters: a.chapters || [a.ch], eco195: 1
        });
        bilan.auteurs++;
      });
    }
  } catch(e) { console.warn('[v195] auteurs', e); }

  /* --------------------------------- 2. cours (CH_CONTENT) et 3. fiches */
  try {
    D.notions.forEach(function(n){
      var ajoutCours = false;
      if (typeof CH_CONTENT !== 'undefined' && CH_CONTENT[n.ch]) {
        var c = CH_CONTENT[n.ch];
        c.notions = c.notions || [];
        if (!c.notions.some(function(x){ return nz(x.term) === nz(n.term); })) {
          c.notions.push({ term: n.term, def: n.def, type: 'definition', eco195: 1 });
          bilan.notions++; ajoutCours = true;
        }
      }
      if (typeof FC_DATA !== 'undefined' && Array.isArray(FC_DATA)) {
        if (!FC_DATA.some(function(x){ return nz(x.term) === nz(n.term) && Number(x.ch) === Number(n.ch); })) {
          FC_DATA.push({ term: n.term, def: n.def, type: 'definition', ch: n.ch, eco195: 1 });
          bilan.fiches++;
        }
      }
      void ajoutCours;
    });
  } catch(e) { console.warn('[v195] notions', e); }

  /* ----------------------------------------- 4. recherche (index hérité) */
  try {
    if (typeof SEARCH_INDEX !== 'undefined' && Array.isArray(SEARCH_INDEX)) {
      D.aut.forEach(function(a){
        if (SEARCH_INDEX.some(function(x){ return nz(x.term) === nz(a.name); })) return;
        SEARCH_INDEX.push({
          type: 'auteur', term: a.name,
          def: [a.courant, a.idea, a.detail, (a.oeuvres || []).join(' · ')].filter(Boolean).join(' — '),
          ch: a.ch, source: 'auteur', eco195: 1
        });
        bilan.recherche++;
      });
      D.notions.forEach(function(n){
        if (SEARCH_INDEX.some(function(x){ return nz(x.term) === nz(n.term); })) return;
        SEARCH_INDEX.push({ type: 'definition', term: n.term, def: n.def, ch: n.ch,
                            source: 'définition du chapitre', eco195: 1 });
        bilan.recherche++;
      });
    }
  } catch(e) { console.warn('[v195] recherche', e); }
  /* la recherche v48 (buildSearch48) relit AUTHORS, CH_CONTENT et FC_DATA à
     chaque requête : les ajouts ci-dessus y apparaissent sans autre travail. */

  /* --------------------------------------------------------- 5. le quiz */
  /* Des couches ultérieures installent la banque d'un chapitre uniquement si
     la clé est absente : on n'en crée donc jamais, on complète seulement une
     banque déjà installée, et la passe est rejouée jusqu'à l'être partout. */
  var quizFait = {};

  function appliqueQuiz(){
    var QB = window.ECOSPHERE_QUESTION_BANK;
    if (!QB) return;
    Object.keys(D.quiz).forEach(function(ch){
      if (quizFait[ch]) return;
      var banque = QB[ch];
      if (!Array.isArray(banque) || !banque.length) return;   /* pas encore installée */
      var deja = {};
      banque.forEach(function(q){ deja[nz(q.q)] = 1; });
      D.quiz[ch].forEach(function(q, i){
        if (deja[nz(q.q)]) return;
        var o = {};
        Object.keys(q).forEach(function(k){ o[k] = q[k]; });
        o.ch = Number(ch);
        o.id = 'ch' + ch + '-aut195-' + (i + 1);
        o.eco195 = 1;
        banque.push(o);
        bilan.quiz++;
      });
      quizFait[ch] = 1;
    });
  }

  /* ------------------------------------------------------- 6. les sujets */
  /* Chaque sujet est visé nommément et l'argument est inséré à la fin de la
     partie du plan où il prend place : l'auteur n'apparaît donc que là où son
     raisonnement sert réellement la démonstration.
     Les sujets des chapitres de deuxième année sont enregistrés par des couches
     ultérieures : la passe est donc rejouable et idempotente. */
  var estPartie = function(t){ return /^\s*[IVX]+\.\s/.test(t); };
  var estSousPartie = function(t){ return /^\s*[A-Z]\.\s/.test(t); };
  var estArg = function(t){ return /^\s*\d+\)/.test(t); };
  var faits = {};

  function appliqueSujets(){
    var S = window.SUBJECTS_BANK_PREMIUM;
    if (!S || !Array.isArray(S)) return 0;
    var parId = {}, n = 0;
    S.forEach(function(x){ if (x && x.id) parId[x.id] = x; });

    D.sujets.forEach(function(ins, idx){
      if (faits[idx]) return;
      var suj = parId[ins.id];
      if (!suj || !Array.isArray(suj.plan) || !suj.plan.length) return;

      /* bornes de la partie visée */
      var vu = 0, debut = -1, fin = suj.plan.length;
      for (var i = 0; i < suj.plan.length; i++) {
        if (estPartie(String(suj.plan[i]))) {
          vu++;
          if (vu === ins.part) debut = i;
          else if (vu === ins.part + 1) { fin = i; break; }
        }
      }
      if (debut < 0) {                   /* partie absente : dernière partie */
        for (var k = suj.plan.length - 1; k >= 0; k--) {
          if (estPartie(String(suj.plan[k]))) { debut = k; fin = suj.plan.length; break; }
        }
      }
      if (debut < 0) {                   /* plan sans parties : fin du plan */
        debut = 0; fin = suj.plan.length;
      }

      /* numéro à donner : suite des arguments de la dernière sous-partie */
      var num = 0;
      for (var j = fin - 1; j > debut; j--) {
        if (estSousPartie(String(suj.plan[j]))) break;
        if (estArg(String(suj.plan[j]))) num++;
      }

      var ajouts = ins.args.map(function(txt, q){ return (num + q + 1) + ')\u00a0' + txt; });
      ajouts = ajouts.filter(function(a){
        var corps = nz(a.replace(/^\s*\d+\)\s*/, '')).slice(0, 70);
        return corps && !suj.plan.some(function(pl){ return nz(pl).indexOf(corps) >= 0; });
      });
      faits[idx] = 1;
      if (!ajouts.length) return;
      suj.plan = suj.plan.slice(0, fin).concat(ajouts, suj.plan.slice(fin));
      suj.__aut195 = (suj.__aut195 || 0) + ajouts.length;
      bilan.sujets += ajouts.length;
      n += ajouts.length;
    });
    return n;
  }

  function rejoue(){
    try { appliqueQuiz(); } catch(e) { console.warn('[v195] quiz', e); }
    try { appliqueSujets(); } catch(e) { console.warn('[v195] sujets', e); }
    try { appliqueCartes(); } catch(e) { console.warn('[v195] cartes', e); }
  }
  try {
    rejoue();
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', rejoue);
    [400, 1500, 4000, 9000].forEach(function(ms){ setTimeout(rejoue, ms); });
    if (typeof window.showPg === 'function' && !window.showPg.__aut195) {
      var vieux = window.showPg;
      window.showPg = function(id){ var r = vieux.apply(this, arguments); try { rejoue(); } catch(e){} return r; };
      window.showPg.__aut195 = 1;
    }
  } catch(e) { console.warn('[v195] relances', e); }

  /* ------------------------------------------------- 7. cartes mentales */
  /* Les cartes des chapitres de deuxième année sont installées par des couches
     ultérieures : la passe est rejouable, et n'ajoute qu'un nœud absent. */
  var cartesFait = {};

  function appliqueCartes(){
    var VM = window.VISUAL_MAPS_V83;
    if (!VM) return;
    Object.keys(D.maps).forEach(function(ch){
      if (cartesFait[ch]) return;
      var m = VM[ch];
      if (!m || !Array.isArray(m.branches) || !m.branches.length) return;
      var deja = nz(JSON.stringify(m));
      if (deja.indexOf(nz(D.maps[ch].titre)) >= 0) { cartesFait[ch] = 1; return; }
      var enfants = D.maps[ch].enfants.filter(function(x){
        var cle = nz(x.split(/[:(]/)[0]);
        return cle && deja.indexOf(cle) < 0;
      });
      cartesFait[ch] = 1;
      if (!enfants.length) return;
      m.branches.push({ title: D.maps[ch].titre, children: enfants });
      bilan.cartes += enfants.length;
    });
  }

  /* ------------------------------------------- rafraîchir ce qui est visible */
  function refresh(){
    try { if (typeof window.renderAuthors === 'function' && document.getElementById('ag')) window.renderAuthors(); } catch(e){}
    try { if (typeof window.renderFlashcards === 'function' && document.getElementById('fc-grid')) window.renderFlashcards(); } catch(e){}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', refresh);
  else refresh();

  window.__ECO_AUT_V195_BILAN = bilan;
  console.log('[ÉcoSphère v195] audit des auteurs — ' + bilan.auteurs + ' auteurs, '
    + bilan.notions + ' notions de cours, ' + bilan.fiches + ' fiches, '
    + bilan.recherche + ' entrées de recherche, ' + bilan.quiz + ' questions de quiz, '
    + bilan.sujets + ' arguments de sujets, ' + bilan.cartes + ' nœuds de cartes mentales');
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', J(PAYLOAD))
s = s.rstrip() + '\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
print('  %d auteurs, %d notions, %d questions, %d arguments dans %d sujets, %d chapitres de cartes'
      % (len(aut_v195.AUTEURS), len(aut_v195.NOTIONS),
         sum(len(v) for v in aut_v195.QUIZ.values()),
         sum(len(a) for (_i, _n, a) in aut_v195.SUJETS),
         len({i for (i, _n, _a) in aut_v195.SUJETS}), len(aut_v195.MAPS)))
