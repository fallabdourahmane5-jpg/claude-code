/* ÉcoSphère — Flashcards v227
   Remplace entièrement l'ancienne section : la banque automatique est
   vidée et scellée, la page est reconstruite autour de trois vues. */
(function(){
'use strict';
if(window.__ECO_FC_V227) return;
window.__ECO_FC_V227 = true;

/* __PAYLOAD__ */

var CARTES = FX.cartes, PAR_ID = {};
CARTES.forEach(function(k){ PAR_ID[k.i] = k; });

var TYPES = {def:'Définition', aut:'Auteur', mec:'Mécanisme',
             dist:'Distinction', fait:'Chiffre ou fait', form:'Formule'};
var ORDRE_T = ['def','aut','mec','dist','fait','form'];

function titreCh(ch){
  try{ var C = eval('CH_CONTENT'); if(C && C[ch] && C[ch].title) return C[ch].title; }
  catch(e){}
  return FX.titres[ch] || ('Chapitre ' + ch);
}
function etiqCh(ch){
  return FX.an[ch] === 1 ? ('1re année · ch. ' + ch)
                         : ('2e année · ch. ' + (Number(ch) - 20));
}
function numCh(ch){ return FX.an[ch] === 1 ? String(ch) : String(Number(ch) - 20); }

var CHAPS = Object.keys(FX.an).filter(function(c){
  return CARTES.some(function(k){ return k.ch === c; });
}).sort(function(a,b){ return Number(a) - Number(b); });

/* ============================================================ utilitaires */

function e(s){ return String(s == null ? '' : s)
  .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
  .replace(/"/g,'&quot;').replace(/'/g,'&#39;'); }

function nz(s){ return String(s || '').normalize('NFD')
  .replace(/[̀-ͯ]/g,'').toLowerCase().replace(/œ/g,'oe')
  .replace(/[^a-z0-9]+/g,' ').trim(); }

function $(s, r){ return (r || document).querySelector(s); }
function $$(s, r){ return [].slice.call((r || document).querySelectorAll(s)); }

/* ====================================================== ancien système */

function tableauAncien(){
  try{ var A = eval('FC_DATA'); return Array.isArray(A) ? A : null; }
  catch(x){ return null; }
}

var LEG = {def:'definition', aut:'auteur', mec:'notion', dist:'notion',
           fait:'notion', form:'formule'};

/* on écrit par indice, jamais par push : push est scellé juste après, et
   une couche tardive qui remet le tableau à zéro doit pouvoir être réparée */
function remplir(A){
  try{ A.length = 0; }catch(x){}
  CARTES.forEach(function(k, i){
    A[i] = {term:k.q, def:k.r + (k.x ? ' — ' + k.x : ''), type:LEG[k.t],
            ch:Number(k.ch), fc227:1};
  });
  try{ A.length = CARTES.length; }catch(x){}
}

function reparer(){
  var A = tableauAncien();
  if(A && A.length !== CARTES.length) remplir(A);
}

function sceller(A){
  ['push','unshift','splice','pop','shift'].forEach(function(m){
    try{
      Object.defineProperty(A, m, {value:function(){ return A.length; },
        writable:false, configurable:false, enumerable:false});
    }catch(x){}
  });
}

var ANCIEN = 0;
function neutraliser(){
  var A = tableauAncien();
  if(!A) return;
  ANCIEN = A.length;
  remplir(A);
  sceller(A);
  /* une couche tardive pourrait encore vider le tableau : on veille */
  [600, 2500, 7000, 14000].forEach(function(ms){ setTimeout(reparer, ms); });
  /* les générateurs automatiques ne doivent plus produire une seule carte */
  ['buildAllFlashcards','buildHighQualityChapterFlashcards',
   'extractHtmlDefinitionCards'].forEach(function(f){
    try{ if(typeof window[f] === 'function') window[f] = function(){ return []; }; }catch(x){}
    try{ eval(f + ' = function(){ return []; }'); }catch(x){}
  });
}

/* les anciennes cartes avaient laissé des « maîtrisée » dans eco_state :
   on ne garde que les clés qui correspondent à une carte de la banque */
function purgerAncienEtat(){
  var S = null;
  try{ S = eval('STATE'); }catch(x){}
  if(!S || !S.known) return 0;
  var bon = {};
  CARTES.forEach(function(k){ bon[k.ch + '::' + LEG[k.t] + '::' + k.q] = 1; });
  var n = 0;
  Object.keys(S.known).forEach(function(c){
    if(!bon[c]){ delete S.known[c]; n++; }
  });
  if(n){ try{ eval('saveState()'); }catch(x){} }
  return n;
}

/* la progression de l'application lit STATE.known : on l'y tient à jour */
function refleter(k, note){
  var S = null;
  try{ S = eval('STATE'); }catch(x){}
  if(!S || !S.known) return;
  var c = k.ch + '::' + LEG[k.t] + '::' + k.q;
  if(note === 3) S.known[c] = true; else delete S.known[c];
  try{ eval('saveState()'); }catch(x){}
}

/* ========================================================= mémorisation */

var CLE = 'eco-fc-v227', CLE_S = 'eco-fc-seance-v227';
var ET = {};
try{ ET = JSON.parse(localStorage.getItem(CLE) || '{}') || {}; }catch(x){ ET = {}; }
Object.keys(ET).forEach(function(i){ if(!PAR_ID[i]) delete ET[i]; });

function garder(){
  try{ localStorage.setItem(CLE, JSON.stringify(ET)); }catch(x){}
}

var JOUR = 86400000;
var INTER = [0, 1, 3, 7, 16, 35, 90];

function planifier(k, note){
  var s = ET[k.i] || (ET[k.i] = {n:0, v:0});
  if(note === 1){ s.n = 0; s.du = Date.now() + 8 * 60000; }
  else if(note === 2){ s.n = Math.max(1, (s.n || 0) - 1);
                       s.du = Date.now() + INTER[Math.min(s.n, 6)] * JOUR; }
  else { s.n = Math.min(6, (s.n || 0) + 1);
         s.du = Date.now() + INTER[s.n] * JOUR; }
  s.d = note; s.v = (s.v || 0) + 1; s.t = Date.now();
  garder();
  refleter(k, note);
}

/* état d'une carte : 0 nouvelle · 1 à revoir · 2 en cours · 3 maîtrisée */
function etat(k){
  var s = ET[k.i];
  if(!s || !s.v) return 0;
  if((s.du || 0) <= Date.now()) return 1;
  return s.d === 3 ? 3 : 2;
}

function echeance(k){
  var s = ET[k.i];
  if(!s || !s.du) return '';
  var j = Math.round((s.du - Date.now()) / JOUR);
  if(s.du <= Date.now()) return 'à revoir maintenant';
  if(j < 1) return 'à revoir dans la journée';
  return 'à revoir dans ' + j + ' jour' + (j > 1 ? 's' : '');
}

function delaiPrevu(k, note){
  var n = (ET[k.i] && ET[k.i].n) || 0;
  if(note === 1) return '8 min';
  if(note === 2) return INTER[Math.min(Math.max(1, n - 1), 6)] + ' j';
  return INTER[Math.min(6, n + 1)] + ' j';
}

/* ============================================================== séance */

var S = null;
try{ S = JSON.parse(localStorage.getItem(CLE_S) || 'null'); }catch(x){ S = null; }
if(S && (!S.file || !S.file.length || !S.file.every(function(i){ return PAR_ID[i]; }))) S = null;

function garderSeance(){
  try{
    if(S) localStorage.setItem(CLE_S, JSON.stringify(S));
    else localStorage.removeItem(CLE_S);
  }catch(x){}
}

var LOT_NEUF = 20, LOT_DU = 30;

function vivier(f){
  return CARTES.filter(function(k){
    if(f.an && FX.an[k.ch] !== f.an) return false;
    if(f.ch && k.ch !== f.ch && (k.aussi || []).indexOf(f.ch) < 0) return false;
    if(f.ty && f.ty.length && f.ty.indexOf(k.t) < 0) return false;
    return true;
  });
}

function ordreCours(a, b){
  return Number(a.ch) - Number(b.ch) || a.b - b.b;
}

function construire(mode, f){
  var v = vivier(f), l;
  if(mode === 'new'){
    l = v.filter(function(k){ return !ET[k.i] || !ET[k.i].v; }).sort(ordreCours)
         .slice(0, LOT_NEUF);
  } else {
    l = v.filter(function(k){ return etat(k) === 1; })
         .sort(function(a, b){ return (ET[a.i].du || 0) - (ET[b.i].du || 0); })
         .slice(0, LOT_DU);
  }
  return l.map(function(k){ return k.i; });
}

function nomSeance(mode, f){
  var quoi = mode === 'new' ? 'Découverte' : 'Révision';
  if(f.ch) return quoi + ' · ' + etiqCh(f.ch);
  if(f.an) return quoi + ' · ' + (f.an === 1 ? '1re année' : '2e année');
  return quoi + ' · tous les chapitres';
}

function lancer(mode, f, file){
  file = file || construire(mode, f);
  if(!file.length){ VUE = 'accueil'; dessiner(); return false; }
  S = {mode:mode, f:f, file:file, i:0, faits:{}, rates:[], lot:1,
       titre:nomSeance(mode, f), t0:Date.now()};
  garderSeance();
  VUE = 'revision'; REVELE = false;
  dessiner();
  return true;
}

function noter(note){
  if(!S || REVELE !== true) return;
  var k = PAR_ID[S.file[S.i]];
  if(!k) return;
  planifier(k, note);
  S.faits[k.i] = note;
  if(note === 1){
    if(S.rates.indexOf(k.i) < 0) S.rates.push(k.i);
    var reste = S.file.length - S.i - 1;
    var pos = reste >= 5 ? S.i + 5 : S.file.length;
    S.file.splice(pos, 0, k.i);
  }
  S.i++;
  REVELE = false;
  garderSeance();
  var z = $('#fx-k');
  if(z){
    z.classList.add('sort');
    setTimeout(function(){ dessiner(); }, 150);
  } else dessiner();
}

function finie(){ return !S || S.i >= S.file.length; }

function quitter(){
  if(S && finie()){ S = null; garderSeance(); }
  VUE = 'accueil';
  dessiner();
}

/* ============================================================= comptes */

function comptes(cartes){
  var c = {t:cartes.length, neuf:0, du:0, ok:0, cours:0};
  cartes.forEach(function(k){
    var x = etat(k);
    if(x === 0) c.neuf++; else if(x === 1) c.du++;
    else if(x === 3) c.ok++; else c.cours++;
  });
  return c;
}

function cartesCh(ch){
  return CARTES.filter(function(k){
    return k.ch === ch || (k.aussi || []).indexOf(ch) >= 0;
  });
}

/* =============================================================== rendu */

var VUE = 'accueil', REVELE = false;
var F = {an:0, ch:'', ty:[]};        /* filtres de la bibliothèque */
var RQ = '', LIM = 60, OUV = {};

function dessiner(){
  var z = $('#pg-fc');
  if(!z) return;
  if(VUE === 'revision' && S && !finie()){ z.innerHTML = revisionHTML(); brancherRevision(z); return; }
  if(VUE === 'revision' && S && finie()){ z.innerHTML = finHTML(); brancherFin(z); return; }
  z.innerHTML = '<div class="fx">' + enteteHTML() +
    (VUE === 'biblio' ? biblioHTML() : accueilHTML()) + '</div>';
  if(VUE === 'biblio') brancherBiblio(z); else brancherAccueil(z);
}

function enteteHTML(){
  return '<div class="fx-top"><div>' +
    '<div class="fx-h1">Flashcards</div>' +
    '<div class="fx-sub">' + CARTES.length + ' cartes écrites à partir des cours, ' +
    'chacune rattachée à sa sous-partie.</div></div>' +
    '<div class="fx-seg">' +
    '<button data-v="accueil"' + (VUE === 'accueil' ? ' class="on"' : '') + '>Accueil</button>' +
    '<button data-v="biblio"' + (VUE === 'biblio' ? ' class="on"' : '') + '>Bibliothèque</button>' +
    '</div></div>';
}

/* -------------------------------------------------------------- accueil */

function accueilHTML(){
  var g = comptes(CARTES), h = '';

  if(S && !finie()){
    h += '<div class="fx-reprise"><div><div class="t">Séance en cours</div>' +
      '<div class="s">' + e(S.titre) + ' — carte ' + (S.i + 1) + ' sur ' +
      S.file.length + '</div></div><div class="sp"></div>' +
      '<button class="fx-rev-btn" style="width:auto;padding:12px 22px" ' +
      'data-a="reprendre">Reprendre</button>' +
      '<button class="fx-sec" style="width:auto;padding:12px 18px" ' +
      'data-a="abandonner">Abandonner</button></div>';
  }

  h += '<div class="fx-cpt">' +
    cc(g.neuf, 'Nouvelles', 'var(--fx-ac)') +
    cc(g.du, 'À revoir', 'var(--fx-mid)') +
    cc(g.ok, 'Maîtrisées', 'var(--fx-ok)') + '</div>';

  h += '<div class="fx-go">' +
    bouton('pr', '✦', 'Découvrir de nouvelles cartes',
      g.neuf ? g.neuf + ' carte' + (g.neuf > 1 ? 's' : '') + ' jamais vue' +
        (g.neuf > 1 ? 's' : '') : 'Réserve épuisée',
      'new', !g.neuf) +
    bouton('', '↻', 'Réviser les cartes dues',
      g.du ? g.du + ' carte' + (g.du > 1 ? 's' : '') + ' à revoir maintenant'
           : 'Rien à revoir pour l’instant', 'due', !g.du) + '</div>';

  [1, 2].forEach(function(an){
    var L = CHAPS.filter(function(c){ return FX.an[c] === an; });
    if(!L.length) return;
    h += '<div class="fx-an">' + (an === 1 ? 'Première année' : 'Deuxième année') + '</div>';
    L.forEach(function(ch){
      var kk = cartesCh(ch), c = comptes(kk), t = c.t || 1;
      h += '<button class="fx-ch" data-ch="' + ch + '">' +
        '<span class="num">' + numCh(ch) + '</span>' +
        '<span class="mid"><span class="ti">' + e(titreCh(ch)) + '</span>' +
        '<span class="ba">' +
          seg(c.ok / t, 'var(--fx-ok)') + seg(c.cours / t, 'var(--fx-ac)') +
          seg(c.du / t, 'var(--fx-mid)') +
        '</span></span>' +
        '<span class="pts"><b class="p-new">' + c.neuf + ' neuves</b>' +
        '<b class="p-due">' + c.du + ' à revoir</b>' +
        '<b class="p-ok">' + c.ok + ' acquises</b></span>' +
        '<span class="go">›</span></button>';
    });
  });
  return h;
}

function seg(p, c){
  return '<i style="width:' + (Math.max(0, Math.min(1, p)) * 100).toFixed(1) +
    '%;background:' + c + '"></i>';
}
function cc(n, l, c){
  return '<div class="fx-cc" style="--c:' + c + '"><div class="n">' + n +
    '</div><div class="l">' + l + '</div></div>';
}
function bouton(cl, ico, t, s, a, off){
  return '<button class="fx-b ' + cl + '" data-m="' + a + '"' +
    (off ? ' disabled' : '') + '><span class="ico">' + ico + '</span>' +
    '<span><span class="t">' + t + '</span><span class="s">' + e(s) +
    '</span></span></button>';
}

function brancherAccueil(z){
  $$('.fx-seg button', z).forEach(function(b){
    b.onclick = function(){ VUE = b.getAttribute('data-v'); dessiner(); };
  });
  $$('.fx-b', z).forEach(function(b){
    b.onclick = function(){
      if(b.hasAttribute('disabled')) return;
      lancer(b.getAttribute('data-m'), {an:0, ch:'', ty:[]});
    };
  });
  $$('.fx-ch', z).forEach(function(b){
    b.onclick = function(){ ouvrirChapitre(b.getAttribute('data-ch')); };
  });
  var r = $('[data-a=reprendre]', z);
  if(r) r.onclick = function(){ VUE = 'revision'; REVELE = false; dessiner(); };
  var a = $('[data-a=abandonner]', z);
  if(a) a.onclick = function(){ S = null; garderSeance(); dessiner(); };
}

/* un chapitre : s'il reste des cartes dues on révise, sinon on découvre,
   sinon on ouvre la bibliothèque filtrée sur ce chapitre */
function ouvrirChapitre(ch){
  var f = {an:0, ch:ch, ty:[]};
  if(construire('due', f).length) return lancer('due', f);
  if(construire('new', f).length) return lancer('new', f);
  F = {an:0, ch:ch, ty:[]}; RQ = ''; LIM = 60; VUE = 'biblio'; dessiner();
}

/* --------------------------------------------------------- bibliothèque */

function filtrees(){
  var L = vivier(F);
  if(RQ){
    var m = nz(RQ).split(' ').filter(Boolean);
    L = L.filter(function(k){
      var t = nz(k.q + ' ' + k.r + ' ' + (k.x || '') + ' ' + k.sp);
      return m.every(function(w){ return t.indexOf(w) >= 0; });
    });
  }
  return L.sort(ordreCours);
}

function biblioHTML(){
  var L = filtrees(), h = '';
  h += '<div class="fx-bar"><div class="fx-q">' +
    '<span style="color:var(--fx-t3)">⌕</span>' +
    '<input id="fx-rq" type="search" placeholder="Chercher une notion, un auteur, un chiffre…" ' +
    'value="' + e(RQ) + '" autocomplete="off"><span class="kbd">/</span></div>' +
    '<div class="fx-fl">' +
    p('an', '0', 'Tout', F.an === 0) +
    p('an', '1', '1re année', F.an === 1) +
    p('an', '2', '2e année', F.an === 2) +
    '<span class="fx-sep"></span><select class="fx-sel" id="fx-selch">' +
    '<option value="">Tous les chapitres</option>' +
    CHAPS.filter(function(c){ return !F.an || FX.an[c] === F.an; })
      .map(function(c){
        return '<option value="' + c + '"' + (F.ch === c ? ' selected' : '') +
          '>' + e(etiqCh(c) + ' — ' + titreCh(c)) + '</option>';
      }).join('') + '</select>' +
    '<span class="fx-sep"></span>' +
    ORDRE_T.map(function(t){ return p('ty', t, TYPES[t], F.ty.indexOf(t) >= 0); }).join('') +
    '<span class="fx-nb">' + L.length + ' carte' + (L.length > 1 ? 's' : '') +
    (F.ch ? ' · dans l’ordre du cours' : '') + '</span></div></div>';

  if(!L.length){
    return h + '<div class="fx-rien"><div class="g">⌕</div>' +
      '<div class="t">Aucune carte ne correspond</div>' +
      '<div>Élargissez la recherche ou retirez un filtre.</div></div>';
  }

  var vus = L.slice(0, LIM), grp = '';
  vus.forEach(function(k){
    var g = F.ch ? (k.pa + (k.sp !== k.pa ? ' › ' + k.sp : ''))
                 : etiqCh(k.ch) + '|' + titreCh(k.ch);
    if(g !== grp){
      grp = g;
      h += '<div class="fx-grp">' + (F.ch
        ? e(g)
        : e(g.split('|')[0]) + ' <span>— ' + e(g.split('|')[1]) + '</span>') +
        '</div>';
    }
    h += itemHTML(k);
  });
  if(L.length > LIM){
    h += '<button class="fx-plus" data-plus="1">Afficher ' +
      Math.min(60, L.length - LIM) + ' cartes de plus (' + (L.length - LIM) +
      ' restantes)</button>';
  }
  return h;
}

function p(g, v, l, on){
  return '<button class="fx-p' + (on ? ' on' : '') + '" data-g="' + g +
    '" data-v="' + v + '">' + e(l) + '</button>';
}

function itemHTML(k){
  var o = OUV[k.i];
  return '<div class="fx-it' + (o ? ' ouv' : '') + '" data-i="' + k.i + '">' +
    '<button class="fx-ith"><span class="fx-etat e' + etat(k) + '"></span>' +
    '<span class="qq">' + e(k.q) + '</span>' +
    '<span class="fx-ty" data-t="' + k.t + '">' + TYPES[k.t] + '</span>' +
    '<span class="ch">⌄</span></button>' +
    '<div class="fx-itb"><div class="fx-rr">' + e(k.r) + '</div>' +
    (k.x ? '<div class="fx-xx">' + e(k.x) + '</div>' : '') +
    '<div class="fx-meta"><span class="fx-src">' + e(etiqCh(k.ch)) + ' · ' +
    e(k.sp) + (etat(k) ? ' · ' + e(echeance(k)) : '') + '</span>' +
    '<button class="fx-lien" data-src="' + k.i + '">Voir dans le cours →</button>' +
    '</div></div></div>';
}

function brancherBiblio(z){
  $$('.fx-seg button', z).forEach(function(b){
    b.onclick = function(){ VUE = b.getAttribute('data-v'); dessiner(); };
  });
  var q = $('#fx-rq', z);
  if(q){
    var min;
    q.oninput = function(){
      clearTimeout(min);
      min = setTimeout(function(){
        RQ = q.value; LIM = 60;
        var pos = q.selectionStart;
        dessiner();
        var n = $('#fx-rq');
        if(n){ n.focus(); try{ n.setSelectionRange(pos, pos); }catch(x){} }
      }, 180);
    };
  }
  $$('.fx-p', z).forEach(function(b){
    b.onclick = function(){
      var g = b.getAttribute('data-g'), v = b.getAttribute('data-v');
      if(g === 'an'){ F.an = Number(v); if(F.ch && FX.an[F.ch] !== F.an && F.an) F.ch = ''; }
      else { var i = F.ty.indexOf(v); if(i < 0) F.ty.push(v); else F.ty.splice(i, 1); }
      LIM = 60; dessiner();
    };
  });
  var sc = $('#fx-selch', z);
  if(sc) sc.onchange = function(){ F.ch = sc.value; LIM = 60; dessiner(); };
  $$('.fx-ith', z).forEach(function(b){
    b.onclick = function(){
      var it = b.parentNode, i = it.getAttribute('data-i');
      OUV[i] = !OUV[i];
      it.classList.toggle('ouv', !!OUV[i]);
    };
  });
  $$('[data-src]', z).forEach(function(b){
    b.onclick = function(ev){ ev.stopPropagation(); auCours(PAR_ID[b.getAttribute('data-src')]); };
  });
  var pl = $('[data-plus]', z);
  if(pl) pl.onclick = function(){ LIM += 60; dessiner(); };
}

/* --------------------------------------------------------------- révision */

function revisionHTML(){
  var k = PAR_ID[S.file[S.i]];
  var pct = (S.i / S.file.length * 100).toFixed(1);
  var h = '<div class="fx-rev"><div class="fx-rh">' +
    '<button class="fx-x" data-a="x">✕</button>' +
    '<div class="ti">' + e(S.titre) + '<i>' + e(etiqCh(k.ch)) + ' · ' + e(k.sp) + '</i></div>' +
    '<div class="pr">' + (S.i + 1) + ' / ' + S.file.length + '</div></div>' +
    '<div class="fx-jau"><i style="width:' + pct + '%"></i></div>' +
    '<div class="fx-sc"><div class="fx-k" id="fx-k">' +
    '<div class="fx-kh"><span class="fx-ty" data-t="' + k.t + '">' + TYPES[k.t] + '</span></div>' +
    '<div class="fx-kq">' + e(k.q) + '</div>';

  if(REVELE){
    h += '<div class="fx-ka"><div class="fx-kr">' + e(k.r) + '</div>' +
      (k.x ? '<div class="fx-kx">' + e(k.x) + '</div>' : '') +
      '<div class="fx-ks"><span>' + e(etiqCh(k.ch)) + ' · ' + e(k.pa) +
      (k.sp !== k.pa ? ' › ' + e(k.sp) : '') + '</span>' +
      '<button class="fx-lien" data-src="' + k.i + '">Voir dans le cours →</button>' +
      '</div></div>';
  }
  h += '</div></div><div class="fx-pied"><div class="fx-pied-in">';
  if(!REVELE){
    h += '<button class="fx-rev-btn" data-a="voir">Révéler la réponse</button>' +
      '<div class="fx-aide"><b>Espace</b> pour révéler · <b>Échap</b> pour quitter</div>';
  } else {
    h += '<div class="fx-notes">' +
      n(1, 'À revoir', delaiPrevu(k, 1)) +
      n(2, 'Difficile', delaiPrevu(k, 2)) +
      n(3, 'Maîtrisée', delaiPrevu(k, 3)) + '</div>' +
      '<div class="fx-aide"><b>1</b> à revoir · <b>2</b> difficile · <b>3</b> maîtrisée</div>';
  }
  return h + '</div></div></div>';
}

function n(v, l, d){
  return '<button class="fx-n" data-n="' + v + '"><span class="nl">' + l +
    '</span><span class="nd">+ ' + d + '</span></button>';
}

function brancherRevision(z){
  var x = $('[data-a=x]', z); if(x) x.onclick = quitter;
  var v = $('[data-a=voir]', z);
  if(v) v.onclick = function(){ REVELE = true; dessiner(); };
  $$('.fx-n', z).forEach(function(b){
    b.onclick = function(){ noter(Number(b.getAttribute('data-n'))); };
  });
  $$('[data-src]', z).forEach(function(b){
    b.onclick = function(){ auCours(PAR_ID[b.getAttribute('data-src')]); };
  });
}

/* ------------------------------------------------------------ fin de séance */

function finHTML(){
  var ids = Object.keys(S.faits);
  var r = 0, d = 0, m = 0;
  ids.forEach(function(i){
    var v = S.faits[i];
    if(v === 1) r++; else if(v === 2) d++; else m++;
  });
  var min = Math.max(1, Math.round((Date.now() - S.t0) / 60000));
  var reste = construire(S.mode, S.f).length;
  var h = '<div class="fx-rev"><div class="fx-rh">' +
    '<button class="fx-x" data-a="x">✕</button>' +
    '<div class="ti">' + e(S.titre) + '<i>séance terminée</i></div></div>' +
    '<div class="fx-jau"><i style="width:100%"></i></div>' +
    '<div class="fx-sc"><div class="fx-fin"><div class="g">✓</div>' +
    '<div class="t">Séance terminée</div>' +
    '<div class="s">' + ids.length + ' carte' + (ids.length > 1 ? 's' : '') +
    ' passée' + (ids.length > 1 ? 's' : '') + ' en ' + min + ' minute' +
    (min > 1 ? 's' : '') + '.</div>' +
    '<div class="fx-bil">' +
    '<div><div class="n p-ok">' + m + '</div><div class="l">Maîtrisées</div></div>' +
    '<div><div class="n p-due">' + d + '</div><div class="l">Difficiles</div></div>' +
    '<div><div class="n" style="color:var(--fx-ko)">' + r + '</div><div class="l">À revoir</div></div>' +
    '</div>';
  if(S.rates.length){
    h += '<button class="fx-rev-btn" data-a="erreurs">Reprendre mes ' +
      S.rates.length + ' erreur' + (S.rates.length > 1 ? 's' : '') + '</button>';
  }
  if(reste){
    h += '<button class="' + (S.rates.length ? 'fx-sec' : 'fx-rev-btn') +
      '" data-a="suite">Continuer — ' + reste + ' carte' + (reste > 1 ? 's' : '') +
      ' en attente</button>';
  } else if(S.mode === 'new'){
    h += '<div class="s" style="margin:14px 0 0">La réserve de cartes ' +
      'inédites est épuisée pour cette sélection.</div>';
  }
  h += '<button class="fx-sec" style="margin-top:9px" data-a="x">Revenir à l’accueil</button>';
  return h + '</div></div></div>';
}

function brancherFin(z){
  $$('[data-a]', z).forEach(function(b){
    var a = b.getAttribute('data-a');
    b.onclick = function(){
      if(a === 'x') return quitter();
      if(a === 'erreurs'){
        var l = S.rates.slice();
        S = {mode:S.mode, f:S.f, file:l, i:0, faits:{}, rates:[], lot:S.lot,
             titre:S.titre + ' · reprise', t0:Date.now()};
        garderSeance(); REVELE = false; dessiner();
      }
      if(a === 'suite'){
        var mode = S.mode, f = S.f;
        S = null; garderSeance();
        lancer(mode, f);
      }
    };
  });
}

/* ------------------------------------------------------- renvoi au cours */

function auCours(k){
  if(!k) return;
  try{ window.__ECO_GARDE_COURS.restaurer(); }catch(x){}
  var txt = '';
  try{ txt = window.__ECO_QUIZ.texteBloc(k.ch, k.b) || ''; }catch(x){}
  try{
    if(window.__ECO_RECHERCHE && window.__ECO_RECHERCHE.ouvrir){
      window.__ECO_RECHERCHE.ouvrir(['ch', String(k.ch), -1]);
    } else { eval('openCh(' + Number(k.ch) + ')'); }
  }catch(x){ try{ eval('openCh(' + Number(k.ch) + ')'); }catch(y){} }
  try{ if(txt) window.__ECO_QUIZ.viserPassage(k.b, txt); }catch(x){}
}

/* ------------------------------------------------------------- clavier */

document.addEventListener('keydown', function(ev){
  var pg = $('#pg-fc');
  if(!pg || !pg.classList.contains('on')) return;
  var c = ev.target && ev.target.tagName;
  if(c === 'INPUT' || c === 'TEXTAREA' || c === 'SELECT'){
    if(ev.key === 'Escape' && ev.target.id === 'fx-rq'){ ev.target.blur(); }
    return;
  }
  if(VUE === 'revision' && S){
    if(finie()) return;
    if(ev.key === ' ' || ev.key === 'Enter'){
      ev.preventDefault();
      if(!REVELE){ REVELE = true; dessiner(); }
      return;
    }
    if(ev.key === 'Escape'){ ev.preventDefault(); quitter(); return; }
    if(REVELE && '123'.indexOf(ev.key) >= 0){ ev.preventDefault(); noter(Number(ev.key)); }
    return;
  }
  if(ev.key === '/'){
    ev.preventDefault();
    if(VUE !== 'biblio'){ VUE = 'biblio'; dessiner(); }
    var q = $('#fx-rq'); if(q) q.focus();
    return;
  }
  if(VUE === 'accueil'){
    if(ev.key === 'n' || ev.key === 'N'){ ev.preventDefault(); lancer('new', {an:0, ch:'', ty:[]}); }
    if(ev.key === 'r' || ev.key === 'R'){ ev.preventDefault(); lancer('due', {an:0, ch:'', ty:[]}); }
  }
});

/* --------------------------------------------------------------- amorce */

function poser(){
  var z = $('#pg-fc');
  if(!z) return;
  reparer();
  if(VUE === 'revision' && (!S || finie()) ) VUE = 'accueil';
  dessiner();
}

/* les anciens appels continuent d'ouvrir la section, filtrée si besoin */
window.renderFC = function(ch){
  if(ch && Number(ch) > 0){ F = {an:0, ch:String(ch), ty:[]}; RQ = ''; LIM = 60; VUE = 'biblio'; }
  poser();
};
window.filterFC = function(ch){
  if(Number(ch) > 0){ F = {an:0, ch:String(ch), ty:[]}; RQ = ''; LIM = 60; VUE = 'biblio'; }
  else { F = {an:0, ch:'', ty:[]}; VUE = Number(ch) === -1 ? 'biblio' : 'accueil'; }
  poser();
};
window.renderFlashcards = function(){ poser(); };
try{ eval('renderFC = window.renderFC; filterFC = window.filterFC;'); }catch(x){}

/* quitter la section referme la révision plein écran */
if(typeof window.showPg === 'function' && !window.showPg.__fc227){
  var vieux = window.showPg;
  var neuf = function(id){
    if(id !== 'fc' && VUE === 'revision'){ VUE = 'accueil'; }
    var r = vieux.apply(this, arguments);
    if(id === 'fc') setTimeout(poser, 0);
    return r;
  };
  neuf.__fc227 = true;
  window.showPg = neuf;
  try{ eval('showPg = window.showPg;'); }catch(x){}
}

neutraliser();
var purgees = purgerAncienEtat();
/* la progression et l'accueil comptent désormais la nouvelle banque */
['renderProg','renderHomeStats'].forEach(function(f){
  try{ setTimeout(function(){ try{ eval(f + '()'); }catch(x){} }, 40); }catch(x){}
});
setTimeout(function(){
  try{
    var st = document.querySelectorAll('.stat .n');
    if(st.length >= 3) st[2].textContent = String(CARTES.length);
  }catch(x){}
}, 120);
poser();

window.__ECO_FC = {cartes:CARTES, etats:ET, seance:function(){ return S; },
  vue:function(v){ VUE = v; dessiner(); }, filtres:F, lancer:lancer,
  noter:noter, reveler:function(){ REVELE = true; dessiner(); },
  comptes:comptes, etat:etat, auCours:auCours, poser:poser,
  bilans:FX.bilans};

console.log('[ÉcoSphère v227] flashcards — ' + CARTES.length +
  ' cartes écrites, ' + ANCIEN + ' cartes générées retirées, ' +
  purgees + ' marques de progression périmées effacées.');
})();
