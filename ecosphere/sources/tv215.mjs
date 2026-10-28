import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';

const F = 'file://' + process.argv[2];
const W = parseInt(process.argv[3] || '1440', 10);
const H = parseInt(process.argv[4] || '900', 10);

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: W, height: H },
  deviceScaleFactor: 2, isMobile: W < 700, hasTouch: W < 700 });
const errs = [];
p.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
p.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE ' + m.text()); });
await p.goto(F, { waitUntil: 'load' });
await p.waitForTimeout(900);

const dump = async (tag) => {
  const s = await p.evaluate(() => {
    const g = i => document.getElementById(i);
    return {
      idx: g('vzIndex') ? getComputedStyle(g('vzIndex')).display : 'ABSENT',
      stage: g('vzStage') ? getComputedStyle(g('vzStage')).display : 'ABSENT',
      cards: document.querySelectorAll('#vzGrid .vz-card').length,
      nodes: document.querySelectorAll('#vzWorld .vz-node').length,
      labs: document.querySelectorAll('#vzWorld .vz-lab').length,
      paths: document.querySelectorAll('#vzEdges path').length,
      stats: (g('vzStats') || {}).textContent,
      tf: g('vzWorld') ? g('vzWorld').style.transform : '',
      z: (g('vzZ') || {}).textContent,
      panel: g('vzPanel') ? g('vzPanel').className : 'ABSENT',
      full: g('vzFull') ? g('vzFull').className : 'ABSENT',
    };
  });
  console.log(tag, JSON.stringify(s));
  return s;
};

await p.evaluate(() => showPg('visualisations'));
await p.waitForTimeout(600);
await dump('INDEX');
await p.screenshot({ path: `v215_${W}_index.png`, fullPage: false });

await p.click('#vzGrid .vz-card');
await p.waitForTimeout(800);
await dump('SCENE');
await p.screenshot({ path: `v215_${W}_scene.png` });

const ov = await p.evaluate(() => {
  const ns = [...document.querySelectorAll('#vzWorld .vz-node')];
  const r = ns.map(n => ({ id: n.getAttribute('data-e') || n.getAttribute('data-v') || '?',
    x: parseFloat(n.style.left), y: parseFloat(n.style.top),
    w: n.offsetWidth, h: n.offsetHeight }));
  const bad = [];
  for (let i = 0; i < r.length; i++) for (let j = i + 1; j < r.length; j++) {
    const a = r[i], c = r[j];
    const ox = Math.min(a.x + a.w, c.x + c.w) - Math.max(a.x, c.x);
    const oy = Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y);
    if (ox > -6 && oy > -6) bad.push(a.id + '/' + c.id + ' ' + ox.toFixed(0) + 'x' + oy.toFixed(0));
  }
  const mw = Math.max(...r.map(x => x.x + x.w)), mh = Math.max(...r.map(x => x.y + x.h));
  return { n: r.length, monde: [Math.round(mw), Math.round(mh)], bad };
});
console.log('OVERLAP', JSON.stringify(ov));
const ol = await p.evaluate(() => {
  const w = document.getElementById('vzWorld'); const av = w.classList.contains('loin');
  const etroit = document.getElementById('vzView').clientWidth < 700;
  if (!etroit) w.classList.add('loin');
  const nb = [...document.querySelectorAll('#vzWorld .vz-node')].map(n => ({
    t: (n.querySelector('.vzt')||{}).textContent, x: parseFloat(n.style.left), y: parseFloat(n.style.top),
    w: n.offsetWidth, h: n.offsetHeight }));
  const lb = [...document.querySelectorAll('#vzWorld .vz-lab')].map(l => ({
    t: l.textContent, x: parseFloat(l.style.left) - l.offsetWidth/2, y: parseFloat(l.style.top) - l.offsetHeight/2,
    w: l.offsetWidth, h: l.offsetHeight }));
  if (!av && !etroit) w.classList.remove('loin');
  const inter = (a,b) => Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x) > 0 && Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y) > 0;
  const bad = [];
  lb.forEach(l => nb.forEach(n => { if (inter(l,n)) bad.push(l.t.slice(0,22) + ' // ' + (n.t||'').slice(0,22)); }));
  for (let i=0;i<lb.length;i++) for (let j=i+1;j<lb.length;j++) if (inter(lb[i],lb[j])) bad.push('LL ' + lb[i].t.slice(0,18) + ' // ' + lb[j].t.slice(0,18));
  const deb = nb.filter(n => n.h < 40).map(n => n.t);
  return { nlab: lb.length, bad, trop_court: deb };
});
console.log('LABOVER', JSON.stringify(ol));
console.log('VUE', JSON.stringify(await p.evaluate(() => {
  const v = document.getElementById('vzView');
  return { w: v.clientWidth, h: v.clientHeight, vh: window.innerHeight };
})));
await p.click('#vzPleinT'); await p.waitForTimeout(600);
console.log('PLEIN', JSON.stringify(await p.evaluate(() => {
  const v = document.getElementById('vzView');
  return { w: v.clientWidth, h: v.clientHeight, z: (document.getElementById('vzZ')||{}).textContent };
})));
await p.screenshot({ path: `v215_${W}_plein.png` });
await p.keyboard.press('Escape'); await p.waitForTimeout(500);
console.log('PLEINOFF', JSON.stringify(await p.evaluate(() =>
  document.getElementById('pg-visualisations').className)));

