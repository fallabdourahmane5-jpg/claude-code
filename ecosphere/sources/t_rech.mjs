import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:Number(process.argv[3]||1400),height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + (process.argv[2]||'app_v218.html'));
await p.waitForTimeout(32000);
console.log('bilan', JSON.stringify(await p.evaluate(()=>{
  const c = window.__ECO_RECHERCHE.compter();
  return {types:c, chapitres:Object.keys(CH_CONTENT).length};
})));
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(1200);
const Q = ['position extérieure nette','avantage comparatif','multiplicateur keynésien',
  'anomie','capabilités','courbe de Phillips','mercantilisme','chaînes de valeur mondiales',
  'solidarité organique','coefficient de Gini','Bairoch','deuxième dégroupage',
  'taux de pénétration','zones économiques spéciales','PEN','psoition exterieur nette',
  'habitus','dilemme de Triffin','externalité','croissance intensive'];
for (const q of Q) {
  const r = await p.evaluate((q)=>{
    const i = document.getElementById('rq-in'); i.value = q;
    window.__ECO_RECHERCHE.lancer();
    const g = [...document.querySelectorAll('#pg-search .rq-g')];
    return {n: g.length,
      etat: (document.getElementById('rq-etat').textContent||'').slice(0,110),
      top: g.slice(0,4).map(x=>({
        ty: x.querySelector('.rq-ty').textContent,
        loc: (x.querySelector('.rq-loc')||{}).textContent||'',
        ti: x.querySelector('.rq-ti').textContent.slice(0,70),
        mark: x.querySelectorAll('mark').length,
        ou: x.querySelectorAll('.rq-o').length}))};
  }, q);
  console.log('\n### ' + q + '  → ' + r.n + ' groupes | ' + r.etat.replace(/\s+/g,' '));
  r.top.forEach(x=>console.log('   [' + x.ty + '] ' + x.loc + ' | ' + x.ti + '  (mark ' + x.mark + ', ou ' + x.ou + ')'));
}
console.log('\nerrs', JSON.stringify(errs.slice(0,5)));
await b.close();
