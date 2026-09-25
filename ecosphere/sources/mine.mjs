import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v176.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(()=>{
  const CH=(function(){try{return CH_CONTENT}catch(e){return {}}})();
  const out={};
  [9,10,21].forEach(k=>{
    const div=document.createElement('div'); div.innerHTML=CH[k].cours;
    out[k]=div.innerText.replace(/\s+/g,' ');
  });
  return out;
});
fs.writeFileSync('cours_texte.json', JSON.stringify(r));
for(const [k,v] of Object.entries(r)) console.log(`chapitre ${k} : ${v.length} caractères de texte`);
await b.close();
