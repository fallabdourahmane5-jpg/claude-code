import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v174.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5200);
const r=await p.evaluate(async ()=>{
  const o={};
  o.clesV83 = Object.keys(window.VISUAL_MAPS_V83||{});
  o.rendu={};
  window.showPg('maps'); await new Promise(r=>setTimeout(r,400));
  for(const ch of [1,9,10,21]){
    window.renderVisualMap(ch); await new Promise(r=>setTimeout(r,450));
    const txt=[...document.querySelectorAll('#visual-map-area .v83-root-t')].map(t=>t.textContent).join(' ');
    const sub=document.getElementById('visual-map-sub')?.textContent||'';
    o.rendu['ch'+ch]={racine:txt.slice(0,70), sousTitre:sub.slice(0,70)};
  }
  return o;
});
console.log('clés VISUAL_MAPS_V83 :', r.clesV83.join(', '));
console.log();
for(const [k,v] of Object.entries(r.rendu)) console.log(`  ${k.padEnd(5)} racine="${v.racine}"  |  ${v.sousTitre}`);
await b.close();
