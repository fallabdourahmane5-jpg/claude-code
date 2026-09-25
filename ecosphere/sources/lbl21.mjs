import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
for (const pg of ['subjects','fc','maps']) {
  const t = await p.evaluate((pg)=>{ window.showPg(pg); return 1; }, pg);
  await p.waitForTimeout(800);
  const txt = await p.evaluate((pg)=>{
    const e=document.getElementById('pg-'+pg); const t=e?e.innerText:'';
    return t.split('\n').filter(l=>/2.{0,3}\s*ann|Deuxi|Ch\.?\s*21|Chapitre 21/i.test(l)).slice(0,6);
  }, pg);
  console.log('['+pg+'] →', JSON.stringify(txt));
}
await b.close();
