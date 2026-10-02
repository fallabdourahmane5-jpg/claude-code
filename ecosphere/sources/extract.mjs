import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const dir = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const b = await chromium.launch({ args: ['--no-sandbox'] });
const p = await b.newPage();
await p.goto('file://' + dir + 'base.html', { waitUntil: 'load', timeout: 180000 });
await p.waitForTimeout(9000);

const out = await p.evaluate(() => {
  const g = n => { try { return eval(n); } catch (e) { return null; } };
  const CH = g('CH_CONTENT') || {};
  const chaps = {};
  const strip = h => String(h || '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&#39;|&apos;/g, "'").replace(/&quot;/g, '"').replace(/\s+/g, ' ').trim();
  Object.keys(CH).forEach(k => {
    const v = CH[k] || {};
    const cours = String(v.cours || '');
    const ab = [...cours.matchAll(/<div class="ab">\s*<div class="an">([\s\S]*?)<\/div>\s*<div class="ai">([\s\S]*?)<\/div>/gi)]
      .map(m => [strip(m[1]), strip(m[2])]);
    // titres de sections pour situer les idees
    const h = [...cours.matchAll(/<h([234])>([\s\S]*?)<\/h\1>/gi)].map(m => [m[1], strip(m[2])]);
    chaps[k] = {
      title: v.title, sub: v.sub, annee: v.annee || 1, numAnnee: v.numAnnee || null,
      taille: cours.length, nbAb: ab.length, ab, plan: h,
      notions: (v.notions || []).map(n => [n.term, n.def, n.type]),
    };
  });
  return {
    chapitres: chaps,
    AUTHORS: (g('AUTHORS') || []).map(a => ({
      name: a.name, dates: a.dates, courant: a.courant, idea: a.idea,
      oeuvres: a.oeuvres, detail: a.detail, ch: a.ch, chapters: a.chapters, phrase: a.phrase,
    })),
  };
});
fs.writeFileSync(dir + 'data.json', JSON.stringify(out, null, 1));
console.log('chapitres:', Object.keys(out.chapitres).join(','));
console.log('auteurs:', out.AUTHORS.length);
for (const k of Object.keys(out.chapitres)) {
  const c = out.chapitres[k];
  console.log('  ch' + k, '| cours', Math.round(c.taille / 1024) + 'Ko', '| blocs auteur-idée', c.nbAb, '| notions', c.notions.length, '|', String(c.title).slice(0, 60));
}
await b.close();
