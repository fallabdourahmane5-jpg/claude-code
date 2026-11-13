import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(30000);
const o = await p.evaluate(()=>{
  const par = {};
  SEARCH_INDEX.forEach(x=>{ const k = x.type+' / '+(x.source||'?'); par[k]=(par[k]||0)+1; });
  return {total: SEARCH_INDEX.length, par,
    exemple: SEARCH_INDEX.slice(0,3),
    champs: [...new Set(SEARCH_INDEX.flatMap(x=>Object.keys(x)))]};
});
console.log(JSON.stringify(o, null, 1));
// requêtes test
const tests = ['position extérieure nette','multiplicateur','avantage comparatif','habitus',
  'courbe de Phillips','anomie','taux de change réel','capabilités','hystérèse',
  'dilemme de Triffin','salaire d’efficience','mercantilisme'];
for (const q of tests) {
  const r = await p.evaluate((q)=>{
    document.getElementById('si').value = q; doSearch();
    const box = document.getElementById('search-res');
    return [...box.querySelectorAll('.ri')].slice(0,6).map(x=>({
      t: (x.querySelector('.ri-type')||{}).textContent,
      n: (x.querySelector('.ri-term')||{}).textContent}));
  }, q);
  console.log('\n### ' + q);
  r.forEach(x=>console.log('   ', x.t, '|', x.n));
  if(!r.length) console.log('    AUCUN RÉSULTAT');
}
console.log('\nerrs', JSON.stringify(errs));
await b.close();