const box = await p.locator('#vzView').boundingBox();
await p.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
await p.mouse.wheel(0, -600); await p.waitForTimeout(300);
console.log('WHEEL+', await p.evaluate(() => [document.getElementById('vzWorld').style.transform,
  (document.getElementById('vzZ') || {}).textContent]));
await p.screenshot({ path: `v215_${W}_zoom.png` });
await p.mouse.wheel(0, 1400); await p.waitForTimeout(300);
console.log('WHEEL-', await p.evaluate(() => (document.getElementById('vzZ') || {}).textContent));

// boutons zoom
const nz = await p.evaluate(() => document.querySelectorAll('[data-z]').length);
if (nz) { await p.click('[data-z="1"]'); await p.waitForTimeout(250);
  console.log('BTN+', await p.evaluate(() => (document.getElementById('vzZ') || {}).textContent)); }
await p.click('[data-fit="1"]'); await p.waitForTimeout(400);
console.log('FIT', await p.evaluate(() => [document.getElementById('vzWorld').style.transform,
  (document.getElementById('vzZ') || {}).textContent]));

// glisser
const t0 = await p.evaluate(() => document.getElementById('vzWorld').style.transform);
await p.mouse.move(box.x + 180, box.y + 180);
await p.mouse.down(); await p.mouse.move(box.x + 430, box.y + 330, { steps: 10 }); await p.mouse.up();
await p.waitForTimeout(250);
const t1 = await p.evaluate(() => document.getElementById('vzWorld').style.transform);
console.log('PAN', t0 !== t1 ? 'ok' : 'IMMOBILE', t1);
await p.click('[data-fit="1"]'); await p.waitForTimeout(400);

// ouvrir un nœud
await p.click('#vzWorld .vz-node');
await p.waitForTimeout(700);
await dump('PANEL');
const pv = await p.evaluate(() => {
  const e = document.getElementById('vzPanel');
  if (!e) return null;
  return { h2: (e.querySelector('h2') || {}).textContent,
    secs: [...e.querySelectorAll('.vp-sec h4')].map(x => x.textContent.trim()),
    liens: e.querySelectorAll('[data-ch],[data-fc],[data-su],[data-at],[data-aut],[data-dos]').length,
    len: e.textContent.length, x: getComputedStyle(e).transform, op: getComputedStyle(e).opacity,
    w: e.getBoundingClientRect().width, r: e.getBoundingClientRect().right };
});
console.log('PANELCONT', JSON.stringify(pv));
await p.screenshot({ path: `v215_${W}_panel.png` });

