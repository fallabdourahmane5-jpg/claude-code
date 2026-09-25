import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(6000);
const r=await p.evaluate(async ()=>{
  window.showPg('fc'); await new Promise(r=>setTimeout(r,1200));
  const o={};
  o.patchCharge = !!window.__ECO_MAJ_FRA;
  o.nbBadges = document.querySelectorAll('#pg-fc .fc-badge').length;
  o.badges21 = [...document.querySelectorAll('#pg-fc .fc-badge')].filter(x=>/21/.test(x.textContent)).length;
  o.exemple21 = [...document.querySelectorAll('#pg-fc .fc-badge')].filter(x=>/21/.test(x.textContent))[0]?.textContent;
  // test manuel du remplacement
  const t = o.exemple21 || '';
  o.testRegex = t.replace(/\bCH\.?\s*21\b/i, '2ᵉ ANNÉE · CH.1');
  return o;
});
console.log(JSON.stringify(r,null,1));
await b.close();
