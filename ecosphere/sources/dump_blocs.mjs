import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);
const o = await p.evaluate(()=>{
  // Énumération déterministe des blocs d'un chapitre : même règle au montage
  // et à l'exécution.
  const SEL = 'h2,h3,h4,h5,p,li,.db,table,blockquote';
  const r = {};
  Object.keys(CH_CONTENT).forEach(k=>{
    const d = document.createElement('div');
    d.innerHTML = CH_CONTENT[k].cours || '';
    const out = [];
    let h2='', h3='', h4='';
    d.querySelectorAll(SEL).forEach(el=>{
      // un .db contient des div : on le traite en bloc et on ignore ses enfants
      if (el.closest('.db') && !el.classList.contains('db')) return;
      if (el.tagName === 'TABLE' && el.closest('.db')) return;
      const tag = el.classList.contains('db') ? 'db' : el.tagName.toLowerCase();
      let txt = (el.innerText||'').replace(/\s+/g,' ').trim();
      let dt = '', dd = '';
      if (tag === 'db') {
        dt = (el.querySelector('.dt')||{}).innerText || '';
        dd = (el.querySelector('.dd')||{}).innerText || '';
        dt = dt.replace(/\s+/g,' ').trim(); dd = dd.replace(/\s+/g,' ').trim();
        txt = (dt + ' : ' + dd).trim();
      }
      if (tag === 'h2') { h2 = txt; h3=''; h4=''; }
      else if (tag === 'h3') { h3 = txt; h4=''; }
      else if (tag === 'h4' || tag === 'h5') { h4 = txt; }
      out.push({g: tag, x: txt, dt, dd, p: [h2, h3, h4]});
    });
    r[k] = out;
  });
  return r;
});
fs.writeFileSync('blocs_bruts.json', JSON.stringify(o));
let n=0, c=0, par={};
Object.entries(o).forEach(([k,v])=>{ n+=v.length; v.forEach(x=>{ c+=x.x.length; par[x.g]=(par[x.g]||0)+1; }); });
console.log('chapitres', Object.keys(o).length, 'blocs', n, 'signes', c);
console.log(JSON.stringify(par));
await b.close();
