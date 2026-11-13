import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
async function mesure(f, W){
  const p = await b.newPage({viewport:{width:W,height:950}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://' + D + f);
  await p.waitForTimeout(34000);
  const r = await p.evaluate(()=>({
    chapitres:Object.keys(CH_CONTENT).length, fiches:FC_DATA.length,
    auteurs:AUTHORS.length, sujets:SUBJECTS_BANK_PREMIUM.length,
    onglets:document.querySelectorAll('nav .nt').length,
    pages:document.querySelectorAll('.pg').length,
    ancienIndex:(typeof SEARCH_INDEX!=='undefined')?SEARCH_INDEX.length:null,
    ancienUI:!!document.querySelector('#pg-search .si-wrap'),
    nouvelleUI:!!document.getElementById('rq-in'),
    visu:(window.visualisationsStrategiques||[]).length
  }));
  // les autres sections répondent toujours
  const sections = {};
  for (const id of ['home','chapter','quiz','fc','search','authors','subjects',
      'visualisations','method','graphs','maps','formulas','autour','atlas',
      'chiffres','resumes','frise','prog']) {
    sections[id] = await p.evaluate((id)=>{
      try{ showPg(id); }catch(e){ return 'err'; }
      const el = document.getElementById('pg-'+id);
      return el ? (el.classList.contains('on') ? (el.innerText||'').length : 'off') : 'absent';
    }, id);
    await p.waitForTimeout(90);
  }
  r.sections = sections; r.errs = errs; await p.close(); return r;
}
const a = await mesure('app_v217.html', 1400);
const c = await mesure('app_v218.html', 1400);
console.log('v217', JSON.stringify(a));
console.log('v218', JSON.stringify(c));
// mobile
const m = await b.newPage({viewport:{width:390,height:844}});
const me=[]; m.on('pageerror',e=>me.push(e.message));
await m.goto('file://' + D + 'app_v218.html');
await m.waitForTimeout(32000);
await m.evaluate(()=>showPg('search'));
await m.waitForTimeout(600);
const mob = await m.evaluate(()=>{
  const i=document.getElementById('rq-in'); i.value='position extérieure nette';
  window.__ECO_RECHERCHE.lancer();
  const g=[...document.querySelectorAll('#pg-search .rq-g')];
  const w=document.querySelector('#pg-search .rq-wrap');
  return {grp:g.length, debord:document.documentElement.scrollWidth>document.documentElement.clientWidth,
    largeur:w?w.getBoundingClientRect().width:0,
    titre:g.length?g[0].querySelector('.rq-ti').textContent:''};
});
console.log('mobile', JSON.stringify(mob), 'errs', JSON.stringify(me.slice(0,3)));
await b.close();
