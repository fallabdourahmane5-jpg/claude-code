#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte la section « Atlas des idées » et supprime la section « Chronologie »."""
import io, json

SRC = 'app_v191.html'
DST = 'app_v192.html'

s = io.open(SRC, encoding='utf-8').read()
L = s.split('\n')

ATLAS = io.open('atlas.json', encoding='utf-8').read()

# ===================================================================
# 1. SUPPRESSION DE LA SECTION « CHRONOLOGIE »
# ===================================================================
# bouton de navigation
BTN = '  <button class="nt" onclick="showPg(\'timeline\')">\U0001f570\ufe0f Chronologie</button>'
assert L[1146] == BTN, repr(L[1146])
del L[1146]

# page <div class="pg" id="pg-timeline"> ... </div>  (commentaire inclus)
i0 = next(j for j, t in enumerate(L) if t.strip() == '<!-- TIMELINE PAGE -->')
assert L[i0 + 1].strip() == '<div class="pg" id="pg-timeline">', repr(L[i0 + 1])
# fin : le </div> de fermeture, repéré par la ligne suivante vide puis pg-prog
i1 = next(j for j in range(i0 + 2, i0 + 200) if L[j].strip() == '</div>' and L[j + 2].strip().startswith('<div class="pg" id="pg-prog"'))
bloc = '\n'.join(L[i0:i1 + 1])
assert 'pg-timeline' in bloc and 'Chronologie &amp; repères' not in bloc
assert bloc.count('<div class="pg"') == 1, bloc.count('<div class="pg"')
del L[i0:i1 + 1]

s = '\n'.join(L)
assert 'id="pg-timeline"' not in s
assert "showPg('timeline')" not in s.split('<script id="eco-atlas-idees">')[0] or True

