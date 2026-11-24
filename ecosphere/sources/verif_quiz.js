/* Campagne de vérification de la section Quiz (v223).
   Chaque test écrit une ligne OK / ÉCHEC. */
const { chromium } = require('playwright');
const path = require('path');

const FICHIER = 'file://' + path.resolve(process.argv[2] || 'app_v223.html');
const CLE = 'eco.quiz.v223';
let ko = 0;
function dire(ok, txt, det) {
  if (!ok) ko++;
  console.log((ok ? 'OK    ' : 'ÉCHEC ') + txt + (det ? ' — ' + det : ''));
}

(async () => {
  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const p = await ctx.newPage();
  const erreurs = [];
  const boites = [];
  p.on('pageerror', e => erreurs.push(String(e)));
  p.on('dialog', d => { boites.push(d.message()); d.accept().catch(() => {}); });

  async function ouvrirQuiz() {
    await p.waitForFunction(() => typeof window.showPg === 'function', { timeout: 180000 });
    await p.waitForFunction(() => !!window.__ECO_QUIZ, { timeout: 180000 });
    await p.evaluate(() => window.showPg('quiz'));
    await p.waitForSelector('#qz-start', { timeout: 30000 });
  }
  async function recharger() {
    await p.reload({ waitUntil: 'domcontentloaded', timeout: 180000 });
    await ouvrirQuiz();
  }
  async function poserHisto(f) {
    await p.evaluate(([src, cle]) => {
      /* eslint-disable no-new-func */
      const ids = window.__ECO_QUIZ.banque.filter(q => String(q.ch) === '22')
        .map(q => q.id);
      const s = { vues: {}, series: [], maj: Date.now() };
      new Function('ids', 's', src)(ids, s);
      localStorage.setItem(cle, JSON.stringify(s));
    }, [f, CLE]);
  }
  const histo = () => p.evaluate(cle =>
    Object.keys(JSON.parse(localStorage.getItem(cle) || '{"vues":{}}').vues).length, CLE);

  await p.goto(FICHIER, { waitUntil: 'domcontentloaded', timeout: 180000 });
  await ouvrirQuiz();

  /* 1 — la page du quiz s'ouvre et le moteur v223 a pris la main */
  const titre = await p.textContent('#pg-quiz .qz-hero h1');
  dire(/quiz/i.test(titre), 'la page Quiz affiche le nouvel écran', titre.trim());

  /* 2 — les filtres sont tous présents */
  for (const [sel, nom, att] of [['#qz-ch', 'chapitres', 'data-ch'],
                            ['#qz-niv', 'niveaux', 'data-niv'],
                            ['#qz-type', 'formats', 'data-type'],
                            ['#qz-n', 'nombre de questions', 'data-n']]) {
    const n = await p.locator(sel + ' [' + att + ']').count();
    dire(n > 0, 'filtre « ' + nom + " » présent", n + ' choix');
  }
  const modes = await p.locator('#pg-quiz [data-mode]').count();
  dire(modes === 4, 'les quatre modes sont proposés', modes + ' modes');

  /* 3 — la banque embarquée */
  const nbBanque = await p.evaluate(() => window.__ECO_QUIZ.banque.length);
  dire(nbBanque === 2340, 'la banque embarquée compte 2340 questions', String(nbBanque));

  /* 4 — pilotage par l'interface */
  async function reglerParUI(chapitre, nombre) {
    await p.locator('#qz-ch [data-ch="' + chapitre + '"]').click();
    await p.waitForTimeout(120);
    await p.locator('#qz-n [data-n="' + nombre + '"]').click();
    await p.waitForTimeout(120);
  }
  /* répond à la question affichée, selon son format */
  async function repondre() {
    const t = await p.evaluate(() => {
      const P = window.__ECO_QUIZ.rejouer();
      return P && P.l[P.i] ? P.l[P.i].type : '';
    });
    if (t === 'qcmm') {
      const n = await p.locator('#qz-opts [data-i]').count();
      for (let k = 0; k < Math.min(2, n); k++)
        await p.locator('#qz-opts [data-i]').nth(k).click();
    } else if (t === 'ordre') {
      const n = await p.locator('#qz-opts [data-i]').count();
      for (let k = 0; k < n; k++)
        await p.locator('#qz-opts [data-i]').nth(k).click();
    } else if (t === 'assoc') {
      const n = await p.locator('#qz-assoc select').count();
      for (let k = 0; k < n; k++)
        await p.locator('#qz-assoc select').nth(k).selectOption({ index: 1 });
    } else if (t === 'courte') {
      await p.fill('#qz-txt', 'La réponse attendue mobilise les mécanismes du cours.');
    } else {
      if (await p.locator('#qz-opts [data-i]').count())
        await p.locator('#qz-opts [data-i]').first().click();
      if (await p.locator('#qz-just').count())
        await p.fill('#qz-just', 'Justification de test.');
    }
    return t;
  }
  /* enchaîne une série entière ; renvoie les identifiants réels */
  async function serieUI(nombre, dejaLancee) {
    if (!dejaLancee) await p.locator('#qz-start').click();
    await p.waitForTimeout(200);
    if (await p.locator('#qz-dlg').count()) return { dialogue: true, ids: [] };
    await p.waitForSelector('#qz-val', { timeout: 20000 });
    const ids = await p.evaluate(() => window.__ECO_QUIZ.rejouer().l.map(q => q.id));
    const vus = [];
    for (let i = 0; i < nombre + 4; i++) {
      if (!(await p.locator('#qz-val').count())) break;
      vus.push(await repondre());
      await p.locator('#qz-val').click();
      await p.waitForTimeout(90);
      if (await p.locator('#qz-suite').count()) {
        await p.locator('#qz-suite').click();
        await p.waitForTimeout(90);
      }
    }
    await p.waitForSelector('#qz-encore', { timeout: 30000 });
    return { ids: ids, formats: vus };
  }

  await reglerParUI('22', '10');
  const dispo1 = await p.textContent('#qz-dispo');
  dire(/inédite/.test(dispo1), 'le compteur d’inédites s’affiche',
       dispo1.replace(/\s+/g, ' ').trim());

  const s1 = await serieUI(10);
  dire(!s1.dialogue && s1.ids.length === 10, 'série 1 : 10 questions enchaînées',
       s1.ids.length + ' question(s), formats : ' +
       [...new Set(s1.formats)].join(', '));
  dire(await histo() === 10, 'les 10 questions vues sont enregistrées',
       String(await histo()));
  dire(boites.length === 0, 'aucune boîte « vous n’avez pas répondu » parasite',
       boites.slice(0, 2).join(' | '));

  /* 5 — bilan : maîtrise / à revoir / liens vers le cours */
  const liens = await p.locator('#pg-quiz .qz-src').count();
  dire(await p.locator('#pg-quiz .qz-card h3').first().isVisible(),
       'le bilan affiche les rubriques de synthèse');
  dire(liens > 0, 'liens « Rouvrir ce passage » présents dans le bilan',
       liens + ' lien(s)');

  /* 6 — série 2 avec les mêmes filtres : aucune répétition */
  await p.locator('#qz-encore').click();
  await p.waitForTimeout(250);
  const s2 = await serieUI(10, true);
  dire(!s2.dialogue && s2.ids.length === 10, 'série 2 : 10 questions enchaînées',
       String(s2.ids.length));
  const croise12 = s2.ids.filter(x => s1.ids.indexOf(x) >= 0);
  dire(croise12.length === 0, 'série 2 sans aucune question de la série 1',
       croise12.length + ' répétition(s)');
  dire(await histo() === 20, 'historique cumulé à 20 questions', String(await histo()));

  /* 7 — rechargement de la page : l'historique survit */
  await recharger();
  dire(await histo() === 20, 'après rechargement, l’historique est conservé',
       String(await histo()));
  await reglerParUI('22', '10');
  const s3 = await serieUI(10);
  const croise3 = s3.ids.filter(x => s1.ids.indexOf(x) >= 0 || s2.ids.indexOf(x) >= 0);
  dire(!s3.dialogue && s3.ids.length === 10 && croise3.length === 0,
       'série 3 après rechargement : aucune question déjà vue',
       croise3.length + ' répétition(s) sur ' + s3.ids.length);

  /* 8 — réserve insuffisante : le dialogue s'affiche avant de lancer */
  await poserHisto("ids.slice(0, ids.length - 3).forEach(function(i){ s.vues[i] = {d:1, t:Date.now()}; });");
  await recharger();
  await reglerParUI('22', '20');
  await p.locator('#qz-start').click();
  await p.waitForTimeout(300);
  const dlg = await p.locator('#qz-dlg').count();
  let txtDlg = '';
  if (dlg) txtDlg = (await p.textContent('#qz-dlg')).replace(/\s+/g, ' ').trim();
  dire(dlg === 1, 'réserve insuffisante : le dialogue s’affiche AVANT la série',
       txtDlg.slice(0, 140));
  const choix = await p.locator('#qz-dlg [data-ch]').count();
  dire(choix === 4, 'le dialogue propose 4 issues (courte / élargir / répétitions / annuler)',
       choix + ' choix');
  dire(/\b3\b/.test(txtDlg) && /inédite/.test(txtDlg),
       'le dialogue annonce le nombre exact d’inédites', txtDlg.slice(0, 90));

  /* 9 — série courte acceptée : 3 questions */
  await p.locator('#qz-dlg [data-ch="court"]').click();
  await p.waitForTimeout(250);
  const nQ = await p.evaluate(() => window.__ECO_QUIZ.rejouer().l.length);
  dire(nQ === 3, 'la série courte comporte bien 3 questions', String(nQ));
  const ined = await p.evaluate(cle => {
    const v = JSON.parse(localStorage.getItem(cle)).vues;
    return window.__ECO_QUIZ.rejouer().l.filter(q => v[q.id]).length;
  }, CLE);
  dire(ined === 0, 'la série courte ne contient que des inédites',
       ined + ' déjà vue(s)');

  /* 10 — accepter les répétitions */
  await recharger();
  await reglerParUI('22', '20');
  await p.locator('#qz-start').click();
  await p.waitForTimeout(300);
  await p.locator('#qz-dlg [data-ch="repet"]').click();
  await p.waitForTimeout(300);
  const nRep = await p.evaluate(() => window.__ECO_QUIZ.rejouer().l.length);
  dire(nRep === 20, 'répétitions explicitement acceptées : la série fait 20 questions',
       String(nRep));

  /* 11 — annuler laisse l'écran d'accueil intact */
  await recharger();
  await reglerParUI('22', '20');
  await p.locator('#qz-start').click();
  await p.waitForTimeout(250);
  await p.locator('#qz-dlg [data-ch="rien"]').click();
  await p.waitForTimeout(250);
  dire(await p.locator('#qz-start').count() === 1 &&
       await p.locator('#qz-dlg').count() === 0,
       'le choix « Annuler » revient à l’écran de réglage sans lancer de série');

  /* 12 — mode Revoir mes erreurs */
  await poserHisto("ids.slice(0,6).forEach(function(i){ s.vues[i]={d:0,t:Date.now()}; });" +
                   "ids.slice(6,30).forEach(function(i){ s.vues[i]={d:1,t:Date.now()}; });");
  await recharger();
  await p.locator('#pg-quiz [data-mode="erreurs"]').click();
  await p.waitForTimeout(200);
  await reglerParUI('22', '10');
  await p.locator('#qz-start').click();
  await p.waitForTimeout(300);
  const err = await p.evaluate(cle => {
    const P = window.__ECO_QUIZ.rejouer();
    if (!P) return null;
    const v = JSON.parse(localStorage.getItem(cle)).vues;
    return { n: P.l.length, rates: P.l.filter(q => v[q.id] && !v[q.id].d).length };
  }, CLE);
  dire(err && err.rates === 6 && err.n >= 6 && err.n <= 10,
       'mode « Revoir mes erreurs » : les 6 questions ratées reviennent, complétées par des voisines',
       err ? err.n + ' question(s), ' + err.rates + ' déjà ratée(s)' : 'pas de série');

  /* 13 — mode Examen : correction à la fin seulement */
  await recharger();
  await p.evaluate(cle => localStorage.removeItem(cle), CLE);
  await recharger();
  await p.locator('#pg-quiz [data-mode="examen"]').click();
  await p.waitForTimeout(200);
  await reglerParUI('26', '10');
  await p.locator('#qz-start').click();
  await p.waitForTimeout(250);
  let correctionPendant = false;
  for (let i = 0; i < 11; i++) {
    if (!(await p.locator('#qz-val').count())) break;
    await repondre();
    await p.locator('#qz-val').click();
    await p.waitForTimeout(90);
    if ((await p.locator('#qz-corr').count()) &&
        (await p.locator('#qz-corr').textContent()).trim().length > 40)
      correctionPendant = true;
    if (await p.locator('#qz-suite').count()) {
      await p.locator('#qz-suite').click();
      await p.waitForTimeout(90);
    }
  }
  dire(!correctionPendant, 'mode Examen : aucune correction pendant la série');
  await p.waitForSelector('#qz-encore', { timeout: 20000 });
  const bilanExam = (await p.textContent('#pg-quiz')).replace(/\s+/g, ' ');
  dire(/[Cc]orrection/.test(bilanExam),
       'mode Examen : la correction détaillée figure dans le bilan');

  /* 14 — transversal : plusieurs chapitres dans une même série */
  await recharger();
  await p.evaluate(cle => localStorage.removeItem(cle), CLE);
  await recharger();
  await p.locator('#pg-quiz [data-mode="transversal"]').click();
  await p.waitForTimeout(200);
  await p.locator('#qz-n [data-n="10"]').click();
  await p.waitForTimeout(150);
  await p.locator('#qz-start').click();
  await p.waitForTimeout(300);
  const chaps = await p.evaluate(() => {
    const P = window.__ECO_QUIZ.rejouer();
    return P ? [...new Set(P.l.map(q => String(q.ch)))] : [];
  });
  dire(chaps.length >= 4, 'quiz transversal : la série brasse plusieurs chapitres',
       chaps.length + ' chapitre(s) : ' + chaps.join(' '));

  /* 15 — filtres sous-partie, niveau et format */
  await recharger();
  await p.evaluate(cle => localStorage.removeItem(cle), CLE);
  await recharger();
  await reglerParUI('23', '10');
  await p.locator('#qz-niv [data-niv="raisonner"]').click();
  await p.waitForTimeout(150);
  await p.locator('#qz-type [data-type="courte"]').click();
  await p.waitForTimeout(150);
  await p.locator('#qz-start').click();
  await p.waitForTimeout(300);
  const filtre = await p.evaluate(() => {
    const P = window.__ECO_QUIZ.rejouer();
    return P ? P.l.map(q => String(q.ch) + '/' + q.niv + '/' + q.type) : [];
  });
  dire(filtre.length > 0 && filtre.every(x => x === '23/raisonner/courte'),
       'filtres niveau + format respectés', filtre.length + ' question(s) : ' +
       [...new Set(filtre)].join(', '));

  await p.evaluate(cle => localStorage.removeItem(cle), CLE);
  await recharger();
  /* on prend la sous-partie du chapitre 23 la plus fournie */
  const sp = await p.evaluate(() => {
    const n = {};
    window.__ECO_QUIZ.banque.forEach(q => {
      if (String(q.ch) === '23') n[q.sp] = (n[q.sp] || 0) + 1;
    });
    return Object.keys(n).sort((a, b) => n[b] - n[a])[0];
  });
  await p.locator('#qz-ch [data-ch="23"]').click();
  await p.waitForTimeout(250);
  if (await p.locator('#qz-sp [data-sp="' + sp + '"]').count()) {
    await p.locator('#qz-sp [data-sp="' + sp + '"]').click();
    await p.waitForTimeout(150);
    await p.locator('#qz-n [data-n="10"]').click();
    await p.waitForTimeout(150);
    await p.locator('#qz-start').click();
    await p.waitForTimeout(400);
    const spl = await p.evaluate(() => {
      const P = window.__ECO_QUIZ.rejouer();
      return P ? [...new Set(P.l.map(q => q.sp))] : [];
    });
    dire(spl.length === 1 && spl[0] === sp, 'filtre sous-partie respecté',
         sp + ' → ' + (spl.join(', ') || 'série non lancée'));
  } else {
    dire(false, 'filtre sous-partie proposé après choix du chapitre', 'absent');
  }

  /* 16 — Ma progression */
  await poserHisto("ids.slice(0,12).forEach(function(i){ s.vues[i]={d:1,t:Date.now()}; });" +
                   "ids.slice(12,18).forEach(function(i){ s.vues[i]={d:0,t:Date.now()}; });");
  await recharger();
  dire(await p.locator('#qz-prog').count() === 1, 'le bouton « Ma progression » existe');
  await p.locator('#qz-prog').click();
  await p.waitForTimeout(300);
  const prog = (await p.textContent('#pg-quiz')).replace(/\s+/g, ' ');
  dire(/progression/i.test(prog), 'l’écran « Ma progression » s’ouvre');
  const lignes = await p.evaluate(() => [...document.querySelectorAll('#pg-quiz .qz-card')]
    .filter(c => /Par chapitre/.test(c.querySelector('h3') ? c.querySelector('h3').textContent : ''))
    .map(c => [...c.querySelectorAll('.qz-li b')].map(b => b.textContent))[0] || []);
  dire(lignes.length === 16, 'la progression couvre les 16 chapitres',
       lignes.length + ' ligne(s) : ' + lignes.slice(0, 2).join(' / ') + ' … ' +
       lignes.slice(-1));

  /* 17 — lien profond vers le cours depuis le bilan */
  await recharger();
  await p.evaluate(cle => localStorage.removeItem(cle), CLE);
  await recharger();
  await reglerParUI('22', '10');
  const s5 = await serieUI(10);
  dire(!s5.dialogue, 'série courte de contrôle lancée');
  const src = p.locator('#pg-quiz .qz-src').first();
  let lien = 'aucun';
  if (await src.count()) {
    lien = (await src.getAttribute('data-ch')) + '/' + (await src.getAttribute('data-b'));
    await src.click();
    await p.waitForTimeout(600);
    const page = await p.evaluate(() => {
      const v = [...document.querySelectorAll('.page, [id^="pg-"]')]
        .filter(e => e.offsetParent !== null);
      return v.length ? v[v.length - 1].id : '';
    });
    dire(/cours|chap/i.test(page) || page !== 'pg-quiz',
         'le lien « Rouvrir ce passage » ouvre le cours', lien + ' → ' + page);
  } else {
    dire(false, 'le bilan propose un lien vers le cours', lien);
  }

  /* 18 — aucune erreur JavaScript pendant toute la campagne */
  dire(erreurs.length === 0, 'aucune erreur JavaScript levée',
       erreurs.slice(0, 3).join(' | '));

  await nav.close();
  console.log('\n' + (ko ? ko + ' test(s) en échec' : 'tous les tests passent'));
  process.exit(ko ? 1 : 0);
})();
