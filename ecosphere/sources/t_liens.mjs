import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v218.html');
await p.waitForTimeout(34000);

async function fermer(){
  await p.evaluate(()=>{
    document.querySelectorAll('.modal-ov.on, .modal-ov').forEach(m=>{
      m.classList.remove('on'); m.style.display='none'; });
  });
}
async function essai(q, quoi, idx) {
  await fermer();
  await p.evaluate(()=>showPg('search'));
  await p.waitForTimeout(250);
  const att = await p.evaluate(({q, quoi, idx})=>{
    const i = document.getElementById('rq-in'); i.value = q;
    window.__ECO_RECHERCHE.lancer();
    const g = [...document.querySelectorAll('#pg-search .rq-g')];
    let el, lib;
    if(quoi === 'prim'){ el = g[idx||0].querySelector('.rq-prim');
      lib = g[idx||0].querySelector('.rq-ti').textContent; }
    else { const o = [...g[0].querySelectorAll('.rq-o')]; el = o[idx||0];
      lib = el ? el.textContent : null; }
    if(!el) return null;
    el.setAttribute('data-essai','1');
    return {lib: lib, k: el.getAttribute('data-k')};
  }, {q, quoi, idx});
  if(!att) return {q, quoi, idx, ko:'élément absent'};
  await p.evaluate(()=>{ const e=document.querySelector('[data-essai="1"]'); if(e) e.click(); });
  await p.waitForTimeout(2200);
  const r = await p.evaluate(()=>{
    const pg = [...document.querySelectorAll('.pg')].find(x=>x.classList.contains('on'));
    const f = document.querySelector('.rq-flash');
    const vis = f ? (f.offsetParent !== null) : false;
    return {page: pg ? pg.id : null,
      titre: (document.getElementById('cv-title')||{}).textContent || '',
      flash: f ? (f.innerText||'').replace(/\s+/g,' ').slice(0,120) : null,
      flashVisible: vis,
      sect: f ? (f.closest('.csect')||{}).id : null};
  });
  await p.evaluate(()=>{ const e=document.querySelector('[data-essai]'); if(e) e.removeAttribute('data-essai'); });
  return {q, quoi, idx, att: att.lib.slice(0,70), k: att.k, ...r};
}

const cas = [
  ['position extérieure nette','prim',0],
  ['position extérieure nette','ou',0],
  ['position extérieure nette','ou',3],
  ['avantage comparatif','prim',0],
  ['anomie','prim',0],
  ['Bairoch','prim',0],
  ['coefficient de Gini','prim',0],
  ['temps partiel subi','prim',0],
  ['multiplicateur keynésien','prim',0],
  ['secteurs stratégiques','ou',1],
];
for (const [q,quoi,idx] of cas) {
  const r = await essai(q, quoi, idx);
  console.log('— ' + q + ' [' + quoi + idx + '] k=' + r.k);
  console.log('   annoncé : ' + (r.att||''));
  console.log('   obtenu  : page=' + r.page + ' | ' + (r.titre||'').slice(0,60) +
    ' | sect=' + r.sect + ' | visible=' + r.flashVisible);
  console.log('   passage : ' + (r.flash||'AUCUN SURLIGNAGE'));
}
console.log('\nerrs', JSON.stringify(errs.slice(0,4)));
await b.close();
