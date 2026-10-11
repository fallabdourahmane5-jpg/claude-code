import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const mesure = async (fichier) => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1400,height:1000}});
  const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,120)));
  const t0=Date.now();
  await p.goto('file://'+process.cwd()+'/'+fichier,{waitUntil:'load',timeout:240000});
  await p.waitForTimeout(16000);
  const o = await p.evaluate(()=>{
    const g={};
    try{ g.AUTHORS=AUTHORS.length; }catch(e){ g.AUTHORS='n/a'; }
    try{ g.FC=FC_DATA.length; }catch(e){ g.FC='n/a'; }
    try{ g.SI=SEARCH_INDEX.length; }catch(e){ g.SI='n/a'; }
    try{ g.CHC=Object.keys(CH_CONTENT).length; }catch(e){ g.CHC='n/a'; }
    try{ g.SUBJ=Object.values(SUBJECTS_DB||{}).reduce((a,x)=>a+(x.length||0),0); }catch(e){ g.SUBJ='n/a'; }
    try{ g.QUIZ=Object.values(QB).reduce((a,x)=>a+(x.length||0),0); }catch(e){ g.QUIZ='n/a'; }
    try{ g.VMAPS=Object.keys(VISUAL_MAPS_V83).length; }catch(e){ g.VMAPS='n/a'; }
    g.nav=document.querySelectorAll('.nt').length;
    g.pages=document.querySelectorAll('.pg').length;
    g.perf=Math.round(performance.timing.domComplete-performance.timing.navigationStart);
    return g;
  });
  o.chargement=Date.now()-t0; o.errs=errs.length; o.err1=errs[0]||'';
  await b.close(); return o;
};
const a = await mesure('app_v200.html');
const c = await mesure('app_v202.html');
console.log('champ        v200        v202');
for (const k of Object.keys(a)) console.log(String(k).padEnd(12), String(a[k]).padEnd(11), String(c[k]));
