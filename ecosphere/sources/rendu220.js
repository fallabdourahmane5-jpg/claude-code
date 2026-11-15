/* --------------------------------------------------- où le retrouver
   Les destinations ne sont plus une suite de pastilles : elles sont
   réparties par section — Cours, Fiches, Atlas, Visualisations… — et, dans
   le cours, regroupées par chapitre, pour ne plus répéter dix fois le même
   libellé de chapitre. */
var OU_GROUPES = [
  ['cours',    'Cours'],
  ['notions',  'Notions'],
  ['fiches',   'Fiches'],
  ['resumes',  'Résumés'],
  ['dossiers', 'Dossiers'],
  ['atlas',    'Atlas'],
  ['auteurs',  'Auteurs'],
  ['chiffres', 'Chiffres & faits'],
  ['formules', 'Formules'],
  ['visu',     'Visualisations'],
  ['sujets',   'Sujets']
];

function chLib(c){ return D.ch[c] ? D.ch[c].l : (c || ''); }
function chCourt(l){
  return String(l || '').replace('Chapitre ', 'ch.').replace('2ᵉ année — ', '2ᵉ ');
}

/* coupe au dernier mot entier plutôt qu'au milieu d'un mot */
function coupe(s, n){
  s = String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  if(s.length <= n) return s;
  var t = s.slice(0, n), e = t.lastIndexOf(' ');
  if(e > n * 0.55) t = t.slice(0, e);
  return t.replace(/[\s,;:.’'-]+$/, '') + '…';
}

function ouItems(l, cap){
  function bt(e){
    return '<button class="rq-o" data-k="' + esc(e.k) + '">' + esc(e.l)
      + '</button>';
  }
  if(l.length <= cap + 1) return l.map(bt).join('');
  return l.slice(0, cap).map(bt).join('')
    + '<span class="rq-cache" data-cache="1">' + l.slice(cap).map(bt).join('')
    + '</span><button class="rq-ou-plus" data-tout="1">+ '
    + (l.length - cap) + ' autres</button>';
}

function puces(g, Q, cap){
  var vus = Object.create(null), vusLib = Object.create(null);
  var ents = [], prim = g.prim;
  cap = cap || 5;
  function pose(k, grp, ch, lib){
    var sig = JSON.stringify(k);
    if(vus[sig] || !lib) return;
    /* deux blocs distincts portant le même intitulé dans le même chapitre
       n'ont pas à figurer deux fois dans la liste des destinations */
    var sigl = grp + '|' + (ch || '') + '|' + nz(lib);
    if(vusLib[sigl]) return;
    vus[sig] = 1; vusLib[sigl] = 1;
    ents.push({k:sig, g:grp, ch:ch || '', l:lib});
  }
  if(prim.y === 'def' && prim.ou && prim.ou.length){
    prim.ou.forEach(function(z){
      if(!D.ch[z[0]]) return;
      pose(['ch', z[0], z[1]], 'cours', chLib(z[0]),
        z[1] >= 0 ? 'le passage' : 'le chapitre');
    });
  }
  var parL = Object.create(null);
  g.items.forEach(function(r){
    if(r === prim) return;
    var y = r.y;
    if(y === 'passage' || y === 'sect'){
      var sg = r.c + '|' + cle(r.sect || r.t);
      if(parL[sg]) return;
      parL[sg] = 1;
      pose(r.k, 'cours', chLib(r.c), coupe(R_TITRE(r.sect || r.t), 56));
    }
    else if(y === 'notion')  pose(r.k, 'notions', chLib(r.c), coupe(r.t, 48));
    else if(y === 'fiche')   pose(r.k, 'fiches', '', chLib(r.c));
    else if(y === 'resume')  pose(r.k, 'resumes', '', chLib(r.c));
    else if(y === 'dossier') pose(r.k, 'dossiers', '', coupe(r.t, 52));
    else if(y === 'atlas')   pose(r.k, 'atlas', '',
      (r.aut ? r.aut + ' — ' : '') + coupe(r.t, 44));
    else if(y === 'auteur')  pose(r.k, 'auteurs', '', r.t);
    else if(y === 'chiffre') pose(r.k, 'chiffres', '', coupe(r.t, 52));
    else if(y === 'fait')    pose(r.k, 'chiffres', '',
      String(r.an) + (r.t ? ' — ' + coupe(r.t, 40) : ''));
    else if(y === 'formule') pose(r.k, 'formules', '', coupe(r.t, 50));
    else if(y === 'sujet')   pose(r.k, 'sujets', '', coupe(r.t, 64));
    else if(y === 'visu')    pose(r.k, 'visu', '', coupe(r.t, 46));
  });
  if(!ents.length) return '';

  var html = '', maxSg = cap >= 3 ? 3 : 2;
  OU_GROUPES.forEach(function(G0){
    var l = ents.filter(function(e){ return e.g === G0[0]; });
    if(!l.length) return;
    var corps;
    if(G0[0] === 'cours' || G0[0] === 'notions'){
      var ordre = [], parCh = Object.create(null);
      l.forEach(function(e){
        if(!parCh[e.ch]){ parCh[e.ch] = []; ordre.push(e.ch); }
        parCh[e.ch].push(e);
      });
      var sgs = ordre.map(function(c){
        return '<div class="rq-sg">'
          + (c ? '<span class="rq-sg-t">' + esc(c) + '</span>' : '')
          + ouItems(parCh[c], cap) + '</div>';
      });
      /* au-delà de trois chapitres, les suivants restent pliés : la carte
         de réponse n'a pas à dérouler vingt destinations */
      corps = sgs.length <= maxSg + 1 ? sgs.join('')
        : sgs.slice(0, maxSg).join('')
          + '<span class="rq-cache" data-cache="1">' + sgs.slice(maxSg).join('')
          + '</span><button class="rq-ou-plus" data-tout="1">+ '
          + (sgs.length - maxSg) + ' chapitres</button>';
    } else {
      corps = '<div class="rq-sg">' + ouItems(l, cap) + '</div>';
    }
    html += '<div class="rq-g"><div class="rq-g-l">' + G0[1] + '</div>'
      + '<div class="rq-g-c">' + corps + '</div></div>';
  });
  return '<div class="rq-ou"><div class="rq-ou-t">Où le retrouver'
    + '<span>' + ents.length + '</span></div>' + html + '</div>';
}

/* ------------------------------------------------- à ne pas confondre */
function confondre(r, fam){
  if(r.x)
    return '<div class="rq-conf"><div class="rq-conf-t">À ne pas confondre'
      + '</div><div class="rq-conf-d">' + esc(r.x) + '</div></div>';
  if(!fam || fam.membres.length < 2) return '';
  var autres = fam.membres.filter(function(z){ return z.nt !== r.nt; }).slice(0, 6);
  if(!autres.length) return '';
  return '<div class="rq-conf"><div class="rq-conf-t">À ne pas confondre avec'
    + '</div><div class="rq-conf-l">' + autres.map(function(z){
        return '<button class="rq-cf" data-q="' + esc(z.t) + '"><b>'
          + esc(z.t) + '</b>'
          + (z.c && D.ch[z.c] ? '<i>' + esc(chCourt(D.ch[z.c].l)) + '</i>' : '')
          + '</button>';
      }).join('') + '</div></div>';
}

/* --------------------------------------------------------------- réponse */
function rendreReponse(g, Q, fam){
  if(!g) return '';
  var r = g.prim;
  var meta = ['<span class="rq-ty ' + (TYPE_CL[r.y] || '') + '">'
    + esc(TYPE_LIB[r.y] || r.y) + '</span>'];
  if(lieu(r)) meta.push(esc(lieu(r)));
  if(r.o && r.o.indexOf('redigee') >= 0)
    meta.push('définition rédigée d’après le cours');
  else if(r.o && r.o.indexOf('cours-encadre') >= 0)
    meta.push('définition du cours');
  var alias = (r.al || []).filter(function(z){
    return z && z !== r.nt && (z === Q.cle || (Q.syn || []).indexOf(z) >= 0); });
  if(alias.length)
    meta.push('aussi écrit ' + esc(alias.join(', ').toUpperCase()));
  return '<div class="rq-rep">'
    + '<div class="rq-rep-k">Réponse</div>'
    + '<div class="rq-rep-t">' + esc(r.t) + '</div>'
    + '<div class="rq-rep-m">' + meta.join('<i>·</i>') + '</div>'
    + '<div class="rq-rep-d">' + surligner(texteDe(r, Q), Q, r.al) + '</div>'
    + confondre(r, fam) + puces(g, Q, 3) + '</div>';
}

/* --------------------------------------------------------------- famille */
function rendreFamille(fam, Q){
  if(!fam) return '';
  var l = fam.membres.filter(function(z){ return z.nt !== Q.cle; });
  if(l.length < 2) return '';
  return '<div class="rq-fam"><div class="rq-fam-t">Les formes de <b>« '
    + esc(fam.tete) + ' »</b> dans tes chapitres<span>' + l.length + '</span>'
    + '</div><div class="rq-fam-l">' + l.map(function(z){
        return '<button class="rq-k" data-q="' + esc(z.t) + '">' + esc(z.t)
          + (z.c && D.ch[z.c] ? '<em>' + esc(chCourt(D.ch[z.c].l)) + '</em>' : '')
          + '</button>';
      }).join('') + '</div></div>';
}

/* --------------------------------------------------------------- lignes */
function rendreLigne(g, Q, i){
  var r = g.prim;
  var txt = texteDe(r, Q);
  var chemin = r.path || (r.y === 'sect' ? r.p : '');
  return '<div class="rq-r" data-i="' + i + '">'
    + '<div class="rq-rh" data-bascule="1">'
    + '<span class="rq-rt">' + surligner(r.t, Q, r.al)
    + (g.items.length > 1 ? ' <i>· ' + g.items.length + ' occurrences</i>' : '')
    + '</span>'
    + '<span class="rq-rm">'
    + '<span class="rq-ty ' + (TYPE_CL[r.y] || '') + '">'
    + esc(TYPE_LIB[r.y] || r.y) + '</span>'
    + (lieu(r) ? '<span class="rq-ch">' + esc(lieu(r)) + '</span>' : '')
    + '</span>'
    + '<span class="rq-car">›</span></div>'
    + (txt ? '<div class="rq-ex">' + surligner(extrait(txt, Q, 300), Q, r.al)
        + '</div>' : '')
    + '<div class="rq-corps">'
    + confondre(r, null)
    + (chemin ? '<div class="rq-path">' + esc(chemin) + '</div>' : '')
    + '<button class="rq-go" data-k="' + esc(JSON.stringify(r.k)) + '">'
    + 'Ouvrir ' + esc(ouLib(r)) + ' <span>→</span></button>'
    + puces(g, Q, 2)
    + '</div></div>';
}
function ouLib(r){
  if(r.y === 'passage' || r.y === 'sect' || r.y === 'def' || r.y === 'fait'
     || r.y === 'notion') return 'le passage';
  if(r.y === 'auteur') return 'la fiche de l’auteur';
  if(r.y === 'dossier') return 'le dossier';
  if(r.y === 'atlas') return 'l’Atlas';
  if(r.y === 'chiffre') return 'les chiffres';
  if(r.y === 'resume') return 'le résumé';
  if(r.y === 'sujet') return 'les sujets';
  if(r.y === 'fiche') return 'les fiches';
  if(r.y === 'visu') return 'la visualisation';
  if(r.y === 'formule') return 'les formules';
  return 'la section';
}

var PAS = 12;
var MONTRE = {ex:PAS, el:PAS};

function rendre(R){
  var Q = R.Q;
  var rep = document.getElementById('rq-rep');
  var fam = document.getElementById('rq-fam');
  var out = document.getElementById('rq-outils');
  var box = document.getElementById('rq-res');

  if(!R.groupes.length){
    rep.innerHTML = ''; fam.innerHTML = '';
    out.innerHTML = barreOutils(R);
    var pistes = ['position extérieure nette','capital humain',
      'avantage comparatif','anomie','Bairoch','destruction créatrice'];
    box.innerHTML = '<div class="rq-vide"><div class="rq-vide-t">'
      + 'Rien dans ÉcoSphère ne porte cette expression.</div>'
      + 'La recherche balaie le texte des quatorze chapitres, les fiches, les '
      + 'auteurs, les sujets, les dossiers, l’Atlas, les chiffres et les '
      + 'résumés. Si l’expression n’y est pas, c’est qu’elle n’est pas '
      + 'traitée dans tes cours.'
      + '<div class="rq-pistes">' + pistes.map(function(x){
          return '<button class="rq-k" data-q="' + esc(x) + '">' + esc(x)
            + '</button>';
        }).join('') + '</div></div>';
    return;
  }
  rep.innerHTML = rendreReponse(R.reponse, Q, R.famille);
  fam.innerHTML = rendreFamille(R.famille, Q);
  out.innerHTML = barreOutils(R);

  var h = '';
  var ex = R.exactes.filter(function(g){ return g !== R.reponse; });
  if(ex.length){
    h += '<div class="rq-bloc-t">Correspondances exactes<em>' + ex.length
      + '</em></div>';
    h += ex.slice(0, MONTRE.ex).map(function(g, i){
      return rendreLigne(g, Q, 'e' + i); }).join('');
    if(ex.length > MONTRE.ex)
      h += '<button class="rq-plus" data-plus="ex">Afficher '
        + Math.min(PAS, ex.length - MONTRE.ex) + ' résultats de plus · '
        + (ex.length - MONTRE.ex) + ' restants</button>';
  }
  if(R.elargies.length){
    h += '<div class="rq-bloc-t">Recherche élargie<em>' + R.elargies.length
      + ' · l’expression n’y figure pas telle quelle</em></div>';
    h += R.elargies.slice(0, MONTRE.el).map(function(g, i){
      return rendreLigne(g, Q, 'l' + i); }).join('');
    if(R.elargies.length > MONTRE.el)
      h += '<button class="rq-plus" data-plus="el">Afficher '
        + Math.min(PAS, R.elargies.length - MONTRE.el) + ' résultats de plus · '
        + (R.elargies.length - MONTRE.el) + ' restants</button>';
  }
  box.innerHTML = h;
}

function barreOutils(R){
  var Q = R.Q, c = comptesRequete(R);
  var tot = R.groupes.length;
  var msg = '<div class="rq-cpt"><b>' + (R.montres || tot) + '</b> '
    + ((R.montres || tot) > 1 ? 'résultats' : 'résultat')
    + (R.tronque ? ' les plus pertinents sur ' + tot : '')
    + (R.exactes.length && R.elargies.length
        ? ' · ' + R.exactes.length + ' exacts' : '')
    + (Q.ch ? ' · chapitre ' + esc(Q.ch) : '') + '</div>';
  var ordre = ['tout','definitions','cours','auteurs','dossiers','atlas',
    'chiffres','faits','formules','sujets','fiches','resumes','visu'];
  var dispo = ordre.filter(function(f){
    return f === 'tout' || f === FILTRE || (c[f] || 0) > 0; });
  var liens = dispo.slice(0, 7).map(function(f){
    var n = f === 'tout' ? tot : (c[f] || 0);
    return '<button class="rq-f' + (f === FILTRE ? ' on' : '') + '" data-f="'
      + f + '">' + FAM_LIB[f] + '<u>' + n + '</u></button>';
  }).join('');
  var sel = '<select class="rq-sel" id="rq-sel">' + dispo.map(function(f){
    var n = f === 'tout' ? tot : (c[f] || 0);
    return '<option value="' + f + '"' + (f === FILTRE ? ' selected' : '')
      + '>' + FAM_LIB[f] + ' (' + n + ')</option>';
  }).join('') + '</select>';
  var corr = '';
  if(Q.corrige)
    corr = '<div class="rq-corr">Aucun résultat pour '
      + '« <b>' + esc(Q.brut) + '</b> » : recherche élargie à « <b>'
      + esc(Q.mots.join(' ')) + '</b> ».'
      + '<button data-litteral="1">chercher « ' + esc(Q.brut)
      + ' » littéralement</button></div>';
  return corr + msg + sel + '<div class="rq-fl">' + liens + '</div>';
}

