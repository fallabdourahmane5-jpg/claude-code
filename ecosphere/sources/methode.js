/* =======================================================================
   Méthode Dissertation — v226
   Deux ajouts à la section existante :
     · une grille d'autoévaluation interactive, reprise de la fiche de cours ;
     · un exemple fil rouge entièrement rédigé et annoté, « Faut-il toujours
       défendre le libre-échange ? », lisible comme une copie ou avec ses
       annotations.
   Couche additive : on n'écrase rien, on ajoute deux cartes à #methodGrid.
   ======================================================================= */
(function(){
if(window.__ECO_METHODE_V226) return;
window.__ECO_METHODE_V226 = true;

/* __PAYLOAD__ */

var G = MT.grille, P = MT.pieces, PLAN = MT.plan;
var CLE = 'eco-autoeval-v226';

function esc(s){
  return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
  });
}

/* mise en forme de la copie : [[u:…]] = souligné (titre d'ouvrage) */
function forme(h){
  return h.replace(/\[\[u:(.*?)\]\]/g, '<u>$1</u>');
}

/* ------------------------------------------------------- mémorisation */
var ETAT = {};
try{ ETAT = JSON.parse(localStorage.getItem(CLE) || '{}') || {}; }catch(e){ ETAT = {}; }
function garder(){
  try{ localStorage.setItem(CLE, JSON.stringify(ETAT)); }catch(e){}
}

function critere(id){
  for(var i = 0; i < G.length; i++)
    for(var j = 0; j < G[i].items.length; j++)
      if(G[i].items[j].id === id) return G[i].items[j];
  return null;
}

/* ============================================================== grille */
var LIB = {ok: 'Réussi', ko: 'Raté', ab: 'Absent', na: 'Non concerné'};
var CLASSE = {ok: 'fait', ko: 'corr', ab: 'oubli', na: ''};

function compte(){
  var n = 0, ok = 0, ko = 0, ab = 0, na = 0;
  G.forEach(function(g){ g.items.forEach(function(c){
    n++;
    var v = ETAT[c.id];
    if(v === 'ok') ok++; else if(v === 'ko') ko++;
    else if(v === 'ab') ab++; else if(v === 'na') na++;
  }); });
  return {n: n, ok: ok, ko: ko, ab: ab, na: na,
          rep: ok + ko + ab + na, pris: n - na};
}

function barreHTML(){
  var c = compte(), t = Math.max(1, c.pris);
  return '<div class="mt-barre">' +
    '<div class="mt-jauge">' +
      '<i class="j-ok" style="width:' + (c.ok / t * 100) + '%"></i>' +
      '<i class="j-ko" style="width:' + ((c.ok + c.ko) / t * 100) + '%;' +
        'z-index:-1"></i>' +
      '<i class="j-ab" style="width:' + ((c.ok + c.ko + c.ab) / t * 100) +
        '%;z-index:-2"></i>' +
    '</div>' +
    '<span class="mt-cpt">' + c.ok + ' réussi' + (c.ok > 1 ? 's' : '') +
      ' <em>· ' + c.ko + ' à corriger · ' + c.ab + ' oublié' +
      (c.ab > 1 ? 's' : '') + ' · ' + c.rep + '/' + c.n + ' renseignés</em>' +
    '</span>' +
    '<button class="mt-btn" data-raz="1">Repartir de zéro</button>' +
    '<button class="mt-btn" data-aides="1">Afficher toutes les aides</button>' +
    '</div>';
}

