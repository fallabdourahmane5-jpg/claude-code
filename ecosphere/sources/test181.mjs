import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v181.html'); await p.waitForTimeout(4500);
const r = await p.evaluate(()=>{
  const SI=eval('SEARCH_INDEX')||[];
  const t={};
  SI.forEach(e=>{ const ty=String(e.type), c=String(e.ch); t[ty]=t[ty]||{}; t[ty][c]=(t[ty][c]||0)+1; });
  const parCh={}; SI.forEach(e=>{const c=String(e.ch); parCh[c]=(parCh[c]||0)+1;});
  // doublons stricts
  const seen={}, dup=[];
  SI.forEach(e=>{ const k=String(e.type)+'|'+String(e.ch)+'|'+String(e.term).toLowerCase(); if(seen[k])dup.push(k); else seen[k]=1; });
  return {total:SI.length, ajouts:window.__ECO_SEARCH_AJOUTS, t, parCh, doublons:dup.length};
});
console.log('total index :', r.total, '| ajouts :', r.ajouts, '| doublons stricts :', r.doublons);
console.log('par chapitre :', JSON.stringify(r.parCh));
const chs=['1','2','3','4','5','6','7','8','9','10','21'];
console.log('\ntype'.padEnd(23)+chs.map(c=>c.padStart(6)).join(''));
['auteur','auteur-idée','auteur-repère','auteur-révision','courant','mobilisation','mobilisation-auteur','ouvrage'].forEach(ty=>{
  console.log(ty.padEnd(22)+chs.map(c=>String((r.t[ty]||{})[c]||0).padStart(6)).join(''));
});
console.log('\nerrors',errs.length,errs);
await b.close();
