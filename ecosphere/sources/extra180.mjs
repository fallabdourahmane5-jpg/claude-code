import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(1000);

// "Tout selectionner"
const all = await p.evaluate(async ()=>{
  document.getElementById('adv-select-all').click();
  await new Promise(r=>setTimeout(r,500));
  return {coches:[...document.querySelectorAll('.adv-ch:checked')].map(x=>x.value),
          compteur:(document.getElementById('adv-counter')||{}).textContent};
});
console.log('Tout sélectionner →', JSON.stringify(all.coches), '|', all.compteur);

// Reinitialiser
const rst = await p.evaluate(async ()=>{
  document.getElementById('adv-reset').click();
  await new Promise(r=>setTimeout(r,400));
  return [...document.querySelectorAll('.adv-ch:checked')].length;
});
console.log('Réinitialiser → cases cochées :', rst);

// startQuiz(0) : couverture des chapitres sur 400 tirages
const mix = await p.evaluate(()=>{
  const A = window.__ECO_ADV_ALL_BANK||[];
  const s = new Set(A.map(q=>q.ch));
  return [...s].sort((x,y)=>x-y);
});
console.log('Chapitres présents dans la banque « tous » :', JSON.stringify(mix));

// quiz chapitre 9 jouable : repondre a la 1re question
const jeu = await p.evaluate(async ()=>{
  window.startQuiz(9);
  await new Promise(r=>setTimeout(r,700));
  const opt=document.querySelector('#pg-quiz .opt,#pg-quiz .q-opt,#pg-quiz button.opt');
  if(opt){ opt.click(); await new Promise(r=>setTimeout(r,400)); }
  const t=document.getElementById('pg-quiz').innerText;
  return {aRepondu: !!opt, extrait: t.split('\n').slice(2,7).join(' | ')};
});
console.log('Quiz ch.9 jouable :', jeu.aRepondu, '|', jeu.extrait.slice(0,150));
console.log('\nerrors', errs.length, errs);
await b.close();
