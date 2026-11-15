import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';

// ---------- 1. correctifs ciblés
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v220.html');
await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(700);
for (const q of ['libre entrée','société mère','capitl humain','deficit comercial',
                 'capabilités','externalité','coût','taux']) {
  const r = await p.evaluate((q)=>{
    window.__ECO_RECHERCHE.lancer(q);
    const rep = document.querySelector('#rq-rep .rq-rep');
    const corr = document.querySelector('#rq-outils .rq-corr');
    return {rep: rep ? rep.querySelector('.rq-rep-t').textContent : null,
      ty: rep ? rep.querySelector('.rq-ty').textContent : null,
      corr: corr ? corr.textContent.replace(/\s+/g,' ').slice(0,90) : null,
      cpt: (document.querySelector('#rq-outils .rq-cpt')||{}).textContent||'',
      fam: document.querySelectorAll('#rq-fam .rq-k').length};
  }, q);
  console.log(q.padEnd(22) + '| rép: ' + (r.rep ? '['+r.ty+'] '+r.rep : '—') +
    ' | fam ' + r.fam + ' | ' + r.cpt.replace(/\s+/g,' ') + (r.corr ? ' | ' + r.corr : ''));
}

// ---------- 2. dépliement et lien profond
console.log('\n--- dépliement + lien profond ---');
for (const [q, idx] of [['position extérieure nette',0],['capital technologique',0],
                        ['coût marginal',0],['tarif Méline',0]]) {
  const a = await p.evaluate(({q,idx})=>{
    window.__ECO_RECHERCHE.lancer(q);
    const rep = document.querySelector('#rq-rep .rq-o');
    if(rep){ rep.setAttribute('data-essai','1'); return {lib: rep.textContent, src:'réponse'}; }
    const l = document.querySelectorAll('#rq-res .rq-r');
    if(!l[idx]) return null;
    l[idx].querySelector('[data-bascule]').click();
    const go = l[idx].querySelector('.rq-go');
    if(go){ go.setAttribute('data-essai','1'); return {lib: go.textContent, src:'ligne dépliée'}; }
    return null;
  }, {q, idx});
  if(!a){ console.log(q + ' : rien à ouvrir'); continue; }
  await p.evaluate(()=>{ const e=document.querySelector('[data-essai]'); if(e) e.click(); });
  await p.waitForTimeout(2200);
  const r = await p.evaluate(()=>{
    const pg = [...document.querySelectorAll('.pg')].find(x=>x.classList.contains('on'));
    const f = document.querySelector('.rq-flash');
    return {page: pg?pg.id:null, titre:(document.getElementById('cv-title')||{}).textContent||'',
      flash: f ? (f.innerText||'').replace(/\s+/g,' ').slice(0,90) : null};
  });
  console.log(q.padEnd(26) + '(' + a.src + ') → ' + r.page + ' | ' + (r.titre||'').slice(0,42) +
    ' | ' + (r.flash||'AUCUN SURLIGNAGE'));
  await p.evaluate(()=>{ const e=document.querySelector('[data-essai]'); if(e) e.removeAttribute('data-essai');
    document.querySelectorAll('.modal-ov.on').forEach(m=>m.classList.remove('on'));
    showPg('search'); });
  await p.waitForTimeout(400);
}

// ---------- 3. suggestions
console.log('\n--- suggestions ---');
for (const q of ['capit','taux de ch','exter','protec']) {
  const r = await p.evaluate((q)=>{
    const i = document.getElementById('rq-in');
    i.value = q;
    i.dispatchEvent(new Event('input'));
    return new Promise(res=>setTimeout(()=>{
      const z = document.getElementById('rq-sug');
      res({on: z.classList.contains('on'),
        l: [...z.querySelectorAll('.rq-s b')].map(x=>x.textContent).slice(0,6)});
    }, 420));
  }, q);
  console.log(q.padEnd(12) + (r.on ? r.l.join(' / ') : 'aucune suggestion'));
}
console.log('errs ' + JSON.stringify(errs.slice(0,4)));
await p.close();

// ---------- 4. mobile
const m = await b.newPage({viewport:{width:390,height:844}});
const me=[]; m.on('pageerror',e=>me.push(e.message));
await m.goto('file://' + D + 'app_v220.html');
await m.waitForTimeout(32000);
await m.evaluate(()=>showPg('search'));
await m.waitForTimeout(600);
console.log('\nmobile ' + JSON.stringify(await m.evaluate(()=>{
  window.__ECO_RECHERCHE.lancer('capital humain');
  const r = document.querySelector('#rq-rep .rq-rep');
  const sel = document.getElementById('rq-sel');
  return {debord: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    rep: !!r, select: sel ? getComputedStyle(sel).display : 'absent',
    liens: getComputedStyle(document.querySelector('#rq-outils .rq-fl')).display,
    lignes: document.querySelectorAll('#rq-res .rq-r').length};
})) + ' errs ' + JSON.stringify(me.slice(0,3)));
await b.close();
