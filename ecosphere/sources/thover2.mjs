import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const D='/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:950}});
await p.goto('file://'+D+'app_v220.html'); await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.evaluate(()=>window.__ECO_RECHERCHE.lancer('capital humain')); await p.waitForTimeout(900);
for(const [sel,nom] of [['#rq-outils .rq-f:not(.on)','filtre inactif'],
   ['#rq-res .rq-r .rq-rh','entête de ligne'],['#rq-res .rq-plus','afficher plus']]){
  const el=await p.$(sel); if(!el){console.log(nom+' absent');continue;}
  const av=await el.evaluate(e=>getComputedStyle(e).backgroundColor+' '+getComputedStyle(e).color);
  await el.hover(); await p.waitForTimeout(250);
  const ap=await el.evaluate(e=>getComputedStyle(e).backgroundColor+' '+getComputedStyle(e).color);
  console.log(nom.padEnd(18)+(av!==ap?'survol OK  ':'IDENTIQUE  ')+av+' -> '+ap);
}
// état déplié + focus clavier
const r=await p.evaluate(()=>{
  const l=document.querySelector('#rq-res .rq-r');
  l.querySelector('[data-bascule]').click();
  const o=l.classList.contains('ouvert');
  const go=l.querySelector('.rq-go'); go.focus();
  return {ouvert:o, corps:getComputedStyle(l.querySelector('.rq-corps')).display,
    bouton:!!go, focus:document.activeElement===go};});
console.log('déplié', JSON.stringify(r));
await b.close();
