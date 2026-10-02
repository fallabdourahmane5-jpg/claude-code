import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const dir = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b = await chromium.launch({ args: ['--no-sandbox'] });

async function sonde(f) {
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e).slice(0, 200)));
  await p.goto('file://' + dir + f, { waitUntil: 'load', timeout: 180000 });
  await p.waitForTimeout(8000);

  // visiter toutes les pages pour declencher les rendus
  await p.evaluate(async () => {
    for (const pg of ['home', 'chapter', 'quiz', 'subjects', 'maps', 'fc', 'search', 'authors', 'prog', 'graphs', 'frise', 'visualisations']) {
      try { showPg(pg); } catch (e) {}
      await new Promise(r => setTimeout(r, 300));
    }
    try { openCh(22); } catch (e) {}
    await new Promise(r => setTimeout(r, 600));
  });

  // libelles residuels sur textContent de chaque conteneur
  const libel = await p.evaluate(() => {
    const out = {};
    document.querySelectorAll('[id^="pg-"]').forEach(el => {
      const t = el.textContent || '';
      const c22 = (t.match(/chapitre\s*22(?![0-9])/gi) || []).length;
      const c21 = (t.match(/chapitre\s*21(?![0-9])/gi) || []).length;
      const b22 = (t.match(/\bch\.?\s*22(?![0-9])/gi) || []).length;
      const b21 = (t.match(/\bch\.?\s*21(?![0-9])/gi) || []).length;
      if (c22 || c21 || b22 || b21) out[el.id] = { c22, c21, b22, b21 };
    });
    out.__an2 = (document.body.textContent.match(/2.{0,3}\s*ann[eé]e/gi) || []).length;
    return out;
  });

  // recherche : on compte les enfants du conteneur de resultats
  const rech = {};
  for (const q of ['mondialisation', 'chaine de valeur', 'Baldwin', 'dumping', 'politique industrielle', 'Ricardo', 'dumping social']) {
    rech[q] = await p.evaluate(async (t) => {
      try { showPg('search'); } catch (e) {}
      const si = document.getElementById('si');
      if (!si) return 'pas de champ';
      si.value = t;
      si.dispatchEvent(new Event('input', { bubbles: true }));
      if (typeof doSearch === 'function') try { doSearch(); } catch (e) { return 'ERR ' + e.message; }
      await new Promise(r => setTimeout(r, 500));
      for (const id of ['search-res', 'sr', 'sres', 'searchResults']) {
        const el = document.getElementById(id);
        if (el) return el.children.length;
      }
      return 'pas de conteneur';
    }, q);
  }

  // en-tete : plus de « Abdourahmane » visible, ligne de sous-titre masquee
  const hero = await p.evaluate(async () => {
    try { showPg('home'); } catch (e) {}
    await new Promise(r => setTimeout(r, 300));
    const vis = [...document.querySelectorAll('body *')].filter(el => (el.textContent || '').trim() === 'Abdourahmane').length;
    const lignes = [...document.querySelectorAll('body *')].filter(el => {
      const t = (el.textContent || '').trim();
      return t.length < 140 && t.includes('TOUS LES CHAPITRES');
    }).map(el => ({ t: el.textContent.trim().slice(0, 60), cache: getComputedStyle(el).display === 'none' }));
    const stat = [...document.querySelectorAll('.stat')].map(s => (s.querySelector('.l')?.textContent || '') + '=' + (s.querySelector('.n')?.textContent || ''));
    return { abdourahmane: vis, lignes, stat };
  });

  await p.close();
  return { libel, rech, hero, errs };
}

const r = {};
for (const f of process.argv.slice(2)) r[f] = await sonde(f);
console.log(JSON.stringify(r, null, 1));
await b.close();
