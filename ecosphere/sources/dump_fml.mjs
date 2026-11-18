import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>{
  // même énumération que dump_blocs.mjs, mais on note en plus la position des
  // div.formula par rapport au dernier bloc retenu
  const SEL = 'h2,h3,h4,h5,p,li,.db,table,blockquote';
  const TOUT = SEL + ',.formula';
  const r = {};
  ['25','26'].forEach(k=>{
    const d = document.createElement('div');
    d.innerHTML = (CH_CONTENT[k]||{}).cours || '';
    const out = [];
    let n = -1, h3 = '', h4 = '', dernier = '';
    d.querySelectorAll(TOUT).forEach(el=>{
      if (el.closest('.db') && !el.classList.contains('db')) return;
      if (el.tagName === 'TABLE' && el.closest('.db')) return;
      const txt = (el.innerText||'').replace(/\s+/g,' ').trim();
      if (el.classList.contains('formula')) {
        out.push({b: n, h3, h4, av: dernier, f: txt});
        return;
      }
      n += 1;
      const tag = el.classList.contains('db') ? 'db' : el.tagName.toLowerCase();
      if (tag === 'h3') { h3 = txt; h4 = ''; }
      else if (tag === 'h4' || tag === 'h5') { h4 = txt; }
      dernier = txt;
    });
    r[k] = out;
  });
  return r;
});
fs.writeFileSync('fml2526.json', JSON.stringify(o));
console.log('ch25', o['25'].length, 'ch26', o['26'].length);
await b.close();
