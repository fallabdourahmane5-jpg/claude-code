import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>{
  const G = n => { try { return (new Function('try{return '+n+'}catch(e){return undefined}'))(); } catch(e){ return undefined; } };
  const QB = window.ECOSPHERE_QUESTION_BANK || G('ECOSPHERE_QUESTION_BANK') || {};
  const AB = window.__ECO_ADV_ALL_BANK || {};
  const out = {bank:{}, adv:{}, tags:{}};
  Object.keys(QB).forEach(k=>{ out.bank[k] = QB[k]; });
  Object.keys(AB).forEach(k=>{ out.adv[k] = AB[k]; });
  // étiquettes posées par les couches v221 et antérieures
  const T = G('QUIZ_TAGS') || window.__ECO_QUIZ_TAGS || null;
  if (T) out.tags = T;
  // page quiz : structure actuelle
  out.pageHtml = (document.getElementById('pg-quiz')||{}).innerHTML || '';
  return out;
});
fs.writeFileSync('quiz_actuel.json', JSON.stringify(o));
const n = Object.entries(o.bank).map(([k,v])=>[k, (v||[]).length]);
console.log('banque :', JSON.stringify(Object.fromEntries(n)));
console.log('total', n.reduce((s,x)=>s+x[1],0));
console.log('adv :', JSON.stringify(Object.fromEntries(Object.entries(o.adv).map(([k,v])=>[k,(v||[]).length]))));
console.log('page quiz : %d signes de HTML', o.pageHtml.length);
await b.close();
