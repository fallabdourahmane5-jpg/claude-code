/* ÉcoSphère — section « Courbes » (v225).

   Chaque fiche décrit un graphique sous forme de données : des séries
   (droites, courbes, points, flèches, zones) placées dans un repère
   normalisé, puis des étapes qui déplacent ces séries. Le moteur dessine le
   tout en SVG — donc net à n'importe quel zoom — et gère la lecture guidée,
   la comparaison de deux configurations, le tracé à la main et le plein
   écran. Les courbes se distinguent par leur trait autant que par leur
   couleur, pour rester lisibles sans se fier aux couleurs. */
(function(){
'use strict';
if(window.__ECO_COURBES_V225) return;
window.__ECO_COURBES_V225 = true;

/* __PAYLOAD__ */

var F = CB.f;            /* les fiches */
var LIBCAT = CB.cat;     /* libellés des thèmes */

var ORDRE_CH = ['1','2','3','4','5','6','7','8','9','10',
                '21','22','23','24','25','26'];

function libCh(k){
  k = String(k);
  var n = Number(k);
  return n >= 21 ? '2ᵉ année — ch.' + (n - 20) : 'Chapitre ' + k;
}
function chCourt(k){
  var n = Number(k);
  return n >= 21 ? '2A·' + (n - 20) : 'ch.' + k;
}
function esc(s){
  return String(s == null ? '' : s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
  });
}
function nz(s){
  return String(s == null ? '' : s).toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, ' ').trim();
}
function pg(){ return document.getElementById('pg-graphs'); }
function el(id){ return document.getElementById(id); }

/* ====================================================== dessin d'une figure

   Repère normalisé : x et y vont de 0 à 1, l'origine en bas à gauche. Le
   moteur convertit en coordonnées SVG, trace les axes, puis chaque série. */

var W = 760, H = 520;                       /* boîte de dessin */
var M = {g: 74, d: 108, h: 34, b: 62};      /* marges : place aux libellés */

function X(x){ return M.g + x * (W - M.g - M.d); }
function Y(y){ return H - M.b - y * (H - M.h - M.b); }

var COUL = {
  ac:  {c:'#7c6af7', d:''},            /* violet  — trait plein */
  ok:  {c:'#6af7c4', d:'9 5'},         /* vert    — tirets */
  ac2: {c:'#f7a26a', d:'2 5'},         /* orange  — pointillés */
  bl:  {c:'#6ab8f7', d:'14 5 3 5'},    /* bleu    — trait-point */
  ko:  {c:'#ff7a8a', d:'5 4'},         /* rouge   — tirets courts */
  jn:  {c:'#f7df6a', d:'1 4'},         /* jaune   — points serrés */
  gr:  {c:'#8a93a8', d:'3 4'}          /* gris    — repères */
};
function coul(k){ return COUL[k] || COUL.ac; }

/* courbe lissée passant par les points (Catmull-Rom convertie en Bézier) */
function lisser(pts){
  if(pts.length < 3) return 'M' + pts.map(function(p){ return X(p[0]) + ' ' + Y(p[1]); }).join('L');
  var d = 'M' + X(pts[0][0]) + ' ' + Y(pts[0][1]);
  for(var i = 0; i < pts.length - 1; i++){
    var p0 = pts[i ? i - 1 : 0], p1 = pts[i], p2 = pts[i + 1],
        p3 = pts[i + 2 < pts.length ? i + 2 : i + 1];
    var c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    var c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d += 'C' + X(c1[0]) + ' ' + Y(c1[1]) + ',' + X(c2[0]) + ' ' + Y(c2[1]) +
         ',' + X(p2[0]) + ' ' + Y(p2[1]);
  }
  return d;
}

function paires(p){
  var out = [];
  for(var i = 0; i + 1 < p.length; i += 2) out.push([p[i], p[i + 1]]);
  return out;
}

/* translation d'une série */
function bouger(s, dx, dy){
  var p = s.p.slice();
  for(var i = 0; i + 1 < p.length; i += 2){ p[i] += dx; p[i + 1] += dy; }
  var o = {};
  for(var k in s) o[k] = s[k];
  o.p = p;
  return o;
}

