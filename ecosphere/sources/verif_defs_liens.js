/* Contrôles complémentaires sur la rubrique « Définitions » des chapitres
   25 et 26 : le bouton d'ouverture conduit-il au bon passage, les faux
   termes ont-ils disparu, les renvois ajoutés fonctionnent-ils ? */
const { chromium } = require('playwright');
const path = require('path');

const FICHIER = 'file://' + path.resolve(process.argv[2] || 'app_v224.html');
const ECHANTILLON = [
  ['Loi des débouchés', '25'], ['Circuit économique', '25'],
  ['Diagramme à 45°', '25'], ['Surchauffe', '25'],
  ['Préférence pour la liquidité', '25'], ['Zone classique', '25'],
  ['Triple équilibre', '25'], ['Équilibre interne', '25'],
  ['Critères de Maastricht', '25'], ['Passager clandestin', '25'],
  ['Pouvoir libératoire', '26'], ['Volatilité', '26'],
  ['Option de change', '26'], ['PPA absolue', '26'],
  ['Sous-évaluation', '26'], ['Parité centrale', '26'],
  ['Cryptoactif', '26'], ['Taux de marge', '26'],
  ['Monnaie', '26'], ['Dévaluation', '26'], ['Prix', '26']
];
const DISPARUS = ['Lecture du graphique', 'Lecture du tableau', 'Son raisonnement'];
const RENVOIS = [['Exportations', '25'], ['Importations', '25'],
                 ['Compétitivité', '26'], ['Désindustrialisation', '26'],
                 ['Balance des paiements', '26'], ['Effet de bilan', '25']];
let ko = 0;
function dire(ok, t, d) { if (!ok) ko++; console.log((ok ? 'OK    ' : 'ÉCHEC ') + t + (d ? ' — ' + d : '')); }

(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({ viewport: { width: 1400, height: 1000 } })).newPage();
  const err = [];
  p.on('pageerror', e => err.push(String(e)));
  await p.goto(FICHIER, { waitUntil: 'domcontentloaded', timeout: 180000 });
  await p.waitForFunction(() => !!window.__ECO_RECHERCHE, { timeout: 180000 });
  await p.evaluate(() => window.showPg('search'));
  await p.waitForSelector('#rq-in', { timeout: 30000 });
  await p.evaluate(() => window.__ECO_RECHERCHE.lancer('monnaie'));
  await p.waitForTimeout(250);
  await p.locator('#rq-outils [data-f="definitions"]').click();
  await p.waitForTimeout(250);

  /* 1 — les faux termes ont disparu de la rubrique */
  for (const t of DISPARUS) {
    const r = await p.evaluate(async terme => {
      window.__ECO_RECHERCHE.lancer(terme);
      await new Promise(r2 => setTimeout(r2, 70));
      const rep = document.querySelector('#rq-rep .rq-rep-t');
      return rep ? rep.textContent.trim() : '';
    }, t);
    dire(r.toLowerCase() !== t.toLowerCase(),
         '« ' + t + " » n'est plus une définition", r || 'aucune réponse');
  }

  /* 2 — les renvois ajoutés conduisent bien au chapitre visé */
  for (const [t, ch] of RENVOIS) {
    const r = await p.evaluate(async ([terme, k]) => {
      window.__ECO_RECHERCHE.lancer(terme);
      await new Promise(r2 => setTimeout(r2, 70));
      const b = [...document.querySelectorAll('#rq-rep [data-k]')]
        .map(x => { try { return JSON.parse(x.getAttribute('data-k')); } catch (e) { return null; } })
        .filter(Boolean);
      return b.map(x => String(x[1]));
    }, [t, ch]);
    dire(r.indexOf(ch) >= 0, '« ' + t + " » renvoie au chapitre " + ch, r.join(','));
  }

  /* 3 — le bouton d'ouverture conduit au passage du cours */
  for (const [t, ch] of ECHANTILLON) {
    const r = await p.evaluate(async ([terme, k]) => {
      const nz = s => String(s || '').toLowerCase()
        .normalize('NFD').replace(/[̀-ͯ]/g, '')
        .replace(/[^a-z0-9]+/g, ' ').trim();
      document.querySelectorAll('.rq-flash').forEach(e => e.classList.remove('rq-flash'));
      window.__ECO_RECHERCHE.lancer(terme);
      await new Promise(r2 => setTimeout(r2, 90));
      const b = [...document.querySelectorAll('#rq-rep [data-k]')].find(x => {
        try { return String(JSON.parse(x.getAttribute('data-k'))[1]) === k; }
        catch (e) { return false; }
      });
      if (!b) return { ouvert: false, raison: 'aucun bouton pour ce chapitre' };
      const cle = JSON.parse(b.getAttribute('data-k'));
      b.click();
      for (let i = 0; i < 45; i++) {
        await new Promise(r2 => setTimeout(r2, 90));
        const e = document.querySelector('#sect-cours .rq-flash');
        if (e) return { ouvert: true, bloc: cle[2],
                        txt: nz(e.innerText).slice(0, 55),
                        page: (document.querySelector('#pg-chapter.on') || {}).id || '' };
      }
      return { ouvert: false, raison: 'aucun passage surligné', bloc: cle[2] };
    }, [t, ch]);
    dire(r.ouvert, '« ' + t + " » ouvre le passage du chapitre " + ch,
         r.ouvert ? 'bloc ' + r.bloc + ' : ' + r.txt : r.raison);
    await p.evaluate(() => window.showPg('search'));
    await p.waitForTimeout(120);
  }

  dire(err.length === 0, 'aucune erreur JavaScript', err.slice(0, 2).join(' | '));
  await nav.close();
  console.log('\n' + (ko ? ko + ' contrôle(s) en échec' : 'tous les contrôles passent'));
  process.exit(ko ? 1 : 0);
})();
