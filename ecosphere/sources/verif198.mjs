import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const out = {};
for (const f of ['app_v197.html','app_v198.html']) {
  const p = await b.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(String(e).slice(0,160)));
  p.on('console',m=>{if(m.type()==='error'&&!/CERT/.test(m.text()))errs.push('c:'+m.text().slice(0,120));});
  await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'load',timeout:240000});
  const perf = await p.evaluate(()=>{const t=performance.timing;return t.domComplete-t.navigationStart;});
  await p.waitForTimeout(15000);
  const r = await p.evaluate(async ()=>{
    const sleep=ms=>new Promise(r=>setTimeout(r,ms));
    const o={};
    const S=window.SUBJECTS_BANK_PREMIUM||[];
    o.total=S.length;
    const par={}; S.forEach(x=>{par[x.chapter]=(par[x.chapter]||0)+1;}); o.parCh=par;
    o.sousVingt=Object.entries(par).filter(([k,v])=>v<20).map(([k,v])=>k+':'+v);
    o.AUTHORS=AUTHORS.length; o.FC=FC_DATA.length; o.SI=SEARCH_INDEX.length;
    o.CHC=Object.keys(CH_CONTENT).length; o.nav=document.querySelectorAll('.nt').length;
    o.pages=document.querySelectorAll('.pg').length;
    o.quizTotal=Object.values(window.ECOSPHERE_QUESTION_BANK||{}).flat().length;
    o.bilan198=window.__ECO_SUJ198_BILAN||null;
    // page Sujets
    showPg('subjects'); await sleep(1500);
    const cards=[...document.querySelectorAll('#subjChaptersPremium .subj-ch-card')];
    o.cartes=cards.map(c=>(c.innerText||'').split('\n').filter(Boolean).map(t=>t.trim()).join(' | '));
    o.nbCartes=cards.length;
    // rendu par chapitre
    o.rendu={};
    for (const ch of [4,8,23]) {
      try{ setSubjectChapterPremium(ch); await sleep(700);
        o.rendu[ch]=document.querySelectorAll('#pg-subjects .subj-card, #pg-subjects .subject-item').length; }
      catch(e){ o.rendu[ch]='err'; }
    }
    // un corrige doit s'afficher
    try{
      setSubjectChapterPremium(8); await sleep(600);
      const btn=[...document.querySelectorAll('#pg-subjects button')].find(x=>/Afficher le corrigé/.test(x.textContent));
      if(btn){ btn.click(); await sleep(800);
        o.corrige=(document.getElementById('pg-subjects').innerText||'').length; }
    }catch(e){ o.corrige='err '+e; }
    return o;
  });
  out[f]={perf,nErrs:errs.length,errs:errs.slice(0,4),...r};
  await p.close();
}
console.log(JSON.stringify(out,null,1));
await b.close();
