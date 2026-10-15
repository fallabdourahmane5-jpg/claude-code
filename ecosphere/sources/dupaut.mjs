import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.argv[2]);
await p.waitForTimeout(13000);
const noms = ['Montesquieu','Marx','Luttwak','Baldwin','Fontagné','Milanovic','Orain','Kesslassy','Rodrigues','Kindleberger','Krugman','Balassa','Viner','Lawrence','Bhagwati','Rodrik','Jean','Bolhuis','Bensidoun','Péron','Ricardo','HOS','Heckscher','Ohlin','Samuelson','Nash','Roosevelt'];
console.log(JSON.stringify(await p.evaluate((noms)=>{
  const out = {};
  noms.forEach(n => {
    const h = AUTHORS.filter(a => a.name.toLowerCase().includes(n.toLowerCase()))
      .map(a => a.name + ' [ch ' + JSON.stringify(a.chapters||a.ch) + ']');
    if (h.length) out[n] = h;
  });
  return out;
}, noms), null, 1));
await b.close();