/* état des séries à l'étape i : on rejoue les étapes depuis le début */
function etat(fiche, etapes, i, vr){
  var base = (fiche.fig.series || []).map(function(s){
    var o = {}; for(var k in s) o[k] = s[k]; o.p = s.p.slice(); return o;
  });
  var index = {}, ordre = [];
  base.forEach(function(s){ index[s.id] = s; ordre.push(s.id); });
  var on = {};
  (etapes[0] && etapes[0].on ? etapes[0].on : ordre).forEach(function(id){ on[id] = 1; });
  for(var k = 0; k <= i && k < etapes.length; k++){
    var e = etapes[k];
    (e.add || []).forEach(function(s){
      var o = {}; for(var q in s) o[q] = s[q]; o.p = s.p.slice();
      if(!index[o.id]) ordre.push(o.id);
      index[o.id] = o; on[o.id] = 1;
    });
    for(var id in (e.move || {})){
      if(index[id]) index[id] = bouger(index[id], e.move[id][0], e.move[id][1]);
    }
    (e.on || []).forEach(function(id){ on[id] = 1; });
    (e.off || []).forEach(function(id){ delete on[id]; });
    if(e.seul){ on = {}; e.seul.forEach(function(id){ on[id] = 1; }); }
  }
  var vus = ordre.filter(function(id){ return on[id]; }).map(function(id){ return index[id]; });
  var act = {};
  if(i >= 0 && etapes[i]) (etapes[i].vif || []).forEach(function(id){ act[id] = 1; });
  var st = {series: vus, vif: act};
  if(vr && vr.axes){
    st.ax = {};
    for(var a in (fiche.axes || {})) st.ax[a] = fiche.axes[a];
    for(var b in vr.axes) st.ax[b] = vr.axes[b];
  }
  return st;
}

function fleche(id){
  return '<marker id="' + id + '" viewBox="0 0 10 10" refX="9" refY="5" ' +
    'markerWidth="6" markerHeight="6" orient="auto-start-reverse">' +
    '<path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker>';
}