function grilleHTML(){
  var h = '<div class="mt-top"><div><p>Relisez votre copie une ligne à la ' +
    'fois et choisissez un statut par critère. <b>Réussi</b> = maîtrisé ; ' +
    '<b>Raté</b> = présent mais à corriger ; <b>Absent</b> = oublié. Le ' +
    'critère sur le graphique peut être déclaré non concerné si vous n’en ' +
    'avez tracé aucun. Vos réponses sont conservées sur cet appareil.</p>' +
    '</div></div>';
  h += '<div id="mt-barre">' + barreHTML() + '</div>';
  h += G.map(function(g){
    var faits = g.items.filter(function(c){ return ETAT[c.id] === 'ok'; }).length;
    return '<section class="mt-grp">' +
      '<h3>' + esc(g.t) + '<small>' + faits + '/' + g.items.length +
        ' réussis</small></h3>' +
      (g.intro ? '<p>' + esc(g.intro) + '</p>' : '') +
      g.items.map(function(c){
        var v = ETAT[c.id] || '';
        var st = ['ok', 'ko', 'ab'].concat(c.na ? ['na'] : []);
        return '<div class="mt-crit ' + (CLASSE[v] || '') + '" ' +
          'id="mt-c-' + c.id + '" data-c="' + c.id + '">' +
          '<div class="mt-lib"><b>' + esc(c.t) + '</b>' +
            '<div class="mt-outils">' +
              (c.aide ? '<button class="mt-mini" data-aide="' + c.id +
                '">Comment le juger</button>' : '') +
              (c.ex ? '<button class="mt-mini" data-ex="' + c.ex[0] + '" ' +
                'data-k="' + esc(c.ex[1] || '') + '" data-c2="' + c.id +
                '">Voir dans l’exemple →</button>' : '') +
            '</div>' +
          '</div>' +
          '<div class="mt-statuts">' + st.map(function(s){
            return '<button class="mt-st' + (v === s ? ' on' : '') +
              '" data-v="' + s + '" data-id="' + c.id + '">' + LIB[s] +
              '</button>';
          }).join('') + '</div>' +
          (c.aide ? '<p class="mt-aide">' + esc(c.aide) + '</p>' : '') +
          '</div>';
      }).join('') + '</section>';
  }).join('');
  return '<div class="mt">' + h + '</div>';
}

function majGrille(){
  var z = document.getElementById('mt-grille');
  if(!z) return;
  z.innerHTML = grilleHTML();
  brancherGrille(z);
}

function brancherGrille(z){
  z.querySelectorAll('.mt-st').forEach(function(b){
    b.addEventListener('click', function(){
      var id = b.getAttribute('data-id'), v = b.getAttribute('data-v');
      if(ETAT[id] === v) delete ETAT[id]; else ETAT[id] = v;
      garder();
      majGrille();
      var e = document.getElementById('mt-c-' + id);
      if(e) e.scrollIntoView({block: 'nearest'});
    });
  });
  z.querySelectorAll('[data-aide]').forEach(function(b){
    b.addEventListener('click', function(){
      var e = document.getElementById('mt-c-' + b.getAttribute('data-aide'));
      if(e) e.classList.toggle('aide');
    });
  });
  z.querySelectorAll('[data-raz]').forEach(function(b){
    b.addEventListener('click', function(){
      ETAT = {}; garder(); majGrille();
    });
  });
  z.querySelectorAll('[data-aides]').forEach(function(b){
    b.addEventListener('click', function(){
      var tout = z.querySelectorAll('.mt-crit.aide').length <
                 z.querySelectorAll('.mt-crit').length;
      z.querySelectorAll('.mt-crit').forEach(function(c){
        c.classList.toggle('aide', tout);
      });
    });
  });
  z.querySelectorAll('[data-ex]').forEach(function(b){
    b.addEventListener('click', function(){
      viser(b.getAttribute('data-ex'), b.getAttribute('data-k'),
            b.getAttribute('data-c2'));
    });
  });
}

/* ====================================================== pièces rédigées */
var MODE = {};   /* id de pièce → 'copie' | 'annote' */

function morceaux(txt, notes, base){
  /* découpe le texte en segments, en marquant chaque extrait annoté */
  var bornes = [];
  (notes || []).forEach(function(n, i){
    var a = txt.indexOf(n.e);
    if(a < 0) return;
    bornes.push({a: a, b: a + n.e.length, i: i});
  });
  bornes.sort(function(x, y){ return x.a - y.a; });
  /* on écarte les chevauchements : le premier annoté l'emporte */
  var gardees = [], fin = -1;
  bornes.forEach(function(s){ if(s.a >= fin){ gardees.push(s); fin = s.b; } });
  var out = '', pos = 0;
  gardees.forEach(function(s){
    out += forme(esc(txt.slice(pos, s.a)));
    var no = base + s.i + 1;
    out += '<span class="mt-mark" data-n="' + no + '">' +
           forme(esc(txt.slice(s.a, s.b))) +
           '<span class="mt-num">' + no + '</span></span>';
    pos = s.b;
  });
  out += forme(esc(txt.slice(pos)));
  return out;
}

