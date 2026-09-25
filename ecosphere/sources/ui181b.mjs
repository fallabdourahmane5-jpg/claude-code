import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(5000);
await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(800);
async function q(mot){
  const r = await p.evaluate(async (mot)=>{
    const inp=document.querySelector('#pg-search input');
    inp.value=mot; inp.dispatchEvent(new Event('input',{bubbles:true}));
    await new Promise(r=>setTimeout(r,1200));
    try{ if(typeof doSearch==='function') doSearch(); }catch(e){}
    await new Promise(r=>setTimeout(r,400));
    const all=[...document.querySelectorAll('#pg-search .ri')];
    return {n:all.length, types:[...new Set(all.map(e=>(e.querySelector('.ri-type')||{}).textContent||''))].slice(0,12)};
  }, mot);
  console.log('\n« '+mot+' » → '+r.n+' résultats');
  r.types.forEach(t=>console.log('   '+t.trim()));
}
for (const m of ['Volcker','Chamberlin','Bronner','Prebisch']) await q(m);
console.log('\nerrors',errs.length,errs);
await b.close();
