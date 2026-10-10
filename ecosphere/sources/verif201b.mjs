import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,180)));
await p.goto('file://'+process.cwd()+'/app_v201.html',{waitUntil:'load',timeout:240000});
await p.waitForTimeout(16000);
const r = await p.evaluate(async ()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const o={liens:{}};
  const ouvre=async(ch)=>{ ouvrirResume(String(ch)); await sleep(700); };
  const cible=(attr)=>document.querySelector('#pg-resumes [data-'+attr+']');
  for(const [attr,label] of [['cours','Cours'],['fiches','Fiches'],['carte','Carte'],['atlas','Atlas'],['chiffres','Chiffres'],['sujets','Sujets']]){
    await ouvre(22);
    const el=cible(attr);
    if(!el){ o.liens[label]='bouton absent'; continue; }
    el.click(); await sleep(1400);
    const pg=(document.querySelector('.pg.on')||{}).id;
    let detail='';
    if(attr==='carte'){ detail=' map='+String(window.currentMapCh); }
    if(attr==='atlas'){ const s=document.getElementById('at-ch'); detail=' at-ch='+(s?s.value:'?'); }
    if(attr==='chiffres'){ const c=document.querySelector('#pg-chiffres .cf-chip.on'); detail=' chip='+(c?c.textContent.trim():'?'); }
    if(attr==='cours'){ const t=document.querySelector('#pg-chapter h1,#pg-chapter h2'); detail=' titre='+(t?t.textContent.trim().slice(0,46):'?'); }
    if(attr==='sujets'){ const n=document.querySelectorAll('#pg-subjects .subj-card,#pg-subjects [class*=subj]').length; detail=' blocs='+n; }
    if(attr==='fiches'){ const n=document.querySelectorAll('#pg-fc .fc-card,#pg-fc [class*=fcard]').length; detail=' blocs='+n; }
    o.liens[label]=pg+detail;
  }
  // recherche globale
  showPg('search'); await sleep(900);
  try{ o.SIresumes=SEARCH_INDEX.filter(x=>x.type==='résumé').length; }catch(e){ o.SIresumes='err'; }
  const si=document.getElementById('si');
  si.value='commerce international'; doSearch(); await sleep(400);
  const it=[...document.querySelectorAll('#search-res .ri')];
  o.rechGlobale=it.length;
  o.rechResume=it.filter(x=>/résumé/i.test(x.querySelector('.ri-type').textContent)).length;
  const c0=it.find(x=>/résumé/i.test(x.querySelector('.ri-type').textContent));
  if(c0){ c0.click(); await sleep(1000); o.apresClic=(document.querySelector('.pg.on')||{}).id
    + ' / ' + ((document.querySelector('#pg-resumes .rs-det-t')||{}).textContent||''); }
  // les autres sections fonctionnent toujours
  const etats={};
  for(const pg of ['home','quiz','fc','authors','atlas','subjects','maps','frise','chiffres','prog']){
    showPg(pg); await sleep(260);
    etats[pg]=(document.querySelector('.pg.on')||{}).id;
  }
  o.autresPages=etats;
  return o;
});
console.log(JSON.stringify({nErrs:errs.length,errs:errs.slice(0,5),...r},null,1));
await b.close();
