const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const nav = await chromium.launch();
  const ctx = await nav.newContext({viewport:{width:1440,height:1000}, deviceScaleFactor:1});
  const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(String(e)));
  p.on('dialog', d => d.accept());
  await p.goto('file://' + path.resolve('app_v225.html'), {waitUntil:'domcontentloaded', timeout:180000});
  await p.waitForFunction(() => !!window.__ECO_COURBES, {timeout:180000});
  await p.evaluate(() => window.showPg('graphs'));
  await p.waitForSelector('#pg-graphs .cb-vign', {timeout:30000});

  const ids = await p.evaluate(() => window.__ECO_COURBES.fiches.map(f => f.id));
  console.log('fiches :', ids.length, '· vignettes :', await p.locator('#pg-graphs .cb-vign').count());

  // --- 1. chaque fiche : toutes les étapes de toutes les variantes
  const pb = [];
  for (const id of ids) {
    const r = await p.evaluate(i => {
      const C = window.__ECO_COURBES, f = C.fiches.filter(x => x.id === i)[0];
      const jeux = f.variantes ? f.variantes.map(v => v.etapes) : [f.etapes || []];
      const out = {hors: 0, vides: 0, n: 0};
      jeux.forEach(ets => {
        for (let k = 0; k < ets.length; k++) {
          const st = C.calc(f, ets, k);
          out.n++;
          if (!st.series.length) out.vides++;
          st.series.forEach(s => {
            for (let q = 0; q < s.p.length; q += 2) {
              if (s.p[q] < -0.12 || s.p[q] > 1.14 ||
                  s.p[q+1] < -0.12 || s.p[q+1] > 1.14) out.hors++;
            }
          });
        }
      });
      return out;
    }, id);
    if (r.hors || r.vides) pb.push(id + ' hors=' + r.hors + ' vides=' + r.vides);
  }
  console.log(pb.length ? 'ÉTATS À REPRENDRE :\n  ' + pb.join('\n  ') : 'états : tous valides');

  // --- 2. ouverture réelle de chaque fiche + dernière étape + rendu SVG
  const rendus = [];
  for (const id of ids) {
    await p.evaluate(i => window.__ECO_COURBES.ouvrir(i), id);
    await p.waitForSelector('#cb-fig svg', {timeout:15000});
    const n = await p.evaluate(() => document.querySelectorAll('#cb-suiv').length);
    if (n) { for (let k = 0; k < 12; k++) {
      const off = await p.evaluate(() => document.querySelector('#cb-suiv').disabled);
      if (off) break;
      await p.locator('#cb-suiv').click(); await p.waitForTimeout(25);
    } }
    const info = await p.evaluate(() => {
      const svg = document.querySelector('#cb-fig svg');
      return {paths: svg.querySelectorAll('path,line,circle').length,
              textes: svg.querySelectorAll('text').length,
              liens: document.querySelectorAll('#pg-graphs .cb-lien').length};
    });
    if (info.paths < 4 || !info.liens) rendus.push(id + ' ' + JSON.stringify(info));
  }
  console.log(rendus.length ? 'RENDUS FAIBLES :\n  ' + rendus.join('\n  ') : 'rendus : tous corrects');

  // --- 3. boutons de la fiche
  await p.evaluate(() => window.__ECO_COURBES.ouvrir('mundell-monetaire'));
  await p.waitForSelector('#cb-fig svg');
  const outils = await p.evaluate(() => ({
    cmp: !!document.querySelector('#cb-cmp'), sel: !!document.querySelector('#cb-sel-var'),
    main: !!document.querySelector('#cb-main'), raz: !!document.querySelector('#cb-raz2'),
    zoom: !!document.querySelector('#cb-plus'), plein: !!document.querySelector('#cb-plein')}));
  console.log('outils IS-LM-BP :', JSON.stringify(outils));
  await p.locator('#cb-cmp').click(); await p.waitForTimeout(200);
  console.log('comparer → figures :', await p.locator('#cb-fig .cb-fig-cel').count());
  await p.locator('#cb-cmp').click(); await p.waitForTimeout(150);

  // --- 4. refaire à la main
  await p.locator('#cb-main').click(); await p.waitForTimeout(200);
  const vide = await p.evaluate(() => document.querySelectorAll('#cb-fig svg path').length);
  const rev = await p.evaluate(() => !!document.querySelector('#cb-rev'));
  console.log('mode main → tracés restants :', vide, '· bouton révéler :', rev);
  if (rev) { await p.locator('#cb-rev').click(); await p.waitForTimeout(200);
    console.log('après révélation → tracés :', await p.evaluate(() => document.querySelectorAll('#cb-fig svg path').length)); }

  // --- 5. zoom, vue initiale, plein écran
  await p.locator('#cb-plus').click(); await p.waitForTimeout(120);
  const vb1 = await p.evaluate(() => document.querySelector('#cb-fig svg').getAttribute('viewBox'));
  await p.locator('#cb-vue').click(); await p.waitForTimeout(120);
  const vb2 = await p.evaluate(() => document.querySelector('#cb-fig svg').getAttribute('viewBox'));
  console.log('zoom :', vb1, '→ vue initiale :', vb2);
  await p.locator('#cb-plein').click(); await p.waitForTimeout(300);
  console.log('plein écran :', await p.locator('.cb-plein').count());
  await p.locator('#cbp-fin').click(); await p.waitForTimeout(200);

  // --- 6. lien vers le cours
  await p.evaluate(() => window.__ECO_COURBES.ouvrir('courbe-is'));
  await p.waitForSelector('#pg-graphs .cb-lien');
  await p.locator('#pg-graphs .cb-lien').first().click();
  await p.waitForTimeout(1400);
  const dest = await p.evaluate(() => {
    const v = document.querySelector('.eco-vise, [data-vise], mark');
    return {page: (document.querySelector('.pg.show, .page.show, [id^=pg-]:not([hidden])')||{}).id,
            texte: document.body.innerText.slice(0, 0) + (v ? v.textContent.slice(0,60) : ''),
            ch: (window.CURRENT_CH || '?')};
  });
  console.log('lien cours →', JSON.stringify(dest));

  console.log(err.length ? 'ERREURS JS : ' + err.slice(0,4).join(' | ') : 'aucune erreur JS');
  await nav.close();
})();
