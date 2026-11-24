/* Rendu de la section Quiz sur téléphone, tablette et ordinateur :
   pas de débordement horizontal, cibles tactiles suffisantes, et une
   question entière lisible. */
const { chromium, devices } = require('playwright');
const path = require('path');
const FICHIER = 'file://' + path.resolve(process.argv[2] || 'app_v223.html');
const ECRANS = [
  ['telephone', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2,
                  isMobile: true, hasTouch: true }],
  ['tablette', { viewport: { width: 834, height: 1194 }, deviceScaleFactor: 2,
                 isMobile: true, hasTouch: true }],
  ['ordinateur', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 }]
];
let ko = 0;
function dire(ok, t, d) { if (!ok) ko++; console.log((ok ? 'OK    ' : 'ÉCHEC ') + t + (d ? ' — ' + d : '')); }

(async () => {
  const nav = await chromium.launch();
  for (const [nom, opt] of ECRANS) {
    const ctx = await nav.newContext(opt);
    const p = await ctx.newPage();
    const err = [];
    p.on('pageerror', e => err.push(String(e)));
    p.on('dialog', d => d.accept().catch(() => {}));
    await p.goto(FICHIER, { waitUntil: 'domcontentloaded', timeout: 180000 });
    await p.waitForFunction(() => !!window.__ECO_QUIZ, { timeout: 180000 });
    await p.evaluate(() => window.showPg('quiz'));
    await p.waitForSelector('#qz-start', { timeout: 30000 });

    const deb = await p.evaluate(() => {
      const z = document.getElementById('pg-quiz');
      return { page: document.documentElement.scrollWidth - window.innerWidth,
               bloc: z.scrollWidth - z.clientWidth };
    });
    dire(deb.page <= 1 && deb.bloc <= 1, nom + ' · écran de réglage sans débordement',
         'page +' + deb.page + 'px, bloc +' + deb.bloc + 'px');
    const petits = await p.evaluate(() => [...document.querySelectorAll(
      '#pg-quiz .qz-chip, #pg-quiz .qz-btn, #pg-quiz .qz-mode')]
      .filter(e => e.offsetParent !== null)
      .filter(e => e.getBoundingClientRect().height < 30).length);
    dire(petits === 0, nom + ' · cibles tactiles d’au moins 30 px',
         petits + ' trop petite(s)');
    await p.screenshot({ path: 'ecran_quiz_' + nom + '_reglages.png' });

    await p.locator('#qz-ch [data-ch="23"]').click();
    await p.waitForTimeout(200);
    await p.locator('#qz-start').click();
    await p.waitForSelector('#qz-val', { timeout: 30000 });
    const deb2 = await p.evaluate(() => {
      const z = document.getElementById('pg-quiz');
      return { page: document.documentElement.scrollWidth - window.innerWidth,
               bloc: z.scrollWidth - z.clientWidth,
               enonce: (document.querySelector('#pg-quiz .qz-q') || {}).clientWidth || 0 };
    });
    dire(deb2.page <= 1 && deb2.bloc <= 1, nom + ' · question sans débordement',
         'page +' + deb2.page + 'px, bloc +' + deb2.bloc + 'px');
    await p.screenshot({ path: 'ecran_quiz_' + nom + '_question.png' });

    /* on va jusqu'à une correction pour vérifier sa mise en page */
    if (await p.locator('#qz-opts [data-i]').count())
      await p.locator('#qz-opts [data-i]').first().click();
    await p.locator('#qz-val').click();
    await p.waitForTimeout(400);
    const deb3 = await p.evaluate(() => {
      const z = document.getElementById('pg-quiz');
      const c = document.getElementById('qz-corr');
      return { page: document.documentElement.scrollWidth - window.innerWidth,
               bloc: z.scrollWidth - z.clientWidth,
               corr: c ? c.innerText.trim().length : 0 };
    });
    dire(deb3.page <= 1 && deb3.bloc <= 1 && deb3.corr > 80,
         nom + ' · correction lisible sans débordement',
         'page +' + deb3.page + 'px, bloc +' + deb3.bloc + 'px, ' + deb3.corr + ' signes');
    await p.screenshot({ path: 'ecran_quiz_' + nom + '_correction.png' });
    dire(err.length === 0, nom + ' · aucune erreur JavaScript', err.slice(0, 2).join(' | '));
    await ctx.close();
  }
  await nav.close();
  console.log('\n' + (ko ? ko + ' test(s) en échec' : 'tous les tests passent'));
  process.exit(ko ? 1 : 0);
})();
