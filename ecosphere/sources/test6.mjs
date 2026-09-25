import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message.split('\n')[0]));
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v176.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(async ()=>{
  const o={};
  o.clesV83=Object.keys(window.VISUAL_MAPS_V83||{});
  o.clesMap=Object.keys((function(){try{return MAP_DATA}catch(e){return {}}})());
  window.showPg('maps'); await new Promise(r=>setTimeout(r,700));
  o.onglets=[...document.querySelectorAll('.map-btn')].map(x=>x.textContent);
  if(window.renderMaps) window.renderMaps(6);
  await new Promise(r=>setTimeout(r,800));
  const a=document.getElementById('visual-map-area');
  o.racine=[...a.querySelectorAll('.v83-root-t')].map(t=>t.textContent).join(' ');
  o.branches=[...a.querySelectorAll('.v83-main-t')].map(t=>t.textContent);
  o.nbNoeuds=a.querySelectorAll('.v83-node').length;
  o.panneau=(document.getElementById('pg-maps')?.innerText||'').includes('Schémas clés');
  o.sousTitre=(document.getElementById('visual-map-sub')?.textContent||'').slice(0,70);
  // les autres chapitres restent corrects
  o.controle={};
  for(const ch of [1,5,7,9,10,21]){
    window.renderVisualMap(ch); await new Promise(r=>setTimeout(r,320));
    o.controle['ch'+ch]=[...document.querySelectorAll('#visual-map-area .v83-root-t')].map(t=>t.textContent).join(' ').slice(0,42);
  }
  return o;
});
console.log('clés VISUAL_MAPS_V83 :', r.clesV83.join(', '));
console.log('clés MAP_DATA        :', r.clesMap.join(', '));
console.log('onglets Cartes       :', r.onglets.join(' | '));
console.log();
console.log('  chapitre 6 :', r.nbNoeuds, 'nœuds | racine =', JSON.stringify(r.racine));
console.log('  branches   :', r.branches.join(' / '));
console.log('  sous-titre :', r.sousTitre);
console.log('  panneau schémas présent :', r.panneau);
console.log('\n  contrôle des autres cartes :');
for(const [k,v] of Object.entries(r.controle)) console.log(`    ${k.padEnd(5)} ${v}`);
console.log('\nERREURS JS :', errs.length); [...new Set(errs)].slice(0,4).forEach(e=>console.log('  - '+e));
await p.evaluate(async()=>{window.showPg('maps'); await new Promise(r=>setTimeout(r,400));
  window.renderMaps&&window.renderMaps(6); await new Promise(r=>setTimeout(r,800));});
await p.waitForTimeout(500); await p.screenshot({path:'map_ch6.png'});
await b.close();