function dessiner(fiche, st, opt){
  opt = opt || {};
  var ax = (st && st.ax) || fiche.axes || {};
  var uid = 'cbm' + (dessiner._n = (dessiner._n || 0) + 1);
  var h = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" ' +
    'aria-label="' + esc(fiche.t) + '" preserveAspectRatio="xMidYMid meet">';
  h += '<defs>' + fleche(uid) + '</defs>';
  h += '<rect x="0" y="0" width="' + W + '" height="' + H + '" fill="none"/>';

  /* --- quadrillage discret */
  var nu = !!ax.sans;
  var g = '';
  for(var q = 1; q <= 4; q++){
    g += '<line x1="' + X(0) + '" y1="' + Y(q / 5) + '" x2="' + X(1) +
         '" y2="' + Y(q / 5) + '"/>';
    g += '<line x1="' + X(q / 5) + '" y1="' + Y(0) + '" x2="' + X(q / 5) +
         '" y2="' + Y(1) + '"/>';
  }
  if(!nu) h += '<g stroke="#232a3a" stroke-width="1">' + g + '</g>';

  /* --- axes */
  if(!nu){
  h += '<g stroke="#67708a" stroke-width="2" color="#67708a" ' +
       'marker-end="url(#' + uid + ')">' +
       '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(1.04) + '" y2="' + Y(0) + '"/>' +
       '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(0) + '" y2="' + Y(1.06) + '"/>' +
       '</g>';
  var bas = (ax.gx && ax.gx.length) ? 38 : 30;
  h += '<text x="' + X(1.04) + '" y="' + (Y(0) + bas) + '" text-anchor="end" ' +
       'fill="#c3cad9" font-size="17" font-weight="600">' + esc(ax.x || '') + '</text>';
  h += '<text x="' + (X(0) + 14) + '" y="18" text-anchor="start" ' +
       'fill="#c3cad9" font-size="17" font-weight="600">' + esc(ax.y || '') + '</text>';
  if(ax.xu) h += '<text x="' + X(1.04) + '" y="' + (Y(0) + bas + 18) + '" text-anchor="end" ' +
       'fill="#7a8299" font-size="13">' + esc(ax.xu) + '</text>';
  if(ax.yu) h += '<text x="' + (X(0) + 14) + '" y="35" ' +
       'fill="#7a8299" font-size="13">' + esc(ax.yu) + '</text>';
  }

  /* --- graduations chiffrées (graphiques de données) */
  (ax.gx || []).forEach(function(t){
    h += '<g stroke="#67708a" stroke-width="1.6"><line x1="' + X(t[0]) + '" y1="' +
      Y(0) + '" x2="' + X(t[0]) + '" y2="' + (Y(0) + 6) + '"/></g>' +
      '<text x="' + X(t[0]) + '" y="' + (Y(0) + 19) + '" text-anchor="middle" ' +
      'fill="#8d95ab" font-size="12.5">' + esc(t[1]) + '</text>';
  });
  (ax.gy || []).forEach(function(t){
    h += '<g stroke="#67708a" stroke-width="1.6"><line x1="' + X(0) + '" y1="' +
      Y(t[0]) + '" x2="' + (X(0) - 7) + '" y2="' + Y(t[0]) + '"/></g>' +
      '<text x="' + (X(0) - 12) + '" y="' + (Y(t[0]) + 5) + '" text-anchor="end" ' +
      'fill="#8d95ab" font-size="13">' + esc(t[1]) + '</text>';
  });

  /* --- séries */
  st.series.forEach(function(s){
    var c = coul(s.c), vif = st.vif[s.id], pts = paires(s.p);
    var op = vif ? 1 : (s.pale ? .42 : .9);
    var ep = (s.ep || 3) * (vif ? 1.45 : 1);
    var lib = s.lib ? esc(s.lib) : '';
    if(s.type === 'zone'){
      h += '<path d="M' + pts.map(function(p){ return X(p[0]) + ' ' + Y(p[1]); }).join('L') +
           'Z" fill="' + c.c + '" fill-opacity="' + (vif ? .3 : .17) +
           '" stroke="' + c.c + '" stroke-width="1" stroke-opacity=".5"/>';
      if(lib) h += '<text x="' + X(pts[0][0]) + '" y="' + Y(pts[0][1]) +
        '" fill="' + c.c + '" font-size="14" font-weight="600">' + lib + '</text>';
      return;
    }
    if(s.type === 'pt'){
      h += '<circle cx="' + X(pts[0][0]) + '" cy="' + Y(pts[0][1]) + '" r="' +
        (vif ? 8 : 6) + '" fill="' + c.c + '" stroke="#0f131b" stroke-width="2"/>';
      if(lib) h += '<text x="' + (X(pts[0][0]) + 12) + '" y="' + (Y(pts[0][1]) - 10) +
        '" fill="' + c.c + '" font-size="16" font-weight="800">' + lib + '</text>';
      return;
    }
    if(s.type === 'txt'){
      h += '<text x="' + X(pts[0][0]) + '" y="' + Y(pts[0][1]) + '" fill="' +
        (s.c ? c.c : '#c3cad9') + '" font-size="' + (s.pt || 15) + '" ' +
        'font-weight="' + (s.gras ? 700 : 500) + '" opacity="' + op + '">' + lib + '</text>';
      return;
    }
    if(s.type === 'fl'){
      h += '<g color="' + c.c + '"><line x1="' + X(pts[0][0]) + '" y1="' + Y(pts[0][1]) +
        '" x2="' + X(pts[1][0]) + '" y2="' + Y(pts[1][1]) + '" stroke="' + c.c +
        '" stroke-width="' + (vif ? 3.4 : 2.6) + '" marker-end="url(#' + uid +
        ')" opacity="' + op + '"/></g>';
      if(lib){
        var mx = (pts[0][0] + pts[1][0]) / 2, my = (pts[0][1] + pts[1][1]) / 2;
        h += '<text x="' + X(mx) + '" y="' + (Y(my) - 9) + '" fill="' + c.c +
          '" font-size="14" font-weight="700" text-anchor="middle">' + lib + '</text>';
      }
      return;
    }
    if(s.type === 'rep'){      /* repères en pointillés vers les axes */
      h += '<g stroke="' + c.c + '" stroke-width="1.6" stroke-dasharray="4 4" ' +
        'opacity="' + (vif ? .85 : .5) + '">' +
        '<line x1="' + X(0) + '" y1="' + Y(pts[0][1]) + '" x2="' + X(pts[0][0]) +
        '" y2="' + Y(pts[0][1]) + '"/>' +
        '<line x1="' + X(pts[0][0]) + '" y1="' + Y(0) + '" x2="' + X(pts[0][0]) +
        '" y2="' + Y(pts[0][1]) + '"/></g>';
      if(s.lx) h += '<text x="' + X(pts[0][0]) + '" y="' + (Y(0) + 20) +
        '" text-anchor="middle" fill="' + c.c + '" font-size="14" font-weight="700">' +
        esc(s.lx) + '</text>';
      if(s.ly) h += '<text x="' + (X(0) - 9) + '" y="' + (Y(pts[0][1]) + 5) +
        '" text-anchor="end" fill="' + c.c + '" font-size="14" font-weight="700">' +
        esc(s.ly) + '</text>';
      return;
    }
    /* droites et courbes */
    var d = s.type === 'lin'
      ? 'M' + X(pts[0][0]) + ' ' + Y(pts[0][1]) + 'L' + X(pts[1][0]) + ' ' + Y(pts[1][1])
      : lisser(pts);
    h += '<path d="' + d + '" fill="none" stroke="' + c.c + '" stroke-width="' + ep +
      '" stroke-linecap="round" stroke-linejoin="round" opacity="' + op + '"' +
      (c.d ? ' stroke-dasharray="' + c.d + '"' : '') + '/>';
    if(lib){
      var f = pts[pts.length - 1], av = pts[pts.length - 2] || f;
      var dy = (f[1] >= av[1]) ? -12 : 20;
      var ancre = f[0] > .93 ? 'end' : 'start';
      var lx = X(f[0]) + (ancre === 'end' ? -4 : 9);
      if(s.lp){ lx = X(s.lp[0]); ancre = 'middle'; }
      h += '<text x="' + lx + '" y="' + ((s.lp ? Y(s.lp[1]) : Y(f[1]) + dy)) +
        '" fill="' + c.c + '" font-size="16" font-weight="800" text-anchor="' +
        ancre + '" opacity="' + op + '">' + lib + '</text>';
    }
  });
  h += '</svg>';
  return h;
}

