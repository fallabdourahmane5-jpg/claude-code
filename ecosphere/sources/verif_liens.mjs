import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

// (requête, chapitre attendu) : on tape la requête dans la recherche, on clique
// le premier résultat et on contrôle que l'application ouvre bien le bon
// passage du bon chapitre.
const CAS = [
  ['demande effective', '25'], ['multiplicateur fiscal', '25'],
  ['trappe à liquidité', '25'], ['courbe BP', '25'],
  ['policy mix Clinton-Greenspan', '25'], ['règle de Mundell', '25'],
  ['loi d’Okun', '25'], ['Alvin Hansen', '25'],
  ['condition de Marshall-Lerner', '26'], ['théorème de Schmidt', '26'],
  ['parité des pouvoirs d’achat', '26'], ['peur du flottement', '26'],
  ['doctrine Miran', '26'], ['caisse d’émission', '26'],
  ['Gustav Cassel', '26'], ['taux de marge', '26'],
];

const b = await chromium.launch();
const p = await b.newPage();
const erreurs = [];
p.on('pageerror', e => erreurs.push(String(e).slice(0, 160)));
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(32000);

const out = [];
for (const [q, ch] of CAS) {
  await p.evaluate(() => { if (window.showPg) window.showPg('search'); });
  await p.waitForTimeout(250);
  await p.evaluate(q => {
    const i = document.getElementById('rq-in');
    i.value = q;
    i.dispatchEvent(new Event('input', {bubbles: true}));
  }, q);
  await p.waitForTimeout(900);
  const r = await p.evaluate(() => {
    const z = document.querySelectorAll('#rq-rep .rq-r, #rq-res .rq-r');
    const c = document.querySelector('#rq-rep [data-k], #rq-res [data-k]');
    return {n: z.length, t: z.length ? (z[0].innerText || '').replace(/\s+/g, ' ').slice(0, 110) : '',
      k: c ? c.getAttribute('data-k') : null};
  });
  let clic = {ok: false};
  if (r.k) {
    await p.evaluate(() => {
      const z = document.querySelector('#rq-rep [data-k], #rq-res [data-k]');
      z.scrollIntoView(); z.click();
    });
    await p.waitForTimeout(2200);
    clic = await p.evaluate(() => {
      const vis = [...document.querySelectorAll('.pg')].filter(x => x.offsetParent !== null || x.classList.contains('active'));
      const fl = document.querySelector('.rq-flash');
      const tc = document.getElementById('chTitle') || document.querySelector('#sect-cours h2');
      return {ok: true, pages: vis.map(x => x.id).slice(0, 3),
        flash: fl ? (fl.innerText || '').replace(/\s+/g, ' ').slice(0, 90) : '',
        titre: tc ? (tc.innerText || '').replace(/\s+/g, ' ').slice(0, 70) : '',
        courant: (window.currentChapter !== undefined ? String(window.currentChapter) : '')};
    });
  }
  out.push({q, ch, res: r, clic});
  console.log((clic.flash ? '✓' : '·'), q, '| n=' + r.n, '| k=' + (r.k||'-'), '|', (r.t || '').slice(0, 46),
    '| page=' + (clic.pages || []).join(','), '| ch=' + (clic.courant || '?'),
    '| flash=' + (clic.flash || '').slice(0, 50));
}
fs.writeFileSync('verif_liens.json', JSON.stringify({out, erreurs}, null, 1));
console.log('erreurs JS :', erreurs.length);
await b.close();
