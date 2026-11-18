import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const Q25 = ['demande effective', 'multiplicateur fiscal', 'trappe à liquidité',
  "effet d'éviction", 'courbe BP', 'policy mix', 'écart de production',
  "loi d'Okun", 'équivalence ricardienne', 'triangle de Mundell', 'stagflation',
  'règle de Mundell', 'Alvin Hansen', 'Arthur Okun', 'Robert Barro',
  'Richard Kahn', 'modèle OG-DG', 'propension marginale à importer',
  'ex ante et ex post', 'courbe de Phillips', 'taux de chômage naturel',
  'revenu permanent', 'écart inflationniste', 'balance globale',
  'les trois D', 'idéal-type', 'loi psychologique fondamentale',
  'multiplicateur des dépenses publiques', 'courbe LM', 'choc d’offre'];

const Q26 = ["parité des pouvoirs d'achat", 'condition de Marshall-Lerner',
  'courbe en J', 'désinflation compétitive', 'théorème de Schmidt',
  'effet de massue', 'effet de levier', 'peur du flottement',
  "caisse d'émission", 'taux de change réel', 'monnaie véhiculaire',
  'stablecoin', 'doctrine Miran', 'guerre des monnaies', 'Gustav Cassel',
  'Guillermo Calvo', 'effet Balassa-Samuelson', 'accords du Plaza',
  'recyclage des pétrodollars', 'cercle vicieux de la monnaie faible',
  'taux de marge', 'régime de change', 'dollarisation', 'bandes de fluctuation',
  'inflation importée', 'réserves de change', 'loi du prix unique',
  'dévaluation compétitive', 'taux de change effectif', 'risque de change',
  'monnaie numérique de banque centrale', 'arbitrage sur le marché des changes',
  'convertibilité', 'comportement de marge', "taux d'intérêt réel"];

const b = await chromium.launch();
const p = await b.newPage();
const erreurs = [];
p.on('pageerror', e => erreurs.push(String(e).slice(0, 200)));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);

