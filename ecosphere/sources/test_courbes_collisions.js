const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const nav = await chromium.launch();
  const p = await (await nav.newContext({viewport:{width:1600,height:1100}})).newPage();
  const err=[]; p.on('pageerror',e=>err.push(String(e)));
  await p.goto('file://'+path.resolve(process.argv[2]),{waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_COURBES,{timeout:180000});
  await p.evaluate(()=>window.showPg('graphs'));
  await p.waitForSelector('#pg-graphs .cb-vign',{timeout:30000});
  const ids = await p.evaluate(()=>window.__ECO_COURBES.fiches.map(f=>f.id));
  const pb = [];
  for (const id of ids) {
    await p.evaluate(i=>window.__ECO_COURBES.ouvrir(i), id);
    await p.waitForSelector('#cb-fig svg',{timeout:15000});
    const nv = await p.evaluate(()=>{
      const f=window.__ECO_COURBES.fiches.filter(x=>x.id===window.__ECO_COURBES.etat().id)[0];
      return f.variantes ? f.variantes.length : 1;});
    for (let v=0; v<nv; v++) {
      if (nv>1) { await p.selectOption('#cb-sel-var', String(v)); await p.waitForTimeout(90); }
      let k=0;
      while (true) {
        await p.waitForTimeout(40);
        const r = await p.evaluate(()=>{
          const svg=document.querySelector('#cb-fig svg');
          const vb=svg.getAttribute('viewBox').split(' ').map(Number);
          const box=svg.getBoundingClientRect();
          const sx=box.width/vb[2], sy=box.height/vb[3];
          const ts=[...svg.querySelectorAll('text')].map(t=>{
            const b=t.getBoundingClientRect();
            return {t:t.textContent, x:b.left, y:b.top, w:b.width, h:b.height};
          }).filter(t=>t.t.trim() && t.w>0);
          const col=[];
          for(let i=0;i<ts.length;i++) for(let j=i+1;j<ts.length;j++){
            const a=ts[i], b=ts[j];
            const ox=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x);
            const oy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
            if(ox>6 && oy>5) col.push(a.t.slice(0,26)+' ✕ '+b.t.slice(0,26));
          }
          // débordement hors du cadre
          const deb=ts.filter(t=>t.x<box.left-2 || t.x+t.w>box.right+2 ||
                                 t.y<box.top-2 || t.y+t.h>box.bottom+2)
                      .map(t=>t.t.slice(0,26));
          return {col, deb};
        });
        if (r.col.length) pb.push(id+' v'+v+' é'+(k+1)+' CHEVAUCHE : '+r.col.join(' · '));
        if (r.deb.length) pb.push(id+' v'+v+' é'+(k+1)+' DÉBORDE : '+r.deb.join(' · '));
        const fin = await p.evaluate(()=>document.querySelector('#cb-suiv').disabled);
        if (fin) break;
        await p.locator('#cb-suiv').click(); k++;
        if (k>14) break;
      }
      if (nv>1) { await p.locator('#cb-raz2').click(); await p.waitForTimeout(80); }
    }
  }
  console.log(pb.length ? pb.join('\n') : 'aucun chevauchement de texte');
  console.log('—', pb.length, 'signalements ·', err.length?('ERR '+err[0]):'aucune erreur JS');
  await nav.close();
})();
