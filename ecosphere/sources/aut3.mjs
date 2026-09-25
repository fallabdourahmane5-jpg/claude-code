import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4200);
const r = await p.evaluate(()=>{
  const SI=eval('SEARCH_INDEX')||[];
  const o={};
  [9,10,21].forEach(n=>{ o[n]=SI.filter(e=>e.type==='auteur'&&String(e.ch)===String(n)).map(e=>e.term); });
  // notion-révision : source pour ch1-6
  o.notionRev = SI.filter(e=>e.type==='notion-révision').slice(0,1);
  // nombre d'entrees par source pour 9/10/21
  const src={};
  SI.filter(e=>[9,10,21].includes(Number(e.ch))).forEach(e=>{ const k=String(e.ch)+'/'+String(e.source); src[k]=(src[k]||0)+1; });
  o.sources=src;
  return o;
});
[9,10,21].forEach(n=>console.log('\n=== auteur, ch'+n+' ('+r[n].length+') ===\n  '+r[n].join('\n  ')));
console.log('\n=== sources ch9/10/21 ===', JSON.stringify(r.sources,null,1));
await b.close();
