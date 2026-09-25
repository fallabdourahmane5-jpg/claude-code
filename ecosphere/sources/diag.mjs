import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v181.html',{waitUntil:'domcontentloaded'});
for (const t of [0, 600, 1500, 3000, 4500]) {
  await p.waitForTimeout(t===0?0:(t - (t===600?0:0)));
  const r = await p.evaluate(()=>{
    const A=(typeof AUTHORS!=='undefined')?AUTHORS:null;
    if(!A) return {aucun:true};
    const avecCh = A.filter(a=>[].concat(a.chapters||[]).length>0).length;
    const c9 = A.filter(a=>[].concat(a.chapters||[]).map(String).includes('9')).length;
    return {total:A.length, avecCh, c9};
  });
  console.log('t~'+t+'ms →', JSON.stringify(r));
  if(t===0) await p.waitForTimeout(600);
}
await b.close();
