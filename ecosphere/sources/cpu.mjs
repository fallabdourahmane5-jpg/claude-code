import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';

const f = process.argv[2];
const b = await chromium.launch({ args:['--no-sandbox'] });
const p = await b.newPage();
const cdp = await p.context().newCDPSession(p);
await cdp.send('Profiler.enable');
await cdp.send('Profiler.setSamplingInterval', { interval: 500 });
await cdp.send('Profiler.start');
const t0 = Date.now();
await p.goto('file://' + f, { waitUntil: 'load', timeout: 180000 });
const tLoad = Date.now() - t0;
await p.waitForTimeout(Number(process.env.APRES||0));
const { profile } = await cdp.send('Profiler.stop');

// aggregate self time per (functionName, url, line)
const byId = new Map();
for (const n of profile.nodes) byId.set(n.id, n);
const self = new Map();
const total = profile.samples.length;
const dt = profile.timeDeltas;
for (let i = 0; i < profile.samples.length; i++) {
  const n = byId.get(profile.samples[i]);
  if (!n) continue;
  const cf = n.callFrame;
  const k = (cf.functionName || '(anonymous)') + ' @' + (cf.lineNumber+1);
  self.set(k, (self.get(k) || 0) + (dt[i] || 0));
}
const arr = [...self.entries()].sort((a,b)=>b[1]-a[1]).slice(0, 35);
console.log('load wall:', tLoad, 'ms   samples:', total);
console.log('--- self time (ms) ---');
for (const [k,v] of arr) console.log(String(Math.round(v/1000)).padStart(7), k);

// also total CPU in profile
const sum = dt.reduce((a,b)=>a+b,0);
console.log('profile span ms:', Math.round(sum/1000));
await b.close();
