import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v178.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(6000);
const r=await p.evaluate(()=>{
  const SB=(function(){try{return SUBJECTS_BANK_PREMIUM}catch(e){return []}})();
  return SB.filter(s=>!s.mobiliser||String(s.mobiliser).trim().length<5)
           .map(s=>({id:s.id, ch:s.chapter, num:s.num, title:s.title, mob:String(s.mobiliser||'')}));
});
r.forEach(s=>console.log(`${s.id.padEnd(9)} ch${String(s.ch).padStart(2)} mob="${s.mob}"  ${s.title}`));
console.log('total :', r.length);
await b.close();
