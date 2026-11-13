import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v218.html');
await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(500);
const chips = await p.evaluate(()=>[...document.querySelectorAll('#rq-chips .rq-c')]
  .map(x=>({f:x.getAttribute('data-f'), t:x.textContent})));
console.log('filtres : ' + chips.map(c=>c.t).join(' | '));
for (const q of ['protectionnisme','croissance','Keynes']) {
  console.log('\n### ' + q);
  for (const c of chips) {
    const r = await p.evaluate(({q,f})=>{
      window.__ECO_RECHERCHE.filtre(f);
      const i=document.getElementById('rq-in'); i.value=q;
      window.__ECO_RECHERCHE.lancer();
      const g=[...document.querySelectorAll('#pg-search .rq-g')];
      return {n:g.length, types:[...new Set(g.map(x=>x.querySelector('.rq-ty').textContent))]};
    }, {q, f:c.f});
    console.log('   ' + c.f.padEnd(12) + String(r.n).padStart(3) + ' grp  types=' + r.types.join(','));
  }
}
console.log('\nerrs', JSON.stringify(errs.slice(0,3)));
await b.close();