const o = await p.evaluate(({Q25, Q26}) => {
  const G = n => { try { return (new Function('try{return ' + n + '}catch(e){return undefined}'))(); } catch(e){ return undefined; } };
  const r = {};

  // ----------------------------------------------------------------- cours
  const CH = G('CH_CONTENT') || {};
  r.cours = {};
  ['24','25','26'].forEach(k=>{
    const c = CH[k] || {};
    r.cours[k] = {present: !!c.cours, titre: c.title || '',
      signes: (c.cours||'').length, img: ((c.cours||'').match(/<img/g)||[]).length,
      notions: (c.notions||[]).length};
  });

  // ---------------------------------------------------------------- fiches
  const FC = G('FC_DATA') || [];
  r.fiches = {};
  ['24','25','26'].forEach(k=>{
    const v = FC.filter(x=>String(x.ch)===k);
    const par = {};
    v.forEach(x=>{ par[x.type]=(par[x.type]||0)+1; });
    r.fiches[k] = {n: v.length, types: par};
  });

  // ------------------------------------------------------------------ quiz
  const QB = G('ECOSPHERE_QUESTION_BANK') || {};
  const AB = (window.__ECO_ADV_ALL_BANK) || {};
  r.quiz = {};
  ['24','25','26'].forEach(k=>{
    const a = (QB[k]||QB[Number(k)]||[]);
    const c = (AB[k]||AB[Number(k)]||[]);
    const par = {};
    a.forEach(x=>{ par[x.type]=(par[x.type]||0)+1; });
    r.quiz[k] = {bank: a.length, adv: c.length, types: par,
      avecExp: a.filter(x=>x.exp && x.exp.length>40).length};
  });

  // ---------------------------------------------------------------- cartes
  const MD = G('MAP_DATA') || {};
  const VM = G('VISUAL_MAPS_V83') || {};
  r.cartes = {};
  ['24','25','26'].forEach(k=>{
    const m = MD[k]||MD[Number(k)];
    const v = VM[k]||VM[Number(k)];
    r.cartes[k] = {map: m ? (m.parts||m.branches||m.nodes||[]).length || Object.keys(m).length : 0,
      visuel: v ? ((v.nodes||v.parts||[]).length || Object.keys(v).length) : 0};
  });

  // --------------------------------------------------------------- auteurs
  const AU = G('AUTHORS') || [];
  r.auteurs = {};
  ['24','25','26'].forEach(k=>{
    const lc = a => { const x = a.chapters || a.ch || a.chapitres || [];
      return (Array.isArray(x) ? x : String(x).split(/[^0-9]+/)).map(String); };
    const v = AU.filter(a=>lc(a).indexOf(k)>=0);
    r.auteurs[k] = {n: v.length, noms: v.map(a=>a.name).slice(0,80)};
  });
  r.auteursTotal = AU.length;

  // ----------------------------------------------------------------- atlas
  const at = document.getElementById('eco-atlas-idees');
  r.atlas = {};
  if (at) {
    const m = at.textContent.match(/var DATA = (\{.*?\});\n/s);
    try {
      const A = JSON.parse(m[1]);
      ['24','25','26'].forEach(k=>{
        const c = (A.ch||A.chapitres||{})[k];
        r.atlas[k] = c ? (c.idees||c.i||[]).length : 0;
      });
      r.atlas.chapitres = Object.keys(A.ch||A.chapitres||{}).length;
    } catch(e) { r.atlas.err = String(e).slice(0,120); }
  }

  // ----------------------------------------------------------------- frise
  const IT = G('ITEMS') || [];
  r.frise = {total: IT.length};
  ['25','26'].forEach(k=>{
    r.frise['c'+k] = IT.filter(x=>String(x.id||'').indexOf('c'+k+'_')===0).length;
  });
  r.frise.majCh = IT.filter(x=>{ const y = x.ch;
    const l = Array.isArray(y) ? y.map(String) : String(y==null?'':y).split(/[^0-9]+/);
    return l.indexOf('25')>=0 || l.indexOf('26')>=0; }).length;

  // ----------------------------------------------------- sujets de dissertation
  const SB = G('SUBJECTS_BANK_PREMIUM') || {};
  const liste = k => { const v = SB[k];
    if (Array.isArray(v)) return v;
    if (v && typeof v === 'object') {
      for (const n of ['subjects','sujets','items','list','l'])
        if (Array.isArray(v[n])) return v[n];
      const t = Object.values(v).filter(Array.isArray);
      if (t.length) return [].concat(...t);
    }
    return []; };
  r.sujets = {};
  Object.keys(SB).forEach(k=>{ r.sujets[k] = liste(k).length; });
  r.sujetsForme = Object.keys(SB).slice(0,3).map(k=>({k, t: typeof SB[k],
    arr: Array.isArray(SB[k]), cles: (SB[k] && typeof SB[k]==='object' && !Array.isArray(SB[k])) ? Object.keys(SB[k]).slice(0,8) : null}));
  let mob = 0, tot = 0, ex2526 = [];
  Object.keys(SB).forEach(k=>{
    liste(k).forEach(s=>{
      tot++;
      const t = String(s.mobiliser||'');
      if (/ch\.5|ch\.6|chapitre 5|chapitre 6/.test(t)) { mob++;
        if (ex2526.length < 6) ex2526.push({k, id:s.id, m:t.slice(0,150)}); }
    });
  });
  r.sujetsMobiliser = {total: tot, avec2526: mob, exemples: ex2526};

  // ------------------------------------------------------- autour d'une notion
  const an = document.getElementById('eco-autour-notion');
  if (an) {
    const m = an.textContent.match(/var D = (\{.*?\});\n/s);
    try {
      const A = JSON.parse(m[1]);
      const li = A.dossiers.filter(d=>((d.liens||{}).ch||[]).some(c=>['25','26'].indexOf(String(c.k))>=0));
      r.autour = {dossiers: A.dossiers.length, lies: li.length,
        cles: li.map(d=>d.cle).slice(0,60)};
    } catch(e) { r.autour = {err: String(e).slice(0,120)}; }
  }

  // ---------------------------------------------------------- visualisations
  const vz = document.getElementById('v215-visu-engine');
  if (vz) {
    const m = vz.textContent.match(/var VZ = (\[.*?\]);\n/s);
    try {
      const V = JSON.parse(m[1]);
      const li = V.filter(v=>(v.chapitres||[]).some(c=>['25','26'].indexOf(String(c.k))>=0));
      r.visu = {total: V.length, lies: li.length, cles: li.map(v=>v.cle)};
    } catch(e) { r.visu = {err: String(e).slice(0,120)}; }
  }

  // --------------------------------------------------------------- recherche
  const RE = window.__ECO_RECHERCHE;
  r.rech = {dispo: !!RE, resultats: {}};
  if (RE) {
    const faire = (q, ch) => {
      let R;
      try { R = RE.chercher(q); } catch(e) { return {err: String(e).slice(0,100)}; }
      const g = (R.groupes||[]);
      const prem = g.slice(0, 5).map(x=>({y:x.prim.y, t:x.prim.t, c:String(x.prim.c||''), b:x.prim.b}));
      const auCh = g.some(x=>String(x.prim.c)===ch) ||
        g.some(x=>(x.items||[]).some(i=>String(i.c)===ch));
      return {n: R.n, groupes: g.length, tete: prem[0]||null, auCh: auCh,
        premiers: prem};
    };
    Q25.forEach(q=>{ r.rech.resultats[q] = faire(q, '25'); });
    Q26.forEach(q=>{ r.rech.resultats[q] = faire(q, '26'); });
  }

  // ------------------------------------------------- chiffres et résumés
  const ch = document.getElementById('eco-chiffres');
  if (ch) {
    const m = ch.textContent.match(/var D = (\{.*?\});\n/s);
    try { const A = JSON.parse(m[1]);
      r.chiffres = {chapitres: Object.keys(A.ch).length,
        c25: (A.ch['25'].p.length + A.ch['25'].c.length),
        c26: (A.ch['26'].p.length + A.ch['26'].c.length)};
    } catch(e) { r.chiffres = {err: String(e).slice(0,120)}; }
  }
  const rs = document.getElementById('eco-resumes');
  if (rs) {
    const m = rs.textContent.match(/var D = (\{.*?\});\n/s);
    try { const A = JSON.parse(m[1]);
      r.resumes = {chapitres: Object.keys(A.ch).length,
        c25: A.ch['25'].parties.length, c26: A.ch['26'].parties.length,
        ess25: A.ch['25'].ess.length, ess26: A.ch['26'].ess.length};
    } catch(e) { r.resumes = {err: String(e).slice(0,120)}; }
  }

  // --------------------------------------------------------- navigation
  r.nav = [...document.querySelectorAll('nav .nt')].map(x=>x.textContent.trim());
  r.pages = [...document.querySelectorAll('.pg')].map(x=>x.id);
  return r;
}, {Q25, Q26});

o.erreursJs = erreurs;
fs.writeFileSync('verif2526.json', JSON.stringify(o, null, 1));
console.log('erreurs JS :', erreurs.length);
const ko = Object.entries(o.rech.resultats || {}).filter(([q, v]) => !v.auCh || v.n === 0);
console.log('requêtes sans résultat dans le bon chapitre :', ko.length);
ko.forEach(([q, v]) => console.log('  ✗', q, JSON.stringify(v).slice(0, 220)));
await b.close();
