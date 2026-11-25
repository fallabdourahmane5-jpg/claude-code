/* Chaque définition des chapitres 25 et 26 ressort-elle sous le filtre
   « Définitions » quand on cherche son intitulé, et renvoie-t-elle au bon
   chapitre ? On pilote la recherche par l'interface, comme un utilisateur. */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const FICHIER = 'file://' + path.resolve(process.argv[2] || 'app_v224.html');
const LISTE = JSON.parse(fs.readFileSync(process.argv[3] || 'defs2526.json', 'utf8'));

(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({ viewport: { width: 1400, height: 1000 } })).newPage();
  const err = [];
  p.on('pageerror', e => err.push(String(e)));
  await p.goto(FICHIER, { waitUntil: 'domcontentloaded', timeout: 180000 });
  await p.waitForFunction(() => !!window.__ECO_RECHERCHE, { timeout: 180000 });
  await p.evaluate(() => window.showPg('search'));
  await p.waitForSelector('#rq-in', { timeout: 30000 });

  /* on amorce une recherche puis on clique sur le filtre « Définitions » :
     il reste ensuite actif d'une recherche à l'autre */
  await p.evaluate(() => window.__ECO_RECHERCHE.lancer('monnaie'));
  await p.waitForTimeout(250);
  await p.locator('#rq-outils [data-f="definitions"]').click();
  await p.waitForTimeout(250);

  let ok = 0;
  const echecs = [];
  for (const d of LISTE) {
    const r = await p.evaluate(async ([terme, chapitre]) => {
      const inp = document.getElementById('rq-in');
      inp.value = terme;
      window.__ECO_RECHERCHE.lancer(terme);
      await new Promise(r2 => setTimeout(r2, 60));
      const rep = document.querySelector('#rq-rep .rq-rep-t');
      const meta = document.querySelector('#rq-rep .rq-rep-m');
      const type = document.querySelector('#rq-rep .rq-ty');
      const corps = document.querySelector('#rq-rep .rq-rep-d');
      const ouvre = [...document.querySelectorAll('#rq-rep .rq-go, #rq-rep .rq-p, ' +
        '#rq-rep [data-k]')].map(b => b.getAttribute('data-k'));
      const filtre = (document.querySelector('#rq-outils .rq-f.on') || {}).textContent || '';
      return {
        titre: rep ? rep.textContent.trim() : null,
        type: type ? type.textContent.trim() : null,
        meta: meta ? meta.textContent.trim() : '',
        texte: corps ? corps.textContent.trim().length : 0,
        cles: ouvre.filter(Boolean),
        filtre: filtre.replace(/\d+$/, '').trim()
      };
    }, [d.t, d.ch]);

    const bonTitre = r.titre &&
      r.titre.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '') ===
      d.t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    const bonType = /d\u00e9finition/i.test(r.type || '');
    const chapitres = r.cles.map(k => { try { return JSON.parse(k)[1]; } catch (e) { return ''; } });
    const bonChap = chapitres.indexOf(d.ch) >= 0;
    if (bonTitre && bonType && bonChap && r.texte > 80) ok++;
    else echecs.push({ t: d.t, ch: d.ch, trouve: r.titre, type: r.type,
                       chapitres: chapitres.join(','), signes: r.texte,
                       filtre: r.filtre });
  }

  console.log(ok + ' / ' + LISTE.length + ' définitions trouvées sous le filtre « Définitions », au bon chapitre');
  echecs.slice(0, 25).forEach(e => console.log('  ÉCHEC ' + e.t + ' (ch' + e.ch + ')' +
    ' → titre=' + e.trouve + ' type=' + e.type + ' chapitres=' + e.chapitres +
    ' signes=' + e.signes + ' filtre=' + e.filtre));
  console.log(err.length ? 'erreurs JS : ' + err.slice(0, 3).join(' | ') : 'aucune erreur JS');
  await nav.close();
  process.exit(echecs.length ? 1 : 0);
})();
