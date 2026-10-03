#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute les auteurs issus de l'audit des chapitres et synchronise, dans la
section « Auteurs », la liste des chapitres où chaque auteur est traité."""
import io, json
import aut_v196

SRC = 'app_v195.html'
DST = 'app_v196.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-auteurs-v196' not in s

CH = json.load(io.open('chapitres_auteurs.json', encoding='utf-8'))
PAYLOAD = {'aut': aut_v196.AUTEURS, 'ch': CH}

SCRIPT = """
<script id="eco-auteurs-v196">
/* =====================================================================
   ÉcoSphère Pro — audit par chapitre de l'Atlas des idées (v196)
   Ajoute les auteurs manquants et aligne, pour chaque auteur, la liste des
   chapitres où une de ses idées est effectivement traitée.
   ===================================================================== */
(function(){
  'use strict';
  if (window.__ECO_AUT_V196) return;
  window.__ECO_AUT_V196 = true;

  var D = __PAYLOAD__;
  var bilan = { auteurs:0, chapitres:0, recherche:0 };

  function nz(x){
    return String(x == null ? '' : x)
      .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }

  /* ----------------------------------------------- nouveaux auteurs */
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
          ch: a.ch, chapters: a.chapters || [a.ch], eco196: 1
        });
        bilan.auteurs++;
      });

      /* ------------------- chapitres réellement traités dans l'Atlas */
      var parNom = {};
      Object.keys(D.ch).forEach(function(n){ parNom[nz(n)] = D.ch[n]; });
      AUTHORS.forEach(function(a){
        var lst = parNom[nz(a.name)];
        if (!lst || !lst.length) return;
        var avant = (a.chapters || []).join(',');
        var apres = lst.join(',');
        if (avant === apres) return;
        a.chapters = lst.slice();
        bilan.chapitres++;
      });
    }
  } catch(e) { console.warn('[v196] auteurs', e); }

  /* ------------------------------------------- index hérité de recherche */
  try {
    if (typeof SEARCH_INDEX !== 'undefined' && Array.isArray(SEARCH_INDEX)) {
      D.aut.forEach(function(a){
        if (SEARCH_INDEX.some(function(x){ return nz(x.term) === nz(a.name); })) return;
        SEARCH_INDEX.push({
          type: 'auteur', term: a.name,
          def: [a.courant, a.idea, a.detail, (a.oeuvres || []).join(' · ')].filter(Boolean).join(' — '),
          ch: a.ch, source: 'auteur', eco196: 1
        });
        bilan.recherche++;
      });
    }
  } catch(e) { console.warn('[v196] recherche', e); }

  function refresh(){
    try { if (typeof window.renderAuthors === 'function' && document.getElementById('ag')) window.renderAuthors(); } catch(e){}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', refresh);
  else refresh();

  window.__ECO_AUT_V196_BILAN = bilan;
  console.log('[ÉcoSphère v196] audit par chapitre — ' + bilan.auteurs + ' auteurs ajoutés, '
    + bilan.chapitres + ' auteurs dont les chapitres ont été complétés, '
    + bilan.recherche + ' entrées de recherche');
})();
</script>
"""

SCRIPT = SCRIPT.replace('__PAYLOAD__', json.dumps(PAYLOAD, ensure_ascii=False, separators=(',', ':')))
s = s.rstrip() + '\n' + SCRIPT.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
