import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage();
await p.goto('file:///tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/app_v176.html',{waitUntil:'load',timeout:180000});
await p.waitForTimeout(5500);
const r=await p.evaluate(async ()=>{
  window.showPg('fc'); await new Promise(r=>setTimeout(r,900));
  const fc=document.getElementById('pg-fc');
  const chips=[...fc.querySelectorAll('*')].filter(e=>/^(Toutes|Ch\.\d+|⚡ À revoir)$/.test(e.textContent.trim()) && e.children.length===0);
  return {
    nb:chips.length,
    html:chips.slice(0,4).map(c=>c.outerHTML),
    parent:chips[0]?chips[0].parentElement.outerHTML.slice(0,700):null,
    parentId:chips[0]?(chips[0].parentElement.id||chips[0].parentElement.className):null,
    fns:Object.keys(window).filter(k=>/fc|flash|card/i.test(k)).slice(0,25)
  };
});
console.log('puces trouvées :', r.nb);
console.log('conteneur :', r.parentId);
console.log('exemples :'); r.html.forEach(h=>console.log('   '+h));
console.log('\nparent HTML :', r.parent);
console.log('\nfonctions globales liées aux fiches :', r.fns.join(', '));
await b.close();
