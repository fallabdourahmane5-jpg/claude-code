import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const D='/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+D+'app_v220.html'); await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.evaluate(()=>window.__ECO_RECHERCHE.lancer('capital humain')); await p.waitForTimeout(900);
const cibles=[['#rq-rep .rq-o','destination'],['#rq-rep .rq-cf','à ne pas confondre'],
  ['#rq-fam .rq-k','forme voisine'],['#rq-res .rq-r','ligne de résultat'],
  ['#rq-outils .rq-f','filtre']];
for(const [sel,nom] of cibles){
  const el=await p.$(sel); if(!el){console.log(nom+' : absent');continue;}
  const av=await el.evaluate(e=>{const s=getComputedStyle(e);return s.color+' / '+s.backgroundColor+' / '+s.borderBottomColor;});
  await el.hover(); await p.waitForTimeout(260);
  const ap=await el.evaluate(e=>{const s=getComputedStyle(e);return s.color+' / '+s.backgroundColor+' / '+s.borderBottomColor;});
  console.log(nom.padEnd(20)+(av!==ap?'survol OK   ':'IDENTIQUE   ')+av+'  ->  '+ap);
}
// doublons dans « où le retrouver »
const d=await p.evaluate(()=>{
  const r={};
  for(const q of ['position extérieure nette','capital humain','coût marginal','compétitivité']){
    window.__ECO_RECHERCHE.lancer(q);
    const b=document.querySelector('#rq-rep [data-tout]'); if(b) b.click();
    document.querySelectorAll('#rq-rep [data-tout]').forEach(x=>x.click());
    const g={};
    document.querySelectorAll('#rq-rep .rq-g').forEach(G=>{
      const lab=G.querySelector('.rq-g-l').textContent;
      G.querySelectorAll('.rq-sg').forEach(S=>{
        const ch=(S.querySelector('.rq-sg-t')||{}).textContent||'';
        S.querySelectorAll('.rq-o').forEach(o=>{
          const k=lab+'|'+ch+'|'+o.textContent.toLowerCase();
          g[k]=(g[k]||0)+1; });});});
    r[q]=Object.keys(g).filter(k=>g[k]>1);
  }
  return r;});
console.log('doublons :', JSON.stringify(d));
console.log('errs', errs);
await b.close();
