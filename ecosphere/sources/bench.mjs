import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch({ args: ['--no-sandbox'] });
const dir = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';

async function mesure(f) {
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  const t0 = Date.now();
  await p.goto('file://' + dir + f, { waitUntil: 'load', timeout: 180000 });
  const load = Date.now() - t0;
  // premier instant où le thread principal répond sous 100 ms
  let pret = null;
  for (let k = 0; k < 120; k++) {
    const t1 = Date.now();
    let ok = false;
    try { ok = await p.evaluate(() => typeof showPg === 'function' && !!document.getElementById('pg-home')); } catch (e) {}
    const rtt = Date.now() - t1;
    if (ok && rtt < 100) { pret = Date.now() - t0; break; }
    await p.waitForTimeout(100);
  }
  const perf = await p.evaluate(() => {
    const n = performance.getEntriesByType('navigation')[0] || {};
    const fp = performance.getEntriesByType('paint').find(x => x.name === 'first-contentful-paint');
    return {
      interactive: Math.round(n.domInteractive || 0),
      complete: Math.round(n.domComplete || 0),
      fcp: fp ? Math.round(fp.startTime) : null,
    };
  });
  await p.close();
  return { load, pret, ...perf };
}

const fichiers = process.argv.slice(2);
const N = 3;
for (const f of fichiers) {
  const rs = [];
  for (let i = 0; i < N; i++) rs.push(await mesure(f));
  const med = k => rs.map(r => r[k]).sort((a, c) => a - c)[Math.floor(N / 2)];
  console.log(
    f.padEnd(16) +
    ' FCP ' + String(med('fcp')).padStart(6) +
    ' · domInteractive ' + String(med('interactive')).padStart(6) +
    ' · domComplete ' + String(med('complete')).padStart(6) +
    ' · load ' + String(med('load')).padStart(6) +
    ' · interface prête ' + String(med('pret')).padStart(6) + ' ms'
  );
}
await b.close();
