import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const dir = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b = await chromium.launch({ args: ['--no-sandbox'] });

const PAGES = ['home', 'chapters', 'fc', 'quiz', 'search', 'maps', 'subjects', 'authors', 'graphs', 'prog', 'visualisations', 'frise'];

async function sonde(f) {
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e).slice(0, 160)));
  await p.goto('file://' + dir + f, { waitUntil: 'load', timeout: 180000 });
  await p.waitForTimeout(8000);

  const base = await p.evaluate(() => {
    const g = n => { try { return eval(n); } catch (e) { return null; } };
    const len = n => { const v = g(n); return Array.isArray(v) ? v.length : (v && typeof v === 'object' ? Object.keys(v).length : null); };
    return {
      FC_DATA: len('FC_DATA'),
      SEARCH_INDEX: len('SEARCH_INDEX'),
      AUTHORS: len('AUTHORS'),
      CH_CONTENT: len('CH_CONTENT'),
      SUBJECTS: len('SUBJECTS'),
      SUBJECTS_BANK_PREMIUM: len('SUBJECTS_BANK_PREMIUM'),
      MAP_DATA: len('MAP_DATA'),
      QB: (() => { try { return Object.keys(window.ECOSPHERE_QUESTION_BANK || {}).length; } catch (e) { return null; } })(),
      QB22: (() => { try { return (window.ECOSPHERE_QUESTION_BANK || {})[22]?.length ?? null; } catch (e) { return null; } })(),
      FRISE: len('FRISE_DATA') ?? len('TL_DATA'),
      abdou: document.body.innerText.includes('Abdourahmane'),
    };
  });

  // recherche
  const rech = {};
  for (const q of ['mondialisation', 'chaîne de valeur', 'Baldwin', 'dumping', 'politique industrielle', 'Ricardo']) {
    rech[q] = await p.evaluate(async (t) => {
      const si = document.getElementById('si');
      if (!si) return -1;
      si.value = t;
      if (typeof doSearch === 'function') doSearch();
      await new Promise(r => setTimeout(r, 350));
      const res = document.getElementById('search-res') || document.getElementById('sr');
      return res ? res.querySelectorAll('.sr-item, .search-item, .res-card, .sres, [class*="res"]').length : -2;
    }, q);
  }

  // navigation complète
  const nav = {};
  for (const pg of PAGES) {
    nav[pg] = await p.evaluate(async (id) => {
      try { showPg(id); } catch (e) { return 'ERR'; }
      await new Promise(r => setTimeout(r, 450));
      const el = document.getElementById('pg-' + id);
      if (!el) return 'absent';
      return el.innerText.trim().length;
    }, pg);
  }

  // fiches : nombre de cartes + badges mal libellés
  const fc = await p.evaluate(async () => {
    try { showPg('fc'); if (typeof renderFC === 'function') renderFC(0); } catch (e) {}
    await new Promise(r => setTimeout(r, 600));
    const g = document.getElementById('fc-grid');
    return { cartes: g ? g.querySelectorAll('.fc').length : -1 };
  });

  // quiz chapitre 22 : tags + nombre de questions
  const quiz = await p.evaluate(async () => {
    try { showPg('quiz'); } catch (e) {}
    await new Promise(r => setTimeout(r, 500));
    const out = { tags: null, boutons: null };
    try {
      const tg = document.querySelectorAll('#pg-quiz .qtag, #pg-quiz [class*="tag"]');
      out.tags = tg.length;
    } catch (e) {}
    out.boutons = document.querySelectorAll('#pg-quiz .qo-btn').length;
    out.deux = [...document.querySelectorAll('#pg-quiz .qo-btn')].map(x => x.textContent.trim()).filter(t => /2.{0,3}\s*ann/i.test(t));
    return out;
  });

  // sujets : onglets
  const subj = await p.evaluate(async () => {
    try { showPg('subjects'); } catch (e) {}
    await new Promise(r => setTimeout(r, 700));
    const t = document.getElementById('subjTabsPremium');
    const onglets = t ? [...t.querySelectorAll('button')].map(x => x.textContent.trim()) : null;
    let n22 = null;
    try { setSubjectChapterPremium(22); await new Promise(r => setTimeout(r, 500));
      n22 = document.querySelectorAll('#pg-subjects .subj-card, #pg-subjects .subject-card, #subjListPremium > *').length; } catch (e) {}
    return { onglets: onglets ? onglets.slice(-4) : null, nbOnglets: onglets?.length, n22 };
  });

  // libellés résiduels
  const libel = await p.evaluate(async () => {
    for (const pg of ['home', 'chapters', 'quiz', 'subjects', 'maps', 'fc', 'search']) {
      try { showPg(pg); } catch (e) {}
      await new Promise(r => setTimeout(r, 250));
    }
    const t = document.body.innerText;
    return {
      ch22: (t.match(/chapitre\s*22(?![0-9])/gi) || []).length,
      ch21: (t.match(/chapitre\s*21(?![0-9])/gi) || []).length,
      badge22: (t.match(/\bch\.?\s*22(?![0-9])/gi) || []).length,
      badge21: (t.match(/\bch\.?\s*21(?![0-9])/gi) || []).length,
      an2: (t.match(/2.{0,3}\s*ann[eé]e/gi) || []).length,
    };
  });

  await p.close();
  return { base, rech, nav, fc, quiz, subj, libel, errs };
}

const r = {};
for (const f of process.argv.slice(2)) r[f] = await sonde(f);
console.log(JSON.stringify(r, null, 1));
await b.close();
