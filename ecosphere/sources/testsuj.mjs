import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v178.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(6000);
const r=await p.evaluate(async ()=>{
  const SB=(function(){try{return SUBJECTS_BANK_PREMIUM}catch(e){return []}})();
  const o={stats:window.__ECO_MAJ_SUJ_STATS, total:SB.length, parCh:{}};
  const g={}; SB.forEach(s=>{(g[s.chapter]=g[s.chapter]||[]).push(s);});
  Object.keys(g).sort((a,b)=>a-b).forEach(k=>{
    const a=g[k];
    const moy=f=>Math.round(a.reduce((x,s)=>x+((typeof s[f]==='string'?s[f].length:(s[f]||[]).join(' ').length)||0),0)/a.length);
    o.parCh[k]={n:a.length, planItems:Math.round(a.reduce((x,s)=>x+(s.plan||[]).length,0)/a.length),
                intro:moy('intro'), com:moy('commentaire'), concl:moy('conclusion'),
                mobLen:Math.round(a.reduce((x,s)=>x+String(s.mobiliser||'').length,0)/a.length)};
  });
  o.sansMob = SB.filter(s=>!s.mobiliser || String(s.mobiliser).trim().length<5).length;
  o.exCh9  = SB.find(s=>s.id==='ch9-1');
  o.exCh10 = SB.find(s=>s.id==='ch10-1');
  o.exCh21 = SB.find(s=>s.id==='ch21-1');
  o.exCh3  = SB.find(s=>s.id==='ch3-12');
  // page sujets
  window.showPg('subjects'); await new Promise(r=>setTimeout(r,900));
  o.pageOk = (document.getElementById('pg-subjects')?.innerText||'').length;
  return o;
});
console.log('stats du patch :', JSON.stringify(r.stats));
console.log('sujets sans « mobiliser » :', r.sansMob, ' | total :', r.total);
console.log('\nch | n  | lignes | intro | comm | concl | mobiliser');
Object.entries(r.parCh).forEach(([k,v])=>console.log(
  `${k.padStart(3)}| ${String(v.n).padStart(2)} | ${String(v.planItems).padStart(6)} | ${String(v.intro).padStart(5)} | ${String(v.com).padStart(4)} | ${String(v.concl).padStart(5)} | ${v.mobLen}`));
console.log('\n— ch9-1 mobiliser :', r.exCh9.mobiliser.slice(0,110));
console.log('— ch10-1 mobiliser:', r.exCh10.mobiliser.slice(0,110));
console.log('— ch21-1 mobiliser:', r.exCh21.mobiliser.slice(0,110));
console.log('— ch3-12 mobiliser:', r.exCh3.mobiliser.slice(0,140));
console.log('\npage Sujets :', r.pageOk, 'caractères | ERREURS JS :', errs.length);
await b.close();
