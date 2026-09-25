import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5800);
const r=await p.evaluate(()=>{
  const SB=(function(){try{return SUBJECTS_BANK_PREMIUM}catch(e){return []}})();
  return SB.map(s=>({id:s.id,ch:s.chapter,num:s.num,title:s.title,mob:s.mobiliser,
                     planLen:(s.plan||[]).length, plan6:(s.plan||[]).slice(0,14)}));
});
fs.writeFileSync('sujets_liste.json', JSON.stringify(r,null,1));
const ch6=r.find(x=>x.ch===6);
console.log('--- structure plan ch6 ('+ch6.planLen+' lignes) ---');
ch6.plan6.forEach(l=>console.log('   '+l.slice(0,120)));
console.log('\n--- titres des sujets par chapitre ---');
for(const ch of [1,2,3,4,5,6,7,8]){
  console.log(`\nCHAPITRE ${ch} :`);
  r.filter(x=>x.ch===ch).forEach(s=>console.log(`  [${s.mob.padEnd(22)}] ${s.title}`));
}
await b.close();
