import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const out = {};

// maps : liste des chapitres
await p.evaluate(()=>showPg('maps'));
await p.waitForTimeout(1000);
out.mapsChapitres = await p.evaluate(()=>{
  const el = document.getElementById('pg-maps');
  return [...el.querySelectorAll('button, .map-tab, .eco-v83-tab, option')].map(x=>x.textContent.trim()).filter(t=>t&&t.length<40).slice(0,40);
});
await p.evaluate(()=>{ if(typeof renderVisualMap==='function') renderVisualMap(24); });
await p.waitForTimeout(1200);
out.map24 = await p.evaluate(()=>{
  const el = document.getElementById('pg-maps');
  const t = el.innerText;
  return {len:t.length, titre:t.slice(0,400),
   omc:t.includes('OMC'), cairns:t.includes('Cairns'), seattle:t.includes('Seattle'),
   gatt:t.includes('GATT'), multifibres:t.includes('multifibres')};
});

// auteurs : filtres de chapitre
await p.evaluate(()=>showPg('authors'));
await p.waitForTimeout(900);
out.auteursFiltres = await p.evaluate(()=>{
  const el = document.getElementById('pg-authors');
  return [...el.querySelectorAll('button, option, .chip')].map(x=>x.textContent.trim()).filter(t=>/chapitre|année/i.test(t)).slice(0,30);
});

// résumé 24
out.res24 = await p.evaluate(()=>{
  if(typeof ouvrirResume==='function'){ ouvrirResume('24'); return 'ok'; } return 'absent';
});
await p.waitForTimeout(1200);
out.res24txt = await p.evaluate(()=>{
  const el=document.getElementById('pg-resumes'); const t=el.innerText;
  return {len:t.length, debut:t.slice(0,500),
    parties:(t.match(/\n[IVX]+\./g)||[]).length,
    cairns:t.includes('Cairns'), seattle:t.includes('Seattle'), arachide:t.includes('arachide'),
    multifibres:t.includes('multifibres'), orourke:t.includes('O’Rourke'), gatt:t.includes('GATT')};
});

// chiffres 24
out.chif24 = await p.evaluate(()=>{ ouvrirChiffres('24'); return 'ok'; });
await p.waitForTimeout(1200);
out.chif24txt = await p.evaluate(()=>{
  const el=document.getElementById('pg-chiffres'); const t=el.innerText;
  return {len:t.length, extrait:t.slice(0,1600)};
});

// recherche ciblée
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(500);
for (const q of ['Cairns','multifibres','Kindleberger','détournement de trafic','bol de spaghettis']) {
  const r = await p.evaluate((q)=>{ const i=document.getElementById('si'); i.value=q; doSearch();
    const box=document.getElementById('search-res');
    return [...box.querySelectorAll('.sr-item, .search-item, .res-item, li, .sr')].map(x=>x.innerText.split('\n')[0].slice(0,70)).slice(0,5);
  }, q);
  out['rech_'+q] = r;
  await p.waitForTimeout(250);
}

// frise : items ch24
await p.evaluate(()=>showPg('frise'));
await p.waitForTimeout(1200);
out.frise24 = await p.evaluate(()=>{
  const el=document.getElementById('pg-frise');
  const sel=el.querySelector('select');
  sel.value='24'; sel.dispatchEvent(new Event('change'));
  return 'ok';
});
await p.waitForTimeout(1000);
out.frise24txt = await p.evaluate(()=>{
  const el=document.getElementById('pg-frise'); const t=el.innerText;
  return {len:t.length, extrait:t.slice(0,900),
    items: el.querySelectorAll('.fr-it, .frise-item, .fr-card').length};
});
console.log(JSON.stringify(out,null,1));
console.log('erreurs:',errs.length, errs.slice(0,5));
await b.close();
