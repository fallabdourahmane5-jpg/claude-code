import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage();
const err=[]; p.on('pageerror',e=>err.push(String(e).slice(0,160)));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);

const R = await p.evaluate(()=>{
  const G = n => { try { return (new Function('try{return '+n+'}catch(e){return undefined}'))(); } catch(e){ return undefined; } };
  const out = {};
  // Atlas : plus aucun renvoi non cliquable, Mundell conservé
  const at = document.getElementById('eco-atlas-idees');
  const m = at.textContent.match(/var DATA = (\{.*?\});\n/s);
  const A = JSON.parse(m[1]);
  const noms = new Set();
  A.chapitres.forEach(c=>c.e.forEach(e=>noms.add(e.n)));
  const manq = [];
  A.chapitres.forEach(c=>c.e.forEach(e=>(e.li||[]).forEach(l=>{ if(!noms.has(l.a)) manq.push(c.k+' → '+l.a); })));
  out.atlas = {idees: A.chapitres.reduce((s,c)=>s+c.e.length,0), manquants: manq,
    mundell2: A.chapitres.find(c=>c.k===2).e.filter(e=>e.n==='Robert Mundell').map(e=>({ti:e.ti, ou:e.ou, no:e.no})),
    galluzzo: [...noms].filter(n=>n.indexOf('Galluzzo')>=0),
    orain: [...noms].filter(n=>n.indexOf('Orain')>=0)};
  // base d'auteurs
  const AU = G('AUTHORS')||[];
  out.auteurs = {galluzzo: AU.filter(a=>String(a.name).indexOf('Galluzzo')>=0).map(a=>a.name),
    orain: AU.filter(a=>String(a.name).indexOf('Orain')>=0).map(a=>a.name), total: AU.length};
  // graphie Généreux
  const CH = G('CH_CONTENT')||{};
  const t25 = (CH['25']||{}).cours||'';
  out.genereux = {jean: (t25.match(/Jean Généreux/g)||[]).length,
    jacques: (t25.match(/Jacques Généreux/g)||[]).length};
  return out;
});

// recherche : les trois noms doivent répondre
const RQ = {};
for (const q of ['Anthony Galluzzo', 'Arnaud Orain', 'Jacques Généreux', 'zone monétaire optimale', 'triangle de Mundell']) {
  await p.evaluate(()=>window.showPg('search'));
  await p.waitForTimeout(200);
  await p.evaluate(q=>{ const i=document.getElementById('rq-in'); i.value=q; i.dispatchEvent(new Event('input',{bubbles:true})); }, q);
  await p.waitForTimeout(900);
  RQ[q] = await p.evaluate(()=>{
    const z=document.querySelectorAll('#rq-rep .rq-r, #rq-res .rq-r');
    return {n:z.length, t: z.length?(z[0].innerText||'').replace(/\s+/g,' ').slice(0,100):''};
  });
}
R.recherche = RQ; R.erreurs = err;
fs.writeFileSync('verif_v222.json', JSON.stringify(R,null,1));
console.log(JSON.stringify(R,null,1));
await b.close();
