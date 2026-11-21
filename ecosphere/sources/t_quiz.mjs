import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage();
await p.setViewportSize({width:1280, height:900});
const err=[]; p.on('pageerror',e=>err.push(String(e).slice(0,200)));
p.on('dialog', d=>d.accept());
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
await p.evaluate(()=>window.showPg('quiz'));
await p.waitForTimeout(1500);
const d = await p.evaluate(()=>{
  const z=document.getElementById('pg-quiz');
  return {signes:(z.innerText||'').length, tete:(z.innerText||'').replace(/\s+/g,' ').slice(0,260),
    api: !!window.__ECO_QUIZ, n: window.__ECO_QUIZ ? window.__ECO_QUIZ.banque.length : 0,
    chips: z.querySelectorAll('.qz-chip').length};
});
console.log(JSON.stringify(d,null,1));
await p.screenshot({path:'q_accueil.png'});
// lancer une série
// on force une série de QCM pour éprouver le rendu complet
await p.evaluate(()=>{ window.__ECO_QUIZ.F.type=['qcm']; window.__ECO_QUIZ.accueil(); });
await p.waitForTimeout(600);
await p.evaluate(()=>{ document.getElementById('qz-start').click(); });
await p.waitForTimeout(1200);
const q1 = await p.evaluate(()=>{
  const z=document.getElementById('pg-quiz');
  return {t:(z.innerText||'').replace(/\s+/g,' ').slice(0,300), opts:z.querySelectorAll('.qz-opt').length};
});
console.log(JSON.stringify(q1,null,1));
await p.screenshot({path:'q_question.png'});
// répondre
await p.evaluate(()=>{ const o=document.querySelector('.qz-opt'); if(o) o.click(); document.getElementById('qz-val').click(); });
await p.waitForTimeout(900);
const c1 = await p.evaluate(()=>{
  const z=document.getElementById('qz-corr');
  return {corr:(z.innerText||'').replace(/\s+/g,' ').slice(0,300), src: !!document.querySelector('.qz-src')};
});
console.log(JSON.stringify(c1,null,1));
await p.screenshot({path:'q_corr.png'});
console.log('erreurs JS', err.length, JSON.stringify(err.slice(0,5)));
await b.close();
