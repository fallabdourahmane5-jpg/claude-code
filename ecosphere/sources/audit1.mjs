import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v176.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(()=>{
  const G=n=>{try{return eval(n)}catch(e){return undefined}};
  const CH=G('CH_CONTENT')||{}, FC=G('FC_DATA')||[], AU=G('AUTHORS')||[], SI=G('SEARCH_INDEX')||[];
  const out={chapitres:{}, auteurs:{total:AU.length, champs:AU[0]?Object.keys(AU[0]):[], parCh:{}, noms:AU.map(a=>a.name)}};
  Object.keys(CH).forEach(k=>{
    out.chapitres[k]={titre:CH[k].title, cours:(CH[k].cours||'').length,
      notions:(CH[k].notions||[]).length,
      fiches:FC.filter(f=>String(f.ch)===String(k)).length,
      recherche:SI.filter(x=>String(x.ch)===String(k)).length};
  });
  AU.forEach(a=>{ const c=a.ch||'?'; out.auteurs.parCh[c]=(out.auteurs.parCh[c]||0)+1; });
  out.fichesTotal=FC.length; out.fichesSansCh=FC.filter(f=>!f.ch).length;
  out.fcChamps=FC[0]?Object.keys(FC[0]):[];
  out.fcTypes={}; FC.forEach(f=>{out.fcTypes[f.type||'(aucun)']=(out.fcTypes[f.type||'(aucun)']||0)+1;});
  return out;
});
console.log('chap | titre                                      | cours   | notions | fiches | recherche');
Object.entries(r.chapitres).forEach(([k,v])=>{
  console.log(`${k.padStart(4)} | ${v.titre.slice(0,42).padEnd(42)} | ${String(v.cours).padStart(7)} | ${String(v.notions).padStart(7)} | ${String(v.fiches).padStart(6)} | ${String(v.recherche).padStart(9)}`);
});
console.log('\nFICHES total:', r.fichesTotal, ' sans chapitre:', r.fichesSansCh);
console.log('champs fiche :', r.fcChamps.join(', '));
console.log('types de fiches :', JSON.stringify(r.fcTypes));
console.log('\nAUTEURS total:', r.auteurs.total);
console.log('champs auteur :', r.auteurs.champs.join(', '));
console.log('auteurs par chapitre :', JSON.stringify(r.auteurs.parCh));
fs.writeFileSync('audit1.json', JSON.stringify(r,null,1));
await b.close();
