const { chromium } = require('playwright'); const path = require('path');
const F = process.argv[2] || 'app_v227.html';
(async () => {
  const nav = await chromium.launch();
  const ctx = await nav.newContext({viewport:{width:1440,height:950}, deviceScaleFactor:1});
  const p = await ctx.newPage(); const err=[];
  p.on('pageerror', e=>err.push(String(e).slice(0,160)));
  await p.goto('file://'+path.resolve(F),{waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_FC,{timeout:180000});
  await p.evaluate(()=>window.showPg('fc'));
  await p.waitForSelector('#pg-fc .fx-cpt',{timeout:30000});

  const G = n => p.evaluate(s=>{try{return eval(s)}catch(e){return 'ERR '+e.message}}, n);
  console.log('ancienne banque FC_DATA :', await G('FC_DATA.length'),
              '· toutes marquées fc227 :', await G('FC_DATA.every(c=>c.fc227)'));
  console.log('push scellé :', await G('(function(){var n=FC_DATA.length;FC_DATA.push({term:"x",def:"y"});return FC_DATA.length===n})()'));
  console.log('générateur neutralisé :', await G('buildAllFlashcards().length'));
  console.log('cartes :', await G('__ECO_FC.cartes.length'));

  // accueil
  const acc = await p.evaluate(()=>({
    compteurs:[...document.querySelectorAll('#pg-fc .fx-cc')].map(x=>x.querySelector('.n').textContent+' '+x.querySelector('.l').textContent),
    boutons:[...document.querySelectorAll('#pg-fc .fx-b')].map(b=>b.querySelector('.t').textContent+' | '+b.querySelector('.s').textContent+(b.hasAttribute('disabled')?' [off]':'')),
    chapitres:document.querySelectorAll('#pg-fc .fx-ch').length}));
  console.log('accueil :', JSON.stringify(acc,null,0));

  // séance de découverte
  await p.click('#pg-fc .fx-b[data-m=new]');
  await p.waitForSelector('#pg-fc .fx-rev',{timeout:10000});
  const q1 = await p.textContent('#pg-fc .fx-kq');
  console.log('1re carte :', q1.slice(0,70), '| réponse visible avant révélation :',
    await p.evaluate(()=>!!document.querySelector('#pg-fc .fx-ka')));
  await p.keyboard.press('Space');
  await p.waitForSelector('#pg-fc .fx-ka',{timeout:5000});
  console.log('réponse :', (await p.textContent('#pg-fc .fx-kr')).slice(0,70));
  console.log('notes proposées :', await p.evaluate(()=>[...document.querySelectorAll('#pg-fc .fx-n')].map(b=>b.querySelector('.nl').textContent+' '+b.querySelector('.nd').textContent)));
  // noter : 3 maîtrisée, 1 à revoir, 2 difficile
  await p.keyboard.press('3'); await p.waitForTimeout(260);
  const q2 = await p.textContent('#pg-fc .fx-kq');
  console.log('carte suivante différente :', q1!==q2, '| progression :', await p.textContent('#pg-fc .pr'));
  await p.keyboard.press('Space'); await p.waitForTimeout(120);
  await p.keyboard.press('1'); await p.waitForTimeout(260);
  console.log('file après « à revoir » :', await G('__ECO_FC.seance().file.length'),
    '| carte replacée plus loin :', await G('__ECO_FC.seance().file.indexOf(__ECO_FC.seance().file[1])'));
  const rep = await G('(function(){var s=__ECO_FC.seance();var id=Object.keys(s.faits).find(k=>s.faits[k]===1);return s.file.slice(s.i).indexOf(id);})()');
  console.log('écart avant réapparition :', rep);

  // persistance
  const etats = await G('JSON.stringify(Object.keys(__ECO_FC.etats).length)');
  await p.reload({waitUntil:'domcontentloaded',timeout:180000});
  await p.waitForFunction(()=>!!window.__ECO_FC,{timeout:180000});
  await p.evaluate(()=>window.showPg('fc'));
  await p.waitForSelector('#pg-fc .fx-cpt',{timeout:30000});
  console.log('après rechargement — états conservés :', await G('Object.keys(__ECO_FC.etats).length'), '(avant :', etats+')');
  console.log('séance reprise :', await p.evaluate(()=>!!document.querySelector('#pg-fc .fx-reprise')));
  console.log('aucune carte générée :', await G('FC_DATA.every(c=>c.fc227)'), '| total', await G('FC_DATA.length'));

  // bibliothèque
  await p.click('#pg-fc .fx-seg button[data-v=biblio]');
  await p.waitForSelector('#pg-fc .fx-it',{timeout:10000});
  console.log('bibliothèque :', await p.textContent('#pg-fc .fx-nb'));
  await p.fill('#fx-rq','keynes');
  await p.waitForTimeout(400);
  console.log('recherche « keynes » :', await p.textContent('#pg-fc .fx-nb'));
  await p.fill('#fx-rq','plihon');
  await p.waitForTimeout(400);
  console.log('recherche « plihon » :', await p.textContent('#pg-fc .fx-nb'),
    '|', (await p.textContent('#pg-fc .fx-it .qq')).slice(0,60));
  console.log('ERREURS JS :', err.length?err:'aucune');
  await nav.close();
})();
