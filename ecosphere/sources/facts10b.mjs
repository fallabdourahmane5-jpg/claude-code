import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html'); await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const d=document.createElement('div'); d.innerHTML=CH[10].cours;
  const t=d.textContent.replace(/\s+/g,' ');
  const keys=['inégalités de salaire','Toutes choses égales','temps partiel','secteur tertiaire','cage d','désenchantement','idéal-type','neutralité axiologique','zone d’incertitude','ouvriers d’entretien','Métamorphoses','désaffiliation','anomie','solidarité organique','flexibilité','pauvreté laborieuse','permis de conduire','1976','CDD','intérim'];
  const out={};
  keys.forEach(k=>{ const i=t.indexOf(k); out[k]= i<0?null:t.slice(Math.max(0,i-200), i+320); });
  return out;
});
Object.entries(r).forEach(([k,v])=>console.log('### '+k+'\n'+(v||'ABSENT')+'\n'));
await b.close();
