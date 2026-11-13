import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>{
  const r = {};
  Object.keys(CH_CONTENT).forEach(k=>{ r[k] = CH_CONTENT[k].cours || ''; });
  return r;
});
fs.writeFileSync('cours_html.json', JSON.stringify(o));
const tags = {};
Object.values(o).forEach(h=>{
  for (const m of h.matchAll(/<([a-z0-9]+)(\s[^>]*)?>/g)) tags[m[1]] = (tags[m[1]]||0)+1;
});
console.log('chapitres', Object.keys(o).length, 'octets', Object.values(o).reduce((a,c)=>a+c.length,0));
console.log(JSON.stringify(tags));
await b.close();
