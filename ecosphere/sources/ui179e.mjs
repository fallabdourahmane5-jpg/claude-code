import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3500);
await p.evaluate(()=>window.showPg('subjects')); await p.waitForTimeout(500);
async function check(id, marks){
  const ok = await p.evaluate((id)=>{
    window.setSubjectChapterPremium(Number(id.split('-')[0].replace('ch','')));
    return true;
  }, id);
  await p.waitForTimeout(500);
  await p.evaluate((id)=>window.toggleSubjectCorrection(id), id);
  await p.waitForTimeout(400);
  const t = await p.evaluate((id)=>{
    const el=document.querySelector(`#pg-subjects .subj-card[data-id="${CSS.escape(id)}"]`);
    return el? el.innerText : 'CARTE INTROUVABLE';
  }, id);
  console.log('\n=== '+id+' === ('+t.length+' caractères affichés)');
  marks.forEach(m=>console.log((t.includes(m)?'  OK  ':'  --  ')+m));
}
await check('ch10-7', ['solidarité organique','18,7 %','Le Quai de Ouistreham (2010)','accords Matignon de 1936','10,3 %','grande démission','Castel']);
await check('ch21-17', ['List','1841','Hawley-Smoot','protectionnisme éducateur','arsenalisation','Prebisch']);
await check('ch9-1',  ['Chamberlin','contestables','Phoebus','Alstom-Siemens']);
console.log('\nerrors', errs.length, errs);
await b.close();
