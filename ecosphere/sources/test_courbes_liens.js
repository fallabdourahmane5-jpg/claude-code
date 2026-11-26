const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const ATT = JSON.parse(fs.readFileSync('_attendus.json','utf8'));
(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({viewport:{width:1440,height:1000}})).newPage();
  const err=[]; p.on('pageerror',e=>err.push(String(e))); p.on('dialog',d=>d.accept());
  await p.goto('file://'+path.resolve(process.argv[2]),{waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_COURBES,{timeout:180000});
  await p.evaluate(()=>window.showPg('graphs'));
  await p.waitForSelector('#pg-graphs .cb-vign',{timeout:30000});
  let ok=0; const ko=[];
  for (const a of ATT) {
    await p.evaluate(()=>window.showPg('graphs'));
    await p.evaluate(id=>window.__ECO_COURBES.ouvrir(id), a.id);
    await p.waitForSelector('#pg-graphs .cb-lien',{timeout:10000});
    await p.locator('#pg-graphs .cb-lien').nth(a.i).click();
    await p.waitForTimeout(2400);
    const r = await p.evaluate(()=>{
      const v=document.querySelector('#pg-chapter .qz-vise, .qz-vise');
      return {pg:[...document.querySelectorAll('[id^=pg-]')].filter(e=>e.offsetParent!==null).map(e=>e.id)[0],
              y:Math.round(document.scrollingElement.scrollTop),
              vise: v ? v.textContent.trim().slice(0,90) : null,
              dansVue: v ? (()=>{const b=v.getBoundingClientRect();
                return b.top>-60 && b.top<window.innerHeight-40;})() : false};
    });
    const nz = s => (s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
    const att = nz(a.attendu), vis = nz(r.vise);
    const bon = r.pg==='pg-chapter' && r.vise && r.dansVue &&
                (att.indexOf(vis.slice(0,40))>=0 || vis.indexOf(att.slice(0,40))>=0);
    if (bon) ok++; else ko.push(a.id+' #'+(a.i+1)+' ch'+a.c+'/b'+a.b+' → visé='+JSON.stringify(r.vise)+' vue='+r.dansVue+' y='+r.y);
  }
  console.log('LIENS : '+(ok+ko.length)+' testés · '+ok+' flashent le bon passage');
  if (ko.length) console.log('ÉCHECS ('+ko.length+') :\n  ' + ko.join('\n  '));
  console.log(err.length?'ERR '+err.slice(0,2).join(' | '):'aucune erreur JS');
  await nav.close();
})();
