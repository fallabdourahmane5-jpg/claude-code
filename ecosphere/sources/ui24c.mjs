import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:Number(process.argv[3]||1400),height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const out={};
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(400);
for (const q of ['Cairns','multifibres','Kindleberger','detournement de trafic','bol de spaghettis','Seattle','arachide','O’Rourke']) {
  out['rech_'+q] = await p.evaluate((q)=>{ const i=document.getElementById('si'); i.value=q; doSearch();
    const t=document.getElementById('search-res').innerText;
    return {n:(t.match(/\n/g)||[]).length, ch24:/2ᵉ ANNÉE — CHAPITRE 4|2ᵉ année — chapitre 4|CHAPITRE 4/i.test(t), tete:t.slice(0,140).replace(/\n/g,' | ')};
  }, q);
  await p.waitForTimeout(200);
}
// mobile-friendly checks
out.overflow = await p.evaluate(()=>{
  const r=[];
  ['home','chapter','fc','maps','atlas','subjects','quiz','frise','chiffres','resumes','authors'].forEach(id=>{
    const el=document.getElementById('pg-'+id);
    if(el && el.scrollWidth > document.documentElement.clientWidth+2) r.push(id+':'+el.scrollWidth);
  });
  return r;
});
console.log(JSON.stringify(out,null,1)); console.log('erreurs',errs.length,errs.slice(0,5));
await b.close();
