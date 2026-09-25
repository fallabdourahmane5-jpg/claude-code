import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5800);
const r=await p.evaluate(async ()=>{
  const o={};
  window.showPg('fc'); await new Promise(r=>setTimeout(r,1000));
  const grid=document.querySelector('#pg-fc .fc-grid, #pg-fc .fcg, #pg-fc .grid') || document.getElementById('pg-fc');
  o.classeGrille=grid.className||grid.id;
  for(const ch of [0,1,9,10,21]){
    window.filterFC(ch); await new Promise(r=>setTimeout(r,500));
    const cartes=[...document.querySelectorAll('#pg-fc [class*="fc"]')].filter(e=>e.className.match(/card|flash/i));
    const visibles=cartes.filter(e=>e.offsetParent!==null);
    // premiere carte visible
    const t=visibles[0]?visibles[0].innerText.split('\n')[0].slice(0,50):'(aucune)';
    o['filtre_'+ch]={total:cartes.length, visibles:visibles.length, premiere:t};
  }
  return o;
});
console.log('grille :', r.classeGrille);
for(const [k,v] of Object.entries(r)) if(k.startsWith('filtre_'))
  console.log(`  ${k.padEnd(12)} visibles=${String(v.visibles).padStart(5)} / ${String(v.total).padStart(5)}  · ${v.premiere}`);
console.log('ERREURS :', errs.length);
await p.evaluate(async()=>{window.showPg('fc'); await new Promise(r=>setTimeout(r,500)); window.filterFC(21); await new Promise(r=>setTimeout(r,600));});
await p.waitForTimeout(400); await p.screenshot({path:'fc_ch21.png'});
await b.close();
