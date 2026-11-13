import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v219.html');
await p.waitForTimeout(34000);
console.log('index', JSON.stringify(await p.evaluate(()=>{
  const c = window.__ECO_RECHERCHE.compter();
  return {types:c, familles:Object.keys(window.__ECO_RECHERCHE.familles?window.__ECO_RECHERCHE.familles():{}).length};
})));
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(900);
const Q = ['capital','capital humain','taux de change','position extérieure nette',
  'coût marginal','anomie','état stationnaire','zone euro','Bairoch','PEN',
  'protectionisme','capitl humain','concurrence','effet','rente','dépendance'];
for (const q of Q) {
  const r = await p.evaluate((q)=>{
    window.__ECO_RECHERCHE.lancer(q);
    const rep = document.querySelector('#rq-rep .rq-rep');
    const fam = document.querySelector('#rq-fam .rq-fam');
    const lignes = [...document.querySelectorAll('#rq-res .rq-r')];
    const blocs = [...document.querySelectorAll('#rq-res .rq-bloc-t')].map(x=>x.textContent);
    return {
      rep: rep ? {t: rep.querySelector('.rq-rep-t').textContent,
                  ty: rep.querySelector('.rq-ty').textContent,
                  d: rep.querySelector('.rq-rep-d').textContent.length,
                  dist: !!rep.querySelector('.rq-dist'),
                  ou: rep.querySelectorAll('.rq-o').length} : null,
      fam: fam ? {t: fam.querySelector('.rq-fam-t').textContent,
                  n: fam.querySelectorAll('.rq-k').length,
                  ex: [...fam.querySelectorAll('.rq-k')].slice(0,6).map(x=>x.textContent)} : null,
      blocs, n: lignes.length,
      outils: (document.getElementById('rq-outils').textContent||'').replace(/\s+/g,' ').slice(0,120),
      top: lignes.slice(0,3).map(x=>({ty:x.querySelector('.rq-ty').textContent,
        ch:x.querySelector('.rq-ch').textContent,
        t:x.querySelector('.rq-rt').textContent.slice(0,48),
        mk:x.querySelectorAll('mark').length}))};
  }, q);
  console.log('\n======== ' + q);
  console.log('  outils : ' + r.outils);
  console.log('  réponse: ' + (r.rep ? '['+r.rep.ty+'] '+r.rep.t+'  (def '+r.rep.d+' car., dist '+r.rep.dist+', où '+r.rep.ou+')' : '—'));
  console.log('  famille: ' + (r.fam ? r.fam.t + ' → ' + r.fam.ex.join(' / ') : '—'));
  console.log('  blocs  : ' + r.blocs.join(' // ') + '  (' + r.n + ' lignes)');
  r.top.forEach(x=>console.log('    [' + x.ty + '] ' + x.ch + ' | ' + x.t + ' (mk' + x.mk + ')'));
}
console.log('\nerrs', JSON.stringify(errs.slice(0,4)));
await b.close();
