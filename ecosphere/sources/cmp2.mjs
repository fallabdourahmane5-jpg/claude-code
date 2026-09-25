import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
const r = await p.evaluate(()=>{
  const S = eval('SUBJECTS_BANK_PREMIUM');
  const par={};
  S.forEach(s=>{ const c=String(s.chapter); par[c]=par[c]||{n:0,ch:0};
    par[c].n++; par[c].ch+=(s.plan||[]).join(' ').length; });
  Object.keys(par).forEach(k=>par[k]=Math.round(par[k].ch/par[k].n));
  return par;
});
console.log('caractères moyens du plan développé, par chapitre :');
console.log(JSON.stringify(r,null,1));
await b.close();
