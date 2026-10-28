# -*- coding: utf-8 -*-
"""Remplace la section « Visualisations stratégiques ».

Les 19 affiches en images base64 (6,2 Mo) sont retirées et remplacées par des
visualisations interactives : le texte reste du HTML, donc net à tout niveau de
zoom, et chaque élément s'ouvre sur son contenu détaillé.
"""
import json
import sys

CSS = r"""
<style id="v215-visu-css">
#pg-visualisations{--vzA:#7c5cff;--vzB:#00d4ff;--vzC:#6af7c4;--vzD:#ffd250;--vzE:#ff7d9c}
#pg-visualisations .vz{max-width:1320px;margin:0 auto;padding:30px 20px 80px}
/* une scène ouverte prend toute la largeur disponible : c'est elle qui
   porte l'information, l'index garde une colonne de lecture confortable. */
#pg-visualisations .vz.scene{max-width:1720px}
#pg-visualisations .vz-hero{border:1px solid var(--bdr);border-radius:26px;padding:28px 30px;
  background:linear-gradient(135deg,rgba(124,92,255,.16),rgba(0,212,255,.07) 55%,rgba(106,247,196,.05));margin-bottom:22px}
#pg-visualisations .vz-kick{color:var(--acc2);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:900;margin-bottom:9px}
#pg-visualisations .vz-hero h1{font-family:'Playfair Display',serif;font-size:2.2rem;line-height:1.06;margin:0 0 11px}
#pg-visualisations .vz-hero p{margin:0;color:var(--txt2);line-height:1.72;max-width:900px;font-size:.93rem}
#pg-visualisations .vz-hero-st{display:flex;gap:18px;flex-wrap:wrap;margin-top:16px}
#pg-visualisations .vz-hero-st div{font-size:.78rem;color:var(--txt3)}
#pg-visualisations .vz-hero-st b{display:block;font-size:1.3rem;color:var(--txt);font-weight:900;line-height:1.2}

#pg-visualisations .vz-filters{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:18px}
#pg-visualisations .vz-chip{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:999px;
  padding:7px 13px;font-size:.78rem;cursor:pointer;font-family:inherit}
#pg-visualisations .vz-chip:hover{border-color:rgba(124,92,255,.5);color:var(--txt)}
#pg-visualisations .vz-chip.on{background:rgba(124,92,255,.16);border-color:rgba(124,92,255,.55);color:#fff}
#pg-visualisations .vz-q{flex:1;min-width:210px;background:var(--s2);border:1px solid var(--bdr);border-radius:12px;
  padding:9px 13px;color:var(--txt);font-family:inherit;font-size:.86rem}

#pg-visualisations .vz-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:18px}
#pg-visualisations .vz-card{background:var(--s1);border:1px solid var(--bdr);border-radius:20px;overflow:hidden;
  cursor:pointer;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease;text-align:left;
  font-family:inherit;color:inherit;padding:0;display:flex;flex-direction:column}
#pg-visualisations .vz-card:hover{transform:translateY(-3px);border-color:rgba(124,92,255,.45);box-shadow:0 18px 40px rgba(0,0,0,.26)}
#pg-visualisations .vz-card-top{padding:15px 16px 0}
#pg-visualisations .vz-card-kick{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--txt3);font-weight:800;margin-bottom:6px}
#pg-visualisations .vz-card h3{font-family:'Playfair Display',serif;font-size:1.1rem;line-height:1.25;margin:0 0 8px}
#pg-visualisations .vz-card p{margin:0;color:var(--txt2);font-size:.82rem;line-height:1.6}
#pg-visualisations .vz-prev{margin:13px 0 0;background:rgba(255,255,255,.015);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr)}
#pg-visualisations .vz-prev svg{display:block;width:100%;height:92px}
#pg-visualisations .vz-card-foot{padding:11px 16px 15px;display:flex;gap:7px;flex-wrap:wrap;align-items:center;margin-top:auto}
#pg-visualisations .vz-tag{font-size:.68rem;padding:3px 8px;border-radius:999px;background:var(--s2);border:1px solid var(--bdr);color:var(--txt3)}
#pg-visualisations .vz-tag.t{background:rgba(0,212,255,.09);border-color:rgba(0,212,255,.26);color:var(--vzB)}

/* ---------------------------------------------------------------- scène */
#pg-visualisations .vz-stage-top{display:flex;gap:12px;align-items:flex-start;flex-wrap:wrap;margin-bottom:12px}
#pg-visualisations .vz-stage-top h2{font-family:'Playfair Display',serif;font-size:1.5rem;margin:0 0 6px;line-height:1.14}
#pg-visualisations .vz-stage-top p{margin:0;color:var(--txt2);font-size:.86rem;line-height:1.65;max-width:820px}
#pg-visualisations .vz-back{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:10px;
  padding:8px 13px;cursor:pointer;font-family:inherit;font-size:.82rem;white-space:nowrap}
#pg-visualisations .vz-back:hover{color:#fff;border-color:rgba(124,92,255,.5)}

#pg-visualisations .vz-read{display:none;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px;margin:12px 0 0}
#pg-visualisations .vz-read.on{display:grid}
#pg-visualisations .vz-read div{background:var(--s2);border:1px solid var(--bdr);border-radius:12px;padding:11px 13px}
#pg-visualisations .vz-read b{display:block;font-size:.76rem;color:var(--vzB);margin-bottom:5px;letter-spacing:.03em}
#pg-visualisations .vz-read span{font-size:.8rem;color:var(--txt2);line-height:1.6}

#pg-visualisations .vz-tools{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-bottom:9px}
#pg-visualisations .vz-tool{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:9px;
  min-width:36px;height:34px;padding:0 11px;cursor:pointer;font-family:inherit;font-size:.82rem;font-weight:700}
#pg-visualisations .vz-tool:hover{color:#fff;border-color:rgba(124,92,255,.5)}
#pg-visualisations .vz-tool.on{background:rgba(124,92,255,.18);border-color:rgba(124,92,255,.55);color:#fff}
#pg-visualisations .vz-zoomval{font-size:.76rem;color:var(--txt3);min-width:52px;text-align:center}
#pg-visualisations .vz-hint{font-size:.74rem;color:var(--txt3);margin-left:auto}

#pg-visualisations .vz-view{position:relative;border:1px solid var(--bdr);border-radius:18px;overflow:hidden;
  background:
    radial-gradient(900px 420px at 18% 8%,rgba(124,92,255,.1),transparent 70%),
    radial-gradient(760px 420px at 86% 92%,rgba(0,212,255,.07),transparent 70%),
    var(--s1);
  height:clamp(430px,calc(100vh - 212px),900px);touch-action:none;cursor:grab;contain:paint}
/* plein écran de la scène : la vue d'ensemble occupe tout l'écran, ce qui
   permet de lire la structure sans rien réduire. */
#pg-visualisations.plein .vz{max-width:none;padding:0}
#pg-visualisations.plein #vzStage{position:fixed;inset:0;z-index:9100;background:var(--bg,#07080d);
  padding:12px 16px;overflow:auto}
#pg-visualisations.plein .vz-view{height:calc(100vh - 118px);border-radius:14px}
#pg-visualisations.plein .vz-stage-top{margin-bottom:8px}
#pg-visualisations.plein .vz-stage-top h2{font-size:1.2rem}
#pg-visualisations.plein .vz-kick{display:none}
#pg-visualisations .vz-view.drag{cursor:grabbing}
#pg-visualisations .vz-world{position:absolute;left:0;top:0;transform-origin:0 0}
#pg-visualisations .vz-edges{position:absolute;left:0;top:0;overflow:visible;pointer-events:none}

#pg-visualisations .vz-node{position:absolute;box-sizing:border-box;text-align:left;font-family:inherit;
  white-space:normal;overflow-wrap:break-word;overflow:hidden;
  background:var(--s2);border:1px solid var(--bdr);border-radius:14px;padding:11px 13px;cursor:pointer;color:var(--txt);
  box-shadow:0 7px 20px rgba(0,0,0,.26);transition:border-color .16s ease,box-shadow .16s ease}
#pg-visualisations .vz-node:hover{border-color:rgba(124,92,255,.6);box-shadow:0 10px 28px rgba(0,0,0,.4)}
#pg-visualisations .vz-node.sel{border-color:var(--vzA);box-shadow:0 0 0 2px rgba(124,92,255,.35),0 10px 28px rgba(0,0,0,.4)}
#pg-visualisations .vz-node .vzt{font-weight:800;font-size:.9rem;line-height:1.3;margin-bottom:5px;
  transition:font-size .18s ease}
#pg-visualisations .vz-node .vzr{font-size:.78rem;color:var(--txt2);line-height:1.52;
  display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
#pg-visualisations .vz-node .vzb{display:flex;gap:5px;flex-wrap:wrap;margin-top:8px}
/* vue d'ensemble : en dessous d'un certain zoom, seuls les titres restent,
   agrandis, pour que la structure du thème se lise d'un coup d'œil. */
#pg-visualisations .vz-world.loin .vz-node{display:flex;flex-direction:column;justify-content:center}
#pg-visualisations .vz-world.loin .vz-node .vzr,
#pg-visualisations .vz-world.loin .vz-node .vzb{display:none}
#pg-visualisations .vz-world.loin .vz-node .vzk{font-size:1.02rem;margin-bottom:10px;letter-spacing:.06em}
#pg-visualisations .vz-world.loin .vz-node .vzt{font-size:1.78rem;line-height:1.2;margin:0}
#pg-visualisations .vz-world.loin .vz-node.r-coeur .vzt{font-size:2.25rem}
#pg-visualisations .vz-world.loin .vz-lab{font-size:1.04rem;padding:6px 14px;max-width:244px;
  white-space:normal;line-height:1.3;border-radius:14px;border-width:2px}
#pg-visualisations .vz-node .vzb i{font-style:normal;font-size:.64rem;padding:2px 6px;border-radius:5px;
  background:rgba(255,255,255,.05);color:var(--txt3);border:1px solid rgba(255,255,255,.07)}
#pg-visualisations .vz-node .vzk{font-size:.63rem;letter-spacing:.09em;text-transform:uppercase;font-weight:900;margin-bottom:6px}
#pg-visualisations .vz-node.r-coeur{background:linear-gradient(145deg,rgba(124,92,255,.22),rgba(0,212,255,.08));border-color:rgba(124,92,255,.5)}
#pg-visualisations .vz-node.r-coeur .vzt{font-family:'Playfair Display',serif;font-size:1.06rem}
#pg-visualisations .vz-node.r-coeur .vzk{color:var(--vzA)}
#pg-visualisations .vz-node.r-pilier{border-color:rgba(0,212,255,.34);background:linear-gradient(145deg,rgba(0,212,255,.1),rgba(255,255,255,.012))}
#pg-visualisations .vz-node.r-pilier .vzk{color:var(--vzB)}
#pg-visualisations .vz-node.r-limite{border-color:rgba(255,210,80,.34);background:linear-gradient(145deg,rgba(255,210,80,.09),rgba(255,255,255,.012))}
#pg-visualisations .vz-node.r-limite .vzk{color:var(--vzD)}
#pg-visualisations .vz-node.r-debat{border-color:rgba(255,125,156,.32);background:linear-gradient(145deg,rgba(255,125,156,.09),rgba(255,255,255,.012))}
#pg-visualisations .vz-node.r-debat .vzk{color:var(--vzE)}
#pg-visualisations .vz-node.r-fait,#pg-visualisations .vz-node.r-sortie{border-color:rgba(106,247,196,.32);background:linear-gradient(145deg,rgba(106,247,196,.09),rgba(255,255,255,.012))}
#pg-visualisations .vz-node.r-fait .vzk,#pg-visualisations .vz-node.r-sortie .vzk{color:var(--vzC)}
#pg-visualisations .vz-node.dim{opacity:.26}

#pg-visualisations .vz-lab{position:absolute;box-sizing:border-box;transform:translate(-50%,-50%);
  background:rgba(12,14,22,.93);border:1px solid var(--bdr);border-radius:999px;padding:3px 9px;
  font-size:.7rem;color:var(--txt2);cursor:pointer;font-family:inherit;max-width:230px;line-height:1.35;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
#pg-visualisations .vz-lab:hover{color:#fff;border-color:rgba(124,92,255,.6);background:rgba(20,16,38,.97)}
#pg-visualisations .vz-lab.dim{opacity:.2}
#pg-visualisations .vz-lab.e-oppose{border-color:rgba(255,125,156,.45)}
#pg-visualisations .vz-lab.e-limite{border-color:rgba(255,210,80,.45)}
#pg-visualisations .vz-lab.e-renforce{border-color:rgba(106,247,196,.45)}
#pg-visualisations .vz-lab.e-mesure{border-color:rgba(0,212,255,.45)}
#pg-visualisations .vz-lab.e-conditionne{border-color:rgba(124,92,255,.45)}

#pg-visualisations .vz-band{position:absolute;box-sizing:border-box;border:1px dashed rgba(255,255,255,.1);
  border-radius:16px;pointer-events:none}
#pg-visualisations .vz-band span{position:absolute;left:16px;top:-14px;background:var(--s1);padding:3px 13px;
  font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--txt2);font-weight:800;
  border:1px solid var(--bdr);border-radius:999px;white-space:nowrap}
#pg-visualisations .vz-world.loin .vz-band span{font-size:1.18rem;padding:5px 18px;top:-22px;letter-spacing:.07em}

#pg-visualisations .vz-leg{display:flex;gap:9px;flex-wrap:wrap;margin-top:11px;font-size:.73rem;color:var(--txt3)}
#pg-visualisations .vz-leg span{display:inline-flex;align-items:center;gap:5px;background:var(--s2);
  border:1px solid var(--bdr);border-radius:999px;padding:4px 10px}
#pg-visualisations .vz-leg i{width:9px;height:9px;border-radius:3px;display:inline-block}

/* ---------------------------------------------------------------- panneau */
#vzPanel{position:fixed;top:0;right:0;width:min(560px,100%);height:100%;background:var(--s1);
  border-left:1px solid var(--bdr);box-shadow:-24px 0 60px rgba(0,0,0,.5);z-index:9200;
  transform:translateX(102%);transition:transform .28s cubic-bezier(.22,.9,.3,1);display:flex;flex-direction:column}
#vzPanel.on{transform:none}
#vzPanel .vp-top{padding:16px 18px 13px;border-bottom:1px solid var(--bdr);display:flex;gap:11px;align-items:flex-start}
#vzPanel .vp-kind{font-size:.64rem;letter-spacing:.1em;text-transform:uppercase;font-weight:900;color:var(--acc2);margin-bottom:5px}
#vzPanel .vp-top h3{font-family:'Playfair Display',serif;font-size:1.26rem;margin:0;line-height:1.22}
#vzPanel .vp-x{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:9px;width:32px;height:32px;
  cursor:pointer;font-size:.95rem;flex:0 0 auto;font-family:inherit}
#vzPanel .vp-x:hover{color:#fff}
#vzPanel .vp-acts{display:flex;gap:7px;padding:11px 18px;border-bottom:1px solid var(--bdr);flex-wrap:wrap}
#vzPanel .vp-acts button{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:9px;padding:7px 13px;font-size:.8rem;font-weight:700;cursor:pointer;font-family:inherit}
#vzPanel .vp-acts button:hover{color:#fff;border-color:rgba(124,92,255,.55)}
#vzPanel .vp-body{overflow:auto;padding:16px 18px 50px;flex:1;-webkit-overflow-scrolling:touch}
#vzPanel .vp-sec{margin-bottom:17px}
#vzPanel .vp-sec>h4{font-size:.73rem;letter-spacing:.11em;text-transform:uppercase;color:var(--txt3);
  margin:0 0 9px;padding-bottom:6px;border-bottom:1px solid var(--bdr);font-weight:900}
#vzPanel .vp-p{color:var(--txt2);font-size:.88rem;line-height:1.72;margin:0 0 9px}
#vzPanel .vp-it{background:var(--s2);border:1px solid var(--bdr);border-radius:11px;padding:11px 13px;margin-bottom:8px}
#vzPanel .vp-it b{display:block;font-size:.83rem;color:var(--txt);margin-bottom:5px;line-height:1.4}
#vzPanel .vp-it span{display:block;font-size:.83rem;color:var(--txt2);line-height:1.68}
#vzPanel .vp-it em{display:block;font-style:normal;font-size:.79rem;color:var(--txt3);line-height:1.6;margin-top:6px;
  padding-top:6px;border-top:1px dashed rgba(255,255,255,.1)}
#vzPanel .vp-it.step{border-left:2px solid rgba(0,212,255,.5)}
#vzPanel .vp-it.arg{border-left:2px solid rgba(106,247,196,.5)}
#vzPanel .vp-it.opp{border-left:2px solid rgba(255,125,156,.5)}
#vzPanel .vp-it.aut{border-left:2px solid rgba(124,92,255,.5)}
#vzPanel .vp-it.fait{border-left:2px solid rgba(255,210,80,.5)}
#vzPanel .vp-it span.vp-n{display:inline-block;min-width:19px;height:19px;line-height:19px;text-align:center;border-radius:5px;
  background:rgba(0,212,255,.14);color:var(--vzB);font-size:.68rem;font-weight:900;margin-right:7px}
#vzPanel .vp-lk{display:flex;gap:6px;flex-wrap:wrap}
#vzPanel .vp-lk button{background:var(--s2);border:1px solid var(--bdr);color:var(--txt2);border-radius:999px;
  padding:5px 11px;font-size:.76rem;cursor:pointer;font-family:inherit;text-align:left}
#vzPanel .vp-lk button:hover{color:#fff;border-color:rgba(124,92,255,.55)}
#vzPanel .vp-lk button b{color:var(--txt3);font-weight:700}
#vzPanel .vp-arrow{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin-bottom:11px}
#vzPanel .vp-arrow b{background:var(--s2);border:1px solid var(--bdr);border-radius:9px;padding:7px 11px;font-size:.84rem;font-weight:800}
#vzPanel .vp-arrow i{font-style:normal;color:var(--acc2);font-size:1.05rem}

#vzFull{position:fixed;inset:0;background:var(--bg,#07080d);z-index:9400;display:none;overflow:auto}
#vzFull.on{display:block}
#vzFull .vf-in{max-width:860px;margin:0 auto;padding:26px 22px 80px}
#vzFull .vf-top{display:flex;gap:12px;align-items:flex-start;margin-bottom:18px}
#vzFull .vf-top h2{font-family:'Playfair Display',serif;font-size:1.9rem;margin:0;line-height:1.1}
#vzFull .vf-kind{font-size:.68rem;letter-spacing:.11em;text-transform:uppercase;font-weight:900;color:var(--acc2);margin-bottom:6px}
#vzScrim{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:9100;opacity:0;pointer-events:none;transition:opacity .25s}
#vzScrim.on{opacity:1;pointer-events:auto}

@media(max-width:760px){
  #pg-visualisations .vz{padding:18px 12px 60px}
  #pg-visualisations .vz-hero{padding:20px 17px;border-radius:20px}
  #pg-visualisations .vz-hero h1{font-size:1.6rem}
  #pg-visualisations .vz-grid{grid-template-columns:1fr}
  #pg-visualisations .vz-view{height:min(66vh,560px);border-radius:14px}
  #pg-visualisations .vz-hint{display:none}
  #pg-visualisations .vz-stage-top h2{font-size:1.24rem}
  #vzPanel{width:100%;height:90%;top:auto;bottom:0;border-left:0;border-top:1px solid var(--bdr);
    border-radius:20px 20px 0 0;transform:translateY(102%)}
  #vzPanel.on{transform:none}
  #vzFull .vf-in{padding:18px 14px 70px}
  #vzFull .vf-top h2{font-size:1.4rem}
}
</style>
"""

