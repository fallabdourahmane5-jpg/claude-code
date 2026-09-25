import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html'); await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const d=document.createElement('div'); d.innerHTML=CH[21].cours;
  const t=d.textContent.replace(/\s+/g,' ');
  const keys=['Michalet','Baldwin','Bairoch','Milanovic','éléphant','Prebisch','Stolper','Hawley','List','étalon-or','Giraud','Hélène Rey','Nurkse','Acemoglu','taux d’ouverture','valeur ajoutée','DIPP','slowbalization','privilège exorbitant','arsenalisation','BRICS','Volcker','Béraud','malédiction','déficits jumeaux','termes de l’échange'];
  const out={};
  keys.forEach(k=>{ const i=t.indexOf(k); out[k]= i<0?null:t.slice(Math.max(0,i-240), i+380); });
  return out;
});
Object.entries(r).forEach(([k,v])=>console.log('### '+k+'\n'+(v||'ABSENT')+'\n'));
await b.close();
