import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.setViewportSize({width:1440, height:960});
const err=[]; p.on('pageerror',e=>err.push(String(e).slice(0,140)));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const R = {};

// dossier « Autour d'une notion » mis à jour par le chapitre 5
R.dossier = await p.evaluate(()=>{
  try { window.ouvrirNotion('n15-multiplicateur-budgetaire'); } catch(e) { return {err:String(e).slice(0,90)}; }
  return null;
});
await p.waitForTimeout(2000);
R.dossier = await p.evaluate(()=>{
  const z=[...document.querySelectorAll('.pg')].filter(x=>x.offsetParent!==null)[0];
  const t=z?(z.innerText||''):'';
  return {page:z?z.id:'?', ch5:/ch\.\s*5/i.test(t), ch6:/ch\.\s*6/i.test(t),
    signes:t.length, extrait:t.replace(/\s+/g,' ').slice(0,200)};
});
await p.screenshot({path:'f_dossier.png'});

// visualisation mise à jour
await p.evaluate(()=>{ try{ window.VZ_OUVRIR('vz-court-long'); }catch(e){ window.showPg('visualisations'); } });
await p.waitForTimeout(2500);
R.visu = await p.evaluate(()=>{
  const z=[...document.querySelectorAll('.pg')].filter(x=>x.offsetParent!==null)[0];
  const t=z?(z.innerText||''):'';
  return {page:z?z.id:'?', ch5:/ch\.\s*5/i.test(t), ch6:/ch\.\s*6/i.test(t), signes:t.length};
});
await p.screenshot({path:'f_visu.png'});

// chiffres du chapitre 5
await p.evaluate(()=>{ try{ window.ouvrirChiffres('25'); }catch(e){ window.showPg('chiffres'); } });
await p.waitForTimeout(2200);
R.chiffres = await p.evaluate(()=>{
  const z=document.getElementById('pg-chiffres'); const t=z?(z.innerText||''):'';
  return {ch5:/ch\.\s*5|Chapitre 5/i.test(t), cartes:z?z.querySelectorAll('.cardx, .ch-card, article').length:0,
    extrait:t.replace(/\s+/g,' ').slice(0,200)};
});
await p.screenshot({path:'f_chiffres.png'});

// résumé du chapitre 6
await p.evaluate(()=>{ try{ window.ouvrirResume('26'); }catch(e){ window.showPg('resumes'); } });
await p.waitForTimeout(2200);
R.resume = await p.evaluate(()=>{
  const z=document.getElementById('pg-resumes'); const t=z?(z.innerText||''):'';
  return {ch6:/ch\.\s*6|Chapitre 6/i.test(t), signes:t.length,
    extrait:t.replace(/\s+/g,' ').slice(0,200)};
});
await p.screenshot({path:'f_resume.png'});

// Atlas : entrée de Richard Lipsey
await p.evaluate(()=>{ try{ window.allerAtlas && window.allerAtlas('Richard Lipsey'); }catch(e){} window.showPg('atlas'); });
await p.waitForTimeout(2000);
R.atlas = await p.evaluate(()=>{
  const z=document.getElementById('pg-atlas'); const t=z?(z.innerText||''):'';
  return {lipsey:t.indexOf('Lipsey')>=0, ch5:/ch\.\s*5/i.test(t), ch6:/ch\.\s*6/i.test(t), signes:t.length};
});
await p.screenshot({path:'f_atlas.png'});

R.err = err;
fs.writeFileSync('verif_final.json', JSON.stringify(R,null,1));
console.log(JSON.stringify(R,null,1));
await b.close();
