import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
const r = await p.evaluate(()=>{
  const ADV = window.__ECO_ADV_ALL_BANK||[];
  const types={};
  ADV.forEach(q=>{ const k=String(q.ch)+' ('+typeof q.ch+')'; types[k]=(types[k]||0)+1; });
  const QB = window.ECOSPHERE_QUESTION_BANK||{};
  const qbType={}; Object.keys(QB).forEach(k=>{ const s=QB[k][0]; qbType[k]= s? (typeof s.ch)+'/'+(typeof s.chapter) : '?'; });
  return {types, qbType, startQuiz: typeof window.startQuiz};
});
console.log('ADV ch types:'); console.log(JSON.stringify(r.types,null,1));
console.log('QB first-item ch/chapter types:', JSON.stringify(r.qbType));
console.log('startQuiz:', r.startQuiz);
// test startQuiz sur 9,10,21
for (const n of [9,10,21]) {
  const res = await p.evaluate((n)=>{
    try{ window.showPg('quiz'); window.startQuiz(n); }catch(e){ return 'ERREUR '+e; }
    const el=document.getElementById('pg-quiz');
    return (el.innerText||'').slice(0,150).replace(/\s+/g,' ');
  }, n);
  console.log('\nstartQuiz('+n+') →', res);
  await p.waitForTimeout(400);
}
console.log('\nerrors',errs.length,errs);
await b.close();
