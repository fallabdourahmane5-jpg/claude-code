import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html');
await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const d=document.createElement('div'); d.innerHTML=CH[10].cours;
  const heads=[...d.querySelectorAll('h2,h3,h4')].map(h=>h.tagName+' '+h.textContent.trim());
  const defs=[...d.querySelectorAll('.db')].map(x=>x.textContent.trim().replace(/\s+/g,' ').slice(0,180));
  const auth=[...d.querySelectorAll('.ab')].map(x=>x.textContent.trim().replace(/\s+/g,' ').slice(0,300));
  return {heads,defs,auth};
});
console.log('HEADS:\n'+r.heads.join('\n'));
console.log('\nAUTHORS('+r.auth.length+'):\n'+r.auth.join('\n---\n'));
console.log('\nDEFS('+r.defs.length+'):\n'+r.defs.join('\n'));
await b.close();
