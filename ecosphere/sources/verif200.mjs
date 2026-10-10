import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1400,height:1000}});
const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,180)));
p.on('console',m=>{if(m.type()==='error'&&!/CERT/.test(m.text()))errs.push('c:'+m.text().slice(0,140));});
await p.goto('file://'+process.cwd()+'/app_v200.html',{waitUntil:'load',timeout:240000});
await p.waitForTimeout(16000);
const r = await p.evaluate(async ()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const o={};
  o.nav=[...document.querySelectorAll('.nt')].map(x=>x.textContent.trim());
  o.pages=document.querySelectorAll('.pg').length;
  o.N=window.__ECO_CHIFFRES_N;
  showPg('chiffres'); await sleep(1200);
  const z=document.getElementById('pg-chiffres');
  o.visible=!!z && z.classList.contains('on');
  o.cartes=z.querySelectorAll('.cf-card').length;
  // titres : chaque carte doit porter un titre explicite
  const tt=[...z.querySelectorAll('.cf-card')].map(c=>{
    const e=c.querySelector('.cf-t'); return e?e.textContent.trim():null; });
  o.titres={total:tt.length, vides:tt.filter(x=>!x).length,
            sansValeur:tt.filter(x=>x&&x.indexOf(' : ')<0).length,
            nombreSeul:tt.filter(x=>x&&/^[\d\s,.%€+\u2212-]+$/.test(x.split(' : ')[0])).length,
            avecAnnee:tt.filter(x=>x&&/\b(1[5-9]\d\d|20\d\d)\b/.test(x)).length,
            exemples:tt.slice(0,5)};
  o.ancienneClasse=z.querySelectorAll('.cf-v').length;
  o.precision=z.querySelectorAll('.cf-u').length;
  o.corps={src:z.querySelectorAll('.cf-src').length, demontre:z.querySelectorAll('.cf-sec').length,
           diss:z.querySelectorAll('.cf-q').length};
  o.groupes=z.querySelectorAll('.cf-grp').length;
  o.compteur=(document.getElementById('cf-count')||{}).textContent;
  o.chips=[...z.querySelectorAll('.cf-chip')].map(x=>x.textContent.trim());
  // filtre par chapitre
  const c23=[...z.querySelectorAll('.cf-chip')].find(x=>x.textContent.trim()==='2ᵉ année — Ch. 3');
  if(c23){ c23.click(); await sleep(500);
    o.ch23={cartes:z.querySelectorAll('.cf-card').length, groupes:z.querySelectorAll('.cf-grp').length,
            prio:z.querySelectorAll('.cf-card.prio').length, comp:z.querySelectorAll('.cf-card.comp').length}; }
  // filtre annee
  document.querySelector('.cf-chip[data-ch="0"]').click(); await sleep(300);
  const an=document.getElementById('cf-an'); an.value='2'; an.dispatchEvent(new Event('change',{bubbles:true}));
  await sleep(400); o.annee2=z.querySelectorAll('.cf-card').length;
  an.value='0'; an.dispatchEvent(new Event('change',{bubbles:true})); await sleep(300);
  // filtre priorite
  const im=document.getElementById('cf-imp'); im.value='p'; im.dispatchEvent(new Event('change',{bubbles:true}));
  await sleep(400); o.prioSeules=z.querySelectorAll('.cf-card').length;
  im.value='0'; im.dispatchEvent(new Event('change',{bubbles:true})); await sleep(300);
  // recherche
  const q=document.getElementById('cf-q'); o.rech={};
  for(const t of ['dette','taux d’ouverture','Prebisch','INSEE','terres rares','1 288','Hawley']){
    q.value=t; q.dispatchEvent(new Event('input',{bubbles:true})); await sleep(300);
    o.rech[t]=z.querySelectorAll('.cf-card').length;
  }
  q.value=''; q.dispatchEvent(new Event('input',{bubbles:true})); await sleep(300);
  // lien vers le cours
  const lk=z.querySelector('[data-cours]');
  o.lienCours=lk?lk.getAttribute('data-cours'):'absent';
  if(lk){ lk.click(); await sleep(900); o.apresCours=(document.querySelector('.pg.on')||{}).id; }
  showPg('chiffres'); await sleep(600);
  const lf=document.querySelector('#pg-chiffres [data-fiches]');
  if(lf){ lf.click(); await sleep(1200); o.apresFiches=(document.querySelector('.pg.on')||{}).id; }
  // indexation dans la recherche globale
  showPg('search'); await sleep(900);
  try{ o.SIchiffres=SEARCH_INDEX.filter(x=>x.type==='chiffre').length; }catch(e){ o.SIchiffres='err'; }
  const si=document.getElementById('si');
  si.value='taux d’ouverture'; doSearch(); await sleep(300);
  const it=[...document.querySelectorAll('#search-res .ri')];
  o.rechGlobale=it.length;
  o.rechChiffre=it.filter(x=>/chiffre/i.test(x.querySelector('.ri-type').textContent)).length;
  const cible=it.find(x=>/chiffre/i.test(x.querySelector('.ri-type').textContent));
  if(cible){ cible.click(); await sleep(1000); o.apresClic=(document.querySelector('.pg.on')||{}).id; }
  return o;
});
console.log(JSON.stringify({errs:errs.slice(0,6),nErrs:errs.length,...r},null,1));
await p.evaluate(()=>showPg('chiffres')); await p.waitForTimeout(1200);
await p.screenshot({path:'v200_chiffres.png'});
await b.close();
