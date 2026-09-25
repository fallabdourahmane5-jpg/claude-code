import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const A=eval('AUTHORS')||[];
  const champs = A[0]?Object.keys(A[0]):[];
  const parCh={};
  A.forEach(a=>{ const cs=[].concat(a.chapters||a.chapitres||a.ch||[]); cs.forEach(c=>{parCh[String(c)]=(parCh[String(c)]||0)+1;}); });
  const pour = n => A.filter(a=>[].concat(a.chapters||a.chapitres||a.ch||[]).map(String).includes(String(n)));
  return {total:A.length, champs, parCh, ex:A[0], n9:pour(9).length, n10:pour(10).length, n21:pour(21).length,
    ech9:pour(9).slice(0,3), ech10:pour(10).slice(0,2), ech21:pour(21).slice(0,2)};
});
console.log('total auteurs', r.total, '| champs', JSON.stringify(r.champs));
console.log('par chapitre', JSON.stringify(r.parCh));
console.log('ch9:',r.n9,'ch10:',r.n10,'ch21:',r.n21);
console.log('\n--- exemple générique ---'); console.log(JSON.stringify(r.ex,null,1));
console.log('\n--- ch9 ---'); console.log(JSON.stringify(r.ech9,null,1).slice(0,1400));
await b.close();
