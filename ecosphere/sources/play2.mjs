import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
for (const ch of [9,10,21]) {
  const r = await p.evaluate(async (ch)=>{
    window.showPg('quiz'); window.startQuiz(ch);
    await new Promise(r=>setTimeout(r,800));
    const pg=document.getElementById('pg-quiz');
    const o=pg.querySelectorAll('.qopt');
    if(o.length) o[0].click();
    await new Promise(r=>setTimeout(r,600));
    const t=pg.innerText;
    return {nbOpt:o.length, score:(t.match(/Score:\s*\d+/)||[''])[0],
            feedback:/Bonne réponse|Mauvaise|Correct|Faux|Explication/i.test(t),
            entete:(t.match(/QUESTION \d+ · [^\n]*/)||[''])[0]};
  }, ch);
  console.log('ch'+ch, '| options:'+r.nbOpt, '|', r.score, '| correction affichée:'+r.feedback, '|', r.entete);
}
console.log('errors', errs.length, errs);
await b.close();