function pieceHTML(p){
  var mode = MODE[p.id] || 'copie';
  var annote = mode === 'annote';
  var h = '<article class="mt-piece' + (annote ? ' annote' : '') +
    '" id="mt-p-' + p.id + '">';
  h += '<div class="mt-ph"><h3>' + esc(p.t) + '</h3><p>' + esc(p.st) + '</p>' +
    (p.meta ? '<span class="mt-meta">' + esc(p.meta) + '</span>' : '') +
    '</div>';
  h += '<div class="mt-modes">' +
    '<button class="mt-btn' + (annote ? '' : ' on') + '" data-mode="copie" ' +
      'data-p="' + p.id + '">Lire comme une copie</button>' +
    '<button class="mt-btn' + (annote ? ' on' : '') + '" data-mode="annote" ' +
      'data-p="' + p.id + '">Voir les annotations</button>' +
    '</div>';
  h += '<div class="mt-corps">';
  if(annote && p.chapeau) h += '<p class="mt-chapeau">' + esc(p.chapeau) + '</p>';

  var num = 0, notes = [];
  h += '<div class="mt-copie">';
  p.paras.forEach(function(pa){
    var cls = 'mt-p';
    if(pa.iso) cls += ' iso';
    if(pa.r === 'Titre de la partie' || pa.r === 'Titre de la sous-partie')
      cls += ' titre';
    if(pa.r === 'Fin de la partie I' || pa.r === 'Début de la partie II')
      cls += ' ctx';
    var corps;
    if(annote && pa.n && pa.n.length){
      var base = num;
      /* on numérote dans l'ordre de lecture du paragraphe, pas dans
         l'ordre de rédaction des annotations */
      var ord = pa.n.slice().sort(function(a, b){
        return pa.txt.indexOf(a.e) - pa.txt.indexOf(b.e);
      });
      ord.forEach(function(n){
        num++;
        notes.push({i: num, k: n.k, e: n.e, x: n.x});
      });
      corps = morceaux(pa.txt, ord, base);
    } else {
      corps = forme(esc(pa.txt));
    }
    h += '<p class="' + cls + '">' +
      (annote && pa.r ? '<span class="mt-role">' + esc(pa.r) + '</span>' : '') +
      corps + '</p>';
  });
  h += '</div>';

  if(annote){
    if(notes.length){
      h += '<div class="mt-notes"><h4>Annotations — où et comment chaque ' +
        'critère est respecté</h4>' + notes.map(function(n){
        var c = critere(n.k);
        return '<div class="mt-note" id="mt-n-' + p.id + '-' + n.i + '" ' +
          'data-n="' + n.i + '" data-k="' + n.k + '">' +
          '<i>' + n.i + '</i><div>' +
          '<span class="mt-k">' + esc(c ? c.t : n.k) + '</span>' +
          '<blockquote>' + forme(esc(n.e)) + '</blockquote>' +
          '<p>' + esc(n.x) + '</p></div></div>';
      }).join('') + '</div>';
    }
    if(p.globaux && p.globaux.length){
      h += '<div class="mt-notes"><h4>Critères qui se jugent sur la copie ' +
        'entière</h4>' + p.globaux.map(function(n){
        var c = critere(n.k);
        return '<div class="mt-note glob" data-k="' + n.k + '">' +
          '<i>↻</i><div><span class="mt-k">' + esc(c ? c.t : n.k) +
          '</span><p>' + esc(n.x) + '</p></div></div>';
      }).join('') + '</div>';
    }
  }
  h += '</div></article>';
  return h;
}

