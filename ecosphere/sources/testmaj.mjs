import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v177.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5800);
const r=await p.evaluate(async ()=>{
  const G=n=>{try{return eval(n)}catch(e){return undefined}};
  const o={};
  const AU=G('AUTHORS')||[];
  o.auteursTotal=AU.length;
  o.parCh={};
  AU.forEach(a=>{ (Array.isArray(a.chapters)?a.chapters:[a.ch]).forEach(c=>{o.parCh[c]=(o.parCh[c]||0)+1;}); });
  o.avecOeuvres=AU.filter(a=>a.oeuvres&&a.oeuvres.length).length;
  // fiches : puces
  window.showPg('fc'); await new Promise(r=>setTimeout(r,900));
  o.chips=[...document.querySelectorAll('#pg-fc .fc-controls button')].map(x=>x.textContent.trim());
  // filtre ch9 opérationnel ?
  window.filterFC(9); await new Promise(r=>setTimeout(r,600));
  o.fcCh9=document.querySelectorAll('#pg-fc .fcard:not([style*="display: none"]), #pg-fc .fc-card:not([style*="display: none"])').length;
  o.fcStat=(document.getElementById('pg-fc')?.innerText||'').match(/[^\n]*fiche[^\n]*/i)?.[0]||'';
  window.filterFC(21); await new Promise(r=>setTimeout(r,600));
  o.fcCh21stat=(document.getElementById('pg-fc')?.innerText||'').match(/[^\n]*fiche[^\n]*/i)?.[0]||'';
  // recherche
  window.showPg('search'); await new Promise(r=>setTimeout(r,400));
  const si=document.getElementById('si'); o.recherche={};
  for(const t of ['Crozier','Michalet','Le Quai de Ouistreham','Apocalypse cognitive','Chamberlin','Les Métamorphoses de la question sociale','Bairoch','Stolper']){
    si.value=t; window.doSearch(); await new Promise(r=>setTimeout(r,250));
    o.recherche[t]=(document.getElementById('search-res')?.innerText||'').split('\n').slice(0,2).join(' | ').slice(0,78);
  }
  // page auteurs
  window.showPg('authors'); await new Promise(r=>setTimeout(r,800));
  const at=document.getElementById('pg-authors')?.innerText||'';
  o.auteursAffiches=['Michel Crozier','Émile Durkheim','Charles-Albert Michalet','Emmanuel Combe','Florence Aubenas'].map(n=>({n, present:at.includes(n)}));
  return o;
});
console.log('AUTEURS total :', r.auteursTotal, '| avec œuvres :', r.avecOeuvres);
console.log('par chapitre  :', JSON.stringify(r.parCh));
console.log('\nPUCES FICHES :', r.chips.join(' | '));
console.log('filtre Ch.9  :', r.fcStat);
console.log('filtre 2e an :', r.fcCh21stat);
console.log('\nRECHERCHE :');
for(const [k,v] of Object.entries(r.recherche)) console.log(`   ${k.padEnd(38)} → ${v}`);
console.log('\nPAGE AUTEURS :'); r.auteursAffiches.forEach(x=>console.log(`   ${x.present?'✓':'✗'} ${x.n}`));
console.log('\nERREURS JS :', errs.length); [...new Set(errs)].slice(0,4).forEach(e=>console.log('  - '+e));
await b.close();
