import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:390,height:844}, isMobile:true, hasTouch:true});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const pages = ['home','chapter','fc','maps','atlas','subjects','quiz','frise','authors','search'];
const out={};
for (const id of pages) {
  await p.evaluate((id)=>showPg(id==='chapter'?'chapter':id), id);
  if (id==='chapter') await p.evaluate(()=>openCh(24));
  await p.waitForTimeout(900);
  out[id] = await p.evaluate(()=>{
    const d=document.documentElement;
    const deb = [...document.querySelectorAll('.pg.on *')].filter(e=>e.getBoundingClientRect().right > d.clientWidth+4).length;
    return {scrollW:d.scrollWidth, clientW:d.clientWidth, debordent:deb};
  });
}
await p.evaluate(()=>{ ouvrirChiffres('24'); });
await p.waitForTimeout(900);
out.chiffres = await p.evaluate(()=>({scrollW:document.documentElement.scrollWidth, clientW:document.documentElement.clientWidth}));
await p.evaluate(()=>{ ouvrirResume('24'); });
await p.waitForTimeout(900);
out.resumes = await p.evaluate(()=>({scrollW:document.documentElement.scrollWidth, clientW:document.documentElement.clientWidth}));
console.log(JSON.stringify(out,null,1));
console.log('erreurs', errs.length, errs.slice(0,5));
await b.close();