/* vignette du catalogue : même moteur, sans texte ni marges */
function vignette(fiche){
  var st = etat(fiche, fiche.etapes || [{}], (fiche.etapes || []).length - 1);
  var vg = M, sv;
  M = {g: 26, d: 26, h: 18, b: 24};
  var ax = fiche.axes; fiche.axes = {};
  var garde = st.series.filter(function(s){
    return s.type !== 'txt' && s.type !== 'rep';
  }).map(function(s){ var o = {}; for(var k in s) o[k] = s[k]; o.lib = ''; return o; });
  sv = dessiner(fiche, {series: garde, vif: {}}, {});
  fiche.axes = ax; M = vg;
  return sv.replace('viewBox="0 0 ' + W + ' ' + H + '"',
                    'viewBox="0 0 ' + W + ' ' + H + '" style="max-height:150px"');
}

/* ========================================================= état de la page */

var VUE = null;        /* null = catalogue, sinon {id, i, var, main} */
var FIL = {q: '', an: '', ch: '', cat: '', type: ''};

function filtrer(){
  var q = nz(FIL.q);
  return F.filter(function(f){
    if(FIL.an && String(f.an) !== FIL.an) return false;
    if(FIL.ch && f.ch.indexOf(FIL.ch) < 0) return false;
    if(FIL.cat && f.cat !== FIL.cat) return false;
    if(FIL.type && f.type !== FIL.type) return false;
    if(!q) return true;
    var t = nz([f.t, f.st, f.q, (f.mots || []).join(' '),
                f.ch.map(libCh).join(' '), LIBCAT[f.cat]].join(' '));
    return q.split(' ').every(function(m){ return t.indexOf(m) >= 0; });
  });
}

function compter(champ, val){
  var s = {};
  for(var k in FIL) s[k] = FIL[k];
  s[champ] = val;
  var av = FIL; FIL = s;
  var n = filtrer().length;
  FIL = av;
  return n;
}

/* ============================================================== catalogue */

function accueil(){
  var z = pg();
  if(!z) return;
  VUE = null;
  var liste = filtrer();
  var nDon = F.filter(function(f){ return f.type === 'donnees'; }).length;
  var h = '<div class="cb">';
  h += '<div class="cb-hero"><h1>Courbes</h1><p>Chaque graphique du programme, ' +
    'redessiné en vectoriel et expliqué pas à pas : la question à laquelle il ' +
    'répond, ses axes et ses hypothèses, le déplacement provoqué par chaque ' +
    'choc, les pièges à éviter, l’ordre dans lequel le retracer à la main et ' +
    'la phrase qui l’explique en dissertation.</p>' +
    '<div class="cb-stat"><b><i>' + F.length + '</i> fiches</b>' +
    '<b><i>' + (F.length - nDon) + '</i> schémas théoriques</b>' +
    '<b><i>' + nDon + '</i> graphiques de données</b>' +
    '<b><i>' + Object.keys(LIBCAT).length + '</i> thèmes</b></div></div>';

  h += '<div class="cb-card"><div class="cb-rech">' +
    '<input id="cb-q" type="search" placeholder="Chercher une courbe, une notion, un auteur…" ' +
    'value="' + esc(FIL.q) + '" autocomplete="off">' +
    '<button id="cb-raz" type="button">Effacer</button></div></div>';

  h += '<div class="cb-card"><div class="cb-grid-f">';
  h += bloc('Année', 'an', [['', 'Les deux'], ['1', '1re année'], ['2', '2e année']]);
  h += bloc('Thème', 'cat', [['', 'Tous']].concat(Object.keys(LIBCAT).map(function(c){
    return [c, LIBCAT[c]];
  })));
  h += bloc('Nature', 'type', [['', 'Toutes'], ['schema', 'Schéma théorique'],
                               ['donnees', 'Graphique de données']]);
  h += '</div><div style="margin-top:16px">' +
    bloc('Chapitre', 'ch', [['', 'Tous']].concat(ORDRE_CH.map(function(k){
      return [k, libCh(k)];
    }))) + '</div></div>';

  h += '<div class="cb-liste" id="cb-liste">';
  h += liste.map(function(f){
    return '<button class="cb-vign" data-f="' + f.id + '">' +
      '<div class="cb-mini">' + vignette(f) + '</div>' +
      '<div class="cb-vt"><h4>' + esc(f.t) + '</h4><p>' + esc(f.st) + '</p>' +
      '<div class="cb-tags"><span class="cb-tag">' + esc(LIBCAT[f.cat] || f.cat) + '</span>' +
      f.ch.map(function(k){ return '<span class="cb-tag">' + esc(chCourt(k)) + '</span>'; }).join('') +
      (f.type === 'donnees' ? '<span class="cb-tag cb-don">données</span>' : '') +
      (f.variantes ? '<span class="cb-tag">' + f.variantes.length + ' configurations</span>' : '') +
      '</div></div></button>';
  }).join('') || '<div class="cb-vide">Aucune courbe ne correspond à ces filtres.</div>';
  h += '</div></div>';
  z.innerHTML = h;
  brancherAccueil();
}

