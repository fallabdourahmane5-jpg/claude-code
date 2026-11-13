import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
async function suivi(f){
  const p = await b.newPage({viewport:{width:1400,height:950}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://' + D + f);
  const l=[];
  for(const t of [30,45,60,75,90]){
    await p.waitForTimeout(15000);
    l.push([t, await p.evaluate(()=>[FC_DATA.length,
      (typeof __ECO_ADV_ALL_BANK!=='undefined'?__ECO_ADV_ALL_BANK.length:(window.__ECO_ADV_ALL_BANK||[]).length),
      AUTHORS.length, SUBJECTS_BANK_PREMIUM.length])]);
  }
  await p.close(); return {f, l, errs};
}
console.log(JSON.stringify(await suivi('app_v217.html')));
console.log(JSON.stringify(await suivi('app_v218.html')));
await b.close();
