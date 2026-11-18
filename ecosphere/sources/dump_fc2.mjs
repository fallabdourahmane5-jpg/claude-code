import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>({
  fc: FC_DATA.map(x=>({ch:x.ch, type:x.type, term:x.term, def:x.def, src:x.source||''})),
  nav: [...document.querySelectorAll('nav .nt')].map(x=>({t:x.textContent.trim(), o:x.getAttribute('onclick')})),
  pages: [...document.querySelectorAll('.pg')].map(x=>x.id)
}));
fs.writeFileSync('fc_data.json', JSON.stringify(o.fc));
fs.writeFileSync('nav_pages.json', JSON.stringify({nav:o.nav, pages:o.pages}));
const parCh = {};
o.fc.forEach(x=>{ parCh[x.ch] = (parCh[x.ch]||0)+1; });
console.log('fiches', o.fc.length);
console.log('par chapitre', JSON.stringify(parCh));
console.log('pages', o.pages.length);
await b.close();
