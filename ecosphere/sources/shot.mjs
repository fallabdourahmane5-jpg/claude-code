import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const file = process.argv[2] || 'app_v219.html';
const tag  = process.argv[3] || 'v219';
const b = await chromium.launch();

async function tirer(nom, vp, scheme, q, opts={}) {
  const p = await b.newPage({viewport:vp, colorScheme:scheme, deviceScaleFactor:2});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://' + D + file);
  await p.waitForTimeout(34000);
  await p.evaluate(()=>showPg('search'));
  await p.waitForTimeout(500);
  await p.evaluate((q)=>window.__ECO_RECHERCHE.lancer(q), q);
  await p.waitForTimeout(900);
  if (opts.deplier) await p.evaluate(()=>{
    const l=document.querySelectorAll('#rq-res .rq-r');
    if(l[0]) l[0].querySelector('[data-bascule]').click();
  });
  await p.waitForTimeout(400);
  await p.screenshot({path: D+'sh_'+tag+'_'+nom+'.png', fullPage: !!opts.full});
  console.log(nom + ' ' + vp.width + 'x' + vp.height + ' ' + scheme + ' « ' + q + ' »' +
    (errs.length ? '  ERREURS: '+errs.join(' | ') : ''));
  await p.close();
}

const jobs = [
  ['pc_dark',  {width:1440,height:1000}, 'dark',  'position extérieure nette', {full:true}],
  ['pc_light', {width:1440,height:1000}, 'light', 'position extérieure nette', {}],
  ['pc_cap',   {width:1440,height:1000}, 'dark',  'capital', {full:true}],
  ['ipad',     {width:834,height:1112},  'dark',  'coût marginal', {full:true, deplier:true}],
  ['tel',      {width:390,height:844},   'dark',  'capital humain', {full:true}],
];
for (const j of jobs) await tirer(...j);
await b.close();
