import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v200.html',{waitUntil:'load',timeout:240000});
await p.waitForTimeout(16000);
const r = await p.evaluate(()=>{
  const o={};
  Object.keys(CH_CONTENT).forEach(k=>{
    const c=CH_CONTENT[k];
    const d=document.createElement('div'); d.innerHTML=c.cours||'';
    const h=[...d.querySelectorAll('h2,h3,h4')].map(x=>x.tagName+'|'+x.textContent.trim().replace(/\s+/g,' '));
    o[k]={titre:c.title, nH:h.length, plan:h, nNotions:(c.notions||[]).length};
  });
  return o;
});
let out='';
for (const k of Object.keys(r)) {
  out += '\n\n########## CHAPITRE '+k+' — '+r[k].titre+'  ('+r[k].nH+' titres, '+r[k].nNotions+' notions)\n'
       + r[k].plan.join('\n');
}
fs.writeFileSync('plan_chapitres.txt', out.trim());
console.log(Object.keys(r).map(k=>k+':'+r[k].nH).join(' '));
await b.close();
