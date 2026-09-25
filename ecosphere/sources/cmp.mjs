import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
const r = await p.evaluate(()=>{
  const S = eval('SUBJECTS_BANK_PREMIUM');
  const a=S.find(x=>x.id==='ch5-3');
  return {t:a.title, plan:a.plan, tot:a.plan.join(' ').length};
});
console.log(r.t, '| lignes', r.plan.length, '| total chars', r.tot);
r.plan.slice(0,24).forEach(l=>console.log('  '+l));
await b.close();
