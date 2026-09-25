import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,180)));
await p.goto('file://'+process.cwd()+'/app_v179.html');
await p.waitForTimeout(4000);
const r = await p.evaluate(()=>{
  const S = eval('SUBJECTS_BANK_PREMIUM');
  const par={}; const sansMob=[]; const courts=[];
  S.forEach(s=>{
    const c=String(s.chapter); par[c]=par[c]||{n:0,plan:0,intro:0};
    par[c].n++; par[c].plan+=(s.plan||[]).length; par[c].intro+=(s.intro||'').length;
    if(!String(s.mobiliser||'').trim()) sansMob.push(s.id);
    if((s.plan||[]).length<20) courts.push(s.id+':'+(s.plan||[]).length);
  });
  Object.keys(par).forEach(k=>{par[k].plan=Math.round(par[k].plan/par[k].n); par[k].intro=Math.round(par[k].intro/par[k].n);});
  return {total:S.length, par, sansMob:sansMob.length, courts:courts.length, stats:window.__ECO_MAJ_SUJ2_STATS,
    ex10:S.find(x=>x.id==='ch10-7'), ex21:S.find(x=>x.id==='ch21-17')};
});
console.log('total', r.total, '| sans mobiliser', r.sansMob, '| plans <20 lignes', r.courts);
console.log('stats', JSON.stringify(r.stats));
console.log('par chapitre (n, plan moy, intro moy):'); console.log(JSON.stringify(r.par));
console.log('\nch10-7 plan', r.ex10.plan.length, '| mob:', r.ex10.mobiliser.slice(0,110));
console.log('ch21-17 plan', r.ex21.plan.length, '| mob:', r.ex21.mobiliser.slice(0,110));
console.log('\nerrors', errs.length, errs);
await b.close();
