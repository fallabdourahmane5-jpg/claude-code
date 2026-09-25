import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(700);
const info = await p.evaluate(()=>({
  addUnique: typeof window.addUniqueSearch, doSearch: typeof window.doSearch, setF: typeof window.setF,
  chips: [...document.querySelectorAll('#pg-search .fchip')].map(c=>c.textContent.trim()),
  input: !!document.querySelector('#pg-search input')
}));
console.log('helpers:', JSON.stringify(info));
for (const q of ['Crozier','Milanovic','contestable','Volcker']) {
  const r = await p.evaluate(async (q)=>{
    const inp=document.querySelector('#pg-search input'); inp.value=q;
    inp.dispatchEvent(new Event('input',{bubbles:true}));
    await new Promise(r=>setTimeout(r,450));
    const items=[...document.querySelectorAll('#pg-search .ri')].slice(0,4).map(e=>{
      const t=e.querySelector('.ri-type'), m=e.querySelector('.ri-term');
      return (t?t.textContent.trim():'')+' → '+(m?m.textContent.trim().slice(0,52):'');
    });
    return {n:document.querySelectorAll('#pg-search .ri').length, items};
  }, q);
  console.log('\n« '+q+' » → '+r.n+' résultats');
  r.items.forEach(i=>console.log('   '+i));
}
console.log('\nerrors',errs.length,errs);
await b.close();
