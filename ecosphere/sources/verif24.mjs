import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const f = process.argv[2];
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs = [];
p.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
p.on('console', m => { if (m.type()==='error') errs.push('CONSOLE ' + m.text().slice(0,200)); });
await p.goto('file://' + f);
await p.waitForTimeout(14000);

const r = await p.evaluate(() => {
  const o = {};
  o.chContent = typeof CH_CONTENT!=='undefined' ? Object.keys(CH_CONTENT) : null;
  o.ch24 = typeof CH_CONTENT!=='undefined' && CH_CONTENT[24] ? {
    title: CH_CONTENT[24].title, cours: CH_CONTENT[24].cours.length,
    notions: CH_CONTENT[24].notions.length, methode: (CH_CONTENT[24].methode||'').length,
    numAnnee: CH_CONTENT[24].numAnnee } : null;
  o.fc24 = typeof FC_DATA!=='undefined' ? FC_DATA.filter(c=>Number(c.ch)===24).length : null;
  o.fcTotal = typeof FC_DATA!=='undefined' ? FC_DATA.length : null;
  o.quizBank24 = window.ECOSPHERE_QUESTION_BANK ? (window.ECOSPHERE_QUESTION_BANK[24]||[]).length : null;
  o.advBank24 = window.__ECO_ADV_ALL_BANK ? window.__ECO_ADV_ALL_BANK.filter(q=>Number(q.ch)===24).length : null;
  o.advTags24 = window.__ECO_ADV_ALL_BANK ? window.__ECO_ADV_ALL_BANK.filter(q=>Number(q.ch)===24 && (q.tags||[]).length>2).length : null;
  o.map24 = typeof MAP_DATA!=='undefined' && MAP_DATA[24] ? 1 : 0;
  o.vmap24 = typeof VISUAL_MAPS_V83!=='undefined' && VISUAL_MAPS_V83[24] ?
     {branches: VISUAL_MAPS_V83[24].branches.length,
      sous: VISUAL_MAPS_V83[24].branches.reduce((a,x)=>a+(x.children||x.sub||[]).length,0)} : null;
  o.authors24 = typeof AUTHORS!=='undefined' ? AUTHORS.filter(a=>(a.chapters||[]).map(String).includes('24')).length : null;
  o.authorsTotal = typeof AUTHORS!=='undefined' ? AUTHORS.length : null;
  o.suj24 = typeof SUBJECTS_BANK_PREMIUM!=='undefined' ? SUBJECTS_BANK_PREMIUM.filter(x=>Number(x.chapter)===24).length : null;
  o.sujTotal = typeof SUBJECTS_BANK_PREMIUM!=='undefined' ? SUBJECTS_BANK_PREMIUM.length : null;
  o.mobiliser24 = typeof SUBJECTS_BANK_PREMIUM!=='undefined' ? SUBJECTS_BANK_PREMIUM.filter(x=>String(x.mobiliser||'').includes('2ᵉ année ch. 4')).length : null;
  o.argsAjoutes = typeof SUBJECTS_BANK_PREMIUM!=='undefined' ? SUBJECTS_BANK_PREMIUM.filter(x=>x.__ch24).length : null;
  o.bilan = window.__ECO_CH24_BILAN || null;
  o.cg = [...document.querySelectorAll('.cg [data-c]')].map(e=>e.getAttribute('data-c'));
  return o;
});
console.log(JSON.stringify(r, null, 1));
console.log('--- erreurs:', errs.length);
errs.slice(0,15).forEach(e=>console.log('   ', e));
await b.close();
