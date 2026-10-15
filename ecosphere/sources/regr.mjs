import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
async function mesure(f, W) {
  const p = await b.newPage({viewport:{width:W,height:950}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://' + f);
  await p.waitForTimeout(14000);
  const r = await p.evaluate(()=>{
    const o={};
    o.chapitres = Object.keys(CH_CONTENT).length;
    o.fiches = FC_DATA.length;
    o.auteurs = AUTHORS.length;
    o.sujets = SUBJECTS_BANK_PREMIUM.length;
    o.quizBanque = window.__ECO_ADV_ALL_BANK ? window.__ECO_ADV_ALL_BANK.length : 0;
    o.cartesVisuelles = typeof VISUAL_MAPS_V83!=='undefined' ? Object.keys(VISUAL_MAPS_V83).length : 0;
    o.mapData = typeof MAP_DATA!=='undefined' ? Object.keys(MAP_DATA).length : 0;
    o.recherche = typeof SEARCH_INDEX!=='undefined' ? SEARCH_INDEX.length : null;
    o.onglets = [...document.querySelectorAll('nav .nt')].length;
    return o;
  });
  // chiffres / resumes / frise / atlas totaux
  const t = await p.evaluate(()=>{
    const o={};
    try{ ouvrirChiffres('1'); }catch(e){}
    return o;
  });
  await p.waitForTimeout(600);
  r.chiffresTotal = await p.evaluate(()=>{
    const el=document.getElementById('pg-chiffres');
    const m = el ? el.innerText.match(/sur (\d+)/) : null; return m?m[1]:null;
  });
  await p.evaluate(()=>showPg('atlas'));
  await p.waitForTimeout(900);
  r.atlasIdees = await p.evaluate(()=>{
    const rz=document.getElementById('at-rz'); if(rz) rz.click();
    const n=document.getElementById('at-nb'); return n?n.textContent:null;
  });
  r.errs = errs.length;
  await p.close();
  return r;
}
const a = await mesure(process.argv[2], 1400);
const c = await mesure(process.argv[3], 1400);
console.log('v204', JSON.stringify(a));
console.log('v205', JSON.stringify(c));
await b.close();
