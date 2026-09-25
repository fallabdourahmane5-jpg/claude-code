import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
const r = await p.evaluate(()=>{
  const G=n=>{try{return eval(n)}catch(e){return undefined}};
  const CH=G('CH_CONTENT')||{};
  const titres={}; Object.keys(CH).forEach(k=>titres[k]=CH[k].title);
  return {CHAPTER_LABELS:G('CHAPTER_LABELS'), titres,
    aFn: typeof window.renderAdvancedSelector, esc: typeof window.esc,
    relabel: typeof window.relabelBadges};
});
console.log(JSON.stringify(r,null,1));
await b.close();
