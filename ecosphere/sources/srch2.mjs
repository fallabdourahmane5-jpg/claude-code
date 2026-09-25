import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const SI=eval('SEARCH_INDEX')||[];
  const t={};
  SI.forEach(e=>{ const ty=String(e.type||'?'), c=String(e.ch); t[ty]=t[ty]||{}; t[ty][c]=(t[ty][c]||0)+1; });
  return t;
});
const chs=['1','2','3','4','5','6','7','8','9','10','21'];
console.log('type'.padEnd(22)+chs.map(c=>c.padStart(6)).join(''));
Object.keys(r).sort().forEach(ty=>{
  console.log(ty.padEnd(22)+chs.map(c=>String(r[ty][c]||0).padStart(6)).join(''));
});
await b.close();
