import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const G=n=>{try{return eval(n)}catch(e){return undefined}};
  const SI=G('SEARCH_INDEX')||[];
  const ex = SI[0]? Object.keys(SI[0]) : [];
  const parCh={}, parType={};
  SI.forEach(e=>{
    const c=String(e.ch!=null?e.ch:(e.chapter!=null?e.chapter:'?'));
    parCh[c]=(parCh[c]||0)+1;
    const t=String(e.type||e.kind||'?'); parType[t]=(parType[t]||0)+1;
  });
  return {total:SI.length, champs:ex, parCh, parType, echantillon:SI.slice(0,2)};
});
console.log('total', r.total);
console.log('champs', JSON.stringify(r.champs));
console.log('par chapitre', JSON.stringify(r.parCh));
console.log('par type', JSON.stringify(r.parType));
console.log('échantillon', JSON.stringify(r.echantillon,null,1).slice(0,900));
console.log('errors',errs.length,errs);
await b.close();
