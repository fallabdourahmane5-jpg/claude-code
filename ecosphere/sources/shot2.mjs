import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const file = process.argv[2] || 'app_v220.html';
const tag  = process.argv[3] || 'v220b';
const b = await chromium.launch();

async function page(vp, scheme) {
  const p = await b.newPage({viewport:vp, colorScheme:scheme, deviceScaleFactor:2});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  p.__errs = errs;
  await p.goto('file://' + D + file);
  await p.waitForTimeout(34000);
  await p.evaluate(()=>showPg('search'));
  await p.waitForTimeout(500);
  return p;
}

async function tir(p, nom, q, sel, opts={}) {
  await p.evaluate((q)=>window.__ECO_RECHERCHE.lancer(q), q);
  await p.waitForTimeout(800);
  if (opts.deplier) {
    await p.evaluate((i)=>{ const l=document.querySelectorAll('#rq-res .rq-r');
      if(l[i]) l[i].querySelector('[data-bascule]').click(); }, opts.deplier-1);
    await p.waitForTimeout(350);
  }
  if (opts.hover) await p.hover(opts.hover).catch(()=>{});
  if (opts.tout) await p.evaluate(()=>{ const b=document.querySelector('#rq-rep [data-tout]'); if(b) b.click(); });
  await p.waitForTimeout(250);
  const el = sel ? await p.$(sel) : null;
  await (el || p).screenshot({path: D+'sh_'+tag+'_'+nom+'.png'});
  console.log(nom + ' « ' + q + ' »' + (p.__errs.length ? '  ERREURS: '+p.__errs.join(' | ') : ''));
}

let p = await page({width:1440,height:1000}, 'dark');
await tir(p, 'rep',   'position extérieure nette', '#rq-rep');
await tir(p, 'repx',  'coût marginal', '#rq-rep');
await tir(p, 'reptout','position extérieure nette', '#rq-rep', {tout:1});
await tir(p, 'liste', 'capital', '#rq-res', {deplier:1});
await tir(p, 'fam',   'capital', '#rq-fam');
await tir(p, 'corr',  'capitl humain', '#rq-outils');
await tir(p, 'vide',  'hystérèse du chômage', '#rq-res');
await p.close();

p = await page({width:1440,height:1000}, 'light');
await tir(p, 'clair', 'capital humain', null);
await p.close();

p = await page({width:390,height:844}, 'dark');
await tir(p, 'tel_rep', 'capital humain', '#rq-rep');
await tir(p, 'tel_liste', 'capital humain', null);
await tir(p, 'tel_ouv', 'coût marginal', null, {deplier:1});
await p.close();

p = await page({width:834,height:1112}, 'dark');
await tir(p, 'ipad_rep', 'avantage comparatif', '#rq-rep');
await p.close();
await b.close();
