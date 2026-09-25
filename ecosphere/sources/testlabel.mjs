import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1280,height:900}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v174.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(async ()=>{
  const o={};
  o.carteNum = document.querySelector('.cg [data-c="21"] .cc-num')?.textContent;
  o.carteTitre = document.querySelector('.cg [data-c="21"] .cc-title')?.textContent;
  o.badge = !!document.querySelector('.cg [data-c="21"] .tag-a2');
  // cours
  window.openCh(21); await new Promise(r=>setTimeout(r,900));
  const cp=document.getElementById('pg-chapter');
  o.enTete = (cp?.innerText||'').split('\n').slice(0,2).join(' | ');
  o.coursTexte=(cp?.innerText||'').length; o.coursH2=cp?cp.querySelectorAll('h2').length:0;
  o.resteChapitre21 = /chapitre\s*21/i.test(cp?.innerText||'');
  // chapitre 1 de 1re annee : doit rester "Chapitre 1"
  window.openCh(1); await new Promise(r=>setTimeout(r,700));
  o.ch1Annee1 = (document.getElementById('pg-chapter')?.innerText||'').split('\n')[0];
  // quiz
  window.showPg('quiz'); await new Promise(r=>setTimeout(r,400));
  o.boutonsQuiz = [...document.querySelectorAll('.quiz-options-grid .qo-btn')].map(b=>b.innerText.split('\n')[0]).slice(-4);
  window.startQuiz(21); await new Promise(r=>setTimeout(r,900));
  o.quizEnTete=(document.getElementById('quiz-area')?.innerText||'').slice(0,150).replace(/\n/g,' | ');
  // cartes
  window.showPg('maps'); await new Promise(r=>setTimeout(r,400));
  if(window.renderMaps) window.renderMaps(21);
  await new Promise(r=>setTimeout(r,800));
  o.ongletsCartes=[...document.querySelectorAll('.map-btn')].map(b=>b.textContent).join(' | ');
  o.carteSvg=document.getElementById('visual-map-area')?.querySelectorAll('svg').length;
  // sujets
  window.showPg('subjects'); await new Promise(r=>setTimeout(r,600));
  o.ongletsSujets=[...document.querySelectorAll('#subjTabsPremium .subj-tab')].map(b=>b.textContent).slice(-3).join(' | ');
  if(window.setSubjectChapterPremium) window.setSubjectChapterPremium(21);
  await new Promise(r=>setTimeout(r,600));
  o.listeSujets=(document.getElementById('subjListPremium')?.innerText||'').slice(0,80).replace(/\n/g,' | ');
  // recherche
  window.showPg('search'); await new Promise(r=>setTimeout(r,300));
  const si=document.getElementById('si'); o.recherche={};
  for(const t of ['courbe de l’éléphant','balance des paiements','slowbalization','termes de l’échange']){
    si.value=t; window.doSearch(); await new Promise(r=>setTimeout(r,250));
    o.recherche[t]=(document.getElementById('search-res')?.innerText||'').slice(0,72).replace(/\n/g,' | ');
  }
  window.showPg('home'); await new Promise(r=>setTimeout(r,500));
  o.compteur=document.querySelectorAll('.stat .n')[0]?.textContent;
  return o;
});
console.log(JSON.stringify(r,null,1));
console.log('\nERREURS JS :', errs.length); [...new Set(errs)].slice(0,5).forEach(e=>console.log('  - '+e));
await p.evaluate(async()=>{window.showPg('home'); await new Promise(r=>setTimeout(r,500));
  document.querySelector('.cg [data-c="21"]')?.scrollIntoView({block:'center'});});
await p.waitForTimeout(500); await p.screenshot({path:'shot_home21.png'});
await p.evaluate(async()=>{window.openCh(21); await new Promise(r=>setTimeout(r,900));});
await p.waitForTimeout(500); await p.screenshot({path:'shot_cours21.png'});
await b.close();
