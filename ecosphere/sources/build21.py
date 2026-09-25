# -*- coding: utf-8 -*-
import json
cours   = open('ch21_cours.html').read()
cours   = '\n'.join(l.lstrip() for l in cours.split('\n') if l.strip())
notions = json.load(open('ch21_notions.json'))
quiz    = json.load(open('ch21_quiz.json'))
subjects= json.load(open('ch21_subjects.json'))
extras  = json.load(open('ch21_extras.json'))

KEY   = 21
LABEL = "Deuxième année — Chapitre 1"
TITLE = "Mondialisation, ouverture internationale et déséquilibres extérieurs"
SUB   = ("Dimensions de l’ouverture · Michalet · asymétries et termes de l’échange · courbe de l’éléphant · "
         "balance des paiements · commerce en valeur ajoutée · chaînes de valeur · histoire des mondialisations")

TOPICS = {
 'ouverture':['ouverture','commercial','productive','financière','devise','change'],
 'mondialisation':['mondialisation','michalet','hypermondialisation','globalisation','interdépendance'],
 'asymétries':['prebisch','termes de l’échange','centre','périphérie','échange inégal','extractive','malédiction'],
 'inégalités':['milanovic','éléphant','inégalit','gagnant','perdant'],
 'balance des paiements':['balance','compte courant','compte financier','solde','déficit','excédent','épargne'],
 'mesure':['taux d’ouverture','valeur ajoutée','double comptage','indicateur','intermédiaire'],
 'chaînes de valeur':['dipp','chaîne de valeur','fragmentation','relocalisation','dépendance','vulnérabilit'],
 'histoire':['première mondialisation','entre-deux-guerres','étalon-or','1914','1945','slowbalization','démondialisation','protectionnisme'],
}
def tags_for(q):
    txt=((q.get('q') or '')+' '+(q.get('exp') or '')+' '+' '.join(q.get('opts') or [])).lower()
    t={'questions générales','deuxième année','chapitre 1 (2e année)'}
    t.add({'qcm':'qcm','vf':'vrai/faux','open':'question ouverte'}[q['type']])
    for tag,kws in TOPICS.items():
        if any(k in txt for k in kws): t.add(tag)
    return sorted(t)

notions_c=[[n['term'],n['def']] for n in notions]
quiz_c=[]
for q in quiz:
    o=dict(q)
    if o['type']=='open' and o.get('exp')==o.get('sample'): o.pop('exp',None)
    quiz_c.append(o)

CARD = (f'<div class="cc cc-annee2" data-c="{KEY}" onclick="openCh({KEY})">'
        '<div class="cc-num">// DEUXIÈME ANNÉE · CHAPITRE 01</div>'
        f'<div class="cc-title">{TITLE}</div>'
        '<div class="cc-desc">Les trois dimensions de l’ouverture, les configurations de Michalet, les asymétries '
        'centre / périphérie, la courbe de l’éléphant, la balance des paiements, le commerce en valeur ajoutée, '
        'les chaînes de valeur mondiales et l’histoire des mondialisations.</div>'
        '<div class="cc-tags"><span class="tag tag-a2">2ᵉ année</span><span class="tag">Mondialisation</span>'
        '<span class="tag">Balance des paiements</span><span class="tag">Inégalités</span></div>'
        f'<div class="cc-btns"><button class="btn btn-p" onclick="event.stopPropagation();openCh({KEY})">📖 Cours</button>'
        f'<button class="btn btn-g" onclick="event.stopPropagation();startQuiz({KEY})">🎯 Quiz IA</button></div></div>')

D = dict(key=KEY, label=LABEL, title=TITLE, sub=SUB, cours=cours, notions=notions_c,
         methode=extras['methode'], ctx=extras['ctx'], map=extras['map'],
         quiz=quiz_c, topics=TOPICS, subjects=subjects, card=CARD)

