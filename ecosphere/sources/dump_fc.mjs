import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>({
  fc: FC_DATA.map(x=>({ch:x.ch, type:x.type, term:x.term, def:x.def, src:x.source||''})),
  nav: [...document.querySelectorAll('nav .nt')].map(x=>({t:x.textContent.trim(), o:x.getAttribute('onclick')})),
  pages: [...document.querySelectorAll('.pg')].map(x=>x.id),
  anciens: (()=>{ const par={}; SEARCH_INDEX.forEach(x=>{const k=x.type+' / '+(x.source||'?'); par[k]=(par[k]||0)+1;}); return par; })(),
  termes: [...new Set(SEARCH_INDEX.map(x=>x.term))].length
}));
fs.writeFileSync('fc_data.json', JSON.stringify(o.fc));
fs.writeFileSync('nav_pages.json', JSON.stringify({nav:o.nav, pages:o.pages}));
console.log('fiches', o.fc.length, 'termes distincts dans l ancien index', o.termes);
console.log(JSON.stringify(o.anciens, null, 1));
console.log(JSON.stringify(o.nav.map(x=>x.t)));
await b.close();
