import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const A=eval('AUTHORS')||[];
  const has=(a,n)=>[].concat(a.chapters||[]).map(String).includes(String(n));
  const out={};
  [9,10,21].forEach(n=>{ out[n]=A.filter(a=>has(a,n)).map(a=>({name:a.name,dates:a.dates,courant:a.courant,idea:a.idea,oeuvres:a.oeuvres||[],detail:a.detail,phrase:a.phrase})); });
  return out;
});
fs.writeFileSync('auteurs_9_10_21.json', JSON.stringify(r,null,1));
[9,10,21].forEach(n=>{
  console.log('\n===== chapitre '+n+' ('+r[n].length+' auteurs) =====');
  r[n].forEach(a=>console.log('  '+a.name+' ['+(a.dates||'—')+'] · '+(a.courant||'—')+' · oeuvres:'+a.oeuvres.length+' · phrase:'+(a.phrase?'oui':'NON')+' · detail:'+(a.detail?'oui':'NON')+' · idea:'+(a.idea?'oui':'NON')));
});
await b.close();