function planHTML(){
  var annote = (MODE.plan || 'copie') === 'annote';
  var h = '<article class="mt-piece' + (annote ? ' annote' : '') +
    '" id="mt-p-plan">';
  h += '<div class="mt-ph"><h3>Plan détaillé</h3><p>Trois parties de trois ' +
    'sous-parties. Les titres sont écrits tels qu’ils figureraient sur la ' +
    'copie.</p><span class="mt-meta">' + esc(PLAN.chapeau) + '</span></div>';
  h += '<div class="mt-modes">' +
    '<button class="mt-btn' + (annote ? '' : ' on') + '" data-mode="copie" ' +
      'data-p="plan">Lire comme une copie</button>' +
    '<button class="mt-btn' + (annote ? ' on' : '') + '" data-mode="annote" ' +
      'data-p="plan">Voir les annotations</button>' +
    '</div><div class="mt-corps">';
  h += '<p class="mt-chapeau"><b>Problématique rappelée :</b> ' +
    esc(PLAN.pb) + '</p>';
  h += '<div class="mt-plan">' + PLAN.parties.map(function(pt){
    return '<div class="mt-pt"><b><i>' + esc(pt.num) + '.</i>' +
      esc(pt.titre) + '</b>' +
      '<p class="mt-pq">Pourquoi ce titre : ' + esc(pt.pourquoi) + '</p>' +
      pt.sp.map(function(s){
        return '<div class="mt-sp"><b>' + esc(s[0]) + '.</b>' + esc(s[1]) +
          (annote ? '<span>' + esc(s[2]) + '</span>' : '') + '</div>';
      }).join('') + '</div>';
  }).join('') + '</div>';
  if(annote && PLAN.notes && PLAN.notes.length){
    h += '<div class="mt-notes"><h4>Annotations</h4>' +
      PLAN.notes.map(function(n){
        var c = critere(n.k);
        return '<div class="mt-note glob" data-k="' + n.k + '">' +
          '<i>↻</i><div><span class="mt-k">' + esc(c ? c.t : n.k) +
          '</span><p>' + esc(n.x) + '</p></div></div>';
      }).join('') + '</div>';
  }
  h += '</div></article>';
  return h;
}

function filHTML(){
  var h = '<div class="mt">';
  h += '<div class="mt-sujet"><b>Sujet du fil rouge</b><span>' +
    esc(PLAN.sujetLibelle) + '</span></div>';
  h += '<div class="mt-top"><div><p>Le même sujet est traité du premier mot ' +
    'de l’accroche à la dernière phrase de l’ouverture, avec les références ' +
    'des cours d’ÉcoSphère. Chaque pièce se lit d’abord comme une copie, ' +
    'puis annotée : en mode annoté, chaque passage surligné renvoie au ' +
    'critère de la grille qu’il respecte, avec l’explication de la raison.' +
    '</p></div></div>';
  h += pieceHTML(P[0]);
  h += planHTML();
  h += P.slice(1).map(pieceHTML).join('');
  h += '</div>';
  return h;
}

function majFil(){
  var z = document.getElementById('mt-fil');
  if(!z) return;
  z.innerHTML = filHTML();
  brancherFil(z);
}

function brancherFil(z){
  z.querySelectorAll('[data-mode]').forEach(function(b){
    b.addEventListener('click', function(){
      MODE[b.getAttribute('data-p')] = b.getAttribute('data-mode');
      var y = b.getBoundingClientRect().top;
      majFil();
      var n = document.querySelector('[data-p="' + b.getAttribute('data-p') +
        '"][data-mode="' + b.getAttribute('data-mode') + '"]');
      if(n) window.scrollBy(0, n.getBoundingClientRect().top - y);
    });
  });
  z.querySelectorAll('.mt-mark').forEach(function(m){
    m.addEventListener('click', function(){
      var p = m.closest('.mt-piece');
      var n = p && p.querySelector('.mt-note[data-n="' +
        m.getAttribute('data-n') + '"]');
      if(n){ souligner(m, n); n.scrollIntoView({behavior: 'smooth', block: 'center'}); }
    });
    m.addEventListener('mouseenter', function(){
      var p = m.closest('.mt-piece');
      var n = p && p.querySelector('.mt-note[data-n="' +
        m.getAttribute('data-n') + '"]');
      if(n) n.classList.add('vif');
    });
    m.addEventListener('mouseleave', function(){
      z.querySelectorAll('.mt-note.vif').forEach(function(n){
        n.classList.remove('vif');
      });
    });
  });
  z.querySelectorAll('.mt-note[data-n]').forEach(function(n){
    n.addEventListener('click', function(){
      var p = n.closest('.mt-piece');
      var m = p && p.querySelector('.mt-mark[data-n="' +
        n.getAttribute('data-n') + '"]');
      if(m){ souligner(m, n); m.scrollIntoView({behavior: 'smooth', block: 'center'}); }
    });
  });
}

function souligner(m, n){
  var z = document.getElementById('mt-fil');
  if(z){
    z.querySelectorAll('.mt-mark.vif').forEach(function(x){ x.classList.remove('vif'); });
    z.querySelectorAll('.mt-note.vif').forEach(function(x){ x.classList.remove('vif'); });
  }
  if(m) m.classList.add('vif');
  if(n) n.classList.add('vif');
}