function bloc(titre, champ, choix){
  return '<div><div class="cb-lab">' + esc(titre) + '</div><div class="cb-chips">' +
    choix.map(function(c){
      var n = compter(champ, c[0]);
      if(c[0] && !n) return '';
      return '<button class="cb-chip' + (FIL[champ] === c[0] ? ' on' : '') +
        '" data-' + champ + '="' + c[0] + '">' + esc(c[1]) +
        (c[0] ? '<small>' + n + '</small>' : '') + '</button>';
    }).join('') + '</div></div>';
}

function brancherAccueil(){
  var z = pg();
  ['an', 'ch', 'cat', 'type'].forEach(function(champ){
    z.querySelectorAll('[data-' + champ + ']').forEach(function(b){
      b.addEventListener('click', function(){
        FIL[champ] = b.getAttribute('data-' + champ);
        accueil();
      });
    });
  });
  var inp = el('cb-q');
  if(inp){
    var min;
    inp.addEventListener('input', function(){
      clearTimeout(min);
      min = setTimeout(function(){
        FIL.q = inp.value;
        var l = el('cb-liste');
        if(!l) return;
        var pos = inp.selectionStart;
        accueil();
        var n = el('cb-q');
        if(n){ n.focus(); try{ n.setSelectionRange(pos, pos); }catch(e){} }
      }, 180);
    });
  }
  var raz = el('cb-raz');
  if(raz) raz.addEventListener('click', function(){
    FIL = {q: '', an: '', ch: '', cat: '', type: ''};
    accueil();
  });
  z.querySelectorAll('[data-f]').forEach(function(b){
    b.addEventListener('click', function(){ ouvrir(b.getAttribute('data-f')); });
  });
}

/* ================================================================= fiche */

function trouver(id){
  for(var i = 0; i < F.length; i++) if(F[i].id === id) return F[i];
  return null;
}

function etapesDe(f, v){
  if(v != null && f.variantes && f.variantes[v]) return f.variantes[v].etapes;
  return f.etapes || [];
}

function ouvrir(id){
  var f = trouver(id);
  if(!f) return;
  VUE = {id: id, i: 0, v: f.variantes ? 0 : null, cmp: false, main: false, rev: false};
  rendre();
  try{ pg().scrollIntoView({block: 'start', behavior: 'smooth'}); }catch(e){}
}

function figureHTML(f){
  if(VUE.cmp && f.variantes){
    return '<div class="cb-fig cb-double" id="cb-fig">' +
      f.variantes.map(function(v, i){
        var ets = v.etapes;
        return '<div class="cb-fig-cel"><b>' + esc(v.lib) + '</b>' +
          dessiner(f, etat(f, ets, Math.min(VUE.i, ets.length - 1), v)) + '</div>';
      }).join('') + '</div>';
  }
  var ets = etapesDe(f, VUE.v);
  var vr = (VUE.v != null && f.variantes) ? f.variantes[VUE.v] : null;
  var st = VUE.main && !VUE.rev ? {series: [], vif: {}, ax: vr && vr.axes ?
    etat(f, ets, -1, vr).ax : null} : etat(f, ets, VUE.i, vr);
  return '<div class="cb-fig" id="cb-fig">' +
    '<div class="cb-zoom"><button class="cb-zb" id="cb-moins" title="Dézoomer">−</button>' +
    '<button class="cb-zb" id="cb-plus" title="Zoomer">+</button>' +
    '<button class="cb-zb" id="cb-vue" title="Vue initiale">⟲</button>' +
    '<button class="cb-zb" id="cb-plein" title="Plein écran">⛶</button></div>' +
    dessiner(f, st) + '</div>';
}

