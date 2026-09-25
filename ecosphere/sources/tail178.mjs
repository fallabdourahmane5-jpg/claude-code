import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v178.html');
await p.waitForTimeout(3500);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const out={};
  Object.keys(CH).forEach(k=>{ out[k]=(CH[k].cours||'').length; });
  return out;
});
console.log(JSON.stringify(r));
console.log('errors', errs.length, errs);
await b.close();
