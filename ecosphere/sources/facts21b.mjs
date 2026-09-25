import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html'); await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const d=document.createElement('div'); d.innerHTML=CH[21].cours;
  const t=d.textContent.replace(/\s+/g,' ');
  const keys=['configuration','internationalisation','multinationalisation','globalisation','hypermondialisation','double comptage','iPhone','second dégroupage','Ricardo','HOS','Chine','Europe','relocalisation','balance des paiements','compte financier','compte courant','solde courant','1870','1913','2008','IDE','montée en gamme','semi-conducteur','terres rares','souveraineté'];
  const out={};
  keys.forEach(k=>{ const i=t.indexOf(k); out[k]= i<0?null:t.slice(Math.max(0,i-200), i+340); });
  return out;
});
Object.entries(r).forEach(([k,v])=>console.log('### '+k+'\n'+(v||'ABSENT')+'\n'));
await b.close();
