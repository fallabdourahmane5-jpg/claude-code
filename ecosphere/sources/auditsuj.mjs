import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5800);
const r=await p.evaluate(()=>{
  const SB=(function(){try{return SUBJECTS_BANK_PREMIUM}catch(e){return []}})();
  const parCh={};
  SB.forEach(s=>{ (parCh[s.chapter]=parCh[s.chapter]||[]).push(s); });
  const stats={};
  Object.keys(parCh).sort((a,b)=>a-b).forEach(k=>{
    const arr=parCh[k];
    const moy=f=>Math.round(arr.reduce((a,s)=>a+((typeof s[f]==='string'?s[f].length:(s[f]||[]).join(' ').length)||0),0)/arr.length);
    stats[k]={n:arr.length, mobiliser:arr[0].mobiliser, champs:Object.keys(arr[0]),
      moyIntro:moy('intro'), moyCom:moy('commentaire'), moyPlan:moy('plan'),
      moyConcl:moy('conclusion'), moyPb:moy('problematique'),
      planItems:Math.round(arr.reduce((a,s)=>a+(s.plan||[]).length,0)/arr.length)};
  });
  return {stats, exemple1:parCh['1']?parCh['1'][0]:null, exemple9:parCh['9']?parCh['9'][0]:null};
});
console.log('ch |  n | champs | mobiliser (1er sujet)               | intro | comm | plan | items | concl');
Object.entries(r.stats).forEach(([k,v])=>{
  console.log(`${k.padStart(3)}| ${String(v.n).padStart(2)} | ${String(v.champs.length).padStart(6)} | ${String(v.mobiliser).slice(0,34).padEnd(34)} | ${String(v.moyIntro).padStart(5)} | ${String(v.moyCom).padStart(4)} | ${String(v.moyPlan).padStart(4)} | ${String(v.planItems).padStart(5)} | ${String(v.moyConcl).padStart(5)}`);
});
fs.writeFileSync('sujets_audit.json', JSON.stringify(r,null,1));
await b.close();
