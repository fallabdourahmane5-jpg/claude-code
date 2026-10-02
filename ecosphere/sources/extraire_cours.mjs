import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const dir='/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b=await chromium.launch({args:['--no-sandbox']});
const p=await b.newPage();
await p.goto('file://'+dir+'app_v192.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(9000);
const o=await p.evaluate(()=>{
  const CH=(()=>{try{return CH_CONTENT}catch(e){return {}}})();
  const out={};
  const d=document.createElement('div');
  Object.keys(CH).forEach(k=>{
    d.innerHTML=String(CH[k].cours||'');
    out[k]=(d.textContent||'').replace(/\s+/g,' ').trim();
  });
  return out;
});
fs.writeFileSync(dir+'cours.json', JSON.stringify(o));
console.log(Object.entries(o).map(([k,v])=>k+':'+Math.round(v.length/1024)+'Ko').join(' '));
await b.close();
