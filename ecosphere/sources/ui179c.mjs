import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
await p.evaluate(()=>{ window.showPg('subjects'); });
await p.waitForTimeout(600);
const res = await p.evaluate(()=>{
  try{ window.goSubjectPremium('ch10-7'); }catch(e){ try{ window.openSubjectV73('ch10-7'); }catch(e2){ return 'fail '+e+' | '+e2; } }
  return 'ok';
});
await p.waitForTimeout(900);
await p.evaluate(()=>{ try{ window.toggleSubjectCorrection && window.toggleSubjectCorrection(); }catch(e){} });
await p.waitForTimeout(600);
const txt = await p.evaluate(()=>document.body.innerText);
console.log('ouverture:', res, '| longueur texte', txt.length);
['solidarité organique','18,7 %','Le Quai de Ouistreham (2010)','accords Matignon de 1936','10,3 %','grande démission'].forEach(m=>console.log((txt.includes(m)?'OK  ':'--  ')+m));
console.log('errors', errs.length, errs);
await b.close();
