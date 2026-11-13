import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const D = '/tmp/claude-0/-home-user-claude-code/c0291a61-f762-553a-8cee-cee4697398a0/scratchpad/';
const p = await b.newPage({viewport:{width:1400,height:950}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://' + D + 'app_v219.html');
await p.waitForTimeout(34000);
await p.evaluate(()=>showPg('search'));
await p.waitForTimeout(700);
const Q = [
 ['1','capital'],['1','dette publique'],['1','multiplicateur keynésien'],['1','salaire'],
 ['2','taux de change'],['2','économie d’endettement'],['2','marché interbancaire'],
 ['3','demande effective'],['3','classe stérile'],['3','état stationnaire'],
 ['4','taux marginal de substitution'],['4','utilité totale'],['4','courbe de demande'],
 ['5','externalité'],['5','coût social'],['5','rente de monopole'],
 ['6','capital naturel'],['6','coefficient de capital'],['6','croissance intensive'],
 ['7','capabilités'],['7','spécialisation primaire'],['7','économie duale'],
 ['8','capital technologique'],['8','production de masse'],['8','temps partiel subi'],
 ['9','libre entrée'],['9','concentration géographique'],['9','marchés contestables'],
 ['10','anomie'],['10','classe ouvrière'],['10','dynamique de groupe'],
 ['21','position extérieure nette'],['21','taux de couverture'],['21','tarif Méline'],
 ['22','compétitivité'],['22','société mère'],['22','dépendance technologique'],
 ['23','prix international'],['23','demande de variété'],['23','concurrence déloyale'],
 ['24','multilatéralisme commercial'],['24','tarif extérieur commun'],['24','coordination internationale'],
 ['*','coût'],['*','taux'],['*','PEN'],['*','capitl humain'],['*','deficit comercial'],
 ['*','habitus'],['*','balance courante'],['*','effet d’aubaine'],['*','intégration régionale'],
];
let ko = [];
for (const [ch,q] of Q) {
  const r = await p.evaluate((q)=>{
    window.__ECO_RECHERCHE.lancer(q);
    const rep = document.querySelector('#rq-rep .rq-rep');
    const fam = document.querySelector('#rq-fam .rq-fam');
    const l = [...document.querySelectorAll('#rq-res .rq-r')];
    const cpt = (document.querySelector('#rq-outils .rq-cpt')||{}).textContent||'';
    return {rep: rep ? rep.querySelector('.rq-rep-t').textContent : null,
      ty: rep ? rep.querySelector('.rq-ty').textContent : null,
      dl: rep ? rep.querySelector('.rq-rep-d').textContent.length : 0,
      ou: rep ? rep.querySelectorAll('.rq-o').length : 0,
      dist: rep ? !!rep.querySelector('.rq-dist') : false,
      fam: fam ? fam.querySelectorAll('.rq-k').length : 0,
      cpt: cpt.replace(/\s+/g,' '), n: l.length,
      t1: l.length ? l[0].querySelector('.rq-rt').textContent.slice(0,40) : '',
      mk: l.length ? l[0].querySelectorAll('mark').length : 0};
  }, q);
  const ok = r.rep || r.n;
  if(!ok && q!=='habitus') ko.push(q);
  console.log(('ch'+ch).padEnd(5) + q.padEnd(32) + ' | ' + (r.cpt||'0').padEnd(34) +
    ' | rép: ' + (r.rep ? ('['+r.ty+'] '+r.rep.slice(0,30)+' ('+r.dl+'c, où'+r.ou+(r.dist?', dist':'')+')') : '—') +
    (r.fam ? ' | fam '+r.fam : ''));
}
console.log('\nSANS RÉSULTAT : ' + JSON.stringify(ko));
console.log('errs ' + JSON.stringify(errs.slice(0,4)));
await b.close();
