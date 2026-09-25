import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4500);
const r = await p.evaluate(()=>{
  const QB = window.ECOSPHERE_QUESTION_BANK||{};
  const base={}; Object.keys(QB).forEach(k=>base[k]=QB[k].length);
  const ADV = window.__ECO_ADV_ALL_BANK||[];
  const adv={}; ADV.forEach(q=>{ const c=String(q.chapter!=null?q.chapter:(q.ch!=null?q.ch:'?')); adv[c]=(adv[c]||0)+1; });
  const CH = eval('CH_CONTENT');
  return {clesBase:Object.keys(QB), base, adv, chapitres:Object.keys(CH), advEx: ADV[0]?Object.keys(ADV[0]):null};
});
console.log(JSON.stringify(r,null,1));
console.log('errors',errs.length,errs);
await b.close();
