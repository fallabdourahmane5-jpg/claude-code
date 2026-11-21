/* ÉcoSphère — section « Quiz IA », moteur v223.
   Banque validée, filtres par chapitre, sous-partie, niveau et format,
   quatre modes de révision, et surtout : aucune question déjà vue tant qu'il
   reste des inédites. L'historique survit à la fermeture de l'application. */
(function(){
'use strict';
if(window.__ECO_QUIZ_V223) return;
window.__ECO_QUIZ_V223 = true;

/* __PAYLOAD__ */

var Q = BQ.q, SPS = BQ.sp;
var LIBN = {connaitre:'Connaître', comprendre:'Comprendre',
            appliquer:'Appliquer', raisonner:'Raisonner'};
var LIBT = {qcm:'QCM', qcmm:'QCM · plusieurs réponses', vf:'Vrai ou faux',
            assoc:'Association', ordre:'Remise en ordre',
            courte:'Réponse rédigée'};
var ORDRE_CH = ['1','2','3','4','5','6','7','8','9','10',
                '21','22','23','24','25','26'];

function libCh(k){
  k = String(k);
  var i = ORDRE_CH.indexOf(k);
  if(i < 0) return 'Chapitre ' + k;
  return Number(k) >= 21 ? '2ᵉ année — ch.' + (Number(k) - 20) : 'Chapitre ' + k;
}
function titreCh(k){
  try{ var c = CH_CONTENT[String(k)]; if(c && c.title) return c.title; }catch(e){}
  return '';
}

/* ===================================================== état persistant */
var CLE = 'eco.quiz.v223';
var S = {vues:{}, series:[], maj:0};
function lire(){
  try{
    var b = localStorage.getItem(CLE);
    if(b){ var o = JSON.parse(b); if(o && o.vues) S = o; }
  }catch(e){}
  if(!S.vues) S.vues = {};
  if(!S.series) S.series = [];
}
function ecrire(){
  S.maj = Date.now();
  try{ localStorage.setItem(CLE, JSON.stringify(S)); }catch(e){}
}
/* une question « vue » l'est pour toujours et pour tous les modes :
   l'historique ne dépend ni du mode ni des filtres employés ce jour-là */
function marquer(id, bon){
  var v = S.vues[id] || {n:0, ok:0, ko:0};
  v.n++; if(bon) v.ok++; else v.ko++;
  v.t = Date.now(); v.d = bon ? 1 : 0;
  S.vues[id] = v;
}
function vue(id){ return !!S.vues[id]; }
function ratee(id){ var v = S.vues[id]; return !!v && v.d === 0; }

/* ============================================================ sélection */
function filtrer(f){
  return Q.filter(function(q){
    if(f.ch && f.ch.length && f.ch.indexOf(String(q.ch)) < 0) return false;
    if(f.sp && f.sp.length && f.sp.indexOf(q.sp) < 0) return false;
    if(f.niv && f.niv.length && f.niv.indexOf(q.niv) < 0) return false;
    if(f.type && f.type.length && f.type.indexOf(q.type) < 0) return false;
    return true;
  });
}
function melanger(a){
  a = a.slice();
  for(var i = a.length - 1; i > 0; i--){
    var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
  }
  return a;
}
/* on équilibre la série sur les sous-parties : une série de vingt questions
   ne doit pas se concentrer sur un seul passage du cours */
function repartir(liste, n){
  var par = {}, cles = [];
  melanger(liste).forEach(function(q){
    if(!par[q.sp]){ par[q.sp] = []; cles.push(q.sp); }
    par[q.sp].push(q);
  });
  cles = melanger(cles);
  var out = [], reste = true;
  while(out.length < n && reste){
    reste = false;
    for(var i = 0; i < cles.length && out.length < n; i++){
      var l = par[cles[i]];
      if(l && l.length){ out.push(l.shift()); reste = true; }
    }
  }
  return out;
}
function choisir(f, n, mode){
  var base = filtrer(f);
  if(mode === 'erreurs'){
    var r = base.filter(function(q){ return ratee(q.id); });
    return {liste: repartir(r, n), inedites: r.length, total: base.length,
            voisines: proches(r, base, n)};
  }
  var ined = base.filter(function(q){ return !vue(q.id); });
  return {liste: repartir(ined, n), inedites: ined.length, total: base.length,
          deja: base.length - ined.length};
}
/* « Revoir mes erreurs » : on propose aussi d'autres questions portant sur la
   même sous-partie, pour vérifier que la notion est comprise et pas seulement
   la question mémorisée */
function proches(ratees, base, n){
  var sp = {}; ratees.forEach(function(q){ sp[q.sp] = 1; });
  var autres = base.filter(function(q){
    return sp[q.sp] && !ratee(q.id);
  });
  return repartir(autres, Math.max(0, Math.min(n, autres.length)));
}

/* ============================================================ rendu brut */
function esc(s){
  return String(s == null ? '' : s).replace(/[&<>"']/g, function(m){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m];
  });
}
function el(id){ return document.getElementById(id); }
function pg(){ return el('pg-quiz'); }

/* =========================================================== écran d'accueil */
var F = {mode:'entrainement', ch:[], sp:[], niv:[], type:[], n:15};

function compterPar(champ, f){
  var out = {}, base = filtrer(f);
  base.forEach(function(q){
    var k = String(q[champ]);
    if(!out[k]) out[k] = {n:0, ined:0};
    out[k].n++; if(!vue(q.id)) out[k].ined++;
  });
  return out;
}

function accueil(){
  var parCh = {};
  Q.forEach(function(q){
    var k = String(q.ch);
    if(!parCh[k]) parCh[k] = {n:0, ined:0, ok:0, vu:0};
    parCh[k].n++;
    var v = S.vues[q.id];
    if(v){ parCh[k].vu++; if(v.d === 1) parCh[k].ok++; } else parCh[k].ined++;
  });
  var tot = Q.length, vus = Object.keys(S.vues).length;
  var ratees = Q.filter(function(q){ return ratee(q.id); }).length;

  var h = '<div class="qz">';
  h += '<div class="qz-hero"><h1>Quiz</h1><p>Une banque de ' + tot +
       ' questions vérifiées sur les seize chapitres : définitions, auteurs, '
       + 'mécanismes, faits et chiffres. Chaque série est inédite tant qu’il '
       + 'reste des questions que vous n’avez pas vues.</p>'
       + '<div class="qz-stat"><b><i>' + tot + '</i> questions</b>'
       + '<b><i>' + (tot - vus) + '</i> inédites</b>'
       + '<b><i>' + vus + '</i> déjà vues</b>'
       + '<b><i>' + ratees + '</i> à revoir</b></div></div>';

  /* --- modes */
  var modes = [
    ['entrainement','🎯','Entraînement','Correction immédiate après chaque question, avec le raisonnement détaillé.'],
    ['examen','⏱️','Examen','Vous répondez d’abord, la correction complète arrive à la fin.'],
    ['erreurs','🔁','Revoir mes erreurs','Les questions ratées reviennent, accompagnées d’autres questions sur la même notion.'],
    ['transversal','🔗','Quiz transversal','Plusieurs chapitres mêlés, pour apprendre à relier les connaissances.']
  ];
  h += '<div class="qz-modes">';
  modes.forEach(function(m){
    h += '<button class="qz-mode' + (F.mode === m[0] ? ' on' : '') +
         '" data-mode="' + m[0] + '"><div class="qz-mi">' + m[1] + '</div>' +
         '<div class="qz-mt">' + m[2] + '</div><div class="qz-md">' + m[3] +
         '</div></button>';
  });
  h += '</div>';

  /* --- chapitres */
  h += '<div class="qz-card"><h3>Chapitres</h3><div class="qz-chips" id="qz-ch">';
  h += '<button class="qz-chip' + (!F.ch.length ? ' on' : '') + '" data-ch="">Tous</button>';
  ORDRE_CH.forEach(function(k){
    var c = parCh[k] || {n:0, ined:0};
    h += '<button class="qz-chip' + (F.ch.indexOf(k) >= 0 ? ' on' : '') +
         '" data-ch="' + k + '" title="' + esc(titreCh(k)) + '">' +
         esc(libCh(k)) + '<small>' + c.ined + '/' + c.n + '</small></button>';
  });
  h += '</div></div>';

  /* --- sous-parties : seulement quand un seul chapitre est choisi */
  if(F.ch.length === 1){
    var liste = SPS[F.ch[0]] || [];
    var cnt = compterPar('sp', {ch:F.ch});
    h += '<div class="qz-card"><h3>Sous-parties du chapitre</h3>' +
         '<div class="qz-chips" id="qz-sp">';
    h += '<button class="qz-chip' + (!F.sp.length ? ' on' : '') + '" data-sp="">Toutes</button>';
    liste.forEach(function(s){
      var c = cnt[s.cle] || {n:0, ined:0};
      if(!c.n) return;
      h += '<button class="qz-chip' + (F.sp.indexOf(s.cle) >= 0 ? ' on' : '') +
           '" data-sp="' + s.cle + '">' + esc(s.lib) +
           '<small>' + c.ined + '/' + c.n + '</small></button>';
    });
    h += '</div></div>';
  }

  /* --- niveaux et formats */
  h += '<div class="qz-card"><div class="qz-row">';
  h += '<div><div class="qz-lab">NIVEAU DE TRAVAIL</div><div class="qz-chips" id="qz-niv">';
  h += '<button class="qz-chip' + (!F.niv.length ? ' on' : '') + '" data-niv="">Tous</button>';
  var cn = compterPar('niv', {ch:F.ch, sp:F.sp});
  ['connaitre','comprendre','appliquer','raisonner'].forEach(function(n){
    var c = cn[n] || {n:0, ined:0};
    if(!c.n) return;
    h += '<button class="qz-chip' + (F.niv.indexOf(n) >= 0 ? ' on' : '') +
         '" data-niv="' + n + '">' + LIBN[n] + '<small>' + c.ined + '/' + c.n +
         '</small></button>';
  });
  h += '</div></div>';
  h += '<div><div class="qz-lab">FORMAT</div><div class="qz-chips" id="qz-type">';
  h += '<button class="qz-chip' + (!F.type.length ? ' on' : '') + '" data-type="">Tous</button>';
  var ct = compterPar('type', {ch:F.ch, sp:F.sp, niv:F.niv});
  ['qcm','qcmm','vf','assoc','ordre','courte'].forEach(function(t){
    var c = ct[t] || {n:0, ined:0};
    if(!c.n) return;
    h += '<button class="qz-chip' + (F.type.indexOf(t) >= 0 ? ' on' : '') +
         '" data-type="' + t + '">' + LIBT[t] + '<small>' + c.ined + '/' + c.n +
         '</small></button>';
  });
  h += '</div></div></div></div>';

  /* --- nombre de questions et lancement */
  var dispo = choisir(F, 999, F.mode);
  h += '<div class="qz-card"><div class="qz-row"><div>' +
       '<div class="qz-lab">NOMBRE DE QUESTIONS</div><div class="qz-chips" id="qz-n">';
  [10,15,20,30].forEach(function(n){
    h += '<button class="qz-chip' + (F.n === n ? ' on' : '') + '" data-n="' + n +
         '">' + n + '</button>';
  });
  h += '</div></div><div><div class="qz-lab">RÉSERVE DISPONIBLE</div>' +
       '<div class="qz-dispo" id="qz-dispo">' + texteDispo(dispo) + '</div>' +
       '</div></div><div class="qz-go" style="margin-top:18px">' +
       '<button class="qz-btn" id="qz-start">Commencer</button>' +
       (Object.keys(S.vues).length ?
        '<button class="qz-btn qz-sec" id="qz-prog">Ma progression</button>' +
        '<button class="qz-btn qz-sec" id="qz-raz">Réinitialiser l’historique</button>' : '') +
       '</div></div>';

  h += '</div>';
  pg().innerHTML = h;
  brancherAccueil();
}

function texteDispo(d){
  if(F.mode === 'erreurs'){
    return d.inedites ? '<b>' + d.inedites + '</b> question(s) ratée(s) à revoir'
      + (d.voisines && d.voisines.length ? ', et ' + d.voisines.length +
         ' question(s) voisine(s) sur les mêmes notions' : '')
      : 'aucune erreur enregistrée pour ces filtres';
  }
  return '<b>' + d.inedites + '</b> inédite(s) sur ' + d.total +
         ' question(s) correspondant à vos filtres';
}

function bascule(tab, val){
  if(!val){ tab.length = 0; return; }
  var i = tab.indexOf(val);
  if(i >= 0) tab.splice(i, 1); else tab.push(val);
}

function brancherAccueil(){
  var z = pg();
  z.querySelectorAll('[data-mode]').forEach(function(b){
    b.addEventListener('click', function(){
      F.mode = b.getAttribute('data-mode');
      if(F.mode === 'transversal' && F.ch.length === 1) F.ch = [];
      accueil();
    });
  });
  z.querySelectorAll('#qz-ch [data-ch]').forEach(function(b){
    b.addEventListener('click', function(){
      bascule(F.ch, b.getAttribute('data-ch'));
      F.sp = [];
      accueil();
    });
  });
  z.querySelectorAll('#qz-sp [data-sp]').forEach(function(b){
    b.addEventListener('click', function(){
      bascule(F.sp, b.getAttribute('data-sp')); accueil();
    });
  });
  z.querySelectorAll('#qz-niv [data-niv]').forEach(function(b){
    b.addEventListener('click', function(){
      bascule(F.niv, b.getAttribute('data-niv')); accueil();
    });
  });
  z.querySelectorAll('#qz-type [data-type]').forEach(function(b){
    b.addEventListener('click', function(){
      bascule(F.type, b.getAttribute('data-type')); accueil();
    });
  });
  z.querySelectorAll('#qz-n [data-n]').forEach(function(b){
    b.addEventListener('click', function(){
      F.n = Number(b.getAttribute('data-n')); accueil();
    });
  });
  var s = el('qz-start');
  if(s) s.addEventListener('click', demarrer);
  var p = el('qz-prog');
  if(p) p.addEventListener('click', progression);
  var r = el('qz-raz');
  if(r) r.addEventListener('click', function(){
    if(confirm('Effacer l’historique des questions vues, des réussites et des '
             + 'erreurs ? Cette action ne peut pas être annulée.')){
      S = {vues:{}, series:[], maj:0}; ecrire(); accueil();
    }
  });
}

/* ====================================================== lancement d'une série */
var P = null;   /* partie en cours */

function demarrer(){
  var d = choisir(F, F.n, F.mode);
  if(F.mode === 'erreurs'){
    if(!d.inedites){
      alert('Aucune question ratée ne correspond à ces filtres. '
          + 'Faites d’abord une série en Entraînement ou en Examen.');
      return;
    }
    var l = d.liste.slice();
    (d.voisines || []).forEach(function(q){
      if(l.length < F.n && l.indexOf(q) < 0) l.push(q);
    });
    return lancer(l);
  }
  if(d.inedites >= F.n) return lancer(d.liste.slice(0, F.n));
  /* réserve insuffisante : on ne recycle jamais en silence */
  dialogueReserve(d);
}

function dialogueReserve(d){
  var n = d.inedites;
  var h = '<div class="qz-dlg" id="qz-dlg"><div class="qz-in">' +
    '<h4>Il reste ' + n + ' question' + (n > 1 ? 's' : '') + ' inédite' +
    (n > 1 ? 's' : '') + ' pour ces filtres</h4>' +
    '<p>Vous en avez demandé ' + F.n + '. Les ' + (d.total - n) +
    ' autres questions correspondant à vos filtres ont déjà été vues, dans ce '
    + 'mode ou dans un autre. Que faire ?</p><div class="qz-ch">' +
    (n > 0 ? '<button class="qz-btn" data-ch="court">Faire une série de ' + n +
      ' question' + (n > 1 ? 's' : '') + '</button>' : '') +
    '<button class="qz-btn qz-sec" data-ch="large">Élargir les filtres</button>' +
    '<button class="qz-btn qz-sec" data-ch="repet">Accepter ' + (F.n - n) +
    ' question' + ((F.n - n) > 1 ? 's' : '') + ' déjà vue' +
    ((F.n - n) > 1 ? 's' : '') + '</button>' +
    '<button class="qz-btn qz-sec" data-ch="rien">Annuler</button>' +
    '</div></div></div>';
  var w = document.createElement('div');
  w.innerHTML = h;
  pg().appendChild(w.firstChild);
  el('qz-dlg').addEventListener('click', function(e){
    var b = e.target.closest('[data-ch]');
    if(!b){ if(e.target.id === 'qz-dlg') fermerDlg(); return; }
    var c = b.getAttribute('data-ch');
    fermerDlg();
    if(c === 'court') return lancer(d.liste.slice(0, n));
    if(c === 'large') return accueil();
    if(c === 'repet'){
      var base = filtrer(F);
      var deja = melanger(base.filter(function(q){ return vue(q.id); }));
      /* les plus anciennes d'abord, et les erreurs avant les réussites */
      deja.sort(function(a, b2){
        var va = S.vues[a.id], vb = S.vues[b2.id];
        return (va.d - vb.d) || ((va.t || 0) - (vb.t || 0));
      });
      var l = d.liste.slice(0, n);
      for(var i = 0; i < deja.length && l.length < F.n; i++){
        if(l.indexOf(deja[i]) < 0) l.push(deja[i]);
      }
      return lancer(melanger(l));
    }
  });
}
function fermerDlg(){ var d = el('qz-dlg'); if(d) d.remove(); }

function lancer(liste){
  if(!liste.length){ alert('Aucune question ne correspond à ces filtres.'); return; }
  P = {l:liste, i:0, rep:[], mode:F.mode, debut:Date.now()};
  question();
}

/* ======================================================== une question */
function question(){
  var q = P.l[P.i], n = P.l.length;
  var sp = (SPS[String(q.ch)] || []).filter(function(s){ return s.cle === q.sp; })[0];
  var h = '<div class="qz">';
  h += '<div class="qz-bar"><i style="width:' + Math.round(P.i / n * 100) + '%"></i></div>';
  h += '<div class="qz-top"><div class="qz-meta">' +
       '<span class="qz-tag">' + esc(libCh(q.ch)) + '</span>' +
       (sp ? '<span class="qz-tag">' + esc(sp.lib) + '</span>' : '') +
       '<span class="qz-tag n-' + q.niv + '">' + LIBN[q.niv] + '</span>' +
       '<span class="qz-tag">' + LIBT[q.type] + '</span></div>' +
       '<div class="qz-tag">' + (P.i + 1) + ' / ' + n + '</div></div>';
  h += '<div class="qz-q">' + esc(q.q) + '</div>';
  h += corps(q);
  h += '<div id="qz-corr"></div>';
  h += '<div class="qz-act" id="qz-act"></div></div>';
  pg().innerHTML = h;
  brancherQuestion(q);
  window.scrollTo({top:0, behavior:'smooth'});
}

var REP = null;   /* réponse en cours de saisie */

function corps(q){
  var h = '';
  if(q.type === 'qcm' || q.type === 'qcmm'){
    if(q.type === 'qcmm'){
      h += '<div class="qz-cons">Plusieurs réponses sont exactes — '
         + 'cochez-les toutes.</div>';
    }
    h += '<div class="qz-opts" id="qz-opts">';
    q.opts.forEach(function(o, i){
      h += '<button class="qz-opt" data-i="' + i + '">' +
           '<span class="qz-k">' + 'ABCDEF'[i] + '</span><span>' + esc(o) +
           '</span></button>';
    });
    h += '</div>';
  } else if(q.type === 'vf'){
    h += '<div class="qz-opts" id="qz-opts">' +
      '<button class="qz-opt" data-i="1"><span class="qz-k">V</span><span>Vrai</span></button>' +
      '<button class="qz-opt" data-i="0"><span class="qz-k">F</span><span>Faux</span></button>' +
      '</div><div class="qz-lab" style="margin:16px 0 7px">JUSTIFIEZ EN UNE '
      + 'PHRASE (facultatif, pour vous entraîner)</div>' +
      '<textarea class="qz-txt" id="qz-just" rows="2" placeholder="Parce que…"></textarea>';
  } else if(q.type === 'courte'){
    h += '<textarea class="qz-txt" id="qz-txt" placeholder="Rédigez votre '
       + 'réponse en quelques phrases…"></textarea>';
  } else if(q.type === 'ordre'){
    h += '<div class="qz-cons">Cliquez les étapes dans l’ordre du mécanisme.</div>';
    h += '<div class="qz-ordre" id="qz-opts">';
    melanger(q.ans.map(function(t, i){ return {t:t, i:i}; })).forEach(function(o){
      h += '<button class="qz-opt" data-i="' + o.i + '"><span class="qz-k"></span>' +
           '<span>' + esc(o.t) + '</span></button>';
    });
    h += '</div>';
  } else if(q.type === 'assoc'){
    var idees = melanger(q.ans.map(function(c){ return c[1]; }));
    h += '<div class="qz-assoc" id="qz-assoc">';
    q.ans.forEach(function(c, i){
      h += '<div class="qz-pair" data-i="' + i + '"><div class="qz-g">' +
           esc(c[0]) + '</div><select class="qz-sel" data-i="' + i + '">' +
           '<option value="">— choisir —</option>';
      idees.forEach(function(t){
        h += '<option value="' + esc(t) + '">' + esc(t) + '</option>';
      });
      h += '</select></div>';
    });
    h += '</div>';
  }
  return h;
}

function brancherQuestion(q){
  REP = (q.type === 'qcmm' || q.type === 'ordre') ? [] : null;
  var act = el('qz-act');
  act.innerHTML = '<button class="qz-btn" id="qz-val">Valider</button>' +
    '<button class="qz-btn qz-sec" id="qz-stop">Arrêter la série</button>';
  el('qz-val').addEventListener('click', function(){ valider(q); });
  el('qz-stop').addEventListener('click', function(){
    if(confirm('Arrêter la série et voir le bilan ?')) bilan();
  });

  var opts = el('qz-opts');
  if(opts){
    opts.addEventListener('click', function(e){
      var b = e.target.closest('.qz-opt');
      if(!b || b.disabled) return;
      var i = Number(b.getAttribute('data-i'));
      if(q.type === 'qcmm'){
        var k = REP.indexOf(i);
        if(k >= 0) REP.splice(k, 1); else REP.push(i);
        b.classList.toggle('sel');
      } else if(q.type === 'ordre'){
        if(REP.indexOf(i) >= 0) return;
        REP.push(i);
        b.classList.add('sel');
        b.querySelector('.qz-k').textContent = REP.length;
      } else {
        REP = i;
        opts.querySelectorAll('.qz-opt').forEach(function(x){
          x.classList.remove('sel');
        });
        b.classList.add('sel');
      }
    });
  }
  var as = el('qz-assoc');
  if(as){
    REP = {};
    as.addEventListener('change', function(e){
      var s = e.target;
      if(s.tagName === 'SELECT') REP[s.getAttribute('data-i')] = s.value;
    });
  }
  document.onkeydown = function(e){
    if(!P || el('qz-corr') === null) return;
    if(e.key === 'Enter' && !e.shiftKey){
      var v = el('qz-val'), s = el('qz-suite');
      if(s){ e.preventDefault(); s.click(); }
      else if(v && document.activeElement.tagName !== 'TEXTAREA'){
        e.preventDefault(); v.click();
      }
      return;
    }
    if(document.activeElement.tagName === 'TEXTAREA') return;
    var k = 'abcdef'.indexOf(String(e.key).toLowerCase());
    var o = el('qz-opts');
    if(k >= 0 && o){
      var b = o.querySelector('[data-i="' + k + '"]');
      if(b && !b.disabled) b.click();
    }
  };
}

/* ======================================================== validation */
function nzr(s){
  return String(s == null ? '' : s).toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[’‘]/g, "'").replace(/[^a-z0-9' ]/g, ' ')
    .replace(/\s+/g, ' ').trim();
}
function contient(txt, cle){
  var t = ' ' + nzr(txt) + ' ';
  var formes = [].concat(cle);
  for(var i = 0; i < formes.length; i++){
    if(t.indexOf(' ' + nzr(formes[i]) + ' ') >= 0) return true;
    if(nzr(formes[i]).length > 5 && t.indexOf(nzr(formes[i])) >= 0) return true;
  }
  return false;
}
function juger(q){
  if(q.type === 'qcm') return {bon: REP === q.ans, rep: REP};
  if(q.type === 'vf') return {bon: (REP === 1) === (q.ans === true), rep: REP};
  if(q.type === 'qcmm'){
    var a = (q.ans || []).slice().sort().join(','),
        r = (REP || []).slice().sort().join(',');
    return {bon: a === r && r !== '', rep: REP};
  }
  if(q.type === 'ordre'){
    var ok = REP && REP.length === q.ans.length;
    if(ok) for(var i = 0; i < REP.length; i++) if(REP[i] !== i) ok = false;
    return {bon: !!ok, rep: REP};
  }
  if(q.type === 'assoc'){
    var n = 0;
    q.ans.forEach(function(c, i){ if((REP || {})[i] === c[1]) n++; });
    return {bon: n === q.ans.length, rep: REP, n:n};
  }
  if(q.type === 'courte'){
    var t = (el('qz-txt') || {}).value || '';
    var cles = (q.ans && q.ans.cles) || [];
    var trouves = [], manquants = [];
    cles.forEach(function(c){
      (contient(t, c.f || c) ? trouves : manquants).push(c.l || [].concat(c.f || c)[0]);
    });
    var seuil = Math.max(1, Math.ceil(cles.length * 0.6));
    return {bon: cles.length ? trouves.length >= seuil : t.trim().length > 40,
            rep: t, trouves: trouves, manquants: manquants};
  }
  return {bon:false};
}

function valider(q){
  if(REP === null || (Array.isArray(REP) && !REP.length) ||
     (q.type === 'courte' && !((el('qz-txt') || {}).value || '').trim())){
    if(!confirm('Vous n’avez pas répondu. Passer à la correction ?')) return;
  }
  var j = juger(q);
  P.rep.push({id:q.id, bon:j.bon, q:q, j:j});
  marquer(q.id, j.bon);
  ecrire();
  /* on fige l'énoncé : plus aucune modification possible */
  var opts = el('qz-opts');
  if(opts) opts.querySelectorAll('.qz-opt').forEach(function(b){ b.disabled = true; });
  var as = el('qz-assoc');
  if(as) as.querySelectorAll('select').forEach(function(s){ s.disabled = true; });
  var t = el('qz-txt'); if(t) t.disabled = true;
  var ju = el('qz-just'); if(ju) ju.disabled = true;

  if(P.mode === 'examen'){
    el('qz-act').innerHTML = '<button class="qz-btn" id="qz-suite">' +
      (P.i + 1 < P.l.length ? 'Question suivante' : 'Voir la correction') +
      '</button>';
    el('qz-suite').addEventListener('click', suite);
    return;
  }
  marquerOptions(q, j);
  el('qz-corr').innerHTML = correction(q, j);
  brancherCorr();
  el('qz-act').innerHTML = '<button class="qz-btn" id="qz-suite">' +
    (P.i + 1 < P.l.length ? 'Question suivante' : 'Voir le bilan') + '</button>';
  el('qz-suite').addEventListener('click', suite);
}

function marquerOptions(q, j){
  var opts = el('qz-opts');
  if(opts && (q.type === 'qcm' || q.type === 'qcmm' || q.type === 'vf')){
    var bons = q.type === 'qcm' ? [q.ans]
             : q.type === 'qcmm' ? q.ans : [q.ans === true ? 1 : 0];
    opts.querySelectorAll('.qz-opt').forEach(function(b){
      var i = Number(b.getAttribute('data-i'));
      b.classList.remove('sel');
      if(bons.indexOf(i) >= 0) b.classList.add('ok');
      else if(q.type === 'qcmm' ? (j.rep || []).indexOf(i) >= 0 : j.rep === i)
        b.classList.add('ko');
    });
  }
  if(opts && q.type === 'ordre'){
    opts.querySelectorAll('.qz-opt').forEach(function(b){
      var i = Number(b.getAttribute('data-i'));
      var rang = (j.rep || []).indexOf(i);
      b.classList.remove('sel');
      b.classList.add(rang === i ? 'ok' : 'ko');
      b.querySelector('.qz-k').textContent = i + 1;
    });
  }
  var as = el('qz-assoc');
  if(as){
    as.querySelectorAll('.qz-pair').forEach(function(p){
      var i = Number(p.getAttribute('data-i'));
      p.classList.add((j.rep || {})[i] === q.ans[i][1] ? 'ok' : 'ko');
    });
  }
}

function suite(){
  if(P.i + 1 < P.l.length){ P.i++; question(); }
  else bilan();
}

/* ======================================================== la correction */
function correction(q, j){
  var h = '<div class="qz-corr ' + (j.bon ? 'bon' : 'mauvais') + '">';
  h += '<div class="qz-head">' + (j.bon ? '✓ Bonne réponse' : '✗ Réponse inexacte') +
       (q.type === 'assoc' && j.n != null ?
        ' — ' + j.n + ' association(s) juste(s) sur ' + q.ans.length : '') +
       '</div><div class="qz-body">';

  if(q.type === 'qcm' || q.type === 'qcmm'){
    var bons = q.type === 'qcm' ? [q.ans] : q.ans;
    h += '<p><b>Réponse : ' + bons.map(function(i){ return 'ABCDEF'[i]; }).join(' et ') +
         '.</b> ' + esc(q.exp) + '</p>';
    if(q.why && q.why.length){
      h += '<div class="qz-sous">Pourquoi les autres propositions sont fausses</div><ul>';
      q.opts.forEach(function(o, i){
        if(q.type === 'qcm' && i === q.ans) return;
        var k = q.type === 'qcm' ? (i < q.ans ? i : i - 1) : i;
        var t = q.why[k];
        if(!t) return;
        if(q.type === 'qcmm' && bons.indexOf(i) >= 0){
          h += '<li><b>' + 'ABCDEF'[i] + ' — exacte.</b> ' + esc(t) + '</li>';
        } else {
          h += '<li><b>' + 'ABCDEF'[i] + '.</b> ' + esc(t) + '</li>';
        }
      });
      h += '</ul>';
    }
  } else if(q.type === 'vf'){
    h += '<p><b>' + (q.ans ? 'Vrai.' : 'Faux.') + '</b> ' + esc(q.exp) + '</p>';
    var ju = (el('qz-just') || {}).value;
    if(ju && ju.trim()) h += '<p class="qz-t3"><i>Votre justification : ' +
      esc(ju.trim()) + '</i></p>';
  } else if(q.type === 'ordre'){
    h += '<div class="qz-sous">L’enchaînement, étape par étape</div><ul>';
    q.ans.forEach(function(t, i){
      h += '<li><b>' + (i + 1) + '.</b> ' + esc(t) + '</li>';
    });
    h += '</ul><p>' + esc(q.exp) + '</p>';
  } else if(q.type === 'assoc'){
    h += '<ul>';
    q.ans.forEach(function(c){
      h += '<li><b>' + esc(c[0]) + '</b> — ' + esc(c[1]) + '</li>';
    });
    h += '</ul><p>' + esc(q.exp) + '</p>';
  } else if(q.type === 'courte'){
    if(j.trouves && j.trouves.length){
      h += '<div class="qz-sous">Ce que votre réponse contient</div><ul>' +
        j.trouves.map(function(t){ return '<li>' + esc(t) + '</li>'; }).join('') +
        '</ul>';
    }
    if(j.manquants && j.manquants.length){
      h += '<div class="qz-sous">Ce qui manque</div><ul>' +
        j.manquants.map(function(t){ return '<li>' + esc(t) + '</li>'; }).join('') +
        '</ul>';
    }
    h += '<div class="qz-sous">Réponse attendue</div><p>' +
         esc((q.ans && q.ans.modele) || q.exp) + '</p>';
    if(q.ans && q.ans.modele && q.exp && q.exp !== q.ans.modele)
      h += '<p>' + esc(q.exp) + '</p>';
  }

  if(q.diss){
    h += '<div class="qz-diss"><div class="qz-sous">Comment l’utiliser en '
       + 'dissertation</div><p style="margin:0">' + esc(q.diss) + '</p></div>';
  }
  if(q.b != null && q.b >= 0){
    h += '<div><button class="qz-src" data-ch="' + q.ch + '" data-b="' + q.b +
         '">📖 Ouvrir le passage du cours' +
         (q.src ? ' — ' + esc(q.src) : '') + '</button></div>';
  }
  h += '</div></div>';
  return h;
}

function brancherCorr(){
  pg().querySelectorAll('.qz-src').forEach(function(b){
    if(b.__q) return;
    b.__q = 1;
    b.addEventListener('click', function(){
      var ch = b.getAttribute('data-ch'), bl = Number(b.getAttribute('data-b'));
      try{
        if(window.__ECO_RECHERCHE && window.__ECO_RECHERCHE.ouvrir){
          window.__ECO_RECHERCHE.ouvrir(['ch', String(ch), bl]);
          return;
        }
      }catch(e){}
      try{ openCh(Number(ch)); }catch(e){}
    });
  });
}

/* ============================================================== bilan */
function bilan(){
  document.onkeydown = null;
  var n = P.rep.length, bons = P.rep.filter(function(r){ return r.bon; }).length;
  var pct = n ? Math.round(bons / n * 100) : 0;
  var coul = pct >= 75 ? 'var(--qz-ok)' : pct >= 50 ? 'var(--qz-ac2)' : 'var(--qz-ko)';
  S.series.push({t:Date.now(), n:n, ok:bons, mode:P.mode,
                 ch:F.ch.slice(), min:Math.round((Date.now() - P.debut) / 60000)});
  if(S.series.length > 60) S.series = S.series.slice(-60);
  ecrire();

  var parSp = {};
  P.rep.forEach(function(r){
    var k = r.q.sp;
    if(!parSp[k]) parSp[k] = {n:0, ok:0, ch:r.q.ch, b:r.q.b};
    parSp[k].n++; if(r.bon) parSp[k].ok++;
  });
  var maitrise = [], revoir = [];
  Object.keys(parSp).forEach(function(k){
    var o = parSp[k], p = Math.round(o.ok / o.n * 100);
    var lib = (SPS[String(o.ch)] || []).filter(function(s){ return s.cle === k; })[0];
    var item = {lib: lib ? lib.lib : k, ch:o.ch, p:p, n:o.n, ok:o.ok, b:o.b};
    (p >= 70 ? maitrise : revoir).push(item);
  });
  revoir.sort(function(a, b){ return a.p - b.p; });

  var h = '<div class="qz"><div class="qz-hero"><h1>Bilan de la série</h1>' +
    '<p>' + (P.mode === 'examen' ? 'Mode examen — voici la correction complète, '
      + 'question par question.' : 'Ce que vous maîtrisez, ce qu’il faut revoir, '
      + 'et les passages du cours à rouvrir.') + '</p></div>';
  h += '<div class="qz-score"><div class="qz-donut" style="background:conic-gradient('
    + coul + ' ' + (pct * 3.6) + 'deg,var(--qz-s2) 0)"><span>' + pct + '%</span></div>' +
    '<div><div style="font-size:1.25rem;font-weight:800">' + bons + ' / ' + n +
    ' bonne' + (bons > 1 ? 's' : '') + ' réponse' + (bons > 1 ? 's' : '') + '</div>' +
    '<div class="qz-dispo" style="margin-top:6px">Historique : <b>' +
    Object.keys(S.vues).length + '</b> question(s) vue(s) sur ' + Q.length +
    ' — il reste <b>' + (Q.length - Object.keys(S.vues).length) + '</b> inédites.</div>' +
    '</div></div>';

  h += '<div class="qz-rec">';
  h += '<div class="qz-card"><h3>Ce que vous maîtrisez</h3>' +
    (maitrise.length ? maitrise.map(function(x){
      return '<div class="qz-li"><b>' + esc(x.lib) + '</b><span class="qz-pct bon">' +
        x.ok + '/' + x.n + '</span></div>';
    }).join('') : '<div class="qz-dispo">Rien de consolidé dans cette série.</div>') +
    '</div>';
  h += '<div class="qz-card"><h3>À revoir en priorité</h3>' +
    (revoir.length ? revoir.map(function(x){
      return '<div class="qz-li"><b>' + esc(x.lib) + '</b>' +
        '<span class="qz-pct ' + (x.p >= 50 ? 'moy' : 'bas') + '">' + x.ok + '/' +
        x.n + '</span></div>' +
        '<button class="qz-src" data-ch="' + x.ch + '" data-b="' + x.b +
        '">📖 Rouvrir ce passage</button>';
    }).join('') : '<div class="qz-dispo">Aucune faiblesse dans cette série.</div>') +
    '</div></div>';

  if(P.mode === 'examen'){
    h += '<div class="qz-card" style="margin-top:18px"><h3>Correction détaillée</h3>';
    P.rep.forEach(function(r, i){
      h += '<div style="margin:18px 0 6px;font-weight:800">' + (i + 1) + '. ' +
        esc(r.q.q) + '</div>' + correction(r.q, r.j);
    });
    h += '</div>';
  }

  h += '<div class="qz-go" style="margin-top:22px">' +
    '<button class="qz-btn" id="qz-encore">Nouvelle série inédite</button>' +
    '<button class="qz-btn qz-sec" id="qz-err">Revoir mes erreurs</button>' +
    '<button class="qz-btn qz-sec" id="qz-home">Retour aux réglages</button></div></div>';
  pg().innerHTML = h;
  brancherCorr();
  el('qz-encore').addEventListener('click', demarrer);
  el('qz-err').addEventListener('click', function(){ F.mode = 'erreurs'; demarrer(); });
  el('qz-home').addEventListener('click', accueil);
  window.scrollTo({top:0, behavior:'smooth'});
}

/* ======================================================== progression */
function progression(){
  var h = '<div class="qz"><div class="qz-hero"><h1>Ma progression</h1>' +
    '<p>Ce que l’historique retient, chapitre par chapitre. Il est conservé '
    + 'dans ce navigateur et survit à la fermeture de l’application.</p></div>';
  h += '<div class="qz-card"><h3>Par chapitre</h3>';
  ORDRE_CH.forEach(function(k){
    var qs = Q.filter(function(q){ return String(q.ch) === k; });
    if(!qs.length) return;
    var vus = qs.filter(function(q){ return vue(q.id); });
    var ok = vus.filter(function(q){ return S.vues[q.id].d === 1; }).length;
    var p = vus.length ? Math.round(ok / vus.length * 100) : 0;
    h += '<div class="qz-li"><b>' + esc(libCh(k)) + '</b><span>' +
      vus.length + '/' + qs.length + ' vues' +
      (vus.length ? ' · <span class="qz-pct ' +
        (p >= 70 ? 'bon' : p >= 50 ? 'moy' : 'bas') + '">' + p + '% de réussite</span>'
        : '') + '</span></div>';
  });
  h += '</div>';
  var s = S.series.slice(-10).reverse();
  if(s.length){
    h += '<div class="qz-card"><h3>Dernières séries</h3>' + s.map(function(x){
      var d = new Date(x.t);
      return '<div class="qz-li"><b>' + d.toLocaleDateString('fr-FR') + ' · ' +
        (LIBMODE[x.mode] || x.mode) + '</b><span class="qz-pct ' +
        (x.ok / x.n >= .7 ? 'bon' : x.ok / x.n >= .5 ? 'moy' : 'bas') + '">' +
        x.ok + '/' + x.n + '</span></div>';
    }).join('') + '</div>';
  }
  h += '<div class="qz-go" style="margin-top:20px">' +
    '<button class="qz-btn" id="qz-home">Retour aux réglages</button></div></div>';
  pg().innerHTML = h;
  el('qz-home').addEventListener('click', accueil);
}
var LIBMODE = {entrainement:'Entraînement', examen:'Examen',
               erreurs:'Révision des erreurs', transversal:'Transversal'};

/* ============================================================ démarrage */
function installer(){
  if(!pg()) return;
  lire();
  accueil();
}
if(typeof window.showPg === 'function'){
  var _s = window.showPg;
  window.showPg = function(id){
    var r = _s.apply(this, arguments);
    if(String(id).indexOf('quiz') >= 0){
      try{ if(!P) accueil(); }catch(e){}
    }
    return r;
  };
}
if(document.readyState === 'loading'){
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(installer, 900); });
} else {
  setTimeout(installer, 900);
}

window.__ECO_QUIZ = {banque:Q, sousparties:SPS, etat:function(){ return S; },
  filtrer:filtrer, choisir:choisir, lancer:lancer, accueil:accueil,
  demarrer:demarrer, F:F, rejouer:function(){ return P; },
  oublier:function(){ S = {vues:{}, series:[], maj:0}; ecrire(); }};
})();
