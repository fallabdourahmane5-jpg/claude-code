import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://'+process.cwd()+'/app_v180.html'); await p.waitForTimeout(4000);
// quiz classique chapitre 21
await p.evaluate(()=>{ window.showPg('quiz'); window.startQuiz(21); });
await p.waitForTimeout(900);
let t = await p.evaluate(()=>document.getElementById('pg-quiz').innerText);
console.log('=== startQuiz(21), extrait ===');
console.log(t.split('\n').slice(0,10).join('\n'));
console.log('\nlignes contenant 21 / 2e annee :');
console.log(JSON.stringify(t.split('\n').filter(l=>/21|2.{0,3}\s*ann|Deuxi/i.test(l)).slice(0,8)));
await b.close();
