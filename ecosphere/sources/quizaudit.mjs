import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
const r = await p.evaluate(()=>{
  const out={};
  // trouver toutes les banques de quiz
  const names=['QUIZ_BANK','QUIZ_BANK_PREMIUM','QUIZ_ADVANCED','QUIZ_BANK_ADV','QUIZZES','QUIZ_DATA','QUIZ_BANK_V2'];
  const found={};
  names.forEach(n=>{ try{ const v=eval(n); if(v) found[n]=Array.isArray(v)?v.length:Object.keys(v).length; }catch(e){} });
  out.banques=found;
  // repartition par chapitre
  function rep(arr){ const d={}; arr.forEach(q=>{ const c=String(q.chapter!=null?q.chapter:(q.ch!=null?q.ch:'?')); d[c]=(d[c]||0)+1; }); return d; }
  try{ out.quiz = rep(eval('QUIZ_BANK')); }catch(e){ out.quizErr=String(e).slice(0,80); }
  try{ out.adv  = rep(eval('QUIZ_ADVANCED')); }catch(e){ out.advErr=String(e).slice(0,80); }
  // chapitres existants
  try{ out.chapitres = Object.keys(eval('CH_CONTENT')); }catch(e){}
  return out;
});
console.log(JSON.stringify(r,null,1));
console.log('errors',errs.length);
await b.close();
