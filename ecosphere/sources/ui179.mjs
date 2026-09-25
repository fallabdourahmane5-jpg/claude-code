import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
await p.evaluate(()=>window.showPg && window.showPg('subjects'));
await p.waitForTimeout(900);
const r = await p.evaluate(()=>{
  const fns=['openSubjectPremium','showSubjectPremium','openSujet','ouvrirSujet'];
  const f=fns.find(n=>typeof window[n]==='function');
  if(f){ try{ window[f]('ch10-7'); }catch(e){ return {err:String(e), f}; } }
  return {f};
});
await p.waitForTimeout(700);
const txt = await p.evaluate(()=>document.body.innerText);
console.log('fonction ouverture :', JSON.stringify(r));
const marks=['Castel','désaffiliation','Aubenas','Quai de Ouistreham','solidarité organique','18,7 %'];
marks.forEach(m=>console.log((txt.includes(m)?'OK  ':'--  ')+m));
console.log('errors', errs.length, errs);
await b.close();
