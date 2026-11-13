import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v218.html');
await p.waitForTimeout(34000);
for (const q of (process.argv.slice(2).length ? process.argv.slice(2) :
   ['position extérieure nette','mercantilisme','PEN','solidarité organique','habitus'])) {
  const r = await p.evaluate(q=>window.__ECO_RECHERCHE.debug(q), q);
  console.log('\n======== ' + q + '  (' + r.n + ' résultats, ' + r.groupes + ' groupes)  Q=' + JSON.stringify(r.Q));
  r.liste.forEach((g,i)=>console.log(String(i+1).padStart(2)+'. ['+String(g.prim.y).padEnd(8)+'] sc'+String(g.sc).padStart(5)+
    ' ch'+String(g.prim.c||'-').padEnd(3)+' b'+String(g.prim.b).padEnd(5)+' n'+g.n+' | '+g.prim.t.slice(0,62)+
    '   {'+[...new Set(g.types)].join(',')+'}'));
}
console.log('\nerrs', JSON.stringify(errs.slice(0,3)));
await b.close();
