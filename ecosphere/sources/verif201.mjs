import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,180)));
p.on('console',m=>{if(m.type()==='error'&&!/CERT/.test(m.text()))errs.push('c:'+m.text().slice(0,140));});
await p.goto('file://'+process.cwd()+'/app_v201.html',{waitUntil:'load',timeout:240000});
await p.waitForTimeout(16000);
const r = await p.evaluate(async ()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const o={};
  o.nav=[...document.querySelectorAll('.nt')].map(x=>x.textContent.trim());
  o.pages=document.querySelectorAll('.pg').length;
  o.N=window.__ECO_RESUMES_N;
  showPg('resumes'); await sleep(1200);
  const z=document.getElementById('pg-resumes');
  o.visible=!!z && z.classList.contains('on');
  o.cartes=z.querySelectorAll('.rs-card').length;
  o.annees=[...z.querySelectorAll('.rs-year')].map(x=>x.textContent.trim());
  o.compteur=(document.getElementById('rs-count')||{}).textContent;
  // ouvrir un chapitre
  z.querySelector('.rs-card[data-ouvre="23"]').click(); await sleep(500);
  o.det={
    titre:(z.querySelector('.rs-det-t')||{}).textContent,
    sections:[...z.querySelectorAll('.rs-sec-t')].map(x=>x.textContent.trim()),
    idees:z.querySelectorAll('.rs-idee').length,
    transitions:z.querySelectorAll('.rs-idee-v').length,
    ae:z.querySelectorAll('.rs-ae-c').length,
    auteurs:z.querySelectorAll('.rs-ae-c.au').length,
    exemples:z.querySelectorAll('.rs-ae-c.ex').length,
    args:z.querySelectorAll('.rs-ul:not(.deb) li').length,
    debats:z.querySelectorAll('.rs-ul.deb li').length,
    liensCh:z.querySelectorAll('.rs-lien').length,
    min:z.querySelectorAll('.rs-min li').length,
    boutons:[...z.querySelectorAll('.rs-lk')].map(x=>x.textContent.trim())
  };
  // lien vers un autre chapitre depuis la section 5
  z.querySelector('.rs-lien').click(); await sleep(400);
  o.apresLienCh=(z.querySelector('.rs-det-n')||{}).textContent;
  // retour
  document.getElementById('rs-back').click(); await sleep(400);
  o.retourCartes=z.querySelectorAll('.rs-card').length;
  // filtre annee
  const an=document.getElementById('rs-an'); an.value='2'; an.dispatchEvent(new Event('change',{bubbles:true}));
  await sleep(400); o.annee2=z.querySelectorAll('.rs-card').length;
  an.value='0'; an.dispatchEvent(new Event('change',{bubbles:true})); await sleep(300);
  // recherche
  const q=document.getElementById('rs-q'); o.rech={};
  for(const t of ['Ostrom','destruction créatrice','zone d’incertitude','Stolper','courbe du sourire','polycrise','bureaucratie']){
    q.value=t; q.dispatchEvent(new Event('input',{bubbles:true})); await sleep(250);
    o.rech[t]=[...z.querySelectorAll('.rs-card .rs-card-n')].map(x=>x.textContent.trim());
  }
  q.value=''; q.dispatchEvent(new Event('input',{bubbles:true})); await sleep(300);
  // select chapitre
  const sc=document.getElementById('rs-ch'); sc.value='10'; sc.dispatchEvent(new Event('change',{bubbles:true}));
  await sleep(400); o.viaSelect=(z.querySelector('.rs-det-t')||{}).textContent;
  return o;
});
console.log(JSON.stringify({errs:errs.slice(0,6),nErrs:errs.length,...r},null,1));
await b.close();