// plein écran
if (await p.evaluate(() => !!document.querySelector('[data-plein]'))) {
  await p.click('[data-plein]'); await p.waitForTimeout(700);
  const fv = await p.evaluate(() => {
    const e = document.getElementById('vzFull');
    return { cls: e.className, op: getComputedStyle(e).opacity, len: e.textContent.length };
  });
  console.log('FULL', JSON.stringify(fv));
  await p.screenshot({ path: `v215_${W}_full.png` });
  await p.keyboard.press('Escape'); await p.waitForTimeout(400);
  console.log('FULLCLOSE', await p.evaluate(() => document.getElementById('vzFull').className));
}
await p.keyboard.press('Escape'); await p.waitForTimeout(400);
console.log('PANELCLOSE', await p.evaluate(() => document.getElementById('vzPanel').className));

// étiquette de lien
if (await p.evaluate(() => document.querySelectorAll('#vzWorld .vz-lab').length)) {
  await p.click('#vzWorld .vz-lab'); await p.waitForTimeout(700);
  const lv = await p.evaluate(() => {
    const e = document.getElementById('vzPanel');
    return { cls: e.className, kind: (e.querySelector('.vp-kind') || {}).textContent,
      h2: (e.querySelector('h2') || {}).textContent, len: e.textContent.length };
  });
  console.log('LIEN', JSON.stringify(lv));
  await p.screenshot({ path: `v215_${W}_lien.png` });
  await p.keyboard.press('Escape'); await p.waitForTimeout(300);
}

// retour
await p.click('#vzRetour'); await p.waitForTimeout(700);
await dump('RETOUR');

// navigation vers un chapitre
await p.click('#vzGrid .vz-card'); await p.waitForTimeout(700);
await p.click('#vzWorld .vz-node'); await p.waitForTimeout(600);
const nav = await p.evaluate(() => {
  const a = document.querySelector('#vzPanel [data-ch]');
  return a ? { txt: a.textContent.trim(), k: a.getAttribute('data-ch') } : null;
});
console.log('NAVBTN', JSON.stringify(nav));
if (nav) {
  await p.click('#vzPanel [data-ch]'); await p.waitForTimeout(1100);
  console.log('APRESNAV', JSON.stringify(await p.evaluate(() =>
    [...document.querySelectorAll('.pg.on')].map(x => x.id))));
  await p.screenshot({ path: `v215_${W}_nav.png` });
}

// dossier Autour d'une notion
await p.evaluate(() => showPg('visualisations'));
await p.waitForTimeout(700);
if (await p.evaluate(() => getComputedStyle(document.getElementById('vzIndex')).display === 'none')) {
  await p.click('#vzRetour'); await p.waitForTimeout(600);
}
await p.click('#vzGrid .vz-card'); await p.waitForTimeout(700);
const dosn = await p.evaluate(() => {
  const ns = [...document.querySelectorAll('#vzWorld .vz-node')];
  for (const n of ns) { n.click(); const a = document.querySelector('#vzPanel [data-dos]');
    if (a) return { t: a.textContent.trim(), cle: a.getAttribute('data-dos') }; }
  return null;
});
console.log('DOSBTN', JSON.stringify(dosn));
if (dosn) {
  await p.click('#vzPanel [data-dos]'); await p.waitForTimeout(1600);
  console.log('APRESDOS', JSON.stringify(await p.evaluate(() => ({
    pg: [...document.querySelectorAll('.pg.on')].map(x => x.id),
    h: (document.querySelector('.an-dt') || document.querySelector('#pg-autour h1') || {}).textContent }))));
  await p.screenshot({ path: `v215_${W}_dos.png` });
}

console.log('ERREURS', errs.length ? JSON.stringify(errs.slice(0, 8)) : 'aucune');
await b.close();