js = """
<style id="eco-annee2-ch1-style">
.cc[data-c="21"]::before{background:linear-gradient(90deg,#6af7f7,#7c6af7)}
.tag-a2{background:rgba(106,247,247,.16)!important;color:#6af7f7!important;border:1px solid rgba(106,247,247,.35)!important}
.ch21-premium-course{padding:18px!important}
.ch21-premium-course h2{font-size:1.05rem!important;line-height:1.35}
.ch21-premium-course p strong{color:var(--txt)}
.a2-badge{display:inline-block;font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:9px;background:rgba(106,247,247,.16);color:#6af7f7;border:1px solid rgba(106,247,247,.35);margin-right:7px;vertical-align:middle}
</style>
<script id="eco-annee2-ch1-v174">
(function(){
'use strict';
if(window.__ECO_A2_CH1) return;
window.__ECO_A2_CH1 = true;
var D = %s;
var K = String(D.key);
D.notions = D.notions.map(function(n){ return {term:n[0], def:n[1], type:'definition'}; });
D.quiz.forEach(function(q){ if(q.type==='open' && !q.exp) q.exp = q.sample; });
function advTags(q){
  var txt = ((q.q||'')+' '+(q.exp||'')+' '+((q.opts||[]).join(' '))).toLowerCase();
  var t = {'questions générales':1,'deuxième année':1};
  t[{qcm:'qcm', vf:'vrai/faux', open:'question ouverte'}[q.type]] = 1;
  Object.keys(D.topics).forEach(function(tag){
    if(D.topics[tag].some(function(k){ return txt.indexOf(k) >= 0; })) t[tag] = 1;
  });
  return Object.keys(t).sort();
}
D.adv = D.quiz.map(function(q){
  var o = {type:q.type, q:q.q, exp:q.exp, ch:D.key, id:q.id, source:'principale586', tags:advTags(q)};
  if(q.type==='qcm'){ o.opts = q.opts; o.ans = q.ans; }
  else if(q.type==='vf'){ o.opts = ['Vrai','Faux']; o.ans = q.ans ? 0 : 1; }
  else { o.opts = []; o.sample = q.sample; }
  return o;
});

/* registre des libelles d'annee : extensible aux prochains chapitres de 2e annee */
window.ECO_CHAP_LABEL = window.ECO_CHAP_LABEL || {};
window.ECO_CHAP_LABEL[K] = D.label;

function applyContent(){
  try{ if(typeof CH_CONTENT !== 'undefined' && !CH_CONTENT[D.key]){
    CH_CONTENT[D.key] = {title:D.title, sub:D.sub, cours:D.cours, notions:D.notions, methode:D.methode, annee:2, numAnnee:1};
  } }catch(e){}
  try{ if(typeof CH_CONTEXT !== 'undefined' && !CH_CONTEXT[D.key]) CH_CONTEXT[D.key] = D.ctx; }catch(e){}
  try{ if(typeof MAP_DATA   !== 'undefined' && !MAP_DATA[D.key])   MAP_DATA[D.key]   = D.map; }catch(e){}
  try{
    if(typeof SUBJECTS_BANK_PREMIUM !== 'undefined' && !SUBJECTS_BANK_PREMIUM.some(function(s){return s.chapter===D.key;})){
      D.subjects.forEach(function(s){ SUBJECTS_BANK_PREMIUM.push(s); });
    }
  }catch(e){}
  try{ var QB = window.ECOSPHERE_QUESTION_BANK; if(QB && !QB[K]) QB[K] = D.quiz; }catch(e){}
  try{
    var AB = window.__ECO_ADV_ALL_BANK;
    if(AB && Array.isArray(AB) && !AB.some(function(q){return q.ch===D.key;})){
      D.adv.forEach(function(q){ AB.push(q); });
    }
  }catch(e){}
}
applyContent();

/* ---- affichage : remplacer partout "Chapitre 21" par le libelle d'annee ---- */
var RE = new RegExp('\\\\bchapitres?\\\\s*0*' + D.key + '\\\\b', 'gi');
function relabelNode(root){
  if(!root) return;
  var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), n;
  var cibles = [];
  while((n = w.nextNode())) if(RE.test(n.nodeValue)) cibles.push(n);
  cibles.forEach(function(t){
    t.nodeValue = t.nodeValue.replace(RE, function(m){
      return m === m.toUpperCase() ? D.label.toUpperCase() : D.label;
    });
  });
}
var enCours = false;
function relabelAll(){
  if(enCours) return;
  enCours = true;
  try{ relabelAllInner(); } finally { enCours = false; }
}
function relabelAllInner(){
  ['#pg-chapter','#pg-quiz','#pg-maps','#pg-subjects','#pg-search','#pg-home','#pg-fc','#pg-prog','#pg-graphs']
    .forEach(function(sel){ try{ relabelNode(document.querySelector(sel)); }catch(e){} });
}
/* surveiller les zones qui se redessinent (quiz, cours, recherche, cartes, sujets) */
function surveiller(){
  if(!window.MutationObserver) return;
  ['#pg-quiz','#pg-chapter','#pg-search','#pg-maps','#pg-subjects','#pg-home','#pg-prog','#pg-fc']
    .forEach(function(sel){
      var el = document.querySelector(sel);
      if(!el || el.__a2obs) return;
      el.__a2obs = true;
      var mo = new MutationObserver(function(){
        if(enCours) return;
        enCours = true;
        try{ relabelNode(el); } finally { enCours = false; }
      });
      try{ mo.observe(el, {childList:true, subtree:true, characterData:true}); }catch(e){}
    });
}

/* le cours du chapitre : on prefixe l'en-tete d'un badge d'annee */
function badgeChapitre(){
  var h = document.querySelector('#pg-chapter .ch-title, #pg-chapter h1, #pg-chapter .chapter-title');
  if(h && !h.querySelector('.a2-badge') && RE.test(h.textContent + ' ')){
    h.insertAdjacentHTML('afterbegin', '<span class="a2-badge">2ᵉ année</span>');
  }
}

function addCard(){
  var grid = document.querySelector('.cg');
  if(grid && !grid.querySelector('[data-c="' + K + '"]')) grid.insertAdjacentHTML('beforeend', D.card);
}
function addQuizButton(){
  var grid = document.querySelector('.quiz-options-grid');
  if(grid && grid.innerText.indexOf('2ᵉ année') === -1){
    var html = '<button class="qo-btn" onclick="startQuiz(' + D.key + ')">2ᵉ année — Ch. 1<span>Mondialisation</span></button>';
    var btns = [].slice.call(grid.querySelectorAll('.qo-btn'));
    var last = btns.filter(function(b){ return /Chapitre \\d+/.test(b.textContent); }).pop();
    if(last) last.insertAdjacentHTML('afterend', html);
    else grid.insertAdjacentHTML('beforeend', html);
  }
}
function extendSubjects(){
  var tabs = document.getElementById('subjTabsPremium');
  if(tabs && tabs.textContent.indexOf('2ᵉ année') === -1){
    tabs.insertAdjacentHTML('beforeend',
      '<button class="subj-tab' + (window.currentSubjChapter===D.key?' on':'') +
      '" onclick="setSubjectChapterPremium(' + D.key + ')">2ᵉ année — Ch. 1</button>');
  }
  var grid = document.getElementById('subjChaptersPremium');
  if(grid && grid.children.length && !grid.querySelector('[data-a2ch1]')){
    grid.insertAdjacentHTML('beforeend',
      '<div class="subj-ch-card" data-a2ch1="1" onclick="setSubjectChapterPremium(' + D.key + ')">' +
      '<div class="subj-ch-num"><span class="a2-badge">2ᵉ année</span>Chapitre 1</div>' +
      '<div class="subj-ch-title">Sujets corrigés</div>' +
      '<div class="subj-ch-count">' + D.subjects.length + ' dissertations corrigées</div></div>');
  }
}
if(typeof window.renderSubjectsPremium === 'function'){
  var oldRSP = window.renderSubjectsPremium;
  window.renderSubjectsPremium = function(){
    var r = oldRSP.apply(this, arguments);
    try{ extendSubjects(); relabelNode(document.querySelector('#pg-subjects')); }catch(e){}
    return r;
  };
}
if(typeof window.openCh === 'function'){
  var oldOpenCh = window.openCh;
  window.openCh = function(n){
    var r = oldOpenCh.apply(this, arguments);
    setTimeout(function(){
      try{
        if(String(n) === K){
          var c = document.getElementById('sect-cours');
          if(c && (!c.innerHTML || c.innerHTML.length < 1000)) c.innerHTML = D.cours;
        }
        relabelNode(document.querySelector('#pg-chapter'));
        badgeChapitre();
      }catch(e){}
    }, 0);
    return r;
  };
}
if(typeof window.renderMaps === 'function'){
  var oldRM = window.renderMaps;
  window.renderMaps = function(){
    var r = oldRM.apply(this, arguments);
    try{ relabelNode(document.querySelector('#pg-maps')); }catch(e){}
    return r;
  };
}
if(typeof window.doSearch === 'function'){
  var oldDS = window.doSearch;
  window.doSearch = function(){
    var r = oldDS.apply(this, arguments);
    try{ relabelNode(document.getElementById('search-res')); }catch(e){}
    return r;
  };
}
if(typeof window.showPg === 'function'){
  var oldShowPg = window.showPg;
  window.showPg = function(pg){
    var r = oldShowPg.apply(this, arguments);
    try{
      if(pg==='subjects') setTimeout(extendSubjects, 0);
      if(pg==='quiz')     setTimeout(addQuizButton, 0);
      if(pg==='home')     setTimeout(addCard, 0);
      setTimeout(relabelAll, 90);
    }catch(e){}
    return r;
  };
}
function refreshIndex(){
  try{ if(typeof rebuildSearchIndex === 'function') rebuildSearchIndex(); }catch(e){}
  try{ if(typeof buildFC === 'function') buildFC(); }catch(e){}
}
function boot(){
  applyContent(); addCard(); addQuizButton(); extendSubjects(); refreshIndex();
  surveiller(); relabelAll();
}
if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
setTimeout(boot, 800);
setTimeout(boot, 1800);
setTimeout(function(){ relabelAll(); }, 3000);
setTimeout(function(){ relabelAll(); }, 4500);
})();
</script>
""" % json.dumps(D, ensure_ascii=False)

head, sep, tail = js.partition('var D = ')
de = tail.index('\n'); data, rest = tail[:de], tail[de:]
def strip_js(t):
    out=[]
    for line in t.split('\n'):
        st=line.strip()
        if not st: continue
        if st.startswith('/*') and st.endswith('*/'): continue
        out.append(line)
    return '\n'.join(out)
js = strip_js(head) + sep + data + strip_js(rest)
open('ch21_patch.html','w').write(js)
print('bloc 2e année ch.1 :', f"{len(js):,}".replace(',',' '), 'caractères')
