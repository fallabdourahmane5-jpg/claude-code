import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const f = process.argv[2];
const W = Number(process.argv[3] || 1400);
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:W,height:950}});
const errs = [];
p.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
await p.goto('file://' + f);
await p.waitForTimeout(14000);
const out = {};

// --- COURS
await p.evaluate(() => openCh(24));
await p.waitForTimeout(1200);
out.cours = await p.evaluate(() => {
  const el = document.getElementById('pg-chapter');
  const t = el.innerText;
  return {visible: el.classList.contains('on'),
    h2: [...el.querySelectorAll('h2')].map(x=>x.textContent.trim().slice(0,70)),
    nbH3: el.querySelectorAll('h3').length, nbH4: el.querySelectorAll('h4').length,
    len: t.length,
    gatt: t.includes('GATT'), seattle: t.includes('Seattle'), cairns: t.includes('Cairns'),
    arachide: t.includes('arachide'), multifibres: t.includes('multifibres'),
    orourke: t.includes('O’Rourke'), ch24brut: /Chapitre 24|chapitre 24/.test(t)};
});

// --- FICHES
await p.evaluate(() => { showPg('fc'); });
await p.waitForTimeout(600);
await p.evaluate(() => { if (typeof filterFC === 'function') filterFC(24); });
await p.waitForTimeout(900);
out.fiches = await p.evaluate(() => {
  const el = document.getElementById('pg-fc');
  const chips = [...el.querySelectorAll('.fc-chip, .chip, button')].map(x=>x.textContent.trim()).filter(t=>/Ch\.?\s*\d|année/i.test(t));
  return {chips: chips.slice(0,30), cartes: el.querySelectorAll('.fc-card, .fcard, .card').length,
     txt: el.innerText.slice(0,200), ch24brut: /chapitre 24/i.test(el.innerText)};
});

// --- CARTE MENTALE
await p.evaluate(() => { showPg('maps'); });
await p.waitForTimeout(700);
await p.evaluate(() => { if (typeof renderVisualMap === 'function') renderVisualMap(24); });
await p.waitForTimeout(1200);
out.maps = await p.evaluate(() => {
  const el = document.getElementById('pg-maps');
  return {len: el.innerText.length, nodes: el.querySelectorAll('svg g, .vm-node, .eco-v83-node').length,
    txt: el.innerText.slice(0,260), ch24brut: /chapitre 24/i.test(el.innerText)};
});

// --- ATLAS
await p.evaluate(() => { showPg('atlas'); });
await p.waitForTimeout(900);
out.atlas = await p.evaluate(() => {
  const sel = document.getElementById('at-ch');
  const has24 = !!(sel && [...sel.options].some(o=>o.value==='24'));
  if (sel) { sel.value='24'; sel.dispatchEvent(new Event('change')); }
  return {has24, options: sel ? [...sel.options].map(o=>o.value+':'+o.textContent).slice(-4) : null};
});
await p.waitForTimeout(700);
out.atlas.cartes = await p.evaluate(() => document.querySelectorAll('#at-liste .at-card').length);
out.atlas.compteur = await p.evaluate(() => (document.getElementById('at-nb')||{}).textContent);

// --- CHIFFRES
out.chiffres = await p.evaluate(() => {
  if (typeof ouvrirChiffres === 'function') { ouvrirChiffres('24'); return 'ok'; }
  return 'absent';
});
await p.waitForTimeout(1000);
out.chiffresTxt = await p.evaluate(() => {
  const el = document.getElementById('pg-chiffres');
  if (!el) return null;
  return {len: el.innerText.length, cartes: el.querySelectorAll('.cf-card, .chif-card, .cf-it').length,
     extrait: el.innerText.slice(0,300)};
});

// --- RESUMES
out.resumes = await p.evaluate(() => {
  if (typeof ouvrirResume === 'function') { ouvrirResume('24'); return 'ouvrirResume'; }
  const f = Object.keys(window).filter(k=>/resum/i.test(k));
  return f.join(',') || 'absent';
});
await p.waitForTimeout(1200);
out.resumesTxt = await p.evaluate(() => {
  const el = document.getElementById('pg-resumes');
  if (!el) return null;
  return {len: el.innerText.length, extrait: el.innerText.slice(0,260)};
});

// --- SUJETS
await p.evaluate(() => { showPg('subjects'); });
await p.waitForTimeout(900);
out.sujets = await p.evaluate(() => {
  const tabs = document.getElementById('subjTabsPremium');
  const grid = document.getElementById('subjChaptersPremium');
  return {onglets: tabs ? [...tabs.children].map(x=>x.textContent.trim()).slice(-4) : null,
    carte24: grid ? (grid.querySelector('[data-ch24]')||{}).innerText : null};
});
await p.evaluate(() => setSubjectChapterPremium(24));
await p.waitForTimeout(900);
out.sujets.liste = await p.evaluate(() => {
  const el = document.getElementById('pg-subjects');
  return {len: el.innerText.length, extrait: el.innerText.slice(0,300), ch24brut: /chapitre 24/i.test(el.innerText)};
});

// --- QUIZ
await p.evaluate(() => { showPg('quiz'); });
await p.waitForTimeout(900);
out.quiz = await p.evaluate(() => {
  const el = document.getElementById('pg-quiz');
  const btns = [...el.querySelectorAll('.qo-btn')].map(x=>x.textContent.trim().slice(0,40));
  const labs = [...el.querySelectorAll('label')].map(x=>x.textContent.trim()).filter(t=>/Ch\.4|Ch\. 4|année/.test(t));
  return {btns: btns.slice(-5), labs: labs.slice(-4), ch24brut: /chapitre 24/i.test(el.innerText)};
});

// --- FRISE
await p.evaluate(() => { showPg('frise'); });
await p.waitForTimeout(1000);
out.frise = await p.evaluate(() => {
  const el = document.getElementById('pg-frise');
  const sel = el.querySelector('select');
  const sels = [...el.querySelectorAll('select')].map(s=>[...s.options].map(o=>o.value).join(','));
  return {selects: sels.map(x=>x.slice(0,120)), len: el.innerText.length};
});

// --- RECHERCHE
await p.evaluate(() => { showPg('search'); });
await p.waitForTimeout(500);
out.recherche = await p.evaluate(() => {
  const i = document.getElementById('si');
  if (!i) return 'pas de champ';
  i.value = 'groupe de Cairns'; doSearch();
  return document.getElementById('search-res').innerText.slice(0,300);
});
await p.waitForTimeout(400);
out.recherche2 = await p.evaluate(() => {
  const i = document.getElementById('si');
  i.value = 'accord multifibres'; doSearch();
  return document.getElementById('search-res').innerText.slice(0,260);
});

// --- AUTEURS
await p.evaluate(() => { showPg('authors'); });
await p.waitForTimeout(700);
out.auteurs = await p.evaluate(() => {
  const el = document.getElementById('pg-authors');
  const q = document.getElementById('aq') || el.querySelector('input[type=text]');
  if (q) { q.value = 'Kindleberger'; q.dispatchEvent(new Event('input', {bubbles:true})); }
  return el.innerText.length;
});
await p.waitForTimeout(600);
out.auteursRes = await p.evaluate(() => document.getElementById('pg-authors').innerText.slice(0,300));

console.log(JSON.stringify(out, null, 1));
console.log('--- erreurs JS:', errs.length);
errs.slice(0,10).forEach(e=>console.log('  ', e));
await b.close();