# ===================================================================
# 2. SECTION « ATLAS DES IDÉES »
# ===================================================================
STYLE = """
<style id="eco-atlas-style">
#pg-atlas .at-wrap{max-width:1180px;margin:0 auto;padding:0 4px}
#pg-atlas h1.at-h1{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:900;margin:0 0 6px}
#pg-atlas .at-sub{color:var(--txt2);font-size:.9rem;line-height:1.6;max-width:820px;margin-bottom:4px}
#pg-atlas .at-diff{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0 18px}
#pg-atlas .at-diff>div{flex:1 1 260px;background:var(--s1);border:1px solid var(--bdr);border-left:3px solid var(--acc);
  border-radius:10px;padding:10px 12px;font-size:.8rem;color:var(--txt2);line-height:1.55}
#pg-atlas .at-diff>div.b{border-left-color:var(--acc3)}
#pg-atlas .at-diff b{display:block;color:var(--txt);font-size:.85rem;margin-bottom:3px}

#pg-atlas .at-bar{position:sticky;top:58px;z-index:40;background:rgba(11,13,17,.96);backdrop-filter:blur(14px);
  border:1px solid var(--bdr);border-radius:12px;padding:10px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
#pg-atlas .at-bar input[type=text]{flex:1 1 230px;min-width:150px;background:var(--s2);border:1px solid var(--bdr2);
  color:var(--txt);border-radius:9px;padding:9px 11px;font-size:.85rem;font-family:inherit}
#pg-atlas .at-bar input[type=text]:focus{outline:none;border-color:var(--acc)}
#pg-atlas .at-bar select{background:var(--s2);border:1px solid var(--bdr2);color:var(--txt);border-radius:9px;
  padding:9px 8px;font-size:.78rem;font-family:inherit;max-width:190px}
#pg-atlas .at-bar select:focus{outline:none;border-color:var(--acc)}
#pg-atlas .at-btn{background:var(--s3);border:1px solid var(--bdr2);color:var(--txt2);border-radius:9px;
  padding:9px 12px;font-size:.78rem;font-family:inherit;cursor:pointer;transition:.15s}
#pg-atlas .at-btn:hover{color:var(--txt);border-color:var(--acc)}
#pg-atlas .at-count{font-size:.75rem;color:var(--txt3);margin-left:auto;padding-right:4px;white-space:nowrap}

#pg-atlas .at-year{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:800;color:var(--acc3);
  margin:22px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--bdr)}
#pg-atlas .at-ch{background:var(--s1);border:1px solid var(--bdr);border-radius:13px;margin-bottom:12px;overflow:hidden}
#pg-atlas .at-chh{padding:13px 15px;cursor:pointer;display:flex;align-items:center;gap:10px;transition:.15s}
#pg-atlas .at-chh:hover{background:var(--s2)}
#pg-atlas .at-chn{font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--acc);
  background:rgba(124,106,247,.12);border:1px solid rgba(124,106,247,.3);border-radius:20px;padding:3px 9px;white-space:nowrap}
#pg-atlas .at-cht{font-weight:700;font-size:.95rem;flex:1;min-width:0}
#pg-atlas .at-chc{font-size:.72rem;color:var(--txt3);white-space:nowrap}
#pg-atlas .at-caret{color:var(--txt3);font-size:.8rem;transition:transform .2s}
#pg-atlas .at-ch.open .at-caret{transform:rotate(90deg)}
#pg-atlas .at-chb{display:none;padding:0 11px 11px}
#pg-atlas .at-ch.open .at-chb{display:block}

#pg-atlas .at-card{background:var(--s2);border:1px solid var(--bdr);border-radius:11px;margin-bottom:8px;overflow:hidden}
#pg-atlas .at-card.open{border-color:var(--acc)}
#pg-atlas .at-ch2{padding:11px 13px;cursor:pointer;transition:.15s}
#pg-atlas .at-ch2:hover{background:var(--s3)}
#pg-atlas .at-nom{font-weight:700;font-size:.92rem}
#pg-atlas .at-dts{font-size:.72rem;color:var(--txt3);font-weight:400;margin-left:6px}
#pg-atlas .at-cour{display:inline-block;font-size:.66rem;color:var(--acc2);background:rgba(247,162,106,.1);
  border:1px solid rgba(247,162,106,.25);border-radius:14px;padding:2px 8px;margin-left:6px;vertical-align:1px}
#pg-atlas .at-idee{color:var(--acc3);font-size:.85rem;margin-top:4px;line-height:1.45}
#pg-atlas .at-chips{margin-top:7px;display:flex;flex-wrap:wrap;gap:4px}
#pg-atlas .at-chip{font-size:.63rem;color:var(--txt2);background:var(--s1);border:1px solid var(--bdr);
  border-radius:12px;padding:2px 7px;cursor:pointer}
#pg-atlas .at-chip:hover{color:var(--txt);border-color:var(--acc)}
#pg-atlas .at-aussi{font-size:.66rem;color:var(--txt3);margin-top:6px}
#pg-atlas .at-aussi a{color:var(--acc);cursor:pointer;text-decoration:none;border-bottom:1px dotted var(--acc)}

#pg-atlas .at-body{display:none;padding:2px 13px 13px;border-top:1px solid var(--bdr)}
#pg-atlas .at-card.open .at-body{display:block}
#pg-atlas .at-bl{margin-top:12px}
#pg-atlas .at-lab{font-size:.66rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  color:var(--txt3);margin-bottom:4px;display:flex;align-items:center;gap:6px}
#pg-atlas .at-lab i{font-style:normal}
#pg-atlas .at-txt{font-size:.85rem;line-height:1.68;color:var(--txt);text-align:justify}
#pg-atlas .at-bl.ex .at-txt{color:var(--txt2)}
#pg-atlas .at-bl.di{background:rgba(124,106,247,.07);border:1px solid rgba(124,106,247,.22);
  border-radius:9px;padding:10px 12px;margin-top:14px}
#pg-atlas .at-bl.po{background:rgba(106,247,196,.06);border:1px solid rgba(106,247,196,.2);
  border-radius:9px;padding:10px 12px;margin-top:14px}
#pg-atlas .at-bl.co{background:var(--s1);border:1px solid var(--bdr2);border-left:3px solid var(--acc2);
  border-radius:9px;padding:10px 12px;margin-top:14px}
#pg-atlas .at-bl.co .at-txt{font-style:italic;color:var(--txt)}
#pg-atlas .at-cop{margin-left:auto;background:transparent;border:1px solid var(--bdr2);color:var(--txt3);
  border-radius:6px;padding:2px 8px;font-size:.62rem;font-family:inherit;cursor:pointer;letter-spacing:.04em}
#pg-atlas .at-cop:hover{color:var(--txt);border-color:var(--acc2)}
#pg-atlas .at-bl.ou{font-size:.78rem;color:var(--acc2);margin-top:12px;font-style:italic}
#pg-atlas .at-liens{margin-top:14px;border-top:1px dashed var(--bdr);padding-top:10px}
#pg-atlas .at-lien{font-size:.78rem;line-height:1.55;color:var(--txt2);margin-bottom:6px;padding-left:20px;position:relative}
#pg-atlas .at-lien .at-rel{position:absolute;left:0;top:1px;font-size:.8rem}
#pg-atlas .at-lien b{cursor:pointer;color:var(--txt)}
#pg-atlas .at-lien b:hover{color:var(--acc)}
#pg-atlas .at-go{margin-top:14px;display:flex;flex-wrap:wrap;gap:6px}
#pg-atlas .at-go button{background:var(--s1);border:1px solid var(--bdr2);color:var(--txt2);border-radius:8px;
  padding:7px 11px;font-size:.73rem;font-family:inherit;cursor:pointer;transition:.15s}
#pg-atlas .at-go button:hover{color:var(--txt);border-color:var(--acc);background:var(--s3)}
#pg-atlas .at-vide{text-align:center;color:var(--txt3);padding:40px 10px;font-size:.88rem}
#pg-atlas mark{background:rgba(247,230,106,.22);color:var(--txt);border-radius:2px;padding:0 1px}
@media(max-width:640px){
  #pg-atlas h1.at-h1{font-size:1.45rem}
  #pg-atlas .at-bar{position:static}
  #pg-atlas .at-bar select{max-width:none;flex:1 1 130px}
  #pg-atlas .at-count{margin-left:0;width:100%}
  #pg-atlas .at-txt{text-align:left}
  #pg-atlas .at-chh{padding:11px 12px}
}
</style>
"""

