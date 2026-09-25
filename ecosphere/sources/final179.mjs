import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
const r = await p.evaluate(()=>{
  const S = eval('SUBJECTS_BANK_PREMIUM');
  let ref9=0, ref10=0, ref21=0, e18=0, vides=0, brut=0;
  const parCh={};
  S.forEach(s=>{
    const m=String(s.mobiliser||'');
    if(!m.trim()) vides++;
    if(/^[0-9,\s]+$/.test(m.trim())) brut++;
    const c=String(s.chapter);
    const neuf = /Ch\.?\s*9\b|Ch\. 9 \(/.test(m), dix=/Ch\.?\s*10\b/.test(m), deux=/2ᵉ année/.test(m);
    if(neuf) ref9++; if(dix) ref10++; if(deux) ref21++;
    if(['1','2','3','4','5','6','7','8'].includes(c) && (neuf||dix||deux)){ e18++; parCh[c]=(parCh[c]||0)+1; }
  });
  return {total:S.length, vides, brut, ref9, ref10, ref21, e18, parCh};
});
console.log(JSON.stringify(r,null,1));
await b.close();
