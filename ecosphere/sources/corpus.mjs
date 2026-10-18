import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(14000);
const data = await p.evaluate(() => {
  const o = {chapitres:{}, auteurs:[], fiches:[], sujets:[], atlas:[]};
  Object.keys(CH_CONTENT).forEach(k => {
    const v = CH_CONTENT[k];
    const d = document.createElement('div'); d.innerHTML = v.cours || '';
    o.chapitres[k] = {title:v.title, sub:v.sub, texte:d.innerText,
      notions:(v.notions||[]).map(n=>({t:n.term, d:n.def}))};
  });
  o.auteurs = AUTHORS.map(a=>({name:a.name, ch:a.chapters||a.ch, idea:a.idea, detail:a.detail,
     oeuvres:a.oeuvres, courant:a.courant, phrase:a.phrase, dates:a.dates}));
  o.sujets = SUBJECTS_BANK_PREMIUM.map(s=>({id:s.id, ch:s.chapter, title:s.title}));
  return o;
});
fs.writeFileSync('corpus.json', JSON.stringify(data));
console.log('chapitres', Object.keys(data.chapitres).length,
  'signes', Object.values(data.chapitres).reduce((a,c)=>a+c.texte.length,0),
  'auteurs', data.auteurs.length, 'sujets', data.sujets.length);
await b.close();