HTML = """<div class="pg" id="pg-visualisations">
  <section class="vz">
    <div id="vzIndex">
      <div class="vz-hero">
        <div class="vz-kick">Thèmes transversaux · exploration interactive</div>
        <h1>Visualisations stratégiques</h1>
        <p>Chaque thème est une carte explorable : une vue d’ensemble donne la structure
        au premier regard, puis chaque élément s’ouvre sur sa définition, ses mécanismes
        étape par étape, ses arguments, ses oppositions, ses auteurs et ses chiffres.
        Les flèches sont cliquables : elles expliquent pourquoi deux idées sont liées.
        Zoom, déplacement et plein écran sont libres, et le texte reste net à tous les niveaux.</p>
        <div class="vz-hero-st" id="vzStats"></div>
      </div>
      <div class="vz-filters">
        <input class="vz-q" id="vzQ" type="text" placeholder="Rechercher un thème, un auteur, un mécanisme…">
        <span id="vzChips"></span>
      </div>
      <div class="vz-grid" id="vzGrid"></div>
    </div>
    <div id="vzStage" style="display:none"></div>
  </section>
</div>
"""

JS = r"""
<script id="v215-visu-engine">
(function(){
'use strict';
if(window.__VZ) return; window.__VZ = true;

var VZ = __PAYLOAD__;
window.visualisationsStrategiques = VZ;

var LIBROLE = {coeur:'Cœur du thème', pilier:'Branche', detail:'Approfondissement',
  limite:'Limite', debat:'Débat', fait:'Faits et chiffres', sortie:'Issue'};
var LIBTYPE = {hub:'Noyau et branches', flux:'Chaîne causale', duel:'Deux positions',
  cycle:'Boucle', arbre:'Arborescence', strates:'Niveaux emboîtés', courants:'Filiations'};
var LIBLIEN = {cause:'entraîne', oppose:'s’oppose à', limite:'limite',
  renforce:'renforce', mesure:'mesure', conditionne:'conditionne'};
var COUL = {cause:'rgba(190,196,220,.55)', oppose:'rgba(255,125,156,.72)',
  limite:'rgba(255,210,80,.72)', renforce:'rgba(106,247,196,.72)',
  mesure:'rgba(0,212,255,.72)', conditionne:'rgba(124,92,255,.75)'};

function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){
  return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'})[m];});}
function nz(s){return String(s==null?'':s).toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g,'');}
function el(id){return document.getElementById(id);}

/* ======================================================= état */
var S = {visu:null, z:1, x:0, y:0, sel:null, filtre:'', type:'', mesures:null};

/* ======================================================= index */
function statsGlobales(){
  var nn=0, nl=0, chs={};
  VZ.forEach(function(v){ nn+=v.noeuds.length; nl+=v.liens.length;
    (v.chapitres||[]).forEach(function(c){ chs[c.k]=1; }); });
  return {th:VZ.length, nn:nn, nl:nl, ch:Object.keys(chs).length};
}

function apercu(v){
  /* miniature structurelle : des formes, aucun texte minuscule */
  var W=300,H=92,P=12,t=v.type,n=v.noeuds.length,s='';
  function rc(x,y,w,h,o,r){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+(h||9)+
    '" rx="'+(r||4)+'" fill="rgba(124,92,255,'+(o||.3)+')"/>';}
  function li(a,b,c,d){return '<line x1="'+a+'" y1="'+b+'" x2="'+c+'" y2="'+d+
    '" stroke="rgba(190,196,220,.3)" stroke-width="1.2"/>';}
  var i,k,ang,cx=W/2,cy=H/2;
  if(t==='hub'||t==='cycle'){
    var m=Math.min(n-1,8);
    for(i=0;i<m;i++){ ang=-Math.PI/2+i*2*Math.PI/m;
      var px=cx+Math.cos(ang)*104, py=cy+Math.sin(ang)*31;
      s+=li(cx,cy,px,py)+rc(px-20,py-5,40,10,.34); }
    s+=rc(cx-30,cy-8,60,16,.6,6);
  } else if(t==='flux'||t==='courants'){
    var g={}; v.noeuds.forEach(function(d){g[d.grp]=(g[d.grp]||0)+1;});
    var ks=Object.keys(g).sort(function(a,b){return a-b;}), cw=(W-2*P)/Math.max(ks.length,1);
    ks.forEach(function(kk,ci){ var c=Math.min(g[kk],4), x=P+ci*cw;
      for(k=0;k<c;k++){ var yy=cy-(c*13)/2+k*13;
        s+=rc(x+3,yy,cw-10,10,.3+ci*0.04); }
      if(ci<ks.length-1) s+=li(x+cw-4,cy,x+cw+3,cy); });
  } else if(t==='duel'){
    s+=rc(cx-26,P,52,12,.55,6);
    for(i=0;i<3;i++){ s+=rc(P+6,30+i*16,96,11,.3); s+=rc(W-P-102,30+i*16,96,11,.3); }
    s+=li(cx,P+14,cx,H-P-12);
    s+=rc(cx-30,H-P-12,60,11,.45,6);
  } else if(t==='strates'){
    var gg={}; v.noeuds.forEach(function(d){gg[d.grp]=(gg[d.grp]||0)+1;});
    var kz=Object.keys(gg).sort(function(a,b){return a-b;}), bh=(H-2*P)/Math.max(kz.length,1);
    kz.forEach(function(kk,bi){ var c=Math.min(gg[kk],5), bw=(W-2*P)/c;
      for(k=0;k<c;k++) s+=rc(P+k*bw+2,P+bi*bh+2,bw-6,Math.max(bh-7,7),.28+bi*0.05); });
  } else { /* arbre */
    s+=rc(cx-28,P,56,12,.55,6);
    for(i=0;i<3;i++){ s+=rc(P+i*((W-2*P)/3)+6,42,(W-2*P)/3-14,11,.34);
      s+=li(cx,P+13,P+i*((W-2*P)/3)+6+((W-2*P)/3-14)/2,42); }
    for(i=0;i<4;i++) s+=rc(P+i*((W-2*P)/4)+6,70,(W-2*P)/4-13,10,.24);
  }
  return '<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none" aria-hidden="true">'+s+'</svg>';
}

function rendreIndex(){
  var st=statsGlobales(), h='';
  h+='<div><b>'+st.th+'</b>thèmes explorables</div>';
  h+='<div><b>'+st.nn+'</b>éléments à ouvrir</div>';
  h+='<div><b>'+st.nl+'</b>liens expliqués</div>';
  h+='<div><b>'+st.ch+'</b>chapitres reliés</div>';
  if(el('vzStats')) el('vzStats').innerHTML=h;

  var types={}, ordre=[];
  VZ.forEach(function(v){ var f=v.fam||LIBTYPE[v.type]||v.type;
    if(!types[f]) ordre.push(f); types[f]=(types[f]||0)+1; });
  var c='<button class="vz-chip'+(S.type===''?' on':'')+'" data-t="">Tous · '+VZ.length+'</button>';
  ordre.forEach(function(t){
    c+='<button class="vz-chip'+(S.type===t?' on':'')+'" data-t="'+esc(t)+'">'+
       esc(t)+' · '+types[t]+'</button>';});
  if(el('vzChips')) el('vzChips').innerHTML=c;

  var q=nz(S.filtre), g='';
  VZ.forEach(function(v,i){
    if(S.type && (v.fam||LIBTYPE[v.type]||v.type)!==S.type) return;
    if(q){
      var foin=nz(v.titre+' '+v.resume+' '+v.kicker+' '+
        v.noeuds.map(function(d){return d.t+' '+d.r+' '+
          (d.aut||[]).map(function(a){return a.n;}).join(' ');}).join(' '));
      if(foin.indexOf(q)<0) return;
    }
    var nch=(v.chapitres||[]).length, naut={};
    v.noeuds.forEach(function(d){(d.aut||[]).forEach(function(a){naut[a.n]=1;});});
    g+='<button class="vz-card" data-v="'+i+'">'+
      '<div class="vz-card-top"><div class="vz-card-kick">'+esc(v.kicker)+'</div>'+
      '<h3>'+esc(v.titre)+'</h3><p>'+esc(v.resume)+'</p></div>'+
      '<div class="vz-prev">'+apercu(v)+'</div>'+
      '<div class="vz-card-foot"><span class="vz-tag t">'+esc(LIBTYPE[v.type]||v.type)+'</span>'+
      '<span class="vz-tag">'+v.noeuds.length+' éléments</span>'+
      '<span class="vz-tag">'+v.liens.length+' liens</span>'+
      '<span class="vz-tag">'+Object.keys(naut).length+' auteurs</span>'+
      (nch?'<span class="vz-tag">'+nch+' chapitres</span>':'')+'</div></button>';
  });
  if(el('vzGrid')) el('vzGrid').innerHTML = g ||
    '<p style="color:var(--txt3);font-size:.86rem">Aucun thème ne correspond à cette recherche.</p>';
}

/* ======================================================= scène */
function ouvrirVisu(i){
  S.visu=VZ[i]; S.sel=null; S.mesures=null;
  el('vzIndex').style.display='none';
  var st=el('vzStage'); st.style.display='';
  var sec=document.querySelector('#pg-visualisations .vz');
  if(sec) sec.classList.add('scene');
  var v=S.visu, h='';
  h+='<div class="vz-stage-top"><div style="flex:1;min-width:230px">'+
     '<div class="vz-kick">'+esc(v.kicker)+'</div>'+
     '<h2>'+esc(v.titre)+'</h2></div>'+
     '<button class="vz-back" id="vzRetour">← Tous les thèmes</button></div>';
  h+='<div class="vz-read" id="vzRead"><div><b>Ce que montre ce thème</b><span>'+
     esc(v.resume)+'</span></div>'+(v.lecture||[]).map(function(p){
      return '<div><b>'+esc(p[0])+'</b><span>'+esc(p[1])+'</span></div>';}).join('')+'</div>';
  h+='<div class="vz-tools">'+
     '<button class="vz-tool" data-z="-1" title="Dézoomer">−</button>'+
     '<span class="vz-zoomval" id="vzZ">100 %</span>'+
     '<button class="vz-tool" data-z="1" title="Zoomer">+</button>'+
     '<button class="vz-tool" data-fit="1">Ajuster</button>'+
     '<button class="vz-tool" data-fit="0">100 %</button>'+
     '<button class="vz-tool" id="vzPleinT">Plein écran</button>'+
     '<button class="vz-tool" id="vzReadT">Comment lire</button>'+
     '<button class="vz-tool" id="vzLegT">Légende</button>'+
     '<span class="vz-hint">Molette ou pincement : zoom · glisser : déplacer · clic sur un élément ou une flèche : ouvrir</span></div>';
  h+='<div class="vz-view" id="vzView"><div class="vz-world" id="vzWorld">'+
     '<svg class="vz-edges" id="vzEdges"></svg></div></div>';
  h+='<div class="vz-leg" id="vzLeg" style="display:none"></div>';
  if((v.chapitres||[]).length){
    h+='<div class="vz-leg" style="margin-top:12px"><span style="border:0;background:none;padding-left:0">Chapitres mobilisés :</span>';
    v.chapitres.forEach(function(c){
      h+='<span style="cursor:pointer" data-goch="'+esc(c.k)+'">'+esc(c.lib)+'</span>';});
    h+='</div>';
  }
  st.innerHTML=h;
  el('vzRetour').onclick=retourIndex;
  construireScene();
  brancherScene();
  try{ window.scrollTo({top:0,behavior:'smooth'}); }catch(e){ window.scrollTo(0,0); }
}

function retourIndex(){
  fermerPanneau(); fermerPlein(); quitterPlein();
  var sec2=document.querySelector('#pg-visualisations .vz');
  if(sec2) sec2.classList.remove('scene');
  el('vzStage').style.display='none'; el('vzStage').innerHTML='';
  el('vzIndex').style.display='';
  S.visu=null;
}

function chips(d){
  var b=[];
  if(d.defi) b.push('définition');
  if((d.mec||[]).length) b.push((d.mec.length)+' étapes');
  if((d.args||[]).length) b.push((d.args.length)+' arg.');
  if((d.opp||[]).length) b.push((d.opp.length)+' débat'+(d.opp.length>1?'s':''));
  if((d.aut||[]).length) b.push((d.aut.length)+' auteur'+(d.aut.length>1?'s':''));
  if((d.faits||[]).length) b.push((d.faits.length)+' faits');
  return b.map(function(x){return '<i>'+esc(x)+'</i>';}).join('');
}

function largeurRole(r){
  if(r==='coeur') return 300;
  if(r==='pilier') return 262;
  if(r==='debat'||r==='limite') return 258;
  return 236;
}

function construireScene(){
  var v=S.visu, world=el('vzWorld');
  world.querySelectorAll('.vz-node,.vz-lab,.vz-band').forEach(function(n){n.remove();});

  /* 1. créer les nœuds, puis mesurer leur hauteur réelle */
  var noeuds=v.noeuds.map(function(d,i){
    var b=document.createElement('button');
    b.className='vz-node r-'+d.role; b.setAttribute('data-n',i);
    b.style.width=largeurRole(d.role)+'px';
    b.innerHTML='<div class="vzk">'+esc(LIBROLE[d.role]||d.role)+'</div>'+
      '<div class="vzt">'+esc(d.t)+'</div><div class="vzr">'+esc(d.r)+'</div>'+
      '<div class="vzb">'+chips(d)+'</div>';
    world.appendChild(b);
    return {d:d, i:i, el:b, w:largeurRole(d.role), h:0};
  });
  noeuds.forEach(function(n){ n.h=n.el.offsetHeight||140;
    n.el.style.height=n.h+'px'; });

  var vue=el('vzView');
  S.etroit = !!(vue && vue.clientWidth < 700);
  S.colonne = S.etroit ? Math.max(210, vue.clientWidth-52) : 0;
  placer(v, noeuds, S.etroit);
  if(!S.etroit) separer(noeuds);

  /* 2. normaliser pour que tout soit en coordonnées positives */
  var minx=1e9,miny=1e9,maxx=-1e9,maxy=-1e9;
  noeuds.forEach(function(n){
    minx=Math.min(minx,n.x); miny=Math.min(miny,n.y);
    maxx=Math.max(maxx,n.x+n.w); maxy=Math.max(maxy,n.y+n.h); });
  var M=S.etroit?14:90, dx=M-minx, dy=M-miny;
  noeuds.forEach(function(n){ n.x+=dx; n.y+=dy;
    n.el.style.left=Math.round(n.x)+'px'; n.el.style.top=Math.round(n.y)+'px'; });
  var W=maxx-minx+2*M, H=maxy-miny+2*M;
  S.mesures={noeuds:noeuds, W:W, H:H};
  world.style.width=W+'px'; world.style.height=H+'px';

  /* 3. bandes éventuelles (types strates / courants) */
  (v.bandes||[]).forEach(function(bd){
    var ns=noeuds.filter(function(n){return String(n.d.grp)===String(bd[0]);});
    if(!ns.length) return;
    var a=1e9,b=1e9,c=-1e9,e2=-1e9;
    ns.forEach(function(n){ a=Math.min(a,n.x); b=Math.min(b,n.y);
      c=Math.max(c,n.x+n.w); e2=Math.max(e2,n.y+n.h); });
    var z=document.createElement('div'); z.className='vz-band';
    z.style.left=(a-26)+'px'; z.style.top=(b-34)+'px';
    z.style.width=(c-a+52)+'px'; z.style.height=(e2-b+60)+'px';
    z.innerHTML='<span>'+esc(bd[1])+'</span>';
    world.insertBefore(z, world.firstChild.nextSibling);
  });

  /* 4. arêtes, puis ajustement du monde aux étiquettes posées */
  var ex=tracerLiens(noeuds, W, H);
  if(ex.x0<0||ex.y0<0){
    var ddx=-Math.min(0,ex.x0), ddy=-Math.min(0,ex.y0);
    world.querySelectorAll('.vz-node,.vz-lab,.vz-band').forEach(function(n){
      n.style.left=(parseFloat(n.style.left)+ddx)+'px';
      n.style.top=(parseFloat(n.style.top)+ddy)+'px'; });
    el('vzEdges').style.left=ddx+'px'; el('vzEdges').style.top=ddy+'px';
    noeuds.forEach(function(n){ n.x+=ddx; n.y+=ddy; });
    ex.x1+=ddx; ex.y1+=ddy;
  }
  W=Math.max(W, ex.x1); H=Math.max(H, ex.y1);
  S.mesures.W=W; S.mesures.H=H;
  world.style.width=W+'px'; world.style.height=H+'px';
  ajuster(true);
  legende();
}

/* ------------------------------------------------- placements par type */
function groupes(noeuds){
  var g={}, ks=[];
  noeuds.forEach(function(n){
    var k=String(n.d.grp);
    if(!g[k]){ g[k]=[]; ks.push(k); }
    g[k].push(n); });
  ks.sort(function(a,b){return (parseFloat(a)||0)-(parseFloat(b)||0);});
  return {g:g, ks:ks};
}

/* Aucun placement ne peut garantir à lui seul l'absence de chevauchement,
   puisque la hauteur des cartes dépend du texte réellement écrit. Cette
   passe écarte donc les cartes qui se touchent encore, dans la direction
   où elles se recouvrent le moins : les positions calculées par `placer`
   sont conservées, seules les collisions sont corrigées. */
function separer(noeuds, marge, fixes){
  var M=marge||26;
  for(var it=0; it<220; it++){
    var bouge=false;
    /* les obstacles fixes (les cartes) ne bougent pas : seules les
       étiquettes s'écartent, par petits pas pour éviter les allers-retours. */
    (fixes||[]).forEach(function(b){
      noeuds.forEach(function(a){
        var ox=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)+5;
        var oy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)+5;
        if(ox<=0||oy<=0) return;
        bouge=true;
        if(ox<oy) a.x+=(a.x+a.w/2<=b.x+b.w/2?-1:1)*ox*0.55;
        else a.y+=(a.y+a.h/2<=b.y+b.h/2?-1:1)*oy*0.55;
      });
    });
    for(var i=0;i<noeuds.length;i++) for(var j=i+1;j<noeuds.length;j++){
      var a=noeuds[i], b=noeuds[j];
      var ox=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)+M;
      var oy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)+M;
      if(ox<=0||oy<=0) continue;
      bouge=true;
      if(ox<oy){
        var s=(a.x+a.w/2<=b.x+b.w/2)?1:-1;
        a.x-=s*ox/2; b.x+=s*ox/2;
      }else{
        var s2=(a.y+a.h/2<=b.y+b.h/2)?1:-1;
        a.y-=s2*oy/2; b.y+=s2*oy/2;
      }
    }
    if(!bouge) return;
  }
}

function placer(v, noeuds, etroit){
  var t=v.type, GX=132, GY=34;
  var Q=groupes(noeuds);

  /* téléphone : une seule colonne, dans l'ordre de lecture du thème ;
     la vue s'ajuste alors à la largeur et l'on se déplace verticalement. */
  if(etroit){
    var ordre=noeuds.slice().sort(function(a,b){
      var ga=parseFloat(a.d.grp)||0, gb=parseFloat(b.d.grp)||0;
      if(a.d.role==='coeur') ga=-1; if(b.d.role==='coeur') gb=-1;
      if(ga!==gb) return ga-gb;
      return a.i-b.i; });
    var ix={}; ordre.forEach(function(n,k){ ix[n.d.id]=k; });
    /* chaque détail est ramené juste sous la branche dont il dépend */
    var fin=[], pris={};
    ordre.forEach(function(n){
      if(pris[n.d.id]) return;
      pris[n.d.id]=1; fin.push(n);
      ordre.forEach(function(m){
        if(!pris[m.d.id] && m.d.par===n.d.id){ pris[m.d.id]=1; fin.push(m); } });
    });
    var yy=0;
    fin.forEach(function(n){
      n.w=S.colonne;
      n.el.style.width=n.w+'px'; n.el.style.height='';
      n.h=n.el.offsetHeight||n.h; n.el.style.height=n.h+'px';
      n.x=0; n.y=yy; yy+=n.h+150; });
    S.ordre=fin;
    return;
  }

  if(t==='flux'||t==='courants'){
    var cx=0;
    Q.ks.forEach(function(k){
      var col=Q.g[k], wmax=0, htot=0;
      col.forEach(function(n){ wmax=Math.max(wmax,n.w); htot+=n.h+GY; });
      htot-=GY;
      var y=-htot/2;
      col.forEach(function(n){ n.x=cx+(wmax-n.w)/2; n.y=y; y+=n.h+GY; });
      cx+=wmax+GX*1.5;
    });
    return;
  }

  if(t==='strates'){
    var cy=0;
    Q.ks.forEach(function(k){
      var row=Q.g[k], wtot=0, hmax=0;
      row.forEach(function(n){ wtot+=n.w+GX*0.74; hmax=Math.max(hmax,n.h); });
      wtot-=GX*0.74;
      var x=-wtot/2;
      row.forEach(function(n){ n.x=x; n.y=cy+(hmax-n.h)/2; x+=n.w+GX*0.74; });
      cy+=hmax+GY*2.5;
    });
    return;
  }

  if(t==='arbre'){
    var cy2=0;
    Q.ks.forEach(function(k){
      var row=Q.g[k], wtot=0, hmax=0;
      row.forEach(function(n){ wtot+=n.w+GX*0.56; hmax=Math.max(hmax,n.h); });
      wtot-=GX*0.56;
      var x=-wtot/2;
      row.forEach(function(n){ n.x=x; n.y=cy2; x+=n.w+GX*0.56; });
      cy2+=hmax+GY*2.9;
    });
    return;
  }

  if(t==='duel'){
    /* Chaque camp est disposé en grille et non en file : au-delà de trois
       cartes, une colonne unique rendrait la scène trop haute pour tenir
       dans un écran, donc illisible sans zoomer. */
    var coeur=noeuds.filter(function(n){return n.d.role==='coeur';})[0];
    var ga=noeuds.filter(function(n){return String(n.d.grp)==='1';});
    var gb=noeuds.filter(function(n){return String(n.d.grp)==='2';});
    var gs=noeuds.filter(function(n){return String(n.d.grp)==='3';});
    function grille(ns, gauche){
      if(!ns.length) return {w:0, h:0};
      var nc=ns.length>3?2:1, parcol=Math.ceil(ns.length/nc);
      var cols=[], i;
      for(i=0;i<nc;i++) cols.push(ns.slice(i*parcol,(i+1)*parcol));
      cols=cols.filter(function(c){return c.length;});
      var hauts=cols.map(function(c){var h=0;c.forEach(function(n){h+=n.h+GY;});return h-GY;});
      var H2=Math.max.apply(null,hauts);
      var larg=0; cols.forEach(function(c){
        var w=0; c.forEach(function(n){w=Math.max(w,n.w);}); larg+=w+GX*0.46; });
      larg-=GX*0.46;
      var x0 = gauche ? -(GX*0.9)/2-larg : (GX*0.9)/2;
      cols.forEach(function(c,ci){
        var w=0; c.forEach(function(n){w=Math.max(w,n.w);});
        var y0=-hauts[ci]/2;
        c.forEach(function(n){ n.x=x0+(w-n.w)/2; n.y=y0; y0+=n.h+GY; });
        x0+=w+GX*0.46;
      });
      return {w:larg, h:H2};
    }
    var A=grille(ga, true), B=grille(gb, false);
    var HT=Math.max(A.h,B.h), y;
    if(coeur){ coeur.x=-coeur.w/2; coeur.y=-HT/2-coeur.h-74; }
    y=HT/2+74;
    var wt=0; gs.forEach(function(n){wt+=n.w+GX*0.46;}); wt-=GX*0.46;
    var x2=-wt/2;
    gs.forEach(function(n){ n.x=x2; n.y=y; x2+=n.w+GX*0.46; });
    return;
  }

  if(t==='cycle'){
    var c2=noeuds.filter(function(n){return n.d.role==='coeur';})[0];
    var ring=noeuds.filter(function(n){return n.d.role!=='coeur';});
    /* On ordonne l'anneau en suivant les liens : deux étapes enchaînées se
       retrouvent côte à côte, de sorte que le cycle se lise en tournant
       autour du centre plutôt qu'en traversant la figure. */
    (function(){
      var ids={}; ring.forEach(function(n){ ids[n.d.id]=n; });
      var suiv={};
      v.liens.forEach(function(l){
        if(ids[l.de] && ids[l.vers] && !suiv[l.de]) suiv[l.de]=l.vers; });
      var entrants={};
      Object.keys(suiv).forEach(function(k){ entrants[suiv[k]]=1; });
      var depart=ring.filter(function(n){return !entrants[n.d.id];})[0]||ring[0];
      var out=[], vu={}, cur=depart;
      while(cur && !vu[cur.d.id]){
        vu[cur.d.id]=1; out.push(ids[cur.d.id]);
        cur = suiv[cur.d.id] ? ids[suiv[cur.d.id]] : null;
      }
      ring.forEach(function(n){ if(!vu[n.d.id]) out.push(n); });
      ring = out;
    })();
    var m=ring.length, R=Math.max(380, m*78), RY=Math.max(230, m*42);
    ring.forEach(function(n,i){
      var a=-Math.PI/2+i*2*Math.PI/m;
      n.x=Math.cos(a)*R-n.w/2; n.y=Math.sin(a)*RY-n.h/2; });
    if(c2){ c2.x=-c2.w/2; c2.y=-c2.h/2; }
    return;
  }

  /* hub : cœur au centre, branches sur une ellipse, détails en dehors */
  var co=noeuds.filter(function(n){return n.d.role==='coeur';})[0];
  var br=noeuds.filter(function(n){return String(n.d.grp)==='1';});
  var de=noeuds.filter(function(n){return String(n.d.grp)==='2';});
  if(co){ co.x=-co.w/2; co.y=-co.h/2; }
  /* ellipse volontairement aplatie : les écrans sont larges et peu hauts,
     une étoile « ronde » obligerait à tout réduire pour la voir entière. */
  var nb=br.length||1, RX=Math.max(540, nb*122), RYh=Math.max(215, nb*46);
  var ang={};
  br.forEach(function(n,i){
    var a=-Math.PI/2+i*2*Math.PI/nb;
    ang[n.d.id]=a;
    n.x=Math.cos(a)*RX-n.w/2; n.y=Math.sin(a)*RYh-n.h/2; });
  var parc={};
  de.forEach(function(n){
    var p=n.d.par, a=(p&&ang[p]!==undefined)?ang[p]:(-Math.PI/2);
    var k=parc[p||'_']=(parc[p||'_']||0)+1;
    var ecart=(k-1)*0.42-((contParents(de,p)-1)*0.42)/2;
    var aa=a+ecart;
    n.x=Math.cos(aa)*(RX+290)-n.w/2;
    n.y=Math.sin(aa)*(RYh+135)-n.h/2;
  });
}
function contParents(de,p){
  var c=0; de.forEach(function(n){ if((n.d.par||'_')===(p||'_')) c++; }); return c;
}

/* ------------------------------------------------- arêtes */
function bord(n, vx, vy){
  /* point de sortie du rectangle n dans la direction (vx,vy) */
  var cx=n.x+n.w/2, cy=n.y+n.h/2;
  if(vx===0 && vy===0) return {x:cx,y:cy};
  var hw=n.w/2+6, hh=n.h/2+6;
  var tx=vx!==0?Math.abs(hw/vx):1e9, ty=vy!==0?Math.abs(hh/vy):1e9;
  var tt=Math.min(tx,ty);
  return {x:cx+vx*tt, y:cy+vy*tt};
}

/* Sur téléphone, la visualisation se lit en colonne : chaque étiquette se
   place dans l'intervalle qui suit la carte d'où part le lien, et les
   intervalles s'élargissent d'eux-mêmes pour les accueillir. Rien ne
   dépasse alors de la colonne : la vue tient dans la largeur de l'écran
   et le texte garde sa taille normale. */
function tracerLiensEtroit(noeuds){
  var v=S.visu, svg=el('vzEdges'), world=el('vzWorld');
  var par={}; noeuds.forEach(function(n){ par[n.d.id]=n; });
  var rang={}; (S.ordre||noeuds).forEach(function(n,k){ rang[n.d.id]=k; });
  var suite=(S.ordre||noeuds);

  var etiq=v.liens.map(function(l,li){
    var lab=document.createElement('button');
    lab.className='vz-lab e-'+l.t; lab.setAttribute('data-l',li);
    lab.style.maxWidth=S.colonne+'px'; lab.style.whiteSpace='normal';
    lab.textContent=l.lab;
    lab.title=l.lab+' — cliquer pour l’explication';
    world.appendChild(lab);
    return {el:lab, l:l, de:par[l.de], vers:par[l.vers]};
  }).filter(function(e){ return e.de && e.vers; });
  etiq.forEach(function(e){ e.w=e.el.offsetWidth; e.h=e.el.offsetHeight;
    e.k=Math.min(rang[e.de.d.id], rang[e.vers.d.id]); });

  /* intervalle nécessaire sous chaque carte */
  var dans={};
  etiq.forEach(function(e){ (dans[e.k]=dans[e.k]||[]).push(e); });
  var y=0;
  suite.forEach(function(n,k){
    n.y=y; n.el.style.top=Math.round(n.y)+'px';
    var h=0; (dans[k]||[]).forEach(function(e){ h+=e.h+10; });
    y += n.h + Math.max(74, h+40);
  });

  var W=S.colonne, H=y;
  svg.setAttribute('width',W); svg.setAttribute('height',H);
  svg.setAttribute('viewBox','0 0 '+W+' '+H);
  var defs='<defs>';
  Object.keys(COUL).forEach(function(t){
    defs+='<marker id="vzm-'+t+'" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '+
      'markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="'+COUL[t]+'"/></marker>';
  });
  defs+='</defs>';
  var paths='';
  v.liens.forEach(function(l,li){
    var a=par[l.de], b=par[l.vers]; if(!a||!b) return;
    var ax=a.x+a.w/2, ay=a.y+a.h/2, bx=b.x+b.w/2, by=b.y+b.h/2;
    var dx=bx-ax, dy=by-ay, d=Math.sqrt(dx*dx+dy*dy)||1;
    var p1=bord(a, dx/d, dy/d), p2=bord(b, -dx/d, -dy/d);
    var ecart=Math.min(Math.abs(rang[l.vers]-rang[l.de]||1), 4);
    var cote=(li%2?1:-1), amp=22+ecart*26;
    var qx=(p1.x+p2.x)/2+cote*amp, qy=(p1.y+p2.y)/2;
    var dash=(l.t==='oppose'||l.t==='limite')?' stroke-dasharray="7 5"':'';
    paths+='<path d="M'+p1.x.toFixed(1)+','+p1.y.toFixed(1)+' Q'+qx.toFixed(1)+','+
      qy.toFixed(1)+' '+p2.x.toFixed(1)+','+p2.y.toFixed(1)+
      '" fill="none" stroke="'+COUL[l.t]+'" stroke-width="1.7"'+dash+
      ' marker-end="url(#vzm-'+l.t+')" data-e="'+li+'"/>';
  });
  svg.innerHTML=defs+paths;

  Object.keys(dans).forEach(function(k){
    var n=suite[k]; if(!n) return;
    var yy=n.y+n.h+18;
    dans[k].forEach(function(e){
      e.el.style.left=Math.round(W/2)+'px';
      e.el.style.top=Math.round(yy+e.h/2)+'px';
      yy+=e.h+10;
    });
  });
  return {x0:0, y0:0, x1:W, y1:H};
}

function tracerLiens(noeuds, W, H){
  if(S.etroit) return tracerLiensEtroit(noeuds);
  var v=S.visu, svg=el('vzEdges'), world=el('vzWorld');
  var par={}; noeuds.forEach(function(n){ par[n.d.id]=n; });
  svg.setAttribute('width',W); svg.setAttribute('height',H);
  svg.setAttribute('viewBox','0 0 '+W+' '+H);
  var defs='<defs>';
  Object.keys(COUL).forEach(function(t){
    defs+='<marker id="vzm-'+t+'" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '+
      'markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="'+COUL[t]+'"/></marker>';
  });
  defs+='</defs>';
  var paths='', etiq=[];
  /* les étiquettes sont mesurées au gabarit de la vue d'ensemble, celui où
     la place manque le plus : elles ne se recouvriront donc jamais. */
  var loinAvant=world.classList.contains('loin');
  world.classList.add('loin');
  v.liens.forEach(function(l,li){
    var a=par[l.de], b=par[l.vers]; if(!a||!b) return;
    var ax=a.x+a.w/2, ay=a.y+a.h/2, bx=b.x+b.w/2, by=b.y+b.h/2;
    var dx=bx-ax, dy=by-ay, d=Math.sqrt(dx*dx+dy*dy)||1;
    var p1=bord(a, dx/d, dy/d), p2=bord(b, -dx/d, -dy/d);
    var mx=(p1.x+p2.x)/2, my=(p1.y+p2.y)/2;
    var nxp=-(p2.y-p1.y), nyp=(p2.x-p1.x), nl=Math.sqrt(nxp*nxp+nyp*nyp)||1;
    var cur=Math.min(58, d*0.14);
    var qx=mx+(nxp/nl)*cur, qy=my+(nyp/nl)*cur;
    var dash=(l.t==='oppose'||l.t==='limite')?' stroke-dasharray="7 5"':'';
    paths+='<path d="M'+p1.x.toFixed(1)+','+p1.y.toFixed(1)+' Q'+qx.toFixed(1)+','+
      qy.toFixed(1)+' '+p2.x.toFixed(1)+','+p2.y.toFixed(1)+
      '" fill="none" stroke="'+COUL[l.t]+'" stroke-width="1.7"'+dash+
      ' marker-end="url(#vzm-'+l.t+')" data-e="'+li+'"/>';
    var lab=document.createElement('button');
    lab.className='vz-lab e-'+l.t; lab.setAttribute('data-l',li);
    lab.textContent=l.lab;
    lab.title=l.lab+' — cliquer pour l’explication';
    world.appendChild(lab);
    etiq.push({el:lab, p1:p1, p2:p2, q:{x:qx,y:qy}, nx:nxp/nl, ny:nyp/nl});
  });
  function surCourbe(e,t){
    var u=1-t;
    return {x:u*u*e.p1.x+2*u*t*e.q.x+t*t*e.p2.x,
            y:u*u*e.p1.y+2*u*t*e.q.y+t*t*e.p2.y};
  }
  /* Placement des étiquettes : pour chacune, on essaie une série de points
     le long de sa courbe, décalés perpendiculairement, et l'on retient la
     position qui recouvre le moins les cartes et les étiquettes déjà
     posées. La recherche est déterministe, donc le résultat est stable. */
  var boites=noeuds.map(function(n){return {x:n.x,y:n.y,w:n.w,h:n.h};});
  /* les intitulés de bande sont eux aussi des obstacles : une étiquette de
     lien ne doit pas venir masquer le nom d'une strate. */
  world.querySelectorAll('.vz-band').forEach(function(z){
    var sp=z.querySelector('span'); if(!sp) return;
    boites.push({x:parseFloat(z.style.left)+sp.offsetLeft-4,
                 y:parseFloat(z.style.top)+sp.offsetTop-4,
                 w:sp.offsetWidth+8, h:sp.offsetHeight+8});
  });
  var PAS=[0.5,0.44,0.56,0.38,0.62,0.32,0.68,0.26,0.74,0.2,0.8];
  var poses=[];
  function chevauche(a,b){
    var ox=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x);
    var oy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
    return (ox>0&&oy>0) ? ox*oy : 0;
  }
  etiq.forEach(function(e){ e.w=e.el.offsetWidth; e.h=e.el.offsetHeight; });
  function poser(e){
    var mieux=null, score=Infinity;
    for(var k=0;k<PAS.length;k++){
      var c=surCourbe(e,PAS[k]);
      var ecarts=[0];
      [16,42,74,112,156,206,262,330,412].forEach(function(d){
        ecarts.push(e.h/2+d); ecarts.push(-(e.h/2+d)); });
      for(var j=0;j<ecarts.length;j++){
        var r={x:c.x+e.nx*ecarts[j]-e.w/2-6, y:c.y+e.ny*ecarts[j]-e.h/2-6,
               w:e.w+12, h:e.h+12};
        var s=0, t1=0, t2=0;
        boites.forEach(function(b){ var o=chevauche(r,b); if(o){ t1++; s+=o*3.4; } });
        poses.forEach(function(b){ var o=chevauche(r,b); if(o){ t2++; s+=o*1.6; } });
        /* toute position sans recouvrement passe avant toute autre */
        s += t1*90000 + t2*14000;
        s += Math.abs(PAS[k]-0.5)*420 + Math.abs(ecarts[j])*3.1;
        if(s<score){ score=s; mieux={x:r.x+6, y:r.y+6}; }
      }
    }
    e.x=mieux.x; e.y=mieux.y;
  }
  /* trois passes : la première pose les étiquettes une à une, les suivantes
     les reprennent en tenant compte de la position finale des autres. */
  etiq.forEach(function(e){
    poser(e);
    poses.push({x:e.x-6, y:e.y-6, w:e.w+12, h:e.h+12});
  });
  for(var sw=0; sw<3; sw++){
    etiq.forEach(function(e,k){
      poses.splice(k,1);
      poser(e);
      poses.splice(k,0,{x:e.x-6, y:e.y-6, w:e.w+12, h:e.h+12});
    });
  }
  /* Dernier recours : si une étiquette reste posée sur une carte, on
     cherche en spirale autour d'elle la position libre la plus proche. Le
     lien reste lisible, et aucun titre n'est masqué. */
  function surCarte(r){
    return boites.some(function(b){ return chevauche(r,b)>0; });
  }
  etiq.forEach(function(e,k){
    var r0={x:e.x-6, y:e.y-6, w:e.w+12, h:e.h+12};
    if(!surCarte(r0)) return;
    var trouve=null, replis=null, scoreReplis=Infinity;
    for(var ray=22; ray<=640 && !trouve; ray+=22){
      for(var a=0; a<24 && !trouve; a++){
        var an=a*Math.PI/12;
        var r={x:e.x-6+Math.cos(an)*ray, y:e.y-6+Math.sin(an)*ray,
               w:e.w+12, h:e.h+12};
        if(surCarte(r)) continue;
        var g=0;
        poses.forEach(function(b,j){ if(j!==k) g+=chevauche(r,b); });
        if(g===0){ trouve={x:r.x+6, y:r.y+6}; break; }
        /* à défaut, la meilleure place qui au moins ne masque aucune carte */
        if(g+ray<scoreReplis){ scoreReplis=g+ray; replis={x:r.x+6, y:r.y+6}; }
      }
    }
    if(!trouve) trouve=replis;
    if(trouve){ e.x=trouve.x; e.y=trouve.y;
      poses[k]={x:e.x-6, y:e.y-6, w:e.w+12, h:e.h+12}; }
  });
  etiq.forEach(function(e){
    e.el.style.left=Math.round(e.x+e.w/2)+'px';
    e.el.style.top=Math.round(e.y+e.h/2)+'px';
  });
  if(!loinAvant) world.classList.remove('loin');
  svg.innerHTML=defs+paths;
  var ex={x0:0,y0:0,x1:W,y1:H};
  etiq.forEach(function(e){
    ex.x0=Math.min(ex.x0,e.x-14); ex.y0=Math.min(ex.y0,e.y-14);
    ex.x1=Math.max(ex.x1,e.x+e.w+14); ex.y1=Math.max(ex.y1,e.y+e.h+14); });
  return ex;
}

function legende(){
  var v=S.visu, used={}, roles={};
  v.liens.forEach(function(l){used[l.t]=1;});
  v.noeuds.forEach(function(n){roles[n.role]=1;});
  var h='';
  Object.keys(roles).forEach(function(r){
    var c={coeur:'var(--vzA)',pilier:'var(--vzB)',detail:'rgba(190,196,220,.5)',
      limite:'var(--vzD)',debat:'var(--vzE)',fait:'var(--vzC)',sortie:'var(--vzC)'}[r];
    h+='<span><i style="background:'+c+'"></i>'+esc(LIBROLE[r]||r)+'</span>';});
  Object.keys(used).forEach(function(t){
    h+='<span><i style="background:'+COUL[t]+';border-radius:1px;height:3px;width:16px"></i>'+
       esc(LIBLIEN[t]||t)+'</span>';});
  var L=el('vzLeg'); if(L) L.innerHTML=h;
}

/* ------------------------------------------------- zoom et déplacement */
function appliquer(){
  var w=el('vzWorld'); if(!w) return;
  w.style.transform='translate('+S.x.toFixed(1)+'px,'+S.y.toFixed(1)+'px) scale('+S.z.toFixed(4)+')';
  var loin = !S.etroit && S.z < 0.78;
  if(loin !== w.classList.contains('loin')) w.classList.toggle('loin', loin);
  var z=el('vzZ'); if(z) z.textContent=Math.round(S.z*100)+' %';
}
function borner(z){ return Math.max(0.22, Math.min(3.2, z)); }

function ajuster(centrer){
  var vue=el('vzView'); if(!vue||!S.mesures) return;
  var vw=vue.clientWidth, vh=vue.clientHeight;
  if(vw<700){
    /* sur téléphone on cadre sur la largeur : le thème se parcourt
       verticalement, en gardant le texte à sa taille normale. */
    S.z=borner(Math.min(vw/S.mesures.W*0.98, 1.1));
    S.x=(vw-S.mesures.W*S.z)/2; S.y=10;
    appliquer(); return;
  }
  var z=Math.min(vw/S.mesures.W, vh/S.mesures.H);
  S.z=borner(Math.min(z*0.97, 1.25));
  S.x=(vw-S.mesures.W*S.z)/2; S.y=(vh-S.mesures.H*S.z)/2;
  appliquer();
  if(centrer!==true) return;
}
function cent100(){
  var vue=el('vzView'); if(!vue||!S.mesures) return;
  S.z=1;
  S.x=(vue.clientWidth-S.mesures.W)/2; S.y=(vue.clientHeight-S.mesures.H)/2;
  appliquer();
}
function zoomVers(f, px, py){
  var z2=borner(S.z*f);
  S.x = px-(px-S.x)*(z2/S.z); S.y = py-(py-S.y)*(z2/S.z);
  S.z=z2; appliquer();
}

function brancherScene(){
  var vue=el('vzView');
  vue.addEventListener('wheel', function(e){
    e.preventDefault();
    var r=vue.getBoundingClientRect();
    zoomVers(e.deltaY<0?1.12:1/1.12, e.clientX-r.left, e.clientY-r.top);
  }, {passive:false});

  var pts={}, bouge=false, dep=null, base=null;
  vue.addEventListener('pointerdown', function(e){
    pts[e.pointerId]={x:e.clientX,y:e.clientY};
    var k=Object.keys(pts);
    /* la cible est retenue ici : une fois le pointeur capturé par la vue,
       les événements suivants ne portent plus sur la carte cliquée. */
    if(k.length===1){ bouge=false;
      dep={x:e.clientX,y:e.clientY,ox:S.x,oy:S.y,cible:e.target}; }
    if(k.length===2){
      var a=pts[k[0]], b=pts[k[1]];
      base={d:Math.hypot(a.x-b.x,a.y-b.y), z:S.z,
            cx:(a.x+b.x)/2, cy:(a.y+b.y)/2, x:S.x, y:S.y};
    }
    try{ vue.setPointerCapture(e.pointerId); }catch(err){}
  });
  vue.addEventListener('pointermove', function(e){
    if(!pts[e.pointerId]) return;
    pts[e.pointerId]={x:e.clientX,y:e.clientY};
    var k=Object.keys(pts);
    if(k.length>=2 && base){
      var a=pts[k[0]], b=pts[k[1]];
      var d2=Math.hypot(a.x-b.x,a.y-b.y);
      var f=d2/(base.d||1), z2=borner(base.z*f);
      var r=vue.getBoundingClientRect();
      var px=base.cx-r.left, py=base.cy-r.top;
      S.x=px-(px-base.x)*(z2/base.z); S.y=py-(py-base.y)*(z2/base.z);
      S.z=z2; appliquer(); bouge=true; return;
    }
    if(dep){
      var ddx=e.clientX-dep.x, ddy=e.clientY-dep.y;
      if(Math.abs(ddx)+Math.abs(ddy)>6){ bouge=true; vue.classList.add('drag'); }
      if(bouge){ S.x=dep.ox+ddx; S.y=dep.oy+ddy; appliquer(); }
    }
  });
  function fin(e){
    delete pts[e.pointerId];
    if(Object.keys(pts).length<2) base=null;
    if(!Object.keys(pts).length){
      vue.classList.remove('drag');
      if(!bouge){
        var c=(dep&&dep.cible)||e.target;
        var n=c.closest ? c.closest('.vz-node') : null;
        var l=c.closest ? c.closest('.vz-lab') : null;
        if(n){ S.ouvertLe=Date.now(); ouvrirNoeud(parseInt(n.getAttribute('data-n'),10)); }
        else if(l){ S.ouvertLe=Date.now(); ouvrirLien(parseInt(l.getAttribute('data-l'),10)); }
      }
      dep=null;
    }
  }
  vue.addEventListener('pointerup', fin);
  vue.addEventListener('pointercancel', fin);

  /* Les cartes et les étiquettes sont des boutons : la touche Entrée, et
     plus généralement tout clic qui ne passe pas par le suivi du pointeur,
     doivent les ouvrir aussi. On évite la double ouverture par un garde. */
  el('vzWorld').addEventListener('click', function(e){
    if(Date.now() - (S.ouvertLe||0) < 120) return;
    var n=e.target.closest ? e.target.closest('.vz-node') : null;
    var l=e.target.closest ? e.target.closest('.vz-lab') : null;
    if(n){ S.ouvertLe=Date.now(); ouvrirNoeud(parseInt(n.getAttribute('data-n'),10)); }
    else if(l){ S.ouvertLe=Date.now(); ouvrirLien(parseInt(l.getAttribute('data-l'),10)); }
  });

  el('vzStage').addEventListener('click', function(e){
    var b=e.target.closest('[data-z]');
    if(b){ var r=el('vzView').getBoundingClientRect();
      zoomVers(b.getAttribute('data-z')==='1'?1.18:1/1.18, r.width/2, r.height/2); return; }
    var f=e.target.closest('[data-fit]');
    if(f){ if(f.getAttribute('data-fit')==='1') ajuster(true); else cent100(); return; }
    var g=e.target.closest('[data-goch]');
    if(g){ allerCours(g.getAttribute('data-goch')); return; }
    if(e.target.id==='vzPleinT'){ basculerPlein(); return; }
    if(e.target.id==='vzReadT'){
      var R=el('vzRead'); R.classList.toggle('on');
      e.target.classList.toggle('on', R.classList.contains('on'));
      ajuster(true); return;
    }
    if(e.target.id==='vzLegT'){
      var L=el('vzLeg'); L.style.display = L.style.display==='none' ? 'flex' : 'none';
      e.target.classList.toggle('on'); return;
    }
  });
  window.addEventListener('resize', function(){ if(S.visu) ajuster(true); });
}

function basculerPlein(){
  var pg=document.getElementById('pg-visualisations');
  var on=!pg.classList.contains('plein');
  pg.classList.toggle('plein', on);
  var b=el('vzPleinT');
  if(b){ b.classList.toggle('on', on); b.textContent = on ? 'Quitter le plein écran' : 'Plein écran'; }
  document.body.style.overflow = on ? 'hidden' : '';
  setTimeout(function(){ ajuster(true); }, 40);
}
function quitterPlein(){
  var pg=document.getElementById('pg-visualisations');
  if(pg && pg.classList.contains('plein')) basculerPlein();
}

/* ======================================================= navigation app */
function allerCours(k){
  try{ if(typeof openCh==='function'){ openCh(Number(k)); return; } }catch(e){}
  try{ showPg('chapter'); }catch(e){}
}
function allerFiches(k){
  try{ showPg('fc'); }catch(e){}
  setTimeout(function(){ try{ if(typeof filterFC==='function') filterFC(Number(k)); }catch(e){} },70);
}
function allerSujets(k){
  try{ showPg('subjects'); }catch(e){}
  setTimeout(function(){ try{ if(typeof setSubjectChapterPremium==='function')
    setSubjectChapterPremium(Number(k)); }catch(e){} },120);
}
function allerAtlas(k){
  try{ showPg('atlas'); }catch(e){}
  setTimeout(function(){ try{ var s=document.getElementById('at-ch');
    if(s){ s.value=String(k); s.dispatchEvent(new Event('change')); } }catch(e){} },120);
}
function allerAuteur(nom){
  try{ if(typeof openAuthorByName==='function'){ openAuthorByName(nom); return; } }catch(e){}
  try{ showPg('authors');
    setTimeout(function(){
      var q=document.getElementById('aq')||document.querySelector('#pg-authors input[type=text]');
      if(q){ q.value=nom; q.dispatchEvent(new Event('input',{bubbles:true})); } },90);
  }catch(e){}
}
function allerDossier(cle){
  try{ showPg('autour'); }catch(e){}
  setTimeout(function(){
    try{ var rz=document.getElementById('an-rz'); if(rz) rz.click(); }catch(e){}
    setTimeout(function(){
      var b=document.querySelector('[data-go="'+cle+'"]');
      if(b){ b.click(); try{ window.scrollTo(0,0); }catch(e){} }
    },140);
  },150);
}

/* ======================================================= panneau */
function blocs(d){
  var h='';
  if(d.defi){ h+='<div class="vp-sec"><h4>Définition</h4><p class="vp-p">'+esc(d.defi)+'</p></div>'; }
  if((d.mec||[]).length){
    h+='<div class="vp-sec"><h4>Mécanisme, étape par étape</h4>';
    d.mec.forEach(function(m,i){ h+='<div class="vp-it step"><b><span class="vp-n">'+(i+1)+
      '</span>'+esc(m.t)+'</b><span>'+esc(m.e)+'</span></div>'; });
    h+='</div>';
  }
  if((d.args||[]).length){
    h+='<div class="vp-sec"><h4>Arguments et conditions de validité</h4>';
    d.args.forEach(function(a){ h+='<div class="vp-it arg"><span>'+esc(a.a)+
      '</span><em><b style="display:inline;color:var(--txt3)">Limite — </b>'+esc(a.lim)+'</em></div>'; });
    h+='</div>';
  }
  if((d.opp||[]).length){
    h+='<div class="vp-sec"><h4>Oppositions et débats</h4>';
    d.opp.forEach(function(o){
      h+='<div class="vp-it opp"><b>'+esc(o.t)+'</b>'+
        (o.qui?'<span style="color:var(--txt3);font-size:.78rem">Porté par : '+esc(o.qui)+'</span>':'')+
        '<em><b style="display:inline;color:var(--txt3)">Réponse — </b>'+esc(o.rep)+'</em></div>'; });
    h+='</div>';
  }
  if((d.aut||[]).length){
    h+='<div class="vp-sec"><h4>Auteurs et idées précises</h4>';
    d.aut.forEach(function(a){ h+='<div class="vp-it aut"><b>'+esc(a.n)+'</b><span>'+esc(a.i)+
      '</span><div class="vp-lk" style="margin-top:8px"><button data-aut="'+esc(a.n)+
      '">Voir sa fiche auteur</button></div></div>'; });
    h+='</div>';
  }
  if((d.faits||[]).length){
    h+='<div class="vp-sec"><h4>Faits, exemples et chiffres</h4>';
    d.faits.forEach(function(f){ h+='<div class="vp-it fait"><b>'+esc(f.f)+
      '</b><em><b style="display:inline;color:var(--txt3)">Ce que cela montre — </b>'+esc(f.p)+'</em></div>'; });
    h+='</div>';
  }
  var L=d.lk||{};
  var nb=(L.ch||[]).length+(L.fi||[]).length+(L.at||[]).length+(L.su||[]).length+(L.dos||[]).length;
  if(nb){
    h+='<div class="vp-sec"><h4>Où retrouver cela dans ÉcoSphère</h4>';
    if((L.dos||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin-bottom:7px">Dossiers « Autour d’une notion »</p><div class="vp-lk">';
      L.dos.forEach(function(x){ h+='<button data-dos="'+esc(x.cle)+'">🧩 '+esc(x.t)+'</button>'; });
      h+='</div>';
    }
    if((L.ch||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin:11px 0 7px">Cours</p><div class="vp-lk">';
      L.ch.forEach(function(x){ h+='<button data-ch="'+esc(x.k)+'">📘 '+esc(x.lib)+
        ' <b>· '+x.n+' occurrences</b></button>'; });
      h+='</div>';
    }
    if((L.fi||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin:11px 0 7px">Fiches de révision</p><div class="vp-lk">';
      L.fi.forEach(function(x){ h+='<button data-fc="'+esc(x.k)+'">🃏 '+esc(x.t)+'</button>'; });
      h+='</div>';
    }
    if((L.at||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin:11px 0 7px">Atlas des idées</p><div class="vp-lk">';
      L.at.forEach(function(x){ h+='<button data-at="'+esc(x.k)+'">🗺️ '+esc(x.ti)+'</button>'; });
      h+='</div>';
    }
    if((L.su||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin:11px 0 7px">Sujets de dissertation</p><div class="vp-lk">';
      L.su.forEach(function(x){ h+='<button data-su="'+esc(x.ch)+'">📝 '+esc(x.t)+'</button>'; });
      h+='</div>';
    }
    if((L.au||[]).length){
      h+='<p class="vp-p" style="font-size:.8rem;color:var(--txt3);margin:11px 0 7px">Auteurs mobilisés</p><div class="vp-lk">';
      L.au.forEach(function(x){ var nom = (typeof x === 'string') ? x : (x.n || x.nom || '');
        if(nom) h+='<button data-aut="'+esc(nom)+'">👤 '+esc(nom)+'</button>'; });
      h+='</div>';
    }
    h+='</div>';
  }
  return h;
}

function panneau(){
  var p=el('vzPanel');
  if(p) return p;
  p=document.createElement('aside'); p.id='vzPanel';
  p.innerHTML='<div class="vp-top"><div style="flex:1"><div class="vp-kind" id="vpKind"></div>'+
    '<h3 id="vpTitre"></h3></div><button class="vp-x" id="vpX" aria-label="Fermer">✕</button></div>'+
    '<div class="vp-acts" id="vpActs"></div><div class="vp-body" id="vpBody"></div>';
  document.body.appendChild(p);
  var sc=document.createElement('div'); sc.id='vzScrim'; document.body.appendChild(sc);
  sc.addEventListener('click', fermerPanneau);
  el('vpX').addEventListener('click', fermerPanneau);
  p.addEventListener('click', function(e){
    var b;
    if((b=e.target.closest('[data-ch]'))){ allerCours(b.getAttribute('data-ch')); return; }
    if((b=e.target.closest('[data-fc]'))){ allerFiches(b.getAttribute('data-fc')); return; }
    if((b=e.target.closest('[data-at]'))){ allerAtlas(b.getAttribute('data-at')); return; }
    if((b=e.target.closest('[data-su]'))){ allerSujets(b.getAttribute('data-su')); return; }
    if((b=e.target.closest('[data-aut]'))){ allerAuteur(b.getAttribute('data-aut')); return; }
    if((b=e.target.closest('[data-dos]'))){ allerDossier(b.getAttribute('data-dos')); return; }
    if((b=e.target.closest('[data-go-n]'))){ ouvrirNoeud(parseInt(b.getAttribute('data-go-n'),10)); return; }
    if((b=e.target.closest('[data-plein]'))){ ouvrirPlein(parseInt(b.getAttribute('data-plein'),10)); return; }
    if((b=e.target.closest('[data-centre]'))){ centrerSur(parseInt(b.getAttribute('data-centre'),10)); return; }
  });
  return p;
}

function ouvrirNoeud(i){
  var d=S.visu.noeuds[i]; if(!d) return;
  S.sel=i; panneau();
  el('vpKind').textContent=(LIBROLE[d.role]||d.role)+' · '+S.visu.titre;
  el('vpTitre').textContent=d.t;
  var voisins=S.visu.liens.filter(function(l){return l.de===d.id||l.vers===d.id;});
  var a='<button class="vz-tool" data-plein="'+i+'">⛶ Plein écran</button>'+
        '<button class="vz-tool" data-centre="'+i+'">◎ Centrer</button>';
  el('vpActs').innerHTML=a;
  var h=blocs(d);
  if(voisins.length){
    h+='<div class="vp-sec"><h4>Liens avec les autres éléments</h4>';
    voisins.forEach(function(l){
      var autre=(l.de===d.id)?l.vers:l.de, sens=(l.de===d.id)?'→':'←';
      var j=S.visu.noeuds.map(function(x){return x.id;}).indexOf(autre);
      var na=S.visu.noeuds[j];
      h+='<div class="vp-it"><b>'+sens+' '+esc(na?na.t:autre)+' <span style="color:var(--txt3);font-weight:600">· '+
        esc(l.lab)+'</span></b><span>'+esc(l.expl)+'</span>'+
        '<div class="vp-lk" style="margin-top:8px"><button data-go-n="'+j+'">Ouvrir cet élément</button></div></div>';
    });
    h+='</div>';
  }
  el('vpBody').innerHTML=h;
  el('vpBody').scrollTop=0;
  el('vzPanel').classList.add('on');
  el('vzScrim').classList.add('on');
  surligner(d.id);
}

function ouvrirLien(li){
  var l=S.visu.liens[li]; if(!l) return;
  panneau();
  var ids=S.visu.noeuds.map(function(x){return x.id;});
  var ia=ids.indexOf(l.de), ib=ids.indexOf(l.vers);
  var a=S.visu.noeuds[ia], b=S.visu.noeuds[ib];
  el('vpKind').textContent='Lien · '+(LIBLIEN[l.t]||l.t);
  el('vpTitre').textContent=l.lab;
  el('vpActs').innerHTML='<button class="vz-tool" data-go-n="'+ia+'">Ouvrir « '+esc(a?a.t:'')+' »</button>'+
    '<button class="vz-tool" data-go-n="'+ib+'">Ouvrir « '+esc(b?b.t:'')+' »</button>';
  el('vpBody').innerHTML='<div class="vp-arrow"><b>'+esc(a?a.t:l.de)+'</b><i>→</i><b>'+
    esc(b?b.t:l.vers)+'</b></div>'+
    '<div class="vp-sec"><h4>Pourquoi ces deux idées sont liées</h4><p class="vp-p">'+
    esc(l.expl)+'</p></div>';
  el('vpBody').scrollTop=0;
  el('vzPanel').classList.add('on'); el('vzScrim').classList.add('on');
}

function surligner(id){
  var v=S.visu;
  var proches={}; proches[id]=1;
  v.liens.forEach(function(l){ if(l.de===id) proches[l.vers]=1; if(l.vers===id) proches[l.de]=1; });
  el('vzWorld').querySelectorAll('.vz-node').forEach(function(n){
    var d=v.noeuds[parseInt(n.getAttribute('data-n'),10)];
    n.classList.toggle('sel', d.id===id);
    n.classList.toggle('dim', !proches[d.id]);
  });
  el('vzWorld').querySelectorAll('.vz-lab').forEach(function(n){
    var l=v.liens[parseInt(n.getAttribute('data-l'),10)];
    n.classList.toggle('dim', !(l.de===id||l.vers===id));
  });
}
function eteindre(){
  if(!el('vzWorld')) return;
  el('vzWorld').querySelectorAll('.dim,.sel').forEach(function(n){
    n.classList.remove('dim','sel'); });
}
function centrerSur(i){
  if(!S.mesures) return;
  var n=S.mesures.noeuds[i], vue=el('vzView'); if(!n||!vue) return;
  S.z=borner(Math.max(S.z,0.85));
  S.x=vue.clientWidth/2-(n.x+n.w/2)*S.z;
  S.y=vue.clientHeight/2-(n.y+n.h/2)*S.z;
  appliquer(); fermerPanneau();
}
function fermerPanneau(){
  var p=el('vzPanel'); if(p) p.classList.remove('on');
  var s=el('vzScrim'); if(s) s.classList.remove('on');
  eteindre();
}

/* ======================================================= plein écran */
function ouvrirPlein(i){
  var d=S.visu.noeuds[i]; if(!d) return;
  var f=el('vzFull');
  if(!f){
    f=document.createElement('div'); f.id='vzFull';
    f.innerHTML='<div class="vf-in"><div class="vf-top"><div style="flex:1">'+
      '<div class="vf-kind" id="vfKind"></div><h2 id="vfTitre"></h2></div>'+
      '<button class="vz-back" id="vfX">✕ Revenir à la carte</button></div>'+
      '<div id="vfBody"></div></div>';
    document.body.appendChild(f);
    f.addEventListener('click', function(e){
      if(e.target.id==='vfX'){ fermerPlein(); return; }
      var b;
      if((b=e.target.closest('[data-ch]'))){ allerCours(b.getAttribute('data-ch')); return; }
      if((b=e.target.closest('[data-fc]'))){ allerFiches(b.getAttribute('data-fc')); return; }
      if((b=e.target.closest('[data-at]'))){ allerAtlas(b.getAttribute('data-at')); return; }
      if((b=e.target.closest('[data-su]'))){ allerSujets(b.getAttribute('data-su')); return; }
      if((b=e.target.closest('[data-aut]'))){ allerAuteur(b.getAttribute('data-aut')); return; }
      if((b=e.target.closest('[data-dos]'))){ allerDossier(b.getAttribute('data-dos')); return; }
    });
  }
  el('vfKind').textContent=(LIBROLE[d.role]||d.role)+' · '+S.visu.titre;
  el('vfTitre').textContent=d.t;
  el('vfBody').innerHTML=blocs(d);
  f.classList.add('on'); f.scrollTop=0;
  document.body.style.overflow='hidden';
}
function fermerPlein(){
  var f=el('vzFull'); if(f) f.classList.remove('on');
  document.body.style.overflow='';
}

/* ======================================================= branchements */
function brancherIndex(){
  var g=el('vzGrid');
  if(g && !g.__b){ g.__b=1;
    g.addEventListener('click', function(e){
      var c=e.target.closest('.vz-card'); if(c) ouvrirVisu(parseInt(c.getAttribute('data-v'),10));
    });
  }
  var ch=el('vzChips');
  if(ch && !ch.__b){ ch.__b=1;
    ch.addEventListener('click', function(e){
      var b=e.target.closest('.vz-chip'); if(!b) return;
      S.type=b.getAttribute('data-t')||''; rendreIndex();
    });
  }
  var q=el('vzQ');
  if(q && !q.__b){ q.__b=1;
    q.addEventListener('input', function(){ S.filtre=q.value||''; rendreIndex(); });
  }
}

document.addEventListener('keydown', function(e){
  if(e.key==='Escape'){
    if(el('vzFull') && el('vzFull').classList.contains('on')){ fermerPlein(); return; }
    if(el('vzPanel') && el('vzPanel').classList.contains('on')){ fermerPanneau(); return; }
    var pgv=document.getElementById('pg-visualisations');
    if(pgv && pgv.classList.contains('plein')){ quitterPlein(); return; }
    if(S.visu){ retourIndex(); return; }
  }
  if(!S.visu) return;
  var p=el('vzPanel');
  if(p && p.classList.contains('on')) return;
  var vue=el('vzView'); if(!vue) return;
  var r=vue.getBoundingClientRect();
  if(e.key==='+'||e.key==='='){ zoomVers(1.18, r.width/2, r.height/2); }
  if(e.key==='-'||e.key==='_'){ zoomVers(1/1.18, r.width/2, r.height/2); }
  if(e.key==='0'){ ajuster(true); }
});

function boot(){
  if(!el('vzGrid')) return;
  rendreIndex(); brancherIndex();
}
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', boot);
else boot();

var anc=window.showPg;
if(typeof anc==='function'){
  window.showPg=function(pg){
    var r=anc.apply(this, arguments);
    if(pg==='visualisations'){ setTimeout(boot,0); }
    else { fermerPanneau(); fermerPlein(); }
    return r;
  };
}
window.VZ_OUVRIR=function(cle){
  var i=VZ.map(function(v){return v.cle;}).indexOf(cle);
  if(i<0) return false;
  try{ showPg('visualisations'); }catch(e){}
  setTimeout(function(){ ouvrirVisu(i); }, 60);
  return true;
};
})();
</script>
"""


