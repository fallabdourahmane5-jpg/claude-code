const { chromium } = require('playwright');
const path = require('path');
const C = [
  {n:'ordinateur', v:{width:1440,height:1000}, d:2},
  {n:'ipad',       v:{width:834,height:1112},  d:2},
  {n:'telephone',  v:{width:390,height:844},   d:2},
];
(async () => {
  const nav = await chromium.launch();
  for (const c of C) {
    const p = await (await nav.newContext({viewport:c.v, deviceScaleFactor:c.d,
      isMobile:c.n!=='ordinateur', hasTouch:c.n!=='ordinateur'})).newPage();
    const err=[]; p.on('pageerror',e=>err.push(String(e)));
    await p.goto('file://'+path.resolve('app_v226.html'),{waitUntil:'domcontentloaded',timeout:180000});
    await p.waitForFunction(()=>!!window.__ECO_METHODE,{timeout:180000});
    await p.evaluate(()=>window.showPg('method'));
    await p.waitForSelector('#mt-grille .mt-crit',{timeout:30000});
    await p.waitForTimeout(400);
    const g = await p.evaluate(()=>({
      cartes: document.querySelectorAll('#methodGrid .method-card').length,
      scrollH: document.scrollingElement.scrollWidth,
      vp: window.innerWidth,
      statutsSurLigne: (()=>{const c=document.querySelector('#mt-c-i1');
        const l=c.querySelector('.mt-lib').getBoundingClientRect();
        const s=c.querySelector('.mt-statuts').getBoundingClientRect();
        return s.left >= l.right - 4 ? 'à droite' : 'dessous';})(),
      deborde: [...document.querySelectorAll('#mt-grille *, #mt-fil *')]
        .filter(e=>e.getBoundingClientRect().right > window.innerWidth + 2).length,
    }));
    await p.evaluate(()=>window.__ECO_METHODE.mode('intro','annote'));
    await p.waitForTimeout(350);
    await p.locator('#mt-p-intro').screenshot({path:'meth_'+c.n+'_annote.png'});
    await p.evaluate(()=>document.getElementById('method-eco-grille').scrollIntoView());
    await p.waitForTimeout(250);
    await p.screenshot({path:'meth_'+c.n+'_grille.png'});
    console.log(c.n, JSON.stringify(g), err.length?('ERR '+err[0]):'ok');
    await p.close();
  }
  await nav.close();
})();
