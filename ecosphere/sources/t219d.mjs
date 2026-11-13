import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
// régression + contrôles ciblés
async function mesure(f){
  const p = await b.newPage({viewport:{width:1400,height:950}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://' + D + f);
  await p.waitForTimeout(34000);
  const r = await p.evaluate(()=>({
    chapitres:Object.keys(CH_CONTENT).length, auteurs:AUTHORS.length,
    sujets:SUBJECTS_BANK_PREMIUM.length,
    onglets:document.querySelectorAll('nav .nt').length,
    pages:document.querySelectorAll('.pg').length,
    ancienUI:!!document.querySelector('#pg-search .si-wrap'),
    nouvelleUI:!!document.getElementById('rq-in')}));
  const sec = {};
  for (const id of ['home','chapter','quiz','fc','search','authors','subjects',
      'visualisations','method','graphs','maps','formulas','autour','atlas',
      'chiffres','resumes','frise','prog']) {
    sec[id] = await p.evaluate((id)=>{ try{ showPg(id); }catch(e){ return 'err'; }
      const el=document.getElementById('pg-'+id);
      return el ? (el.classList.contains('on') ? (el.innerText||'').length : 'off') : 'absent'; }, id);
    await p.waitForTimeout(80);
  }
  r.sections = sec; r.errs = errs; await p.close(); return r;
}
console.log('v217 ' + JSON.stringify(await mesure('app_v217.html')));
console.log('v219 ' + JSON.stringify(await mesure('app_v219.html')));

const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v219.html');
await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(600);
console.log('\n--- contrôles ---');
for (const q of ['deficit comercial','coût marginal','capital','capital social',
                 'capital institutionnel','taux de profit','classe stérile']) {
  const r = await p.evaluate((q)=>{
    window.__ECO_RECHERCHE.lancer(q);
    const rep = document.querySelector('#rq-rep .rq-rep');
    const o = rep ? rep.querySelector('.rq-o') : null;
    return {rep: rep ? rep.querySelector('.rq-rep-t').textContent : null,
      ty: rep ? rep.querySelector('.rq-ty').textContent : null,
      premier: o ? o.textContent.replace(/\s+/g,' ') : null,
      cpt: (document.querySelector('#rq-outils .rq-cpt')||{}).textContent||''};
  }, q);
  console.log(q.padEnd(24) + '| ' + (r.rep ? '['+r.ty+'] '+r.rep : '—').padEnd(42) +
    '| 1er lien : ' + (r.premier||'—') + ' | ' + r.cpt.replace(/\s+/g,' '));
}
console.log('errs ' + JSON.stringify(errs.slice(0,4)));
await b.close();
