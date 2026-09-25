import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
await p.evaluate(()=>window.showPg && window.showPg('subjects'));
await p.waitForTimeout(900);
// find clickable element referencing ch10-7
const info = await p.evaluate(()=>{
  const fns=Object.keys(window).filter(k=>typeof window[k]==='function' && /subj|sujet/i.test(k));
  const el=[...document.querySelectorAll('#pg-subjects [onclick]')].slice(0,3).map(e=>e.getAttribute('onclick').slice(0,90));
  return {fns:fns.slice(0,15), el};
});
console.log(JSON.stringify(info,null,1));
await b.close();
