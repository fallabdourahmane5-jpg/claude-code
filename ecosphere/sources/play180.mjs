import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
for (const ch of [9,10,21]) {
  const r = await p.evaluate(async (ch)=>{
    window.showPg('quiz'); window.startQuiz(ch);
    await new Promise(r=>setTimeout(r,700));
    const pg=document.getElementById('pg-quiz');
    const cands=[...pg.querySelectorAll('[onclick],button,li,div')].filter(e=>/answer|opt|choice/i.test(e.className+' '+(e.getAttribute('onclick')||'')));
    const cls=[...new Set(cands.map(e=>e.className))].slice(0,4);
    if(cands[0]) cands[0].click();
    await new Promise(r=>setTimeout(r,500));
    const t=pg.innerText;
    return {classes:cls, aClique:!!cands[0], score:(t.match(/Score:\s*\d+/)||[''])[0], suite:/Suivant|Question 2|Continuer/i.test(t)};
  }, ch);
  console.log('ch'+ch+' → clic:'+r.aClique, '| classes:'+JSON.stringify(r.classes), '|', r.score, '| suite:'+r.suite);
}
console.log('errors', errs.length, errs);
await b.close();
