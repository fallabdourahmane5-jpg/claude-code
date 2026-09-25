import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(5000);
await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(600);
const r = await p.evaluate(async ()=>{
  const si=document.getElementById('si');
  const inputTrouve = !!si;
  si.value='Volcker';
  si.dispatchEvent(new Event('input',{bubbles:true}));
  await new Promise(r=>setTimeout(r,900));
  const SI=eval('SEARCH_INDEX');
  const marques=SI.filter(e=>e.eco910).length;
  // reproduire doSearch
  const qRaw='Volcker';
  let res = SI.map(it=>({...it,_score:scoreItem(it,qRaw)})).filter(it=>it._score>=12);
  const apresScore=res.length;
  const apresUnique = uniqueBy(res, r=>`${r.type}-${norm(r.term)}-${r.ch||0}`).length;
  return {inputTrouve, marques, apresScore, apresUnique,
          rendu: document.querySelectorAll('#pg-search .ri').length,
          filtre: (typeof SEARCH_FILTER!=='undefined')?SEARCH_FILTER:'?'};
});
console.log(JSON.stringify(r,null,1));
await b.close();
