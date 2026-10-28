import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const F='file://'+process.argv[2], W=+(process.argv[3]||1440);
const b=await chromium.launch();
const p=await b.newPage({viewport:{width:W,height:900},deviceScaleFactor:1,isMobile:W<700,hasTouch:W<700});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
p.on('console',m=>{if(m.type()==='error')errs.push('CONSOLE '+m.text());});
await p.goto(F); await p.waitForTimeout(1200);
await p.evaluate(()=>showPg('visualisations')); await p.waitForTimeout(600);
const n=await p.evaluate(()=>document.querySelectorAll('#vzGrid .vz-card').length);
console.log('cartes', n, '| stats', await p.evaluate(()=>document.getElementById('vzStats').textContent));
let ko=0;
for(let i=0;i<n;i++){
  await p.evaluate(i=>{ if(window.VZ_OUVRIR_I) VZ_OUVRIR_I(i); else document.querySelectorAll('#vzGrid .vz-card')[i].click(); }, i);
  await p.waitForTimeout(600);
  const r=await p.evaluate(()=>{
    const g=i=>document.getElementById(i); const w=g('vzWorld');
    const etroit=g('vzView').clientWidth<700; const av=w.classList.contains('loin');
    if(!etroit) w.classList.add('loin');
    const nb=[...document.querySelectorAll('#vzWorld .vz-node')].map(x=>({t:(x.querySelector('.vzt')||{}).textContent,x:parseFloat(x.style.left),y:parseFloat(x.style.top),w:x.offsetWidth,h:x.offsetHeight}));
    const lb=[...document.querySelectorAll('#vzWorld .vz-lab')].map(l=>({t:l.textContent,x:parseFloat(l.style.left)-l.offsetWidth/2,y:parseFloat(l.style.top)-l.offsetHeight/2,w:l.offsetWidth,h:l.offsetHeight}));
    if(!av&&!etroit) w.classList.remove('loin');
    const I=(a,c)=>Math.min(a.x+a.w,c.x+c.w)-Math.max(a.x,c.x)>0&&Math.min(a.y+a.h,c.y+c.h)-Math.max(a.y,c.y)>0;
    const bad=[];
    for(let i=0;i<nb.length;i++)for(let j=i+1;j<nb.length;j++) if(I(nb[i],nb[j])) bad.push('NN');
    lb.forEach(l=>nb.forEach(x=>{if(I(l,x))bad.push('LN '+l.t.slice(0,16));}));
    for(let i=0;i<lb.length;i++)for(let j=i+1;j<lb.length;j++) if(I(lb[i],lb[j])) bad.push('LL');
    const titre=(document.querySelector('#vzStage h2')||{}).textContent||'';
    return {titre:titre.slice(0,42), z:(g('vzZ')||{}).textContent, n:nb.length, l:lb.length, bad};
  });
  if(r.bad.length) ko++;
  console.log(String(i).padStart(2), r.z.padStart(5), String(r.n).padStart(3)+'n', String(r.l).padStart(3)+'l', r.titre.padEnd(44), r.bad.length?JSON.stringify(r.bad.slice(0,3)):'ok');
  await p.click('#vzRetour'); await p.waitForTimeout(350);
}
console.log('themes en defaut:', ko, '| erreurs js:', errs.length?errs.slice(0,4):'aucune');
await b.close();
