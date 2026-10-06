import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';

const fichier = process.argv[2] || 'app_v197.html';
const b = await chromium.launch();
const p = await b.newPage();
const errs = [];
p.on('pageerror', e => errs.push(String(e).slice(0, 200)));
p.on('console', m => { if (m.type() === 'error' && !/CERT/.test(m.text())) errs.push('c:' + m.text().slice(0, 150)); });
const t0 = Date.now();
await p.goto('file://' + process.cwd() + '/' + fichier, { waitUntil: 'load', timeout: 240000 });
const tLoad = Date.now() - t0;
await p.waitForTimeout(11000);

const r = await p.evaluate(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const o = {};
  o.AUTHORS = AUTHORS.length;
  o.FC = FC_DATA.length;
  o.SI = (window.SEARCH_INDEX || []).length;
  o.CHC = Object.keys(CH_CONTENT).length;
  o.CHC_keys = Object.keys(CH_CONTENT).join(',');
  o.SUBJ = (window.SUBJECTS_BANK_PREMIUM || []).length;
  o.quizTotal = Object.values(window.ECOSPHERE_QUESTION_BANK || {}).flat().length;
  o.qbKeys = Object.keys(window.ECOSPHERE_QUESTION_BANK || {}).join(',');
  o.nav = [...document.querySelectorAll('.nt')].map(x => x.textContent.trim());
  o.pages = document.querySelectorAll('.pg').length;
  o.bilan23 = window.__ECO_CH23_BILAN;

  /* --- chapitre 23 --- */
  const c = CH_CONTENT[23];
  o.ch23 = c ? { titre: c.title, cours: c.cours.length, notions: (c.notions || []).length,
                 methode: (c.methode || '').length, annee: c.annee, numAnnee: c.numAnnee,
                 h2: (c.cours.match(/<h2>/g) || []).length,
                 h3: (c.cours.match(/<h3>/g) || []).length,
                 h4: (c.cours.match(/<h4>/g) || []).length } : null;
  o.fc23 = FC_DATA.filter(x => String(x.ch) === '23').length;
  o.fc23types = [...new Set(FC_DATA.filter(x => String(x.ch) === '23').map(x => x.type))].length;
  o.aut23 = AUTHORS.filter(a => (a.chapters || []).map(String).includes('23')).length;
  const A = window.__ECO_ADV_ALL_BANK || [];
  o.adv23 = A.filter(q => Number(q.ch) === 23).length;
  o.adv23tags = A.filter(q => Number(q.ch) === 23 && (q.tags || []).length > 2).length;
  o.qb23 = (window.ECOSPHERE_QUESTION_BANK || {})[23] ? window.ECOSPHERE_QUESTION_BANK[23].length : 0;
  o.subj23 = (window.SUBJECTS_BANK_PREMIUM || []).filter(s => Number(s.chapter) === 23).length;
  o.subj23plans = (window.SUBJECTS_BANK_PREMIUM || []).filter(s => Number(s.chapter) === 23)
    .map(s => (s.plan || []).length);
  o.mobil23 = (window.SUBJECTS_BANK_PREMIUM || []).filter(s => /2ᵉ année ch\. 3/.test(s.mobiliser || '')).length;
  o.args23 = (window.SUBJECTS_BANK_PREMIUM || []).filter(s => s.__ch23).length;
  o.args23n = (window.SUBJECTS_BANK_PREMIUM || []).reduce((a, s) => a + (s.__ch23 || 0), 0);
  try { o.vmap23 = VISUAL_MAPS_V83['23'] ? (function f(n){ let k=1; (n.children||n.branches||[]).forEach(x=>{ k += typeof x==='string'?1:f(x); }); return k; })(VISUAL_MAPS_V83['23']) : 0; } catch(e){ o.vmap23 = 'err '+e; }
  try { o.map23 = MAP_DATA[23] ? MAP_DATA[23].branches.length : 0; } catch(e){ o.map23 = 'err'; }
  try { o.vmapKeys = Object.keys(VISUAL_MAPS_V83).join(','); } catch(e){}

  /* --- page du chapitre --- */
  openCh(23); await sleep(900);
  const pc = document.getElementById('pg-chapter');
  o.pageCh23 = pc ? (pc.innerText || '').length : 0;
  o.pageCh23Titre = pc ? (pc.innerText || '').slice(0, 120).replace(/\n/g, ' | ') : '';
  o.pageCh23Lib = pc ? !/Chapitre 23/.test(pc.innerText) : null;

  /* --- recherche --- */
  showPg('search'); await sleep(600);
  const si = document.querySelector('#pg-search input');
  o.recherche = {};
  for (const q of ['avantage comparatif', 'Rybczynski', 'Bhagwati', 'protectionnisme éducateur',
                   'courbe de l’éléphant', 'Hawley-Smoot', 'seuil critique', 'Lassudrie']) {
    if (!si) break;
    si.value = q; si.dispatchEvent(new Event('input', { bubbles: true })); await sleep(420);
    o.recherche[q] = document.querySelectorAll('#pg-search .sr-item, #pg-search .search-result, #pg-search .res').length
      || (document.querySelector('#pg-search')?.innerText.match(/résultat/i) ? 'txt' : 0);
  }
  if (si) { si.value = ''; si.dispatchEvent(new Event('input', { bubbles: true })); }

  /* --- sujets --- */
  showPg('subjects'); await sleep(900);
  o.subjTabs = [...document.querySelectorAll('#subjTabsPremium .subj-tab')].map(x => x.textContent.trim());
  o.subjCards = [...document.querySelectorAll('#subjChaptersPremium .subj-ch-card')].length;
  o.subjCard23 = !!document.querySelector('#subjChaptersPremium [data-ch23]');
  try { setSubjectChapterPremium(23); await sleep(700);
    o.subj23Rendu = document.querySelectorAll('#pg-subjects .subj-card, #pg-subjects .subject-item').length;
    o.subj23Texte = (document.getElementById('pg-subjects').innerText || '').slice(0, 200).replace(/\n/g, ' | ');
  } catch (e) { o.subj23Rendu = 'err ' + e; }

  /* --- cartes --- */
  showPg('maps'); await sleep(900);
  o.mapsNodes23 = null;
  try {
    const sel = document.querySelector('#pg-maps select');
    o.mapsOptions = sel ? [...sel.options].map(x => x.value).join(',') : 'pas de select';
  } catch (e) {}

  /* --- atlas --- */
  showPg('atlas'); await sleep(900);
  o.atlasCards = document.querySelectorAll('#pg-atlas .at-card').length;
  o.atlasChapOptions = [...document.querySelectorAll('#pg-atlas select option')].map(x => x.textContent.trim());

  /* --- frise --- */
  showPg('frise'); await sleep(1200);
  const fs = document.getElementById('fr-ch');
  o.friseOptions = fs ? [...fs.options].map(x => x.textContent.trim()) : null;
  if (fs) { fs.value = '23'; fs.dispatchEvent(new Event('change', { bubbles: true })); await sleep(900);
    o.friseItems23 = document.querySelectorAll('#pg-frise .fr-it, #pg-frise .fr-item, #pg-frise [data-id]').length; }

  o.quizTags = A.filter(q => Number(q.ch) === 23).slice(0, 2).map(q => (q.tags || []).join('/'));
  return o;
});

await p.waitForTimeout(500);
console.log(JSON.stringify({ fichier, tLoad, errs: errs.slice(0, 12), nErrs: errs.length, ...r }, null, 1));
await b.close();
