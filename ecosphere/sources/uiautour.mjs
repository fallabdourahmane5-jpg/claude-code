import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:Number(process.argv[3]||1400),height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const out={};
out.onglet = await p.evaluate(()=>[...document.querySelectorAll('nav .nt')].map(x=>x.textContent.trim()).slice(-4));
await p.evaluate(()=>showPg('autour'));
await p.waitForTimeout(1200);
out.index = await p.evaluate(()=>{
  const el=document.getElementById('pg-autour');
  return {visible: el.classList.contains('on'), ens: el.querySelectorAll('.an-ens').length,
    nb: (document.getElementById('an-nb')||{}).textContent, len: el.innerText.length};
});
// ouvrir l'ensemble 28 puis un dossier
out.dossier = await p.evaluate(()=>{
  const sel=document.getElementById('an-ens'); sel.value='28'; sel.dispatchEvent(new Event('change'));
  return 'ok';
});
await p.waitForTimeout(700);
out.ens28 = await p.evaluate(()=>{
  const items=[...document.querySelectorAll('.an-it')];
  return {n: items.length, titres: items.slice(0,5).map(x=>x.querySelector('b').textContent)};
});
await p.evaluate(()=>{
  const it=[...document.querySelectorAll('.an-it')].find(x=>/éducateur/.test(x.textContent));
  it.click();
});
await p.waitForTimeout(900);
out.educateur = await p.evaluate(()=>{
  const el=document.getElementById('pg-autour');
  const t=el.innerText;
  return {len:t.length, som:[...el.querySelectorAll('.an-som a')].map(a=>a.textContent),
    mec: el.querySelectorAll('.an-etape').length, args: el.querySelectorAll('.an-blo').length,
    crit: el.querySelectorAll('.an-crit').length, aut: el.querySelectorAll('.an-aut').length,
    faits: el.querySelectorAll('.an-fait').length, diss: el.querySelectorAll('.an-diss').length,
    liens: el.querySelectorAll('.an-lk button').length,
    list: t.includes('List'), krugman: t.includes('Krugman'), hamilton: t.includes('Hamilton')};
});
// comparaison offensif / défensif
await p.evaluate(()=>{ document.querySelector('[data-retour]').click(); });
await p.waitForTimeout(500);
await p.evaluate(()=>{
  const it=[...document.querySelectorAll('.an-it')].find(x=>/Protectionnisme offensif/.test(x.textContent));
  it.click();
});
await p.waitForTimeout(800);
out.offensif = await p.evaluate(()=>{
  const el=document.getElementById('pg-autour');
  return {tab: el.querySelectorAll('.an-tab tbody tr').length,
    cols: [...el.querySelectorAll('.an-tab th')].map(x=>x.textContent),
    brander: el.innerText.includes('Brander')};
});
// recherche
await p.evaluate(()=>{ document.querySelector('[data-retour]').click(); });
await p.waitForTimeout(400);
out.recherche = await p.evaluate(()=>{
  const sel=document.getElementById('an-ens'); sel.value=''; sel.dispatchEvent(new Event('change'));
  const q=document.getElementById('an-q'); q.value='canards boiteux';
  q.dispatchEvent(new Event('input'));
  return {nb:(document.getElementById('an-nb')||{}).textContent,
    items:[...document.querySelectorAll('.an-it b')].map(x=>x.textContent).slice(0,6)};
});
// navigation croisée : cliquer un lien vers un chapitre
await p.evaluate(()=>{
  const q=document.getElementById('an-q'); q.value=''; q.dispatchEvent(new Event('input'));
  const sel=document.getElementById('an-ens'); sel.value='28'; sel.dispatchEvent(new Event('change'));
});
await p.waitForTimeout(500);
await p.evaluate(()=>{
  [...document.querySelectorAll('.an-it')].find(x=>/Droits de douane|droits de douane/.test(x.textContent)).click();
});
await p.waitForTimeout(700);
await p.evaluate(()=>{ document.querySelector('.an-lk button[data-ch]').click(); });
await p.waitForTimeout(1200);
out.navCours = await p.evaluate(()=>{
  const el=document.getElementById('pg-chapter');
  return {actif: el && el.classList.contains('on'), titre: el?el.innerText.slice(0,90):null};
});
console.log(JSON.stringify(out,null,1));
console.log('erreurs', errs.length, errs.slice(0,5));
await b.close();
