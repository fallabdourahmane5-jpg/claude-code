import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
async function probe(file){
  const p = await b.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
  await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/'+file,{waitUntil:'load',timeout:180000});
  await p.waitForTimeout(5200);
  const r = await p.evaluate(async ()=>{
    const G=n=>{try{return eval(n)}catch(e){return undefined}};
    const o={};
    o.search=(G('SEARCH_INDEX')||[]).length;
    o.fiches=(G('FC_DATA')||[]).length;
    o.auteurs=(G('AUTHORS')||[]).length;
    o.sujets=(G('SUBJECTS_BANK_PREMIUM')||[]).length;
    o.cartes=Object.keys(G('MAP_DATA')||{}).length;
    const QB=window.ECOSPHERE_QUESTION_BANK||{};
    o.quiz=Object.keys(QB).reduce((s,k)=>s+QB[k].length,0);
    o.quizAdv=(window.__ECO_ADV_ALL_BANK||[]).length;
    o.glossaire=(G('MANUAL_GLOSSARY')||[]).length;
    o.chapitres=Object.keys(G('CH_CONTENT')||{}).length;
    o.pages={};
    for(const pg of ['home','quiz','fc','search','authors','subjects','visualisations','method','graphs','maps','formulas','timeline','prog']){
      window.showPg(pg); await new Promise(r=>setTimeout(r,260));
      o.pages[pg]=(document.getElementById('pg-'+pg)?.innerText||'').trim().length;
    }
    o.cours={};
    const G2=n=>{try{return eval(n)}catch(e){return undefined}};
    const CH=G2('CH_CONTENT')||{};
    for(const ch of [1,2,3,4,5,6,7,8,9,10,21]){
      if(!CH[ch]){ o.cours[ch]=0; continue; }
      try{ window.openCh(ch); }catch(e){ o.cours[ch]=-1; continue; }
      await new Promise(r=>setTimeout(r,420));
      o.cours[ch]=(document.getElementById('sect-cours')?.innerHTML||'').length;
    }
    return o;
  });
  await p.close(); return {r, errs};
}
const A = await probe('app_v180.html');
const B = await probe('app_v181.html');
console.log('=== SECTIONS (avant → après) ===');
for(const k of ['chapitres','search','fiches','auteurs','sujets','cartes','quiz','quizAdv','glossaire']){
  const d=B.r[k]-A.r[k];
  console.log(`  ${k.padEnd(11)} ${String(A.r[k]).padStart(6)} → ${String(B.r[k]).padStart(6)}  ${d===0?'identique':(d>0?'+'+d:d)}`);
}
console.log('\n=== PAGES ===');
for(const k of Object.keys(A.r.pages)){
  const same=A.r.pages[k]===B.r.pages[k];
  console.log(`  ${k.padEnd(15)} ${String(A.r.pages[k]).padStart(7)} → ${String(B.r.pages[k]).padStart(7)}  ${same?'identique':'modifié'}`);
}
console.log('\n=== COURS ===');
for(const ch of [1,2,3,4,5,6,7,8,9,10,21]){
  const a=A.r.cours[ch]||0, c=B.r.cours[ch]||0;
  const nom = ch===21 ? '2e année ch.1' : ('ch'+ch);
  const tag = ch===21 ? (c>1000?'AJOUTÉ':'*** ABSENT ***') : (a===c?'inchangé':'*** MODIFIÉ ***');
  console.log(`  ${nom.padEnd(14)} ${String(a).padStart(7)} → ${String(c).padStart(7)}   ${tag}`);
}
console.log('\nERREURS JS  avant:',A.errs.length,' après:',B.errs.length);
[...new Set(B.errs)].slice(0,5).forEach(e=>console.log('  - '+e));
await b.close();
