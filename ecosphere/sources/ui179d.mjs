import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(3000);
const s = await p.evaluate(()=>({go:String(window.goSubjectPremium).slice(0,700), tog:String(window.toggleSubjectCorrection).slice(0,500)}));
console.log('--- goSubjectPremium ---\n'+s.go);
console.log('\n--- toggleSubjectCorrection ---\n'+s.tog);
await b.close();
