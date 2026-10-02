# -*- coding: utf-8 -*-
import io, json, re

# --- tags thematiques, deduits du contenu de chaque question ---
TAGS = [
 ('fmn',            ['multinational','fmn','cnuced','filiale','affili','portefeuille','greenfield','fusion-acquisition','maison mère']),
 ('ide',            ['ide','investissement direct','horizontal','vertical','implantation']),
 ('chaînes de valeur',['chaîne de valeur','cvm','dipp','dégroupage','fragmentation','sourire','shih','baldwin','assemblage','made in','valeur ajoutée domestique']),
 ('gouvernance',    ['shareholder','stakeholder','actionnaire','partie prenante','vigilance','donneur d','coase','agence']),
 ('dumping',        ['dumping','omc','ord','différends','sous-évalu']),
 ('désindustrialisation',['désindustrialisation','délocalisation','externalisation','fourastié','déversement','engel','emploi industriel','tertiaris']),
 ('choc chinois',   ['chinois','chine','autor','china syndrome','malgouyres','importations']),
 ('mondialisation', ['mondialisation','gagnants','perdants','fontagné','giraud','nomade','sédentaire','caddie','feuille de paye','mouhoud','compensation']),
 ('compétitivité',  ['compétitivité','compétitif','coût unitaire','hors-prix','krugman','productivité','cir','cice','marge']),
 ('attractivité',   ['attractivité','michalet','séduction','fiscal','prisonnier','ocde','pilier','15 %','optimisation']),
 ('politique industrielle',['politique industrielle','horizontale','verticale','subvention','aide','colbertisme','champion','concurrence']),
 ('innovation',     ['innovation','r&d','recherche','capital-risque','mazzucato','darpa','aghion','entrepreneur','schumpét','externalité']),
 ('protectionnisme',['protectionnisme','list','industrie naissante','droits de douane','éducateur']),
 ('souveraineté',   ['souveraineté','dépendance','critique','filtrage','géoéconomie','lithium','relocalis','autosuffisance']),
 ('transition écologique',['verdissement','écologique','batterie','véhicule électrique','byd','catl','transition']),
]
def tags_de(q):
    t = (q['q'] + ' ' + ' '.join(q.get('opts') or []) + ' ' + q.get('exp','')).lower()
    out = [nom for nom, mots in TAGS if any(m in t for m in mots)]
    return out or ['fmn']

js = r"""
<script id="eco-ch22-correctifs">
(function(){
'use strict';
if(window.__ECO_CH22_FIX) return;
window.__ECO_CH22_FIX = true;

var TAGS = __TAGS__;
var N = 22;

/* --- 1. Tags thématiques des questions du chapitre 22 ---------------------
   Elles n'avaient que deux tags d'identification ; les autres chapitres en
   proposent une quinzaine, par thème. */
function poserTags(){
  var A = window.__ECO_ADV_ALL_BANK;
  if(!A) return false;
  var n = 0;
  A.forEach(function(q){
    if(Number(q.ch) !== N) return;
    var t = TAGS[q.id];
    if(!t) return;
    var base = ['deuxième année', 'chapitre 22'];
    var voulu = base.concat(t);
    if((q.tags || []).length === voulu.length) return;
    q.tags = voulu;
    n++;
  });
  return n > 0;
}

/* --- 2. Onglet et carte du chapitre 22 dans la section Sujets ---------------
   Le rendu de base construit les chapitres 1 à 8 ; chaque chapitre ajouté
   depuis complète la liste lui-même. Le chapitre 22 ne le faisait pas. */
function nbSujets(){
  try{
    return (SUBJECTS_BANK_PREMIUM || []).filter(function(s){ return Number(s.chapter) === N; }).length;
  }catch(e){ return 0; }
}
function poserSujets(){
  var n = nbSujets();
  if(!n) return;
  var tabs = document.getElementById('subjTabsPremium');
  if(tabs && !tabs.querySelector('[data-ch22]')){
    tabs.insertAdjacentHTML('beforeend',
      '<button class="subj-tab" data-ch22="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '2ᵉ année — Ch. 2</button>');
  }
  var grid = document.getElementById('subjChaptersPremium');
  if(grid && grid.children.length && !grid.querySelector('[data-ch22]')){
    grid.insertAdjacentHTML('beforeend',
      '<div class="subj-ch-card" data-ch22="1" onclick="setSubjectChapterPremium(' + N + ')">' +
      '<div class="subj-ch-num">2ᵉ année — Chapitre 2</div>' +
      '<div class="subj-ch-title">Sujets corrigés</div>' +
      '<div class="subj-ch-count">' + n + ' dissertations corrigées</div></div>');
  }
  /* marquer l'onglet actif */
  try{
    var actif = (window.currentSubjChapter === N);
    var b = tabs && tabs.querySelector('[data-ch22]');
    if(b) b.classList.toggle('on', !!actif);
  }catch(e){}
}

function tout(){ try{ poserTags(); poserSujets(); }catch(e){} }

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tout);
else tout();
[300, 900, 2000, 3500, 6000].forEach(function(t){ setTimeout(tout, t); });

if(typeof window.showPg === 'function'){
  var old = window.showPg;
  window.showPg = function(pg){
    var r = old.apply(this, arguments);
    if(pg === 'subjects' || pg === 'quiz'){
      setTimeout(tout, 50); setTimeout(tout, 300);
    }
    return r;
  };
}
if(typeof window.setSubjectChapterPremium === 'function'){
  var oldS = window.setSubjectChapterPremium;
  window.setSubjectChapterPremium = function(){
    var r = oldS.apply(this, arguments);
    setTimeout(tout, 40);
    return r;
  };
}
try{
  var z = document.getElementById('pg-subjects');
  if(z) new MutationObserver(function(){ poserSujets(); }).observe(z, {childList:true, subtree:true});
}catch(e){}
})();
</script>
"""

quiz_tags = {}
src = io.open('app_v185.html', encoding='utf-8').read()
m = re.search(r'<script id="eco-chapitre-22">\s*\(function\(\)\{\s*\'use strict\';.*?var D = (\{.*?\});\s*var N = 22;', src, re.S)
assert m, 'charge utile du chapitre 22 introuvable'
D = json.loads(m.group(1))
for q in D['quiz']:
    quiz_tags[q['id']] = tags_de(q)

js = js.replace('__TAGS__', json.dumps(quiz_tags, ensure_ascii=False, separators=(',',':')))
io.open('fix22_patch.html','w',encoding='utf-8').write(js)
i = src.rfind('</body>')
io.open('app_v186.html','w',encoding='utf-8').write(src[:i] + js + src[i:])

from collections import Counter
c = Counter(t for v in quiz_tags.values() for t in v)
print('questions taguées :', len(quiz_tags))
print('tags distincts    :', len(c))
for k,v in c.most_common(): print('   %-26s %d' % (k, v))
print('\napp_v186.html écrit')
