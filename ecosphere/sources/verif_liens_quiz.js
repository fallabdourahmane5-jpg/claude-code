/* Les corrections renvoient-elles au bon passage du cours ?
   Pour chaque chapitre, on tire 6 questions réparties dans la banque et on
   suit le chemin exact du bouton « Ouvrir le passage du cours » : on vérifie
   qu'un passage est surligné et que son texte est bien celui du bloc visé. */
const { chromium } = require('playwright');
const path = require('path');
const FICHIER = 'file://' + path.resolve(process.argv[2] || 'app_v223.html');
const CHAPS = ['1','2','3','4','5','6','7','8','9','10','21','22','23','24','25','26'];
const N = Number(process.argv[3] || 6);

(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({ viewport: { width: 1400, height: 1000 } })).newPage();
  const err = [];
  p.on('pageerror', e => err.push(String(e)));
  await p.goto(FICHIER, { waitUntil: 'domcontentloaded', timeout: 180000 });
  await p.waitForFunction(() => !!window.__ECO_QUIZ && !!window.__ECO_RECHERCHE &&
    !!window.__ECO_GARDE_COURS, { timeout: 180000 });
  await p.waitForTimeout(2500);

  let ok = 0, ko = 0;
  const details = [];
  for (const c of CHAPS) {
    const ech = await p.evaluate(([ch, n]) => {
      const l = window.__ECO_QUIZ.banque.filter(q => String(q.ch) === ch);
      const pas = Math.max(1, Math.floor(l.length / n));
      return Array.from({ length: n }, (_, i) => l[i * pas]).filter(Boolean)
        .map(q => ({ id: q.id, ch: String(q.ch), b: q.b }));
    }, [c, N]);
    let bons = 0;
    for (const q of ech) {
      const r = await p.evaluate(async ({ ch, b }) => {
        const red = s => String(s || '').toLowerCase()
          .replace(/[^0-9a-zàâäçéèêëîïôöùûüÿœæ]+/g, ' ').replace(/\s+/g, ' ').trim();
        document.querySelectorAll('.qz-vise, .rq-flash')
          .forEach(e => { e.classList.remove('qz-vise'); e.classList.remove('rq-flash'); });
        try { window.__ECO_GARDE_COURS.restaurer(); } catch (e) {}
        const txt = window.__ECO_QUIZ.texteBloc(ch, b);
        try { window.__ECO_RECHERCHE.ouvrir(['ch', ch, -1]); } catch (e) {}
        window.__ECO_QUIZ.viserPassage(b, txt);
        for (let i = 0; i < 45; i++) {
          await new Promise(r2 => setTimeout(r2, 90));
          const e = document.querySelector('#sect-cours .qz-vise');
          if (e) {
            const z = red(e.innerText || e.textContent), t = red(txt);
            return { trouve: true,
              bon: z.indexOf(t.slice(0, 45)) >= 0 || t.indexOf(z.slice(0, 40)) >= 0,
              vu: z.slice(0, 60), attendu: t.slice(0, 60) };
          }
        }
        return { trouve: false, attendu: red(txt).slice(0, 60) };
      }, q);
      /* on laisse le repérage se stabiliser avant le cas suivant */
      await p.waitForTimeout(700);
      if (r.trouve && r.bon) { ok++; bons++; } else {
        ko++;
        details.push('ÉCHEC ' + q.id + ' (ch' + q.ch + ' bloc ' + q.b + ')' +
          '\n  surligné : ' + (r.vu || '— rien —') + '\n  attendu  : ' + r.attendu);
      }
    }
    process.stdout.write('ch' + c + ':' + bons + '/' + ech.length + ' ');
  }
  console.log('\n');
  details.slice(0, 14).forEach(d => console.log(d));
  console.log('\n' + ok + ' lien(s) exact(s), ' + ko + ' en échec');
  console.log(err.length ? 'erreurs JS : ' + err.slice(0, 3).join(' | ')
                         : 'aucune erreur JS');
  await nav.close();
  process.exit(ko ? 1 : 0);
})();