def main(src, dst, payload='visu_payload.json'):
    t = open(src, encoding='utf-8').read()
    data = json.load(open(payload, encoding='utf-8'))

    # 1. retirer l'ancien CSS
    a = t.find('<style id="v167-visualisations-strategiques-css">')
    b = t.find('</style>', a)
    assert a > 0 and b > a, 'bloc CSS introuvable'
    t = t[:a] + CSS.strip() + t[b + 8:]

    # 2. retirer l'ancien moteur et ses 19 images base64
    a = t.find('<script id="v167-visualisations-strategiques-engine">')
    b = t.find('</script>', a)
    assert a > 0 and b > a, 'bloc moteur introuvable'
    poids = b + 9 - a
    js = JS.replace('__PAYLOAD__', json.dumps(data, ensure_ascii=False,
                                              separators=(',', ':')))
    t = t[:a] + js.strip() + t[b + 9:]

    # 3. remplacer la page
    a = t.find('<div class="pg" id="pg-visualisations">')
    b = t.find('<div class="pg" id="pg-method">', a)
    assert a > 0 and b > a, 'page introuvable'
    t = t[:a] + HTML.strip() + '\n\n' + t[b:]

    assert 'data:image/webp;base64' not in t[:a] or True
    open(dst, 'w', encoding='utf-8').write(t)
    print('ancien moteur retiré      : %.2f Mo' % (poids / 1048576))
    print('nouveau moteur + contenus : %.2f Mo' % (len(js) / 1048576))
    print('OK %s -> %s (%.2f Mo)' % (src, dst, len(t) / 1048576))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