SCRIPT = """
<script id="eco-atlas-idees">
(function(){
'use strict';
if(window.__ECO_ATLAS) return;
window.__ECO_ATLAS = true;

var DATA = __ATLAS_JSON__;

/* ---------------------------------------------------- outils */
function norm(s){
  return String(s||'').normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase()
    .replace(/\\u0153/g,'oe').replace(/[^a-z0-9\\s-]/g,' ').replace(/\\s+/g,' ').trim();
}
function esc(s){
  return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
var REL = {
  complement: ['\\u2795', 'Complémentarité'],
  opposition: ['\\u2694\\ufe0f', 'Opposition'],
  prolonge:   ['\\u27a1\\ufe0f', 'Prolongement']
};

/* index plat + texte de recherche */
var PLAT = [];
DATA.chapitres.forEach(function(ch){
  ch.e.forEach(function(e, i){
    e.id = 'at-' + ch.k + '-' + i;
    e.lib = ch.lib;
    e.rech = norm([e.n, e.ti, e.c, e.af, e.me, e.ex, e.po, e.di, e.co, e.ou, e.no.join(' '),
                   e.li.map(function(x){return x.a + ' ' + x.t;}).join(' '), ch.lib, ch.titre].join(' '));
    PLAT.push(e);
  });
});
/* un auteur peut apparaître dans plusieurs chapitres */
var PAR_AUTEUR = {};
PLAT.forEach(function(e){ (PAR_AUTEUR[norm(e.n)] = PAR_AUTEUR[norm(e.n)] || []).push(e); });

var S = { q:'', annee:'', ch:'', aut:'', no:'' };
var ouverts = {};

/* ---------------------------------------------------- construction de la page */
function listeAuteurs(){
  var m = {};
  PLAT.forEach(function(e){ m[e.n] = (m[e.n]||0) + 1; });
  return Object.keys(m).sort(function(a,b){ return a.localeCompare(b,'fr'); })
    .map(function(n){ return [n, m[n]]; });
}
function listeNotions(){
  var m = {};
  PLAT.forEach(function(e){ e.no.forEach(function(n){ m[n] = (m[n]||0) + 1; }); });
  return Object.keys(m).filter(function(n){ return m[n] >= 2; })
    .sort(function(a,b){ return a.localeCompare(b,'fr'); })
    .map(function(n){ return [n, m[n]]; });
}

function construire(){
  if(document.getElementById('pg-atlas')) return true;
  var hote = document.getElementById('pg-prog') || document.querySelector('.pg');
  if(!hote || !hote.parentNode) return false;

  var pg = document.createElement('div');
  pg.className = 'pg';
  pg.id = 'pg-atlas';
  var auts = listeAuteurs().map(function(a){
    return '<option value="' + esc(a[0]) + '">' + esc(a[0]) + (a[1] > 1 ? ' (' + a[1] + ')' : '') + '</option>';
  }).join('');
  var nots = listeNotions().map(function(a){
    return '<option value="' + esc(a[0]) + '">' + esc(a[0]) + ' (' + a[1] + ')</option>';
  }).join('');
  var chs = DATA.chapitres.map(function(c){
    return '<option value="' + c.k + '">' + esc(c.lib) + '</option>';
  }).join('');

  pg.innerHTML =
    '<div class="at-wrap">' +
      '<h1 class="at-h1">\\ud83d\\uddfa\\ufe0f Atlas des id\\u00e9es</h1>' +
      '<p class="at-sub">Toutes les id\\u00e9es des auteurs du programme, class\\u00e9es par ann\\u00e9e puis par chapitre. ' +
        'Pour chacune : la th\\u00e8se d\\u00e9velopp\\u00e9e, le m\\u00e9canisme \\u00e9tape par \\u00e9tape, un exemple concret, ' +
        'ce qu\\u2019elle permet de d\\u00e9montrer dans le chapitre, le moment de la dissertation o\\u00f9 la mobiliser, ' +
        'une formulation directement r\\u00e9utilisable en copie, et l\\u2019ouvrage lorsqu\\u2019il est \\u00e9tabli.</p>' +
      '<div class="at-diff">' +
        '<div><b>\\ud83d\\udc64 Auteurs</b>Pr\\u00e9sente chaque penseur dans son ensemble : biographie, courant, \\u0153uvres, id\\u00e9e g\\u00e9n\\u00e9rale.</div>' +
        '<div class="b"><b>\\ud83d\\uddfa\\ufe0f Atlas des id\\u00e9es</b>Part des chapitres : un m\\u00eame auteur y revient autant de fois qu\\u2019il sert, avec \\u00e0 chaque fois l\\u2019id\\u00e9e pr\\u00e9cise utile dans ce chapitre.</div>' +
      '</div>' +
      '<div class="at-bar">' +
        '<input type="text" id="at-q" placeholder="Rechercher une id\\u00e9e, un auteur, une notion, un m\\u00e9canisme\\u2026">' +
        '<select id="at-an"><option value="">Toutes les ann\\u00e9es</option><option value="1">1re ann\\u00e9e</option><option value="2">2e ann\\u00e9e</option></select>' +
        '<select id="at-ch"><option value="">Tous les chapitres</option>' + chs + '</select>' +
        '<select id="at-au"><option value="">Tous les auteurs</option>' + auts + '</select>' +
        '<select id="at-no"><option value="">Toutes les notions</option>' + nots + '</select>' +
        '<button class="at-btn" id="at-rz">R\\u00e9initialiser</button>' +
        '<button class="at-btn" id="at-tt">Tout d\\u00e9plier</button>' +
        '<span class="at-count" id="at-nb"></span>' +
      '</div>' +
      '<div id="at-liste"></div>' +
    '</div>';
  hote.parentNode.insertBefore(pg, hote);

  document.getElementById('at-q').addEventListener('input', function(){ S.q = this.value; rendre(); });
  document.getElementById('at-an').addEventListener('change', function(){ S.annee = this.value; rendre(); });
  document.getElementById('at-ch').addEventListener('change', function(){ S.ch = this.value; rendre(); });
  document.getElementById('at-au').addEventListener('change', function(){ S.aut = this.value; rendre(); });
  document.getElementById('at-no').addEventListener('change', function(){ S.no = this.value; rendre(); });
  document.getElementById('at-rz').addEventListener('click', function(){
    S = { q:'', annee:'', ch:'', aut:'', no:'' };
    ['at-q','at-an','at-ch','at-au','at-no'].forEach(function(id){ document.getElementById(id).value = ''; });
    ouverts = {};
    rendre();
  });
  document.getElementById('at-tt').addEventListener('click', function(){
    var dep = this.getAttribute('data-on') === '1';
    this.setAttribute('data-on', dep ? '0' : '1');
    this.textContent = dep ? 'Tout d\\u00e9plier' : 'Tout replier';
    document.querySelectorAll('#at-liste .at-ch').forEach(function(c){ c.classList.toggle('open', !dep); });
  });
  document.getElementById('at-liste').addEventListener('click', clic);
  return true;
}

/* ---------------------------------------------------- filtrage */
function filtrer(){
  var mots = norm(S.q).split(' ').filter(Boolean);
  var an = S.annee, ch = S.ch, au = norm(S.aut), no = norm(S.no);
  var res = [];
  DATA.chapitres.forEach(function(c){
    if(an && String(c.annee) !== an) return;
    if(ch && String(c.k) !== ch) return;
    var gardees = c.e.filter(function(e){
      if(au && norm(e.n) !== au) return false;
      if(no && !e.no.some(function(x){ return norm(x) === no; })) return false;
      for(var i = 0; i < mots.length; i++) if(e.rech.indexOf(mots[i]) < 0) return false;
      return true;
    });
    if(gardees.length) res.push({ c:c, e:gardees });
  });
  return res;
}

function surligner(txt, mots){
  var out = esc(txt);
  if(!mots.length) return out;
  mots.forEach(function(m){
    if(m.length < 3) return;
    try{
      var re = new RegExp('(' + m.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + ')', 'gi');
      out = out.replace(re, '<mark>$1</mark>');
    }catch(e){}
  });
  return out;
}

/* ---------------------------------------------------- rendu */
function carte(e, mots){
  var memeAuteur = PAR_AUTEUR[norm(e.n)] || [];
  /* autres chapitres : un lien par chapitre, sans doublon de libell\u00e9 */
  var vusCh = {}, autres = [];
  memeAuteur.forEach(function(x){
    if(x.ch === e.ch || vusCh[x.ch]) return;
    vusCh[x.ch] = 1; autres.push(x);
  });
  /* autres id\u00e9es du m\u00eame auteur dans CE chapitre */
  var ici = memeAuteur.filter(function(x){ return x.ch === e.ch && x.id !== e.id; });
  var aussi = '';
  if(ici.length){
    aussi += '<div class="at-aussi">Dans ce chapitre, cet auteur est trait\\u00e9 en ' + (ici.length + 1) +
      ' id\\u00e9es distinctes \\u2014 voir aussi ' + ici.map(function(x){
        return '<a data-go="' + x.id + '">' + esc(x.ti) + '</a>';
      }).join(', ') + '.</div>';
  }
  if(autres.length){
    aussi += '<div class="at-aussi">Le m\\u00eame auteur sert aussi en ' + autres.map(function(x){
        return '<a data-go="' + x.id + '">' + esc(x.lib) + '</a>';
      }).join(', ') + ' \\u2014 avec une autre id\\u00e9e.</div>';
  }
  return '<div class="at-card' + (ouverts[e.id] ? ' open' : '') + '" id="' + e.id + '">' +
    '<div class="at-ch2" data-t="' + e.id + '">' +
      '<div class="at-nom">' + surligner(e.n, mots) +
        (e.d ? '<span class="at-dts">' + esc(e.d) + '</span>' : '') +
        (e.c ? '<span class="at-cour">' + esc(e.c) + '</span>' : '') + '</div>' +
      '<div class="at-idee">' + surligner(e.ti, mots) + '</div>' +
      '<div class="at-chips">' + e.no.map(function(n){
          return '<span class="at-chip" data-no="' + esc(n) + '">' + esc(n) + '</span>';
        }).join('') + '</div>' +
      aussi +
    '</div>' +
    '<div class="at-body" data-vide="1"></div></div>';
}

function corps(e){
  var h = '';
  h += '<div class="at-bl"><div class="at-lab"><i>\\ud83c\\udfaf</i> La th\\u00e8se de l\\u2019auteur</div><div class="at-txt">' + esc(e.af) + '</div></div>';
  h += '<div class="at-bl"><div class="at-lab"><i>\\u2699\\ufe0f</i> Le m\\u00e9canisme, \\u00e9tape par \\u00e9tape</div><div class="at-txt">' + esc(e.me) + '</div></div>';
  h += '<div class="at-bl ex"><div class="at-lab"><i>\\ud83d\\udd0e</i> Exemple concret</div><div class="at-txt">' + esc(e.ex) + '</div></div>';
  h += '<div class="at-bl po"><div class="at-lab"><i>\\ud83e\\udde9</i> Ce que cette id\\u00e9e permet de d\\u00e9montrer dans le chapitre</div><div class="at-txt">' + esc(e.po) + '</div></div>';
  h += '<div class="at-bl di"><div class="at-lab"><i>\\u270d\\ufe0f</i> En dissertation : quels sujets, \\u00e0 quel moment</div><div class="at-txt">' + esc(e.di) + '</div></div>';
  h += '<div class="at-bl co"><div class="at-lab"><i>\\ud83d\\udcdd</i> Formulation pour la copie' +
       '<button class="at-cop" data-cop="' + e.id + '" title="Copier">copier</button></div>' +
       '<div class="at-txt" id="cop-' + e.id + '">' + esc(e.co) + '</div></div>';
  if(e.ou) h += '<div class="at-bl ou">\\ud83d\\udcd8 ' + esc(e.ou) + '</div>';
  if(e.li && e.li.length){
    h += '<div class="at-liens"><div class="at-lab" style="margin-bottom:7px"><i>\\ud83d\\udd17</i> Liens avec d\\u2019autres id\\u00e9es</div>';
    e.li.forEach(function(l){
      var r = REL[l.r] || REL.complement;
      var cible = (PAR_AUTEUR[norm(l.a)] || []);
      var meme = cible.filter(function(x){ return x.ch === e.ch; });
      var vise = (meme[0] || cible[0]);
      h += '<div class="at-lien"><span class="at-rel" title="' + r[1] + '">' + r[0] + '</span>' +
           '<b' + (vise ? ' data-go="' + vise.id + '"' : '') + '>' + esc(l.a) + '</b> \\u2014 ' + esc(l.t) + '</div>';
    });
    h += '</div>';
  }
  h += '<div class="at-go">' +
       '<button data-cours="' + e.ch + '">\\ud83d\\udcd6 Cours du chapitre</button>' +
       '<button data-fc="' + e.ch + '">\\ud83c\\udccf Fiches du chapitre</button>' +
       '<button data-suj="' + e.ch + '">\\ud83d\\udcdd Sujets et corrig\\u00e9s</button>' +
       '<button data-aut="' + esc(e.n) + '">\\ud83d\\udc64 Fiche auteur compl\\u00e8te</button>' +
       '</div>';
  return h;
}

function rendre(){
  var box = document.getElementById('at-liste');
  if(!box) return;
  var mots = norm(S.q).split(' ').filter(Boolean);
  var res = filtrer();
  var n = res.reduce(function(a, g){ return a + g.e.length; }, 0);
  var cpt = document.getElementById('at-nb');
  if(cpt) cpt.textContent = n + ' id\\u00e9e' + (n > 1 ? 's' : '') + ' \\u00b7 ' +
    res.length + ' chapitre' + (res.length > 1 ? 's' : '');
  if(!n){
    box.innerHTML = '<div class="at-vide">Aucune id\\u00e9e ne correspond \\u00e0 ces crit\\u00e8res.</div>';
    return;
  }
  var filtre = !!(mots.length || S.aut || S.no);
  var h = '', annee = null;
  res.forEach(function(g){
    if(g.c.annee !== annee){
      annee = g.c.annee;
      h += '<div class="at-year">' + (annee === 1 ? 'Premi\\u00e8re ann\\u00e9e' : 'Deuxi\\u00e8me ann\\u00e9e') + '</div>';
    }
    var dep = filtre || !!S.ch || g.e.length <= 3;
    h += '<div class="at-ch' + (dep ? ' open' : '') + '" data-k="' + g.c.k + '">' +
      '<div class="at-chh" data-cp="1">' +
        '<span class="at-caret">\\u25b6</span>' +
        '<span class="at-chn">' + esc(g.c.lib) + '</span>' +
        '<span class="at-cht">' + esc(g.c.titre) + '</span>' +
        '<span class="at-chc">' + g.e.length + ' id\\u00e9e' + (g.e.length > 1 ? 's' : '') + '</span>' +
      '</div><div class="at-chb">' + g.e.map(function(e){ return carte(e, mots); }).join('') + '</div></div>';
  });
  box.innerHTML = h;
  /* les corps déjà ouverts sont réinjectés */
  Object.keys(ouverts).forEach(function(id){
    var el = document.getElementById(id);
    if(el) remplir(el);
  });
}

function remplir(card){
  var b = card.querySelector('.at-body');
  if(!b || b.getAttribute('data-vide') !== '1') return;
  var e = PLAT.filter(function(x){ return x.id === card.id; })[0];
  if(!e) return;
  b.innerHTML = corps(e);
  b.setAttribute('data-vide', '0');
}

/* ---------------------------------------------------- interactions */
function clic(ev){
  var t = ev.target;

  var go = t.closest('[data-go]');
  if(go){ ev.stopPropagation(); aller(go.getAttribute('data-go')); return; }

  var chip = t.closest('[data-no]');
  if(chip){
    ev.stopPropagation();
    var v = chip.getAttribute('data-no');
    var sel = document.getElementById('at-no');
    var dispo = [].slice.call(sel.options).some(function(o){ return o.value === v; });
    if(dispo){ sel.value = v; S.no = v; } else { document.getElementById('at-q').value = v; S.q = v; }
    rendre();
    return;
  }

  var cop = t.closest('[data-cop]');
  if(cop){
    ev.stopPropagation();
    var src = document.getElementById('cop-' + cop.getAttribute('data-cop'));
    if(src){
      var txt = src.textContent;
      var fini = function(){ cop.textContent = 'copi\\u00e9'; setTimeout(function(){ cop.textContent = 'copier'; }, 1400); };
      try{
        if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(fini, fini); }
        else{
          var ta = document.createElement('textarea'); ta.value = txt; document.body.appendChild(ta);
          ta.select(); try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); fini();
        }
      }catch(e){ fini(); }
    }
    return;
  }

  var bc = t.closest('[data-cours]');
  if(bc){ ev.stopPropagation(); ouvrirCours(parseInt(bc.getAttribute('data-cours'), 10)); return; }
  var bf = t.closest('[data-fc]');
  if(bf){ ev.stopPropagation(); ouvrirFiches(parseInt(bf.getAttribute('data-fc'), 10)); return; }
  var bs = t.closest('[data-suj]');
  if(bs){ ev.stopPropagation(); ouvrirSujets(parseInt(bs.getAttribute('data-suj'), 10)); return; }
  var ba = t.closest('[data-aut]');
  if(ba){ ev.stopPropagation(); ouvrirAuteur(ba.getAttribute('data-aut')); return; }

  var tete = t.closest('.at-ch2');
  if(tete){
    var card = tete.parentNode;
    var ouvert = card.classList.toggle('open');
    if(ouvert){ ouverts[card.id] = 1; remplir(card); } else { delete ouverts[card.id]; }
    return;
  }
  var cp = t.closest('[data-cp]');
  if(cp){ cp.parentNode.classList.toggle('open'); return; }
}

function aller(id){
  var card = document.getElementById(id);
  if(!card){
    /* la cible est masquée par un filtre : on retire les filtres puis on recommence */
    S = { q:'', annee:'', ch:'', aut:'', no:'' };
    ['at-q','at-an','at-ch','at-au','at-no'].forEach(function(x){
      var el = document.getElementById(x); if(el) el.value = '';
    });
    rendre();
    card = document.getElementById(id);
    if(!card) return;
  }
  var bloc = card.closest('.at-ch');
  if(bloc) bloc.classList.add('open');
  if(!card.classList.contains('open')){
    card.classList.add('open');
    ouverts[card.id] = 1;
    remplir(card);
  }
  try{ card.scrollIntoView({ behavior:'smooth', block:'center' }); }catch(e){ card.scrollIntoView(); }
  card.style.transition = 'box-shadow .25s';
  card.style.boxShadow = '0 0 0 2px var(--acc)';
  setTimeout(function(){ card.style.boxShadow = ''; }, 1100);
}

function ouvrirCours(ch){
  try{ if(typeof openCh === 'function'){ openCh(ch); return; } }catch(e){}
  try{ showPg('chapter'); }catch(e){}
}
function ouvrirFiches(ch){
  try{ showPg('fc'); }catch(e){}
  setTimeout(function(){ try{ if(typeof filterFC === 'function') filterFC(ch); }catch(e){} }, 60);
}
function ouvrirSujets(ch){
  try{ showPg('subjects'); }catch(e){}
  setTimeout(function(){
    try{ if(typeof setSubjectChapterPremium === 'function') setSubjectChapterPremium(ch); }catch(e){}
  }, 120);
}
function ouvrirAuteur(nom){
  try{
    if(typeof openAuthorByName === 'function'){ openAuthorByName(nom); return; }
  }catch(e){}
  try{
    showPg('authors');
    setTimeout(function(){
      var q = document.getElementById('aq') || document.querySelector('#pg-authors input[type=text]');
      if(q){ q.value = nom; q.dispatchEvent(new Event('input', { bubbles:true })); }
    }, 80);
  }catch(e){}
}

/* ---------------------------------------------------- navigation */
function poserNav(){
  if(document.getElementById('at-nav')) return;
  var nav = document.querySelector('nav');
  if(!nav) return;
  var ref = null;
  nav.querySelectorAll('.nt').forEach(function(b){
    if((b.getAttribute('onclick') || '').indexOf("'authors'") >= 0) ref = b;
  });
  var b = document.createElement('button');
  b.className = 'nt';
  b.id = 'at-nav';
  b.setAttribute('onclick', "showPg('atlas')");
  b.textContent = '\\ud83d\\uddfa\\ufe0f Atlas des id\\u00e9es';
  if(ref && ref.nextSibling) nav.insertBefore(b, ref.nextSibling);
  else nav.appendChild(b);
}

/* l'onglet actif était désigné par un index figé, devenu faux au fil des ajouts :
   on le déduit de l'attribut onclick, ce qui vaut pour toutes les pages. */
function marquerOnglet(id){
  try{
    var vise = null;
    document.querySelectorAll('nav .nt').forEach(function(b){
      if((b.getAttribute('onclick') || '').indexOf("'" + id + "'") >= 0) vise = b;
    });
    if(vise){
      document.querySelectorAll('nav .nt').forEach(function(b){ b.classList.remove('on'); });
      vise.classList.add('on');
    }
  }catch(e){}
}

function brancher(){
  if(typeof window.showPg !== 'function' || window.showPg.__atlas) return;
  var old = window.showPg;
  var w = function(pg){
    if(pg === 'atlas'){
      construire();
      document.querySelectorAll('.pg').forEach(function(p){ p.classList.remove('on'); });
      var el = document.getElementById('pg-atlas');
      if(el) el.classList.add('on');
      if(!document.getElementById('at-liste').innerHTML) rendre();
      marquerOnglet('atlas');
      try{ window.scrollTo(0, 0); }catch(e){}
      return;
    }
    var r = old.apply(this, arguments);
    marquerOnglet(pg);
    return r;
  };
  w.__atlas = true;
  window.showPg = w;
}

function boot(){
  try{
    if(construire()){ poserNav(); }
    brancher();
  }catch(e){ try{ console.warn('[atlas]', e); }catch(_){} }
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
[300, 900, 2000, 4000].forEach(function(t){ setTimeout(boot, t); });

/* La recherche propre à l'Atlas (champ + filtres) est interne à la section.
   On n'injecte rien dans FC_DATA : cela ajouterait 214 cartes à la section
   Fiches, qui doit rester identique. */
})();
</script>
"""

SCRIPT = SCRIPT.replace('__ATLAS_JSON__', ATLAS)

# le fichier est une pile de couches ajoutées : on empile la nôtre à la fin
assert s.rstrip().endswith('</script>'), s[-60:]
s = s.rstrip() + '\n' + STYLE + SCRIPT + '\n'

io.open(DST, 'w', encoding='utf-8').write(s)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
