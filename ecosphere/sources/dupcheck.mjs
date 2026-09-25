import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
async function m(f){
  const p=await b.newPage(); await p.goto('file://'+process.cwd()+'/'+f); await p.waitForTimeout(5000);
  const r=await p.evaluate(()=>{const FC=eval('FC_DATA')||[];const s={},d=[];FC.forEach(e=>{const k=String(e.type)+'|'+e.ch+'|'+String(e.term).toLowerCase();if(s[k])d.push(k);else s[k]=1;});return {n:FC.length,dup:d.length};});
  await p.close(); return r;
}
console.log('v180 :', JSON.stringify(await m('app_v180.html')));
console.log('v181 :', JSON.stringify(await m('app_v181.html')));
await b.close();
