import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:390,height:844}, isMobile:true, hasTouch:true});
await p.goto('file://' + process.argv[2]); await p.waitForTimeout(14000);
await p.evaluate(()=>showPg('autour')); await p.waitForTimeout(900);
console.log('index:', JSON.stringify(await p.evaluate(()=>{
  const d=document.documentElement;
  return [...document.querySelectorAll('#pg-autour *')]
    .filter(e=>e.getBoundingClientRect().right>d.clientWidth+2)
    .slice(0,6).map(e=>e.tagName+'.'+e.className+' w='+Math.round(e.getBoundingClientRect().width)+' r='+Math.round(e.getBoundingClientRect().right));
})));
await p.evaluate(()=>{ const s=document.getElementById('an-ens'); s.value='28'; s.dispatchEvent(new Event('change')); });
await p.waitForTimeout(500);
await p.evaluate(()=>{[...document.querySelectorAll('.an-it')].find(x=>/offensif/.test(x.textContent)).click();});
await p.waitForTimeout(800);
console.log('dossier:', JSON.stringify(await p.evaluate(()=>{
  const d=document.documentElement;
  return [...document.querySelectorAll('#pg-autour *')]
    .filter(e=>e.getBoundingClientRect().right>d.clientWidth+2)
    .slice(0,8).map(e=>e.tagName+'.'+(e.className||'')+' w='+Math.round(e.getBoundingClientRect().width)+' r='+Math.round(e.getBoundingClientRect().right));
})));
await b.close();
