import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const b = await chromium.launch();
const p = await b.newPage();
const erreurs = [];
p.on('pageerror', e => erreurs.push(String(e).slice(0, 160)));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);

const r = {};

// --------------------------------------------------------------- étiquettes
r.libelles = await p.evaluate(() => {
  const mauvais = [];
  const scan = () => {
    document.querySelectorAll('.pg, nav').forEach(z => {
      if (z.offsetParent === null && !z.classList.contains('active')) return;
      const t = (z.innerText || '');
      ['Chapitre 25', 'Chapitre 26', 'chapitre 25', 'chapitre 26',
       'ch.25', 'ch.26'].forEach(m => {
        if (t.indexOf(m) >= 0) mauvais.push({pg: z.id || z.tagName, m});
      });
    });
  };
  scan();
  return mauvais;
});

// ---------------------------------------------- pages, une à une
const PAGES = ['home', 'quiz', 'fc', 'search', 'authors', 'atlas', 'notions',
  'subjects', 'visualisations', 'method', 'curves', 'maps', 'formulas',
  'frise', 'progress', 'chiffres', 'resumes'];
r.pages = {};
for (const id of PAGES) {
  const o = await p.evaluate(id => {
    try { window.showPg(id); } catch(e) { return {err: String(e).slice(0,90)}; }
    return null;
  }, id);
  await p.waitForTimeout(900);
  const d = await p.evaluate(() => {
    const vis = [...document.querySelectorAll('.pg')].filter(x => x.offsetParent !== null);
    const z = vis[0];
    const t = z ? (z.innerText || '') : '';
    return {page: z ? z.id : '?', signes: t.length,
      ch5: /ch\.\s*5|chapitre 5|IS-LM|équilibre macro/i.test(t),
      ch6: /ch\.\s*6|chapitre 6|taux de change|change/i.test(t),
      mauvais: ['Chapitre 25', 'Chapitre 26'].filter(m => t.indexOf(m) >= 0)};
  });
  r.pages[id] = o && o.err ? o : d;
}

// --------------------------------------------------------- chapitres 25 et 26
r.chapitres = {};
for (const n of [25, 26]) {
  await p.evaluate(n => { try { window.openCh(n); } catch(e) {} }, n);
  await p.waitForTimeout(1800);
  r.chapitres[n] = await p.evaluate(() => {
    const c = document.getElementById('sect-cours');
    const t = document.getElementById('chTitle');
    const sections = [...document.querySelectorAll('.sect-btn, [data-sect], .chip-sect')]
      .map(x => (x.innerText || '').trim()).filter(Boolean).slice(0, 12);
    return {titre: t ? (t.innerText || '').replace(/\s+/g,' ').slice(0,90) : '',
      coursSignes: c ? (c.innerText || '').length : 0,
      img: c ? c.querySelectorAll('img').length : 0,
      formules: c ? c.querySelectorAll('.formula').length : 0,
      tableaux: c ? c.querySelectorAll('table').length : 0,
      sections};
  });
  await p.screenshot({path: 'ch' + n + '_cours.png', fullPage: false});
}

// ------------------------------------------------------------------- frise
await p.evaluate(() => { try { window.showPg('frise'); } catch(e) {} });
await p.waitForTimeout(2500);
r.frise = await p.evaluate(() => {
  const z = document.getElementById('pg-frise');
  const t = z ? (z.innerText || '') : '';
  return {signes: t.length,
    filtres: [...document.querySelectorAll('#pg-frise [data-ch], #pg-frise .fr-ch')]
      .map(x => (x.innerText || x.getAttribute('data-ch') || '').trim()).slice(0, 30)};
});

// -------------------------------------------------------------------- quiz
await p.evaluate(() => { try { window.showPg('quiz'); } catch(e) {} });
await p.waitForTimeout(1500);
r.quiz = await p.evaluate(() => {
  const z = document.getElementById('pg-quiz');
  const txt = z ? (z.innerText || '') : '';
  const cases = [...document.querySelectorAll('#pg-quiz input[type=checkbox], #pg-quiz .adv-ch')]
    .map(x => (x.closest('label') ? x.closest('label').innerText : x.value || '').replace(/\s+/g,' ').trim())
    .filter(Boolean);
  const opts = [...document.querySelectorAll('#pg-quiz select option')]
    .map(x => (x.textContent||'').trim());
  return {ch5: /ch\.\s*5|chapitre 5/i.test(txt), ch6: /ch\.\s*6|chapitre 6/i.test(txt),
    cases: cases.slice(0, 40), options: opts.slice(0, 40)};
});

r.erreurs = erreurs;
fs.writeFileSync('verif_ui2526.json', JSON.stringify(r, null, 1));
console.log('étiquettes fautives :', JSON.stringify(r.libelles));
console.log('erreurs JS :', erreurs.length, JSON.stringify(erreurs.slice(0,4)));
Object.entries(r.pages).forEach(([k,v]) => console.log(' ', k, JSON.stringify(v).slice(0,150)));
console.log('ch25', JSON.stringify(r.chapitres[25]).slice(0,260));
console.log('ch26', JSON.stringify(r.chapitres[26]).slice(0,260));
console.log('quiz', JSON.stringify(r.quiz).slice(0,500));
await b.close();
