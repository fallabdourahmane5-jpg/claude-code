import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:Number(process.argv[3]||1400),height:950}});
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(500);
const out={};
for (const q of ['Cairns','Seattle']) {
  await p.evaluate((q)=>{ const i=document.getElementById('si'); i.value=q; doSearch(); }, q);
  await p.waitForTimeout(1200);
  out[q] = await p.evaluate(()=>{ const t=document.getElementById('search-res').innerText;
    return {brut:/CHAPITRE 24|Chapitre 24/.test(t), tete:t.slice(0,160).replace(/\n/g,' | ')}; });
}
// fiches : libellé brut après filtre
await p.evaluate(()=>{ showPg('fc'); });
await p.waitForTimeout(600);
await p.evaluate(()=>filterFC(24));
await p.waitForTimeout(1500);
out.fiches = await p.evaluate(()=>{ const t=document.getElementById('pg-fc').innerText;
  return {brut:/Chapitre 24|CHAPITRE 24|Ch\.24|ch\.24/.test(t), n:t.length, tete:t.slice(0,220).replace(/\n/g,' | ')}; });
// quiz lancé sur 24
await p.evaluate(()=>{ showPg('quiz'); });
await p.waitForTimeout(600);
const q24 = await p.evaluate(()=>{ try{ startQuiz(24); return 'ok'; }catch(e){ return String(e); } });
await p.waitForTimeout(2000);
out.quiz24 = {start:q24, txt: await p.evaluate(()=>document.getElementById('pg-quiz').innerText.slice(0,300).replace(/\n/g,' | '))};
console.log(JSON.stringify(out,null,1));
await b.close();
