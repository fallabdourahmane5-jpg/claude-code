import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(1200);
const r = await p.evaluate(()=>{
  const pg=document.getElementById('pg-quiz');
  const sels=[...pg.querySelectorAll('select')].map(s=>({id:s.id, opts:[...s.options].map(o=>o.value+'|'+o.text)}));
  const btns=[...pg.querySelectorAll('button,[onclick]')].map(e=>(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,40)).filter(Boolean);
  return {texte: pg.innerText.slice(0,1800), sels, btns:btns.slice(0,60)};
});
console.log('--- SELECTS ---'); console.log(JSON.stringify(r.sels,null,1));
console.log('--- BOUTONS ---'); console.log(JSON.stringify(r.btns));
console.log('--- TEXTE PAGE ---'); console.log(r.texte);
console.log('errors',errs.length,errs);
await b.close();
