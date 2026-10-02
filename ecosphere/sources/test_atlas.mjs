import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const dir = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const f = process.argv[2] || 'app_v192.html';
const b = await chromium.launch({ args: ['--no-sandbox'] });
const p = await b.newPage({ viewport: { width: 1500, height: 1000 } });
const errs = [];
p.on('pageerror', e => errs.push(String(e).slice(0, 220)));
await p.goto('file://' + dir + f, { waitUntil: 'load', timeout: 180000 });
await p.waitForTimeout(9000);

const r = {};

r.nav = await p.evaluate(() => [...document.querySelectorAll('nav .nt')].map(x => x.textContent.trim()));
r.pages = await p.evaluate(() => [...document.querySelectorAll('.pg')].map(x => x.id));

// ouvrir l'Atlas
r.ouverture = await p.evaluate(async () => {
  showPg('atlas');
  await new Promise(r => setTimeout(r, 700));
  const pg = document.getElementById('pg-atlas');
  return {
    visible: !!pg && pg.classList.contains('on'),
    ongletActif: [...document.querySelectorAll('nav .nt.on')].map(x => x.textContent.trim()),
    compteur: (document.getElementById('at-nb') || {}).textContent,
    annees: [...document.querySelectorAll('#at-liste .at-year')].map(x => x.textContent),
    chapitres: [...document.querySelectorAll('#at-liste .at-ch')].map(x => ({
      lib: x.querySelector('.at-chn').textContent,
      n: x.querySelectorAll('.at-card').length,
    })),
    cartes: document.querySelectorAll('#at-liste .at-card').length,
  };
});

// déplier une carte et vérifier les 5 blocs
r.carte = await p.evaluate(async () => {
  document.querySelectorAll('#at-liste .at-ch').forEach(c => c.classList.add('open'));
  const t = document.querySelector('#at-liste .at-card .at-ch2');
  t.click();
  await new Promise(r => setTimeout(r, 350));
  const card = t.parentNode;
  const q = s => { const e = card.querySelector(s); return e ? e.textContent.trim().length : 0; };
  return {
    id: card.id,
    auteur: card.querySelector('.at-nom').textContent.trim(),
    idee: card.querySelector('.at-idee').textContent.trim(),
    affirme: q('.at-bl:nth-of-type(1) .at-txt'),
    blocs: [...card.querySelectorAll('.at-body .at-lab')].map(x => x.textContent.trim()),
    ouvrage: (card.querySelector('.at-bl.ou') || {}).textContent || '',
    liens: card.querySelectorAll('.at-lien').length,
    boutons: [...card.querySelectorAll('.at-go button')].map(x => x.textContent.trim()),
    longueurTotale: card.querySelector('.at-body').textContent.length,
  };
});

// recherche
r.recherche = {};
for (const q of ['destruction créatrice', 'courbe du sourire', 'capabilités', 'coûts de transaction', 'zone d incertitude', 'xyzzy']) {
  r.recherche[q] = await p.evaluate(async (t) => {
    const i = document.getElementById('at-q');
    i.value = t; i.dispatchEvent(new Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 250));
    return {
      n: document.querySelectorAll('#at-liste .at-card').length,
      cpt: document.getElementById('at-nb').textContent,
      premier: (document.querySelector('#at-liste .at-nom') || {}).textContent || '',
    };
  }, q);
}

