import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5800);
const r=await p.evaluate(async ()=>{
  window.showPg('fc'); await new Promise(r=>setTimeout(r,1000));
  const g=document.querySelector('#pg-fc .fc-grid');
  const o={enfants:g?g.children.length:0};
  if(g&&g.children[0]) o.exemple=g.children[0].outerHTML.slice(0,320);
  // compter par filtre via le compteur affiche
  o.stats={};
  for(const ch of [0,9,10,21]){
    window.filterFC(ch); await new Promise(r=>setTimeout(r,450));
    const vis=[...g.children].filter(e=>e.offsetParent!==null);
    o.stats[ch]={visibles:vis.length, premiere:vis[0]?vis[0].innerText.split('\n').slice(0,2).join(' / ').slice(0,60):'(aucune)'};
  }
  return o;
});
console.log('enfants de .fc-grid :', r.enfants);
console.log('exemple de carte :', r.exemple);
console.log();
for(const [k,v] of Object.entries(r.stats)) console.log(`  filtre ${k.padStart(2)} → ${String(v.visibles).padStart(5)} visibles · ${v.premiere}`);
await b.close();
