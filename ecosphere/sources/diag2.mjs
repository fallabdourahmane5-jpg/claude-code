import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const logs=[]; p.on('console',m=>logs.push(m.text().slice(0,200)));
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(4500);
const r = await p.evaluate(()=>{
  const SI=eval('SEARCH_INDEX'), A=eval('AUTHORS');
  const normal=s=>String(s==null?'':s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();
  const vus={}; SI.forEach(e=>{ vus[normal(e.term)+'|'+e.ch+'|'+e.type]=true; });
  const a9 = A.filter(x=>[].concat(x.chapters||[]).map(String).includes('9'));
  const tests = a9.slice(0,3).map(a=>{
    const term='Quel auteur associer à l’idée suivante : '+a.idea;
    const k=normal(term)+'|9|auteur-idée';
    return {nom:a.name, idea:!!a.idea, k:k.slice(0,60), existe:!!vus[k]};
  });
  return {nbAuteurs9:a9.length, tests, flagFait:window.__ECO_SEARCH_FAIT, flagAjouts:window.__ECO_SEARCH_AJOUTS,
    scriptPresent: !!document.getElementById('eco-recherche-9-10-21')};
});
console.log(JSON.stringify(r,null,1));
console.log('console logs:', logs.slice(0,10));
await b.close();
