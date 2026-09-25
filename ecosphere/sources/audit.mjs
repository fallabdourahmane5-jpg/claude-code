import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v175.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5200);
const r=await p.evaluate(()=>{
  const T=window.VISUAL_MAPS_V83||{};
  const CH=(function(){try{return CH_CONTENT}catch(e){return {}}})();
  const MD=(function(){try{return MAP_DATA}catch(e){return {}}})();
  const out=[];
  Object.keys(CH).forEach(k=>{
    out.push({ch:k, carteVisuelle: !!T[k], panneauTexte: !!MD[k],
              replieSur: T[k] ? '—' : 'chapitre 1'});
  });
  return out;
});
console.log('chapitre | carte visuelle | panneau texte | repli');
r.forEach(x=>console.log(`  ${String(x.ch).padEnd(7)} | ${(x.carteVisuelle?'oui':'NON').padEnd(14)} | ${(x.panneauTexte?'oui':'non').padEnd(13)} | ${x.replieSur}`));
await b.close();
