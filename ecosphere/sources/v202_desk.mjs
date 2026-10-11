import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,200)));
await p.goto('file://'+process.cwd()+'/app_v202.html',{waitUntil:'load',timeout:300000});
await p.waitForTimeout(14000);

const nav = await p.evaluate(()=>{
  const b=[...document.querySelectorAll('.nt')].find(x=>(x.getAttribute('onclick')||'').includes("'resumes'"));
  if(b) b.click();
  return !!b;
});
await p.waitForTimeout(1200);
console.log('onglet Résumés présent :', nav);

const liste = await p.evaluate(()=>({
  cartes: document.querySelectorAll('#pg-resumes .rs-card').length,
  compteur: (document.getElementById('rs-count')||{}).textContent,
  annees: [...document.querySelectorAll('#pg-resumes .rs-year')].map(x=>x.textContent),
  meta: (document.querySelector('#pg-resumes .rs-card-m')||{}).textContent,
}));
console.log('liste :', JSON.stringify(liste));

// ouvrir chaque résumé et vérifier la structure
const rows=[];
for (const c of ['1','2','3','4','5','6','7','8','9','10','21','22','23']) {
  await p.evaluate(ch=>window.ouvrirResume(ch), c);
  await p.waitForTimeout(650);
  const o = await p.evaluate(()=>{
    const q=s=>document.querySelectorAll('#pg-resumes '+s).length;
    return {
      titre: (document.querySelector('#pg-resumes .rs-det-t')||{}).textContent,
      sections: q('.rs-sec'),
      liens: q('.rs-lk'),
      plan: q('.rs-plan li'),
      parties: q('.rs-part'),
      sp: q('.rs-sp'),
      para: q('.rs-sp-d'),
      mec: q('.rs-mec'),
      lim: q('.rs-lim'),
      transitions: q('.rs-part-v'),
      ae: q('.rs-ae-c'),
      arg: q('.rs-ul:not(.deb) li'),
      deb: q('.rs-ul.deb li'),
      liensCh: q('.rs-lien'),
      min: q('.rs-min li'),
      gras: q('.rs-sp-d b'),
      hauteur: Math.round(document.querySelector('#pg-resumes .rs-wrap').getBoundingClientRect().height),
      overflow: document.documentElement.scrollWidth - window.innerWidth,
    };
  });
  rows.push([c,o]);
}
for (const [c,o] of rows) {
  console.log(('ch'+c).padEnd(5), 'sec',o.sections,'liens',o.liens,'plan',o.plan,'parties',o.parties,
    'sp',o.sp,'para',o.para,'mec',o.mec,'lim',o.lim,'trans',o.transitions,'ae',o.ae,
    'arg',o.arg,'deb',o.deb,'lienCh',o.liensCh,'min',o.min,'gras',o.gras,
    'h',o.hauteur,'ovf',o.overflow,'|',o.titre);
}

// replier / déplier
const pli = await p.evaluate(()=>{
  const r={};
  document.getElementById('rs-fermer').click();
  r.apresFermer = [...document.querySelectorAll('#pg-resumes .rs-part-b')]
    .filter(x=>x.style.display==='none').length;
  document.getElementById('rs-ouvrir').click();
  r.apresOuvrir = [...document.querySelectorAll('#pg-resumes .rs-part-b')]
    .filter(x=>x.style.display==='none').length;
  const h=document.querySelector('#pg-resumes .rs-part-h');
  h.click();
  r.apresClicEntete = [...document.querySelectorAll('#pg-resumes .rs-part-b')]
    .filter(x=>x.style.display==='none').length;
  h.click();
  r.total = document.querySelectorAll('#pg-resumes .rs-part-b').length;
  return r;
});
console.log('pliage :', JSON.stringify(pli));

// plan cliquable
const plan = await p.evaluate(()=>{
  const li=document.querySelectorAll('#pg-resumes .rs-plan li');
  if(!li.length) return 'aucun';
  li[li.length-1].click();
  return 'clic sur « '+li[li.length-1].textContent.slice(0,40)+' »';
});
await p.waitForTimeout(500);
console.log('plan :', plan);

// recherche interne
const rech = await p.evaluate(()=>{
  const i=document.getElementById('rs-q');
  i.value='Stolper-Samuelson';
  i.dispatchEvent(new Event('input',{bubbles:true}));
  return {cartes:document.querySelectorAll('#pg-resumes .rs-card').length,
          cpt:(document.getElementById('rs-count')||{}).textContent};
});
console.log('recherche « Stolper-Samuelson » :', JSON.stringify(rech));

// index global
const idx = await p.evaluate(()=>{
  try{ return SEARCH_INDEX.filter(x=>x.type==='résumé').length; }catch(e){ return 'n/a'; }
});
console.log('entrées « résumé » dans SEARCH_INDEX :', idx);

// les six liens de navigation
await p.evaluate(()=>window.ouvrirResume('23'));
await p.waitForTimeout(500);
for (const [attr,cible] of [['data-cours','pg-ch'],['data-fiches','pg-fc'],['data-carte','pg-maps'],
                            ['data-atlas','pg-atlas'],['data-chiffres',null],['data-sujets','pg-subjects']]) {
  await p.evaluate(()=>window.ouvrirResume('23'));
  await p.waitForTimeout(450);
  const ok = await p.evaluate(a=>{
    const b=document.querySelector('#pg-resumes ['+a+']');
    if(!b) return 'bouton absent';
    b.click();
    return 'cliqué';
  }, attr);
  await p.waitForTimeout(900);
  const vis = await p.evaluate(()=>{
    const on=[...document.querySelectorAll('.pg.on')].map(x=>x.id);
    const mod=[...document.querySelectorAll('[id*=chiffre],[id*=Chiffre]')]
      .filter(x=>getComputedStyle(x).display!=='none').map(x=>x.id).slice(0,3);
    return {on, mod};
  });
  console.log(attr.padEnd(14), ok, '->', JSON.stringify(vis));
}

console.log('erreurs JS :', errs.length, errs.slice(0,4));
await b.close();
