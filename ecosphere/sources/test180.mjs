import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(1200);

let r = await p.evaluate(()=>{
  const cases=[...document.querySelectorAll('#adv-chapters .adv-ch')].map(x=>x.value+':'+x.closest('.smart-check').textContent.trim());
  const btns=[...document.querySelectorAll('#pg-quiz .quiz-options-grid .qo-btn')].map(x=>(x.getAttribute('onclick')||'')+' → '+x.textContent.trim().replace(/\s+/g,' ').slice(0,52));
  return {cases, btns};
});
console.log('=== CASES A COCHER ('+r.cases.length+') ===');
r.cases.forEach(c=>console.log('  '+c));
console.log('\n=== ACCES RAPIDE ('+r.btns.length+') ===');
r.btns.forEach(c=>console.log('  '+c));

// cocher ch 9 + 10 + 21 et verifier le compteur / les tags
const sel = await p.evaluate(async ()=>{
  [9,10,21].forEach(n=>{ const c=document.querySelector('.adv-ch[value="'+n+'"]'); if(c){c.checked=true; c.dispatchEvent(new Event('change'));} });
  await new Promise(r=>setTimeout(r,400));
  return {
    compteur: (document.getElementById('adv-counter')||{}).textContent,
    tags: [...document.querySelectorAll('#adv-tags .adv-tag')].map(t=>t.textContent.trim().replace(/\s+/g,' ')).slice(0,14)
  };
});
console.log('\n=== 9+10+21 COCHES ===');
console.log('compteur :', sel.compteur);
console.log('tags     :', JSON.stringify(sel.tags));

// generer le quiz
const gen = await p.evaluate(async ()=>{
  document.getElementById('adv-generate').click();
  await new Promise(r=>setTimeout(r,800));
  return document.getElementById('pg-quiz').innerText.slice(0,220).replace(/\s+/g,' ');
});
console.log('\n=== GENERATION ===\n', gen);
console.log('\nerrors', errs.length, errs);
await b.close();
