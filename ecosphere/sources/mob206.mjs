import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:390,height:844}, isMobile:true, hasTouch:true});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]); await p.waitForTimeout(14000);
await p.evaluate(()=>showPg('autour')); await p.waitForTimeout(1000);
const idx = await p.evaluate(()=>({scrollW:document.documentElement.scrollWidth, clientW:document.documentElement.clientWidth}));
await p.evaluate(()=>{ const s=document.getElementById('an-ens'); s.value='28'; s.dispatchEvent(new Event('change')); });
await p.waitForTimeout(600);
await p.evaluate(()=>{[...document.querySelectorAll('.an-it')].find(x=>/offensif/.test(x.textContent)).click();});
await p.waitForTimeout(900);
const dos = await p.evaluate(()=>{
  const d=document.documentElement;
  const deb=[...document.querySelectorAll('#pg-autour *')].filter(e=>e.getBoundingClientRect().right>d.clientWidth+4).length;
  return {scrollW:d.scrollWidth, clientW:d.clientWidth, debordent:deb, tab:document.querySelectorAll('.an-tab tr').length};
});
console.log(JSON.stringify({idx,dos},null,1)); console.log('erreurs',errs.length,errs.slice(0,3));
await b.close();
