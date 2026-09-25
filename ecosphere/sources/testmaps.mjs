import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v175.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(async ()=>{
  const o={cles:Object.keys(window.VISUAL_MAPS_V83||{}), rendu:{}};
  window.showPg('maps'); await new Promise(r=>setTimeout(r,500));
  for(const ch of [1,2,9,10,21]){
    window.renderVisualMap(ch); await new Promise(r=>setTimeout(r,550));
    const a=document.getElementById('visual-map-area');
    o.rendu['ch'+ch]={
      racine:[...a.querySelectorAll('.v83-root-t')].map(t=>t.textContent).join(' ').slice(0,60),
      main:[...a.querySelectorAll('.v83-main-t')].map(t=>t.textContent).slice(0,3),
      nbNoeuds:a.querySelectorAll('.v83-node').length,
      sousTitre:(document.getElementById('visual-map-sub')?.textContent||'').slice(0,60)
    };
  }
  return o;
});
console.log('clés VISUAL_MAPS_V83 :', r.cles.join(', '));
console.log();
for(const [k,v] of Object.entries(r.rendu)){
  console.log(`  ${k.padEnd(5)} ${String(v.nbNoeuds).padStart(3)} nœuds | racine="${v.racine}"`);
  console.log(`        branches: ${v.main.join(' / ')}`);
}
console.log('\nERREURS JS :', errs.length); [...new Set(errs)].slice(0,4).forEach(e=>console.log('  - '+e));
await b.close();
