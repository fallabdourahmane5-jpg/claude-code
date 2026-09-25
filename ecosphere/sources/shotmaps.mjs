import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v175.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
for(const [ch,nom] of [[9,'ch9'],[10,'ch10'],[21,'ch21']]){
  await p.evaluate(async c=>{window.showPg('maps'); await new Promise(r=>setTimeout(r,400));
    window.renderVisualMap(c); await new Promise(r=>setTimeout(r,800));
    document.getElementById('visual-map-area')?.scrollIntoView({block:'start'});}, ch);
  await p.waitForTimeout(700);
  await p.screenshot({path:`map_${nom}.png`});
}
const t=await p.evaluate(()=>({
  titre:document.getElementById('visual-map-title')?.textContent,
  sousTitre:document.getElementById('visual-map-sub')?.textContent?.slice(0,90)}));
console.log(JSON.stringify(t,null,1));
await b.close();
