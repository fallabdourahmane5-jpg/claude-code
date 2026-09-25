import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v178.html'); await p.waitForTimeout(3000);
const r = await p.evaluate(()=>{
  const CH = eval('CH_CONTENT');
  const d=document.createElement('div'); d.innerHTML=CH[10].cours;
  const t=d.textContent.replace(/\s+/g,' ');
  const keys=['Challenger','Simone Weil','Apocalypse','Démocratie des crédules','Brandolini','syndicalisation','Hawthorne','Western Electric','SEITA','désindustrialisation','Matignon','halo','grande démission','Asch','Janis','Kahneman','Akerlof','Williamson','tertiaire','salariat'];
  const out={};
  keys.forEach(k=>{ const i=t.indexOf(k); out[k]= i<0?null:t.slice(Math.max(0,i-260), i+360); });
  return out;
});
Object.entries(r).forEach(([k,v])=>console.log('### '+k+'\n'+(v||'ABSENT')+'\n'));
await b.close();
