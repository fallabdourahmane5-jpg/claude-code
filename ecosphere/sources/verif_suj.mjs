import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>{
  const G = n => { try { return (new Function('try{return ' + n + '}catch(e){return undefined}'))(); } catch(e){ return undefined; } };
  const SB = G('SUBJECTS_BANK_PREMIUM') || [];
  const L = Array.isArray(SB) ? SB : Object.values(SB);
  const parCh = {}; let mob = 0; const ex = []; const sans = [];
  L.forEach(s=>{
    const c = String(s.chapter);
    parCh[c] = (parCh[c]||0)+1;
    const t = String(s.mobiliser||'');
    if (/2(e|ᵉ|è|e) ann[eé]e\s*[—-]?\s*ch\.?\s*[56]|chapitre 5 de deuxi|chapitre 6 de deuxi|ch\.5|ch\.6/i.test(t)) {
      mob++; if (ex.length<4) ex.push({id:s.id, m:t.slice(0,200)});
    }
    if (!t) sans.push(s.id);
    // contrôle de forme des nouveaux sujets
  });
  const n2526 = L.filter(s=>['25','26'].indexOf(String(s.chapter))>=0);
  return {total: L.length, parCh, mobiliser2526: mob, exemples: ex,
    sansMobiliser: sans.length,
    nouveaux: n2526.map(s=>({id:s.id, ch:s.chapter, t:(s.title||'').slice(0,70),
      planType: Array.isArray(s.plan) ? 'array' : typeof s.plan,
      plan: Array.isArray(s.plan) ? s.plan.length
        : String(s.plan||'').split('\n').filter(x=>x.trim()).length,
      args: (JSON.stringify(s.plan||'').match(/Argument/g)||[]).length,
      intro: (s.intro||'').length, pb: (s.problematique||'').length,
      concl: (s.conclusion||'').length}))};
});
fs.writeFileSync('verif_suj.json', JSON.stringify(o, null, 1));
console.log('sujets', o.total, 'dont ch25/26', o.nouveaux.length, '· mobiliser citant ch.5/ch.6 :', o.mobiliser2526, '· sans mobiliser :', o.sansMobiliser);
console.log(JSON.stringify(o.parCh));
await b.close();
