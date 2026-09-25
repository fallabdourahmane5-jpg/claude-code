import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(4500);
await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(600);
async function q(mot){
  const r = await p.evaluate(async (mot)=>{
    const inp=document.querySelector('#pg-search input'); inp.value=mot;
    inp.dispatchEvent(new Event('input',{bubbles:true}));
    await new Promise(r=>setTimeout(r,450));
    const items=[...document.querySelectorAll('#pg-search .ri')].slice(0,6).map(e=>{
      const t=e.querySelector('.ri-type'), m=e.querySelector('.ri-term');
      return (t?t.textContent.trim():'')+'  |  '+(m?m.textContent.trim().slice(0,58):'');
    });
    return {n:document.querySelectorAll('#pg-search .ri').length, items};
  }, mot);
  console.log('\n« '+mot+' » → '+r.n+' résultats');
  r.items.forEach(i=>console.log('   '+i));
}
for (const m of ['Volcker','Coase','Crozier','Milanovic','Chamberlin','Bronner']) await q(m);
console.log('\nerrors',errs.length,errs);
await b.close();
