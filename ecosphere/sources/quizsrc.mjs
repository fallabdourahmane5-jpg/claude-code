import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v179.html'); await p.waitForTimeout(4000);
await p.evaluate(()=>window.showPg('quiz')); await p.waitForTimeout(1000);
const r = await p.evaluate(()=>{
  const pg=document.getElementById('pg-quiz');
  // structure DOM de la zone chapitres
  const el=[...pg.querySelectorAll('*')].find(e=>/Plusieurs choix possibles/.test(e.textContent)&&e.children.length<12);
  const host = el? el.parentElement : null;
  const chips = host? [...host.querySelectorAll('[data-ch],[data-chapter],.chip,.chap-chip,label')].slice(0,20).map(e=>({tag:e.tagName, cls:e.className, dch:e.getAttribute('data-ch'), dchapter:e.getAttribute('data-chapter'), txt:(e.textContent||'').trim().slice(0,45)})) : [];
  // fonctions candidates
  const fns=Object.keys(window).filter(k=>typeof window[k]==='function'&&/quiz|chap/i.test(k));
  return {hostHTML: host? host.innerHTML.slice(0,1400):'—', chips, fns};
});
console.log('--- CHIPS ---'); console.log(JSON.stringify(r.chips,null,1));
console.log('--- FNS ---'); console.log(JSON.stringify(r.fns));
console.log('--- HTML ---'); console.log(r.hostHTML);
await b.close();
