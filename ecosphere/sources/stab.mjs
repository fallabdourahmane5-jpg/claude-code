import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const f of [process.argv[2], process.argv[3], process.argv[2], process.argv[3]]) {
  const p = await b.newPage({viewport:{width:1400,height:950}});
  await p.goto('file://' + f); await p.waitForTimeout(16000);
  console.log(f.split('/').pop(), JSON.stringify(await p.evaluate(()=>({
    fiches: FC_DATA.length, recherche: typeof SEARCH_INDEX!=='undefined'?SEARCH_INDEX.length:null,
    auteurs: AUTHORS.length, sujets: SUBJECTS_BANK_PREMIUM.length}))));
  await p.close();
}
await b.close();
