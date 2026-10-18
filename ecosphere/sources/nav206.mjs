import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
console.log(JSON.stringify(await p.evaluate(()=>({
  onglets:[...document.querySelectorAll('nav .nt')].map(x=>x.textContent.trim())
})),null,1));
await p.evaluate(()=>showPg('autour'));
await p.waitForTimeout(1200);
console.log(JSON.stringify(await p.evaluate(()=>{
  const sel=document.getElementById('an-ens'); sel.value='16'; sel.dispatchEvent(new Event('change'));
  return {nb:(document.getElementById('an-nb')||{}).textContent};
}),null,1));
await p.waitForTimeout(500);
console.log(JSON.stringify(await p.evaluate(()=>{
  const it=[...document.querySelectorAll('.an-it')].map(x=>x.querySelector('b').textContent);
  return {n:it.length, libre: it.includes('Libre-échange')};
}),null,1));
await p.evaluate(()=>{
  [...document.querySelectorAll('.an-it')].find(x=>x.querySelector('b').textContent==='Libre-échange').click();
});
await p.waitForTimeout(800);
console.log(JSON.stringify(await p.evaluate(()=>{
  const el=document.getElementById('pg-autour');
  return {titre: (el.querySelector('.an-dt')||{}).textContent,
          sections: el.querySelectorAll('.an-s').length};
}),null,1));
console.log('erreurs',errs.length,errs.slice(0,3));
await b.close();
