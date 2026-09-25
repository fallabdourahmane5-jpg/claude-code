import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html'); await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const S = eval('SUBJECTS_BANK_PREMIUM');
  return S.filter(s=>String(s.chapter)==='21').map(s=>({id:s.id,num:s.num,title:s.title,mob:s.mobiliser}));
});
console.log(JSON.stringify(r,null,1));
await b.close();