/* un critère de la grille → le passage exact dans l'exemple */
function viser(pid, cle, crit){
  var carte = document.getElementById('method-eco-fil');
  if(carte) carte.classList.add('open');
  MODE[pid] = 'annote';
  majFil();
  setTimeout(function(){
    var p = document.getElementById('mt-p-' + pid);
    if(!p) return;
    var n = null;
    if(cle) n = p.querySelector('.mt-note[data-k="' + cle + '"]');
    if(!n && crit) n = p.querySelector('.mt-note[data-k="' + crit + '"]');
    if(!n) n = p;
    var m = n.getAttribute && n.getAttribute('data-n') ?
      p.querySelector('.mt-mark[data-n="' + n.getAttribute('data-n') + '"]') : null;
    souligner(m, n.classList && n.classList.contains('mt-note') ? n : null);
    n.scrollIntoView({behavior: 'smooth', block: 'center'});
  }, 60);
}

/* ============================================= insertion dans la page */
function carte(id, num, icone, titre, corps){
  return '<article class="method-card open" id="method-' + id + '">' +
    '<div class="method-head" data-mt-tog="' + id + '">' +
      '<span class="method-num">' + num + '</span>' +
      '<span class="method-icon">' + icone + '</span>' +
      '<h2>' + titre + '</h2>' +
      '<span class="method-toggle">ouvrir / fermer</span>' +
    '</div><div class="method-body">' + corps + '</div></article>';
}

function poser(){
  var grid = document.getElementById('methodGrid');
  if(!grid || grid.querySelector('#method-eco-grille')) return;
  if(!grid.children.length) return;
  grid.insertAdjacentHTML('beforeend',
    carte('eco-grille', '15', '✅', 'Grille d’autoévaluation de ma copie',
          '<p class="method-intro">La grille distribuée en cours, rendue ' +
          'interactive : vingt-quatre critères à cocher en relisant votre ' +
          'copie, et un renvoi direct vers le passage de l’exemple qui ' +
          'montre à quoi ressemble chaque critère respecté.</p>' +
          '<div id="mt-grille"></div>') +
    carte('eco-fil', '16', '🧵',
          'Exemple fil rouge : « Faut-il toujours défendre le libre-échange ? »',
          '<p class="method-intro">Une copie modèle sur un seul sujet, ' +
          'du premier mot de l’accroche à l’ouverture : introduction, plan ' +
          'détaillé, annonce des sous-parties, sous-partie rédigée, ' +
          'transition et conclusion. Chaque pièce se lit nue, puis annotée.' +
          '</p><div id="mt-fil"></div>'));

  var nav = document.getElementById('methodNav');
  if(nav && !nav.querySelector('[data-mt-nav]')){
    nav.insertAdjacentHTML('beforeend',
      '<button data-mt-nav="eco-grille">15. Grille d’autoévaluation</button>' +
      '<button data-mt-nav="eco-fil">16. Exemple fil rouge</button>');
    nav.querySelectorAll('[data-mt-nav]').forEach(function(b){
      b.addEventListener('click', function(){
        var e = document.getElementById('method-' + b.getAttribute('data-mt-nav'));
        if(e){ e.classList.add('open'); e.scrollIntoView({behavior: 'smooth', block: 'start'}); }
      });
    });
  }
  document.querySelectorAll('[data-mt-tog]').forEach(function(b){
    if(b.__mt) return; b.__mt = 1;
    b.addEventListener('click', function(){
      var e = document.getElementById('method-' + b.getAttribute('data-mt-tog'));
      if(e) e.classList.toggle('open');
    });
  });
  majGrille();
  majFil();
}

function installer(){
  poser();
  var grid = document.getElementById('methodGrid');
  if(grid && !grid.__mtObs){
    grid.__mtObs = 1;
    try{
      new MutationObserver(function(){ setTimeout(poser, 0); })
        .observe(grid, {childList: true});
    }catch(e){}
  }
}

if(document.readyState === 'loading')
  document.addEventListener('DOMContentLoaded', installer);
else installer();

var ancien = window.showPg;
if(typeof ancien === 'function'){
  window.showPg = function(pg){
    var r = ancien.apply(this, arguments);
    if(pg === 'method'){ setTimeout(installer, 0); setTimeout(installer, 120); }
    return r;
  };
}

window.__ECO_METHODE = {grille: G, pieces: P, plan: PLAN,
  etat: function(){ return ETAT; }, viser: viser,
  mode: function(id, m){ MODE[id] = m; majFil(); },
  poser: installer};
})();
