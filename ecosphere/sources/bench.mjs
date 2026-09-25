import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const mots=['Coase','Simon','Chandler','Jensen','Marshall','Chamberlin','Baumol','Combe','Crozier','Weber','Durkheim','Mayo','Bronner','Morel','Castel','Aubenas','Asch','Janis','Michalet','Baldwin','Bairoch','Milanovic','Prebisch','Nurkse','Volcker','List','Giraud','Hélène Rey','Acemoglu','Béraud'];
async function run(f){
  const p=await b.newPage(); await p.goto('file://'+process.cwd()+'/'+f); await p.waitForTimeout(5000);
  await p.evaluate(()=>window.showPg('search')); await p.waitForTimeout(600);
  const out={};
  for(const m of mots){
    out[m]=await p.evaluate(async (m)=>{
      const si=document.getElementById('si'); si.value=m; si.dispatchEvent(new Event('input',{bubbles:true}));
      await new Promise(r=>setTimeout(r,320));
      return document.querySelectorAll('#pg-search .ri').length;
    }, m);
  }
  await p.close(); return out;
}
const A=await run('app_v180.html'), B=await run('app_v181.html');
let ga=0,gb=0,amel=0;
console.log('terme'.padEnd(14)+'avant'.padStart(7)+'après'.padStart(7)+'   gain');
mots.forEach(m=>{ ga+=A[m]; gb+=B[m]; if(B[m]>A[m])amel++;
  console.log(m.padEnd(14)+String(A[m]).padStart(7)+String(B[m]).padStart(7)+'   '+(B[m]-A[m]>0?'+'+(B[m]-A[m]):'='));});
console.log('\nTOTAL'.padEnd(14)+String(ga).padStart(7)+String(gb).padStart(7));
console.log('termes améliorés : '+amel+'/'+mots.length+' · aucun en régression : '+mots.every(m=>B[m]>=A[m]));
await b.close();
