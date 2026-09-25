import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
p.on('console',m=>{ const t=m.text(); if(t.includes('[DIAG]')) console.log(t); });
p.on('pageerror',e=>console.log('PAGEERROR', String(e).slice(0,200)));
await p.goto('file://'+process.cwd()+'/app_dbg2.html'); await p.waitForTimeout(5000);
const r = await p.evaluate(()=>({ajouts:window.__ECO_SEARCH_AJOUTS, fait:window.__ECO_SEARCH_FAIT, n:eval('SEARCH_INDEX').length}));
console.log('FINAL', JSON.stringify(r));
await b.close();
