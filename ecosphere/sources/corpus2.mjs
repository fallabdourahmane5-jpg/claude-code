import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const extra = await p.evaluate(() => {
  const o = {atlas:[], chiffres:[], resumes:[], frise:[]};
  // atlas : payload interne du bloc
  const sc = document.getElementById('eco-atlas-idees');
  return o;
});
// atlas depuis la source
const s = fs.readFileSync(process.argv[2], 'utf8');
function payload(id, marqueur) {
  const i = s.indexOf('id="' + id + '"');
  if (i < 0) return null;
  const j = s.indexOf(marqueur, i);
  if (j < 0) return null;
  const k = s.indexOf('\n', j);
  let raw = s.slice(j + marqueur.length, k).trim();
  if (raw.endsWith(';')) raw = raw.slice(0, -1);
  try { return JSON.parse(raw); } catch(e) { return 'ERR:' + e.message.slice(0,80); }
}
const atlas = payload('eco-atlas-idees', 'var DATA = ');
const out = {atlas: atlas && atlas.chapitres ? atlas.chapitres.map(c=>({k:c.k, lib:c.lib,
   e:c.e.map(x=>({n:x.n, ti:x.ti, no:x.no, ou:x.ou}))})) : null};
fs.writeFileSync('corpus_atlas.json', JSON.stringify(out));
console.log('atlas chapitres', out.atlas ? out.atlas.length : null,
  'idées', out.atlas ? out.atlas.reduce((a,c)=>a+c.e.length,0) : null);
await b.close();