function rendre(){
  var z = pg(), f = trouver(VUE.id);
  if(!z || !f) return;
  var ets = etapesDe(f, VUE.v);
  var h = '<div class="cb">';
  h += '<div class="cb-top"><div><h2>' + esc(f.t) + '</h2>' +
    '<p class="cb-sous">' + esc(f.st) + '</p></div>' +
    '<button class="cb-btn cb-sec" id="cb-retour">← Toutes les courbes</button></div>';

  h += '<div class="cb-fiche"><div>';
  h += figureHTML(f);

  /* --- commandes */
  h += '<div class="cb-outils">';
  if(!VUE.main){
    h += '<button class="cb-btn" id="cb-suiv"' +
      (VUE.i >= ets.length - 1 ? ' disabled' : '') + '>Étape suivante →</button>';
    h += '<button class="cb-btn cb-sec" id="cb-prec"' +
      (VUE.i <= 0 ? ' disabled' : '') + '>← Précédente</button>';
  }
  if(f.variantes){
    h += '<button class="cb-btn cb-sec' + (VUE.cmp ? ' on' : '') + '" id="cb-cmp">' +
      (VUE.cmp ? '✓ Comparaison' : 'Comparer les ' + f.variantes.length + ' configurations') +
      '</button>';
    if(!VUE.cmp) h += '<select class="cb-btn cb-sec" id="cb-sel-var">' +
      f.variantes.map(function(v, i){
        return '<option value="' + i + '"' + (VUE.v === i ? ' selected' : '') + '>' +
          esc(v.lib) + '</option>';
      }).join('') + '</select>';
  }
  h += '<button class="cb-btn cb-sec' + (VUE.main ? ' on' : '') + '" id="cb-main">' +
    (VUE.main ? '✓ Refaire à la main' : '✏️ Refaire à la main') + '</button>';
  if(VUE.main) h += '<button class="cb-btn" id="cb-rev">' +
    (VUE.rev ? 'Masquer le tracé' : 'Afficher le tracé final') + '</button>';
  h += '<button class="cb-btn cb-sec" id="cb-raz2">Réinitialiser</button>';
  h += '</div>';

  /* --- étape courante, sous la figure */
  if(!VUE.main){
    var e = ets[VUE.i];
    if(e) h += '<div class="cb-bloc" style="margin-top:14px"><h3>Étape ' +
      (VUE.i + 1) + ' sur ' + ets.length +
      (f.variantes && !VUE.cmp ? ' · ' + esc(f.variantes[VUE.v].lib) : '') +
      '</h3><div class="cb-etape"><b>' + esc(e.t) + '</b><span>' + esc(e.d) +
      '</span></div>' +
      (VUE.cmp ? '<div class="cb-etape"><b>' +
        esc(f.variantes[1] ? f.variantes[1].lib : '') + '</b><span>' +
        esc((f.variantes[1].etapes[Math.min(VUE.i, f.variantes[1].etapes.length - 1)] || {}).d || '') +
        '</span></div>' : '') + '</div>';
  } else {
    h += '<div class="cb-bloc cb-main" style="margin-top:14px"><h3>Refaire à la main</h3>' +
      '<ol>' + (f.main || []).map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') +
      '</ol></div>';
  }
  h += '</div>';

  /* --- colonne d'explication */
  h += '<div class="cb-pan">';
  h += '<div class="cb-bloc"><h3>La question à laquelle elle répond</h3><p>' +
    esc(f.q) + '</p></div>';

  h += '<div class="cb-bloc"><h3>Axes, variables et hypothèses</h3><div class="cb-def">' +
    '<b>Abscisse</b><span>' + esc(f.axes.x) + (f.axes.xu ? ' (' + esc(f.axes.xu) + ')' : '') + '</span>' +
    '<b>Ordonnée</b><span>' + esc(f.axes.y) + (f.axes.yu ? ' (' + esc(f.axes.yu) + ')' : '') + '</span>' +
    (f.depart ? '<b>Départ</b><span>' + esc(f.depart) + '</span>' : '') +
    '</div>' +
    (f.hyp && f.hyp.length ? '<p style="margin-top:11px"><b style="color:var(--cb-ac2)">Hypothèses retenues</b></p><ul>' +
      f.hyp.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') +
    (f.pente && f.pente.length ? '<p style="margin-top:11px"><b style="color:var(--cb-ac2)">Pourquoi ces pentes</b></p><ul>' +
      f.pente.map(function(x){ return '<li><b>' + esc(x.s) + '</b> — ' + esc(x.d) + '</li>'; }).join('') +
      '</ul>' : '') + '</div>';

  if(!VUE.main){
    h += '<div class="cb-bloc"><h3>Lecture guidée</h3>' + ets.map(function(e, i){
      return '<div class="cb-etape' + (i > VUE.i ? ' off' : '') + '" data-et="' + i +
        '" style="cursor:pointer"><b>' + (i + 1) + '. ' + esc(e.t) + '</b><span>' +
        esc(e.d) + '</span></div>';
    }).join('') + '</div>';
  }

  if(f.pieges && f.pieges.length)
    h += '<div class="cb-bloc"><h3>Pièges à éviter</h3>' + f.pieges.map(function(p){
      return '<div class="cb-etape cb-piege"><b>' + esc(p.t) + '</b><span>' +
        esc(p.d) + '</span></div>';
    }).join('') + '</div>';

  if(f.src){
    h += '<div class="cb-bloc"><h3>Source des données</h3><div class="cb-src">';
    if(typeof f.src === 'string') h += esc(f.src);
    else h += [['Source', f.src.so], ['Période', f.src.pe],
               ['Unités', f.src.un], ['Précaution', f.src.nb]]
      .filter(function(z){ return z[1]; })
      .map(function(z){
        return '<div class="cb-srcl"><b>' + z[0] + '</b><span>' + esc(z[1]) +
          '</span></div>';
      }).join('');
    h += '</div></div>';
  }

  h += '<div class="cb-bloc"><h3>Phrase parfaite</h3><div class="cb-phrase">« ' +
    esc(f.phrase) + ' »</div></div>';

  h += '<div class="cb-bloc"><h3>Où le cours en parle</h3>' +
    (f.liens || []).map(function(l){
      return '<button class="cb-lien" data-c="' + l.c + '" data-b="' + l.b + '">📖 ' +
        esc(libCh(l.c)) + '<em>' + esc(l.l) + '</em></button>';
    }).join('') + '</div>';
  h += '</div></div></div>';
  z.innerHTML = h;
  brancherFiche(f, ets);
}

function brancherFiche(f, ets){
  var z = pg();
  function maj(){ rendre(); }
  function clic(id, fn){ var b = el(id); if(b) b.addEventListener('click', fn); }
  clic('cb-retour', function(){ accueil(); });
  clic('cb-suiv', function(){ VUE.i = Math.min(VUE.i + 1, ets.length - 1); maj(); });
  clic('cb-prec', function(){ VUE.i = Math.max(VUE.i - 1, 0); maj(); });
  clic('cb-raz2', function(){ VUE.i = 0; VUE.cmp = false; VUE.main = false; VUE.rev = false; maj(); });
  clic('cb-cmp', function(){ VUE.cmp = !VUE.cmp; VUE.main = false; maj(); });
  clic('cb-main', function(){ VUE.main = !VUE.main; VUE.rev = false; VUE.cmp = false; maj(); });
  clic('cb-rev', function(){ VUE.rev = !VUE.rev; maj(); });
  var sel = el('cb-sel-var');
  if(sel) sel.addEventListener('change', function(){
    VUE.v = Number(sel.value); VUE.i = 0; maj();
  });
  z.querySelectorAll('[data-et]').forEach(function(b){
    b.addEventListener('click', function(){
      VUE.i = Number(b.getAttribute('data-et')); maj();
    });
  });
  z.querySelectorAll('[data-c][data-b]').forEach(function(b){
    b.addEventListener('click', function(){
      var c = b.getAttribute('data-c'), bl = Number(b.getAttribute('data-b'));
      /* d'anciennes couches vident le texte du cours à chaque ouverture de
         chapitre : on le remet d'aplomb avant de viser. */
      try{ window.__ECO_GARDE_COURS.restaurer(); }catch(e){}
      var Q = window.__ECO_QUIZ, txt = '';
      try{ if(Q && Q.texteBloc) txt = Q.texteBloc(String(c), bl); }catch(e){}
      try{
        if(window.__ECO_RECHERCHE && window.__ECO_RECHERCHE.ouvrir){
          /* -1 ouvre le chapitre sans se fier à l'index du bloc : c'est le
             repérage par le texte, plus sûr, qui fait ensuite le travail. */
          window.__ECO_RECHERCHE.ouvrir(['ch', String(c), txt ? -1 : bl]);
        } else { openCh(Number(c)); }
      }catch(e){ try{ openCh(Number(c)); }catch(x){} }
      try{ if(txt && Q && Q.viserPassage) Q.viserPassage(bl, txt); }catch(e){}
    });
  });
  brancherZoom();
  clic('cb-plein', function(){ plein(f); });
}

/* ------------------------------------------------- zoom et plein écran */

function brancherZoom(ctx){
  var cadre = (ctx || document).querySelector('#cb-fig') ||
              (ctx || document).querySelector('.cb-fig');
  if(!cadre) return;
  var svgs = cadre.querySelectorAll('svg');
  if(!svgs.length) return;
  var st = {k: 1, x: 0, y: 0};
  function poser(){
    svgs.forEach(function(sv){
      sv.setAttribute('viewBox', st.x + ' ' + st.y + ' ' + (W / st.k) + ' ' + (H / st.k));
    });
  }
  function zoom(f, cx, cy){
    var k2 = Math.min(6, Math.max(1, st.k * f));
    if(k2 === st.k) return;
    var lx = st.x + (cx == null ? .5 : cx) * W / st.k;
    var ly = st.y + (cy == null ? .5 : cy) * H / st.k;
    st.k = k2;
    st.x = Math.max(0, Math.min(W - W / st.k, lx - (cx == null ? .5 : cx) * W / st.k));
    st.y = Math.max(0, Math.min(H - H / st.k, ly - (cy == null ? .5 : cy) * H / st.k));
    poser();
  }
  var zp = (ctx || document).querySelector('#cb-plus'),
      zm = (ctx || document).querySelector('#cb-moins'),
      zv = (ctx || document).querySelector('#cb-vue');
  if(zp) zp.addEventListener('click', function(){ zoom(1.5); });
  if(zm) zm.addEventListener('click', function(){ zoom(1 / 1.5); });
  if(zv) zv.addEventListener('click', function(){ st = {k: 1, x: 0, y: 0}; poser(); });
  cadre.addEventListener('wheel', function(e){
    if(st.k === 1 && e.deltaY > 0) return;
    if(e.target && e.target.closest && e.target.closest('button')) return;
    e.preventDefault();
    var r = cadre.getBoundingClientRect();
    zoom(e.deltaY < 0 ? 1.18 : 1 / 1.18,
         (e.clientX - r.left) / r.width, (e.clientY - r.top) / r.height);
  }, {passive: false});
  var dr = null;
  cadre.addEventListener('pointerdown', function(e){
    if(st.k <= 1) return;
    /* ne jamais capturer le pointeur sur les boutons d'outils : sinon le
       clic sur « vue initiale » ou « plein écran » n'aboutit plus */
    if(e.target && e.target.closest && e.target.closest('button')) return;
    dr = {x: e.clientX, y: e.clientY, ox: st.x, oy: st.y};
    cadre.setPointerCapture(e.pointerId);
  });
  cadre.addEventListener('pointermove', function(e){
    if(!dr) return;
    var r = cadre.getBoundingClientRect();
    st.x = Math.max(0, Math.min(W - W / st.k, dr.ox - (e.clientX - dr.x) / r.width * W / st.k));
    st.y = Math.max(0, Math.min(H - H / st.k, dr.oy - (e.clientY - dr.y) / r.height * H / st.k));
    poser();
  });
  cadre.addEventListener('pointerup', function(){ dr = null; });
  cadre.addEventListener('pointercancel', function(){ dr = null; });
}

function plein(f){
  var ets = etapesDe(f, VUE.v);
  var vrp = (VUE.v != null && f.variantes) ? f.variantes[VUE.v] : null;
  var d = document.createElement('div');
  d.className = 'cb-plein';
  d.innerHTML = '<div class="cb-pbar"><b>' + esc(f.t) + '</b>' +
    '<div class="cb-outils" style="margin:0">' +
    '<button class="cb-btn cb-sec" id="cbp-prec">← Précédente</button>' +
    '<button class="cb-btn" id="cbp-suiv">Étape suivante →</button>' +
    '<button class="cb-zb" id="cb-moins">−</button>' +
    '<button class="cb-zb" id="cb-plus">+</button>' +
    '<button class="cb-zb" id="cb-vue">⟲</button>' +
    '<button class="cb-btn cb-sec" id="cbp-fin">Fermer ✕</button></div></div>' +
    '<div class="cb-fig" id="cb-fig"></div>' +
    '<div class="cb-bloc" id="cbp-txt" style="margin-top:10px"></div>';
  pg().appendChild(d);
  var i = VUE.i;
  function dessine(){
    var cadre = d.querySelector('#cb-fig');
    if(VUE.cmp && f.variantes){
      cadre.className = 'cb-fig cb-double';
      cadre.innerHTML = f.variantes.map(function(v){
        return '<div class="cb-fig-cel"><b>' + esc(v.lib) + '</b>' +
          dessiner(f, etat(f, v.etapes, Math.min(i, v.etapes.length - 1), v)) + '</div>';
      }).join('');
    } else {
      cadre.className = 'cb-fig';
      cadre.innerHTML = dessiner(f, etat(f, ets, i, vrp));
    }
    var e = ets[i];
    d.querySelector('#cbp-txt').innerHTML = '<h3>Étape ' + (i + 1) + ' sur ' +
      ets.length + '</h3><div class="cb-etape"><b>' + esc(e ? e.t : '') +
      '</b><span>' + esc(e ? e.d : '') + '</span></div>';
    d.querySelector('#cbp-prec').disabled = i <= 0;
    d.querySelector('#cbp-suiv').disabled = i >= ets.length - 1;
    brancherZoom(d);
  }
  d.querySelector('#cbp-suiv').addEventListener('click', function(){
    i = Math.min(i + 1, ets.length - 1); dessine();
  });
  d.querySelector('#cbp-prec').addEventListener('click', function(){
    i = Math.max(i - 1, 0); dessine();
  });
  function fermer(){
    VUE.i = i;
    d.remove();
    document.removeEventListener('keydown', esc2);
    rendre();
  }
  function esc2(ev){ if(ev.key === 'Escape') fermer(); }
  d.querySelector('#cbp-fin').addEventListener('click', fermer);
  document.addEventListener('keydown', esc2);
  dessine();
}

/* ============================================================ démarrage */

function installer(){
  if(!pg()) return;
  accueil();
  var _s = window.showPg;
  window.showPg = function(id){
    var r = _s.apply(this, arguments);
    if(String(id).indexOf('graph') >= 0){
      try{ if(!pg().querySelector('.cb')) accueil(); }catch(e){}
    }
    return r;
  };
}
if(document.readyState === 'loading'){
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(installer, 950); });
} else {
  setTimeout(installer, 950);
}

window.__ECO_COURBES = {fiches: F, ouvrir: ouvrir, accueil: accueil,
  etat: function(){ return VUE; }, filtres: FIL, filtrer: filtrer,
  dessiner: dessiner, calc: etat};
})();
