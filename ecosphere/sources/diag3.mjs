import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(4500);
await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(500);
const r = await p.evaluate(async ()=>{
  const inp=document.querySelector('#pg-search input'); inp.value='Volcker';
  inp.dispatchEvent(new Event('input',{bubbles:true}));
  await new Promise(r=>setTimeout(r,500));
  const SI=eval('SEARCH_INDEX');
  const mes=SI.filter(e=>e.eco910);
  const volcker=SI.filter(e=>String(e.term).includes('Volcker')||String(e.def).includes('Volcker'));
  let scores=[];
  try{ scores = volcker.map(e=>({type:e.type, term:e.term.slice(0,52), score: (typeof scoreItem==='function')?scoreItem(e,'Volcker'):'n/a'})); }catch(err){ scores=[String(err)]; }
  return {totalIndex:SI.length, marques:mes.length, volckerEntries:volcker.length, scores};
});
console.log('index:', r.totalIndex, '| entrées marquées:', r.marques, '| contenant Volcker:', r.volckerEntries);
console.log(JSON.stringify(r.scores,null,1));
await b.close();
