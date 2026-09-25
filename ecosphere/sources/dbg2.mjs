import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
const logs=[]; p.on('console',m=>logs.push(m.text().slice(0,160)));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(6000);
const r=await p.evaluate(async ()=>{
  window.showPg('fc'); await new Promise(r=>setTimeout(r,1500));
  const o={};
  o.filterFCwrapped = !!(window.filterFC && window.filterFC.__a2wrapped);
  o.renderFCwrapped = !!(window.renderFC && window.renderFC.__a2wrapped);
  o.grille = !!document.querySelector('#pg-fc .fc-grid');
  // appliquer manuellement pour confirmer que ca marche
  const bs=document.querySelectorAll('#pg-fc .fc-grid .fc-badge');
  let n=0;
  bs.forEach(x=>{ const t=x.textContent; const nt=t.replace(/\bCH\.?\s*21\b/i,'2ᵉ ANNÉE · CH.1'); if(nt!==t){x.textContent=nt;n++;} });
  o.remplacesManuellement=n;
  o.apres=[...document.querySelectorAll('#pg-fc .fc-badge')].filter(x=>/CH\.?\s*21/i.test(x.textContent)).length;
  return o;
});
console.log(JSON.stringify(r,null,1));
console.log('console:', logs.filter(l=>/err|Err|fail/i.test(l)).slice(0,4));
await b.close();