// filtres
r.filtres = await p.evaluate(async () => {
  const set = async (id, v) => {
    const e = document.getElementById(id); e.value = v;
    e.dispatchEvent(new Event(id === 'at-q' ? 'input' : 'change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 220));
  };
  const out = {};
  await set('at-q', '');
  await set('at-an', '2');
  out.annee2 = document.querySelectorAll('#at-liste .at-card').length;
  await set('at-an', '');
  await set('at-ch', '22');
  out.ch22 = document.querySelectorAll('#at-liste .at-card').length;
  await set('at-ch', '');
  await set('at-au', 'Karl Marx');
  out.marx = [...document.querySelectorAll('#at-liste .at-ch')].map(x => x.querySelector('.at-chn').textContent);
  await set('at-au', '');
  await set('at-no', 'institutions');
  out.notionInstitutions = document.querySelectorAll('#at-liste .at-card').length;
  await set('at-no', '');
  out.nbOptionsAuteur = document.getElementById('at-au').options.length - 1;
  out.nbOptionsNotion = document.getElementById('at-no').options.length - 1;
  out.total = document.querySelectorAll('#at-liste .at-card').length;
  return out;
});

// auteur multi-chapitres : lien « sert aussi en »
r.multi = await p.evaluate(async () => {
  const i = document.getElementById('at-q');
  i.value = 'destruction créatrice'; i.dispatchEvent(new Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 250));
  const a = document.querySelector('#at-liste .at-aussi a');
  const txt = (document.querySelector('#at-liste .at-aussi') || {}).textContent || '';
  if (!a) return { txt, saut: null };
  const cible = a.getAttribute('data-go');
  a.click();
  await new Promise(r => setTimeout(r, 600));
  const c = document.getElementById(cible);
  return { txt: txt.trim(), cible, ouvert: !!c && c.classList.contains('open'), auteur: c ? c.querySelector('.at-nom').textContent.trim() : null };
});

// liens entre idées
r.lienIdee = await p.evaluate(async () => {
  const bt = document.getElementById('at-rz'); bt.click();
  await new Promise(r => setTimeout(r, 300));
  document.querySelectorAll('#at-liste .at-ch').forEach(c => c.classList.add('open'));
  const t = document.querySelector('#at-liste .at-card .at-ch2'); t.click();
  await new Promise(r => setTimeout(r, 300));
  const b = t.parentNode.querySelector('.at-lien b[data-go]');
  if (!b) return null;
  const cible = b.getAttribute('data-go');
  b.click();
  await new Promise(r => setTimeout(r, 600));
  const c = document.getElementById(cible);
  return { cible, ouvert: !!c && c.classList.contains('open'), auteur: c ? c.querySelector('.at-nom').textContent.trim() : null };
});

// liens vers cours / fiches / sujets / auteurs
r.liens = await p.evaluate(async () => {
  const out = {};
  const prep = async () => {
    showPg('atlas'); await new Promise(r => setTimeout(r, 250));
    document.getElementById('at-rz').click(); await new Promise(r => setTimeout(r, 250));
    document.querySelectorAll('#at-liste .at-ch').forEach(c => c.classList.add('open'));
    const t = document.querySelector('#at-liste .at-card .at-ch2');
    if (!t.parentNode.classList.contains('open')) t.click();
    await new Promise(r => setTimeout(r, 250));
    return t.parentNode;
  };
  let card = await prep();
  card.querySelector('[data-cours]').click();
  await new Promise(r => setTimeout(r, 600));
  out.cours = { page: [...document.querySelectorAll('.pg.on')].map(x => x.id), titre: (document.getElementById('cv-title') || {}).textContent };
  card = await prep();
  card.querySelector('[data-fc]').click();
  await new Promise(r => setTimeout(r, 700));
  out.fiches = { page: [...document.querySelectorAll('.pg.on')].map(x => x.id), cartes: document.querySelectorAll('#fc-grid .fc').length };
  card = await prep();
  card.querySelector('[data-suj]').click();
  await new Promise(r => setTimeout(r, 900));
  out.sujets = { page: [...document.querySelectorAll('.pg.on')].map(x => x.id) };
  card = await prep();
  card.querySelector('[data-aut]').click();
  await new Promise(r => setTimeout(r, 700));
  out.auteur = { page: [...document.querySelectorAll('.pg.on')].map(x => x.id) };
  return out;
});

// autres sections intactes
r.autres = await p.evaluate(async () => {
  const out = {};
  for (const pg of ['home', 'quiz', 'fc', 'search', 'authors', 'subjects', 'maps', 'formulas', 'prog', 'graphs', 'method', 'visualisations', 'frise']) {
    try { showPg(pg); } catch (e) { out[pg] = 'ERR'; continue; }
    await new Promise(r => setTimeout(r, 300));
    const el = document.getElementById('pg-' + pg);
    out[pg] = el ? el.textContent.trim().length : 'absent';
  }
  return out;
});

// recherche globale du site
r.rechercheSite = await p.evaluate(async () => {
  showPg('search'); await new Promise(r => setTimeout(r, 300));
  const out = {};
  for (const t of ['destruction créatrice', 'courbe du sourire', 'Crozier', 'Mazzucato']) {
    const si = document.getElementById('si');
    si.value = t; si.dispatchEvent(new Event('input', { bubbles: true }));
    if (typeof doSearch === 'function') doSearch();
    await new Promise(r => setTimeout(r, 400));
    const res = document.getElementById('search-res');
    out[t] = res ? res.children.length : -1;
  }
  return out;
});

r.chronologie = await p.evaluate(() => ({
  nav: [...document.querySelectorAll('nav .nt')].some(x => /Chronologie/i.test(x.textContent)),
  page: !!document.getElementById('pg-timeline'),
}));

r.erreurs = errs;
console.log(JSON.stringify(r, null, 1));
await b.close();
