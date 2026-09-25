import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const SI=eval('SEARCH_INDEX')||[];
  const types=['auteur','auteur-idée','auteur-repère','courant','mobilisation','mobilisation-auteur','ouvrage','notion-révision','auteur-révision','tableau'];
  const out={};
  types.forEach(t=>{ out[t]=SI.filter(e=>e.type===t).slice(0,2); });
  return out;
});
Object.entries(r).forEach(([t,v])=>{
  console.log('\n===== '+t+' =====');
  v.forEach(e=>console.log(JSON.stringify(e,null,1)));
});
await b.close();
