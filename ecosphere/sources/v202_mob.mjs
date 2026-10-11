import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:390,height:844}, deviceScaleFactor:2, isMobile:true,
  hasTouch:true});
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,200)));
await p.goto('file://'+process.cwd()+'/app_v202.html',{waitUntil:'load',timeout:300000});
await p.waitForTimeout(14000);
await p.evaluate(()=>{
  const b=[...document.querySelectorAll('.nt')].find(x=>(x.getAttribute('onclick')||'').includes("'resumes'"));
  if(b) b.click();
});
await p.waitForTimeout(1200);
const l = await p.evaluate(()=>({
  ovf: document.documentElement.scrollWidth - window.innerWidth,
  barre: ['rs-q','rs-an','rs-ch'].map(id=>{
    const e=document.getElementById(id); const r=e.getBoundingClientRect();
    return id+' '+Math.round(r.width)+'×'+Math.round(r.height);
  }),
  cartes: document.querySelectorAll('#pg-resumes .rs-card').length,
  largeurCarte: Math.round((document.querySelector('#pg-resumes .rs-card')||{getBoundingClientRect:()=>({width:0})}).getBoundingClientRect().width),
}));
console.log('liste mobile :', JSON.stringify(l));
await p.screenshot({path:'v202_mob_liste.png'});

await p.evaluate(()=>window.ouvrirResume('23'));
await p.waitForTimeout(900);
const d = await p.evaluate(()=>{
  const el=s=>document.querySelector('#pg-resumes '+s);
  const r=(s)=>{const e=el(s); if(!e) return null; const x=e.getBoundingClientRect();
    return Math.round(x.left)+'..'+Math.round(x.right);};
  return {
    ovf: document.documentElement.scrollWidth - window.innerWidth,
    scrollW: document.documentElement.scrollWidth,
    titre: r('.rs-det-t'), plan: r('.rs-plan'), partie: r('.rs-part'),
    mec: r('.rs-mec'), ae: r('.rs-ae-c'), min: r('.rs-min'),
    compteurPart: getComputedStyle(el('.rs-part-c')).display,
    outils: document.querySelectorAll('#pg-resumes .rs-tool').length,
    hauteur: Math.round(el('.rs-wrap').getBoundingClientRect().height),
  };
});
console.log('détail mobile ch23 :', JSON.stringify(d));
await p.screenshot({path:'v202_mob_det.png'});

const pli = await p.evaluate(()=>{
  document.getElementById('rs-fermer').click();
  return {replies:[...document.querySelectorAll('#pg-resumes .rs-part-b')]
    .filter(x=>x.style.display==='none').length,
    hauteur:Math.round(document.querySelector('#pg-resumes .rs-wrap').getBoundingClientRect().height),
    ovf: document.documentElement.scrollWidth - window.innerWidth};
});
console.log('tout replié :', JSON.stringify(pli));
await p.screenshot({path:'v202_mob_plie.png'});

// un chapitre de première année, pour vérifier le rendu sans gras
await p.evaluate(()=>window.ouvrirResume('5'));
await p.waitForTimeout(700);
console.log('ch5 mobile ovf :', await p.evaluate(()=>document.documentElement.scrollWidth-window.innerWidth));
await p.screenshot({path:'v202_mob_ch5.png'});

console.log('erreurs JS :', errs.length, errs.slice(0,3));
await b.close();
