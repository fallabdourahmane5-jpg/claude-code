import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1440,height:900}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]); await p.waitForTimeout(1200);
await p.evaluate(()=>showPg('visualisations')); await p.waitForTimeout(500);
await p.evaluate(()=>document.querySelectorAll('#vzGrid .vz-card')[0].click()); await p.waitForTimeout(700);
// ouvrir un noeud et cliquer le bouton dossier via dispatch
const r = await p.evaluate(()=>{
  const ns=[...document.querySelectorAll('#vzWorld .vz-node')];
  for(const n of ns){ n.click();
    const a=document.querySelector('#vzPanel [data-dos]');
    if(a){ const t=a.textContent.trim(), c=a.getAttribute('data-dos');
      a.dispatchEvent(new MouseEvent('click',{bubbles:true})); return {t,c}; } }
  return null;
});
console.log('DOS', JSON.stringify(r));
await p.waitForTimeout(2200);
console.log('APRES', JSON.stringify(await p.evaluate(()=>({
  pg:[...document.querySelectorAll('.pg.on')].map(x=>x.id),
  titre:(document.querySelector('#pg-autour .an-dt')||document.querySelector('#pg-autour h1')||{}).textContent}))));
await p.screenshot({path:'v215_dos.png'});
// atlas, auteur, fiches, sujets
for (const [sel,lab] of [['[data-at]','ATLAS'],['[data-aut]','AUTEUR'],['[data-fc]','FICHES'],['[data-su]','SUJETS']]) {
  await p.evaluate(()=>showPg('visualisations')); await p.waitForTimeout(500);
  const ok = await p.evaluate(sel=>{
    const r=document.getElementById('vzRetour'); if(r) r.click(); return true;
  }, sel);
  await p.waitForTimeout(400);
  await p.evaluate(()=>document.querySelectorAll('#vzGrid .vz-card')[0].click()); await p.waitForTimeout(700);
  const found = await p.evaluate(sel=>{
    const ns=[...document.querySelectorAll('#vzWorld .vz-node')];
    for(const n of ns){ n.click(); const a=document.querySelector('#vzPanel '+sel);
      if(a){ const t=a.textContent.trim(); a.dispatchEvent(new MouseEvent('click',{bubbles:true})); return t; } }
    return null;
  }, sel);
  await p.waitForTimeout(1600);
  console.log(lab, JSON.stringify(found), JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('.pg.on')].map(x=>x.id))));
}
console.log('ERR', errs.length?errs.slice(0,3):'aucune');
await b.close();
