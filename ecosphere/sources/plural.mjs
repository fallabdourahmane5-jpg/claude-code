import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(900);
const out = await p.evaluate(async (list)=>{
  list.forEach(n=>{ const c=document.querySelector('.adv-ch[value="'+n+'"]'); if(c){c.checked=true; c.dispatchEvent(new Event('change'));} });
  await new Promise(r=>setTimeout(r,300));
  document.getElementById('adv-generate').click();
  await new Promise(r=>setTimeout(r,900));
  const t=document.getElementById('pg-quiz').innerText;
  return t.split('\n').filter(l=>/Chapitres?\s/i.test(l)).slice(0,4);
}, [9,10,21]);
console.log('lignes « Chapitre(s) » :', JSON.stringify(out,null,1));
// et avec seulement 21
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(700);
const out2 = await p.evaluate(async ()=>{
  const c=document.querySelector('.adv-ch[value="21"]'); if(c){c.checked=true; c.dispatchEvent(new Event('change'));}
  await new Promise(r=>setTimeout(r,300));
  document.getElementById('adv-generate').click();
  await new Promise(r=>setTimeout(r,900));
  return document.getElementById('pg-quiz').innerText.split('\n').filter(l=>/Chapitres?\s/i.test(l)).slice(0,4);
});
console.log('seul 21 :', JSON.stringify(out2,null,1));
await b.close();
