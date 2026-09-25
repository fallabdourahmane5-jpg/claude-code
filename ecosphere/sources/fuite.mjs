import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v174.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(async ()=>{
  const fuites={};
  const RE=/chapitres?\s*0*21\b/i;
  const pages=['home','quiz','fc','search','authors','subjects','visualisations','method','graphs','maps','formulas','timeline','prog'];
  for(const pg of pages){
    window.showPg(pg); await new Promise(r=>setTimeout(r,450));
    const t=document.getElementById('pg-'+pg)?.innerText||'';
    const m=t.split('\n').filter(l=>RE.test(l));
    if(m.length) fuites[pg]=m.slice(0,3);
  }
  // cours du chapitre + navigation quiz sur plusieurs questions
  window.openCh(21); await new Promise(r=>setTimeout(r,900));
  let t=document.getElementById('pg-chapter')?.innerText||'';
  if(RE.test(t)) fuites['cours']=t.split('\n').filter(l=>RE.test(l)).slice(0,3);
  window.showPg('quiz'); await new Promise(r=>setTimeout(r,300));
  window.startQuiz(21); await new Promise(r=>setTimeout(r,800));
  for(let k=0;k<3;k++){
    const btn=document.querySelector('#quiz-area .opt, #quiz-area button');
    if(btn) btn.click();
    await new Promise(r=>setTimeout(r,450));
    const qt=document.getElementById('quiz-area')?.innerText||'';
    if(RE.test(qt)){ fuites['quiz-q'+k]=qt.split('\n').filter(l=>RE.test(l)).slice(0,2); }
  }
  // sujets du chapitre
  window.showPg('subjects'); await new Promise(r=>setTimeout(r,400));
  window.setSubjectChapterPremium && window.setSubjectChapterPremium(21);
  await new Promise(r=>setTimeout(r,600));
  const st=document.getElementById('pg-subjects')?.innerText||'';
  if(RE.test(st)) fuites['sujets-liste']=st.split('\n').filter(l=>RE.test(l)).slice(0,3);
  return fuites;
});
const n=Object.keys(r).length;
console.log(n===0 ? 'AUCUNE FUITE DE « Chapitre 21 » sur les 13 pages, le cours, le quiz et les sujets'
                  : JSON.stringify(r,null,1));
console.log('ERREURS JS :', errs.length);
await b.close();
