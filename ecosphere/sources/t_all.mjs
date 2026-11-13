import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v218.html');
await p.waitForTimeout(34000);
console.log('index', JSON.stringify(await p.evaluate(()=>window.__ECO_RECHERCHE.compter())));
// une requête par chapitre + les cas limites
const Q = [
 ['1','multiplicateur keynésien'], ['1','comptabilité nationale'], ['1','dette publique'],
 ['2','création monétaire'], ['2','économie d’endettement'], ['2','quantitative easing'],
 ['3','demande effective'], ['3','loi des débouchés'], ['3','destruction créatrice'],
 ['4','utilité marginale'], ['4','élasticité de la demande'], ['4','taux marginal de substitution'],
 ['5','externalité'], ['5','bien public'], ['5','monopole naturel'],
 ['6','productivité globale des facteurs'], ['6','croissance endogène'], ['6','coefficient de Gini'],
 ['7','capabilités'], ['7','termes de l’échange'], ['7','dividende démographique'],
 ['8','taylorisme'], ['8','temps partiel subi'], ['8','destruction créatrice d’emplois'],
 ['9','pouvoir de marché'], ['9','marchés contestables'], ['9','différenciation des produits'],
 ['10','anomie'], ['10','solidarité organique'], ['10','bureaucratie'],
 ['21','position extérieure nette'], ['21','deuxième dégroupage'], ['21','taux de pénétration'],
 ['22','compétitivité hors-prix'], ['22','secteurs stratégiques'], ['22','premier choc chinois'],
 ['23','avantage comparatif'], ['23','protectionnisme éducateur'], ['23','paradoxe de Leontief'],
 ['24','multilatéralisme'], ['24','stabilité hégémonique'], ['24','bien public mondial'],
 ['*','Bairoch'], ['*','Keynes'], ['*','PEN'], ['*','IDE'], ['*','PIB'],
 ['*','avantage comparatifs'], ['*','protectionisme'], ['*','exterrnalite'],
 ['*','habitus'], ['*','dilemme de Triffin'], ['*','chapitre 7 pauvreté'],
];
let ko = [];
for (const [ch, q] of Q) {
  const r = await p.evaluate((q)=>{
    const i = document.getElementById('rq-in'); i.value = q;
    window.__ECO_RECHERCHE.lancer();
    const g = [...document.querySelectorAll('#pg-search .rq-g')];
    const dbg = window.__ECO_RECHERCHE.debug(q);
    return {n:g.length, corr:dbg.Q.corrige,
      top: g.slice(0,3).map(x=>({ty:x.querySelector('.rq-ty').textContent,
        ti:x.querySelector('.rq-ti').textContent.slice(0,54),
        tx:(x.querySelector('.rq-tx')||{}).textContent.slice(0,58),
        mk:x.querySelectorAll('mark').length, ou:x.querySelectorAll('.rq-o').length}))};
  }, q);
  const t = r.top[0];
  const statut = !r.n ? 'VIDE' : (t.mk===0 ? 'SANS SURLIGNAGE' : (!t.tx ? 'SANS EXTRAIT' : 'ok'));
  if(statut !== 'ok' && q !== 'habitus' && q !== 'dilemme de Triffin') ko.push(q+' → '+statut);
  console.log(('ch'+ch).padEnd(5) + (q+'').padEnd(34) + String(r.n).padStart(3) + ' grp  ' +
    (r.corr?'[corrigé] ':'') + '[' + (t?t.ty:'—') + '] ' + (t?t.ti:'') + '  (mk'+(t?t.mk:0)+' ou'+(t?t.ou:0)+')');
  if (r.top[1]) console.log('     └─ 2e: [' + r.top[1].ty + '] ' + r.top[1].ti);
}
console.log('\nANOMALIES', JSON.stringify(ko));
console.log('errs', JSON.stringify(errs.slice(0,4)));
await b.close();
