import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4800);
const r = await p.evaluate(()=>{
  const FC=eval('FC_DATA')||[];
  const t={};
  FC.forEach(e=>{ const ty=String(e.type||'?'), c=String(e.ch); t[ty]=t[ty]||{}; t[ty][c]=(t[ty][c]||0)+1; });
  const A=eval('AUTHORS')||[];
  const parChPrimaire={}; A.forEach(a=>{ const c=String(a.ch); parChPrimaire[c]=(parChPrimaire[c]||0)+1; });
  return {total:FC.length, t, champs:FC[0]?Object.keys(FC[0]):[], parChPrimaire};
});
console.log('FC_DATA total', r.total, '| champs', JSON.stringify(r.champs));
console.log('AUTHORS par ch PRIMAIRE (a.ch) :', JSON.stringify(r.parChPrimaire));
const chs=['1','2','3','4','5','6','7','8','9','10','21'];
console.log('\ntype'.padEnd(27)+chs.map(c=>c.padStart(6)).join(''));
Object.keys(r.t).sort().forEach(ty=>console.log(ty.padEnd(26)+chs.map(c=>String(r.t[ty][c]||0).padStart(6)).join('')));
await b.close();
