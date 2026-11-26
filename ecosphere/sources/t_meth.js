const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({viewport:{width:1440,height:1000}, deviceScaleFactor:2})).newPage();
  const err=[]; p.on('pageerror',e=>err.push(String(e)));
  await p.goto('file://'+path.resolve(process.argv[2]),{waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_METHODE,{timeout:180000});
  await p.evaluate(()=>window.showPg('method'));
  await p.waitForSelector('#mt-grille .mt-crit',{timeout:30000});

  console.log('critères :', await p.locator('#mt-grille .mt-crit').count(),
              '· groupes :', await p.locator('#mt-grille .mt-grp').count(),
              '· pièces :', await p.locator('#mt-fil .mt-piece').count());
  console.log('statuts offerts (1er critère) :',
    await p.locator('#mt-grille .mt-crit').first().locator('.mt-st').allInnerTexts());
  const naRow = await p.evaluate(()=>{
    const e=document.querySelector('#mt-c-d9');
    return e ? [...e.querySelectorAll('.mt-st')].map(b=>b.textContent) : null;});
  console.log('critère graphique (d9) :', JSON.stringify(naRow));

  // 1. cocher trois critères et vérifier le compteur + la persistance
  await p.locator('#mt-c-i2 .mt-st[data-v="ok"]').click(); await p.waitForTimeout(90);
  await p.locator('#mt-c-i3 .mt-st[data-v="ko"]').click(); await p.waitForTimeout(90);
  await p.locator('#mt-c-i5 .mt-st[data-v="ab"]').click(); await p.waitForTimeout(90);
  console.log('compteur :', (await p.locator('#mt-barre .mt-cpt').innerText()).replace(/\s+/g,' '));
  console.log('mémorisé :', await p.evaluate(()=>localStorage.getItem('eco-autoeval-v226')));
  await p.reload({waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_METHODE,{timeout:180000});
  await p.evaluate(()=>window.showPg('method'));
  await p.waitForSelector('#mt-grille .mt-crit',{timeout:30000});
  console.log('après rechargement :', (await p.locator('#mt-barre .mt-cpt').innerText()).replace(/\s+/g,' '));

  // 2. les deux modes
  const pieces = await p.evaluate(()=>[...document.querySelectorAll('#mt-fil .mt-piece')].map(e=>e.id));
  console.log('pièces :', pieces.join(' · '));
  await p.locator('#mt-p-souspartie [data-mode="annote"]').click(); await p.waitForTimeout(250);
  const sp = await p.evaluate(()=>{
    const e=document.querySelector('#mt-p-souspartie');
    return {marques:e.querySelectorAll('.mt-mark').length,
            notes:e.querySelectorAll('.mt-note[data-n]').length,
            globaux:e.querySelectorAll('.mt-note.glob').length,
            roles:e.querySelectorAll('.mt-role').length};});
  console.log('sous-partie annotée :', JSON.stringify(sp));
  // numéros cohérents ?
  const coh = await p.evaluate(()=>{
    const e=document.querySelector('#mt-p-souspartie');
    const m=[...e.querySelectorAll('.mt-mark')].map(x=>x.getAttribute('data-n'));
    const n=[...e.querySelectorAll('.mt-note[data-n]')].map(x=>x.getAttribute('data-n'));
    const vus=[...e.querySelectorAll('.mt-num')].map(x=>x.textContent);
    return {marques:m.join(','), notes:n.join(','), affichés:vus.join(','),
            appariés:m.every(x=>n.includes(x)) && m.length===new Set(m).size};});
  console.log('appariement marques/notes :', coh.appariés, '| marques', coh.marques, '| notes', coh.notes);

  await p.locator('#mt-p-souspartie [data-mode="copie"]').click(); await p.waitForTimeout(220);
  console.log('mode copie → marques restantes :',
    await p.evaluate(()=>document.querySelectorAll('#mt-p-souspartie .mt-mark').length));

  // 3. critère → passage exact
  await p.locator('#mt-c-d4 [data-ex]').click(); await p.waitForTimeout(600);
  console.log('renvoi d4 :', await p.evaluate(()=>{
    const n=document.querySelector('#mt-p-souspartie .mt-note.vif, #mt-p-souspartie .mt-note[data-k="d4"]');
    return n ? n.querySelector('blockquote').textContent.slice(0,70) : null;}));
  await p.locator('#mt-c-d1 [data-ex]').click(); await p.waitForTimeout(600);
  console.log('renvoi d1 (copie entière) :', await p.evaluate(()=>{
    const n=document.querySelector('#mt-p-plan .mt-note[data-k="d1"]');
    return n ? n.querySelector('p').textContent.slice(0,80) : null;}));

  // 4. aides
  await p.locator('#mt-grille [data-aides]').click(); await p.waitForTimeout(200);
  console.log('aides visibles :', await p.evaluate(()=>
    [...document.querySelectorAll('#mt-grille .mt-aide')].filter(e=>e.offsetParent!==null).length));

  console.log(err.length ? 'ERREURS JS : '+err.slice(0,3).join(' | ') : 'aucune erreur JS');
  await nav.close();
})();
