const { chromium, devices } = require('playwright');
const path = require('path');
const CIBLES = [
  {n:'ordinateur', v:{width:1440,height:1000}, d:2},
  {n:'ipad',       v:{width:834,height:1112},  d:2},
  {n:'telephone',  v:{width:390,height:844},   d:2},
];
(async () => {
  const nav = await chromium.launch();
  for (const c of CIBLES) {
    const p = await (await nav.newContext({viewport:c.v, deviceScaleFactor:c.d,
      isMobile:c.n!=='ordinateur', hasTouch:c.n!=='ordinateur'})).newPage();
    const err=[]; p.on('pageerror',e=>err.push(String(e)));
    await p.goto('file://'+path.resolve('app_v225.html'),{waitUntil:'domcontentloaded',timeout:180000});
    await p.waitForFunction(()=>!!window.__ECO_COURBES,{timeout:180000});
    await p.evaluate(()=>window.showPg('graphs'));
    await p.waitForSelector('#pg-graphs .cb-vign',{timeout:30000});
    await p.waitForTimeout(400);
    await p.screenshot({path:'cb_'+c.n+'_catalogue.png'});
    await p.evaluate(()=>window.__ECO_COURBES.ouvrir('mundell-budgetaire'));
    await p.waitForSelector('#cb-fig svg',{timeout:20000});
    for (let k=0;k<2;k++){ await p.locator('#cb-suiv').click(); await p.waitForTimeout(120); }
    await p.waitForTimeout(300);
    await p.screenshot({path:'cb_'+c.n+'_fiche.png'});
    // le tracé ne doit jamais être recouvert par le texte
    const geo = await p.evaluate(()=>{
      const fig=document.querySelector('#cb-fig'), col=document.querySelector('#pg-graphs .cb-fiche');
      const svg=fig.querySelector('svg');
      const rf=svg.getBoundingClientRect();
      const blocs=[...document.querySelectorAll('#pg-graphs .cb-bloc')].map(b=>b.getBoundingClientRect());
      const chevauche = blocs.filter(b=> b.left < rf.right-4 && b.right > rf.left+4 &&
                                         b.top < rf.bottom-4 && b.bottom > rf.top+4).length;
      return {largeurSvg:Math.round(rf.width), hauteurSvg:Math.round(rf.height),
              colonnes:getComputedStyle(col).gridTemplateColumns,
              chevauchements:chevauche,
              scrollH:document.scrollingElement.scrollWidth,
              vp:window.innerWidth};
    });
    await p.locator('#cb-cmp').click(); await p.waitForTimeout(400);
    await p.screenshot({path:'cb_'+c.n+'_comparer.png'});
    console.log(c.n, JSON.stringify(geo), err.length?('ERR '+err[0]):'ok');
    await p.close();
  }
  await nav.close();
})();
